
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
      "fsm_id": "ba_Rjbrc6t11SkSl+PtLsKLCzng737vp2IkgSPIX1h6nzCsmtkZ"
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
      "fsm_id": "ba_cKKQX2HSEx1bk6gBavDsp/b6lnWri3c0bujq+OeTbF8dwMHK"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY0MbMHjQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422828,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEA6Ng8oZgmfxrss/Rv0fncwPSl5yXVNGMlwnZ41+hjnwbY1LnHqG7/RueMLUdCmpaVuaO0vjkbG0Zdb1vyh40INuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGNIfvCgI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422828,
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_cKKQX2HSEx1bk6gBavDsp/b6lnWri3c0bujq+OeTbF8dwMHK"
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEA6Ng8oZgmfxrss/Rv0fncwPSl5yXVNGMlwnZ41+hjnwbY1LnHqG7/RueMLUdCmpaVuaO0vjkbG0Zdb1vyh40INuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGNIfvCgI=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422827,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAOjYPKGYJn8a7LP0b9H53MD0pecl1TRjJcJ2eNfoY58G2NS5x6hu/0bnjC1HQpqWlbmjtL45GxtGXW9b8oeNCDbhAqCD/JBvvfBotcBM9NGvVTwunJuRq1E2Kgc2l5Xpr/M+ixHCu+x7CovVn22M769nbVBAD8Qej/YNRyZT+UFZSCbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjTvdn9d"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422827,
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAOjYPKGYJn8a7LP0b9H53MD0pecl1TRjJcJ2eNfoY58G2NS5x6hu/0bnjC1HQpqWlbmjtL45GxtGXW9b8oeNCDbhAqCD/JBvvfBotcBM9NGvVTwunJuRq1E2Kgc2l5Xpr/M+ixHCu+x7CovVn22M769nbVBAD8Qej/YNRyZT+UFZSCbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjTvdn9d",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_Rjbrc6t11SkSl+PtLsKLCzng737vp2IkgSPIX1h6nzCsmtkZ"
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAOjYPKGYJn8a7LP0b9H53MD0pecl1TRjJcJ2eNfoY58G2NS5x6hu/0bnjC1HQpqWlbmjtL45GxtGXW9b8oeNCDbhAqCD/JBvvfBotcBM9NGvVTwunJuRq1E2Kgc2l5Xpr/M+ixHCu+x7CovVn22M769nbVBAD8Qej/YNRyZT+UFZSCbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjTvdn9d",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAOjYPKGYJn8a7LP0b9H53MD0pecl1TRjJcJ2eNfoY58G2NS5x6hu/0bnjC1HQpqWlbmjtL45GxtGXW9b8oeNCDbhAqCD/JBvvfBotcBM9NGvVTwunJuRq1E2Kgc2l5Xpr/M+ixHCu+x7CovVn22M769nbVBAD8Qej/YNRyZT+UFZSCbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjTvdn9d",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAOjYPKGYJn8a7LP0b9H53MD0pecl1TRjJcJ2eNfoY58G2NS5x6hu/0bnjC1HQpqWlbmjtL45GxtGXW9b8oeNCDbhAqCD/JBvvfBotcBM9NGvVTwunJuRq1E2Kgc2l5Xpr/M+ixHCu+x7CovVn22M769nbVBAD8Qej/YNRyZT+UFZSCbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjTvdn9d",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "message": {
        "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "message": {
        "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
  "id": -576460752303422826,
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422826,
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "state": "tx_+QENCwH4hLhAOjYPKGYJn8a7LP0b9H53MD0pecl1TRjJcJ2eNfoY58G2NS5x6hu/0bnjC1HQpqWlbmjtL45GxtGXW9b8oeNCDbhAqCD/JBvvfBotcBM9NGvVTwunJuRq1E2Kgc2l5Xpr/M+ixHCu+x7CovVn22M769nbVBAD8Qej/YNRyZT+UFZSCbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjTvdn9d"
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "state": "tx_+QENCwH4hLhAOjYPKGYJn8a7LP0b9H53MD0pecl1TRjJcJ2eNfoY58G2NS5x6hu/0bnjC1HQpqWlbmjtL45GxtGXW9b8oeNCDbhAqCD/JBvvfBotcBM9NGvVTwunJuRq1E2Kgc2l5Xpr/M+ixHCu+x7CovVn22M769nbVBAD8Qej/YNRyZT+UFZSCbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RjTvdn9d"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422825,
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422825,
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpDUBO+a/RgR6K6WW8RXHQ34o4ijMezrRfbiY/TlTFODAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyv6QTag=",
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
  "id": -576460752303422824,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC/Di81o5qwmxfholGepxbLkxEL1a5ZCor4NNMvU85KPtGP/RAn6uYPycIC3QQ4LREp/qZ+Ehyt3C5NhN1PBtsKuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsr4YZvg"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422824,
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC/Di81o5qwmxfholGepxbLkxEL1a5ZCor4NNMvU85KPtGP/RAn6uYPycIC3QQ4LREp/qZ+Ehyt3C5NhN1PBtsKuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsr4YZvg",
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
  "id": -576460752303422823,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBSgioS2N3HvrclWxtL7OqfEhqM18hJDyOfZsb8MWovkjMQJ5VQRQ8odeggEJEf+wUa37qkweQJCS6OFyqHWXoNuEC/Di81o5qwmxfholGepxbLkxEL1a5ZCor4NNMvU85KPtGP/RAn6uYPycIC3QQ4LREp/qZ+Ehyt3C5NhN1PBtsKuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspeEizv"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422823,
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "state": "tx_+NILAfiEuEBSgioS2N3HvrclWxtL7OqfEhqM18hJDyOfZsb8MWovkjMQJ5VQRQ8odeggEJEf+wUa37qkweQJCS6OFyqHWXoNuEC/Di81o5qwmxfholGepxbLkxEL1a5ZCor4NNMvU85KPtGP/RAn6uYPycIC3QQ4LREp/qZ+Ehyt3C5NhN1PBtsKuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspeEizv"
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "state": "tx_+NILAfiEuEBSgioS2N3HvrclWxtL7OqfEhqM18hJDyOfZsb8MWovkjMQJ5VQRQ8odeggEJEf+wUa37qkweQJCS6OFyqHWXoNuEC/Di81o5qwmxfholGepxbLkxEL1a5ZCor4NNMvU85KPtGP/RAn6uYPycIC3QQ4LREp/qZ+Ehyt3C5NhN1PBtsKuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspeEizv"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422822,
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422822,
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
  "id": -576460752303422821,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422821,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBSgioS2N3HvrclWxtL7OqfEhqM18hJDyOfZsb8MWovkjMQJ5VQRQ8odeggEJEf+wUa37qkweQJCS6OFyqHWXoNuEC/Di81o5qwmxfholGepxbLkxEL1a5ZCor4NNMvU85KPtGP/RAn6uYPycIC3QQ4LREp/qZ+Ehyt3C5NhN1PBtsKuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspeEizv",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422820,
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422820,
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpDUBO+a/RgR6K6WW8RXHQ34o4ijMezrRfbiY/TlTFODA6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rr9frlc=",
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
  "id": -576460752303422819,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA6XNvpq3BGnXC9lDMzXw520M78X4/dsz1aohciuKmy1YDEU6JCKxhsanMbVIITUBqluOQQG97n6jKo9qLm2rMAuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZkbem2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422819,
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA6XNvpq3BGnXC9lDMzXw520M78X4/dsz1aohciuKmy1YDEU6JCKxhsanMbVIITUBqluOQQG97n6jKo9qLm2rMAuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZkbem2",
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
  "id": -576460752303422818,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAvOdvfLnyBHJVA0MQa8hUPewTIhFqVdjC+XIkwmpxizdZA8ykl+mnhyvr3BxdtGv11MmpTJeG0/CuItmfFpF4HuEA6XNvpq3BGnXC9lDMzXw520M78X4/dsz1aohciuKmy1YDEU6JCKxhsanMbVIITUBqluOQQG97n6jKo9qLm2rMAuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY4fEac"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422818,
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "state": "tx_+NILAfiEuEAvOdvfLnyBHJVA0MQa8hUPewTIhFqVdjC+XIkwmpxizdZA8ykl+mnhyvr3BxdtGv11MmpTJeG0/CuItmfFpF4HuEA6XNvpq3BGnXC9lDMzXw520M78X4/dsz1aohciuKmy1YDEU6JCKxhsanMbVIITUBqluOQQG97n6jKo9qLm2rMAuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY4fEac"
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "state": "tx_+NILAfiEuEAvOdvfLnyBHJVA0MQa8hUPewTIhFqVdjC+XIkwmpxizdZA8ykl+mnhyvr3BxdtGv11MmpTJeG0/CuItmfFpF4HuEA6XNvpq3BGnXC9lDMzXw520M78X4/dsz1aohciuKmy1YDEU6JCKxhsanMbVIITUBqluOQQG97n6jKo9qLm2rMAuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY4fEac"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422817,
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422817,
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
  "id": -576460752303422816,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422816,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAvOdvfLnyBHJVA0MQa8hUPewTIhFqVdjC+XIkwmpxizdZA8ykl+mnhyvr3BxdtGv11MmpTJeG0/CuItmfFpF4HuEA6XNvpq3BGnXC9lDMzXw520M78X4/dsz1aohciuKmy1YDEU6JCKxhsanMbVIITUBqluOQQG97n6jKo9qLm2rMAuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEY4fEac",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422815,
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422815,
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpDUBO+a/RgR6K6WW8RXHQ34o4ijMezrRfbiY/TlTFODBKDdqOzEXWz8Y2itvyrEosD88v7VNFxfGdbGSLDDea6BYJjP2jY=",
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
  "id": -576460752303422814,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBi3szYG/5HlA2W5JNfwUWQHlflr2UlOHLZjyQBCK+M923cxbATEnhh2Bkwe/W70U/CBxDfE8KSgZKvMyW0mukBuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAtpZ1x"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422814,
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBi3szYG/5HlA2W5JNfwUWQHlflr2UlOHLZjyQBCK+M923cxbATEnhh2Bkwe/W70U/CBxDfE8KSgZKvMyW0mukBuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAtpZ1x",
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
  "id": -576460752303422813,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAERvUtfROwIS4poS3822JPkq0P5L/j73wCThVPWqrEiBNdR612yW5Sk5i7ZIGiI343EFXWLGfWbd6vTbFr5E4IuEBi3szYG/5HlA2W5JNfwUWQHlflr2UlOHLZjyQBCK+M923cxbATEnhh2Bkwe/W70U/CBxDfE8KSgZKvMyW0mukBuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAdMb2k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422813,
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "state": "tx_+NILAfiEuEAERvUtfROwIS4poS3822JPkq0P5L/j73wCThVPWqrEiBNdR612yW5Sk5i7ZIGiI343EFXWLGfWbd6vTbFr5E4IuEBi3szYG/5HlA2W5JNfwUWQHlflr2UlOHLZjyQBCK+M923cxbATEnhh2Bkwe/W70U/CBxDfE8KSgZKvMyW0mukBuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAdMb2k"
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "state": "tx_+NILAfiEuEAERvUtfROwIS4poS3822JPkq0P5L/j73wCThVPWqrEiBNdR612yW5Sk5i7ZIGiI343EFXWLGfWbd6vTbFr5E4IuEBi3szYG/5HlA2W5JNfwUWQHlflr2UlOHLZjyQBCK+M923cxbATEnhh2Bkwe/W70U/CBxDfE8KSgZKvMyW0mukBuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAdMb2k"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422812,
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422812,
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
  "id": -576460752303422811,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422811,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAERvUtfROwIS4poS3822JPkq0P5L/j73wCThVPWqrEiBNdR612yW5Sk5i7ZIGiI343EFXWLGfWbd6vTbFr5E4IuEBi3szYG/5HlA2W5JNfwUWQHlflr2UlOHLZjyQBCK+M923cxbATEnhh2Bkwe/W70U/CBxDfE8KSgZKvMyW0mukBuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAdMb2k",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAALDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiYACdCDgG"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422810,
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422810,
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpDUBO+a/RgR6K6WW8RXHQ34o4ijMezrRfbiY/TlTFODBaBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkB2tl4=",
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
  "id": -576460752303422809,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECQwqthp2U61hl1HzMtUyfy2S86+xdNZukdygwPbf+Et+isCFpag2J4w6DOR6oiCBx1SDp3Q08sD3pDcVTHz9wFuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaGi02J"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422809,
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "signed_tx": "tx_+JALAfhCuECQwqthp2U61hl1HzMtUyfy2S86+xdNZukdygwPbf+Et+isCFpag2J4w6DOR6oiCBx1SDp3Q08sD3pDcVTHz9wFuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaGi02J",
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
  "id": -576460752303422808,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAkemrUStyd8Bxifeq0/U3JVV1NXCZChbf2j1Noep7XtF2vnCLahLbK4JPJM+mnxatdTlgAjkQYjRx3MzpTH/wMuECQwqthp2U61hl1HzMtUyfy2S86+xdNZukdygwPbf+Et+isCFpag2J4w6DOR6oiCBx1SDp3Q08sD3pDcVTHz9wFuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZSNKeP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422808,
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "state": "tx_+NILAfiEuEAkemrUStyd8Bxifeq0/U3JVV1NXCZChbf2j1Noep7XtF2vnCLahLbK4JPJM+mnxatdTlgAjkQYjRx3MzpTH/wMuECQwqthp2U61hl1HzMtUyfy2S86+xdNZukdygwPbf+Et+isCFpag2J4w6DOR6oiCBx1SDp3Q08sD3pDcVTHz9wFuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZSNKeP"
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "state": "tx_+NILAfiEuEAkemrUStyd8Bxifeq0/U3JVV1NXCZChbf2j1Noep7XtF2vnCLahLbK4JPJM+mnxatdTlgAjkQYjRx3MzpTH/wMuECQwqthp2U61hl1HzMtUyfy2S86+xdNZukdygwPbf+Et+isCFpag2J4w6DOR6oiCBx1SDp3Q08sD3pDcVTHz9wFuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZSNKeP"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422807,
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422807,
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
  "id": -576460752303422806,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422806,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAkemrUStyd8Bxifeq0/U3JVV1NXCZChbf2j1Noep7XtF2vnCLahLbK4JPJM+mnxatdTlgAjkQYjRx3MzpTH/wMuECQwqthp2U61hl1HzMtUyfy2S86+xdNZukdygwPbf+Et+isCFpag2J4w6DOR6oiCBx1SDp3Q08sD3pDcVTHz9wFuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwWgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZSNKeP",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422805,
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422805,
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpDUBO+a/RgR6K6WW8RXHQ34o4ijMezrRfbiY/TlTFODBqDdqOzEXWz8Y2itvyrEosD88v7VNFxfGdbGSLDDea6BYGf/QjY=",
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
  "id": -576460752303422804,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECQ0SdqmbqVV4feL4eJyYrn7/AO/5K6Ek5lSoptR3O7jporA4GroNHfNLa5BKaFhzY/VZv/w/3/LIMYRGINh78LuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBRlVmU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422804,
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "signed_tx": "tx_+JALAfhCuECQ0SdqmbqVV4feL4eJyYrn7/AO/5K6Ek5lSoptR3O7jporA4GroNHfNLa5BKaFhzY/VZv/w/3/LIMYRGINh78LuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBRlVmU",
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
  "id": -576460752303422803,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAQli6NsyVYt5cZOyTdgqDqfswYOsajD1zeJoi4JodOIfcJdLa8E5BF+HlPBp/izQQiaT0M5J4TsyMkoV9i6gAAuECQ0SdqmbqVV4feL4eJyYrn7/AO/5K6Ek5lSoptR3O7jporA4GroNHfNLa5BKaFhzY/VZv/w/3/LIMYRGINh78LuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCOEnTR"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422803,
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "state": "tx_+NILAfiEuEAQli6NsyVYt5cZOyTdgqDqfswYOsajD1zeJoi4JodOIfcJdLa8E5BF+HlPBp/izQQiaT0M5J4TsyMkoV9i6gAAuECQ0SdqmbqVV4feL4eJyYrn7/AO/5K6Ek5lSoptR3O7jporA4GroNHfNLa5BKaFhzY/VZv/w/3/LIMYRGINh78LuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCOEnTR"
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "state": "tx_+NILAfiEuEAQli6NsyVYt5cZOyTdgqDqfswYOsajD1zeJoi4JodOIfcJdLa8E5BF+HlPBp/izQQiaT0M5J4TsyMkoV9i6gAAuECQ0SdqmbqVV4feL4eJyYrn7/AO/5K6Ek5lSoptR3O7jporA4GroNHfNLa5BKaFhzY/VZv/w/3/LIMYRGINh78LuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCOEnTR"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422802,
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422802,
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
  "id": -576460752303422801,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
  "id": -576460752303422801,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAQli6NsyVYt5cZOyTdgqDqfswYOsajD1zeJoi4JodOIfcJdLa8E5BF+HlPBp/izQQiaT0M5J4TsyMkoV9i6gAAuECQ0SdqmbqVV4feL4eJyYrn7/AO/5K6Ek5lSoptR3O7jporA4GroNHfNLa5BKaFhzY/VZv/w/3/LIMYRGINh78LuEj4RjkCoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTgwag3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWCOEnTR",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAALDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiYACdCDgG"
  },
  "version": 1
}
```
