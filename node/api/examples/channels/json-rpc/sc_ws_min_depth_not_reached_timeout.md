
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&minimum_depth=1&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_min_depth_not_reached_timeout_%2F2644&timeout_funding_lock=3000
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
      "fsm_id": "ba_JoD4Gwb3hZXkBDG/3uKMteMPMVOfIrAGTQ0DzGyOWNL9k8+L"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&minimum_depth=1&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_min_depth_not_reached_timeout_%2F2644&timeout_funding_lock=3000
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
      "fsm_id": "ba_62rxlJmoKkjGxXtX7kJgHTlwbMXNPZebixGLrUFo9QoZvzbo"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4BLZt9YQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423488,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuED2IVe5XVuCwY1OtZcBJzwJwQ4tv+BabksjHBi3Rc/Y7qU4XhREPDgrKR7EtcqnJco22uqQB389BXk4DENjr9sNuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uAbRbGR0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423488,
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
      "signed_tx": "tx_+MsLAfhCuED2IVe5XVuCwY1OtZcBJzwJwQ4tv+BabksjHBi3Rc/Y7qU4XhREPDgrKR7EtcqnJco22uqQB389BXk4DENjr9sNuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uAbRbGR0=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423487,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAbSTtjta4RQ8jZgyVfEOnc++9WTgm2FEVkuv5uYvrs2nlJ5Z1wpltlOaAFXJe3+0D7LEqRbMSLUwC9ho0ULgICLhA9iFXuV1bgsGNTrWXASc8CcEOLb/gWm5LIxwYt0XP2O6lOF4URDw4KykexLXKpyXKNtrqkAd/PQV5OAxDY6/bDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gHnxEQV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423487,
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
    "channel_id": "ch_27NMquoWkXqSdfLUZHwJTDs23897nzcZgWxZh4kM31mCpQKk3q",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAbSTtjta4RQ8jZgyVfEOnc++9WTgm2FEVkuv5uYvrs2nlJ5Z1wpltlOaAFXJe3+0D7LEqRbMSLUwC9ho0ULgICLhA9iFXuV1bgsGNTrWXASc8CcEOLb/gWm5LIxwYt0XP2O6lOF4URDw4KykexLXKpyXKNtrqkAd/PQV5OAxDY6/bDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gHnxEQV",
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
    "channel_id": "ch_27NMquoWkXqSdfLUZHwJTDs23897nzcZgWxZh4kM31mCpQKk3q",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAbSTtjta4RQ8jZgyVfEOnc++9WTgm2FEVkuv5uYvrs2nlJ5Z1wpltlOaAFXJe3+0D7LEqRbMSLUwC9ho0ULgICLhA9iFXuV1bgsGNTrWXASc8CcEOLb/gWm5LIxwYt0XP2O6lOF4URDw4KykexLXKpyXKNtrqkAd/PQV5OAxDY6/bDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gHnxEQV",
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
    "channel_id": "ch_27NMquoWkXqSdfLUZHwJTDs23897nzcZgWxZh4kM31mCpQKk3q",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAbSTtjta4RQ8jZgyVfEOnc++9WTgm2FEVkuv5uYvrs2nlJ5Z1wpltlOaAFXJe3+0D7LEqRbMSLUwC9ho0ULgICLhA9iFXuV1bgsGNTrWXASc8CcEOLb/gWm5LIxwYt0XP2O6lOF4URDw4KykexLXKpyXKNtrqkAd/PQV5OAxDY6/bDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gHnxEQV",
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
    "channel_id": "ch_27NMquoWkXqSdfLUZHwJTDs23897nzcZgWxZh4kM31mCpQKk3q",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAbSTtjta4RQ8jZgyVfEOnc++9WTgm2FEVkuv5uYvrs2nlJ5Z1wpltlOaAFXJe3+0D7LEqRbMSLUwC9ho0ULgICLhA9iFXuV1bgsGNTrWXASc8CcEOLb/gWm5LIxwYt0XP2O6lOF4URDw4KykexLXKpyXKNtrqkAd/PQV5OAxDY6/bDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gHnxEQV",
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
    "channel_id": "ch_27NMquoWkXqSdfLUZHwJTDs23897nzcZgWxZh4kM31mCpQKk3q",
    "data": {
      "event": "timeout"
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
    "channel_id": "ch_27NMquoWkXqSdfLUZHwJTDs23897nzcZgWxZh4kM31mCpQKk3q",
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
    "channel_id": "ch_27NMquoWkXqSdfLUZHwJTDs23897nzcZgWxZh4kM31mCpQKk3q",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
