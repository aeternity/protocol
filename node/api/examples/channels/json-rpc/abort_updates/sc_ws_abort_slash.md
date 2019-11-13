
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
      "fsm_id": "ba_HV7Ywzl4TeEc0NPexfi5VDmVverGs4RLD4n9TH/MAQo5qH8Y"
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
      "fsm_id": "ba_ADfN6AJZS4yyXKiCuK/mgqvbph8GBq369g+KosEXVLoCWEex"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnY+W79q7g==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422856,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBvDl8w2CBHsSDkLgwW9KGlF7CUcjIDlCf3LlN5KLlAUBgctSNsFtqZk6KQLY7PxhNY+FdHtWBC7JODeJoEXnUOuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2Plx05RM="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422856,
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
      "signed_tx": "tx_+MsLAfhCuEBvDl8w2CBHsSDkLgwW9KGlF7CUcjIDlCf3LlN5KLlAUBgctSNsFtqZk6KQLY7PxhNY+FdHtWBC7JODeJoEXnUOuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2Plx05RM=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422855,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAHb9KKVnZYBYjK+tM6p9iinTe2CZv51vHhFwszkUC3UPbNNhbcrWfRAa/OTsZNs6Qd+DEU3oYUePS9F5oXo0dDrhAbw5fMNggR7Eg5C4MFvShpRewlHIyA5Qn9y5TeSi5QFAYHLUjbBbamZOikC2Oz8YTWPhXR7VgQuyTg3iaBF51DriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdj5vYFRl"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422855,
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAHb9KKVnZYBYjK+tM6p9iinTe2CZv51vHhFwszkUC3UPbNNhbcrWfRAa/OTsZNs6Qd+DEU3oYUePS9F5oXo0dDrhAbw5fMNggR7Eg5C4MFvShpRewlHIyA5Qn9y5TeSi5QFAYHLUjbBbamZOikC2Oz8YTWPhXR7VgQuyTg3iaBF51DriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdj5vYFRl",
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAHb9KKVnZYBYjK+tM6p9iinTe2CZv51vHhFwszkUC3UPbNNhbcrWfRAa/OTsZNs6Qd+DEU3oYUePS9F5oXo0dDrhAbw5fMNggR7Eg5C4MFvShpRewlHIyA5Qn9y5TeSi5QFAYHLUjbBbamZOikC2Oz8YTWPhXR7VgQuyTg3iaBF51DriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdj5vYFRl",
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAHb9KKVnZYBYjK+tM6p9iinTe2CZv51vHhFwszkUC3UPbNNhbcrWfRAa/OTsZNs6Qd+DEU3oYUePS9F5oXo0dDrhAbw5fMNggR7Eg5C4MFvShpRewlHIyA5Qn9y5TeSi5QFAYHLUjbBbamZOikC2Oz8YTWPhXR7VgQuyTg3iaBF51DriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdj5vYFRl",
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAHb9KKVnZYBYjK+tM6p9iinTe2CZv51vHhFwszkUC3UPbNNhbcrWfRAa/OTsZNs6Qd+DEU3oYUePS9F5oXo0dDrhAbw5fMNggR7Eg5C4MFvShpRewlHIyA5Qn9y5TeSi5QFAYHLUjbBbamZOikC2Oz8YTWPhXR7VgQuyTg3iaBF51DriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdj5vYFRl",
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "message": {
        "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "message": {
        "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
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
  "id": -576460752303422854,
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
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422854,
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "event": "funding_locked"
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "event": "open"
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Channel is `open` and ready to use

#### responder info
> Channel is `open` and ready to use

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "state": "tx_+QENCwH4hLhAHb9KKVnZYBYjK+tM6p9iinTe2CZv51vHhFwszkUC3UPbNNhbcrWfRAa/OTsZNs6Qd+DEU3oYUePS9F5oXo0dDrhAbw5fMNggR7Eg5C4MFvShpRewlHIyA5Qn9y5TeSi5QFAYHLUjbBbamZOikC2Oz8YTWPhXR7VgQuyTg3iaBF51DriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdj5vYFRl"
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "state": "tx_+QENCwH4hLhAHb9KKVnZYBYjK+tM6p9iinTe2CZv51vHhFwszkUC3UPbNNhbcrWfRAa/OTsZNs6Qd+DEU3oYUePS9F5oXo0dDrhAbw5fMNggR7Eg5C4MFvShpRewlHIyA5Qn9y5TeSi5QFAYHLUjbBbamZOikC2Oz8YTWPhXR7VgQuyTg3iaBF51DriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdj5vYFRl"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422853,
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
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422853,
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBszCxzMpQ1eSZfJa83BqH6XiERtkOT6w/WmNc7DE23GaAqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrtyS2fS4=",
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
  "id": -576460752303422852,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC925M5Ycoq7YQ5VpoH0vpk5xfZUEaPAFPP2nxcHydTyfJrppBMUOf5kp4WjonpOxqm4Qy3/HCi7oM+TVzXcSEPuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7e8LLTt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422852,
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC925M5Ycoq7YQ5VpoH0vpk5xfZUEaPAFPP2nxcHydTyfJrppBMUOf5kp4WjonpOxqm4Qy3/HCi7oM+TVzXcSEPuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7e8LLTt",
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
  "id": -576460752303422851,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEC925M5Ycoq7YQ5VpoH0vpk5xfZUEaPAFPP2nxcHydTyfJrppBMUOf5kp4WjonpOxqm4Qy3/HCi7oM+TVzXcSEPuEDCfZj7WZOiEK6+KaVYuksXhMfS0m9UP8+jlooRPD9lsUJaozL/olstFjm5c7HMB4YxseRlnA44+PCZPj8mOHoHuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7ckU7W/"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422851,
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "state": "tx_+NILAfiEuEC925M5Ycoq7YQ5VpoH0vpk5xfZUEaPAFPP2nxcHydTyfJrppBMUOf5kp4WjonpOxqm4Qy3/HCi7oM+TVzXcSEPuEDCfZj7WZOiEK6+KaVYuksXhMfS0m9UP8+jlooRPD9lsUJaozL/olstFjm5c7HMB4YxseRlnA44+PCZPj8mOHoHuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7ckU7W/"
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "state": "tx_+NILAfiEuEC925M5Ycoq7YQ5VpoH0vpk5xfZUEaPAFPP2nxcHydTyfJrppBMUOf5kp4WjonpOxqm4Qy3/HCi7oM+TVzXcSEPuEDCfZj7WZOiEK6+KaVYuksXhMfS0m9UP8+jlooRPD9lsUJaozL/olstFjm5c7HMB4YxseRlnA44+PCZPj8mOHoHuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7ckU7W/"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422850,
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
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422850,
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
  "id": -576460752303422849,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422849,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEC925M5Ycoq7YQ5VpoH0vpk5xfZUEaPAFPP2nxcHydTyfJrppBMUOf5kp4WjonpOxqm4Qy3/HCi7oM+TVzXcSEPuEDCfZj7WZOiEK6+KaVYuksXhMfS0m9UP8+jlooRPD9lsUJaozL/olstFjm5c7HMB4YxseRlnA44+PCZPj8mOHoHuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7ckU7W/",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422848,
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
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422848,
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBszCxzMpQ1eSZfJa83BqH6XiERtkOT6w/WmNc7DE23GaA6BoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdn97WHo=",
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
  "id": -576460752303422847,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECeWIYhL6d2P+gyaOZGt1TjnrUZD2Q8vpAH78ib2VSdFZLmmPwPidAdamNmXT7tMd1GYpc3qil8BOuf1O5YQVEPuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbZ5tVU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422847,
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "signed_tx": "tx_+JALAfhCuECeWIYhL6d2P+gyaOZGt1TjnrUZD2Q8vpAH78ib2VSdFZLmmPwPidAdamNmXT7tMd1GYpc3qil8BOuf1O5YQVEPuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbZ5tVU",
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
  "id": -576460752303422846,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECdAkAg/XGo+4O8GfDNXFZMUubi0OZXsjx0/NKxlSSXHKjAGsu+eYLJHshYZKs1pyBcgzJfjLsp4K4BYRVbQS8FuECeWIYhL6d2P+gyaOZGt1TjnrUZD2Q8vpAH78ib2VSdFZLmmPwPidAdamNmXT7tMd1GYpc3qil8BOuf1O5YQVEPuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZJ0WiR"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422846,
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "state": "tx_+NILAfiEuECdAkAg/XGo+4O8GfDNXFZMUubi0OZXsjx0/NKxlSSXHKjAGsu+eYLJHshYZKs1pyBcgzJfjLsp4K4BYRVbQS8FuECeWIYhL6d2P+gyaOZGt1TjnrUZD2Q8vpAH78ib2VSdFZLmmPwPidAdamNmXT7tMd1GYpc3qil8BOuf1O5YQVEPuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZJ0WiR"
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "state": "tx_+NILAfiEuECdAkAg/XGo+4O8GfDNXFZMUubi0OZXsjx0/NKxlSSXHKjAGsu+eYLJHshYZKs1pyBcgzJfjLsp4K4BYRVbQS8FuECeWIYhL6d2P+gyaOZGt1TjnrUZD2Q8vpAH78ib2VSdFZLmmPwPidAdamNmXT7tMd1GYpc3qil8BOuf1O5YQVEPuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZJ0WiR"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422845,
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
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422845,
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
  "id": -576460752303422844,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422844,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECdAkAg/XGo+4O8GfDNXFZMUubi0OZXsjx0/NKxlSSXHKjAGsu+eYLJHshYZKs1pyBcgzJfjLsp4K4BYRVbQS8FuECeWIYhL6d2P+gyaOZGt1TjnrUZD2Q8vpAH78ib2VSdFZLmmPwPidAdamNmXT7tMd1GYpc3qil8BOuf1O5YQVEPuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZJ0WiR",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422843,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422843,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECdAkAg/XGo+4O8GfDNXFZMUubi0OZXsjx0/NKxlSSXHKjAGsu+eYLJHshYZKs1pyBcgzJfjLsp4K4BYRVbQS8FuECeWIYhL6d2P+gyaOZGt1TjnrUZD2Q8vpAH78ib2VSdFZLmmPwPidAdamNmXT7tMd1GYpc3qil8BOuf1O5YQVEPuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZJ0WiR",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422842,
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
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422842,
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBszCxzMpQ1eSZfJa83BqH6XiERtkOT6w/WmNc7DE23GaBKBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt/3sgBc=",
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
  "id": -576460752303422841,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDBVWr1RSYAv5tYLkXLecvUr+37vQ4yvjsZ+NJZTjUeluHP4him9Nm9QUj+qPCglyzv+rk0HrRex9w9ifO2Zy8MuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dVgJVa"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422841,
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDBVWr1RSYAv5tYLkXLecvUr+37vQ4yvjsZ+NJZTjUeluHP4him9Nm9QUj+qPCglyzv+rk0HrRex9w9ifO2Zy8MuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dVgJVa",
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
  "id": -576460752303422840,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECwbq2OaBRHWvDplua0ftj3L7ii540D/upu4O8aipnxSCiwSNi6GBDmWODmp07BV/KsoAPZXJzrYUx9VjNuKkMAuEDBVWr1RSYAv5tYLkXLecvUr+37vQ4yvjsZ+NJZTjUeluHP4him9Nm9QUj+qPCglyzv+rk0HrRex9w9ifO2Zy8MuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fju9Td"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422840,
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "state": "tx_+NILAfiEuECwbq2OaBRHWvDplua0ftj3L7ii540D/upu4O8aipnxSCiwSNi6GBDmWODmp07BV/KsoAPZXJzrYUx9VjNuKkMAuEDBVWr1RSYAv5tYLkXLecvUr+37vQ4yvjsZ+NJZTjUeluHP4him9Nm9QUj+qPCglyzv+rk0HrRex9w9ifO2Zy8MuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fju9Td"
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "state": "tx_+NILAfiEuECwbq2OaBRHWvDplua0ftj3L7ii540D/upu4O8aipnxSCiwSNi6GBDmWODmp07BV/KsoAPZXJzrYUx9VjNuKkMAuEDBVWr1RSYAv5tYLkXLecvUr+37vQ4yvjsZ+NJZTjUeluHP4him9Nm9QUj+qPCglyzv+rk0HrRex9w9ifO2Zy8MuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fju9Td"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422839,
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
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422839,
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
  "id": -576460752303422838,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422838,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECwbq2OaBRHWvDplua0ftj3L7ii540D/upu4O8aipnxSCiwSNi6GBDmWODmp07BV/KsoAPZXJzrYUx9VjNuKkMAuEDBVWr1RSYAv5tYLkXLecvUr+37vQ4yvjsZ+NJZTjUeluHP4him9Nm9QUj+qPCglyzv+rk0HrRex9w9ifO2Zy8MuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fju9Td",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422837,
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
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422837,
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBszCxzMpQ1eSZfJa83BqH6XiERtkOT6w/WmNc7DE23GaBaBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhTktxk=",
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
  "id": -576460752303422836,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECxRASS6YIHSU8L6lhK7ujd5Icu4ZVMzOCi6oVhGBzxTSbknJb4pP1HyR+yMJh/Jt5Le8nfMAWkNF5Wywpi4MMPuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbMqpna"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422836,
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "signed_tx": "tx_+JALAfhCuECxRASS6YIHSU8L6lhK7ujd5Icu4ZVMzOCi6oVhGBzxTSbknJb4pP1HyR+yMJh/Jt5Le8nfMAWkNF5Wywpi4MMPuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbMqpna",
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
  "id": -576460752303422835,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECHohnf3r6UUu4m+rDC1m/zwxsbszbXiurAz4k7h0NRMeAVjbtuyXRj1dr/CwqbLzUEat+oF1JNx22XAbyyAhQCuECxRASS6YIHSU8L6lhK7ujd5Icu4ZVMzOCi6oVhGBzxTSbknJb4pP1HyR+yMJh/Jt5Le8nfMAWkNF5Wywpi4MMPuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbSvUuz"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422835,
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "state": "tx_+NILAfiEuECHohnf3r6UUu4m+rDC1m/zwxsbszbXiurAz4k7h0NRMeAVjbtuyXRj1dr/CwqbLzUEat+oF1JNx22XAbyyAhQCuECxRASS6YIHSU8L6lhK7ujd5Icu4ZVMzOCi6oVhGBzxTSbknJb4pP1HyR+yMJh/Jt5Le8nfMAWkNF5Wywpi4MMPuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbSvUuz"
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "state": "tx_+NILAfiEuECHohnf3r6UUu4m+rDC1m/zwxsbszbXiurAz4k7h0NRMeAVjbtuyXRj1dr/CwqbLzUEat+oF1JNx22XAbyyAhQCuECxRASS6YIHSU8L6lhK7ujd5Icu4ZVMzOCi6oVhGBzxTSbknJb4pP1HyR+yMJh/Jt5Le8nfMAWkNF5Wywpi4MMPuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbSvUuz"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422834,
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
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422834,
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
  "id": -576460752303422833,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422833,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECHohnf3r6UUu4m+rDC1m/zwxsbszbXiurAz4k7h0NRMeAVjbtuyXRj1dr/CwqbLzUEat+oF1JNx22XAbyyAhQCuECxRASS6YIHSU8L6lhK7ujd5Icu4ZVMzOCi6oVhGBzxTSbknJb4pP1HyR+yMJh/Jt5Le8nfMAWkNF5Wywpi4MMPuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbSvUuz",
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECHohnf3r6UUu4m+rDC1m/zwxsbszbXiurAz4k7h0NRMeAVjbtuyXRj1dr/CwqbLzUEat+oF1JNx22XAbyyAhQCuECxRASS6YIHSU8L6lhK7ujd5Icu4ZVMzOCi6oVhGBzxTSbknJb4pP1HyR+yMJh/Jt5Le8nfMAWkNF5Wywpi4MMPuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbSvUuz",
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECHohnf3r6UUu4m+rDC1m/zwxsbszbXiurAz4k7h0NRMeAVjbtuyXRj1dr/CwqbLzUEat+oF1JNx22XAbyyAhQCuECxRASS6YIHSU8L6lhK7ujd5Icu4ZVMzOCi6oVhGBzxTSbknJb4pP1HyR+yMJh/Jt5Le8nfMAWkNF5Wywpi4MMPuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbSvUuz",
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
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
  "method": "channels.slash",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBszCxzMpQ1eSZfJa83BqH6XiERtkOT6w/WmNc7DE23GaoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FbjU+NILAfiEuECHohnf3r6UUu4m+rDC1m/zwxsbszbXiurAz4k7h0NRMeAVjbtuyXRj1dr/CwqbLzUEat+oF1JNx22XAbyyAhQCuECxRASS6YIHSU8L6lhK7ujd5Icu4ZVMzOCi6oVhGBzxTSbknJb4pP1HyR+yMJh/Jt5Le8nfMAWkNF5Wywpi4MMPuEj4RjkCoQbMwsczKUNXkmXyWvNwah+l4hEbZDk+sP1pjXOwxNtxmgWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wna5AUz5AUk8AfkBP/kBPKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvkBGPh0oCiW0e4qVvD/C94E6/En+1vvEgzoctloLayg1hD1Tl5u+FGAgICAgICg46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVuAgICAoKcJtie4oQxB6+5JVy+F3eNaNF7V7TgRPXFlQNJ4W/wIgICAgID4T6CnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CO2gP/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWLygoBAIY/qiUiX//4T6DjooHlLkRUA0QFUOns+/GhHcvejx4IPZN7Jd7GGFRtW+2gNllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAHAwMDAwACGGR7ISegAQD+S4tE=",
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
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
  "id": -576460752303422832,
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
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
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422832,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422831,
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
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
    "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
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
  "channel_id": "ch_2ZBLncxjsBJuh1AavsGVtavRmLJoKY7oGATejhy9iBCU6xsdss",
  "id": -576460752303422831,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
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
      "fsm_id": "ba_OlJcHxmDt4PfyIoCAjI5c69x+9RpB4WSD6aOSQ4zG1r14uix"
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
      "fsm_id": "ba_P+ulE0i2u2WwqySwCZ2BcIAhSVxtSa8fzfj78E6wf/pMVZ4z"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZAh+gNEg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422830,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEB474/FFMf/o1Z2hDUdGw9Bykb1Esqnr+XGFt1gwJq41tp9kAV4TByDPm8HAj/tDkenl+vxjhT6d3HZuDYHTIAGuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2QPe1P70="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422830,
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
      "signed_tx": "tx_+MsLAfhCuEB474/FFMf/o1Z2hDUdGw9Bykb1Esqnr+XGFt1gwJq41tp9kAV4TByDPm8HAj/tDkenl+vxjhT6d3HZuDYHTIAGuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2QPe1P70=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422829,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhANzcGYo9RJI2UtzGjTzofXT8O93fHrK9FVQznlKO2D+b11Cq+1ILQDEMWqIivrfjsZghzuVGL4tuUq8su/+D+AbhAeO+PxRTH/6NWdoQ1HRsPQcpG9RLKp6/lxhbdYMCauNbafZAFeEwcgz5vBwI/7Q5Hp5fr8Y4U+ndx2bg2B0yABriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkAjRkZI"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422829,
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhANzcGYo9RJI2UtzGjTzofXT8O93fHrK9FVQznlKO2D+b11Cq+1ILQDEMWqIivrfjsZghzuVGL4tuUq8su/+D+AbhAeO+PxRTH/6NWdoQ1HRsPQcpG9RLKp6/lxhbdYMCauNbafZAFeEwcgz5vBwI/7Q5Hp5fr8Y4U+ndx2bg2B0yABriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkAjRkZI",
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhANzcGYo9RJI2UtzGjTzofXT8O93fHrK9FVQznlKO2D+b11Cq+1ILQDEMWqIivrfjsZghzuVGL4tuUq8su/+D+AbhAeO+PxRTH/6NWdoQ1HRsPQcpG9RLKp6/lxhbdYMCauNbafZAFeEwcgz5vBwI/7Q5Hp5fr8Y4U+ndx2bg2B0yABriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkAjRkZI",
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhANzcGYo9RJI2UtzGjTzofXT8O93fHrK9FVQznlKO2D+b11Cq+1ILQDEMWqIivrfjsZghzuVGL4tuUq8su/+D+AbhAeO+PxRTH/6NWdoQ1HRsPQcpG9RLKp6/lxhbdYMCauNbafZAFeEwcgz5vBwI/7Q5Hp5fr8Y4U+ndx2bg2B0yABriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkAjRkZI",
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhANzcGYo9RJI2UtzGjTzofXT8O93fHrK9FVQznlKO2D+b11Cq+1ILQDEMWqIivrfjsZghzuVGL4tuUq8su/+D+AbhAeO+PxRTH/6NWdoQ1HRsPQcpG9RLKp6/lxhbdYMCauNbafZAFeEwcgz5vBwI/7Q5Hp5fr8Y4U+ndx2bg2B0yABriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkAjRkZI",
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "message": {
        "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "message": {
        "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
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
  "id": -576460752303422828,
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
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422828,
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "event": "funding_locked"
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "event": "open"
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder info
> Channel is `open` and ready to use

#### initiator info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "state": "tx_+QENCwH4hLhANzcGYo9RJI2UtzGjTzofXT8O93fHrK9FVQznlKO2D+b11Cq+1ILQDEMWqIivrfjsZghzuVGL4tuUq8su/+D+AbhAeO+PxRTH/6NWdoQ1HRsPQcpG9RLKp6/lxhbdYMCauNbafZAFeEwcgz5vBwI/7Q5Hp5fr8Y4U+ndx2bg2B0yABriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkAjRkZI"
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "state": "tx_+QENCwH4hLhANzcGYo9RJI2UtzGjTzofXT8O93fHrK9FVQznlKO2D+b11Cq+1ILQDEMWqIivrfjsZghzuVGL4tuUq8su/+D+AbhAeO+PxRTH/6NWdoQ1HRsPQcpG9RLKp6/lxhbdYMCauNbafZAFeEwcgz5vBwI/7Q5Hp5fr8Y4U+ndx2bg2B0yABriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkAjRkZI"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422827,
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
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422827,
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBm8/ajuUXDNED+r/e/wuRRzvR+6J/e1NP2hKHnzyHy+sAqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt9VWiFk=",
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
  "id": -576460752303422826,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECWRC6mrbiqABmnuqr/nYT3hJXCendgzHTRpAJs5hqX8R3msuk7AKsvz/oGqgO6itfONk3YOik9DrHkGKwVjLIGuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrAKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7frVE+f"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422826,
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "signed_tx": "tx_+JALAfhCuECWRC6mrbiqABmnuqr/nYT3hJXCendgzHTRpAJs5hqX8R3msuk7AKsvz/oGqgO6itfONk3YOik9DrHkGKwVjLIGuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrAKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7frVE+f",
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
  "id": -576460752303422825,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBCWI/LSYSGyi7/wxXy6k6z4bCdiw0LngidQvnDo1ij1fI88lb/vMaiwyr2raetGfZ/ZGYxFB9yMeFkmuiF0KcPuECWRC6mrbiqABmnuqr/nYT3hJXCendgzHTRpAJs5hqX8R3msuk7AKsvz/oGqgO6itfONk3YOik9DrHkGKwVjLIGuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrAKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eNzYvg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422825,
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "state": "tx_+NILAfiEuEBCWI/LSYSGyi7/wxXy6k6z4bCdiw0LngidQvnDo1ij1fI88lb/vMaiwyr2raetGfZ/ZGYxFB9yMeFkmuiF0KcPuECWRC6mrbiqABmnuqr/nYT3hJXCendgzHTRpAJs5hqX8R3msuk7AKsvz/oGqgO6itfONk3YOik9DrHkGKwVjLIGuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrAKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eNzYvg"
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "state": "tx_+NILAfiEuEBCWI/LSYSGyi7/wxXy6k6z4bCdiw0LngidQvnDo1ij1fI88lb/vMaiwyr2raetGfZ/ZGYxFB9yMeFkmuiF0KcPuECWRC6mrbiqABmnuqr/nYT3hJXCendgzHTRpAJs5hqX8R3msuk7AKsvz/oGqgO6itfONk3YOik9DrHkGKwVjLIGuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrAKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eNzYvg"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422824,
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
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422824,
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
  "id": -576460752303422823,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422823,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBCWI/LSYSGyi7/wxXy6k6z4bCdiw0LngidQvnDo1ij1fI88lb/vMaiwyr2raetGfZ/ZGYxFB9yMeFkmuiF0KcPuECWRC6mrbiqABmnuqr/nYT3hJXCendgzHTRpAJs5hqX8R3msuk7AKsvz/oGqgO6itfONk3YOik9DrHkGKwVjLIGuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrAKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eNzYvg",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422822,
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
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422822,
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBm8/ajuUXDNED+r/e/wuRRzvR+6J/e1NP2hKHnzyHy+sA6BoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhKta6Q=",
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
  "id": -576460752303422821,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECImL83BdLdh1pJvMr4Oi7w+m0qiW/jZO4jUXAkpTU6KwLC+JNBktaxvf0j1MJ5Qb2t2HkttVccgks3yLh89eIDuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrAOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaals7R"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422821,
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "signed_tx": "tx_+JALAfhCuECImL83BdLdh1pJvMr4Oi7w+m0qiW/jZO4jUXAkpTU6KwLC+JNBktaxvf0j1MJ5Qb2t2HkttVccgks3yLh89eIDuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrAOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaals7R",
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
  "id": -576460752303422820,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBoJNlt+Z9kTdqp9RtyFVjHSuOqmGgiskHxisVK4wpEPOPXdR6gbZkFakSLWmohsikRrkZBFepd+9vlt4ptalgBuECImL83BdLdh1pJvMr4Oi7w+m0qiW/jZO4jUXAkpTU6KwLC+JNBktaxvf0j1MJ5Qb2t2HkttVccgks3yLh89eIDuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrAOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZMV7yC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422820,
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "state": "tx_+NILAfiEuEBoJNlt+Z9kTdqp9RtyFVjHSuOqmGgiskHxisVK4wpEPOPXdR6gbZkFakSLWmohsikRrkZBFepd+9vlt4ptalgBuECImL83BdLdh1pJvMr4Oi7w+m0qiW/jZO4jUXAkpTU6KwLC+JNBktaxvf0j1MJ5Qb2t2HkttVccgks3yLh89eIDuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrAOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZMV7yC"
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "state": "tx_+NILAfiEuEBoJNlt+Z9kTdqp9RtyFVjHSuOqmGgiskHxisVK4wpEPOPXdR6gbZkFakSLWmohsikRrkZBFepd+9vlt4ptalgBuECImL83BdLdh1pJvMr4Oi7w+m0qiW/jZO4jUXAkpTU6KwLC+JNBktaxvf0j1MJ5Qb2t2HkttVccgks3yLh89eIDuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrAOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZMV7yC"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422819,
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
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422819,
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
  "id": -576460752303422818,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422818,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBoJNlt+Z9kTdqp9RtyFVjHSuOqmGgiskHxisVK4wpEPOPXdR6gbZkFakSLWmohsikRrkZBFepd+9vlt4ptalgBuECImL83BdLdh1pJvMr4Oi7w+m0qiW/jZO4jUXAkpTU6KwLC+JNBktaxvf0j1MJ5Qb2t2HkttVccgks3yLh89eIDuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrAOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZMV7yC",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422817,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422817,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBoJNlt+Z9kTdqp9RtyFVjHSuOqmGgiskHxisVK4wpEPOPXdR6gbZkFakSLWmohsikRrkZBFepd+9vlt4ptalgBuECImL83BdLdh1pJvMr4Oi7w+m0qiW/jZO4jUXAkpTU6KwLC+JNBktaxvf0j1MJ5Qb2t2HkttVccgks3yLh89eIDuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrAOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZMV7yC",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422816,
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
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422816,
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBm8/ajuUXDNED+r/e/wuRRzvR+6J/e1NP2hKHnzyHy+sBKBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrtw7vghg=",
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
  "id": -576460752303422815,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBpjNhohCCSN6fTqpdQQnLGS6J0Sc3Ihhik7sEdO8yj4X6nneW2re5H5R3Nksad/+dCJyqGVKsp4pTIowQmoPsFuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrASgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cWswK2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422815,
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBpjNhohCCSN6fTqpdQQnLGS6J0Sc3Ihhik7sEdO8yj4X6nneW2re5H5R3Nksad/+dCJyqGVKsp4pTIowQmoPsFuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrASgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cWswK2",
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
  "id": -576460752303422814,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEApPe/Ls5Ccie4QFsk6t6QCIBBK1/AJmDC7QKzJ3idKmbp5SPEjPxziduy/kRAWSa421urKe7xqK6GufSej0x8FuEBpjNhohCCSN6fTqpdQQnLGS6J0Sc3Ihhik7sEdO8yj4X6nneW2re5H5R3Nksad/+dCJyqGVKsp4pTIowQmoPsFuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrASgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eNBcxg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422814,
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "state": "tx_+NILAfiEuEApPe/Ls5Ccie4QFsk6t6QCIBBK1/AJmDC7QKzJ3idKmbp5SPEjPxziduy/kRAWSa421urKe7xqK6GufSej0x8FuEBpjNhohCCSN6fTqpdQQnLGS6J0Sc3Ihhik7sEdO8yj4X6nneW2re5H5R3Nksad/+dCJyqGVKsp4pTIowQmoPsFuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrASgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eNBcxg"
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "state": "tx_+NILAfiEuEApPe/Ls5Ccie4QFsk6t6QCIBBK1/AJmDC7QKzJ3idKmbp5SPEjPxziduy/kRAWSa421urKe7xqK6GufSej0x8FuEBpjNhohCCSN6fTqpdQQnLGS6J0Sc3Ihhik7sEdO8yj4X6nneW2re5H5R3Nksad/+dCJyqGVKsp4pTIowQmoPsFuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrASgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eNBcxg"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422813,
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
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422813,
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
  "id": -576460752303422812,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422812,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEApPe/Ls5Ccie4QFsk6t6QCIBBK1/AJmDC7QKzJ3idKmbp5SPEjPxziduy/kRAWSa421urKe7xqK6GufSej0x8FuEBpjNhohCCSN6fTqpdQQnLGS6J0Sc3Ihhik7sEdO8yj4X6nneW2re5H5R3Nksad/+dCJyqGVKsp4pTIowQmoPsFuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrASgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eNBcxg",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422811,
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
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422811,
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBm8/ajuUXDNED+r/e/wuRRzvR+6J/e1NP2hKHnzyHy+sBaBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdlDYBI0=",
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
  "id": -576460752303422810,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBjiIR2unG2ZXKa4wWmM9b7QaY/Rjds0wnIofUbDvSvQvcp7Fl4zHQDZL5jIyvuzRwmVGeIbCPgKLkarqOKra8HuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrAWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbUpfYt"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422810,
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBjiIR2unG2ZXKa4wWmM9b7QaY/Rjds0wnIofUbDvSvQvcp7Fl4zHQDZL5jIyvuzRwmVGeIbCPgKLkarqOKra8HuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrAWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbUpfYt",
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
  "id": -576460752303422809,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBjiIR2unG2ZXKa4wWmM9b7QaY/Rjds0wnIofUbDvSvQvcp7Fl4zHQDZL5jIyvuzRwmVGeIbCPgKLkarqOKra8HuEBl/jTFZQEl/Dfr34GUeshRkGq7i1fwFAyCiuw8LsOdTFxbaI944hOae8aQ5fXJBOOIcoyey/+XQUvAQMYI1W8AuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrAWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbprhf1"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422809,
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "state": "tx_+NILAfiEuEBjiIR2unG2ZXKa4wWmM9b7QaY/Rjds0wnIofUbDvSvQvcp7Fl4zHQDZL5jIyvuzRwmVGeIbCPgKLkarqOKra8HuEBl/jTFZQEl/Dfr34GUeshRkGq7i1fwFAyCiuw8LsOdTFxbaI944hOae8aQ5fXJBOOIcoyey/+XQUvAQMYI1W8AuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrAWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbprhf1"
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "state": "tx_+NILAfiEuEBjiIR2unG2ZXKa4wWmM9b7QaY/Rjds0wnIofUbDvSvQvcp7Fl4zHQDZL5jIyvuzRwmVGeIbCPgKLkarqOKra8HuEBl/jTFZQEl/Dfr34GUeshRkGq7i1fwFAyCiuw8LsOdTFxbaI944hOae8aQ5fXJBOOIcoyey/+XQUvAQMYI1W8AuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrAWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbprhf1"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422808,
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
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422808,
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
  "id": -576460752303422807,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422807,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBjiIR2unG2ZXKa4wWmM9b7QaY/Rjds0wnIofUbDvSvQvcp7Fl4zHQDZL5jIyvuzRwmVGeIbCPgKLkarqOKra8HuEBl/jTFZQEl/Dfr34GUeshRkGq7i1fwFAyCiuw8LsOdTFxbaI944hOae8aQ5fXJBOOIcoyey/+XQUvAQMYI1W8AuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrAWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbprhf1",
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBjiIR2unG2ZXKa4wWmM9b7QaY/Rjds0wnIofUbDvSvQvcp7Fl4zHQDZL5jIyvuzRwmVGeIbCPgKLkarqOKra8HuEBl/jTFZQEl/Dfr34GUeshRkGq7i1fwFAyCiuw8LsOdTFxbaI944hOae8aQ5fXJBOOIcoyey/+XQUvAQMYI1W8AuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrAWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbprhf1",
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBjiIR2unG2ZXKa4wWmM9b7QaY/Rjds0wnIofUbDvSvQvcp7Fl4zHQDZL5jIyvuzRwmVGeIbCPgKLkarqOKra8HuEBl/jTFZQEl/Dfr34GUeshRkGq7i1fwFAyCiuw8LsOdTFxbaI944hOae8aQ5fXJBOOIcoyey/+XQUvAQMYI1W8AuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrAWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbprhf1",
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
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
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBm8/ajuUXDNED+r/e/wuRRzvR+6J/e1NP2hKHnzyHy+soQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv7jU+NILAfiEuEBjiIR2unG2ZXKa4wWmM9b7QaY/Rjds0wnIofUbDvSvQvcp7Fl4zHQDZL5jIyvuzRwmVGeIbCPgKLkarqOKra8HuEBl/jTFZQEl/Dfr34GUeshRkGq7i1fwFAyCiuw8LsOdTFxbaI944hOae8aQ5fXJBOOIcoyey/+XQUvAQMYI1W8AuEj4RjkCoQZvP2o7lFwzRA/q/3v8LkUc70fuif3tTT9oSh588h8vrAWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wna5AUz5AUk8AfkBP/kBPKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvkBGPh0oCiW0e4qVvD/C94E6/En+1vvEgzoctloLayg1hD1Tl5u+FGAgICAgICg46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVuAgICAoKcJtie4oQxB6+5JVy+F3eNaNF7V7TgRPXFlQNJ4W/wIgICAgID4T6CnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CO2gP/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWLygoBAIY/qiUiX//4T6DjooHlLkRUA0QFUOns+/GhHcvejx4IPZN7Jd7GGFRtW+2gNllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAHAwMDAwACGGR7ISegAF42/GGk=",
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "event": "aborted_update"
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder info
> Channel is `open` and ready to use

#### responder ---> node
```javascript
{
  "id": -576460752303422806,
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
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422806,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422805,
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
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
  "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
  "id": -576460752303422805,
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
    "channel_id": "ch_qzg4s9mFBrc61myW9Bfv551XY5kGDxbuqcQ7KQtHGCBmyNHgv",
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
      "fsm_id": "ba_fxcLXzVJ6XhwnAdFaj7Nstzv8Ii/2SM+W/ejn9nlWX5/qCh9"
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
      "fsm_id": "ba_LGpTckYO8UtMgqU8Yrwt3bkt7VPsQdS93fOpkD16wyX1Cb12"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZCjySt2Q==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422804,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDe3dFklHqd90Hh/MkRMio9jWgrZBn+nRQDeUJjtO7PSin8BD1J92wBR1nNjqYnLI29DfraJPMsBvB8GAxR65kAuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2Qim1tVo="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422804,
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
      "signed_tx": "tx_+MsLAfhCuEDe3dFklHqd90Hh/MkRMio9jWgrZBn+nRQDeUJjtO7PSin8BD1J92wBR1nNjqYnLI29DfraJPMsBvB8GAxR65kAuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2Qim1tVo=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422803,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhALQDJVV+C7VDC4ZpMunMcm+xeh+rD6kRxyniF0m6NgGXEYj3gOt5DxtahfbwUiDGtMcqo/jBVUhsnxs1j0dZOAbhA3t3RZJR6nfdB4fzJETIqPY1oK2QZ/p0UA3lCY7Tuz0op/AQ9SfdsAUdZzY6mJyyNvQ362iTzLAbwfBgMUeuZALiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkLf9784"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422803,
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhALQDJVV+C7VDC4ZpMunMcm+xeh+rD6kRxyniF0m6NgGXEYj3gOt5DxtahfbwUiDGtMcqo/jBVUhsnxs1j0dZOAbhA3t3RZJR6nfdB4fzJETIqPY1oK2QZ/p0UA3lCY7Tuz0op/AQ9SfdsAUdZzY6mJyyNvQ362iTzLAbwfBgMUeuZALiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkLf9784",
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhALQDJVV+C7VDC4ZpMunMcm+xeh+rD6kRxyniF0m6NgGXEYj3gOt5DxtahfbwUiDGtMcqo/jBVUhsnxs1j0dZOAbhA3t3RZJR6nfdB4fzJETIqPY1oK2QZ/p0UA3lCY7Tuz0op/AQ9SfdsAUdZzY6mJyyNvQ362iTzLAbwfBgMUeuZALiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkLf9784",
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhALQDJVV+C7VDC4ZpMunMcm+xeh+rD6kRxyniF0m6NgGXEYj3gOt5DxtahfbwUiDGtMcqo/jBVUhsnxs1j0dZOAbhA3t3RZJR6nfdB4fzJETIqPY1oK2QZ/p0UA3lCY7Tuz0op/AQ9SfdsAUdZzY6mJyyNvQ362iTzLAbwfBgMUeuZALiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkLf9784",
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhALQDJVV+C7VDC4ZpMunMcm+xeh+rD6kRxyniF0m6NgGXEYj3gOt5DxtahfbwUiDGtMcqo/jBVUhsnxs1j0dZOAbhA3t3RZJR6nfdB4fzJETIqPY1oK2QZ/p0UA3lCY7Tuz0op/AQ9SfdsAUdZzY6mJyyNvQ362iTzLAbwfBgMUeuZALiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkLf9784",
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "message": {
        "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "message": {
        "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
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
  "id": -576460752303422802,
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
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422802,
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "event": "funding_locked"
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Channel is `open` and ready to use

#### responder info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "state": "tx_+QENCwH4hLhALQDJVV+C7VDC4ZpMunMcm+xeh+rD6kRxyniF0m6NgGXEYj3gOt5DxtahfbwUiDGtMcqo/jBVUhsnxs1j0dZOAbhA3t3RZJR6nfdB4fzJETIqPY1oK2QZ/p0UA3lCY7Tuz0op/AQ9SfdsAUdZzY6mJyyNvQ362iTzLAbwfBgMUeuZALiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkLf9784"
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "state": "tx_+QENCwH4hLhALQDJVV+C7VDC4ZpMunMcm+xeh+rD6kRxyniF0m6NgGXEYj3gOt5DxtahfbwUiDGtMcqo/jBVUhsnxs1j0dZOAbhA3t3RZJR6nfdB4fzJETIqPY1oK2QZ/p0UA3lCY7Tuz0op/AQ9SfdsAUdZzY6mJyyNvQ362iTzLAbwfBgMUeuZALiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkLf9784"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422801,
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
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422801,
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBh4e8Zpd4ALfoKBuSTU8iiTTaYzjapHAny3uzNCWKbkJAqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt3CRyoE=",
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
  "id": -576460752303422800,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA6DtcHWEt9NtNIau7kBVb1qsqj/caiLYhxAKrtHkspDSQ6WIgF94T5amFwC3fzT0cVf/9ftZmYCREv7HTs+s8KuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7e1cr98"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422800,
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA6DtcHWEt9NtNIau7kBVb1qsqj/caiLYhxAKrtHkspDSQ6WIgF94T5amFwC3fzT0cVf/9ftZmYCREv7HTs+s8KuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7e1cr98",
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
  "id": -576460752303422799,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA6DtcHWEt9NtNIau7kBVb1qsqj/caiLYhxAKrtHkspDSQ6WIgF94T5amFwC3fzT0cVf/9ftZmYCREv7HTs+s8KuEC3hK8kkvlIfSmE80K5fZHgesGFh0uVMauSWnBRdpK4oUUMy+US8n1eFJka6gkB5D/7ZqxkFPFS/M3ELC22mk4CuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7efB9S4"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422799,
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "state": "tx_+NILAfiEuEA6DtcHWEt9NtNIau7kBVb1qsqj/caiLYhxAKrtHkspDSQ6WIgF94T5amFwC3fzT0cVf/9ftZmYCREv7HTs+s8KuEC3hK8kkvlIfSmE80K5fZHgesGFh0uVMauSWnBRdpK4oUUMy+US8n1eFJka6gkB5D/7ZqxkFPFS/M3ELC22mk4CuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7efB9S4"
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "state": "tx_+NILAfiEuEA6DtcHWEt9NtNIau7kBVb1qsqj/caiLYhxAKrtHkspDSQ6WIgF94T5amFwC3fzT0cVf/9ftZmYCREv7HTs+s8KuEC3hK8kkvlIfSmE80K5fZHgesGFh0uVMauSWnBRdpK4oUUMy+US8n1eFJka6gkB5D/7ZqxkFPFS/M3ELC22mk4CuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7efB9S4"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422798,
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
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422798,
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
  "id": -576460752303422797,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422797,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA6DtcHWEt9NtNIau7kBVb1qsqj/caiLYhxAKrtHkspDSQ6WIgF94T5amFwC3fzT0cVf/9ftZmYCREv7HTs+s8KuEC3hK8kkvlIfSmE80K5fZHgesGFh0uVMauSWnBRdpK4oUUMy+US8n1eFJka6gkB5D/7ZqxkFPFS/M3ELC22mk4CuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7efB9S4",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422796,
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
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422796,
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBh4e8Zpd4ALfoKBuSTU8iiTTaYzjapHAny3uzNCWKbkJA6BoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdroZKq8=",
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
  "id": -576460752303422795,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDMvK6O36AgicMXsYq+r8LNE8S80gpXzfXc2U05cJM0tBgAW+rZearSonE+/SMOvc1npgpciK2s6LY4FEhZZbELuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnY9BS/o"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422795,
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDMvK6O36AgicMXsYq+r8LNE8S80gpXzfXc2U05cJM0tBgAW+rZearSonE+/SMOvc1npgpciK2s6LY4FEhZZbELuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnY9BS/o",
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
  "id": -576460752303422794,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECxAvpq4e/F1LRj36wRNphnM+OgL6qZiachRS7YgPDGyqJiF04BHTyFY7g0jaITq9TwYlnLjwE+OXlvRficVzQKuEDMvK6O36AgicMXsYq+r8LNE8S80gpXzfXc2U05cJM0tBgAW+rZearSonE+/SMOvc1npgpciK2s6LY4FEhZZbELuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbHc5D6"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422794,
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "state": "tx_+NILAfiEuECxAvpq4e/F1LRj36wRNphnM+OgL6qZiachRS7YgPDGyqJiF04BHTyFY7g0jaITq9TwYlnLjwE+OXlvRficVzQKuEDMvK6O36AgicMXsYq+r8LNE8S80gpXzfXc2U05cJM0tBgAW+rZearSonE+/SMOvc1npgpciK2s6LY4FEhZZbELuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbHc5D6"
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "state": "tx_+NILAfiEuECxAvpq4e/F1LRj36wRNphnM+OgL6qZiachRS7YgPDGyqJiF04BHTyFY7g0jaITq9TwYlnLjwE+OXlvRficVzQKuEDMvK6O36AgicMXsYq+r8LNE8S80gpXzfXc2U05cJM0tBgAW+rZearSonE+/SMOvc1npgpciK2s6LY4FEhZZbELuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbHc5D6"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422793,
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
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422793,
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
  "id": -576460752303422792,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422792,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECxAvpq4e/F1LRj36wRNphnM+OgL6qZiachRS7YgPDGyqJiF04BHTyFY7g0jaITq9TwYlnLjwE+OXlvRficVzQKuEDMvK6O36AgicMXsYq+r8LNE8S80gpXzfXc2U05cJM0tBgAW+rZearSonE+/SMOvc1npgpciK2s6LY4FEhZZbELuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbHc5D6",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422791,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422791,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECxAvpq4e/F1LRj36wRNphnM+OgL6qZiachRS7YgPDGyqJiF04BHTyFY7g0jaITq9TwYlnLjwE+OXlvRficVzQKuEDMvK6O36AgicMXsYq+r8LNE8S80gpXzfXc2U05cJM0tBgAW+rZearSonE+/SMOvc1npgpciK2s6LY4FEhZZbELuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbHc5D6",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422790,
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
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422790,
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBh4e8Zpd4ALfoKBuSTU8iiTTaYzjapHAny3uzNCWKbkJBKBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrtxtAZBo=",
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
  "id": -576460752303422789,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDr2joymsQCG/f2/zAeKZPEi7G6p6U1FN3W7C49KF4dzWRmkiRoWd3aqm/Gorx6C93JO3PvCYWWjJjfJz09+SoFuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cq3Wft"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422789,
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDr2joymsQCG/f2/zAeKZPEi7G6p6U1FN3W7C49KF4dzWRmkiRoWd3aqm/Gorx6C93JO3PvCYWWjJjfJz09+SoFuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cq3Wft",
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
  "id": -576460752303422788,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBp3j+1QohXtBEok1xQEcwFJ617JMoijjOzb1nfTHZKMtl21rRZz02C7vzm1AszcBJpFpAj1B3HcLWrPp402PkAuEDr2joymsQCG/f2/zAeKZPEi7G6p6U1FN3W7C49KF4dzWRmkiRoWd3aqm/Gorx6C93JO3PvCYWWjJjfJz09+SoFuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fikedg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422788,
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "state": "tx_+NILAfiEuEBp3j+1QohXtBEok1xQEcwFJ617JMoijjOzb1nfTHZKMtl21rRZz02C7vzm1AszcBJpFpAj1B3HcLWrPp402PkAuEDr2joymsQCG/f2/zAeKZPEi7G6p6U1FN3W7C49KF4dzWRmkiRoWd3aqm/Gorx6C93JO3PvCYWWjJjfJz09+SoFuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fikedg"
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "state": "tx_+NILAfiEuEBp3j+1QohXtBEok1xQEcwFJ617JMoijjOzb1nfTHZKMtl21rRZz02C7vzm1AszcBJpFpAj1B3HcLWrPp402PkAuEDr2joymsQCG/f2/zAeKZPEi7G6p6U1FN3W7C49KF4dzWRmkiRoWd3aqm/Gorx6C93JO3PvCYWWjJjfJz09+SoFuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fikedg"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422787,
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
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422787,
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
  "id": -576460752303422786,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422786,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBp3j+1QohXtBEok1xQEcwFJ617JMoijjOzb1nfTHZKMtl21rRZz02C7vzm1AszcBJpFpAj1B3HcLWrPp402PkAuEDr2joymsQCG/f2/zAeKZPEi7G6p6U1FN3W7C49KF4dzWRmkiRoWd3aqm/Gorx6C93JO3PvCYWWjJjfJz09+SoFuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fikedg",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422785,
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
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422785,
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBh4e8Zpd4ALfoKBuSTU8iiTTaYzjapHAny3uzNCWKbkJBaBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjSSijs=",
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
  "id": -576460752303422784,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBaWUejcvTUD7ABJh/m4yFbUroy9g1Ho1FknHKhL7KWdY7HPWgpau3JYOqv4OaOQJWMvmPzl76sJXoNgcUDhn4AuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaadSGH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422784,
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBaWUejcvTUD7ABJh/m4yFbUroy9g1Ho1FknHKhL7KWdY7HPWgpau3JYOqv4OaOQJWMvmPzl76sJXoNgcUDhn4AuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaadSGH",
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
  "id": -576460752303422783,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBAQHd/Dp2mFE8YtAVr43hgN8E10B2c/Sieu8ZX8cDpQvPP2eo/GtqJlBMoMNbqp3eWp2JbOxE9Shp9ajt4P30OuEBaWUejcvTUD7ABJh/m4yFbUroy9g1Ho1FknHKhL7KWdY7HPWgpau3JYOqv4OaOQJWMvmPzl76sJXoNgcUDhn4AuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZbpfK5"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422783,
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "state": "tx_+NILAfiEuEBAQHd/Dp2mFE8YtAVr43hgN8E10B2c/Sieu8ZX8cDpQvPP2eo/GtqJlBMoMNbqp3eWp2JbOxE9Shp9ajt4P30OuEBaWUejcvTUD7ABJh/m4yFbUroy9g1Ho1FknHKhL7KWdY7HPWgpau3JYOqv4OaOQJWMvmPzl76sJXoNgcUDhn4AuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZbpfK5"
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "state": "tx_+NILAfiEuEBAQHd/Dp2mFE8YtAVr43hgN8E10B2c/Sieu8ZX8cDpQvPP2eo/GtqJlBMoMNbqp3eWp2JbOxE9Shp9ajt4P30OuEBaWUejcvTUD7ABJh/m4yFbUroy9g1Ho1FknHKhL7KWdY7HPWgpau3JYOqv4OaOQJWMvmPzl76sJXoNgcUDhn4AuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZbpfK5"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422782,
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
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422782,
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
  "id": -576460752303422781,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422781,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBAQHd/Dp2mFE8YtAVr43hgN8E10B2c/Sieu8ZX8cDpQvPP2eo/GtqJlBMoMNbqp3eWp2JbOxE9Shp9ajt4P30OuEBaWUejcvTUD7ABJh/m4yFbUroy9g1Ho1FknHKhL7KWdY7HPWgpau3JYOqv4OaOQJWMvmPzl76sJXoNgcUDhn4AuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZbpfK5",
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBAQHd/Dp2mFE8YtAVr43hgN8E10B2c/Sieu8ZX8cDpQvPP2eo/GtqJlBMoMNbqp3eWp2JbOxE9Shp9ajt4P30OuEBaWUejcvTUD7ABJh/m4yFbUroy9g1Ho1FknHKhL7KWdY7HPWgpau3JYOqv4OaOQJWMvmPzl76sJXoNgcUDhn4AuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZbpfK5",
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBAQHd/Dp2mFE8YtAVr43hgN8E10B2c/Sieu8ZX8cDpQvPP2eo/GtqJlBMoMNbqp3eWp2JbOxE9Shp9ajt4P30OuEBaWUejcvTUD7ABJh/m4yFbUroy9g1Ho1FknHKhL7KWdY7HPWgpau3JYOqv4OaOQJWMvmPzl76sJXoNgcUDhn4AuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZbpfK5",
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
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
  "method": "channels.slash",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBh4e8Zpd4ALfoKBuSTU8iiTTaYzjapHAny3uzNCWKbkJoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FbjU+NILAfiEuEBAQHd/Dp2mFE8YtAVr43hgN8E10B2c/Sieu8ZX8cDpQvPP2eo/GtqJlBMoMNbqp3eWp2JbOxE9Shp9ajt4P30OuEBaWUejcvTUD7ABJh/m4yFbUroy9g1Ho1FknHKhL7KWdY7HPWgpau3JYOqv4OaOQJWMvmPzl76sJXoNgcUDhn4AuEj4RjkCoQYeHvGaXeAC36Cgbkk1PIok02mM42qRwJ8t7szQlim5CQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wna5AUz5AUk8AfkBP/kBPKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvkBGPh0oCiW0e4qVvD/C94E6/En+1vvEgzoctloLayg1hD1Tl5u+FGAgICAgICg46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVuAgICAoKcJtie4oQxB6+5JVy+F3eNaNF7V7TgRPXFlQNJ4W/wIgICAgID4T6CnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CO2gP/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWLygoBAIY/qiUiX//4T6DjooHlLkRUA0QFUOns+/GhHcvejx4IPZN7Jd7GGFRtW+2gNllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAHAwMDAwACGGR7ISegAQ7ReExY=",
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
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
  "id": -576460752303422780,
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
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
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422780,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422779,
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
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
    "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
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
  "channel_id": "ch_EGQ3XK3xorMzJUKNdGbvPtUKNwpz4fYmkaddNwYV7jxNTJpjp",
  "id": -576460752303422779,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
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
      "fsm_id": "ba_heAJgPqS2zzjhuYNstXy0CRq6jRdiIRM0auPy7D9JxfUmn8S"
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
      "fsm_id": "ba_yxbdfePcxtWp8FGIswhtuSC8DdYBaY+pc2MD5ckHwrkLOWKG"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZD71c1LA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422778,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDmd95M71pR2F13oyBZxdviVphBrKcbJ6gufMZbL+dMDlOLQNctM/41R6RzdEQoEhKp65+KQYl5VGdGjAhK5y4FuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2Q3vMVMA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422778,
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
      "signed_tx": "tx_+MsLAfhCuEDmd95M71pR2F13oyBZxdviVphBrKcbJ6gufMZbL+dMDlOLQNctM/41R6RzdEQoEhKp65+KQYl5VGdGjAhK5y4FuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2Q3vMVMA=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422777,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAB0SEnUoBN9dekKe7SHuzjqD+9V/rKr/Wqm/XU00HQ4QUXjD/Ba7/RQ/kRjR7Z9vGX5fITuvP+U6OtfzM3PUyBLhA5nfeTO9aUdhdd6MgWcXb4laYQaynGyeoLnzGWy/nTA5Ti0DXLTP+NUekc3REKBISqeufikGJeVRnRowISucuBbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkOgllTj"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422777,
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAB0SEnUoBN9dekKe7SHuzjqD+9V/rKr/Wqm/XU00HQ4QUXjD/Ba7/RQ/kRjR7Z9vGX5fITuvP+U6OtfzM3PUyBLhA5nfeTO9aUdhdd6MgWcXb4laYQaynGyeoLnzGWy/nTA5Ti0DXLTP+NUekc3REKBISqeufikGJeVRnRowISucuBbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkOgllTj",
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAB0SEnUoBN9dekKe7SHuzjqD+9V/rKr/Wqm/XU00HQ4QUXjD/Ba7/RQ/kRjR7Z9vGX5fITuvP+U6OtfzM3PUyBLhA5nfeTO9aUdhdd6MgWcXb4laYQaynGyeoLnzGWy/nTA5Ti0DXLTP+NUekc3REKBISqeufikGJeVRnRowISucuBbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkOgllTj",
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAB0SEnUoBN9dekKe7SHuzjqD+9V/rKr/Wqm/XU00HQ4QUXjD/Ba7/RQ/kRjR7Z9vGX5fITuvP+U6OtfzM3PUyBLhA5nfeTO9aUdhdd6MgWcXb4laYQaynGyeoLnzGWy/nTA5Ti0DXLTP+NUekc3REKBISqeufikGJeVRnRowISucuBbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkOgllTj",
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAB0SEnUoBN9dekKe7SHuzjqD+9V/rKr/Wqm/XU00HQ4QUXjD/Ba7/RQ/kRjR7Z9vGX5fITuvP+U6OtfzM3PUyBLhA5nfeTO9aUdhdd6MgWcXb4laYQaynGyeoLnzGWy/nTA5Ti0DXLTP+NUekc3REKBISqeufikGJeVRnRowISucuBbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkOgllTj",
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "message": {
        "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "message": {
        "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
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
  "id": -576460752303422776,
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
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422776,
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "state": "tx_+QENCwH4hLhAB0SEnUoBN9dekKe7SHuzjqD+9V/rKr/Wqm/XU00HQ4QUXjD/Ba7/RQ/kRjR7Z9vGX5fITuvP+U6OtfzM3PUyBLhA5nfeTO9aUdhdd6MgWcXb4laYQaynGyeoLnzGWy/nTA5Ti0DXLTP+NUekc3REKBISqeufikGJeVRnRowISucuBbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkOgllTj"
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "state": "tx_+QENCwH4hLhAB0SEnUoBN9dekKe7SHuzjqD+9V/rKr/Wqm/XU00HQ4QUXjD/Ba7/RQ/kRjR7Z9vGX5fITuvP+U6OtfzM3PUyBLhA5nfeTO9aUdhdd6MgWcXb4laYQaynGyeoLnzGWy/nTA5Ti0DXLTP+NUekc3REKBISqeufikGJeVRnRowISucuBbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdkOgllTj"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422775,
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
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422775,
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgc116Sd1o3Efu8dyvzaAOF1Mt0mAxofHe7+lSeFRNV5AqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt7hHJF8=",
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
  "id": -576460752303422774,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDouWBrhRaiRZV4x1v76HfKH5XLg3A1daBU4ic4IeHvvn1g7yPvtOg9OxNWtX/bqN9GsVeA/EwJ+DChEPnas7oCuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7czoYfY"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422774,
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDouWBrhRaiRZV4x1v76HfKH5XLg3A1daBU4ic4IeHvvn1g7yPvtOg9OxNWtX/bqN9GsVeA/EwJ+DChEPnas7oCuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7czoYfY",
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
  "id": -576460752303422773,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDouWBrhRaiRZV4x1v76HfKH5XLg3A1daBU4ic4IeHvvn1g7yPvtOg9OxNWtX/bqN9GsVeA/EwJ+DChEPnas7oCuED+K2XH2h/miJjeNvTznYxlbSSDrQMGEEq01ZI2O/gyWrA+kZnN6WvKudidCTmuVREW58pWyG/mVXvOw0CL/GcFuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7ejN72O"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422773,
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "state": "tx_+NILAfiEuEDouWBrhRaiRZV4x1v76HfKH5XLg3A1daBU4ic4IeHvvn1g7yPvtOg9OxNWtX/bqN9GsVeA/EwJ+DChEPnas7oCuED+K2XH2h/miJjeNvTznYxlbSSDrQMGEEq01ZI2O/gyWrA+kZnN6WvKudidCTmuVREW58pWyG/mVXvOw0CL/GcFuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7ejN72O"
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "state": "tx_+NILAfiEuEDouWBrhRaiRZV4x1v76HfKH5XLg3A1daBU4ic4IeHvvn1g7yPvtOg9OxNWtX/bqN9GsVeA/EwJ+DChEPnas7oCuED+K2XH2h/miJjeNvTznYxlbSSDrQMGEEq01ZI2O/gyWrA+kZnN6WvKudidCTmuVREW58pWyG/mVXvOw0CL/GcFuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7ejN72O"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422772,
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
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422772,
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
  "id": -576460752303422771,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422771,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDouWBrhRaiRZV4x1v76HfKH5XLg3A1daBU4ic4IeHvvn1g7yPvtOg9OxNWtX/bqN9GsVeA/EwJ+DChEPnas7oCuED+K2XH2h/miJjeNvTznYxlbSSDrQMGEEq01ZI2O/gyWrA+kZnN6WvKudidCTmuVREW58pWyG/mVXvOw0CL/GcFuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7ejN72O",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422770,
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
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422770,
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgc116Sd1o3Efu8dyvzaAOF1Mt0mAxofHe7+lSeFRNV5A6BoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdlsvP+g=",
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
  "id": -576460752303422769,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDVd8VKIymN72PewYd+JHd/z9KRJ9dSWVk7E23g6OH8QDzVBsAwa9lYcc689W0ajHRiRxX7Qwtjju8LLVL1dPwGuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnakPyHj"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422769,
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDVd8VKIymN72PewYd+JHd/z9KRJ9dSWVk7E23g6OH8QDzVBsAwa9lYcc689W0ajHRiRxX7Qwtjju8LLVL1dPwGuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnakPyHj",
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
  "id": -576460752303422768,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDVd8VKIymN72PewYd+JHd/z9KRJ9dSWVk7E23g6OH8QDzVBsAwa9lYcc689W0ajHRiRxX7Qwtjju8LLVL1dPwGuEDppoIs2LxBO3NDw6mGz1K6hcXdDGjdIkC8uyovv4JsD815MSbnztHroq0H3PxUzJc1oeJnOJxP95G1DiNW4CgBuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbege/k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422768,
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "state": "tx_+NILAfiEuEDVd8VKIymN72PewYd+JHd/z9KRJ9dSWVk7E23g6OH8QDzVBsAwa9lYcc689W0ajHRiRxX7Qwtjju8LLVL1dPwGuEDppoIs2LxBO3NDw6mGz1K6hcXdDGjdIkC8uyovv4JsD815MSbnztHroq0H3PxUzJc1oeJnOJxP95G1DiNW4CgBuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbege/k"
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "state": "tx_+NILAfiEuEDVd8VKIymN72PewYd+JHd/z9KRJ9dSWVk7E23g6OH8QDzVBsAwa9lYcc689W0ajHRiRxX7Qwtjju8LLVL1dPwGuEDppoIs2LxBO3NDw6mGz1K6hcXdDGjdIkC8uyovv4JsD815MSbnztHroq0H3PxUzJc1oeJnOJxP95G1DiNW4CgBuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbege/k"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422767,
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
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422767,
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
  "id": -576460752303422766,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422766,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDVd8VKIymN72PewYd+JHd/z9KRJ9dSWVk7E23g6OH8QDzVBsAwa9lYcc689W0ajHRiRxX7Qwtjju8LLVL1dPwGuEDppoIs2LxBO3NDw6mGz1K6hcXdDGjdIkC8uyovv4JsD815MSbnztHroq0H3PxUzJc1oeJnOJxP95G1DiNW4CgBuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbege/k",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422765,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422765,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDVd8VKIymN72PewYd+JHd/z9KRJ9dSWVk7E23g6OH8QDzVBsAwa9lYcc689W0ajHRiRxX7Qwtjju8LLVL1dPwGuEDppoIs2LxBO3NDw6mGz1K6hcXdDGjdIkC8uyovv4JsD815MSbnztHroq0H3PxUzJc1oeJnOJxP95G1DiNW4CgBuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbege/k",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422764,
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
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422764,
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgc116Sd1o3Efu8dyvzaAOF1Mt0mAxofHe7+lSeFRNV5BKBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt4WqQ7c=",
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
  "id": -576460752303422763,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA5deQ/HNn7RxJVo8QrIaHl0Yv5kSBpaW10cwrzJo4/ar9aT9Q8zQzal1z80w4COzcztRFLlNgEgM3maZ2bBrMJuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7erDd2R"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422763,
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA5deQ/HNn7RxJVo8QrIaHl0Yv5kSBpaW10cwrzJo4/ar9aT9Q8zQzal1z80w4COzcztRFLlNgEgM3maZ2bBrMJuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7erDd2R",
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
  "id": -576460752303422762,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA5deQ/HNn7RxJVo8QrIaHl0Yv5kSBpaW10cwrzJo4/ar9aT9Q8zQzal1z80w4COzcztRFLlNgEgM3maZ2bBrMJuEDrHcy6n7Zic4AeSHiEKbF/aqE7xOHf3YP6OmlK/FcnGqT7snSE0dGfKnqEDGByPbgJ5u6Q6g1ruDQauMW4yJoLuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eAzBmG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422762,
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "state": "tx_+NILAfiEuEA5deQ/HNn7RxJVo8QrIaHl0Yv5kSBpaW10cwrzJo4/ar9aT9Q8zQzal1z80w4COzcztRFLlNgEgM3maZ2bBrMJuEDrHcy6n7Zic4AeSHiEKbF/aqE7xOHf3YP6OmlK/FcnGqT7snSE0dGfKnqEDGByPbgJ5u6Q6g1ruDQauMW4yJoLuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eAzBmG"
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "state": "tx_+NILAfiEuEA5deQ/HNn7RxJVo8QrIaHl0Yv5kSBpaW10cwrzJo4/ar9aT9Q8zQzal1z80w4COzcztRFLlNgEgM3maZ2bBrMJuEDrHcy6n7Zic4AeSHiEKbF/aqE7xOHf3YP6OmlK/FcnGqT7snSE0dGfKnqEDGByPbgJ5u6Q6g1ruDQauMW4yJoLuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eAzBmG"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422761,
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
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422761,
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
  "id": -576460752303422760,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422760,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA5deQ/HNn7RxJVo8QrIaHl0Yv5kSBpaW10cwrzJo4/ar9aT9Q8zQzal1z80w4COzcztRFLlNgEgM3maZ2bBrMJuEDrHcy6n7Zic4AeSHiEKbF/aqE7xOHf3YP6OmlK/FcnGqT7snSE0dGfKnqEDGByPbgJ5u6Q6g1ruDQauMW4yJoLuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eAzBmG",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422759,
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
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422759,
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgc116Sd1o3Efu8dyvzaAOF1Mt0mAxofHe7+lSeFRNV5BaBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdlbACyg=",
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
  "id": -576460752303422758,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAX8FXQXp4+xVp+2XxE0xFX4lSMVD/DuHhloITeThuzJqt7Ei21BZ/Axi6pTDLwEWPefB0ApsAyXKHE6VD9/5gIuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYQfEce"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422758,
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAX8FXQXp4+xVp+2XxE0xFX4lSMVD/DuHhloITeThuzJqt7Ei21BZ/Axi6pTDLwEWPefB0ApsAyXKHE6VD9/5gIuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYQfEce",
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
  "id": -576460752303422757,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAX8FXQXp4+xVp+2XxE0xFX4lSMVD/DuHhloITeThuzJqt7Ei21BZ/Axi6pTDLwEWPefB0ApsAyXKHE6VD9/5gIuEDUu48FwdssAT3EIe60pk9oGodf34riwz+ITVDOk5NtvrwuCPFClmr14Xuxyo/OtkdgC4QYtlsjiWvLjpnuplUOuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZkXQIM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422757,
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "state": "tx_+NILAfiEuEAX8FXQXp4+xVp+2XxE0xFX4lSMVD/DuHhloITeThuzJqt7Ei21BZ/Axi6pTDLwEWPefB0ApsAyXKHE6VD9/5gIuEDUu48FwdssAT3EIe60pk9oGodf34riwz+ITVDOk5NtvrwuCPFClmr14Xuxyo/OtkdgC4QYtlsjiWvLjpnuplUOuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZkXQIM"
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "state": "tx_+NILAfiEuEAX8FXQXp4+xVp+2XxE0xFX4lSMVD/DuHhloITeThuzJqt7Ei21BZ/Axi6pTDLwEWPefB0ApsAyXKHE6VD9/5gIuEDUu48FwdssAT3EIe60pk9oGodf34riwz+ITVDOk5NtvrwuCPFClmr14Xuxyo/OtkdgC4QYtlsjiWvLjpnuplUOuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZkXQIM"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422756,
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
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422756,
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
  "id": -576460752303422755,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422755,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAX8FXQXp4+xVp+2XxE0xFX4lSMVD/DuHhloITeThuzJqt7Ei21BZ/Axi6pTDLwEWPefB0ApsAyXKHE6VD9/5gIuEDUu48FwdssAT3EIe60pk9oGodf34riwz+ITVDOk5NtvrwuCPFClmr14Xuxyo/OtkdgC4QYtlsjiWvLjpnuplUOuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZkXQIM",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAX8FXQXp4+xVp+2XxE0xFX4lSMVD/DuHhloITeThuzJqt7Ei21BZ/Axi6pTDLwEWPefB0ApsAyXKHE6VD9/5gIuEDUu48FwdssAT3EIe60pk9oGodf34riwz+ITVDOk5NtvrwuCPFClmr14Xuxyo/OtkdgC4QYtlsjiWvLjpnuplUOuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZkXQIM",
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAX8FXQXp4+xVp+2XxE0xFX4lSMVD/DuHhloITeThuzJqt7Ei21BZ/Axi6pTDLwEWPefB0ApsAyXKHE6VD9/5gIuEDUu48FwdssAT3EIe60pk9oGodf34riwz+ITVDOk5NtvrwuCPFClmr14Xuxyo/OtkdgC4QYtlsjiWvLjpnuplUOuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZkXQIM",
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
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
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBgc116Sd1o3Efu8dyvzaAOF1Mt0mAxofHe7+lSeFRNV5oQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv7jU+NILAfiEuEAX8FXQXp4+xVp+2XxE0xFX4lSMVD/DuHhloITeThuzJqt7Ei21BZ/Axi6pTDLwEWPefB0ApsAyXKHE6VD9/5gIuEDUu48FwdssAT3EIe60pk9oGodf34riwz+ITVDOk5NtvrwuCPFClmr14Xuxyo/OtkdgC4QYtlsjiWvLjpnuplUOuEj4RjkCoQYHNdekndaNxH7vHcr82gDhdTLdJgMaHx3u/pUnhUTVeQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wna5AUz5AUk8AfkBP/kBPKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvkBGPh0oCiW0e4qVvD/C94E6/En+1vvEgzoctloLayg1hD1Tl5u+FGAgICAgICg46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVuAgICAoKcJtie4oQxB6+5JVy+F3eNaNF7V7TgRPXFlQNJ4W/wIgICAgID4T6CnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CO2gP/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWLygoBAIY/qiUiX//4T6DjooHlLkRUA0QFUOns+/GhHcvejx4IPZN7Jd7GGFRtW+2gNllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAHAwMDAwACGGR7ISegAGeJNcKc=",
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "event": "aborted_update"
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder info
> Channel is `open` and ready to use

#### responder ---> node
```javascript
{
  "id": -576460752303422754,
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
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422754,
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422753,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### responder closes WebSocket connection
```

```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
  "id": -576460752303422753,
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
    "channel_id": "ch_4BBKm6p7iDxiRjus5cNpp5LNyWTbDuxVhbvGsmrEhtiV1n2f7",
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
