
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
      "fsm_id": "ba_NBjSF7CtZ9TdJVQzlBUwFPx59JkJ4f+isd3ioFTjhmI6D2rh"
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
      "fsm_id": "ba_zoD9Nxcxdz7l1cW8zt6PJHcoAQVXM01pSzluNsDFS0uVIhHn"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4nA0Ep7w==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422969,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECNPGM3xtyQ8dEtiRWyjAVoqfpprzV7819nhODYWlEqYOuqe8nGvjTaEY5NARfXlSP+aLuF2x72krJJinL4qJ8CuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uJ5frARM="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422969,
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
      "signed_tx": "tx_+MsLAfhCuECNPGM3xtyQ8dEtiRWyjAVoqfpprzV7819nhODYWlEqYOuqe8nGvjTaEY5NARfXlSP+aLuF2x72krJJinL4qJ8CuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uJ5frARM=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422968,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAjTxjN8bckPHRLYkVsowFaKn6aa81e/NfZ4Tg2FpRKmDrqnvJxr402hGOTQEX15Uj/mi7hdse9pKySYpy+KifArhA01M8SMjjA7NhCkfQK5KrUx9VpEYrThLS1unSFiGRtGfdpUOcZMO3YtOtj5Eea8GJKGgO/8HfIBzhP3BUnnusDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7ifiItl/"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422968,
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAjTxjN8bckPHRLYkVsowFaKn6aa81e/NfZ4Tg2FpRKmDrqnvJxr402hGOTQEX15Uj/mi7hdse9pKySYpy+KifArhA01M8SMjjA7NhCkfQK5KrUx9VpEYrThLS1unSFiGRtGfdpUOcZMO3YtOtj5Eea8GJKGgO/8HfIBzhP3BUnnusDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7ifiItl/",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAjTxjN8bckPHRLYkVsowFaKn6aa81e/NfZ4Tg2FpRKmDrqnvJxr402hGOTQEX15Uj/mi7hdse9pKySYpy+KifArhA01M8SMjjA7NhCkfQK5KrUx9VpEYrThLS1unSFiGRtGfdpUOcZMO3YtOtj5Eea8GJKGgO/8HfIBzhP3BUnnusDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7ifiItl/",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAjTxjN8bckPHRLYkVsowFaKn6aa81e/NfZ4Tg2FpRKmDrqnvJxr402hGOTQEX15Uj/mi7hdse9pKySYpy+KifArhA01M8SMjjA7NhCkfQK5KrUx9VpEYrThLS1unSFiGRtGfdpUOcZMO3YtOtj5Eea8GJKGgO/8HfIBzhP3BUnnusDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7ifiItl/",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAjTxjN8bckPHRLYkVsowFaKn6aa81e/NfZ4Tg2FpRKmDrqnvJxr402hGOTQEX15Uj/mi7hdse9pKySYpy+KifArhA01M8SMjjA7NhCkfQK5KrUx9VpEYrThLS1unSFiGRtGfdpUOcZMO3YtOtj5Eea8GJKGgO/8HfIBzhP3BUnnusDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7ifiItl/",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "message": {
        "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "message": {
        "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
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
  "id": -576460752303422967,
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
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422967,
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "state": "tx_+QENCwH4hLhAjTxjN8bckPHRLYkVsowFaKn6aa81e/NfZ4Tg2FpRKmDrqnvJxr402hGOTQEX15Uj/mi7hdse9pKySYpy+KifArhA01M8SMjjA7NhCkfQK5KrUx9VpEYrThLS1unSFiGRtGfdpUOcZMO3YtOtj5Eea8GJKGgO/8HfIBzhP3BUnnusDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7ifiItl/"
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "state": "tx_+QENCwH4hLhAjTxjN8bckPHRLYkVsowFaKn6aa81e/NfZ4Tg2FpRKmDrqnvJxr402hGOTQEX15Uj/mi7hdse9pKySYpy+KifArhA01M8SMjjA7NhCkfQK5KrUx9VpEYrThLS1unSFiGRtGfdpUOcZMO3YtOtj5Eea8GJKGgO/8HfIBzhP3BUnnusDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7ifiItl/"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422966,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422966,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QENCwH4hLhAjTxjN8bckPHRLYkVsowFaKn6aa81e/NfZ4Tg2FpRKmDrqnvJxr402hGOTQEX15Uj/mi7hdse9pKySYpy+KifArhA01M8SMjjA7NhCkfQK5KrUx9VpEYrThLS1unSFiGRtGfdpUOcZMO3YtOtj5Eea8GJKGgO/8HfIBzhP3BUnnusDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7ifiItl/",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422965,
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
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422965,
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmeRMK3OVlEKAIRGilHAApomqBnZvgNV2ehdyhfhmFXaAqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B7se7+I=",
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
  "id": -576460752303422964,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA9VIoNg2zPpRqMJQMLE4Ijq9xQMPzYJpBFUq8NrpegbNXvf3GP1sPI7vv3M72hVNdvNOJ3RP5cTFPx1AUQSTsJuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAe7fWWp"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422964,
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA9VIoNg2zPpRqMJQMLE4Ijq9xQMPzYJpBFUq8NrpegbNXvf3GP1sPI7vv3M72hVNdvNOJ3RP5cTFPx1AUQSTsJuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAe7fWWp",
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
  "id": -576460752303422963,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA9VIoNg2zPpRqMJQMLE4Ijq9xQMPzYJpBFUq8NrpegbNXvf3GP1sPI7vv3M72hVNdvNOJ3RP5cTFPx1AUQSTsJuEC8SqRYc8+cKhj8Pg166S12c+TxWow582HqlAuRF8hefMctPIvgcM/Aus8MgbDica5zYddo+qZc39ui2kvLOpMHuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeD+vV3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422963,
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "state": "tx_+NILAfiEuEA9VIoNg2zPpRqMJQMLE4Ijq9xQMPzYJpBFUq8NrpegbNXvf3GP1sPI7vv3M72hVNdvNOJ3RP5cTFPx1AUQSTsJuEC8SqRYc8+cKhj8Pg166S12c+TxWow582HqlAuRF8hefMctPIvgcM/Aus8MgbDica5zYddo+qZc39ui2kvLOpMHuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeD+vV3"
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "state": "tx_+NILAfiEuEA9VIoNg2zPpRqMJQMLE4Ijq9xQMPzYJpBFUq8NrpegbNXvf3GP1sPI7vv3M72hVNdvNOJ3RP5cTFPx1AUQSTsJuEC8SqRYc8+cKhj8Pg166S12c+TxWow582HqlAuRF8hefMctPIvgcM/Aus8MgbDica5zYddo+qZc39ui2kvLOpMHuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeD+vV3"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422962,
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
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422962,
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
  "id": -576460752303422961,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422961,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA9VIoNg2zPpRqMJQMLE4Ijq9xQMPzYJpBFUq8NrpegbNXvf3GP1sPI7vv3M72hVNdvNOJ3RP5cTFPx1AUQSTsJuEC8SqRYc8+cKhj8Pg166S12c+TxWow582HqlAuRF8hefMctPIvgcM/Aus8MgbDica5zYddo+qZc39ui2kvLOpMHuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeD+vV3",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422960,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {
    "fee": 123456789876543
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422960,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBmeRMK3OVlEKAIRGilHAApomqBnZvgNV2ehdyhfhmFXaoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79LjU+NILAfiEuEA9VIoNg2zPpRqMJQMLE4Ijq9xQMPzYJpBFUq8NrpegbNXvf3GP1sPI7vv3M72hVNdvNOJ3RP5cTFPx1AUQSTsJuEC8SqRYc8+cKhj8Pg166S12c+TxWow582HqlAuRF8hefMctPIvgcM/Aus8MgbDica5zYddo+qZc39ui2kvLOpMHuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcAhnBIhhsPPyj3aRpy",
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
  "method": "channels.snapshot_solo_sign",
  "params": {
    "signed_tx": "tx_+QFxCwH4QrhAHLhZgzZwMz+6izLbLOzeIKFw4hQ+PBT9+Vi3Snh8RJo2/A/YX1vICxdNpjRvFUP9x5toGF6PytzxFbh44O3+BrkBKPkBJTsBoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/S41PjSCwH4hLhAPVSKDYNsz6UajCUDCxOCI6vcUDD82CaQRVKvDa6XoGzV739xj9bDyO779zO9oVTXbzTid0T+XExT8dQFEEk7CbhAvEqkWHPPnCoY/D4NeuktdnPk8VqMOfNh6pQLkRfIXnzHLTyL4HDPwLrPDIGw4nGuc2HXaPqmXN/botpLyzqTB7hI+EY5AqEGZ5Ewrc5WUQoAhEaKUcACmiaoGdm+A1XZ6F3KF+GYVdoCoCob2XomoLXVasfWjCsSocPPoSuXDKwFnKboiPTlQXwHAIZwSIYbDz8oKIsqhQ=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422959,
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
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422959,
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmeRMK3OVlEKAIRGilHAApomqBnZvgNV2ehdyhfhmFXaA6BAspkUHVc+kYM7Vvj4WOMGppoVtE+bix63giuF7Bmg1++/F7I=",
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
  "id": -576460752303422958,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBnWVfvQY5ZC9Ud4JKmyl2DgcQVc7Cr1P5uClB4FlQOxb5feDqx8FWHyEGef5BHHo+0r+Ui0PNLH56ClDG4v68EuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gOgQLKZFB1XPpGDO1b4+FjjBqaaFbRPm4set4IrhewZoNd04WtK"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422958,
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBnWVfvQY5ZC9Ud4JKmyl2DgcQVc7Cr1P5uClB4FlQOxb5feDqx8FWHyEGef5BHHo+0r+Ui0PNLH56ClDG4v68EuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gOgQLKZFB1XPpGDO1b4+FjjBqaaFbRPm4set4IrhewZoNd04WtK",
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
  "id": -576460752303422957,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEABlMJrticXQ5BSTQnlqttDR4gMbMKSPqxapZPajBWk6iSKWRKP9NVm2qm3jaqBMLM1SxKLUobkreoK5rpAOtkKuEBnWVfvQY5ZC9Ud4JKmyl2DgcQVc7Cr1P5uClB4FlQOxb5feDqx8FWHyEGef5BHHo+0r+Ui0PNLH56ClDG4v68EuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gOgQLKZFB1XPpGDO1b4+FjjBqaaFbRPm4set4IrhewZoNf1IeOU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422957,
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "state": "tx_+NILAfiEuEABlMJrticXQ5BSTQnlqttDR4gMbMKSPqxapZPajBWk6iSKWRKP9NVm2qm3jaqBMLM1SxKLUobkreoK5rpAOtkKuEBnWVfvQY5ZC9Ud4JKmyl2DgcQVc7Cr1P5uClB4FlQOxb5feDqx8FWHyEGef5BHHo+0r+Ui0PNLH56ClDG4v68EuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gOgQLKZFB1XPpGDO1b4+FjjBqaaFbRPm4set4IrhewZoNf1IeOU"
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "state": "tx_+NILAfiEuEABlMJrticXQ5BSTQnlqttDR4gMbMKSPqxapZPajBWk6iSKWRKP9NVm2qm3jaqBMLM1SxKLUobkreoK5rpAOtkKuEBnWVfvQY5ZC9Ud4JKmyl2DgcQVc7Cr1P5uClB4FlQOxb5feDqx8FWHyEGef5BHHo+0r+Ui0PNLH56ClDG4v68EuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gOgQLKZFB1XPpGDO1b4+FjjBqaaFbRPm4set4IrhewZoNf1IeOU"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422956,
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
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422956,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999997
    },
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000003
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422955,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422955,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEABlMJrticXQ5BSTQnlqttDR4gMbMKSPqxapZPajBWk6iSKWRKP9NVm2qm3jaqBMLM1SxKLUobkreoK5rpAOtkKuEBnWVfvQY5ZC9Ud4JKmyl2DgcQVc7Cr1P5uClB4FlQOxb5feDqx8FWHyEGef5BHHo+0r+Ui0PNLH56ClDG4v68EuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gOgQLKZFB1XPpGDO1b4+FjjBqaaFbRPm4set4IrhewZoNf1IeOU",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAA7DvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/3+vQVj"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422954,
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
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422954,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000003
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999997
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmeRMK3OVlEKAIRGilHAApomqBnZvgNV2ehdyhfhmFXaBKAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B82UAZY=",
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
  "id": -576460752303422953,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECEugMLfIfHXSioFA3Nd4fUi/67hOWShoLmJBVe7LrvASa7JaQub2q3ED7RiSftuYnPyoVKLhX6ymDrNryfSD4BuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAdOpOBJ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422953,
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "signed_tx": "tx_+JALAfhCuECEugMLfIfHXSioFA3Nd4fUi/67hOWShoLmJBVe7LrvASa7JaQub2q3ED7RiSftuYnPyoVKLhX6ymDrNryfSD4BuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAdOpOBJ",
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
  "id": -576460752303422952,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECEugMLfIfHXSioFA3Nd4fUi/67hOWShoLmJBVe7LrvASa7JaQub2q3ED7RiSftuYnPyoVKLhX6ymDrNryfSD4BuEDfCJiAUVV2JarCiK82ZcU8emwQf3qiNzSR5RLlBipjVENij120P++h4AAP7KHBvi3k3fca/z65fgkzpYTczcsJuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAejy87O"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422952,
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "state": "tx_+NILAfiEuECEugMLfIfHXSioFA3Nd4fUi/67hOWShoLmJBVe7LrvASa7JaQub2q3ED7RiSftuYnPyoVKLhX6ymDrNryfSD4BuEDfCJiAUVV2JarCiK82ZcU8emwQf3qiNzSR5RLlBipjVENij120P++h4AAP7KHBvi3k3fca/z65fgkzpYTczcsJuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAejy87O"
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "state": "tx_+NILAfiEuECEugMLfIfHXSioFA3Nd4fUi/67hOWShoLmJBVe7LrvASa7JaQub2q3ED7RiSftuYnPyoVKLhX6ymDrNryfSD4BuEDfCJiAUVV2JarCiK82ZcU8emwQf3qiNzSR5RLlBipjVENij120P++h4AAP7KHBvi3k3fca/z65fgkzpYTczcsJuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAejy87O"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422951,
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
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422951,
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

#### initiator ---> node
```javascript
{
  "id": -576460752303422950,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422950,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECEugMLfIfHXSioFA3Nd4fUi/67hOWShoLmJBVe7LrvASa7JaQub2q3ED7RiSftuYnPyoVKLhX6ymDrNryfSD4BuEDfCJiAUVV2JarCiK82ZcU8emwQf3qiNzSR5RLlBipjVENij120P++h4AAP7KHBvi3k3fca/z65fgkzpYTczcsJuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAejy87O",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAHLhZgzZwMz+6izLbLOzeIKFw4hQ+PBT9+Vi3Snh8RJo2/A/YX1vICxdNpjRvFUP9x5toGF6PytzxFbh44O3+BrkBKPkBJTsBoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/S41PjSCwH4hLhAPVSKDYNsz6UajCUDCxOCI6vcUDD82CaQRVKvDa6XoGzV739xj9bDyO779zO9oVTXbzTid0T+XExT8dQFEEk7CbhAvEqkWHPPnCoY/D4NeuktdnPk8VqMOfNh6pQLkRfIXnzHLTyL4HDPwLrPDIGw4nGuc2HXaPqmXN/botpLyzqTB7hI+EY5AqEGZ5Ewrc5WUQoAhEaKUcACmiaoGdm+A1XZ6F3KF+GYVdoCoCob2XomoLXVasfWjCsSocPPoSuXDKwFnKboiPTlQXwHAIZwSIYbDz8oKIsqhQ==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAHLhZgzZwMz+6izLbLOzeIKFw4hQ+PBT9+Vi3Snh8RJo2/A/YX1vICxdNpjRvFUP9x5toGF6PytzxFbh44O3+BrkBKPkBJTsBoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/S41PjSCwH4hLhAPVSKDYNsz6UajCUDCxOCI6vcUDD82CaQRVKvDa6XoGzV739xj9bDyO779zO9oVTXbzTid0T+XExT8dQFEEk7CbhAvEqkWHPPnCoY/D4NeuktdnPk8VqMOfNh6pQLkRfIXnzHLTyL4HDPwLrPDIGw4nGuc2HXaPqmXN/botpLyzqTB7hI+EY5AqEGZ5Ewrc5WUQoAhEaKUcACmiaoGdm+A1XZ6F3KF+GYVdoCoCob2XomoLXVasfWjCsSocPPoSuXDKwFnKboiPTlQXwHAIZwSIYbDz8oKIsqhQ==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "(�i�J�\u0011�')�x�[s�7�y\u0014\u0002�5�\u0012�A�M��",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422949,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422949,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECEugMLfIfHXSioFA3Nd4fUi/67hOWShoLmJBVe7LrvASa7JaQub2q3ED7RiSftuYnPyoVKLhX6ymDrNryfSD4BuEDfCJiAUVV2JarCiK82ZcU8emwQf3qiNzSR5RLlBipjVENij120P++h4AAP7KHBvi3k3fca/z65fgkzpYTczcsJuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAejy87O",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422948,
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
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422948,
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmeRMK3OVlEKAIRGilHAApomqBnZvgNV2ehdyhfhmFXaBaAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7i03Vqc=",
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
  "id": -576460752303422947,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC5RAmyNBRLa6wOEr1AeTshcBp+xP8aEtHMJRIa1kHcZ8TR053QU1retwZL6JACTnvYfNsp7tiUIMeSYST5ztEHuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6+N8xX"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422947,
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC5RAmyNBRLa6wOEr1AeTshcBp+xP8aEtHMJRIa1kHcZ8TR053QU1retwZL6JACTnvYfNsp7tiUIMeSYST5ztEHuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6+N8xX",
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
  "id": -576460752303422946,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBamM7DP1RkyCa89gneIIhqrCoufSRCnqZOwvYFWdx/Ri/oXS5W9RmubSJbkHKFchgEBMd5OVd6vemPOOoopM8IuEC5RAmyNBRLa6wOEr1AeTshcBp+xP8aEtHMJRIa1kHcZ8TR053QU1retwZL6JACTnvYfNsp7tiUIMeSYST5ztEHuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+68/HL5"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422946,
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "state": "tx_+NILAfiEuEBamM7DP1RkyCa89gneIIhqrCoufSRCnqZOwvYFWdx/Ri/oXS5W9RmubSJbkHKFchgEBMd5OVd6vemPOOoopM8IuEC5RAmyNBRLa6wOEr1AeTshcBp+xP8aEtHMJRIa1kHcZ8TR053QU1retwZL6JACTnvYfNsp7tiUIMeSYST5ztEHuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+68/HL5"
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "state": "tx_+NILAfiEuEBamM7DP1RkyCa89gneIIhqrCoufSRCnqZOwvYFWdx/Ri/oXS5W9RmubSJbkHKFchgEBMd5OVd6vemPOOoopM8IuEC5RAmyNBRLa6wOEr1AeTshcBp+xP8aEtHMJRIa1kHcZ8TR053QU1retwZL6JACTnvYfNsp7tiUIMeSYST5ztEHuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+68/HL5"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422945,
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
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422945,
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
  "id": -576460752303422944,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422944,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBamM7DP1RkyCa89gneIIhqrCoufSRCnqZOwvYFWdx/Ri/oXS5W9RmubSJbkHKFchgEBMd5OVd6vemPOOoopM8IuEC5RAmyNBRLa6wOEr1AeTshcBp+xP8aEtHMJRIa1kHcZ8TR053QU1retwZL6JACTnvYfNsp7tiUIMeSYST5ztEHuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+68/HL5",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422943,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {
    "fee": 123456789876543
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422943,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBmeRMK3OVlEKAIRGilHAApomqBnZvgNV2ehdyhfhmFXaoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROELjU+NILAfiEuEBamM7DP1RkyCa89gneIIhqrCoufSRCnqZOwvYFWdx/Ri/oXS5W9RmubSJbkHKFchgEBMd5OVd6vemPOOoopM8IuEC5RAmyNBRLa6wOEr1AeTshcBp+xP8aEtHMJRIa1kHcZ8TR053QU1retwZL6JACTnvYfNsp7tiUIMeSYST5ztEHuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4AhnBIhhsPPw+PPpDb",
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
  "method": "channels.snapshot_solo_sign",
  "params": {
    "signed_tx": "tx_+QFxCwH4QrhAERFOXTCgI9pkvU5p4IAgVSzTI1x3zE3BeaTKC+RgWmWrQWXUZolfKB6/weG1AtK/tPFFzwEbYgwF4rJlkvIYBLkBKPkBJTsBoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2qEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThC41PjSCwH4hLhAWpjOwz9UZMgmvPYJ3iCIaqwqLn0kQp6mTsL2BVncf0Yv6F0uVvUZrm0iW5ByhXIYBATHeTlXer3pjzjqKKTPCLhAuUQJsjQUS2usDhK9QHk7IXAafsT/GhLRzCUSGtZB3GfE0dOd0FNa3rcGS+iQAk572HzbKe7YlCDHkmEk+c7RB7hI+EY5AqEGZ5Ewrc5WUQoAhEaKUcACmiaoGdm+A1XZ6F3KF+GYVdoFoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uAIZwSIYbDz8PxITSNA=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422942,
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
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422942,
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmeRMK3OVlEKAIRGilHAApomqBnZvgNV2ehdyhfhmFXaBqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B3v57oc=",
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
  "id": -576460752303422941,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDL2TdSzSnmlitnJPf3WCPlvje5Mc67XH7bAwZCbzHFjp0CNagRkPqR4lZyYI3S6e+X4QubMV1t21yKLdHsTHoKuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gagKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeSQH/X"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422941,
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDL2TdSzSnmlitnJPf3WCPlvje5Mc67XH7bAwZCbzHFjp0CNagRkPqR4lZyYI3S6e+X4QubMV1t21yKLdHsTHoKuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gagKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeSQH/X",
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
  "id": -576460752303422940,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECszgrQ8cmkCadepgPjg8ziCAWtbxm+qBm3N8UH8b/Y8ZfUVVsAMjswXY07VXZVwqFBMHQGjeh59gBW+3Eq0AgEuEDL2TdSzSnmlitnJPf3WCPlvje5Mc67XH7bAwZCbzHFjp0CNagRkPqR4lZyYI3S6e+X4QubMV1t21yKLdHsTHoKuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gagKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfjVtaZ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422940,
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "state": "tx_+NILAfiEuECszgrQ8cmkCadepgPjg8ziCAWtbxm+qBm3N8UH8b/Y8ZfUVVsAMjswXY07VXZVwqFBMHQGjeh59gBW+3Eq0AgEuEDL2TdSzSnmlitnJPf3WCPlvje5Mc67XH7bAwZCbzHFjp0CNagRkPqR4lZyYI3S6e+X4QubMV1t21yKLdHsTHoKuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gagKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfjVtaZ"
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "state": "tx_+NILAfiEuECszgrQ8cmkCadepgPjg8ziCAWtbxm+qBm3N8UH8b/Y8ZfUVVsAMjswXY07VXZVwqFBMHQGjeh59gBW+3Eq0AgEuEDL2TdSzSnmlitnJPf3WCPlvje5Mc67XH7bAwZCbzHFjp0CNagRkPqR4lZyYI3S6e+X4QubMV1t21yKLdHsTHoKuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gagKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfjVtaZ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422939,
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
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422939,
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
  "id": -576460752303422938,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422938,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECszgrQ8cmkCadepgPjg8ziCAWtbxm+qBm3N8UH8b/Y8ZfUVVsAMjswXY07VXZVwqFBMHQGjeh59gBW+3Eq0AgEuEDL2TdSzSnmlitnJPf3WCPlvje5Mc67XH7bAwZCbzHFjp0CNagRkPqR4lZyYI3S6e+X4QubMV1t21yKLdHsTHoKuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gagKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfjVtaZ",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422937,
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
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422937,
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmeRMK3OVlEKAIRGilHAApomqBnZvgNV2ehdyhfhmFXaB6AWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7i6tZEw=",
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
  "id": -576460752303422936,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB+On0tnZaBWUBLaTgkJwjEIM/YeckVLrvlCQ5Cg65crEhu2Vyk8DaWZuc0OFlUtYyHDJe3tMRmWbdeXuYn6igBuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gegFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7APP1L"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422936,
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB+On0tnZaBWUBLaTgkJwjEIM/YeckVLrvlCQ5Cg65crEhu2Vyk8DaWZuc0OFlUtYyHDJe3tMRmWbdeXuYn6igBuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gegFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7APP1L",
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
  "id": -576460752303422935,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEB+On0tnZaBWUBLaTgkJwjEIM/YeckVLrvlCQ5Cg65crEhu2Vyk8DaWZuc0OFlUtYyHDJe3tMRmWbdeXuYn6igBuECTTYy0JtuIuXIoQ1y/0njXSkFBUDwUPU150Q44SdbQq5XgI815oWgn6KnWreZDQOZNRHbm2tD7HVyp3jFeUlsGuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gegFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+59XArM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422935,
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "state": "tx_+NILAfiEuEB+On0tnZaBWUBLaTgkJwjEIM/YeckVLrvlCQ5Cg65crEhu2Vyk8DaWZuc0OFlUtYyHDJe3tMRmWbdeXuYn6igBuECTTYy0JtuIuXIoQ1y/0njXSkFBUDwUPU150Q44SdbQq5XgI815oWgn6KnWreZDQOZNRHbm2tD7HVyp3jFeUlsGuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gegFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+59XArM"
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "state": "tx_+NILAfiEuEB+On0tnZaBWUBLaTgkJwjEIM/YeckVLrvlCQ5Cg65crEhu2Vyk8DaWZuc0OFlUtYyHDJe3tMRmWbdeXuYn6igBuECTTYy0JtuIuXIoQ1y/0njXSkFBUDwUPU150Q44SdbQq5XgI815oWgn6KnWreZDQOZNRHbm2tD7HVyp3jFeUlsGuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gegFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+59XArM"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422934,
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
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422934,
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
  "id": -576460752303422933,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422933,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEB+On0tnZaBWUBLaTgkJwjEIM/YeckVLrvlCQ5Cg65crEhu2Vyk8DaWZuc0OFlUtYyHDJe3tMRmWbdeXuYn6igBuECTTYy0JtuIuXIoQ1y/0njXSkFBUDwUPU150Q44SdbQq5XgI815oWgn6KnWreZDQOZNRHbm2tD7HVyp3jFeUlsGuEj4RjkCoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2gegFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+59XArM",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAERFOXTCgI9pkvU5p4IAgVSzTI1x3zE3BeaTKC+RgWmWrQWXUZolfKB6/weG1AtK/tPFFzwEbYgwF4rJlkvIYBLkBKPkBJTsBoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2qEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThC41PjSCwH4hLhAWpjOwz9UZMgmvPYJ3iCIaqwqLn0kQp6mTsL2BVncf0Yv6F0uVvUZrm0iW5ByhXIYBATHeTlXer3pjzjqKKTPCLhAuUQJsjQUS2usDhK9QHk7IXAafsT/GhLRzCUSGtZB3GfE0dOd0FNa3rcGS+iQAk572HzbKe7YlCDHkmEk+c7RB7hI+EY5AqEGZ5Ewrc5WUQoAhEaKUcACmiaoGdm+A1XZ6F3KF+GYVdoFoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uAIZwSIYbDz8PxITSNA==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAERFOXTCgI9pkvU5p4IAgVSzTI1x3zE3BeaTKC+RgWmWrQWXUZolfKB6/weG1AtK/tPFFzwEbYgwF4rJlkvIYBLkBKPkBJTsBoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2qEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThC41PjSCwH4hLhAWpjOwz9UZMgmvPYJ3iCIaqwqLn0kQp6mTsL2BVncf0Yv6F0uVvUZrm0iW5ByhXIYBATHeTlXer3pjzjqKKTPCLhAuUQJsjQUS2usDhK9QHk7IXAafsT/GhLRzCUSGtZB3GfE0dOd0FNa3rcGS+iQAk572HzbKe7YlCDHkmEk+c7RB7hI+EY5AqEGZ5Ewrc5WUQoAhEaKUcACmiaoGdm+A1XZ6F3KF+GYVdoFoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uAIZwSIYbDz8PxITSNA==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "`�3���(��f\u0010hYγ����W���\rtu����",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBmeRMK3OVlEKAIRGilHAApomqBnZvgNV2ehdyhfhmFXaoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY2kdavv/+GG0jrV+ABAIYSMJzlQAApO2deKw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422932,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEDXV4mYyp//pQn/w1I3he62LlkRBlv00dbqVsMuP6DyB3HJJGf2fKiCDqi1un7vgva6ih3PUO4m57NSFkzLI/0MuF/4XTUBoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7//hhtI61fgAQCGEjCc5UAAKZ/aJ14="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422932,
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEDXV4mYyp//pQn/w1I3he62LlkRBlv00dbqVsMuP6DyB3HJJGf2fKiCDqi1un7vgva6ih3PUO4m57NSFkzLI/0MuF/4XTUBoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7//hhtI61fgAQCGEjCc5UAAKZ/aJ14=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422931,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEAjVFLYalSGIkOfJ/hr2zimu4y49tmVslx2BpwsW138kXXS8a8TAGLFa2lylnyRYHD9zigbK0DT67E1XxlnF3MAuEDXV4mYyp//pQn/w1I3he62LlkRBlv00dbqVsMuP6DyB3HJJGf2fKiCDqi1un7vgva6ih3PUO4m57NSFkzLI/0MuF/4XTUBoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7//hhtI61fgAQCGEjCc5UAAKTN0HJE="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
  "id": -576460752303422931,
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAjVFLYalSGIkOfJ/hr2zimu4y49tmVslx2BpwsW138kXXS8a8TAGLFa2lylnyRYHD9zigbK0DT67E1XxlnF3MAuEDXV4mYyp//pQn/w1I3he62LlkRBlv00dbqVsMuP6DyB3HJJGf2fKiCDqi1un7vgva6ih3PUO4m57NSFkzLI/0MuF/4XTUBoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7//hhtI61fgAQCGEjCc5UAAKTN0HJE=",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAjVFLYalSGIkOfJ/hr2zimu4y49tmVslx2BpwsW138kXXS8a8TAGLFa2lylnyRYHD9zigbK0DT67E1XxlnF3MAuEDXV4mYyp//pQn/w1I3he62LlkRBlv00dbqVsMuP6DyB3HJJGf2fKiCDqi1un7vgva6ih3PUO4m57NSFkzLI/0MuF/4XTUBoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7//hhtI61fgAQCGEjCc5UAAKTN0HJE=",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAjVFLYalSGIkOfJ/hr2zimu4y49tmVslx2BpwsW138kXXS8a8TAGLFa2lylnyRYHD9zigbK0DT67E1XxlnF3MAuEDXV4mYyp//pQn/w1I3he62LlkRBlv00dbqVsMuP6DyB3HJJGf2fKiCDqi1un7vgva6ih3PUO4m57NSFkzLI/0MuF/4XTUBoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7//hhtI61fgAQCGEjCc5UAAKTN0HJE=",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAjVFLYalSGIkOfJ/hr2zimu4y49tmVslx2BpwsW138kXXS8a8TAGLFa2lylnyRYHD9zigbK0DT67E1XxlnF3MAuEDXV4mYyp//pQn/w1I3he62LlkRBlv00dbqVsMuP6DyB3HJJGf2fKiCDqi1un7vgva6ih3PUO4m57NSFkzLI/0MuF/4XTUBoQZnkTCtzlZRCgCERopRwAKaJqgZ2b4DVdnoXcoX4ZhV2qEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGNpHWr7//hhtI61fgAQCGEjCc5UAAKTN0HJE=",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "event": "closed_confirmed"
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
    "channel_id": "ch_ncV4a8JLAc1MGv4kiai7uFXzdjafc17UXXy6UmqS4ARFWLbFS",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection
