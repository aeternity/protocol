
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
      "fsm_id": "ba_dhRMEE+MzPGMtXx0mZgqyYSnohuAeCyx+yyGkW9S6WrpGeBy"
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
      "fsm_id": "ba_6U5gwCBkPu8t7Z/aJ5GUvKQMTUaJ+xcVYx4nUZDP4b4GGWjF"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZpKp1Cow==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422490,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECfAO6+VfEZw6eFUjvAJvtArWonN/1mkSsZBnMmd9cPr4v804J3PGT6xyG2os7muCSHt0EPU3XdShuGSDhTXKkFuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGaf326Jo="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422490,
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_6U5gwCBkPu8t7Z/aJ5GUvKQMTUaJ+xcVYx4nUZDP4b4GGWjF"
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "signed_tx": "tx_+MsLAfhCuECfAO6+VfEZw6eFUjvAJvtArWonN/1mkSsZBnMmd9cPr4v804J3PGT6xyG2os7muCSHt0EPU3XdShuGSDhTXKkFuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGaf326Jo=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422489,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhALlfpEiqreeC61bwREsUXqeyA74CQid8gqg1K1XPLACncLEzGup4r4GwY3r8WP9uDhihNB+8EeB/F/iL+oYviDbhAnwDuvlXxGcOnhVI7wCb7QK1qJzf9ZpErGQZzJnfXD6+L/NOCdzxk+schtqLO5rgkh7dBD1N13Uobhkg4U1ypBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rmn1EEQF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
  "id": -576460752303422489,
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhALlfpEiqreeC61bwREsUXqeyA74CQid8gqg1K1XPLACncLEzGup4r4GwY3r8WP9uDhihNB+8EeB/F/iL+oYviDbhAnwDuvlXxGcOnhVI7wCb7QK1qJzf9ZpErGQZzJnfXD6+L/NOCdzxk+schtqLO5rgkh7dBD1N13Uobhkg4U1ypBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rmn1EEQF",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_dhRMEE+MzPGMtXx0mZgqyYSnohuAeCyx+yyGkW9S6WrpGeBy"
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhALlfpEiqreeC61bwREsUXqeyA74CQid8gqg1K1XPLACncLEzGup4r4GwY3r8WP9uDhihNB+8EeB/F/iL+oYviDbhAnwDuvlXxGcOnhVI7wCb7QK1qJzf9ZpErGQZzJnfXD6+L/NOCdzxk+schtqLO5rgkh7dBD1N13Uobhkg4U1ypBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rmn1EEQF",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhALlfpEiqreeC61bwREsUXqeyA74CQid8gqg1K1XPLACncLEzGup4r4GwY3r8WP9uDhihNB+8EeB/F/iL+oYviDbhAnwDuvlXxGcOnhVI7wCb7QK1qJzf9ZpErGQZzJnfXD6+L/NOCdzxk+schtqLO5rgkh7dBD1N13Uobhkg4U1ypBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rmn1EEQF",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhALlfpEiqreeC61bwREsUXqeyA74CQid8gqg1K1XPLACncLEzGup4r4GwY3r8WP9uDhihNB+8EeB/F/iL+oYviDbhAnwDuvlXxGcOnhVI7wCb7QK1qJzf9ZpErGQZzJnfXD6+L/NOCdzxk+schtqLO5rgkh7dBD1N13Uobhkg4U1ypBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rmn1EEQF",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "message": {
        "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "message": {
        "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
  "id": -576460752303422488,
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
  "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
  "id": -576460752303422488,
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "state": "tx_+QENCwH4hLhALlfpEiqreeC61bwREsUXqeyA74CQid8gqg1K1XPLACncLEzGup4r4GwY3r8WP9uDhihNB+8EeB/F/iL+oYviDbhAnwDuvlXxGcOnhVI7wCb7QK1qJzf9ZpErGQZzJnfXD6+L/NOCdzxk+schtqLO5rgkh7dBD1N13Uobhkg4U1ypBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rmn1EEQF"
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "state": "tx_+QENCwH4hLhALlfpEiqreeC61bwREsUXqeyA74CQid8gqg1K1XPLACncLEzGup4r4GwY3r8WP9uDhihNB+8EeB/F/iL+oYviDbhAnwDuvlXxGcOnhVI7wCb7QK1qJzf9ZpErGQZzJnfXD6+L/NOCdzxk+schtqLO5rgkh7dBD1N13Uobhkg4U1ypBbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rmn1EEQF"
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "message": {
        "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "message": {
        "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
  "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "message": {
        "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "message": {
        "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2,
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBj65mZWhx7YCsRCCrgVWqXWCCheV4OGC/sjg/krcFuWdoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQIAhuCRDDYefqAPDv3EgYxO6pJCcB7FVjOvZgsDtaevvDl0iT9iRjxNjgJq3X/0TA==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainDeposit"
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
  "id": -576460752303422487,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuECzVdnBz+33YJ1SQDRzU0Mo0Edj299VZ/dHcQyVqiXc2QG0bHKnS1JM5+AsjlS+VydzR34tGlxvm++4LtoxpqUOuHT4cjMBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIbgkQw2Hn6gDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CapshC7E="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
  "id": -576460752303422487,
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "signed_tx": "tx_+LwLAfhCuECzVdnBz+33YJ1SQDRzU0Mo0Edj299VZ/dHcQyVqiXc2QG0bHKnS1JM5+AsjlS+VydzR34tGlxvm++4LtoxpqUOuHT4cjMBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIbgkQw2Hn6gDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CapshC7E=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainDeposit"
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
  "id": -576460752303422486,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuECnmZQFwOGH6tCHL5oKEnVB6jQtW+1LYKOgvXgBIDbP8c2hy0kHNKPM7j7lsfoMHIKtMqlIysXrqWQsaR10d8QLuECzVdnBz+33YJ1SQDRzU0Mo0Edj299VZ/dHcQyVqiXc2QG0bHKnS1JM5+AsjlS+VydzR34tGlxvm++4LtoxpqUOuHT4cjMBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIbgkQw2Hn6gDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CalZ78Sk="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
  "id": -576460752303422486,
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuECnmZQFwOGH6tCHL5oKEnVB6jQtW+1LYKOgvXgBIDbP8c2hy0kHNKPM7j7lsfoMHIKtMqlIysXrqWQsaR10d8QLuECzVdnBz+33YJ1SQDRzU0Mo0Edj299VZ/dHcQyVqiXc2QG0bHKnS1JM5+AsjlS+VydzR34tGlxvm++4LtoxpqUOuHT4cjMBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIbgkQw2Hn6gDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CalZ78Sk=",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuECnmZQFwOGH6tCHL5oKEnVB6jQtW+1LYKOgvXgBIDbP8c2hy0kHNKPM7j7lsfoMHIKtMqlIysXrqWQsaR10d8QLuECzVdnBz+33YJ1SQDRzU0Mo0Edj299VZ/dHcQyVqiXc2QG0bHKnS1JM5+AsjlS+VydzR34tGlxvm++4LtoxpqUOuHT4cjMBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIbgkQw2Hn6gDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CalZ78Sk=",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "message": {
        "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "message": {
        "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "info": "Hello back",
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
      }
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECnmZQFwOGH6tCHL5oKEnVB6jQtW+1LYKOgvXgBIDbP8c2hy0kHNKPM7j7lsfoMHIKtMqlIysXrqWQsaR10d8QLuECzVdnBz+33YJ1SQDRzU0Mo0Edj299VZ/dHcQyVqiXc2QG0bHKnS1JM5+AsjlS+VydzR34tGlxvm++4LtoxpqUOuHT4cjMBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIbgkQw2Hn6gDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CalZ78Sk=",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECnmZQFwOGH6tCHL5oKEnVB6jQtW+1LYKOgvXgBIDbP8c2hy0kHNKPM7j7lsfoMHIKtMqlIysXrqWQsaR10d8QLuECzVdnBz+33YJ1SQDRzU0Mo0Edj299VZ/dHcQyVqiXc2QG0bHKnS1JM5+AsjlS+VydzR34tGlxvm++4LtoxpqUOuHT4cjMBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIbgkQw2Hn6gDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CalZ78Sk=",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "state": "tx_+P4LAfiEuECnmZQFwOGH6tCHL5oKEnVB6jQtW+1LYKOgvXgBIDbP8c2hy0kHNKPM7j7lsfoMHIKtMqlIysXrqWQsaR10d8QLuECzVdnBz+33YJ1SQDRzU0Mo0Edj299VZ/dHcQyVqiXc2QG0bHKnS1JM5+AsjlS+VydzR34tGlxvm++4LtoxpqUOuHT4cjMBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIbgkQw2Hn6gDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CalZ78Sk="
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "state": "tx_+P4LAfiEuECnmZQFwOGH6tCHL5oKEnVB6jQtW+1LYKOgvXgBIDbP8c2hy0kHNKPM7j7lsfoMHIKtMqlIysXrqWQsaR10d8QLuECzVdnBz+33YJ1SQDRzU0Mo0Edj299VZ/dHcQyVqiXc2QG0bHKnS1JM5+AsjlS+VydzR34tGlxvm++4LtoxpqUOuHT4cjMBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIbgkQw2Hn6gDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CalZ78Sk="
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "message": {
        "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "message": {
        "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "info": "Hello back",
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
  "method": "channels.deposit",
  "params": {
    "amount": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "message": {
        "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "message": {
        "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "info": "Hello back",
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
  "method": "channels.deposit",
  "params": {
    "amount": 2,
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBj65mZWhx7YCsRCCrgVWqXWCCheV4OGC/sjg/krcFuWdoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQIAhuCRDDYefqBY8rhhwx3FNZzZtoqk4aiWG2eYbpEkfYl8gYb5T3SICgMr7qUe8w==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainDeposit"
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
  "id": -576460752303422485,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEA4xc31dWVNa0dIsTG3IaIjPrI+EHpRjn5bXLwDf7r6dWwlsVS6WkUHDBjMRokuq+8TcCgwhi27woCST3MamboPuHT4cjMBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIbgkQw2Hn6gWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDKxP3w6E="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
  "id": -576460752303422485,
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEA4xc31dWVNa0dIsTG3IaIjPrI+EHpRjn5bXLwDf7r6dWwlsVS6WkUHDBjMRokuq+8TcCgwhi27woCST3MamboPuHT4cjMBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIbgkQw2Hn6gWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDKxP3w6E=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainDeposit"
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
  "id": -576460752303422484,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEAbhTlSg/xNl9edrAtRdAm8PfjIT4TbAVE4syKXHgdJ+LLJ5aElt8Ppc+T4dO7s1h4ITbFJ8pNB+ouaGE/wl7cJuEA4xc31dWVNa0dIsTG3IaIjPrI+EHpRjn5bXLwDf7r6dWwlsVS6WkUHDBjMRokuq+8TcCgwhi27woCST3MamboPuHT4cjMBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIbgkQw2Hn6gWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDK/IRGBQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
  "id": -576460752303422484,
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEAbhTlSg/xNl9edrAtRdAm8PfjIT4TbAVE4syKXHgdJ+LLJ5aElt8Ppc+T4dO7s1h4ITbFJ8pNB+ouaGE/wl7cJuEA4xc31dWVNa0dIsTG3IaIjPrI+EHpRjn5bXLwDf7r6dWwlsVS6WkUHDBjMRokuq+8TcCgwhi27woCST3MamboPuHT4cjMBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIbgkQw2Hn6gWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDK/IRGBQ=",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEAbhTlSg/xNl9edrAtRdAm8PfjIT4TbAVE4syKXHgdJ+LLJ5aElt8Ppc+T4dO7s1h4ITbFJ8pNB+ouaGE/wl7cJuEA4xc31dWVNa0dIsTG3IaIjPrI+EHpRjn5bXLwDf7r6dWwlsVS6WkUHDBjMRokuq+8TcCgwhi27woCST3MamboPuHT4cjMBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIbgkQw2Hn6gWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDK/IRGBQ=",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "message": {
        "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "message": {
        "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "info": "Hello back",
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
      }
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAbhTlSg/xNl9edrAtRdAm8PfjIT4TbAVE4syKXHgdJ+LLJ5aElt8Ppc+T4dO7s1h4ITbFJ8pNB+ouaGE/wl7cJuEA4xc31dWVNa0dIsTG3IaIjPrI+EHpRjn5bXLwDf7r6dWwlsVS6WkUHDBjMRokuq+8TcCgwhi27woCST3MamboPuHT4cjMBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIbgkQw2Hn6gWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDK/IRGBQ=",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAbhTlSg/xNl9edrAtRdAm8PfjIT4TbAVE4syKXHgdJ+LLJ5aElt8Ppc+T4dO7s1h4ITbFJ8pNB+ouaGE/wl7cJuEA4xc31dWVNa0dIsTG3IaIjPrI+EHpRjn5bXLwDf7r6dWwlsVS6WkUHDBjMRokuq+8TcCgwhi27woCST3MamboPuHT4cjMBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIbgkQw2Hn6gWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDK/IRGBQ=",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "state": "tx_+P4LAfiEuEAbhTlSg/xNl9edrAtRdAm8PfjIT4TbAVE4syKXHgdJ+LLJ5aElt8Ppc+T4dO7s1h4ITbFJ8pNB+ouaGE/wl7cJuEA4xc31dWVNa0dIsTG3IaIjPrI+EHpRjn5bXLwDf7r6dWwlsVS6WkUHDBjMRokuq+8TcCgwhi27woCST3MamboPuHT4cjMBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIbgkQw2Hn6gWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDK/IRGBQ="
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "state": "tx_+P4LAfiEuEAbhTlSg/xNl9edrAtRdAm8PfjIT4TbAVE4syKXHgdJ+LLJ5aElt8Ppc+T4dO7s1h4ITbFJ8pNB+ouaGE/wl7cJuEA4xc31dWVNa0dIsTG3IaIjPrI+EHpRjn5bXLwDf7r6dWwlsVS6WkUHDBjMRokuq+8TcCgwhi27woCST3MamboPuHT4cjMBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIbgkQw2Hn6gWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDK/IRGBQ="
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBj65mZWhx7YCsRCCrgVWqXWCCheV4OGC/sjg/krcFuWdoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+rnizAGGHLHOiuwDAIYPXtZ/KABrQiFkfg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422483,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEBDs/rf2dOKnuxErRDWJzpvXZwD//0XSxNbSBXAwmfpTQz7GB9uqsWBrofOg8E+gElo00s7KWomhDzhODyZsdwLuF/4XTUBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54swBhhyxzorsAwCGD17WfygAa/eH+T0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
  "id": -576460752303422483,
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEBDs/rf2dOKnuxErRDWJzpvXZwD//0XSxNbSBXAwmfpTQz7GB9uqsWBrofOg8E+gElo00s7KWomhDzhODyZsdwLuF/4XTUBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54swBhhyxzorsAwCGD17WfygAa/eH+T0=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422482,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEBDs/rf2dOKnuxErRDWJzpvXZwD//0XSxNbSBXAwmfpTQz7GB9uqsWBrofOg8E+gElo00s7KWomhDzhODyZsdwLuEB6dsXE7mqyN1a4yI3AJtl/sbJoGeACCjQ+ZWrrCZHhoqU4ISDDCWnBQ19Q5W25UlgTf09eIc2xCLmaHzHz89oDuF/4XTUBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54swBhhyxzorsAwCGD17WfygAaxfnLV8="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
  "id": -576460752303422482,
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBDs/rf2dOKnuxErRDWJzpvXZwD//0XSxNbSBXAwmfpTQz7GB9uqsWBrofOg8E+gElo00s7KWomhDzhODyZsdwLuEB6dsXE7mqyN1a4yI3AJtl/sbJoGeACCjQ+ZWrrCZHhoqU4ISDDCWnBQ19Q5W25UlgTf09eIc2xCLmaHzHz89oDuF/4XTUBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54swBhhyxzorsAwCGD17WfygAaxfnLV8=",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBDs/rf2dOKnuxErRDWJzpvXZwD//0XSxNbSBXAwmfpTQz7GB9uqsWBrofOg8E+gElo00s7KWomhDzhODyZsdwLuEB6dsXE7mqyN1a4yI3AJtl/sbJoGeACCjQ+ZWrrCZHhoqU4ISDDCWnBQ19Q5W25UlgTf09eIc2xCLmaHzHz89oDuF/4XTUBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54swBhhyxzorsAwCGD17WfygAaxfnLV8=",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBDs/rf2dOKnuxErRDWJzpvXZwD//0XSxNbSBXAwmfpTQz7GB9uqsWBrofOg8E+gElo00s7KWomhDzhODyZsdwLuEB6dsXE7mqyN1a4yI3AJtl/sbJoGeACCjQ+ZWrrCZHhoqU4ISDDCWnBQ19Q5W25UlgTf09eIc2xCLmaHzHz89oDuF/4XTUBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54swBhhyxzorsAwCGD17WfygAaxfnLV8=",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBDs/rf2dOKnuxErRDWJzpvXZwD//0XSxNbSBXAwmfpTQz7GB9uqsWBrofOg8E+gElo00s7KWomhDzhODyZsdwLuEB6dsXE7mqyN1a4yI3AJtl/sbJoGeACCjQ+ZWrrCZHhoqU4ISDDCWnBQ19Q5W25UlgTf09eIc2xCLmaHzHz89oDuF/4XTUBoQY+uZmVoce2ArEQgq4FVql1ggoXleDhgv7I4P5K3BblnaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54swBhhyxzorsAwCGD17WfygAaxfnLV8=",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
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
    "channel_id": "ch_UdE73G5Q2qPA2KkpmFXWHRVmhrqK52hGYUV87s6QhNmh39ZKG",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
