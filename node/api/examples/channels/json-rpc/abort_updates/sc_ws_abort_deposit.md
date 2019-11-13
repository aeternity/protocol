
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
      "fsm_id": "ba_0c7ncwu1F3SzzByyTyTZNGNUCOAnmzO9Nz4fujyCYIOEOCxA"
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
      "fsm_id": "ba_7T0JqFwOZsBWTPadpXcwI4UAklYNUm760OCl4L/aTn3K5+pb"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnY6B1nLJQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422889,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEC9zZxinkmJRCH4ruQfBYPq3w55cMQPkOmr+GU8gyIMCMC966haUcqnjxdU6lfnyCkuZnZ+tfSgAipVmOmJ4+4FuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2Ol/P3FQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422889,
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
      "signed_tx": "tx_+MsLAfhCuEC9zZxinkmJRCH4ruQfBYPq3w55cMQPkOmr+GU8gyIMCMC966haUcqnjxdU6lfnyCkuZnZ+tfSgAipVmOmJ4+4FuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2Ol/P3FQ=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422888,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAvc2cYp5JiUQh+K7kHwWD6t8OeXDED5Dpq/hlPIMiDAjAveuoWlHKp48XVOpX58gpLmZ2frX0oAIqVZjpiePuBbhA1AWh6d43eOWrGvAlK5AEinkLE7MhOV60SHy8HCPn+JHkE0xzsNcIAaz/yLE7FEzIkEFc4aM6LyuHdiYrms2xB7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjpPhA3U"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422888,
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
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAvc2cYp5JiUQh+K7kHwWD6t8OeXDED5Dpq/hlPIMiDAjAveuoWlHKp48XVOpX58gpLmZ2frX0oAIqVZjpiePuBbhA1AWh6d43eOWrGvAlK5AEinkLE7MhOV60SHy8HCPn+JHkE0xzsNcIAaz/yLE7FEzIkEFc4aM6LyuHdiYrms2xB7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjpPhA3U",
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
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAvc2cYp5JiUQh+K7kHwWD6t8OeXDED5Dpq/hlPIMiDAjAveuoWlHKp48XVOpX58gpLmZ2frX0oAIqVZjpiePuBbhA1AWh6d43eOWrGvAlK5AEinkLE7MhOV60SHy8HCPn+JHkE0xzsNcIAaz/yLE7FEzIkEFc4aM6LyuHdiYrms2xB7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjpPhA3U",
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
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAvc2cYp5JiUQh+K7kHwWD6t8OeXDED5Dpq/hlPIMiDAjAveuoWlHKp48XVOpX58gpLmZ2frX0oAIqVZjpiePuBbhA1AWh6d43eOWrGvAlK5AEinkLE7MhOV60SHy8HCPn+JHkE0xzsNcIAaz/yLE7FEzIkEFc4aM6LyuHdiYrms2xB7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjpPhA3U",
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
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAvc2cYp5JiUQh+K7kHwWD6t8OeXDED5Dpq/hlPIMiDAjAveuoWlHKp48XVOpX58gpLmZ2frX0oAIqVZjpiePuBbhA1AWh6d43eOWrGvAlK5AEinkLE7MhOV60SHy8HCPn+JHkE0xzsNcIAaz/yLE7FEzIkEFc4aM6LyuHdiYrms2xB7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjpPhA3U",
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
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
    "data": {
      "message": {
        "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
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
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
    "data": {
      "message": {
        "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
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
  "id": -576460752303422887,
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
  "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
  "id": -576460752303422887,
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
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
    "data": {
      "event": "own_funding_locked"
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
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### initiator info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
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
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
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
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
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
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
    "data": {
      "state": "tx_+QENCwH4hLhAvc2cYp5JiUQh+K7kHwWD6t8OeXDED5Dpq/hlPIMiDAjAveuoWlHKp48XVOpX58gpLmZ2frX0oAIqVZjpiePuBbhA1AWh6d43eOWrGvAlK5AEinkLE7MhOV60SHy8HCPn+JHkE0xzsNcIAaz/yLE7FEzIkEFc4aM6LyuHdiYrms2xB7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjpPhA3U"
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
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
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
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
    "data": {
      "state": "tx_+QENCwH4hLhAvc2cYp5JiUQh+K7kHwWD6t8OeXDED5Dpq/hlPIMiDAjAveuoWlHKp48XVOpX58gpLmZ2frX0oAIqVZjpiePuBbhA1AWh6d43eOWrGvAlK5AEinkLE7MhOV60SHy8HCPn+JHkE0xzsNcIAaz/yLE7FEzIkEFc4aM6LyuHdiYrms2xB7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjpPhA3U"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBiu3likmgM/uVFZHmi0sWHK78EjrIi8iauFkQpzDFOksoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FQIAhg/AoHKQAKBkHkp+5scV2OHwQbjEIZHR7qRYh9akzYCkDxPO9Ji42QI7BD0fCw==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainDeposit"
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
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
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
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
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
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBiu3likmgM/uVFZHmi0sWHK78EjrIi8iauFkQpzDFOksoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWvwIAhg/AoHKQAKCrqnfKzIiWVHOBzfLr5rNELJOPLHdCEdiPdzAvTDJPTwIXDTu2Xg==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainDeposit"
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
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
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
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBiu3likmgM/uVFZHmi0sWHK78EjrIi8iauFkQpzDFOksoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FQIAhg/AoHKQAKBkHkp+5scV2OHwQbjEIZHR7qRYh9akzYCkDxPO9Ji42QI7BD0fCw==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainDeposit"
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
  "id": -576460752303422886,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEDfAlCMleXzrZOA188puxkCs3MTPe1q2sLUW5DE3iFGgRSmp4nR4ia4EpPCm4ms6nNyen0971EEWWfmheYTC+kNuHT4cjMBoQYrt5YpJoDP7lRWR5otLFhyu/BI6yIvImrhZEKcwxTpLKEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgZB5KfubHFdjh8EG4xCGR0e6kWIfWpM2ApA8TzvSYuNkCO5016hs="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
  "id": -576460752303422886,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1018,
        "message": "Not allowed at current channel state"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.deposit_tx",
      "params": {
        "error": 42
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
    "data": {
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEDfAlCMleXzrZOA188puxkCs3MTPe1q2sLUW5DE3iFGgRSmp4nR4ia4EpPCm4ms6nNyen0971EEWWfmheYTC+kNuHT4cjMBoQYrt5YpJoDP7lRWR5otLFhyu/BI6yIvImrhZEKcwxTpLKEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgZB5KfubHFdjh8EG4xCGR0e6kWIfWpM2ApA8TzvSYuNkCO5016hs=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainDeposit"
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
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
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
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
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
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
    "data": {
      "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
      "error_code": 42,
      "error_msg": "unknown",
      "round": 1
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422885,
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
  "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
  "id": -576460752303422885,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422884,
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
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
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
    "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
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
  "channel_id": "ch_LFhLo786eb8RwFGr63Ukt8HYHf5UF1eR3cFsXy77RRWhRJV2S",
  "id": -576460752303422884,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```
