
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL&keep_running=false&lock_period=10&port=12890&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo&role=initiator
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
      "fsm_id": "ba_KUOf2iDMz+kFIYYyEicLBg0gaJ1p0ae9ByoVc3gGCUin0g0M"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL&keep_running=false&lock_period=10&port=12890&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo&role=responder
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
      "fsm_id": "ba_jmyBFiU8hu4gVfXl0D4p+gQnYcPLJxCWfy24+fmzi0iw7SmV"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHhj+qJSJgAKEBNz+qJ0Z1mW15NlxLac4zJezq2R7sGk9GQ6USiTiMgN6GJGE5yoAAAgoAhhAGeddIAMCg+SJvQ23aI0LuMYbCXBo+TWjlfvGscvMXTZ4d9hX+RU8A0EClMw==",
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
    "signed_tx": "tx_+NQLAcC4z/jNUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQGtbwc0st31fTTF+s/rXaerNpYZiDTG7BQ49StjqaYjx4Y/qiUiYAChATc/qidGdZlteTZcS2nOMyXs6tke7BpPRkOlEok4jIDehiRhOcqAAAIKAIYQBnnXSADAoPkib0Nt2iNC7jGGwlwaPk1o5X7xrHLzF02eHfYV/kVPAIQwZgY="
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_jmyBFiU8hu4gVfXl0D4p+gQnYcPLJxCWfy24+fmzi0iw7SmV"
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "signed_tx": "tx_+NQLAcC4z/jNUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQGtbwc0st31fTTF+s/rXaerNpYZiDTG7BQ49StjqaYjx4Y/qiUiYAChATc/qidGdZlteTZcS2nOMyXs6tke7BpPRkOlEok4jIDehiRhOcqAAAIKAIYQBnnXSADAoPkib0Nt2iNC7jGGwlwaPk1o5X7xrHLzF02eHfYV/kVPAIQwZgY=",
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
    "signed_tx": "tx_+QEZCwHAuQET+QEQUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhA2if1OXiSgJOnKIXSDrqh0f0wioxrpnaxF8v22PrOptIO2uuL6acAXLtj8E0aWBjrce26HnMAkENX0rG8ADh7CbiD+IEyAaEBrW8HNLLd9X00xfrP612nqzaWGYg0xuwUOPUrY6mmI8eGP6olImAAoQE3P6onRnWZbXk2XEtpzjMl7OrZHuwaT0ZDpRKJOIyA3oYkYTnKgAACCgCGEAZ510gAwKD5Im9DbdojQu4xhsJcGj5NaOV+8axy8xdNnh32Ff5FTwBeFJjV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhA2if1OXiSgJOnKIXSDrqh0f0wioxrpnaxF8v22PrOptIO2uuL6acAXLtj8E0aWBjrce26HnMAkENX0rG8ADh7CbiD+IEyAaEBrW8HNLLd9X00xfrP612nqzaWGYg0xuwUOPUrY6mmI8eGP6olImAAoQE3P6onRnWZbXk2XEtpzjMl7OrZHuwaT0ZDpRKJOIyA3oYkYTnKgAACCgCGEAZ510gAwKD5Im9DbdojQu4xhsJcGj5NaOV+8axy8xdNnh32Ff5FTwBeFJjV",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_KUOf2iDMz+kFIYYyEicLBg0gaJ1p0ae9ByoVc3gGCUin0g0M"
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhA2if1OXiSgJOnKIXSDrqh0f0wioxrpnaxF8v22PrOptIO2uuL6acAXLtj8E0aWBjrce26HnMAkENX0rG8ADh7CbiD+IEyAaEBrW8HNLLd9X00xfrP612nqzaWGYg0xuwUOPUrY6mmI8eGP6olImAAoQE3P6onRnWZbXk2XEtpzjMl7OrZHuwaT0ZDpRKJOIyA3oYkYTnKgAACCgCGEAZ510gAwKD5Im9DbdojQu4xhsJcGj5NaOV+8axy8xdNnh32Ff5FTwBeFJjV",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhA2if1OXiSgJOnKIXSDrqh0f0wioxrpnaxF8v22PrOptIO2uuL6acAXLtj8E0aWBjrce26HnMAkENX0rG8ADh7CbiD+IEyAaEBrW8HNLLd9X00xfrP612nqzaWGYg0xuwUOPUrY6mmI8eGP6olImAAoQE3P6onRnWZbXk2XEtpzjMl7OrZHuwaT0ZDpRKJOIyA3oYkYTnKgAACCgCGEAZ510gAwKD5Im9DbdojQu4xhsJcGj5NaOV+8axy8xdNnh32Ff5FTwBeFJjV",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhA2if1OXiSgJOnKIXSDrqh0f0wioxrpnaxF8v22PrOptIO2uuL6acAXLtj8E0aWBjrce26HnMAkENX0rG8ADh7CbiD+IEyAaEBrW8HNLLd9X00xfrP612nqzaWGYg0xuwUOPUrY6mmI8eGP6olImAAoQE3P6onRnWZbXk2XEtpzjMl7OrZHuwaT0ZDpRKJOIyA3oYkYTnKgAACCgCGEAZ510gAwKD5Im9DbdojQu4xhsJcGj5NaOV+8axy8xdNnh32Ff5FTwBeFJjV",
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
    "to": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "message": {
        "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
        "from": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
        "info": "Hello",
        "to": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
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
    "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "message": {
        "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
        "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
        "info": "Hello back",
        "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
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
      "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
      "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
  "id": -576460752303421247,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
      "balance": 69999999999999
    },
    {
      "account": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "state": "tx_+QEZCwHAuQET+QEQUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhA2if1OXiSgJOnKIXSDrqh0f0wioxrpnaxF8v22PrOptIO2uuL6acAXLtj8E0aWBjrce26HnMAkENX0rG8ADh7CbiD+IEyAaEBrW8HNLLd9X00xfrP612nqzaWGYg0xuwUOPUrY6mmI8eGP6olImAAoQE3P6onRnWZbXk2XEtpzjMl7OrZHuwaT0ZDpRKJOIyA3oYkYTnKgAACCgCGEAZ510gAwKD5Im9DbdojQu4xhsJcGj5NaOV+8axy8xdNnh32Ff5FTwBeFJjV"
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "state": "tx_+QEZCwHAuQET+QEQUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhA2if1OXiSgJOnKIXSDrqh0f0wioxrpnaxF8v22PrOptIO2uuL6acAXLtj8E0aWBjrce26HnMAkENX0rG8ADh7CbiD+IEyAaEBrW8HNLLd9X00xfrP612nqzaWGYg0xuwUOPUrY6mmI8eGP6olImAAoQE3P6onRnWZbXk2XEtpzjMl7OrZHuwaT0ZDpRKJOIyA3oYkYTnKgAACCgCGEAZ510gAwKD5Im9DbdojQu4xhsJcGj5NaOV+8axy8xdNnh32Ff5FTwBeFJjV"
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
      "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
      "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
  "id": -576460752303421246,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
      "balance": 69999999999999
    },
    {
      "account": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
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
    "from": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
    "to": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
        "from": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
        "to": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
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
    "to": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
        "to": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
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
    "from": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
        "from": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
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
    "from": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
    "meta": 17,
    "to": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
        "from": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
        "meta": 17,
        "to": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
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
    "from": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
    "to": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmPLcXVhRxIPGtnMwhEr+pi1L4e1MGwp4Scr8klGTcVbAqBt0h0wyCx37Fz8JMZIcEh+dfSASY38wdMBT4Rzfe6f8xD5n2g=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
          "op": "OffChainTransfer",
          "to": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
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
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZjy3F1YUcSDxrZzMIRK/qYtS+HtTBsKeEnK/JJRk3FWwKgbdIdMMgsd+xc/CTGSHBIfnX0gEmN/MHTAU+Ec33un/NCmeSK"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZjy3F1YUcSDxrZzMIRK/qYtS+HtTBsKeEnK/JJRk3FWwKgbdIdMMgsd+xc/CTGSHBIfnX0gEmN/MHTAU+Ec33un/NCmeSK",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
          "op": "OffChainTransfer",
          "to": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
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
    "signed_tx": "tx_+NwLAcC41/jVUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAE4O/WWeZvEoKi2aMxYmfX7/xr9cyrKXImjZjJWiGJJqNmSHisHWk2Zu9Gz5aK5k0rK0+sP01fB81tBuDHG4+BrhI+EY5AqEGY8txdWFHEg8a2czCESv6mLUvh7UwbCnhJyvySUZNxVsCoG3SHTDILHfsXPwkxkhwSH519IBJjfzB0wFPhHN97p/zjA9MNQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAE4O/WWeZvEoKi2aMxYmfX7/xr9cyrKXImjZjJWiGJJqNmSHisHWk2Zu9Gz5aK5k0rK0+sP01fB81tBuDHG4+BrhI+EY5AqEGY8txdWFHEg8a2czCESv6mLUvh7UwbCnhJyvySUZNxVsCoG3SHTDILHfsXPwkxkhwSH519IBJjfzB0wFPhHN97p/zjA9MNQ=="
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAE4O/WWeZvEoKi2aMxYmfX7/xr9cyrKXImjZjJWiGJJqNmSHisHWk2Zu9Gz5aK5k0rK0+sP01fB81tBuDHG4+BrhI+EY5AqEGY8txdWFHEg8a2czCESv6mLUvh7UwbCnhJyvySUZNxVsCoG3SHTDILHfsXPwkxkhwSH519IBJjfzB0wFPhHN97p/zjA9MNQ=="
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
      "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
      "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
  "id": -576460752303421243,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
      "balance": 69999999999998
    },
    {
      "account": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
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
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
  "id": -576460752303421242,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAE4O/WWeZvEoKi2aMxYmfX7/xr9cyrKXImjZjJWiGJJqNmSHisHWk2Zu9Gz5aK5k0rK0+sP01fB81tBuDHG4+BrhI+EY5AqEGY8txdWFHEg8a2czCESv6mLUvh7UwbCnhJyvySUZNxVsCoG3SHTDILHfsXPwkxkhwSH519IBJjfzB0wFPhHN97p/zjA9MNQ==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCtbwc0st31fTTF+s/rXaerNpYZiDTG7BQ49StjqaYjx4vKCgEAhj+qJSJf/rDvQAGgNz+qJ0Z1mW15NlxLac4zJezq2R7sGk9GQ6USiTiMgN6LygoBAIYkYTnKgAK8THEE"
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
      "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
      "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
  "id": -576460752303421241,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
      "balance": 40000000000002
    },
    {
      "account": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
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
    "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
    "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
        "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
        "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
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
    "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
        "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
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
    "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
        "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
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
    "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
    "meta": 17,
    "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
        "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
        "meta": 17,
        "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
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
    "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
    "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmPLcXVhRxIPGtnMwhEr+pi1L4e1MGwp4Scr8klGTcVbA6D5Im9DbdojQu4xhsJcGj5NaOV+8axy8xdNnh32Ff5FT38wenE=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
          "op": "OffChainTransfer",
          "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
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
    "signed_tx": "tx_+JALAfhCuEBcyMBH5bvOYabVlA5KbOV0JGp8lCi1wTGdXj0cTr66rRhjPf/vmubMhjlTr7fkgi54O8eDQS8BUFi38PN1/K8AuEj4RjkCoQZjy3F1YUcSDxrZzMIRK/qYtS+HtTBsKeEnK/JJRk3FWwOg+SJvQ23aI0LuMYbCXBo+TWjlfvGscvMXTZ4d9hX+RU+JHjqE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBcyMBH5bvOYabVlA5KbOV0JGp8lCi1wTGdXj0cTr66rRhjPf/vmubMhjlTr7fkgi54O8eDQS8BUFi38PN1/K8AuEj4RjkCoQZjy3F1YUcSDxrZzMIRK/qYtS+HtTBsKeEnK/JJRk3FWwOg+SJvQ23aI0LuMYbCXBo+TWjlfvGscvMXTZ4d9hX+RU+JHjqE",
      "updates": [
        {
          "amount": 1,
          "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
          "op": "OffChainTransfer",
          "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
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
    "signed_tx": "tx_+NwLAcC41/jVUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAXMjAR+W7zmGm1ZQOSmzldCRqfJQotcExnV49HE6+uq0YYz3/75rmzIY5U6+35IIueDvHg0EvAVBYt/DzdfyvALhI+EY5AqEGY8txdWFHEg8a2czCESv6mLUvh7UwbCnhJyvySUZNxVsDoPkib0Nt2iNC7jGGwlwaPk1o5X7xrHLzF02eHfYV/kVPVZcFLw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAXMjAR+W7zmGm1ZQOSmzldCRqfJQotcExnV49HE6+uq0YYz3/75rmzIY5U6+35IIueDvHg0EvAVBYt/DzdfyvALhI+EY5AqEGY8txdWFHEg8a2czCESv6mLUvh7UwbCnhJyvySUZNxVsDoPkib0Nt2iNC7jGGwlwaPk1o5X7xrHLzF02eHfYV/kVPVZcFLw=="
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAXMjAR+W7zmGm1ZQOSmzldCRqfJQotcExnV49HE6+uq0YYz3/75rmzIY5U6+35IIueDvHg0EvAVBYt/DzdfyvALhI+EY5AqEGY8txdWFHEg8a2czCESv6mLUvh7UwbCnhJyvySUZNxVsDoPkib0Nt2iNC7jGGwlwaPk1o5X7xrHLzF02eHfYV/kVPVZcFLw=="
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
      "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
      "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
  "id": -576460752303421238,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
      "balance": 40000000000001
    },
    {
      "account": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
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
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
  "id": -576460752303421237,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAXMjAR+W7zmGm1ZQOSmzldCRqfJQotcExnV49HE6+uq0YYz3/75rmzIY5U6+35IIueDvHg0EvAVBYt/DzdfyvALhI+EY5AqEGY8txdWFHEg8a2czCESv6mLUvh7UwbCnhJyvySUZNxVsDoPkib0Nt2iNC7jGGwlwaPk1o5X7xrHLzF02eHfYV/kVPVZcFLw==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCtbwc0st31fTTF+s/rXaerNpYZiDTG7BQ49StjqaYjx4vKCgEAhj+qJSJf/7DvQAGgNz+qJ0Z1mW15NlxLac4zJezq2R7sGk9GQ6USiTiMgN6LygoBAIYkYTnKgAHFwWTK"
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
      "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
      "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
  "id": -576460752303421236,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
      "balance": 40000000000001
    },
    {
      "account": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
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
    "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
    "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
        "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
        "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
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
    "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
        "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
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
    "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
        "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
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
    "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
    "meta": 17,
    "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
        "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
        "meta": 17,
        "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
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
    "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
    "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmPLcXVhRxIPGtnMwhEr+pi1L4e1MGwp4Scr8klGTcVbBKCS5Z88trBzDDYG6DRBRphCwHlXN7eKWuW/6WiVGmYJ5cugeJE=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
          "op": "OffChainTransfer",
          "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
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
    "signed_tx": "tx_+JALAfhCuEDaGQs8J6AzuiCUMMoRGs1md+h0ilo2yLzR0VLpyWv9yAs75KtuJqFraFRlNzOrKEL0QiOBa+D1C+o3Kvd5B08GuEj4RjkCoQZjy3F1YUcSDxrZzMIRK/qYtS+HtTBsKeEnK/JJRk3FWwSgkuWfPLawcww2Bug0QUaYQsB5Vze3ilrlv+lolRpmCeWF3hRW"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDaGQs8J6AzuiCUMMoRGs1md+h0ilo2yLzR0VLpyWv9yAs75KtuJqFraFRlNzOrKEL0QiOBa+D1C+o3Kvd5B08GuEj4RjkCoQZjy3F1YUcSDxrZzMIRK/qYtS+HtTBsKeEnK/JJRk3FWwSgkuWfPLawcww2Bug0QUaYQsB5Vze3ilrlv+lolRpmCeWF3hRW",
      "updates": [
        {
          "amount": 1,
          "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
          "op": "OffChainTransfer",
          "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
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
    "signed_tx": "tx_+NwLAcC41/jVUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA2hkLPCegM7oglDDKERrNZnfodIpaNsi80dFS6clr/cgLO+Srbiaha2hUZTczqyhC9EIjgWvg9QvqNyr3eQdPBrhI+EY5AqEGY8txdWFHEg8a2czCESv6mLUvh7UwbCnhJyvySUZNxVsEoJLlnzy2sHMMNgboNEFGmELAeVc3t4pa5b/paJUaZgnlIFiTpQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA2hkLPCegM7oglDDKERrNZnfodIpaNsi80dFS6clr/cgLO+Srbiaha2hUZTczqyhC9EIjgWvg9QvqNyr3eQdPBrhI+EY5AqEGY8txdWFHEg8a2czCESv6mLUvh7UwbCnhJyvySUZNxVsEoJLlnzy2sHMMNgboNEFGmELAeVc3t4pa5b/paJUaZgnlIFiTpQ=="
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA2hkLPCegM7oglDDKERrNZnfodIpaNsi80dFS6clr/cgLO+Srbiaha2hUZTczqyhC9EIjgWvg9QvqNyr3eQdPBrhI+EY5AqEGY8txdWFHEg8a2czCESv6mLUvh7UwbCnhJyvySUZNxVsEoJLlnzy2sHMMNgboNEFGmELAeVc3t4pa5b/paJUaZgnlIFiTpQ=="
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
      "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
      "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
  "id": -576460752303421233,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
      "balance": 40000000000000
    },
    {
      "account": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
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
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
  "id": -576460752303421232,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA2hkLPCegM7oglDDKERrNZnfodIpaNsi80dFS6clr/cgLO+Srbiaha2hUZTczqyhC9EIjgWvg9QvqNyr3eQdPBrhI+EY5AqEGY8txdWFHEg8a2czCESv6mLUvh7UwbCnhJyvySUZNxVsEoJLlnzy2sHMMNgboNEFGmELAeVc3t4pa5b/paJUaZgnlIFiTpQ==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCtbwc0st31fTTF+s/rXaerNpYZiDTG7BQ49StjqaYjx4vKCgEAhj+qJSJgALDvQAGgNz+qJ0Z1mW15NlxLac4zJezq2R7sGk9GQ6USiTiMgN6LygoBAIYkYTnKgAC/jN5k"
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
      "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
      "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
  "id": -576460752303421231,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
      "balance": 70000000000000
    },
    {
      "account": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
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
    "from": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
    "to": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
        "from": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
        "to": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
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
    "to": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
        "to": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
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
    "from": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
        "from": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
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
    "from": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
    "meta": 17,
    "to": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
        "from": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
        "meta": 17,
        "to": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
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
    "from": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
    "to": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmPLcXVhRxIPGtnMwhEr+pi1L4e1MGwp4Scr8klGTcVbBaD5Im9DbdojQu4xhsJcGj5NaOV+8axy8xdNnh32Ff5FT6GHk2E=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
          "op": "OffChainTransfer",
          "to": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
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
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZjy3F1YUcSDxrZzMIRK/qYtS+HtTBsKeEnK/JJRk3FWwWg+SJvQ23aI0LuMYbCXBo+TWjlfvGscvMXTZ4d9hX+RU9iUIA3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZjy3F1YUcSDxrZzMIRK/qYtS+HtTBsKeEnK/JJRk3FWwWg+SJvQ23aI0LuMYbCXBo+TWjlfvGscvMXTZ4d9hX+RU9iUIA3",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
          "op": "OffChainTransfer",
          "to": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
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
    "signed_tx": "tx_+NwLAcC41/jVUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAJHajxyvn5acKgi1B/oI/ipW619wT2F1OHgj+ZJBW25Am8jMLpo+IccbVUPiqifBq3w6e8AtA5bhuUrVJod0wDLhI+EY5AqEGY8txdWFHEg8a2czCESv6mLUvh7UwbCnhJyvySUZNxVsFoPkib0Nt2iNC7jGGwlwaPk1o5X7xrHLzF02eHfYV/kVPT2NLYw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAJHajxyvn5acKgi1B/oI/ipW619wT2F1OHgj+ZJBW25Am8jMLpo+IccbVUPiqifBq3w6e8AtA5bhuUrVJod0wDLhI+EY5AqEGY8txdWFHEg8a2czCESv6mLUvh7UwbCnhJyvySUZNxVsFoPkib0Nt2iNC7jGGwlwaPk1o5X7xrHLzF02eHfYV/kVPT2NLYw=="
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAJHajxyvn5acKgi1B/oI/ipW619wT2F1OHgj+ZJBW25Am8jMLpo+IccbVUPiqifBq3w6e8AtA5bhuUrVJod0wDLhI+EY5AqEGY8txdWFHEg8a2czCESv6mLUvh7UwbCnhJyvySUZNxVsFoPkib0Nt2iNC7jGGwlwaPk1o5X7xrHLzF02eHfYV/kVPT2NLYw=="
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
      "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
      "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
  "id": -576460752303421228,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
      "balance": 69999999999999
    },
    {
      "account": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
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
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
  "id": -576460752303421227,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAJHajxyvn5acKgi1B/oI/ipW619wT2F1OHgj+ZJBW25Am8jMLpo+IccbVUPiqifBq3w6e8AtA5bhuUrVJod0wDLhI+EY5AqEGY8txdWFHEg8a2czCESv6mLUvh7UwbCnhJyvySUZNxVsFoPkib0Nt2iNC7jGGwlwaPk1o5X7xrHLzF02eHfYV/kVPT2NLYw==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCtbwc0st31fTTF+s/rXaerNpYZiDTG7BQ49StjqaYjx4vKCgEAhj+qJSJf/7DvQAGgNz+qJ0Z1mW15NlxLac4zJezq2R7sGk9GQ6USiTiMgN6LygoBAIYkYTnKgAHFwWTK"
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
      "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
      "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
  "id": -576460752303421226,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
      "balance": 40000000000001
    },
    {
      "account": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
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
    "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
    "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
        "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
        "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
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
    "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
        "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
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
    "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
        "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
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
    "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
    "meta": 17,
    "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
        "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
        "meta": 17,
        "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
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
    "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
    "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmPLcXVhRxIPGtnMwhEr+pi1L4e1MGwp4Scr8klGTcVbBqCS5Z88trBzDDYG6DRBRphCwHlXN7eKWuW/6WiVGmYJ5fikS2k=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
          "op": "OffChainTransfer",
          "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
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
    "signed_tx": "tx_+JALAfhCuECnQqUl8unUwozDNWOOqhC9NlucHsaOcKPPY/fxYh2Bbsd1Uo0tLaweRmv+YT0a/G4MPrgYzTGMzoC7JO/Nz38KuEj4RjkCoQZjy3F1YUcSDxrZzMIRK/qYtS+HtTBsKeEnK/JJRk3FWwagkuWfPLawcww2Bug0QUaYQsB5Vze3ilrlv+lolRpmCeU/alhC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "signed_tx": "tx_+JALAfhCuECnQqUl8unUwozDNWOOqhC9NlucHsaOcKPPY/fxYh2Bbsd1Uo0tLaweRmv+YT0a/G4MPrgYzTGMzoC7JO/Nz38KuEj4RjkCoQZjy3F1YUcSDxrZzMIRK/qYtS+HtTBsKeEnK/JJRk3FWwagkuWfPLawcww2Bug0QUaYQsB5Vze3ilrlv+lolRpmCeU/alhC",
      "updates": [
        {
          "amount": 1,
          "from": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
          "op": "OffChainTransfer",
          "to": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
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
    "signed_tx": "tx_+NwLAcC41/jVUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAp0KlJfLp1MKMwzVjjqoQvTZbnB7GjnCjz2P38WIdgW7HdVKNLS2sHkZr/mE9GvxuDD64GM0xjM6AuyTvzc9/CrhI+EY5AqEGY8txdWFHEg8a2czCESv6mLUvh7UwbCnhJyvySUZNxVsGoJLlnzy2sHMMNgboNEFGmELAeVc3t4pa5b/paJUaZgnlR0XupQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAp0KlJfLp1MKMwzVjjqoQvTZbnB7GjnCjz2P38WIdgW7HdVKNLS2sHkZr/mE9GvxuDD64GM0xjM6AuyTvzc9/CrhI+EY5AqEGY8txdWFHEg8a2czCESv6mLUvh7UwbCnhJyvySUZNxVsGoJLlnzy2sHMMNgboNEFGmELAeVc3t4pa5b/paJUaZgnlR0XupQ=="
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAp0KlJfLp1MKMwzVjjqoQvTZbnB7GjnCjz2P38WIdgW7HdVKNLS2sHkZr/mE9GvxuDD64GM0xjM6AuyTvzc9/CrhI+EY5AqEGY8txdWFHEg8a2czCESv6mLUvh7UwbCnhJyvySUZNxVsGoJLlnzy2sHMMNgboNEFGmELAeVc3t4pa5b/paJUaZgnlR0XupQ=="
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
      "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
      "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
  "id": -576460752303421223,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_RLFiEZ2Cq165ftSppQwVJ5jCQRBXjY31yPDLRB9WEK8v2qNQo",
      "balance": 40000000000000
    },
    {
      "account": "ak_2KP8cKSPR1Zt6BP3PtdfKqmYGArvp9RDdPz7xdjf6DRa9PNyPL",
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
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
  "id": -576460752303421222,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAa1vBzSy3fV9NMX6z+tdp6s2lhmINMbsFDj1K2OppiPHiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAp0KlJfLp1MKMwzVjjqoQvTZbnB7GjnCjz2P38WIdgW7HdVKNLS2sHkZr/mE9GvxuDD64GM0xjM6AuyTvzc9/CrhI+EY5AqEGY8txdWFHEg8a2czCESv6mLUvh7UwbCnhJyvySUZNxVsGoJLlnzy2sHMMNgboNEFGmELAeVc3t4pa5b/paJUaZgnlR0XupQ==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCtbwc0st31fTTF+s/rXaerNpYZiDTG7BQ49StjqaYjx4vKCgEAhj+qJSJgALDvQAGgNz+qJ0Z1mW15NlxLac4zJezq2R7sGk9GQ6USiTiMgN6LygoBAIYkYTnKgAC/jN5k"
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
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
    "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
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
  "channel_id": "ch_kx84JnGKFSoK2myYCxq1cJ8AmwkiY3bNPGJfRpdVnhjUFufbn",
  "id": -576460752303421220,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
