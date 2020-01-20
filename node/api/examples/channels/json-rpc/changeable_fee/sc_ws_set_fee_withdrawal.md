
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=initiator
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
      "fsm_id": "ba_8MeEvyiKeuWL8X4LsP5wEcloozay3S7X0IXjIy9d9jEUZlJF"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=responder
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
      "fsm_id": "ba_nSgoMrimMGGDE7nfq0QWZHXAAl+i3oejjR8iZT7W3ROLSgDQ"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4kcRvVLg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422978,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDiffGEijuaifRTgKIjF6N3hQJYzCEPAf75vqeQq8IlR9+ghD+qGPcy/curdKN9LCoIKeUXdfz+3+MV6ARW2+sFuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uJJna2lY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422978,
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
      "signed_tx": "tx_+MsLAfhCuEDiffGEijuaifRTgKIjF6N3hQJYzCEPAf75vqeQq8IlR9+ghD+qGPcy/curdKN9LCoIKeUXdfz+3+MV6ARW2+sFuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uJJna2lY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422977,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAsaSBJLhSkrGgH5Zp8kOGcoGFTv+0/3JL75K1oqJUTIjrkZR3nxe8tiEnnDqJL31JWT4H7AzgFyUddU2dsL4wCbhA4n3xhIo7mon0U4CiIxejd4UCWMwhDwH++b6nkKvCJUffoIQ/qhj3Mv3Lq3SjfSwqCCnlF3X8/t/jFegEVtvrBbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7iQx7TzM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422977,
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAsaSBJLhSkrGgH5Zp8kOGcoGFTv+0/3JL75K1oqJUTIjrkZR3nxe8tiEnnDqJL31JWT4H7AzgFyUddU2dsL4wCbhA4n3xhIo7mon0U4CiIxejd4UCWMwhDwH++b6nkKvCJUffoIQ/qhj3Mv3Lq3SjfSwqCCnlF3X8/t/jFegEVtvrBbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7iQx7TzM",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAsaSBJLhSkrGgH5Zp8kOGcoGFTv+0/3JL75K1oqJUTIjrkZR3nxe8tiEnnDqJL31JWT4H7AzgFyUddU2dsL4wCbhA4n3xhIo7mon0U4CiIxejd4UCWMwhDwH++b6nkKvCJUffoIQ/qhj3Mv3Lq3SjfSwqCCnlF3X8/t/jFegEVtvrBbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7iQx7TzM",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAsaSBJLhSkrGgH5Zp8kOGcoGFTv+0/3JL75K1oqJUTIjrkZR3nxe8tiEnnDqJL31JWT4H7AzgFyUddU2dsL4wCbhA4n3xhIo7mon0U4CiIxejd4UCWMwhDwH++b6nkKvCJUffoIQ/qhj3Mv3Lq3SjfSwqCCnlF3X8/t/jFegEVtvrBbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7iQx7TzM",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAsaSBJLhSkrGgH5Zp8kOGcoGFTv+0/3JL75K1oqJUTIjrkZR3nxe8tiEnnDqJL31JWT4H7AzgFyUddU2dsL4wCbhA4n3xhIo7mon0U4CiIxejd4UCWMwhDwH++b6nkKvCJUffoIQ/qhj3Mv3Lq3SjfSwqCCnlF3X8/t/jFegEVtvrBbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7iQx7TzM",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "message": {
        "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "message": {
        "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
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
  "id": -576460752303422976,
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
  "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
  "id": -576460752303422976,
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "state": "tx_+QENCwH4hLhAsaSBJLhSkrGgH5Zp8kOGcoGFTv+0/3JL75K1oqJUTIjrkZR3nxe8tiEnnDqJL31JWT4H7AzgFyUddU2dsL4wCbhA4n3xhIo7mon0U4CiIxejd4UCWMwhDwH++b6nkKvCJUffoIQ/qhj3Mv3Lq3SjfSwqCCnlF3X8/t/jFegEVtvrBbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7iQx7TzM"
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "state": "tx_+QENCwH4hLhAsaSBJLhSkrGgH5Zp8kOGcoGFTv+0/3JL75K1oqJUTIjrkZR3nxe8tiEnnDqJL31JWT4H7AzgFyUddU2dsL4wCbhA4n3xhIo7mon0U4CiIxejd4UCWMwhDwH++b6nkKvCJUffoIQ/qhj3Mv3Lq3SjfSwqCCnlF3X8/t/jFegEVtvrBbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7iQx7TzM"
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "message": {
        "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "message": {
        "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
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
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
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
      "method": "channels.withdraw",
      "params": {
        "amount": "2"
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "message": {
        "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "message": {
        "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
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
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 2,
    "fee": 123456789876543
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBjpGUMlewYBqcAzRCfe8tUlI2El+cwL3jlNPXg0ry7XWoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79AIAhnBIhhsPP6DzbRVCr+DdkhskLcCBV1D3dvqUhQ5X1avffdiIqRPtFwIl9b6WcA==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303422975,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEDPlMYHK+M51x7GtSRxh5tqVPA9N1id7cQ6BAauaUtwfNZIbchkcS446e3lTYSBtFooiGNIO4e2f2groXu/zgYEuHT4cjQBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIZwSIYbDz+g820VQq/g3ZIbJC3AgVdQ93b6lIUOV9Wr333YiKkT7RcCJVB4HJw="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
  "id": -576460752303422975,
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEDPlMYHK+M51x7GtSRxh5tqVPA9N1id7cQ6BAauaUtwfNZIbchkcS446e3lTYSBtFooiGNIO4e2f2groXu/zgYEuHT4cjQBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIZwSIYbDz+g820VQq/g3ZIbJC3AgVdQ93b6lIUOV9Wr333YiKkT7RcCJVB4HJw=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303422974,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuECeVcQPZmL4bAU3XgYpqxCu1SIiLd+m8X5dHVgD/GMskkRDQCW3Up9NnQFb+b/h+EbZT+0beVzyD6NF/Toj1y4MuEDPlMYHK+M51x7GtSRxh5tqVPA9N1id7cQ6BAauaUtwfNZIbchkcS446e3lTYSBtFooiGNIO4e2f2groXu/zgYEuHT4cjQBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIZwSIYbDz+g820VQq/g3ZIbJC3AgVdQ93b6lIUOV9Wr333YiKkT7RcCJVhz+/I="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
  "id": -576460752303422974,
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuECeVcQPZmL4bAU3XgYpqxCu1SIiLd+m8X5dHVgD/GMskkRDQCW3Up9NnQFb+b/h+EbZT+0beVzyD6NF/Toj1y4MuEDPlMYHK+M51x7GtSRxh5tqVPA9N1id7cQ6BAauaUtwfNZIbchkcS446e3lTYSBtFooiGNIO4e2f2groXu/zgYEuHT4cjQBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIZwSIYbDz+g820VQq/g3ZIbJC3AgVdQ93b6lIUOV9Wr333YiKkT7RcCJVhz+/I=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuECeVcQPZmL4bAU3XgYpqxCu1SIiLd+m8X5dHVgD/GMskkRDQCW3Up9NnQFb+b/h+EbZT+0beVzyD6NF/Toj1y4MuEDPlMYHK+M51x7GtSRxh5tqVPA9N1id7cQ6BAauaUtwfNZIbchkcS446e3lTYSBtFooiGNIO4e2f2groXu/zgYEuHT4cjQBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIZwSIYbDz+g820VQq/g3ZIbJC3AgVdQ93b6lIUOV9Wr333YiKkT7RcCJVhz+/I=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "message": {
        "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "message": {
        "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "info": "Hello back",
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
      }
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECeVcQPZmL4bAU3XgYpqxCu1SIiLd+m8X5dHVgD/GMskkRDQCW3Up9NnQFb+b/h+EbZT+0beVzyD6NF/Toj1y4MuEDPlMYHK+M51x7GtSRxh5tqVPA9N1id7cQ6BAauaUtwfNZIbchkcS446e3lTYSBtFooiGNIO4e2f2groXu/zgYEuHT4cjQBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIZwSIYbDz+g820VQq/g3ZIbJC3AgVdQ93b6lIUOV9Wr333YiKkT7RcCJVhz+/I=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECeVcQPZmL4bAU3XgYpqxCu1SIiLd+m8X5dHVgD/GMskkRDQCW3Up9NnQFb+b/h+EbZT+0beVzyD6NF/Toj1y4MuEDPlMYHK+M51x7GtSRxh5tqVPA9N1id7cQ6BAauaUtwfNZIbchkcS446e3lTYSBtFooiGNIO4e2f2groXu/zgYEuHT4cjQBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIZwSIYbDz+g820VQq/g3ZIbJC3AgVdQ93b6lIUOV9Wr333YiKkT7RcCJVhz+/I=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "state": "tx_+P4LAfiEuECeVcQPZmL4bAU3XgYpqxCu1SIiLd+m8X5dHVgD/GMskkRDQCW3Up9NnQFb+b/h+EbZT+0beVzyD6NF/Toj1y4MuEDPlMYHK+M51x7GtSRxh5tqVPA9N1id7cQ6BAauaUtwfNZIbchkcS446e3lTYSBtFooiGNIO4e2f2groXu/zgYEuHT4cjQBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIZwSIYbDz+g820VQq/g3ZIbJC3AgVdQ93b6lIUOV9Wr333YiKkT7RcCJVhz+/I="
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "state": "tx_+P4LAfiEuECeVcQPZmL4bAU3XgYpqxCu1SIiLd+m8X5dHVgD/GMskkRDQCW3Up9NnQFb+b/h+EbZT+0beVzyD6NF/Toj1y4MuEDPlMYHK+M51x7GtSRxh5tqVPA9N1id7cQ6BAauaUtwfNZIbchkcS446e3lTYSBtFooiGNIO4e2f2groXu/zgYEuHT4cjQBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIZwSIYbDz+g820VQq/g3ZIbJC3AgVdQ93b6lIUOV9Wr333YiKkT7RcCJVhz+/I="
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
    "info": "Hello",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "message": {
        "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "message": {
        "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "info": "Hello back",
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
  "method": "channels.withdraw",
  "params": {
    "amount": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
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
      "method": "channels.withdraw",
      "params": {
        "amount": "2"
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
  "method": "channels.message",
  "params": {
    "info": "Hello",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "message": {
        "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "message": {
        "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "info": "Hello back",
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
  "method": "channels.withdraw",
  "params": {
    "amount": 2,
    "fee": 123456789876543
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBjpGUMlewYBqcAzRCfe8tUlI2El+cwL3jlNPXg0ry7XWoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEAIAhnBIhhsPP6BK0MMMBNB9J+gSTUtqqYfmb9GBimM3qN6hsS4K0QhzQgMO4RdLKw==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303422973,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuED7LFg2QqEFOjg6Fw9vNpTMElPwoJaIVXyWw4yWl3D8hqvmETsX3pMbTuqFl3BUh+17Q7w39c4+jH37DiwhQesOuHT4cjQBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIZwSIYbDz+gStDDDATQfSfoEk1LaqmH5m/RgYpjN6jeobEuCtEIc0IDDhHNpBk="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
  "id": -576460752303422973,
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "signed_tx": "tx_+LwLAfhCuED7LFg2QqEFOjg6Fw9vNpTMElPwoJaIVXyWw4yWl3D8hqvmETsX3pMbTuqFl3BUh+17Q7w39c4+jH37DiwhQesOuHT4cjQBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIZwSIYbDz+gStDDDATQfSfoEk1LaqmH5m/RgYpjN6jeobEuCtEIc0IDDhHNpBk=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303422972,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuECudl46rdZ8kTyC2Lg0NtqRf8gb0MWWqbx9cJeBf6s6b2Gyx2BlDCtyQtGjTEMBKcCKB1LBjhSsHsgOW3O3vAsCuED7LFg2QqEFOjg6Fw9vNpTMElPwoJaIVXyWw4yWl3D8hqvmETsX3pMbTuqFl3BUh+17Q7w39c4+jH37DiwhQesOuHT4cjQBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIZwSIYbDz+gStDDDATQfSfoEk1LaqmH5m/RgYpjN6jeobEuCtEIc0IDDrfffZM="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
  "id": -576460752303422972,
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuECudl46rdZ8kTyC2Lg0NtqRf8gb0MWWqbx9cJeBf6s6b2Gyx2BlDCtyQtGjTEMBKcCKB1LBjhSsHsgOW3O3vAsCuED7LFg2QqEFOjg6Fw9vNpTMElPwoJaIVXyWw4yWl3D8hqvmETsX3pMbTuqFl3BUh+17Q7w39c4+jH37DiwhQesOuHT4cjQBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIZwSIYbDz+gStDDDATQfSfoEk1LaqmH5m/RgYpjN6jeobEuCtEIc0IDDrfffZM=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuECudl46rdZ8kTyC2Lg0NtqRf8gb0MWWqbx9cJeBf6s6b2Gyx2BlDCtyQtGjTEMBKcCKB1LBjhSsHsgOW3O3vAsCuED7LFg2QqEFOjg6Fw9vNpTMElPwoJaIVXyWw4yWl3D8hqvmETsX3pMbTuqFl3BUh+17Q7w39c4+jH37DiwhQesOuHT4cjQBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIZwSIYbDz+gStDDDATQfSfoEk1LaqmH5m/RgYpjN6jeobEuCtEIc0IDDrfffZM=",
      "type": "channel_withdraw_tx"
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
    "info": "Hello",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "message": {
        "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "message": {
        "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "info": "Hello back",
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
      }
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECudl46rdZ8kTyC2Lg0NtqRf8gb0MWWqbx9cJeBf6s6b2Gyx2BlDCtyQtGjTEMBKcCKB1LBjhSsHsgOW3O3vAsCuED7LFg2QqEFOjg6Fw9vNpTMElPwoJaIVXyWw4yWl3D8hqvmETsX3pMbTuqFl3BUh+17Q7w39c4+jH37DiwhQesOuHT4cjQBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIZwSIYbDz+gStDDDATQfSfoEk1LaqmH5m/RgYpjN6jeobEuCtEIc0IDDrfffZM=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECudl46rdZ8kTyC2Lg0NtqRf8gb0MWWqbx9cJeBf6s6b2Gyx2BlDCtyQtGjTEMBKcCKB1LBjhSsHsgOW3O3vAsCuED7LFg2QqEFOjg6Fw9vNpTMElPwoJaIVXyWw4yWl3D8hqvmETsX3pMbTuqFl3BUh+17Q7w39c4+jH37DiwhQesOuHT4cjQBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIZwSIYbDz+gStDDDATQfSfoEk1LaqmH5m/RgYpjN6jeobEuCtEIc0IDDrfffZM=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "state": "tx_+P4LAfiEuECudl46rdZ8kTyC2Lg0NtqRf8gb0MWWqbx9cJeBf6s6b2Gyx2BlDCtyQtGjTEMBKcCKB1LBjhSsHsgOW3O3vAsCuED7LFg2QqEFOjg6Fw9vNpTMElPwoJaIVXyWw4yWl3D8hqvmETsX3pMbTuqFl3BUh+17Q7w39c4+jH37DiwhQesOuHT4cjQBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIZwSIYbDz+gStDDDATQfSfoEk1LaqmH5m/RgYpjN6jeobEuCtEIc0IDDrfffZM="
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "state": "tx_+P4LAfiEuECudl46rdZ8kTyC2Lg0NtqRf8gb0MWWqbx9cJeBf6s6b2Gyx2BlDCtyQtGjTEMBKcCKB1LBjhSsHsgOW3O3vAsCuED7LFg2QqEFOjg6Fw9vNpTMElPwoJaIVXyWw4yWl3D8hqvmETsX3pMbTuqFl3BUh+17Q7w39c4+jH37DiwhQesOuHT4cjQBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIZwSIYbDz+gStDDDATQfSfoEk1LaqmH5m/RgYpjN6jeobEuCtEIc0IDDrfffZM="
    }
  },
  "version": 1
}
```

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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBjpGUMlewYBqcAzRCfe8tUlI2El+cwL3jlNPXg0ry7XWoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY2kdavv/2GG0jrV9//AIYSMJzlQAAmrl7ptg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422971,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEAxLz8uBHZ56HWtMHeflZOzNPD/fI35gjLQP2qGZj5sdMOYU0gKsX9HrCgMwSr5Y+P2fPtCy/At4UgfsUBaJFQPuF/4XTUBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7/9hhtI61ff/wCGEjCc5UAAJoQuQWE="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
  "id": -576460752303422971,
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEAxLz8uBHZ56HWtMHeflZOzNPD/fI35gjLQP2qGZj5sdMOYU0gKsX9HrCgMwSr5Y+P2fPtCy/At4UgfsUBaJFQPuF/4XTUBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7/9hhtI61ff/wCGEjCc5UAAJoQuQWE=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422970,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEAxLz8uBHZ56HWtMHeflZOzNPD/fI35gjLQP2qGZj5sdMOYU0gKsX9HrCgMwSr5Y+P2fPtCy/At4UgfsUBaJFQPuEC4feCt/5zEOoTx9ldyaHNWr0hqkp4qNzjuqJgQnGPvwFiclw+pNr9ukyofOAEW+aAAjSDRbStqbPPlyZF/CIcMuF/4XTUBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7/9hhtI61ff/wCGEjCc5UAAJjfuK7g="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
  "id": -576460752303422970,
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAxLz8uBHZ56HWtMHeflZOzNPD/fI35gjLQP2qGZj5sdMOYU0gKsX9HrCgMwSr5Y+P2fPtCy/At4UgfsUBaJFQPuEC4feCt/5zEOoTx9ldyaHNWr0hqkp4qNzjuqJgQnGPvwFiclw+pNr9ukyofOAEW+aAAjSDRbStqbPPlyZF/CIcMuF/4XTUBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7/9hhtI61ff/wCGEjCc5UAAJjfuK7g=",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAxLz8uBHZ56HWtMHeflZOzNPD/fI35gjLQP2qGZj5sdMOYU0gKsX9HrCgMwSr5Y+P2fPtCy/At4UgfsUBaJFQPuEC4feCt/5zEOoTx9ldyaHNWr0hqkp4qNzjuqJgQnGPvwFiclw+pNr9ukyofOAEW+aAAjSDRbStqbPPlyZF/CIcMuF/4XTUBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7/9hhtI61ff/wCGEjCc5UAAJjfuK7g=",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAxLz8uBHZ56HWtMHeflZOzNPD/fI35gjLQP2qGZj5sdMOYU0gKsX9HrCgMwSr5Y+P2fPtCy/At4UgfsUBaJFQPuEC4feCt/5zEOoTx9ldyaHNWr0hqkp4qNzjuqJgQnGPvwFiclw+pNr9ukyofOAEW+aAAjSDRbStqbPPlyZF/CIcMuF/4XTUBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7/9hhtI61ff/wCGEjCc5UAAJjfuK7g=",
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
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAxLz8uBHZ56HWtMHeflZOzNPD/fI35gjLQP2qGZj5sdMOYU0gKsX9HrCgMwSr5Y+P2fPtCy/At4UgfsUBaJFQPuEC4feCt/5zEOoTx9ldyaHNWr0hqkp4qNzjuqJgQnGPvwFiclw+pNr9ukyofOAEW+aAAjSDRbStqbPPlyZF/CIcMuF/4XTUBoQY6RlDJXsGAanAM0Qn3vLVJSNhJfnMC945TT14NK8u11qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7/9hhtI61ff/wCGEjCc5UAAJjfuK7g=",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
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
    "channel_id": "ch_SfYoGimQ17dE8A8m2zWkhYoFkBzaBaMXHXiaaa9b8sNacRiym",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator closes WebSocket connection
