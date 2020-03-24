
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD&keep_running=false&lock_period=10&port=12515&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY&role=initiator
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
      "fsm_id": "ba_Qsc+/+LL8hl5BFkzfdB5Vr8lSvEVkejPbIReDEweejia4/8Z"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD&keep_running=false&lock_period=10&port=12515&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY&role=responder
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
      "fsm_id": "ba_/vjE72pzJGM/IYnObfqCZhiQ+JOGTtp3In7FjDWf+La+f5cq"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAVGDQH45qjG0a+MP5OsbdT4/IqPUrkpJcJExruIzsYNwhj+qJSJgAKEBwt4y9fTVZcmds2McB0gMAAZwlzuzQV1Kdngyzne4nkyGJGE5yoAAAgoAhhAGeddIAMCgW+RiwFjCPsDr7r6unzC9D1F7YHL3GA4SosyqMaSVA54BPHU9fQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421219,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECyPm2twZmQU88pkMg6c7GLAV/1fcbvJsB1rsI0a7FMHSgUm1HaKFJwbpLIJbsjsWdZPzqS0LBnIB+5l53fQ6cIuIP4gTIBoQFRg0B+OaoxtGvjD+TrG3U+PyKj1K5KSXCRMa7iM7GDcIY/qiUiYAChAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MhiRhOcqAAAIKAIYQBnnXSADAoFvkYsBYwj7A6+6+rp8wvQ9Re2By9xgOEqLMqjGklQOeAdKnSCU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421219,
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "fsm_id": "ba_/vjE72pzJGM/IYnObfqCZhiQ+JOGTtp3In7FjDWf+La+f5cq",
      "signed_tx": "tx_+MsLAfhCuECyPm2twZmQU88pkMg6c7GLAV/1fcbvJsB1rsI0a7FMHSgUm1HaKFJwbpLIJbsjsWdZPzqS0LBnIB+5l53fQ6cIuIP4gTIBoQFRg0B+OaoxtGvjD+TrG3U+PyKj1K5KSXCRMa7iM7GDcIY/qiUiYAChAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MhiRhOcqAAAIKAIYQBnnXSADAoFvkYsBYwj7A6+6+rp8wvQ9Re2By9xgOEqLMqjGklQOeAdKnSCU=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421218,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEZCwHAuQET+QEQUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAsj5trcGZkFPPKZDIOnOxiwFf9X3G7ybAda7CNGuxTB0oFJtR2ihScG6SyCW7I7FnWT86ktCwZyAfuZed30OnCLiD+IEyAaEBUYNAfjmqMbRr4w/k6xt1Pj8io9SuSklwkTGu4jOxg3CGP6olImAAoQHC3jL19NVlyZ2zYxwHSAwABnCXO7NBXUp2eDLOd7ieTIYkYTnKgAACCgCGEAZ510gAwKBb5GLAWMI+wOvuvq6fML0PUXtgcvcYDhKizKoxpJUDngGiyz2m"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421218,
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAsj5trcGZkFPPKZDIOnOxiwFf9X3G7ybAda7CNGuxTB0oFJtR2ihScG6SyCW7I7FnWT86ktCwZyAfuZed30OnCLiD+IEyAaEBUYNAfjmqMbRr4w/k6xt1Pj8io9SuSklwkTGu4jOxg3CGP6olImAAoQHC3jL19NVlyZ2zYxwHSAwABnCXO7NBXUp2eDLOd7ieTIYkYTnKgAACCgCGEAZ510gAwKBb5GLAWMI+wOvuvq6fML0PUXtgcvcYDhKizKoxpJUDngGiyz2m",
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_Qsc+/+LL8hl5BFkzfdB5Vr8lSvEVkejPbIReDEweejia4/8Z"
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAsj5trcGZkFPPKZDIOnOxiwFf9X3G7ybAda7CNGuxTB0oFJtR2ihScG6SyCW7I7FnWT86ktCwZyAfuZed30OnCLiD+IEyAaEBUYNAfjmqMbRr4w/k6xt1Pj8io9SuSklwkTGu4jOxg3CGP6olImAAoQHC3jL19NVlyZ2zYxwHSAwABnCXO7NBXUp2eDLOd7ieTIYkYTnKgAACCgCGEAZ510gAwKBb5GLAWMI+wOvuvq6fML0PUXtgcvcYDhKizKoxpJUDngGiyz2m",
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAsj5trcGZkFPPKZDIOnOxiwFf9X3G7ybAda7CNGuxTB0oFJtR2ihScG6SyCW7I7FnWT86ktCwZyAfuZed30OnCLiD+IEyAaEBUYNAfjmqMbRr4w/k6xt1Pj8io9SuSklwkTGu4jOxg3CGP6olImAAoQHC3jL19NVlyZ2zYxwHSAwABnCXO7NBXUp2eDLOd7ieTIYkYTnKgAACCgCGEAZ510gAwKBb5GLAWMI+wOvuvq6fML0PUXtgcvcYDhKizKoxpJUDngGiyz2m",
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAsj5trcGZkFPPKZDIOnOxiwFf9X3G7ybAda7CNGuxTB0oFJtR2ihScG6SyCW7I7FnWT86ktCwZyAfuZed30OnCLiD+IEyAaEBUYNAfjmqMbRr4w/k6xt1Pj8io9SuSklwkTGu4jOxg3CGP6olImAAoQHC3jL19NVlyZ2zYxwHSAwABnCXO7NBXUp2eDLOd7ieTIYkYTnKgAACCgCGEAZ510gAwKBb5GLAWMI+wOvuvq6fML0PUXtgcvcYDhKizKoxpJUDngGiyz2m",
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
    "to": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "message": {
        "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
        "from": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
        "info": "Hello",
        "to": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
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
    "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "message": {
        "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
        "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
        "info": "Hello back",
        "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421217,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
      "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421217,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
      "balance": 69999999999999
    },
    {
      "account": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "state": "tx_+QEZCwHAuQET+QEQUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAsj5trcGZkFPPKZDIOnOxiwFf9X3G7ybAda7CNGuxTB0oFJtR2ihScG6SyCW7I7FnWT86ktCwZyAfuZed30OnCLiD+IEyAaEBUYNAfjmqMbRr4w/k6xt1Pj8io9SuSklwkTGu4jOxg3CGP6olImAAoQHC3jL19NVlyZ2zYxwHSAwABnCXO7NBXUp2eDLOd7ieTIYkYTnKgAACCgCGEAZ510gAwKBb5GLAWMI+wOvuvq6fML0PUXtgcvcYDhKizKoxpJUDngGiyz2m"
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "state": "tx_+QEZCwHAuQET+QEQUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAsj5trcGZkFPPKZDIOnOxiwFf9X3G7ybAda7CNGuxTB0oFJtR2ihScG6SyCW7I7FnWT86ktCwZyAfuZed30OnCLiD+IEyAaEBUYNAfjmqMbRr4w/k6xt1Pj8io9SuSklwkTGu4jOxg3CGP6olImAAoQHC3jL19NVlyZ2zYxwHSAwABnCXO7NBXUp2eDLOd7ieTIYkYTnKgAACCgCGEAZ510gAwKBb5GLAWMI+wOvuvq6fML0PUXtgcvcYDhKizKoxpJUDngGiyz2m"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421216,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
      "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421216,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
      "balance": 69999999999999
    },
    {
      "account": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
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
    "from": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
    "to": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
        "from": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
        "to": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
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
    "to": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
        "to": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
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
    "from": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
        "from": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
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
    "from": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
    "meta": 17,
    "to": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
        "from": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
        "meta": 17,
        "to": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
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
    "from": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
    "to": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnjoWjIcGeRfGw3iF7DpVh1CtU5BJnxNjwKGHc+h50VZAqB0BKLzjP0XCmuAzkUDR6w1/JVMJ4ncMBfcYwoPXmwL+kfpw7M=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
          "op": "OffChainTransfer",
          "to": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
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
  "id": -576460752303421215,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDYRySz61x4PYijysTEkudzzwMBw1Edug7k5gw0D7EHQOZZZoLAu1iCl/zdOhU5wVuTro9Npi+4XK61YkSMKr4NuEj4RjkCoQZ46FoyHBnkXxsN4hew6VYdQrVOQSZ8TY8Chh3PoedFWQKgdASi84z9FwprgM5FA0esNfyVTCeJ3DAX3GMKD15sC/rKltJf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421215,
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDYRySz61x4PYijysTEkudzzwMBw1Edug7k5gw0D7EHQOZZZoLAu1iCl/zdOhU5wVuTro9Npi+4XK61YkSMKr4NuEj4RjkCoQZ46FoyHBnkXxsN4hew6VYdQrVOQSZ8TY8Chh3PoedFWQKgdASi84z9FwprgM5FA0esNfyVTCeJ3DAX3GMKD15sC/rKltJf",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
          "op": "OffChainTransfer",
          "to": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
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
  "id": -576460752303421214,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA2Ecks+tceD2Io8rExJLnc88DAcNRHboO5OYMNA+xB0DmWWaCwLtYgpf83ToVOcFbk66PTaYvuFyutWJEjCq+DbhI+EY5AqEGeOhaMhwZ5F8bDeIXsOlWHUK1TkEmfE2PAoYdz6HnRVkCoHQEovOM/RcKa4DORQNHrDX8lUwnidwwF9xjCg9ebAv6cT8Bzw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421214,
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA2Ecks+tceD2Io8rExJLnc88DAcNRHboO5OYMNA+xB0DmWWaCwLtYgpf83ToVOcFbk66PTaYvuFyutWJEjCq+DbhI+EY5AqEGeOhaMhwZ5F8bDeIXsOlWHUK1TkEmfE2PAoYdz6HnRVkCoHQEovOM/RcKa4DORQNHrDX8lUwnidwwF9xjCg9ebAv6cT8Bzw=="
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA2Ecks+tceD2Io8rExJLnc88DAcNRHboO5OYMNA+xB0DmWWaCwLtYgpf83ToVOcFbk66PTaYvuFyutWJEjCq+DbhI+EY5AqEGeOhaMhwZ5F8bDeIXsOlWHUK1TkEmfE2PAoYdz6HnRVkCoHQEovOM/RcKa4DORQNHrDX8lUwnidwwF9xjCg9ebAv6cT8Bzw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421213,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
      "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421213,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
      "balance": 69999999999998
    },
    {
      "account": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421212,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421212,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA2Ecks+tceD2Io8rExJLnc88DAcNRHboO5OYMNA+xB0DmWWaCwLtYgpf83ToVOcFbk66PTaYvuFyutWJEjCq+DbhI+EY5AqEGeOhaMhwZ5F8bDeIXsOlWHUK1TkEmfE2PAoYdz6HnRVkCoHQEovOM/RcKa4DORQNHrDX8lUwnidwwF9xjCg9ebAv6cT8Bzw==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDC3jL19NVlyZ2zYxwHSAwABnCXO7NBXUp2eDLOd7ieTIvKCgEAhiRhOcqAArDvQAGgUYNAfjmqMbRr4w/k6xt1Pj8io9SuSklwkTGu4jOxg3CLygoBAIY/qiUiX/7jbGU9"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421211,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
      "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421211,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
      "balance": 40000000000002
    },
    {
      "account": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
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
    "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
    "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
        "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
        "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
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
    "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
        "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
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
    "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
        "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
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
    "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
    "meta": 17,
    "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
        "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
        "meta": 17,
        "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
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
    "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
    "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnjoWjIcGeRfGw3iF7DpVh1CtU5BJnxNjwKGHc+h50VZA6Bb5GLAWMI+wOvuvq6fML0PUXtgcvcYDhKizKoxpJUDnqG7ASM=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
          "op": "OffChainTransfer",
          "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
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
  "id": -576460752303421210,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZ46FoyHBnkXxsN4hew6VYdQrVOQSZ8TY8Chh3PoedFWQOgW+RiwFjCPsDr7r6unzC9D1F7YHL3GA4SosyqMaSVA55IsYFp"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421210,
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZ46FoyHBnkXxsN4hew6VYdQrVOQSZ8TY8Chh3PoedFWQOgW+RiwFjCPsDr7r6unzC9D1F7YHL3GA4SosyqMaSVA55IsYFp",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
          "op": "OffChainTransfer",
          "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
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
  "id": -576460752303421209,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhANTYALjVcAukq1YTxrTVWqsEECnQJcy5v1aW94BdGDy40PyA7GBfy3bDLH5igREkZgC0T2vwM4YDPiTKeSBkOB7hI+EY5AqEGeOhaMhwZ5F8bDeIXsOlWHUK1TkEmfE2PAoYdz6HnRVkDoFvkYsBYwj7A6+6+rp8wvQ9Re2By9xgOEqLMqjGklQOe1L2Zmg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421209,
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhANTYALjVcAukq1YTxrTVWqsEECnQJcy5v1aW94BdGDy40PyA7GBfy3bDLH5igREkZgC0T2vwM4YDPiTKeSBkOB7hI+EY5AqEGeOhaMhwZ5F8bDeIXsOlWHUK1TkEmfE2PAoYdz6HnRVkDoFvkYsBYwj7A6+6+rp8wvQ9Re2By9xgOEqLMqjGklQOe1L2Zmg=="
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhANTYALjVcAukq1YTxrTVWqsEECnQJcy5v1aW94BdGDy40PyA7GBfy3bDLH5igREkZgC0T2vwM4YDPiTKeSBkOB7hI+EY5AqEGeOhaMhwZ5F8bDeIXsOlWHUK1TkEmfE2PAoYdz6HnRVkDoFvkYsBYwj7A6+6+rp8wvQ9Re2By9xgOEqLMqjGklQOe1L2Zmg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421208,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
      "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421208,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
      "balance": 40000000000001
    },
    {
      "account": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421207,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421207,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhANTYALjVcAukq1YTxrTVWqsEECnQJcy5v1aW94BdGDy40PyA7GBfy3bDLH5igREkZgC0T2vwM4YDPiTKeSBkOB7hI+EY5AqEGeOhaMhwZ5F8bDeIXsOlWHUK1TkEmfE2PAoYdz6HnRVkDoFvkYsBYwj7A6+6+rp8wvQ9Re2By9xgOEqLMqjGklQOe1L2Zmg==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDC3jL19NVlyZ2zYxwHSAwABnCXO7NBXUp2eDLOd7ieTIvKCgEAhiRhOcqAAbDvQAGgUYNAfjmqMbRr4w/k6xt1Pj8io9SuSklwkTGu4jOxg3CLygoBAIY/qiUiX/+lpPcm"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421206,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
      "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421206,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
      "balance": 40000000000001
    },
    {
      "account": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
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
    "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
    "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
        "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
        "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
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
    "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
        "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
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
    "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
        "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
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
    "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
    "meta": 17,
    "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
        "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
        "meta": 17,
        "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
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
    "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
    "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnjoWjIcGeRfGw3iF7DpVh1CtU5BJnxNjwKGHc+h50VZBKDYQv83afMuLFCUmCa4ClyCrDzBFDVhnKR6kiR7wg4F0YIez/M=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
          "op": "OffChainTransfer",
          "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
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
  "id": -576460752303421205,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZ46FoyHBnkXxsN4hew6VYdQrVOQSZ8TY8Chh3PoedFWQSg2EL/N2nzLixQlJgmuApcgqw8wRQ1YZykepIke8IOBdFblVDp"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421205,
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZ46FoyHBnkXxsN4hew6VYdQrVOQSZ8TY8Chh3PoedFWQSg2EL/N2nzLixQlJgmuApcgqw8wRQ1YZykepIke8IOBdFblVDp",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
          "op": "OffChainTransfer",
          "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
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
  "id": -576460752303421204,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAsq+Omn/4QR86jlAJ9ae1qE3QEon0J/A6aAXfoxfP3iV+fmc+fB99geQco1MvH6xO9ytj8FqdqFj+idaGAsaODrhI+EY5AqEGeOhaMhwZ5F8bDeIXsOlWHUK1TkEmfE2PAoYdz6HnRVkEoNhC/zdp8y4sUJSYJrgKXIKsPMEUNWGcpHqSJHvCDgXR0P7+VA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421204,
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAsq+Omn/4QR86jlAJ9ae1qE3QEon0J/A6aAXfoxfP3iV+fmc+fB99geQco1MvH6xO9ytj8FqdqFj+idaGAsaODrhI+EY5AqEGeOhaMhwZ5F8bDeIXsOlWHUK1TkEmfE2PAoYdz6HnRVkEoNhC/zdp8y4sUJSYJrgKXIKsPMEUNWGcpHqSJHvCDgXR0P7+VA=="
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAsq+Omn/4QR86jlAJ9ae1qE3QEon0J/A6aAXfoxfP3iV+fmc+fB99geQco1MvH6xO9ytj8FqdqFj+idaGAsaODrhI+EY5AqEGeOhaMhwZ5F8bDeIXsOlWHUK1TkEmfE2PAoYdz6HnRVkEoNhC/zdp8y4sUJSYJrgKXIKsPMEUNWGcpHqSJHvCDgXR0P7+VA=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421203,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
      "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421203,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
      "balance": 40000000000000
    },
    {
      "account": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421202,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421202,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAsq+Omn/4QR86jlAJ9ae1qE3QEon0J/A6aAXfoxfP3iV+fmc+fB99geQco1MvH6xO9ytj8FqdqFj+idaGAsaODrhI+EY5AqEGeOhaMhwZ5F8bDeIXsOlWHUK1TkEmfE2PAoYdz6HnRVkEoNhC/zdp8y4sUJSYJrgKXIKsPMEUNWGcpHqSJHvCDgXR0P7+VA==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDC3jL19NVlyZ2zYxwHSAwABnCXO7NBXUp2eDLOd7ieTIvKCgEAhiRhOcqAALDvQAGgUYNAfjmqMbRr4w/k6xt1Pj8io9SuSklwkTGu4jOxg3CLygoBAIY/qiUiYADLzkqw"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421201,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
      "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421201,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
      "balance": 70000000000000
    },
    {
      "account": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
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
    "from": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
    "to": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
        "from": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
        "to": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
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
    "to": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
        "to": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
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
    "from": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
        "from": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
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
    "from": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
    "meta": 17,
    "to": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
        "from": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
        "meta": 17,
        "to": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
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
    "from": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
    "to": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnjoWjIcGeRfGw3iF7DpVh1CtU5BJnxNjwKGHc+h50VZBaBb5GLAWMI+wOvuvq6fML0PUXtgcvcYDhKizKoxpJUDnlNog9M=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
          "op": "OffChainTransfer",
          "to": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
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
  "id": -576460752303421200,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDQ/zO5l2fXR0WpmDnhoaISamImTD051ACVwy3HpOVQvj7Ufr7AmTJLp7Yx/t09/SSnZ+rSt3siSPplYlwxoKIEuEj4RjkCoQZ46FoyHBnkXxsN4hew6VYdQrVOQSZ8TY8Chh3PoedFWQWgW+RiwFjCPsDr7r6unzC9D1F7YHL3GA4SosyqMaSVA542txWw"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421200,
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDQ/zO5l2fXR0WpmDnhoaISamImTD051ACVwy3HpOVQvj7Ufr7AmTJLp7Yx/t09/SSnZ+rSt3siSPplYlwxoKIEuEj4RjkCoQZ46FoyHBnkXxsN4hew6VYdQrVOQSZ8TY8Chh3PoedFWQWgW+RiwFjCPsDr7r6unzC9D1F7YHL3GA4SosyqMaSVA542txWw",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
          "op": "OffChainTransfer",
          "to": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
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
  "id": -576460752303421199,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA0P8zuZdn10dFqZg54aGiEmpiJkw9OdQAlcMtx6TlUL4+1H6+wJkyS6e2Mf7dPf0kp2fq0rd7Ikj6ZWJcMaCiBLhI+EY5AqEGeOhaMhwZ5F8bDeIXsOlWHUK1TkEmfE2PAoYdz6HnRVkFoFvkYsBYwj7A6+6+rp8wvQ9Re2By9xgOEqLMqjGklQOe0wZ0/Q=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421199,
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA0P8zuZdn10dFqZg54aGiEmpiJkw9OdQAlcMtx6TlUL4+1H6+wJkyS6e2Mf7dPf0kp2fq0rd7Ikj6ZWJcMaCiBLhI+EY5AqEGeOhaMhwZ5F8bDeIXsOlWHUK1TkEmfE2PAoYdz6HnRVkFoFvkYsBYwj7A6+6+rp8wvQ9Re2By9xgOEqLMqjGklQOe0wZ0/Q=="
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA0P8zuZdn10dFqZg54aGiEmpiJkw9OdQAlcMtx6TlUL4+1H6+wJkyS6e2Mf7dPf0kp2fq0rd7Ikj6ZWJcMaCiBLhI+EY5AqEGeOhaMhwZ5F8bDeIXsOlWHUK1TkEmfE2PAoYdz6HnRVkFoFvkYsBYwj7A6+6+rp8wvQ9Re2By9xgOEqLMqjGklQOe0wZ0/Q=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421198,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
      "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421198,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
      "balance": 69999999999999
    },
    {
      "account": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421197,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421197,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA0P8zuZdn10dFqZg54aGiEmpiJkw9OdQAlcMtx6TlUL4+1H6+wJkyS6e2Mf7dPf0kp2fq0rd7Ikj6ZWJcMaCiBLhI+EY5AqEGeOhaMhwZ5F8bDeIXsOlWHUK1TkEmfE2PAoYdz6HnRVkFoFvkYsBYwj7A6+6+rp8wvQ9Re2By9xgOEqLMqjGklQOe0wZ0/Q==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDC3jL19NVlyZ2zYxwHSAwABnCXO7NBXUp2eDLOd7ieTIvKCgEAhiRhOcqAAbDvQAGgUYNAfjmqMbRr4w/k6xt1Pj8io9SuSklwkTGu4jOxg3CLygoBAIY/qiUiX/+lpPcm"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421196,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
      "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421196,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
      "balance": 40000000000001
    },
    {
      "account": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
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
    "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
    "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
        "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
        "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
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
    "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
        "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
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
    "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
        "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
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
    "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
    "meta": 17,
    "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
        "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
        "meta": 17,
        "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
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
    "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
    "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnjoWjIcGeRfGw3iF7DpVh1CtU5BJnxNjwKGHc+h50VZBqDYQv83afMuLFCUmCa4ClyCrDzBFDVhnKR6kiR7wg4F0fm8drU=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
          "op": "OffChainTransfer",
          "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
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
  "id": -576460752303421195,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZ46FoyHBnkXxsN4hew6VYdQrVOQSZ8TY8Chh3PoedFWQag2EL/N2nzLixQlJgmuApcgqw8wRQ1YZykepIke8IOBdEsUMTV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421195,
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZ46FoyHBnkXxsN4hew6VYdQrVOQSZ8TY8Chh3PoedFWQag2EL/N2nzLixQlJgmuApcgqw8wRQ1YZykepIke8IOBdEsUMTV",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
          "op": "OffChainTransfer",
          "to": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
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
  "id": -576460752303421194,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAPg/YK8ptCSMxOpx/FTTElGImIAZbNkovHRVoltCAyxOXfpPSt5oaKUkUSrvrTesVLtiIejS11zn4yJQpG3YTB7hI+EY5AqEGeOhaMhwZ5F8bDeIXsOlWHUK1TkEmfE2PAoYdz6HnRVkGoNhC/zdp8y4sUJSYJrgKXIKsPMEUNWGcpHqSJHvCDgXRseGZiA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421194,
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAPg/YK8ptCSMxOpx/FTTElGImIAZbNkovHRVoltCAyxOXfpPSt5oaKUkUSrvrTesVLtiIejS11zn4yJQpG3YTB7hI+EY5AqEGeOhaMhwZ5F8bDeIXsOlWHUK1TkEmfE2PAoYdz6HnRVkGoNhC/zdp8y4sUJSYJrgKXIKsPMEUNWGcpHqSJHvCDgXRseGZiA=="
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAPg/YK8ptCSMxOpx/FTTElGImIAZbNkovHRVoltCAyxOXfpPSt5oaKUkUSrvrTesVLtiIejS11zn4yJQpG3YTB7hI+EY5AqEGeOhaMhwZ5F8bDeIXsOlWHUK1TkEmfE2PAoYdz6HnRVkGoNhC/zdp8y4sUJSYJrgKXIKsPMEUNWGcpHqSJHvCDgXRseGZiA=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421193,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
      "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421193,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2UpeA5DBWybQuiJztXTaewHJ3Lw9LLePaQZhWa6SMTm5Xg2ePY",
      "balance": 40000000000000
    },
    {
      "account": "ak_cu8h3MaVvfzT1F7DpQUwA9B7a1a8pFMmiPC2qXSHhVfe1gfnD",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421192,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421192,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAcLeMvX01WXJnbNjHAdIDAAGcJc7s0FdSnZ4Ms53uJ5MiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAPg/YK8ptCSMxOpx/FTTElGImIAZbNkovHRVoltCAyxOXfpPSt5oaKUkUSrvrTesVLtiIejS11zn4yJQpG3YTB7hI+EY5AqEGeOhaMhwZ5F8bDeIXsOlWHUK1TkEmfE2PAoYdz6HnRVkGoNhC/zdp8y4sUJSYJrgKXIKsPMEUNWGcpHqSJHvCDgXRseGZiA==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDC3jL19NVlyZ2zYxwHSAwABnCXO7NBXUp2eDLOd7ieTIvKCgEAhiRhOcqAALDvQAGgUYNAfjmqMbRr4w/k6xt1Pj8io9SuSklwkTGu4jOxg3CLygoBAIY/qiUiYADLzkqw"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421191,
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
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421191,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421190,
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
    "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
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
  "channel_id": "ch_vFRY6ocaFrXC2Ui5QYPditWyRJAeTvjfxzVWY6XBDgwZN3wSK",
  "id": -576460752303421190,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
