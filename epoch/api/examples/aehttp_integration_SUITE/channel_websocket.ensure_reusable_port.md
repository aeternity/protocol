
#### initiator init (2018-10-16 17:13:41.252)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb&role=initiator
```

#### responder init (2018-10-16 17:13:41.256)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb&role=responder
```

#### responder <--- (2018-10-16 17:13:42.259)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 17:13:42.261)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 17:13:42.266)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpALGJSrzwTy6oub8Qv4su7RMx2hck9JNUEgjtyU6qrUG48oB7x4ucqxPokv4rA4P5zaAWfi6eCujMzNBvMMu3xP8p9Svn5xM77VDy3ntvSFDRTNLxquqDLKr53dA7VoLQyju8FB1sKcPCeRhzzU2bUngSvayNdyo"
  }
}
```

#### initiator ---> (2018-10-16 17:13:42.292)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HoRPhbcxCNobwSgMzCLSknJuMGoLtFMBeBqawky39U72m8TSK1PgDgUT6vr62H98MTFobzMmRnVpkCzY1vshJJGPQXs4gsMbSAGJzcJZXVNqtEca2FWSBYXgDi6BsCm3knhcr2gRyWiodQMAayddQveT6S9UJzi4dha6DgHnQ32M61GRdiUS13yaYH2Exa1PjhrMqUVKK7QUWUx9jnbQMnTADQvy2UXitR28P8DDre3kqvWGRcS34ZoPfJnKBwnSN"
  }
}
```

#### responder <--- (2018-10-16 17:13:42.293)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 17:13:42.294)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpALGJSrzwTy6oub8Qv4su7RMx2hck9JNUEgjtyU6qrUG48oB7x4ucqxPokv4rA4P5zaAWfi6eCujMzNBvMMu3xP8p9Svn5xM77VDy3ntvSFDRTNLxquqDLKr53dA7VoLQyju8FB1sKcPCeRhzzU2bUngSvayNdyo"
  }
}
```

#### responder ---> (2018-10-16 17:13:42.294)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4Ho5gSvTvzH7LZu9i6vmMZQDcDBFPwk7bvuhCkSZCnzwKTKW1ZkrdYi5U6opR1SBZ6boF9fqTSdCusoRbz4PwNY9AFKZk6WH1khkDPH5eDkAXFXyqYnx9dmb1AFzU1VX61ur5RUcnSn2HZpkP5YZyXw1yg7kkfx99XrWudPVP33CgninedjTuck78wdMwVaBUFcX8WP4QzX9wSCpaE5dXfp2JVZQfAgW1GeVRZUGcKYe8rZZEZiELhapiRJ6Q5JNwN"
  }
}
```

#### initiator <--- (2018-10-16 17:13:42.296)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 17:13:42.296)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmTWBRrkW43ChvW57fQmRGRD3aBPeRyf7JX32c4c977ZS4hRvJ2H83kpYuCeptpNfs5GxH7FPwrprDxXmVHD58XAJAGXJqxrsevPZrw5cu1TASw5FiFwMDnYR2ETmhBdx3LcXCLTQxTf4G4PpGfV3RDMkHEzBBDUBQkJmXrzxtnAfW77wgxhAYZeYCTuq1Qv7C8NzxYaY4w7TtZfa5ZuqabqEMipC3YffooQsMFCoiHfxFtLSP5ntysNhuedQhPgoYopmwc8Mc4631FbmTERRLvh2tJQWd4YkJjNUi2qDwkL5YCgnhkSavxM8uyDSHMdPJHWS1No2NmrrRBMuZcgz6tKMgTj"
  }
}
```

#### initiator <--- (2018-10-16 17:13:42.297)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmTWBRrkW43ChvW57fQmRGRD3aBPeRyf7JX32c4c977ZS4hRvJ2H83kpYuCeptpNfs5GxH7FPwrprDxXmVHD58XAJAGXJqxrsevPZrw5cu1TASw5FiFwMDnYR2ETmhBdx3LcXCLTQxTf4G4PpGfV3RDMkHEzBBDUBQkJmXrzxtnAfW77wgxhAYZeYCTuq1Qv7C8NzxYaY4w7TtZfa5ZuqabqEMipC3YffooQsMFCoiHfxFtLSP5ntysNhuedQhPgoYopmwc8Mc4631FbmTERRLvh2tJQWd4YkJjNUi2qDwkL5YCgnhkSavxM8uyDSHMdPJHWS1No2NmrrRBMuZcgz6tKMgTj"
  }
}
```

#### initiator <--- (2018-10-16 17:13:42.889)
```javascript
{
  "id": -576460752303423477,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 699
    },
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 401
    }
  ]
}
```

#### initiator <--- (2018-10-16 17:13:43.952)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_iyJZrsPcxrxgFc8h4TKEcxJijYAVWZQsdKSAXdpgeaEAg4LSM"
  }
}
```

#### responder <--- (2018-10-16 17:13:43.952)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_iyJZrsPcxrxgFc8h4TKEcxJijYAVWZQsdKSAXdpgeaEAg4LSM"
  }
}
```

#### responder <--- (2018-10-16 17:13:43.953)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_iyJZrsPcxrxgFc8h4TKEcxJijYAVWZQsdKSAXdpgeaEAg4LSM"
  }
}
```

#### initiator <--- (2018-10-16 17:13:43.954)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_iyJZrsPcxrxgFc8h4TKEcxJijYAVWZQsdKSAXdpgeaEAg4LSM"
  }
}
```

#### responder <--- (2018-10-16 17:13:43.957)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_iyJZrsPcxrxgFc8h4TKEcxJijYAVWZQsdKSAXdpgeaEAg4LSM"
  }
}
```

#### responder <--- (2018-10-16 17:13:43.958)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmTWBRrkW43ChvW57fQmRGRD3aBPeRyf7JX32c4c977ZS4hRvJ2H83kpYuCeptpNfs5GxH7FPwrprDxXmVHD58XAJAGXJqxrsevPZrw5cu1TASw5FiFwMDnYR2ETmhBdx3LcXCLTQxTf4G4PpGfV3RDMkHEzBBDUBQkJmXrzxtnAfW77wgxhAYZeYCTuq1Qv7C8NzxYaY4w7TtZfa5ZuqabqEMipC3YffooQsMFCoiHfxFtLSP5ntysNhuedQhPgoYopmwc8Mc4631FbmTERRLvh2tJQWd4YkJjNUi2qDwkL5YCgnhkSavxM8uyDSHMdPJHWS1No2NmrrRBMuZcgz6tKMgTj",
    "channel_id": "ch_iyJZrsPcxrxgFc8h4TKEcxJijYAVWZQsdKSAXdpgeaEAg4LSM"
  }
}
```

#### initiator <--- (2018-10-16 17:13:43.959)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_iyJZrsPcxrxgFc8h4TKEcxJijYAVWZQsdKSAXdpgeaEAg4LSM"
  }
}
```

#### initiator <--- (2018-10-16 17:13:43.960)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmTWBRrkW43ChvW57fQmRGRD3aBPeRyf7JX32c4c977ZS4hRvJ2H83kpYuCeptpNfs5GxH7FPwrprDxXmVHD58XAJAGXJqxrsevPZrw5cu1TASw5FiFwMDnYR2ETmhBdx3LcXCLTQxTf4G4PpGfV3RDMkHEzBBDUBQkJmXrzxtnAfW77wgxhAYZeYCTuq1Qv7C8NzxYaY4w7TtZfa5ZuqabqEMipC3YffooQsMFCoiHfxFtLSP5ntysNhuedQhPgoYopmwc8Mc4631FbmTERRLvh2tJQWd4YkJjNUi2qDwkL5YCgnhkSavxM8uyDSHMdPJHWS1No2NmrrRBMuZcgz6tKMgTj",
    "channel_id": "ch_iyJZrsPcxrxgFc8h4TKEcxJijYAVWZQsdKSAXdpgeaEAg4LSM"
  }
}
```

##### initiator: (2018-10-16 17:13:43.995)
> Funding has been confirmed locally on-chain

##### responder: (2018-10-16 17:13:43.995)
> Funding has been confirmed locally on-chain

##### initiator: (2018-10-16 17:13:43.995)
> Funding has been confirmed on-chain by other party

##### responder: (2018-10-16 17:13:43.995)
> Funding has been confirmed on-chain by other party

##### initiator: (2018-10-16 17:13:43.995)
> Channel is `open` and ready to use

##### responder: (2018-10-16 17:13:43.995)
> Channel is `open` and ready to use

#### initiator ---> (2018-10-16 17:13:44.33)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 10000,
    "from": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
    "to": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb"
  }
}
```

#### initiator <--- (2018-10-16 17:13:44.41)
```javascript
{
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1001,
        "message": "Insufficient balance"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 10000,
        "from": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
        "to": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0"
}
```

#### initiator ---> (2018-10-16 17:13:44.42)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": -1,
    "from": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
    "to": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb"
  }
}
```

#### initiator <--- (2018-10-16 17:13:44.42)
```javascript
{
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1002,
        "message": "Negative amount"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": -1,
        "from": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
        "to": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0"
}
```

#### initiator ---> (2018-10-16 17:13:44.43)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_11111111111111111111111111111115rHyByZ",
    "to": "ak_11111111111111111111111111111115sBJATr"
  }
}
```

#### initiator <--- (2018-10-16 17:13:44.45)
```javascript
{
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1003,
        "message": "Invalid pubkeys"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_11111111111111111111111111111115rHyByZ",
        "to": "ak_11111111111111111111111111111115sBJATr"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0"
}
```

#### responder ---> (2018-10-16 17:13:44.46)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 10000,
    "from": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
    "to": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7"
  }
}
```

#### responder <--- (2018-10-16 17:13:44.53)
```javascript
{
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1001,
        "message": "Insufficient balance"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 10000,
        "from": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
        "to": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0"
}
```

#### responder ---> (2018-10-16 17:13:44.54)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": -1,
    "from": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
    "to": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7"
  }
}
```

#### responder <--- (2018-10-16 17:13:44.55)
```javascript
{
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1002,
        "message": "Negative amount"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": -1,
        "from": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
        "to": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0"
}
```

#### responder ---> (2018-10-16 17:13:44.55)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_11111111111111111111111111111115sBJATr",
    "to": "ak_11111111111111111111111111111115rHyByZ"
  }
}
```

#### responder <--- (2018-10-16 17:13:44.57)
```javascript
{
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1003,
        "message": "Invalid pubkeys"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_11111111111111111111111111111115sBJATr",
        "to": "ak_11111111111111111111111111111115rHyByZ"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0"
}
```

#### initiator init (2018-10-16 17:13:44.163)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb&role=initiator
```

#### responder init (2018-10-16 17:13:44.168)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb&role=responder
```

#### responder <--- (2018-10-16 17:13:45.168)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 17:13:45.170)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 17:13:45.181)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpALGJSrzwTy6oub8Qv4su7RMx2hck9JNUEgjtyU6qrUG48oB7x4ucqxPokv4rA4P5zaAWfi6eCujMzNBvMMu3xP8p9Svn5xM77VDy3ntvSFDRTNLxquqDLKr53dA7VoLQyju8FB1sKcPCeRhzzU2bUngSveJ1Auh"
  }
}
```

#### initiator ---> (2018-10-16 17:13:45.213)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HnZkNtmdJ6XZjem97hWkF94wVRmVcwU2iTtfg79titSWRa6HpbXb6KYdSbfY8nfUCLcARBGezy7ZU5Jc9VgQENg8gK7SW6JwNUXt55hApBYc824xdF93GsCadPa85b3f78Qab81EinDGDWHZZiBa6iNY7UJo8eqcvUw6wGSiQPf853w7rfzV5ooKLfiH9rUznHMGtL7FspNX1nfgYNY6iUZ4ZMbdC7ZP198aBxkg66AkE5jjQiqqCpHEWWVi3Q4Yf"
  }
}
```

#### responder <--- (2018-10-16 17:13:45.214)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 17:13:45.214)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpALGJSrzwTy6oub8Qv4su7RMx2hck9JNUEgjtyU6qrUG48oB7x4ucqxPokv4rA4P5zaAWfi6eCujMzNBvMMu3xP8p9Svn5xM77VDy3ntvSFDRTNLxquqDLKr53dA7VoLQyju8FB1sKcPCeRhzzU2bUngSveJ1Auh"
  }
}
```

#### responder ---> (2018-10-16 17:13:45.215)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4Hok9V8wAu9cFEmr3dfbtSzLqzHoT8HNmAGKHddGGr7dbuM21zjCLuutYNGytBUEkCnCWMzFDAChqk8xmY9SFe9Z76CSdwQr2vj186hBNTZtjwn61wUc4YjivdJLgCQgacLffTGBhrdJRT3jzheMKSGfejYrY5p3fJ6MnrBRGRT6H8GDGHqAP8bitKxkoJBLWyhASstFdM4TpiDDPUy12mqhbmWynoFnj4HSf8gXqGuW2H5bYA1wP49cJyHimJsBES"
  }
}
```

#### initiator <--- (2018-10-16 17:13:45.217)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 17:13:45.217)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmSciqMaQLTmf1oxf4kA2kmohJT3Ac6AYp3vm5qmnXD1bxJf4jspCNuMCpgHsnJP3P7zPmhkhXXoU16PPQDCzHBAHgHTkTgy2tXSYUH9iDqmSsGQfT9BP9EkpoRH5WziwPw6pzjDnJgZi4q7WvyVDEXxmd4QgLiE4PUTp1tX8bPqVSXwP82yM7iaw4C4csfMbMGVc6oosrKiMxNMNGCnoJGYs4YbHiqroYKXzVYeg3nX3wgaLkU3q4crrXczxjDJ6abJXmzfJ4oNEhTdwhLU4j1dsdFJ2FUA3gVcBiCLSLcePUxsJjpvfNSEZPWLRL8VKxDEQw5hTXeLSEj6o7qC9mrg5VjR"
  }
}
```

#### initiator <--- (2018-10-16 17:13:45.218)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmSciqMaQLTmf1oxf4kA2kmohJT3Ac6AYp3vm5qmnXD1bxJf4jspCNuMCpgHsnJP3P7zPmhkhXXoU16PPQDCzHBAHgHTkTgy2tXSYUH9iDqmSsGQfT9BP9EkpoRH5WziwPw6pzjDnJgZi4q7WvyVDEXxmd4QgLiE4PUTp1tX8bPqVSXwP82yM7iaw4C4csfMbMGVc6oosrKiMxNMNGCnoJGYs4YbHiqroYKXzVYeg3nX3wgaLkU3q4crrXczxjDJ6abJXmzfJ4oNEhTdwhLU4j1dsdFJ2FUA3gVcBiCLSLcePUxsJjpvfNSEZPWLRL8VKxDEQw5hTXeLSEj6o7qC9mrg5VjR"
  }
}
```

#### initiator <--- (2018-10-16 17:13:45.500)
```javascript
{
  "id": -576460752303423476,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 699
    },
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 401
    }
  ]
}
```

#### initiator <--- (2018-10-16 17:13:46.428)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_kMPC3Q67LoMquQEKhsyvkrHixzpvyyhYSckPiQ4YE3NMeZdD8"
  }
}
```

#### responder <--- (2018-10-16 17:13:46.429)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_kMPC3Q67LoMquQEKhsyvkrHixzpvyyhYSckPiQ4YE3NMeZdD8"
  }
}
```

#### responder <--- (2018-10-16 17:13:46.430)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_kMPC3Q67LoMquQEKhsyvkrHixzpvyyhYSckPiQ4YE3NMeZdD8"
  }
}
```

#### initiator <--- (2018-10-16 17:13:46.430)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_kMPC3Q67LoMquQEKhsyvkrHixzpvyyhYSckPiQ4YE3NMeZdD8"
  }
}
```

#### responder <--- (2018-10-16 17:13:46.433)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_kMPC3Q67LoMquQEKhsyvkrHixzpvyyhYSckPiQ4YE3NMeZdD8"
  }
}
```

#### initiator <--- (2018-10-16 17:13:46.434)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_kMPC3Q67LoMquQEKhsyvkrHixzpvyyhYSckPiQ4YE3NMeZdD8"
  }
}
```

#### responder <--- (2018-10-16 17:13:46.434)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmSciqMaQLTmf1oxf4kA2kmohJT3Ac6AYp3vm5qmnXD1bxJf4jspCNuMCpgHsnJP3P7zPmhkhXXoU16PPQDCzHBAHgHTkTgy2tXSYUH9iDqmSsGQfT9BP9EkpoRH5WziwPw6pzjDnJgZi4q7WvyVDEXxmd4QgLiE4PUTp1tX8bPqVSXwP82yM7iaw4C4csfMbMGVc6oosrKiMxNMNGCnoJGYs4YbHiqroYKXzVYeg3nX3wgaLkU3q4crrXczxjDJ6abJXmzfJ4oNEhTdwhLU4j1dsdFJ2FUA3gVcBiCLSLcePUxsJjpvfNSEZPWLRL8VKxDEQw5hTXeLSEj6o7qC9mrg5VjR",
    "channel_id": "ch_kMPC3Q67LoMquQEKhsyvkrHixzpvyyhYSckPiQ4YE3NMeZdD8"
  }
}
```

#### initiator <--- (2018-10-16 17:13:46.435)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmSciqMaQLTmf1oxf4kA2kmohJT3Ac6AYp3vm5qmnXD1bxJf4jspCNuMCpgHsnJP3P7zPmhkhXXoU16PPQDCzHBAHgHTkTgy2tXSYUH9iDqmSsGQfT9BP9EkpoRH5WziwPw6pzjDnJgZi4q7WvyVDEXxmd4QgLiE4PUTp1tX8bPqVSXwP82yM7iaw4C4csfMbMGVc6oosrKiMxNMNGCnoJGYs4YbHiqroYKXzVYeg3nX3wgaLkU3q4crrXczxjDJ6abJXmzfJ4oNEhTdwhLU4j1dsdFJ2FUA3gVcBiCLSLcePUxsJjpvfNSEZPWLRL8VKxDEQw5hTXeLSEj6o7qC9mrg5VjR",
    "channel_id": "ch_kMPC3Q67LoMquQEKhsyvkrHixzpvyyhYSckPiQ4YE3NMeZdD8"
  }
}
```

##### initiator: (2018-10-16 17:13:48.941)
> Funding has been confirmed locally on-chain

##### responder: (2018-10-16 17:13:48.941)
> Funding has been confirmed locally on-chain

##### initiator: (2018-10-16 17:13:48.941)
> Funding has been confirmed on-chain by other party

##### responder: (2018-10-16 17:13:48.941)
> Funding has been confirmed on-chain by other party

##### initiator: (2018-10-16 17:13:48.941)
> Channel is `open` and ready to use

##### responder: (2018-10-16 17:13:48.941)
> Channel is `open` and ready to use

#### initiator ---> (2018-10-16 17:13:48.988)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "hejsan",
    "to": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb"
  }
}
```

#### responder <--- (2018-10-16 17:13:48.992)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "message": {
      "channel_id": "ch_kMPC3Q67LoMquQEKhsyvkrHixzpvyyhYSckPiQ4YE3NMeZdD8",
      "from": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "info": "hejsan",
      "to": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb"
    },
    "channel_id": "ch_kMPC3Q67LoMquQEKhsyvkrHixzpvyyhYSckPiQ4YE3NMeZdD8"
  }
}
```

#### responder ---> (2018-10-16 17:13:48.993)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "svejsan",
    "to": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7"
  }
}
```

#### initiator <--- (2018-10-16 17:13:48.996)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "message": {
      "channel_id": "ch_kMPC3Q67LoMquQEKhsyvkrHixzpvyyhYSckPiQ4YE3NMeZdD8",
      "from": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "info": "svejsan",
      "to": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7"
    },
    "channel_id": "ch_kMPC3Q67LoMquQEKhsyvkrHixzpvyyhYSckPiQ4YE3NMeZdD8"
  }
}
```

#### initiator ---> (2018-10-16 17:13:48.996)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "first message in a row",
    "to": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb"
  }
}
```

#### responder <--- (2018-10-16 17:13:48.998)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "message": {
      "channel_id": "ch_kMPC3Q67LoMquQEKhsyvkrHixzpvyyhYSckPiQ4YE3NMeZdD8",
      "from": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "info": "first message in a row",
      "to": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb"
    },
    "channel_id": "ch_kMPC3Q67LoMquQEKhsyvkrHixzpvyyhYSckPiQ4YE3NMeZdD8"
  }
}
```

#### initiator ---> (2018-10-16 17:13:48.999)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "second message in a row",
    "to": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb"
  }
}
```

#### responder <--- (2018-10-16 17:13:49.48)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "message": {
      "channel_id": "ch_kMPC3Q67LoMquQEKhsyvkrHixzpvyyhYSckPiQ4YE3NMeZdD8",
      "from": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "info": "second message in a row",
      "to": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb"
    },
    "channel_id": "ch_kMPC3Q67LoMquQEKhsyvkrHixzpvyyhYSckPiQ4YE3NMeZdD8"
  }
}
```

#### responder ---> (2018-10-16 17:13:49.49)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "some message",
    "to": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7"
  }
}
```

#### initiator <--- (2018-10-16 17:13:49.54)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "message": {
      "channel_id": "ch_kMPC3Q67LoMquQEKhsyvkrHixzpvyyhYSckPiQ4YE3NMeZdD8",
      "from": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "info": "some message",
      "to": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7"
    },
    "channel_id": "ch_kMPC3Q67LoMquQEKhsyvkrHixzpvyyhYSckPiQ4YE3NMeZdD8"
  }
}
```

#### responder ---> (2018-10-16 17:13:49.55)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "other message",
    "to": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7"
  }
}
```

#### initiator <--- (2018-10-16 17:13:49.98)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "message": {
      "channel_id": "ch_kMPC3Q67LoMquQEKhsyvkrHixzpvyyhYSckPiQ4YE3NMeZdD8",
      "from": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "info": "other message",
      "to": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7"
    },
    "channel_id": "ch_kMPC3Q67LoMquQEKhsyvkrHixzpvyyhYSckPiQ4YE3NMeZdD8"
  }
}
```

#### initiator init (2018-10-16 17:13:49.198)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb&role=initiator
```

#### responder init (2018-10-16 17:13:49.202)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb&role=responder
```

#### responder <--- (2018-10-16 17:13:50.204)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 17:13:50.207)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 17:13:50.216)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpALGJSrzwTy6oub8Qv4su7RMx2hck9JNUEgjtyU6qrUG48oB7x4ucqxPokv4rA4P5zaAWfi6eCujMzNBvMMu3xP8p9Svn5xM77VDy3ntvSFDRTNLxquqDLKr53dA7VoLQyju8FB1sKcPCeRhzzU2bUngSvnzpspL"
  }
}
```

#### initiator ---> (2018-10-16 17:13:50.253)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4Hn9XzuAQziwd23yY9HmAHWPakKyFuoWmaY7soPuzETMoC1esG4GGtZds6gDHkSJ5McB3gjmMBFygctYDGCXkttmFuXVA3uKCXANUrAL2maaUsyzJ4KT7kLZ6SMv1XCzeM3NtrmMKh8UKrKRjWKwcYh43bKZWceYPhGJNFjYyxLqKAZq5VoRH6k2HSWp3icyJnJkP9ZHSg3CcveeSPMyySw3UzyphNMxw4ABJnFZNr1oQSx8aph8pCfnZ7bZQ6wiEM"
  }
}
```

#### responder <--- (2018-10-16 17:13:50.254)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 17:13:50.255)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpALGJSrzwTy6oub8Qv4su7RMx2hck9JNUEgjtyU6qrUG48oB7x4ucqxPokv4rA4P5zaAWfi6eCujMzNBvMMu3xP8p9Svn5xM77VDy3ntvSFDRTNLxquqDLKr53dA7VoLQyju8FB1sKcPCeRhzzU2bUngSvnzpspL"
  }
}
```

#### responder ---> (2018-10-16 17:13:50.256)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4Hn6N9s1gmwXrLo337FFPLqhJkJnxiUb3tFFWxjnFttqFPzBJbspASoLJ3h8jdrHEi8ywgu7SYj1Ldj3b8DwENKb7zURft2s2zzx2bGfcrT3jePGyCbUmPwro4qtEnBHMLR58G2cKXTAev9Km55N1f6Nqqb4M3gNBNC7SGcARSVi9S6NSob56xKoXs41N3w7H9WaTm3xb73HTaT65HfS8rtXjNNjgeCgVBK6TZeXgqwrEevDF8sQahJQYoU8fe12cV"
  }
}
```

#### initiator <--- (2018-10-16 17:13:50.257)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 17:13:50.257)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmRoeQiSeA7nNxdvEeC2SMWfCaGp7TfRsD3JHMCFVUed1DF5TBhWCpXg7HM2NzvH26hvoijo31Fr6DVHUPLcgQA1e9fF91TPZnCR2GNuYjzCEYz5uwMhr52fRYP7dRF2FBhtcPpMZhJu8c78w9iVKMVeULt9zuMYbQebNyKeAHYkCmHzNjY6KfHZhTkfa2GZdDmkx2zQir6AJhuTH82TN7gCMTcNsZHUsesCe8F2qvPsPr3Zkzmz9z1ayFnbNfWSHnkghUUXPTj3GGKZnJMpePTKSRxZbzP34mVAFkV4mVTKLEM5EWgxZpn5RBJnj2asRx4CesPLv5wKkbkZWK8atAKQiQJ1"
  }
}
```

#### initiator <--- (2018-10-16 17:13:50.258)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmRoeQiSeA7nNxdvEeC2SMWfCaGp7TfRsD3JHMCFVUed1DF5TBhWCpXg7HM2NzvH26hvoijo31Fr6DVHUPLcgQA1e9fF91TPZnCR2GNuYjzCEYz5uwMhr52fRYP7dRF2FBhtcPpMZhJu8c78w9iVKMVeULt9zuMYbQebNyKeAHYkCmHzNjY6KfHZhTkfa2GZdDmkx2zQir6AJhuTH82TN7gCMTcNsZHUsesCe8F2qvPsPr3Zkzmz9z1ayFnbNfWSHnkghUUXPTj3GGKZnJMpePTKSRxZbzP34mVAFkV4mVTKLEM5EWgxZpn5RBJnj2asRx4CesPLv5wKkbkZWK8atAKQiQJ1"
  }
}
```

#### initiator <--- (2018-10-16 17:13:50.913)
```javascript
{
  "id": -576460752303423475,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 699
    },
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 401
    }
  ]
}
```

#### initiator <--- (2018-10-16 17:13:52.669)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_frPFGHKJBuod8SkxEms4F1BQgBUAGJG7QSf8GigMDaiRwVXnK"
  }
}
```

#### responder <--- (2018-10-16 17:13:52.669)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_frPFGHKJBuod8SkxEms4F1BQgBUAGJG7QSf8GigMDaiRwVXnK"
  }
}
```

#### responder <--- (2018-10-16 17:13:52.670)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_frPFGHKJBuod8SkxEms4F1BQgBUAGJG7QSf8GigMDaiRwVXnK"
  }
}
```

#### initiator <--- (2018-10-16 17:13:52.670)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_frPFGHKJBuod8SkxEms4F1BQgBUAGJG7QSf8GigMDaiRwVXnK"
  }
}
```

#### responder <--- (2018-10-16 17:13:52.674)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_frPFGHKJBuod8SkxEms4F1BQgBUAGJG7QSf8GigMDaiRwVXnK"
  }
}
```

#### initiator <--- (2018-10-16 17:13:52.674)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_frPFGHKJBuod8SkxEms4F1BQgBUAGJG7QSf8GigMDaiRwVXnK"
  }
}
```

#### responder <--- (2018-10-16 17:13:52.675)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmRoeQiSeA7nNxdvEeC2SMWfCaGp7TfRsD3JHMCFVUed1DF5TBhWCpXg7HM2NzvH26hvoijo31Fr6DVHUPLcgQA1e9fF91TPZnCR2GNuYjzCEYz5uwMhr52fRYP7dRF2FBhtcPpMZhJu8c78w9iVKMVeULt9zuMYbQebNyKeAHYkCmHzNjY6KfHZhTkfa2GZdDmkx2zQir6AJhuTH82TN7gCMTcNsZHUsesCe8F2qvPsPr3Zkzmz9z1ayFnbNfWSHnkghUUXPTj3GGKZnJMpePTKSRxZbzP34mVAFkV4mVTKLEM5EWgxZpn5RBJnj2asRx4CesPLv5wKkbkZWK8atAKQiQJ1",
    "channel_id": "ch_frPFGHKJBuod8SkxEms4F1BQgBUAGJG7QSf8GigMDaiRwVXnK"
  }
}
```

#### initiator <--- (2018-10-16 17:13:52.676)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmRoeQiSeA7nNxdvEeC2SMWfCaGp7TfRsD3JHMCFVUed1DF5TBhWCpXg7HM2NzvH26hvoijo31Fr6DVHUPLcgQA1e9fF91TPZnCR2GNuYjzCEYz5uwMhr52fRYP7dRF2FBhtcPpMZhJu8c78w9iVKMVeULt9zuMYbQebNyKeAHYkCmHzNjY6KfHZhTkfa2GZdDmkx2zQir6AJhuTH82TN7gCMTcNsZHUsesCe8F2qvPsPr3Zkzmz9z1ayFnbNfWSHnkghUUXPTj3GGKZnJMpePTKSRxZbzP34mVAFkV4mVTKLEM5EWgxZpn5RBJnj2asRx4CesPLv5wKkbkZWK8atAKQiQJ1",
    "channel_id": "ch_frPFGHKJBuod8SkxEms4F1BQgBUAGJG7QSf8GigMDaiRwVXnK"
  }
}
```

##### initiator: (2018-10-16 17:13:53.281)
> Funding has been confirmed locally on-chain

##### responder: (2018-10-16 17:13:53.281)
> Funding has been confirmed locally on-chain

##### initiator: (2018-10-16 17:13:53.281)
> Funding has been confirmed on-chain by other party

##### responder: (2018-10-16 17:13:53.281)
> Funding has been confirmed on-chain by other party

##### initiator: (2018-10-16 17:13:53.281)
> Channel is `open` and ready to use

##### responder: (2018-10-16 17:13:53.281)
> Channel is `open` and ready to use

#### initiator ---> (2018-10-16 17:13:53.321)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
    "to": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb"
  }
}
```

#### responder ---> (2018-10-16 17:13:53.321)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 2,
    "from": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
    "to": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb"
  }
}
```

#### responder <--- (2018-10-16 17:13:53.333)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQPhAm1EBLD2sfUS8LXy3Qa3LLyYjEpBQCmhZ5kfwoPQGgkqUAQ1U9KxWd1d83udg6pvGSnGKZoi114cuHAGPy2Bss2YZ3cDCrePdYjxpGjpn6KUUnvyKY9VekTc2yUcNsZpRHW8h66LkTjbCegZxksDcTLCQZj5BiEFJZz4NvWrYyzzFHHHghXjNWLKc85omdinwzacqzsHtT"
  }
}
```

#### initiator <--- (2018-10-16 17:13:53.334)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQPhAm1EBLD2sfUS8LXy3Qa3LLyYjEpBQCmhZ5kfwoPQGgkqUAQ1U9KxWd1d83udg6pvGSnGKZoi114cuHAGPy2Bss2YZ3cDCrePdYjxpGjpn6KUUnvyKY9VekTc2yUcNsZpRHW8h66LkTjbCegZxksDcTL3otKE8wQu2jKoamCiiqzmW5hwUfnN5BFMcLTJwDR6DMoVSuZxJF"
  }
}
```

#### initiator ---> (2018-10-16 17:13:53.338)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4ksoQxAWrRY5im9KqexYaMNzJrLFTuXDTRwQzqv7MHaghmE98JEj4jfe7XF8DJNdNj6kjZFfLpZyoLZRDhPvq7gYLusbx6vcePCGTzTMTHySQKFp9CvS5rdSUFQNEpvyeD548QLdQDLGgT5KkBjJ4367zVEd57KsWVdMGqbi8wxigwBjxdWXH1WVUMJmDd6FiD5ju1ZcywTQxXHcS9nZZdFDyqBqk5sFEydmrwc4H3Hg5GizQMnNhaneDNQL4uiKK4aXCTFq2SYc6gewL29zy79yd5zaeLceZxAS2Tkr2z8KHFg"
  }
}
```

#### responder ---> (2018-10-16 17:13:53.339)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4pYG6mMoM1iUgztnGobAc4j9Jd79srgdsQsW1AQqjn7Btb6129UG2yazf3ArcYfkHGorFE5WWNXzm254KPFTPrAagpMhkiBAc2DPqwYvXA8YRvKDBiwz9LqzZAuHy72wMXSyiSWSJBhEkiSD1odJRA3t5hWnCVJjp1s2KhNTBmBVZcc9L17M6o8uoBMq4moKpCfYQkpqtDkVfWYJMEnzdN2JsunXxJbVxkoAiawWHDtAKDE2NFKPweUjUS5yoGD1QxRfebZbrYH4kQoMsZJHDKyEM2S1819Q73n2TgQ3ADgdUeM"
  }
}
```

#### responder <--- (2018-10-16 17:13:53.343)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_frPFGHKJBuod8SkxEms4F1BQgBUAGJG7QSf8GigMDaiRwVXnK",
    "round": 1
  }
}
```

#### initiator <--- (2018-10-16 17:13:53.344)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_frPFGHKJBuod8SkxEms4F1BQgBUAGJG7QSf8GigMDaiRwVXnK",
    "round": 1
  }
}
```

#### responder ---> (2018-10-16 17:13:53.345)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
    "to": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7"
  }
}
```

#### initiator ---> (2018-10-16 17:13:53.345)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 2,
    "from": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
    "to": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7"
  }
}
```

#### initiator <--- (2018-10-16 17:13:53.351)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQPhAm1EBLD2sfUS8LXy3Qa3LLyYjEpBQCmhZ5kfwoPQGgkqUAQ1U9KxWd1d83ueWSVfkVKH6L6KkV9T2gLNvC8y1Tey5W4Upumb5vyNgBMCJwkgsW9ASmBKCLM1xwbmK69vYuPvjGzKDenoHAha85ojBaeUoawFvx475SHvDcw3UpoX9tXUnzABQpFqK69v7x5TJHtiJ6n1Nu"
  }
}
```

#### responder <--- (2018-10-16 17:13:53.351)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQPhAm1EBLD2sfUS8LXy3Qa3LLyYjEpBQCmhZ5kfwoPQGgkqUAQ1U9KxWd1d83ueWSVfkVKH6L6KkV9T2gLNvC8y1Tey5W4Upumb5vyNgBMCJwkgsW9ASmBKCLM1xwbmK69vYuPvjGzKDenoHAha85ojBaeLE1iXhoqoNw9zzzYGyA9xz2XheMQJVhC3fMbea2VBSMNnjLmCYQ"
  }
}
```

#### responder ---> (2018-10-16 17:13:53.354)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4vxSnyZRvgurQ36nNev38XAujbaRA2PZkWpewGnuenQEc2rkeFanwLqkiVDMrnfqhCQ9RuqW96jDBxaM5YfAedizrL336Kx43PMUYNoU2b9ffnFWL9Sb95dMsNkDrctfuy9YLqMBNsXwm4EfKviMTnqhVvvr2mJkeH1Vp9Wek8o76pXWGwn67uLLAndsYZpGMuAy1uS5NRNwwFewDA87mGZcBcPQUyQvYXiHxpTU9pwiTWxrbzD7b1DXMYS1cueyqoJHYWsmiwzwFBMZPNF1jRpDrcHGUKdacrrPSbhMzaZWDii"
  }
}
```

#### initiator ---> (2018-10-16 17:13:53.354)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4zN7nchAxVYT6WdLe3o4rQws1ujUBhC8XpstHTSFJSUPPi3PoLHoEWWTrT58g6KoW7bK4XugUgwr2DK7P6WZqFLxNwK2jNwp193ZFQEPBtjKrVRZGX5RrZxmzyQTWipUk7WRGMumQTMmhSscbjY1hBQfzHAMEjo1aqHU4EVmqX2nWrNx9fQAhaz5EksNEGqKETAyKgDKB6qFAmpGaR1xfW7KRdQLXz99gsBEp3pfCjzdiMNp8p7s3ZjfuVwQ8tD5WWqqabtDU1bevUmz7bon4hhgrqVVv521p28BTSx8f9kYdb7"
  }
}
```

#### initiator <--- (2018-10-16 17:13:53.355)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_frPFGHKJBuod8SkxEms4F1BQgBUAGJG7QSf8GigMDaiRwVXnK",
    "round": 1
  }
}
```

#### responder <--- (2018-10-16 17:13:53.356)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_frPFGHKJBuod8SkxEms4F1BQgBUAGJG7QSf8GigMDaiRwVXnK",
    "round": 1
  }
}
```
