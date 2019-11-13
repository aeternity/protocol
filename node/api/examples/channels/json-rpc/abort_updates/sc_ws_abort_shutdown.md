
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
      "fsm_id": "ba_RYCNizIsO41fU38MTWnFKpxyQ5aKT/SzTPrryGawkpwyafDi"
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
      "fsm_id": "ba_4LeWtRG6UsygKzjB4ZcMVtKRE6Pi+877c/4Ay3kBEj5CpB03"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnY9w9/Ukg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422862,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAcU7zwCFTSg5aE7iGRK20vd/quTqS0h8/VIn6mqE/XLriLV68zmk+wejpoYj2fuh316hLBOiqD8ALPAwD9qh8CuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2PYsEVCY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422862,
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
      "signed_tx": "tx_+MsLAfhCuEAcU7zwCFTSg5aE7iGRK20vd/quTqS0h8/VIn6mqE/XLriLV68zmk+wejpoYj2fuh316hLBOiqD8ALPAwD9qh8CuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2PYsEVCY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422861,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAHFO88AhU0oOWhO4hkSttL3f6rk6ktIfP1SJ+pqhP1y64i1evM5pPsHo6aGI9n7od9eoSwToqg/ACzwMA/aofArhAyCsS0aTPKsVtSK2s/w97xteOtKIwGN1atV+xI1A4PTcgSR8p3s7deYSb7yqDsJaRn44iDEKTy8H+CrXoOEMjDbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdj04OO1c"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422861,
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
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAHFO88AhU0oOWhO4hkSttL3f6rk6ktIfP1SJ+pqhP1y64i1evM5pPsHo6aGI9n7od9eoSwToqg/ACzwMA/aofArhAyCsS0aTPKsVtSK2s/w97xteOtKIwGN1atV+xI1A4PTcgSR8p3s7deYSb7yqDsJaRn44iDEKTy8H+CrXoOEMjDbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdj04OO1c",
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
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAHFO88AhU0oOWhO4hkSttL3f6rk6ktIfP1SJ+pqhP1y64i1evM5pPsHo6aGI9n7od9eoSwToqg/ACzwMA/aofArhAyCsS0aTPKsVtSK2s/w97xteOtKIwGN1atV+xI1A4PTcgSR8p3s7deYSb7yqDsJaRn44iDEKTy8H+CrXoOEMjDbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdj04OO1c",
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
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAHFO88AhU0oOWhO4hkSttL3f6rk6ktIfP1SJ+pqhP1y64i1evM5pPsHo6aGI9n7od9eoSwToqg/ACzwMA/aofArhAyCsS0aTPKsVtSK2s/w97xteOtKIwGN1atV+xI1A4PTcgSR8p3s7deYSb7yqDsJaRn44iDEKTy8H+CrXoOEMjDbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdj04OO1c",
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
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAHFO88AhU0oOWhO4hkSttL3f6rk6ktIfP1SJ+pqhP1y64i1evM5pPsHo6aGI9n7od9eoSwToqg/ACzwMA/aofArhAyCsS0aTPKsVtSK2s/w97xteOtKIwGN1atV+xI1A4PTcgSR8p3s7deYSb7yqDsJaRn44iDEKTy8H+CrXoOEMjDbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdj04OO1c",
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
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
    "data": {
      "message": {
        "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
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
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
    "data": {
      "message": {
        "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
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
  "id": -576460752303422860,
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
  "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
  "id": -576460752303422860,
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
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
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
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
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

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
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
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
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
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
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
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
    "data": {
      "state": "tx_+QENCwH4hLhAHFO88AhU0oOWhO4hkSttL3f6rk6ktIfP1SJ+pqhP1y64i1evM5pPsHo6aGI9n7od9eoSwToqg/ACzwMA/aofArhAyCsS0aTPKsVtSK2s/w97xteOtKIwGN1atV+xI1A4PTcgSR8p3s7deYSb7yqDsJaRn44iDEKTy8H+CrXoOEMjDbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdj04OO1c"
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
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
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
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
    "data": {
      "state": "tx_+QENCwH4hLhAHFO88AhU0oOWhO4hkSttL3f6rk6ktIfP1SJ+pqhP1y64i1evM5pPsHo6aGI9n7od9eoSwToqg/ACzwMA/aofArhAyCsS0aTPKsVtSK2s/w97xteOtKIwGN1atV+xI1A4PTcgSR8p3s7deYSb7yqDsJaRn44iDEKTy8H+CrXoOEMjDbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdj04OO1c"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBjhJtHCeX1uRiTTBuWTJuW0s7B1n47vUpE7jDOUYdKDwoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY2kdavv/+GG0jrV+ABAIYSMJzlQAA+tWoGxg==",
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
  "method": "channels.shutdown_sign",
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
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
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
  "method": "channels.shutdown",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBjhJtHCeX1uRiTTBuWTJuW0s7B1n47vUpE7jDOUYdKDwoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4Y2kdavv/+GG0jrV+ABAIYSMJzlQAAXl3DICQ==",
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
  "method": "channels.shutdown_sign",
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
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
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
  "method": "channels.shutdown",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBjhJtHCeX1uRiTTBuWTJuW0s7B1n47vUpE7jDOUYdKDwoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY2kdavv/+GG0jrV+ABAIYSMJzlQAA+tWoGxg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422859,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEDxrCiBPOoNgXl+tkcxprgoOSX3PaGYMRH21Pu1+A+WEFBngCM8dfkIGoW3hE3nQOghlY9zkQIER0Z4b+O2GKYOuF/4XTUBoQY4SbRwnl9bkYk0wblkybltLOwdZ+O71KRO4wzlGHSg8KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7//hhtI61fgAQCGEjCc5UAAPoxHu8Y="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
  "id": -576460752303422859,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
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
      "method": "channels.shutdown_sign",
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
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
    "data": {
      "event": "shutdown"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEDxrCiBPOoNgXl+tkcxprgoOSX3PaGYMRH21Pu1+A+WEFBngCM8dfkIGoW3hE3nQOghlY9zkQIER0Z4b+O2GKYOuF/4XTUBoQY4SbRwnl9bkYk0wblkybltLOwdZ+O71KRO4wzlGHSg8KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7//hhtI61fgAQCGEjCc5UAAPoxHu8Y=",
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
  "method": "channels.shutdown_sign_ack",
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
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
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
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
    "data": {
      "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
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
  "id": -576460752303422858,
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
  "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
  "id": -576460752303422858,
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
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
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
  "id": -576460752303422857,
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
    "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
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
  "channel_id": "ch_RnoMBaNN995VZ1uSEgeymsjg3z6adMZys4jeEaRNbvhFEfBwP",
  "id": -576460752303422857,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```
