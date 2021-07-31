
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&fee=246913579753086&gas_price=1000000000&host=localhost&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=initiator
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
      "fsm_id": "ba_7EwEcHMuSYQSFmPLIkRtNga30xOWs9Pm+voi3I+yjpVObmJ7"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&fee=246913579753086&gas_price=1000000000&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=responder
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
      "fsm_id": "ba_bCYqwNwSK9pVQLo+3hPtwj2rahLzllYueRqAdVr9g063oB2X"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhuCRDDYefsCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZnAFwAwg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422495,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDEHpK6E+0/rhB07n6ZwtXVQdRM+Pb8jaRsJigTrjGGZriN1yZa+A4VjVsgKuSOwGmMxLgiwBJ6etGQRkuKKZgOuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIbgkQw2Hn7AoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGZwMrSiY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422495,
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_bCYqwNwSK9pVQLo+3hPtwj2rahLzllYueRqAdVr9g063oB2X"
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEDEHpK6E+0/rhB07n6ZwtXVQdRM+Pb8jaRsJigTrjGGZriN1yZa+A4VjVsgKuSOwGmMxLgiwBJ6etGQRkuKKZgOuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIbgkQw2Hn7AoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGZwMrSiY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422494,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAxB6SuhPtP64QdO5+mcLV1UHUTPj2/I2kbCYoE64xhma4jdcmWvgOFY1bICrkjsBpjMS4IsASenrRkEZLiimYDrhA6EDVNPcNeYA9FFsGQaWJyyfEkm48jd4PqZU2GxtosGRx2H42qGTKjB4Ok6oX5PStgAhXOJI1xAzN10tpUPcEA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCG4JEMNh5+wKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmcD3aeG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
  "id": -576460752303422494,
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAxB6SuhPtP64QdO5+mcLV1UHUTPj2/I2kbCYoE64xhma4jdcmWvgOFY1bICrkjsBpjMS4IsASenrRkEZLiimYDrhA6EDVNPcNeYA9FFsGQaWJyyfEkm48jd4PqZU2GxtosGRx2H42qGTKjB4Ok6oX5PStgAhXOJI1xAzN10tpUPcEA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCG4JEMNh5+wKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmcD3aeG",
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_7EwEcHMuSYQSFmPLIkRtNga30xOWs9Pm+voi3I+yjpVObmJ7"
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAxB6SuhPtP64QdO5+mcLV1UHUTPj2/I2kbCYoE64xhma4jdcmWvgOFY1bICrkjsBpjMS4IsASenrRkEZLiimYDrhA6EDVNPcNeYA9FFsGQaWJyyfEkm48jd4PqZU2GxtosGRx2H42qGTKjB4Ok6oX5PStgAhXOJI1xAzN10tpUPcEA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCG4JEMNh5+wKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmcD3aeG",
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAxB6SuhPtP64QdO5+mcLV1UHUTPj2/I2kbCYoE64xhma4jdcmWvgOFY1bICrkjsBpjMS4IsASenrRkEZLiimYDrhA6EDVNPcNeYA9FFsGQaWJyyfEkm48jd4PqZU2GxtosGRx2H42qGTKjB4Ok6oX5PStgAhXOJI1xAzN10tpUPcEA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCG4JEMNh5+wKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmcD3aeG",
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAxB6SuhPtP64QdO5+mcLV1UHUTPj2/I2kbCYoE64xhma4jdcmWvgOFY1bICrkjsBpjMS4IsASenrRkEZLiimYDrhA6EDVNPcNeYA9FFsGQaWJyyfEkm48jd4PqZU2GxtosGRx2H42qGTKjB4Ok6oX5PStgAhXOJI1xAzN10tpUPcEA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCG4JEMNh5+wKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmcD3aeG",
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
    "data": {
      "message": {
        "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
    "data": {
      "message": {
        "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
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
  "id": -576460752303422493,
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
  "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
  "id": -576460752303422493,
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
    "data": {
      "state": "tx_+QENCwH4hLhAxB6SuhPtP64QdO5+mcLV1UHUTPj2/I2kbCYoE64xhma4jdcmWvgOFY1bICrkjsBpjMS4IsASenrRkEZLiimYDrhA6EDVNPcNeYA9FFsGQaWJyyfEkm48jd4PqZU2GxtosGRx2H42qGTKjB4Ok6oX5PStgAhXOJI1xAzN10tpUPcEA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCG4JEMNh5+wKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmcD3aeG"
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
    "data": {
      "state": "tx_+QENCwH4hLhAxB6SuhPtP64QdO5+mcLV1UHUTPj2/I2kbCYoE64xhma4jdcmWvgOFY1bICrkjsBpjMS4IsASenrRkEZLiimYDrhA6EDVNPcNeYA9FFsGQaWJyyfEkm48jd4PqZU2GxtosGRx2H42qGTKjB4Ok6oX5PStgAhXOJI1xAzN10tpUPcEA7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCG4JEMNh5+wKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmcD3aeG"
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBp87hXgZw+h5FbPfE/B9FAHHYTPuViFgJFUJfu8kT9aooQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY3+rniy/+GHLHOiuwBAIYPXtZ/KABoMydUtg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422492,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEAayLXBIrP/VphT85oxLJ/si+LkR+HiCVythXL7PxuzF+SuJz9gDTswN5iMC9aW1DGxAilL9NFl/uf2I1k4uP0DuF/4XTUBoQafO4V4GcPoeRWz3xPwfRQBx2Ez7lYhYCRVCX7vJE/WqKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAaKYNYS0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
  "id": -576460752303422492,
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEAayLXBIrP/VphT85oxLJ/si+LkR+HiCVythXL7PxuzF+SuJz9gDTswN5iMC9aW1DGxAilL9NFl/uf2I1k4uP0DuF/4XTUBoQafO4V4GcPoeRWz3xPwfRQBx2Ez7lYhYCRVCX7vJE/WqKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAaKYNYS0=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422491,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEAayLXBIrP/VphT85oxLJ/si+LkR+HiCVythXL7PxuzF+SuJz9gDTswN5iMC9aW1DGxAilL9NFl/uf2I1k4uP0DuEC6cq/jorgYqDsaOGdlJShbSUZRp/6XuLNMLNecXUGOmdIxz/8/9ySTq5+XHm4F0spdvFnhwywC/0/HL/QTkwYPuF/4XTUBoQafO4V4GcPoeRWz3xPwfRQBx2Ez7lYhYCRVCX7vJE/WqKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAaH0Qfoc="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
  "id": -576460752303422491,
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAayLXBIrP/VphT85oxLJ/si+LkR+HiCVythXL7PxuzF+SuJz9gDTswN5iMC9aW1DGxAilL9NFl/uf2I1k4uP0DuEC6cq/jorgYqDsaOGdlJShbSUZRp/6XuLNMLNecXUGOmdIxz/8/9ySTq5+XHm4F0spdvFnhwywC/0/HL/QTkwYPuF/4XTUBoQafO4V4GcPoeRWz3xPwfRQBx2Ez7lYhYCRVCX7vJE/WqKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAaH0Qfoc=",
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAayLXBIrP/VphT85oxLJ/si+LkR+HiCVythXL7PxuzF+SuJz9gDTswN5iMC9aW1DGxAilL9NFl/uf2I1k4uP0DuEC6cq/jorgYqDsaOGdlJShbSUZRp/6XuLNMLNecXUGOmdIxz/8/9ySTq5+XHm4F0spdvFnhwywC/0/HL/QTkwYPuF/4XTUBoQafO4V4GcPoeRWz3xPwfRQBx2Ez7lYhYCRVCX7vJE/WqKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAaH0Qfoc=",
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAayLXBIrP/VphT85oxLJ/si+LkR+HiCVythXL7PxuzF+SuJz9gDTswN5iMC9aW1DGxAilL9NFl/uf2I1k4uP0DuEC6cq/jorgYqDsaOGdlJShbSUZRp/6XuLNMLNecXUGOmdIxz/8/9ySTq5+XHm4F0spdvFnhwywC/0/HL/QTkwYPuF/4XTUBoQafO4V4GcPoeRWz3xPwfRQBx2Ez7lYhYCRVCX7vJE/WqKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAaH0Qfoc=",
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAayLXBIrP/VphT85oxLJ/si+LkR+HiCVythXL7PxuzF+SuJz9gDTswN5iMC9aW1DGxAilL9NFl/uf2I1k4uP0DuEC6cq/jorgYqDsaOGdlJShbSUZRp/6XuLNMLNecXUGOmdIxz/8/9ySTq5+XHm4F0spdvFnhwywC/0/HL/QTkwYPuF/4XTUBoQafO4V4GcPoeRWz3xPwfRQBx2Ez7lYhYCRVCX7vJE/WqKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGN/q54sv/hhyxzorsAQCGD17WfygAaH0Qfoc=",
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
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
    "channel_id": "ch_2D8P5TePFnGH3b5AAiMgNmvVVXS2LXdsgGpSE4mywgbTv5gdiE",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
