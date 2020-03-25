
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&gas_price=1000001234&host=localhost&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=initiator
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
      "fsm_id": "ba_MQL8Cu84VlmgOXNEp/rOQaaW4WACie0qYHDo+d3AT7ZyhU/a"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&gas_price=1000001234&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=responder
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
      "fsm_id": "ba_lDXw8kBeyb/vJm9NN3Hh4seVw4Y7sbRe3u7AbGRO3a03crlF"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeyMN6MCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZPQgj2/g==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422587,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECZxvyTUxZ9U1tKYKU+PPX4JZHzEq+e52u3RXHvTHAJiZrbcA+C0EL7ih9c3UC53lG6gcFWJHrp7gLnMeI3jDELuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnsjDejAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGT+ElhIM="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422587,
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_lDXw8kBeyb/vJm9NN3Hh4seVw4Y7sbRe3u7AbGRO3a03crlF"
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
    "data": {
      "signed_tx": "tx_+MsLAfhCuECZxvyTUxZ9U1tKYKU+PPX4JZHzEq+e52u3RXHvTHAJiZrbcA+C0EL7ih9c3UC53lG6gcFWJHrp7gLnMeI3jDELuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnsjDejAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGT+ElhIM=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422586,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAFZjEsqF4+ibd84Mk14hSMxIOqqmWo8pvzSHtH2GceZIS91JTzrSmMnlE2gLdpRJGk5en/7QtTrVJLiTsWvHSC7hAmcb8k1MWfVNbSmClPjz1+CWR8xKvnudrt0Vx70xwCYma23APgtBC+4ofXN1Aud5RuoHBViR66e4C5zHiN4wxC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ7Iw3owKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rk95UQxs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
  "id": -576460752303422586,
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAFZjEsqF4+ibd84Mk14hSMxIOqqmWo8pvzSHtH2GceZIS91JTzrSmMnlE2gLdpRJGk5en/7QtTrVJLiTsWvHSC7hAmcb8k1MWfVNbSmClPjz1+CWR8xKvnudrt0Vx70xwCYma23APgtBC+4ofXN1Aud5RuoHBViR66e4C5zHiN4wxC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ7Iw3owKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rk95UQxs",
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_MQL8Cu84VlmgOXNEp/rOQaaW4WACie0qYHDo+d3AT7ZyhU/a"
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAFZjEsqF4+ibd84Mk14hSMxIOqqmWo8pvzSHtH2GceZIS91JTzrSmMnlE2gLdpRJGk5en/7QtTrVJLiTsWvHSC7hAmcb8k1MWfVNbSmClPjz1+CWR8xKvnudrt0Vx70xwCYma23APgtBC+4ofXN1Aud5RuoHBViR66e4C5zHiN4wxC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ7Iw3owKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rk95UQxs",
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAFZjEsqF4+ibd84Mk14hSMxIOqqmWo8pvzSHtH2GceZIS91JTzrSmMnlE2gLdpRJGk5en/7QtTrVJLiTsWvHSC7hAmcb8k1MWfVNbSmClPjz1+CWR8xKvnudrt0Vx70xwCYma23APgtBC+4ofXN1Aud5RuoHBViR66e4C5zHiN4wxC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ7Iw3owKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rk95UQxs",
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAFZjEsqF4+ibd84Mk14hSMxIOqqmWo8pvzSHtH2GceZIS91JTzrSmMnlE2gLdpRJGk5en/7QtTrVJLiTsWvHSC7hAmcb8k1MWfVNbSmClPjz1+CWR8xKvnudrt0Vx70xwCYma23APgtBC+4ofXN1Aud5RuoHBViR66e4C5zHiN4wxC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ7Iw3owKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rk95UQxs",
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
    "data": {
      "message": {
        "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
    "data": {
      "message": {
        "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
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
  "id": -576460752303422585,
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
  "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
  "id": -576460752303422585,
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
    "data": {
      "state": "tx_+QENCwH4hLhAFZjEsqF4+ibd84Mk14hSMxIOqqmWo8pvzSHtH2GceZIS91JTzrSmMnlE2gLdpRJGk5en/7QtTrVJLiTsWvHSC7hAmcb8k1MWfVNbSmClPjz1+CWR8xKvnudrt0Vx70xwCYma23APgtBC+4ofXN1Aud5RuoHBViR66e4C5zHiN4wxC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ7Iw3owKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rk95UQxs"
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
    "data": {
      "state": "tx_+QENCwH4hLhAFZjEsqF4+ibd84Mk14hSMxIOqqmWo8pvzSHtH2GceZIS91JTzrSmMnlE2gLdpRJGk5en/7QtTrVJLiTsWvHSC7hAmcb8k1MWfVNbSmClPjz1+CWR8xKvnudrt0Vx70xwCYma23APgtBC+4ofXN1Aud5RuoHBViR66e4C5zHiN4wxC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ7Iw3owKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rk95UQxs"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBij22nbk4fBZE8PkHHayNE6X9Fme9sOujskttyhmuKz6oQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+rniy/+GHLHOiuwBAIYPXtZ/KABQmW5GPw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422584,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuED2NLdPcKzetKk3/CEHurxkYOSvjc3ecwBYRAaxBknPpp0cTYtm9CaCAGZml6qLAZ3GiwGgsbGUUXqTNM32mA0GuF/4XTUBoQYo9tp25OHwWRPD5Bx2sjROl/RZnvbDro7JLbcoZris+qEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAUO7gRDU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
  "id": -576460752303422584,
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
    "data": {
      "event": "shutdown"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
    "data": {
      "signed_tx": "tx_+KcLAfhCuED2NLdPcKzetKk3/CEHurxkYOSvjc3ecwBYRAaxBknPpp0cTYtm9CaCAGZml6qLAZ3GiwGgsbGUUXqTNM32mA0GuF/4XTUBoQYo9tp25OHwWRPD5Bx2sjROl/RZnvbDro7JLbcoZris+qEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAUO7gRDU=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422583,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEBwMr1T6vlDevzMBct6tcAYTFpvcCK1JHqxHaR7NUWWtJR5r4eTBwqtmpG9eSvI7GKaponPF5GOFlBEJQXZWnAEuED2NLdPcKzetKk3/CEHurxkYOSvjc3ecwBYRAaxBknPpp0cTYtm9CaCAGZml6qLAZ3GiwGgsbGUUXqTNM32mA0GuF/4XTUBoQYo9tp25OHwWRPD5Bx2sjROl/RZnvbDro7JLbcoZris+qEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAUNJ2+uE="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
  "id": -576460752303422583,
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBwMr1T6vlDevzMBct6tcAYTFpvcCK1JHqxHaR7NUWWtJR5r4eTBwqtmpG9eSvI7GKaponPF5GOFlBEJQXZWnAEuED2NLdPcKzetKk3/CEHurxkYOSvjc3ecwBYRAaxBknPpp0cTYtm9CaCAGZml6qLAZ3GiwGgsbGUUXqTNM32mA0GuF/4XTUBoQYo9tp25OHwWRPD5Bx2sjROl/RZnvbDro7JLbcoZris+qEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAUNJ2+uE=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
    "data": {
      "event": "closing"
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBwMr1T6vlDevzMBct6tcAYTFpvcCK1JHqxHaR7NUWWtJR5r4eTBwqtmpG9eSvI7GKaponPF5GOFlBEJQXZWnAEuED2NLdPcKzetKk3/CEHurxkYOSvjc3ecwBYRAaxBknPpp0cTYtm9CaCAGZml6qLAZ3GiwGgsbGUUXqTNM32mA0GuF/4XTUBoQYo9tp25OHwWRPD5Bx2sjROl/RZnvbDro7JLbcoZris+qEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAUNJ2+uE=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
    "data": {
      "event": "closing"
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBwMr1T6vlDevzMBct6tcAYTFpvcCK1JHqxHaR7NUWWtJR5r4eTBwqtmpG9eSvI7GKaponPF5GOFlBEJQXZWnAEuED2NLdPcKzetKk3/CEHurxkYOSvjc3ecwBYRAaxBknPpp0cTYtm9CaCAGZml6qLAZ3GiwGgsbGUUXqTNM32mA0GuF/4XTUBoQYo9tp25OHwWRPD5Bx2sjROl/RZnvbDro7JLbcoZris+qEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAUNJ2+uE=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBwMr1T6vlDevzMBct6tcAYTFpvcCK1JHqxHaR7NUWWtJR5r4eTBwqtmpG9eSvI7GKaponPF5GOFlBEJQXZWnAEuED2NLdPcKzetKk3/CEHurxkYOSvjc3ecwBYRAaxBknPpp0cTYtm9CaCAGZml6qLAZ3GiwGgsbGUUXqTNM32mA0GuF/4XTUBoQYo9tp25OHwWRPD5Bx2sjROl/RZnvbDro7JLbcoZris+qEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAUNJ2+uE=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
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
    "channel_id": "ch_K3NtKE3fBTsTH36Lt6JFJ2gzF5MDSgyHuzs7jJxxsKabWivtH",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
