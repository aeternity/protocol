
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=initiator
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
      "fsm_id": "ba_ed/pAczaDmsqugmDbv0fEPuOynd4zoAWHs1i+OwQNvTZqLoA"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=responder
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
      "fsm_id": "ba_bV3putDkdDTwlq/AGTSgj766LIwXs0aXmWMoYAJnLmYZsqfO"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBuRfl/iQ=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422107,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEBn7026d6WEEklGrokECDqFLEO7AeOp+lc/4p7UhgzFAjckI1GvQVKztKhTVsGEecbJLIM7u8TxPZDH694YZAIKuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgbk1wSfu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422107,
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
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_bV3putDkdDTwlq/AGTSgj766LIwXs0aXmWMoYAJnLmYZsqfO"
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
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEBn7026d6WEEklGrokECDqFLEO7AeOp+lc/4p7UhgzFAjckI1GvQVKztKhTVsGEecbJLIM7u8TxPZDH694YZAIKuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgbk1wSfu",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422106,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAIalKcGME1DrOw8cIe4eNY4i3U+Lgtb5wIxQNB/ZfTEZJ6C+YL1sPgXVjxsRzBKVxcPbOrq07Mu749t2nHFK9BrhAZ+9NunelhBJJRq6JBAg6hSxDuwHjqfpXP+Ke1IYMxQI3JCNRr0FSs7SoU1bBhHnGySyDO7vE8T2Qx+veGGQCCriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG5gqZFUw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
  "id": -576460752303422106,
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
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAIalKcGME1DrOw8cIe4eNY4i3U+Lgtb5wIxQNB/ZfTEZJ6C+YL1sPgXVjxsRzBKVxcPbOrq07Mu749t2nHFK9BrhAZ+9NunelhBJJRq6JBAg6hSxDuwHjqfpXP+Ke1IYMxQI3JCNRr0FSs7SoU1bBhHnGySyDO7vE8T2Qx+veGGQCCriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG5gqZFUw==",
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
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_ed/pAczaDmsqugmDbv0fEPuOynd4zoAWHs1i+OwQNvTZqLoA"
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
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAIalKcGME1DrOw8cIe4eNY4i3U+Lgtb5wIxQNB/ZfTEZJ6C+YL1sPgXVjxsRzBKVxcPbOrq07Mu749t2nHFK9BrhAZ+9NunelhBJJRq6JBAg6hSxDuwHjqfpXP+Ke1IYMxQI3JCNRr0FSs7SoU1bBhHnGySyDO7vE8T2Qx+veGGQCCriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG5gqZFUw==",
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
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAIalKcGME1DrOw8cIe4eNY4i3U+Lgtb5wIxQNB/ZfTEZJ6C+YL1sPgXVjxsRzBKVxcPbOrq07Mu749t2nHFK9BrhAZ+9NunelhBJJRq6JBAg6hSxDuwHjqfpXP+Ke1IYMxQI3JCNRr0FSs7SoU1bBhHnGySyDO7vE8T2Qx+veGGQCCriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG5gqZFUw==",
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
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAIalKcGME1DrOw8cIe4eNY4i3U+Lgtb5wIxQNB/ZfTEZJ6C+YL1sPgXVjxsRzBKVxcPbOrq07Mu749t2nHFK9BrhAZ+9NunelhBJJRq6JBAg6hSxDuwHjqfpXP+Ke1IYMxQI3JCNRr0FSs7SoU1bBhHnGySyDO7vE8T2Qx+veGGQCCriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG5gqZFUw==",
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
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
    "data": {
      "message": {
        "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "info": "Hello",
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
    "data": {
      "message": {
        "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "info": "Hello back",
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422105,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
  "id": -576460752303422105,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999999
    },
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
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
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
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
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
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
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
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
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
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
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
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
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
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
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
    "data": {
      "state": "tx_+QEOCwH4hLhAIalKcGME1DrOw8cIe4eNY4i3U+Lgtb5wIxQNB/ZfTEZJ6C+YL1sPgXVjxsRzBKVxcPbOrq07Mu749t2nHFK9BrhAZ+9NunelhBJJRq6JBAg6hSxDuwHjqfpXP+Ke1IYMxQI3JCNRr0FSs7SoU1bBhHnGySyDO7vE8T2Qx+veGGQCCriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG5gqZFUw=="
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
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
    "data": {
      "state": "tx_+QEOCwH4hLhAIalKcGME1DrOw8cIe4eNY4i3U+Lgtb5wIxQNB/ZfTEZJ6C+YL1sPgXVjxsRzBKVxcPbOrq07Mu749t2nHFK9BrhAZ+9NunelhBJJRq6JBAg6hSxDuwHjqfpXP+Ke1IYMxQI3JCNRr0FSs7SoU1bBhHnGySyDO7vE8T2Qx+veGGQCCriE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG5gqZFUw=="
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
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzNAGhBjzKxIEBOEQQxrPRon2uItDHWe6Ym+/HE6auG6QEGTDSoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQIAhg/FSIpYAKDc0aEz/UgoEcs4ajohf9X9BGhuePf6GLqnUld1F+cQwQKBupmVbZg=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "method": "channels.withdraw_tx",
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
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
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
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBjzKxIEBOEQQxrPRon2uItDHWe6Ym+/HE6auG6QEGTDSoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQIAhg/AoHKQAKA5h8lYmnwxnMmzI9HJYz8WeQqOJ0lIGp/4HghPxzVzOQJBsFYzpg==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
  "method": "channels.withdraw_tx",
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
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
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
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzNAGhBjzKxIEBOEQQxrPRon2uItDHWe6Ym+/HE6auG6QEGTDSoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQIAhg/FSIpYAKDc0aEz/UgoEcs4ajohf9X9BGhuePf6GLqnUld1F+cQwQKBupmVbZg=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "id": -576460752303422104,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+L0LAfhCuEBlSFI585Fts9SnwznKB/WHq43v/cDorriYU99M0yFAHbLRPslYvazP5kY0RzXvk7X35AuF5PVy1iI7CsfIWaALuHX4czQBoQY8ysSBAThEEMaz0aJ9riLQx1numJvvxxOmrhukBBkw0qEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUiKWACg3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECgbqiDcYa"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
  "id": -576460752303422104,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
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
      "method": "channels.withdraw_tx",
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
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
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
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
    "data": {
      "signed_tx": "tx_+L0LAfhCuEBlSFI585Fts9SnwznKB/WHq43v/cDorriYU99M0yFAHbLRPslYvazP5kY0RzXvk7X35AuF5PVy1iI7CsfIWaALuHX4czQBoQY8ysSBAThEEMaz0aJ9riLQx1numJvvxxOmrhukBBkw0qEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUiKWACg3NGhM/1IKBHLOGo6IX/V/QRobnj3+hi6p1JXdRfnEMECgbqiDcYa",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "method": "channels.withdraw_ack",
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
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
    "data": {
      "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
      "error_code": 42,
      "error_msg": "unknown",
      "round": 1
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422103,
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
  "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
  "id": -576460752303422103,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422102,
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
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
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
    "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
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
  "channel_id": "ch_TmrPoF1up4eu9WU9wkyBirjknaPJy5SseZKKNTLoD8C32CqtT",
  "id": -576460752303422102,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
