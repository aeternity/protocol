
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
      "fsm_id": "ba_zuqdwU3/Ka3iX1HulywU0XuOzqWE2u8vZhEOrCAwYrS7KKzA"
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
      "fsm_id": "ba_9hzw1Tt8RVW6eIj9I0Pa4cPxxXyZV9qrbDxgd7qbK2ptbFSj"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+46ht+p/A==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422889,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDk3NI/KNto3rrzgszvrM6iesOXLdOyehl+eNIKVAGzXq074cPfQvd51MgDPr6Pd8uFtYITm/zUu/gqceRFqfwHuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uOtMC8kA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422889,
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
      "signed_tx": "tx_+MsLAfhCuEDk3NI/KNto3rrzgszvrM6iesOXLdOyehl+eNIKVAGzXq074cPfQvd51MgDPr6Pd8uFtYITm/zUu/gqceRFqfwHuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uOtMC8kA=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422888,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAyxLkWGd4RK20J9//oQZY6n2CyKAsZYOK4bSdYEyn6VU5IEctdaNdk4a6pqhylqvpNadnHoTacaEec5zpxrAJDLhA5NzSPyjbaN6684LM76zOonrDly3TsnoZfnjSClQBs16tO+HD30L3edTIAz6+j3fLhbWCE5v81Lv4KnHkRan8B7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jp3QR94"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422888,
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
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAyxLkWGd4RK20J9//oQZY6n2CyKAsZYOK4bSdYEyn6VU5IEctdaNdk4a6pqhylqvpNadnHoTacaEec5zpxrAJDLhA5NzSPyjbaN6684LM76zOonrDly3TsnoZfnjSClQBs16tO+HD30L3edTIAz6+j3fLhbWCE5v81Lv4KnHkRan8B7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jp3QR94",
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
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAyxLkWGd4RK20J9//oQZY6n2CyKAsZYOK4bSdYEyn6VU5IEctdaNdk4a6pqhylqvpNadnHoTacaEec5zpxrAJDLhA5NzSPyjbaN6684LM76zOonrDly3TsnoZfnjSClQBs16tO+HD30L3edTIAz6+j3fLhbWCE5v81Lv4KnHkRan8B7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jp3QR94",
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
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAyxLkWGd4RK20J9//oQZY6n2CyKAsZYOK4bSdYEyn6VU5IEctdaNdk4a6pqhylqvpNadnHoTacaEec5zpxrAJDLhA5NzSPyjbaN6684LM76zOonrDly3TsnoZfnjSClQBs16tO+HD30L3edTIAz6+j3fLhbWCE5v81Lv4KnHkRan8B7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jp3QR94",
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
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAyxLkWGd4RK20J9//oQZY6n2CyKAsZYOK4bSdYEyn6VU5IEctdaNdk4a6pqhylqvpNadnHoTacaEec5zpxrAJDLhA5NzSPyjbaN6684LM76zOonrDly3TsnoZfnjSClQBs16tO+HD30L3edTIAz6+j3fLhbWCE5v81Lv4KnHkRan8B7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jp3QR94",
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
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
    "data": {
      "message": {
        "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
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
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
    "data": {
      "message": {
        "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
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
  "id": -576460752303422887,
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
  "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
  "id": -576460752303422887,
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
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
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
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
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
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
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
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
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
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
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
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
    "data": {
      "event": "open"
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
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
    "data": {
      "state": "tx_+QENCwH4hLhAyxLkWGd4RK20J9//oQZY6n2CyKAsZYOK4bSdYEyn6VU5IEctdaNdk4a6pqhylqvpNadnHoTacaEec5zpxrAJDLhA5NzSPyjbaN6684LM76zOonrDly3TsnoZfnjSClQBs16tO+HD30L3edTIAz6+j3fLhbWCE5v81Lv4KnHkRan8B7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jp3QR94"
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
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
    "data": {
      "state": "tx_+QENCwH4hLhAyxLkWGd4RK20J9//oQZY6n2CyKAsZYOK4bSdYEyn6VU5IEctdaNdk4a6pqhylqvpNadnHoTacaEec5zpxrAJDLhA5NzSPyjbaN6684LM76zOonrDly3TsnoZfnjSClQBs16tO+HD30L3edTIAz6+j3fLhbWCE5v81Lv4KnHkRan8B7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jp3QR94"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBj2mK4xoggJnX3mnJoTd0ZdNxHUbPC9rsC+SRkq5JLK5oQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79AIAhg/AoHKQAKChXLDyVpEyqFjhIeWBI1DOO4boF2NOsTcvscbEzeU31gI7tz6VIw==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainDeposit"
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
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
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
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
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
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBj2mK4xoggJnX3mnJoTd0ZdNxHUbPC9rsC+SRkq5JLK5oQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEAIAhg/AoHKQAKCrxDtQzyez86BLbjvUuOUeV9h2xXHFJA9GSc2nrWsrIQIX2A0RIQ==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainDeposit"
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
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
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
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBj2mK4xoggJnX3mnJoTd0ZdNxHUbPC9rsC+SRkq5JLK5oQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79AIAhg/AoHKQAKChXLDyVpEyqFjhIeWBI1DOO4boF2NOsTcvscbEzeU31gI7tz6VIw==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainDeposit"
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
  "id": -576460752303422886,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEBNizT5iU1YWU22BhAQ7CaU3QAeFuQWVU5Q/OrgSa0c+y2aQx3TD5zMQKGeFAftvllmC8aXUdkvQS3Xy/Ff1fMEuHT4cjMBoQY9piuMaIICZ195pyaE3dGXTcR1Gzwva7AvkkZKuSSyuaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgoVyw8laRMqhY4SHlgSNQzjuG6BdjTrE3L7HGxM3lN9YCOy5nDvY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
  "id": -576460752303422886,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1018,
        "message": "Not allowed at current channel state"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.deposit_tx",
      "params": {
        "error": 42
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
    "data": {
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEBNizT5iU1YWU22BhAQ7CaU3QAeFuQWVU5Q/OrgSa0c+y2aQx3TD5zMQKGeFAftvllmC8aXUdkvQS3Xy/Ff1fMEuHT4cjMBoQY9piuMaIICZ195pyaE3dGXTcR1Gzwva7AvkkZKuSSyuaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgoVyw8laRMqhY4SHlgSNQzjuG6BdjTrE3L7HGxM3lN9YCOy5nDvY=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainDeposit"
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
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
    "data": {
      "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
      "error_code": 42,
      "error_msg": "unknown",
      "round": 1
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
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
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
  "id": -576460752303422885,
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
  "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
  "id": -576460752303422885,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422884,
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
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
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
  "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
  "id": -576460752303422884,
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
    "channel_id": "ch_U9k8NApq5yuMAvSw5PqRuywfcXeFhnTTpLce6TEHrvdpfLh3f",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection
