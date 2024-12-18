
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&fee=123456789876543&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=initiator
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
      "fsm_id": "ba_FadlL3lrCrIp+mScsNwqG97ALYOevT7Lu0WfyEFY7Ss+PSRe"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&fee=123456789876543&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=responder
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
      "fsm_id": "ba_rRndoxTRGTQRv+zoeNHj/zQ4//QQ3nnA2of7zOR1HC/TJSA6"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhnBIhhsPP8CgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4fkYXU8w==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422992,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECwpJof4Hx0pVvTo2F7UJ6ZsEhuTdmxUjzRqnQCZKM9hAZq4HjfxsSverURgJUrn5oD0laTpqRrBwSPG6L7V90NuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIZwSIYbDz/AoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uHznOyRQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422992,
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
      "signed_tx": "tx_+MsLAfhCuECwpJof4Hx0pVvTo2F7UJ6ZsEhuTdmxUjzRqnQCZKM9hAZq4HjfxsSverURgJUrn5oD0laTpqRrBwSPG6L7V90NuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIZwSIYbDz/AoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uHznOyRQ=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422991,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAntaWOeTaRDpc97+nsiieBiUnetQgAQTfPOgCJH3oFivVVpE4aCV2imOHUuLEP/Qn6Jd2IONZeDeOxQD3GW/GCLhAsKSaH+B8dKVb06Nhe1CembBIbk3ZsVI80ap0AmSjPYQGauB438bEr3q1EYCVK5+aA9JWk6akawcEjxui+1fdDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGcEiGGw8/wKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7h/uT11+"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422991,
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAntaWOeTaRDpc97+nsiieBiUnetQgAQTfPOgCJH3oFivVVpE4aCV2imOHUuLEP/Qn6Jd2IONZeDeOxQD3GW/GCLhAsKSaH+B8dKVb06Nhe1CembBIbk3ZsVI80ap0AmSjPYQGauB438bEr3q1EYCVK5+aA9JWk6akawcEjxui+1fdDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGcEiGGw8/wKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7h/uT11+",
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAntaWOeTaRDpc97+nsiieBiUnetQgAQTfPOgCJH3oFivVVpE4aCV2imOHUuLEP/Qn6Jd2IONZeDeOxQD3GW/GCLhAsKSaH+B8dKVb06Nhe1CembBIbk3ZsVI80ap0AmSjPYQGauB438bEr3q1EYCVK5+aA9JWk6akawcEjxui+1fdDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGcEiGGw8/wKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7h/uT11+",
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAntaWOeTaRDpc97+nsiieBiUnetQgAQTfPOgCJH3oFivVVpE4aCV2imOHUuLEP/Qn6Jd2IONZeDeOxQD3GW/GCLhAsKSaH+B8dKVb06Nhe1CembBIbk3ZsVI80ap0AmSjPYQGauB438bEr3q1EYCVK5+aA9JWk6akawcEjxui+1fdDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGcEiGGw8/wKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7h/uT11+",
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAntaWOeTaRDpc97+nsiieBiUnetQgAQTfPOgCJH3oFivVVpE4aCV2imOHUuLEP/Qn6Jd2IONZeDeOxQD3GW/GCLhAsKSaH+B8dKVb06Nhe1CembBIbk3ZsVI80ap0AmSjPYQGauB438bEr3q1EYCVK5+aA9JWk6akawcEjxui+1fdDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGcEiGGw8/wKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7h/uT11+",
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
    "data": {
      "message": {
        "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
    "data": {
      "message": {
        "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
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
  "id": -576460752303422990,
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
  "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
  "id": -576460752303422990,
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
    "data": {
      "state": "tx_+QENCwH4hLhAntaWOeTaRDpc97+nsiieBiUnetQgAQTfPOgCJH3oFivVVpE4aCV2imOHUuLEP/Qn6Jd2IONZeDeOxQD3GW/GCLhAsKSaH+B8dKVb06Nhe1CembBIbk3ZsVI80ap0AmSjPYQGauB438bEr3q1EYCVK5+aA9JWk6akawcEjxui+1fdDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGcEiGGw8/wKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7h/uT11+"
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
    "data": {
      "state": "tx_+QENCwH4hLhAntaWOeTaRDpc97+nsiieBiUnetQgAQTfPOgCJH3oFivVVpE4aCV2imOHUuLEP/Qn6Jd2IONZeDeOxQD3GW/GCLhAsKSaH+B8dKVb06Nhe1CembBIbk3ZsVI80ap0AmSjPYQGauB438bEr3q1EYCVK5+aA9JWk6akawcEjxui+1fdDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGcEiGGw8/wKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7h/uT11+"
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBiq1I623qXZGZxBvtdFufnMSGw5K6qzeZmD0OHeQaQdzoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY2kdavv/+GG0jrV+ABAIYSMJzlQAAgKwgAmw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422989,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEC+OVX9Nuh7ey/tpeyhYtklZJptoIhVtZcb6u99QrFBUNdOyUYIYa+3chLoSDKWKC2ow1+cfbTnrTcQAtdug7MFuF/4XTUBoQYqtSOtt6l2RmcQb7XRbn5zEhsOSuqs3mZg9Dh3kGkHc6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7//hhtI61fgAQCGEjCc5UAAIFlp460="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
  "id": -576460752303422989,
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEC+OVX9Nuh7ey/tpeyhYtklZJptoIhVtZcb6u99QrFBUNdOyUYIYa+3chLoSDKWKC2ow1+cfbTnrTcQAtdug7MFuF/4XTUBoQYqtSOtt6l2RmcQb7XRbn5zEhsOSuqs3mZg9Dh3kGkHc6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7//hhtI61fgAQCGEjCc5UAAIFlp460=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422988,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuECDa+If0UBOXS0e0ikBKXJS2eacYDaYF/RxkWX0XDaAX7utlM0YBBq00/JQZBP3UfPNkKFOtnW3aBppk2vvn7sPuEC+OVX9Nuh7ey/tpeyhYtklZJptoIhVtZcb6u99QrFBUNdOyUYIYa+3chLoSDKWKC2ow1+cfbTnrTcQAtdug7MFuF/4XTUBoQYqtSOtt6l2RmcQb7XRbn5zEhsOSuqs3mZg9Dh3kGkHc6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7//hhtI61fgAQCGEjCc5UAAIOYzu2g="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
  "id": -576460752303422988,
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuECDa+If0UBOXS0e0ikBKXJS2eacYDaYF/RxkWX0XDaAX7utlM0YBBq00/JQZBP3UfPNkKFOtnW3aBppk2vvn7sPuEC+OVX9Nuh7ey/tpeyhYtklZJptoIhVtZcb6u99QrFBUNdOyUYIYa+3chLoSDKWKC2ow1+cfbTnrTcQAtdug7MFuF/4XTUBoQYqtSOtt6l2RmcQb7XRbn5zEhsOSuqs3mZg9Dh3kGkHc6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7//hhtI61fgAQCGEjCc5UAAIOYzu2g=",
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuECDa+If0UBOXS0e0ikBKXJS2eacYDaYF/RxkWX0XDaAX7utlM0YBBq00/JQZBP3UfPNkKFOtnW3aBppk2vvn7sPuEC+OVX9Nuh7ey/tpeyhYtklZJptoIhVtZcb6u99QrFBUNdOyUYIYa+3chLoSDKWKC2ow1+cfbTnrTcQAtdug7MFuF/4XTUBoQYqtSOtt6l2RmcQb7XRbn5zEhsOSuqs3mZg9Dh3kGkHc6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7//hhtI61fgAQCGEjCc5UAAIOYzu2g=",
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuECDa+If0UBOXS0e0ikBKXJS2eacYDaYF/RxkWX0XDaAX7utlM0YBBq00/JQZBP3UfPNkKFOtnW3aBppk2vvn7sPuEC+OVX9Nuh7ey/tpeyhYtklZJptoIhVtZcb6u99QrFBUNdOyUYIYa+3chLoSDKWKC2ow1+cfbTnrTcQAtdug7MFuF/4XTUBoQYqtSOtt6l2RmcQb7XRbn5zEhsOSuqs3mZg9Dh3kGkHc6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7//hhtI61fgAQCGEjCc5UAAIOYzu2g=",
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuECDa+If0UBOXS0e0ikBKXJS2eacYDaYF/RxkWX0XDaAX7utlM0YBBq00/JQZBP3UfPNkKFOtnW3aBppk2vvn7sPuEC+OVX9Nuh7ey/tpeyhYtklZJptoIhVtZcb6u99QrFBUNdOyUYIYa+3chLoSDKWKC2ow1+cfbTnrTcQAtdug7MFuF/4XTUBoQYqtSOtt6l2RmcQb7XRbn5zEhsOSuqs3mZg9Dh3kGkHc6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7//hhtI61fgAQCGEjCc5UAAIOYzu2g=",
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
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
    "channel_id": "ch_KoueWHrBN2oCNPhKKwYSdhCHjJMfSDzW616ZUxw9sAqWkEGZ8",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator closes WebSocket connection
