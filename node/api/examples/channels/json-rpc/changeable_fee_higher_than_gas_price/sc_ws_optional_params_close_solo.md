
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
      "fsm_id": "ba_J6l2f/q32zLkvEMHDc8DxJf45vIujW9oEX9OzzXLQ6qznIUU"
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
      "fsm_id": "ba_eImre0L2PTA4eeRidONgMjtRGc+iFZ/Gnrhn0qxLUZjFzqu6"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZyhyZqGw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422433,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECcOQJklPSxwBJ/j1+ffwuKDkiKXb9gBsbuRhFsq5Ctcn5y+rb0icnufG/FxyUE5wSfpGNqGwfQJHyLMbNk/iMLuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGctHUaBM="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422433,
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_eImre0L2PTA4eeRidONgMjtRGc+iFZ/Gnrhn0qxLUZjFzqu6"
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
    "data": {
      "signed_tx": "tx_+MsLAfhCuECcOQJklPSxwBJ/j1+ffwuKDkiKXb9gBsbuRhFsq5Ctcn5y+rb0icnufG/FxyUE5wSfpGNqGwfQJHyLMbNk/iMLuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGctHUaBM=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422432,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAcaC1i4GieUzIxX2eFa0RnXB7tCk0k3Z2QcZe3nTZG8cPND2ieaBfdkMOY6EwiUosLpobpU2x1lVwG3EVcyKLALhAnDkCZJT0scASf49fn38Lig5Iil2/YAbG7kYRbKuQrXJ+cvq29InJ7nxvxcclBOcEn6RjahsH0CR8izGzZP4jC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnJT+jFY"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
  "id": -576460752303422432,
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAcaC1i4GieUzIxX2eFa0RnXB7tCk0k3Z2QcZe3nTZG8cPND2ieaBfdkMOY6EwiUosLpobpU2x1lVwG3EVcyKLALhAnDkCZJT0scASf49fn38Lig5Iil2/YAbG7kYRbKuQrXJ+cvq29InJ7nxvxcclBOcEn6RjahsH0CR8izGzZP4jC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnJT+jFY",
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_J6l2f/q32zLkvEMHDc8DxJf45vIujW9oEX9OzzXLQ6qznIUU"
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAcaC1i4GieUzIxX2eFa0RnXB7tCk0k3Z2QcZe3nTZG8cPND2ieaBfdkMOY6EwiUosLpobpU2x1lVwG3EVcyKLALhAnDkCZJT0scASf49fn38Lig5Iil2/YAbG7kYRbKuQrXJ+cvq29InJ7nxvxcclBOcEn6RjahsH0CR8izGzZP4jC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnJT+jFY",
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAcaC1i4GieUzIxX2eFa0RnXB7tCk0k3Z2QcZe3nTZG8cPND2ieaBfdkMOY6EwiUosLpobpU2x1lVwG3EVcyKLALhAnDkCZJT0scASf49fn38Lig5Iil2/YAbG7kYRbKuQrXJ+cvq29InJ7nxvxcclBOcEn6RjahsH0CR8izGzZP4jC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnJT+jFY",
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAcaC1i4GieUzIxX2eFa0RnXB7tCk0k3Z2QcZe3nTZG8cPND2ieaBfdkMOY6EwiUosLpobpU2x1lVwG3EVcyKLALhAnDkCZJT0scASf49fn38Lig5Iil2/YAbG7kYRbKuQrXJ+cvq29InJ7nxvxcclBOcEn6RjahsH0CR8izGzZP4jC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnJT+jFY",
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
    "data": {
      "message": {
        "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
    "data": {
      "message": {
        "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
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
  "id": -576460752303422431,
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
  "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
  "id": -576460752303422431,
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
    "data": {
      "state": "tx_+QENCwH4hLhAcaC1i4GieUzIxX2eFa0RnXB7tCk0k3Z2QcZe3nTZG8cPND2ieaBfdkMOY6EwiUosLpobpU2x1lVwG3EVcyKLALhAnDkCZJT0scASf49fn38Lig5Iil2/YAbG7kYRbKuQrXJ+cvq29InJ7nxvxcclBOcEn6RjahsH0CR8izGzZP4jC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnJT+jFY"
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
    "data": {
      "state": "tx_+QENCwH4hLhAcaC1i4GieUzIxX2eFa0RnXB7tCk0k3Z2QcZe3nTZG8cPND2ieaBfdkMOY6EwiUosLpobpU2x1lVwG3EVcyKLALhAnDkCZJT0scASf49fn38Lig5Iil2/YAbG7kYRbKuQrXJ+cvq29InJ7nxvxcclBOcEn6RjahsH0CR8izGzZP4jC7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnJT+jFY"
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
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBga/D8884WgF3RuOP0324Y9t0zgM4Y5CfHVi1ZeQ3ECHoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYC5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACG4JEMNh5+c/G1+gk=",
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
    "signed_tx": "tx_+QHrCwH4QrhARNC5xCjA7OclD/DVlWPEVv0xsfofZo2OF3cppUvuxXJMwNhVjdaAl2C0BgXSx0a3khS6KPNbG457mbZ1ArogC7kBovkBnzYBoQYGvw/PPOFoBd0bjj9N9uGPbdM4DOGOQnx1YtWXkNxAh6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhuCRDDYefnMCSEL6"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhARNC5xCjA7OclD/DVlWPEVv0xsfofZo2OF3cppUvuxXJMwNhVjdaAl2C0BgXSx0a3khS6KPNbG457mbZ1ArogC7kBovkBnzYBoQYGvw/PPOFoBd0bjj9N9uGPbdM4DOGOQnx1YtWXkNxAh6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhuCRDDYefnMCSEL6",
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhARNC5xCjA7OclD/DVlWPEVv0xsfofZo2OF3cppUvuxXJMwNhVjdaAl2C0BgXSx0a3khS6KPNbG457mbZ1ArogC7kBovkBnzYBoQYGvw/PPOFoBd0bjj9N9uGPbdM4DOGOQnx1YtWXkNxAh6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhuCRDDYefnMCSEL6",
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBga/D8884WgF3RuOP0324Y9t0zgM4Y5CfHVi1ZeQ3ECHoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/+GJGE5yoABAIYPXtZ/KAAu85E+xA==",
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
    "signed_tx": "tx_+KcLAfhCuEA8RAV2rnIlIi1vuckKNGctJBie7ImqT/SYFty86b4RrK/cSwAXB+qK6JUKi1sqv/Wk9a/rUxQqT25NXW8/+h0DuF/4XTgBoQYGvw/PPOFoBd0bjj9N9uGPbdM4DOGOQnx1YtWXkNxAh6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygALhzkpOA="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEA8RAV2rnIlIi1vuckKNGctJBie7ImqT/SYFty86b4RrK/cSwAXB+qK6JUKi1sqv/Wk9a/rUxQqT25NXW8/+h0DuF/4XTgBoQYGvw/PPOFoBd0bjj9N9uGPbdM4DOGOQnx1YtWXkNxAh6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygALhzkpOA=",
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEA8RAV2rnIlIi1vuckKNGctJBie7ImqT/SYFty86b4RrK/cSwAXB+qK6JUKi1sqv/Wk9a/rUxQqT25NXW8/+h0DuF/4XTgBoQYGvw/PPOFoBd0bjj9N9uGPbdM4DOGOQnx1YtWXkNxAh6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygALhzkpOA=",
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
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
    "channel_id": "ch_3yKuugdY2cemApPhZywUCsvJgEpwqFDZK9WUVHvG4dqnVcqEp",
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
      "fsm_id": "ba_NsE1/xEWQasHdG3Mug9EBTLP37VnTG3zt6BE+3OElDTtweQh"
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
      "fsm_id": "ba_EVN8guEXTqXSH972KU5uxdS1TJLguRXjlLF/JtNr+bCADL3O"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZ0h+bmGw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422430,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEApqPN0x07ztvsmHJxqzwGjSiutIMC8iiDV4j4+pIPV8CgM006WBVZG0H9kX+WMppCDa2I+/wC5yI8bkNL5Sz8KuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGdFZJKis="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422430,
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_EVN8guEXTqXSH972KU5uxdS1TJLguRXjlLF/JtNr+bCADL3O"
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEApqPN0x07ztvsmHJxqzwGjSiutIMC8iiDV4j4+pIPV8CgM006WBVZG0H9kX+WMppCDa2I+/wC5yI8bkNL5Sz8KuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGdFZJKis=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422429,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAKajzdMdO87b7Jhycas8Bo0orrSDAvIog1eI+PqSD1fAoDNNOlgVWRtB/ZF/ljKaQg2tiPv8AuciPG5DS+Us/CrhA0l0SoHglaY37rLCq+szr/HiUEwzTj0vqnBGG2f+ioyWiAX6jOwwm8bHpjApSeRiX7FXToZsh3TeBSc0f+g/3B7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnRWbk+m"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
  "id": -576460752303422429,
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAKajzdMdO87b7Jhycas8Bo0orrSDAvIog1eI+PqSD1fAoDNNOlgVWRtB/ZF/ljKaQg2tiPv8AuciPG5DS+Us/CrhA0l0SoHglaY37rLCq+szr/HiUEwzTj0vqnBGG2f+ioyWiAX6jOwwm8bHpjApSeRiX7FXToZsh3TeBSc0f+g/3B7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnRWbk+m",
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_NsE1/xEWQasHdG3Mug9EBTLP37VnTG3zt6BE+3OElDTtweQh"
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAKajzdMdO87b7Jhycas8Bo0orrSDAvIog1eI+PqSD1fAoDNNOlgVWRtB/ZF/ljKaQg2tiPv8AuciPG5DS+Us/CrhA0l0SoHglaY37rLCq+szr/HiUEwzTj0vqnBGG2f+ioyWiAX6jOwwm8bHpjApSeRiX7FXToZsh3TeBSc0f+g/3B7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnRWbk+m",
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAKajzdMdO87b7Jhycas8Bo0orrSDAvIog1eI+PqSD1fAoDNNOlgVWRtB/ZF/ljKaQg2tiPv8AuciPG5DS+Us/CrhA0l0SoHglaY37rLCq+szr/HiUEwzTj0vqnBGG2f+ioyWiAX6jOwwm8bHpjApSeRiX7FXToZsh3TeBSc0f+g/3B7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnRWbk+m",
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAKajzdMdO87b7Jhycas8Bo0orrSDAvIog1eI+PqSD1fAoDNNOlgVWRtB/ZF/ljKaQg2tiPv8AuciPG5DS+Us/CrhA0l0SoHglaY37rLCq+szr/HiUEwzTj0vqnBGG2f+ioyWiAX6jOwwm8bHpjApSeRiX7FXToZsh3TeBSc0f+g/3B7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnRWbk+m",
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
    "data": {
      "message": {
        "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
    "data": {
      "message": {
        "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
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
  "id": -576460752303422428,
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
  "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
  "id": -576460752303422428,
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
    "data": {
      "state": "tx_+QENCwH4hLhAKajzdMdO87b7Jhycas8Bo0orrSDAvIog1eI+PqSD1fAoDNNOlgVWRtB/ZF/ljKaQg2tiPv8AuciPG5DS+Us/CrhA0l0SoHglaY37rLCq+szr/HiUEwzTj0vqnBGG2f+ioyWiAX6jOwwm8bHpjApSeRiX7FXToZsh3TeBSc0f+g/3B7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnRWbk+m"
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
    "data": {
      "state": "tx_+QENCwH4hLhAKajzdMdO87b7Jhycas8Bo0orrSDAvIog1eI+PqSD1fAoDNNOlgVWRtB/ZF/ljKaQg2tiPv8AuciPG5DS+Us/CrhA0l0SoHglaY37rLCq+szr/HiUEwzTj0vqnBGG2f+ioyWiAX6jOwwm8bHpjApSeRiX7FXToZsh3TeBSc0f+g/3B7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RnRWbk+m"
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
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBsksdFzarQH1qlgoHBQoVJxBTCTwhCFHIZDxvJRV+2HuoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYC5AUz5AUk8AfkBP/kBPKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/kBGPh0oCNUzmsFwO8JW2KKUudPGyTXdzmQLyewuLVuDjWYVRpv+FGAgICAgICgmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUaAgKDJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c4CAgICAgID4T6CZ36HSw2UtzwDHftg4q3/mNA6xY525nVQAX+0SUIhRRu2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//4T6DJDIPhwDis2TZUmAJD2Gt0XhOJhKVd5T3NbMzrvKg1c+2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgAHAwMDAwACG4JEMNh5+L/s4wnY=",
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
    "signed_tx": "tx_+QHrCwH4QrhAzU24d0GptU3FvDqplZHaS/dQO1RttVRY2s4HjLhbb3RmItTAKFtSNNkbv3hYs8lJ1Jmh/bVo6jnbEz76wijGCrkBovkBnzYBoQbJLHRc2q0B9apYKBwUKFScQUwk8IQhRyGQ8byUVfth7qEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhuCRDDYefi83DH+H"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAzU24d0GptU3FvDqplZHaS/dQO1RttVRY2s4HjLhbb3RmItTAKFtSNNkbv3hYs8lJ1Jmh/bVo6jnbEz76wijGCrkBovkBnzYBoQbJLHRc2q0B9apYKBwUKFScQUwk8IQhRyGQ8byUVfth7qEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhuCRDDYefi83DH+H",
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAzU24d0GptU3FvDqplZHaS/dQO1RttVRY2s4HjLhbb3RmItTAKFtSNNkbv3hYs8lJ1Jmh/bVo6jnbEz76wijGCrkBovkBnzYBoQbJLHRc2q0B9apYKBwUKFScQUwk8IQhRyGQ8byUVfth7qEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGAuQFM+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAAhuCRDDYefi83DH+H",
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBsksdFzarQH1qlgoHBQoVJxBTCTwhCFHIZDxvJRV+2HuoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/+GJGE5yoABAIYPXtZ/KAAwC+pQOw==",
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
    "signed_tx": "tx_+KcLAfhCuECwxrjOByfibigVWrEHjVoqy/W1jmkvl4MtzxvHHLFY5Oor8FrbmLCXQ7KcsmyWEUlmZVYS7rJtHgU72MIDeZcNuF/4XTgBoQbJLHRc2q0B9apYKBwUKFScQUwk8IQhRyGQ8byUVfth7qEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAMHaS6Zg="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECwxrjOByfibigVWrEHjVoqy/W1jmkvl4MtzxvHHLFY5Oor8FrbmLCXQ7KcsmyWEUlmZVYS7rJtHgU72MIDeZcNuF/4XTgBoQbJLHRc2q0B9apYKBwUKFScQUwk8IQhRyGQ8byUVfth7qEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAMHaS6Zg=",
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECwxrjOByfibigVWrEHjVoqy/W1jmkvl4MtzxvHHLFY5Oor8FrbmLCXQ7KcsmyWEUlmZVYS7rJtHgU72MIDeZcNuF/4XTgBoQbJLHRc2q0B9apYKBwUKFScQUwk8IQhRyGQ8byUVfth7qEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl//hiRhOcqAAQCGD17WfygAMHaS6Zg=",
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
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
    "channel_id": "ch_2XbiEU5qNnofZMhJKHDxW2c24dUHNKgxjtmNj5D4NsPDNmHrn2",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
