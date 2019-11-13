
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
      "fsm_id": "ba_ssRAN6hALVWP2kZ/4bQbvU+UECbrlk5eQqJ/5CXITlzkMz9/"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": null,
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

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
      "fsm_id": "ba_FVcvPFjQm1A+zVyjLNzNBpf0GK11xVsbWbzzNsQqbMVbFVLl"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": null,
    "data": {
      "action": "system",
      "tag": "pong"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYF1tKnPQ==",
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
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": null,
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": null,
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423396,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBc92LsZB4wDKUme3oXzLhqKQpfpWFtE0LoBGGLN7gZPh5jfncxfxDDh8KWsPEn8CjB1JDlkbrlYiyy4eZTglQFuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2BWXATDw="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423396,
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

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
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
      "signed_tx": "tx_+MsLAfhCuEBc92LsZB4wDKUme3oXzLhqKQpfpWFtE0LoBGGLN7gZPh5jfncxfxDDh8KWsPEn8CjB1JDlkbrlYiyy4eZTglQFuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2BWXATDw=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": null,
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": null,
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423395,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAQXHPdaBTpZq2aEPO/vCgXjWvpj9YlyLyXiIEZr9hvlUKQBHMH4Oc6NwGqaPkPOP+u3rdp1CqN4xx1K6eHTJCDbhAXPdi7GQeMAylJnt6F8y4aikKX6VhbRNC6ARhize4GT4eY353MX8Qw4fClrDxJ/AowdSQ5ZG65WIssuHmU4JUBbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgWoTjuh"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423395,
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
    "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAQXHPdaBTpZq2aEPO/vCgXjWvpj9YlyLyXiIEZr9hvlUKQBHMH4Oc6NwGqaPkPOP+u3rdp1CqN4xx1K6eHTJCDbhAXPdi7GQeMAylJnt6F8y4aikKX6VhbRNC6ARhize4GT4eY353MX8Qw4fClrDxJ/AowdSQ5ZG65WIssuHmU4JUBbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgWoTjuh",
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

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": null,
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
    "data": {
      "action": "system",
      "tag": "pong"
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
    "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAQXHPdaBTpZq2aEPO/vCgXjWvpj9YlyLyXiIEZr9hvlUKQBHMH4Oc6NwGqaPkPOP+u3rdp1CqN4xx1K6eHTJCDbhAXPdi7GQeMAylJnt6F8y4aikKX6VhbRNC6ARhize4GT4eY353MX8Qw4fClrDxJ/AowdSQ5ZG65WIssuHmU4JUBbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgWoTjuh",
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
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
    "data": {
      "action": "system",
      "tag": "pong"
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
    "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAQXHPdaBTpZq2aEPO/vCgXjWvpj9YlyLyXiIEZr9hvlUKQBHMH4Oc6NwGqaPkPOP+u3rdp1CqN4xx1K6eHTJCDbhAXPdi7GQeMAylJnt6F8y4aikKX6VhbRNC6ARhize4GT4eY353MX8Qw4fClrDxJ/AowdSQ5ZG65WIssuHmU4JUBbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgWoTjuh",
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
    "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAQXHPdaBTpZq2aEPO/vCgXjWvpj9YlyLyXiIEZr9hvlUKQBHMH4Oc6NwGqaPkPOP+u3rdp1CqN4xx1K6eHTJCDbhAXPdi7GQeMAylJnt6F8y4aikKX6VhbRNC6ARhize4GT4eY353MX8Qw4fClrDxJ/AowdSQ5ZG65WIssuHmU4JUBbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgWoTjuh",
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
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
    "data": {
      "action": "system",
      "tag": "pong"
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
    "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
    "data": {
      "message": {
        "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
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
    "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
    "data": {
      "message": {
        "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
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
  "id": -576460752303423394,
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
  "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
  "id": -576460752303423394,
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
    "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
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
    "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
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
    "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
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
    "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
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
    "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
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
    "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
    "data": {
      "state": "tx_+QENCwH4hLhAQXHPdaBTpZq2aEPO/vCgXjWvpj9YlyLyXiIEZr9hvlUKQBHMH4Oc6NwGqaPkPOP+u3rdp1CqN4xx1K6eHTJCDbhAXPdi7GQeMAylJnt6F8y4aikKX6VhbRNC6ARhize4GT4eY353MX8Qw4fClrDxJ/AowdSQ5ZG65WIssuHmU4JUBbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgWoTjuh"
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
    "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
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
    "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
    "data": {
      "state": "tx_+QENCwH4hLhAQXHPdaBTpZq2aEPO/vCgXjWvpj9YlyLyXiIEZr9hvlUKQBHMH4Oc6NwGqaPkPOP+u3rdp1CqN4xx1K6eHTJCDbhAXPdi7GQeMAylJnt6F8y4aikKX6VhbRNC6ARhize4GT4eY353MX8Qw4fClrDxJ/AowdSQ5ZG65WIssuHmU4JUBbiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgWoTjuh"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423393,
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
  "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
  "id": -576460752303423393,
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
    "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
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
  "id": -576460752303423392,
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
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
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
  "channel_id": "ch_EeYbtmghnbRqhBctcEh9ABRNLuCwEXL166P6JeE3H9fBC2U8R",
  "id": -576460752303423392,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```
