
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
      "fsm_id": "ba_f4fZWVt+QHUvb6KjWRPZQE35pBjdTEUubN4ACHJVS8CdUdBF"
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
      "fsm_id": "ba_qdQOjvryfn+N7crl5kRxyvPi02W2OlmJD8zM5rCL7ptVSE8c"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAYFyX20tJ3kJWZba8QX1zQgAqZ+Fvto7b6xDt9XcJ52mhj+qJSJgAKEBY7BAnZQdwHCfa8IWz8sy3BIvv194bbM9K7ToL6Ya5sOGJGE5yoAAAgoAhhAGeddIAMCg7HrkhJzrXwFy5IKtmxhbJuaCbjSV3VFmmnRgb+Tsdg8DndmSdA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422689,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECMXMZYrOmLUob1JvFaV21nudANszV+n55kFHEr51Buuf1y114JWUXXsjHY3vQoiqi2XFzeWWTzM8V8uqkBG8wMuIP4gTIBoQGBcl9tLSd5CVmW2vEF9c0IAKmfhb7aO2+sQ7fV3CedpoY/qiUiYAChAWOwQJ2UHcBwn2vCFs/LMtwSL79feG2zPSu06C+mGubDhiRhOcqAAAIKAIYQBnnXSADAoOx65ISc618BcuSCrZsYWybmgm40ld1RZpp0YG/k7HYPAzv5eHY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422689,
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
    "data": {
      "fsm_id": "ba_qdQOjvryfn+N7crl5kRxyvPi02W2OlmJD8zM5rCL7ptVSE8c",
      "signed_tx": "tx_+MsLAfhCuECMXMZYrOmLUob1JvFaV21nudANszV+n55kFHEr51Buuf1y114JWUXXsjHY3vQoiqi2XFzeWWTzM8V8uqkBG8wMuIP4gTIBoQGBcl9tLSd5CVmW2vEF9c0IAKmfhb7aO2+sQ7fV3CedpoY/qiUiYAChAWOwQJ2UHcBwn2vCFs/LMtwSL79feG2zPSu06C+mGubDhiRhOcqAAAIKAIYQBnnXSADAoOx65ISc618BcuSCrZsYWybmgm40ld1RZpp0YG/k7HYPAzv5eHY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422688,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAG+C2lKwKYZ0g5LBcVRkmsezrq2SzvUftDRiPALfV7780ojngnDIZHuDJLIQq8naAPRkKLONz4hzbJh/aJdn5DLhAjFzGWKzpi1KG9SbxWldtZ7nQDbM1fp+eZBRxK+dQbrn9ctdeCVlF17Ix2N70KIqotlxc3llk8zPFfLqpARvMDLiD+IEyAaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGP6olImAAoQFjsECdlB3AcJ9rwhbPyzLcEi+/X3htsz0rtOgvphrmw4YkYTnKgAACCgCGEAZ510gAwKDseuSEnOtfAXLkgq2bGFsm5oJuNJXdUWaadGBv5Ox2DwM9FCUo"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
  "id": -576460752303422688,
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAG+C2lKwKYZ0g5LBcVRkmsezrq2SzvUftDRiPALfV7780ojngnDIZHuDJLIQq8naAPRkKLONz4hzbJh/aJdn5DLhAjFzGWKzpi1KG9SbxWldtZ7nQDbM1fp+eZBRxK+dQbrn9ctdeCVlF17Ix2N70KIqotlxc3llk8zPFfLqpARvMDLiD+IEyAaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGP6olImAAoQFjsECdlB3AcJ9rwhbPyzLcEi+/X3htsz0rtOgvphrmw4YkYTnKgAACCgCGEAZ510gAwKDseuSEnOtfAXLkgq2bGFsm5oJuNJXdUWaadGBv5Ox2DwM9FCUo",
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_f4fZWVt+QHUvb6KjWRPZQE35pBjdTEUubN4ACHJVS8CdUdBF"
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAG+C2lKwKYZ0g5LBcVRkmsezrq2SzvUftDRiPALfV7780ojngnDIZHuDJLIQq8naAPRkKLONz4hzbJh/aJdn5DLhAjFzGWKzpi1KG9SbxWldtZ7nQDbM1fp+eZBRxK+dQbrn9ctdeCVlF17Ix2N70KIqotlxc3llk8zPFfLqpARvMDLiD+IEyAaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGP6olImAAoQFjsECdlB3AcJ9rwhbPyzLcEi+/X3htsz0rtOgvphrmw4YkYTnKgAACCgCGEAZ510gAwKDseuSEnOtfAXLkgq2bGFsm5oJuNJXdUWaadGBv5Ox2DwM9FCUo",
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAG+C2lKwKYZ0g5LBcVRkmsezrq2SzvUftDRiPALfV7780ojngnDIZHuDJLIQq8naAPRkKLONz4hzbJh/aJdn5DLhAjFzGWKzpi1KG9SbxWldtZ7nQDbM1fp+eZBRxK+dQbrn9ctdeCVlF17Ix2N70KIqotlxc3llk8zPFfLqpARvMDLiD+IEyAaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGP6olImAAoQFjsECdlB3AcJ9rwhbPyzLcEi+/X3htsz0rtOgvphrmw4YkYTnKgAACCgCGEAZ510gAwKDseuSEnOtfAXLkgq2bGFsm5oJuNJXdUWaadGBv5Ox2DwM9FCUo",
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAG+C2lKwKYZ0g5LBcVRkmsezrq2SzvUftDRiPALfV7780ojngnDIZHuDJLIQq8naAPRkKLONz4hzbJh/aJdn5DLhAjFzGWKzpi1KG9SbxWldtZ7nQDbM1fp+eZBRxK+dQbrn9ctdeCVlF17Ix2N70KIqotlxc3llk8zPFfLqpARvMDLiD+IEyAaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGP6olImAAoQFjsECdlB3AcJ9rwhbPyzLcEi+/X3htsz0rtOgvphrmw4YkYTnKgAACCgCGEAZ510gAwKDseuSEnOtfAXLkgq2bGFsm5oJuNJXdUWaadGBv5Ox2DwM9FCUo",
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
    "data": {
      "message": {
        "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
    "data": {
      "message": {
        "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
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
  "id": -576460752303422687,
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
  "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
  "id": -576460752303422687,
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
    "data": {
      "state": "tx_+QENCwH4hLhAG+C2lKwKYZ0g5LBcVRkmsezrq2SzvUftDRiPALfV7780ojngnDIZHuDJLIQq8naAPRkKLONz4hzbJh/aJdn5DLhAjFzGWKzpi1KG9SbxWldtZ7nQDbM1fp+eZBRxK+dQbrn9ctdeCVlF17Ix2N70KIqotlxc3llk8zPFfLqpARvMDLiD+IEyAaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGP6olImAAoQFjsECdlB3AcJ9rwhbPyzLcEi+/X3htsz0rtOgvphrmw4YkYTnKgAACCgCGEAZ510gAwKDseuSEnOtfAXLkgq2bGFsm5oJuNJXdUWaadGBv5Ox2DwM9FCUo"
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
    "data": {
      "state": "tx_+QENCwH4hLhAG+C2lKwKYZ0g5LBcVRkmsezrq2SzvUftDRiPALfV7780ojngnDIZHuDJLIQq8naAPRkKLONz4hzbJh/aJdn5DLhAjFzGWKzpi1KG9SbxWldtZ7nQDbM1fp+eZBRxK+dQbrn9ctdeCVlF17Ix2N70KIqotlxc3llk8zPFfLqpARvMDLiD+IEyAaEBgXJfbS0neQlZltrxBfXNCACpn4W+2jtvrEO31dwnnaaGP6olImAAoQFjsECdlB3AcJ9rwhbPyzLcEi+/X3htsz0rtOgvphrmw4YkYTnKgAACCgCGEAZ510gAwKDseuSEnOtfAXLkgq2bGFsm5oJuNJXdUWaadGBv5Ox2DwM9FCUo"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm",
    "to": "ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBu8JMKqzQr1agqofwcLQ0Rx+Gr8L2X7E3QYEgdaYYcDMAqBpVxyHZWOFrCJJY/Ce3OU0fBDJM6wjQcA2W3MAq6pGLrwS3fY=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm",
          "op": "OffChainTransfer",
          "to": "ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr"
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
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECFC27cqVEG+VAOWJLisuhQImk2ph6hhfVuAnz3X7u2o0+HOkXZWDc/u2QF6BzcNkyAWpKzsNUV6NfmvJi//ncNuEj4RjkCoQbvCTCqs0K9WoKqH8HC0NEcfhq/C9l+xN0GBIHWmGHAzAKgaVcch2VjhawiSWPwntzlNHwQyTOsI0HANltzAKuqRi7pbQ2L"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
    "data": {
      "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 1
    }
  },
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
    "from": "ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm",
    "to": "ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBu8JMKqzQr1agqofwcLQ0Rx+Gr8L2X7E3QYEgdaYYcDMAqBpVxyHZWOFrCJJY/Ce3OU0fBDJM6wjQcA2W3MAq6pGLrwS3fY=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_z1YYuduppEhsxGZmzEnuqWoui4vwgSFVeBXKLsmbUvPAGnHDm",
          "op": "OffChainTransfer",
          "to": "ak_kuQhTPzhJ6XicQfXXRvT5CT7V3GtXMk3b8vGqMUzdedBTh2Yr"
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
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+NILAfiEuECFC27cqVEG+VAOWJLisuhQImk2ph6hhfVuAnz3X7u2o0+HOkXZWDc/u2QF6BzcNkyAWpKzsNUV6NfmvJi//ncNuECh4MftuewJOSSUF5BhJVu5lCcR5mWGI5DVM4n/PtvHNQQMbTGoO5gXxu3CiKl/QRXYWusY4BntDG/o9zMYACUDuEj4RjkCoQbvCTCqs0K9WoKqH8HC0NEcfhq/C9l+xN0GBIHWmGHAzAKgaVcch2VjhawiSWPwntzlNHwQyTOsI0HANltzAKuqRi7gj66G"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
    "data": {
      "state": "tx_+NILAfiEuECFC27cqVEG+VAOWJLisuhQImk2ph6hhfVuAnz3X7u2o0+HOkXZWDc/u2QF6BzcNkyAWpKzsNUV6NfmvJi//ncNuECh4MftuewJOSSUF5BhJVu5lCcR5mWGI5DVM4n/PtvHNQQMbTGoO5gXxu3CiKl/QRXYWusY4BntDG/o9zMYACUDuEj4RjkCoQbvCTCqs0K9WoKqH8HC0NEcfhq/C9l+xN0GBIHWmGHAzAKgaVcch2VjhawiSWPwntzlNHwQyTOsI0HANltzAKuqRi7gj66G"
    }
  },
  "version": 1
}
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy&host=localhost&offchain_tx=tx_%2BNILAfiEuECFC27cqVEG%2BVAOWJLisuhQImk2ph6hhfVuAnz3X7u2o0%2BHOkXZWDc%2Fu2QF6BzcNkyAWpKzsNUV6NfmvJi%2F%2FncNuECh4MftuewJOSSUF5BhJVu5lCcR5mWGI5DVM4n%2FPtvHNQQMbTGoO5gXxu3CiKl%2FQRXYWusY4BntDG%2Fo9zMYACUDuEj4RjkCoQbvCTCqs0K9WoKqH8HC0NEcfhq%2FC9l%2BxN0GBIHWmGHAzAKgaVcch2VjhawiSWPwntzlNHwQyTOsI0HANltzAKuqRi7gj66G&port=14035&protocol=json-rpc&role=responder
```

#### responder <--- node
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

#### responder closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy&existing_fsm_id=Invalid&host=localhost&offchain_tx=tx_%2BNILAfiEuECFC27cqVEG%2BVAOWJLisuhQImk2ph6hhfVuAnz3X7u2o0%2BHOkXZWDc%2Fu2QF6BzcNkyAWpKzsNUV6NfmvJi%2F%2FncNuECh4MftuewJOSSUF5BhJVu5lCcR5mWGI5DVM4n%2FPtvHNQQMbTGoO5gXxu3CiKl%2FQRXYWusY4BntDG%2Fo9zMYACUDuEj4RjkCoQbvCTCqs0K9WoKqH8HC0NEcfhq%2FC9l%2BxN0GBIHWmGHAzAKgaVcch2VjhawiSWPwntzlNHwQyTOsI0HANltzAKuqRi7gj66G&port=14035&protocol=json-rpc&role=responder
```

#### responder <--- node
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

#### responder closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy&existing_fsm_id=ba_uX2lpycbn1olymNg&host=localhost&offchain_tx=tx_%2BNILAfiEuECFC27cqVEG%2BVAOWJLisuhQImk2ph6hhfVuAnz3X7u2o0%2BHOkXZWDc%2Fu2QF6BzcNkyAWpKzsNUV6NfmvJi%2F%2FncNuECh4MftuewJOSSUF5BhJVu5lCcR5mWGI5DVM4n%2FPtvHNQQMbTGoO5gXxu3CiKl%2FQRXYWusY4BntDG%2Fo9zMYACUDuEj4RjkCoQbvCTCqs0K9WoKqH8HC0NEcfhq%2FC9l%2BxN0GBIHWmGHAzAKgaVcch2VjhawiSWPwntzlNHwQyTOsI0HANltzAKuqRi7gj66G&port=14035&protocol=json-rpc&role=responder
```

#### responder <--- node
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

#### responder closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy&existing_fsm_id=ba_4rXzPQA6lJ28IaNwIs%2FlLRvz0roxJF4ZEuukmj%2FS8sBqyRZQ&host=localhost&offchain_tx=tx_%2BNILAfiEuECFC27cqVEG%2BVAOWJLisuhQImk2ph6hhfVuAnz3X7u2o0%2BHOkXZWDc%2Fu2QF6BzcNkyAWpKzsNUV6NfmvJi%2F%2FncNuECh4MftuewJOSSUF5BhJVu5lCcR5mWGI5DVM4n%2FPtvHNQQMbTGoO5gXxu3CiKl%2FQRXYWusY4BntDG%2Fo9zMYACUDuEj4RjkCoQbvCTCqs0K9WoKqH8HC0NEcfhq%2FC9l%2BxN0GBIHWmGHAzAKgaVcch2VjhawiSWPwntzlNHwQyTOsI0HANltzAKuqRi7gj66G&port=14035&protocol=json-rpc&role=responder
```

#### responder <--- node
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

#### responder closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy&existing_fsm_id=ba_qdQOjvryfn%2BN7crl5kRxyvPi02W2OlmJD8zM5rCL7ptVSE8c&offchain_tx=tx_%2BNILAfiEuECFC27cqVEG%2BVAOWJLisuhQImk2ph6hhfVuAnz3X7u2o0%2BHOkXZWDc%2Fu2QF6BzcNkyAWpKzsNUV6NfmvJi%2F%2FncNuECh4MftuewJOSSUF5BhJVu5lCcR5mWGI5DVM4n%2FPtvHNQQMbTGoO5gXxu3CiKl%2FQRXYWusY4BntDG%2Fo9zMYACUDuEj4RjkCoQbvCTCqs0K9WoKqH8HC0NEcfhq%2FC9l%2BxN0GBIHWmGHAzAKgaVcch2VjhawiSWPwntzlNHwQyTOsI0HANltzAKuqRi7gj66G&port=14035&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_qdQOjvryfn+N7crl5kRxyvPi02W2OlmJD8zM5rCL7ptVSE8c"
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBu8JMKqzQr1agqofwcLQ0Rx+Gr8L2X7E3QYEgdaYYcDMoQFjsECdlB3AcJ9rwhbPyzLcEi+/X3htsz0rtOgvphrmw4Y3+rniy/6GHLHOiuwCAIYPXtZ/KAAB65Pg6A==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422686,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEASWXOn6vf8qAl0ohUTgz/Cdo9XNCzO91/Eu6GhAEd5xqj22wkLHhAy0nUG7q4MFTvWBsc8ARFgGx+sLp6FNEMMuF/4XTUBoQbvCTCqs0K9WoKqH8HC0NEcfhq/C9l+xN0GBIHWmGHAzKEBY7BAnZQdwHCfa8IWz8sy3BIvv194bbM9K7ToL6Ya5sOGN/q54sv+hhyxzorsAgCGD17WfygAAWWeJNA="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
  "id": -576460752303422686,
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
    "data": {
      "event": "shutdown"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEASWXOn6vf8qAl0ohUTgz/Cdo9XNCzO91/Eu6GhAEd5xqj22wkLHhAy0nUG7q4MFTvWBsc8ARFgGx+sLp6FNEMMuF/4XTUBoQbvCTCqs0K9WoKqH8HC0NEcfhq/C9l+xN0GBIHWmGHAzKEBY7BAnZQdwHCfa8IWz8sy3BIvv194bbM9K7ToL6Ya5sOGN/q54sv+hhyxzorsAgCGD17WfygAAWWeJNA=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422685,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEASWXOn6vf8qAl0ohUTgz/Cdo9XNCzO91/Eu6GhAEd5xqj22wkLHhAy0nUG7q4MFTvWBsc8ARFgGx+sLp6FNEMMuECIddzFKcInTpqM6y1egMnyDYtaxw4PQ3cF6tgStGpz/1M7ZBcvQzgE0uklGLh3ZDLSJQN4bAfWFGPpJtGvJUECuF/4XTUBoQbvCTCqs0K9WoKqH8HC0NEcfhq/C9l+xN0GBIHWmGHAzKEBY7BAnZQdwHCfa8IWz8sy3BIvv194bbM9K7ToL6Ya5sOGN/q54sv+hhyxzorsAgCGD17WfygAAfycsN8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
  "id": -576460752303422685,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEASWXOn6vf8qAl0ohUTgz/Cdo9XNCzO91/Eu6GhAEd5xqj22wkLHhAy0nUG7q4MFTvWBsc8ARFgGx+sLp6FNEMMuECIddzFKcInTpqM6y1egMnyDYtaxw4PQ3cF6tgStGpz/1M7ZBcvQzgE0uklGLh3ZDLSJQN4bAfWFGPpJtGvJUECuF/4XTUBoQbvCTCqs0K9WoKqH8HC0NEcfhq/C9l+xN0GBIHWmGHAzKEBY7BAnZQdwHCfa8IWz8sy3BIvv194bbM9K7ToL6Ya5sOGN/q54sv+hhyxzorsAgCGD17WfygAAfycsN8=",
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEASWXOn6vf8qAl0ohUTgz/Cdo9XNCzO91/Eu6GhAEd5xqj22wkLHhAy0nUG7q4MFTvWBsc8ARFgGx+sLp6FNEMMuECIddzFKcInTpqM6y1egMnyDYtaxw4PQ3cF6tgStGpz/1M7ZBcvQzgE0uklGLh3ZDLSJQN4bAfWFGPpJtGvJUECuF/4XTUBoQbvCTCqs0K9WoKqH8HC0NEcfhq/C9l+xN0GBIHWmGHAzKEBY7BAnZQdwHCfa8IWz8sy3BIvv194bbM9K7ToL6Ya5sOGN/q54sv+hhyxzorsAgCGD17WfygAAfycsN8=",
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEASWXOn6vf8qAl0ohUTgz/Cdo9XNCzO91/Eu6GhAEd5xqj22wkLHhAy0nUG7q4MFTvWBsc8ARFgGx+sLp6FNEMMuECIddzFKcInTpqM6y1egMnyDYtaxw4PQ3cF6tgStGpz/1M7ZBcvQzgE0uklGLh3ZDLSJQN4bAfWFGPpJtGvJUECuF/4XTUBoQbvCTCqs0K9WoKqH8HC0NEcfhq/C9l+xN0GBIHWmGHAzKEBY7BAnZQdwHCfa8IWz8sy3BIvv194bbM9K7ToL6Ya5sOGN/q54sv+hhyxzorsAgCGD17WfygAAfycsN8=",
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEASWXOn6vf8qAl0ohUTgz/Cdo9XNCzO91/Eu6GhAEd5xqj22wkLHhAy0nUG7q4MFTvWBsc8ARFgGx+sLp6FNEMMuECIddzFKcInTpqM6y1egMnyDYtaxw4PQ3cF6tgStGpz/1M7ZBcvQzgE0uklGLh3ZDLSJQN4bAfWFGPpJtGvJUECuF/4XTUBoQbvCTCqs0K9WoKqH8HC0NEcfhq/C9l+xN0GBIHWmGHAzKEBY7BAnZQdwHCfa8IWz8sy3BIvv194bbM9K7ToL6Ya5sOGN/q54sv+hhyxzorsAgCGD17WfygAAfycsN8=",
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
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
    "channel_id": "ch_2pGrNVSbcwu8iZNc3qiDmagdLvGS97QKmvHwhjHCYADGnkEYTy",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
