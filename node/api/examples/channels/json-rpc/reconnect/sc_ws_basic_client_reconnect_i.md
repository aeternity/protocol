
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm&keep_running=false&lock_period=10&port=14035&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr&role=initiator
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
      "fsm_id": "ba_tN+ZDj1onPOAk469bF49Hb3ywnWk3BqLoNvycnzhJfxGhTBY"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm&keep_running=false&lock_period=10&port=14035&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr&role=responder
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
      "fsm_id": "ba_etyMKyulzYfqSj0hlxa9WiZVIWKS23k31StOeqx9JClNXbBf"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAYFyX20tJ3kJWZba8QX1zQgAqZ+Fvto7b6xDt9XcJ52mhj+qJSJgAKEBY7BAnZQdwHCfa8IWz8sy3BIvv194bbM9K7ToL6Ya5sOGJGE5yoAAAgoAhhAGeddIAMCg7HrkhJzrXwFy5IKtmxhbJuaCbjSV3VFmmnRgb+Tsdg8BVB4rog==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422694,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEC/qUcjZhrB0x3KqICje/xGQu9i7sgegYynGwQhjzxBtsw0oqdWS+RzCz6VFVFZ+mpOKGnhjpSz75o8VEO2gkwMuIP4gTIBoQGBcl9tLSd5CVmW2vEF9c0IAKmfhb7aO2+sQ7fV3CedpoY/qiUiYAChAWOwQJ2UHcBwn2vCFs/LMtwSL79feG2zPSu06C+mGubDhiRhOcqAAAIKAIYQBnnXSADAoOx65ISc618BcuSCrZsYWybmgm40ld1RZpp0YG/k7HYPAV2Kv6I="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422694,
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
    "data": {
      "fsm_id": "ba_etyMKyulzYfqSj0hlxa9WiZVIWKS23k31StOeqx9JClNXbBf",
      "signed_tx": "tx_+MsLAfhCuEC/qUcjZhrB0x3KqICje/xGQu9i7sgegYynGwQhjzxBtsw0oqdWS+RzCz6VFVFZ+mpOKGnhjpSz75o8VEO2gkwMuIP4gTIBoQGBcl9tLSd5CVmW2vEF9c0IAKmfhb7aO2+sQ7fV3CedpoY/qiUiYAChAWOwQJ2UHcBwn2vCFs/LMtwSL79feG2zPSu06C+mGubDhiRhOcqAAAIKAIYQBnnXSADAoOx65ISc618BcuSCrZsYWybmgm40ld1RZpp0YG/k7HYPAV2Kv6I=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422693,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAGiZ3+7SvROZ5L8xus9nh1gbN0GL24VOybIuTYUHUHjPKE7sjQzqrouvHZF3VxGBiaUIRFsiSwHGlLHcL91XHCrhAv6lHI2YawdMdyqiAo3v8RkLvYu7IHoGMpxsEIY88QbbMNKKnVkvkcws+lRVRWfpqTihp4Y6Us++aPFRDtoJMDLiD+IEyAaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGP6olImAAoQFjsECdlB3AcJ9rwhbPyzLcEi+/X3htsz0rtOgvphrmw4YkYTnKgAACCgCGEAZ510gAwKDseuSEnOtfAXLkgq2bGFsm5oJuNJXdUWaadGBv5Ox2DwHpquVQ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
  "id": -576460752303422693,
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAGiZ3+7SvROZ5L8xus9nh1gbN0GL24VOybIuTYUHUHjPKE7sjQzqrouvHZF3VxGBiaUIRFsiSwHGlLHcL91XHCrhAv6lHI2YawdMdyqiAo3v8RkLvYu7IHoGMpxsEIY88QbbMNKKnVkvkcws+lRVRWfpqTihp4Y6Us++aPFRDtoJMDLiD+IEyAaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGP6olImAAoQFjsECdlB3AcJ9rwhbPyzLcEi+/X3htsz0rtOgvphrmw4YkYTnKgAACCgCGEAZ510gAwKDseuSEnOtfAXLkgq2bGFsm5oJuNJXdUWaadGBv5Ox2DwHpquVQ",
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_tN+ZDj1onPOAk469bF49Hb3ywnWk3BqLoNvycnzhJfxGhTBY"
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAGiZ3+7SvROZ5L8xus9nh1gbN0GL24VOybIuTYUHUHjPKE7sjQzqrouvHZF3VxGBiaUIRFsiSwHGlLHcL91XHCrhAv6lHI2YawdMdyqiAo3v8RkLvYu7IHoGMpxsEIY88QbbMNKKnVkvkcws+lRVRWfpqTihp4Y6Us++aPFRDtoJMDLiD+IEyAaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGP6olImAAoQFjsECdlB3AcJ9rwhbPyzLcEi+/X3htsz0rtOgvphrmw4YkYTnKgAACCgCGEAZ510gAwKDseuSEnOtfAXLkgq2bGFsm5oJuNJXdUWaadGBv5Ox2DwHpquVQ",
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAGiZ3+7SvROZ5L8xus9nh1gbN0GL24VOybIuTYUHUHjPKE7sjQzqrouvHZF3VxGBiaUIRFsiSwHGlLHcL91XHCrhAv6lHI2YawdMdyqiAo3v8RkLvYu7IHoGMpxsEIY88QbbMNKKnVkvkcws+lRVRWfpqTihp4Y6Us++aPFRDtoJMDLiD+IEyAaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGP6olImAAoQFjsECdlB3AcJ9rwhbPyzLcEi+/X3htsz0rtOgvphrmw4YkYTnKgAACCgCGEAZ510gAwKDseuSEnOtfAXLkgq2bGFsm5oJuNJXdUWaadGBv5Ox2DwHpquVQ",
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAGiZ3+7SvROZ5L8xus9nh1gbN0GL24VOybIuTYUHUHjPKE7sjQzqrouvHZF3VxGBiaUIRFsiSwHGlLHcL91XHCrhAv6lHI2YawdMdyqiAo3v8RkLvYu7IHoGMpxsEIY88QbbMNKKnVkvkcws+lRVRWfpqTihp4Y6Us++aPFRDtoJMDLiD+IEyAaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGP6olImAAoQFjsECdlB3AcJ9rwhbPyzLcEi+/X3htsz0rtOgvphrmw4YkYTnKgAACCgCGEAZ510gAwKDseuSEnOtfAXLkgq2bGFsm5oJuNJXdUWaadGBv5Ox2DwHpquVQ",
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
    "to": "ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
    "data": {
      "message": {
        "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
        "from": "ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm",
        "info": "Hello",
        "to": "ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr"
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
    "to": "ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
    "data": {
      "message": {
        "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
        "from": "ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr",
        "info": "Hello back",
        "to": "ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422692,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm",
      "ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
  "id": -576460752303422692,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm",
      "balance": 69999999999999
    },
    {
      "account": "ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr",
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
    "data": {
      "state": "tx_+QENCwH4hLhAGiZ3+7SvROZ5L8xus9nh1gbN0GL24VOybIuTYUHUHjPKE7sjQzqrouvHZF3VxGBiaUIRFsiSwHGlLHcL91XHCrhAv6lHI2YawdMdyqiAo3v8RkLvYu7IHoGMpxsEIY88QbbMNKKnVkvkcws+lRVRWfpqTihp4Y6Us++aPFRDtoJMDLiD+IEyAaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGP6olImAAoQFjsECdlB3AcJ9rwhbPyzLcEi+/X3htsz0rtOgvphrmw4YkYTnKgAACCgCGEAZ510gAwKDseuSEnOtfAXLkgq2bGFsm5oJuNJXdUWaadGBv5Ox2DwHpquVQ"
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
    "data": {
      "state": "tx_+QENCwH4hLhAGiZ3+7SvROZ5L8xus9nh1gbN0GL24VOybIuTYUHUHjPKE7sjQzqrouvHZF3VxGBiaUIRFsiSwHGlLHcL91XHCrhAv6lHI2YawdMdyqiAo3v8RkLvYu7IHoGMpxsEIY88QbbMNKKnVkvkcws+lRVRWfpqTihp4Y6Us++aPFRDtoJMDLiD+IEyAaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGP6olImAAoQFjsECdlB3AcJ9rwhbPyzLcEi+/X3htsz0rtOgvphrmw4YkYTnKgAACCgCGEAZ510gAwKDseuSEnOtfAXLkgq2bGFsm5oJuNJXdUWaadGBv5Ox2DwHpquVQ"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr",
    "to": "ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBl1/WGq2SpxsFg+dWgeQM6Pi73l60KT1I/aoD2Cck9DXAqBRKdAo9Ra0kJxynZwYowrhRLTvz49zVGnqVpE47qEsWwvbZcg=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr",
          "op": "OffChainTransfer",
          "to": "ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm"
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
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECTt3v4cYZtgc6guTNnVN+zYfGiVzUUxk7FdIArd8xGPMh669wC+INpmR+PvNIDvXgWbzVKxcxvhJay6yAAcjAPuEj4RjkCoQZdf1hqtkqcbBYPnVoHkDOj4u95etCk9SP2qA9gnJPQ1wKgUSnQKPUWtJCccp2cGKMK4US078+Pc1Rp6laROO6hLFsqLkaU"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
    "data": {
      "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 1
    }
  },
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
    "from": "ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr",
    "to": "ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBl1/WGq2SpxsFg+dWgeQM6Pi73l60KT1I/aoD2Cck9DXAqBRKdAo9Ra0kJxynZwYowrhRLTvz49zVGnqVpE47qEsWwvbZcg=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr",
          "op": "OffChainTransfer",
          "to": "ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm"
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
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+NILAfiEuECTt3v4cYZtgc6guTNnVN+zYfGiVzUUxk7FdIArd8xGPMh669wC+INpmR+PvNIDvXgWbzVKxcxvhJay6yAAcjAPuECVwQMCpJ3FC7LbU7LLUJkoCDcasC7wCNLbvNxOvaUp1M3YToI1vo3UiKvsDlXxt1qaU5cizLNgRlggl756ggYPuEj4RjkCoQZdf1hqtkqcbBYPnVoHkDOj4u95etCk9SP2qA9gnJPQ1wKgUSnQKPUWtJCccp2cGKMK4US078+Pc1Rp6laROO6hLFsu1cWH"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
    "data": {
      "state": "tx_+NILAfiEuECTt3v4cYZtgc6guTNnVN+zYfGiVzUUxk7FdIArd8xGPMh669wC+INpmR+PvNIDvXgWbzVKxcxvhJay6yAAcjAPuECVwQMCpJ3FC7LbU7LLUJkoCDcasC7wCNLbvNxOvaUp1M3YToI1vo3UiKvsDlXxt1qaU5cizLNgRlggl756ggYPuEj4RjkCoQZdf1hqtkqcbBYPnVoHkDOj4u95etCk9SP2qA9gnJPQ1wKgUSnQKPUWtJCccp2cGKMK4US078+Pc1Rp6laROO6hLFsu1cWH"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu&host=localhost&offchain_tx=tx_%2BNILAfiEuECTt3v4cYZtgc6guTNnVN%2BzYfGiVzUUxk7FdIArd8xGPMh669wC%2BINpmR%2BPvNIDvXgWbzVKxcxvhJay6yAAcjAPuECVwQMCpJ3FC7LbU7LLUJkoCDcasC7wCNLbvNxOvaUp1M3YToI1vo3UiKvsDlXxt1qaU5cizLNgRlggl756ggYPuEj4RjkCoQZdf1hqtkqcbBYPnVoHkDOj4u95etCk9SP2qA9gnJPQ1wKgUSnQKPUWtJCccp2cGKMK4US078%2BPc1Rp6laROO6hLFsu1cWH&port=14035&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 2000,
        "message": "Missing field: existing_fsm_id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu&existing_fsm_id=Invalid&host=localhost&offchain_tx=tx_%2BNILAfiEuECTt3v4cYZtgc6guTNnVN%2BzYfGiVzUUxk7FdIArd8xGPMh669wC%2BINpmR%2BPvNIDvXgWbzVKxcxvhJay6yAAcjAPuECVwQMCpJ3FC7LbU7LLUJkoCDcasC7wCNLbvNxOvaUp1M3YToI1vo3UiKvsDlXxt1qaU5cizLNgRlggl756ggYPuEj4RjkCoQZdf1hqtkqcbBYPnVoHkDOj4u95etCk9SP2qA9gnJPQ1wKgUSnQKPUWtJCccp2cGKMK4US078%2BPc1Rp6laROO6hLFsu1cWH&port=14035&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu&existing_fsm_id=ba_HyQuD1U6unjpal8v&host=localhost&offchain_tx=tx_%2BNILAfiEuECTt3v4cYZtgc6guTNnVN%2BzYfGiVzUUxk7FdIArd8xGPMh669wC%2BINpmR%2BPvNIDvXgWbzVKxcxvhJay6yAAcjAPuECVwQMCpJ3FC7LbU7LLUJkoCDcasC7wCNLbvNxOvaUp1M3YToI1vo3UiKvsDlXxt1qaU5cizLNgRlggl756ggYPuEj4RjkCoQZdf1hqtkqcbBYPnVoHkDOj4u95etCk9SP2qA9gnJPQ1wKgUSnQKPUWtJCccp2cGKMK4US078%2BPc1Rp6laROO6hLFsu1cWH&port=14035&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu&existing_fsm_id=ba_u5RQ29E7CrnVX6d8Bzm5lRLLnNrZxWWDsI8uocwZ1UYM503C&host=localhost&offchain_tx=tx_%2BNILAfiEuECTt3v4cYZtgc6guTNnVN%2BzYfGiVzUUxk7FdIArd8xGPMh669wC%2BINpmR%2BPvNIDvXgWbzVKxcxvhJay6yAAcjAPuECVwQMCpJ3FC7LbU7LLUJkoCDcasC7wCNLbvNxOvaUp1M3YToI1vo3UiKvsDlXxt1qaU5cizLNgRlggl756ggYPuEj4RjkCoQZdf1hqtkqcbBYPnVoHkDOj4u95etCk9SP2qA9gnJPQ1wKgUSnQKPUWtJCccp2cGKMK4US078%2BPc1Rp6laROO6hLFsu1cWH&port=14035&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu&existing_fsm_id=ba_tN%2BZDj1onPOAk469bF49Hb3ywnWk3BqLoNvycnzhJfxGhTBY&host=localhost&offchain_tx=tx_%2BNILAfiEuECTt3v4cYZtgc6guTNnVN%2BzYfGiVzUUxk7FdIArd8xGPMh669wC%2BINpmR%2BPvNIDvXgWbzVKxcxvhJay6yAAcjAPuECVwQMCpJ3FC7LbU7LLUJkoCDcasC7wCNLbvNxOvaUp1M3YToI1vo3UiKvsDlXxt1qaU5cizLNgRlggl756ggYPuEj4RjkCoQZdf1hqtkqcbBYPnVoHkDOj4u95etCk9SP2qA9gnJPQ1wKgUSnQKPUWtJCccp2cGKMK4US078%2BPc1Rp6laROO6hLFsu1cWH&port=14035&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_tN+ZDj1onPOAk469bF49Hb3ywnWk3BqLoNvycnzhJfxGhTBY"
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBl1/WGq2SpxsFg+dWgeQM6Pi73l60KT1I/aoD2Cck9DXoQGBcl9tLSd5CVmW2vEF9c0IAKmfhb7aO2+sQ7fV3CedpoY3+rnizACGHLHOiuwAAIYPXtZ/KAAC0qxgrw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422691,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEBq+chZ7hpCFTQN5WIFHmDkYkMx9NLvPabg2DDlPXwd67iyT8zy8XeLSLn8molu1SRaY2nPTOnhdUAjDhempN4IuF/4XTUBoQZdf1hqtkqcbBYPnVoHkDOj4u95etCk9SP2qA9gnJPQ16EBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGN/q54swAhhyxzorsAACGD17WfygAAkDyL7c="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
  "id": -576460752303422691,
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEBq+chZ7hpCFTQN5WIFHmDkYkMx9NLvPabg2DDlPXwd67iyT8zy8XeLSLn8molu1SRaY2nPTOnhdUAjDhempN4IuF/4XTUBoQZdf1hqtkqcbBYPnVoHkDOj4u95etCk9SP2qA9gnJPQ16EBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGN/q54swAhhyxzorsAACGD17WfygAAkDyL7c=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422690,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEBq+chZ7hpCFTQN5WIFHmDkYkMx9NLvPabg2DDlPXwd67iyT8zy8XeLSLn8molu1SRaY2nPTOnhdUAjDhempN4IuEDXmJuCMpuBrla5NHddzWOr0w/V9u1igkcpBBacVawogBlWhlzLumk47X3HdRVX/YTgaVSCRAcof3Y191X/CsgBuF/4XTUBoQZdf1hqtkqcbBYPnVoHkDOj4u95etCk9SP2qA9gnJPQ16EBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGN/q54swAhhyxzorsAACGD17WfygAAvuL3a4="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
  "id": -576460752303422690,
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBq+chZ7hpCFTQN5WIFHmDkYkMx9NLvPabg2DDlPXwd67iyT8zy8XeLSLn8molu1SRaY2nPTOnhdUAjDhempN4IuEDXmJuCMpuBrla5NHddzWOr0w/V9u1igkcpBBacVawogBlWhlzLumk47X3HdRVX/YTgaVSCRAcof3Y191X/CsgBuF/4XTUBoQZdf1hqtkqcbBYPnVoHkDOj4u95etCk9SP2qA9gnJPQ16EBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGN/q54swAhhyxzorsAACGD17WfygAAvuL3a4=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBq+chZ7hpCFTQN5WIFHmDkYkMx9NLvPabg2DDlPXwd67iyT8zy8XeLSLn8molu1SRaY2nPTOnhdUAjDhempN4IuEDXmJuCMpuBrla5NHddzWOr0w/V9u1igkcpBBacVawogBlWhlzLumk47X3HdRVX/YTgaVSCRAcof3Y191X/CsgBuF/4XTUBoQZdf1hqtkqcbBYPnVoHkDOj4u95etCk9SP2qA9gnJPQ16EBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGN/q54swAhhyxzorsAACGD17WfygAAvuL3a4=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBq+chZ7hpCFTQN5WIFHmDkYkMx9NLvPabg2DDlPXwd67iyT8zy8XeLSLn8molu1SRaY2nPTOnhdUAjDhempN4IuEDXmJuCMpuBrla5NHddzWOr0w/V9u1igkcpBBacVawogBlWhlzLumk47X3HdRVX/YTgaVSCRAcof3Y191X/CsgBuF/4XTUBoQZdf1hqtkqcbBYPnVoHkDOj4u95etCk9SP2qA9gnJPQ16EBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGN/q54swAhhyxzorsAACGD17WfygAAvuL3a4=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBq+chZ7hpCFTQN5WIFHmDkYkMx9NLvPabg2DDlPXwd67iyT8zy8XeLSLn8molu1SRaY2nPTOnhdUAjDhempN4IuEDXmJuCMpuBrla5NHddzWOr0w/V9u1igkcpBBacVawogBlWhlzLumk47X3HdRVX/YTgaVSCRAcof3Y191X/CsgBuF/4XTUBoQZdf1hqtkqcbBYPnVoHkDOj4u95etCk9SP2qA9gnJPQ16EBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGN/q54swAhhyxzorsAACGD17WfygAAvuL3a4=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
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
    "channel_id": "ch_iBGU9jmo2KBMdcy9GmsZRu2PysTBgKHbTFLJjLLSbXRLvASBu",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
