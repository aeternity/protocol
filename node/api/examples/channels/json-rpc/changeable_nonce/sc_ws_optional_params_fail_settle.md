
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
      "fsm_id": "ba_028ZQZWA6RG23wdpFx1g1PRfe65tOTTcmfolCXCsDE8HtwbJ"
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
      "fsm_id": "ba_V3kDQnNzAjzd4oOWIe3q/SJ8bCHZsQkQeVkSmWiNV2oFaSyi"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBs2EqgeY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422145,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEAUft+7dLD9iIqd1IzIc4OjeDg+yLExPrs30S+ZdZLDFFQm9h6vVE7jLXWcMa5lZox/wRvwJvkhkZomKSrgJbgOuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgbMbSR4H"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422145,
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_V3kDQnNzAjzd4oOWIe3q/SJ8bCHZsQkQeVkSmWiNV2oFaSyi"
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEAUft+7dLD9iIqd1IzIc4OjeDg+yLExPrs30S+ZdZLDFFQm9h6vVE7jLXWcMa5lZox/wRvwJvkhkZomKSrgJbgOuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgbMbSR4H",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422144,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAFH7fu3Sw/YiKndSMyHODo3g4PsixMT67N9EvmXWSwxRUJvYer1RO4y11nDGuZWaMf8Eb8Cb5IZGaJikq4CW4DrhAhSKhQlIeh9FES81mRAVwSgl9OZFL9HSayQhZw6jLoTptbEvs6YWqHsPURXI0GaQAfAyJE1C9QaBB9a+969iwDLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGzm1pdvA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
  "id": -576460752303422144,
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAFH7fu3Sw/YiKndSMyHODo3g4PsixMT67N9EvmXWSwxRUJvYer1RO4y11nDGuZWaMf8Eb8Cb5IZGaJikq4CW4DrhAhSKhQlIeh9FES81mRAVwSgl9OZFL9HSayQhZw6jLoTptbEvs6YWqHsPURXI0GaQAfAyJE1C9QaBB9a+969iwDLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGzm1pdvA==",
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_028ZQZWA6RG23wdpFx1g1PRfe65tOTTcmfolCXCsDE8HtwbJ"
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAFH7fu3Sw/YiKndSMyHODo3g4PsixMT67N9EvmXWSwxRUJvYer1RO4y11nDGuZWaMf8Eb8Cb5IZGaJikq4CW4DrhAhSKhQlIeh9FES81mRAVwSgl9OZFL9HSayQhZw6jLoTptbEvs6YWqHsPURXI0GaQAfAyJE1C9QaBB9a+969iwDLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGzm1pdvA==",
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAFH7fu3Sw/YiKndSMyHODo3g4PsixMT67N9EvmXWSwxRUJvYer1RO4y11nDGuZWaMf8Eb8Cb5IZGaJikq4CW4DrhAhSKhQlIeh9FES81mRAVwSgl9OZFL9HSayQhZw6jLoTptbEvs6YWqHsPURXI0GaQAfAyJE1C9QaBB9a+969iwDLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGzm1pdvA==",
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAFH7fu3Sw/YiKndSMyHODo3g4PsixMT67N9EvmXWSwxRUJvYer1RO4y11nDGuZWaMf8Eb8Cb5IZGaJikq4CW4DrhAhSKhQlIeh9FES81mRAVwSgl9OZFL9HSayQhZw6jLoTptbEvs6YWqHsPURXI0GaQAfAyJE1C9QaBB9a+969iwDLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGzm1pdvA==",
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "message": {
        "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "message": {
        "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
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
  "id": -576460752303422143,
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
  "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
  "id": -576460752303422143,
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "state": "tx_+QEOCwH4hLhAFH7fu3Sw/YiKndSMyHODo3g4PsixMT67N9EvmXWSwxRUJvYer1RO4y11nDGuZWaMf8Eb8Cb5IZGaJikq4CW4DrhAhSKhQlIeh9FES81mRAVwSgl9OZFL9HSayQhZw6jLoTptbEvs6YWqHsPURXI0GaQAfAyJE1C9QaBB9a+969iwDLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGzm1pdvA=="
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "state": "tx_+QEOCwH4hLhAFH7fu3Sw/YiKndSMyHODo3g4PsixMT67N9EvmXWSwxRUJvYer1RO4y11nDGuZWaMf8Eb8Cb5IZGaJikq4CW4DrhAhSKhQlIeh9FES81mRAVwSgl9OZFL9HSayQhZw6jLoTptbEvs6YWqHsPURXI0GaQAfAyJE1C9QaBB9a+969iwDLiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGzm1pdvA=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422142,
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
  "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
  "id": -576460752303422142,
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

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnJdMX6kmvn4FLBOXDi+smZzddL77QlHswUGjdzWtGdeAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCytrNAwI=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainTransfer",
          "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
  "id": -576460752303422141,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBNkkhfT6sqg4SqGI2hJZdVUgNDjveqho9ZZGW6RpYoP73XmuoWPIUZSdq735LATuAw7QsvhtrOakLwdkzi+vwCuEj4RjkCoQZyXTF+pJr5+BSwTlw4vrJmc3XS++0JR7MFBo3c1rRnXgKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqtttjI"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
  "id": -576460752303422141,
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBNkkhfT6sqg4SqGI2hJZdVUgNDjveqho9ZZGW6RpYoP73XmuoWPIUZSdq735LATuAw7QsvhtrOakLwdkzi+vwCuEj4RjkCoQZyXTF+pJr5+BSwTlw4vrJmc3XS++0JR7MFBo3c1rRnXgKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqtttjI",
      "updates": [
        {
          "amount": 1,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainTransfer",
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
  "id": -576460752303422140,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAsF1KKwu1yL7x1fAkQSBUBOVOszL3JcTuNUN/sVoJiBLZoVuVx2nzNCxe+TTxd7U2s1Kzcn95zIwSZe3f6CmcEuEBNkkhfT6sqg4SqGI2hJZdVUgNDjveqho9ZZGW6RpYoP73XmuoWPIUZSdq735LATuAw7QsvhtrOakLwdkzi+vwCuEj4RjkCoQZyXTF+pJr5+BSwTlw4vrJmc3XS++0JR7MFBo3c1rRnXgKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsq6mTUe"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
  "id": -576460752303422140,
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "state": "tx_+NILAfiEuEAsF1KKwu1yL7x1fAkQSBUBOVOszL3JcTuNUN/sVoJiBLZoVuVx2nzNCxe+TTxd7U2s1Kzcn95zIwSZe3f6CmcEuEBNkkhfT6sqg4SqGI2hJZdVUgNDjveqho9ZZGW6RpYoP73XmuoWPIUZSdq735LATuAw7QsvhtrOakLwdkzi+vwCuEj4RjkCoQZyXTF+pJr5+BSwTlw4vrJmc3XS++0JR7MFBo3c1rRnXgKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsq6mTUe"
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "state": "tx_+NILAfiEuEAsF1KKwu1yL7x1fAkQSBUBOVOszL3JcTuNUN/sVoJiBLZoVuVx2nzNCxe+TTxd7U2s1Kzcn95zIwSZe3f6CmcEuEBNkkhfT6sqg4SqGI2hJZdVUgNDjveqho9ZZGW6RpYoP73XmuoWPIUZSdq735LATuAw7QsvhtrOakLwdkzi+vwCuEj4RjkCoQZyXTF+pJr5+BSwTlw4vrJmc3XS++0JR7MFBo3c1rRnXgKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsq6mTUe"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422139,
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
  "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
  "id": -576460752303422139,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999998
    },
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422138,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
  "id": -576460752303422138,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAsF1KKwu1yL7x1fAkQSBUBOVOszL3JcTuNUN/sVoJiBLZoVuVx2nzNCxe+TTxd7U2s1Kzcn95zIwSZe3f6CmcEuEBNkkhfT6sqg4SqGI2hJZdVUgNDjveqho9ZZGW6RpYoP73XmuoWPIUZSdq735LATuAw7QsvhtrOakLwdkzi+vwCuEj4RjkCoQZyXTF+pJr5+BSwTlw4vrJmc3XS++0JR7MFBo3c1rRnXgKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsq6mTUe",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422137,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
  "id": -576460752303422137,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000002
    },
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
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
    "amount": 1,
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnJdMX6kmvn4FLBOXDi+smZzddL77QlHswUGjdzWtGdeA6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rogkwrw=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
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
  "id": -576460752303422136,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB12mjQWMitJLhf8aU6KrV3V7ZpS5gmzxTurnLtvsZzhLvZWgSqJaZEIgg7FoYx/Vz5WWHNxxfupABCMQ2JAVkJuEj4RjkCoQZyXTF+pJr5+BSwTlw4vrJmc3XS++0JR7MFBo3c1rRnXgOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbdMOLD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
  "id": -576460752303422136,
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB12mjQWMitJLhf8aU6KrV3V7ZpS5gmzxTurnLtvsZzhLvZWgSqJaZEIgg7FoYx/Vz5WWHNxxfupABCMQ2JAVkJuEj4RjkCoQZyXTF+pJr5+BSwTlw4vrJmc3XS++0JR7MFBo3c1rRnXgOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbdMOLD",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
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
  "id": -576460752303422135,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBx39kZRlNZIw56hfly7o6mqda2IBuIACLqvcSsq5XR5cxD2GvTJxDJR36oSYBQJGTqgCKTdWaEjLCTfjuqCmsLuEB12mjQWMitJLhf8aU6KrV3V7ZpS5gmzxTurnLtvsZzhLvZWgSqJaZEIgg7FoYx/Vz5WWHNxxfupABCMQ2JAVkJuEj4RjkCoQZyXTF+pJr5+BSwTlw4vrJmc3XS++0JR7MFBo3c1rRnXgOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZscnMu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
  "id": -576460752303422135,
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "state": "tx_+NILAfiEuEBx39kZRlNZIw56hfly7o6mqda2IBuIACLqvcSsq5XR5cxD2GvTJxDJR36oSYBQJGTqgCKTdWaEjLCTfjuqCmsLuEB12mjQWMitJLhf8aU6KrV3V7ZpS5gmzxTurnLtvsZzhLvZWgSqJaZEIgg7FoYx/Vz5WWHNxxfupABCMQ2JAVkJuEj4RjkCoQZyXTF+pJr5+BSwTlw4vrJmc3XS++0JR7MFBo3c1rRnXgOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZscnMu"
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "state": "tx_+NILAfiEuEBx39kZRlNZIw56hfly7o6mqda2IBuIACLqvcSsq5XR5cxD2GvTJxDJR36oSYBQJGTqgCKTdWaEjLCTfjuqCmsLuEB12mjQWMitJLhf8aU6KrV3V7ZpS5gmzxTurnLtvsZzhLvZWgSqJaZEIgg7FoYx/Vz5WWHNxxfupABCMQ2JAVkJuEj4RjkCoQZyXTF+pJr5+BSwTlw4vrJmc3XS++0JR7MFBo3c1rRnXgOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZscnMu"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422134,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
  "id": -576460752303422134,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000001
    },
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422133,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
  "id": -576460752303422133,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBx39kZRlNZIw56hfly7o6mqda2IBuIACLqvcSsq5XR5cxD2GvTJxDJR36oSYBQJGTqgCKTdWaEjLCTfjuqCmsLuEB12mjQWMitJLhf8aU6KrV3V7ZpS5gmzxTurnLtvsZzhLvZWgSqJaZEIgg7FoYx/Vz5WWHNxxfupABCMQ2JAVkJuEj4RjkCoQZyXTF+pJr5+BSwTlw4vrJmc3XS++0JR7MFBo3c1rRnXgOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZscnMu",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "signed_tx": "tx_+QJ+CwHAuQJ4+QJ1NgGhBnJdMX6kmvn4FLBOXDi+smZzddL77QlHswUGjdzWtGdeoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuEBx39kZRlNZIw56hfly7o6mqda2IBuIACLqvcSsq5XR5cxD2GvTJxDJR36oSYBQJGTqgCKTdWaEjLCTfjuqCmsLuEB12mjQWMitJLhf8aU6KrV3V7ZpS5gmzxTurnLtvsZzhLvZWgSqJaZEIgg7FoYx/Vz5WWHNxxfupABCMQ2JAVkJuEj4RjkCoQZyXTF+pJr5+BSwTlw4vrJmc3XS++0JR7MFBo3c1rRnXgOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEa5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGGSNwYbAAgbRsVI0J",
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
    "signed_tx": "tx_+QLBCwH4QrhAp4qHEjoEzgZmZWNL43q09MPd3xKMnT+qIGYEa52bW7vSqhnMSm1USdxBWhzxuhr7s47j4WCGHEXa6I+EEFHJB7kCePkCdTYBoQZyXTF+pJr5+BSwTlw4vrJmc3XS++0JR7MFBo3c1rRnXqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAcd/ZGUZTWSMOeoX5cu6OpqnWtiAbiAAi6r3ErKuV0eXMQ9hr0ycQyUd+qEmAUCRk6oAik3VmhIywk347qgprC7hAddpo0FjIrSS4X/GlOiq1d1e2aUuYJs8U7q5y7b7Gc4S72VoEqiWmRCIIOxaGMf1c+VlhzccX7qQAQjENiQFZCbhI+EY5AqEGcl0xfqSa+fgUsE5cOL6yZnN10vvtCUezBQaN3Na0Z14DoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhkjcGGwAIG0N3oBuA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLBCwH4QrhAp4qHEjoEzgZmZWNL43q09MPd3xKMnT+qIGYEa52bW7vSqhnMSm1USdxBWhzxuhr7s47j4WCGHEXa6I+EEFHJB7kCePkCdTYBoQZyXTF+pJr5+BSwTlw4vrJmc3XS++0JR7MFBo3c1rRnXqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAcd/ZGUZTWSMOeoX5cu6OpqnWtiAbiAAi6r3ErKuV0eXMQ9hr0ycQyUd+qEmAUCRk6oAik3VmhIywk347qgprC7hAddpo0FjIrSS4X/GlOiq1d1e2aUuYJs8U7q5y7b7Gc4S72VoEqiWmRCIIOxaGMf1c+VlhzccX7qQAQjENiQFZCbhI+EY5AqEGcl0xfqSa+fgUsE5cOL6yZnN10vvtCUezBQaN3Na0Z14DoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhkjcGGwAIG0N3oBuA==",
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLBCwH4QrhAp4qHEjoEzgZmZWNL43q09MPd3xKMnT+qIGYEa52bW7vSqhnMSm1USdxBWhzxuhr7s47j4WCGHEXa6I+EEFHJB7kCePkCdTYBoQZyXTF+pJr5+BSwTlw4vrJmc3XS++0JR7MFBo3c1rRnXqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAcd/ZGUZTWSMOeoX5cu6OpqnWtiAbiAAi6r3ErKuV0eXMQ9hr0ycQyUd+qEmAUCRk6oAik3VmhIywk347qgprC7hAddpo0FjIrSS4X/GlOiq1d1e2aUuYJs8U7q5y7b7Gc4S72VoEqiWmRCIIOxaGMf1c+VlhzccX7qQAQjENiQFZCbhI+EY5AqEGcl0xfqSa+fgUsE5cOL6yZnN10vvtCUezBQaN3Na0Z14DoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhkjcGGwAIG0N3oBuA==",
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
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
    "nonce": 1234567
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "signed_tx": "tx_+GcLAcC4YvhgOAGhBnJdMX6kmvn4FLBOXDi+smZzddL77QlHswUGjdzWtGdeoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiX/+GJGE5yoABAIYPbM7GgACDEtaHSeK/3w==",
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
    "channel_id": "ch_sNGzrcd9cQuK7f71ZZPktYdr4raPhDgBV1tfqqueTkmQddM8x",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

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
      "fsm_id": "ba_oOU6pNMXNR4p0DxMu7U2XBF7gTbqvuu5p4Ad0boBvE7n59oH"
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
      "fsm_id": "ba_hpAr/v3TrY8EieZIOGn2VMhNdsdzxXLXxmGbR2UXQRdybPdC"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBtbbDOX0=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422132,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEDXM2zc9LOABPyBBl+RlIvhMrFu05SsBx+9cL0JPJXepZauJvKQI9TLn4HzGH48SmU7d1mxO1Emlr92/Bgc4PAJuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgbUyQz+0"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422132,
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_hpAr/v3TrY8EieZIOGn2VMhNdsdzxXLXxmGbR2UXQRdybPdC"
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEDXM2zc9LOABPyBBl+RlIvhMrFu05SsBx+9cL0JPJXepZauJvKQI9TLn4HzGH48SmU7d1mxO1Emlr92/Bgc4PAJuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgbUyQz+0",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422131,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAO8096Yehly44ls9XJWsrXG3gUzBLZSFhzJYa9Srjn56MeChQ7hURIWvAVv/0KWyUlLH9hMt4MRbyHrXXqFU3DrhA1zNs3PSzgAT8gQZfkZSL4TKxbtOUrAcfvXC9CTyV3qWWribykCPUy5+B8xh+PEplO3dZsTtRJpa/dvwYHODwCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG1ono8oQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
  "id": -576460752303422131,
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAO8096Yehly44ls9XJWsrXG3gUzBLZSFhzJYa9Srjn56MeChQ7hURIWvAVv/0KWyUlLH9hMt4MRbyHrXXqFU3DrhA1zNs3PSzgAT8gQZfkZSL4TKxbtOUrAcfvXC9CTyV3qWWribykCPUy5+B8xh+PEplO3dZsTtRJpa/dvwYHODwCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG1ono8oQ==",
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_oOU6pNMXNR4p0DxMu7U2XBF7gTbqvuu5p4Ad0boBvE7n59oH"
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAO8096Yehly44ls9XJWsrXG3gUzBLZSFhzJYa9Srjn56MeChQ7hURIWvAVv/0KWyUlLH9hMt4MRbyHrXXqFU3DrhA1zNs3PSzgAT8gQZfkZSL4TKxbtOUrAcfvXC9CTyV3qWWribykCPUy5+B8xh+PEplO3dZsTtRJpa/dvwYHODwCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG1ono8oQ==",
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAO8096Yehly44ls9XJWsrXG3gUzBLZSFhzJYa9Srjn56MeChQ7hURIWvAVv/0KWyUlLH9hMt4MRbyHrXXqFU3DrhA1zNs3PSzgAT8gQZfkZSL4TKxbtOUrAcfvXC9CTyV3qWWribykCPUy5+B8xh+PEplO3dZsTtRJpa/dvwYHODwCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG1ono8oQ==",
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAO8096Yehly44ls9XJWsrXG3gUzBLZSFhzJYa9Srjn56MeChQ7hURIWvAVv/0KWyUlLH9hMt4MRbyHrXXqFU3DrhA1zNs3PSzgAT8gQZfkZSL4TKxbtOUrAcfvXC9CTyV3qWWribykCPUy5+B8xh+PEplO3dZsTtRJpa/dvwYHODwCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG1ono8oQ==",
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "message": {
        "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "message": {
        "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
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
  "id": -576460752303422130,
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
  "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
  "id": -576460752303422130,
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "state": "tx_+QEOCwH4hLhAO8096Yehly44ls9XJWsrXG3gUzBLZSFhzJYa9Srjn56MeChQ7hURIWvAVv/0KWyUlLH9hMt4MRbyHrXXqFU3DrhA1zNs3PSzgAT8gQZfkZSL4TKxbtOUrAcfvXC9CTyV3qWWribykCPUy5+B8xh+PEplO3dZsTtRJpa/dvwYHODwCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG1ono8oQ=="
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "state": "tx_+QEOCwH4hLhAO8096Yehly44ls9XJWsrXG3gUzBLZSFhzJYa9Srjn56MeChQ7hURIWvAVv/0KWyUlLH9hMt4MRbyHrXXqFU3DrhA1zNs3PSzgAT8gQZfkZSL4TKxbtOUrAcfvXC9CTyV3qWWribykCPUy5+B8xh+PEplO3dZsTtRJpa/dvwYHODwCbiE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoG1ono8oQ=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422129,
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
  "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
  "id": -576460752303422129,
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

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvtItCFjmjnCOIMZjm0VWOakbLv/+LLT5QNCFBA58KwTAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyhgBqSE=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainTransfer",
          "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
  "id": -576460752303422128,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA7xpE80b811SjIXbrJ5ePTGQE4bcoq08QlUeOAwEvnZSk47Dc6vE5mr5x7IYrTtfG4Gnn/el/R7OK8xrqzPMkEuEj4RjkCoQb7SLQhY5o5wjiDGY5tFVjmpGy7//iy0+UDQhQQOfCsEwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoUnHqC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
  "id": -576460752303422128,
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA7xpE80b811SjIXbrJ5ePTGQE4bcoq08QlUeOAwEvnZSk47Dc6vE5mr5x7IYrTtfG4Gnn/el/R7OK8xrqzPMkEuEj4RjkCoQb7SLQhY5o5wjiDGY5tFVjmpGy7//iy0+UDQhQQOfCsEwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoUnHqC",
      "updates": [
        {
          "amount": 1,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainTransfer",
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
  "id": -576460752303422127,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA7xpE80b811SjIXbrJ5ePTGQE4bcoq08QlUeOAwEvnZSk47Dc6vE5mr5x7IYrTtfG4Gnn/el/R7OK8xrqzPMkEuED4CQk8y5BsK4DfWoaSpWQcWmoVBPqYGXh5kWK7HXMM/j46PfcDybvSo8dq4rRINE9IcTVcWJ46ZwmnPiIcINQIuEj4RjkCoQb7SLQhY5o5wjiDGY5tFVjmpGy7//iy0+UDQhQQOfCsEwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQso/hmwi"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
  "id": -576460752303422127,
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "state": "tx_+NILAfiEuEA7xpE80b811SjIXbrJ5ePTGQE4bcoq08QlUeOAwEvnZSk47Dc6vE5mr5x7IYrTtfG4Gnn/el/R7OK8xrqzPMkEuED4CQk8y5BsK4DfWoaSpWQcWmoVBPqYGXh5kWK7HXMM/j46PfcDybvSo8dq4rRINE9IcTVcWJ46ZwmnPiIcINQIuEj4RjkCoQb7SLQhY5o5wjiDGY5tFVjmpGy7//iy0+UDQhQQOfCsEwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQso/hmwi"
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "state": "tx_+NILAfiEuEA7xpE80b811SjIXbrJ5ePTGQE4bcoq08QlUeOAwEvnZSk47Dc6vE5mr5x7IYrTtfG4Gnn/el/R7OK8xrqzPMkEuED4CQk8y5BsK4DfWoaSpWQcWmoVBPqYGXh5kWK7HXMM/j46PfcDybvSo8dq4rRINE9IcTVcWJ46ZwmnPiIcINQIuEj4RjkCoQb7SLQhY5o5wjiDGY5tFVjmpGy7//iy0+UDQhQQOfCsEwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQso/hmwi"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422126,
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
  "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
  "id": -576460752303422126,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999998
    },
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422125,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
  "id": -576460752303422125,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA7xpE80b811SjIXbrJ5ePTGQE4bcoq08QlUeOAwEvnZSk47Dc6vE5mr5x7IYrTtfG4Gnn/el/R7OK8xrqzPMkEuED4CQk8y5BsK4DfWoaSpWQcWmoVBPqYGXh5kWK7HXMM/j46PfcDybvSo8dq4rRINE9IcTVcWJ46ZwmnPiIcINQIuEj4RjkCoQb7SLQhY5o5wjiDGY5tFVjmpGy7//iy0+UDQhQQOfCsEwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQso/hmwi",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422124,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
  "id": -576460752303422124,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000002
    },
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
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
    "amount": 1,
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvtItCFjmjnCOIMZjm0VWOakbLv/+LLT5QNCFBA58KwTA6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmXTrG4=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
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
  "id": -576460752303422123,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECUVABy3dqnuQF8Jj7VdGXUXbT2app2ND2Hs2Y4SsawhP2agpZfzradtZpChrkMkIAjRq+C5YRm6MvdtvlX8kYIuEj4RjkCoQb7SLQhY5o5wjiDGY5tFVjmpGy7//iy0+UDQhQQOfCsEwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbkG9Xu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
  "id": -576460752303422123,
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "signed_tx": "tx_+JALAfhCuECUVABy3dqnuQF8Jj7VdGXUXbT2app2ND2Hs2Y4SsawhP2agpZfzradtZpChrkMkIAjRq+C5YRm6MvdtvlX8kYIuEj4RjkCoQb7SLQhY5o5wjiDGY5tFVjmpGy7//iy0+UDQhQQOfCsEwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbkG9Xu",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
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
  "id": -576460752303422122,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAZdbGt+0nt1rb4dSrUCqZ1+xlLBzAwzmSKhMfbwM12ISSrna/AcLUk8AbdWCfHxGOpm8K45gWYyHHQw3JuyRMCuECUVABy3dqnuQF8Jj7VdGXUXbT2app2ND2Hs2Y4SsawhP2agpZfzradtZpChrkMkIAjRq+C5YRm6MvdtvlX8kYIuEj4RjkCoQb7SLQhY5o5wjiDGY5tFVjmpGy7//iy0+UDQhQQOfCsEwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEap926d"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
  "id": -576460752303422122,
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "state": "tx_+NILAfiEuEAZdbGt+0nt1rb4dSrUCqZ1+xlLBzAwzmSKhMfbwM12ISSrna/AcLUk8AbdWCfHxGOpm8K45gWYyHHQw3JuyRMCuECUVABy3dqnuQF8Jj7VdGXUXbT2app2ND2Hs2Y4SsawhP2agpZfzradtZpChrkMkIAjRq+C5YRm6MvdtvlX8kYIuEj4RjkCoQb7SLQhY5o5wjiDGY5tFVjmpGy7//iy0+UDQhQQOfCsEwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEap926d"
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "state": "tx_+NILAfiEuEAZdbGt+0nt1rb4dSrUCqZ1+xlLBzAwzmSKhMfbwM12ISSrna/AcLUk8AbdWCfHxGOpm8K45gWYyHHQw3JuyRMCuECUVABy3dqnuQF8Jj7VdGXUXbT2app2ND2Hs2Y4SsawhP2agpZfzradtZpChrkMkIAjRq+C5YRm6MvdtvlX8kYIuEj4RjkCoQb7SLQhY5o5wjiDGY5tFVjmpGy7//iy0+UDQhQQOfCsEwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEap926d"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422121,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
  "id": -576460752303422121,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000001
    },
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422120,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
  "id": -576460752303422120,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAZdbGt+0nt1rb4dSrUCqZ1+xlLBzAwzmSKhMfbwM12ISSrna/AcLUk8AbdWCfHxGOpm8K45gWYyHHQw3JuyRMCuECUVABy3dqnuQF8Jj7VdGXUXbT2app2ND2Hs2Y4SsawhP2agpZfzradtZpChrkMkIAjRq+C5YRm6MvdtvlX8kYIuEj4RjkCoQb7SLQhY5o5wjiDGY5tFVjmpGy7//iy0+UDQhQQOfCsEwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEap926d",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "signed_tx": "tx_+QJ+CwHAuQJ4+QJ1NgGhBvtItCFjmjnCOIMZjm0VWOakbLv/+LLT5QNCFBA58KwToQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuEAZdbGt+0nt1rb4dSrUCqZ1+xlLBzAwzmSKhMfbwM12ISSrna/AcLUk8AbdWCfHxGOpm8K45gWYyHHQw3JuyRMCuECUVABy3dqnuQF8Jj7VdGXUXbT2app2ND2Hs2Y4SsawhP2agpZfzradtZpChrkMkIAjRq+C5YRm6MvdtvlX8kYIuEj4RjkCoQb7SLQhY5o5wjiDGY5tFVjmpGy7//iy0+UDQhQQOfCsEwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEa5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGGSNwYbAAgbaCxYLe",
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
    "signed_tx": "tx_+QLBCwH4QrhAeyyvC7lUa767rtQVwK9wkks9w9LcKRUpyWyGK9wqzKnN9vKE3cRhP/XiTP9M7cDlUPFnanDoJBqNMZ0TYk89D7kCePkCdTYBoQb7SLQhY5o5wjiDGY5tFVjmpGy7//iy0+UDQhQQOfCsE6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAGXWxrftJ7da2+HUq1AqmdfsZSwcwMM5kioTH28DNdiEkq52vwHC1JPAG3Vgnx8RjqZvCuOYFmMhx0MNybskTArhAlFQAct3ap7kBfCY+1XRl1F209mqadjQ9h7NmOErGsIT9moKWX862nbWaQoa5DJCAI0avguWEZujL3bb5V/JGCLhI+EY5AqEG+0i0IWOaOcI4gxmObRVY5qRsu//4stPlA0IUEDnwrBMDoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhkjcGGwAIG2Sy6QIQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLBCwH4QrhAeyyvC7lUa767rtQVwK9wkks9w9LcKRUpyWyGK9wqzKnN9vKE3cRhP/XiTP9M7cDlUPFnanDoJBqNMZ0TYk89D7kCePkCdTYBoQb7SLQhY5o5wjiDGY5tFVjmpGy7//iy0+UDQhQQOfCsE6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAGXWxrftJ7da2+HUq1AqmdfsZSwcwMM5kioTH28DNdiEkq52vwHC1JPAG3Vgnx8RjqZvCuOYFmMhx0MNybskTArhAlFQAct3ap7kBfCY+1XRl1F209mqadjQ9h7NmOErGsIT9moKWX862nbWaQoa5DJCAI0avguWEZujL3bb5V/JGCLhI+EY5AqEG+0i0IWOaOcI4gxmObRVY5qRsu//4stPlA0IUEDnwrBMDoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhkjcGGwAIG2Sy6QIQ==",
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLBCwH4QrhAeyyvC7lUa767rtQVwK9wkks9w9LcKRUpyWyGK9wqzKnN9vKE3cRhP/XiTP9M7cDlUPFnanDoJBqNMZ0TYk89D7kCePkCdTYBoQb7SLQhY5o5wjiDGY5tFVjmpGy7//iy0+UDQhQQOfCsE6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAGXWxrftJ7da2+HUq1AqmdfsZSwcwMM5kioTH28DNdiEkq52vwHC1JPAG3Vgnx8RjqZvCuOYFmMhx0MNybskTArhAlFQAct3ap7kBfCY+1XRl1F209mqadjQ9h7NmOErGsIT9moKWX862nbWaQoa5DJCAI0avguWEZujL3bb5V/JGCLhI+EY5AqEG+0i0IWOaOcI4gxmObRVY5qRsu//4stPlA0IUEDnwrBMDoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhkjcGGwAIG2Sy6QIQ==",
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
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
    "nonce": 1234567
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "signed_tx": "tx_+GcLAcC4YvhgOAGhBvtItCFjmjnCOIMZjm0VWOakbLv/+LLT5QNCFBA58KwToQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/+GJGE5yoABAIYPbM7GgACDEtaHpl4jPg==",
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
    "channel_id": "ch_2ufiKoKbn7eJGycx5ZyGFBUZVsFcVisvejySCBpSmXvjX8PPBD",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator closes WebSocket connection

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
