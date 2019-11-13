
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD&keep_running=false&lock_period=10&port=13088&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF&role=initiator
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
      "fsm_id": "ba_AKkQpmEOStHEgqASoOCBBs20kvasPmvOyE2Bs6RGiPSgrWK7"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD&keep_running=false&lock_period=10&port=13088&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF&role=responder
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
      "fsm_id": "ba_StJzM59R3evqhQ/1zrjC5C1bDCkOd9MEb3yid17dmf1Dj/sF"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhATPu8lNgSzuUiyhiYlN00DVKQAzgGGvYB3RHgv5Rl00ghj+qJSJgAKEBHFiFBezDq9Ex60Z046Rw+pmF+jqtkO+/vHItDiS2VveGJGE5yoAAAgoAhhAGeddIAMCgLufj+xfJvis2kyNKIz494bsW0SGb+ddiL28IrRC3SrEAP+sLeA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422125,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+QFuCwHAuQFo+QFlUQGhATPu8lNgSzuUiyhiYlN00DVKQAzgGGvYB3RHgv5Rl00guKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiK+IgLAcC4g/iBMgGhATPu8lNgSzuUiyhiYlN00DVKQAzgGGvYB3RHgv5Rl00ghj+qJSJgAKEBHFiFBezDq9Ex60Z046Rw+pmF+jqtkO+/vHItDiS2VveGJGE5yoAAAgoAhhAGeddIAMCgLufj+xfJvis2kyNKIz494bsW0SGb+ddiL28IrRC3SrEAWxQ9UQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422125,
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
      "signed_tx": "tx_+QFuCwHAuQFo+QFlUQGhATPu8lNgSzuUiyhiYlN00DVKQAzgGGvYB3RHgv5Rl00guKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiK+IgLAcC4g/iBMgGhATPu8lNgSzuUiyhiYlN00DVKQAzgGGvYB3RHgv5Rl00ghj+qJSJgAKEBHFiFBezDq9Ex60Z046Rw+pmF+jqtkO+/vHItDiS2VveGJGE5yoAAAgoAhhAGeddIAMCgLufj+xfJvis2kyNKIz494bsW0SGb+ddiL28IrRC3SrEAWxQ9UQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422124,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QJWCwHAuQJQ+QJNUQGhARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3uKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBcfkBbgsBwLkBaPkBZVEBoQEz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNILigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQEz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNIIY/qiUiYAChARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3hiRhOcqAAAIKAIYQBnnXSADAoC7n4/sXyb4rNpMjSiM+PeG7FtEhm/nXYi9vCK0Qt0qxAL63ZXw="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422124,
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QJWCwHAuQJQ+QJNUQGhARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3uKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBcfkBbgsBwLkBaPkBZVEBoQEz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNILigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQEz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNIIY/qiUiYAChARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3hiRhOcqAAAIKAIYQBnnXSADAoC7n4/sXyb4rNpMjSiM+PeG7FtEhm/nXYi9vCK0Qt0qxAL63ZXw=",
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QJWCwHAuQJQ+QJNUQGhARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3uKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBcfkBbgsBwLkBaPkBZVEBoQEz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNILigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQEz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNIIY/qiUiYAChARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3hiRhOcqAAAIKAIYQBnnXSADAoC7n4/sXyb4rNpMjSiM+PeG7FtEhm/nXYi9vCK0Qt0qxAL63ZXw=",
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QJWCwHAuQJQ+QJNUQGhARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3uKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBcfkBbgsBwLkBaPkBZVEBoQEz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNILigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQEz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNIIY/qiUiYAChARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3hiRhOcqAAAIKAIYQBnnXSADAoC7n4/sXyb4rNpMjSiM+PeG7FtEhm/nXYi9vCK0Qt0qxAL63ZXw=",
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QJWCwHAuQJQ+QJNUQGhARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3uKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBcfkBbgsBwLkBaPkBZVEBoQEz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNILigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQEz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNIIY/qiUiYAChARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3hiRhOcqAAAIKAIYQBnnXSADAoC7n4/sXyb4rNpMjSiM+PeG7FtEhm/nXYi9vCK0Qt0qxAL63ZXw=",
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
    "to": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "message": {
        "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
        "from": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
        "info": "Hello",
        "to": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
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
    "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "message": {
        "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
        "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
        "info": "Hello back",
        "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422123,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
      "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422123,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
      "balance": 69999999999999
    },
    {
      "account": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### responder info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "state": "tx_+QJWCwHAuQJQ+QJNUQGhARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3uKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBcfkBbgsBwLkBaPkBZVEBoQEz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNILigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQEz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNIIY/qiUiYAChARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3hiRhOcqAAAIKAIYQBnnXSADAoC7n4/sXyb4rNpMjSiM+PeG7FtEhm/nXYi9vCK0Qt0qxAL63ZXw="
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "state": "tx_+QJWCwHAuQJQ+QJNUQGhARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3uKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBcfkBbgsBwLkBaPkBZVEBoQEz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNILigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQEz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNIIY/qiUiYAChARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3hiRhOcqAAAIKAIYQBnnXSADAoC7n4/sXyb4rNpMjSiM+PeG7FtEhm/nXYi9vCK0Qt0qxAL63ZXw="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422122,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
      "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422122,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
      "balance": 69999999999999
    },
    {
      "account": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
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
    "from": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
    "to": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
        "from": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
        "to": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
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
    "to": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
        "to": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
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
    "from": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
        "from": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
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
    "from": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
    "meta": 17,
    "to": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
        "from": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
        "meta": 17,
        "to": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
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
    "from": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
    "to": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpt7SGycMdlaW6dr79B+qwI7HHIqPWKeO+yRcCXf3FFhAqCtKaVBV0Qkc1ek5mhzkpBUNdN2K6oM0WkYyOHl/O+99hl4aHs=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
          "op": "OffChainTransfer",
          "to": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
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
  "id": -576460752303422121,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhATPu8lNgSzuUiyhiYlN00DVKQAzgGGvYB3RHgv5Rl00guKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBpt7SGycMdlaW6dr79B+qwI7HHIqPWKeO+yRcCXf3FFhAqCtKaVBV0Qkc1ek5mhzkpBUNdN2K6oM0WkYyOHl/O+99kn3UEA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422121,
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhATPu8lNgSzuUiyhiYlN00DVKQAzgGGvYB3RHgv5Rl00guKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBpt7SGycMdlaW6dr79B+qwI7HHIqPWKeO+yRcCXf3FFhAqCtKaVBV0Qkc1ek5mhzkpBUNdN2K6oM0WkYyOHl/O+99kn3UEA=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
          "op": "OffChainTransfer",
          "to": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
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
  "id": -576460752303422120,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3uKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNILigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQabe0hsnDHZWluna+/QfqsCOxxyKj1injvskXAl39xRYQKgrSmlQVdEJHNXpOZoc5KQVDXTdiuqDNFpGMjh5fzvvfZnDVIt"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422120,
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3uKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNILigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQabe0hsnDHZWluna+/QfqsCOxxyKj1injvskXAl39xRYQKgrSmlQVdEJHNXpOZoc5KQVDXTdiuqDNFpGMjh5fzvvfZnDVIt"
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3uKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNILigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQabe0hsnDHZWluna+/QfqsCOxxyKj1injvskXAl39xRYQKgrSmlQVdEJHNXpOZoc5KQVDXTdiuqDNFpGMjh5fzvvfZnDVIt"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422119,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
      "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422119,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
      "balance": 69999999999998
    },
    {
      "account": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422118,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422118,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3uKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNILigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQabe0hsnDHZWluna+/QfqsCOxxyKj1injvskXAl39xRYQKgrSmlQVdEJHNXpOZoc5KQVDXTdiuqDNFpGMjh5fzvvfZnDVIt",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaAz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNIIvKCgEAhj+qJSJf/rDvQAGgHFiFBezDq9Ex60Z046Rw+pmF+jqtkO+/vHItDiS2VveLygoBAIYkYTnKgALyWjWc"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422117,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
      "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422117,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
      "balance": 40000000000002
    },
    {
      "account": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
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
    "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
    "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
        "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
        "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
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
    "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
        "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
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
    "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
        "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
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
    "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
    "meta": 17,
    "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
        "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
        "meta": 17,
        "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
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
    "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
    "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpt7SGycMdlaW6dr79B+qwI7HHIqPWKeO+yRcCXf3FFhA6Au5+P7F8m+KzaTI0ojPj3huxbRIZv512IvbwitELdKsQa481g=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
          "op": "OffChainTransfer",
          "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
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
  "id": -576460752303422116,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3uKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBpt7SGycMdlaW6dr79B+qwI7HHIqPWKeO+yRcCXf3FFhA6Au5+P7F8m+KzaTI0ojPj3huxbRIZv512IvbwitELdKseU6i2U="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422116,
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3uKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBpt7SGycMdlaW6dr79B+qwI7HHIqPWKeO+yRcCXf3FFhA6Au5+P7F8m+KzaTI0ojPj3huxbRIZv512IvbwitELdKseU6i2U=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
          "op": "OffChainTransfer",
          "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
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
  "id": -576460752303422115,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhATPu8lNgSzuUiyhiYlN00DVKQAzgGGvYB3RHgv5Rl00guKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEcWIUF7MOr0THrRnTjpHD6mYX6Oq2Q77+8ci0OJLZW97igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQabe0hsnDHZWluna+/QfqsCOxxyKj1injvskXAl39xRYQOgLufj+xfJvis2kyNKIz494bsW0SGb+ddiL28IrRC3SrEAXjtx"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422115,
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhATPu8lNgSzuUiyhiYlN00DVKQAzgGGvYB3RHgv5Rl00guKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEcWIUF7MOr0THrRnTjpHD6mYX6Oq2Q77+8ci0OJLZW97igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQabe0hsnDHZWluna+/QfqsCOxxyKj1injvskXAl39xRYQOgLufj+xfJvis2kyNKIz494bsW0SGb+ddiL28IrRC3SrEAXjtx"
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhATPu8lNgSzuUiyhiYlN00DVKQAzgGGvYB3RHgv5Rl00guKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEcWIUF7MOr0THrRnTjpHD6mYX6Oq2Q77+8ci0OJLZW97igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQabe0hsnDHZWluna+/QfqsCOxxyKj1injvskXAl39xRYQOgLufj+xfJvis2kyNKIz494bsW0SGb+ddiL28IrRC3SrEAXjtx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422114,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
      "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422114,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
      "balance": 40000000000001
    },
    {
      "account": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422113,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422113,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhATPu8lNgSzuUiyhiYlN00DVKQAzgGGvYB3RHgv5Rl00guKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEcWIUF7MOr0THrRnTjpHD6mYX6Oq2Q77+8ci0OJLZW97igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQabe0hsnDHZWluna+/QfqsCOxxyKj1injvskXAl39xRYQOgLufj+xfJvis2kyNKIz494bsW0SGb+ddiL28IrRC3SrEAXjtx",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaAz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNIIvKCgEAhj+qJSJf/7DvQAGgHFiFBezDq9Ex60Z046Rw+pmF+jqtkO+/vHItDiS2VveLygoBAIYkYTnKgAHjINUN"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422112,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
      "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422112,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
      "balance": 40000000000001
    },
    {
      "account": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
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
    "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
    "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
        "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
        "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
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
    "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
        "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
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
    "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
        "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
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
    "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
    "meta": 17,
    "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
        "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
        "meta": 17,
        "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
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
    "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
    "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpt7SGycMdlaW6dr79B+qwI7HHIqPWKeO+yRcCXf3FFhBKAe70eVAQEQuNsH5LQDVrb5orowQjiMMnQ7/t9IGVyV95PUOmk=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
          "op": "OffChainTransfer",
          "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
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
  "id": -576460752303422111,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3uKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBpt7SGycMdlaW6dr79B+qwI7HHIqPWKeO+yRcCXf3FFhBKAe70eVAQEQuNsH5LQDVrb5orowQjiMMnQ7/t9IGVyV9zPes6U="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422111,
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3uKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBpt7SGycMdlaW6dr79B+qwI7HHIqPWKeO+yRcCXf3FFhBKAe70eVAQEQuNsH5LQDVrb5orowQjiMMnQ7/t9IGVyV9zPes6U=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
          "op": "OffChainTransfer",
          "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
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
  "id": -576460752303422110,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhATPu8lNgSzuUiyhiYlN00DVKQAzgGGvYB3RHgv5Rl00guKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEcWIUF7MOr0THrRnTjpHD6mYX6Oq2Q77+8ci0OJLZW97igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQabe0hsnDHZWluna+/QfqsCOxxyKj1injvskXAl39xRYQSgHu9HlQEBELjbB+S0A1a2+aK6MEI4jDJ0O/7fSBlclfeWL5mj"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422110,
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhATPu8lNgSzuUiyhiYlN00DVKQAzgGGvYB3RHgv5Rl00guKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEcWIUF7MOr0THrRnTjpHD6mYX6Oq2Q77+8ci0OJLZW97igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQabe0hsnDHZWluna+/QfqsCOxxyKj1injvskXAl39xRYQSgHu9HlQEBELjbB+S0A1a2+aK6MEI4jDJ0O/7fSBlclfeWL5mj"
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhATPu8lNgSzuUiyhiYlN00DVKQAzgGGvYB3RHgv5Rl00guKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEcWIUF7MOr0THrRnTjpHD6mYX6Oq2Q77+8ci0OJLZW97igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQabe0hsnDHZWluna+/QfqsCOxxyKj1injvskXAl39xRYQSgHu9HlQEBELjbB+S0A1a2+aK6MEI4jDJ0O/7fSBlclfeWL5mj"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422109,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
      "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422109,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
      "balance": 40000000000000
    },
    {
      "account": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422108,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422108,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhATPu8lNgSzuUiyhiYlN00DVKQAzgGGvYB3RHgv5Rl00guKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEcWIUF7MOr0THrRnTjpHD6mYX6Oq2Q77+8ci0OJLZW97igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQabe0hsnDHZWluna+/QfqsCOxxyKj1injvskXAl39xRYQSgHu9HlQEBELjbB+S0A1a2+aK6MEI4jDJ0O/7fSBlclfeWL5mj",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaAz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNIIvKCgEAhj+qJSJgALDvQAGgHFiFBezDq9Ex60Z046Rw+pmF+jqtkO+/vHItDiS2VveLygoBAIYkYTnKgABqdTtV"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422107,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
      "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422107,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
      "balance": 70000000000000
    },
    {
      "account": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
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
    "from": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
    "to": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
        "from": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
        "to": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
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
    "to": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
        "to": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
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
    "from": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
        "from": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
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
    "from": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
    "meta": 17,
    "to": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
        "from": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
        "meta": 17,
        "to": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
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
    "from": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
    "to": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpt7SGycMdlaW6dr79B+qwI7HHIqPWKeO+yRcCXf3FFhBaAu5+P7F8m+KzaTI0ojPj3huxbRIZv512IvbwitELdKsWHZOy0=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
          "op": "OffChainTransfer",
          "to": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
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
  "id": -576460752303422106,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhATPu8lNgSzuUiyhiYlN00DVKQAzgGGvYB3RHgv5Rl00guKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBpt7SGycMdlaW6dr79B+qwI7HHIqPWKeO+yRcCXf3FFhBaAu5+P7F8m+KzaTI0ojPj3huxbRIZv512IvbwitELdKsY0C0oA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422106,
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhATPu8lNgSzuUiyhiYlN00DVKQAzgGGvYB3RHgv5Rl00guKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBpt7SGycMdlaW6dr79B+qwI7HHIqPWKeO+yRcCXf3FFhBaAu5+P7F8m+KzaTI0ojPj3huxbRIZv512IvbwitELdKsY0C0oA=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
          "op": "OffChainTransfer",
          "to": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
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
  "id": -576460752303422105,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3uKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNILigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQabe0hsnDHZWluna+/QfqsCOxxyKj1injvskXAl39xRYQWgLufj+xfJvis2kyNKIz494bsW0SGb+ddiL28IrRC3SrFTYbUt"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422105,
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3uKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNILigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQabe0hsnDHZWluna+/QfqsCOxxyKj1injvskXAl39xRYQWgLufj+xfJvis2kyNKIz494bsW0SGb+ddiL28IrRC3SrFTYbUt"
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3uKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNILigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQabe0hsnDHZWluna+/QfqsCOxxyKj1injvskXAl39xRYQWgLufj+xfJvis2kyNKIz494bsW0SGb+ddiL28IrRC3SrFTYbUt"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422104,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
      "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422104,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
      "balance": 69999999999999
    },
    {
      "account": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422103,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422103,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3uKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNILigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQabe0hsnDHZWluna+/QfqsCOxxyKj1injvskXAl39xRYQWgLufj+xfJvis2kyNKIz494bsW0SGb+ddiL28IrRC3SrFTYbUt",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaAz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNIIvKCgEAhj+qJSJf/7DvQAGgHFiFBezDq9Ex60Z046Rw+pmF+jqtkO+/vHItDiS2VveLygoBAIYkYTnKgAHjINUN"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422102,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
      "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422102,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
      "balance": 40000000000001
    },
    {
      "account": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
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
    "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
    "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
        "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
        "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
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
    "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
        "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
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
    "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
        "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
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
    "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
    "meta": 17,
    "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
        "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
        "meta": 17,
        "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
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
    "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
    "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpt7SGycMdlaW6dr79B+qwI7HHIqPWKeO+yRcCXf3FFhBqAe70eVAQEQuNsH5LQDVrb5orowQjiMMnQ7/t9IGVyV97YfOu0=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
          "op": "OffChainTransfer",
          "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
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
  "id": -576460752303422101,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3uKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBpt7SGycMdlaW6dr79B+qwI7HHIqPWKeO+yRcCXf3FFhBqAe70eVAQEQuNsH5LQDVrb5orowQjiMMnQ7/t9IGVyV97nTbmk="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422101,
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhARxYhQXsw6vRMetGdOOkcPqZhfo6rZDvv7xyLQ4ktlb3uKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBpt7SGycMdlaW6dr79B+qwI7HHIqPWKeO+yRcCXf3FFhBqAe70eVAQEQuNsH5LQDVrb5orowQjiMMnQ7/t9IGVyV97nTbmk=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
          "op": "OffChainTransfer",
          "to": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
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
  "id": -576460752303422100,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhATPu8lNgSzuUiyhiYlN00DVKQAzgGGvYB3RHgv5Rl00guKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEcWIUF7MOr0THrRnTjpHD6mYX6Oq2Q77+8ci0OJLZW97igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQabe0hsnDHZWluna+/QfqsCOxxyKj1injvskXAl39xRYQagHu9HlQEBELjbB+S0A1a2+aK6MEI4jDJ0O/7fSBlclffuDnV+"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422100,
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhATPu8lNgSzuUiyhiYlN00DVKQAzgGGvYB3RHgv5Rl00guKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEcWIUF7MOr0THrRnTjpHD6mYX6Oq2Q77+8ci0OJLZW97igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQabe0hsnDHZWluna+/QfqsCOxxyKj1injvskXAl39xRYQagHu9HlQEBELjbB+S0A1a2+aK6MEI4jDJ0O/7fSBlclffuDnV+"
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhATPu8lNgSzuUiyhiYlN00DVKQAzgGGvYB3RHgv5Rl00guKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEcWIUF7MOr0THrRnTjpHD6mYX6Oq2Q77+8ci0OJLZW97igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQabe0hsnDHZWluna+/QfqsCOxxyKj1injvskXAl39xRYQagHu9HlQEBELjbB+S0A1a2+aK6MEI4jDJ0O/7fSBlclffuDnV+"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422099,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
      "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422099,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_DV4Bgh6egoa7DrUaaaGXSx5Jb9Cq4vH3JGkvLE3hktGBjKazF",
      "balance": 40000000000000
    },
    {
      "account": "ak_PsZyqeYNN2mBx5ty7JXJArorD2LfB4FtWr3NdbZMPDN1CWAfD",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422098,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422098,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhATPu8lNgSzuUiyhiYlN00DVKQAzgGGvYB3RHgv5Rl00guKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEcWIUF7MOr0THrRnTjpHD6mYX6Oq2Q77+8ci0OJLZW97igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQabe0hsnDHZWluna+/QfqsCOxxyKj1injvskXAl39xRYQagHu9HlQEBELjbB+S0A1a2+aK6MEI4jDJ0O/7fSBlclffuDnV+",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaAz7vJTYEs7lIsoYmJTdNA1SkAM4Bhr2Ad0R4L+UZdNIIvKCgEAhj+qJSJgALDvQAGgHFiFBezDq9Ex60Z046Rw+pmF+jqtkO+/vHItDiS2VveLygoBAIYkYTnKgABqdTtV"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422097,
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
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422097,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422096,
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
    "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
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
  "channel_id": "ch_2BUZxBAagojAimRrdW6hqfNi9b9wpVwW8diFjG9mtfzcNqkhq5",
  "id": -576460752303422096,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC&keep_running=false&lock_period=10&port=12524&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9&role=initiator
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
      "fsm_id": "ba_zVdL9eaonfalsqER8yyUEhqO0KC0Zvz1abPhbLnLSf9bME9F"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC&keep_running=false&lock_period=10&port=12524&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9&role=responder
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
      "fsm_id": "ba_UD90/P3AmwRfaP4MWfvjyeR8PaLm5W9CH8YqgUhMFURPDqiw"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAQzZGJngb3pOhqdum3EmjGTveXaWmWpjvKwL8cwIiVkahj+qJSJgAKEB+JudYBE729Z8Pt1HUP8rmWSkcETlc89QvnVTf+XXEA+GJGE5yoAAAgoAhhAGeddIAMCgUBoxCT20diIpYY5gKLjB9mG1pKYpynFXsvAVXkhOhd8AezZIGg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421478,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+NQLAcC4z/jNUQGhAQzZGJngb3pOhqdum3EmjGTveXaWmWpjvKwL8cwIiVkaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQEM2RiZ4G96ToanbptxJoxk73l2lplqY7ysC/HMCIlZGoY/qiUiYAChAfibnWARO9vWfD7dR1D/K5lkpHBE5XPPUL51U3/l1xAPhiRhOcqAAAIKAIYQBnnXSADAoFAaMQk9tHYiKWGOYCi4wfZhtaSmKcpxV7LwFV5IToXfAF2M8NE="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421478,
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
      "signed_tx": "tx_+NQLAcC4z/jNUQGhAQzZGJngb3pOhqdum3EmjGTveXaWmWpjvKwL8cwIiVkaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQEM2RiZ4G96ToanbptxJoxk73l2lplqY7ysC/HMCIlZGoY/qiUiYAChAfibnWARO9vWfD7dR1D/K5lkpHBE5XPPUL51U3/l1xAPhiRhOcqAAAIKAIYQBnnXSADAoFAaMQk9tHYiKWGOYCi4wfZhtaSmKcpxV7LwFV5IToXfAF2M8NE=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421477,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEiCwHAuQEc+QEZUQGhAfibnWARO9vWfD7dR1D/K5lkpHBE5XPPUL51U3/l1xAPiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQEM2RiZ4G96ToanbptxJoxk73l2lplqY7ysC/HMCIlZGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBDNkYmeBvek6Gp26bcSaMZO95dpaZamO8rAvxzAiJWRqGP6olImAAoQH4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4YkYTnKgAACCgCGEAZ510gAwKBQGjEJPbR2IilhjmAouMH2YbWkpinKcVey8BVeSE6F3wCyxvkh"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421477,
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEiCwHAuQEc+QEZUQGhAfibnWARO9vWfD7dR1D/K5lkpHBE5XPPUL51U3/l1xAPiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQEM2RiZ4G96ToanbptxJoxk73l2lplqY7ysC/HMCIlZGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBDNkYmeBvek6Gp26bcSaMZO95dpaZamO8rAvxzAiJWRqGP6olImAAoQH4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4YkYTnKgAACCgCGEAZ510gAwKBQGjEJPbR2IilhjmAouMH2YbWkpinKcVey8BVeSE6F3wCyxvkh",
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEiCwHAuQEc+QEZUQGhAfibnWARO9vWfD7dR1D/K5lkpHBE5XPPUL51U3/l1xAPiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQEM2RiZ4G96ToanbptxJoxk73l2lplqY7ysC/HMCIlZGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBDNkYmeBvek6Gp26bcSaMZO95dpaZamO8rAvxzAiJWRqGP6olImAAoQH4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4YkYTnKgAACCgCGEAZ510gAwKBQGjEJPbR2IilhjmAouMH2YbWkpinKcVey8BVeSE6F3wCyxvkh",
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEiCwHAuQEc+QEZUQGhAfibnWARO9vWfD7dR1D/K5lkpHBE5XPPUL51U3/l1xAPiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQEM2RiZ4G96ToanbptxJoxk73l2lplqY7ysC/HMCIlZGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBDNkYmeBvek6Gp26bcSaMZO95dpaZamO8rAvxzAiJWRqGP6olImAAoQH4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4YkYTnKgAACCgCGEAZ510gAwKBQGjEJPbR2IilhjmAouMH2YbWkpinKcVey8BVeSE6F3wCyxvkh",
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEiCwHAuQEc+QEZUQGhAfibnWARO9vWfD7dR1D/K5lkpHBE5XPPUL51U3/l1xAPiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQEM2RiZ4G96ToanbptxJoxk73l2lplqY7ysC/HMCIlZGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBDNkYmeBvek6Gp26bcSaMZO95dpaZamO8rAvxzAiJWRqGP6olImAAoQH4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4YkYTnKgAACCgCGEAZ510gAwKBQGjEJPbR2IilhjmAouMH2YbWkpinKcVey8BVeSE6F3wCyxvkh",
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
    "to": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "message": {
        "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
        "from": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
        "info": "Hello",
        "to": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
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
    "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "message": {
        "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
        "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
        "info": "Hello back",
        "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421476,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
      "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421476,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
      "balance": 69999999999999
    },
    {
      "account": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "state": "tx_+QEiCwHAuQEc+QEZUQGhAfibnWARO9vWfD7dR1D/K5lkpHBE5XPPUL51U3/l1xAPiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQEM2RiZ4G96ToanbptxJoxk73l2lplqY7ysC/HMCIlZGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBDNkYmeBvek6Gp26bcSaMZO95dpaZamO8rAvxzAiJWRqGP6olImAAoQH4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4YkYTnKgAACCgCGEAZ510gAwKBQGjEJPbR2IilhjmAouMH2YbWkpinKcVey8BVeSE6F3wCyxvkh"
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "state": "tx_+QEiCwHAuQEc+QEZUQGhAfibnWARO9vWfD7dR1D/K5lkpHBE5XPPUL51U3/l1xAPiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQEM2RiZ4G96ToanbptxJoxk73l2lplqY7ysC/HMCIlZGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBDNkYmeBvek6Gp26bcSaMZO95dpaZamO8rAvxzAiJWRqGP6olImAAoQH4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4YkYTnKgAACCgCGEAZ510gAwKBQGjEJPbR2IilhjmAouMH2YbWkpinKcVey8BVeSE6F3wCyxvkh"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421475,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
      "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421475,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
      "balance": 69999999999999
    },
    {
      "account": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
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
    "from": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
    "to": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
        "from": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
        "to": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
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
    "to": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
        "to": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
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
    "from": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
        "from": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
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
    "from": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
    "meta": 17,
    "to": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
        "from": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
        "meta": 17,
        "to": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
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
    "from": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
    "to": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlJMOvMyZrk8zML60msCizSH2aTH65jbHFfSlc5bigAAAqABq6ugYE+Xf7QlKdj6G4/R99eTVtlffiAyrcJ1Y8HIRxhTU44=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
          "op": "OffChainTransfer",
          "to": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
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
  "id": -576460752303421474,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAQzZGJngb3pOhqdum3EmjGTveXaWmWpjvKwL8cwIiVkaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZSTDrzMma5PMzC+tJrAos0h9mkx+uY2xxX0pXOW4oAAAKgAauroGBPl3+0JSnY+huP0ffXk1bZX34gMq3CdWPByEfYAhRg"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421474,
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAQzZGJngb3pOhqdum3EmjGTveXaWmWpjvKwL8cwIiVkaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZSTDrzMma5PMzC+tJrAos0h9mkx+uY2xxX0pXOW4oAAAKgAauroGBPl3+0JSnY+huP0ffXk1bZX34gMq3CdWPByEfYAhRg",
      "updates": [
        {
          "amount": 1,
          "from": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
          "op": "OffChainTransfer",
          "to": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
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
  "id": -576460752303421473,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhAfibnWARO9vWfD7dR1D/K5lkpHBE5XPPUL51U3/l1xAPiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQEM2RiZ4G96ToanbptxJoxk73l2lplqY7ysC/HMCIlZGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGUkw68zJmuTzMwvrSawKLNIfZpMfrmNscV9KVzluKAAACoAGrq6BgT5d/tCUp2Pobj9H315NW2V9+IDKtwnVjwchH/yAzig=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421473,
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAfibnWARO9vWfD7dR1D/K5lkpHBE5XPPUL51U3/l1xAPiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQEM2RiZ4G96ToanbptxJoxk73l2lplqY7ysC/HMCIlZGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGUkw68zJmuTzMwvrSawKLNIfZpMfrmNscV9KVzluKAAACoAGrq6BgT5d/tCUp2Pobj9H315NW2V9+IDKtwnVjwchH/yAzig=="
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAfibnWARO9vWfD7dR1D/K5lkpHBE5XPPUL51U3/l1xAPiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQEM2RiZ4G96ToanbptxJoxk73l2lplqY7ysC/HMCIlZGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGUkw68zJmuTzMwvrSawKLNIfZpMfrmNscV9KVzluKAAACoAGrq6BgT5d/tCUp2Pobj9H315NW2V9+IDKtwnVjwchH/yAzig=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421472,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
      "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421472,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
      "balance": 69999999999998
    },
    {
      "account": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421471,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421471,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhAfibnWARO9vWfD7dR1D/K5lkpHBE5XPPUL51U3/l1xAPiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQEM2RiZ4G96ToanbptxJoxk73l2lplqY7ysC/HMCIlZGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGUkw68zJmuTzMwvrSawKLNIfZpMfrmNscV9KVzluKAAACoAGrq6BgT5d/tCUp2Pobj9H315NW2V9+IDKtwnVjwchH/yAzig==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4vKCgEAhiRhOcqAArDvQAGgDNkYmeBvek6Gp26bcSaMZO95dpaZamO8rAvxzAiJWRqLygoBAIY/qiUiX/5QGjUO"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421470,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
      "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421470,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
      "balance": 40000000000002
    },
    {
      "account": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
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
    "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
    "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
        "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
        "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
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
    "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
        "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
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
    "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
        "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
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
    "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
    "meta": 17,
    "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
        "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
        "meta": 17,
        "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
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
    "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
    "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlJMOvMyZrk8zML60msCizSH2aTH65jbHFfSlc5bigAAA6BQGjEJPbR2IilhjmAouMH2YbWkpinKcVey8BVeSE6F3+komTQ=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
          "op": "OffChainTransfer",
          "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
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
  "id": -576460752303421469,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAfibnWARO9vWfD7dR1D/K5lkpHBE5XPPUL51U3/l1xAPiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZSTDrzMma5PMzC+tJrAos0h9mkx+uY2xxX0pXOW4oAAAOgUBoxCT20diIpYY5gKLjB9mG1pKYpynFXsvAVXkhOhd9DB5rp"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421469,
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAfibnWARO9vWfD7dR1D/K5lkpHBE5XPPUL51U3/l1xAPiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZSTDrzMma5PMzC+tJrAos0h9mkx+uY2xxX0pXOW4oAAAOgUBoxCT20diIpYY5gKLjB9mG1pKYpynFXsvAVXkhOhd9DB5rp",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
          "op": "OffChainTransfer",
          "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
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
  "id": -576460752303421468,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhAQzZGJngb3pOhqdum3EmjGTveXaWmWpjvKwL8cwIiVkaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQH4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGUkw68zJmuTzMwvrSawKLNIfZpMfrmNscV9KVzluKAAADoFAaMQk9tHYiKWGOYCi4wfZhtaSmKcpxV7LwFV5IToXflQU0wg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421468,
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAQzZGJngb3pOhqdum3EmjGTveXaWmWpjvKwL8cwIiVkaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQH4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGUkw68zJmuTzMwvrSawKLNIfZpMfrmNscV9KVzluKAAADoFAaMQk9tHYiKWGOYCi4wfZhtaSmKcpxV7LwFV5IToXflQU0wg=="
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAQzZGJngb3pOhqdum3EmjGTveXaWmWpjvKwL8cwIiVkaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQH4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGUkw68zJmuTzMwvrSawKLNIfZpMfrmNscV9KVzluKAAADoFAaMQk9tHYiKWGOYCi4wfZhtaSmKcpxV7LwFV5IToXflQU0wg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421467,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
      "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421467,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
      "balance": 40000000000001
    },
    {
      "account": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421466,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421466,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhAQzZGJngb3pOhqdum3EmjGTveXaWmWpjvKwL8cwIiVkaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQH4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGUkw68zJmuTzMwvrSawKLNIfZpMfrmNscV9KVzluKAAADoFAaMQk9tHYiKWGOYCi4wfZhtaSmKcpxV7LwFV5IToXflQU0wg==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4vKCgEAhiRhOcqAAbDvQAGgDNkYmeBvek6Gp26bcSaMZO95dpaZamO8rAvxzAiJWRqLygoBAIY/qiUiX/8G5NHj"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421465,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
      "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421465,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
      "balance": 40000000000001
    },
    {
      "account": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
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
    "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
    "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
        "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
        "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
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
    "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
        "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
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
    "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
        "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
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
    "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
    "meta": 17,
    "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
        "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
        "meta": 17,
        "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
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
    "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
    "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlJMOvMyZrk8zML60msCizSH2aTH65jbHFfSlc5bigAABKDjIB6ns/olh4vibwqiESQ6BhX1c3vcfBxzp0W4XCVPsOcdUfc=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
          "op": "OffChainTransfer",
          "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
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
  "id": -576460752303421464,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAfibnWARO9vWfD7dR1D/K5lkpHBE5XPPUL51U3/l1xAPiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZSTDrzMma5PMzC+tJrAos0h9mkx+uY2xxX0pXOW4oAAASg4yAep7P6JYeL4m8KohEkOgYV9XN73Hwcc6dFuFwlT7BV7M6P"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421464,
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAfibnWARO9vWfD7dR1D/K5lkpHBE5XPPUL51U3/l1xAPiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZSTDrzMma5PMzC+tJrAos0h9mkx+uY2xxX0pXOW4oAAASg4yAep7P6JYeL4m8KohEkOgYV9XN73Hwcc6dFuFwlT7BV7M6P",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
          "op": "OffChainTransfer",
          "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
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
  "id": -576460752303421463,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhAQzZGJngb3pOhqdum3EmjGTveXaWmWpjvKwL8cwIiVkaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQH4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGUkw68zJmuTzMwvrSawKLNIfZpMfrmNscV9KVzluKAAAEoOMgHqez+iWHi+JvCqIRJDoGFfVze9x8HHOnRbhcJU+wXwRURw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421463,
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAQzZGJngb3pOhqdum3EmjGTveXaWmWpjvKwL8cwIiVkaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQH4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGUkw68zJmuTzMwvrSawKLNIfZpMfrmNscV9KVzluKAAAEoOMgHqez+iWHi+JvCqIRJDoGFfVze9x8HHOnRbhcJU+wXwRURw=="
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAQzZGJngb3pOhqdum3EmjGTveXaWmWpjvKwL8cwIiVkaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQH4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGUkw68zJmuTzMwvrSawKLNIfZpMfrmNscV9KVzluKAAAEoOMgHqez+iWHi+JvCqIRJDoGFfVze9x8HHOnRbhcJU+wXwRURw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421462,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
      "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421462,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
      "balance": 40000000000000
    },
    {
      "account": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421461,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421461,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhAQzZGJngb3pOhqdum3EmjGTveXaWmWpjvKwL8cwIiVkaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQH4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGUkw68zJmuTzMwvrSawKLNIfZpMfrmNscV9KVzluKAAAEoOMgHqez+iWHi+JvCqIRJDoGFfVze9x8HHOnRbhcJU+wXwRURw==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4vKCgEAhiRhOcqAALDvQAGgDNkYmeBvek6Gp26bcSaMZO95dpaZamO8rAvxzAiJWRqLygoBAIY/qiUiYACaLApA"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421460,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
      "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421460,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
      "balance": 70000000000000
    },
    {
      "account": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
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
    "from": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
    "to": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
        "from": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
        "to": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
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
    "to": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
        "to": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
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
    "from": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
        "from": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
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
    "from": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
    "meta": 17,
    "to": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
        "from": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
        "meta": 17,
        "to": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
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
    "from": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
    "to": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlJMOvMyZrk8zML60msCizSH2aTH65jbHFfSlc5bigAABaBQGjEJPbR2IilhjmAouMH2YbWkpinKcVey8BVeSE6F31OxgjQ=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
          "op": "OffChainTransfer",
          "to": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
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
  "id": -576460752303421459,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAQzZGJngb3pOhqdum3EmjGTveXaWmWpjvKwL8cwIiVkaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZSTDrzMma5PMzC+tJrAos0h9mkx+uY2xxX0pXOW4oAAAWgUBoxCT20diIpYY5gKLjB9mG1pKYpynFXsvAVXkhOhd8Z5yzE"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421459,
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAQzZGJngb3pOhqdum3EmjGTveXaWmWpjvKwL8cwIiVkaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZSTDrzMma5PMzC+tJrAos0h9mkx+uY2xxX0pXOW4oAAAWgUBoxCT20diIpYY5gKLjB9mG1pKYpynFXsvAVXkhOhd8Z5yzE",
      "updates": [
        {
          "amount": 1,
          "from": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
          "op": "OffChainTransfer",
          "to": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
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
  "id": -576460752303421458,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhAfibnWARO9vWfD7dR1D/K5lkpHBE5XPPUL51U3/l1xAPiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQEM2RiZ4G96ToanbptxJoxk73l2lplqY7ysC/HMCIlZGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGUkw68zJmuTzMwvrSawKLNIfZpMfrmNscV9KVzluKAAAFoFAaMQk9tHYiKWGOYCi4wfZhtaSmKcpxV7LwFV5IToXfc/UeZw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421458,
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAfibnWARO9vWfD7dR1D/K5lkpHBE5XPPUL51U3/l1xAPiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQEM2RiZ4G96ToanbptxJoxk73l2lplqY7ysC/HMCIlZGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGUkw68zJmuTzMwvrSawKLNIfZpMfrmNscV9KVzluKAAAFoFAaMQk9tHYiKWGOYCi4wfZhtaSmKcpxV7LwFV5IToXfc/UeZw=="
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAfibnWARO9vWfD7dR1D/K5lkpHBE5XPPUL51U3/l1xAPiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQEM2RiZ4G96ToanbptxJoxk73l2lplqY7ysC/HMCIlZGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGUkw68zJmuTzMwvrSawKLNIfZpMfrmNscV9KVzluKAAAFoFAaMQk9tHYiKWGOYCi4wfZhtaSmKcpxV7LwFV5IToXfc/UeZw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421457,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
      "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421457,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
      "balance": 69999999999999
    },
    {
      "account": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421456,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421456,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhAfibnWARO9vWfD7dR1D/K5lkpHBE5XPPUL51U3/l1xAPiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQEM2RiZ4G96ToanbptxJoxk73l2lplqY7ysC/HMCIlZGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGUkw68zJmuTzMwvrSawKLNIfZpMfrmNscV9KVzluKAAAFoFAaMQk9tHYiKWGOYCi4wfZhtaSmKcpxV7LwFV5IToXfc/UeZw==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4vKCgEAhiRhOcqAAbDvQAGgDNkYmeBvek6Gp26bcSaMZO95dpaZamO8rAvxzAiJWRqLygoBAIY/qiUiX/8G5NHj"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421455,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
      "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421455,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
      "balance": 40000000000001
    },
    {
      "account": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
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
    "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
    "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
        "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
        "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
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
    "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
        "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
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
    "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
        "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
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
    "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
    "meta": 17,
    "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
        "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
        "meta": 17,
        "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
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
    "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
    "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlJMOvMyZrk8zML60msCizSH2aTH65jbHFfSlc5bigAABqDjIB6ns/olh4vibwqiESQ6BhX1c3vcfBxzp0W4XCVPsHQjCT8=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
          "op": "OffChainTransfer",
          "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
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
  "id": -576460752303421454,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAfibnWARO9vWfD7dR1D/K5lkpHBE5XPPUL51U3/l1xAPiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZSTDrzMma5PMzC+tJrAos0h9mkx+uY2xxX0pXOW4oAAAag4yAep7P6JYeL4m8KohEkOgYV9XN73Hwcc6dFuFwlT7ASLr4m"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421454,
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAfibnWARO9vWfD7dR1D/K5lkpHBE5XPPUL51U3/l1xAPiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZSTDrzMma5PMzC+tJrAos0h9mkx+uY2xxX0pXOW4oAAAag4yAep7P6JYeL4m8KohEkOgYV9XN73Hwcc6dFuFwlT7ASLr4m",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
          "op": "OffChainTransfer",
          "to": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
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
  "id": -576460752303421453,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhAQzZGJngb3pOhqdum3EmjGTveXaWmWpjvKwL8cwIiVkaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQH4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGUkw68zJmuTzMwvrSawKLNIfZpMfrmNscV9KVzluKAAAGoOMgHqez+iWHi+JvCqIRJDoGFfVze9x8HHOnRbhcJU+wb4xgXw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421453,
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAQzZGJngb3pOhqdum3EmjGTveXaWmWpjvKwL8cwIiVkaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQH4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGUkw68zJmuTzMwvrSawKLNIfZpMfrmNscV9KVzluKAAAGoOMgHqez+iWHi+JvCqIRJDoGFfVze9x8HHOnRbhcJU+wb4xgXw=="
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAQzZGJngb3pOhqdum3EmjGTveXaWmWpjvKwL8cwIiVkaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQH4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGUkw68zJmuTzMwvrSawKLNIfZpMfrmNscV9KVzluKAAAGoOMgHqez+iWHi+JvCqIRJDoGFfVze9x8HHOnRbhcJU+wb4xgXw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421452,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
      "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421452,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2tVMZ7n4P9UxA376bU1MDj4mVVhcyCLvyZHg1vZiyC3xXvWkY9",
      "balance": 40000000000000
    },
    {
      "account": "ak_6fBmn1tMojrnz87vuM73Nip2SrZKzteFxfjuarRq12vde2NFC",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421451,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421451,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhAQzZGJngb3pOhqdum3EmjGTveXaWmWpjvKwL8cwIiVkaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQH4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGUkw68zJmuTzMwvrSawKLNIfZpMfrmNscV9KVzluKAAAGoOMgHqez+iWHi+JvCqIRJDoGFfVze9x8HHOnRbhcJU+wb4xgXw==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD4m51gETvb1nw+3UdQ/yuZZKRwROVzz1C+dVN/5dcQD4vKCgEAhiRhOcqAALDvQAGgDNkYmeBvek6Gp26bcSaMZO95dpaZamO8rAvxzAiJWRqLygoBAIY/qiUiYACaLApA"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421450,
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
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421450,
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
  "id": -576460752303421449,
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
    "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
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
  "channel_id": "ch_dFBoMmhXX8M7c2tmkZG2HyzmUB8tCJPREpUiUj5uGFH1KgvtU",
  "id": -576460752303421449,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```
