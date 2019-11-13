
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
      "fsm_id": "ba_zDhcg6NNJMLToL5m6ksDOiXW4sLdZ4jRorBhOBJh91Ou1g1f"
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
      "fsm_id": "ba_qMGpLL5L0pHDafrSZZU6VJOGvojW1e9Nx/+/Gcw2busS7XPh"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYsM11aIw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422925,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDAKFnDWQ/ie3LoC2FYA0wFNvYYSBfNKnJsvZEIlmqVy48dIQ4aXH7MQAFbCPgduIVmv74Rt+qUKBXUEmTgM08EuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2LEiUe/4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422925,
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
      "signed_tx": "tx_+MsLAfhCuEDAKFnDWQ/ie3LoC2FYA0wFNvYYSBfNKnJsvZEIlmqVy48dIQ4aXH7MQAFbCPgduIVmv74Rt+qUKBXUEmTgM08EuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2LEiUe/4=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422924,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAXJSfWTunxSzemHMqmgj8lJ4Vm0BfKqGEv2rTfsirMhQFPIq8Cx76b6ghnjDzoTC0nzfl0VIU/AUucgzaCTH+DLhAwChZw1kP4nty6AthWANMBTb2GEgXzSpybL2RCJZqlcuPHSEOGlx+zEABWwj4HbiFZr++EbfqlCgV1BJk4DNPBLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiwg9CHA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422924,
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
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAXJSfWTunxSzemHMqmgj8lJ4Vm0BfKqGEv2rTfsirMhQFPIq8Cx76b6ghnjDzoTC0nzfl0VIU/AUucgzaCTH+DLhAwChZw1kP4nty6AthWANMBTb2GEgXzSpybL2RCJZqlcuPHSEOGlx+zEABWwj4HbiFZr++EbfqlCgV1BJk4DNPBLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiwg9CHA",
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
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAXJSfWTunxSzemHMqmgj8lJ4Vm0BfKqGEv2rTfsirMhQFPIq8Cx76b6ghnjDzoTC0nzfl0VIU/AUucgzaCTH+DLhAwChZw1kP4nty6AthWANMBTb2GEgXzSpybL2RCJZqlcuPHSEOGlx+zEABWwj4HbiFZr++EbfqlCgV1BJk4DNPBLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiwg9CHA",
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
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAXJSfWTunxSzemHMqmgj8lJ4Vm0BfKqGEv2rTfsirMhQFPIq8Cx76b6ghnjDzoTC0nzfl0VIU/AUucgzaCTH+DLhAwChZw1kP4nty6AthWANMBTb2GEgXzSpybL2RCJZqlcuPHSEOGlx+zEABWwj4HbiFZr++EbfqlCgV1BJk4DNPBLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiwg9CHA",
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
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAXJSfWTunxSzemHMqmgj8lJ4Vm0BfKqGEv2rTfsirMhQFPIq8Cx76b6ghnjDzoTC0nzfl0VIU/AUucgzaCTH+DLhAwChZw1kP4nty6AthWANMBTb2GEgXzSpybL2RCJZqlcuPHSEOGlx+zEABWwj4HbiFZr++EbfqlCgV1BJk4DNPBLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiwg9CHA",
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
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
    "data": {
      "message": {
        "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
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
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
    "data": {
      "message": {
        "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
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
  "id": -576460752303422923,
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
  "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
  "id": -576460752303422923,
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
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
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
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
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
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
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
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
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
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
    "data": {
      "state": "tx_+QENCwH4hLhAXJSfWTunxSzemHMqmgj8lJ4Vm0BfKqGEv2rTfsirMhQFPIq8Cx76b6ghnjDzoTC0nzfl0VIU/AUucgzaCTH+DLhAwChZw1kP4nty6AthWANMBTb2GEgXzSpybL2RCJZqlcuPHSEOGlx+zEABWwj4HbiFZr++EbfqlCgV1BJk4DNPBLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiwg9CHA"
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
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
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
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
    "data": {
      "state": "tx_+QENCwH4hLhAXJSfWTunxSzemHMqmgj8lJ4Vm0BfKqGEv2rTfsirMhQFPIq8Cx76b6ghnjDzoTC0nzfl0VIU/AUucgzaCTH+DLhAwChZw1kP4nty6AthWANMBTb2GEgXzSpybL2RCJZqlcuPHSEOGlx+zEABWwj4HbiFZr++EbfqlCgV1BJk4DNPBLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiwg9CHA"
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
  "params": {
    "fee": 123456789876543
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBrtiDfCzPBYjyNB5in8SGsxOHR2qNTwBQGjhXBTi2UrkoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYC5AUz5AUk8AfkBP/kBPKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvkBGPh0oCiW0e4qVvD/C94E6/En+1vvEgzoctloLayg1hD1Tl5u+FGAgICAgICg46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVuAgICAoKcJtie4oQxB6+5JVy+F3eNaNF7V7TgRPXFlQNJ4W/wIgICAgID4T6CnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CO2gP/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWLygoBAIY/qiUiX//4T6DjooHlLkRUA0QFUOns+/GhHcvejx4IPZN7Jd7GGFRtW+2gNllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAHAwMDAwACGcEiGGw8/LeqJTnw=",
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
    "signed_tx": "tx_+QHrCwH4QrhAMdPcK+6CgEK0J/6CuHPjCFoXqm90RFdOzCILaRNucKrsmQy588Ew0QVZSZr8rP+Hdrzqnhg6eZtRHtiS/NlNDbkBovkBnzYBoQa7Yg3wszwWI8jQeYp/EhrMTh0dqjU8AUBo4VwU4tlK5KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWAuQFM+QFJPAH5AT/5ATygKJbR7ipW8P8L3gTr8Sf7W+8SDOhy2WgtrKDWEPVOXm75ARj4dKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvhRgICAgICAoOOigeUuRFQDRAVQ6ez78aEdy96PHgg9k3sl3sYYVG1bgICAgKCnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CICAgICA+E+gpwm2J7ihDEHr7klXL4Xd41o0XtXtOBE9cWVA0nhb/AjtoD/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVi8oKAQCGP6olIl//+E+g46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVvtoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoABwMDAwMAAhnBIhhsPPy1boQ9r"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAMdPcK+6CgEK0J/6CuHPjCFoXqm90RFdOzCILaRNucKrsmQy588Ew0QVZSZr8rP+Hdrzqnhg6eZtRHtiS/NlNDbkBovkBnzYBoQa7Yg3wszwWI8jQeYp/EhrMTh0dqjU8AUBo4VwU4tlK5KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWAuQFM+QFJPAH5AT/5ATygKJbR7ipW8P8L3gTr8Sf7W+8SDOhy2WgtrKDWEPVOXm75ARj4dKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvhRgICAgICAoOOigeUuRFQDRAVQ6ez78aEdy96PHgg9k3sl3sYYVG1bgICAgKCnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CICAgICA+E+gpwm2J7ihDEHr7klXL4Xd41o0XtXtOBE9cWVA0nhb/AjtoD/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVi8oKAQCGP6olIl//+E+g46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVvtoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoABwMDAwMAAhnBIhhsPPy1boQ9r",
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
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
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
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAMdPcK+6CgEK0J/6CuHPjCFoXqm90RFdOzCILaRNucKrsmQy588Ew0QVZSZr8rP+Hdrzqnhg6eZtRHtiS/NlNDbkBovkBnzYBoQa7Yg3wszwWI8jQeYp/EhrMTh0dqjU8AUBo4VwU4tlK5KEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWAuQFM+QFJPAH5AT/5ATygKJbR7ipW8P8L3gTr8Sf7W+8SDOhy2WgtrKDWEPVOXm75ARj4dKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvhRgICAgICAoOOigeUuRFQDRAVQ6ez78aEdy96PHgg9k3sl3sYYVG1bgICAgKCnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CICAgICA+E+gpwm2J7ihDEHr7klXL4Xd41o0XtXtOBE9cWVA0nhb/AjtoD/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVi8oKAQCGP6olIl//+E+g46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVvtoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoABwMDAwMAAhnBIhhsPPy1boQ9r",
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
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
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
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBrtiDfCzPBYjyNB5in8SGsxOHR2qNTwBQGjhXBTi2UrkoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4Y/qiUiX/+GJGE5yoABAIYPXtZ/KAAQlNCotw==",
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
    "signed_tx": "tx_+KcLAfhCuECN+Dzfrk9sfMtKRgO+cC5Tcx9CCUFrL5qu8NnNZ63QMlz+xw7xr/65OXyd4tWejo9+AUuIre4R2Z4Rd9094d0OuF/4XTgBoQa7Yg3wszwWI8jQeYp/EhrMTh0dqjU8AUBo4VwU4tlK5KEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl//hiRhOcqAAQCGD17WfygAEC22V80="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECN+Dzfrk9sfMtKRgO+cC5Tcx9CCUFrL5qu8NnNZ63QMlz+xw7xr/65OXyd4tWejo9+AUuIre4R2Z4Rd9094d0OuF/4XTgBoQa7Yg3wszwWI8jQeYp/EhrMTh0dqjU8AUBo4VwU4tlK5KEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl//hiRhOcqAAQCGD17WfygAEC22V80=",
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
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECN+Dzfrk9sfMtKRgO+cC5Tcx9CCUFrL5qu8NnNZ63QMlz+xw7xr/65OXyd4tWejo9+AUuIre4R2Z4Rd9094d0OuF/4XTgBoQa7Yg3wszwWI8jQeYp/EhrMTh0dqjU8AUBo4VwU4tlK5KEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl//hiRhOcqAAQCGD17WfygAEC22V80=",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
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
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
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
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
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
    "channel_id": "ch_2RXSygd1My3FZEQ3YmZHjbHzpCLrdrA5zcRXn8tXgSyZg6XxDy",
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
      "fsm_id": "ba_DU3P7oOslNBShqMVADwuRKa9l+0zefivaFFxVtccBNSE/B6U"
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
      "fsm_id": "ba_X5ny2xt6UC9lxkKC5bgRkzMJQgRVfNgYXOFS+WwLHEOVTuii"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYu1dJA3g==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422922,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAqSVKcuHebWLCZ1umI+QbKw1tHjheQS3yngJX6o07FvLBbz79uouFBrP0Z6RcGCdiw8Q9+h5rUSdW6fvdE5voCuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2LrlR37Y="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422922,
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
      "signed_tx": "tx_+MsLAfhCuEAqSVKcuHebWLCZ1umI+QbKw1tHjheQS3yngJX6o07FvLBbz79uouFBrP0Z6RcGCdiw8Q9+h5rUSdW6fvdE5voCuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2LrlR37Y=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422921,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAKklSnLh3m1iwmdbpiPkGysNbR44XkEt8p4CV+qNOxbywW8+/bqLhQaz9GekXBgnYsPEPfoea1EnVun73ROb6ArhAtAJfDoiZl5BnT6PFjz8ik5SPZKTrG0z9ZPzt40FgfSMh5bqBmmw67OGodw48NM/7adtryvp0tk/0y26sQaHjBLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdi7E+eJj"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422921,
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
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAKklSnLh3m1iwmdbpiPkGysNbR44XkEt8p4CV+qNOxbywW8+/bqLhQaz9GekXBgnYsPEPfoea1EnVun73ROb6ArhAtAJfDoiZl5BnT6PFjz8ik5SPZKTrG0z9ZPzt40FgfSMh5bqBmmw67OGodw48NM/7adtryvp0tk/0y26sQaHjBLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdi7E+eJj",
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
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAKklSnLh3m1iwmdbpiPkGysNbR44XkEt8p4CV+qNOxbywW8+/bqLhQaz9GekXBgnYsPEPfoea1EnVun73ROb6ArhAtAJfDoiZl5BnT6PFjz8ik5SPZKTrG0z9ZPzt40FgfSMh5bqBmmw67OGodw48NM/7adtryvp0tk/0y26sQaHjBLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdi7E+eJj",
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
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAKklSnLh3m1iwmdbpiPkGysNbR44XkEt8p4CV+qNOxbywW8+/bqLhQaz9GekXBgnYsPEPfoea1EnVun73ROb6ArhAtAJfDoiZl5BnT6PFjz8ik5SPZKTrG0z9ZPzt40FgfSMh5bqBmmw67OGodw48NM/7adtryvp0tk/0y26sQaHjBLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdi7E+eJj",
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
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAKklSnLh3m1iwmdbpiPkGysNbR44XkEt8p4CV+qNOxbywW8+/bqLhQaz9GekXBgnYsPEPfoea1EnVun73ROb6ArhAtAJfDoiZl5BnT6PFjz8ik5SPZKTrG0z9ZPzt40FgfSMh5bqBmmw67OGodw48NM/7adtryvp0tk/0y26sQaHjBLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdi7E+eJj",
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
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
    "data": {
      "message": {
        "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
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
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
    "data": {
      "message": {
        "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
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
  "id": -576460752303422920,
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
  "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
  "id": -576460752303422920,
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
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
    "data": {
      "event": "own_funding_locked"
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
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
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
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
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
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
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
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
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
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
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
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
    "data": {
      "state": "tx_+QENCwH4hLhAKklSnLh3m1iwmdbpiPkGysNbR44XkEt8p4CV+qNOxbywW8+/bqLhQaz9GekXBgnYsPEPfoea1EnVun73ROb6ArhAtAJfDoiZl5BnT6PFjz8ik5SPZKTrG0z9ZPzt40FgfSMh5bqBmmw67OGodw48NM/7adtryvp0tk/0y26sQaHjBLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdi7E+eJj"
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
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
    "data": {
      "state": "tx_+QENCwH4hLhAKklSnLh3m1iwmdbpiPkGysNbR44XkEt8p4CV+qNOxbywW8+/bqLhQaz9GekXBgnYsPEPfoea1EnVun73ROb6ArhAtAJfDoiZl5BnT6PFjz8ik5SPZKTrG0z9ZPzt40FgfSMh5bqBmmw67OGodw48NM/7adtryvp0tk/0y26sQaHjBLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdi7E+eJj"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {
    "fee": 123456789876543
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBgecIw/T9QvJy6Tws2+p7kSsp326Meh6f5DBrXQrCJIWoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4C5AUz5AUk8AfkBP/kBPKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvkBGPh0oCiW0e4qVvD/C94E6/En+1vvEgzoctloLayg1hD1Tl5u+FGAgICAgICg46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVuAgICAoKcJtie4oQxB6+5JVy+F3eNaNF7V7TgRPXFlQNJ4W/wIgICAgID4T6CnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CO2gP/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWLygoBAIY/qiUiX//4T6DjooHlLkRUA0QFUOns+/GhHcvejx4IPZN7Jd7GGFRtW+2gNllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAHAwMDAwACGcEiGGw8/EXcbenY=",
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
  "method": "channels.close_solo_sign",
  "params": {
    "signed_tx": "tx_+QHrCwH4QrhAzSfkz3gDKfjvwMEdX3nwMGE0HtFbAhgVB/g6jCukliOzEkGs1H24U/2oEj0qkV7cAwEV9SShVxnfEZebKliqC7kBovkBnzYBoQYHnCMP0/ULycuk8LNvqe5ErKd9ujHoen+Qwa10KwiSFqEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+AuQFM+QFJPAH5AT/5ATygKJbR7ipW8P8L3gTr8Sf7W+8SDOhy2WgtrKDWEPVOXm75ARj4dKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvhRgICAgICAoOOigeUuRFQDRAVQ6ez78aEdy96PHgg9k3sl3sYYVG1bgICAgKCnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CICAgICA+E+gpwm2J7ihDEHr7klXL4Xd41o0XtXtOBE9cWVA0nhb/AjtoD/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVi8oKAQCGP6olIl//+E+g46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVvtoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoABwMDAwMAAhnBIhhsPPxHS2ZsS"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAzSfkz3gDKfjvwMEdX3nwMGE0HtFbAhgVB/g6jCukliOzEkGs1H24U/2oEj0qkV7cAwEV9SShVxnfEZebKliqC7kBovkBnzYBoQYHnCMP0/ULycuk8LNvqe5ErKd9ujHoen+Qwa10KwiSFqEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+AuQFM+QFJPAH5AT/5ATygKJbR7ipW8P8L3gTr8Sf7W+8SDOhy2WgtrKDWEPVOXm75ARj4dKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvhRgICAgICAoOOigeUuRFQDRAVQ6ez78aEdy96PHgg9k3sl3sYYVG1bgICAgKCnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CICAgICA+E+gpwm2J7ihDEHr7klXL4Xd41o0XtXtOBE9cWVA0nhb/AjtoD/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVi8oKAQCGP6olIl//+E+g46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVvtoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoABwMDAwMAAhnBIhhsPPxHS2ZsS",
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
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
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
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAzSfkz3gDKfjvwMEdX3nwMGE0HtFbAhgVB/g6jCukliOzEkGs1H24U/2oEj0qkV7cAwEV9SShVxnfEZebKliqC7kBovkBnzYBoQYHnCMP0/ULycuk8LNvqe5ErKd9ujHoen+Qwa10KwiSFqEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+AuQFM+QFJPAH5AT/5ATygKJbR7ipW8P8L3gTr8Sf7W+8SDOhy2WgtrKDWEPVOXm75ARj4dKAoltHuKlbw/wveBOvxJ/tb7xIM6HLZaC2soNYQ9U5ebvhRgICAgICAoOOigeUuRFQDRAVQ6ez78aEdy96PHgg9k3sl3sYYVG1bgICAgKCnCbYnuKEMQevuSVcvhd3jWjRe1e04ET1xZUDSeFv8CICAgICA+E+gpwm2J7ihDEHr7klXL4Xd41o0XtXtOBE9cWVA0nhb/AjtoD/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVi8oKAQCGP6olIl//+E+g46KB5S5EVANEBVDp7PvxoR3L3o8eCD2TeyXexhhUbVvtoDZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/i8oKAQCGJGE5yoABwMDAwMAAhnBIhhsPPxHS2ZsS",
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
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
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
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBgecIw/T9QvJy6Tws2+p7kSsp326Meh6f5DBrXQrCJIWoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4Y/qiUiX/+GJGE5yoABAIYPXtZ/KAASoUN1fQ==",
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
    "signed_tx": "tx_+KcLAfhCuEBt6CvivOwNU/zIiCL5POHA/IhPG8Up9+2/MHurj65XqCSuhTaof4hmtgv83Nyfek37R3PQ7UJJ1HMLMg2ceSwHuF/4XTgBoQYHnCMP0/ULycuk8LNvqe5ErKd9ujHoen+Qwa10KwiSFqEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl//hiRhOcqAAQCGD17WfygAErywCmI="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBt6CvivOwNU/zIiCL5POHA/IhPG8Up9+2/MHurj65XqCSuhTaof4hmtgv83Nyfek37R3PQ7UJJ1HMLMg2ceSwHuF/4XTgBoQYHnCMP0/ULycuk8LNvqe5ErKd9ujHoen+Qwa10KwiSFqEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl//hiRhOcqAAQCGD17WfygAErywCmI=",
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
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBt6CvivOwNU/zIiCL5POHA/IhPG8Up9+2/MHurj65XqCSuhTaof4hmtgv83Nyfek37R3PQ7UJJ1HMLMg2ceSwHuF/4XTgBoQYHnCMP0/ULycuk8LNvqe5ErKd9ujHoen+Qwa10KwiSFqEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GP6olIl//hiRhOcqAAQCGD17WfygAErywCmI=",
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
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
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
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
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
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
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
    "channel_id": "ch_4MPKvuWoWeujPQf8cp6d2o9TWRta1849hLPyC18zziQk5ygTV",
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
