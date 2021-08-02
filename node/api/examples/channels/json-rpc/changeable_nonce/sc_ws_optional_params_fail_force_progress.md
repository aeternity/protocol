
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
      "fsm_id": "ba_q0WFMau+z9i+46KZBoUiGvnMtIwkERvaC13W9ZKETdm+PrTm"
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
      "fsm_id": "ba_nLD9mbeKSkq58DRp+f3ySiM2TQaRHB0vuVl9Q5fxjsMHLzCj"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBl4mAlBs=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422311,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuECiJlOaGM5zX/j2z9O4JgmQY0gRTeC4bkToFZmQAcRLqG0jOZnsg94np77gIhSNxVlb6UszfRz4MupEY0cVSJYNuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgZfDAf0+"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422311,
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_nLD9mbeKSkq58DRp+f3ySiM2TQaRHB0vuVl9Q5fxjsMHLzCj"
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "signed_tx": "tx_+MwLAfhCuECiJlOaGM5zX/j2z9O4JgmQY0gRTeC4bkToFZmQAcRLqG0jOZnsg94np77gIhSNxVlb6UszfRz4MupEY0cVSJYNuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgZfDAf0+",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422310,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAoiZTmhjOc1/49s/TuCYJkGNIEU3guG5E6BWZkAHES6htIzmZ7IPeJ6e+4CIUjcVZW+lLM30c+DLqRGNHFUiWDbhA3dMxnrU4Bp0zehMyZpDwVKeW7q2FdeQxmJf1DLavzaU/tqw3NsHORh0+DLJQCc7xiiHM63l5upWbGhsrMQxIB7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGXhP40aw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "id": -576460752303422310,
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAoiZTmhjOc1/49s/TuCYJkGNIEU3guG5E6BWZkAHES6htIzmZ7IPeJ6e+4CIUjcVZW+lLM30c+DLqRGNHFUiWDbhA3dMxnrU4Bp0zehMyZpDwVKeW7q2FdeQxmJf1DLavzaU/tqw3NsHORh0+DLJQCc7xiiHM63l5upWbGhsrMQxIB7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGXhP40aw==",
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_q0WFMau+z9i+46KZBoUiGvnMtIwkERvaC13W9ZKETdm+PrTm"
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAoiZTmhjOc1/49s/TuCYJkGNIEU3guG5E6BWZkAHES6htIzmZ7IPeJ6e+4CIUjcVZW+lLM30c+DLqRGNHFUiWDbhA3dMxnrU4Bp0zehMyZpDwVKeW7q2FdeQxmJf1DLavzaU/tqw3NsHORh0+DLJQCc7xiiHM63l5upWbGhsrMQxIB7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGXhP40aw==",
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAoiZTmhjOc1/49s/TuCYJkGNIEU3guG5E6BWZkAHES6htIzmZ7IPeJ6e+4CIUjcVZW+lLM30c+DLqRGNHFUiWDbhA3dMxnrU4Bp0zehMyZpDwVKeW7q2FdeQxmJf1DLavzaU/tqw3NsHORh0+DLJQCc7xiiHM63l5upWbGhsrMQxIB7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGXhP40aw==",
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAoiZTmhjOc1/49s/TuCYJkGNIEU3guG5E6BWZkAHES6htIzmZ7IPeJ6e+4CIUjcVZW+lLM30c+DLqRGNHFUiWDbhA3dMxnrU4Bp0zehMyZpDwVKeW7q2FdeQxmJf1DLavzaU/tqw3NsHORh0+DLJQCc7xiiHM63l5upWbGhsrMQxIB7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGXhP40aw==",
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "message": {
        "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "message": {
        "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
  "id": -576460752303422309,
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
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "id": -576460752303422309,
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "state": "tx_+QEOCwH4hLhAoiZTmhjOc1/49s/TuCYJkGNIEU3guG5E6BWZkAHES6htIzmZ7IPeJ6e+4CIUjcVZW+lLM30c+DLqRGNHFUiWDbhA3dMxnrU4Bp0zehMyZpDwVKeW7q2FdeQxmJf1DLavzaU/tqw3NsHORh0+DLJQCc7xiiHM63l5upWbGhsrMQxIB7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGXhP40aw=="
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "state": "tx_+QEOCwH4hLhAoiZTmhjOc1/49s/TuCYJkGNIEU3guG5E6BWZkAHES6htIzmZ7IPeJ6e+4CIUjcVZW+lLM30c+DLqRGNHFUiWDbhA3dMxnrU4Bp0zehMyZpDwVKeW7q2FdeQxmJf1DLavzaU/tqw3NsHORh0+DLJQCc7xiiHM63l5upWbGhsrMQxIB7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGXhP40aw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 1,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
    "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
    "deposit": 10,
    "vm_version": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnHy3HjQqT2KCXF3CH7VzO+IJSLFt25cpBcURgngTTiAAqDGHrblf5txU9BzEiN2aWf2oO3b2+8I7hB7hqLuKnpTULQd2z8=",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "vm_version": 6
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
  "id": -576460752303422308,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAtJuAAE315X3+lGYak0RmXqB8CwvrQohWYkqLv5cvxGoJgjxHH73ZulTx96Dd2NVw+8J7ALy+ybKm0hOCJ/ncIuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAKgxh625X+bcVPQcxIjdmln9qDt29vvCO4Qe4ai7ip6U1B2uMv3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "id": -576460752303422308,
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAtJuAAE315X3+lGYak0RmXqB8CwvrQohWYkqLv5cvxGoJgjxHH73ZulTx96Dd2NVw+8J7ALy+ybKm0hOCJ/ncIuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAKgxh625X+bcVPQcxIjdmln9qDt29vvCO4Qe4ai7ip6U1B2uMv3",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "vm_version": 6
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
  "id": -576460752303422307,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAtJuAAE315X3+lGYak0RmXqB8CwvrQohWYkqLv5cvxGoJgjxHH73ZulTx96Dd2NVw+8J7ALy+ybKm0hOCJ/ncIuEBeS1ai2ToFACTO9gPR+zt7Ni0BlyQwE648bN6ZWLR9DvMZPsyV3O0h9VAJVVobvfqzmWEmRQlAeioUTthYTBoJuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAKgxh625X+bcVPQcxIjdmln9qDt29vvCO4Qe4ai7ip6U1DI6gTv"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "id": -576460752303422307,
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "state": "tx_+NILAfiEuEAtJuAAE315X3+lGYak0RmXqB8CwvrQohWYkqLv5cvxGoJgjxHH73ZulTx96Dd2NVw+8J7ALy+ybKm0hOCJ/ncIuEBeS1ai2ToFACTO9gPR+zt7Ni0BlyQwE648bN6ZWLR9DvMZPsyV3O0h9VAJVVobvfqzmWEmRQlAeioUTthYTBoJuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAKgxh625X+bcVPQcxIjdmln9qDt29vvCO4Qe4ai7ip6U1DI6gTv"
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "state": "tx_+NILAfiEuEAtJuAAE315X3+lGYak0RmXqB8CwvrQohWYkqLv5cvxGoJgjxHH73ZulTx96Dd2NVw+8J7ALy+ybKm0hOCJ/ncIuEBeS1ai2ToFACTO9gPR+zt7Ni0BlyQwE648bN6ZWLR9DvMZPsyV3O0h9VAJVVobvfqzmWEmRQlAeioUTthYTBoJuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAKgxh625X+bcVPQcxIjdmln9qDt29vvCO4Qe4ai7ip6U1DI6gTv"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnHy3HjQqT2KCXF3CH7VzO+IJSLFt25cpBcURgngTTiAA6DSs0d5zT+S71XBk4fUFBsokGXLzRDXNDvyMBghIq6GatupVek=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422306,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAGk7RN9+O8sSoUNbC2dp8hLWPbwhg9YNObdtCTbuJ0JY7F+X/kanvw0cm6QRxfqyBZgbXIo5Ud2C2HNctuSt4JuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAOg0rNHec0/ku9VwZOH1BQbKJBly80Q1zQ78jAYISKuhmpWf9ic"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "id": -576460752303422306,
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAGk7RN9+O8sSoUNbC2dp8hLWPbwhg9YNObdtCTbuJ0JY7F+X/kanvw0cm6QRxfqyBZgbXIo5Ud2C2HNctuSt4JuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAOg0rNHec0/ku9VwZOH1BQbKJBly80Q1zQ78jAYISKuhmpWf9ic",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422305,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAGk7RN9+O8sSoUNbC2dp8hLWPbwhg9YNObdtCTbuJ0JY7F+X/kanvw0cm6QRxfqyBZgbXIo5Ud2C2HNctuSt4JuECvAqN9fNon3cNNsGdlRgln63yyhr8H4rnYAt1negfXv7dVCrqKotUNSfEpuicojOMW1bmyTbVPhFqHkJusa/sKuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAOg0rNHec0/ku9VwZOH1BQbKJBly80Q1zQ78jAYISKuhmpgH4cF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "id": -576460752303422305,
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "state": "tx_+NILAfiEuEAGk7RN9+O8sSoUNbC2dp8hLWPbwhg9YNObdtCTbuJ0JY7F+X/kanvw0cm6QRxfqyBZgbXIo5Ud2C2HNctuSt4JuECvAqN9fNon3cNNsGdlRgln63yyhr8H4rnYAt1negfXv7dVCrqKotUNSfEpuicojOMW1bmyTbVPhFqHkJusa/sKuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAOg0rNHec0/ku9VwZOH1BQbKJBly80Q1zQ78jAYISKuhmpgH4cF"
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "state": "tx_+NILAfiEuEAGk7RN9+O8sSoUNbC2dp8hLWPbwhg9YNObdtCTbuJ0JY7F+X/kanvw0cm6QRxfqyBZgbXIo5Ud2C2HNctuSt4JuECvAqN9fNon3cNNsGdlRgln63yyhr8H4rnYAt1negfXv7dVCrqKotUNSfEpuicojOMW1bmyTbVPhFqHkJusa/sKuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAOg0rNHec0/ku9VwZOH1BQbKJBly80Q1zQ78jAYISKuhmpgH4cF"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 4,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 4,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 3,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 3,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnHy3HjQqT2KCXF3CH7VzO+IJSLFt25cpBcURgngTTiABKCk4l91nJhEC4ml+q+KxPucmCoX/VZxs0D4U3nhCRtBQ/LJWpU=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422304,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC16X9if3EksZ02RTRNOD9IJAFldKERxT2ONxQE2FMBcuWato4tmEQX72XQKKWzxjuiAoCUifjlcPwVBsHYxJINuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gASgpOJfdZyYRAuJpfqvisT7nJgqF/1WcbNA+FN54QkbQUNaJ7Ye"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "id": -576460752303422304,
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC16X9if3EksZ02RTRNOD9IJAFldKERxT2ONxQE2FMBcuWato4tmEQX72XQKKWzxjuiAoCUifjlcPwVBsHYxJINuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gASgpOJfdZyYRAuJpfqvisT7nJgqF/1WcbNA+FN54QkbQUNaJ7Ye",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422303,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAVedi2DT3POmDcwnD/oD6KZ9ucmytofDEYIBRtE/WGX1+JievZ8pRn9jEpepnfX35Fq9vC41g0x1JpW5z4oGEBuEC16X9if3EksZ02RTRNOD9IJAFldKERxT2ONxQE2FMBcuWato4tmEQX72XQKKWzxjuiAoCUifjlcPwVBsHYxJINuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gASgpOJfdZyYRAuJpfqvisT7nJgqF/1WcbNA+FN54QkbQUOnvEGr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "id": -576460752303422303,
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "state": "tx_+NILAfiEuEAVedi2DT3POmDcwnD/oD6KZ9ucmytofDEYIBRtE/WGX1+JievZ8pRn9jEpepnfX35Fq9vC41g0x1JpW5z4oGEBuEC16X9if3EksZ02RTRNOD9IJAFldKERxT2ONxQE2FMBcuWato4tmEQX72XQKKWzxjuiAoCUifjlcPwVBsHYxJINuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gASgpOJfdZyYRAuJpfqvisT7nJgqF/1WcbNA+FN54QkbQUOnvEGr"
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "state": "tx_+NILAfiEuEAVedi2DT3POmDcwnD/oD6KZ9ucmytofDEYIBRtE/WGX1+JievZ8pRn9jEpepnfX35Fq9vC41g0x1JpW5z4oGEBuEC16X9if3EksZ02RTRNOD9IJAFldKERxT2ONxQE2FMBcuWato4tmEQX72XQKKWzxjuiAoCUifjlcPwVBsHYxJINuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gASgpOJfdZyYRAuJpfqvisT7nJgqF/1WcbNA+FN54QkbQUOnvEGr"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnHy3HjQqT2KCXF3CH7VzO+IJSLFt25cpBcURgngTTiABaBARDoHvJo/gpX+ILDnEN1yLjKMbvQJJg5pUyEHdCwbL+QMjFQ=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422302,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDtCSrxFm929AlrsoiG+HhW6rTJsyBvCNhsXSbR/5L7F/N3X/+wS5ZiiCoi2s9iO1FUYYZkBrZ+Nv3XSLG0OOsBuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAWgQEQ6B7yaP4KV/iCw5xDdci4yjG70CSYOaVMhB3QsGy/Cf1o6"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "id": -576460752303422302,
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDtCSrxFm929AlrsoiG+HhW6rTJsyBvCNhsXSbR/5L7F/N3X/+wS5ZiiCoi2s9iO1FUYYZkBrZ+Nv3XSLG0OOsBuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAWgQEQ6B7yaP4KV/iCw5xDdci4yjG70CSYOaVMhB3QsGy/Cf1o6",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422301,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBRQQaVDwLRReo838B6BDrcf9NnlffVVbmzXuCxNpu7wVw4E+SLSQlmHcWxYx8EkA8PGmgZApuh6c1DxkiYzZgMuEDtCSrxFm929AlrsoiG+HhW6rTJsyBvCNhsXSbR/5L7F/N3X/+wS5ZiiCoi2s9iO1FUYYZkBrZ+Nv3XSLG0OOsBuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAWgQEQ6B7yaP4KV/iCw5xDdci4yjG70CSYOaVMhB3QsGy+DCOIY"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "id": -576460752303422301,
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "state": "tx_+NILAfiEuEBRQQaVDwLRReo838B6BDrcf9NnlffVVbmzXuCxNpu7wVw4E+SLSQlmHcWxYx8EkA8PGmgZApuh6c1DxkiYzZgMuEDtCSrxFm929AlrsoiG+HhW6rTJsyBvCNhsXSbR/5L7F/N3X/+wS5ZiiCoi2s9iO1FUYYZkBrZ+Nv3XSLG0OOsBuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAWgQEQ6B7yaP4KV/iCw5xDdci4yjG70CSYOaVMhB3QsGy+DCOIY"
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "state": "tx_+NILAfiEuEBRQQaVDwLRReo838B6BDrcf9NnlffVVbmzXuCxNpu7wVw4E+SLSQlmHcWxYx8EkA8PGmgZApuh6c1DxkiYzZgMuEDtCSrxFm929AlrsoiG+HhW6rTJsyBvCNhsXSbR/5L7F/N3X/+wS5ZiiCoi2s9iO1FUYYZkBrZ+Nv3XSLG0OOsBuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAWgQEQ6B7yaP4KV/iCw5xDdci4yjG70CSYOaVMhB3QsGy+DCOIY"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnHy3HjQqT2KCXF3CH7VzO+IJSLFt25cpBcURgngTTiABqCRPcMH9LBOb2JW1FmRdtOTQ9FTTG5TYMdn+OwMYJQc/blhGv8=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422300,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDzpjWvgHpdBvCvy4cvgKxOD2oG62GvYj/YLseZ9WsJdXMT1DeIuyv2xrgOJ9PWmr5LEofwn7wj7Wa5UVPaoO0IuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAagkT3DB/SwTm9iVtRZkXbTk0PRU0xuU2DHZ/jsDGCUHP1cMkrk"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "id": -576460752303422300,
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDzpjWvgHpdBvCvy4cvgKxOD2oG62GvYj/YLseZ9WsJdXMT1DeIuyv2xrgOJ9PWmr5LEofwn7wj7Wa5UVPaoO0IuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAagkT3DB/SwTm9iVtRZkXbTk0PRU0xuU2DHZ/jsDGCUHP1cMkrk",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422299,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAppTpjQSVNMIr69epJe67z5S47Fk4POMRR2ge8Ev/loDWfMMyd0cKhAufGk29vCQXiH9kLZz5J9+F0mnYOb+sNuEDzpjWvgHpdBvCvy4cvgKxOD2oG62GvYj/YLseZ9WsJdXMT1DeIuyv2xrgOJ9PWmr5LEofwn7wj7Wa5UVPaoO0IuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAagkT3DB/SwTm9iVtRZkXbTk0PRU0xuU2DHZ/jsDGCUHP2VXL1B"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "id": -576460752303422299,
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "state": "tx_+NILAfiEuEAppTpjQSVNMIr69epJe67z5S47Fk4POMRR2ge8Ev/loDWfMMyd0cKhAufGk29vCQXiH9kLZz5J9+F0mnYOb+sNuEDzpjWvgHpdBvCvy4cvgKxOD2oG62GvYj/YLseZ9WsJdXMT1DeIuyv2xrgOJ9PWmr5LEofwn7wj7Wa5UVPaoO0IuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAagkT3DB/SwTm9iVtRZkXbTk0PRU0xuU2DHZ/jsDGCUHP2VXL1B"
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "state": "tx_+NILAfiEuEAppTpjQSVNMIr69epJe67z5S47Fk4POMRR2ge8Ev/loDWfMMyd0cKhAufGk29vCQXiH9kLZz5J9+F0mnYOb+sNuEDzpjWvgHpdBvCvy4cvgKxOD2oG62GvYj/YLseZ9WsJdXMT1DeIuyv2xrgOJ9PWmr5LEofwn7wj7Wa5UVPaoO0IuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAagkT3DB/SwTm9iVtRZkXbTk0PRU0xuU2DHZ/jsDGCUHP2VXL1B"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 5,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 5,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 6,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 6,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 3,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 3,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.clean_contract_calls",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.calls_pruned.reply",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "action": "calls_pruned"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1004,
        "message": "Call not found"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 3
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnHy3HjQqT2KCXF3CH7VzO+IJSLFt25cpBcURgngTTiAB6CsrbuB33ZB7rArVZ7xM8bN2LCroN3l5LRcD+uqSlkit53GN2Y=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422298,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBXXFSuE9ygd7yDdPm7cZ09Jw3RptnDGXr9uUGD4SmwHcFvBy3bB6LcG0ZIZH9d9BhaVZJaYhGiiSkbVj6pRzUHuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAegrK27gd92Qe6wK1We8TPGzdiwq6Dd5eS0XA/rqkpZIrcguGv+"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "id": -576460752303422298,
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBXXFSuE9ygd7yDdPm7cZ09Jw3RptnDGXr9uUGD4SmwHcFvBy3bB6LcG0ZIZH9d9BhaVZJaYhGiiSkbVj6pRzUHuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAegrK27gd92Qe6wK1We8TPGzdiwq6Dd5eS0XA/rqkpZIrcguGv+",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422297,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBXXFSuE9ygd7yDdPm7cZ09Jw3RptnDGXr9uUGD4SmwHcFvBy3bB6LcG0ZIZH9d9BhaVZJaYhGiiSkbVj6pRzUHuEDMAZrhZNE/WlBjMJsKRBYkN0rrdQ09mb26tXTnDxhW+o44ocPR62/zxPaio3HjIm1L18jIMgOMZ7mF3xPHwgoIuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAegrK27gd92Qe6wK1We8TPGzdiwq6Dd5eS0XA/rqkpZIrfQ6Sqa"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "id": -576460752303422297,
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "state": "tx_+NILAfiEuEBXXFSuE9ygd7yDdPm7cZ09Jw3RptnDGXr9uUGD4SmwHcFvBy3bB6LcG0ZIZH9d9BhaVZJaYhGiiSkbVj6pRzUHuEDMAZrhZNE/WlBjMJsKRBYkN0rrdQ09mb26tXTnDxhW+o44ocPR62/zxPaio3HjIm1L18jIMgOMZ7mF3xPHwgoIuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAegrK27gd92Qe6wK1We8TPGzdiwq6Dd5eS0XA/rqkpZIrfQ6Sqa"
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "state": "tx_+NILAfiEuEBXXFSuE9ygd7yDdPm7cZ09Jw3RptnDGXr9uUGD4SmwHcFvBy3bB6LcG0ZIZH9d9BhaVZJaYhGiiSkbVj6pRzUHuEDMAZrhZNE/WlBjMJsKRBYkN0rrdQ09mb26tXTnDxhW+o44ocPR62/zxPaio3HjIm1L18jIMgOMZ7mF3xPHwgoIuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAegrK27gd92Qe6wK1We8TPGzdiwq6Dd5eS0XA/rqkpZIrfQ6Sqa"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 8,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 8,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 7,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 7,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnHy3HjQqT2KCXF3CH7VzO+IJSLFt25cpBcURgngTTiACKArw6gvWbkHyj1kDlmweauYqkAtt8ym6D1MmX2+wTxti/+KBHQ=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422296,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBBfXl/xalmtiq43isUJ93W34/nt7JdonOBWEBFb7ra1u81wBwzybSBiPrE2wg6rmt+sSU805BxuPBRq5oOzzoGuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAigK8OoL1m5B8o9ZA5ZsHmrmKpALbfMpug9TJl9vsE8bYuMLiry"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "id": -576460752303422296,
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBBfXl/xalmtiq43isUJ93W34/nt7JdonOBWEBFb7ra1u81wBwzybSBiPrE2wg6rmt+sSU805BxuPBRq5oOzzoGuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAigK8OoL1m5B8o9ZA5ZsHmrmKpALbfMpug9TJl9vsE8bYuMLiry",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422295,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBBfXl/xalmtiq43isUJ93W34/nt7JdonOBWEBFb7ra1u81wBwzybSBiPrE2wg6rmt+sSU805BxuPBRq5oOzzoGuECI6bDUKshqavbohH1QNeXZ0B0AF/5mxtB8AT5tQcUGQxIM0a3T4ehDTcrM/WDWoZeQLdBEmxD1Gx3fc9hzveUKuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAigK8OoL1m5B8o9ZA5ZsHmrmKpALbfMpug9TJl9vsE8bYvaR8Sl"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "id": -576460752303422295,
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "state": "tx_+NILAfiEuEBBfXl/xalmtiq43isUJ93W34/nt7JdonOBWEBFb7ra1u81wBwzybSBiPrE2wg6rmt+sSU805BxuPBRq5oOzzoGuECI6bDUKshqavbohH1QNeXZ0B0AF/5mxtB8AT5tQcUGQxIM0a3T4ehDTcrM/WDWoZeQLdBEmxD1Gx3fc9hzveUKuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAigK8OoL1m5B8o9ZA5ZsHmrmKpALbfMpug9TJl9vsE8bYvaR8Sl"
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "state": "tx_+NILAfiEuEBBfXl/xalmtiq43isUJ93W34/nt7JdonOBWEBFb7ra1u81wBwzybSBiPrE2wg6rmt+sSU805BxuPBRq5oOzzoGuECI6bDUKshqavbohH1QNeXZ0B0AF/5mxtB8AT5tQcUGQxIM0a3T4ehDTcrM/WDWoZeQLdBEmxD1Gx3fc9hzveUKuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAigK8OoL1m5B8o9ZA5ZsHmrmKpALbfMpug9TJl9vsE8bYvaR8Sl"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnHy3HjQqT2KCXF3CH7VzO+IJSLFt25cpBcURgngTTiACaDvdd2E2VaG+E002HFNFXNih0aUVoTvVSBDpz5OMGuMwPCPfNM=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422294,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBatsXkbrTHi9aMCs5+S419juViR3IFaECIGNeeHdhxgFr3JoZ2BRnIbbdKLm0QjD8ipgBouTEMEKed6Dw7KV4JuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAmg73XdhNlWhvhNNNhxTRVzYodGlFaE71UgQ6c+TjBrjMApmgNs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "id": -576460752303422294,
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBatsXkbrTHi9aMCs5+S419juViR3IFaECIGNeeHdhxgFr3JoZ2BRnIbbdKLm0QjD8ipgBouTEMEKed6Dw7KV4JuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAmg73XdhNlWhvhNNNhxTRVzYodGlFaE71UgQ6c+TjBrjMApmgNs",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422293,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBatsXkbrTHi9aMCs5+S419juViR3IFaECIGNeeHdhxgFr3JoZ2BRnIbbdKLm0QjD8ipgBouTEMEKed6Dw7KV4JuEDLOL5hi04lmMxWlBGX14EG6gYdoqWD9G00tLe/0hBAkkahziOb5Cd/vrH/isqefEZKC/atU46aIMGOeBJMdFsHuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAmg73XdhNlWhvhNNNhxTRVzYodGlFaE71UgQ6c+TjBrjMDinJC0"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "id": -576460752303422293,
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "state": "tx_+NILAfiEuEBatsXkbrTHi9aMCs5+S419juViR3IFaECIGNeeHdhxgFr3JoZ2BRnIbbdKLm0QjD8ipgBouTEMEKed6Dw7KV4JuEDLOL5hi04lmMxWlBGX14EG6gYdoqWD9G00tLe/0hBAkkahziOb5Cd/vrH/isqefEZKC/atU46aIMGOeBJMdFsHuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAmg73XdhNlWhvhNNNhxTRVzYodGlFaE71UgQ6c+TjBrjMDinJC0"
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "state": "tx_+NILAfiEuEBatsXkbrTHi9aMCs5+S419juViR3IFaECIGNeeHdhxgFr3JoZ2BRnIbbdKLm0QjD8ipgBouTEMEKed6Dw7KV4JuEDLOL5hi04lmMxWlBGX14EG6gYdoqWD9G00tLe/0hBAkkahziOb5Cd/vrH/isqefEZKC/atU46aIMGOeBJMdFsHuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAmg73XdhNlWhvhNNNhxTRVzYodGlFaE71UgQ6c+TjBrjMDinJC0"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnHy3HjQqT2KCXF3CH7VzO+IJSLFt25cpBcURgngTTiACqDvDJM0iYilO7grS80Txf4hicibVZxVjY6HZsJzTJ5ymocMrBM=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422292,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECFwCFasKke7WA1sC/VgDYYCLzzbdRshU9NWJgls8oJS1uVwDv+pENQTp5cRZXKuN2dLhPxirp9ntZgbAXOJyoJuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecprX1vkm"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "id": -576460752303422292,
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "signed_tx": "tx_+JALAfhCuECFwCFasKke7WA1sC/VgDYYCLzzbdRshU9NWJgls8oJS1uVwDv+pENQTp5cRZXKuN2dLhPxirp9ntZgbAXOJyoJuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecprX1vkm",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422291,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBJr5TreYV9GK0vp6ZWsT5C1jErVf4a2Uo+4fjanSOOqWC+nm4qQwKewF5V3didf83XzQvWG/6GHyat49WtpCMCuECFwCFasKke7WA1sC/VgDYYCLzzbdRshU9NWJgls8oJS1uVwDv+pENQTp5cRZXKuN2dLhPxirp9ntZgbAXOJyoJuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecpppuwut"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "id": -576460752303422291,
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "state": "tx_+NILAfiEuEBJr5TreYV9GK0vp6ZWsT5C1jErVf4a2Uo+4fjanSOOqWC+nm4qQwKewF5V3didf83XzQvWG/6GHyat49WtpCMCuECFwCFasKke7WA1sC/VgDYYCLzzbdRshU9NWJgls8oJS1uVwDv+pENQTp5cRZXKuN2dLhPxirp9ntZgbAXOJyoJuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecpppuwut"
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "state": "tx_+NILAfiEuEBJr5TreYV9GK0vp6ZWsT5C1jErVf4a2Uo+4fjanSOOqWC+nm4qQwKewF5V3didf83XzQvWG/6GHyat49WtpCMCuECFwCFasKke7WA1sC/VgDYYCLzzbdRshU9NWJgls8oJS1uVwDv+pENQTp5cRZXKuN2dLhPxirp9ntZgbAXOJyoJuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecpppuwut"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 9,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 9,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 10,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 10,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
    ],
    "contracts": [
      "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaegk+nj4mXf0UdfJRgm4L5FbVvJgFx3rUgij/Xg1PD7l735AYP4T6BjO/y9fLVcbbq+euGKspkj0geiEzuawl02EAKTT5+k/+2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/X4lKCT6ePiZd/RR18lGCbgvkVtW8mAXHetSCKP9eDU8PuXvfhxgICAgICAoGM7/L18tVxtur564YqymSPSB6ITO5rCXTYQApNPn6T/gICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOg+mQXDaDbOGWcenHslGbmWzbWwhDP56xU7w5Sk/D5c72AgICAgID4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAH4SaD6ZBcNoNs4ZZx6ceyUZuZbNtbCEM/nrFTvDlKT8PlzveegN8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXSFxAoBAArj4qDemVZJFGKoVINblPxU/hE+HqQP9b6ZjgvOmxY6jZAfTsDA+Qap+QamoLHf8VwmQd/h60Cq2gFj327dttU0dUjlsD+6exE6jEU6+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+HSgSBEeVwu8cW7q/gUKtI9BT7SQXY1Hq9ywIfX9gYKO8UX4UaAVaiNPbxb1nROfE0C66bQnbZgclArLhJIVIS1S0xfBX6DDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd4CAgICAgICAgICAgICAgPkDtqCFzPTTiFBffe8P/CRAwQy7JB9ShQRel6dQYB7SuYQmlvkDkoCgHdyouV7WvK8NcjTQvraEYvxQpM3YKd3dXGkU6L2B2IyAgICAgICAgICAgICAgLkDX/kDXCgBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAK+Gagsd/xXCZB3+HrQKraAWPfbt221TR1SOWwP7p7ETqMRTr4Q6EAp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXSghcz004hQX33vD/wkQMEMuyQfUoUEXpenUGAe0rmEJpb45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDAMps2tw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
    ],
    "contracts": [
      "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaegk+nj4mXf0UdfJRgm4L5FbVvJgFx3rUgij/Xg1PD7l735AYP4T6BjO/y9fLVcbbq+euGKspkj0geiEzuawl02EAKTT5+k/+2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/X4lKCT6ePiZd/RR18lGCbgvkVtW8mAXHetSCKP9eDU8PuXvfhxgICAgICAoGM7/L18tVxtur564YqymSPSB6ITO5rCXTYQApNPn6T/gICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOg+mQXDaDbOGWcenHslGbmWzbWwhDP56xU7w5Sk/D5c72AgICAgID4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAH4SaD6ZBcNoNs4ZZx6ceyUZuZbNtbCEM/nrFTvDlKT8PlzveegN8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXSFxAoBAArj4qDemVZJFGKoVINblPxU/hE+HqQP9b6ZjgvOmxY6jZAfTsDA+Qap+QamoLHf8VwmQd/h60Cq2gFj327dttU0dUjlsD+6exE6jEU6+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+HSgSBEeVwu8cW7q/gUKtI9BT7SQXY1Hq9ywIfX9gYKO8UX4UaAVaiNPbxb1nROfE0C66bQnbZgclArLhJIVIS1S0xfBX6DDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd4CAgICAgICAgICAgICAgPkDtqCFzPTTiFBffe8P/CRAwQy7JB9ShQRel6dQYB7SuYQmlvkDkoCgHdyouV7WvK8NcjTQvraEYvxQpM3YKd3dXGkU6L2B2IyAgICAgICAgICAgICAgLkDX/kDXCgBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAK+Gagsd/xXCZB3+HrQKraAWPfbt221TR1SOWwP7p7ETqMRTr4Q6EAp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXSghcz004hQX33vD/wkQMEMuyQfUoUEXpenUGAe0rmEJpb45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDAMps2tw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "id": -576460752303422290,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
  "id": -576460752303422290,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_+QL7ggJuAbkC9PkC8T8B+QLsuLn4t0ABuECnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdO8fPBmaSVPqmgiBusf3LOGDDJVgVOLC2Epltiext0tvuHH4bykCoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQoKoQWnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdAGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwLi5+LdAAbhAp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXTbNpXWijWsOX49kkYUP/zdszoKl6Vbyhsx2OfNGEmwErhx+G8pAqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKEICKEFp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQBggHOoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMC4ufi3QAG4QKfKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0lX7zIei0DGZIYw95F0AjiQn31YgQLzQWxawu/lJrdBK4cfhvKQKhAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChBwehBafKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0AYIBfKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFgDAuLn4t0ABuECnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdFUTlMupXff6BHiZkecmAU9bxHaOfhOFn4Tz6N0u2IMQuHH4bykCoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQkJoQWnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdAGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwOa/sTo=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBJr5TreYV9GK0vp6ZWsT5C1jErVf4a2Uo+4fjanSOOqWC+nm4qQwKewF5V3didf83XzQvWG/6GHyat49WtpCMCuECFwCFasKke7WA1sC/VgDYYCLzzbdRshU9NWJgls8oJS1uVwDv+pENQTp5cRZXKuN2dLhPxirp9ntZgbAXOJyoJuEj4RjkCoQZx8tx40Kk9iglxdwh+1czviCUixbduXKQXFEYJ4E04gAqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecpppuwut",
    "trees": "ss_+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGip8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABoqfKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0EAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoafKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0EAC5A4j5A4VAAaCnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdLkDX/kDXCgBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXTvHzwZmklT6poIgbrH9yzhgwyVYFTiwthKZbYnsbdLb7hx+G8pAqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKEKCqEFp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNqulAAaCnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdIXECgEACrDvQAGgkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAGw70ABoGSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl/1h0sosw=="
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.force_progress",
  "params": {
    "abi_version": 1,
    "amount": 10,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "gas_price": 1000001001,
    "nonce": 1234567
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.force_progress_tx",
  "params": {
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
    "data": {
      "signed_tx": "tx_+Qi+CwHAuQi4+Qi1ggIJAaEGcfLceNCpPYoJcXcIftXM74glIsW3blykFxRGCeBNOIChAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+BuNT40gsB+IS4QEmvlOt5hX0YrS+nplaxPkLWMStV/hrZSj7h+NqdI46pYL6ebipDAp7AXlXd2J1/zdfNC9Yb/oYfJq3j1a2kIwK4QIXAIVqwqR7tYDWwL9WANhgIvPNt1GyFT01YmCWzyglLW5XAO/6kQ1BOnlxFlcq43Z0uE/GKun2e1mBsBc4nKgm4SPhGOQKhBnHy3HjQqT2KCXF3CH7VzO+IJSLFt25cpBcURgngTTiACqDvDJM0iYilO7grS80Txf4hicibVZxVjY6HZsJzTJ5ymgu4uPi2ggI+AaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GhBafKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0AQqDD0JAhDuazem4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCgOGxwOhBLTJpzo/mgqNPcpJ/r9iG/gbcY7zBP0iHiNgu5Bqv5Bqg+ALkFGvkFF4ICbQG5BRD5BQ0/AfkFCLjp+OdAAaKnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdBABuMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4afhnQAGip8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQQALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF6blQAGhp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQQALkDiPkDhUABoKfKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0uQNf+QNcKAGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+BgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAq4yfjHggJuAbjB+L8/Afi7uLn4t0ABuECnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdO8fPBmaSVPqmgiBusf3LOGDDJVgVOLC2Epltiext0tvuHH4bykCoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQoKoQWnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdAGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwIrJggJvAYTDPwHAismCAnABhMM/AcCKyYICcQGEwz8BwLib+JmCAnIBuJP4kT8B+I2q6UABoKfKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0hcQKAQAKsO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/UAhwHB33cBB7CDEtaHhPLtUw==",
      "updates": [
        {
          "abi_version": 1,
          "amount": 10,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1000001001,
          "op": "OffChainCallContract"
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
  "method": "channels.force_progress_tx",
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
    "channel_id": "ch_sBfdTQygN3Z7QCVh3gVzbpdWuLCS11cUQyuMNj2i3bDQbWmfs",
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
      "fsm_id": "ba_lGiJDzZ56yKsfBssyvU9rz8ST0s7fb6JoDnqg+48hYUq0NSb"
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
      "fsm_id": "ba_GWXcA8WYMXX6DIOgeeN9HN6F0YdzeFnetBolsYyWLKVbkjKt"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhALIe8QAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaBmODv8wk=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422289,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEDxrz0I8+QhMuWE7/6ktyM6V9D4iLbZeHsLTKf41WASYxu6U0oIoiaVewAV20fyfX6rs6YnDwM9/DfgEaSCmToLuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgZgoGzSg"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422289,
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_GWXcA8WYMXX6DIOgeeN9HN6F0YdzeFnetBolsYyWLKVbkjKt"
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEDxrz0I8+QhMuWE7/6ktyM6V9D4iLbZeHsLTKf41WASYxu6U0oIoiaVewAV20fyfX6rs6YnDwM9/DfgEaSCmToLuIT4gjIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQCyHvEADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGgZgoGzSg",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422288,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhA7smR0xUf5kJpTTUxuQ3j41J8VrqMwERnZtOoMq9aHc7/2rN/51pxvKJubuwcUjaeTCfNfbewLLwFW8sUEYgoAbhA8a89CPPkITLlhO/+pLcjOlfQ+Ii22Xh7C0yn+NVgEmMbulNKCKImlXsAFdtH8n1+q7OmJw8DPfw34BGkgpk6C7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGYMCyNQw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "id": -576460752303422288,
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhA7smR0xUf5kJpTTUxuQ3j41J8VrqMwERnZtOoMq9aHc7/2rN/51pxvKJubuwcUjaeTCfNfbewLLwFW8sUEYgoAbhA8a89CPPkITLlhO/+pLcjOlfQ+Ii22Xh7C0yn+NVgEmMbulNKCKImlXsAFdtH8n1+q7OmJw8DPfw34BGkgpk6C7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGYMCyNQw==",
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_lGiJDzZ56yKsfBssyvU9rz8ST0s7fb6JoDnqg+48hYUq0NSb"
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhA7smR0xUf5kJpTTUxuQ3j41J8VrqMwERnZtOoMq9aHc7/2rN/51pxvKJubuwcUjaeTCfNfbewLLwFW8sUEYgoAbhA8a89CPPkITLlhO/+pLcjOlfQ+Ii22Xh7C0yn+NVgEmMbulNKCKImlXsAFdtH8n1+q7OmJw8DPfw34BGkgpk6C7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGYMCyNQw==",
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhA7smR0xUf5kJpTTUxuQ3j41J8VrqMwERnZtOoMq9aHc7/2rN/51pxvKJubuwcUjaeTCfNfbewLLwFW8sUEYgoAbhA8a89CPPkITLlhO/+pLcjOlfQ+Ii22Xh7C0yn+NVgEmMbulNKCKImlXsAFdtH8n1+q7OmJw8DPfw34BGkgpk6C7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGYMCyNQw==",
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhA7smR0xUf5kJpTTUxuQ3j41J8VrqMwERnZtOoMq9aHc7/2rN/51pxvKJubuwcUjaeTCfNfbewLLwFW8sUEYgoAbhA8a89CPPkITLlhO/+pLcjOlfQ+Ii22Xh7C0yn+NVgEmMbulNKCKImlXsAFdtH8n1+q7OmJw8DPfw34BGkgpk6C7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGYMCyNQw==",
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "message": {
        "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "message": {
        "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
  "id": -576460752303422287,
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
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "id": -576460752303422287,
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "state": "tx_+QEOCwH4hLhA7smR0xUf5kJpTTUxuQ3j41J8VrqMwERnZtOoMq9aHc7/2rN/51pxvKJubuwcUjaeTCfNfbewLLwFW8sUEYgoAbhA8a89CPPkITLlhO/+pLcjOlfQ+Ii22Xh7C0yn+NVgEmMbulNKCKImlXsAFdtH8n1+q7OmJw8DPfw34BGkgpk6C7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGYMCyNQw=="
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "state": "tx_+QEOCwH4hLhA7smR0xUf5kJpTTUxuQ3j41J8VrqMwERnZtOoMq9aHc7/2rN/51pxvKJubuwcUjaeTCfNfbewLLwFW8sUEYgoAbhA8a89CPPkITLlhO/+pLcjOlfQ+Ii22Xh7C0yn+NVgEmMbulNKCKImlXsAFdtH8n1+q7OmJw8DPfw34BGkgpk6C7iE+IIyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAsh7xAAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RoGYMCyNQw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 1,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
    "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
    "deposit": 10,
    "vm_version": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvERpffOpq89VgE3rMGd8A3M734m7glVHnBwxJ4LjBIlAqDGHrblf5txU9BzEiN2aWf2oO3b2+8I7hB7hqLuKnpTUGv/FlI=",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "vm_version": 6
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
  "id": -576460752303422286,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEABUXmNQACFypHl7kWhkW0stQn6BlvFdcadR8zBpqcmt7RqypNg9H4YWfPgP3u2/67LoUt+lX6DRLHRlBQJqpYBuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQKgxh625X+bcVPQcxIjdmln9qDt29vvCO4Qe4ai7ip6U1ChvkYq"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "id": -576460752303422286,
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "signed_tx": "tx_+JALAfhCuEABUXmNQACFypHl7kWhkW0stQn6BlvFdcadR8zBpqcmt7RqypNg9H4YWfPgP3u2/67LoUt+lX6DRLHRlBQJqpYBuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQKgxh625X+bcVPQcxIjdmln9qDt29vvCO4Qe4ai7ip6U1ChvkYq",
      "updates": [
        {
          "abi_version": 1,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDiIx1s38k5Ft5Ms6mFe/Zc9A/CVvShSYs/fnyYDBmTRAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABWctrmZ",
          "code": "cb_+QW5RgOgmeYbHHeqvRg3YvbB0Okz4GJjGybIywoOkveyANNIS/X5BEj4yqBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUt4NnZXQBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD466CzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCToR0aWNrAbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD///////////////////////////////////////////5Aoyg4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0SEaW5pdAC4wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACg//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALkBoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wADGmvPo=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "vm_version": 6
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
  "id": -576460752303422285,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEABUXmNQACFypHl7kWhkW0stQn6BlvFdcadR8zBpqcmt7RqypNg9H4YWfPgP3u2/67LoUt+lX6DRLHRlBQJqpYBuECIm3jkSe6jLkZQ00gF7Eoe+dv5+DPP8kD5CXl0o8cfbi9zXuOJt7k36xRXug4hgcmOBUVThnTmpKC7839kqjMNuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQKgxh625X+bcVPQcxIjdmln9qDt29vvCO4Qe4ai7ip6U1BdGx7y"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "id": -576460752303422285,
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "state": "tx_+NILAfiEuEABUXmNQACFypHl7kWhkW0stQn6BlvFdcadR8zBpqcmt7RqypNg9H4YWfPgP3u2/67LoUt+lX6DRLHRlBQJqpYBuECIm3jkSe6jLkZQ00gF7Eoe+dv5+DPP8kD5CXl0o8cfbi9zXuOJt7k36xRXug4hgcmOBUVThnTmpKC7839kqjMNuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQKgxh625X+bcVPQcxIjdmln9qDt29vvCO4Qe4ai7ip6U1BdGx7y"
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "state": "tx_+NILAfiEuEABUXmNQACFypHl7kWhkW0stQn6BlvFdcadR8zBpqcmt7RqypNg9H4YWfPgP3u2/67LoUt+lX6DRLHRlBQJqpYBuECIm3jkSe6jLkZQ00gF7Eoe+dv5+DPP8kD5CXl0o8cfbi9zXuOJt7k36xRXug4hgcmOBUVThnTmpKC7839kqjMNuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQKgxh625X+bcVPQcxIjdmln9qDt29vvCO4Qe4ai7ip6U1BdGx7y"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvERpffOpq89VgE3rMGd8A3M734m7glVHnBwxJ4LjBIlA6DSs0d5zT+S71XBk4fUFBsokGXLzRDXNDvyMBghIq6GavcgnRk=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422284,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAoJt/33yXYAUAvq03V50//1ScjC0+EnCy2TQqFxBmcqURRHDKQjAvc4McjpbfO+h4ltsHQaKHzW8krjc/kb8QEuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQOg0rNHec0/ku9VwZOH1BQbKJBly80Q1zQ78jAYISKuhmoq2RXz"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "id": -576460752303422284,
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAoJt/33yXYAUAvq03V50//1ScjC0+EnCy2TQqFxBmcqURRHDKQjAvc4McjpbfO+h4ltsHQaKHzW8krjc/kb8QEuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQOg0rNHec0/ku9VwZOH1BQbKJBly80Q1zQ78jAYISKuhmoq2RXz",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422283,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAoJt/33yXYAUAvq03V50//1ScjC0+EnCy2TQqFxBmcqURRHDKQjAvc4McjpbfO+h4ltsHQaKHzW8krjc/kb8QEuEBRBOsthNQ7CZx1bDEtICbCNgavLS3YcM3H9OjwSx8/0koWqtMVIREQ0H4vuhI9Evx/rmideTsQGnM6n8T5mOABuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQOg0rNHec0/ku9VwZOH1BQbKJBly80Q1zQ78jAYISKuhmrmFCi6"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "id": -576460752303422283,
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "state": "tx_+NILAfiEuEAoJt/33yXYAUAvq03V50//1ScjC0+EnCy2TQqFxBmcqURRHDKQjAvc4McjpbfO+h4ltsHQaKHzW8krjc/kb8QEuEBRBOsthNQ7CZx1bDEtICbCNgavLS3YcM3H9OjwSx8/0koWqtMVIREQ0H4vuhI9Evx/rmideTsQGnM6n8T5mOABuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQOg0rNHec0/ku9VwZOH1BQbKJBly80Q1zQ78jAYISKuhmrmFCi6"
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "state": "tx_+NILAfiEuEAoJt/33yXYAUAvq03V50//1ScjC0+EnCy2TQqFxBmcqURRHDKQjAvc4McjpbfO+h4ltsHQaKHzW8krjc/kb8QEuEBRBOsthNQ7CZx1bDEtICbCNgavLS3YcM3H9OjwSx8/0koWqtMVIREQ0H4vuhI9Evx/rmideTsQGnM6n8T5mOABuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQOg0rNHec0/ku9VwZOH1BQbKJBly80Q1zQ78jAYISKuhmrmFCi6"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 4,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 4,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 3,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 3,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvERpffOpq89VgE3rMGd8A3M734m7glVHnBwxJ4LjBIlBKCk4l91nJhEC4ml+q+KxPucmCoX/VZxs0D4U3nhCRtBQz5Fk6g=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422282,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDTkr8+OVGRlWNrYKMuvVJFF0haKYorQ1RvMhVShzUlSU3qroyzGuIi97Jxd+7HnDKsiF0wT3szRCLTv9dBq60GuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQSgpOJfdZyYRAuJpfqvisT7nJgqF/1WcbNA+FN54QkbQUNjMjHN"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "id": -576460752303422282,
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDTkr8+OVGRlWNrYKMuvVJFF0haKYorQ1RvMhVShzUlSU3qroyzGuIi97Jxd+7HnDKsiF0wT3szRCLTv9dBq60GuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQSgpOJfdZyYRAuJpfqvisT7nJgqF/1WcbNA+FN54QkbQUNjMjHN",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422281,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECKxoDzz5CD1wEpVXTDRfSGs4W6CewJ3BFF7HBs4Q1scwhEr5oy5nx4s6RJ40NsMJDqgFGiw3wbtjRG4Sso854PuEDTkr8+OVGRlWNrYKMuvVJFF0haKYorQ1RvMhVShzUlSU3qroyzGuIi97Jxd+7HnDKsiF0wT3szRCLTv9dBq60GuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQSgpOJfdZyYRAuJpfqvisT7nJgqF/1WcbNA+FN54QkbQUOtQLc6"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "id": -576460752303422281,
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "state": "tx_+NILAfiEuECKxoDzz5CD1wEpVXTDRfSGs4W6CewJ3BFF7HBs4Q1scwhEr5oy5nx4s6RJ40NsMJDqgFGiw3wbtjRG4Sso854PuEDTkr8+OVGRlWNrYKMuvVJFF0haKYorQ1RvMhVShzUlSU3qroyzGuIi97Jxd+7HnDKsiF0wT3szRCLTv9dBq60GuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQSgpOJfdZyYRAuJpfqvisT7nJgqF/1WcbNA+FN54QkbQUOtQLc6"
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "state": "tx_+NILAfiEuECKxoDzz5CD1wEpVXTDRfSGs4W6CewJ3BFF7HBs4Q1scwhEr5oy5nx4s6RJ40NsMJDqgFGiw3wbtjRG4Sso854PuEDTkr8+OVGRlWNrYKMuvVJFF0haKYorQ1RvMhVShzUlSU3qroyzGuIi97Jxd+7HnDKsiF0wT3szRCLTv9dBq60GuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQSgpOJfdZyYRAuJpfqvisT7nJgqF/1WcbNA+FN54QkbQUOtQLc6"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvERpffOpq89VgE3rMGd8A3M734m7glVHnBwxJ4LjBIlBaBARDoHvJo/gpX+ILDnEN1yLjKMbvQJJg5pUyEHdCwbLx2VURg=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422280,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDTvqk7SwUlftce4fFvBVKBWmGUHB2g1hJcZUidrhpv8eTjyJ4W1+qV0FXti9+Q8ijjxB+ZEJfZJyMMlrhadYgHuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQWgQEQ6B7yaP4KV/iCw5xDdci4yjG70CSYOaVMhB3QsGy+dub7+"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "id": -576460752303422280,
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDTvqk7SwUlftce4fFvBVKBWmGUHB2g1hJcZUidrhpv8eTjyJ4W1+qV0FXti9+Q8ijjxB+ZEJfZJyMMlrhadYgHuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQWgQEQ6B7yaP4KV/iCw5xDdci4yjG70CSYOaVMhB3QsGy+dub7+",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422279,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBrYSAK8/8/V8WuuK3trnWETDCK3UcC0gagFuCYePrQmtNdGB+Nod4KrCUuHNQmOn1wrxnvWU8+7fVf3daQhpkAuEDTvqk7SwUlftce4fFvBVKBWmGUHB2g1hJcZUidrhpv8eTjyJ4W1+qV0FXti9+Q8ijjxB+ZEJfZJyMMlrhadYgHuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQWgQEQ6B7yaP4KV/iCw5xDdci4yjG70CSYOaVMhB3QsGy8C+nZc"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "id": -576460752303422279,
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "state": "tx_+NILAfiEuEBrYSAK8/8/V8WuuK3trnWETDCK3UcC0gagFuCYePrQmtNdGB+Nod4KrCUuHNQmOn1wrxnvWU8+7fVf3daQhpkAuEDTvqk7SwUlftce4fFvBVKBWmGUHB2g1hJcZUidrhpv8eTjyJ4W1+qV0FXti9+Q8ijjxB+ZEJfZJyMMlrhadYgHuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQWgQEQ6B7yaP4KV/iCw5xDdci4yjG70CSYOaVMhB3QsGy8C+nZc"
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "state": "tx_+NILAfiEuEBrYSAK8/8/V8WuuK3trnWETDCK3UcC0gagFuCYePrQmtNdGB+Nod4KrCUuHNQmOn1wrxnvWU8+7fVf3daQhpkAuEDTvqk7SwUlftce4fFvBVKBWmGUHB2g1hJcZUidrhpv8eTjyJ4W1+qV0FXti9+Q8ijjxB+ZEJfZJyMMlrhadYgHuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQWgQEQ6B7yaP4KV/iCw5xDdci4yjG70CSYOaVMhB3QsGy8C+nZc"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvERpffOpq89VgE3rMGd8A3M734m7glVHnBwxJ4LjBIlBqCRPcMH9LBOb2JW1FmRdtOTQ9FTTG5TYMdn+OwMYJQc/W7vFd4=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422278,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDTYg7Ut5S2c8iW84sl+ys/kIhlfzQioNXyDcDsjn1xOJEOvlWGzW5+tBQGmC5L5pF1itk3iBurr+OKI3Vl75IOuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQagkT3DB/SwTm9iVtRZkXbTk0PRU0xuU2DHZ/jsDGCUHP1AyU6R"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "id": -576460752303422278,
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDTYg7Ut5S2c8iW84sl+ys/kIhlfzQioNXyDcDsjn1xOJEOvlWGzW5+tBQGmC5L5pF1itk3iBurr+OKI3Vl75IOuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQagkT3DB/SwTm9iVtRZkXbTk0PRU0xuU2DHZ/jsDGCUHP1AyU6R",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422277,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA+M6U6IlSkIQfEso5xsRED9NL3lpO2Wx9Bf8pZJ8+kZq8IeElWc4YWEs3h4aVdJV4X6usGBuZffODqmA7FlG0FuEDTYg7Ut5S2c8iW84sl+ys/kIhlfzQioNXyDcDsjn1xOJEOvlWGzW5+tBQGmC5L5pF1itk3iBurr+OKI3Vl75IOuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQagkT3DB/SwTm9iVtRZkXbTk0PRU0xuU2DHZ/jsDGCUHP36C9l6"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "id": -576460752303422277,
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "state": "tx_+NILAfiEuEA+M6U6IlSkIQfEso5xsRED9NL3lpO2Wx9Bf8pZJ8+kZq8IeElWc4YWEs3h4aVdJV4X6usGBuZffODqmA7FlG0FuEDTYg7Ut5S2c8iW84sl+ys/kIhlfzQioNXyDcDsjn1xOJEOvlWGzW5+tBQGmC5L5pF1itk3iBurr+OKI3Vl75IOuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQagkT3DB/SwTm9iVtRZkXbTk0PRU0xuU2DHZ/jsDGCUHP36C9l6"
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "state": "tx_+NILAfiEuEA+M6U6IlSkIQfEso5xsRED9NL3lpO2Wx9Bf8pZJ8+kZq8IeElWc4YWEs3h4aVdJV4X6usGBuZffODqmA7FlG0FuEDTYg7Ut5S2c8iW84sl+ys/kIhlfzQioNXyDcDsjn1xOJEOvlWGzW5+tBQGmC5L5pF1itk3iBurr+OKI3Vl75IOuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQagkT3DB/SwTm9iVtRZkXbTk0PRU0xuU2DHZ/jsDGCUHP36C9l6"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 5
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 5,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 5
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 5
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 5,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 5,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 6
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 6,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 6
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 6
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 6,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 6,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 3,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ABCDEFG",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ABCDEFG",
        "round": 3
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "caller_nonce": 3,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 3,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABX4y1tk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.clean_contract_calls",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.calls_pruned.reply",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "action": "calls_pruned"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 3
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1004,
        "message": "Call not found"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 3
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvERpffOpq89VgE3rMGd8A3M734m7glVHnBwxJ4LjBIlB6CsrbuB33ZB7rArVZ7xM8bN2LCroN3l5LRcD+uqSlkit1lGZvs=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422276,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED+Y1L+EnbM+Ap2kMvddGxwZR3rV1kGgGJrH7vBD8CIxuy7gc9+mJdNYNzbPiBu3J7slt5VDBKAtDzaGPtRLNEMuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQegrK27gd92Qe6wK1We8TPGzdiwq6Dd5eS0XA/rqkpZIreTehvk"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "id": -576460752303422276,
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "signed_tx": "tx_+JALAfhCuED+Y1L+EnbM+Ap2kMvddGxwZR3rV1kGgGJrH7vBD8CIxuy7gc9+mJdNYNzbPiBu3J7slt5VDBKAtDzaGPtRLNEMuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQegrK27gd92Qe6wK1We8TPGzdiwq6Dd5eS0XA/rqkpZIreTehvk",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422275,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAuV5w43tvHBZV6M7GFKxlwuSAUNNHWbH28M1yhNsrDEFWiqoQzf49LqJJHo4PkhKJkUWYuwT69+N9ylyqukGAHuED+Y1L+EnbM+Ap2kMvddGxwZR3rV1kGgGJrH7vBD8CIxuy7gc9+mJdNYNzbPiBu3J7slt5VDBKAtDzaGPtRLNEMuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQegrK27gd92Qe6wK1We8TPGzdiwq6Dd5eS0XA/rqkpZIrdD22Ys"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "id": -576460752303422275,
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "state": "tx_+NILAfiEuEAuV5w43tvHBZV6M7GFKxlwuSAUNNHWbH28M1yhNsrDEFWiqoQzf49LqJJHo4PkhKJkUWYuwT69+N9ylyqukGAHuED+Y1L+EnbM+Ap2kMvddGxwZR3rV1kGgGJrH7vBD8CIxuy7gc9+mJdNYNzbPiBu3J7slt5VDBKAtDzaGPtRLNEMuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQegrK27gd92Qe6wK1We8TPGzdiwq6Dd5eS0XA/rqkpZIrdD22Ys"
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "state": "tx_+NILAfiEuEAuV5w43tvHBZV6M7GFKxlwuSAUNNHWbH28M1yhNsrDEFWiqoQzf49LqJJHo4PkhKJkUWYuwT69+N9ylyqukGAHuED+Y1L+EnbM+Ap2kMvddGxwZR3rV1kGgGJrH7vBD8CIxuy7gc9+mJdNYNzbPiBu3J7slt5VDBKAtDzaGPtRLNEMuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQegrK27gd92Qe6wK1We8TPGzdiwq6Dd5eS0XA/rqkpZIrdD22Ys"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 8,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 8,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 7
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 7,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 7
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 7,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 7,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABbSGxoV"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvERpffOpq89VgE3rMGd8A3M734m7glVHnBwxJ4LjBIlCKArw6gvWbkHyj1kDlmweauYqkAtt8ym6D1MmX2+wTxti6WJBtk=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422274,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDh5Chdpa7222evQcjtXT6Js0nz1pHpB/OH5VacNZpqY+9iTIo7HB37oFE6E53j9amp5DmKA0tm2dR6r/j9k5oDuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQigK8OoL1m5B8o9ZA5ZsHmrmKpALbfMpug9TJl9vsE8bYtT04SY"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "id": -576460752303422274,
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDh5Chdpa7222evQcjtXT6Js0nz1pHpB/OH5VacNZpqY+9iTIo7HB37oFE6E53j9amp5DmKA0tm2dR6r/j9k5oDuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQigK8OoL1m5B8o9ZA5ZsHmrmKpALbfMpug9TJl9vsE8bYtT04SY",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422273,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECSyq6WyZRJDAl3Oeqp1KJdC6d3mv8VTqdrpc2YrnNP1KoeF8xJydaMHEDB0fODtsnyVe+A6NXGgtRVkKDCdxcCuEDh5Chdpa7222evQcjtXT6Js0nz1pHpB/OH5VacNZpqY+9iTIo7HB37oFE6E53j9amp5DmKA0tm2dR6r/j9k5oDuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQigK8OoL1m5B8o9ZA5ZsHmrmKpALbfMpug9TJl9vsE8bYuIUT+S"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "id": -576460752303422273,
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "state": "tx_+NILAfiEuECSyq6WyZRJDAl3Oeqp1KJdC6d3mv8VTqdrpc2YrnNP1KoeF8xJydaMHEDB0fODtsnyVe+A6NXGgtRVkKDCdxcCuEDh5Chdpa7222evQcjtXT6Js0nz1pHpB/OH5VacNZpqY+9iTIo7HB37oFE6E53j9amp5DmKA0tm2dR6r/j9k5oDuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQigK8OoL1m5B8o9ZA5ZsHmrmKpALbfMpug9TJl9vsE8bYuIUT+S"
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "state": "tx_+NILAfiEuECSyq6WyZRJDAl3Oeqp1KJdC6d3mv8VTqdrpc2YrnNP1KoeF8xJydaMHEDB0fODtsnyVe+A6NXGgtRVkKDCdxcCuEDh5Chdpa7222evQcjtXT6Js0nz1pHpB/OH5VacNZpqY+9iTIo7HB37oFE6E53j9amp5DmKA0tm2dR6r/j9k5oDuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQigK8OoL1m5B8o9ZA5ZsHmrmKpALbfMpug9TJl9vsE8bYuIUT+S"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvERpffOpq89VgE3rMGd8A3M734m7glVHnBwxJ4LjBIlCaDvdd2E2VaG+E002HFNFXNih0aUVoTvVSBDpz5OMGuMwOfiJ5I=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422272,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBe7Sl9m2/n7SqcmcGr3uQ/1s2UBqelboHNOrajv43J2QfnD5cGFaiXclw3G5p2+pXPgZGz0NA6oyeYdWqAxSwGuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQmg73XdhNlWhvhNNNhxTRVzYodGlFaE71UgQ6c+TjBrjMDtEeLn"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "id": -576460752303422272,
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBe7Sl9m2/n7SqcmcGr3uQ/1s2UBqelboHNOrajv43J2QfnD5cGFaiXclw3G5p2+pXPgZGz0NA6oyeYdWqAxSwGuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQmg73XdhNlWhvhNNNhxTRVzYodGlFaE71UgQ6c+TjBrjMDtEeLn",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422271,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBe7Sl9m2/n7SqcmcGr3uQ/1s2UBqelboHNOrajv43J2QfnD5cGFaiXclw3G5p2+pXPgZGz0NA6oyeYdWqAxSwGuEDJUAIaOhdH7sC7079Hb667YMJRYJ/FSD19+3hp6+ZmJ2jAol74bOM+n62CKzeSKCSNTexUcY+LGdUROn++6eILuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQmg73XdhNlWhvhNNNhxTRVzYodGlFaE71UgQ6c+TjBrjMAXwr13"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "id": -576460752303422271,
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "state": "tx_+NILAfiEuEBe7Sl9m2/n7SqcmcGr3uQ/1s2UBqelboHNOrajv43J2QfnD5cGFaiXclw3G5p2+pXPgZGz0NA6oyeYdWqAxSwGuEDJUAIaOhdH7sC7079Hb667YMJRYJ/FSD19+3hp6+ZmJ2jAol74bOM+n62CKzeSKCSNTexUcY+LGdUROn++6eILuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQmg73XdhNlWhvhNNNhxTRVzYodGlFaE71UgQ6c+TjBrjMAXwr13"
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "state": "tx_+NILAfiEuEBe7Sl9m2/n7SqcmcGr3uQ/1s2UBqelboHNOrajv43J2QfnD5cGFaiXclw3G5p2+pXPgZGz0NA6oyeYdWqAxSwGuEDJUAIaOhdH7sC7079Hb667YMJRYJ/FSD19+3hp6+ZmJ2jAol74bOM+n62CKzeSKCSNTexUcY+LGdUROn++6eILuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQmg73XdhNlWhvhNNNhxTRVzYodGlFaE71UgQ6c+TjBrjMAXwr13"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": "1",
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": "1",
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 1,
        "amount": 0,
        "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvERpffOpq89VgE3rMGd8A3M734m7glVHnBwxJ4LjBIlCqDvDJM0iYilO7grS80Txf4hicibVZxVjY6HZsJzTJ5ymq490E4=",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422270,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED115i81achz31KiWWvXqoI7104LtSxbKwDTK49A01xkfD30gLtanjhqutaaeHXXWS4rH7Ywd5vFgasfAlUcFsLuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecpr60KtP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "id": -576460752303422270,
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "signed_tx": "tx_+JALAfhCuED115i81achz31KiWWvXqoI7104LtSxbKwDTK49A01xkfD30gLtanjhqutaaeHXXWS4rH7Ywd5vFgasfAlUcFsLuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecpr60KtP",
      "updates": [
        {
          "abi_version": 1,
          "amount": 0,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBJ7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYPjVAQ==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303422269,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAvY02FVzTrB1kUewRC3v3gxOP9eTDl2nULqWaqTKaSaXrG68eU0INZBzsqyi1KJt5W438CjFITFDHIHfKxtmkDuED115i81achz31KiWWvXqoI7104LtSxbKwDTK49A01xkfD30gLtanjhqutaaeHXXWS4rH7Ywd5vFgasfAlUcFsLuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecppi01CU"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "id": -576460752303422269,
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "state": "tx_+NILAfiEuEAvY02FVzTrB1kUewRC3v3gxOP9eTDl2nULqWaqTKaSaXrG68eU0INZBzsqyi1KJt5W438CjFITFDHIHfKxtmkDuED115i81achz31KiWWvXqoI7104LtSxbKwDTK49A01xkfD30gLtanjhqutaaeHXXWS4rH7Ywd5vFgasfAlUcFsLuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecppi01CU"
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "state": "tx_+NILAfiEuEAvY02FVzTrB1kUewRC3v3gxOP9eTDl2nULqWaqTKaSaXrG68eU0INZBzsqyi1KJt5W438CjFITFDHIHfKxtmkDuED115i81achz31KiWWvXqoI7104LtSxbKwDTK49A01xkfD30gLtanjhqutaaeHXXWS4rH7Ywd5vFgasfAlUcFsLuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecppi01CU"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 9
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 9,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 9
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 9
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 9,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 9,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 10
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 10,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ABCDEFG",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "contract_id": "ABCDEFG",
        "round": 10
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "round": 10
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "caller_nonce": 10,
      "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
      "gas_price": 1,
      "gas_used": 380,
      "height": 10,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABc908qb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
    ],
    "contracts": [
      "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaegk+nj4mXf0UdfJRgm4L5FbVvJgFx3rUgij/Xg1PD7l735AYP4T6BjO/y9fLVcbbq+euGKspkj0geiEzuawl02EAKTT5+k/+2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/X4lKCT6ePiZd/RR18lGCbgvkVtW8mAXHetSCKP9eDU8PuXvfhxgICAgICAoGM7/L18tVxtur564YqymSPSB6ITO5rCXTYQApNPn6T/gICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOg+mQXDaDbOGWcenHslGbmWzbWwhDP56xU7w5Sk/D5c72AgICAgID4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAH4SaD6ZBcNoNs4ZZx6ceyUZuZbNtbCEM/nrFTvDlKT8PlzveegN8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXSFxAoBAArj4qDemVZJFGKoVINblPxU/hE+HqQP9b6ZjgvOmxY6jZAfTsDA+Qap+QamoLHf8VwmQd/h60Cq2gFj327dttU0dUjlsD+6exE6jEU6+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+HSgSBEeVwu8cW7q/gUKtI9BT7SQXY1Hq9ywIfX9gYKO8UX4UaAVaiNPbxb1nROfE0C66bQnbZgclArLhJIVIS1S0xfBX6DDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd4CAgICAgICAgICAgICAgPkDtqCFzPTTiFBffe8P/CRAwQy7JB9ShQRel6dQYB7SuYQmlvkDkoCgHdyouV7WvK8NcjTQvraEYvxQpM3YKd3dXGkU6L2B2IyAgICAgICAgICAgICAgLkDX/kDXCgBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAK+Gagsd/xXCZB3+HrQKraAWPfbt221TR1SOWwP7p7ETqMRTr4Q6EAp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXSghcz004hQX33vD/wkQMEMuyQfUoUEXpenUGAe0rmEJpb45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDAMps2tw=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
    ],
    "contracts": [
      "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "poi": "pi_+QiCPAH5Aar5Aaegk+nj4mXf0UdfJRgm4L5FbVvJgFx3rUgij/Xg1PD7l735AYP4T6BjO/y9fLVcbbq+euGKspkj0geiEzuawl02EAKTT5+k/+2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/X4lKCT6ePiZd/RR18lGCbgvkVtW8mAXHetSCKP9eDU8PuXvfhxgICAgICAoGM7/L18tVxtur564YqymSPSB6ITO5rCXTYQApNPn6T/gICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOg+mQXDaDbOGWcenHslGbmWzbWwhDP56xU7w5Sk/D5c72AgICAgID4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAH4SaD6ZBcNoNs4ZZx6ceyUZuZbNtbCEM/nrFTvDlKT8PlzveegN8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXSFxAoBAArj4qDemVZJFGKoVINblPxU/hE+HqQP9b6ZjgvOmxY6jZAfTsDA+Qap+QamoLHf8VwmQd/h60Cq2gFj327dttU0dUjlsD+6exE6jEU6+QaC+GagFWojT28W9Z0TnxNAuum0J22YHJQKy4SSFSEtUtMXwV/4QyC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABf4RKAd3Ki5Xta8rw1yNNC+toRi/FCkzdgp3d1caRTovYHYjOIQoM2miK1kuAVDrf0qzdiTuqIP6z+E2ZL3oonQdMMfIJ3p+HSgSBEeVwu8cW7q/gUKtI9BT7SQXY1Hq9ywIfX9gYKO8UX4UaAVaiNPbxb1nROfE0C66bQnbZgclArLhJIVIS1S0xfBX6DDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd4CAgICAgICAgICAgICAgPkDtqCFzPTTiFBffe8P/CRAwQy7JB9ShQRel6dQYB7SuYQmlvkDkoCgHdyouV7WvK8NcjTQvraEYvxQpM3YKd3dXGkU6L2B2IyAgICAgICAgICAgICAgLkDX/kDXCgBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAK+Gagsd/xXCZB3+HrQKraAWPfbt221TR1SOWwP7p7ETqMRTr4Q6EAp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXSghcz004hQX33vD/wkQMEMuyQfUoUEXpenUGAe0rmEJpb45qDDDeaJlRHo4YX4QKrPXDoo2A+QKyK0sayxjzyBsQNGd/jDILjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+FOgzaaIrWS4BUOt/SrN2JO6og/rP4TZkveiidB0wx8gnenxoEgRHlcLvHFu6v4FCrSPQU+0kF2NR6vcsCH1/YGCjvFFgICAgICAgICAgICAgICAAMDAMps2tw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_3NTNtGF"
    ],
    "contracts": [
      "ct_3NTNtGF"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      },
      {
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_3NTNtGF"
        ],
        "contracts": [
          "ct_3NTNtGF"
        ]
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_11111111111111111111111111111115rHyByZ"
    ],
    "contracts": []
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [
          "ak_11111111111111111111111111111115rHyByZ"
        ],
        "contracts": []
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
  "method": "channels.get.poi",
  "params": {
    "accounts": [],
    "contracts": [
      "ct_11111111111111111111111111111115rHyByZ"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 100,
        "message": "X doesn't exist"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.poi",
      "params": {
        "accounts": [],
        "contracts": [
          "ct_11111111111111111111111111111115rHyByZ"
        ]
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
  "id": -576460752303422268,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
  "id": -576460752303422268,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_+QL7ggJuAbkC9PkC8T8B+QLsuLn4t0ABuECnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdO8fPBmaSVPqmgiBusf3LOGDDJVgVOLC2Epltiext0tvuHH4bykCoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQoKoQWnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdAGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwLi5+LdAAbhAp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXTbNpXWijWsOX49kkYUP/zdszoKl6Vbyhsx2OfNGEmwErhx+G8pAqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKEICKEFp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQBggHOoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMC4ufi3QAG4QKfKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0lX7zIei0DGZIYw95F0AjiQn31YgQLzQWxawu/lJrdBK4cfhvKQKhAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChBwehBafKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0AYIBfKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFgDAuLn4t0ABuECnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdFUTlMupXff6BHiZkecmAU9bxHaOfhOFn4Tz6N0u2IMQuHH4bykCoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQkJoQWnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdAGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwOa/sTo=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAvY02FVzTrB1kUewRC3v3gxOP9eTDl2nULqWaqTKaSaXrG68eU0INZBzsqyi1KJt5W438CjFITFDHIHfKxtmkDuED115i81achz31KiWWvXqoI7104LtSxbKwDTK49A01xkfD30gLtanjhqutaaeHXXWS4rH7Ywd5vFgasfAlUcFsLuEj4RjkCoQbxEaX3zqavPVYBN6zBnfANzO9+Ju4JVR5wcMSeC4wSJQqg7wyTNImIpTu4K0vNE8X+IYnIm1WcVY2Oh2bCc0yecppi01CU",
    "trees": "ss_+QaoPgC5BRr5BReCAm0BuQUQ+QUNPwH5BQi46fjnQAGip8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQQAbjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuGn4Z0ABoqfKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0EAC4QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABem5UABoafKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0EAC5A4j5A4VAAaCnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdLkDX/kDXCgBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYMGAAG5Ay35AypGA6CZ5hscd6q9GDdi9sHQ6TPgYmMbJsjLCg6S97IA00hL9fkBufjKoEnsSQdsAgNxJqQzA+rc5DsuLDKUV7ETxQp+ItyJgJS3g2dldAG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPjroLNWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOhHRpY2sBuGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD//////////////////////////////////////////+4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQWIAAI9iAADCkYCAgFF/SexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLcUYgABNldQgIBRf+IjHWzfyTkW3kyzqYV79lz0D8JW9KFJiz9+fJgMGZNEFGIAANFXUIBRf7NWDlIdI9qcxLyVJ5JfxIV8kx4B8STJHqgp9CEPpcJOFGIAARtXUGABGVEAW2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKQWWAAUVlSYABSYADzW2AAgFJgAPNbYABRUZBWW2AgAVFRkFCDklCAkVBQgFmQgVJZYCABkIFSYCCQA2AAGVlgIAGQgVJgIJADYABZkIFSgVJZYCABkIFSYCCQA2ADgVKBUpBQkFZbUFlQUGAAUWABYABRUQFZkIFSkFBgAFJZkFZbUFBZUFBiAADKVoU0LjIuMACAAcAKuMn4x4ICbgG4wfi/PwH4u7i5+LdAAbhAp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXTvHzwZmklT6poIgbrH9yzhgwyVYFTiwthKZbYnsbdLb7hx+G8pAqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKEKCqEFp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQBggF8oAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAXAMCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4m/iZggJyAbiT+JE/AfiNqulAAaCnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdIXECgEACrDvQAGgkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAGw70ABoGSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl/1h0sosw=="
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.force_progress",
  "params": {
    "abi_version": 1,
    "amount": 10,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
    "gas_price": 1000004215,
    "nonce": 1234567
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.force_progress_tx",
  "params": {
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
    "data": {
      "signed_tx": "tx_+Qi+CwHAuQi4+Qi1ggIJAaEG8RGl986mrz1WATeswZ3wDczvfibuCVUecHDEnguMEiWhAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChuNT40gsB+IS4QC9jTYVXNOsHWRR7BELe/eDE4/15MOXadQupZqpMppJpesbrx5TQg1kHOyrKLUom3lbjfwKMUhMUMcgd8rG2aQO4QPXXmLzVpyHPfUqJZa9eqgjvXTgu1LFsrANMrj0DTXGR8PfSAu1qeOGq61pp4dddZLisftjB3m8WBqx8CVRwWwu4SPhGOQKhBvERpffOpq89VgE3rMGd8A3M734m7glVHnBwxJ4LjBIlCqDvDJM0iYilO7grS80Txf4hicibVZxVjY6HZsJzTJ5ymgu4uPi2ggI+AaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGhBafKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0AQqDD0JAhDua2ne4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMCg8q9ZdAqZR6SPlic0fUN5DjSc7YuQHi4sKhIDPk+f4kC5Bqv5Bqg+ALkFGvkFF4ICbQG5BRD5BQ0/AfkFCLjp+OdAAaKnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdBABuMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAoP//////////////////////////////////////////AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAC4afhnQAGip8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQQALhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAF6blQAGhp8p9Zb+SDVeaMERyxnfqKy+em7RBTVyMI/8/RAQwVXQQALkDiPkDhUABoKfKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0uQNf+QNcKAGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+BgwYAAbkDLfkDKkYDoJnmGxx3qr0YN2L2wdDpM+BiYxsmyMsKDpL3sgDTSEv1+QG5+MqgSexJB2wCA3EmpDMD6tzkOy4sMpRXsRPFCn4i3ImAlLeDZ2V0AbhgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+Ougs1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk6EdGljawG4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7hgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uQFBYgAAj2IAAMKRgICAUX9J7EkHbAIDcSakMwPq3OQ7LiwylFexE8UKfiLciYCUtxRiAAE2V1CAgFF/4iMdbN/JORbeTLOphXv2XPQPwlb0oUmLP358mAwZk0QUYgAA0VdQgFF/s1YOUh0j2pzEvJUnkl/EhXyTHgHxJMkeqCn0IQ+lwk4UYgABG1dQYAEZUQBbYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tgAFFRkFZbYCABUVGQUIOSUICRUFCAWZCBUllgIAGQgVJgIJADYAAZWWAgAZCBUmAgkANgAFmQgVKBUllgIAGQgVJgIJADYAOBUoFSkFCQVltQWVBQYABRYAFgAFFRAVmQgVKQUGAAUlmQVltQUFlQUGIAAMpWhTQuMi4wAIABwAq4yfjHggJuAbjB+L8/Afi7uLn4t0ABuECnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdO8fPBmaSVPqmgiBusf3LOGDDJVgVOLC2Epltiext0tvuHH4bykCoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQoKoQWnyn1lv5INV5owRHLGd+orL56btEFNXIwj/z9EBDBVdAGCAXygAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABcAwIrJggJvAYTDPwHAismCAnABhMM/AcCKyYICcQGEwz8BwLib+JmCAnIBuJP4kT8B+I2q6UABoKfKfWW/kg1XmjBEcsZ36isvnpu0QU1cjCP/P0QEMFV0hcQKAQAKsO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/UAhwHB39XDClCDEtaHT2GbJA==",
      "updates": [
        {
          "abi_version": 1,
          "amount": 10,
          "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
          "call_stack": [],
          "caller_id": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "contract_id": "ct_2Gtzj89e5eGzi1fMxRpRYSRA5zRuz844ZuYECfVYTqguQeTpze",
          "gas": 1000000,
          "gas_price": 1000004215,
          "op": "OffChainCallContract"
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
  "method": "channels.force_progress_tx",
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
    "channel_id": "ch_2qAnPJMxKZ6CB7KMCHBKNPgBMybRNMVPrqqeV1Dn8Z2z16AHHN",
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
