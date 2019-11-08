
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB&role=initiator&state_password=correct%20horse%20battery%20staple
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB&role=responder&state_password=correct%20horse%20battery%20staple
```

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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAUKb/1JfxwzvvmDFIC1o530HacCdDFXnfPTamRdweFTPhj+qJSJgAKEBqgkQQiVH+lHmq3HkWEmjhSXnUuNViX3t3qbSfZk5HKKGJGE5yoAAAgoAhhAGeddIAMCg5jF4dmRhOWF4TfvSSJ5YIbPxsJbhIIZjkX2+cHp8u/Ud+sWETg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423111,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBd/PAwnlkBxwcdCVBOU6CACE4uy2kAGKKnTuKnahYHaKx2277o5hYdMk5LIDZdjDdz43rO6V/oIgV6gk5hK0IFuIP4gTIBoQFCm/9SX8cM775gxSAtaOd9B2nAnQxV53z02pkXcHhUz4Y/qiUiYAChAaoJEEIlR/pR5qtx5FhJo4Ul51LjVYl97d6m0n2ZORyihiRhOcqAAAIKAIYQBnnXSADAoOYxeHZkYTlheE370kieWCGz8bCW4SCGY5F9vnB6fLv1HS7hO58="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423111,
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
      "signed_tx": "tx_+MsLAfhCuEBd/PAwnlkBxwcdCVBOU6CACE4uy2kAGKKnTuKnahYHaKx2277o5hYdMk5LIDZdjDdz43rO6V/oIgV6gk5hK0IFuIP4gTIBoQFCm/9SX8cM775gxSAtaOd9B2nAnQxV53z02pkXcHhUz4Y/qiUiYAChAaoJEEIlR/pR5qtx5FhJo4Ul51LjVYl97d6m0n2ZORyihiRhOcqAAAIKAIYQBnnXSADAoOYxeHZkYTlheE370kieWCGz8bCW4SCGY5F9vnB6fLv1HS7hO58=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423110,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhATX1MybOHiwV8kZIIESbCYp+mWJBevZgiIqdJ4b2U1/GUlV8iOGzaa9+i61T7js24dHUpxL0LmVGM28q7QZDbCLhAXfzwMJ5ZAccHHQlQTlOggAhOLstpABiip07ip2oWB2isdtu+6OYWHTJOSyA2XYw3c+N6zulf6CIFeoJOYStCBbiD+IEyAaEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM+GP6olImAAoQGqCRBCJUf6UearceRYSaOFJedS41WJfe3eptJ9mTkcooYkYTnKgAACCgCGEAZ510gAwKDmMXh2ZGE5YXhN+9JInlghs/GwluEghmORfb5weny79R2M3x1X"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423110,
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhATX1MybOHiwV8kZIIESbCYp+mWJBevZgiIqdJ4b2U1/GUlV8iOGzaa9+i61T7js24dHUpxL0LmVGM28q7QZDbCLhAXfzwMJ5ZAccHHQlQTlOggAhOLstpABiip07ip2oWB2isdtu+6OYWHTJOSyA2XYw3c+N6zulf6CIFeoJOYStCBbiD+IEyAaEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM+GP6olImAAoQGqCRBCJUf6UearceRYSaOFJedS41WJfe3eptJ9mTkcooYkYTnKgAACCgCGEAZ510gAwKDmMXh2ZGE5YXhN+9JInlghs/GwluEghmORfb5weny79R2M3x1X",
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhATX1MybOHiwV8kZIIESbCYp+mWJBevZgiIqdJ4b2U1/GUlV8iOGzaa9+i61T7js24dHUpxL0LmVGM28q7QZDbCLhAXfzwMJ5ZAccHHQlQTlOggAhOLstpABiip07ip2oWB2isdtu+6OYWHTJOSyA2XYw3c+N6zulf6CIFeoJOYStCBbiD+IEyAaEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM+GP6olImAAoQGqCRBCJUf6UearceRYSaOFJedS41WJfe3eptJ9mTkcooYkYTnKgAACCgCGEAZ510gAwKDmMXh2ZGE5YXhN+9JInlghs/GwluEghmORfb5weny79R2M3x1X",
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhATX1MybOHiwV8kZIIESbCYp+mWJBevZgiIqdJ4b2U1/GUlV8iOGzaa9+i61T7js24dHUpxL0LmVGM28q7QZDbCLhAXfzwMJ5ZAccHHQlQTlOggAhOLstpABiip07ip2oWB2isdtu+6OYWHTJOSyA2XYw3c+N6zulf6CIFeoJOYStCBbiD+IEyAaEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM+GP6olImAAoQGqCRBCJUf6UearceRYSaOFJedS41WJfe3eptJ9mTkcooYkYTnKgAACCgCGEAZ510gAwKDmMXh2ZGE5YXhN+9JInlghs/GwluEghmORfb5weny79R2M3x1X",
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhATX1MybOHiwV8kZIIESbCYp+mWJBevZgiIqdJ4b2U1/GUlV8iOGzaa9+i61T7js24dHUpxL0LmVGM28q7QZDbCLhAXfzwMJ5ZAccHHQlQTlOggAhOLstpABiip07ip2oWB2isdtu+6OYWHTJOSyA2XYw3c+N6zulf6CIFeoJOYStCBbiD+IEyAaEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM+GP6olImAAoQGqCRBCJUf6UearceRYSaOFJedS41WJfe3eptJ9mTkcooYkYTnKgAACCgCGEAZ510gAwKDmMXh2ZGE5YXhN+9JInlghs/GwluEghmORfb5weny79R2M3x1X",
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
    "to": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "message": {
        "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
        "from": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
        "info": "Hello",
        "to": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
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
    "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "message": {
        "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
        "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
        "info": "Hello back",
        "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423109,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
      "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423109,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
      "balance": 69999999999999
    },
    {
      "account": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "state": "tx_+QENCwH4hLhATX1MybOHiwV8kZIIESbCYp+mWJBevZgiIqdJ4b2U1/GUlV8iOGzaa9+i61T7js24dHUpxL0LmVGM28q7QZDbCLhAXfzwMJ5ZAccHHQlQTlOggAhOLstpABiip07ip2oWB2isdtu+6OYWHTJOSyA2XYw3c+N6zulf6CIFeoJOYStCBbiD+IEyAaEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM+GP6olImAAoQGqCRBCJUf6UearceRYSaOFJedS41WJfe3eptJ9mTkcooYkYTnKgAACCgCGEAZ510gAwKDmMXh2ZGE5YXhN+9JInlghs/GwluEghmORfb5weny79R2M3x1X"
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "state": "tx_+QENCwH4hLhATX1MybOHiwV8kZIIESbCYp+mWJBevZgiIqdJ4b2U1/GUlV8iOGzaa9+i61T7js24dHUpxL0LmVGM28q7QZDbCLhAXfzwMJ5ZAccHHQlQTlOggAhOLstpABiip07ip2oWB2isdtu+6OYWHTJOSyA2XYw3c+N6zulf6CIFeoJOYStCBbiD+IEyAaEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM+GP6olImAAoQGqCRBCJUf6UearceRYSaOFJedS41WJfe3eptJ9mTkcooYkYTnKgAACCgCGEAZ510gAwKDmMXh2ZGE5YXhN+9JInlghs/GwluEghmORfb5weny79R2M3x1X"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423108,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
      "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423108,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
      "balance": 69999999999999
    },
    {
      "account": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
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
    "from": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
    "meta": [
      "meta 1"
    ],
    "to": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
        "from": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
        "meta": [
          "meta 1"
        ],
        "to": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
        "meta": [
          "meta 1"
        ],
        "to": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
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
    "from": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
        "from": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
        "meta": [
          "meta 1"
        ],
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
    "from": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
    "meta": 17,
    "to": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
        "from": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
        "meta": 17,
        "to": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
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
    "from": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
    "meta": [
      "meta 1"
    ],
    "to": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjGCTVHHgfDoq2BLm+gmDDEVHn5EwSZdEDQMmvONklOUAqAtQgbuVEZJW5mi1gGDG0xeHNhSRhGbYUDWobIZfIC/T/hppwo=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
          "op": "OffChainTransfer",
          "to": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423107,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA+0Fn5lLT5B09mw2RJ0BTp4JpKrQ4GH38k7CFjPP4e6BRnbTrVzEpbixyaCKnRzXT+Etm619rDkCHk0+BfGuAEuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAKgLUIG7lRGSVuZotYBgxtMXhzYUkYRm2FA1qGyGXyAv09bpxf/"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423107,
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA+0Fn5lLT5B09mw2RJ0BTp4JpKrQ4GH38k7CFjPP4e6BRnbTrVzEpbixyaCKnRzXT+Etm619rDkCHk0+BfGuAEuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAKgLUIG7lRGSVuZotYBgxtMXhzYUkYRm2FA1qGyGXyAv09bpxf/",
      "updates": [
        {
          "amount": 1,
          "from": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
          "op": "OffChainTransfer",
          "to": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423106,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA+0Fn5lLT5B09mw2RJ0BTp4JpKrQ4GH38k7CFjPP4e6BRnbTrVzEpbixyaCKnRzXT+Etm619rDkCHk0+BfGuAEuECgk8P9tPi+S8sEsO35I/tprDViyIBGRdQcs3hoUMWRpAN6fHIQhKZ33XpkZk86d4cE9VbxVKJ4CgwwEljrOxMEuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAKgLUIG7lRGSVuZotYBgxtMXhzYUkYRm2FA1qGyGXyAv09LVwXA"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423106,
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "state": "tx_+NILAfiEuEA+0Fn5lLT5B09mw2RJ0BTp4JpKrQ4GH38k7CFjPP4e6BRnbTrVzEpbixyaCKnRzXT+Etm619rDkCHk0+BfGuAEuECgk8P9tPi+S8sEsO35I/tprDViyIBGRdQcs3hoUMWRpAN6fHIQhKZ33XpkZk86d4cE9VbxVKJ4CgwwEljrOxMEuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAKgLUIG7lRGSVuZotYBgxtMXhzYUkYRm2FA1qGyGXyAv09LVwXA"
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "state": "tx_+NILAfiEuEA+0Fn5lLT5B09mw2RJ0BTp4JpKrQ4GH38k7CFjPP4e6BRnbTrVzEpbixyaCKnRzXT+Etm619rDkCHk0+BfGuAEuECgk8P9tPi+S8sEsO35I/tprDViyIBGRdQcs3hoUMWRpAN6fHIQhKZ33XpkZk86d4cE9VbxVKJ4CgwwEljrOxMEuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAKgLUIG7lRGSVuZotYBgxtMXhzYUkYRm2FA1qGyGXyAv09LVwXA"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423105,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
      "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423105,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
      "balance": 69999999999998
    },
    {
      "account": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423104,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423104,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA+0Fn5lLT5B09mw2RJ0BTp4JpKrQ4GH38k7CFjPP4e6BRnbTrVzEpbixyaCKnRzXT+Etm619rDkCHk0+BfGuAEuECgk8P9tPi+S8sEsO35I/tprDViyIBGRdQcs3hoUMWRpAN6fHIQhKZ33XpkZk86d4cE9VbxVKJ4CgwwEljrOxMEuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAKgLUIG7lRGSVuZotYBgxtMXhzYUkYRm2FA1qGyGXyAv09LVwXA",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCqCRBCJUf6UearceRYSaOFJedS41WJfe3eptJ9mTkcoovKCgEAhiRhOcqAArDvQAGgQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM+LygoBAIY/qiUiX/4ceTw5"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423103,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
      "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423103,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
      "balance": 40000000000002
    },
    {
      "account": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
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
    "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
    "meta": [
      "meta 1"
    ],
    "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
        "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
        "meta": [
          "meta 1"
        ],
        "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
        "meta": [
          "meta 1"
        ],
        "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
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
    "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
        "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
        "meta": [
          "meta 1"
        ],
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
    "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
    "meta": 17,
    "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
        "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
        "meta": 17,
        "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
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
    "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
    "meta": [
      "meta 1"
    ],
    "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjGCTVHHgfDoq2BLm+gmDDEVHn5EwSZdEDQMmvONklOUA6DmMXh2ZGE5YXhN+9JInlghs/GwluEghmORfb5weny79cJfsYk=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
          "op": "OffChainTransfer",
          "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423102,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECJ1lkAi3CRfxaJjJkZ15QGNqyPqK20ie1y+FqNa5+b3j/FD/qqoPvVbPgQNEsxYdD92niIYMLSFNiWjfQxuBIIuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAOg5jF4dmRhOWF4TfvSSJ5YIbPxsJbhIIZjkX2+cHp8u/XgbUFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423102,
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "signed_tx": "tx_+JALAfhCuECJ1lkAi3CRfxaJjJkZ15QGNqyPqK20ie1y+FqNa5+b3j/FD/qqoPvVbPgQNEsxYdD92niIYMLSFNiWjfQxuBIIuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAOg5jF4dmRhOWF4TfvSSJ5YIbPxsJbhIIZjkX2+cHp8u/XgbUFG",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
          "op": "OffChainTransfer",
          "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423101,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAnNA5BSP87aAk7I65Id/IZFw9+Qad4X+gQv+9571EUrQvuLWr37T8GXsnRQDEIezjtrKwA+Bts3pex/2/P3IIBuECJ1lkAi3CRfxaJjJkZ15QGNqyPqK20ie1y+FqNa5+b3j/FD/qqoPvVbPgQNEsxYdD92niIYMLSFNiWjfQxuBIIuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAOg5jF4dmRhOWF4TfvSSJ5YIbPxsJbhIIZjkX2+cHp8u/Xr6ses"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423101,
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "state": "tx_+NILAfiEuEAnNA5BSP87aAk7I65Id/IZFw9+Qad4X+gQv+9571EUrQvuLWr37T8GXsnRQDEIezjtrKwA+Bts3pex/2/P3IIBuECJ1lkAi3CRfxaJjJkZ15QGNqyPqK20ie1y+FqNa5+b3j/FD/qqoPvVbPgQNEsxYdD92niIYMLSFNiWjfQxuBIIuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAOg5jF4dmRhOWF4TfvSSJ5YIbPxsJbhIIZjkX2+cHp8u/Xr6ses"
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "state": "tx_+NILAfiEuEAnNA5BSP87aAk7I65Id/IZFw9+Qad4X+gQv+9571EUrQvuLWr37T8GXsnRQDEIezjtrKwA+Bts3pex/2/P3IIBuECJ1lkAi3CRfxaJjJkZ15QGNqyPqK20ie1y+FqNa5+b3j/FD/qqoPvVbPgQNEsxYdD92niIYMLSFNiWjfQxuBIIuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAOg5jF4dmRhOWF4TfvSSJ5YIbPxsJbhIIZjkX2+cHp8u/Xr6ses"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423100,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
      "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423100,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
      "balance": 40000000000001
    },
    {
      "account": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423099,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423099,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAnNA5BSP87aAk7I65Id/IZFw9+Qad4X+gQv+9571EUrQvuLWr37T8GXsnRQDEIezjtrKwA+Bts3pex/2/P3IIBuECJ1lkAi3CRfxaJjJkZ15QGNqyPqK20ie1y+FqNa5+b3j/FD/qqoPvVbPgQNEsxYdD92niIYMLSFNiWjfQxuBIIuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAOg5jF4dmRhOWF4TfvSSJ5YIbPxsJbhIIZjkX2+cHp8u/Xr6ses",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCqCRBCJUf6UearceRYSaOFJedS41WJfe3eptJ9mTkcoovKCgEAhiRhOcqAAbDvQAGgQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM+LygoBAIY/qiUiX//gZUf7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423098,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
      "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423098,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
      "balance": 40000000000001
    },
    {
      "account": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
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
    "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
    "meta": [
      "meta 1"
    ],
    "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
        "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
        "meta": [
          "meta 1"
        ],
        "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
        "meta": [
          "meta 1"
        ],
        "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
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
    "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
        "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
        "meta": [
          "meta 1"
        ],
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
    "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
    "meta": 17,
    "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
        "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
        "meta": 17,
        "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
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
    "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
    "meta": [
      "meta 1"
    ],
    "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjGCTVHHgfDoq2BLm+gmDDEVHn5EwSZdEDQMmvONklOUBKAQ7TXOxjjtnNsz0HcpVXZqKYh7hxLNRQoG2hwEzOp5VO1f3sw=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
          "op": "OffChainTransfer",
          "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423097,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBZ8PBYXtcpsheY+He5YU6LWylkjaHY6HfhztGjwFyocFVRC67+itks5r6sYFrf2aEpLSP+0AVhbZXvLeR9Z0gCuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlASgEO01zsY47ZzbM9B3KVV2aimIe4cSzUUKBtocBMzqeVT4x9gh"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423097,
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBZ8PBYXtcpsheY+He5YU6LWylkjaHY6HfhztGjwFyocFVRC67+itks5r6sYFrf2aEpLSP+0AVhbZXvLeR9Z0gCuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlASgEO01zsY47ZzbM9B3KVV2aimIe4cSzUUKBtocBMzqeVT4x9gh",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
          "op": "OffChainTransfer",
          "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423096,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBZ8PBYXtcpsheY+He5YU6LWylkjaHY6HfhztGjwFyocFVRC67+itks5r6sYFrf2aEpLSP+0AVhbZXvLeR9Z0gCuECazMdSNvtfV8/HA2thTkc56EGkzrosH6Ic3zjWD3coTSk2xfx1jNY4dRu6uNfngRziEbJBp1BDCn6bipaVJ7YKuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlASgEO01zsY47ZzbM9B3KVV2aimIe4cSzUUKBtocBMzqeVSITmKY"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423096,
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "state": "tx_+NILAfiEuEBZ8PBYXtcpsheY+He5YU6LWylkjaHY6HfhztGjwFyocFVRC67+itks5r6sYFrf2aEpLSP+0AVhbZXvLeR9Z0gCuECazMdSNvtfV8/HA2thTkc56EGkzrosH6Ic3zjWD3coTSk2xfx1jNY4dRu6uNfngRziEbJBp1BDCn6bipaVJ7YKuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlASgEO01zsY47ZzbM9B3KVV2aimIe4cSzUUKBtocBMzqeVSITmKY"
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "state": "tx_+NILAfiEuEBZ8PBYXtcpsheY+He5YU6LWylkjaHY6HfhztGjwFyocFVRC67+itks5r6sYFrf2aEpLSP+0AVhbZXvLeR9Z0gCuECazMdSNvtfV8/HA2thTkc56EGkzrosH6Ic3zjWD3coTSk2xfx1jNY4dRu6uNfngRziEbJBp1BDCn6bipaVJ7YKuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlASgEO01zsY47ZzbM9B3KVV2aimIe4cSzUUKBtocBMzqeVSITmKY"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423095,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
      "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423095,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
      "balance": 40000000000000
    },
    {
      "account": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423094,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423094,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBZ8PBYXtcpsheY+He5YU6LWylkjaHY6HfhztGjwFyocFVRC67+itks5r6sYFrf2aEpLSP+0AVhbZXvLeR9Z0gCuECazMdSNvtfV8/HA2thTkc56EGkzrosH6Ic3zjWD3coTSk2xfx1jNY4dRu6uNfngRziEbJBp1BDCn6bipaVJ7YKuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlASgEO01zsY47ZzbM9B3KVV2aimIe4cSzUUKBtocBMzqeVSITmKY",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCqCRBCJUf6UearceRYSaOFJedS41WJfe3eptJ9mTkcoovKCgEAhiRhOcqAALDvQAGgQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM+LygoBAIY/qiUiYADdb3BO"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423093,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
      "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423093,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
      "balance": 70000000000000
    },
    {
      "account": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
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
    "from": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
    "meta": [
      "meta 1"
    ],
    "to": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
        "from": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
        "meta": [
          "meta 1"
        ],
        "to": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
        "meta": [
          "meta 1"
        ],
        "to": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
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
    "from": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
        "from": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
        "meta": [
          "meta 1"
        ],
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
    "from": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
    "meta": 17,
    "to": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
        "from": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
        "meta": 17,
        "to": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
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
    "from": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
    "meta": [
      "meta 1"
    ],
    "to": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjGCTVHHgfDoq2BLm+gmDDEVHn5EwSZdEDQMmvONklOUBaDmMXh2ZGE5YXhN+9JInlghs/GwluEghmORfb5weny79TphDgQ=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
          "op": "OffChainTransfer",
          "to": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423092,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECX2AmPHRUYnruqKRCwGUabilcjGYqdzwU2hIPXBUp4+afyW++uawIsCZpPTKY+Nh4fvJ0M8bzPqNmmDYRhRbwKuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAWg5jF4dmRhOWF4TfvSSJ5YIbPxsJbhIIZjkX2+cHp8u/Ws+RGH"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423092,
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "signed_tx": "tx_+JALAfhCuECX2AmPHRUYnruqKRCwGUabilcjGYqdzwU2hIPXBUp4+afyW++uawIsCZpPTKY+Nh4fvJ0M8bzPqNmmDYRhRbwKuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAWg5jF4dmRhOWF4TfvSSJ5YIbPxsJbhIIZjkX2+cHp8u/Ws+RGH",
      "updates": [
        {
          "amount": 1,
          "from": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
          "op": "OffChainTransfer",
          "to": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423091,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECX2AmPHRUYnruqKRCwGUabilcjGYqdzwU2hIPXBUp4+afyW++uawIsCZpPTKY+Nh4fvJ0M8bzPqNmmDYRhRbwKuECZYtBYjN3udvfx58oremtWt5kK8k3OjGz2D6FUkGhBxAsLQ2B96TV8BSuMCNtO1VhmyDcjD6kKYqswVyxyVkALuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAWg5jF4dmRhOWF4TfvSSJ5YIbPxsJbhIIZjkX2+cHp8u/X3E25W"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423091,
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "state": "tx_+NILAfiEuECX2AmPHRUYnruqKRCwGUabilcjGYqdzwU2hIPXBUp4+afyW++uawIsCZpPTKY+Nh4fvJ0M8bzPqNmmDYRhRbwKuECZYtBYjN3udvfx58oremtWt5kK8k3OjGz2D6FUkGhBxAsLQ2B96TV8BSuMCNtO1VhmyDcjD6kKYqswVyxyVkALuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAWg5jF4dmRhOWF4TfvSSJ5YIbPxsJbhIIZjkX2+cHp8u/X3E25W"
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "state": "tx_+NILAfiEuECX2AmPHRUYnruqKRCwGUabilcjGYqdzwU2hIPXBUp4+afyW++uawIsCZpPTKY+Nh4fvJ0M8bzPqNmmDYRhRbwKuECZYtBYjN3udvfx58oremtWt5kK8k3OjGz2D6FUkGhBxAsLQ2B96TV8BSuMCNtO1VhmyDcjD6kKYqswVyxyVkALuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAWg5jF4dmRhOWF4TfvSSJ5YIbPxsJbhIIZjkX2+cHp8u/X3E25W"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423090,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
      "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423090,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
      "balance": 69999999999999
    },
    {
      "account": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423089,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423089,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECX2AmPHRUYnruqKRCwGUabilcjGYqdzwU2hIPXBUp4+afyW++uawIsCZpPTKY+Nh4fvJ0M8bzPqNmmDYRhRbwKuECZYtBYjN3udvfx58oremtWt5kK8k3OjGz2D6FUkGhBxAsLQ2B96TV8BSuMCNtO1VhmyDcjD6kKYqswVyxyVkALuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAWg5jF4dmRhOWF4TfvSSJ5YIbPxsJbhIIZjkX2+cHp8u/X3E25W",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCqCRBCJUf6UearceRYSaOFJedS41WJfe3eptJ9mTkcoovKCgEAhiRhOcqAAbDvQAGgQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM+LygoBAIY/qiUiX//gZUf7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423088,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
      "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423088,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
      "balance": 40000000000001
    },
    {
      "account": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
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
    "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
    "meta": [
      "meta 1"
    ],
    "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
        "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
        "meta": [
          "meta 1"
        ],
        "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
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
    "meta": [
      "meta 1"
    ],
    "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
        "meta": [
          "meta 1"
        ],
        "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
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
    "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
    "meta": [
      "meta 1"
    ],
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
        "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
        "meta": [
          "meta 1"
        ],
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
    "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
    "meta": 17,
    "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
        "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
        "meta": 17,
        "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
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
    "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
    "meta": [
      "meta 1"
    ],
    "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjGCTVHHgfDoq2BLm+gmDDEVHn5EwSZdEDQMmvONklOUBqAQ7TXOxjjtnNsz0HcpVXZqKYh7hxLNRQoG2hwEzOp5VCYWCw8=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
          "op": "OffChainTransfer",
          "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423087,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAY+oGo3Asi88Pho5KEQvOlj9tNqjsv4f59Cbv2Go3yv9BUq0brZA1c8BQJ8bmAHkKz6IjKgeqO6z7Pd60YhY0KuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAagEO01zsY47ZzbM9B3KVV2aimIe4cSzUUKBtocBMzqeVQDJ8A3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423087,
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAY+oGo3Asi88Pho5KEQvOlj9tNqjsv4f59Cbv2Go3yv9BUq0brZA1c8BQJ8bmAHkKz6IjKgeqO6z7Pd60YhY0KuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAagEO01zsY47ZzbM9B3KVV2aimIe4cSzUUKBtocBMzqeVQDJ8A3",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
          "op": "OffChainTransfer",
          "to": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423086,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAHL2gBJOufi96guIMGovJOQhF3okBFR0+zEBhkr4idK1XCOXOWZVIxjwzbaXPzs390EyAX/l4e8bw+TGsM8X8PuEAY+oGo3Asi88Pho5KEQvOlj9tNqjsv4f59Cbv2Go3yv9BUq0brZA1c8BQJ8bmAHkKz6IjKgeqO6z7Pd60YhY0KuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAagEO01zsY47ZzbM9B3KVV2aimIe4cSzUUKBtocBMzqeVR2NA0N"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423086,
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "state": "tx_+NILAfiEuEAHL2gBJOufi96guIMGovJOQhF3okBFR0+zEBhkr4idK1XCOXOWZVIxjwzbaXPzs390EyAX/l4e8bw+TGsM8X8PuEAY+oGo3Asi88Pho5KEQvOlj9tNqjsv4f59Cbv2Go3yv9BUq0brZA1c8BQJ8bmAHkKz6IjKgeqO6z7Pd60YhY0KuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAagEO01zsY47ZzbM9B3KVV2aimIe4cSzUUKBtocBMzqeVR2NA0N"
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "state": "tx_+NILAfiEuEAHL2gBJOufi96guIMGovJOQhF3okBFR0+zEBhkr4idK1XCOXOWZVIxjwzbaXPzs390EyAX/l4e8bw+TGsM8X8PuEAY+oGo3Asi88Pho5KEQvOlj9tNqjsv4f59Cbv2Go3yv9BUq0brZA1c8BQJ8bmAHkKz6IjKgeqO6z7Pd60YhY0KuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAagEO01zsY47ZzbM9B3KVV2aimIe4cSzUUKBtocBMzqeVR2NA0N"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423085,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
      "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423085,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
      "balance": 40000000000000
    },
    {
      "account": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423084,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423084,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAHL2gBJOufi96guIMGovJOQhF3okBFR0+zEBhkr4idK1XCOXOWZVIxjwzbaXPzs390EyAX/l4e8bw+TGsM8X8PuEAY+oGo3Asi88Pho5KEQvOlj9tNqjsv4f59Cbv2Go3yv9BUq0brZA1c8BQJ8bmAHkKz6IjKgeqO6z7Pd60YhY0KuEj4RjkCoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlAagEO01zsY47ZzbM9B3KVV2aimIe4cSzUUKBtocBMzqeVR2NA0N",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCqCRBCJUf6UearceRYSaOFJedS41WJfe3eptJ9mTkcoovKCgEAhiRhOcqAALDvQAGgQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM+LygoBAIY/qiUiYADdb3BO"
  },
  "version": 1
}
```
