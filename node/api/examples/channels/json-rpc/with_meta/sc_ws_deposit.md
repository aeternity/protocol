
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
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": "2"
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
      "method": "channels.deposit",
      "params": {
        "amount": "2"
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
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2,
    "meta": [
      "meta 1"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBjGCTVHHgfDoq2BLm+gmDDEVHn5EwSZdEDQMmvONklOUoQFCm/9SX8cM775gxSAtaOd9B2nAnQxV53z02pkXcHhUzwIAhg/AoHKQAKDrSX4JQLPKIqG0UoyoZVXcwnecaj74gU0xhI1kvlj74Qcejmimeg==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
          "op": "OffChainDeposit"
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
  "id": -576460752303423083,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEB+mCxlol310A2DJkOl4krHUGcLw7L4O0ynDsq5+VygeiyR1tGej620J05Vs0J/40P0+ZE1EFVbUJd14T/WpiIAuHT4cjMBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM8CAIYPwKBykACg60l+CUCzyiKhtFKMqGVV3MJ3nGo++IFNMYSNZL5Y++EHHiOIb1U="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423083,
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEB+mCxlol310A2DJkOl4krHUGcLw7L4O0ynDsq5+VygeiyR1tGej620J05Vs0J/40P0+ZE1EFVbUJd14T/WpiIAuHT4cjMBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM8CAIYPwKBykACg60l+CUCzyiKhtFKMqGVV3MJ3nGo++IFNMYSNZL5Y++EHHiOIb1U=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_WLSv76gJGys4tVzQMB8xQdyjDB2JbSb23yX4zFGSr8s8RKxR8",
          "op": "OffChainDeposit"
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
  "id": -576460752303423082,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEB+mCxlol310A2DJkOl4krHUGcLw7L4O0ynDsq5+VygeiyR1tGej620J05Vs0J/40P0+ZE1EFVbUJd14T/WpiIAuED1WqfjhTmpj+1JrIwBt3bk/TG4Gb2XCg+sIN6HwJGMWoWzWoiQIuElXcXrK2CcC2g5zj4I3uPDSvDf4HLJMyYKuHT4cjMBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM8CAIYPwKBykACg60l+CUCzyiKhtFKMqGVV3MJ3nGo++IFNMYSNZL5Y++EHHqqeROg="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423082,
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
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEB+mCxlol310A2DJkOl4krHUGcLw7L4O0ynDsq5+VygeiyR1tGej620J05Vs0J/40P0+ZE1EFVbUJd14T/WpiIAuED1WqfjhTmpj+1JrIwBt3bk/TG4Gb2XCg+sIN6HwJGMWoWzWoiQIuElXcXrK2CcC2g5zj4I3uPDSvDf4HLJMyYKuHT4cjMBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM8CAIYPwKBykACg60l+CUCzyiKhtFKMqGVV3MJ3nGo++IFNMYSNZL5Y++EHHqqeROg=",
      "type": "channel_deposit_tx"
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
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEB+mCxlol310A2DJkOl4krHUGcLw7L4O0ynDsq5+VygeiyR1tGej620J05Vs0J/40P0+ZE1EFVbUJd14T/WpiIAuED1WqfjhTmpj+1JrIwBt3bk/TG4Gb2XCg+sIN6HwJGMWoWzWoiQIuElXcXrK2CcC2g5zj4I3uPDSvDf4HLJMyYKuHT4cjMBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM8CAIYPwKBykACg60l+CUCzyiKhtFKMqGVV3MJ3nGo++IFNMYSNZL5Y++EHHqqeROg=",
      "type": "channel_deposit_tx"
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

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEB+mCxlol310A2DJkOl4krHUGcLw7L4O0ynDsq5+VygeiyR1tGej620J05Vs0J/40P0+ZE1EFVbUJd14T/WpiIAuED1WqfjhTmpj+1JrIwBt3bk/TG4Gb2XCg+sIN6HwJGMWoWzWoiQIuElXcXrK2CcC2g5zj4I3uPDSvDf4HLJMyYKuHT4cjMBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM8CAIYPwKBykACg60l+CUCzyiKhtFKMqGVV3MJ3nGo++IFNMYSNZL5Y++EHHqqeROg=",
      "type": "channel_deposit_tx"
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
      "tx": "tx_+P4LAfiEuEB+mCxlol310A2DJkOl4krHUGcLw7L4O0ynDsq5+VygeiyR1tGej620J05Vs0J/40P0+ZE1EFVbUJd14T/WpiIAuED1WqfjhTmpj+1JrIwBt3bk/TG4Gb2XCg+sIN6HwJGMWoWzWoiQIuElXcXrK2CcC2g5zj4I3uPDSvDf4HLJMyYKuHT4cjMBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM8CAIYPwKBykACg60l+CUCzyiKhtFKMqGVV3MJ3nGo++IFNMYSNZL5Y++EHHqqeROg=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "event": "own_deposit_locked"
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
      "event": "own_deposit_locked"
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "event": "deposit_locked"
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
      "event": "deposit_locked"
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
      "state": "tx_+P4LAfiEuEB+mCxlol310A2DJkOl4krHUGcLw7L4O0ynDsq5+VygeiyR1tGej620J05Vs0J/40P0+ZE1EFVbUJd14T/WpiIAuED1WqfjhTmpj+1JrIwBt3bk/TG4Gb2XCg+sIN6HwJGMWoWzWoiQIuElXcXrK2CcC2g5zj4I3uPDSvDf4HLJMyYKuHT4cjMBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM8CAIYPwKBykACg60l+CUCzyiKhtFKMqGVV3MJ3nGo++IFNMYSNZL5Y++EHHqqeROg="
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
      "state": "tx_+P4LAfiEuEB+mCxlol310A2DJkOl4krHUGcLw7L4O0ynDsq5+VygeiyR1tGej620J05Vs0J/40P0+ZE1EFVbUJd14T/WpiIAuED1WqfjhTmpj+1JrIwBt3bk/TG4Gb2XCg+sIN6HwJGMWoWzWoiQIuElXcXrK2CcC2g5zj4I3uPDSvDf4HLJMyYKuHT4cjMBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM8CAIYPwKBykACg60l+CUCzyiKhtFKMqGVV3MJ3nGo++IFNMYSNZL5Y++EHHqqeROg="
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
    "info": "Hello",
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
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
        "info": "Hello back",
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
  "method": "channels.deposit",
  "params": {
    "amount": "2"
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
      "method": "channels.deposit",
      "params": {
        "amount": "2"
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
  "method": "channels.message",
  "params": {
    "info": "Hello",
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
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
        "info": "Hello back",
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
  "method": "channels.deposit",
  "params": {
    "amount": 2,
    "meta": [
      "meta 1"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBjGCTVHHgfDoq2BLm+gmDDEVHn5EwSZdEDQMmvONklOUoQGqCRBCJUf6UearceRYSaOFJedS41WJfe3eptJ9mTkcogIAhg/AoHKQAKAq0RBncwRuBT9kgztch96ZLAPsxuXv1eSS4tqhM3AOpAgL8McMfg==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
          "op": "OffChainDeposit"
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
  "id": -576460752303423081,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEC04ZtuUDQUGgSoE/OzZg/EWdzfBTsCKTzLRXyAOA90G9XRtQrSgkf82ueEqi/yf2ogw5jvdR0s+Xvlhk2NurgFuHT4cjMBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBqgkQQiVH+lHmq3HkWEmjhSXnUuNViX3t3qbSfZk5HKICAIYPwKBykACgKtEQZ3MEbgU/ZIM7XIfemSwD7Mbl79XkkuLaoTNwDqQIC6FuvHI="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423081,
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
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEC04ZtuUDQUGgSoE/OzZg/EWdzfBTsCKTzLRXyAOA90G9XRtQrSgkf82ueEqi/yf2ogw5jvdR0s+Xvlhk2NurgFuHT4cjMBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBqgkQQiVH+lHmq3HkWEmjhSXnUuNViX3t3qbSfZk5HKICAIYPwKBykACgKtEQZ3MEbgU/ZIM7XIfemSwD7Mbl79XkkuLaoTNwDqQIC6FuvHI=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB",
          "op": "OffChainDeposit"
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
  "id": -576460752303423080,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBAm8GZqVVS1mr13gkJ3dqVPh/VjtlS48gHTZDSGhvlr0j1Bxygp6ELZWH3dfM7WceHLBi4VSrQYo6+aEf+GK8GuEC04ZtuUDQUGgSoE/OzZg/EWdzfBTsCKTzLRXyAOA90G9XRtQrSgkf82ueEqi/yf2ogw5jvdR0s+Xvlhk2NurgFuHT4cjMBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBqgkQQiVH+lHmq3HkWEmjhSXnUuNViX3t3qbSfZk5HKICAIYPwKBykACgKtEQZ3MEbgU/ZIM7XIfemSwD7Mbl79XkkuLaoTNwDqQIC1LoPzM="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423080,
  "jsonrpc": "2.0",
  "result": "ok",
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
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEBAm8GZqVVS1mr13gkJ3dqVPh/VjtlS48gHTZDSGhvlr0j1Bxygp6ELZWH3dfM7WceHLBi4VSrQYo6+aEf+GK8GuEC04ZtuUDQUGgSoE/OzZg/EWdzfBTsCKTzLRXyAOA90G9XRtQrSgkf82ueEqi/yf2ogw5jvdR0s+Xvlhk2NurgFuHT4cjMBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBqgkQQiVH+lHmq3HkWEmjhSXnUuNViX3t3qbSfZk5HKICAIYPwKBykACgKtEQZ3MEbgU/ZIM7XIfemSwD7Mbl79XkkuLaoTNwDqQIC1LoPzM=",
      "type": "channel_deposit_tx"
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
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEBAm8GZqVVS1mr13gkJ3dqVPh/VjtlS48gHTZDSGhvlr0j1Bxygp6ELZWH3dfM7WceHLBi4VSrQYo6+aEf+GK8GuEC04ZtuUDQUGgSoE/OzZg/EWdzfBTsCKTzLRXyAOA90G9XRtQrSgkf82ueEqi/yf2ogw5jvdR0s+Xvlhk2NurgFuHT4cjMBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBqgkQQiVH+lHmq3HkWEmjhSXnUuNViX3t3qbSfZk5HKICAIYPwKBykACgKtEQZ3MEbgU/ZIM7XIfemSwD7Mbl79XkkuLaoTNwDqQIC1LoPzM=",
      "type": "channel_deposit_tx"
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
    "info": "Hello",
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
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
        "info": "Hello back",
        "to": "ak_2HtKvJywsEFmLYHirdUL2bDdiCt3F2aShvr6cMMCaAfMC3gJHB"
      }
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
      "tx": "tx_+P4LAfiEuEBAm8GZqVVS1mr13gkJ3dqVPh/VjtlS48gHTZDSGhvlr0j1Bxygp6ELZWH3dfM7WceHLBi4VSrQYo6+aEf+GK8GuEC04ZtuUDQUGgSoE/OzZg/EWdzfBTsCKTzLRXyAOA90G9XRtQrSgkf82ueEqi/yf2ogw5jvdR0s+Xvlhk2NurgFuHT4cjMBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBqgkQQiVH+lHmq3HkWEmjhSXnUuNViX3t3qbSfZk5HKICAIYPwKBykACgKtEQZ3MEbgU/ZIM7XIfemSwD7Mbl79XkkuLaoTNwDqQIC1LoPzM=",
      "type": "channel_deposit_tx"
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
      "tx": "tx_+P4LAfiEuEBAm8GZqVVS1mr13gkJ3dqVPh/VjtlS48gHTZDSGhvlr0j1Bxygp6ELZWH3dfM7WceHLBi4VSrQYo6+aEf+GK8GuEC04ZtuUDQUGgSoE/OzZg/EWdzfBTsCKTzLRXyAOA90G9XRtQrSgkf82ueEqi/yf2ogw5jvdR0s+Xvlhk2NurgFuHT4cjMBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBqgkQQiVH+lHmq3HkWEmjhSXnUuNViX3t3qbSfZk5HKICAIYPwKBykACgKtEQZ3MEbgU/ZIM7XIfemSwD7Mbl79XkkuLaoTNwDqQIC1LoPzM=",
      "type": "channel_deposit_tx"
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
      "event": "own_deposit_locked"
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "event": "deposit_locked"
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
      "event": "deposit_locked"
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
      "state": "tx_+P4LAfiEuEBAm8GZqVVS1mr13gkJ3dqVPh/VjtlS48gHTZDSGhvlr0j1Bxygp6ELZWH3dfM7WceHLBi4VSrQYo6+aEf+GK8GuEC04ZtuUDQUGgSoE/OzZg/EWdzfBTsCKTzLRXyAOA90G9XRtQrSgkf82ueEqi/yf2ogw5jvdR0s+Xvlhk2NurgFuHT4cjMBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBqgkQQiVH+lHmq3HkWEmjhSXnUuNViX3t3qbSfZk5HKICAIYPwKBykACgKtEQZ3MEbgU/ZIM7XIfemSwD7Mbl79XkkuLaoTNwDqQIC1LoPzM="
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
      "state": "tx_+P4LAfiEuEBAm8GZqVVS1mr13gkJ3dqVPh/VjtlS48gHTZDSGhvlr0j1Bxygp6ELZWH3dfM7WceHLBi4VSrQYo6+aEf+GK8GuEC04ZtuUDQUGgSoE/OzZg/EWdzfBTsCKTzLRXyAOA90G9XRtQrSgkf82ueEqi/yf2ogw5jvdR0s+Xvlhk2NurgFuHT4cjMBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBqgkQQiVH+lHmq3HkWEmjhSXnUuNViX3t3qbSfZk5HKICAIYPwKBykACgKtEQZ3MEbgU/ZIM7XIfemSwD7Mbl79XkkuLaoTNwDqQIC1LoPzM="
    }
  },
  "version": 1
}
```
