
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
      "fsm_id": "ba_kiBwaAJ1hXtdfNqDg5hjQ1iypyo5t9dojgGQ3HYam7DABmlr"
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
      "fsm_id": "ba_6qRk7bZ9BcKU8aEjUYZetlBW5b/OKPRaWDRc5oxmspk8V44+"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4vtKkohg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422919,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECnk4PeGC0Y8GaKCLcDqjZiF3vNSIyx3w5wbcX9gpkm0G/SXIZiR7wErcEuhXoPQZzRKHj1NGsNOXIK8ee+VjELuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uL/y7HE8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422919,
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
      "signed_tx": "tx_+MsLAfhCuECnk4PeGC0Y8GaKCLcDqjZiF3vNSIyx3w5wbcX9gpkm0G/SXIZiR7wErcEuhXoPQZzRKHj1NGsNOXIK8ee+VjELuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uL/y7HE8=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422918,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAHG0WJwmw+QnNF1RY/IxpWtCVrYjfZDzQrO7I9IQUNKeRuwFLyQoYJPiHqA1C3zuJn93625SbjSW23ii4qcY8B7hAp5OD3hgtGPBmigi3A6o2Yhd7zUiMsd8OcG3F/YKZJtBv0lyGYke8BK3BLoV6D0Gc0Sh49TRrDTlyCvHnvlYxC7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7i+eUcgX"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422918,
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAHG0WJwmw+QnNF1RY/IxpWtCVrYjfZDzQrO7I9IQUNKeRuwFLyQoYJPiHqA1C3zuJn93625SbjSW23ii4qcY8B7hAp5OD3hgtGPBmigi3A6o2Yhd7zUiMsd8OcG3F/YKZJtBv0lyGYke8BK3BLoV6D0Gc0Sh49TRrDTlyCvHnvlYxC7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7i+eUcgX",
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAHG0WJwmw+QnNF1RY/IxpWtCVrYjfZDzQrO7I9IQUNKeRuwFLyQoYJPiHqA1C3zuJn93625SbjSW23ii4qcY8B7hAp5OD3hgtGPBmigi3A6o2Yhd7zUiMsd8OcG3F/YKZJtBv0lyGYke8BK3BLoV6D0Gc0Sh49TRrDTlyCvHnvlYxC7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7i+eUcgX",
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAHG0WJwmw+QnNF1RY/IxpWtCVrYjfZDzQrO7I9IQUNKeRuwFLyQoYJPiHqA1C3zuJn93625SbjSW23ii4qcY8B7hAp5OD3hgtGPBmigi3A6o2Yhd7zUiMsd8OcG3F/YKZJtBv0lyGYke8BK3BLoV6D0Gc0Sh49TRrDTlyCvHnvlYxC7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7i+eUcgX",
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAHG0WJwmw+QnNF1RY/IxpWtCVrYjfZDzQrO7I9IQUNKeRuwFLyQoYJPiHqA1C3zuJn93625SbjSW23ii4qcY8B7hAp5OD3hgtGPBmigi3A6o2Yhd7zUiMsd8OcG3F/YKZJtBv0lyGYke8BK3BLoV6D0Gc0Sh49TRrDTlyCvHnvlYxC7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7i+eUcgX",
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
    "data": {
      "message": {
        "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
    "data": {
      "message": {
        "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
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
  "id": -576460752303422917,
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
  "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
  "id": -576460752303422917,
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
    "data": {
      "state": "tx_+QENCwH4hLhAHG0WJwmw+QnNF1RY/IxpWtCVrYjfZDzQrO7I9IQUNKeRuwFLyQoYJPiHqA1C3zuJn93625SbjSW23ii4qcY8B7hAp5OD3hgtGPBmigi3A6o2Yhd7zUiMsd8OcG3F/YKZJtBv0lyGYke8BK3BLoV6D0Gc0Sh49TRrDTlyCvHnvlYxC7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7i+eUcgX"
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
    "data": {
      "state": "tx_+QENCwH4hLhAHG0WJwmw+QnNF1RY/IxpWtCVrYjfZDzQrO7I9IQUNKeRuwFLyQoYJPiHqA1C3zuJn93625SbjSW23ii4qcY8B7hAp5OD3hgtGPBmigi3A6o2Yhd7zUiMsd8OcG3F/YKZJtBv0lyGYke8BK3BLoV6D0Gc0Sh49TRrDTlyCvHnvlYxC7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7i+eUcgX"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
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
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
    "data": {
      "poi": "pi_+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMDiSa4B"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422916,
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
  "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
  "id": -576460752303422916,
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuDy52wMk6W8AVulriHvh1I3e8e1Y6B3zchiAZYv/ahrAqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B5iQWY0=",
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
  "id": -576460752303422915,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC5np/jhZCyEPMVgdTMnZCY0kJl6iPaQSyOyr9HenM3yiqfCqVB2vnlEMKrjv9a5sQV+oq/+bnQ1igIy9Dh8wEIuEj4RjkCoQbg8udsDJOlvAFbpa4h74dSN3vHtWOgd83IYgGWL/2oawKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAckMLR0"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
  "id": -576460752303422915,
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC5np/jhZCyEPMVgdTMnZCY0kJl6iPaQSyOyr9HenM3yiqfCqVB2vnlEMKrjv9a5sQV+oq/+bnQ1igIy9Dh8wEIuEj4RjkCoQbg8udsDJOlvAFbpa4h74dSN3vHtWOgd83IYgGWL/2oawKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAckMLR0",
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
  "id": -576460752303422914,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECkydMYz0rf+rCqE8khH4Q2tkzOjFBIt8IzlgktMYDvmx7JXJT3gjVVqFicL4q7CpJcyknVbRrRBRIXD/zo8ZAHuEC5np/jhZCyEPMVgdTMnZCY0kJl6iPaQSyOyr9HenM3yiqfCqVB2vnlEMKrjv9a5sQV+oq/+bnQ1igIy9Dh8wEIuEj4RjkCoQbg8udsDJOlvAFbpa4h74dSN3vHtWOgd83IYgGWL/2oawKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAets/NT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
  "id": -576460752303422914,
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
    "data": {
      "state": "tx_+NILAfiEuECkydMYz0rf+rCqE8khH4Q2tkzOjFBIt8IzlgktMYDvmx7JXJT3gjVVqFicL4q7CpJcyknVbRrRBRIXD/zo8ZAHuEC5np/jhZCyEPMVgdTMnZCY0kJl6iPaQSyOyr9HenM3yiqfCqVB2vnlEMKrjv9a5sQV+oq/+bnQ1igIy9Dh8wEIuEj4RjkCoQbg8udsDJOlvAFbpa4h74dSN3vHtWOgd83IYgGWL/2oawKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAets/NT"
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
    "data": {
      "state": "tx_+NILAfiEuECkydMYz0rf+rCqE8khH4Q2tkzOjFBIt8IzlgktMYDvmx7JXJT3gjVVqFicL4q7CpJcyknVbRrRBRIXD/zo8ZAHuEC5np/jhZCyEPMVgdTMnZCY0kJl6iPaQSyOyr9HenM3yiqfCqVB2vnlEMKrjv9a5sQV+oq/+bnQ1igIy9Dh8wEIuEj4RjkCoQbg8udsDJOlvAFbpa4h74dSN3vHtWOgd83IYgGWL/2oawKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAets/NT"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422913,
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
  "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
  "id": -576460752303422913,
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
  "id": -576460752303422912,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
  "id": -576460752303422912,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECkydMYz0rf+rCqE8khH4Q2tkzOjFBIt8IzlgktMYDvmx7JXJT3gjVVqFicL4q7CpJcyknVbRrRBRIXD/zo8ZAHuEC5np/jhZCyEPMVgdTMnZCY0kJl6iPaQSyOyr9HenM3yiqfCqVB2vnlEMKrjv9a5sQV+oq/+bnQ1igIy9Dh8wEIuEj4RjkCoQbg8udsDJOlvAFbpa4h74dSN3vHtWOgd83IYgGWL/2oawKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAets/NT",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECkydMYz0rf+rCqE8khH4Q2tkzOjFBIt8IzlgktMYDvmx7JXJT3gjVVqFicL4q7CpJcyknVbRrRBRIXD/zo8ZAHuEC5np/jhZCyEPMVgdTMnZCY0kJl6iPaQSyOyr9HenM3yiqfCqVB2vnlEMKrjv9a5sQV+oq/+bnQ1igIy9Dh8wEIuEj4RjkCoQbg8udsDJOlvAFbpa4h74dSN3vHtWOgd83IYgGWL/2oawKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAets/NT",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECkydMYz0rf+rCqE8khH4Q2tkzOjFBIt8IzlgktMYDvmx7JXJT3gjVVqFicL4q7CpJcyknVbRrRBRIXD/zo8ZAHuEC5np/jhZCyEPMVgdTMnZCY0kJl6iPaQSyOyr9HenM3yiqfCqVB2vnlEMKrjv9a5sQV+oq/+bnQ1igIy9Dh8wEIuEj4RjkCoQbg8udsDJOlvAFbpa4h74dSN3vHtWOgd83IYgGWL/2oawKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAets/NT",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
    "data": {
      "event": "closing"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422911,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {
    "fee": 123456789876543
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
  "id": -576460752303422911,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBuDy52wMk6W8AVulriHvh1I3e8e1Y6B3zchiAZYv/ahroQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79LjU+NILAfiEuECkydMYz0rf+rCqE8khH4Q2tkzOjFBIt8IzlgktMYDvmx7JXJT3gjVVqFicL4q7CpJcyknVbRrRBRIXD/zo8ZAHuEC5np/jhZCyEPMVgdTMnZCY0kJl6iPaQSyOyr9HenM3yiqfCqVB2vnlEMKrjv9a5sQV+oq/+bnQ1igIy9Dh8wEIuEj4RjkCoQbg8udsDJOlvAFbpa4h74dSN3vHtWOgd83IYgGWL/2oawKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAe5AUz5AUk8AfkBP/kBPKBr5sKqJEGy2c6K7OYj3B0QSM9YKqp12Cwu0FcoBE12iPkBGPhPoEqVXL/Gi63p37+99IW1AH7Eb//F/0G9uCVe9zFlBvdG7aAxNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAvh0oGvmwqokQbLZzors5iPcHRBIz1gqqnXYLC7QVygETXaI+FGAgICAgICAgICAgICgbYJjbN6iM9NklD1uSm6sox3iiItBMXXpvq1p2MXyRnGgSpVcv8aLrenfv730hbUAfsRv/8X/Qb24JV73MWUG90aAgID4T6BtgmNs3qIz02SUPW5KbqyjHeKIi0Exdem+rWnYxfJGce2gNbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/7AwMDAwACGcEiGGw8/MX6fLBA=",
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
  "method": "channels.slash_sign",
  "params": {
    "signed_tx": "tx_+QLACwH4QrhAhBMURpOMXZDU9wIuTW/aMv2doWBBof0QQvte3LwIcFp42CMOvNfrrvGUYRyZBs/aBkzQTUzeFgBfM/4APrNFA7kCd/kCdDcBoQbg8udsDJOlvAFbpa4h74dSN3vHtWOgd83IYgGWL/2oa6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/S41PjSCwH4hLhApMnTGM9K3/qwqhPJIR+ENrZMzoxQSLfCM5YJLTGA75seyVyU94I1VahYnC+KuwqSXMpJ1W0a0QUSFw/86PGQB7hAuZ6f44WQshDzFYHUzJ2QmNJCZeoj2kEsjsq/R3pzN8oqnwqlQdr55RDCq47/WubEFfqKv/m50NYoCMvQ4fMBCLhI+EY5AqEG4PLnbAyTpbwBW6WuIe+HUjd7x7VjoHfNyGIBli/9qGsCoCob2XomoLXVasfWjCsSocPPoSuXDKwFnKboiPTlQXwHuQFM+QFJPAH5AT/5ATyga+bCqiRBstnOiuzmI9wdEEjPWCqqddgsLtBXKARNdoj5ARj4T6BKlVy/xout6d+/vfSFtQB+xG//xf9BvbglXvcxZQb3Ru2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAL4dKBr5sKqJEGy2c6K7OYj3B0QSM9YKqp12Cwu0FcoBE12iPhRgICAgICAgICAgICAoG2CY2zeojPTZJQ9bkpurKMd4oiLQTF16b6tadjF8kZxoEqVXL/Gi63p37+99IW1AH7Eb//F/0G9uCVe9zFlBvdGgICA+E+gbYJjbN6iM9NklD1uSm6sox3iiItBMXXpvq1p2MXyRnHtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl/+wMDAwMAAhnBIhhsPPzGzn4et"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAhBMURpOMXZDU9wIuTW/aMv2doWBBof0QQvte3LwIcFp42CMOvNfrrvGUYRyZBs/aBkzQTUzeFgBfM/4APrNFA7kCd/kCdDcBoQbg8udsDJOlvAFbpa4h74dSN3vHtWOgd83IYgGWL/2oa6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/S41PjSCwH4hLhApMnTGM9K3/qwqhPJIR+ENrZMzoxQSLfCM5YJLTGA75seyVyU94I1VahYnC+KuwqSXMpJ1W0a0QUSFw/86PGQB7hAuZ6f44WQshDzFYHUzJ2QmNJCZeoj2kEsjsq/R3pzN8oqnwqlQdr55RDCq47/WubEFfqKv/m50NYoCMvQ4fMBCLhI+EY5AqEG4PLnbAyTpbwBW6WuIe+HUjd7x7VjoHfNyGIBli/9qGsCoCob2XomoLXVasfWjCsSocPPoSuXDKwFnKboiPTlQXwHuQFM+QFJPAH5AT/5ATyga+bCqiRBstnOiuzmI9wdEEjPWCqqddgsLtBXKARNdoj5ARj4T6BKlVy/xout6d+/vfSFtQB+xG//xf9BvbglXvcxZQb3Ru2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAL4dKBr5sKqJEGy2c6K7OYj3B0QSM9YKqp12Cwu0FcoBE12iPhRgICAgICAgICAgICAoG2CY2zeojPTZJQ9bkpurKMd4oiLQTF16b6tadjF8kZxoEqVXL/Gi63p37+99IW1AH7Eb//F/0G9uCVe9zFlBvdGgICA+E+gbYJjbN6iM9NklD1uSm6sox3iiItBMXXpvq1p2MXyRnHtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl/+wMDAwMAAhnBIhhsPPzGzn4et",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAhBMURpOMXZDU9wIuTW/aMv2doWBBof0QQvte3LwIcFp42CMOvNfrrvGUYRyZBs/aBkzQTUzeFgBfM/4APrNFA7kCd/kCdDcBoQbg8udsDJOlvAFbpa4h74dSN3vHtWOgd83IYgGWL/2oa6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/S41PjSCwH4hLhApMnTGM9K3/qwqhPJIR+ENrZMzoxQSLfCM5YJLTGA75seyVyU94I1VahYnC+KuwqSXMpJ1W0a0QUSFw/86PGQB7hAuZ6f44WQshDzFYHUzJ2QmNJCZeoj2kEsjsq/R3pzN8oqnwqlQdr55RDCq47/WubEFfqKv/m50NYoCMvQ4fMBCLhI+EY5AqEG4PLnbAyTpbwBW6WuIe+HUjd7x7VjoHfNyGIBli/9qGsCoCob2XomoLXVasfWjCsSocPPoSuXDKwFnKboiPTlQXwHuQFM+QFJPAH5AT/5ATyga+bCqiRBstnOiuzmI9wdEEjPWCqqddgsLtBXKARNdoj5ARj4T6BKlVy/xout6d+/vfSFtQB+xG//xf9BvbglXvcxZQb3Ru2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAL4dKBr5sKqJEGy2c6K7OYj3B0QSM9YKqp12Cwu0FcoBE12iPhRgICAgICAgICAgICAoG2CY2zeojPTZJQ9bkpurKMd4oiLQTF16b6tadjF8kZxoEqVXL/Gi63p37+99IW1AH7Eb//F/0G9uCVe9zFlBvdGgICA+E+gbYJjbN6iM9NklD1uSm6sox3iiItBMXXpvq1p2MXyRnHtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl/+wMDAwMAAhnBIhhsPPzGzn4et",
      "type": "channel_slash_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBuDy52wMk6W8AVulriHvh1I3e8e1Y6B3zchiAZYv/ahroQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIY/qiUiX/6GJGE5yoACAIYPXtZ/KAATUpIvjg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEDN8khECfLpcHLc3HwkmMtt6Uf4C+Q9QjRgb+laww0vE1X9x+xHzL3vPnhiLjwJ9NhlFm0U0GGlaOPbKKQYN7kHuF/4XTgBoQbg8udsDJOlvAFbpa4h74dSN3vHtWOgd83IYgGWL/2oa6EB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl/+hiRhOcqAAgCGD17WfygAEy7S7gs="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDN8khECfLpcHLc3HwkmMtt6Uf4C+Q9QjRgb+laww0vE1X9x+xHzL3vPnhiLjwJ9NhlFm0U0GGlaOPbKKQYN7kHuF/4XTgBoQbg8udsDJOlvAFbpa4h74dSN3vHtWOgd83IYgGWL/2oa6EB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl/+hiRhOcqAAgCGD17WfygAEy7S7gs=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDN8khECfLpcHLc3HwkmMtt6Uf4C+Q9QjRgb+laww0vE1X9x+xHzL3vPnhiLjwJ9NhlFm0U0GGlaOPbKKQYN7kHuF/4XTgBoQbg8udsDJOlvAFbpa4h74dSN3vHtWOgd83IYgGWL/2oa6EB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl/+hiRhOcqAAgCGD17WfygAEy7S7gs=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
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
    "channel_id": "ch_2i51wqEumJXbiwyJCb4TAxFyqnTM7cYoFMQFMuUcqHBnL7Y41p",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator closes WebSocket connection

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
      "fsm_id": "ba_5bM8WxYpp2n5TKNZXn9kRzUs21tMlMCNfZAIu8IWmFzxIOnC"
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
      "fsm_id": "ba_BPSG2oNIQzz89cmzW6HjA7FjZ9p9k6d9Q1XNUdN9vXs5Wpsc"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4y1eR82A==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422910,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEB8m/LDSUJX4xE/Voio2bD2BzHLqdZD6p1YC0YDDI/2kuAL21IrCRIkgctE1hFcK2DBMbnlNdaHkGqdI1FuOTMKuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uMn/6dw4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422910,
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
      "signed_tx": "tx_+MsLAfhCuEB8m/LDSUJX4xE/Voio2bD2BzHLqdZD6p1YC0YDDI/2kuAL21IrCRIkgctE1hFcK2DBMbnlNdaHkGqdI1FuOTMKuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uMn/6dw4=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422909,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAfJvyw0lCV+MRP1aIqNmw9gcxy6nWQ+qdWAtGAwyP9pLgC9tSKwkSJIHLRNYRXCtgwTG55TXWh5BqnSNRbjkzCrhA5q2ycga1yKU7VVXXCKEOI3ibccc1bqAjwGFByqASTxp1f3rruY1MNOuWm0UxPjMn3mHy7sVxMHb9/7t1r+CCBbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jLGcc9C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422909,
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAfJvyw0lCV+MRP1aIqNmw9gcxy6nWQ+qdWAtGAwyP9pLgC9tSKwkSJIHLRNYRXCtgwTG55TXWh5BqnSNRbjkzCrhA5q2ycga1yKU7VVXXCKEOI3ibccc1bqAjwGFByqASTxp1f3rruY1MNOuWm0UxPjMn3mHy7sVxMHb9/7t1r+CCBbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jLGcc9C",
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAfJvyw0lCV+MRP1aIqNmw9gcxy6nWQ+qdWAtGAwyP9pLgC9tSKwkSJIHLRNYRXCtgwTG55TXWh5BqnSNRbjkzCrhA5q2ycga1yKU7VVXXCKEOI3ibccc1bqAjwGFByqASTxp1f3rruY1MNOuWm0UxPjMn3mHy7sVxMHb9/7t1r+CCBbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jLGcc9C",
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAfJvyw0lCV+MRP1aIqNmw9gcxy6nWQ+qdWAtGAwyP9pLgC9tSKwkSJIHLRNYRXCtgwTG55TXWh5BqnSNRbjkzCrhA5q2ycga1yKU7VVXXCKEOI3ibccc1bqAjwGFByqASTxp1f3rruY1MNOuWm0UxPjMn3mHy7sVxMHb9/7t1r+CCBbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jLGcc9C",
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAfJvyw0lCV+MRP1aIqNmw9gcxy6nWQ+qdWAtGAwyP9pLgC9tSKwkSJIHLRNYRXCtgwTG55TXWh5BqnSNRbjkzCrhA5q2ycga1yKU7VVXXCKEOI3ibccc1bqAjwGFByqASTxp1f3rruY1MNOuWm0UxPjMn3mHy7sVxMHb9/7t1r+CCBbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jLGcc9C",
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
    "data": {
      "message": {
        "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
    "data": {
      "message": {
        "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
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
  "id": -576460752303422908,
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
  "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
  "id": -576460752303422908,
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
    "data": {
      "state": "tx_+QENCwH4hLhAfJvyw0lCV+MRP1aIqNmw9gcxy6nWQ+qdWAtGAwyP9pLgC9tSKwkSJIHLRNYRXCtgwTG55TXWh5BqnSNRbjkzCrhA5q2ycga1yKU7VVXXCKEOI3ibccc1bqAjwGFByqASTxp1f3rruY1MNOuWm0UxPjMn3mHy7sVxMHb9/7t1r+CCBbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jLGcc9C"
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
    "data": {
      "state": "tx_+QENCwH4hLhAfJvyw0lCV+MRP1aIqNmw9gcxy6nWQ+qdWAtGAwyP9pLgC9tSKwkSJIHLRNYRXCtgwTG55TXWh5BqnSNRbjkzCrhA5q2ycga1yKU7VVXXCKEOI3ibccc1bqAjwGFByqASTxp1f3rruY1MNOuWm0UxPjMn3mHy7sVxMHb9/7t1r+CCBbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jLGcc9C"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
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
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
    "data": {
      "poi": "pi_+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMDiSa4B"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422907,
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
  "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
  "id": -576460752303422907,
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBh0HOfB6dQkEYe4BsNMtcfTtcXD+9cLIiDood918nrcwAqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B+3f5zg=",
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
  "id": -576460752303422906,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAxkziYni8RdUKZ+2iB3LNrX0Sc46jWauDs49U+gKBOS+XcbnLPAtqtJCOP72Zq8+chOVcyp10kHMjDHKy+uYoOuEj4RjkCoQYdBznwenUJBGHuAbDTLXH07XFw/vXCyIg6KHfdfJ63MAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcuiHWv"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
  "id": -576460752303422906,
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAxkziYni8RdUKZ+2iB3LNrX0Sc46jWauDs49U+gKBOS+XcbnLPAtqtJCOP72Zq8+chOVcyp10kHMjDHKy+uYoOuEj4RjkCoQYdBznwenUJBGHuAbDTLXH07XFw/vXCyIg6KHfdfJ63MAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcuiHWv",
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
  "id": -576460752303422905,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAxkziYni8RdUKZ+2iB3LNrX0Sc46jWauDs49U+gKBOS+XcbnLPAtqtJCOP72Zq8+chOVcyp10kHMjDHKy+uYoOuEBKHWUVRoYFT9Uy4qMfgD7K9ffBlB7cPymOf51kXbCKWmhLsR68O9s0VHSFM7sgolgDgaU3oNSVNp8e5xhSXUsHuEj4RjkCoQYdBznwenUJBGHuAbDTLXH07XFw/vXCyIg6KHfdfJ63MAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfEBQmJ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
  "id": -576460752303422905,
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
    "data": {
      "state": "tx_+NILAfiEuEAxkziYni8RdUKZ+2iB3LNrX0Sc46jWauDs49U+gKBOS+XcbnLPAtqtJCOP72Zq8+chOVcyp10kHMjDHKy+uYoOuEBKHWUVRoYFT9Uy4qMfgD7K9ffBlB7cPymOf51kXbCKWmhLsR68O9s0VHSFM7sgolgDgaU3oNSVNp8e5xhSXUsHuEj4RjkCoQYdBznwenUJBGHuAbDTLXH07XFw/vXCyIg6KHfdfJ63MAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfEBQmJ"
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
    "data": {
      "state": "tx_+NILAfiEuEAxkziYni8RdUKZ+2iB3LNrX0Sc46jWauDs49U+gKBOS+XcbnLPAtqtJCOP72Zq8+chOVcyp10kHMjDHKy+uYoOuEBKHWUVRoYFT9Uy4qMfgD7K9ffBlB7cPymOf51kXbCKWmhLsR68O9s0VHSFM7sgolgDgaU3oNSVNp8e5xhSXUsHuEj4RjkCoQYdBznwenUJBGHuAbDTLXH07XFw/vXCyIg6KHfdfJ63MAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfEBQmJ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422904,
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
  "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
  "id": -576460752303422904,
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
  "id": -576460752303422903,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
  "id": -576460752303422903,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAxkziYni8RdUKZ+2iB3LNrX0Sc46jWauDs49U+gKBOS+XcbnLPAtqtJCOP72Zq8+chOVcyp10kHMjDHKy+uYoOuEBKHWUVRoYFT9Uy4qMfgD7K9ffBlB7cPymOf51kXbCKWmhLsR68O9s0VHSFM7sgolgDgaU3oNSVNp8e5xhSXUsHuEj4RjkCoQYdBznwenUJBGHuAbDTLXH07XFw/vXCyIg6KHfdfJ63MAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfEBQmJ",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAxkziYni8RdUKZ+2iB3LNrX0Sc46jWauDs49U+gKBOS+XcbnLPAtqtJCOP72Zq8+chOVcyp10kHMjDHKy+uYoOuEBKHWUVRoYFT9Uy4qMfgD7K9ffBlB7cPymOf51kXbCKWmhLsR68O9s0VHSFM7sgolgDgaU3oNSVNp8e5xhSXUsHuEj4RjkCoQYdBznwenUJBGHuAbDTLXH07XFw/vXCyIg6KHfdfJ63MAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfEBQmJ",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAxkziYni8RdUKZ+2iB3LNrX0Sc46jWauDs49U+gKBOS+XcbnLPAtqtJCOP72Zq8+chOVcyp10kHMjDHKy+uYoOuEBKHWUVRoYFT9Uy4qMfgD7K9ffBlB7cPymOf51kXbCKWmhLsR68O9s0VHSFM7sgolgDgaU3oNSVNp8e5xhSXUsHuEj4RjkCoQYdBznwenUJBGHuAbDTLXH07XFw/vXCyIg6KHfdfJ63MAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfEBQmJ",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
    "data": {
      "event": "closing"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422902,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {
    "fee": 123456789876543
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
  "id": -576460752303422902,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBh0HOfB6dQkEYe4BsNMtcfTtcXD+9cLIiDood918nrcwoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROELjU+NILAfiEuEAxkziYni8RdUKZ+2iB3LNrX0Sc46jWauDs49U+gKBOS+XcbnLPAtqtJCOP72Zq8+chOVcyp10kHMjDHKy+uYoOuEBKHWUVRoYFT9Uy4qMfgD7K9ffBlB7cPymOf51kXbCKWmhLsR68O9s0VHSFM7sgolgDgaU3oNSVNp8e5xhSXUsHuEj4RjkCoQYdBznwenUJBGHuAbDTLXH07XFw/vXCyIg6KHfdfJ63MAKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAe5AUz5AUk8AfkBP/kBPKBr5sKqJEGy2c6K7OYj3B0QSM9YKqp12Cwu0FcoBE12iPkBGPhPoEqVXL/Gi63p37+99IW1AH7Eb//F/0G9uCVe9zFlBvdG7aAxNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAvh0oGvmwqokQbLZzors5iPcHRBIz1gqqnXYLC7QVygETXaI+FGAgICAgICAgICAgICgbYJjbN6iM9NklD1uSm6sox3iiItBMXXpvq1p2MXyRnGgSpVcv8aLrenfv730hbUAfsRv/8X/Qb24JV73MWUG90aAgID4T6BtgmNs3qIz02SUPW5KbqyjHeKIi0Exdem+rWnYxfJGce2gNbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/7AwMDAwACGcEiGGw8/FD/H3yI=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.slash_sign",
  "params": {
    "signed_tx": "tx_+QLACwH4QrhAQfNIGgkYX9t4068rLO4K3UUjI3m3hLAm2c3FS8OqRjtM+w//bdN1izshTavKAYofu+l9ntW4VtnblA2py09GCrkCd/kCdDcBoQYdBznwenUJBGHuAbDTLXH07XFw/vXCyIg6KHfdfJ63MKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThC41PjSCwH4hLhAMZM4mJ4vEXVCmftogdyza19EnOOo1mrg7OPVPoCgTkvl3G5yzwLarSQjj+9mavPnITlXMqddJBzIwxysvrmKDrhASh1lFUaGBU/VMuKjH4A+yvX3wZQe3D8pjn+dZF2wilpoS7EevDvbNFR0hTO7IKJYA4GlN6DUlTafHucYUl1LB7hI+EY5AqEGHQc58Hp1CQRh7gGw0y1x9O1xcP71wsiIOih33XyetzACoCob2XomoLXVasfWjCsSocPPoSuXDKwFnKboiPTlQXwHuQFM+QFJPAH5AT/5ATyga+bCqiRBstnOiuzmI9wdEEjPWCqqddgsLtBXKARNdoj5ARj4T6BKlVy/xout6d+/vfSFtQB+xG//xf9BvbglXvcxZQb3Ru2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAL4dKBr5sKqJEGy2c6K7OYj3B0QSM9YKqp12Cwu0FcoBE12iPhRgICAgICAgICAgICAoG2CY2zeojPTZJQ9bkpurKMd4oiLQTF16b6tadjF8kZxoEqVXL/Gi63p37+99IW1AH7Eb//F/0G9uCVe9zFlBvdGgICA+E+gbYJjbN6iM9NklD1uSm6sox3iiItBMXXpvq1p2MXyRnHtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl/+wMDAwMAAhnBIhhsPPxSqCyk3"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAQfNIGgkYX9t4068rLO4K3UUjI3m3hLAm2c3FS8OqRjtM+w//bdN1izshTavKAYofu+l9ntW4VtnblA2py09GCrkCd/kCdDcBoQYdBznwenUJBGHuAbDTLXH07XFw/vXCyIg6KHfdfJ63MKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThC41PjSCwH4hLhAMZM4mJ4vEXVCmftogdyza19EnOOo1mrg7OPVPoCgTkvl3G5yzwLarSQjj+9mavPnITlXMqddJBzIwxysvrmKDrhASh1lFUaGBU/VMuKjH4A+yvX3wZQe3D8pjn+dZF2wilpoS7EevDvbNFR0hTO7IKJYA4GlN6DUlTafHucYUl1LB7hI+EY5AqEGHQc58Hp1CQRh7gGw0y1x9O1xcP71wsiIOih33XyetzACoCob2XomoLXVasfWjCsSocPPoSuXDKwFnKboiPTlQXwHuQFM+QFJPAH5AT/5ATyga+bCqiRBstnOiuzmI9wdEEjPWCqqddgsLtBXKARNdoj5ARj4T6BKlVy/xout6d+/vfSFtQB+xG//xf9BvbglXvcxZQb3Ru2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAL4dKBr5sKqJEGy2c6K7OYj3B0QSM9YKqp12Cwu0FcoBE12iPhRgICAgICAgICAgICAoG2CY2zeojPTZJQ9bkpurKMd4oiLQTF16b6tadjF8kZxoEqVXL/Gi63p37+99IW1AH7Eb//F/0G9uCVe9zFlBvdGgICA+E+gbYJjbN6iM9NklD1uSm6sox3iiItBMXXpvq1p2MXyRnHtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl/+wMDAwMAAhnBIhhsPPxSqCyk3",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAQfNIGgkYX9t4068rLO4K3UUjI3m3hLAm2c3FS8OqRjtM+w//bdN1izshTavKAYofu+l9ntW4VtnblA2py09GCrkCd/kCdDcBoQYdBznwenUJBGHuAbDTLXH07XFw/vXCyIg6KHfdfJ63MKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThC41PjSCwH4hLhAMZM4mJ4vEXVCmftogdyza19EnOOo1mrg7OPVPoCgTkvl3G5yzwLarSQjj+9mavPnITlXMqddJBzIwxysvrmKDrhASh1lFUaGBU/VMuKjH4A+yvX3wZQe3D8pjn+dZF2wilpoS7EevDvbNFR0hTO7IKJYA4GlN6DUlTafHucYUl1LB7hI+EY5AqEGHQc58Hp1CQRh7gGw0y1x9O1xcP71wsiIOih33XyetzACoCob2XomoLXVasfWjCsSocPPoSuXDKwFnKboiPTlQXwHuQFM+QFJPAH5AT/5ATyga+bCqiRBstnOiuzmI9wdEEjPWCqqddgsLtBXKARNdoj5ARj4T6BKlVy/xout6d+/vfSFtQB+xG//xf9BvbglXvcxZQb3Ru2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAL4dKBr5sKqJEGy2c6K7OYj3B0QSM9YKqp12Cwu0FcoBE12iPhRgICAgICAgICAgICAoG2CY2zeojPTZJQ9bkpurKMd4oiLQTF16b6tadjF8kZxoEqVXL/Gi63p37+99IW1AH7Eb//F/0G9uCVe9zFlBvdGgICA+E+gbYJjbN6iM9NklD1uSm6sox3iiItBMXXpvq1p2MXyRnHtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl/+wMDAwMAAhnBIhhsPPxSqCyk3",
      "type": "channel_slash_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBh0HOfB6dQkEYe4BsNMtcfTtcXD+9cLIiDood918nrcwoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIY/qiUiX/6GJGE5yoACAIYPXtZ/KAAVc8A7NA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEAsq+og8+nXXOObUfqh/qw+1x6C5ic3bu59T7PNfMEiS5r1nBHbyiPPv/+T62el5R8uHTSyIemB26jEYsc6Jp8BuF/4XTgBoQYdBznwenUJBGHuAbDTLXH07XFw/vXCyIg6KHfdfJ63MKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl/+hiRhOcqAAgCGD17WfygAFd23DvE="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEAsq+og8+nXXOObUfqh/qw+1x6C5ic3bu59T7PNfMEiS5r1nBHbyiPPv/+T62el5R8uHTSyIemB26jEYsc6Jp8BuF/4XTgBoQYdBznwenUJBGHuAbDTLXH07XFw/vXCyIg6KHfdfJ63MKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl/+hiRhOcqAAgCGD17WfygAFd23DvE=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEAsq+og8+nXXOObUfqh/qw+1x6C5ic3bu59T7PNfMEiS5r1nBHbyiPPv/+T62el5R8uHTSyIemB26jEYsc6Jp8BuF/4XTgBoQYdBznwenUJBGHuAbDTLXH07XFw/vXCyIg6KHfdfJ63MKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl/+hiRhOcqAAgCGD17WfygAFd23DvE=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
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
    "channel_id": "ch_DnVFfxuEQBFAF8W91bekmcm1cyjUQUpkvgJhKZwoMqwgdsBuP",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
