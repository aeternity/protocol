
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish_wrong_fsm_id%2F3741
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
      "fsm_id": "ba_D1nnPHG7qqEXDDP6vufkgfstr8spC+Q8wSi1ql2okw+g/Vc5"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish_wrong_fsm_id%2F3741
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
      "fsm_id": "ba_HgXsuteXOQAPf0muqgUWID83wZiCAhgCV+sP797by+h2UuJp"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYWIzFkKg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423247,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECp1KHWPUPluYv2F1z01ivk7YqHDM+Q634ArXOutHI6XzoaUzI53RqrlTOtfIKruDuLXH1q6mIeiPK7OjVZYKYOuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGFoeZv+U="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423247,
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_HgXsuteXOQAPf0muqgUWID83wZiCAhgCV+sP797by+h2UuJp"
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "signed_tx": "tx_+MsLAfhCuECp1KHWPUPluYv2F1z01ivk7YqHDM+Q634ArXOutHI6XzoaUzI53RqrlTOtfIKruDuLXH1q6mIeiPK7OjVZYKYOuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGFoeZv+U=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423246,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAPfCqbE9iAkjDqS/dptexOaWDmlKoSIab/QlqzR6X7OAylOTW9Fdjg2NgO4172AJRBLR5VCgbvyC6qpigOcq2D7hAqdSh1j1D5bmL9hdc9NYr5O2KhwzPkOt+AK1zrrRyOl86GlMyOd0aq5UzrXyCq7g7i1x9aupiHojyuzo1WWCmDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhbxiG20"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423246,
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAPfCqbE9iAkjDqS/dptexOaWDmlKoSIab/QlqzR6X7OAylOTW9Fdjg2NgO4172AJRBLR5VCgbvyC6qpigOcq2D7hAqdSh1j1D5bmL9hdc9NYr5O2KhwzPkOt+AK1zrrRyOl86GlMyOd0aq5UzrXyCq7g7i1x9aupiHojyuzo1WWCmDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhbxiG20",
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_D1nnPHG7qqEXDDP6vufkgfstr8spC+Q8wSi1ql2okw+g/Vc5"
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAPfCqbE9iAkjDqS/dptexOaWDmlKoSIab/QlqzR6X7OAylOTW9Fdjg2NgO4172AJRBLR5VCgbvyC6qpigOcq2D7hAqdSh1j1D5bmL9hdc9NYr5O2KhwzPkOt+AK1zrrRyOl86GlMyOd0aq5UzrXyCq7g7i1x9aupiHojyuzo1WWCmDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhbxiG20",
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAPfCqbE9iAkjDqS/dptexOaWDmlKoSIab/QlqzR6X7OAylOTW9Fdjg2NgO4172AJRBLR5VCgbvyC6qpigOcq2D7hAqdSh1j1D5bmL9hdc9NYr5O2KhwzPkOt+AK1zrrRyOl86GlMyOd0aq5UzrXyCq7g7i1x9aupiHojyuzo1WWCmDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhbxiG20",
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAPfCqbE9iAkjDqS/dptexOaWDmlKoSIab/QlqzR6X7OAylOTW9Fdjg2NgO4172AJRBLR5VCgbvyC6qpigOcq2D7hAqdSh1j1D5bmL9hdc9NYr5O2KhwzPkOt+AK1zrrRyOl86GlMyOd0aq5UzrXyCq7g7i1x9aupiHojyuzo1WWCmDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhbxiG20",
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "message": {
        "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "message": {
        "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
  "id": -576460752303423245,
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
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423245,
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "state": "tx_+QENCwH4hLhAPfCqbE9iAkjDqS/dptexOaWDmlKoSIab/QlqzR6X7OAylOTW9Fdjg2NgO4172AJRBLR5VCgbvyC6qpigOcq2D7hAqdSh1j1D5bmL9hdc9NYr5O2KhwzPkOt+AK1zrrRyOl86GlMyOd0aq5UzrXyCq7g7i1x9aupiHojyuzo1WWCmDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhbxiG20"
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "state": "tx_+QENCwH4hLhAPfCqbE9iAkjDqS/dptexOaWDmlKoSIab/QlqzR6X7OAylOTW9Fdjg2NgO4172AJRBLR5VCgbvyC6qpigOcq2D7hAqdSh1j1D5bmL9hdc9NYr5O2KhwzPkOt+AK1zrrRyOl86GlMyOd0aq5UzrXyCq7g7i1x9aupiHojyuzo1WWCmDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhbxiG20"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "state": "tx_+QENCwH4hLhAPfCqbE9iAkjDqS/dptexOaWDmlKoSIab/QlqzR6X7OAylOTW9Fdjg2NgO4172AJRBLR5VCgbvyC6qpigOcq2D7hAqdSh1j1D5bmL9hdc9NYr5O2KhwzPkOt+AK1zrrRyOl86GlMyOd0aq5UzrXyCq7g7i1x9aupiHojyuzo1WWCmDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhbxiG20"
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "state": "tx_+QENCwH4hLhAPfCqbE9iAkjDqS/dptexOaWDmlKoSIab/QlqzR6X7OAylOTW9Fdjg2NgO4172AJRBLR5VCgbvyC6qpigOcq2D7hAqdSh1j1D5bmL9hdc9NYr5O2KhwzPkOt+AK1zrrRyOl86GlMyOd0aq5UzrXyCq7g7i1x9aupiHojyuzo1WWCmDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhbxiG20"
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAPfCqbE9iAkjDqS%2FdptexOaWDmlKoSIab%2FQlqzR6X7OAylOTW9Fdjg2NgO4172AJRBLR5VCgbvyC6qpigOcq2D7hAqdSh1j1D5bmL9hdc9NYr5O2KhwzPkOt%2BAK1zrrRyOl86GlMyOd0aq5UzrXyCq7g7i1x9aupiHojyuzo1WWCmDriD%2BIEyAaEBZK4OCGLe00s6e%2B4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk%2Fwgc02xPFpin8ZqQbLoxNebwyc6eA%2BR5uowuCfW4RhbxiG20&port=13180&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 2000,
        "message": "Missing field: existing_fsm_id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAPfCqbE9iAkjDqS%2FdptexOaWDmlKoSIab%2FQlqzR6X7OAylOTW9Fdjg2NgO4172AJRBLR5VCgbvyC6qpigOcq2D7hAqdSh1j1D5bmL9hdc9NYr5O2KhwzPkOt%2BAK1zrrRyOl86GlMyOd0aq5UzrXyCq7g7i1x9aupiHojyuzo1WWCmDriD%2BIEyAaEBZK4OCGLe00s6e%2B4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk%2Fwgc02xPFpin8ZqQbLoxNebwyc6eA%2BR5uowuCfW4RhbxiG20&port=13180&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 2000,
        "message": "Missing field: existing_fsm_id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J&existing_fsm_id=Invalid&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAPfCqbE9iAkjDqS%2FdptexOaWDmlKoSIab%2FQlqzR6X7OAylOTW9Fdjg2NgO4172AJRBLR5VCgbvyC6qpigOcq2D7hAqdSh1j1D5bmL9hdc9NYr5O2KhwzPkOt%2BAK1zrrRyOl86GlMyOd0aq5UzrXyCq7g7i1x9aupiHojyuzo1WWCmDriD%2BIEyAaEBZK4OCGLe00s6e%2B4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk%2Fwgc02xPFpin8ZqQbLoxNebwyc6eA%2BR5uowuCfW4RhbxiG20&port=13180&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J&existing_fsm_id=Invalid&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAPfCqbE9iAkjDqS%2FdptexOaWDmlKoSIab%2FQlqzR6X7OAylOTW9Fdjg2NgO4172AJRBLR5VCgbvyC6qpigOcq2D7hAqdSh1j1D5bmL9hdc9NYr5O2KhwzPkOt%2BAK1zrrRyOl86GlMyOd0aq5UzrXyCq7g7i1x9aupiHojyuzo1WWCmDriD%2BIEyAaEBZK4OCGLe00s6e%2B4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk%2Fwgc02xPFpin8ZqQbLoxNebwyc6eA%2BR5uowuCfW4RhbxiG20&port=13180&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J&existing_fsm_id=ba_mxL2EaGUtQeBBqAm&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAPfCqbE9iAkjDqS%2FdptexOaWDmlKoSIab%2FQlqzR6X7OAylOTW9Fdjg2NgO4172AJRBLR5VCgbvyC6qpigOcq2D7hAqdSh1j1D5bmL9hdc9NYr5O2KhwzPkOt%2BAK1zrrRyOl86GlMyOd0aq5UzrXyCq7g7i1x9aupiHojyuzo1WWCmDriD%2BIEyAaEBZK4OCGLe00s6e%2B4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk%2Fwgc02xPFpin8ZqQbLoxNebwyc6eA%2BR5uowuCfW4RhbxiG20&port=13180&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J&existing_fsm_id=ba_mxL2EaGUtQeBBqAm&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAPfCqbE9iAkjDqS%2FdptexOaWDmlKoSIab%2FQlqzR6X7OAylOTW9Fdjg2NgO4172AJRBLR5VCgbvyC6qpigOcq2D7hAqdSh1j1D5bmL9hdc9NYr5O2KhwzPkOt%2BAK1zrrRyOl86GlMyOd0aq5UzrXyCq7g7i1x9aupiHojyuzo1WWCmDriD%2BIEyAaEBZK4OCGLe00s6e%2B4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk%2Fwgc02xPFpin8ZqQbLoxNebwyc6eA%2BR5uowuCfW4RhbxiG20&port=13180&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J&existing_fsm_id=ba_TE%2Bf9hkgwpXxIa%2F%2BB2%2BwoNy9ZeGtnDaeXxB2cMQ03BCGNCm0&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAPfCqbE9iAkjDqS%2FdptexOaWDmlKoSIab%2FQlqzR6X7OAylOTW9Fdjg2NgO4172AJRBLR5VCgbvyC6qpigOcq2D7hAqdSh1j1D5bmL9hdc9NYr5O2KhwzPkOt%2BAK1zrrRyOl86GlMyOd0aq5UzrXyCq7g7i1x9aupiHojyuzo1WWCmDriD%2BIEyAaEBZK4OCGLe00s6e%2B4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk%2Fwgc02xPFpin8ZqQbLoxNebwyc6eA%2BR5uowuCfW4RhbxiG20&port=13180&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J&existing_fsm_id=ba_TE%2Bf9hkgwpXxIa%2F%2BB2%2BwoNy9ZeGtnDaeXxB2cMQ03BCGNCm0&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAPfCqbE9iAkjDqS%2FdptexOaWDmlKoSIab%2FQlqzR6X7OAylOTW9Fdjg2NgO4172AJRBLR5VCgbvyC6qpigOcq2D7hAqdSh1j1D5bmL9hdc9NYr5O2KhwzPkOt%2BAK1zrrRyOl86GlMyOd0aq5UzrXyCq7g7i1x9aupiHojyuzo1WWCmDriD%2BIEyAaEBZK4OCGLe00s6e%2B4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk%2Fwgc02xPFpin8ZqQbLoxNebwyc6eA%2BR5uowuCfW4RhbxiG20&port=13180&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J&existing_fsm_id=ba_HgXsuteXOQAPf0muqgUWID83wZiCAhgCV%2BsP797by%2Bh2UuJp&offchain_tx=tx_%2BQENCwH4hLhAPfCqbE9iAkjDqS%2FdptexOaWDmlKoSIab%2FQlqzR6X7OAylOTW9Fdjg2NgO4172AJRBLR5VCgbvyC6qpigOcq2D7hAqdSh1j1D5bmL9hdc9NYr5O2KhwzPkOt%2BAK1zrrRyOl86GlMyOd0aq5UzrXyCq7g7i1x9aupiHojyuzo1WWCmDriD%2BIEyAaEBZK4OCGLe00s6e%2B4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk%2Fwgc02xPFpin8ZqQbLoxNebwyc6eA%2BR5uowuCfW4RhbxiG20&port=13180&protocol=json-rpc&role=responder
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
      "fsm_id": "ba_p/nQKuPmDqkx3DZ3XW7kfvRgidMsxnONoYwwEHKF1bkvjkst"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J&existing_fsm_id=ba_D1nnPHG7qqEXDDP6vufkgfstr8spC%2BQ8wSi1ql2okw%2Bg%2FVc5&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAPfCqbE9iAkjDqS%2FdptexOaWDmlKoSIab%2FQlqzR6X7OAylOTW9Fdjg2NgO4172AJRBLR5VCgbvyC6qpigOcq2D7hAqdSh1j1D5bmL9hdc9NYr5O2KhwzPkOt%2BAK1zrrRyOl86GlMyOd0aq5UzrXyCq7g7i1x9aupiHojyuzo1WWCmDriD%2BIEyAaEBZK4OCGLe00s6e%2B4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk%2Fwgc02xPFpin8ZqQbLoxNebwyc6eA%2BR5uowuCfW4RhbxiG20&port=13180&protocol=json-rpc&role=initiator
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
      "fsm_id": "ba_I9yadBldtdnE7EoGDBx8LVRmb9jPI51xPd9V0+mhGSjLomJh"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "event": "channel_reestablished"
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "state": "tx_+QENCwH4hLhAPfCqbE9iAkjDqS/dptexOaWDmlKoSIab/QlqzR6X7OAylOTW9Fdjg2NgO4172AJRBLR5VCgbvyC6qpigOcq2D7hAqdSh1j1D5bmL9hdc9NYr5O2KhwzPkOt+AK1zrrRyOl86GlMyOd0aq5UzrXyCq7g7i1x9aupiHojyuzo1WWCmDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhbxiG20"
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "event": "channel_reestablished"
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "state": "tx_+QENCwH4hLhAPfCqbE9iAkjDqS/dptexOaWDmlKoSIab/QlqzR6X7OAylOTW9Fdjg2NgO4172AJRBLR5VCgbvyC6qpigOcq2D7hAqdSh1j1D5bmL9hdc9NYr5O2KhwzPkOt+AK1zrrRyOl86GlMyOd0aq5UzrXyCq7g7i1x9aupiHojyuzo1WWCmDriD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RhbxiG20"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423244,
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
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423244,
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
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqByeRO7bTntX3j+iWqiKK0+AQrjEV4YEowsHWT0QvRaAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyuavQkk=",
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
  "id": -576460752303423243,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBMRKlQQV77AmCPL6o4qFLvBhPBubX9pwCORj3to/wgLS1fjYf4Z0W8d/8Pp5E7oidFP7P/Uaf2kzIGxuEMNUsHuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsofuNuk"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423243,
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBMRKlQQV77AmCPL6o4qFLvBhPBubX9pwCORj3to/wgLS1fjYf4Z0W8d/8Pp5E7oidFP7P/Uaf2kzIGxuEMNUsHuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsofuNuk",
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
  "id": -576460752303423242,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBMRKlQQV77AmCPL6o4qFLvBhPBubX9pwCORj3to/wgLS1fjYf4Z0W8d/8Pp5E7oidFP7P/Uaf2kzIGxuEMNUsHuECuJNqdvsOVJG1PBADUasK5vAg9zGu3ZOT54nht2eVyZ1VGrIIox+kW84/6HfRyujXOO2xIyhCRabQ9O1Z8gU0AuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoE9JJj"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423242,
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "state": "tx_+NILAfiEuEBMRKlQQV77AmCPL6o4qFLvBhPBubX9pwCORj3to/wgLS1fjYf4Z0W8d/8Pp5E7oidFP7P/Uaf2kzIGxuEMNUsHuECuJNqdvsOVJG1PBADUasK5vAg9zGu3ZOT54nht2eVyZ1VGrIIox+kW84/6HfRyujXOO2xIyhCRabQ9O1Z8gU0AuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoE9JJj"
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "state": "tx_+NILAfiEuEBMRKlQQV77AmCPL6o4qFLvBhPBubX9pwCORj3to/wgLS1fjYf4Z0W8d/8Pp5E7oidFP7P/Uaf2kzIGxuEMNUsHuECuJNqdvsOVJG1PBADUasK5vAg9zGu3ZOT54nht2eVyZ1VGrIIox+kW84/6HfRyujXOO2xIyhCRabQ9O1Z8gU0AuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoE9JJj"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423241,
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
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423241,
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
  "id": -576460752303423240,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423240,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBMRKlQQV77AmCPL6o4qFLvBhPBubX9pwCORj3to/wgLS1fjYf4Z0W8d/8Pp5E7oidFP7P/Uaf2kzIGxuEMNUsHuECuJNqdvsOVJG1PBADUasK5vAg9zGu3ZOT54nht2eVyZ1VGrIIox+kW84/6HfRyujXOO2xIyhCRabQ9O1Z8gU0AuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoE9JJj",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423239,
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
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423239,
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
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqByeRO7bTntX3j+iWqiKK0+AQrjEV4YEowsHWT0QvRaA6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmYn5mI=",
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
  "id": -576460752303423238,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBIROvM8vnbKVXB+AiqqM2505jogx9wgF+3gsDGRy7ncaKqy9D0T43KUomZToMfqPpLzdFLrB+Qbw9vvxBPWT8IuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbYW0ij"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423238,
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBIROvM8vnbKVXB+AiqqM2505jogx9wgF+3gsDGRy7ncaKqy9D0T43KUomZToMfqPpLzdFLrB+Qbw9vvxBPWT8IuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbYW0ij",
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
  "id": -576460752303423237,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBIROvM8vnbKVXB+AiqqM2505jogx9wgF+3gsDGRy7ncaKqy9D0T43KUomZToMfqPpLzdFLrB+Qbw9vvxBPWT8IuEDNEozOnzTagiWkpWma71Sett3eD30YLLBFT9VdgIIDKDzndUoNupTO1PN+6sBAjqTdul/U3WJK2cm7QmVJIpsLuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEa85L5f"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423237,
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "state": "tx_+NILAfiEuEBIROvM8vnbKVXB+AiqqM2505jogx9wgF+3gsDGRy7ncaKqy9D0T43KUomZToMfqPpLzdFLrB+Qbw9vvxBPWT8IuEDNEozOnzTagiWkpWma71Sett3eD30YLLBFT9VdgIIDKDzndUoNupTO1PN+6sBAjqTdul/U3WJK2cm7QmVJIpsLuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEa85L5f"
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "state": "tx_+NILAfiEuEBIROvM8vnbKVXB+AiqqM2505jogx9wgF+3gsDGRy7ncaKqy9D0T43KUomZToMfqPpLzdFLrB+Qbw9vvxBPWT8IuEDNEozOnzTagiWkpWma71Sett3eD30YLLBFT9VdgIIDKDzndUoNupTO1PN+6sBAjqTdul/U3WJK2cm7QmVJIpsLuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEa85L5f"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423236,
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
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423236,
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
  "id": -576460752303423235,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423235,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBIROvM8vnbKVXB+AiqqM2505jogx9wgF+3gsDGRy7ncaKqy9D0T43KUomZToMfqPpLzdFLrB+Qbw9vvxBPWT8IuEDNEozOnzTagiWkpWma71Sett3eD30YLLBFT9VdgIIDKDzndUoNupTO1PN+6sBAjqTdul/U3WJK2cm7QmVJIpsLuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEa85L5f",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423234,
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
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423234,
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
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqByeRO7bTntX3j+iWqiKK0+AQrjEV4YEowsHWT0QvRaBKDdqOzEXWz8Y2itvyrEosD88v7VNFxfGdbGSLDDea6BYC52UBg=",
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
  "id": -576460752303423233,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAXZ/MMb/2y8IFCvEmIE/M5dSXGLoCH5BrseID2kypSOiiPiQbcSe/bnn/fdUFzOp1hHK7sPPwwcfWnRIvCt1ILuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAgwoKV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423233,
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAXZ/MMb/2y8IFCvEmIE/M5dSXGLoCH5BrseID2kypSOiiPiQbcSe/bnn/fdUFzOp1hHK7sPPwwcfWnRIvCt1ILuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAgwoKV",
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
  "id": -576460752303423232,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAXZ/MMb/2y8IFCvEmIE/M5dSXGLoCH5BrseID2kypSOiiPiQbcSe/bnn/fdUFzOp1hHK7sPPwwcfWnRIvCt1ILuEDVQPKRzGNhHgsnpScc8SWBheEKVmeC3hL+zj+L3RxtXQNckWmPrOjiVetRmdw2UX5HCmOhjBXiH6jTRp3YC2gHuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCXAWDd"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423232,
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "state": "tx_+NILAfiEuEAXZ/MMb/2y8IFCvEmIE/M5dSXGLoCH5BrseID2kypSOiiPiQbcSe/bnn/fdUFzOp1hHK7sPPwwcfWnRIvCt1ILuEDVQPKRzGNhHgsnpScc8SWBheEKVmeC3hL+zj+L3RxtXQNckWmPrOjiVetRmdw2UX5HCmOhjBXiH6jTRp3YC2gHuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCXAWDd"
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "state": "tx_+NILAfiEuEAXZ/MMb/2y8IFCvEmIE/M5dSXGLoCH5BrseID2kypSOiiPiQbcSe/bnn/fdUFzOp1hHK7sPPwwcfWnRIvCt1ILuEDVQPKRzGNhHgsnpScc8SWBheEKVmeC3hL+zj+L3RxtXQNckWmPrOjiVetRmdw2UX5HCmOhjBXiH6jTRp3YC2gHuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCXAWDd"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423231,
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
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423231,
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
  "id": -576460752303423230,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423230,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAXZ/MMb/2y8IFCvEmIE/M5dSXGLoCH5BrseID2kypSOiiPiQbcSe/bnn/fdUFzOp1hHK7sPPwwcfWnRIvCt1ILuEDVQPKRzGNhHgsnpScc8SWBheEKVmeC3hL+zj+L3RxtXQNckWmPrOjiVetRmdw2UX5HCmOhjBXiH6jTRp3YC2gHuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCXAWDd",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAALDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiYACdCDgG"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423229,
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
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423229,
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
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqByeRO7bTntX3j+iWqiKK0+AQrjEV4YEowsHWT0QvRaBaBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RphvWNY=",
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
  "id": -576460752303423228,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDHB5borAjpMSfYKniz1S/VeJQjUMKltpDGT8nR9Smod0Ib2nMSBbKPnY999MQReD/3Ofg7JZPnN5zHNjxoMwMKuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZ+J9ji"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423228,
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDHB5borAjpMSfYKniz1S/VeJQjUMKltpDGT8nR9Smod0Ib2nMSBbKPnY999MQReD/3Ofg7JZPnN5zHNjxoMwMKuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZ+J9ji",
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
  "id": -576460752303423227,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEC1eb5f+eJMSDrAj/qZ/4zl4fxvdt09HA7h1TOD9rYjqA9gNIS9TaKKUGI5KyeOX8rjueE3fF/3tWToC70SnToPuEDHB5borAjpMSfYKniz1S/VeJQjUMKltpDGT8nR9Smod0Ib2nMSBbKPnY999MQReD/3Ofg7JZPnN5zHNjxoMwMKuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbGSvdn"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423227,
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "state": "tx_+NILAfiEuEC1eb5f+eJMSDrAj/qZ/4zl4fxvdt09HA7h1TOD9rYjqA9gNIS9TaKKUGI5KyeOX8rjueE3fF/3tWToC70SnToPuEDHB5borAjpMSfYKniz1S/VeJQjUMKltpDGT8nR9Smod0Ib2nMSBbKPnY999MQReD/3Ofg7JZPnN5zHNjxoMwMKuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbGSvdn"
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "state": "tx_+NILAfiEuEC1eb5f+eJMSDrAj/qZ/4zl4fxvdt09HA7h1TOD9rYjqA9gNIS9TaKKUGI5KyeOX8rjueE3fF/3tWToC70SnToPuEDHB5borAjpMSfYKniz1S/VeJQjUMKltpDGT8nR9Smod0Ib2nMSBbKPnY999MQReD/3Ofg7JZPnN5zHNjxoMwMKuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbGSvdn"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423226,
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
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423226,
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
  "id": -576460752303423225,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423225,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEC1eb5f+eJMSDrAj/qZ/4zl4fxvdt09HA7h1TOD9rYjqA9gNIS9TaKKUGI5KyeOX8rjueE3fF/3tWToC70SnToPuEDHB5borAjpMSfYKniz1S/VeJQjUMKltpDGT8nR9Smod0Ib2nMSBbKPnY999MQReD/3Ofg7JZPnN5zHNjxoMwMKuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0WgWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbGSvdn",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423224,
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
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423224,
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
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqByeRO7bTntX3j+iWqiKK0+AQrjEV4YEowsHWT0QvRaBqDdqOzEXWz8Y2itvyrEosD88v7VNFxfGdbGSLDDea6BYNvZnj4=",
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
  "id": -576460752303423223,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDV9XtM+wqb5pFWeqC6G5g4iZGvkQ80/gTBsXX2QDDRM/7R8zEB4/sHFvBsDU3CdBDhGMREVhNIUCMCorqFQAYAuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0Wgag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCqvA36"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423223,
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDV9XtM+wqb5pFWeqC6G5g4iZGvkQ80/gTBsXX2QDDRM/7R8zEB4/sHFvBsDU3CdBDhGMREVhNIUCMCorqFQAYAuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0Wgag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCqvA36",
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
  "id": -576460752303423222,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA7bUGaaGlsK+gBL0LxuRtFWJekcA/NsJCmeoCe/hA7paZqoo7dFBgFQKpEDxb63dUNlLPPkhxKmtHgPBXdx9QOuEDV9XtM+wqb5pFWeqC6G5g4iZGvkQ80/gTBsXX2QDDRM/7R8zEB4/sHFvBsDU3CdBDhGMREVhNIUCMCorqFQAYAuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0Wgag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWDfZWYK"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423222,
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "state": "tx_+NILAfiEuEA7bUGaaGlsK+gBL0LxuRtFWJekcA/NsJCmeoCe/hA7paZqoo7dFBgFQKpEDxb63dUNlLPPkhxKmtHgPBXdx9QOuEDV9XtM+wqb5pFWeqC6G5g4iZGvkQ80/gTBsXX2QDDRM/7R8zEB4/sHFvBsDU3CdBDhGMREVhNIUCMCorqFQAYAuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0Wgag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWDfZWYK"
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "state": "tx_+NILAfiEuEA7bUGaaGlsK+gBL0LxuRtFWJekcA/NsJCmeoCe/hA7paZqoo7dFBgFQKpEDxb63dUNlLPPkhxKmtHgPBXdx9QOuEDV9XtM+wqb5pFWeqC6G5g4iZGvkQ80/gTBsXX2QDDRM/7R8zEB4/sHFvBsDU3CdBDhGMREVhNIUCMCorqFQAYAuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0Wgag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWDfZWYK"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423221,
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
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423221,
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
  "id": -576460752303423220,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423220,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA7bUGaaGlsK+gBL0LxuRtFWJekcA/NsJCmeoCe/hA7paZqoo7dFBgFQKpEDxb63dUNlLPPkhxKmtHgPBXdx9QOuEDV9XtM+wqb5pFWeqC6G5g4iZGvkQ80/gTBsXX2QDDRM/7R8zEB4/sHFvBsDU3CdBDhGMREVhNIUCMCorqFQAYAuEj4RjkCoQagcnkTu2057V94/olqoiitPgEK4xFeGBKMLB1k9EL0Wgag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWDfZWYK",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAALDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiYACdCDgG"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423219,
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
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423219,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423218,
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
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
  "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
  "id": -576460752303423218,
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
    "channel_id": "ch_2DfQdMeHhZBdN8BDR5B3cB7LNCNFUkFD2LkCuy21QLe7BEbB1J",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection
