
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
      "fsm_id": "ba_Qay6xidY5UTDF7KpKIGrNaqQW28+wToMWvwhtNIggprOy7yD"
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
      "fsm_id": "ba_5ao56cVPdoNx9JACGqyXeXSq+Hzf2LRoXhy0XTmlsi9g1Slt"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnY8MRwmzA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422877,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECjzGnCLgZ9UShydb1i0lPeO8pnGOapQEtJxuPUsAXgTo8v8l1q9zcu0ZOFFKeLVZTPqEO212P/fRPNLS7mP6UAuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2PFCguGA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422877,
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
      "signed_tx": "tx_+MsLAfhCuECjzGnCLgZ9UShydb1i0lPeO8pnGOapQEtJxuPUsAXgTo8v8l1q9zcu0ZOFFKeLVZTPqEO212P/fRPNLS7mP6UAuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2PFCguGA=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422876,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAIETbpE1Hea97ndkcL939pYwq1Qb+wexPmYDmitQHCCWORv4a7J4zX+CW8tJhb8gGcJEFlB9IUIxlwN3qxtB0BbhAo8xpwi4GfVEocnW9YtJT3jvKZxjmqUBLScbj1LAF4E6PL/Jdavc3LtGThRSni1WUz6hDttdj/30TzS0u5j+lALiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjwkwX7+"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422876,
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAIETbpE1Hea97ndkcL939pYwq1Qb+wexPmYDmitQHCCWORv4a7J4zX+CW8tJhb8gGcJEFlB9IUIxlwN3qxtB0BbhAo8xpwi4GfVEocnW9YtJT3jvKZxjmqUBLScbj1LAF4E6PL/Jdavc3LtGThRSni1WUz6hDttdj/30TzS0u5j+lALiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjwkwX7+",
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAIETbpE1Hea97ndkcL939pYwq1Qb+wexPmYDmitQHCCWORv4a7J4zX+CW8tJhb8gGcJEFlB9IUIxlwN3qxtB0BbhAo8xpwi4GfVEocnW9YtJT3jvKZxjmqUBLScbj1LAF4E6PL/Jdavc3LtGThRSni1WUz6hDttdj/30TzS0u5j+lALiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjwkwX7+",
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAIETbpE1Hea97ndkcL939pYwq1Qb+wexPmYDmitQHCCWORv4a7J4zX+CW8tJhb8gGcJEFlB9IUIxlwN3qxtB0BbhAo8xpwi4GfVEocnW9YtJT3jvKZxjmqUBLScbj1LAF4E6PL/Jdavc3LtGThRSni1WUz6hDttdj/30TzS0u5j+lALiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjwkwX7+",
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAIETbpE1Hea97ndkcL939pYwq1Qb+wexPmYDmitQHCCWORv4a7J4zX+CW8tJhb8gGcJEFlB9IUIxlwN3qxtB0BbhAo8xpwi4GfVEocnW9YtJT3jvKZxjmqUBLScbj1LAF4E6PL/Jdavc3LtGThRSni1WUz6hDttdj/30TzS0u5j+lALiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjwkwX7+",
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
    "data": {
      "message": {
        "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
    "data": {
      "message": {
        "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
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
  "id": -576460752303422875,
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
  "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
  "id": -576460752303422875,
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
    "data": {
      "state": "tx_+QENCwH4hLhAIETbpE1Hea97ndkcL939pYwq1Qb+wexPmYDmitQHCCWORv4a7J4zX+CW8tJhb8gGcJEFlB9IUIxlwN3qxtB0BbhAo8xpwi4GfVEocnW9YtJT3jvKZxjmqUBLScbj1LAF4E6PL/Jdavc3LtGThRSni1WUz6hDttdj/30TzS0u5j+lALiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjwkwX7+"
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
    "data": {
      "state": "tx_+QENCwH4hLhAIETbpE1Hea97ndkcL939pYwq1Qb+wexPmYDmitQHCCWORv4a7J4zX+CW8tJhb8gGcJEFlB9IUIxlwN3qxtB0BbhAo8xpwi4GfVEocnW9YtJT3jvKZxjmqUBLScbj1LAF4E6PL/Jdavc3LtGThRSni1WUz6hDttdj/30TzS0u5j+lALiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjwkwX7+"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422874,
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
  "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
  "id": -576460752303422874,
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkboEEoJN9lAIvQ4VLbnSH5k8UoWUdUk+EzVENgDFnaSAqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt+aAEeU=",
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
  "id": -576460752303422873,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBHNePriPQIqgIiM8iPZC9mymQGdRFTRnHQc1glF44cLeVrhjV4N5j8HEQvihMDnYioRHje2oOuIn5Z695y044MuEj4RjkCoQZG6BBKCTfZQCL0OFS250h+ZPFKFlHVJPhM1RDYAxZ2kgKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dUQbdR"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
  "id": -576460752303422873,
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBHNePriPQIqgIiM8iPZC9mymQGdRFTRnHQc1glF44cLeVrhjV4N5j8HEQvihMDnYioRHje2oOuIn5Z695y044MuEj4RjkCoQZG6BBKCTfZQCL0OFS250h+ZPFKFlHVJPhM1RDYAxZ2kgKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dUQbdR",
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
  "id": -576460752303422872,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBHNePriPQIqgIiM8iPZC9mymQGdRFTRnHQc1glF44cLeVrhjV4N5j8HEQvihMDnYioRHje2oOuIn5Z695y044MuEDkh6/WadgwjSdjEvzQ+YXYQ1bewnqjPqdsFuskGBWl5tSHpyEXsLC44HRHwJyJ+MOFqRV30nzdzk9VvZO0nRYIuEj4RjkCoQZG6BBKCTfZQCL0OFS250h+ZPFKFlHVJPhM1RDYAxZ2kgKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fTnuIY"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
  "id": -576460752303422872,
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
    "data": {
      "state": "tx_+NILAfiEuEBHNePriPQIqgIiM8iPZC9mymQGdRFTRnHQc1glF44cLeVrhjV4N5j8HEQvihMDnYioRHje2oOuIn5Z695y044MuEDkh6/WadgwjSdjEvzQ+YXYQ1bewnqjPqdsFuskGBWl5tSHpyEXsLC44HRHwJyJ+MOFqRV30nzdzk9VvZO0nRYIuEj4RjkCoQZG6BBKCTfZQCL0OFS250h+ZPFKFlHVJPhM1RDYAxZ2kgKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fTnuIY"
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
    "data": {
      "state": "tx_+NILAfiEuEBHNePriPQIqgIiM8iPZC9mymQGdRFTRnHQc1glF44cLeVrhjV4N5j8HEQvihMDnYioRHje2oOuIn5Z695y044MuEDkh6/WadgwjSdjEvzQ+YXYQ1bewnqjPqdsFuskGBWl5tSHpyEXsLC44HRHwJyJ+MOFqRV30nzdzk9VvZO0nRYIuEj4RjkCoQZG6BBKCTfZQCL0OFS250h+ZPFKFlHVJPhM1RDYAxZ2kgKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fTnuIY"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422871,
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
  "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
  "id": -576460752303422871,
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
  "id": -576460752303422870,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
  "id": -576460752303422870,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBHNePriPQIqgIiM8iPZC9mymQGdRFTRnHQc1glF44cLeVrhjV4N5j8HEQvihMDnYioRHje2oOuIn5Z695y044MuEDkh6/WadgwjSdjEvzQ+YXYQ1bewnqjPqdsFuskGBWl5tSHpyEXsLC44HRHwJyJ+MOFqRV30nzdzk9VvZO0nRYIuEj4RjkCoQZG6BBKCTfZQCL0OFS250h+ZPFKFlHVJPhM1RDYAxZ2kgKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fTnuIY",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422869,
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
  "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
  "id": -576460752303422869,
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkboEEoJN9lAIvQ4VLbnSH5k8UoWUdUk+EzVENgDFnaSA6BoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdrVC+6k=",
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
  "id": -576460752303422868,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBwr3h/C3VnOnNrNPJU2ZKIUeDLz9oZ8XMXi+wzD7+ilwCr3X/6ceq9TI9SdFslRwdBm4yL7igM0g6e0fL1WZ0KuEj4RjkCoQZG6BBKCTfZQCL0OFS250h+ZPFKFlHVJPhM1RDYAxZ2kgOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wna26WiA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
  "id": -576460752303422868,
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBwr3h/C3VnOnNrNPJU2ZKIUeDLz9oZ8XMXi+wzD7+ilwCr3X/6ceq9TI9SdFslRwdBm4yL7igM0g6e0fL1WZ0KuEj4RjkCoQZG6BBKCTfZQCL0OFS250h+ZPFKFlHVJPhM1RDYAxZ2kgOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wna26WiA",
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
  "id": -576460752303422867,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBwr3h/C3VnOnNrNPJU2ZKIUeDLz9oZ8XMXi+wzD7+ilwCr3X/6ceq9TI9SdFslRwdBm4yL7igM0g6e0fL1WZ0KuEC+RmXFpNDlhxVtOtNE6NiwtTQNQTiKezcWV7kBMFjhbLYJQ8vksEV6KFID/vt9X5CpHHZrgIdFVsuwJRUZ9kcBuEj4RjkCoQZG6BBKCTfZQCL0OFS250h+ZPFKFlHVJPhM1RDYAxZ2kgOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbNJlNC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
  "id": -576460752303422867,
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
    "data": {
      "state": "tx_+NILAfiEuEBwr3h/C3VnOnNrNPJU2ZKIUeDLz9oZ8XMXi+wzD7+ilwCr3X/6ceq9TI9SdFslRwdBm4yL7igM0g6e0fL1WZ0KuEC+RmXFpNDlhxVtOtNE6NiwtTQNQTiKezcWV7kBMFjhbLYJQ8vksEV6KFID/vt9X5CpHHZrgIdFVsuwJRUZ9kcBuEj4RjkCoQZG6BBKCTfZQCL0OFS250h+ZPFKFlHVJPhM1RDYAxZ2kgOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbNJlNC"
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
    "data": {
      "state": "tx_+NILAfiEuEBwr3h/C3VnOnNrNPJU2ZKIUeDLz9oZ8XMXi+wzD7+ilwCr3X/6ceq9TI9SdFslRwdBm4yL7igM0g6e0fL1WZ0KuEC+RmXFpNDlhxVtOtNE6NiwtTQNQTiKezcWV7kBMFjhbLYJQ8vksEV6KFID/vt9X5CpHHZrgIdFVsuwJRUZ9kcBuEj4RjkCoQZG6BBKCTfZQCL0OFS250h+ZPFKFlHVJPhM1RDYAxZ2kgOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbNJlNC"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422866,
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
  "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
  "id": -576460752303422866,
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
  "id": -576460752303422865,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
  "id": -576460752303422865,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBwr3h/C3VnOnNrNPJU2ZKIUeDLz9oZ8XMXi+wzD7+ilwCr3X/6ceq9TI9SdFslRwdBm4yL7igM0g6e0fL1WZ0KuEC+RmXFpNDlhxVtOtNE6NiwtTQNQTiKezcWV7kBMFjhbLYJQ8vksEV6KFID/vt9X5CpHHZrgIdFVsuwJRUZ9kcBuEj4RjkCoQZG6BBKCTfZQCL0OFS250h+ZPFKFlHVJPhM1RDYAxZ2kgOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbNJlNC",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBkboEEoJN9lAIvQ4VLbnSH5k8UoWUdUk+EzVENgDFnaSoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FbjU+NILAfiEuEBwr3h/C3VnOnNrNPJU2ZKIUeDLz9oZ8XMXi+wzD7+ilwCr3X/6ceq9TI9SdFslRwdBm4yL7igM0g6e0fL1WZ0KuEC+RmXFpNDlhxVtOtNE6NiwtTQNQTiKezcWV7kBMFjhbLYJQ8vksEV6KFID/vt9X5CpHHZrgIdFVsuwJRUZ9kcBuEj4RjkCoQZG6BBKCTfZQCL0OFS250h+ZPFKFlHVJPhM1RDYAxZ2kgOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYAhhMG0SswAD2n0O9p",
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
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
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBkboEEoJN9lAIvQ4VLbnSH5k8UoWUdUk+EzVENgDFnaSoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv7jU+NILAfiEuEBwr3h/C3VnOnNrNPJU2ZKIUeDLz9oZ8XMXi+wzD7+ilwCr3X/6ceq9TI9SdFslRwdBm4yL7igM0g6e0fL1WZ0KuEC+RmXFpNDlhxVtOtNE6NiwtTQNQTiKezcWV7kBMFjhbLYJQ8vksEV6KFID/vt9X5CpHHZrgIdFVsuwJRUZ9kcBuEj4RjkCoQZG6BBKCTfZQCL0OFS250h+ZPFKFlHVJPhM1RDYAxZ2kgOgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYAhhMG0SswABervzTz",
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
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
  "id": -576460752303422864,
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
  "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
  "id": -576460752303422864,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422863,
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
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
    "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
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
  "channel_id": "ch_YEDFwmXt4iT3Qhw2i1Xd9NkwqGxhong6ELJZP4J1bK3WUfyHV",
  "id": -576460752303422863,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```
