
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
      "fsm_id": "ba_c2K4tbmjgMWyLqrEVY3lqZTLkNV1cWgDn9MB4wkgJX4eaWDj"
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
      "fsm_id": "ba_pX7obV77vJGJskFjx0EBLtiD6cjM+5hGz+g8fOjt4x53qw//"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZCiGv0HQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422617,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECS42dexhTlHanTor4L/l6g2t9FQduJdZiP1oxc0qTlhL4BL/bU+B79AJHoQawAl2RM18f5iVVZt0VoYztGMdkNuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGQn+B+n4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422617,
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_pX7obV77vJGJskFjx0EBLtiD6cjM+5hGz+g8fOjt4x53qw//"
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
    "data": {
      "signed_tx": "tx_+MsLAfhCuECS42dexhTlHanTor4L/l6g2t9FQduJdZiP1oxc0qTlhL4BL/bU+B79AJHoQawAl2RM18f5iVVZt0VoYztGMdkNuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGQn+B+n4=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422616,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAkuNnXsYU5R2p06K+C/5eoNrfRUHbiXWYj9aMXNKk5YS+AS/21Pge/QCR6EGsAJdkTNfH+YlVWbdFaGM7RjHZDbhAu5HvANDdwAZp5XylvXMagbrWaqy71j3Vhh/9jN5hgESVK+EXMY2WwgNaAZogaQLYkhnky/aGUS9oIaZmdocqA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkI/54zP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
  "id": -576460752303422616,
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAkuNnXsYU5R2p06K+C/5eoNrfRUHbiXWYj9aMXNKk5YS+AS/21Pge/QCR6EGsAJdkTNfH+YlVWbdFaGM7RjHZDbhAu5HvANDdwAZp5XylvXMagbrWaqy71j3Vhh/9jN5hgESVK+EXMY2WwgNaAZogaQLYkhnky/aGUS9oIaZmdocqA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkI/54zP",
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_c2K4tbmjgMWyLqrEVY3lqZTLkNV1cWgDn9MB4wkgJX4eaWDj"
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAkuNnXsYU5R2p06K+C/5eoNrfRUHbiXWYj9aMXNKk5YS+AS/21Pge/QCR6EGsAJdkTNfH+YlVWbdFaGM7RjHZDbhAu5HvANDdwAZp5XylvXMagbrWaqy71j3Vhh/9jN5hgESVK+EXMY2WwgNaAZogaQLYkhnky/aGUS9oIaZmdocqA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkI/54zP",
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAkuNnXsYU5R2p06K+C/5eoNrfRUHbiXWYj9aMXNKk5YS+AS/21Pge/QCR6EGsAJdkTNfH+YlVWbdFaGM7RjHZDbhAu5HvANDdwAZp5XylvXMagbrWaqy71j3Vhh/9jN5hgESVK+EXMY2WwgNaAZogaQLYkhnky/aGUS9oIaZmdocqA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkI/54zP",
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAkuNnXsYU5R2p06K+C/5eoNrfRUHbiXWYj9aMXNKk5YS+AS/21Pge/QCR6EGsAJdkTNfH+YlVWbdFaGM7RjHZDbhAu5HvANDdwAZp5XylvXMagbrWaqy71j3Vhh/9jN5hgESVK+EXMY2WwgNaAZogaQLYkhnky/aGUS9oIaZmdocqA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkI/54zP",
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
    "data": {
      "message": {
        "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
    "data": {
      "message": {
        "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
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
  "id": -576460752303422615,
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
  "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
  "id": -576460752303422615,
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
    "data": {
      "state": "tx_+QENCwH4hLhAkuNnXsYU5R2p06K+C/5eoNrfRUHbiXWYj9aMXNKk5YS+AS/21Pge/QCR6EGsAJdkTNfH+YlVWbdFaGM7RjHZDbhAu5HvANDdwAZp5XylvXMagbrWaqy71j3Vhh/9jN5hgESVK+EXMY2WwgNaAZogaQLYkhnky/aGUS9oIaZmdocqA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkI/54zP"
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
    "data": {
      "state": "tx_+QENCwH4hLhAkuNnXsYU5R2p06K+C/5eoNrfRUHbiXWYj9aMXNKk5YS+AS/21Pge/QCR6EGsAJdkTNfH+YlVWbdFaGM7RjHZDbhAu5HvANDdwAZp5XylvXMagbrWaqy71j3Vhh/9jN5hgESVK+EXMY2WwgNaAZogaQLYkhnky/aGUS9oIaZmdocqA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkI/54zP"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {
    "fee": 123456789876543
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBovxlPvqjGrwcjfD/yq2g0G7D0rq+BZr57ZMOuKSWEMQoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYC5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGcEiGGw8/Qz8tYMo=",
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
    "signed_tx": "tx_+QHrCwH4QrhAGokdKefb7PxGcyuu5k0iPSA2v33EwYsS80AYL3boMrF/y8lvSwIFT4w36cCsnRGJvh3aczmTTzLQzCEbjd3WA7kBovkBnzYBoQaL8ZT76oxq8HI3w/8qtoNBuw9K6vgWa+e2TDriklhDEKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhnBIhhsPP0PXHQpa"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAGokdKefb7PxGcyuu5k0iPSA2v33EwYsS80AYL3boMrF/y8lvSwIFT4w36cCsnRGJvh3aczmTTzLQzCEbjd3WA7kBovkBnzYBoQaL8ZT76oxq8HI3w/8qtoNBuw9K6vgWa+e2TDriklhDEKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhnBIhhsPP0PXHQpa",
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAGokdKefb7PxGcyuu5k0iPSA2v33EwYsS80AYL3boMrF/y8lvSwIFT4w36cCsnRGJvh3aczmTTzLQzCEbjd3WA7kBovkBnzYBoQaL8ZT76oxq8HI3w/8qtoNBuw9K6vgWa+e2TDriklhDEKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhnBIhhsPP0PXHQpa",
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
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
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBovxlPvqjGrwcjfD/yq2g0G7D0rq+BZr57ZMOuKSWEMQoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/+GJGE5yoABAIYPXtZ/KAAaFSyU1A==",
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
    "signed_tx": "tx_+KcLAfhCuEBTJlutqt4mnclYCDkkgSnaMLIHGQLBu+CLI4U2AAIxS6lJK2obshL2Tnrs6lTobwHwtWObqs13niCX4nY5fO4JuF/4XTgBoQaL8ZT76oxq8HI3w/8qtoNBuw9K6vgWa+e2TDriklhDEKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAGkww86s="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBTJlutqt4mnclYCDkkgSnaMLIHGQLBu+CLI4U2AAIxS6lJK2obshL2Tnrs6lTobwHwtWObqs13niCX4nY5fO4JuF/4XTgBoQaL8ZT76oxq8HI3w/8qtoNBuw9K6vgWa+e2TDriklhDEKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAGkww86s=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBTJlutqt4mnclYCDkkgSnaMLIHGQLBu+CLI4U2AAIxS6lJK2obshL2Tnrs6lTobwHwtWObqs13niCX4nY5fO4JuF/4XTgBoQaL8ZT76oxq8HI3w/8qtoNBuw9K6vgWa+e2TDriklhDEKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAGkww86s=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
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
    "channel_id": "ch_24dg4Z8DQnD159p8aL6f7CcVjKGvpntbdwA3zH21VrxLtn7QYf",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection

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
      "fsm_id": "ba_18TfKV0ElcRGUysptLrZTQhidYvwaeZOLzaRterLuhBqGYOy"
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
      "fsm_id": "ba_y6pc3V8yuI+nm93iLEEz2wwjw1gYHT0ELLnfIP1FAaya6/Lj"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZEM4M/eg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422614,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAs98I64lAkJHNP1hGTl6IQbeiWgwOsydkYzsE1l7Ggk7wx9lhqbAAeELdSWTmMEn7XMS/ZbzAeI2h//3ocQo4LuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGRInuNTE="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422614,
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_y6pc3V8yuI+nm93iLEEz2wwjw1gYHT0ELLnfIP1FAaya6/Lj"
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEAs98I64lAkJHNP1hGTl6IQbeiWgwOsydkYzsE1l7Ggk7wx9lhqbAAeELdSWTmMEn7XMS/ZbzAeI2h//3ocQo4LuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGRInuNTE=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422613,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhALPfCOuJQJCRzT9YRk5eiEG3oloMDrMnZGM7BNZexoJO8MfZYamwAHhC3Ulk5jBJ+1zEv2W8wHiNof/96HEKOC7hAtvhgGRAKXWZGO7GGeiul7/SYJNADDsYebg2CV55ZVOGbhd/wXnLoe5wx5uyjaJeRg0Mr84UhNn+et5Vh+SXKDbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkQRcfd5"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
  "id": -576460752303422613,
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhALPfCOuJQJCRzT9YRk5eiEG3oloMDrMnZGM7BNZexoJO8MfZYamwAHhC3Ulk5jBJ+1zEv2W8wHiNof/96HEKOC7hAtvhgGRAKXWZGO7GGeiul7/SYJNADDsYebg2CV55ZVOGbhd/wXnLoe5wx5uyjaJeRg0Mr84UhNn+et5Vh+SXKDbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkQRcfd5",
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_18TfKV0ElcRGUysptLrZTQhidYvwaeZOLzaRterLuhBqGYOy"
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhALPfCOuJQJCRzT9YRk5eiEG3oloMDrMnZGM7BNZexoJO8MfZYamwAHhC3Ulk5jBJ+1zEv2W8wHiNof/96HEKOC7hAtvhgGRAKXWZGO7GGeiul7/SYJNADDsYebg2CV55ZVOGbhd/wXnLoe5wx5uyjaJeRg0Mr84UhNn+et5Vh+SXKDbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkQRcfd5",
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhALPfCOuJQJCRzT9YRk5eiEG3oloMDrMnZGM7BNZexoJO8MfZYamwAHhC3Ulk5jBJ+1zEv2W8wHiNof/96HEKOC7hAtvhgGRAKXWZGO7GGeiul7/SYJNADDsYebg2CV55ZVOGbhd/wXnLoe5wx5uyjaJeRg0Mr84UhNn+et5Vh+SXKDbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkQRcfd5",
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhALPfCOuJQJCRzT9YRk5eiEG3oloMDrMnZGM7BNZexoJO8MfZYamwAHhC3Ulk5jBJ+1zEv2W8wHiNof/96HEKOC7hAtvhgGRAKXWZGO7GGeiul7/SYJNADDsYebg2CV55ZVOGbhd/wXnLoe5wx5uyjaJeRg0Mr84UhNn+et5Vh+SXKDbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkQRcfd5",
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
    "data": {
      "message": {
        "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
    "data": {
      "message": {
        "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
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
  "id": -576460752303422612,
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
  "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
  "id": -576460752303422612,
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
    "data": {
      "state": "tx_+QENCwH4hLhALPfCOuJQJCRzT9YRk5eiEG3oloMDrMnZGM7BNZexoJO8MfZYamwAHhC3Ulk5jBJ+1zEv2W8wHiNof/96HEKOC7hAtvhgGRAKXWZGO7GGeiul7/SYJNADDsYebg2CV55ZVOGbhd/wXnLoe5wx5uyjaJeRg0Mr84UhNn+et5Vh+SXKDbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkQRcfd5"
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
    "data": {
      "state": "tx_+QENCwH4hLhALPfCOuJQJCRzT9YRk5eiEG3oloMDrMnZGM7BNZexoJO8MfZYamwAHhC3Ulk5jBJ+1zEv2W8wHiNof/96HEKOC7hAtvhgGRAKXWZGO7GGeiul7/SYJNADDsYebg2CV55ZVOGbhd/wXnLoe5wx5uyjaJeRg0Mr84UhNn+et5Vh+SXKDbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkQRcfd5"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {
    "fee": 123456789876543
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBkQ8tov2YLh+QiXetT2b7LiMaukLJK+iINQsxjTA/+UsoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYC5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGcEiGGw8/G+JTemo=",
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
  "method": "channels.close_solo_sign",
  "params": {
    "signed_tx": "tx_+QHrCwH4QrhAmXz3rSrwxgE/6z7yaC9oHk47YCoa/pGWPR8UckJxupdhq/odibEYOAVWSaxZ5lEYXb1UyMln08CtqTblUD6CB7kBovkBnzYBoQZEPLaL9mC4fkIl3rU9m+y4jGrpCySvoiDULMY0wP/lLKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhnBIhhsPPxtOnb0j"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAmXz3rSrwxgE/6z7yaC9oHk47YCoa/pGWPR8UckJxupdhq/odibEYOAVWSaxZ5lEYXb1UyMln08CtqTblUD6CB7kBovkBnzYBoQZEPLaL9mC4fkIl3rU9m+y4jGrpCySvoiDULMY0wP/lLKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhnBIhhsPPxtOnb0j",
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAmXz3rSrwxgE/6z7yaC9oHk47YCoa/pGWPR8UckJxupdhq/odibEYOAVWSaxZ5lEYXb1UyMln08CtqTblUD6CB7kBovkBnzYBoQZEPLaL9mC4fkIl3rU9m+y4jGrpCySvoiDULMY0wP/lLKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhnBIhhsPPxtOnb0j",
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
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
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBkQ8tov2YLh+QiXetT2b7LiMaukLJK+iINQsxjTA/+UsoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/+GJGE5yoABAIYPXtZ/KAAcEw19IQ==",
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
    "signed_tx": "tx_+KcLAfhCuECJFciNvZsVetc1b7kB8mV4HoZLyHrTiRNFT1/3OtxwDUuRYBsRUx6J3MAKLYIWJ1zUZ6/moavEHHq0Dne834QJuF/4XTgBoQZEPLaL9mC4fkIl3rU9m+y4jGrpCySvoiDULMY0wP/lLKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAHFeh3Yw="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECJFciNvZsVetc1b7kB8mV4HoZLyHrTiRNFT1/3OtxwDUuRYBsRUx6J3MAKLYIWJ1zUZ6/moavEHHq0Dne834QJuF/4XTgBoQZEPLaL9mC4fkIl3rU9m+y4jGrpCySvoiDULMY0wP/lLKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAHFeh3Yw=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECJFciNvZsVetc1b7kB8mV4HoZLyHrTiRNFT1/3OtxwDUuRYBsRUx6J3MAKLYIWJ1zUZ6/moavEHHq0Dne834QJuF/4XTgBoQZEPLaL9mC4fkIl3rU9m+y4jGrpCySvoiDULMY0wP/lLKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAHFeh3Yw=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
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
    "channel_id": "ch_X42YkVrsK8uK1U1fGuJcw6AQLa3tPzohfjY4pEF28Gc9Wqi3z",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
