
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&minimum_depth=0&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_reconnect_early%2F2916
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
      "fsm_id": "ba_kP6miwbJUYxg5rz8SnL5VK18jVxBTH6ITFjKBjItu9Nnz32h"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&minimum_depth=0&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_reconnect_early%2F2916
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
      "fsm_id": "ba_HHzKNzlZ5f5Le5wxppmJwKCSqXedVTGzitEb+E+vEJ0KpAHJ"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYZbIWcFg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423157,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBrqfYqVTyFoOgBBR0HDdnhqlrvCO+I+FGM3i+HmpAGLzpcNumrJREe/acmAjYo2fAwCKwo03NSLtZANj/CI6IOuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGGT9fAZI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423157,
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_HHzKNzlZ5f5Le5wxppmJwKCSqXedVTGzitEb+E+vEJ0KpAHJ"
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEBrqfYqVTyFoOgBBR0HDdnhqlrvCO+I+FGM3i+HmpAGLzpcNumrJREe/acmAjYo2fAwCKwo03NSLtZANj/CI6IOuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGGT9fAZI=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423156,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAa6n2KlU8haDoAQUdBw3Z4apa7wjviPhRjN4vh5qQBi86XDbpqyURHv2nJgI2KNnwMAisKNNzUi7WQDY/wiOiDrhAlhA1B1edASE+bEhMisIeCDT6YbOK3OK4uKQ22sobF4O+8cxYQFlThEd1WSC5d9z5gRWpjC41Vu27UkzyIWZgB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhnTQ89O"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
  "id": -576460752303423156,
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAa6n2KlU8haDoAQUdBw3Z4apa7wjviPhRjN4vh5qQBi86XDbpqyURHv2nJgI2KNnwMAisKNNzUi7WQDY/wiOiDrhAlhA1B1edASE+bEhMisIeCDT6YbOK3OK4uKQ22sobF4O+8cxYQFlThEd1WSC5d9z5gRWpjC41Vu27UkzyIWZgB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhnTQ89O",
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_kP6miwbJUYxg5rz8SnL5VK18jVxBTH6ITFjKBjItu9Nnz32h"
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAa6n2KlU8haDoAQUdBw3Z4apa7wjviPhRjN4vh5qQBi86XDbpqyURHv2nJgI2KNnwMAisKNNzUi7WQDY/wiOiDrhAlhA1B1edASE+bEhMisIeCDT6YbOK3OK4uKQ22sobF4O+8cxYQFlThEd1WSC5d9z5gRWpjC41Vu27UkzyIWZgB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhnTQ89O",
      "type": "channel_create_tx"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz&existing_fsm_id=ba_kP6miwbJUYxg5rz8SnL5VK18jVxBTH6ITFjKBjItu9Nnz32h&host=localhost&port=13179&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_kP6miwbJUYxg5rz8SnL5VK18jVxBTH6ITFjKBjItu9Nnz32h"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAa6n2KlU8haDoAQUdBw3Z4apa7wjviPhRjN4vh5qQBi86XDbpqyURHv2nJgI2KNnwMAisKNNzUi7WQDY/wiOiDrhAlhA1B1edASE+bEhMisIeCDT6YbOK3OK4uKQ22sobF4O+8cxYQFlThEd1WSC5d9z5gRWpjC41Vu27UkzyIWZgB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhnTQ89O",
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAa6n2KlU8haDoAQUdBw3Z4apa7wjviPhRjN4vh5qQBi86XDbpqyURHv2nJgI2KNnwMAisKNNzUi7WQDY/wiOiDrhAlhA1B1edASE+bEhMisIeCDT6YbOK3OK4uKQ22sobF4O+8cxYQFlThEd1WSC5d9z5gRWpjC41Vu27UkzyIWZgB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhnTQ89O",
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
    "data": {
      "state": "tx_+QENCwH4hLhAa6n2KlU8haDoAQUdBw3Z4apa7wjviPhRjN4vh5qQBi86XDbpqyURHv2nJgI2KNnwMAisKNNzUi7WQDY/wiOiDrhAlhA1B1edASE+bEhMisIeCDT6YbOK3OK4uKQ22sobF4O+8cxYQFlThEd1WSC5d9z5gRWpjC41Vu27UkzyIWZgB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhnTQ89O"
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
    "data": {
      "state": "tx_+QENCwH4hLhAa6n2KlU8haDoAQUdBw3Z4apa7wjviPhRjN4vh5qQBi86XDbpqyURHv2nJgI2KNnwMAisKNNzUi7WQDY/wiOiDrhAlhA1B1edASE+bEhMisIeCDT6YbOK3OK4uKQ22sobF4O+8cxYQFlThEd1WSC5d9z5gRWpjC41Vu27UkzyIWZgB7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhnTQ89O"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
    "data": {
      "message": {
        "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
    "data": {
      "message": {
        "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
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
  "id": -576460752303423155,
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
  "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
  "id": -576460752303423155,
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBtKiXpjDC4OOxE4f31MhmzvUmQWw5WpG4NvQ1Swr1VVeoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+rniy/+GHLHOiuwBAIYPXtZ/KAAar9KVqQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423154,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEAbVhVoKnLL+FZr8VeNYkMjlN2w4AchmKQ5ltG6ksVFUxu/pLOEYdviqqmV2sXceBswtSRjzH9gHKRqKdp8D8ACuF/4XTUBoQbSol6YwwuDjsROH99TIZs71JkFsOVqRuDb0NUsK9VVXqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAGvEX+tk="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
  "id": -576460752303423154,
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEAbVhVoKnLL+FZr8VeNYkMjlN2w4AchmKQ5ltG6ksVFUxu/pLOEYdviqqmV2sXceBswtSRjzH9gHKRqKdp8D8ACuF/4XTUBoQbSol6YwwuDjsROH99TIZs71JkFsOVqRuDb0NUsK9VVXqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAGvEX+tk=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423153,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEAbVhVoKnLL+FZr8VeNYkMjlN2w4AchmKQ5ltG6ksVFUxu/pLOEYdviqqmV2sXceBswtSRjzH9gHKRqKdp8D8ACuECmEZBDrmsVXx2ckXvLRST2o8eKtYuOz72Sl9p9gYbd+3zFsRAc4kByU4W15YQDuVxoToPKklMspNIb3m7b6tgGuF/4XTUBoQbSol6YwwuDjsROH99TIZs71JkFsOVqRuDb0NUsK9VVXqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAGvHg7xE="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
  "id": -576460752303423153,
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAbVhVoKnLL+FZr8VeNYkMjlN2w4AchmKQ5ltG6ksVFUxu/pLOEYdviqqmV2sXceBswtSRjzH9gHKRqKdp8D8ACuECmEZBDrmsVXx2ckXvLRST2o8eKtYuOz72Sl9p9gYbd+3zFsRAc4kByU4W15YQDuVxoToPKklMspNIb3m7b6tgGuF/4XTUBoQbSol6YwwuDjsROH99TIZs71JkFsOVqRuDb0NUsK9VVXqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAGvHg7xE=",
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAbVhVoKnLL+FZr8VeNYkMjlN2w4AchmKQ5ltG6ksVFUxu/pLOEYdviqqmV2sXceBswtSRjzH9gHKRqKdp8D8ACuECmEZBDrmsVXx2ckXvLRST2o8eKtYuOz72Sl9p9gYbd+3zFsRAc4kByU4W15YQDuVxoToPKklMspNIb3m7b6tgGuF/4XTUBoQbSol6YwwuDjsROH99TIZs71JkFsOVqRuDb0NUsK9VVXqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAGvHg7xE=",
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAbVhVoKnLL+FZr8VeNYkMjlN2w4AchmKQ5ltG6ksVFUxu/pLOEYdviqqmV2sXceBswtSRjzH9gHKRqKdp8D8ACuECmEZBDrmsVXx2ckXvLRST2o8eKtYuOz72Sl9p9gYbd+3zFsRAc4kByU4W15YQDuVxoToPKklMspNIb3m7b6tgGuF/4XTUBoQbSol6YwwuDjsROH99TIZs71JkFsOVqRuDb0NUsK9VVXqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAGvHg7xE=",
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAbVhVoKnLL+FZr8VeNYkMjlN2w4AchmKQ5ltG6ksVFUxu/pLOEYdviqqmV2sXceBswtSRjzH9gHKRqKdp8D8ACuECmEZBDrmsVXx2ckXvLRST2o8eKtYuOz72Sl9p9gYbd+3zFsRAc4kByU4W15YQDuVxoToPKklMspNIb3m7b6tgGuF/4XTUBoQbSol6YwwuDjsROH99TIZs71JkFsOVqRuDb0NUsK9VVXqEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAGvHg7xE=",
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
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
    "channel_id": "ch_2bmNRYsmdxAHxtJhQgjLZDeoXmeHsHRrustxU8qGFoq4wHoitz",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
