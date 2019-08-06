
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L&lock_period=10&port=13088&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z&role=initiator
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L&lock_period=10&port=13088&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z&role=responder
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAZxE4sRXleyuZJdSWPuGHyKOnkWnoPmbtlcg3MH86BRGhj+qJSJgAKEBJuX4qPbJ53aRWBQiJB1xfrD5fTi2f0L3naOFIUL69nKGJGE5yoAAAgoAhhAGeddIAMCgXYZHv3SD+m03lkfOmfKjpATk5PV+AaqRnntKZcFB/XsAXmnJ4A==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422430,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+QFuCwHAuQFo+QFlUQGhAZxE4sRXleyuZJdSWPuGHyKOnkWnoPmbtlcg3MH86BRGuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiK+IgLAcC4g/iBMgGhAZxE4sRXleyuZJdSWPuGHyKOnkWnoPmbtlcg3MH86BRGhj+qJSJgAKEBJuX4qPbJ53aRWBQiJB1xfrD5fTi2f0L3naOFIUL69nKGJGE5yoAAAgoAhhAGeddIAMCgXYZHv3SD+m03lkfOmfKjpATk5PV+AaqRnntKZcFB/XsAuCqAsg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422430,
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
      "signed_tx": "tx_+QFuCwHAuQFo+QFlUQGhAZxE4sRXleyuZJdSWPuGHyKOnkWnoPmbtlcg3MH86BRGuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiK+IgLAcC4g/iBMgGhAZxE4sRXleyuZJdSWPuGHyKOnkWnoPmbtlcg3MH86BRGhj+qJSJgAKEBJuX4qPbJ53aRWBQiJB1xfrD5fTi2f0L3naOFIUL69nKGJGE5yoAAAgoAhhAGeddIAMCgXYZHv3SD+m03lkfOmfKjpATk5PV+AaqRnntKZcFB/XsAuCqAsg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422429,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QJWCwHAuQJQ+QJNUQGhASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBcfkBbgsBwLkBaPkBZVEBoQGcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURrigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQGcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURoY/qiUiYAChASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyhiRhOcqAAAIKAIYQBnnXSADAoF2GR790g/ptN5ZHzpnyo6QE5OT1fgGqkZ57SmXBQf17AH7/Q+M="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422429,
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
    "channel_id": null,
    "data": {
      "info": "funding_created",
      "tx": "tx_+QJWCwHAuQJQ+QJNUQGhASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBcfkBbgsBwLkBaPkBZVEBoQGcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURrigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQGcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURoY/qiUiYAChASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyhiRhOcqAAAIKAIYQBnnXSADAoF2GR790g/ptN5ZHzpnyo6QE5OT1fgGqkZ57SmXBQf17AH7/Q+M=",
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
    "channel_id": null,
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QJWCwHAuQJQ+QJNUQGhASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBcfkBbgsBwLkBaPkBZVEBoQGcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURrigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQGcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURoY/qiUiYAChASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyhiRhOcqAAAIKAIYQBnnXSADAoF2GR790g/ptN5ZHzpnyo6QE5OT1fgGqkZ57SmXBQf17AH7/Q+M=",
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
    "channel_id": null,
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QJWCwHAuQJQ+QJNUQGhASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBcfkBbgsBwLkBaPkBZVEBoQGcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURrigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQGcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURoY/qiUiYAChASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyhiRhOcqAAAIKAIYQBnnXSADAoF2GR790g/ptN5ZHzpnyo6QE5OT1fgGqkZ57SmXBQf17AH7/Q+M=",
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
    "channel_id": null,
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QJWCwHAuQJQ+QJNUQGhASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBcfkBbgsBwLkBaPkBZVEBoQGcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURrigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQGcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURoY/qiUiYAChASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyhiRhOcqAAAIKAIYQBnnXSADAoF2GR790g/ptN5ZHzpnyo6QE5OT1fgGqkZ57SmXBQf17AH7/Q+M=",
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
    "to": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "message": {
        "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
        "from": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
        "info": "Hello",
        "to": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z"
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
    "to": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "message": {
        "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
        "from": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
        "info": "Hello back",
        "to": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422428,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
      "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422428,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
      "balance": 69999999999999
    },
    {
      "account": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "state": "tx_+QJWCwHAuQJQ+QJNUQGhASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBcfkBbgsBwLkBaPkBZVEBoQGcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURrigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQGcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURoY/qiUiYAChASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyhiRhOcqAAAIKAIYQBnnXSADAoF2GR790g/ptN5ZHzpnyo6QE5OT1fgGqkZ57SmXBQf17AH7/Q+M="
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "state": "tx_+QJWCwHAuQJQ+QJNUQGhASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBcfkBbgsBwLkBaPkBZVEBoQGcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURrigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQGcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURoY/qiUiYAChASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyhiRhOcqAAAIKAIYQBnnXSADAoF2GR790g/ptN5ZHzpnyo6QE5OT1fgGqkZ57SmXBQf17AH7/Q+M="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422427,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
      "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422427,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
      "balance": 69999999999999
    },
    {
      "account": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
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
    "from": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
    "to": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
        "from": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
        "to": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z"
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
    "to": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
        "to": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z"
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
    "from": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
        "from": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
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
    "from": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
    "to": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmSPy2YhJSW59CCGmiwSVEJkxcyu8DShHy8xngXtZyQyAqDxY3Pb/ka2joJnoMwPItTf85gF5M6f+En308qMbuZz/Re3rnY=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
          "op": "OffChainTransfer",
          "to": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z"
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
  "id": -576460752303422426,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAZxE4sRXleyuZJdSWPuGHyKOnkWnoPmbtlcg3MH86BRGuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBmSPy2YhJSW59CCGmiwSVEJkxcyu8DShHy8xngXtZyQyAqDxY3Pb/ka2joJnoMwPItTf85gF5M6f+En308qMbuZz/SitWQQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422426,
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAZxE4sRXleyuZJdSWPuGHyKOnkWnoPmbtlcg3MH86BRGuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBmSPy2YhJSW59CCGmiwSVEJkxcyu8DShHy8xngXtZyQyAqDxY3Pb/ka2joJnoMwPItTf85gF5M6f+En308qMbuZz/SitWQQ=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
          "op": "OffChainTransfer",
          "to": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z"
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
  "id": -576460752303422425,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQGcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURrigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZkj8tmISUlufQghposElRCZMXMrvA0oR8vMZ4F7WckMgKg8WNz2/5Gto6CZ6DMDyLU3/OYBeTOn/hJ99PKjG7mc/2tEbGw"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422425,
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQGcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURrigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZkj8tmISUlufQghposElRCZMXMrvA0oR8vMZ4F7WckMgKg8WNz2/5Gto6CZ6DMDyLU3/OYBeTOn/hJ99PKjG7mc/2tEbGw"
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQGcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURrigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZkj8tmISUlufQghposElRCZMXMrvA0oR8vMZ4F7WckMgKg8WNz2/5Gto6CZ6DMDyLU3/OYBeTOn/hJ99PKjG7mc/2tEbGw"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422424,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
      "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422424,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
      "balance": 69999999999998
    },
    {
      "account": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422423,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422423,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQGcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURrigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZkj8tmISUlufQghposElRCZMXMrvA0oR8vMZ4F7WckMgKg8WNz2/5Gto6CZ6DMDyLU3/OYBeTOn/hJ99PKjG7mc/2tEbGw",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURovKCgEAhj+qJSJf/rDvQAGgJuX4qPbJ53aRWBQiJB1xfrD5fTi2f0L3naOFIUL69nKLygoBAIYkYTnKgAJ6zYEh"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422422,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
      "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422422,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
      "balance": 40000000000002
    },
    {
      "account": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
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
    "from": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
    "to": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
        "from": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
        "to": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
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
    "to": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
        "to": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
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
    "from": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
        "from": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
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
    "from": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
    "to": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmSPy2YhJSW59CCGmiwSVEJkxcyu8DShHy8xngXtZyQyA6Bdhke/dIP6bTeWR86Z8qOkBOTk9X4BqpGee0plwUH9ezfBOXY=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
          "op": "OffChainTransfer",
          "to": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
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
  "id": -576460752303422421,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBmSPy2YhJSW59CCGmiwSVEJkxcyu8DShHy8xngXtZyQyA6Bdhke/dIP6bTeWR86Z8qOkBOTk9X4BqpGee0plwUH9e7dLrNE="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422421,
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBmSPy2YhJSW59CCGmiwSVEJkxcyu8DShHy8xngXtZyQyA6Bdhke/dIP6bTeWR86Z8qOkBOTk9X4BqpGee0plwUH9e7dLrNE=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
          "op": "OffChainTransfer",
          "to": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
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
  "id": -576460752303422420,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhAZxE4sRXleyuZJdSWPuGHyKOnkWnoPmbtlcg3MH86BRGuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEm5fio9snndpFYFCIkHXF+sPl9OLZ/Qvedo4UhQvr2crigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZkj8tmISUlufQghposElRCZMXMrvA0oR8vMZ4F7WckMgOgXYZHv3SD+m03lkfOmfKjpATk5PV+AaqRnntKZcFB/XvfNFEv"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422420,
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhAZxE4sRXleyuZJdSWPuGHyKOnkWnoPmbtlcg3MH86BRGuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEm5fio9snndpFYFCIkHXF+sPl9OLZ/Qvedo4UhQvr2crigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZkj8tmISUlufQghposElRCZMXMrvA0oR8vMZ4F7WckMgOgXYZHv3SD+m03lkfOmfKjpATk5PV+AaqRnntKZcFB/XvfNFEv"
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhAZxE4sRXleyuZJdSWPuGHyKOnkWnoPmbtlcg3MH86BRGuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEm5fio9snndpFYFCIkHXF+sPl9OLZ/Qvedo4UhQvr2crigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZkj8tmISUlufQghposElRCZMXMrvA0oR8vMZ4F7WckMgOgXYZHv3SD+m03lkfOmfKjpATk5PV+AaqRnntKZcFB/XvfNFEv"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422419,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
      "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422419,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
      "balance": 40000000000001
    },
    {
      "account": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422418,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422418,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhAZxE4sRXleyuZJdSWPuGHyKOnkWnoPmbtlcg3MH86BRGuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEm5fio9snndpFYFCIkHXF+sPl9OLZ/Qvedo4UhQvr2crigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZkj8tmISUlufQghposElRCZMXMrvA0oR8vMZ4F7WckMgOgXYZHv3SD+m03lkfOmfKjpATk5PV+AaqRnntKZcFB/XvfNFEv",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURovKCgEAhj+qJSJf/7DvQAGgJuX4qPbJ53aRWBQiJB1xfrD5fTi2f0L3naOFIUL69nKLygoBAIYkYTnKgAGQ6oEO"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422417,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
      "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422417,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
      "balance": 40000000000001
    },
    {
      "account": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
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
    "from": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
    "to": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
        "from": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
        "to": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
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
    "to": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
        "to": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
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
    "from": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
        "from": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
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
    "from": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
    "to": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmSPy2YhJSW59CCGmiwSVEJkxcyu8DShHy8xngXtZyQyBKDLFRGZPWh7dAQ17Pb7KpR46x4RPuYs1M8CXMnKRdIbAdMtQY4=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
          "op": "OffChainTransfer",
          "to": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
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
  "id": -576460752303422416,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBmSPy2YhJSW59CCGmiwSVEJkxcyu8DShHy8xngXtZyQyBKDLFRGZPWh7dAQ17Pb7KpR46x4RPuYs1M8CXMnKRdIbATe/umY="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422416,
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBmSPy2YhJSW59CCGmiwSVEJkxcyu8DShHy8xngXtZyQyBKDLFRGZPWh7dAQ17Pb7KpR46x4RPuYs1M8CXMnKRdIbATe/umY=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
          "op": "OffChainTransfer",
          "to": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
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
  "id": -576460752303422415,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhAZxE4sRXleyuZJdSWPuGHyKOnkWnoPmbtlcg3MH86BRGuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEm5fio9snndpFYFCIkHXF+sPl9OLZ/Qvedo4UhQvr2crigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZkj8tmISUlufQghposElRCZMXMrvA0oR8vMZ4F7WckMgSgyxURmT1oe3QENez2+yqUeOseET7mLNTPAlzJykXSGwHzNoOb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422415,
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhAZxE4sRXleyuZJdSWPuGHyKOnkWnoPmbtlcg3MH86BRGuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEm5fio9snndpFYFCIkHXF+sPl9OLZ/Qvedo4UhQvr2crigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZkj8tmISUlufQghposElRCZMXMrvA0oR8vMZ4F7WckMgSgyxURmT1oe3QENez2+yqUeOseET7mLNTPAlzJykXSGwHzNoOb"
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhAZxE4sRXleyuZJdSWPuGHyKOnkWnoPmbtlcg3MH86BRGuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEm5fio9snndpFYFCIkHXF+sPl9OLZ/Qvedo4UhQvr2crigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZkj8tmISUlufQghposElRCZMXMrvA0oR8vMZ4F7WckMgSgyxURmT1oe3QENez2+yqUeOseET7mLNTPAlzJykXSGwHzNoOb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422414,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
      "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422414,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
      "balance": 40000000000000
    },
    {
      "account": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422413,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422413,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhAZxE4sRXleyuZJdSWPuGHyKOnkWnoPmbtlcg3MH86BRGuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEm5fio9snndpFYFCIkHXF+sPl9OLZ/Qvedo4UhQvr2crigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZkj8tmISUlufQghposElRCZMXMrvA0oR8vMZ4F7WckMgSgyxURmT1oe3QENez2+yqUeOseET7mLNTPAlzJykXSGwHzNoOb",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURovKCgEAhj+qJSJgALDvQAGgJuX4qPbJ53aRWBQiJB1xfrD5fTi2f0L3naOFIUL69nKLygoBAIYkYTnKgACWjWlh"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422412,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
      "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422412,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
      "balance": 70000000000000
    },
    {
      "account": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
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
    "from": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
    "to": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
        "from": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
        "to": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z"
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
    "to": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
        "to": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z"
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
    "from": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
        "from": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
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
    "from": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
    "to": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmSPy2YhJSW59CCGmiwSVEJkxcyu8DShHy8xngXtZyQyBaBdhke/dIP6bTeWR86Z8qOkBOTk9X4BqpGee0plwUH9e9DbMgg=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
          "op": "OffChainTransfer",
          "to": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z"
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
  "id": -576460752303422411,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAZxE4sRXleyuZJdSWPuGHyKOnkWnoPmbtlcg3MH86BRGuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBmSPy2YhJSW59CCGmiwSVEJkxcyu8DShHy8xngXtZyQyBaBdhke/dIP6bTeWR86Z8qOkBOTk9X4BqpGee0plwUH9e83pi3U="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422411,
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAZxE4sRXleyuZJdSWPuGHyKOnkWnoPmbtlcg3MH86BRGuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBmSPy2YhJSW59CCGmiwSVEJkxcyu8DShHy8xngXtZyQyBaBdhke/dIP6bTeWR86Z8qOkBOTk9X4BqpGee0plwUH9e83pi3U=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
          "op": "OffChainTransfer",
          "to": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z"
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
  "id": -576460752303422410,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQGcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURrigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZkj8tmISUlufQghposElRCZMXMrvA0oR8vMZ4F7WckMgWgXYZHv3SD+m03lkfOmfKjpATk5PV+AaqRnntKZcFB/Xvm07qv"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422410,
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQGcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURrigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZkj8tmISUlufQghposElRCZMXMrvA0oR8vMZ4F7WckMgWgXYZHv3SD+m03lkfOmfKjpATk5PV+AaqRnntKZcFB/Xvm07qv"
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQGcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURrigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZkj8tmISUlufQghposElRCZMXMrvA0oR8vMZ4F7WckMgWgXYZHv3SD+m03lkfOmfKjpATk5PV+AaqRnntKZcFB/Xvm07qv"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422409,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
      "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422409,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
      "balance": 69999999999999
    },
    {
      "account": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422408,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422408,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQGcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURrigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZkj8tmISUlufQghposElRCZMXMrvA0oR8vMZ4F7WckMgWgXYZHv3SD+m03lkfOmfKjpATk5PV+AaqRnntKZcFB/Xvm07qv",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURovKCgEAhj+qJSJf/7DvQAGgJuX4qPbJ53aRWBQiJB1xfrD5fTi2f0L3naOFIUL69nKLygoBAIYkYTnKgAGQ6oEO"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422407,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
      "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422407,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
      "balance": 40000000000001
    },
    {
      "account": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
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
    "from": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
    "to": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
        "from": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
        "to": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
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
    "to": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
        "to": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
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
    "from": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
        "from": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
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
    "from": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
    "to": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmSPy2YhJSW59CCGmiwSVEJkxcyu8DShHy8xngXtZyQyBqDLFRGZPWh7dAQ17Pb7KpR46x4RPuYs1M8CXMnKRdIbAeDV4E8=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
          "op": "OffChainTransfer",
          "to": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
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
  "id": -576460752303422406,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBmSPy2YhJSW59CCGmiwSVEJkxcyu8DShHy8xngXtZyQyBqDLFRGZPWh7dAQ17Pb7KpR46x4RPuYs1M8CXMnKRdIbAfSc5e4="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422406,
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhASbl+Kj2yed2kVgUIiQdcX6w+X04tn9C952jhSFC+vZyuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBmSPy2YhJSW59CCGmiwSVEJkxcyu8DShHy8xngXtZyQyBqDLFRGZPWh7dAQ17Pb7KpR46x4RPuYs1M8CXMnKRdIbAfSc5e4=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
          "op": "OffChainTransfer",
          "to": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
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
  "id": -576460752303422405,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhAZxE4sRXleyuZJdSWPuGHyKOnkWnoPmbtlcg3MH86BRGuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEm5fio9snndpFYFCIkHXF+sPl9OLZ/Qvedo4UhQvr2crigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZkj8tmISUlufQghposElRCZMXMrvA0oR8vMZ4F7WckMgagyxURmT1oe3QENez2+yqUeOseET7mLNTPAlzJykXSGwGzBHM0"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422405,
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhAZxE4sRXleyuZJdSWPuGHyKOnkWnoPmbtlcg3MH86BRGuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEm5fio9snndpFYFCIkHXF+sPl9OLZ/Qvedo4UhQvr2crigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZkj8tmISUlufQghposElRCZMXMrvA0oR8vMZ4F7WckMgagyxURmT1oe3QENez2+yqUeOseET7mLNTPAlzJykXSGwGzBHM0"
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
    "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhAZxE4sRXleyuZJdSWPuGHyKOnkWnoPmbtlcg3MH86BRGuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEm5fio9snndpFYFCIkHXF+sPl9OLZ/Qvedo4UhQvr2crigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZkj8tmISUlufQghposElRCZMXMrvA0oR8vMZ4F7WckMgagyxURmT1oe3QENez2+yqUeOseET7mLNTPAlzJykXSGwGzBHM0"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422404,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
      "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422404,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_J8c7xoEVvmtpCmG4r6TEa4o58CfF995B9SdTBg8Coa5CPpd5z",
      "balance": 40000000000000
    },
    {
      "account": "ak_2Bpgg8ZHXRvvzymUfxX2k4By2REUGFLPFuaWEHPkWTjKBWhR8L",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422403,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mHiPXDuurxdAm2W7om79gqPCdWWTVC4PyVtjAzY3G5YDm5394",
  "id": -576460752303422403,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhAZxE4sRXleyuZJdSWPuGHyKOnkWnoPmbtlcg3MH86BRGuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEm5fio9snndpFYFCIkHXF+sPl9OLZ/Qvedo4UhQvr2crigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZkj8tmISUlufQghposElRCZMXMrvA0oR8vMZ4F7WckMgagyxURmT1oe3QENez2+yqUeOseET7mLNTPAlzJykXSGwGzBHM0",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCcROLEV5XsrmSXUlj7hh8ijp5Fp6D5m7ZXINzB/OgURovKCgEAhj+qJSJgALDvQAGgJuX4qPbJ53aRWBQiJB1xfrD5fTi2f0L3naOFIUL69nKLygoBAIYkYTnKgACWjWlh"
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u&lock_period=10&port=12524&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM&role=initiator
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u&lock_period=10&port=12524&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM&role=responder
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhATrfgFGxCEtoSdkeoALbeiaaTA5oMVJnz4CXbP1qmGpEhj+qJSJgAKEBLxgk0pazPotWRZlfppzl0ayj74QXWNlHHfdfJoaYvC2GJGE5yoAAAgoAhhAGeddIAMCgULRdJdq+nS/LHFAT1RiwCr4CtC/Q+pYj3so9dkfn7OMAsOEI2w==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421519,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+NQLAcC4z/jNUQGhATrfgFGxCEtoSdkeoALbeiaaTA5oMVJnz4CXbP1qmGpEiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQE634BRsQhLaEnZHqAC23ommkwOaDFSZ8+Al2z9aphqRIY/qiUiYAChAS8YJNKWsz6LVkWZX6ac5dGso++EF1jZRx33XyaGmLwthiRhOcqAAAIKAIYQBnnXSADAoFC0XSXavp0vyxxQE9UYsAq+ArQv0PqWI97KPXZH5+zjAPBJ3nQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421519,
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
      "signed_tx": "tx_+NQLAcC4z/jNUQGhATrfgFGxCEtoSdkeoALbeiaaTA5oMVJnz4CXbP1qmGpEiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQE634BRsQhLaEnZHqAC23ommkwOaDFSZ8+Al2z9aphqRIY/qiUiYAChAS8YJNKWsz6LVkWZX6ac5dGso++EF1jZRx33XyaGmLwthiRhOcqAAAIKAIYQBnnXSADAoFC0XSXavp0vyxxQE9UYsAq+ArQv0PqWI97KPXZH5+zjAPBJ3nQ=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421518,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEiCwHAuQEc+QEZUQGhAS8YJNKWsz6LVkWZX6ac5dGso++EF1jZRx33XyaGmLwtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQE634BRsQhLaEnZHqAC23ommkwOaDFSZ8+Al2z9aphqRIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBOt+AUbEIS2hJ2R6gAtt6JppMDmgxUmfPgJds/WqYakSGP6olImAAoQEvGCTSlrM+i1ZFmV+mnOXRrKPvhBdY2Ucd918mhpi8LYYkYTnKgAACCgCGEAZ510gAwKBQtF0l2r6dL8scUBPVGLAKvgK0L9D6liPeyj12R+fs4wBwqa+7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421518,
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
    "channel_id": null,
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEiCwHAuQEc+QEZUQGhAS8YJNKWsz6LVkWZX6ac5dGso++EF1jZRx33XyaGmLwtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQE634BRsQhLaEnZHqAC23ommkwOaDFSZ8+Al2z9aphqRIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBOt+AUbEIS2hJ2R6gAtt6JppMDmgxUmfPgJds/WqYakSGP6olImAAoQEvGCTSlrM+i1ZFmV+mnOXRrKPvhBdY2Ucd918mhpi8LYYkYTnKgAACCgCGEAZ510gAwKBQtF0l2r6dL8scUBPVGLAKvgK0L9D6liPeyj12R+fs4wBwqa+7",
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
    "channel_id": null,
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEiCwHAuQEc+QEZUQGhAS8YJNKWsz6LVkWZX6ac5dGso++EF1jZRx33XyaGmLwtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQE634BRsQhLaEnZHqAC23ommkwOaDFSZ8+Al2z9aphqRIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBOt+AUbEIS2hJ2R6gAtt6JppMDmgxUmfPgJds/WqYakSGP6olImAAoQEvGCTSlrM+i1ZFmV+mnOXRrKPvhBdY2Ucd918mhpi8LYYkYTnKgAACCgCGEAZ510gAwKBQtF0l2r6dL8scUBPVGLAKvgK0L9D6liPeyj12R+fs4wBwqa+7",
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
    "channel_id": null,
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEiCwHAuQEc+QEZUQGhAS8YJNKWsz6LVkWZX6ac5dGso++EF1jZRx33XyaGmLwtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQE634BRsQhLaEnZHqAC23ommkwOaDFSZ8+Al2z9aphqRIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBOt+AUbEIS2hJ2R6gAtt6JppMDmgxUmfPgJds/WqYakSGP6olImAAoQEvGCTSlrM+i1ZFmV+mnOXRrKPvhBdY2Ucd918mhpi8LYYkYTnKgAACCgCGEAZ510gAwKBQtF0l2r6dL8scUBPVGLAKvgK0L9D6liPeyj12R+fs4wBwqa+7",
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
    "channel_id": null,
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEiCwHAuQEc+QEZUQGhAS8YJNKWsz6LVkWZX6ac5dGso++EF1jZRx33XyaGmLwtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQE634BRsQhLaEnZHqAC23ommkwOaDFSZ8+Al2z9aphqRIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBOt+AUbEIS2hJ2R6gAtt6JppMDmgxUmfPgJds/WqYakSGP6olImAAoQEvGCTSlrM+i1ZFmV+mnOXRrKPvhBdY2Ucd918mhpi8LYYkYTnKgAACCgCGEAZ510gAwKBQtF0l2r6dL8scUBPVGLAKvgK0L9D6liPeyj12R+fs4wBwqa+7",
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
    "to": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "message": {
        "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
        "from": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
        "info": "Hello",
        "to": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM"
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
    "to": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "message": {
        "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
        "from": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
        "info": "Hello back",
        "to": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421517,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
      "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421517,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
      "balance": 69999999999999
    },
    {
      "account": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "state": "tx_+QEiCwHAuQEc+QEZUQGhAS8YJNKWsz6LVkWZX6ac5dGso++EF1jZRx33XyaGmLwtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQE634BRsQhLaEnZHqAC23ommkwOaDFSZ8+Al2z9aphqRIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBOt+AUbEIS2hJ2R6gAtt6JppMDmgxUmfPgJds/WqYakSGP6olImAAoQEvGCTSlrM+i1ZFmV+mnOXRrKPvhBdY2Ucd918mhpi8LYYkYTnKgAACCgCGEAZ510gAwKBQtF0l2r6dL8scUBPVGLAKvgK0L9D6liPeyj12R+fs4wBwqa+7"
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "state": "tx_+QEiCwHAuQEc+QEZUQGhAS8YJNKWsz6LVkWZX6ac5dGso++EF1jZRx33XyaGmLwtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQE634BRsQhLaEnZHqAC23ommkwOaDFSZ8+Al2z9aphqRIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBOt+AUbEIS2hJ2R6gAtt6JppMDmgxUmfPgJds/WqYakSGP6olImAAoQEvGCTSlrM+i1ZFmV+mnOXRrKPvhBdY2Ucd918mhpi8LYYkYTnKgAACCgCGEAZ510gAwKBQtF0l2r6dL8scUBPVGLAKvgK0L9D6liPeyj12R+fs4wBwqa+7"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421516,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
      "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421516,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
      "balance": 69999999999999
    },
    {
      "account": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
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
    "from": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
    "to": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
        "from": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
        "to": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM"
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
    "to": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
        "to": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM"
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
    "from": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
        "from": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
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
    "from": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
    "to": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvuyQJaRPIHbho29m3XOuKnqc3s97R5B6JGOq3z9O8RAAqCSY0OSV7RD9ivsIqLHurqQ54rWkK6TteqfPrJVqRRDVJJEOy8=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
          "op": "OffChainTransfer",
          "to": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM"
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
  "id": -576460752303421515,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhATrfgFGxCEtoSdkeoALbeiaaTA5oMVJnz4CXbP1qmGpEiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQb7skCWkTyB24aNvZt1zrip6nN7Pe0eQeiRjqt8/TvEQAKgkmNDkle0Q/Yr7CKix7q6kOeK1pCuk7Xqnz6yVakUQ1SCQ6q2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421515,
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhATrfgFGxCEtoSdkeoALbeiaaTA5oMVJnz4CXbP1qmGpEiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQb7skCWkTyB24aNvZt1zrip6nN7Pe0eQeiRjqt8/TvEQAKgkmNDkle0Q/Yr7CKix7q6kOeK1pCuk7Xqnz6yVakUQ1SCQ6q2",
      "updates": [
        {
          "amount": 1,
          "from": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
          "op": "OffChainTransfer",
          "to": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM"
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
  "id": -576460752303421514,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhAS8YJNKWsz6LVkWZX6ac5dGso++EF1jZRx33XyaGmLwtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQE634BRsQhLaEnZHqAC23ommkwOaDFSZ8+Al2z9aphqRIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEG+7JAlpE8gduGjb2bdc64qepzez3tHkHokY6rfP07xEACoJJjQ5JXtEP2K+wiose6upDnitaQrpO16p8+slWpFENUHGgMgg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421514,
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAS8YJNKWsz6LVkWZX6ac5dGso++EF1jZRx33XyaGmLwtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQE634BRsQhLaEnZHqAC23ommkwOaDFSZ8+Al2z9aphqRIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEG+7JAlpE8gduGjb2bdc64qepzez3tHkHokY6rfP07xEACoJJjQ5JXtEP2K+wiose6upDnitaQrpO16p8+slWpFENUHGgMgg=="
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAS8YJNKWsz6LVkWZX6ac5dGso++EF1jZRx33XyaGmLwtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQE634BRsQhLaEnZHqAC23ommkwOaDFSZ8+Al2z9aphqRIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEG+7JAlpE8gduGjb2bdc64qepzez3tHkHokY6rfP07xEACoJJjQ5JXtEP2K+wiose6upDnitaQrpO16p8+slWpFENUHGgMgg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421513,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
      "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421513,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
      "balance": 69999999999998
    },
    {
      "account": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421512,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421512,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhAS8YJNKWsz6LVkWZX6ac5dGso++EF1jZRx33XyaGmLwtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQE634BRsQhLaEnZHqAC23ommkwOaDFSZ8+Al2z9aphqRIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEG+7JAlpE8gduGjb2bdc64qepzez3tHkHokY6rfP07xEACoJJjQ5JXtEP2K+wiose6upDnitaQrpO16p8+slWpFENUHGgMgg==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaA634BRsQhLaEnZHqAC23ommkwOaDFSZ8+Al2z9aphqRIvKCgEAhj+qJSJf/rDvQAGgLxgk0pazPotWRZlfppzl0ayj74QXWNlHHfdfJoaYvC2LygoBAIYkYTnKgAJWz8BZ"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421511,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
      "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421511,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
      "balance": 40000000000002
    },
    {
      "account": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
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
    "from": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
    "to": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
        "from": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
        "to": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
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
    "to": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
        "to": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
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
    "from": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
        "from": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
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
    "from": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
    "to": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvuyQJaRPIHbho29m3XOuKnqc3s97R5B6JGOq3z9O8RAA6BQtF0l2r6dL8scUBPVGLAKvgK0L9D6liPeyj12R+fs413wscM=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
          "op": "OffChainTransfer",
          "to": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
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
  "id": -576460752303421510,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAS8YJNKWsz6LVkWZX6ac5dGso++EF1jZRx33XyaGmLwtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQb7skCWkTyB24aNvZt1zrip6nN7Pe0eQeiRjqt8/TvEQAOgULRdJdq+nS/LHFAT1RiwCr4CtC/Q+pYj3so9dkfn7OM0LF81"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421510,
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAS8YJNKWsz6LVkWZX6ac5dGso++EF1jZRx33XyaGmLwtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQb7skCWkTyB24aNvZt1zrip6nN7Pe0eQeiRjqt8/TvEQAOgULRdJdq+nS/LHFAT1RiwCr4CtC/Q+pYj3so9dkfn7OM0LF81",
      "updates": [
        {
          "amount": 1,
          "from": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
          "op": "OffChainTransfer",
          "to": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
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
  "id": -576460752303421509,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhATrfgFGxCEtoSdkeoALbeiaaTA5oMVJnz4CXbP1qmGpEiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQEvGCTSlrM+i1ZFmV+mnOXRrKPvhBdY2Ucd918mhpi8LYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEG+7JAlpE8gduGjb2bdc64qepzez3tHkHokY6rfP07xEADoFC0XSXavp0vyxxQE9UYsAq+ArQv0PqWI97KPXZH5+zjPeoCVQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421509,
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhATrfgFGxCEtoSdkeoALbeiaaTA5oMVJnz4CXbP1qmGpEiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQEvGCTSlrM+i1ZFmV+mnOXRrKPvhBdY2Ucd918mhpi8LYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEG+7JAlpE8gduGjb2bdc64qepzez3tHkHokY6rfP07xEADoFC0XSXavp0vyxxQE9UYsAq+ArQv0PqWI97KPXZH5+zjPeoCVQ=="
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhATrfgFGxCEtoSdkeoALbeiaaTA5oMVJnz4CXbP1qmGpEiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQEvGCTSlrM+i1ZFmV+mnOXRrKPvhBdY2Ucd918mhpi8LYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEG+7JAlpE8gduGjb2bdc64qepzez3tHkHokY6rfP07xEADoFC0XSXavp0vyxxQE9UYsAq+ArQv0PqWI97KPXZH5+zjPeoCVQ=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421508,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
      "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421508,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
      "balance": 40000000000001
    },
    {
      "account": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421507,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421507,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhATrfgFGxCEtoSdkeoALbeiaaTA5oMVJnz4CXbP1qmGpEiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQEvGCTSlrM+i1ZFmV+mnOXRrKPvhBdY2Ucd918mhpi8LYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEG+7JAlpE8gduGjb2bdc64qepzez3tHkHokY6rfP07xEADoFC0XSXavp0vyxxQE9UYsAq+ArQv0PqWI97KPXZH5+zjPeoCVQ==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaA634BRsQhLaEnZHqAC23ommkwOaDFSZ8+Al2z9aphqRIvKCgEAhj+qJSJf/7DvQAGgLxgk0pazPotWRZlfppzl0ayj74QXWNlHHfdfJoaYvC2LygoBAIYkYTnKgAF0d5N2"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421506,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
      "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421506,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
      "balance": 40000000000001
    },
    {
      "account": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
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
    "from": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
    "to": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
        "from": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
        "to": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
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
    "to": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
        "to": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
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
    "from": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
        "from": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
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
    "from": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
    "to": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvuyQJaRPIHbho29m3XOuKnqc3s97R5B6JGOq3z9O8RABKBp+C6fS6sfGxiFU/Dpw/9NfGz0Lr2CmsIfRJ5p5mW3TXIVkSs=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
          "op": "OffChainTransfer",
          "to": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
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
  "id": -576460752303421505,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAS8YJNKWsz6LVkWZX6ac5dGso++EF1jZRx33XyaGmLwtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQb7skCWkTyB24aNvZt1zrip6nN7Pe0eQeiRjqt8/TvEQASgafgun0urHxsYhVPw6cP/TXxs9C69gprCH0SeaeZlt036r1L/"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421505,
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAS8YJNKWsz6LVkWZX6ac5dGso++EF1jZRx33XyaGmLwtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQb7skCWkTyB24aNvZt1zrip6nN7Pe0eQeiRjqt8/TvEQASgafgun0urHxsYhVPw6cP/TXxs9C69gprCH0SeaeZlt036r1L/",
      "updates": [
        {
          "amount": 1,
          "from": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
          "op": "OffChainTransfer",
          "to": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
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
  "id": -576460752303421504,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhATrfgFGxCEtoSdkeoALbeiaaTA5oMVJnz4CXbP1qmGpEiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQEvGCTSlrM+i1ZFmV+mnOXRrKPvhBdY2Ucd918mhpi8LYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEG+7JAlpE8gduGjb2bdc64qepzez3tHkHokY6rfP07xEAEoGn4Lp9Lqx8bGIVT8OnD/018bPQuvYKawh9EnmnmZbdNy2TAUw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421504,
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhATrfgFGxCEtoSdkeoALbeiaaTA5oMVJnz4CXbP1qmGpEiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQEvGCTSlrM+i1ZFmV+mnOXRrKPvhBdY2Ucd918mhpi8LYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEG+7JAlpE8gduGjb2bdc64qepzez3tHkHokY6rfP07xEAEoGn4Lp9Lqx8bGIVT8OnD/018bPQuvYKawh9EnmnmZbdNy2TAUw=="
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhATrfgFGxCEtoSdkeoALbeiaaTA5oMVJnz4CXbP1qmGpEiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQEvGCTSlrM+i1ZFmV+mnOXRrKPvhBdY2Ucd918mhpi8LYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEG+7JAlpE8gduGjb2bdc64qepzez3tHkHokY6rfP07xEAEoGn4Lp9Lqx8bGIVT8OnD/018bPQuvYKawh9EnmnmZbdNy2TAUw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421503,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
      "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421503,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
      "balance": 40000000000000
    },
    {
      "account": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421502,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421502,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhATrfgFGxCEtoSdkeoALbeiaaTA5oMVJnz4CXbP1qmGpEiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQEvGCTSlrM+i1ZFmV+mnOXRrKPvhBdY2Ucd918mhpi8LYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEG+7JAlpE8gduGjb2bdc64qepzez3tHkHokY6rfP07xEAEoGn4Lp9Lqx8bGIVT8OnD/018bPQuvYKawh9EnmnmZbdNy2TAUw==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaA634BRsQhLaEnZHqAC23ommkwOaDFSZ8+Al2z9aphqRIvKCgEAhj+qJSJgALDvQAGgLxgk0pazPotWRZlfppzl0ayj74QXWNlHHfdfJoaYvC2LygoBAIYkYTnKgAD5rXLG"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421501,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
      "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421501,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
      "balance": 70000000000000
    },
    {
      "account": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
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
    "from": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
    "to": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
        "from": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
        "to": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM"
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
    "to": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
        "to": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM"
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
    "from": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
        "from": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
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
    "from": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
    "to": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvuyQJaRPIHbho29m3XOuKnqc3s97R5B6JGOq3z9O8RABaBQtF0l2r6dL8scUBPVGLAKvgK0L9D6liPeyj12R+fs48uYzK8=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
          "op": "OffChainTransfer",
          "to": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM"
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
  "id": -576460752303421500,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhATrfgFGxCEtoSdkeoALbeiaaTA5oMVJnz4CXbP1qmGpEiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQb7skCWkTyB24aNvZt1zrip6nN7Pe0eQeiRjqt8/TvEQAWgULRdJdq+nS/LHFAT1RiwCr4CtC/Q+pYj3so9dkfn7ONw3+VX"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421500,
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhATrfgFGxCEtoSdkeoALbeiaaTA5oMVJnz4CXbP1qmGpEiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQb7skCWkTyB24aNvZt1zrip6nN7Pe0eQeiRjqt8/TvEQAWgULRdJdq+nS/LHFAT1RiwCr4CtC/Q+pYj3so9dkfn7ONw3+VX",
      "updates": [
        {
          "amount": 1,
          "from": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
          "op": "OffChainTransfer",
          "to": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM"
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
  "id": -576460752303421499,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhAS8YJNKWsz6LVkWZX6ac5dGso++EF1jZRx33XyaGmLwtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQE634BRsQhLaEnZHqAC23ommkwOaDFSZ8+Al2z9aphqRIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEG+7JAlpE8gduGjb2bdc64qepzez3tHkHokY6rfP07xEAFoFC0XSXavp0vyxxQE9UYsAq+ArQv0PqWI97KPXZH5+zjp1e8tg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421499,
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAS8YJNKWsz6LVkWZX6ac5dGso++EF1jZRx33XyaGmLwtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQE634BRsQhLaEnZHqAC23ommkwOaDFSZ8+Al2z9aphqRIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEG+7JAlpE8gduGjb2bdc64qepzez3tHkHokY6rfP07xEAFoFC0XSXavp0vyxxQE9UYsAq+ArQv0PqWI97KPXZH5+zjp1e8tg=="
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAS8YJNKWsz6LVkWZX6ac5dGso++EF1jZRx33XyaGmLwtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQE634BRsQhLaEnZHqAC23ommkwOaDFSZ8+Al2z9aphqRIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEG+7JAlpE8gduGjb2bdc64qepzez3tHkHokY6rfP07xEAFoFC0XSXavp0vyxxQE9UYsAq+ArQv0PqWI97KPXZH5+zjp1e8tg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421498,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
      "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421498,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
      "balance": 69999999999999
    },
    {
      "account": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421497,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421497,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhAS8YJNKWsz6LVkWZX6ac5dGso++EF1jZRx33XyaGmLwtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQE634BRsQhLaEnZHqAC23ommkwOaDFSZ8+Al2z9aphqRIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEG+7JAlpE8gduGjb2bdc64qepzez3tHkHokY6rfP07xEAFoFC0XSXavp0vyxxQE9UYsAq+ArQv0PqWI97KPXZH5+zjp1e8tg==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaA634BRsQhLaEnZHqAC23ommkwOaDFSZ8+Al2z9aphqRIvKCgEAhj+qJSJf/7DvQAGgLxgk0pazPotWRZlfppzl0ayj74QXWNlHHfdfJoaYvC2LygoBAIYkYTnKgAF0d5N2"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421496,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
      "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421496,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
      "balance": 40000000000001
    },
    {
      "account": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
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
    "from": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
    "to": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
        "from": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
        "to": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
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
    "to": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
        "to": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
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
    "from": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
        "from": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
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
    "from": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
    "to": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvuyQJaRPIHbho29m3XOuKnqc3s97R5B6JGOq3z9O8RABqBp+C6fS6sfGxiFU/Dpw/9NfGz0Lr2CmsIfRJ5p5mW3TSIRT6I=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
          "op": "OffChainTransfer",
          "to": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
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
  "id": -576460752303421495,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAS8YJNKWsz6LVkWZX6ac5dGso++EF1jZRx33XyaGmLwtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQb7skCWkTyB24aNvZt1zrip6nN7Pe0eQeiRjqt8/TvEQAagafgun0urHxsYhVPw6cP/TXxs9C69gprCH0SeaeZlt03LM4iP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421495,
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAS8YJNKWsz6LVkWZX6ac5dGso++EF1jZRx33XyaGmLwtiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQb7skCWkTyB24aNvZt1zrip6nN7Pe0eQeiRjqt8/TvEQAagafgun0urHxsYhVPw6cP/TXxs9C69gprCH0SeaeZlt03LM4iP",
      "updates": [
        {
          "amount": 1,
          "from": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
          "op": "OffChainTransfer",
          "to": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
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
  "id": -576460752303421494,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhATrfgFGxCEtoSdkeoALbeiaaTA5oMVJnz4CXbP1qmGpEiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQEvGCTSlrM+i1ZFmV+mnOXRrKPvhBdY2Ucd918mhpi8LYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEG+7JAlpE8gduGjb2bdc64qepzez3tHkHokY6rfP07xEAGoGn4Lp9Lqx8bGIVT8OnD/018bPQuvYKawh9EnmnmZbdNODLL+A=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421494,
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhATrfgFGxCEtoSdkeoALbeiaaTA5oMVJnz4CXbP1qmGpEiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQEvGCTSlrM+i1ZFmV+mnOXRrKPvhBdY2Ucd918mhpi8LYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEG+7JAlpE8gduGjb2bdc64qepzez3tHkHokY6rfP07xEAGoGn4Lp9Lqx8bGIVT8OnD/018bPQuvYKawh9EnmnmZbdNODLL+A=="
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
    "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhATrfgFGxCEtoSdkeoALbeiaaTA5oMVJnz4CXbP1qmGpEiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQEvGCTSlrM+i1ZFmV+mnOXRrKPvhBdY2Ucd918mhpi8LYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEG+7JAlpE8gduGjb2bdc64qepzez3tHkHokY6rfP07xEAGoGn4Lp9Lqx8bGIVT8OnD/018bPQuvYKawh9EnmnmZbdNODLL+A=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421493,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
      "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421493,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_Mjxjma2LvX1Y5saH1qsZcBRXDXMrxsZG7GX26tuPReu8cUYzM",
      "balance": 40000000000000
    },
    {
      "account": "ak_SvqKX1rSWywuUEbD6nGn3ySN3Az4W9sKqbcRHCpHJW2S4EK9u",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421492,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2urFADyXbwzCoghxFaejNoFc5BbyLapd5sBoBeZba192Mh8AK1",
  "id": -576460752303421492,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhATrfgFGxCEtoSdkeoALbeiaaTA5oMVJnz4CXbP1qmGpEiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQEvGCTSlrM+i1ZFmV+mnOXRrKPvhBdY2Ucd918mhpi8LYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEG+7JAlpE8gduGjb2bdc64qepzez3tHkHokY6rfP07xEAGoGn4Lp9Lqx8bGIVT8OnD/018bPQuvYKawh9EnmnmZbdNODLL+A==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaA634BRsQhLaEnZHqAC23ommkwOaDFSZ8+Al2z9aphqRIvKCgEAhj+qJSJgALDvQAGgLxgk0pazPotWRZlfppzl0ayj74QXWNlHHfdfJoaYvC2LygoBAIYkYTnKgAD5rXLG"
  },
  "version": 1
}
```
