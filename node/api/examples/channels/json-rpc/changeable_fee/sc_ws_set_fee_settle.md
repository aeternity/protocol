
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
      "fsm_id": "ba_7Gvv/Iz9q/3PHOTt+futtLgb/7R/HHMV1IhJB2kIpPFSPBdu"
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
      "fsm_id": "ba_fX1NUvEUTo00rSll866xk/NciyuQQn4RWChjXChx28L6Rlzw"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnY0LIXhgQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422901,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECHtmpXAOGermuvjQAStgCC8IiOriqWk0ZBSgZ9KXiTVWFsUkK8lKkOeP6EU23t/EkFQRICvENozKWJ5Wx7UM0PuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2NLIptcc="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422901,
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
      "signed_tx": "tx_+MsLAfhCuECHtmpXAOGermuvjQAStgCC8IiOriqWk0ZBSgZ9KXiTVWFsUkK8lKkOeP6EU23t/EkFQRICvENozKWJ5Wx7UM0PuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2NLIptcc=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422900,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhASgwCkStu35lEM9Mf0RJQkwZCIkO6UR3uubXU1KUktig6siA7A1Pafvg4qhLHwkE85n8Tq7HIAsvLo5YT9eQ+BrhAh7ZqVwDhnq5rr40AErYAgvCIjq4qlpNGQUoGfSl4k1VhbFJCvJSpDnj+hFNt7fxJBUESArxDaMylieVse1DND7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjQNDY3K"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422900,
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
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhASgwCkStu35lEM9Mf0RJQkwZCIkO6UR3uubXU1KUktig6siA7A1Pafvg4qhLHwkE85n8Tq7HIAsvLo5YT9eQ+BrhAh7ZqVwDhnq5rr40AErYAgvCIjq4qlpNGQUoGfSl4k1VhbFJCvJSpDnj+hFNt7fxJBUESArxDaMylieVse1DND7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjQNDY3K",
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
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhASgwCkStu35lEM9Mf0RJQkwZCIkO6UR3uubXU1KUktig6siA7A1Pafvg4qhLHwkE85n8Tq7HIAsvLo5YT9eQ+BrhAh7ZqVwDhnq5rr40AErYAgvCIjq4qlpNGQUoGfSl4k1VhbFJCvJSpDnj+hFNt7fxJBUESArxDaMylieVse1DND7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjQNDY3K",
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
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhASgwCkStu35lEM9Mf0RJQkwZCIkO6UR3uubXU1KUktig6siA7A1Pafvg4qhLHwkE85n8Tq7HIAsvLo5YT9eQ+BrhAh7ZqVwDhnq5rr40AErYAgvCIjq4qlpNGQUoGfSl4k1VhbFJCvJSpDnj+hFNt7fxJBUESArxDaMylieVse1DND7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjQNDY3K",
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
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhASgwCkStu35lEM9Mf0RJQkwZCIkO6UR3uubXU1KUktig6siA7A1Pafvg4qhLHwkE85n8Tq7HIAsvLo5YT9eQ+BrhAh7ZqVwDhnq5rr40AErYAgvCIjq4qlpNGQUoGfSl4k1VhbFJCvJSpDnj+hFNt7fxJBUESArxDaMylieVse1DND7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjQNDY3K",
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
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
    "data": {
      "message": {
        "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
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
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
    "data": {
      "message": {
        "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
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
  "id": -576460752303422899,
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
  "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
  "id": -576460752303422899,
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
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
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
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
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
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
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
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
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

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
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
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
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
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
    "data": {
      "state": "tx_+QENCwH4hLhASgwCkStu35lEM9Mf0RJQkwZCIkO6UR3uubXU1KUktig6siA7A1Pafvg4qhLHwkE85n8Tq7HIAsvLo5YT9eQ+BrhAh7ZqVwDhnq5rr40AErYAgvCIjq4qlpNGQUoGfSl4k1VhbFJCvJSpDnj+hFNt7fxJBUESArxDaMylieVse1DND7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjQNDY3K"
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
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
    "data": {
      "state": "tx_+QENCwH4hLhASgwCkStu35lEM9Mf0RJQkwZCIkO6UR3uubXU1KUktig6siA7A1Pafvg4qhLHwkE85n8Tq7HIAsvLo5YT9eQ+BrhAh7ZqVwDhnq5rr40AErYAgvCIjq4qlpNGQUoGfSl4k1VhbFJCvJSpDnj+hFNt7fxJBUESArxDaMylieVse1DND7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjQNDY3K"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBtfz6pcsPrpvYBBYGCe34YlI/8kFefhedQORL1Ytqo9soQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYC5AUz5AUk8AfkBP/kBPKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvkBGPh0oCiW0e4qVvD/C94E6/En+1vvEgzoctloLayg1hD1Tl5u+FGAgICAgICg46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVuAgICAoKcJtie4oQxB6+5JVy+F3eNaNF7V7TgRPXFlQNJ4W/wIgICAgID4T6CnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CO2gP/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWLygoBAIY/qiUiX//4T6DjooHlLkRUA0QFUOns+/GhHcvejx4IPZN7Jd7GGFRtW+2gNllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAHAwMDAwACGFT7sgIAANSyybz8=",
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
  "method": "channels.close_solo_sign",
  "params": {
    "signed_tx": "tx_+QHrCwH4QrhAazjdYrj9avNt69ot40FCelFE9vAEvZg8jCd17j3BiAz3JM3ri+zAch9IcUV/2yvlaNAGJ0iSUO6DAN8xWNwLBrkBovkBnzYBoQbX8+qXLD66b2AQWBgnt+GJSP/JBXn4XnUDkS9WLaqPbKEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWAuQFM+QFJPAH5AT/5ATygKJbR7ipW8P8L3gTr8Sf7W+8SDOhy2WgtrKDWEPVOXm75ARj4dKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvhRgICAgICAoOOigeUuRFQDRAVQ6ez78aEdy96PHgg9k3sl3sYYVG1bgICAgKCnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CICAgICA+E+gpwm2J7ihDEHr7klXL4Xd41o0XtXtOBE9cWVA0nhb/AjtoD/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVi8oKAQCGP6olIl//+E+g46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVvtoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAADXVv4vY"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAazjdYrj9avNt69ot40FCelFE9vAEvZg8jCd17j3BiAz3JM3ri+zAch9IcUV/2yvlaNAGJ0iSUO6DAN8xWNwLBrkBovkBnzYBoQbX8+qXLD66b2AQWBgnt+GJSP/JBXn4XnUDkS9WLaqPbKEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWAuQFM+QFJPAH5AT/5ATygKJbR7ipW8P8L3gTr8Sf7W+8SDOhy2WgtrKDWEPVOXm75ARj4dKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvhRgICAgICAoOOigeUuRFQDRAVQ6ez78aEdy96PHgg9k3sl3sYYVG1bgICAgKCnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CICAgICA+E+gpwm2J7ihDEHr7klXL4Xd41o0XtXtOBE9cWVA0nhb/AjtoD/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVi8oKAQCGP6olIl//+E+g46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVvtoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAADXVv4vY",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
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
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAazjdYrj9avNt69ot40FCelFE9vAEvZg8jCd17j3BiAz3JM3ri+zAch9IcUV/2yvlaNAGJ0iSUO6DAN8xWNwLBrkBovkBnzYBoQbX8+qXLD66b2AQWBgnt+GJSP/JBXn4XnUDkS9WLaqPbKEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWAuQFM+QFJPAH5AT/5ATygKJbR7ipW8P8L3gTr8Sf7W+8SDOhy2WgtrKDWEPVOXm75ARj4dKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvhRgICAgICAoOOigeUuRFQDRAVQ6ez78aEdy96PHgg9k3sl3sYYVG1bgICAgKCnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CICAgICA+E+gpwm2J7ihDEHr7klXL4Xd41o0XtXtOBE9cWVA0nhb/AjtoD/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVi8oKAQCGP6olIl//+E+g46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVvtoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAADXVv4vY",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
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
  "method": "channels.settle",
  "params": {
    "fee": 123456789876543
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBtfz6pcsPrpvYBBYGCe34YlI/8kFefhedQORL1Ytqo9soQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4Y/qiUiX/+GJGE5yoABAIZwSIYbDz8W//3g8Q==",
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
  "method": "channels.settle_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEBQp5G8lerUgxjvc8qdsc5vRkIVqa/BWSWULfdr4tgDnJQ4kGTekDNA8BiLDJjVR12FU5g+5qp1NMhDTnQsMLECuF/4XTgBoQbX8+qXLD66b2AQWBgnt+GJSP/JBXn4XnUDkS9WLaqPbKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl//hiRhOcqAAQCGcEiGGw8/FkSek2c="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBQp5G8lerUgxjvc8qdsc5vRkIVqa/BWSWULfdr4tgDnJQ4kGTekDNA8BiLDJjVR12FU5g+5qp1NMhDTnQsMLECuF/4XTgBoQbX8+qXLD66b2AQWBgnt+GJSP/JBXn4XnUDkS9WLaqPbKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl//hiRhOcqAAQCGcEiGGw8/FkSek2c=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBQp5G8lerUgxjvc8qdsc5vRkIVqa/BWSWULfdr4tgDnJQ4kGTekDNA8BiLDJjVR12FU5g+5qp1NMhDTnQsMLECuF/4XTgBoQbX8+qXLD66b2AQWBgnt+GJSP/JBXn4XnUDkS9WLaqPbKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl//hiRhOcqAAQCGcEiGGw8/FkSek2c=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
    "data": {
      "event": "closed_confirmed"
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
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
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
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
    "data": {
      "event": "closed_confirmed"
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
    "channel_id": "ch_2e7E1ruTLJgwCvo6nJ6xscwxrqLhHNqrv576k7SagMijsX66jZ",
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
      "fsm_id": "ba_sYN56DAdU5VDl0kTM9IOwpjXPmbpMr0IUTqzpxA/Z16G5vRA"
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
      "fsm_id": "ba_81NpA9w14RqG/2O/R+m2wa7Nw0W6TjU3K2dv2T7khUGsByMb"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnY28V7T5w==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422898,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEB1aPn/yeMA6khehk34k/G8x2/lvGVvFmI/Ohw89fp3HRKVAgEaLHuexaq7t48uQGFWEVvjXKepYSlIN9OVmyoMuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2NlBao4s="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422898,
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
      "signed_tx": "tx_+MsLAfhCuEB1aPn/yeMA6khehk34k/G8x2/lvGVvFmI/Ohw89fp3HRKVAgEaLHuexaq7t48uQGFWEVvjXKepYSlIN9OVmyoMuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2NlBao4s=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422897,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAL9dTf+2nzjkXNdkTdPlS0u/ol8UhXs/ZQh/ObkTbaUZh/YvQdZMVpC2LhKsKh0gWYFceG22qmdo/uVQfwkwcB7hAdWj5/8njAOpIXoZN+JPxvMdv5bxlbxZiPzocPPX6dx0SlQIBGix7nsWqu7ePLkBhVhFb41ynqWEpSDfTlZsqDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjaFzop/"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422897,
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
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAL9dTf+2nzjkXNdkTdPlS0u/ol8UhXs/ZQh/ObkTbaUZh/YvQdZMVpC2LhKsKh0gWYFceG22qmdo/uVQfwkwcB7hAdWj5/8njAOpIXoZN+JPxvMdv5bxlbxZiPzocPPX6dx0SlQIBGix7nsWqu7ePLkBhVhFb41ynqWEpSDfTlZsqDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjaFzop/",
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
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAL9dTf+2nzjkXNdkTdPlS0u/ol8UhXs/ZQh/ObkTbaUZh/YvQdZMVpC2LhKsKh0gWYFceG22qmdo/uVQfwkwcB7hAdWj5/8njAOpIXoZN+JPxvMdv5bxlbxZiPzocPPX6dx0SlQIBGix7nsWqu7ePLkBhVhFb41ynqWEpSDfTlZsqDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjaFzop/",
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
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAL9dTf+2nzjkXNdkTdPlS0u/ol8UhXs/ZQh/ObkTbaUZh/YvQdZMVpC2LhKsKh0gWYFceG22qmdo/uVQfwkwcB7hAdWj5/8njAOpIXoZN+JPxvMdv5bxlbxZiPzocPPX6dx0SlQIBGix7nsWqu7ePLkBhVhFb41ynqWEpSDfTlZsqDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjaFzop/",
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
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAL9dTf+2nzjkXNdkTdPlS0u/ol8UhXs/ZQh/ObkTbaUZh/YvQdZMVpC2LhKsKh0gWYFceG22qmdo/uVQfwkwcB7hAdWj5/8njAOpIXoZN+JPxvMdv5bxlbxZiPzocPPX6dx0SlQIBGix7nsWqu7ePLkBhVhFb41ynqWEpSDfTlZsqDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjaFzop/",
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
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
    "data": {
      "message": {
        "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
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
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
    "data": {
      "message": {
        "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
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
  "id": -576460752303422896,
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
  "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
  "id": -576460752303422896,
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
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
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
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
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
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
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
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
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
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
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
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
    "data": {
      "state": "tx_+QENCwH4hLhAL9dTf+2nzjkXNdkTdPlS0u/ol8UhXs/ZQh/ObkTbaUZh/YvQdZMVpC2LhKsKh0gWYFceG22qmdo/uVQfwkwcB7hAdWj5/8njAOpIXoZN+JPxvMdv5bxlbxZiPzocPPX6dx0SlQIBGix7nsWqu7ePLkBhVhFb41ynqWEpSDfTlZsqDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjaFzop/"
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
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
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
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
    "data": {
      "state": "tx_+QENCwH4hLhAL9dTf+2nzjkXNdkTdPlS0u/ol8UhXs/ZQh/ObkTbaUZh/YvQdZMVpC2LhKsKh0gWYFceG22qmdo/uVQfwkwcB7hAdWj5/8njAOpIXoZN+JPxvMdv5bxlbxZiPzocPPX6dx0SlQIBGix7nsWqu7ePLkBhVhFb41ynqWEpSDfTlZsqDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjaFzop/"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBqmZS8QhT5UaiMWi54IkYryNxE93ylUef4zK2/jTkrmWoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYC5AUz5AUk8AfkBP/kBPKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvkBGPh0oCiW0e4qVvD/C94E6/En+1vvEgzoctloLayg1hD1Tl5u+FGAgICAgICg46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVuAgICAoKcJtie4oQxB6+5JVy+F3eNaNF7V7TgRPXFlQNJ4W/wIgICAgID4T6CnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CO2gP/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWLygoBAIY/qiUiX//4T6DjooHlLkRUA0QFUOns+/GhHcvejx4IPZN7Jd7GGFRtW+2gNllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAHAwMDAwACGFT7sgIAAN8AMSG4=",
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
  "method": "channels.close_solo_sign",
  "params": {
    "signed_tx": "tx_+QHrCwH4QrhAcDvfdYxvXx/U9Reg15sqbT54kZnG7Rm8r1Zju312qHOJYE6H5n9TzYle6xLGcd4NqkWnKyLbzP183T8peIBxB7kBovkBnzYBoQapmUvEIU+VGojFoueCJGK8jcRPd8pVHn+Mytv405K5lqEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWAuQFM+QFJPAH5AT/5ATygKJbR7ipW8P8L3gTr8Sf7W+8SDOhy2WgtrKDWEPVOXm75ARj4dKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvhRgICAgICAoOOigeUuRFQDRAVQ6ez78aEdy96PHgg9k3sl3sYYVG1bgICAgKCnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CICAgICA+E+gpwm2J7ihDEHr7klXL4Xd41o0XtXtOBE9cWVA0nhb/AjtoD/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVi8oKAQCGP6olIl//+E+g46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVvtoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAADcoOsOP"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAcDvfdYxvXx/U9Reg15sqbT54kZnG7Rm8r1Zju312qHOJYE6H5n9TzYle6xLGcd4NqkWnKyLbzP183T8peIBxB7kBovkBnzYBoQapmUvEIU+VGojFoueCJGK8jcRPd8pVHn+Mytv405K5lqEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWAuQFM+QFJPAH5AT/5ATygKJbR7ipW8P8L3gTr8Sf7W+8SDOhy2WgtrKDWEPVOXm75ARj4dKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvhRgICAgICAoOOigeUuRFQDRAVQ6ez78aEdy96PHgg9k3sl3sYYVG1bgICAgKCnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CICAgICA+E+gpwm2J7ihDEHr7klXL4Xd41o0XtXtOBE9cWVA0nhb/AjtoD/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVi8oKAQCGP6olIl//+E+g46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVvtoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAADcoOsOP",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
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
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAcDvfdYxvXx/U9Reg15sqbT54kZnG7Rm8r1Zju312qHOJYE6H5n9TzYle6xLGcd4NqkWnKyLbzP183T8peIBxB7kBovkBnzYBoQapmUvEIU+VGojFoueCJGK8jcRPd8pVHn+Mytv405K5lqEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWAuQFM+QFJPAH5AT/5ATygKJbR7ipW8P8L3gTr8Sf7W+8SDOhy2WgtrKDWEPVOXm75ARj4dKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvhRgICAgICAoOOigeUuRFQDRAVQ6ez78aEdy96PHgg9k3sl3sYYVG1bgICAgKCnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CICAgICA+E+gpwm2J7ihDEHr7klXL4Xd41o0XtXtOBE9cWVA0nhb/AjtoD/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVi8oKAQCGP6olIl//+E+g46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVvtoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAADcoOsOP",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
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
  "method": "channels.settle",
  "params": {
    "fee": 123456789876543
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBqmZS8QhT5UaiMWi54IkYryNxE93ylUef4zK2/jTkrmWoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiX/+GJGE5yoABAIZwSIYbDz84bJgpVA==",
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
  "method": "channels.settle_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEBawEXu2LFVRQXGEakj2tBEOdE2mCKSMowM44JrQMVIcX60ybKZbaHi81/jJMv2FwPThsfDCAAlqvGIwhW18bEDuF/4XTgBoQapmUvEIU+VGojFoueCJGK8jcRPd8pVHn+Mytv405K5lqEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olIl//hiRhOcqAAQCGcEiGGw8/OBzrphQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBawEXu2LFVRQXGEakj2tBEOdE2mCKSMowM44JrQMVIcX60ybKZbaHi81/jJMv2FwPThsfDCAAlqvGIwhW18bEDuF/4XTgBoQapmUvEIU+VGojFoueCJGK8jcRPd8pVHn+Mytv405K5lqEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olIl//hiRhOcqAAQCGcEiGGw8/OBzrphQ=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBawEXu2LFVRQXGEakj2tBEOdE2mCKSMowM44JrQMVIcX60ybKZbaHi81/jJMv2FwPThsfDCAAlqvGIwhW18bEDuF/4XTgBoQapmUvEIU+VGojFoueCJGK8jcRPd8pVHn+Mytv405K5lqEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olIl//hiRhOcqAAQCGcEiGGw8/OBzrphQ=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
    "data": {
      "event": "closed_confirmed"
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
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
    "data": {
      "event": "closed_confirmed"
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
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
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
    "channel_id": "ch_2HhB6TUGsJEwEMQ5VsrckZQowsabYuKVtogAnSV3bTEToT5FPW",
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
