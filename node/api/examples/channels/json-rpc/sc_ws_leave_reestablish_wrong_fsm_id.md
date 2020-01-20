
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish_wrong_fsm_id%2F3292
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
      "fsm_id": "ba_+OCDUHn5JhV4u16PSwOe4f1HUI4vi4RdiNRaia6HqKvukmxC"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish_wrong_fsm_id%2F3292
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
      "fsm_id": "ba_2XMnV03zdcG1COO9Lk/T5kImh9ZaULOR69rSicg8RRfTTNpN"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4WRZzMFw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423247,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAUDgULd4TbMxoHvwkTx60aU3+nto+3lcPActWxi/STZtOmFE2cwClPWTZWZhxyoQVbYMt2GSEd2iWfoSq/WK0GuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uFisEHhU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423247,
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
      "signed_tx": "tx_+MsLAfhCuEAUDgULd4TbMxoHvwkTx60aU3+nto+3lcPActWxi/STZtOmFE2cwClPWTZWZhxyoQVbYMt2GSEd2iWfoSq/WK0GuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uFisEHhU=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423246,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAFA4FC3eE2zMaB78JE8etGlN/p7aPt5XDwHLVsYv0k2bTphRNnMApT1k2VmYccqEFW2DLdhkhHdoln6Eqv1itBrhAz96YNKnmr3IXtl+sLXXiDXjlyO/hRBwQWQziNLYYB+lXmE5gY0tA5uNNLVzamSPw6djko5u4/UhYl1J0jBrUDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hZNt/c9"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423246,
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAFA4FC3eE2zMaB78JE8etGlN/p7aPt5XDwHLVsYv0k2bTphRNnMApT1k2VmYccqEFW2DLdhkhHdoln6Eqv1itBrhAz96YNKnmr3IXtl+sLXXiDXjlyO/hRBwQWQziNLYYB+lXmE5gY0tA5uNNLVzamSPw6djko5u4/UhYl1J0jBrUDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hZNt/c9",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAFA4FC3eE2zMaB78JE8etGlN/p7aPt5XDwHLVsYv0k2bTphRNnMApT1k2VmYccqEFW2DLdhkhHdoln6Eqv1itBrhAz96YNKnmr3IXtl+sLXXiDXjlyO/hRBwQWQziNLYYB+lXmE5gY0tA5uNNLVzamSPw6djko5u4/UhYl1J0jBrUDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hZNt/c9",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAFA4FC3eE2zMaB78JE8etGlN/p7aPt5XDwHLVsYv0k2bTphRNnMApT1k2VmYccqEFW2DLdhkhHdoln6Eqv1itBrhAz96YNKnmr3IXtl+sLXXiDXjlyO/hRBwQWQziNLYYB+lXmE5gY0tA5uNNLVzamSPw6djko5u4/UhYl1J0jBrUDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hZNt/c9",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAFA4FC3eE2zMaB78JE8etGlN/p7aPt5XDwHLVsYv0k2bTphRNnMApT1k2VmYccqEFW2DLdhkhHdoln6Eqv1itBrhAz96YNKnmr3IXtl+sLXXiDXjlyO/hRBwQWQziNLYYB+lXmE5gY0tA5uNNLVzamSPw6djko5u4/UhYl1J0jBrUDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hZNt/c9",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "message": {
        "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "message": {
        "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
  "id": -576460752303423245,
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423245,
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "state": "tx_+QENCwH4hLhAFA4FC3eE2zMaB78JE8etGlN/p7aPt5XDwHLVsYv0k2bTphRNnMApT1k2VmYccqEFW2DLdhkhHdoln6Eqv1itBrhAz96YNKnmr3IXtl+sLXXiDXjlyO/hRBwQWQziNLYYB+lXmE5gY0tA5uNNLVzamSPw6djko5u4/UhYl1J0jBrUDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hZNt/c9"
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "state": "tx_+QENCwH4hLhAFA4FC3eE2zMaB78JE8etGlN/p7aPt5XDwHLVsYv0k2bTphRNnMApT1k2VmYccqEFW2DLdhkhHdoln6Eqv1itBrhAz96YNKnmr3IXtl+sLXXiDXjlyO/hRBwQWQziNLYYB+lXmE5gY0tA5uNNLVzamSPw6djko5u4/UhYl1J0jBrUDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hZNt/c9"
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "state": "tx_+QENCwH4hLhAFA4FC3eE2zMaB78JE8etGlN/p7aPt5XDwHLVsYv0k2bTphRNnMApT1k2VmYccqEFW2DLdhkhHdoln6Eqv1itBrhAz96YNKnmr3IXtl+sLXXiDXjlyO/hRBwQWQziNLYYB+lXmE5gY0tA5uNNLVzamSPw6djko5u4/UhYl1J0jBrUDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hZNt/c9"
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "state": "tx_+QENCwH4hLhAFA4FC3eE2zMaB78JE8etGlN/p7aPt5XDwHLVsYv0k2bTphRNnMApT1k2VmYccqEFW2DLdhkhHdoln6Eqv1itBrhAz96YNKnmr3IXtl+sLXXiDXjlyO/hRBwQWQziNLYYB+lXmE5gY0tA5uNNLVzamSPw6djko5u4/UhYl1J0jBrUDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hZNt/c9"
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAFA4FC3eE2zMaB78JE8etGlN%2Fp7aPt5XDwHLVsYv0k2bTphRNnMApT1k2VmYccqEFW2DLdhkhHdoln6Eqv1itBrhAz96YNKnmr3IXtl%2BsLXXiDXjlyO%2FhRBwQWQziNLYYB%2BlXmE5gY0tA5uNNLVzamSPw6djko5u4%2FUhYl1J0jBrUDLiD%2BIEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu%2FSGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G%2BJNZ1%2B3HKCYNWL2rDf7hZNt%2Fc9&port=13180&protocol=json-rpc&role=initiator
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

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAFA4FC3eE2zMaB78JE8etGlN%2Fp7aPt5XDwHLVsYv0k2bTphRNnMApT1k2VmYccqEFW2DLdhkhHdoln6Eqv1itBrhAz96YNKnmr3IXtl%2BsLXXiDXjlyO%2FhRBwQWQziNLYYB%2BlXmE5gY0tA5uNNLVzamSPw6djko5u4%2FUhYl1J0jBrUDLiD%2BIEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu%2FSGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G%2BJNZ1%2B3HKCYNWL2rDf7hZNt%2Fc9&port=13180&protocol=json-rpc&role=responder
```

#### responder <--- node
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

#### responder closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua&existing_fsm_id=Invalid&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAFA4FC3eE2zMaB78JE8etGlN%2Fp7aPt5XDwHLVsYv0k2bTphRNnMApT1k2VmYccqEFW2DLdhkhHdoln6Eqv1itBrhAz96YNKnmr3IXtl%2BsLXXiDXjlyO%2FhRBwQWQziNLYYB%2BlXmE5gY0tA5uNNLVzamSPw6djko5u4%2FUhYl1J0jBrUDLiD%2BIEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu%2FSGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G%2BJNZ1%2B3HKCYNWL2rDf7hZNt%2Fc9&port=13180&protocol=json-rpc&role=initiator
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

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua&existing_fsm_id=Invalid&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAFA4FC3eE2zMaB78JE8etGlN%2Fp7aPt5XDwHLVsYv0k2bTphRNnMApT1k2VmYccqEFW2DLdhkhHdoln6Eqv1itBrhAz96YNKnmr3IXtl%2BsLXXiDXjlyO%2FhRBwQWQziNLYYB%2BlXmE5gY0tA5uNNLVzamSPw6djko5u4%2FUhYl1J0jBrUDLiD%2BIEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu%2FSGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G%2BJNZ1%2B3HKCYNWL2rDf7hZNt%2Fc9&port=13180&protocol=json-rpc&role=responder
```

#### responder <--- node
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

#### responder closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua&existing_fsm_id=ba_hiV1z57%2F1%2FjFI6jS&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAFA4FC3eE2zMaB78JE8etGlN%2Fp7aPt5XDwHLVsYv0k2bTphRNnMApT1k2VmYccqEFW2DLdhkhHdoln6Eqv1itBrhAz96YNKnmr3IXtl%2BsLXXiDXjlyO%2FhRBwQWQziNLYYB%2BlXmE5gY0tA5uNNLVzamSPw6djko5u4%2FUhYl1J0jBrUDLiD%2BIEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu%2FSGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G%2BJNZ1%2B3HKCYNWL2rDf7hZNt%2Fc9&port=13180&protocol=json-rpc&role=initiator
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

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua&existing_fsm_id=ba_hiV1z57%2F1%2FjFI6jS&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAFA4FC3eE2zMaB78JE8etGlN%2Fp7aPt5XDwHLVsYv0k2bTphRNnMApT1k2VmYccqEFW2DLdhkhHdoln6Eqv1itBrhAz96YNKnmr3IXtl%2BsLXXiDXjlyO%2FhRBwQWQziNLYYB%2BlXmE5gY0tA5uNNLVzamSPw6djko5u4%2FUhYl1J0jBrUDLiD%2BIEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu%2FSGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G%2BJNZ1%2B3HKCYNWL2rDf7hZNt%2Fc9&port=13180&protocol=json-rpc&role=responder
```

#### responder <--- node
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

#### responder closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua&existing_fsm_id=ba_b1d64JmlnmyQGwv%2F73cLb9xeOHmR7ID55suRt5dPbx92t3ir&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAFA4FC3eE2zMaB78JE8etGlN%2Fp7aPt5XDwHLVsYv0k2bTphRNnMApT1k2VmYccqEFW2DLdhkhHdoln6Eqv1itBrhAz96YNKnmr3IXtl%2BsLXXiDXjlyO%2FhRBwQWQziNLYYB%2BlXmE5gY0tA5uNNLVzamSPw6djko5u4%2FUhYl1J0jBrUDLiD%2BIEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu%2FSGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G%2BJNZ1%2B3HKCYNWL2rDf7hZNt%2Fc9&port=13180&protocol=json-rpc&role=initiator
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

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua&existing_fsm_id=ba_b1d64JmlnmyQGwv%2F73cLb9xeOHmR7ID55suRt5dPbx92t3ir&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAFA4FC3eE2zMaB78JE8etGlN%2Fp7aPt5XDwHLVsYv0k2bTphRNnMApT1k2VmYccqEFW2DLdhkhHdoln6Eqv1itBrhAz96YNKnmr3IXtl%2BsLXXiDXjlyO%2FhRBwQWQziNLYYB%2BlXmE5gY0tA5uNNLVzamSPw6djko5u4%2FUhYl1J0jBrUDLiD%2BIEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu%2FSGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G%2BJNZ1%2B3HKCYNWL2rDf7hZNt%2Fc9&port=13180&protocol=json-rpc&role=responder
```

#### responder <--- node
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

#### responder closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua&existing_fsm_id=ba_2XMnV03zdcG1COO9Lk%2FT5kImh9ZaULOR69rSicg8RRfTTNpN&offchain_tx=tx_%2BQENCwH4hLhAFA4FC3eE2zMaB78JE8etGlN%2Fp7aPt5XDwHLVsYv0k2bTphRNnMApT1k2VmYccqEFW2DLdhkhHdoln6Eqv1itBrhAz96YNKnmr3IXtl%2BsLXXiDXjlyO%2FhRBwQWQziNLYYB%2BlXmE5gY0tA5uNNLVzamSPw6djko5u4%2FUhYl1J0jBrUDLiD%2BIEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu%2FSGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G%2BJNZ1%2B3HKCYNWL2rDf7hZNt%2Fc9&port=13180&protocol=json-rpc&role=responder
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
      "fsm_id": "ba_t04dIAMm7Uq+8op3Q/FExtog22LZhai5CsLmYUwN6eggM/9U"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua&existing_fsm_id=ba_%2BOCDUHn5JhV4u16PSwOe4f1HUI4vi4RdiNRaia6HqKvukmxC&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAFA4FC3eE2zMaB78JE8etGlN%2Fp7aPt5XDwHLVsYv0k2bTphRNnMApT1k2VmYccqEFW2DLdhkhHdoln6Eqv1itBrhAz96YNKnmr3IXtl%2BsLXXiDXjlyO%2FhRBwQWQziNLYYB%2BlXmE5gY0tA5uNNLVzamSPw6djko5u4%2FUhYl1J0jBrUDLiD%2BIEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu%2FSGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G%2BJNZ1%2B3HKCYNWL2rDf7hZNt%2Fc9&port=13180&protocol=json-rpc&role=initiator
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
      "fsm_id": "ba_AOzPQjuUnneViVxlgKukCJG/1WH2CbScg537Q3H3QkwgxgtV"
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "state": "tx_+QENCwH4hLhAFA4FC3eE2zMaB78JE8etGlN/p7aPt5XDwHLVsYv0k2bTphRNnMApT1k2VmYccqEFW2DLdhkhHdoln6Eqv1itBrhAz96YNKnmr3IXtl+sLXXiDXjlyO/hRBwQWQziNLYYB+lXmE5gY0tA5uNNLVzamSPw6djko5u4/UhYl1J0jBrUDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hZNt/c9"
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "state": "tx_+QENCwH4hLhAFA4FC3eE2zMaB78JE8etGlN/p7aPt5XDwHLVsYv0k2bTphRNnMApT1k2VmYccqEFW2DLdhkhHdoln6Eqv1itBrhAz96YNKnmr3IXtl+sLXXiDXjlyO/hRBwQWQziNLYYB+lXmE5gY0tA5uNNLVzamSPw6djko5u4/UhYl1J0jBrUDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hZNt/c9"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423244,
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423244,
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBulLUX+imUaGmVgrSLieOHHazppUfg2YXI6XbiYH2bnsAqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B1+6amU=",
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
  "id": -576460752303423243,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECmqKmO8+FAzwvv443kA7G8iCqgf4MDIe55UMEbvTjXNSFCo4wkZlzBOsrADrf0z9OCKg4tKY4+cB761qaL/0sIuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeEHNCx"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423243,
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "signed_tx": "tx_+JALAfhCuECmqKmO8+FAzwvv443kA7G8iCqgf4MDIe55UMEbvTjXNSFCo4wkZlzBOsrADrf0z9OCKg4tKY4+cB761qaL/0sIuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeEHNCx",
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
  "id": -576460752303423242,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBqkiw/ccqXl68B5FjjlGyQJVo6dF3AAsJpTO3Gw0SALS2dX47dvptZlQhbGMvARnsXrhEfKjwwAYbm8fVf5BoOuECmqKmO8+FAzwvv443kA7G8iCqgf4MDIe55UMEbvTjXNSFCo4wkZlzBOsrADrf0z9OCKg4tKY4+cB761qaL/0sIuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcr/egQ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423242,
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "state": "tx_+NILAfiEuEBqkiw/ccqXl68B5FjjlGyQJVo6dF3AAsJpTO3Gw0SALS2dX47dvptZlQhbGMvARnsXrhEfKjwwAYbm8fVf5BoOuECmqKmO8+FAzwvv443kA7G8iCqgf4MDIe55UMEbvTjXNSFCo4wkZlzBOsrADrf0z9OCKg4tKY4+cB761qaL/0sIuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcr/egQ"
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "state": "tx_+NILAfiEuEBqkiw/ccqXl68B5FjjlGyQJVo6dF3AAsJpTO3Gw0SALS2dX47dvptZlQhbGMvARnsXrhEfKjwwAYbm8fVf5BoOuECmqKmO8+FAzwvv443kA7G8iCqgf4MDIe55UMEbvTjXNSFCo4wkZlzBOsrADrf0z9OCKg4tKY4+cB761qaL/0sIuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcr/egQ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423241,
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423241,
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
  "id": -576460752303423240,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423240,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBqkiw/ccqXl68B5FjjlGyQJVo6dF3AAsJpTO3Gw0SALS2dX47dvptZlQhbGMvARnsXrhEfKjwwAYbm8fVf5BoOuECmqKmO8+FAzwvv443kA7G8iCqgf4MDIe55UMEbvTjXNSFCo4wkZlzBOsrADrf0z9OCKg4tKY4+cB761qaL/0sIuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcr/egQ",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423239,
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423239,
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBulLUX+imUaGmVgrSLieOHHazppUfg2YXI6XbiYH2bnsA6AWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7v0UFTs=",
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
  "id": -576460752303423238,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBLTMZFfslE1LUqI/t2Whtv3VQakB6iuiicZX5UaxgHcFnTJWirinM6YTXDCA0HX0Es6J5TvCmPHuoP6u954OUCuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6JbW+V"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423238,
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBLTMZFfslE1LUqI/t2Whtv3VQakB6iuiicZX5UaxgHcFnTJWirinM6YTXDCA0HX0Es6J5TvCmPHuoP6u954OUCuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6JbW+V",
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
  "id": -576460752303423237,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBLTMZFfslE1LUqI/t2Whtv3VQakB6iuiicZX5UaxgHcFnTJWirinM6YTXDCA0HX0Es6J5TvCmPHuoP6u954OUCuECO0fdahsX5Ojxhp6mJhwRwwbdm62aSPcfXoimICVLk8J9Gj3+TT8UYXgV4vie570qQ3rOzH7OurAKhOD1h6dsHuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7bMetE"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423237,
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "state": "tx_+NILAfiEuEBLTMZFfslE1LUqI/t2Whtv3VQakB6iuiicZX5UaxgHcFnTJWirinM6YTXDCA0HX0Es6J5TvCmPHuoP6u954OUCuECO0fdahsX5Ojxhp6mJhwRwwbdm62aSPcfXoimICVLk8J9Gj3+TT8UYXgV4vie570qQ3rOzH7OurAKhOD1h6dsHuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7bMetE"
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "state": "tx_+NILAfiEuEBLTMZFfslE1LUqI/t2Whtv3VQakB6iuiicZX5UaxgHcFnTJWirinM6YTXDCA0HX0Es6J5TvCmPHuoP6u954OUCuECO0fdahsX5Ojxhp6mJhwRwwbdm62aSPcfXoimICVLk8J9Gj3+TT8UYXgV4vie570qQ3rOzH7OurAKhOD1h6dsHuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7bMetE"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423236,
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423236,
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
  "id": -576460752303423235,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423235,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBLTMZFfslE1LUqI/t2Whtv3VQakB6iuiicZX5UaxgHcFnTJWirinM6YTXDCA0HX0Es6J5TvCmPHuoP6u954OUCuECO0fdahsX5Ojxhp6mJhwRwwbdm62aSPcfXoimICVLk8J9Gj3+TT8UYXgV4vie570qQ3rOzH7OurAKhOD1h6dsHuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7bMetE",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423234,
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423234,
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBulLUX+imUaGmVgrSLieOHHazppUfg2YXI6XbiYH2bnsBKArw56Yk/nuAn9SDD7EMYNf1i7BI0w+TO2mQGxnQbS3tvjqtsk=",
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
  "id": -576460752303423233,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECuvPtP3HdUyikw8Tl4m1vBL+DD47BaNx+einR5lC0KWckqSEz1qmftm99WoCPVIGyAcwPvxus1Sc0FJ84fG40LuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57ASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7ZIt6xG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423233,
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "signed_tx": "tx_+JALAfhCuECuvPtP3HdUyikw8Tl4m1vBL+DD47BaNx+einR5lC0KWckqSEz1qmftm99WoCPVIGyAcwPvxus1Sc0FJ84fG40LuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57ASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7ZIt6xG",
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
  "id": -576460752303423232,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBEsJj3Lf7CbiQTHOz/FDApAjEDIgQbgdqOoE3NVqpW5+OkB7HYsLNzwn40lU3wNVGez2/A1inNwCoRA4k/q14DuECuvPtP3HdUyikw8Tl4m1vBL+DD47BaNx+einR5lC0KWckqSEz1qmftm99WoCPVIGyAcwPvxus1Sc0FJ84fG40LuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57ASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7ajHCPw"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423232,
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "state": "tx_+NILAfiEuEBEsJj3Lf7CbiQTHOz/FDApAjEDIgQbgdqOoE3NVqpW5+OkB7HYsLNzwn40lU3wNVGez2/A1inNwCoRA4k/q14DuECuvPtP3HdUyikw8Tl4m1vBL+DD47BaNx+einR5lC0KWckqSEz1qmftm99WoCPVIGyAcwPvxus1Sc0FJ84fG40LuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57ASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7ajHCPw"
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "state": "tx_+NILAfiEuEBEsJj3Lf7CbiQTHOz/FDApAjEDIgQbgdqOoE3NVqpW5+OkB7HYsLNzwn40lU3wNVGez2/A1inNwCoRA4k/q14DuECuvPtP3HdUyikw8Tl4m1vBL+DD47BaNx+einR5lC0KWckqSEz1qmftm99WoCPVIGyAcwPvxus1Sc0FJ84fG40LuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57ASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7ajHCPw"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423231,
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423231,
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
  "id": -576460752303423230,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423230,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBEsJj3Lf7CbiQTHOz/FDApAjEDIgQbgdqOoE3NVqpW5+OkB7HYsLNzwn40lU3wNVGez2/A1inNwCoRA4k/q14DuECuvPtP3HdUyikw8Tl4m1vBL+DD47BaNx+einR5lC0KWckqSEz1qmftm99WoCPVIGyAcwPvxus1Sc0FJ84fG40LuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57ASgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7ajHCPw",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAALDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiYABL489v"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423229,
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423229,
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBulLUX+imUaGmVgrSLieOHHazppUfg2YXI6XbiYH2bnsBaAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7uFUGxo=",
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
  "id": -576460752303423228,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDNebpOFJZAbe43phgZ8I5RHjeu3B2SjBmpvNR8MwRtNCtHV+4b3S584zjNZMaINMuXS7Rm8I467LYhgbeqSFEBuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4pKKB3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423228,
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDNebpOFJZAbe43phgZ8I5RHjeu3B2SjBmpvNR8MwRtNCtHV+4b3S584zjNZMaINMuXS7Rm8I467LYhgbeqSFEBuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4pKKB3",
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
  "id": -576460752303423227,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDNebpOFJZAbe43phgZ8I5RHjeu3B2SjBmpvNR8MwRtNCtHV+4b3S584zjNZMaINMuXS7Rm8I467LYhgbeqSFEBuEDnAu14G65rLtuHiVDfKcZYd7AsJdTkXamlRKmlJlD76vD5dDmqkgKOeJGOKvjX+V0UYNRqES3J+dUoYiu+2LkCuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5EbJwv"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423227,
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "state": "tx_+NILAfiEuEDNebpOFJZAbe43phgZ8I5RHjeu3B2SjBmpvNR8MwRtNCtHV+4b3S584zjNZMaINMuXS7Rm8I467LYhgbeqSFEBuEDnAu14G65rLtuHiVDfKcZYd7AsJdTkXamlRKmlJlD76vD5dDmqkgKOeJGOKvjX+V0UYNRqES3J+dUoYiu+2LkCuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5EbJwv"
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "state": "tx_+NILAfiEuEDNebpOFJZAbe43phgZ8I5RHjeu3B2SjBmpvNR8MwRtNCtHV+4b3S584zjNZMaINMuXS7Rm8I467LYhgbeqSFEBuEDnAu14G65rLtuHiVDfKcZYd7AsJdTkXamlRKmlJlD76vD5dDmqkgKOeJGOKvjX+V0UYNRqES3J+dUoYiu+2LkCuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5EbJwv"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423226,
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423226,
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
  "id": -576460752303423225,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423225,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDNebpOFJZAbe43phgZ8I5RHjeu3B2SjBmpvNR8MwRtNCtHV+4b3S584zjNZMaINMuXS7Rm8I467LYhgbeqSFEBuEDnAu14G65rLtuHiVDfKcZYd7AsJdTkXamlRKmlJlD76vD5dDmqkgKOeJGOKvjX+V0UYNRqES3J+dUoYiu+2LkCuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5EbJwv",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423224,
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423224,
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBulLUX+imUaGmVgrSLieOHHazppUfg2YXI6XbiYH2bnsBqArw56Yk/nuAn9SDD7EMYNf1i7BI0w+TO2mQGxnQbS3trDWfcU=",
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
  "id": -576460752303423223,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDkCBp2JWyBvwKVeZow8clmQkWOmZ9pt/HZ3NpNCILF7pPjdWx4iCQQLSlYgC0vZlBNfnopMUy3vL/YyoZ2eMYKuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7a/Q9ll"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423223,
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDkCBp2JWyBvwKVeZow8clmQkWOmZ9pt/HZ3NpNCILF7pPjdWx4iCQQLSlYgC0vZlBNfnopMUy3vL/YyoZ2eMYKuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7a/Q9ll",
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
  "id": -576460752303423222,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDMnVi3rrDFUSItp2GALa3SiCB3O6xpddYs+jiSHFyF2sdLYSANxg37DXpPELyTwkfZcYpfPlFtwb8lWwqRl/sEuEDkCBp2JWyBvwKVeZow8clmQkWOmZ9pt/HZ3NpNCILF7pPjdWx4iCQQLSlYgC0vZlBNfnopMUy3vL/YyoZ2eMYKuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Zp8288"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423222,
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "state": "tx_+NILAfiEuEDMnVi3rrDFUSItp2GALa3SiCB3O6xpddYs+jiSHFyF2sdLYSANxg37DXpPELyTwkfZcYpfPlFtwb8lWwqRl/sEuEDkCBp2JWyBvwKVeZow8clmQkWOmZ9pt/HZ3NpNCILF7pPjdWx4iCQQLSlYgC0vZlBNfnopMUy3vL/YyoZ2eMYKuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Zp8288"
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "state": "tx_+NILAfiEuEDMnVi3rrDFUSItp2GALa3SiCB3O6xpddYs+jiSHFyF2sdLYSANxg37DXpPELyTwkfZcYpfPlFtwb8lWwqRl/sEuEDkCBp2JWyBvwKVeZow8clmQkWOmZ9pt/HZ3NpNCILF7pPjdWx4iCQQLSlYgC0vZlBNfnopMUy3vL/YyoZ2eMYKuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Zp8288"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423221,
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423221,
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
  "id": -576460752303423220,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423220,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDMnVi3rrDFUSItp2GALa3SiCB3O6xpddYs+jiSHFyF2sdLYSANxg37DXpPELyTwkfZcYpfPlFtwb8lWwqRl/sEuEDkCBp2JWyBvwKVeZow8clmQkWOmZ9pt/HZ3NpNCILF7pPjdWx4iCQQLSlYgC0vZlBNfnopMUy3vL/YyoZ2eMYKuEj4RjkCoQbpS1F/oplGhplYK0i4njhx2s6aVH4NmFyOl24mB9m57AagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7Zp8288",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAALDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiYABL489v"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423219,
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423219,
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
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
    "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator ---> node
```javascript
{
  "id": -576460752303423218,
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
  "channel_id": "ch_2mkBstFspzkB9eLSRQx3NhLG1SuZMPWsgonDEeRbFhrmZfm9ua",
  "id": -576460752303423218,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
