
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_close_solo_%2F3566%5Binitiator%5D
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
      "fsm_id": "ba_dEF3sCoVebwzfna0uc9389HrIIAB8bTrXSQA02UwnBmSs+N6"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_close_solo_%2F3566%5Binitiator%5D
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
      "fsm_id": "ba_nRaVhZFjQ+SgsjbeTxyucnnBXhN5I4ie0WO8fRhIItdUv0n4"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYMbA/Paw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423301,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEC9YYAIko7fSAueRKULj0H+UaGYYMccxyR8V3joaaO+drIzIMFpwPVVRPakUkzyo3vbB7WDOsXf2OCiYXr+BrUOuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGDNhdeGY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423301,
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_nRaVhZFjQ+SgsjbeTxyucnnBXhN5I4ie0WO8fRhIItdUv0n4"
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEC9YYAIko7fSAueRKULj0H+UaGYYMccxyR8V3joaaO+drIzIMFpwPVVRPakUkzyo3vbB7WDOsXf2OCiYXr+BrUOuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGDNhdeGY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423300,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAjrKqDct4IT++fK76xe31hgf8PXwqWizyOWN1mPIkmL0NvMWSyNndSHGMtUoO0sM6oYRAhNFS++jP7SFQRCtNALhAvWGACJKO30gLnkSlC49B/lGhmGDHHMckfFd46GmjvnayMyDBacD1VUT2pFJM8qN72we1gzrF39jgomF6/ga1DriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgzAFW/C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
  "id": -576460752303423300,
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAjrKqDct4IT++fK76xe31hgf8PXwqWizyOWN1mPIkmL0NvMWSyNndSHGMtUoO0sM6oYRAhNFS++jP7SFQRCtNALhAvWGACJKO30gLnkSlC49B/lGhmGDHHMckfFd46GmjvnayMyDBacD1VUT2pFJM8qN72we1gzrF39jgomF6/ga1DriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgzAFW/C",
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_dEF3sCoVebwzfna0uc9389HrIIAB8bTrXSQA02UwnBmSs+N6"
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAjrKqDct4IT++fK76xe31hgf8PXwqWizyOWN1mPIkmL0NvMWSyNndSHGMtUoO0sM6oYRAhNFS++jP7SFQRCtNALhAvWGACJKO30gLnkSlC49B/lGhmGDHHMckfFd46GmjvnayMyDBacD1VUT2pFJM8qN72we1gzrF39jgomF6/ga1DriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgzAFW/C",
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAjrKqDct4IT++fK76xe31hgf8PXwqWizyOWN1mPIkmL0NvMWSyNndSHGMtUoO0sM6oYRAhNFS++jP7SFQRCtNALhAvWGACJKO30gLnkSlC49B/lGhmGDHHMckfFd46GmjvnayMyDBacD1VUT2pFJM8qN72we1gzrF39jgomF6/ga1DriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgzAFW/C",
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAjrKqDct4IT++fK76xe31hgf8PXwqWizyOWN1mPIkmL0NvMWSyNndSHGMtUoO0sM6oYRAhNFS++jP7SFQRCtNALhAvWGACJKO30gLnkSlC49B/lGhmGDHHMckfFd46GmjvnayMyDBacD1VUT2pFJM8qN72we1gzrF39jgomF6/ga1DriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgzAFW/C",
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
    "data": {
      "message": {
        "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
    "data": {
      "message": {
        "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
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
  "id": -576460752303423299,
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
  "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
  "id": -576460752303423299,
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
    "data": {
      "state": "tx_+QENCwH4hLhAjrKqDct4IT++fK76xe31hgf8PXwqWizyOWN1mPIkmL0NvMWSyNndSHGMtUoO0sM6oYRAhNFS++jP7SFQRCtNALhAvWGACJKO30gLnkSlC49B/lGhmGDHHMckfFd46GmjvnayMyDBacD1VUT2pFJM8qN72we1gzrF39jgomF6/ga1DriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgzAFW/C"
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
    "data": {
      "state": "tx_+QENCwH4hLhAjrKqDct4IT++fK76xe31hgf8PXwqWizyOWN1mPIkmL0NvMWSyNndSHGMtUoO0sM6oYRAhNFS++jP7SFQRCtNALhAvWGACJKO30gLnkSlC49B/lGhmGDHHMckfFd46GmjvnayMyDBacD1VUT2pFJM8qN72we1gzrF39jgomF6/ga1DriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgzAFW/C"
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
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBuD+o/FjDzgN579NSkY6AKgRrL9BS/q1Z3o65c7J/z7ooQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYC5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGFT7sgIAADfL9OUs=",
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
    "signed_tx": "tx_+QHrCwH4QrhA0pMQnQowHc62GAJpOlJ4cGJP43xfytP8bTpsF8i2GWBsQGFO88JlAQGZ2nca20jEEZ+mbG+XPBNSAMCflGmSD7kBovkBnzYBoQbg/qPxYw84Dee/TUpGOgCoEay/QUv6tWd6OuXOyf8+6KEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAA0uZGtK"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhA0pMQnQowHc62GAJpOlJ4cGJP43xfytP8bTpsF8i2GWBsQGFO88JlAQGZ2nca20jEEZ+mbG+XPBNSAMCflGmSD7kBovkBnzYBoQbg/qPxYw84Dee/TUpGOgCoEay/QUv6tWd6OuXOyf8+6KEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAA0uZGtK",
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhA0pMQnQowHc62GAJpOlJ4cGJP43xfytP8bTpsF8i2GWBsQGFO88JlAQGZ2nca20jEEZ+mbG+XPBNSAMCflGmSD7kBovkBnzYBoQbg/qPxYw84Dee/TUpGOgCoEay/QUv6tWd6OuXOyf8+6KEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAA0uZGtK",
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBuD+o/FjDzgN579NSkY6AKgRrL9BS/q1Z3o65c7J/z7ooQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/+GJGE5yoABAIYPXtZ/KAAEYx5H2w==",
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
    "signed_tx": "tx_+KcLAfhCuEAiF5l65ktNa9UP8U7Uk08zgBrD0yDOgIOAxibK4y25fqBXolcB7gB/XBMaGyLMgqOqJ2aPC7KNbE7voz17AIEDuF/4XTgBoQbg/qPxYw84Dee/TUpGOgCoEay/QUv6tWd6OuXOyf8+6KEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygABOOsp0c="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEAiF5l65ktNa9UP8U7Uk08zgBrD0yDOgIOAxibK4y25fqBXolcB7gB/XBMaGyLMgqOqJ2aPC7KNbE7voz17AIEDuF/4XTgBoQbg/qPxYw84Dee/TUpGOgCoEay/QUv6tWd6OuXOyf8+6KEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygABOOsp0c=",
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEAiF5l65ktNa9UP8U7Uk08zgBrD0yDOgIOAxibK4y25fqBXolcB7gB/XBMaGyLMgqOqJ2aPC7KNbE7voz17AIEDuF/4XTgBoQbg/qPxYw84Dee/TUpGOgCoEay/QUv6tWd6OuXOyf8+6KEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygABOOsp0c=",
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
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
    "channel_id": "ch_2i6BsGhKFuoJRWPgCkJ8Q9G1wn7z7Ex26jgitQCHt5kJm1a7bz",
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
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_close_solo_%2F3566%5Bresponder%5D
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
      "fsm_id": "ba_J7lUTX3SBX7UT5BYASqqkdMc7aHTqvWktjSREbUTu6HZ72E1"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_close_solo_%2F3566%5Bresponder%5D
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
      "fsm_id": "ba_naK2pv0W+JMsWxl/yeqP9jtLuRRrmMLZh6hXAGXYAZQAnGCQ"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYOevRqlA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423298,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDJxtBkFBE6qPXy6LUDX2IytCZb7sRLxU17tYYdbm1Kduu0rOrewGEkgjvrXieOAMOtqgGsmLvLJzx6y3ZJveQIuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGDsb/8TU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423298,
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_naK2pv0W+JMsWxl/yeqP9jtLuRRrmMLZh6hXAGXYAZQAnGCQ"
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEDJxtBkFBE6qPXy6LUDX2IytCZb7sRLxU17tYYdbm1Kduu0rOrewGEkgjvrXieOAMOtqgGsmLvLJzx6y3ZJveQIuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGDsb/8TU=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423297,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAtqW7nQ0wkV0z0ruXMNTxZMqvfocZC/c1TGX2ni3RD29bWWEReeueIMZG1bL4Iar1PfEPZEsY/7WTQz/ht/6oCLhAycbQZBQROqj18ui1A19iMrQmW+7ES8VNe7WGHW5tSnbrtKzq3sBhJII7614njgDDraoBrJi7yyc8est2Sb3kCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rg66wKgB"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
  "id": -576460752303423297,
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAtqW7nQ0wkV0z0ruXMNTxZMqvfocZC/c1TGX2ni3RD29bWWEReeueIMZG1bL4Iar1PfEPZEsY/7WTQz/ht/6oCLhAycbQZBQROqj18ui1A19iMrQmW+7ES8VNe7WGHW5tSnbrtKzq3sBhJII7614njgDDraoBrJi7yyc8est2Sb3kCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rg66wKgB",
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_J7lUTX3SBX7UT5BYASqqkdMc7aHTqvWktjSREbUTu6HZ72E1"
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAtqW7nQ0wkV0z0ruXMNTxZMqvfocZC/c1TGX2ni3RD29bWWEReeueIMZG1bL4Iar1PfEPZEsY/7WTQz/ht/6oCLhAycbQZBQROqj18ui1A19iMrQmW+7ES8VNe7WGHW5tSnbrtKzq3sBhJII7614njgDDraoBrJi7yyc8est2Sb3kCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rg66wKgB",
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAtqW7nQ0wkV0z0ruXMNTxZMqvfocZC/c1TGX2ni3RD29bWWEReeueIMZG1bL4Iar1PfEPZEsY/7WTQz/ht/6oCLhAycbQZBQROqj18ui1A19iMrQmW+7ES8VNe7WGHW5tSnbrtKzq3sBhJII7614njgDDraoBrJi7yyc8est2Sb3kCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rg66wKgB",
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAtqW7nQ0wkV0z0ruXMNTxZMqvfocZC/c1TGX2ni3RD29bWWEReeueIMZG1bL4Iar1PfEPZEsY/7WTQz/ht/6oCLhAycbQZBQROqj18ui1A19iMrQmW+7ES8VNe7WGHW5tSnbrtKzq3sBhJII7614njgDDraoBrJi7yyc8est2Sb3kCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rg66wKgB",
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
    "data": {
      "message": {
        "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
    "data": {
      "message": {
        "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
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
  "id": -576460752303423296,
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
  "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
  "id": -576460752303423296,
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
    "data": {
      "event": "open"
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
    "data": {
      "state": "tx_+QENCwH4hLhAtqW7nQ0wkV0z0ruXMNTxZMqvfocZC/c1TGX2ni3RD29bWWEReeueIMZG1bL4Iar1PfEPZEsY/7WTQz/ht/6oCLhAycbQZBQROqj18ui1A19iMrQmW+7ES8VNe7WGHW5tSnbrtKzq3sBhJII7614njgDDraoBrJi7yyc8est2Sb3kCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rg66wKgB"
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
    "data": {
      "state": "tx_+QENCwH4hLhAtqW7nQ0wkV0z0ruXMNTxZMqvfocZC/c1TGX2ni3RD29bWWEReeueIMZG1bL4Iar1PfEPZEsY/7WTQz/ht/6oCLhAycbQZBQROqj18ui1A19iMrQmW+7ES8VNe7WGHW5tSnbrtKzq3sBhJII7614njgDDraoBrJi7yyc8est2Sb3kCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rg66wKgB"
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
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBt61T4F/LX1Y2c86jJWTOPVPCleaewj8TcPg/ly7DaiUoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYC5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACGFT7sgIAABRy23+U=",
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
    "signed_tx": "tx_+QHrCwH4QrhAARp/7nLd+Vdip+j7SZ0Xz26ZGuFq9wJ5w/lw+TSZW4ua6O++oB4g6MzVeLCcK62FcHHNDPI0cnSSHzht3ekZBbkBovkBnzYBoQbetU+Bfy19WNnPOoyVkzj1TwpXmnsI/E3D4P5cuw2olKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAAVGCqUj"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAARp/7nLd+Vdip+j7SZ0Xz26ZGuFq9wJ5w/lw+TSZW4ua6O++oB4g6MzVeLCcK62FcHHNDPI0cnSSHzht3ekZBbkBovkBnzYBoQbetU+Bfy19WNnPOoyVkzj1TwpXmnsI/E3D4P5cuw2olKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAAVGCqUj",
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAARp/7nLd+Vdip+j7SZ0Xz26ZGuFq9wJ5w/lw+TSZW4ua6O++oB4g6MzVeLCcK62FcHHNDPI0cnSSHzht3ekZBbkBovkBnzYBoQbetU+Bfy19WNnPOoyVkzj1TwpXmnsI/E3D4P5cuw2olKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhhU+7ICAAAVGCqUj",
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
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
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBt61T4F/LX1Y2c86jJWTOPVPCleaewj8TcPg/ly7DaiUoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiX/+GJGE5yoABAIYPXtZ/KAAPwNjSug==",
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
    "signed_tx": "tx_+KcLAfhCuEARL729krsKxvwsM1L3HVE9F0WN1T59/4ZD81mZErRWVeWPe1W4VxGeQRbvDEPL62HJ2J26JKb3nm4eeWu+ZoUOuF/4XTgBoQbetU+Bfy19WNnPOoyVkzj1TwpXmnsI/E3D4P5cuw2olKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olIl//hiRhOcqAAQCGD17WfygADz1yM6c="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEARL729krsKxvwsM1L3HVE9F0WN1T59/4ZD81mZErRWVeWPe1W4VxGeQRbvDEPL62HJ2J26JKb3nm4eeWu+ZoUOuF/4XTgBoQbetU+Bfy19WNnPOoyVkzj1TwpXmnsI/E3D4P5cuw2olKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olIl//hiRhOcqAAQCGD17WfygADz1yM6c=",
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEARL729krsKxvwsM1L3HVE9F0WN1T59/4ZD81mZErRWVeWPe1W4VxGeQRbvDEPL62HJ2J26JKb3nm4eeWu+ZoUOuF/4XTgBoQbetU+Bfy19WNnPOoyVkzj1TwpXmnsI/E3D4P5cuw2olKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olIl//hiRhOcqAAQCGD17WfygADz1yM6c=",
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
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
    "channel_id": "ch_2h5nRgDpjmXEF7CuP9ikNfF9EgdkgN5BHknMmFVJmUNDmHAUTD",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
