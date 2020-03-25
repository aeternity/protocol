
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
      "fsm_id": "ba_oNpUrogHrGheVSlQXpcSmSxFNNYU7ujfQK/N23hlY3nUBDIy"
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
      "fsm_id": "ba_vyG6A7PItTebV5eMFNBe/3zptmLgMCypEw7iNVhXlfx7XZ82"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYI4agpQA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423341,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEASiLv6dpaY6wCAghDHCenCqWElCeLYhos7i7cZyn+4VjII2hP3oXIPSgvRjZoD++bR5rOryx2bl9WTt1w0kQMFuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGCKqfz1Y="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423341,
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_vyG6A7PItTebV5eMFNBe/3zptmLgMCypEw7iNVhXlfx7XZ82"
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEASiLv6dpaY6wCAghDHCenCqWElCeLYhos7i7cZyn+4VjII2hP3oXIPSgvRjZoD++bR5rOryx2bl9WTt1w0kQMFuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGCKqfz1Y=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423340,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAEoi7+naWmOsAgIIQxwnpwqlhJQni2IaLO4u3Gcp/uFYyCNoT96FyD0oL0Y2aA/vm0eazq8sdm5fVk7dcNJEDBbhAT2SsU19L2ii84b1KUMUknbXRSuHJ5LHVKQb0BZeEvpVP2hT3RRsTd2vEuGKNSUrvTa1a1KeWxbrS9wcvPCOQAriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rgj0kxNf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423340,
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAEoi7+naWmOsAgIIQxwnpwqlhJQni2IaLO4u3Gcp/uFYyCNoT96FyD0oL0Y2aA/vm0eazq8sdm5fVk7dcNJEDBbhAT2SsU19L2ii84b1KUMUknbXRSuHJ5LHVKQb0BZeEvpVP2hT3RRsTd2vEuGKNSUrvTa1a1KeWxbrS9wcvPCOQAriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rgj0kxNf",
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_oNpUrogHrGheVSlQXpcSmSxFNNYU7ujfQK/N23hlY3nUBDIy"
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAEoi7+naWmOsAgIIQxwnpwqlhJQni2IaLO4u3Gcp/uFYyCNoT96FyD0oL0Y2aA/vm0eazq8sdm5fVk7dcNJEDBbhAT2SsU19L2ii84b1KUMUknbXRSuHJ5LHVKQb0BZeEvpVP2hT3RRsTd2vEuGKNSUrvTa1a1KeWxbrS9wcvPCOQAriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rgj0kxNf",
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAEoi7+naWmOsAgIIQxwnpwqlhJQni2IaLO4u3Gcp/uFYyCNoT96FyD0oL0Y2aA/vm0eazq8sdm5fVk7dcNJEDBbhAT2SsU19L2ii84b1KUMUknbXRSuHJ5LHVKQb0BZeEvpVP2hT3RRsTd2vEuGKNSUrvTa1a1KeWxbrS9wcvPCOQAriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rgj0kxNf",
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAEoi7+naWmOsAgIIQxwnpwqlhJQni2IaLO4u3Gcp/uFYyCNoT96FyD0oL0Y2aA/vm0eazq8sdm5fVk7dcNJEDBbhAT2SsU19L2ii84b1KUMUknbXRSuHJ5LHVKQb0BZeEvpVP2hT3RRsTd2vEuGKNSUrvTa1a1KeWxbrS9wcvPCOQAriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rgj0kxNf",
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "message": {
        "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "message": {
        "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
  "id": -576460752303423339,
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
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423339,
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "state": "tx_+QENCwH4hLhAEoi7+naWmOsAgIIQxwnpwqlhJQni2IaLO4u3Gcp/uFYyCNoT96FyD0oL0Y2aA/vm0eazq8sdm5fVk7dcNJEDBbhAT2SsU19L2ii84b1KUMUknbXRSuHJ5LHVKQb0BZeEvpVP2hT3RRsTd2vEuGKNSUrvTa1a1KeWxbrS9wcvPCOQAriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rgj0kxNf"
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "state": "tx_+QENCwH4hLhAEoi7+naWmOsAgIIQxwnpwqlhJQni2IaLO4u3Gcp/uFYyCNoT96FyD0oL0Y2aA/vm0eazq8sdm5fVk7dcNJEDBbhAT2SsU19L2ii84b1KUMUknbXRSuHJ5LHVKQb0BZeEvpVP2hT3RRsTd2vEuGKNSUrvTa1a1KeWxbrS9wcvPCOQAriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rgj0kxNf"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423338,
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
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423338,
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
    "amount": "1",
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "meta": [
      "meta 1"
    ],
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "meta": [
          "meta 1"
        ],
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
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
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
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
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "meta": 17,
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "meta": 17,
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBsiTma/084VN3+SuvFWEzAM734wecXPVGs9QRc7sd+hvAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyrn7O/w=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainTransfer",
          "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
  "id": -576460752303423337,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDDGyazCSWxOoHEvax3OnS1gk5I4T/V1nVxwayQSO0ywn4p7Bpi6n6jqLKWzTSwS0qQPxfuufWFNEyW80QpXqEBuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrkN+Xc"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423337,
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDDGyazCSWxOoHEvax3OnS1gk5I4T/V1nVxwayQSO0ywn4p7Bpi6n6jqLKWzTSwS0qQPxfuufWFNEyW80QpXqEBuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrkN+Xc",
      "updates": [
        {
          "amount": 1,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainTransfer",
          "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
  "id": -576460752303423336,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBRFo32AlDHRnUa33ijFq+0lQfy9Hhmlpiz1CT9bVilopN73Vcxp+d3iX5y4fBCI16KUmylEzYUrY/pxP09Oj4CuEDDGyazCSWxOoHEvax3OnS1gk5I4T/V1nVxwayQSO0ywn4p7Bpi6n6jqLKWzTSwS0qQPxfuufWFNEyW80QpXqEBuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspHDLxW"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423336,
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "state": "tx_+NILAfiEuEBRFo32AlDHRnUa33ijFq+0lQfy9Hhmlpiz1CT9bVilopN73Vcxp+d3iX5y4fBCI16KUmylEzYUrY/pxP09Oj4CuEDDGyazCSWxOoHEvax3OnS1gk5I4T/V1nVxwayQSO0ywn4p7Bpi6n6jqLKWzTSwS0qQPxfuufWFNEyW80QpXqEBuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspHDLxW"
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "state": "tx_+NILAfiEuEBRFo32AlDHRnUa33ijFq+0lQfy9Hhmlpiz1CT9bVilopN73Vcxp+d3iX5y4fBCI16KUmylEzYUrY/pxP09Oj4CuEDDGyazCSWxOoHEvax3OnS1gk5I4T/V1nVxwayQSO0ywn4p7Bpi6n6jqLKWzTSwS0qQPxfuufWFNEyW80QpXqEBuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspHDLxW"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423335,
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
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423335,
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
  "id": -576460752303423334,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423334,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBRFo32AlDHRnUa33ijFq+0lQfy9Hhmlpiz1CT9bVilopN73Vcxp+d3iX5y4fBCI16KUmylEzYUrY/pxP09Oj4CuEDDGyazCSWxOoHEvax3OnS1gk5I4T/V1nVxwayQSO0ywn4p7Bpi6n6jqLKWzTSwS0qQPxfuufWFNEyW80QpXqEBuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspHDLxW",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423333,
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
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423333,
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
    "amount": "1",
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "meta": [
      "meta 1"
    ],
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "meta": [
          "meta 1"
        ],
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
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
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
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
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "meta": 17,
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "meta": 17,
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBsiTma/084VN3+SuvFWEzAM734wecXPVGs9QRc7sd+hvA6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RvdUJ6M=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
          "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "id": -576460752303423332,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED5lXBvB9Y5EZ6vBIrNZ8kfQsN+ALDY0By10mcuw0k9DZVUxYroTbPZOkkiZoOC2vtlauh5JkknSryduJzB0mkBuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYuCT/d"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423332,
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "signed_tx": "tx_+JALAfhCuED5lXBvB9Y5EZ6vBIrNZ8kfQsN+ALDY0By10mcuw0k9DZVUxYroTbPZOkkiZoOC2vtlauh5JkknSryduJzB0mkBuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYuCT/d",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
          "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "id": -576460752303423331,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAUnHKfYBClZ5Ytdfti8nEKyLIgMqzvzu0wU68CD613T6NUnQVid0ca0tu6Mdv/vH4SGZ46Upmg6S7wdcgrl5MBuED5lXBvB9Y5EZ6vBIrNZ8kfQsN+ALDY0By10mcuw0k9DZVUxYroTbPZOkkiZoOC2vtlauh5JkknSryduJzB0mkBuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaqVfA+"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423331,
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "state": "tx_+NILAfiEuEAUnHKfYBClZ5Ytdfti8nEKyLIgMqzvzu0wU68CD613T6NUnQVid0ca0tu6Mdv/vH4SGZ46Upmg6S7wdcgrl5MBuED5lXBvB9Y5EZ6vBIrNZ8kfQsN+ALDY0By10mcuw0k9DZVUxYroTbPZOkkiZoOC2vtlauh5JkknSryduJzB0mkBuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaqVfA+"
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "state": "tx_+NILAfiEuEAUnHKfYBClZ5Ytdfti8nEKyLIgMqzvzu0wU68CD613T6NUnQVid0ca0tu6Mdv/vH4SGZ46Upmg6S7wdcgrl5MBuED5lXBvB9Y5EZ6vBIrNZ8kfQsN+ALDY0By10mcuw0k9DZVUxYroTbPZOkkiZoOC2vtlauh5JkknSryduJzB0mkBuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaqVfA+"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423330,
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
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423330,
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
  "id": -576460752303423329,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423329,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAUnHKfYBClZ5Ytdfti8nEKyLIgMqzvzu0wU68CD613T6NUnQVid0ca0tu6Mdv/vH4SGZ46Upmg6S7wdcgrl5MBuED5lXBvB9Y5EZ6vBIrNZ8kfQsN+ALDY0By10mcuw0k9DZVUxYroTbPZOkkiZoOC2vtlauh5JkknSryduJzB0mkBuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaqVfA+",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423328,
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
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423328,
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

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "meta": [
      "meta 1"
    ],
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "meta": [
          "meta 1"
        ],
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
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
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
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
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "meta": 17,
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "meta": 17,
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBsiTma/084VN3+SuvFWEzAM734wecXPVGs9QRc7sd+hvBKDdqOzEXWz8Y2itvyrEosD88v7VNFxfGdbGSLDDea6BYOg9T3M=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
          "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "id": -576460752303423327,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAB6Rg4Im35tXqzD9KDk7wsawP3yCVbI1756MqrGRgjfszjrWx15omhW5w2rqKBBwi6slmEKax4XLR2P/5I4qsJuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBs3d3t"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423327,
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAB6Rg4Im35tXqzD9KDk7wsawP3yCVbI1756MqrGRgjfszjrWx15omhW5w2rqKBBwi6slmEKax4XLR2P/5I4qsJuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBs3d3t",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
          "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "id": -576460752303423326,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAB6Rg4Im35tXqzD9KDk7wsawP3yCVbI1756MqrGRgjfszjrWx15omhW5w2rqKBBwi6slmEKax4XLR2P/5I4qsJuEA8ADwuaE77PH0Xt0QQvqXLDO4QEAy5D3Mdv67j2+4uDX+QVqB8NJMIpkCDtTTC76YGcjDY2LZtAc0LGITBDesHuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBMGz/z"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423326,
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "state": "tx_+NILAfiEuEAB6Rg4Im35tXqzD9KDk7wsawP3yCVbI1756MqrGRgjfszjrWx15omhW5w2rqKBBwi6slmEKax4XLR2P/5I4qsJuEA8ADwuaE77PH0Xt0QQvqXLDO4QEAy5D3Mdv67j2+4uDX+QVqB8NJMIpkCDtTTC76YGcjDY2LZtAc0LGITBDesHuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBMGz/z"
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "state": "tx_+NILAfiEuEAB6Rg4Im35tXqzD9KDk7wsawP3yCVbI1756MqrGRgjfszjrWx15omhW5w2rqKBBwi6slmEKax4XLR2P/5I4qsJuEA8ADwuaE77PH0Xt0QQvqXLDO4QEAy5D3Mdv67j2+4uDX+QVqB8NJMIpkCDtTTC76YGcjDY2LZtAc0LGITBDesHuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBMGz/z"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423325,
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
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423325,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000000
    },
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423324,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423324,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAB6Rg4Im35tXqzD9KDk7wsawP3yCVbI1756MqrGRgjfszjrWx15omhW5w2rqKBBwi6slmEKax4XLR2P/5I4qsJuEA8ADwuaE77PH0Xt0QQvqXLDO4QEAy5D3Mdv67j2+4uDX+QVqB8NJMIpkCDtTTC76YGcjDY2LZtAc0LGITBDesHuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBMGz/z",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAALDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiYACdCDgG"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423323,
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
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423323,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 70000000000000
    },
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
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
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "meta": [
      "meta 1"
    ],
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "meta": [
          "meta 1"
        ],
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
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
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
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
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "meta": 17,
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "meta": 17,
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBsiTma/084VN3+SuvFWEzAM734wecXPVGs9QRc7sd+hvBaBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkdJ5xk=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainTransfer",
          "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
  "id": -576460752303423322,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAclNvRsGdf4ngm9BgF25uD+B4wSp3IdORxrTkr6W71CPNeB+b9gGxTE/LgLMNaMpfAC5Xf4KEb6YEmauQ6PLQAuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY14i8P"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423322,
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAclNvRsGdf4ngm9BgF25uD+B4wSp3IdORxrTkr6W71CPNeB+b9gGxTE/LgLMNaMpfAC5Xf4KEb6YEmauQ6PLQAuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY14i8P",
      "updates": [
        {
          "amount": 1,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainTransfer",
          "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
  "id": -576460752303423321,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAclNvRsGdf4ngm9BgF25uD+B4wSp3IdORxrTkr6W71CPNeB+b9gGxTE/LgLMNaMpfAC5Xf4KEb6YEmauQ6PLQAuED+H23LuHwkjCyUbfScuaMcSzeo3qbCTLt+EXC0rB7b4nMpyJ4FlM1vuiIzCGOVWCYd8BIjqJpHdS/SsHQLjSkOuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbocrQu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423321,
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "state": "tx_+NILAfiEuEAclNvRsGdf4ngm9BgF25uD+B4wSp3IdORxrTkr6W71CPNeB+b9gGxTE/LgLMNaMpfAC5Xf4KEb6YEmauQ6PLQAuED+H23LuHwkjCyUbfScuaMcSzeo3qbCTLt+EXC0rB7b4nMpyJ4FlM1vuiIzCGOVWCYd8BIjqJpHdS/SsHQLjSkOuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbocrQu"
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "state": "tx_+NILAfiEuEAclNvRsGdf4ngm9BgF25uD+B4wSp3IdORxrTkr6W71CPNeB+b9gGxTE/LgLMNaMpfAC5Xf4KEb6YEmauQ6PLQAuED+H23LuHwkjCyUbfScuaMcSzeo3qbCTLt+EXC0rB7b4nMpyJ4FlM1vuiIzCGOVWCYd8BIjqJpHdS/SsHQLjSkOuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbocrQu"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423320,
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
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423320,
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
  "id": -576460752303423319,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423319,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAclNvRsGdf4ngm9BgF25uD+B4wSp3IdORxrTkr6W71CPNeB+b9gGxTE/LgLMNaMpfAC5Xf4KEb6YEmauQ6PLQAuED+H23LuHwkjCyUbfScuaMcSzeo3qbCTLt+EXC0rB7b4nMpyJ4FlM1vuiIzCGOVWCYd8BIjqJpHdS/SsHQLjSkOuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7HfobwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbocrQu",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423318,
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
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423318,
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

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "meta": [
      "meta 1"
    ],
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "meta": [
          "meta 1"
        ],
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
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
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
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
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "meta": 17,
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "meta": 17,
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "meta": [
      "meta 1"
    ],
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBsiTma/084VN3+SuvFWEzAM734wecXPVGs9QRc7sd+hvBqDdqOzEXWz8Y2itvyrEosD88v7VNFxfGdbGSLDDea6BYEgoaE4=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
          "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "id": -576460752303423317,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBXeBPG72LFZZpcqfP8PGOeNkvC9zPvnFeIyWbIikC0jIb3ql1Gyzt1NsAAQB7hh/LB5UYlAQ7bY5mY7E7ynHYDuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7Hfobwag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWA1o9lX"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423317,
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBXeBPG72LFZZpcqfP8PGOeNkvC9zPvnFeIyWbIikC0jIb3ql1Gyzt1NsAAQB7hh/LB5UYlAQ7bY5mY7E7ynHYDuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7Hfobwag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWA1o9lX",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
          "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "id": -576460752303423316,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEArbUJfN9wzx6fBPfyWe9VpKxnbbPO9xzLMaPc+cWsJwAmLGZblrPbxCjcDpVKyKIPFLl9eYVAEpcFXUkVD7IEHuEBXeBPG72LFZZpcqfP8PGOeNkvC9zPvnFeIyWbIikC0jIb3ql1Gyzt1NsAAQB7hh/LB5UYlAQ7bY5mY7E7ynHYDuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7Hfobwag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWD6sJEX"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423316,
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "state": "tx_+NILAfiEuEArbUJfN9wzx6fBPfyWe9VpKxnbbPO9xzLMaPc+cWsJwAmLGZblrPbxCjcDpVKyKIPFLl9eYVAEpcFXUkVD7IEHuEBXeBPG72LFZZpcqfP8PGOeNkvC9zPvnFeIyWbIikC0jIb3ql1Gyzt1NsAAQB7hh/LB5UYlAQ7bY5mY7E7ynHYDuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7Hfobwag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWD6sJEX"
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
    "data": {
      "state": "tx_+NILAfiEuEArbUJfN9wzx6fBPfyWe9VpKxnbbPO9xzLMaPc+cWsJwAmLGZblrPbxCjcDpVKyKIPFLl9eYVAEpcFXUkVD7IEHuEBXeBPG72LFZZpcqfP8PGOeNkvC9zPvnFeIyWbIikC0jIb3ql1Gyzt1NsAAQB7hh/LB5UYlAQ7bY5mY7E7ynHYDuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7Hfobwag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWD6sJEX"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423315,
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
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423315,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000000
    },
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423314,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423314,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEArbUJfN9wzx6fBPfyWe9VpKxnbbPO9xzLMaPc+cWsJwAmLGZblrPbxCjcDpVKyKIPFLl9eYVAEpcFXUkVD7IEHuEBXeBPG72LFZZpcqfP8PGOeNkvC9zPvnFeIyWbIikC0jIb3ql1Gyzt1NsAAQB7hh/LB5UYlAQ7bY5mY7E7ynHYDuEj4RjkCoQbIk5mv9POFTd/krrxVhMwDO9+MHnFz1RrPUEXO7Hfobwag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWD6sJEX",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAALDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiYACdCDgG"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423313,
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
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423313,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423312,
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
    "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
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
  "channel_id": "ch_2XLTdUzdWQXNh7mFCZGtaa1D5D3mjEJVXNmT4gdc8ZXRpBo6RD",
  "id": -576460752303423312,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
