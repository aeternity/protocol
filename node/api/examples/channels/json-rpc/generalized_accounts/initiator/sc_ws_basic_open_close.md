
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz&keep_running=false&lock_period=10&port=12890&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe&role=initiator
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
      "fsm_id": "ba_Z+X+5/aZnBNnPKEvyk94o5RtOXOh0Jy3j4IFNnVPKo6PA2G4"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz&keep_running=false&lock_period=10&port=12890&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe&role=responder
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
      "fsm_id": "ba_0g3u7UyTsZbZyxDOXTxctM8ygfxnHL4ft2oHY2jrH5glhDyf"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/Thj+qJSJgAKEBPk6i5tqmvWM9VTei8Z4Wy1tgoF6m1kyTXKhRn925y++GJGE5yoAAAgoAhhAGeddIAMCgwNXDEK5D8iFnnPcVCn3mG1lbADk8QSqLyf6n02OC+fUAPGwr0A==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421249,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+NQLAcC4z/jNUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQHlpWam+MZIw3jncpCG82zVcULh0WGXgpdyiuKjJZc/04Y/qiUiYAChAT5Ooubapr1jPVU3ovGeFstbYKBeptZMk1yoUZ/ducvvhiRhOcqAAAIKAIYQBnnXSADAoMDVwxCuQ/IhZ5z3FQp95htZWwA5PEEqi8n+p9Njgvn1AORI8vs="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421249,
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "fsm_id": "ba_0g3u7UyTsZbZyxDOXTxctM8ygfxnHL4ft2oHY2jrH5glhDyf",
      "signed_tx": "tx_+NQLAcC4z/jNUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQHlpWam+MZIw3jncpCG82zVcULh0WGXgpdyiuKjJZc/04Y/qiUiYAChAT5Ooubapr1jPVU3ovGeFstbYKBeptZMk1yoUZ/ducvvhiRhOcqAAAIKAIYQBnnXSADAoMDVwxCuQ/IhZ5z3FQp95htZWwA5PEEqi8n+p9Njgvn1AORI8vs=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421248,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEZCwHAuQET+QEQUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAUsu2pxq9PS8N0cDtBM1cQ+cB/P+KErUQxmLHkjQlBM12/4cSpPhezp0WtP/NhZHvykkEgZ0f6OIpp4FB46nMAriD+IEyAaEB5aVmpvjGSMN453KQhvNs1XFC4dFhl4KXcorioyWXP9OGP6olImAAoQE+TqLm2qa9Yz1VN6LxnhbLW2CgXqbWTJNcqFGf3bnL74YkYTnKgAACCgCGEAZ510gAwKDA1cMQrkPyIWec9xUKfeYbWVsAOTxBKovJ/qfTY4L59QAA/20U"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421248,
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAUsu2pxq9PS8N0cDtBM1cQ+cB/P+KErUQxmLHkjQlBM12/4cSpPhezp0WtP/NhZHvykkEgZ0f6OIpp4FB46nMAriD+IEyAaEB5aVmpvjGSMN453KQhvNs1XFC4dFhl4KXcorioyWXP9OGP6olImAAoQE+TqLm2qa9Yz1VN6LxnhbLW2CgXqbWTJNcqFGf3bnL74YkYTnKgAACCgCGEAZ510gAwKDA1cMQrkPyIWec9xUKfeYbWVsAOTxBKovJ/qfTY4L59QAA/20U",
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_Z+X+5/aZnBNnPKEvyk94o5RtOXOh0Jy3j4IFNnVPKo6PA2G4"
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAUsu2pxq9PS8N0cDtBM1cQ+cB/P+KErUQxmLHkjQlBM12/4cSpPhezp0WtP/NhZHvykkEgZ0f6OIpp4FB46nMAriD+IEyAaEB5aVmpvjGSMN453KQhvNs1XFC4dFhl4KXcorioyWXP9OGP6olImAAoQE+TqLm2qa9Yz1VN6LxnhbLW2CgXqbWTJNcqFGf3bnL74YkYTnKgAACCgCGEAZ510gAwKDA1cMQrkPyIWec9xUKfeYbWVsAOTxBKovJ/qfTY4L59QAA/20U",
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAUsu2pxq9PS8N0cDtBM1cQ+cB/P+KErUQxmLHkjQlBM12/4cSpPhezp0WtP/NhZHvykkEgZ0f6OIpp4FB46nMAriD+IEyAaEB5aVmpvjGSMN453KQhvNs1XFC4dFhl4KXcorioyWXP9OGP6olImAAoQE+TqLm2qa9Yz1VN6LxnhbLW2CgXqbWTJNcqFGf3bnL74YkYTnKgAACCgCGEAZ510gAwKDA1cMQrkPyIWec9xUKfeYbWVsAOTxBKovJ/qfTY4L59QAA/20U",
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAUsu2pxq9PS8N0cDtBM1cQ+cB/P+KErUQxmLHkjQlBM12/4cSpPhezp0WtP/NhZHvykkEgZ0f6OIpp4FB46nMAriD+IEyAaEB5aVmpvjGSMN453KQhvNs1XFC4dFhl4KXcorioyWXP9OGP6olImAAoQE+TqLm2qa9Yz1VN6LxnhbLW2CgXqbWTJNcqFGf3bnL74YkYTnKgAACCgCGEAZ510gAwKDA1cMQrkPyIWec9xUKfeYbWVsAOTxBKovJ/qfTY4L59QAA/20U",
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
    "to": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "message": {
        "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
        "from": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
        "info": "Hello",
        "to": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
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
    "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "message": {
        "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
        "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
        "info": "Hello back",
        "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421247,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
      "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421247,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
      "balance": 69999999999999
    },
    {
      "account": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "state": "tx_+QEZCwHAuQET+QEQUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAUsu2pxq9PS8N0cDtBM1cQ+cB/P+KErUQxmLHkjQlBM12/4cSpPhezp0WtP/NhZHvykkEgZ0f6OIpp4FB46nMAriD+IEyAaEB5aVmpvjGSMN453KQhvNs1XFC4dFhl4KXcorioyWXP9OGP6olImAAoQE+TqLm2qa9Yz1VN6LxnhbLW2CgXqbWTJNcqFGf3bnL74YkYTnKgAACCgCGEAZ510gAwKDA1cMQrkPyIWec9xUKfeYbWVsAOTxBKovJ/qfTY4L59QAA/20U"
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "state": "tx_+QEZCwHAuQET+QEQUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAUsu2pxq9PS8N0cDtBM1cQ+cB/P+KErUQxmLHkjQlBM12/4cSpPhezp0WtP/NhZHvykkEgZ0f6OIpp4FB46nMAriD+IEyAaEB5aVmpvjGSMN453KQhvNs1XFC4dFhl4KXcorioyWXP9OGP6olImAAoQE+TqLm2qa9Yz1VN6LxnhbLW2CgXqbWTJNcqFGf3bnL74YkYTnKgAACCgCGEAZ510gAwKDA1cMQrkPyIWec9xUKfeYbWVsAOTxBKovJ/qfTY4L59QAA/20U"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421246,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
      "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421246,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
      "balance": 69999999999999
    },
    {
      "account": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
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
    "from": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
    "to": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
        "from": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
        "to": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
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
    "to": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
        "to": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
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
    "from": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
        "from": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
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
    "from": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
    "meta": 17,
    "to": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
        "from": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
        "meta": 17,
        "to": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
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
    "from": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
    "to": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpUfqPvnAYRIP+ZRLgS/JWlDo68qBfweTu4dnlvaj5WlAqAaSnSUYV3Nh3bJHsDNI1RrmZdnl0o9FSeFCjG17Oo1rAznQM4=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
          "op": "OffChainTransfer",
          "to": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
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
  "id": -576460752303421245,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQaVH6j75wGESD/mUS4EvyVpQ6OvKgX8Hk7uHZ5b2o+VpQKgGkp0lGFdzYd2yR7AzSNUa5mXZ5dKPRUnhQoxtezqNaySiwvr"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421245,
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQaVH6j75wGESD/mUS4EvyVpQ6OvKgX8Hk7uHZ5b2o+VpQKgGkp0lGFdzYd2yR7AzSNUa5mXZ5dKPRUnhQoxtezqNaySiwvr",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
          "op": "OffChainTransfer",
          "to": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
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
  "id": -576460752303421244,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAdy9gd87JxBw5BuhQaxds5IjQaQwK2K8/VvhLjX6LaW+dyyv1GQcgzKkbqBAEOqRKALNyS7d+fQxokHWDDUGzALhI+EY5AqEGlR+o++cBhEg/5lEuBL8laUOjryoF/B5O7h2eW9qPlaUCoBpKdJRhXc2HdskewM0jVGuZl2eXSj0VJ4UKMbXs6jWsJXKq8A=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421244,
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAdy9gd87JxBw5BuhQaxds5IjQaQwK2K8/VvhLjX6LaW+dyyv1GQcgzKkbqBAEOqRKALNyS7d+fQxokHWDDUGzALhI+EY5AqEGlR+o++cBhEg/5lEuBL8laUOjryoF/B5O7h2eW9qPlaUCoBpKdJRhXc2HdskewM0jVGuZl2eXSj0VJ4UKMbXs6jWsJXKq8A=="
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAdy9gd87JxBw5BuhQaxds5IjQaQwK2K8/VvhLjX6LaW+dyyv1GQcgzKkbqBAEOqRKALNyS7d+fQxokHWDDUGzALhI+EY5AqEGlR+o++cBhEg/5lEuBL8laUOjryoF/B5O7h2eW9qPlaUCoBpKdJRhXc2HdskewM0jVGuZl2eXSj0VJ4UKMbXs6jWsJXKq8A=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421243,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
      "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421243,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
      "balance": 69999999999998
    },
    {
      "account": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421242,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421242,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAdy9gd87JxBw5BuhQaxds5IjQaQwK2K8/VvhLjX6LaW+dyyv1GQcgzKkbqBAEOqRKALNyS7d+fQxokHWDDUGzALhI+EY5AqEGlR+o++cBhEg/5lEuBL8laUOjryoF/B5O7h2eW9qPlaUCoBpKdJRhXc2HdskewM0jVGuZl2eXSj0VJ4UKMbXs6jWsJXKq8A==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDlpWam+MZIw3jncpCG82zVcULh0WGXgpdyiuKjJZc/04vKCgEAhj+qJSJf/rDvQAGgPk6i5tqmvWM9VTei8Z4Wy1tgoF6m1kyTXKhRn925y++LygoBAIYkYTnKgAJL4NIL"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421241,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
      "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421241,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
      "balance": 40000000000002
    },
    {
      "account": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
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
    "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
    "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
        "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
        "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
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
    "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
        "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
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
    "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
        "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
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
    "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
    "meta": 17,
    "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
        "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
        "meta": 17,
        "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
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
    "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
    "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpUfqPvnAYRIP+ZRLgS/JWlDo68qBfweTu4dnlvaj5WlA6DA1cMQrkPyIWec9xUKfeYbWVsAOTxBKovJ/qfTY4L59d1yp6E=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
          "op": "OffChainTransfer",
          "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
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
  "id": -576460752303421240,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECu8hS7uhNdwO6n8s+SPKg3lR/XCcIhKx1DSUWIiU7cxi+OCeg4t2nMiNPd1O7wB3RzWAyAB3KLOOyAYrEXUlUHuEj4RjkCoQaVH6j75wGESD/mUS4EvyVpQ6OvKgX8Hk7uHZ5b2o+VpQOgwNXDEK5D8iFnnPcVCn3mG1lbADk8QSqLyf6n02OC+fURrR4g"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421240,
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "signed_tx": "tx_+JALAfhCuECu8hS7uhNdwO6n8s+SPKg3lR/XCcIhKx1DSUWIiU7cxi+OCeg4t2nMiNPd1O7wB3RzWAyAB3KLOOyAYrEXUlUHuEj4RjkCoQaVH6j75wGESD/mUS4EvyVpQ6OvKgX8Hk7uHZ5b2o+VpQOgwNXDEK5D8iFnnPcVCn3mG1lbADk8QSqLyf6n02OC+fURrR4g",
      "updates": [
        {
          "amount": 1,
          "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
          "op": "OffChainTransfer",
          "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
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
  "id": -576460752303421239,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhArvIUu7oTXcDup/LPkjyoN5Uf1wnCISsdQ0lFiIlO3MYvjgnoOLdpzIjT3dTu8Ad0c1gMgAdyizjsgGKxF1JVB7hI+EY5AqEGlR+o++cBhEg/5lEuBL8laUOjryoF/B5O7h2eW9qPlaUDoMDVwxCuQ/IhZ5z3FQp95htZWwA5PEEqi8n+p9Njgvn1TX/y5A=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421239,
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhArvIUu7oTXcDup/LPkjyoN5Uf1wnCISsdQ0lFiIlO3MYvjgnoOLdpzIjT3dTu8Ad0c1gMgAdyizjsgGKxF1JVB7hI+EY5AqEGlR+o++cBhEg/5lEuBL8laUOjryoF/B5O7h2eW9qPlaUDoMDVwxCuQ/IhZ5z3FQp95htZWwA5PEEqi8n+p9Njgvn1TX/y5A=="
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhArvIUu7oTXcDup/LPkjyoN5Uf1wnCISsdQ0lFiIlO3MYvjgnoOLdpzIjT3dTu8Ad0c1gMgAdyizjsgGKxF1JVB7hI+EY5AqEGlR+o++cBhEg/5lEuBL8laUOjryoF/B5O7h2eW9qPlaUDoMDVwxCuQ/IhZ5z3FQp95htZWwA5PEEqi8n+p9Njgvn1TX/y5A=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421238,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
      "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421238,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
      "balance": 40000000000001
    },
    {
      "account": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421237,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421237,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhArvIUu7oTXcDup/LPkjyoN5Uf1wnCISsdQ0lFiIlO3MYvjgnoOLdpzIjT3dTu8Ad0c1gMgAdyizjsgGKxF1JVB7hI+EY5AqEGlR+o++cBhEg/5lEuBL8laUOjryoF/B5O7h2eW9qPlaUDoMDVwxCuQ/IhZ5z3FQp95htZWwA5PEEqi8n+p9Njgvn1TX/y5A==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDlpWam+MZIw3jncpCG82zVcULh0WGXgpdyiuKjJZc/04vKCgEAhj+qJSJf/7DvQAGgPk6i5tqmvWM9VTei8Z4Wy1tgoF6m1kyTXKhRn925y++LygoBAIYkYTnKgAH0HDkd"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421236,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
      "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421236,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
      "balance": 40000000000001
    },
    {
      "account": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
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
    "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
    "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
        "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
        "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
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
    "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
        "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
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
    "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
        "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
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
    "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
    "meta": 17,
    "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
        "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
        "meta": 17,
        "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
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
    "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
    "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpUfqPvnAYRIP+ZRLgS/JWlDo68qBfweTu4dnlvaj5WlBKBm0MJGMwAd8lMq+6AUVVlhEOsi0S4+B8ZcwJmGJ6ZxZBI3hYk=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
          "op": "OffChainTransfer",
          "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
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
  "id": -576460752303421235,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBrVHnYJ23B0aBAsoaeuZp4y34WHvsqZr7zZTnzH2YbG8AM+8eHspXP0tTFJAx7XtJmvSDnyegFq8rqYBCMbbALuEj4RjkCoQaVH6j75wGESD/mUS4EvyVpQ6OvKgX8Hk7uHZ5b2o+VpQSgZtDCRjMAHfJTKvugFFVZYRDrItEuPgfGXMCZhiemcWSwrqcb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421235,
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBrVHnYJ23B0aBAsoaeuZp4y34WHvsqZr7zZTnzH2YbG8AM+8eHspXP0tTFJAx7XtJmvSDnyegFq8rqYBCMbbALuEj4RjkCoQaVH6j75wGESD/mUS4EvyVpQ6OvKgX8Hk7uHZ5b2o+VpQSgZtDCRjMAHfJTKvugFFVZYRDrItEuPgfGXMCZhiemcWSwrqcb",
      "updates": [
        {
          "amount": 1,
          "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
          "op": "OffChainTransfer",
          "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
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
  "id": -576460752303421234,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAa1R52CdtwdGgQLKGnrmaeMt+Fh77Kma+82U58x9mGxvADPvHh7KVz9LUxSQMe17SZr0g58noBavK6mAQjG2wC7hI+EY5AqEGlR+o++cBhEg/5lEuBL8laUOjryoF/B5O7h2eW9qPlaUEoGbQwkYzAB3yUyr7oBRVWWEQ6yLRLj4HxlzAmYYnpnFkiNSb0Q=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421234,
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAa1R52CdtwdGgQLKGnrmaeMt+Fh77Kma+82U58x9mGxvADPvHh7KVz9LUxSQMe17SZr0g58noBavK6mAQjG2wC7hI+EY5AqEGlR+o++cBhEg/5lEuBL8laUOjryoF/B5O7h2eW9qPlaUEoGbQwkYzAB3yUyr7oBRVWWEQ6yLRLj4HxlzAmYYnpnFkiNSb0Q=="
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAa1R52CdtwdGgQLKGnrmaeMt+Fh77Kma+82U58x9mGxvADPvHh7KVz9LUxSQMe17SZr0g58noBavK6mAQjG2wC7hI+EY5AqEGlR+o++cBhEg/5lEuBL8laUOjryoF/B5O7h2eW9qPlaUEoGbQwkYzAB3yUyr7oBRVWWEQ6yLRLj4HxlzAmYYnpnFkiNSb0Q=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421233,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
      "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421233,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
      "balance": 40000000000000
    },
    {
      "account": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421232,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421232,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAa1R52CdtwdGgQLKGnrmaeMt+Fh77Kma+82U58x9mGxvADPvHh7KVz9LUxSQMe17SZr0g58noBavK6mAQjG2wC7hI+EY5AqEGlR+o++cBhEg/5lEuBL8laUOjryoF/B5O7h2eW9qPlaUEoGbQwkYzAB3yUyr7oBRVWWEQ6yLRLj4HxlzAmYYnpnFkiNSb0Q==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDlpWam+MZIw3jncpCG82zVcULh0WGXgpdyiuKjJZc/04vKCgEAhj+qJSJgALDvQAGgPk6i5tqmvWM9VTei8Z4Wy1tgoF6m1kyTXKhRn925y++LygoBAIYkYTnKgAB5CI/K"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421231,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
      "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421231,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
      "balance": 70000000000000
    },
    {
      "account": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
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
    "from": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
    "to": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
        "from": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
        "to": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
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
    "to": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
        "to": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
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
    "from": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
        "from": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
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
    "from": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
    "meta": 17,
    "to": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
        "from": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
        "meta": 17,
        "to": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
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
    "from": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
    "to": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpUfqPvnAYRIP+ZRLgS/JWlDo68qBfweTu4dnlvaj5WlBaDA1cMQrkPyIWec9xUKfeYbWVsAOTxBKovJ/qfTY4L59QKPllI=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
          "op": "OffChainTransfer",
          "to": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
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
  "id": -576460752303421230,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQaVH6j75wGESD/mUS4EvyVpQ6OvKgX8Hk7uHZ5b2o+VpQWgwNXDEK5D8iFnnPcVCn3mG1lbADk8QSqLyf6n02OC+fV7eN38"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421230,
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQaVH6j75wGESD/mUS4EvyVpQ6OvKgX8Hk7uHZ5b2o+VpQWgwNXDEK5D8iFnnPcVCn3mG1lbADk8QSqLyf6n02OC+fV7eN38",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
          "op": "OffChainTransfer",
          "to": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
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
  "id": -576460752303421229,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAr/vlJgnfjuCkWIR5p0sHktgMVgK1pRcUOuWqOLPjT3/1FzLlTwVLAlnbCUCkPCBOa5bu7dTwjIrG5ErBqVClBLhI+EY5AqEGlR+o++cBhEg/5lEuBL8laUOjryoF/B5O7h2eW9qPlaUFoMDVwxCuQ/IhZ5z3FQp95htZWwA5PEEqi8n+p9Njgvn1+hXrKw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421229,
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAr/vlJgnfjuCkWIR5p0sHktgMVgK1pRcUOuWqOLPjT3/1FzLlTwVLAlnbCUCkPCBOa5bu7dTwjIrG5ErBqVClBLhI+EY5AqEGlR+o++cBhEg/5lEuBL8laUOjryoF/B5O7h2eW9qPlaUFoMDVwxCuQ/IhZ5z3FQp95htZWwA5PEEqi8n+p9Njgvn1+hXrKw=="
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAr/vlJgnfjuCkWIR5p0sHktgMVgK1pRcUOuWqOLPjT3/1FzLlTwVLAlnbCUCkPCBOa5bu7dTwjIrG5ErBqVClBLhI+EY5AqEGlR+o++cBhEg/5lEuBL8laUOjryoF/B5O7h2eW9qPlaUFoMDVwxCuQ/IhZ5z3FQp95htZWwA5PEEqi8n+p9Njgvn1+hXrKw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421228,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
      "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421228,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
      "balance": 69999999999999
    },
    {
      "account": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421227,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421227,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAr/vlJgnfjuCkWIR5p0sHktgMVgK1pRcUOuWqOLPjT3/1FzLlTwVLAlnbCUCkPCBOa5bu7dTwjIrG5ErBqVClBLhI+EY5AqEGlR+o++cBhEg/5lEuBL8laUOjryoF/B5O7h2eW9qPlaUFoMDVwxCuQ/IhZ5z3FQp95htZWwA5PEEqi8n+p9Njgvn1+hXrKw==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDlpWam+MZIw3jncpCG82zVcULh0WGXgpdyiuKjJZc/04vKCgEAhj+qJSJf/7DvQAGgPk6i5tqmvWM9VTei8Z4Wy1tgoF6m1kyTXKhRn925y++LygoBAIYkYTnKgAH0HDkd"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421226,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
      "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421226,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
      "balance": 40000000000001
    },
    {
      "account": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
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
    "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
    "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
        "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
        "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
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
    "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
        "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
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
    "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
        "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
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
    "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
    "meta": 17,
    "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
        "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
        "meta": 17,
        "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
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
    "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
    "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpUfqPvnAYRIP+ZRLgS/JWlDo68qBfweTu4dnlvaj5WlBqBm0MJGMwAd8lMq+6AUVVlhEOsi0S4+B8ZcwJmGJ6ZxZMlOQyE=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
          "op": "OffChainTransfer",
          "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
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
  "id": -576460752303421225,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBQVb6mZdT8Y5j/9LYxrUv1tRQvg09K+BashORvGk+XupU82USd9fivJ2k0Q4lx5DPEPXrBaqasm2/09yi8lysNuEj4RjkCoQaVH6j75wGESD/mUS4EvyVpQ6OvKgX8Hk7uHZ5b2o+VpQagZtDCRjMAHfJTKvugFFVZYRDrItEuPgfGXMCZhiemcWTqApVx"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421225,
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBQVb6mZdT8Y5j/9LYxrUv1tRQvg09K+BashORvGk+XupU82USd9fivJ2k0Q4lx5DPEPXrBaqasm2/09yi8lysNuEj4RjkCoQaVH6j75wGESD/mUS4EvyVpQ6OvKgX8Hk7uHZ5b2o+VpQagZtDCRjMAHfJTKvugFFVZYRDrItEuPgfGXMCZhiemcWTqApVx",
      "updates": [
        {
          "amount": 1,
          "from": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
          "op": "OffChainTransfer",
          "to": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
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
  "id": -576460752303421224,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAUFW+pmXU/GOY//S2Ma1L9bUUL4NPSvgWrITkbxpPl7qVPNlEnfX4rydpNEOJceQzxD16wWqmrJtv9PcovJcrDbhI+EY5AqEGlR+o++cBhEg/5lEuBL8laUOjryoF/B5O7h2eW9qPlaUGoGbQwkYzAB3yUyr7oBRVWWEQ6yLRLj4HxlzAmYYnpnFkfAsoDQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421224,
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAUFW+pmXU/GOY//S2Ma1L9bUUL4NPSvgWrITkbxpPl7qVPNlEnfX4rydpNEOJceQzxD16wWqmrJtv9PcovJcrDbhI+EY5AqEGlR+o++cBhEg/5lEuBL8laUOjryoF/B5O7h2eW9qPlaUGoGbQwkYzAB3yUyr7oBRVWWEQ6yLRLj4HxlzAmYYnpnFkfAsoDQ=="
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAUFW+pmXU/GOY//S2Ma1L9bUUL4NPSvgWrITkbxpPl7qVPNlEnfX4rydpNEOJceQzxD16wWqmrJtv9PcovJcrDbhI+EY5AqEGlR+o++cBhEg/5lEuBL8laUOjryoF/B5O7h2eW9qPlaUGoGbQwkYzAB3yUyr7oBRVWWEQ6yLRLj4HxlzAmYYnpnFkfAsoDQ=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421223,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
      "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421223,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_USZ5gALsv6z1G4FmzkvpK6u91C1UHZkHjgL1Lfsg3zyHM8jVe",
      "balance": 40000000000000
    },
    {
      "account": "ak_2k915XXLeEukXUxyo6R5SiNKe6MFgTMm6BneQeS9pE6XwvM2gz",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421222,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421222,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAeWlZqb4xkjDeOdykIbzbNVxQuHRYZeCl3KK4qMllz/TiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAUFW+pmXU/GOY//S2Ma1L9bUUL4NPSvgWrITkbxpPl7qVPNlEnfX4rydpNEOJceQzxD16wWqmrJtv9PcovJcrDbhI+EY5AqEGlR+o++cBhEg/5lEuBL8laUOjryoF/B5O7h2eW9qPlaUGoGbQwkYzAB3yUyr7oBRVWWEQ6yLRLj4HxlzAmYYnpnFkfAsoDQ==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDlpWam+MZIw3jncpCG82zVcULh0WGXgpdyiuKjJZc/04vKCgEAhj+qJSJgALDvQAGgPk6i5tqmvWM9VTei8Z4Wy1tgoF6m1kyTXKhRn925y++LygoBAIYkYTnKgAB5CI/K"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421221,
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
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421221,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421220,
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
    "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
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
  "channel_id": "ch_28gAWuWwdnoFm8PvAaeYdoGYiCgfz8DNzG6gWo2gcSNMW52khB",
  "id": -576460752303421220,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
