
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
      "fsm_id": "ba_AvmErvZuW+fcfP9UcwlR9CmJT1Hmkz5gZZz9eMXLv480tHfF"
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
      "fsm_id": "ba_NEcmuc+E1wkMPxKmT9Qr/HU7gaad0dvSh723PMIzS+JBvqz8"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5ElalMng==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422752,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECEU+iwem0J9K19wI/1LJP8M1gdjhfsoAUBZeM19noCR1p9Wgw1LD5194GFluoRKXVMCEgeFGiwcdVUI0IiwLYLuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uRGeaSkA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422752,
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
      "signed_tx": "tx_+MsLAfhCuECEU+iwem0J9K19wI/1LJP8M1gdjhfsoAUBZeM19noCR1p9Wgw1LD5194GFluoRKXVMCEgeFGiwcdVUI0IiwLYLuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uRGeaSkA=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422751,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAfbY+vWGqMKL/KKl6sfs/wNtCwBeUlYZ92QQfH/D6BTNDkhVeKg+/p1TUOeMIc88pz4FqFJu191N/ihNDl1dFCLhAhFPosHptCfStfcCP9SyT/DNYHY4X7KAFAWXjNfZ6AkdafVoMNSw+dfeBhZbqESl1TAhIHhRosHHVVCNCIsC2C7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kSeuTv6"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422751,
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
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAfbY+vWGqMKL/KKl6sfs/wNtCwBeUlYZ92QQfH/D6BTNDkhVeKg+/p1TUOeMIc88pz4FqFJu191N/ihNDl1dFCLhAhFPosHptCfStfcCP9SyT/DNYHY4X7KAFAWXjNfZ6AkdafVoMNSw+dfeBhZbqESl1TAhIHhRosHHVVCNCIsC2C7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kSeuTv6",
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
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAfbY+vWGqMKL/KKl6sfs/wNtCwBeUlYZ92QQfH/D6BTNDkhVeKg+/p1TUOeMIc88pz4FqFJu191N/ihNDl1dFCLhAhFPosHptCfStfcCP9SyT/DNYHY4X7KAFAWXjNfZ6AkdafVoMNSw+dfeBhZbqESl1TAhIHhRosHHVVCNCIsC2C7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kSeuTv6",
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
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAfbY+vWGqMKL/KKl6sfs/wNtCwBeUlYZ92QQfH/D6BTNDkhVeKg+/p1TUOeMIc88pz4FqFJu191N/ihNDl1dFCLhAhFPosHptCfStfcCP9SyT/DNYHY4X7KAFAWXjNfZ6AkdafVoMNSw+dfeBhZbqESl1TAhIHhRosHHVVCNCIsC2C7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kSeuTv6",
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
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAfbY+vWGqMKL/KKl6sfs/wNtCwBeUlYZ92QQfH/D6BTNDkhVeKg+/p1TUOeMIc88pz4FqFJu191N/ihNDl1dFCLhAhFPosHptCfStfcCP9SyT/DNYHY4X7KAFAWXjNfZ6AkdafVoMNSw+dfeBhZbqESl1TAhIHhRosHHVVCNCIsC2C7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kSeuTv6",
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
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
    "data": {
      "message": {
        "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
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
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
    "data": {
      "message": {
        "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
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
  "id": -576460752303422750,
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
  "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
  "id": -576460752303422750,
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
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
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
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
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
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
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
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
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
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
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
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
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
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
    "data": {
      "state": "tx_+QENCwH4hLhAfbY+vWGqMKL/KKl6sfs/wNtCwBeUlYZ92QQfH/D6BTNDkhVeKg+/p1TUOeMIc88pz4FqFJu191N/ihNDl1dFCLhAhFPosHptCfStfcCP9SyT/DNYHY4X7KAFAWXjNfZ6AkdafVoMNSw+dfeBhZbqESl1TAhIHhRosHHVVCNCIsC2C7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kSeuTv6"
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
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
    "data": {
      "state": "tx_+QENCwH4hLhAfbY+vWGqMKL/KKl6sfs/wNtCwBeUlYZ92QQfH/D6BTNDkhVeKg+/p1TUOeMIc88pz4FqFJu191N/ihNDl1dFCLhAhFPosHptCfStfcCP9SyT/DNYHY4X7KAFAWXjNfZ6AkdafVoMNSw+dfeBhZbqESl1TAhIHhRosHHVVCNCIsC2C7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kSeuTv6"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBucmni3fPLan5ISFXtO0BQHGUeHyVMTWdHqbZs2y0UNzoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IC5AUz5AUk8AfkBP/kBPKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvkBGPh0oCbziXyYo8Ox+VZtROqlQQtKKd21jKCiqh29ftJZTs5e+FGAgICAgICAgICAgICg7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqug5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqeAgID4T6DlslFZIexXT120YXqqt3xFqwcxbt0Suq1WIBNf47yap+2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAH4T6Dt/5Hiy5W70qsqTzdexfFGw0mN5gAjP38MM0HGdpS2q+2gNbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX//AwMDAwACGFT7sgIAARcG7J58=",
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
  "method": "channels.close_solo_sign",
  "params": {
    "signed_tx": "tx_+QHrCwH4QrhA7aQs0r6ZmIsVyXEOpV/f3IOpsRQmU6JkaMSZq19Vg8iR8TZ3SguutZpQ7B27CF0NKsHNRtSMBeYifKkEm2ogDLkBovkBnzYBoQbnJp4t3zy2p+SEhV7TtAUBxlHh8lTE1nR6m2bNstFDc6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SAuQFM+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMAAhhU+7ICAAEVH9RA4"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhA7aQs0r6ZmIsVyXEOpV/f3IOpsRQmU6JkaMSZq19Vg8iR8TZ3SguutZpQ7B27CF0NKsHNRtSMBeYifKkEm2ogDLkBovkBnzYBoQbnJp4t3zy2p+SEhV7TtAUBxlHh8lTE1nR6m2bNstFDc6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SAuQFM+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMAAhhU+7ICAAEVH9RA4",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
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
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhA7aQs0r6ZmIsVyXEOpV/f3IOpsRQmU6JkaMSZq19Vg8iR8TZ3SguutZpQ7B27CF0NKsHNRtSMBeYifKkEm2ogDLkBovkBnzYBoQbnJp4t3zy2p+SEhV7TtAUBxlHh8lTE1nR6m2bNstFDc6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SAuQFM+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMAAhhU+7ICAAEVH9RA4",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
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
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBucmni3fPLan5ISFXtO0BQHGUeHyVMTWdHqbZs2y0UNzoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiX/+GJGE5yoABAIYPXtZ/KABGoSlmpg==",
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
  "method": "channels.settle_sign",
  "params": {
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
    "data": {
      "event": "aborted_update"
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

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
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
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBucmni3fPLan5ISFXtO0BQHGUeHyVMTWdHqbZs2y0UNzoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIY/qiUiX/+GJGE5yoABAIYPXtZ/KAAZQXRfdg==",
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
    "error": 42
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422749,
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
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
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
  "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
  "id": -576460752303422749,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422748,
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
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
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
    "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
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
  "channel_id": "ch_2koSRHkKo4hVUUtF5XVfutXZEhyZbDzQiKWCiMnEZpVeki8jqA",
  "id": -576460752303422748,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
