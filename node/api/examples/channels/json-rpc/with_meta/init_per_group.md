
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
      "fsm_id": "ba_BnxO3VthuFHPHkEDPhTtvxHM9Aypv+QzQm4GLk2rU1iySF/N"
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
      "fsm_id": "ba_OnGGP18wSlBPl7yJF47kdc8cKrZqqQ084rvcOkj2zSl/oegw"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYcM5/6oA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423141,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAJgRIeHPAWCf2iVIWK2M3k/rA3J0goOZ4LIMJYg+hzASSgcIxFUSTXz7oAJ4drDUWPClifGGIS4zGqwXhS9KAMuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2HI4ppIg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423141,
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
      "signed_tx": "tx_+MsLAfhCuEAJgRIeHPAWCf2iVIWK2M3k/rA3J0goOZ4LIMJYg+hzASSgcIxFUSTXz7oAJ4drDUWPClifGGIS4zGqwXhS9KAMuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2HI4ppIg=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423140,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhACYESHhzwFgn9olSFitjN5P6wNydIKDmeCyDCWIPocwEkoHCMRVEk18+6ACeHaw1FjwpYnxhiEuMxqsF4UvSgDLhA3sQz7iHwWeB0iNzdklFO5lNTV0G8zWNy/Db0Q5YWoRxhre29sKhcxjmM+3BTYLhIz92OiYRlrLttfEPCTX/vA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhyztFmz"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423140,
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhACYESHhzwFgn9olSFitjN5P6wNydIKDmeCyDCWIPocwEkoHCMRVEk18+6ACeHaw1FjwpYnxhiEuMxqsF4UvSgDLhA3sQz7iHwWeB0iNzdklFO5lNTV0G8zWNy/Db0Q5YWoRxhre29sKhcxjmM+3BTYLhIz92OiYRlrLttfEPCTX/vA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhyztFmz",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhACYESHhzwFgn9olSFitjN5P6wNydIKDmeCyDCWIPocwEkoHCMRVEk18+6ACeHaw1FjwpYnxhiEuMxqsF4UvSgDLhA3sQz7iHwWeB0iNzdklFO5lNTV0G8zWNy/Db0Q5YWoRxhre29sKhcxjmM+3BTYLhIz92OiYRlrLttfEPCTX/vA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhyztFmz",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhACYESHhzwFgn9olSFitjN5P6wNydIKDmeCyDCWIPocwEkoHCMRVEk18+6ACeHaw1FjwpYnxhiEuMxqsF4UvSgDLhA3sQz7iHwWeB0iNzdklFO5lNTV0G8zWNy/Db0Q5YWoRxhre29sKhcxjmM+3BTYLhIz92OiYRlrLttfEPCTX/vA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhyztFmz",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhACYESHhzwFgn9olSFitjN5P6wNydIKDmeCyDCWIPocwEkoHCMRVEk18+6ACeHaw1FjwpYnxhiEuMxqsF4UvSgDLhA3sQz7iHwWeB0iNzdklFO5lNTV0G8zWNy/Db0Q5YWoRxhre29sKhcxjmM+3BTYLhIz92OiYRlrLttfEPCTX/vA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhyztFmz",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "message": {
        "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "message": {
        "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
  "id": -576460752303423139,
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
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423139,
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "state": "tx_+QENCwH4hLhACYESHhzwFgn9olSFitjN5P6wNydIKDmeCyDCWIPocwEkoHCMRVEk18+6ACeHaw1FjwpYnxhiEuMxqsF4UvSgDLhA3sQz7iHwWeB0iNzdklFO5lNTV0G8zWNy/Db0Q5YWoRxhre29sKhcxjmM+3BTYLhIz92OiYRlrLttfEPCTX/vA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhyztFmz"
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "state": "tx_+QENCwH4hLhACYESHhzwFgn9olSFitjN5P6wNydIKDmeCyDCWIPocwEkoHCMRVEk18+6ACeHaw1FjwpYnxhiEuMxqsF4UvSgDLhA3sQz7iHwWeB0iNzdklFO5lNTV0G8zWNy/Db0Q5YWoRxhre29sKhcxjmM+3BTYLhIz92OiYRlrLttfEPCTX/vA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdhyztFmz"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423138,
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
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423138,
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
        "meta": [
          "meta 1"
        ],
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
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvXwJiJ/s16obG8kx4Cw3ocyFwZ6OR5IExGcQ/wwdfShAqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt7C7+zg=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainTransfer",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423137,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECHuSXIs07aXp4Q/XxNDG57lOtObQOHlL0VJ2sjIx/2RDyrG/yyxAP/iPuR6h4JD3JWtMQ58ik2hTFqf3vOfOQAuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cC2Uhd"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423137,
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "signed_tx": "tx_+JALAfhCuECHuSXIs07aXp4Q/XxNDG57lOtObQOHlL0VJ2sjIx/2RDyrG/yyxAP/iPuR6h4JD3JWtMQ58ik2hTFqf3vOfOQAuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cC2Uhd",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainTransfer",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423136,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECHuSXIs07aXp4Q/XxNDG57lOtObQOHlL0VJ2sjIx/2RDyrG/yyxAP/iPuR6h4JD3JWtMQ58ik2hTFqf3vOfOQAuEDuwXvb+ZJ7jgZvNSqPE+fjq4JnyRQ8h9x72++FmRmFuOIeKNayIeZpdI1RCsDPPZ8xgxb5zI1CcA4acxmpsIYBuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7e5x7Qj"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423136,
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "state": "tx_+NILAfiEuECHuSXIs07aXp4Q/XxNDG57lOtObQOHlL0VJ2sjIx/2RDyrG/yyxAP/iPuR6h4JD3JWtMQ58ik2hTFqf3vOfOQAuEDuwXvb+ZJ7jgZvNSqPE+fjq4JnyRQ8h9x72++FmRmFuOIeKNayIeZpdI1RCsDPPZ8xgxb5zI1CcA4acxmpsIYBuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7e5x7Qj"
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "state": "tx_+NILAfiEuECHuSXIs07aXp4Q/XxNDG57lOtObQOHlL0VJ2sjIx/2RDyrG/yyxAP/iPuR6h4JD3JWtMQ58ik2hTFqf3vOfOQAuEDuwXvb+ZJ7jgZvNSqPE+fjq4JnyRQ8h9x72++FmRmFuOIeKNayIeZpdI1RCsDPPZ8xgxb5zI1CcA4acxmpsIYBuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7e5x7Qj"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423135,
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
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423135,
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
  "id": -576460752303423134,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423134,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECHuSXIs07aXp4Q/XxNDG57lOtObQOHlL0VJ2sjIx/2RDyrG/yyxAP/iPuR6h4JD3JWtMQ58ik2hTFqf3vOfOQAuEDuwXvb+ZJ7jgZvNSqPE+fjq4JnyRQ8h9x72++FmRmFuOIeKNayIeZpdI1RCsDPPZ8xgxb5zI1CcA4acxmpsIYBuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7e5x7Qj",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423133,
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
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423133,
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
        "meta": [
          "meta 1"
        ],
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
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvXwJiJ/s16obG8kx4Cw3ocyFwZ6OR5IExGcQ/wwdfShA6BoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdqa/HdI=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423132,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDZrMeYhRTlfB2hzZJtvcgPSC3dDomjoanNl6oy6MWfKwvumSfyVHNzgN1+dLr1B2Vpnyl7zBf9W0/rq3KUpmMDuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYRNH9M"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423132,
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDZrMeYhRTlfB2hzZJtvcgPSC3dDomjoanNl6oy6MWfKwvumSfyVHNzgN1+dLr1B2Vpnyl7zBf9W0/rq3KUpmMDuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYRNH9M",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423131,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDZfw+5Tdy5FJhVuHIgkDXZEgvC+PfLzEqJ/mXrYt5Q/goQ5vi4rxXNLdpnXlDnKsLbDwc2m2jJRivwAkRbPMMOuEDZrMeYhRTlfB2hzZJtvcgPSC3dDomjoanNl6oy6MWfKwvumSfyVHNzgN1+dLr1B2Vpnyl7zBf9W0/rq3KUpmMDuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZVCAna"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423131,
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "state": "tx_+NILAfiEuEDZfw+5Tdy5FJhVuHIgkDXZEgvC+PfLzEqJ/mXrYt5Q/goQ5vi4rxXNLdpnXlDnKsLbDwc2m2jJRivwAkRbPMMOuEDZrMeYhRTlfB2hzZJtvcgPSC3dDomjoanNl6oy6MWfKwvumSfyVHNzgN1+dLr1B2Vpnyl7zBf9W0/rq3KUpmMDuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZVCAna"
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "state": "tx_+NILAfiEuEDZfw+5Tdy5FJhVuHIgkDXZEgvC+PfLzEqJ/mXrYt5Q/goQ5vi4rxXNLdpnXlDnKsLbDwc2m2jJRivwAkRbPMMOuEDZrMeYhRTlfB2hzZJtvcgPSC3dDomjoanNl6oy6MWfKwvumSfyVHNzgN1+dLr1B2Vpnyl7zBf9W0/rq3KUpmMDuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZVCAna"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423130,
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
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423130,
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
  "id": -576460752303423129,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423129,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDZfw+5Tdy5FJhVuHIgkDXZEgvC+PfLzEqJ/mXrYt5Q/goQ5vi4rxXNLdpnXlDnKsLbDwc2m2jJRivwAkRbPMMOuEDZrMeYhRTlfB2hzZJtvcgPSC3dDomjoanNl6oy6MWfKwvumSfyVHNzgN1+dLr1B2Vpnyl7zBf9W0/rq3KUpmMDuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnZVCAna",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423128,
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
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423128,
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
        "meta": [
          "meta 1"
        ],
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
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvXwJiJ/s16obG8kx4Cw3ocyFwZ6OR5IExGcQ/wwdfShBKBFhwcy1nQ5Bi3OEygVd2MWxy1qnVtAG2qKlPJORZgUAkCjEto=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423127,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBJVfP1wvM8tvDBbTbZBSmh6A7saf7SOdMrrYvr0NsBt4Q4Un+9KTA3mkHyDtaxvkaSzs99cRjMQTQ8dMS02I4NuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKEsX0N"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423127,
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBJVfP1wvM8tvDBbTbZBSmh6A7saf7SOdMrrYvr0NsBt4Q4Un+9KTA3mkHyDtaxvkaSzs99cRjMQTQ8dMS02I4NuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAKEsX0N",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423126,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBJVfP1wvM8tvDBbTbZBSmh6A7saf7SOdMrrYvr0NsBt4Q4Un+9KTA3mkHyDtaxvkaSzs99cRjMQTQ8dMS02I4NuECocsHDnXWi+2Jb2YSd5lTjk+QervRoIxIBSBlEOV3DVtiVDmavnFWN41VJgwYIHavCbGwqbIq9bPeNjC43bvkMuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAJGC0ur"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423126,
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "state": "tx_+NILAfiEuEBJVfP1wvM8tvDBbTbZBSmh6A7saf7SOdMrrYvr0NsBt4Q4Un+9KTA3mkHyDtaxvkaSzs99cRjMQTQ8dMS02I4NuECocsHDnXWi+2Jb2YSd5lTjk+QervRoIxIBSBlEOV3DVtiVDmavnFWN41VJgwYIHavCbGwqbIq9bPeNjC43bvkMuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAJGC0ur"
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "state": "tx_+NILAfiEuEBJVfP1wvM8tvDBbTbZBSmh6A7saf7SOdMrrYvr0NsBt4Q4Un+9KTA3mkHyDtaxvkaSzs99cRjMQTQ8dMS02I4NuECocsHDnXWi+2Jb2YSd5lTjk+QervRoIxIBSBlEOV3DVtiVDmavnFWN41VJgwYIHavCbGwqbIq9bPeNjC43bvkMuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAJGC0ur"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423125,
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
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423125,
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
  "id": -576460752303423124,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423124,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBJVfP1wvM8tvDBbTbZBSmh6A7saf7SOdMrrYvr0NsBt4Q4Un+9KTA3mkHyDtaxvkaSzs99cRjMQTQ8dMS02I4NuECocsHDnXWi+2Jb2YSd5lTjk+QervRoIxIBSBlEOV3DVtiVDmavnFWN41VJgwYIHavCbGwqbIq9bPeNjC43bvkMuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQSgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAJGC0ur",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJgALDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAD60Cqy"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423123,
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
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423123,
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
        "meta": [
          "meta 1"
        ],
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
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvXwJiJ/s16obG8kx4Cw3ocyFwZ6OR5IExGcQ/wwdfShBaBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdmCo00Q=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainTransfer",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423122,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAgPhNoiFC25b4FL+goXOGRScbpXMzOTovzbUD3EaWGYnqSvcNEGUyvTzLJ6HdOxewodhwZisy+yuiYC08B++4JuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnY3R62z"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423122,
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAgPhNoiFC25b4FL+goXOGRScbpXMzOTovzbUD3EaWGYnqSvcNEGUyvTzLJ6HdOxewodhwZisy+yuiYC08B++4JuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnY3R62z",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainTransfer",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423121,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAgPhNoiFC25b4FL+goXOGRScbpXMzOTovzbUD3EaWGYnqSvcNEGUyvTzLJ6HdOxewodhwZisy+yuiYC08B++4JuECMtSAWn5zyB0ZHV0eG+vcLz7fAyq5zGKUP1Gy6+OiYN8mMCpfwpkrDYKtT3XQ8uG33KdkWyWj2Cxb2pwqkVIoOuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaC8qd1"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423121,
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "state": "tx_+NILAfiEuEAgPhNoiFC25b4FL+goXOGRScbpXMzOTovzbUD3EaWGYnqSvcNEGUyvTzLJ6HdOxewodhwZisy+yuiYC08B++4JuECMtSAWn5zyB0ZHV0eG+vcLz7fAyq5zGKUP1Gy6+OiYN8mMCpfwpkrDYKtT3XQ8uG33KdkWyWj2Cxb2pwqkVIoOuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaC8qd1"
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "state": "tx_+NILAfiEuEAgPhNoiFC25b4FL+goXOGRScbpXMzOTovzbUD3EaWGYnqSvcNEGUyvTzLJ6HdOxewodhwZisy+yuiYC08B++4JuECMtSAWn5zyB0ZHV0eG+vcLz7fAyq5zGKUP1Gy6+OiYN8mMCpfwpkrDYKtT3XQ8uG33KdkWyWj2Cxb2pwqkVIoOuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaC8qd1"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423120,
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
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423120,
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
  "id": -576460752303423119,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423119,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAgPhNoiFC25b4FL+goXOGRScbpXMzOTovzbUD3EaWGYnqSvcNEGUyvTzLJ6HdOxewodhwZisy+yuiYC08B++4JuECMtSAWn5zyB0ZHV0eG+vcLz7fAyq5zGKUP1Gy6+OiYN8mMCpfwpkrDYKtT3XQ8uG33KdkWyWj2Cxb2pwqkVIoOuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaC8qd1",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423118,
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
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423118,
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
        "meta": [
          "meta 1"
        ],
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
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
        "meta": [
          "meta 1"
        ],
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
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvXwJiJ/s16obG8kx4Cw3ocyFwZ6OR5IExGcQ/wwdfShBqBFhwcy1nQ5Bi3OEygVd2MWxy1qnVtAG2qKlPJORZgUAs7w58k=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423117,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEArGLDUBshMnwtS+hIASv3VNpc+b4TJUHaMvUwRcoA96ukIGUbcQldBPkd4BlrdbosoBAl1upHqiG90I2puel0DuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFALfeD11"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423117,
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "signed_tx": "tx_+JALAfhCuEArGLDUBshMnwtS+hIASv3VNpc+b4TJUHaMvUwRcoA96ukIGUbcQldBPkd4BlrdbosoBAl1upHqiG90I2puel0DuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFALfeD11",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423116,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEArGLDUBshMnwtS+hIASv3VNpc+b4TJUHaMvUwRcoA96ukIGUbcQldBPkd4BlrdbosoBAl1upHqiG90I2puel0DuEDwnBpr32QjxqUCwcc13rHBOn0jJGfjDgsHs6a482W+0TuFT8LCuGsZ78qzq8pcP20Jc1DeUAysuKhQonUXOY0NuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAL0ZtnT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423116,
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "state": "tx_+NILAfiEuEArGLDUBshMnwtS+hIASv3VNpc+b4TJUHaMvUwRcoA96ukIGUbcQldBPkd4BlrdbosoBAl1upHqiG90I2puel0DuEDwnBpr32QjxqUCwcc13rHBOn0jJGfjDgsHs6a482W+0TuFT8LCuGsZ78qzq8pcP20Jc1DeUAysuKhQonUXOY0NuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAL0ZtnT"
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "state": "tx_+NILAfiEuEArGLDUBshMnwtS+hIASv3VNpc+b4TJUHaMvUwRcoA96ukIGUbcQldBPkd4BlrdbosoBAl1upHqiG90I2puel0DuEDwnBpr32QjxqUCwcc13rHBOn0jJGfjDgsHs6a482W+0TuFT8LCuGsZ78qzq8pcP20Jc1DeUAysuKhQonUXOY0NuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAL0ZtnT"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423115,
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
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423115,
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
  "id": -576460752303423114,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423114,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEArGLDUBshMnwtS+hIASv3VNpc+b4TJUHaMvUwRcoA96ukIGUbcQldBPkd4BlrdbosoBAl1upHqiG90I2puel0DuEDwnBpr32QjxqUCwcc13rHBOn0jJGfjDgsHs6a482W+0TuFT8LCuGsZ78qzq8pcP20Jc1DeUAysuKhQonUXOY0NuEj4RjkCoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oQagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAL0ZtnT",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJgALDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAD60Cqy"
  },
  "version": 1
}
```
