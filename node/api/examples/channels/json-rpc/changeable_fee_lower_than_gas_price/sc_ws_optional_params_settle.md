
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator
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
      "fsm_id": "ba_FB3AeSEHIkk8rTVJMtTmB8WyOla/JxMH1ukYWb/pio7pe060"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder
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
      "fsm_id": "ba_l/hMtWe5el7QiVlTvbKcDPz8KsJri9VXgB9aIHKsQ3Jpfr4C"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBkhm+8bM=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422317,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEB2yOznU3590c2HYBEXzf7DvpCRcFypF82gmEEo1XbNCErcJ5oWb0RrdckmcDOT71AGSZ7MrIv28tyyxERgGBIBuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgZJmY1hI"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422317,
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
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
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
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
    "data": {
      "fsm_id": "ba_l/hMtWe5el7QiVlTvbKcDPz8KsJri9VXgB9aIHKsQ3Jpfr4C",
      "signed_tx": "tx_+MwLAfhCuEB2yOznU3590c2HYBEXzf7DvpCRcFypF82gmEEo1XbNCErcJ5oWb0RrdckmcDOT71AGSZ7MrIv28tyyxERgGBIBuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgZJmY1hI",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422316,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhATRA4ggHCdNE4ZJet5QGX7MYNnRKYYsYW4DgSEgxKJL1C918wDAvVcaAFTx1wrlXOSvakVhaBGNUgI8R7dmQeCrhAdsjs51N+fdHNh2ARF83+w76QkXBcqRfNoJhBKNV2zQhK3CeaFm9Ea3XJJnAzk+9QBkmezKyL9vLcssREYBgSAbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GShBY6xg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
  "id": -576460752303422316,
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
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhATRA4ggHCdNE4ZJet5QGX7MYNnRKYYsYW4DgSEgxKJL1C918wDAvVcaAFTx1wrlXOSvakVhaBGNUgI8R7dmQeCrhAdsjs51N+fdHNh2ARF83+w76QkXBcqRfNoJhBKNV2zQhK3CeaFm9Ea3XJJnAzk+9QBkmezKyL9vLcssREYBgSAbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GShBY6xg==",
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
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_FB3AeSEHIkk8rTVJMtTmB8WyOla/JxMH1ukYWb/pio7pe060"
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
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhATRA4ggHCdNE4ZJet5QGX7MYNnRKYYsYW4DgSEgxKJL1C918wDAvVcaAFTx1wrlXOSvakVhaBGNUgI8R7dmQeCrhAdsjs51N+fdHNh2ARF83+w76QkXBcqRfNoJhBKNV2zQhK3CeaFm9Ea3XJJnAzk+9QBkmezKyL9vLcssREYBgSAbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GShBY6xg==",
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
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhATRA4ggHCdNE4ZJet5QGX7MYNnRKYYsYW4DgSEgxKJL1C918wDAvVcaAFTx1wrlXOSvakVhaBGNUgI8R7dmQeCrhAdsjs51N+fdHNh2ARF83+w76QkXBcqRfNoJhBKNV2zQhK3CeaFm9Ea3XJJnAzk+9QBkmezKyL9vLcssREYBgSAbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GShBY6xg==",
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
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhATRA4ggHCdNE4ZJet5QGX7MYNnRKYYsYW4DgSEgxKJL1C918wDAvVcaAFTx1wrlXOSvakVhaBGNUgI8R7dmQeCrhAdsjs51N+fdHNh2ARF83+w76QkXBcqRfNoJhBKNV2zQhK3CeaFm9Ea3XJJnAzk+9QBkmezKyL9vLcssREYBgSAbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GShBY6xg==",
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
    "data": {
      "message": {
        "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
    "data": {
      "message": {
        "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello back",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422315,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
  "id": -576460752303422315,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999999
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
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
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
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
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
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
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
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
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
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
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
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
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
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
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
    "data": {
      "state": "tx_+QEOCwH4hLhATRA4ggHCdNE4ZJet5QGX7MYNnRKYYsYW4DgSEgxKJL1C918wDAvVcaAFTx1wrlXOSvakVhaBGNUgI8R7dmQeCrhAdsjs51N+fdHNh2ARF83+w76QkXBcqRfNoJhBKNV2zQhK3CeaFm9Ea3XJJnAzk+9QBkmezKyL9vLcssREYBgSAbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GShBY6xg=="
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
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
    "data": {
      "state": "tx_+QEOCwH4hLhATRA4ggHCdNE4ZJet5QGX7MYNnRKYYsYW4DgSEgxKJL1C918wDAvVcaAFTx1wrlXOSvakVhaBGNUgI8R7dmQeCrhAdsjs51N+fdHNh2ARF83+w76QkXBcqRfNoJhBKNV2zQhK3CeaFm9Ea3XJJnAzk+9QBkmezKyL9vLcssREYBgSAbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GShBY6xg=="
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
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
    "data": {
      "signed_tx": "tx_+QGpCwHAuQGj+QGgNgGhBg9BGSA8qtuCOllY28UTwIWemqYYmMND2dZWYWfJo55SoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oC5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGFUOUmEgAgZOBvvTh",
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
    "signed_tx": "tx_+QHsCwH4QrhA1/yOXPeMRHlsjTSR6K4witkZQu/b8a0DXA11IMqFNaq2TWa038pZVnI5rdqNzGonxZ29s3NjLQD8Hnxq8b2vCbkBo/kBoDYBoQYPQRkgPKrbgjpZWNvFE8CFnpqmGJjDQ9nWVmFnyaOeUqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhVDlJhIAIGT1ZjVIQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHsCwH4QrhA1/yOXPeMRHlsjTSR6K4witkZQu/b8a0DXA11IMqFNaq2TWa038pZVnI5rdqNzGonxZ29s3NjLQD8Hnxq8b2vCbkBo/kBoDYBoQYPQRkgPKrbgjpZWNvFE8CFnpqmGJjDQ9nWVmFnyaOeUqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhVDlJhIAIGT1ZjVIQ==",
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
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
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
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHsCwH4QrhA1/yOXPeMRHlsjTSR6K4witkZQu/b8a0DXA11IMqFNaq2TWa038pZVnI5rdqNzGonxZ29s3NjLQD8Hnxq8b2vCbkBo/kBoDYBoQYPQRkgPKrbgjpZWNvFE8CFnpqmGJjDQ9nWVmFnyaOeUqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhVDlJhIAIGT1ZjVIQ==",
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
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
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
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {
    "fee": 1,
    "gas_price": 1000001234
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBg9BGSA8qtuCOllY28UTwIWemqYYmMND2dZWYWfJo55SoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/+GJGE5yoABAIYPXte9X0g+j3JmPg==",
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
    "signed_tx": "tx_+KcLAfhCuEA9zimCynBw/Bbzs/xQpr0I6cs3g9tf98srtqhd/kZYI/sCpCKbn83pZUTWV5/7AM2CzXfrHr3UJ4YK4nUq8zUAuF/4XTgBoQYPQRkgPKrbgjpZWNvFE8CFnpqmGJjDQ9nWVmFnyaOeUqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17XvV9IPqqKwdE="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEA9zimCynBw/Bbzs/xQpr0I6cs3g9tf98srtqhd/kZYI/sCpCKbn83pZUTWV5/7AM2CzXfrHr3UJ4YK4nUq8zUAuF/4XTgBoQYPQRkgPKrbgjpZWNvFE8CFnpqmGJjDQ9nWVmFnyaOeUqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17XvV9IPqqKwdE=",
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
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEA9zimCynBw/Bbzs/xQpr0I6cs3g9tf98srtqhd/kZYI/sCpCKbn83pZUTWV5/7AM2CzXfrHr3UJ4YK4nUq8zUAuF/4XTgBoQYPQRkgPKrbgjpZWNvFE8CFnpqmGJjDQ9nWVmFnyaOeUqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl//hiRhOcqAAQCGD17XvV9IPqqKwdE=",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
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
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
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
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
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
    "channel_id": "ch_7ieio9zMrPAxWp5mLEZcRbZJaX6SXxr9WQ21v4MeCiRaDYha7",
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
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator
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
      "fsm_id": "ba_x3jce+uiqzSE7wdINrynbVWTlRsw7wabAyyijT1S57+zv2Ks"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder
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
      "fsm_id": "ba_QY9jaxU/1gXXV+5ZOkA3CmzCC5mqQ/m7L0FNzwlgQyTkkNNz"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBlFMyxg0=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422314,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEBdPqIyRmr+NBYkUA5l0MpN9yRfuxgKN6fzb9mz1J4Ectqjb0kqWv1n74udKQxbuDLNc/co8Y9bkz8FlMPpgjkCuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgZRhZurN"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422314,
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
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
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
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
    "data": {
      "fsm_id": "ba_QY9jaxU/1gXXV+5ZOkA3CmzCC5mqQ/m7L0FNzwlgQyTkkNNz",
      "signed_tx": "tx_+MwLAfhCuEBdPqIyRmr+NBYkUA5l0MpN9yRfuxgKN6fzb9mz1J4Ectqjb0kqWv1n74udKQxbuDLNc/co8Y9bkz8FlMPpgjkCuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgZRhZurN",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422313,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAXT6iMkZq/jQWJFAOZdDKTfckX7sYCjen82/Zs9SeBHLao29JKlr9Z++LnSkMW7gyzXP3KPGPW5M/BZTD6YI5ArhAYICgAp1nKUzocsmWmVlpBwfIQpRn+xslVsaKISJi+G4uyYmpUyBU6OSyaPrhKTwD8mtDed2IsKlpKUH86oy0AriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GUJkH02A=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
  "id": -576460752303422313,
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
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAXT6iMkZq/jQWJFAOZdDKTfckX7sYCjen82/Zs9SeBHLao29JKlr9Z++LnSkMW7gyzXP3KPGPW5M/BZTD6YI5ArhAYICgAp1nKUzocsmWmVlpBwfIQpRn+xslVsaKISJi+G4uyYmpUyBU6OSyaPrhKTwD8mtDed2IsKlpKUH86oy0AriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GUJkH02A==",
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
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_x3jce+uiqzSE7wdINrynbVWTlRsw7wabAyyijT1S57+zv2Ks"
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
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAXT6iMkZq/jQWJFAOZdDKTfckX7sYCjen82/Zs9SeBHLao29JKlr9Z++LnSkMW7gyzXP3KPGPW5M/BZTD6YI5ArhAYICgAp1nKUzocsmWmVlpBwfIQpRn+xslVsaKISJi+G4uyYmpUyBU6OSyaPrhKTwD8mtDed2IsKlpKUH86oy0AriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GUJkH02A==",
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
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAXT6iMkZq/jQWJFAOZdDKTfckX7sYCjen82/Zs9SeBHLao29JKlr9Z++LnSkMW7gyzXP3KPGPW5M/BZTD6YI5ArhAYICgAp1nKUzocsmWmVlpBwfIQpRn+xslVsaKISJi+G4uyYmpUyBU6OSyaPrhKTwD8mtDed2IsKlpKUH86oy0AriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GUJkH02A==",
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
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAXT6iMkZq/jQWJFAOZdDKTfckX7sYCjen82/Zs9SeBHLao29JKlr9Z++LnSkMW7gyzXP3KPGPW5M/BZTD6YI5ArhAYICgAp1nKUzocsmWmVlpBwfIQpRn+xslVsaKISJi+G4uyYmpUyBU6OSyaPrhKTwD8mtDed2IsKlpKUH86oy0AriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GUJkH02A==",
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
    "data": {
      "message": {
        "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
    "data": {
      "message": {
        "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello back",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422312,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
  "id": -576460752303422312,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999999
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
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
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
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
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
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
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
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
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
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
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
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
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
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
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
    "data": {
      "state": "tx_+QEOCwH4hLhAXT6iMkZq/jQWJFAOZdDKTfckX7sYCjen82/Zs9SeBHLao29JKlr9Z++LnSkMW7gyzXP3KPGPW5M/BZTD6YI5ArhAYICgAp1nKUzocsmWmVlpBwfIQpRn+xslVsaKISJi+G4uyYmpUyBU6OSyaPrhKTwD8mtDed2IsKlpKUH86oy0AriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GUJkH02A=="
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
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
    "data": {
      "state": "tx_+QEOCwH4hLhAXT6iMkZq/jQWJFAOZdDKTfckX7sYCjen82/Zs9SeBHLao29JKlr9Z++LnSkMW7gyzXP3KPGPW5M/BZTD6YI5ArhAYICgAp1nKUzocsmWmVlpBwfIQpRn+xslVsaKISJi+G4uyYmpUyBU6OSyaPrhKTwD8mtDed2IsKlpKUH86oy0AriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GUJkH02A=="
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
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
    "data": {
      "signed_tx": "tx_+QGpCwHAuQGj+QGgNgGhBhsjl5zEMMeopVFQL4EqeL4O3etqR/q1Vh4E/QBykpbDoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oC5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGFUOUmEgAgZVP2gW1",
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
    "signed_tx": "tx_+QHsCwH4QrhAV1jWkeeRmLlLeZtw+PRxJC3ICwP8grGDzZiK9NzLdYQazHohbOijpWz06zJ6M0e6pSvWA1YGqriUHzYb45MEBbkBo/kBoDYBoQYbI5ecxDDHqKVRUC+BKni+Dt3rakf6tVYeBP0AcpKWw6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhVDlJhIAIGVu+0ORA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHsCwH4QrhAV1jWkeeRmLlLeZtw+PRxJC3ICwP8grGDzZiK9NzLdYQazHohbOijpWz06zJ6M0e6pSvWA1YGqriUHzYb45MEBbkBo/kBoDYBoQYbI5ecxDDHqKVRUC+BKni+Dt3rakf6tVYeBP0AcpKWw6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhVDlJhIAIGVu+0ORA==",
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
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
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
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHsCwH4QrhAV1jWkeeRmLlLeZtw+PRxJC3ICwP8grGDzZiK9NzLdYQazHohbOijpWz06zJ6M0e6pSvWA1YGqriUHzYb45MEBbkBo/kBoDYBoQYbI5ecxDDHqKVRUC+BKni+Dt3rakf6tVYeBP0AcpKWw6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhVDlJhIAIGVu+0ORA==",
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
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
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
  "params": {
    "fee": 1,
    "gas_price": 1000001234
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheOAGhBhsjl5zEMMeopVFQL4EqeL4O3etqR/q1Vh4E/QBykpbDoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiX/+GJGE5yoABAIYPY3/Vh7CBlgDrljA=",
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
    "signed_tx": "tx_+KgLAfhCuEDqgLO6c6rsMFgwyLV3hPl3ZQ7d0roN1ojepjaQCKSjiSMr6Lyy10rb8dKmNdfxPMrutnw+wCRisAuc7Xe9VpQKuGD4XjgBoQYbI5ecxDDHqKVRUC+BKni+Dt3rakf6tVYeBP0AcpKWw6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olIl//hiRhOcqAAQCGD2N/1YewgZYjuerC"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KgLAfhCuEDqgLO6c6rsMFgwyLV3hPl3ZQ7d0roN1ojepjaQCKSjiSMr6Lyy10rb8dKmNdfxPMrutnw+wCRisAuc7Xe9VpQKuGD4XjgBoQYbI5ecxDDHqKVRUC+BKni+Dt3rakf6tVYeBP0AcpKWw6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olIl//hiRhOcqAAQCGD2N/1YewgZYjuerC",
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
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KgLAfhCuEDqgLO6c6rsMFgwyLV3hPl3ZQ7d0roN1ojepjaQCKSjiSMr6Lyy10rb8dKmNdfxPMrutnw+wCRisAuc7Xe9VpQKuGD4XjgBoQYbI5ecxDDHqKVRUC+BKni+Dt3rakf6tVYeBP0AcpKWw6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olIl//hiRhOcqAAQCGD2N/1YewgZYjuerC",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
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
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
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
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
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
    "channel_id": "ch_CxEMEVUJhW3tXUTAR98BQD7fHTGZs9aZwetSbwZzzEiGX4fad",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
