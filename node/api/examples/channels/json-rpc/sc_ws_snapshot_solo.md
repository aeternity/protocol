
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
      "fsm_id": "ba_YoWZ7Br73eKhk4Xr14wLaCwsD6pBVihjSsEyS4BDaiubySHi"
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
      "fsm_id": "ba_aR0e6cv7uh0PAdMrz+MHBk30qsZDhxUCNnZ180Faa7f3aFWi"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYGQLOxLA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423391,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBt+fY2zyyk8pOoBWyHYNCTwYeewKnq5qIyrEVwkfh4ElKax49jR5qeOHoj/R8kD/Y7xGLbcK+GuV3t+R6yAxYJuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGBo1JRXc="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423391,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_aR0e6cv7uh0PAdMrz+MHBk30qsZDhxUCNnZ180Faa7f3aFWi"
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEBt+fY2zyyk8pOoBWyHYNCTwYeewKnq5qIyrEVwkfh4ElKax49jR5qeOHoj/R8kD/Y7xGLbcK+GuV3t+R6yAxYJuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGBo1JRXc=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423390,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAQEaDJrqvbbgdkMuTxit3nd0kOmGj7C7bmAA6NilWuxFVC2rQojjwMr4sLUpJXGT9yWTeHbnBbhRkbaogbYzLCLhAbfn2Ns8spPKTqAVsh2DQk8GHnsCp6uaiMqxFcJH4eBJSmsePY0eanjh6I/0fJA/2O8Ri23Cvhrld7fkesgMWCbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rgb5qhgh"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423390,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAQEaDJrqvbbgdkMuTxit3nd0kOmGj7C7bmAA6NilWuxFVC2rQojjwMr4sLUpJXGT9yWTeHbnBbhRkbaogbYzLCLhAbfn2Ns8spPKTqAVsh2DQk8GHnsCp6uaiMqxFcJH4eBJSmsePY0eanjh6I/0fJA/2O8Ri23Cvhrld7fkesgMWCbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rgb5qhgh",
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_YoWZ7Br73eKhk4Xr14wLaCwsD6pBVihjSsEyS4BDaiubySHi"
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAQEaDJrqvbbgdkMuTxit3nd0kOmGj7C7bmAA6NilWuxFVC2rQojjwMr4sLUpJXGT9yWTeHbnBbhRkbaogbYzLCLhAbfn2Ns8spPKTqAVsh2DQk8GHnsCp6uaiMqxFcJH4eBJSmsePY0eanjh6I/0fJA/2O8Ri23Cvhrld7fkesgMWCbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rgb5qhgh",
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAQEaDJrqvbbgdkMuTxit3nd0kOmGj7C7bmAA6NilWuxFVC2rQojjwMr4sLUpJXGT9yWTeHbnBbhRkbaogbYzLCLhAbfn2Ns8spPKTqAVsh2DQk8GHnsCp6uaiMqxFcJH4eBJSmsePY0eanjh6I/0fJA/2O8Ri23Cvhrld7fkesgMWCbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rgb5qhgh",
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAQEaDJrqvbbgdkMuTxit3nd0kOmGj7C7bmAA6NilWuxFVC2rQojjwMr4sLUpJXGT9yWTeHbnBbhRkbaogbYzLCLhAbfn2Ns8spPKTqAVsh2DQk8GHnsCp6uaiMqxFcJH4eBJSmsePY0eanjh6I/0fJA/2O8Ri23Cvhrld7fkesgMWCbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rgb5qhgh",
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "message": {
        "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "message": {
        "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
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
  "id": -576460752303423389,
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
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423389,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "state": "tx_+QENCwH4hLhAQEaDJrqvbbgdkMuTxit3nd0kOmGj7C7bmAA6NilWuxFVC2rQojjwMr4sLUpJXGT9yWTeHbnBbhRkbaogbYzLCLhAbfn2Ns8spPKTqAVsh2DQk8GHnsCp6uaiMqxFcJH4eBJSmsePY0eanjh6I/0fJA/2O8Ri23Cvhrld7fkesgMWCbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rgb5qhgh"
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "state": "tx_+QENCwH4hLhAQEaDJrqvbbgdkMuTxit3nd0kOmGj7C7bmAA6NilWuxFVC2rQojjwMr4sLUpJXGT9yWTeHbnBbhRkbaogbYzLCLhAbfn2Ns8spPKTqAVsh2DQk8GHnsCp6uaiMqxFcJH4eBJSmsePY0eanjh6I/0fJA/2O8Ri23Cvhrld7fkesgMWCbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rgb5qhgh"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423388,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "error": {
    "code": 2,
    "data": [
      {
        "code": 1012,
        "message": "Offchain tx expected"
      }
    ],
    "message": "Action not allowed",
    "request": {
      "id": -576460752303423388,
      "jsonrpc": "2.0",
      "method": "channels.snapshot_solo",
      "params": {}
    }
  },
  "id": -576460752303423388,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423387,
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
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423387,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuW3XpEGEbriNC1+10Yu6DUh+sOl2aRV6oZ5pU3dO7WwAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCytBUntg=",
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
  "id": -576460752303423386,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAwLPIdbO5+mXmLdqD6yC+xum/br3Xlmchb9LYShnuUX47k/6kTgCzt1m+uu6UaK0Vql9+oSC8NKX+TDr6pTo4OuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspvpn/F"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423386,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAwLPIdbO5+mXmLdqD6yC+xum/br3Xlmchb9LYShnuUX47k/6kTgCzt1m+uu6UaK0Vql9+oSC8NKX+TDr6pTo4OuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspvpn/F",
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
  "id": -576460752303423385,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAwLPIdbO5+mXmLdqD6yC+xum/br3Xlmchb9LYShnuUX47k/6kTgCzt1m+uu6UaK0Vql9+oSC8NKX+TDr6pTo4OuEB8eMQ9MabmAoJsbCldDAZ3Pg9UTVndB2mAOsLJOlHJ/syiKetjb04V7/4mqiEA+/uxfsZSdasQcoUJuDX+erULuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqP6lCt"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423385,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "state": "tx_+NILAfiEuEAwLPIdbO5+mXmLdqD6yC+xum/br3Xlmchb9LYShnuUX47k/6kTgCzt1m+uu6UaK0Vql9+oSC8NKX+TDr6pTo4OuEB8eMQ9MabmAoJsbCldDAZ3Pg9UTVndB2mAOsLJOlHJ/syiKetjb04V7/4mqiEA+/uxfsZSdasQcoUJuDX+erULuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqP6lCt"
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "state": "tx_+NILAfiEuEAwLPIdbO5+mXmLdqD6yC+xum/br3Xlmchb9LYShnuUX47k/6kTgCzt1m+uu6UaK0Vql9+oSC8NKX+TDr6pTo4OuEB8eMQ9MabmAoJsbCldDAZ3Pg9UTVndB2mAOsLJOlHJ/syiKetjb04V7/4mqiEA+/uxfsZSdasQcoUJuDX+erULuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqP6lCt"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423384,
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
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423384,
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
  "id": -576460752303423383,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423383,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAwLPIdbO5+mXmLdqD6yC+xum/br3Xlmchb9LYShnuUX47k/6kTgCzt1m+uu6UaK0Vql9+oSC8NKX+TDr6pTo4OuEB8eMQ9MabmAoJsbCldDAZ3Pg9UTVndB2mAOsLJOlHJ/syiKetjb04V7/4mqiEA+/uxfsZSdasQcoUJuDX+erULuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqP6lCt",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423382,
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
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423382,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuW3XpEGEbriNC1+10Yu6DUh+sOl2aRV6oZ5pU3dO7WwA6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoSU7Eo=",
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
  "id": -576460752303423381,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAIA3y4o9nxvqHaKLaNnAFptlNbEdn6pKWiH80FT4dHhTcKJixBNty56qW6y3VCysI8KGIRtlmmH7G8K2n9cw8BuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaRXCmu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423381,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAIA3y4o9nxvqHaKLaNnAFptlNbEdn6pKWiH80FT4dHhTcKJixBNty56qW6y3VCysI8KGIRtlmmH7G8K2n9cw8BuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaRXCmu",
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
  "id": -576460752303423380,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAIA3y4o9nxvqHaKLaNnAFptlNbEdn6pKWiH80FT4dHhTcKJixBNty56qW6y3VCysI8KGIRtlmmH7G8K2n9cw8BuEB7SW1WFIfM/cKreJMrTV7lmTr3gPtA6saEQAp/j1CayPaZ/vN2MvyZmix29lYulxo+Xvu+9jbtIbtOnG5nz90GuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZkiNkW"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423380,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "state": "tx_+NILAfiEuEAIA3y4o9nxvqHaKLaNnAFptlNbEdn6pKWiH80FT4dHhTcKJixBNty56qW6y3VCysI8KGIRtlmmH7G8K2n9cw8BuEB7SW1WFIfM/cKreJMrTV7lmTr3gPtA6saEQAp/j1CayPaZ/vN2MvyZmix29lYulxo+Xvu+9jbtIbtOnG5nz90GuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZkiNkW"
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "state": "tx_+NILAfiEuEAIA3y4o9nxvqHaKLaNnAFptlNbEdn6pKWiH80FT4dHhTcKJixBNty56qW6y3VCysI8KGIRtlmmH7G8K2n9cw8BuEB7SW1WFIfM/cKreJMrTV7lmTr3gPtA6saEQAp/j1CayPaZ/vN2MvyZmix29lYulxo+Xvu+9jbtIbtOnG5nz90GuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZkiNkW"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423379,
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
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423379,
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
  "id": -576460752303423378,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423378,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAIA3y4o9nxvqHaKLaNnAFptlNbEdn6pKWiH80FT4dHhTcKJixBNty56qW6y3VCysI8KGIRtlmmH7G8K2n9cw8BuEB7SW1WFIfM/cKreJMrTV7lmTr3gPtA6saEQAp/j1CayPaZ/vN2MvyZmix29lYulxo+Xvu+9jbtIbtOnG5nz90GuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZkiNkW",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423377,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423377,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBuW3XpEGEbriNC1+10Yu6DUh+sOl2aRV6oZ5pU3dO7WwoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuEAIA3y4o9nxvqHaKLaNnAFptlNbEdn6pKWiH80FT4dHhTcKJixBNty56qW6y3VCysI8KGIRtlmmH7G8K2n9cw8BuEB7SW1WFIfM/cKreJMrTV7lmTr3gPtA6saEQAp/j1CayPaZ/vN2MvyZmix29lYulxo+Xvu+9jbtIbtOnG5nz90GuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYAhhMG0SswAAegwteY",
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
  "method": "channels.snapshot_solo_sign",
  "params": {
    "signed_tx": "tx_+QFxCwH4QrhA+LuecsLsoI/QLQBafTBboWKfN5T7FEG2JxUML7lt5n2oSly1/Vj9xUOtclgWTUN9xwSA1hydJE1wUj1OCR4PDrkBKPkBJTsBoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhACAN8uKPZ8b6h2ii2jZwBabZTWxHZ+qSloh/NBU+HR4U3CiYsQTbcueqlust1QsrCPChiEbZZph+xvCtp/XMPAbhAe0ltVhSHzP3Cq3iTK01e5Zk694D7QOrGhEAKf49Qmsj2mf7zdjL8mZosdvZWLpcaPl77vvY27SG7TpxuZ8/dBrhI+EY5AqEG5bdekQYRuuI0LX7XRi7oNSH6w6XZpFXqhnmlTd07tbADoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGAIYTBtErMAAHocjn8g=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423376,
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
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423376,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuW3XpEGEbriNC1+10Yu6DUh+sOl2aRV6oZ5pU3dO7WwBKCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyurdQSw=",
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
  "id": -576460752303423375,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDFGtxIHrHSBVatx421PrQehQihmxnbD+JQsgxEX79gAvvEnghxtNe7O8nwclxt4NdKOnv6/U0PjUnMWqUZUXgDuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrUVyuf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423375,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDFGtxIHrHSBVatx421PrQehQihmxnbD+JQsgxEX79gAvvEnghxtNe7O8nwclxt4NdKOnv6/U0PjUnMWqUZUXgDuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrUVyuf",
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
  "id": -576460752303423374,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEC7ON/lGxN+ZcWLGyrHLZcTYcWFu37FlYbZ4Od0pI8Xk1DOaKypU56fu370XWSa7k1gmCMyac7fp1U8Jg6/8nkMuEDFGtxIHrHSBVatx421PrQehQihmxnbD+JQsgxEX79gAvvEnghxtNe7O8nwclxt4NdKOnv6/U0PjUnMWqUZUXgDuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqcyrHN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423374,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "state": "tx_+NILAfiEuEC7ON/lGxN+ZcWLGyrHLZcTYcWFu37FlYbZ4Od0pI8Xk1DOaKypU56fu370XWSa7k1gmCMyac7fp1U8Jg6/8nkMuEDFGtxIHrHSBVatx421PrQehQihmxnbD+JQsgxEX79gAvvEnghxtNe7O8nwclxt4NdKOnv6/U0PjUnMWqUZUXgDuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqcyrHN"
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "state": "tx_+NILAfiEuEC7ON/lGxN+ZcWLGyrHLZcTYcWFu37FlYbZ4Od0pI8Xk1DOaKypU56fu370XWSa7k1gmCMyac7fp1U8Jg6/8nkMuEDFGtxIHrHSBVatx421PrQehQihmxnbD+JQsgxEX79gAvvEnghxtNe7O8nwclxt4NdKOnv6/U0PjUnMWqUZUXgDuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqcyrHN"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423373,
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
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423373,
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
  "id": -576460752303423372,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423372,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEC7ON/lGxN+ZcWLGyrHLZcTYcWFu37FlYbZ4Od0pI8Xk1DOaKypU56fu370XWSa7k1gmCMyac7fp1U8Jg6/8nkMuEDFGtxIHrHSBVatx421PrQehQihmxnbD+JQsgxEX79gAvvEnghxtNe7O8nwclxt4NdKOnv6/U0PjUnMWqUZUXgDuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sASgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqcyrHN",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423371,
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
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423371,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuW3XpEGEbriNC1+10Yu6DUh+sOl2aRV6oZ5pU3dO7WwBaBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RrTMj0w=",
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
  "id": -576460752303423370,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECCRnx/ylICX003gVvZQnTpXos85EKPEvyvdDwn5THhIvqUWWHaz57wXPPC/LPmdGg9hmiba06SY2ljok2frjkCuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbGsRsw"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423370,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "signed_tx": "tx_+JALAfhCuECCRnx/ylICX003gVvZQnTpXos85EKPEvyvdDwn5THhIvqUWWHaz57wXPPC/LPmdGg9hmiba06SY2ljok2frjkCuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbGsRsw",
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
  "id": -576460752303423369,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECCRnx/ylICX003gVvZQnTpXos85EKPEvyvdDwn5THhIvqUWWHaz57wXPPC/LPmdGg9hmiba06SY2ljok2frjkCuED7ht599WHSQj9T7MTd4Rj5oDPWgqs8Aoo7DViayoKHsnLurMYGZr9HjLYr2mXxFwtlXaDC05ABZcbvt/dNIxcOuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY4HINF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423369,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "state": "tx_+NILAfiEuECCRnx/ylICX003gVvZQnTpXos85EKPEvyvdDwn5THhIvqUWWHaz57wXPPC/LPmdGg9hmiba06SY2ljok2frjkCuED7ht599WHSQj9T7MTd4Rj5oDPWgqs8Aoo7DViayoKHsnLurMYGZr9HjLYr2mXxFwtlXaDC05ABZcbvt/dNIxcOuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY4HINF"
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "state": "tx_+NILAfiEuECCRnx/ylICX003gVvZQnTpXos85EKPEvyvdDwn5THhIvqUWWHaz57wXPPC/LPmdGg9hmiba06SY2ljok2frjkCuED7ht599WHSQj9T7MTd4Rj5oDPWgqs8Aoo7DViayoKHsnLurMYGZr9HjLYr2mXxFwtlXaDC05ABZcbvt/dNIxcOuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY4HINF"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423368,
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
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423368,
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
  "id": -576460752303423367,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423367,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECCRnx/ylICX003gVvZQnTpXos85EKPEvyvdDwn5THhIvqUWWHaz57wXPPC/LPmdGg9hmiba06SY2ljok2frjkCuED7ht599WHSQj9T7MTd4Rj5oDPWgqs8Aoo7DViayoKHsnLurMYGZr9HjLYr2mXxFwtlXaDC05ABZcbvt/dNIxcOuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY4HINF",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhA+LuecsLsoI/QLQBafTBboWKfN5T7FEG2JxUML7lt5n2oSly1/Vj9xUOtclgWTUN9xwSA1hydJE1wUj1OCR4PDrkBKPkBJTsBoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhACAN8uKPZ8b6h2ii2jZwBabZTWxHZ+qSloh/NBU+HR4U3CiYsQTbcueqlust1QsrCPChiEbZZph+xvCtp/XMPAbhAe0ltVhSHzP3Cq3iTK01e5Zk694D7QOrGhEAKf49Qmsj2mf7zdjL8mZosdvZWLpcaPl77vvY27SG7TpxuZ8/dBrhI+EY5AqEG5bdekQYRuuI0LX7XRi7oNSH6w6XZpFXqhnmlTd07tbADoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGAIYTBtErMAAHocjn8g==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhA+LuecsLsoI/QLQBafTBboWKfN5T7FEG2JxUML7lt5n2oSly1/Vj9xUOtclgWTUN9xwSA1hydJE1wUj1OCR4PDrkBKPkBJTsBoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhACAN8uKPZ8b6h2ii2jZwBabZTWxHZ+qSloh/NBU+HR4U3CiYsQTbcueqlust1QsrCPChiEbZZph+xvCtp/XMPAbhAe0ltVhSHzP3Cq3iTK01e5Zk694D7QOrGhEAKf49Qmsj2mf7zdjL8mZosdvZWLpcaPl77vvY27SG7TpxuZ8/dBrhI+EY5AqEG5bdekQYRuuI0LX7XRi7oNSH6w6XZpFXqhnmlTd07tbADoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGAIYTBtErMAAHocjn8g==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "a��!���[�*\u0005H�.Vk{\u001cҖ'uh�K� \u0011�\u0011",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423366,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423366,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBuW3XpEGEbriNC1+10Yu6DUh+sOl2aRV6oZ5pU3dO7WwoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwobjU+NILAfiEuECCRnx/ylICX003gVvZQnTpXos85EKPEvyvdDwn5THhIvqUWWHaz57wXPPC/LPmdGg9hmiba06SY2ljok2frjkCuED7ht599WHSQj9T7MTd4Rj5oDPWgqs8Aoo7DViayoKHsnLurMYGZr9HjLYr2mXxFwtlXaDC05ABZcbvt/dNIxcOuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYAhhMG0SswAAHfwqox",
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
  "method": "channels.snapshot_solo_sign",
  "params": {
    "signed_tx": "tx_+QFxCwH4QrhAgD5beXhUAHM5GrnVGuIdU/5VOwKC/DQDkqOOK6Ku+gqkGOdXHRRtoQVbdPn0uTyKhTTZpCEcbVHHxNJgwjukBrkBKPkBJTsBoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAgkZ8f8pSAl9NN4Fb2UJ06V6LPORCjxL8r3Q8J+Ux4SL6lFlh2s+e8Fzzwvyz5nRoPYZom2tOkmNpY6JNn645ArhA+4beffVh0kI/U+zE3eEY+aAz1oKrPAKKOw1YmsqCh7Jy7qzGBma/R4y2K9pl8RcLZV2gwtOQAWXG77f3TSMXDrhI+EY5AqEG5bdekQYRuuI0LX7XRi7oNSH6w6XZpFXqhnmlTd07tbAFoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGAIYTBtErMAABESg6Gg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAgD5beXhUAHM5GrnVGuIdU/5VOwKC/DQDkqOOK6Ku+gqkGOdXHRRtoQVbdPn0uTyKhTTZpCEcbVHHxNJgwjukBrkBKPkBJTsBoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAgkZ8f8pSAl9NN4Fb2UJ06V6LPORCjxL8r3Q8J+Ux4SL6lFlh2s+e8Fzzwvyz5nRoPYZom2tOkmNpY6JNn645ArhA+4beffVh0kI/U+zE3eEY+aAz1oKrPAKKOw1YmsqCh7Jy7qzGBma/R4y2K9pl8RcLZV2gwtOQAWXG77f3TSMXDrhI+EY5AqEG5bdekQYRuuI0LX7XRi7oNSH6w6XZpFXqhnmlTd07tbAFoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGAIYTBtErMAABESg6Gg==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAgD5beXhUAHM5GrnVGuIdU/5VOwKC/DQDkqOOK6Ku+gqkGOdXHRRtoQVbdPn0uTyKhTTZpCEcbVHHxNJgwjukBrkBKPkBJTsBoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAgkZ8f8pSAl9NN4Fb2UJ06V6LPORCjxL8r3Q8J+Ux4SL6lFlh2s+e8Fzzwvyz5nRoPYZom2tOkmNpY6JNn645ArhA+4beffVh0kI/U+zE3eEY+aAz1oKrPAKKOw1YmsqCh7Jy7qzGBma/R4y2K9pl8RcLZV2gwtOQAWXG77f3TSMXDrhI+EY5AqEG5bdekQYRuuI0LX7XRi7oNSH6w6XZpFXqhnmlTd07tbAFoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGAIYTBtErMAABESg6Gg==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "\u0006�M��(��\u000e炻Q��\u0002[�S\u0000+8Zyc��̿ǜ",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423365,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1013,
        "message": "Tx already on-chain"
      }
    ],
    "message": "Rejected",
    "request": {
      "id": -576460752303423365,
      "jsonrpc": "2.0",
      "method": "channels.snapshot_solo",
      "params": {}
    }
  },
  "id": -576460752303423365,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423364,
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
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423364,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuW3XpEGEbriNC1+10Yu6DUh+sOl2aRV6oZ5pU3dO7WwBqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCypkcVxg=",
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
  "id": -576460752303423363,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECDZlpbEtnrQ4A+itS1h5ahb74XlqhBhFXmdC6KQNMgZaWQ2fFbJ2hG6T5U/Ng8krEXYQCFTl3dZDzlAqbQedIMuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqqqvbj"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423363,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "signed_tx": "tx_+JALAfhCuECDZlpbEtnrQ4A+itS1h5ahb74XlqhBhFXmdC6KQNMgZaWQ2fFbJ2hG6T5U/Ng8krEXYQCFTl3dZDzlAqbQedIMuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqqqvbj",
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
  "id": -576460752303423362,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA4Vvv3JtTk6zuGLpHjDbMkWG020WUvvzZI2ndek39EMxaceexoYt2w/6Fpy7xBxJ9KYgMdTKacxcOEVFCTlSYEuECDZlpbEtnrQ4A+itS1h5ahb74XlqhBhFXmdC6KQNMgZaWQ2fFbJ2hG6T5U/Ng8krEXYQCFTl3dZDzlAqbQedIMuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp2OeUV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423362,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "state": "tx_+NILAfiEuEA4Vvv3JtTk6zuGLpHjDbMkWG020WUvvzZI2ndek39EMxaceexoYt2w/6Fpy7xBxJ9KYgMdTKacxcOEVFCTlSYEuECDZlpbEtnrQ4A+itS1h5ahb74XlqhBhFXmdC6KQNMgZaWQ2fFbJ2hG6T5U/Ng8krEXYQCFTl3dZDzlAqbQedIMuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp2OeUV"
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "state": "tx_+NILAfiEuEA4Vvv3JtTk6zuGLpHjDbMkWG020WUvvzZI2ndek39EMxaceexoYt2w/6Fpy7xBxJ9KYgMdTKacxcOEVFCTlSYEuECDZlpbEtnrQ4A+itS1h5ahb74XlqhBhFXmdC6KQNMgZaWQ2fFbJ2hG6T5U/Ng8krEXYQCFTl3dZDzlAqbQedIMuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp2OeUV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423361,
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
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423361,
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
  "id": -576460752303423360,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423360,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA4Vvv3JtTk6zuGLpHjDbMkWG020WUvvzZI2ndek39EMxaceexoYt2w/6Fpy7xBxJ9KYgMdTKacxcOEVFCTlSYEuECDZlpbEtnrQ4A+itS1h5ahb74XlqhBhFXmdC6KQNMgZaWQ2fFbJ2hG6T5U/Ng8krEXYQCFTl3dZDzlAqbQedIMuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAagpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp2OeUV",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423359,
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
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423359,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuW3XpEGEbriNC1+10Yu6DUh+sOl2aRV6oZ5pU3dO7WwB6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgXkIhs=",
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
  "id": -576460752303423358,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBLYKAu9OQQpc1YrIdotNYwNx5zLHJIdcKve0p7p7TBC+iRJhfsEut/hu7gq2+xu1hcSnSp2uL3nKjpJoOMG8wEuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYj6P4U"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423358,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBLYKAu9OQQpc1YrIdotNYwNx5zLHJIdcKve0p7p7TBC+iRJhfsEut/hu7gq2+xu1hcSnSp2uL3nKjpJoOMG8wEuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYj6P4U",
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
  "id": -576460752303423357,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBLYKAu9OQQpc1YrIdotNYwNx5zLHJIdcKve0p7p7TBC+iRJhfsEut/hu7gq2+xu1hcSnSp2uL3nKjpJoOMG8wEuECTYYsZiE2/0vU81XM+cPECLMImvakvcnH4q9hs/vftsTTbGmloqjnacrwe6d7IZo6Q4QphNAg1K9iLnpPPU5oHuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZXfY/z"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423357,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "state": "tx_+NILAfiEuEBLYKAu9OQQpc1YrIdotNYwNx5zLHJIdcKve0p7p7TBC+iRJhfsEut/hu7gq2+xu1hcSnSp2uL3nKjpJoOMG8wEuECTYYsZiE2/0vU81XM+cPECLMImvakvcnH4q9hs/vftsTTbGmloqjnacrwe6d7IZo6Q4QphNAg1K9iLnpPPU5oHuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZXfY/z"
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "state": "tx_+NILAfiEuEBLYKAu9OQQpc1YrIdotNYwNx5zLHJIdcKve0p7p7TBC+iRJhfsEut/hu7gq2+xu1hcSnSp2uL3nKjpJoOMG8wEuECTYYsZiE2/0vU81XM+cPECLMImvakvcnH4q9hs/vftsTTbGmloqjnacrwe6d7IZo6Q4QphNAg1K9iLnpPPU5oHuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZXfY/z"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423356,
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
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423356,
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
  "id": -576460752303423355,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423355,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBLYKAu9OQQpc1YrIdotNYwNx5zLHJIdcKve0p7p7TBC+iRJhfsEut/hu7gq2+xu1hcSnSp2uL3nKjpJoOMG8wEuECTYYsZiE2/0vU81XM+cPECLMImvakvcnH4q9hs/vftsTTbGmloqjnacrwe6d7IZo6Q4QphNAg1K9iLnpPPU5oHuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZXfY/z",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423354,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423354,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBuW3XpEGEbriNC1+10Yu6DUh+sOl2aRV6oZ5pU3dO7WwoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwobjU+NILAfiEuEBLYKAu9OQQpc1YrIdotNYwNx5zLHJIdcKve0p7p7TBC+iRJhfsEut/hu7gq2+xu1hcSnSp2uL3nKjpJoOMG8wEuECTYYsZiE2/0vU81XM+cPECLMImvakvcnH4q9hs/vftsTTbGmloqjnacrwe6d7IZo6Q4QphNAg1K9iLnpPPU5oHuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAegZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYAhhMG0SswAAJQZk0J",
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
  "method": "channels.snapshot_solo_sign",
  "params": {
    "signed_tx": "tx_+QFxCwH4QrhAqosbvyPwZyTQqoTO4E4j5YKn4dDuVIvHlMGbg7SnAUVoJZJqXHk1G80gLHRKYPBEiX7Ro+612JvzluY0YEhHAbkBKPkBJTsBoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAS2CgLvTkEKXNWKyHaLTWMDcecyxySHXCr3tKe6e0wQvokSYX7BLrf4bu4KtvsbtYXEp0qdri95yo6SaDjBvMBLhAk2GLGYhNv9L1PNVzPnDxAizCJr2pL3Jx+KvYbP737bE02xppaKo52nK8HuneyGaOkOEKYTQINSvYi56Tz1OaB7hI+EY5AqEG5bdekQYRuuI0LX7XRi7oNSH6w6XZpFXqhnmlTd07tbAHoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGAIYTBtErMAACLcnPSA=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423353,
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
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423353,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuW3XpEGEbriNC1+10Yu6DUh+sOl2aRV6oZ5pU3dO7WwCKCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyk4RTlI=",
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
  "id": -576460752303423352,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAKDG9DhpHoXKvV4N015D8zQcihnI+J2U6kBDkejMpNtVX8bXAVrmg5eaREXElYQ/pYMuCpr9Ai0TXluZLsS0kAuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAigpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspDjeAP"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423352,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAKDG9DhpHoXKvV4N015D8zQcihnI+J2U6kBDkejMpNtVX8bXAVrmg5eaREXElYQ/pYMuCpr9Ai0TXluZLsS0kAuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAigpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspDjeAP",
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
  "id": -576460752303423351,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAKDG9DhpHoXKvV4N015D8zQcihnI+J2U6kBDkejMpNtVX8bXAVrmg5eaREXElYQ/pYMuCpr9Ai0TXluZLsS0kAuEBZy5OxBFB9V/MABjMQR7nzd+ZAJ6flk4JZB2ZlIJCNES/HNn2vKY/IK3PGrqsDwwcbuME7k/xUumAtidhqpZMEuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAigpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspFcZOT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423351,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "state": "tx_+NILAfiEuEAKDG9DhpHoXKvV4N015D8zQcihnI+J2U6kBDkejMpNtVX8bXAVrmg5eaREXElYQ/pYMuCpr9Ai0TXluZLsS0kAuEBZy5OxBFB9V/MABjMQR7nzd+ZAJ6flk4JZB2ZlIJCNES/HNn2vKY/IK3PGrqsDwwcbuME7k/xUumAtidhqpZMEuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAigpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspFcZOT"
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "state": "tx_+NILAfiEuEAKDG9DhpHoXKvV4N015D8zQcihnI+J2U6kBDkejMpNtVX8bXAVrmg5eaREXElYQ/pYMuCpr9Ai0TXluZLsS0kAuEBZy5OxBFB9V/MABjMQR7nzd+ZAJ6flk4JZB2ZlIJCNES/HNn2vKY/IK3PGrqsDwwcbuME7k/xUumAtidhqpZMEuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAigpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspFcZOT"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423350,
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
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423350,
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
  "id": -576460752303423349,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423349,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAKDG9DhpHoXKvV4N015D8zQcihnI+J2U6kBDkejMpNtVX8bXAVrmg5eaREXElYQ/pYMuCpr9Ai0TXluZLsS0kAuEBZy5OxBFB9V/MABjMQR7nzd+ZAJ6flk4JZB2ZlIJCNES/HNn2vKY/IK3PGrqsDwwcbuME7k/xUumAtidhqpZMEuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAigpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspFcZOT",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423348,
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
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423348,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuW3XpEGEbriNC1+10Yu6DUh+sOl2aRV6oZ5pU3dO7WwCaBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RngKnws=",
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
  "id": -576460752303423347,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBPyLImvMpl+SK8/BY98mS98voVtXBZ5gcvJh8wmuzA+UVgJDpqA2RurjH+Q7abaOktAzlhJSJNEHAffRU0Io8IuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAmgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEadScxw"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423347,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBPyLImvMpl+SK8/BY98mS98voVtXBZ5gcvJh8wmuzA+UVgJDpqA2RurjH+Q7abaOktAzlhJSJNEHAffRU0Io8IuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAmgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEadScxw",
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
  "id": -576460752303423346,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEARpUlRETrER0CdCocidbCfZJw7bpviKNnh2Yi7Ii94eD9oqNg2XFaStdCmo7UOwkPaF8g7Idb9zFt1c3Ioc5YAuEBPyLImvMpl+SK8/BY98mS98voVtXBZ5gcvJh8wmuzA+UVgJDpqA2RurjH+Q7abaOktAzlhJSJNEHAffRU0Io8IuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAmgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEawEyh5"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423346,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "state": "tx_+NILAfiEuEARpUlRETrER0CdCocidbCfZJw7bpviKNnh2Yi7Ii94eD9oqNg2XFaStdCmo7UOwkPaF8g7Idb9zFt1c3Ioc5YAuEBPyLImvMpl+SK8/BY98mS98voVtXBZ5gcvJh8wmuzA+UVgJDpqA2RurjH+Q7abaOktAzlhJSJNEHAffRU0Io8IuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAmgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEawEyh5"
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "state": "tx_+NILAfiEuEARpUlRETrER0CdCocidbCfZJw7bpviKNnh2Yi7Ii94eD9oqNg2XFaStdCmo7UOwkPaF8g7Idb9zFt1c3Ioc5YAuEBPyLImvMpl+SK8/BY98mS98voVtXBZ5gcvJh8wmuzA+UVgJDpqA2RurjH+Q7abaOktAzlhJSJNEHAffRU0Io8IuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAmgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEawEyh5"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423345,
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
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423345,
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
  "id": -576460752303423344,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423344,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEARpUlRETrER0CdCocidbCfZJw7bpviKNnh2Yi7Ii94eD9oqNg2XFaStdCmo7UOwkPaF8g7Idb9zFt1c3Ioc5YAuEBPyLImvMpl+SK8/BY98mS98voVtXBZ5gcvJh8wmuzA+UVgJDpqA2RurjH+Q7abaOktAzlhJSJNEHAffRU0Io8IuEj4RjkCoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sAmgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEawEyh5",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAqosbvyPwZyTQqoTO4E4j5YKn4dDuVIvHlMGbg7SnAUVoJZJqXHk1G80gLHRKYPBEiX7Ro+612JvzluY0YEhHAbkBKPkBJTsBoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAS2CgLvTkEKXNWKyHaLTWMDcecyxySHXCr3tKe6e0wQvokSYX7BLrf4bu4KtvsbtYXEp0qdri95yo6SaDjBvMBLhAk2GLGYhNv9L1PNVzPnDxAizCJr2pL3Jx+KvYbP737bE02xppaKo52nK8HuneyGaOkOEKYTQINSvYi56Tz1OaB7hI+EY5AqEG5bdekQYRuuI0LX7XRi7oNSH6w6XZpFXqhnmlTd07tbAHoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGAIYTBtErMAACLcnPSA==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAqosbvyPwZyTQqoTO4E4j5YKn4dDuVIvHlMGbg7SnAUVoJZJqXHk1G80gLHRKYPBEiX7Ro+612JvzluY0YEhHAbkBKPkBJTsBoQblt16RBhG64jQtftdGLug1IfrDpdmkVeqGeaVN3Tu1sKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAS2CgLvTkEKXNWKyHaLTWMDcecyxySHXCr3tKe6e0wQvokSYX7BLrf4bu4KtvsbtYXEp0qdri95yo6SaDjBvMBLhAk2GLGYhNv9L1PNVzPnDxAizCJr2pL3Jx+KvYbP737bE02xppaKo52nK8HuneyGaOkOEKYTQINSvYi56Tz1OaB7hI+EY5AqEG5bdekQYRuuI0LX7XRi7oNSH6w6XZpFXqhnmlTd07tbAHoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGAIYTBtErMAACLcnPSA==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "\u0012\rh>��ZTY-�[�\u000f���f��b]�Θ�n1H\t",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423343,
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
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423343,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423342,
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
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
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
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
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
  "channel_id": "ch_2kAo4oGpeKoDwzRDkuwHgAa3L1pZSfCoNWP7BasWtsFjuy4ziz",
  "id": -576460752303423342,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
