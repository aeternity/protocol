
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&minimum_depth=1&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_min_depth_not_reached_timeout_%2F2870&timeout_funding_lock=3000
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
      "fsm_id": "ba_DdmQP8dGz2kQx6GUcUq/ikibEtkzriRQp3yCU/+QmWxZIzIW"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&minimum_depth=1&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_min_depth_not_reached_timeout_%2F2870&timeout_funding_lock=3000
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
      "fsm_id": "ba_WWp6dpboeCTaNZsVNDuHfMLdXdoB3T58NJFM+9+tHlBG5RDU"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYBwT3bAA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423488,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDvCYtYBDgU+h6LGMpJ9BgIeszpb6F5DbNoAYYCy25lOfTLKhOcmYlZokOgWnYVmKFnfEYP3rtV0LUwxbw7+xsNuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGAULTqGg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423488,
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
    "channel_id": "ch_2AdbZ9KZBSm8jvYnArnniheCgVbudAYP4dEGC6xSPYQdkNXma4",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_WWp6dpboeCTaNZsVNDuHfMLdXdoB3T58NJFM+9+tHlBG5RDU"
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
    "channel_id": "ch_2AdbZ9KZBSm8jvYnArnniheCgVbudAYP4dEGC6xSPYQdkNXma4",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEDvCYtYBDgU+h6LGMpJ9BgIeszpb6F5DbNoAYYCy25lOfTLKhOcmYlZokOgWnYVmKFnfEYP3rtV0LUwxbw7+xsNuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGAULTqGg=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423487,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAIs7znpS3INPHUl/sFPTIptSS1C/XXgtOS8a6Ee6CQLwnZYYIC6bgGiAMgrLfnzETZCkqNrkE4Ysiz7s433jlA7hA7wmLWAQ4FPoeixjKSfQYCHrM6W+heQ2zaAGGAstuZTn0yyoTnJmJWaJDoFp2FZihZ3xGD967VdC1MMW8O/sbDbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgG4kcIK"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2AdbZ9KZBSm8jvYnArnniheCgVbudAYP4dEGC6xSPYQdkNXma4",
  "id": -576460752303423487,
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
    "channel_id": "ch_2AdbZ9KZBSm8jvYnArnniheCgVbudAYP4dEGC6xSPYQdkNXma4",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAIs7znpS3INPHUl/sFPTIptSS1C/XXgtOS8a6Ee6CQLwnZYYIC6bgGiAMgrLfnzETZCkqNrkE4Ysiz7s433jlA7hA7wmLWAQ4FPoeixjKSfQYCHrM6W+heQ2zaAGGAstuZTn0yyoTnJmJWaJDoFp2FZihZ3xGD967VdC1MMW8O/sbDbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgG4kcIK",
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
    "channel_id": "ch_2AdbZ9KZBSm8jvYnArnniheCgVbudAYP4dEGC6xSPYQdkNXma4",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_DdmQP8dGz2kQx6GUcUq/ikibEtkzriRQp3yCU/+QmWxZIzIW"
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
    "channel_id": "ch_2AdbZ9KZBSm8jvYnArnniheCgVbudAYP4dEGC6xSPYQdkNXma4",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAIs7znpS3INPHUl/sFPTIptSS1C/XXgtOS8a6Ee6CQLwnZYYIC6bgGiAMgrLfnzETZCkqNrkE4Ysiz7s433jlA7hA7wmLWAQ4FPoeixjKSfQYCHrM6W+heQ2zaAGGAstuZTn0yyoTnJmJWaJDoFp2FZihZ3xGD967VdC1MMW8O/sbDbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgG4kcIK",
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
    "channel_id": "ch_2AdbZ9KZBSm8jvYnArnniheCgVbudAYP4dEGC6xSPYQdkNXma4",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAIs7znpS3INPHUl/sFPTIptSS1C/XXgtOS8a6Ee6CQLwnZYYIC6bgGiAMgrLfnzETZCkqNrkE4Ysiz7s433jlA7hA7wmLWAQ4FPoeixjKSfQYCHrM6W+heQ2zaAGGAstuZTn0yyoTnJmJWaJDoFp2FZihZ3xGD967VdC1MMW8O/sbDbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgG4kcIK",
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
    "channel_id": "ch_2AdbZ9KZBSm8jvYnArnniheCgVbudAYP4dEGC6xSPYQdkNXma4",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAIs7znpS3INPHUl/sFPTIptSS1C/XXgtOS8a6Ee6CQLwnZYYIC6bgGiAMgrLfnzETZCkqNrkE4Ysiz7s433jlA7hA7wmLWAQ4FPoeixjKSfQYCHrM6W+heQ2zaAGGAstuZTn0yyoTnJmJWaJDoFp2FZihZ3xGD967VdC1MMW8O/sbDbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgG4kcIK",
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
    "channel_id": "ch_2AdbZ9KZBSm8jvYnArnniheCgVbudAYP4dEGC6xSPYQdkNXma4",
    "data": {
      "event": "timeout"
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
    "channel_id": "ch_2AdbZ9KZBSm8jvYnArnniheCgVbudAYP4dEGC6xSPYQdkNXma4",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2AdbZ9KZBSm8jvYnArnniheCgVbudAYP4dEGC6xSPYQdkNXma4",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection
