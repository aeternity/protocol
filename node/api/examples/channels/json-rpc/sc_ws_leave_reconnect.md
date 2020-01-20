
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reconnect%2F3310
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
      "fsm_id": "ba_kfeK7rkI5b6kC1y1L00QTkkRv5pZkUbJyp3hHxUq+OnZJlvJ"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=true&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reconnect%2F3310
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
      "fsm_id": "ba_P/Yqq0yDDL0y6d3zLexIJWzkzHF8hDl+mPjGwhtzkha/Il5b"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4YsFQFyg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423187,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECJ0i5PdNRb4/AUG6os2JbWMueLYen2mocHpbY7mgmY5vml/2c2cR30Y0FG3g6Ia7QmStzeWTyZlXrv/vZ5DCULuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uGCHe8Co="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423187,
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
      "signed_tx": "tx_+MsLAfhCuECJ0i5PdNRb4/AUG6os2JbWMueLYen2mocHpbY7mgmY5vml/2c2cR30Y0FG3g6Ia7QmStzeWTyZlXrv/vZ5DCULuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uGCHe8Co=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423186,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAidIuT3TUW+PwFBuqLNiW1jLni2Hp9pqHB6W2O5oJmOb5pf9nNnEd9GNBRt4OiGu0Jkrc3lk8mZV67/72eQwlC7hArY9Swzyp8UE0SD/c5gwlI2ov0m6wYzDdV6Tt/HgFhqxl/dSWzp/HuTeeM1sB1opoYRqLIyThd9Xgtgd+zFojDriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hgp69Im"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423186,
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAidIuT3TUW+PwFBuqLNiW1jLni2Hp9pqHB6W2O5oJmOb5pf9nNnEd9GNBRt4OiGu0Jkrc3lk8mZV67/72eQwlC7hArY9Swzyp8UE0SD/c5gwlI2ov0m6wYzDdV6Tt/HgFhqxl/dSWzp/HuTeeM1sB1opoYRqLIyThd9Xgtgd+zFojDriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hgp69Im",
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAidIuT3TUW+PwFBuqLNiW1jLni2Hp9pqHB6W2O5oJmOb5pf9nNnEd9GNBRt4OiGu0Jkrc3lk8mZV67/72eQwlC7hArY9Swzyp8UE0SD/c5gwlI2ov0m6wYzDdV6Tt/HgFhqxl/dSWzp/HuTeeM1sB1opoYRqLIyThd9Xgtgd+zFojDriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hgp69Im",
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAidIuT3TUW+PwFBuqLNiW1jLni2Hp9pqHB6W2O5oJmOb5pf9nNnEd9GNBRt4OiGu0Jkrc3lk8mZV67/72eQwlC7hArY9Swzyp8UE0SD/c5gwlI2ov0m6wYzDdV6Tt/HgFhqxl/dSWzp/HuTeeM1sB1opoYRqLIyThd9Xgtgd+zFojDriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hgp69Im",
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAidIuT3TUW+PwFBuqLNiW1jLni2Hp9pqHB6W2O5oJmOb5pf9nNnEd9GNBRt4OiGu0Jkrc3lk8mZV67/72eQwlC7hArY9Swzyp8UE0SD/c5gwlI2ov0m6wYzDdV6Tt/HgFhqxl/dSWzp/HuTeeM1sB1opoYRqLIyThd9Xgtgd+zFojDriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hgp69Im",
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
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "message": {
        "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "info": "Hello",
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "message": {
        "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "info": "Hello back",
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423185,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423185,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999999
    },
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "state": "tx_+QENCwH4hLhAidIuT3TUW+PwFBuqLNiW1jLni2Hp9pqHB6W2O5oJmOb5pf9nNnEd9GNBRt4OiGu0Jkrc3lk8mZV67/72eQwlC7hArY9Swzyp8UE0SD/c5gwlI2ov0m6wYzDdV6Tt/HgFhqxl/dSWzp/HuTeeM1sB1opoYRqLIyThd9Xgtgd+zFojDriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hgp69Im"
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "state": "tx_+QENCwH4hLhAidIuT3TUW+PwFBuqLNiW1jLni2Hp9pqHB6W2O5oJmOb5pf9nNnEd9GNBRt4OiGu0Jkrc3lk8mZV67/72eQwlC7hArY9Swzyp8UE0SD/c5gwlI2ov0m6wYzDdV6Tt/HgFhqxl/dSWzp/HuTeeM1sB1opoYRqLIyThd9Xgtgd+zFojDriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hgp69Im"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "state": "tx_+QENCwH4hLhAidIuT3TUW+PwFBuqLNiW1jLni2Hp9pqHB6W2O5oJmOb5pf9nNnEd9GNBRt4OiGu0Jkrc3lk8mZV67/72eQwlC7hArY9Swzyp8UE0SD/c5gwlI2ov0m6wYzDdV6Tt/HgFhqxl/dSWzp/HuTeeM1sB1opoYRqLIyThd9Xgtgd+zFojDriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hgp69Im"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "state": "tx_+QENCwH4hLhAidIuT3TUW+PwFBuqLNiW1jLni2Hp9pqHB6W2O5oJmOb5pf9nNnEd9GNBRt4OiGu0Jkrc3lk8mZV67/72eQwlC7hArY9Swzyp8UE0SD/c5gwlI2ov0m6wYzDdV6Tt/HgFhqxl/dSWzp/HuTeeM1sB1opoYRqLIyThd9Xgtgd+zFojDriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hgp69Im"
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "event": "peer_disconnected"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAidIuT3TUW%2BPwFBuqLNiW1jLni2Hp9pqHB6W2O5oJmOb5pf9nNnEd9GNBRt4OiGu0Jkrc3lk8mZV67%2F72eQwlC7hArY9Swzyp8UE0SD%2Fc5gwlI2ov0m6wYzDdV6Tt%2FHgFhqxl%2FdSWzp%2FHuTeeM1sB1opoYRqLIyThd9Xgtgd%2BzFojDriD%2BIEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu%2FSGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G%2BJNZ1%2B3HKCYNWL2rDf7hgp69Im&port=13179&protocol=json-rpc&role=initiator
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
ws://localhost:3014/channel?existing_channel_id=ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv&existing_fsm_id=Invalid&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAidIuT3TUW%2BPwFBuqLNiW1jLni2Hp9pqHB6W2O5oJmOb5pf9nNnEd9GNBRt4OiGu0Jkrc3lk8mZV67%2F72eQwlC7hArY9Swzyp8UE0SD%2Fc5gwlI2ov0m6wYzDdV6Tt%2FHgFhqxl%2FdSWzp%2FHuTeeM1sB1opoYRqLIyThd9Xgtgd%2BzFojDriD%2BIEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu%2FSGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G%2BJNZ1%2B3HKCYNWL2rDf7hgp69Im&port=13179&protocol=json-rpc&role=initiator
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
ws://localhost:3014/channel?existing_channel_id=ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv&existing_fsm_id=ba_UbNkOyxwx%2BwdQ%2Bt%2F&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAidIuT3TUW%2BPwFBuqLNiW1jLni2Hp9pqHB6W2O5oJmOb5pf9nNnEd9GNBRt4OiGu0Jkrc3lk8mZV67%2F72eQwlC7hArY9Swzyp8UE0SD%2Fc5gwlI2ov0m6wYzDdV6Tt%2FHgFhqxl%2FdSWzp%2FHuTeeM1sB1opoYRqLIyThd9Xgtgd%2BzFojDriD%2BIEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu%2FSGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G%2BJNZ1%2B3HKCYNWL2rDf7hgp69Im&port=13179&protocol=json-rpc&role=initiator
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
ws://localhost:3014/channel?existing_channel_id=ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv&existing_fsm_id=ba_OULqqOKwgboBwgS9YqNO95t4HQd4OC3rfqb%2FNWKkCNTRGK47&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAidIuT3TUW%2BPwFBuqLNiW1jLni2Hp9pqHB6W2O5oJmOb5pf9nNnEd9GNBRt4OiGu0Jkrc3lk8mZV67%2F72eQwlC7hArY9Swzyp8UE0SD%2Fc5gwlI2ov0m6wYzDdV6Tt%2FHgFhqxl%2FdSWzp%2FHuTeeM1sB1opoYRqLIyThd9Xgtgd%2BzFojDriD%2BIEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu%2FSGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G%2BJNZ1%2B3HKCYNWL2rDf7hgp69Im&port=13179&protocol=json-rpc&role=initiator
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
ws://localhost:3014/channel?existing_channel_id=ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv&existing_fsm_id=ba_kfeK7rkI5b6kC1y1L00QTkkRv5pZkUbJyp3hHxUq%2BOnZJlvJ&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAidIuT3TUW%2BPwFBuqLNiW1jLni2Hp9pqHB6W2O5oJmOb5pf9nNnEd9GNBRt4OiGu0Jkrc3lk8mZV67%2F72eQwlC7hArY9Swzyp8UE0SD%2Fc5gwlI2ov0m6wYzDdV6Tt%2FHgFhqxl%2FdSWzp%2FHuTeeM1sB1opoYRqLIyThd9Xgtgd%2BzFojDriD%2BIEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu%2FSGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G%2BJNZ1%2B3HKCYNWL2rDf7hgp69Im&port=13179&protocol=json-rpc&role=initiator
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
      "fsm_id": "ba_/vFeQcS/E4ICbBjkCPu+rMMi0OKHr0+PRWhO1XDUCvDPiwjN"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "event": "channel_reestablished"
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "event": "channel_reestablished"
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "state": "tx_+QENCwH4hLhAidIuT3TUW+PwFBuqLNiW1jLni2Hp9pqHB6W2O5oJmOb5pf9nNnEd9GNBRt4OiGu0Jkrc3lk8mZV67/72eQwlC7hArY9Swzyp8UE0SD/c5gwlI2ov0m6wYzDdV6Tt/HgFhqxl/dSWzp/HuTeeM1sB1opoYRqLIyThd9Xgtgd+zFojDriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hgp69Im"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423184,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423184,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999999
    },
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
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
    "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
    "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
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
    "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
    "meta": 17,
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "meta": 17,
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
    "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuX6HEC6Lyfz/0ltl6ItdLmESzsnaqOcZlLJxsr79GMgAqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B54vxds=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainTransfer",
          "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
  "id": -576460752303423183,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAjrp3q71+U6AK0/ZMDZ3vHL6p3BVuxaXAwz1mxakphy67EUn2KkT6s9mdVGJsThDIVKNoCFWGvnTDFg7XYXB8EuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAdiWSoL"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423183,
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAjrp3q71+U6AK0/ZMDZ3vHL6p3BVuxaXAwz1mxakphy67EUn2KkT6s9mdVGJsThDIVKNoCFWGvnTDFg7XYXB8EuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAdiWSoL",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainTransfer",
          "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
  "id": -576460752303423182,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAjrp3q71+U6AK0/ZMDZ3vHL6p3BVuxaXAwz1mxakphy67EUn2KkT6s9mdVGJsThDIVKNoCFWGvnTDFg7XYXB8EuEBURjjlgdY8Dn4rM1JoSQY3apOd0yo9ICdW+Thx09fX5YD2RtDSodf+OBW89Bc+dbsuGS0vklURu+y0zhQxzGUFuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcso1qN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423182,
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "state": "tx_+NILAfiEuEAjrp3q71+U6AK0/ZMDZ3vHL6p3BVuxaXAwz1mxakphy67EUn2KkT6s9mdVGJsThDIVKNoCFWGvnTDFg7XYXB8EuEBURjjlgdY8Dn4rM1JoSQY3apOd0yo9ICdW+Thx09fX5YD2RtDSodf+OBW89Bc+dbsuGS0vklURu+y0zhQxzGUFuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcso1qN"
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "state": "tx_+NILAfiEuEAjrp3q71+U6AK0/ZMDZ3vHL6p3BVuxaXAwz1mxakphy67EUn2KkT6s9mdVGJsThDIVKNoCFWGvnTDFg7XYXB8EuEBURjjlgdY8Dn4rM1JoSQY3apOd0yo9ICdW+Thx09fX5YD2RtDSodf+OBW89Bc+dbsuGS0vklURu+y0zhQxzGUFuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcso1qN"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423181,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423181,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999998
    },
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423180,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423180,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAjrp3q71+U6AK0/ZMDZ3vHL6p3BVuxaXAwz1mxakphy67EUn2KkT6s9mdVGJsThDIVKNoCFWGvnTDFg7XYXB8EuEBURjjlgdY8Dn4rM1JoSQY3apOd0yo9ICdW+Thx09fX5YD2RtDSodf+OBW89Bc+dbsuGS0vklURu+y0zhQxzGUFuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcso1qN",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423179,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423179,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000002
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
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
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
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
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "meta": 17,
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "meta": 17,
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuX6HEC6Lyfz/0ltl6ItdLmESzsnaqOcZlLJxsr79GMgA6AWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kNA/8s=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "id": -576460752303423178,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBl5sL3NHiVn99ZvUO6FXWOsGWI513lvchyjc65PEQIY/Ja8KuMChq9Jw2s0UM3I3NVikG8qV4tdmJyUQpDPmYPuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5QAPGH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423178,
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBl5sL3NHiVn99ZvUO6FXWOsGWI513lvchyjc65PEQIY/Ja8KuMChq9Jw2s0UM3I3NVikG8qV4tdmJyUQpDPmYPuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5QAPGH",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "id": -576460752303423177,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBl5sL3NHiVn99ZvUO6FXWOsGWI513lvchyjc65PEQIY/Ja8KuMChq9Jw2s0UM3I3NVikG8qV4tdmJyUQpDPmYPuEC+o4Qto3qh63mEmtGE2hczzk/Np1SdhVSh/+IiFZEx7mfQQKWTj0cf90NQoYczq4dab3v2IgkBpJb0jkgoFhIDuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5V1Rtx"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423177,
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "state": "tx_+NILAfiEuEBl5sL3NHiVn99ZvUO6FXWOsGWI513lvchyjc65PEQIY/Ja8KuMChq9Jw2s0UM3I3NVikG8qV4tdmJyUQpDPmYPuEC+o4Qto3qh63mEmtGE2hczzk/Np1SdhVSh/+IiFZEx7mfQQKWTj0cf90NQoYczq4dab3v2IgkBpJb0jkgoFhIDuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5V1Rtx"
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "state": "tx_+NILAfiEuEBl5sL3NHiVn99ZvUO6FXWOsGWI513lvchyjc65PEQIY/Ja8KuMChq9Jw2s0UM3I3NVikG8qV4tdmJyUQpDPmYPuEC+o4Qto3qh63mEmtGE2hczzk/Np1SdhVSh/+IiFZEx7mfQQKWTj0cf90NQoYczq4dab3v2IgkBpJb0jkgoFhIDuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5V1Rtx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423176,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423176,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000001
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423175,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423175,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBl5sL3NHiVn99ZvUO6FXWOsGWI513lvchyjc65PEQIY/Ja8KuMChq9Jw2s0UM3I3NVikG8qV4tdmJyUQpDPmYPuEC+o4Qto3qh63mEmtGE2hczzk/Np1SdhVSh/+IiFZEx7mfQQKWTj0cf90NQoYczq4dab3v2IgkBpJb0jkgoFhIDuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5V1Rtx",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423174,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423174,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000001
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
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
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
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
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "meta": 17,
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "meta": 17,
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuX6HEC6Lyfz/0ltl6ItdLmESzsnaqOcZlLJxsr79GMgBKArw56Yk/nuAn9SDD7EMYNf1i7BI0w+TO2mQGxnQbS3tljMQ4Q=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "id": -576460752303423173,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB7YBPz+4imdEjjPFsmR5Wu9SlrgrmwKEyVsREpYzNHwnZUSk+c5txIu4cvgk3GVhoLO++Mx0bf58YrzEJjVDsJuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7bi39yH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423173,
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB7YBPz+4imdEjjPFsmR5Wu9SlrgrmwKEyVsREpYzNHwnZUSk+c5txIu4cvgk3GVhoLO++Mx0bf58YrzEJjVDsJuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7bi39yH",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "id": -576460752303423172,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA7Mw8TuD2iVW4PvVIN4kYcikKohIsN32KXr+x26H8TZOJiMHpUyUFkD4avhZzyDoDe7OmqCPY1JShMku1hKEEPuEB7YBPz+4imdEjjPFsmR5Wu9SlrgrmwKEyVsREpYzNHwnZUSk+c5txIu4cvgk3GVhoLO++Mx0bf58YrzEJjVDsJuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7alxTou"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423172,
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "state": "tx_+NILAfiEuEA7Mw8TuD2iVW4PvVIN4kYcikKohIsN32KXr+x26H8TZOJiMHpUyUFkD4avhZzyDoDe7OmqCPY1JShMku1hKEEPuEB7YBPz+4imdEjjPFsmR5Wu9SlrgrmwKEyVsREpYzNHwnZUSk+c5txIu4cvgk3GVhoLO++Mx0bf58YrzEJjVDsJuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7alxTou"
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "state": "tx_+NILAfiEuEA7Mw8TuD2iVW4PvVIN4kYcikKohIsN32KXr+x26H8TZOJiMHpUyUFkD4avhZzyDoDe7OmqCPY1JShMku1hKEEPuEB7YBPz+4imdEjjPFsmR5Wu9SlrgrmwKEyVsREpYzNHwnZUSk+c5txIu4cvgk3GVhoLO++Mx0bf58YrzEJjVDsJuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7alxTou"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423171,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423171,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000000
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423170,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423170,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA7Mw8TuD2iVW4PvVIN4kYcikKohIsN32KXr+x26H8TZOJiMHpUyUFkD4avhZzyDoDe7OmqCPY1JShMku1hKEEPuEB7YBPz+4imdEjjPFsmR5Wu9SlrgrmwKEyVsREpYzNHwnZUSk+c5txIu4cvgk3GVhoLO++Mx0bf58YrzEJjVDsJuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7alxTou",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAALDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiYABL489v"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423169,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423169,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 70000000000000
    },
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
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
    "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
    "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
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
    "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
    "meta": 17,
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "meta": 17,
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
    "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuX6HEC6Lyfz/0ltl6ItdLmESzsnaqOcZlLJxsr79GMgBaAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7ve/wMM=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainTransfer",
          "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
  "id": -576460752303423168,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECr2kMDsYN8WWkQunrZb80TyaIakMMf67Tqf+Li9BT7BwtaPZgo6QB9qDHPBQ9p06V8kJhwdHmH69UjBhIMZuYLuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4ST/dT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423168,
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "signed_tx": "tx_+JALAfhCuECr2kMDsYN8WWkQunrZb80TyaIakMMf67Tqf+Li9BT7BwtaPZgo6QB9qDHPBQ9p06V8kJhwdHmH69UjBhIMZuYLuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4ST/dT",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainTransfer",
          "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
  "id": -576460752303423167,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECgjunLzECgBO90VtKTXmLN37jWi+T2hPHlvL6fTJh05pnf7CrqwahWmLdE2OgW2D5Yt6cfdzVXs/FRkrmXF1ENuECr2kMDsYN8WWkQunrZb80TyaIakMMf67Tqf+Li9BT7BwtaPZgo6QB9qDHPBQ9p06V8kJhwdHmH69UjBhIMZuYLuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5J1e9B"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423167,
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "state": "tx_+NILAfiEuECgjunLzECgBO90VtKTXmLN37jWi+T2hPHlvL6fTJh05pnf7CrqwahWmLdE2OgW2D5Yt6cfdzVXs/FRkrmXF1ENuECr2kMDsYN8WWkQunrZb80TyaIakMMf67Tqf+Li9BT7BwtaPZgo6QB9qDHPBQ9p06V8kJhwdHmH69UjBhIMZuYLuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5J1e9B"
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "state": "tx_+NILAfiEuECgjunLzECgBO90VtKTXmLN37jWi+T2hPHlvL6fTJh05pnf7CrqwahWmLdE2OgW2D5Yt6cfdzVXs/FRkrmXF1ENuECr2kMDsYN8WWkQunrZb80TyaIakMMf67Tqf+Li9BT7BwtaPZgo6QB9qDHPBQ9p06V8kJhwdHmH69UjBhIMZuYLuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5J1e9B"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423166,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423166,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999999
    },
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423165,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423165,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECgjunLzECgBO90VtKTXmLN37jWi+T2hPHlvL6fTJh05pnf7CrqwahWmLdE2OgW2D5Yt6cfdzVXs/FRkrmXF1ENuECr2kMDsYN8WWkQunrZb80TyaIakMMf67Tqf+Li9BT7BwtaPZgo6QB9qDHPBQ9p06V8kJhwdHmH69UjBhIMZuYLuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5J1e9B",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423164,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423164,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000001
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
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
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
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
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "meta": 17,
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "meta": 17,
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuX6HEC6Lyfz/0ltl6ItdLmESzsnaqOcZlLJxsr79GMgBqArw56Yk/nuAn9SDD7EMYNf1i7BI0w+TO2mQGxnQbS3tpGRtXg=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "id": -576460752303423163,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBuyVeoWskH2r/3sIbWvQOQTqkRnkwqPgNIPRU80JyLgxjmoLO13vU+B0Qv/1eo4olMlv9Y/jabJV+nxJXeLJYHuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7ZJRt81"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423163,
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBuyVeoWskH2r/3sIbWvQOQTqkRnkwqPgNIPRU80JyLgxjmoLO13vU+B0Qv/1eo4olMlv9Y/jabJV+nxJXeLJYHuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7ZJRt81",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "id": -576460752303423162,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBqRwJPabZtRKeHM2z/BTt0F3OJ6ZYmF8Pux4le2bgu4LCd1M19vuoyRU5HfhXx0rtqRnCmd2jko/D+x2v6nPsFuEBuyVeoWskH2r/3sIbWvQOQTqkRnkwqPgNIPRU80JyLgxjmoLO13vU+B0Qv/1eo4olMlv9Y/jabJV+nxJXeLJYHuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7bkBjYa"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423162,
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "state": "tx_+NILAfiEuEBqRwJPabZtRKeHM2z/BTt0F3OJ6ZYmF8Pux4le2bgu4LCd1M19vuoyRU5HfhXx0rtqRnCmd2jko/D+x2v6nPsFuEBuyVeoWskH2r/3sIbWvQOQTqkRnkwqPgNIPRU80JyLgxjmoLO13vU+B0Qv/1eo4olMlv9Y/jabJV+nxJXeLJYHuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7bkBjYa"
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "state": "tx_+NILAfiEuEBqRwJPabZtRKeHM2z/BTt0F3OJ6ZYmF8Pux4le2bgu4LCd1M19vuoyRU5HfhXx0rtqRnCmd2jko/D+x2v6nPsFuEBuyVeoWskH2r/3sIbWvQOQTqkRnkwqPgNIPRU80JyLgxjmoLO13vU+B0Qv/1eo4olMlv9Y/jabJV+nxJXeLJYHuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7bkBjYa"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423161,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423161,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000000
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423160,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423160,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBqRwJPabZtRKeHM2z/BTt0F3OJ6ZYmF8Pux4le2bgu4LCd1M19vuoyRU5HfhXx0rtqRnCmd2jko/D+x2v6nPsFuEBuyVeoWskH2r/3sIbWvQOQTqkRnkwqPgNIPRU80JyLgxjmoLO13vU+B0Qv/1eo4olMlv9Y/jabJV+nxJXeLJYHuEj4RjkCoQbl+hxAui8n8/9JbZeiLXS5hEs7J2qjnGZSycbK+/RjIAagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7bkBjYa",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAALDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiYABL489v"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423159,
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
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423159,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423158,
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
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
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
  "channel_id": "ch_2kHTK3aWocecD2M2XfsdxAa5tarbMKWMUXSk1kR48WxnSTskSv",
  "id": -576460752303423158,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
