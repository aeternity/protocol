
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
  "method": "channels.withdraw",
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
      "method": "channels.withdraw",
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
  "method": "channels.withdraw",
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
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBjGCTVHHgfDoq2BLm+gmDDEVHn5EwSZdEDQMmvONklOUoQFCm/9SX8cM775gxSAtaOd9B2nAnQxV53z02pkXcHhUzwIAhg/AoHKQAKCkTLhDiqRotUAwB4OEIixjCOeObq+49In/ESXyi688Igkf61+Pzg==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303423079,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEAYIIyFAySJr2g2+Zf6rXEUnslYEHY2A1+6UFIaA/5u3MQBF1J9HCUQJgrNK/xFC06K/xS6/LfeLsC0KFfTtHcMuHT4cjQBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM8CAIYPwKBykACgpEy4Q4qkaLVAMAeDhCIsYwjnjm6vuPSJ/xEl8ouvPCIJH2653h0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423079,
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
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEAYIIyFAySJr2g2+Zf6rXEUnslYEHY2A1+6UFIaA/5u3MQBF1J9HCUQJgrNK/xFC06K/xS6/LfeLsC0KFfTtHcMuHT4cjQBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM8CAIYPwKBykACgpEy4Q4qkaLVAMAeDhCIsYwjnjm6vuPSJ/xEl8ouvPCIJH2653h0=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303423078,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEAYIIyFAySJr2g2+Zf6rXEUnslYEHY2A1+6UFIaA/5u3MQBF1J9HCUQJgrNK/xFC06K/xS6/LfeLsC0KFfTtHcMuECoBqjlAvD8nDW15B3lchwFc0NJnDguL+u3g8Jrdk2uAjTCm2c2xl4JIY3QuP2ItPF5rom98nqYjUmBl/a7QssDuHT4cjQBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM8CAIYPwKBykACgpEy4Q4qkaLVAMAeDhCIsYwjnjm6vuPSJ/xEl8ouvPCIJH2mSwpo="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423078,
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
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEAYIIyFAySJr2g2+Zf6rXEUnslYEHY2A1+6UFIaA/5u3MQBF1J9HCUQJgrNK/xFC06K/xS6/LfeLsC0KFfTtHcMuECoBqjlAvD8nDW15B3lchwFc0NJnDguL+u3g8Jrdk2uAjTCm2c2xl4JIY3QuP2ItPF5rom98nqYjUmBl/a7QssDuHT4cjQBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM8CAIYPwKBykACgpEy4Q4qkaLVAMAeDhCIsYwjnjm6vuPSJ/xEl8ouvPCIJH2mSwpo=",
      "type": "channel_withdraw_tx"
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
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEAYIIyFAySJr2g2+Zf6rXEUnslYEHY2A1+6UFIaA/5u3MQBF1J9HCUQJgrNK/xFC06K/xS6/LfeLsC0KFfTtHcMuECoBqjlAvD8nDW15B3lchwFc0NJnDguL+u3g8Jrdk2uAjTCm2c2xl4JIY3QuP2ItPF5rom98nqYjUmBl/a7QssDuHT4cjQBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM8CAIYPwKBykACgpEy4Q4qkaLVAMAeDhCIsYwjnjm6vuPSJ/xEl8ouvPCIJH2mSwpo=",
      "type": "channel_withdraw_tx"
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
      "tx": "tx_+P4LAfiEuEAYIIyFAySJr2g2+Zf6rXEUnslYEHY2A1+6UFIaA/5u3MQBF1J9HCUQJgrNK/xFC06K/xS6/LfeLsC0KFfTtHcMuECoBqjlAvD8nDW15B3lchwFc0NJnDguL+u3g8Jrdk2uAjTCm2c2xl4JIY3QuP2ItPF5rom98nqYjUmBl/a7QssDuHT4cjQBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM8CAIYPwKBykACgpEy4Q4qkaLVAMAeDhCIsYwjnjm6vuPSJ/xEl8ouvPCIJH2mSwpo=",
      "type": "channel_withdraw_tx"
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
      "tx": "tx_+P4LAfiEuEAYIIyFAySJr2g2+Zf6rXEUnslYEHY2A1+6UFIaA/5u3MQBF1J9HCUQJgrNK/xFC06K/xS6/LfeLsC0KFfTtHcMuECoBqjlAvD8nDW15B3lchwFc0NJnDguL+u3g8Jrdk2uAjTCm2c2xl4JIY3QuP2ItPF5rom98nqYjUmBl/a7QssDuHT4cjQBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM8CAIYPwKBykACgpEy4Q4qkaLVAMAeDhCIsYwjnjm6vuPSJ/xEl8ouvPCIJH2mSwpo=",
      "type": "channel_withdraw_tx"
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
      "event": "own_withdraw_locked"
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
      "event": "own_withdraw_locked"
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
      "event": "withdraw_locked"
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
      "event": "withdraw_locked"
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
      "state": "tx_+P4LAfiEuEAYIIyFAySJr2g2+Zf6rXEUnslYEHY2A1+6UFIaA/5u3MQBF1J9HCUQJgrNK/xFC06K/xS6/LfeLsC0KFfTtHcMuECoBqjlAvD8nDW15B3lchwFc0NJnDguL+u3g8Jrdk2uAjTCm2c2xl4JIY3QuP2ItPF5rom98nqYjUmBl/a7QssDuHT4cjQBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM8CAIYPwKBykACgpEy4Q4qkaLVAMAeDhCIsYwjnjm6vuPSJ/xEl8ouvPCIJH2mSwpo="
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
      "state": "tx_+P4LAfiEuEAYIIyFAySJr2g2+Zf6rXEUnslYEHY2A1+6UFIaA/5u3MQBF1J9HCUQJgrNK/xFC06K/xS6/LfeLsC0KFfTtHcMuECoBqjlAvD8nDW15B3lchwFc0NJnDguL+u3g8Jrdk2uAjTCm2c2xl4JIY3QuP2ItPF5rom98nqYjUmBl/a7QssDuHT4cjQBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBQpv/Ul/HDO++YMUgLWjnfQdpwJ0MVed89NqZF3B4VM8CAIYPwKBykACgpEy4Q4qkaLVAMAeDhCIsYwjnjm6vuPSJ/xEl8ouvPCIJH2mSwpo="
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
  "method": "channels.withdraw",
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
      "method": "channels.withdraw",
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
  "method": "channels.withdraw",
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
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBjGCTVHHgfDoq2BLm+gmDDEVHn5EwSZdEDQMmvONklOUoQGqCRBCJUf6UearceRYSaOFJedS41WJfe3eptJ9mTkcogIAhg/AoHKQAKAQ7TXOxjjtnNsz0HcpVXZqKYh7hxLNRQoG2hwEzOp5VAoM4G88xg==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303423077,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuED1DZ5mtbcJX+9I94W708j5oHm9QdJxWIk2vEluf18zZVd+ovYL+MMx1oBR6BvU4RrTR/1VzywO7J7EpuDCtyYDuHT4cjQBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBqgkQQiVH+lHmq3HkWEmjhSXnUuNViX3t3qbSfZk5HKICAIYPwKBykACgEO01zsY47ZzbM9B3KVV2aimIe4cSzUUKBtocBMzqeVQKDHAx9i4="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423077,
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
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
    "data": {
      "signed_tx": "tx_+LwLAfhCuED1DZ5mtbcJX+9I94W708j5oHm9QdJxWIk2vEluf18zZVd+ovYL+MMx1oBR6BvU4RrTR/1VzywO7J7EpuDCtyYDuHT4cjQBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBqgkQQiVH+lHmq3HkWEmjhSXnUuNViX3t3qbSfZk5HKICAIYPwKBykACgEO01zsY47ZzbM9B3KVV2aimIe4cSzUUKBtocBMzqeVQKDHAx9i4=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303423076,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEDchQgPhH0bAIxN55Ua8b6cK65fTmAKYFoosqlsMAsA1WhPn3tJ/gl82CdUKtJFDoQlVVA5Tv9DU6b0GaQmhi4LuED1DZ5mtbcJX+9I94W708j5oHm9QdJxWIk2vEluf18zZVd+ovYL+MMx1oBR6BvU4RrTR/1VzywO7J7EpuDCtyYDuHT4cjQBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBqgkQQiVH+lHmq3HkWEmjhSXnUuNViX3t3qbSfZk5HKICAIYPwKBykACgEO01zsY47ZzbM9B3KVV2aimIe4cSzUUKBtocBMzqeVQKDIWJOlI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_NoeAX1g4kRm7cNpPRs47X3HT9yurheDuqekAr6CDVT6KoB9az",
  "id": -576460752303423076,
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
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEDchQgPhH0bAIxN55Ua8b6cK65fTmAKYFoosqlsMAsA1WhPn3tJ/gl82CdUKtJFDoQlVVA5Tv9DU6b0GaQmhi4LuED1DZ5mtbcJX+9I94W708j5oHm9QdJxWIk2vEluf18zZVd+ovYL+MMx1oBR6BvU4RrTR/1VzywO7J7EpuDCtyYDuHT4cjQBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBqgkQQiVH+lHmq3HkWEmjhSXnUuNViX3t3qbSfZk5HKICAIYPwKBykACgEO01zsY47ZzbM9B3KVV2aimIe4cSzUUKBtocBMzqeVQKDIWJOlI=",
      "type": "channel_withdraw_tx"
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
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEDchQgPhH0bAIxN55Ua8b6cK65fTmAKYFoosqlsMAsA1WhPn3tJ/gl82CdUKtJFDoQlVVA5Tv9DU6b0GaQmhi4LuED1DZ5mtbcJX+9I94W708j5oHm9QdJxWIk2vEluf18zZVd+ovYL+MMx1oBR6BvU4RrTR/1VzywO7J7EpuDCtyYDuHT4cjQBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBqgkQQiVH+lHmq3HkWEmjhSXnUuNViX3t3qbSfZk5HKICAIYPwKBykACgEO01zsY47ZzbM9B3KVV2aimIe4cSzUUKBtocBMzqeVQKDIWJOlI=",
      "type": "channel_withdraw_tx"
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
      "tx": "tx_+P4LAfiEuEDchQgPhH0bAIxN55Ua8b6cK65fTmAKYFoosqlsMAsA1WhPn3tJ/gl82CdUKtJFDoQlVVA5Tv9DU6b0GaQmhi4LuED1DZ5mtbcJX+9I94W708j5oHm9QdJxWIk2vEluf18zZVd+ovYL+MMx1oBR6BvU4RrTR/1VzywO7J7EpuDCtyYDuHT4cjQBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBqgkQQiVH+lHmq3HkWEmjhSXnUuNViX3t3qbSfZk5HKICAIYPwKBykACgEO01zsY47ZzbM9B3KVV2aimIe4cSzUUKBtocBMzqeVQKDIWJOlI=",
      "type": "channel_withdraw_tx"
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
      "tx": "tx_+P4LAfiEuEDchQgPhH0bAIxN55Ua8b6cK65fTmAKYFoosqlsMAsA1WhPn3tJ/gl82CdUKtJFDoQlVVA5Tv9DU6b0GaQmhi4LuED1DZ5mtbcJX+9I94W708j5oHm9QdJxWIk2vEluf18zZVd+ovYL+MMx1oBR6BvU4RrTR/1VzywO7J7EpuDCtyYDuHT4cjQBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBqgkQQiVH+lHmq3HkWEmjhSXnUuNViX3t3qbSfZk5HKICAIYPwKBykACgEO01zsY47ZzbM9B3KVV2aimIe4cSzUUKBtocBMzqeVQKDIWJOlI=",
      "type": "channel_withdraw_tx"
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
      "event": "own_withdraw_locked"
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
      "event": "withdraw_locked"
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
      "event": "own_withdraw_locked"
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
      "event": "withdraw_locked"
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
      "state": "tx_+P4LAfiEuEDchQgPhH0bAIxN55Ua8b6cK65fTmAKYFoosqlsMAsA1WhPn3tJ/gl82CdUKtJFDoQlVVA5Tv9DU6b0GaQmhi4LuED1DZ5mtbcJX+9I94W708j5oHm9QdJxWIk2vEluf18zZVd+ovYL+MMx1oBR6BvU4RrTR/1VzywO7J7EpuDCtyYDuHT4cjQBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBqgkQQiVH+lHmq3HkWEmjhSXnUuNViX3t3qbSfZk5HKICAIYPwKBykACgEO01zsY47ZzbM9B3KVV2aimIe4cSzUUKBtocBMzqeVQKDIWJOlI="
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
      "state": "tx_+P4LAfiEuEDchQgPhH0bAIxN55Ua8b6cK65fTmAKYFoosqlsMAsA1WhPn3tJ/gl82CdUKtJFDoQlVVA5Tv9DU6b0GaQmhi4LuED1DZ5mtbcJX+9I94W708j5oHm9QdJxWIk2vEluf18zZVd+ovYL+MMx1oBR6BvU4RrTR/1VzywO7J7EpuDCtyYDuHT4cjQBoQYxgk1Rx4Hw6KtgS5voJgwxFR5+RMEmXRA0DJrzjZJTlKEBqgkQQiVH+lHmq3HkWEmjhSXnUuNViX3t3qbSfZk5HKICAIYPwKBykACgEO01zsY47ZzbM9B3KVV2aimIe4cSzUUKBtocBMzqeVQKDIWJOlI="
    }
  },
  "version": 1
}
```
