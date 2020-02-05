
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish_responder_stays%2F3301
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
      "fsm_id": "ba_oOOWGVWAa+qn2uDX9OBmnHjm8DJI98ocTVOK7LRwEslVLoUq"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=true&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish_responder_stays%2F3301
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
      "fsm_id": "ba_Ra+DXv50gtrFhYZYSCNzEO/rTA8Me/JBeBVIONBH4sFWJo8y"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4Xn3C8PA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423217,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAFrYH9yFRz9mcs01rsc3AjW/l40Wq4CUtgwIBfF5BZdPq9bn0dV/YOuNfQCwIuTWdP79OO3ZJ2c5ZvJZoIJiABuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uFzRK0jA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423217,
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
      "signed_tx": "tx_+MsLAfhCuEAFrYH9yFRz9mcs01rsc3AjW/l40Wq4CUtgwIBfF5BZdPq9bn0dV/YOuNfQCwIuTWdP79OO3ZJ2c5ZvJZoIJiABuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uFzRK0jA=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423216,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhABa2B/chUc/ZnLNNa7HNwI1v5eNFquAlLYMCAXxeQWXT6vW59HVf2DrjX0AsCLk1nT+/Tjt2SdnOWbyWaCCYgAbhAIXh+qVROmzToxViLQIgUZe4HYDyrACtqz3+l7fMBvkyS3Jh1eZOnp9xWq3zmYuOY+7lAa9a2SZjcJATBGJsoAriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hfnGPOo"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423216,
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhABa2B/chUc/ZnLNNa7HNwI1v5eNFquAlLYMCAXxeQWXT6vW59HVf2DrjX0AsCLk1nT+/Tjt2SdnOWbyWaCCYgAbhAIXh+qVROmzToxViLQIgUZe4HYDyrACtqz3+l7fMBvkyS3Jh1eZOnp9xWq3zmYuOY+7lAa9a2SZjcJATBGJsoAriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hfnGPOo",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhABa2B/chUc/ZnLNNa7HNwI1v5eNFquAlLYMCAXxeQWXT6vW59HVf2DrjX0AsCLk1nT+/Tjt2SdnOWbyWaCCYgAbhAIXh+qVROmzToxViLQIgUZe4HYDyrACtqz3+l7fMBvkyS3Jh1eZOnp9xWq3zmYuOY+7lAa9a2SZjcJATBGJsoAriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hfnGPOo",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhABa2B/chUc/ZnLNNa7HNwI1v5eNFquAlLYMCAXxeQWXT6vW59HVf2DrjX0AsCLk1nT+/Tjt2SdnOWbyWaCCYgAbhAIXh+qVROmzToxViLQIgUZe4HYDyrACtqz3+l7fMBvkyS3Jh1eZOnp9xWq3zmYuOY+7lAa9a2SZjcJATBGJsoAriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hfnGPOo",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhABa2B/chUc/ZnLNNa7HNwI1v5eNFquAlLYMCAXxeQWXT6vW59HVf2DrjX0AsCLk1nT+/Tjt2SdnOWbyWaCCYgAbhAIXh+qVROmzToxViLQIgUZe4HYDyrACtqz3+l7fMBvkyS3Jh1eZOnp9xWq3zmYuOY+7lAa9a2SZjcJATBGJsoAriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hfnGPOo",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "message": {
        "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "message": {
        "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
  "id": -576460752303423215,
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423215,
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

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "state": "tx_+QENCwH4hLhABa2B/chUc/ZnLNNa7HNwI1v5eNFquAlLYMCAXxeQWXT6vW59HVf2DrjX0AsCLk1nT+/Tjt2SdnOWbyWaCCYgAbhAIXh+qVROmzToxViLQIgUZe4HYDyrACtqz3+l7fMBvkyS3Jh1eZOnp9xWq3zmYuOY+7lAa9a2SZjcJATBGJsoAriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hfnGPOo"
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "state": "tx_+QENCwH4hLhABa2B/chUc/ZnLNNa7HNwI1v5eNFquAlLYMCAXxeQWXT6vW59HVf2DrjX0AsCLk1nT+/Tjt2SdnOWbyWaCCYgAbhAIXh+qVROmzToxViLQIgUZe4HYDyrACtqz3+l7fMBvkyS3Jh1eZOnp9xWq3zmYuOY+7lAa9a2SZjcJATBGJsoAriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hfnGPOo"
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "state": "tx_+QENCwH4hLhABa2B/chUc/ZnLNNa7HNwI1v5eNFquAlLYMCAXxeQWXT6vW59HVf2DrjX0AsCLk1nT+/Tjt2SdnOWbyWaCCYgAbhAIXh+qVROmzToxViLQIgUZe4HYDyrACtqz3+l7fMBvkyS3Jh1eZOnp9xWq3zmYuOY+7lAa9a2SZjcJATBGJsoAriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hfnGPOo"
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "state": "tx_+QENCwH4hLhABa2B/chUc/ZnLNNa7HNwI1v5eNFquAlLYMCAXxeQWXT6vW59HVf2DrjX0AsCLk1nT+/Tjt2SdnOWbyWaCCYgAbhAIXh+qVROmzToxViLQIgUZe4HYDyrACtqz3+l7fMBvkyS3Jh1eZOnp9xWq3zmYuOY+7lAa9a2SZjcJATBGJsoAriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hfnGPOo"
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "event": "peer_disconnected"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f&existing_fsm_id=ba_oOOWGVWAa%2Bqn2uDX9OBmnHjm8DJI98ocTVOK7LRwEslVLoUq&host=localhost&offchain_tx=tx_%2BQENCwH4hLhABa2B%2FchUc%2FZnLNNa7HNwI1v5eNFquAlLYMCAXxeQWXT6vW59HVf2DrjX0AsCLk1nT%2B%2FTjt2SdnOWbyWaCCYgAbhAIXh%2BqVROmzToxViLQIgUZe4HYDyrACtqz3%2Bl7fMBvkyS3Jh1eZOnp9xWq3zmYuOY%2B7lAa9a2SZjcJATBGJsoAriD%2BIEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu%2FSGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G%2BJNZ1%2B3HKCYNWL2rDf7hfnGPOo&port=13179&protocol=json-rpc&role=initiator
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
      "fsm_id": "ba_Lpihj+fBq7BLN1ae9XdXveuDeicIkwrxYvZmcMDMe1rsJKD9"
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "state": "tx_+QENCwH4hLhABa2B/chUc/ZnLNNa7HNwI1v5eNFquAlLYMCAXxeQWXT6vW59HVf2DrjX0AsCLk1nT+/Tjt2SdnOWbyWaCCYgAbhAIXh+qVROmzToxViLQIgUZe4HYDyrACtqz3+l7fMBvkyS3Jh1eZOnp9xWq3zmYuOY+7lAa9a2SZjcJATBGJsoAriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hfnGPOo"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423214,
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423214,
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjHJFiprwF//cDIZ3Ihqnw3zEhracgKFPnzU7TH6pNEAAqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B1Qnwjo=",
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
  "id": -576460752303423213,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC+apUxyjWgq46vbWgoJTZdoSSgN6M9TL3tTUBrNZEPmXGsxJlzMMXXbyPq1uSUibUCbJibIcleOB3a8dEGWuAHuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAea2ylU"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423213,
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC+apUxyjWgq46vbWgoJTZdoSSgN6M9TL3tTUBrNZEPmXGsxJlzMMXXbyPq1uSUibUCbJibIcleOB3a8dEGWuAHuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAea2ylU",
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
  "id": -576460752303423212,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECAfxTrbb6QIWEwETpES/J2BK5GdVrxlX1cBKxjwtdcD6+utcUATDtSFeCe08gfZxNBESlr2x/OdiMwURR1G4oPuEC+apUxyjWgq46vbWgoJTZdoSSgN6M9TL3tTUBrNZEPmXGsxJlzMMXXbyPq1uSUibUCbJibIcleOB3a8dEGWuAHuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfmWZbK"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423212,
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "state": "tx_+NILAfiEuECAfxTrbb6QIWEwETpES/J2BK5GdVrxlX1cBKxjwtdcD6+utcUATDtSFeCe08gfZxNBESlr2x/OdiMwURR1G4oPuEC+apUxyjWgq46vbWgoJTZdoSSgN6M9TL3tTUBrNZEPmXGsxJlzMMXXbyPq1uSUibUCbJibIcleOB3a8dEGWuAHuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfmWZbK"
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "state": "tx_+NILAfiEuECAfxTrbb6QIWEwETpES/J2BK5GdVrxlX1cBKxjwtdcD6+utcUATDtSFeCe08gfZxNBESlr2x/OdiMwURR1G4oPuEC+apUxyjWgq46vbWgoJTZdoSSgN6M9TL3tTUBrNZEPmXGsxJlzMMXXbyPq1uSUibUCbJibIcleOB3a8dEGWuAHuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfmWZbK"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423211,
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423211,
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
  "id": -576460752303423210,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423210,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECAfxTrbb6QIWEwETpES/J2BK5GdVrxlX1cBKxjwtdcD6+utcUATDtSFeCe08gfZxNBESlr2x/OdiMwURR1G4oPuEC+apUxyjWgq46vbWgoJTZdoSSgN6M9TL3tTUBrNZEPmXGsxJlzMMXXbyPq1uSUibUCbJibIcleOB3a8dEGWuAHuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfmWZbK",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423209,
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423209,
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjHJFiprwF//cDIZ3Ihqnw3zEhracgKFPnzU7TH6pNEAA6AWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7qkWCQI=",
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
  "id": -576460752303423208,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDWosW7+enJyA5pMJqWDFpcZeTWFgUizGI+c2FSuo0P33cphhy5bFl2EXLIwCa9WUIR/rPmBqzJupXBEZH7fEUAuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5XL1T3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423208,
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDWosW7+enJyA5pMJqWDFpcZeTWFgUizGI+c2FSuo0P33cphhy5bFl2EXLIwCa9WUIR/rPmBqzJupXBEZH7fEUAuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5XL1T3",
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
  "id": -576460752303423207,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDI5rxabvfQRGUE3B7FJpb/OoInrJndvF9qKDUufaWYvzmLbZK9nq/KJTGwE6HHOGIjXBTUZP6MHIXxCKFfGO8JuEDWosW7+enJyA5pMJqWDFpcZeTWFgUizGI+c2FSuo0P33cphhy5bFl2EXLIwCa9WUIR/rPmBqzJupXBEZH7fEUAuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7aq/7o"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423207,
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "state": "tx_+NILAfiEuEDI5rxabvfQRGUE3B7FJpb/OoInrJndvF9qKDUufaWYvzmLbZK9nq/KJTGwE6HHOGIjXBTUZP6MHIXxCKFfGO8JuEDWosW7+enJyA5pMJqWDFpcZeTWFgUizGI+c2FSuo0P33cphhy5bFl2EXLIwCa9WUIR/rPmBqzJupXBEZH7fEUAuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7aq/7o"
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "state": "tx_+NILAfiEuEDI5rxabvfQRGUE3B7FJpb/OoInrJndvF9qKDUufaWYvzmLbZK9nq/KJTGwE6HHOGIjXBTUZP6MHIXxCKFfGO8JuEDWosW7+enJyA5pMJqWDFpcZeTWFgUizGI+c2FSuo0P33cphhy5bFl2EXLIwCa9WUIR/rPmBqzJupXBEZH7fEUAuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7aq/7o"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423206,
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423206,
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
  "id": -576460752303423205,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423205,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDI5rxabvfQRGUE3B7FJpb/OoInrJndvF9qKDUufaWYvzmLbZK9nq/KJTGwE6HHOGIjXBTUZP6MHIXxCKFfGO8JuEDWosW7+enJyA5pMJqWDFpcZeTWFgUizGI+c2FSuo0P33cphhy5bFl2EXLIwCa9WUIR/rPmBqzJupXBEZH7fEUAuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7aq/7o",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423204,
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423204,
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjHJFiprwF//cDIZ3Ihqnw3zEhracgKFPnzU7TH6pNEABKArw56Yk/nuAn9SDD7EMYNf1i7BI0w+TO2mQGxnQbS3tuJGJYE=",
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
  "id": -576460752303423203,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDGn9m8W5YGOf/L4/M7g6yfhFGChIKb5BwsHrJAOm1k7r4mseTRhsVzmJayJq+1/0FjpXoHF/ibcQbfz22lYAAHuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Z8B2dJ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423203,
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDGn9m8W5YGOf/L4/M7g6yfhFGChIKb5BwsHrJAOm1k7r4mseTRhsVzmJayJq+1/0FjpXoHF/ibcQbfz22lYAAHuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Z8B2dJ",
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
  "id": -576460752303423202,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECDe8i4YkGfCeCU61tmbfwkM9rjnzAxjevyhWP34S9mz3K8FykTUYNQ3gypqs+BVyY+z5i6RSATXn7ryIkWLD0JuEDGn9m8W5YGOf/L4/M7g6yfhFGChIKb5BwsHrJAOm1k7r4mseTRhsVzmJayJq+1/0FjpXoHF/ibcQbfz22lYAAHuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7YM7xHt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423202,
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "state": "tx_+NILAfiEuECDe8i4YkGfCeCU61tmbfwkM9rjnzAxjevyhWP34S9mz3K8FykTUYNQ3gypqs+BVyY+z5i6RSATXn7ryIkWLD0JuEDGn9m8W5YGOf/L4/M7g6yfhFGChIKb5BwsHrJAOm1k7r4mseTRhsVzmJayJq+1/0FjpXoHF/ibcQbfz22lYAAHuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7YM7xHt"
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "state": "tx_+NILAfiEuECDe8i4YkGfCeCU61tmbfwkM9rjnzAxjevyhWP34S9mz3K8FykTUYNQ3gypqs+BVyY+z5i6RSATXn7ryIkWLD0JuEDGn9m8W5YGOf/L4/M7g6yfhFGChIKb5BwsHrJAOm1k7r4mseTRhsVzmJayJq+1/0FjpXoHF/ibcQbfz22lYAAHuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7YM7xHt"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423201,
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423201,
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
  "id": -576460752303423200,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423200,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECDe8i4YkGfCeCU61tmbfwkM9rjnzAxjevyhWP34S9mz3K8FykTUYNQ3gypqs+BVyY+z5i6RSATXn7ryIkWLD0JuEDGn9m8W5YGOf/L4/M7g6yfhFGChIKb5BwsHrJAOm1k7r4mseTRhsVzmJayJq+1/0FjpXoHF/ibcQbfz22lYAAHuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7YM7xHt",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAALDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiYABL489v"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423199,
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423199,
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjHJFiprwF//cDIZ3Ihqnw3zEhracgKFPnzU7TH6pNEABaAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7pdmT70=",
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
  "id": -576460752303423198,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBcAGCs5Xhne03+VuyXlOaLJzTnabkUg/s7s6x3oddLAy8m+nljzevBrnkSyR6IGfaa6j9O8OQYQfBiRXd7TBEGuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4BlIpO"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423198,
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBcAGCs5Xhne03+VuyXlOaLJzTnabkUg/s7s6x3oddLAy8m+nljzevBrnkSyR6IGfaa6j9O8OQYQfBiRXd7TBEGuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4BlIpO",
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
  "id": -576460752303423197,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAV3Xlq2KC5+CqhuRBhLc6DU8z43DrvWs/CWND5zEI6j7VCs6kVtwLuI+s1DIcnbTZwfWtJaXCaEru6pUY3GIUCuEBcAGCs5Xhne03+VuyXlOaLJzTnabkUg/s7s6x3oddLAy8m+nljzevBrnkSyR6IGfaa6j9O8OQYQfBiRXd7TBEGuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5GChMk"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423197,
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "state": "tx_+NILAfiEuEAV3Xlq2KC5+CqhuRBhLc6DU8z43DrvWs/CWND5zEI6j7VCs6kVtwLuI+s1DIcnbTZwfWtJaXCaEru6pUY3GIUCuEBcAGCs5Xhne03+VuyXlOaLJzTnabkUg/s7s6x3oddLAy8m+nljzevBrnkSyR6IGfaa6j9O8OQYQfBiRXd7TBEGuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5GChMk"
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "state": "tx_+NILAfiEuEAV3Xlq2KC5+CqhuRBhLc6DU8z43DrvWs/CWND5zEI6j7VCs6kVtwLuI+s1DIcnbTZwfWtJaXCaEru6pUY3GIUCuEBcAGCs5Xhne03+VuyXlOaLJzTnabkUg/s7s6x3oddLAy8m+nljzevBrnkSyR6IGfaa6j9O8OQYQfBiRXd7TBEGuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5GChMk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423196,
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423196,
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
  "id": -576460752303423195,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423195,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAV3Xlq2KC5+CqhuRBhLc6DU8z43DrvWs/CWND5zEI6j7VCs6kVtwLuI+s1DIcnbTZwfWtJaXCaEru6pUY3GIUCuEBcAGCs5Xhne03+VuyXlOaLJzTnabkUg/s7s6x3oddLAy8m+nljzevBrnkSyR6IGfaa6j9O8OQYQfBiRXd7TBEGuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5GChMk",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423194,
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423194,
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjHJFiprwF//cDIZ3Ihqnw3zEhracgKFPnzU7TH6pNEABqArw56Yk/nuAn9SDD7EMYNf1i7BI0w+TO2mQGxnQbS3trsPRGw=",
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
  "id": -576460752303423193,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB/HNFnAzzh7oqhFi9HkYqMbtrpBBUWK8ze2S/nO+h929L0YeFPNJL2rx29erjwtodbod1I6flT7WEW07HxPaYIuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7bm4DuN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423193,
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB/HNFnAzzh7oqhFi9HkYqMbtrpBBUWK8ze2S/nO+h929L0YeFPNJL2rx29erjwtodbod1I6flT7WEW07HxPaYIuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7bm4DuN",
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
  "id": -576460752303423192,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBzU1I323OZ6JV+mGgk+7ZBehfD0s/nkL40V1KT7HyhD7qVmvdQ/v+nmaSIn21091nYs01Cm8dpJWKaXefdimAGuEB/HNFnAzzh7oqhFi9HkYqMbtrpBBUWK8ze2S/nO+h929L0YeFPNJL2rx29erjwtodbod1I6flT7WEW07HxPaYIuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7ZJEJI4"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423192,
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "state": "tx_+NILAfiEuEBzU1I323OZ6JV+mGgk+7ZBehfD0s/nkL40V1KT7HyhD7qVmvdQ/v+nmaSIn21091nYs01Cm8dpJWKaXefdimAGuEB/HNFnAzzh7oqhFi9HkYqMbtrpBBUWK8ze2S/nO+h929L0YeFPNJL2rx29erjwtodbod1I6flT7WEW07HxPaYIuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7ZJEJI4"
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "state": "tx_+NILAfiEuEBzU1I323OZ6JV+mGgk+7ZBehfD0s/nkL40V1KT7HyhD7qVmvdQ/v+nmaSIn21091nYs01Cm8dpJWKaXefdimAGuEB/HNFnAzzh7oqhFi9HkYqMbtrpBBUWK8ze2S/nO+h929L0YeFPNJL2rx29erjwtodbod1I6flT7WEW07HxPaYIuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7ZJEJI4"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423191,
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423191,
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
  "id": -576460752303423190,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423190,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBzU1I323OZ6JV+mGgk+7ZBehfD0s/nkL40V1KT7HyhD7qVmvdQ/v+nmaSIn21091nYs01Cm8dpJWKaXefdimAGuEB/HNFnAzzh7oqhFi9HkYqMbtrpBBUWK8ze2S/nO+h929L0YeFPNJL2rx29erjwtodbod1I6flT7WEW07HxPaYIuEj4RjkCoQYxyRYqa8Bf/3AyGdyIap8N8xIa2nIChT581O0x+qTRAAagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7ZJEJI4",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAALDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiYABL489v"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423189,
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423189,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423188,
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
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
  "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
  "id": -576460752303423188,
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
    "channel_id": "ch_Nvhp33EMCj6XUqTaFb5knh5cV1PKmGSvcZAJeX66Gasv1u72f",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection
