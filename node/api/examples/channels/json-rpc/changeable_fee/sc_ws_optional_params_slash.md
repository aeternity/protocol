
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
      "fsm_id": "ba_Z+If/cFjC/wcYiM050WoJrLvkhk/xQTgjc8WVsONsUrMXEcJ"
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
      "fsm_id": "ba_SkyeVrfZSqL4aFG/QK79oH2Eu+WpRlZV5AcpyCmsvIqbPqve"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZF0q8GfQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422611,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECbvunYvZ4f62eVcJ6WFa1g0w9O9jhZ9VSJHMHUIcA/h1B8t9Sx/OZK4AFzXrQSrJQj9HEukuNIoiWpPnQIgrcHuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGRauT0Uc="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422611,
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_SkyeVrfZSqL4aFG/QK79oH2Eu+WpRlZV5AcpyCmsvIqbPqve"
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "signed_tx": "tx_+MsLAfhCuECbvunYvZ4f62eVcJ6WFa1g0w9O9jhZ9VSJHMHUIcA/h1B8t9Sx/OZK4AFzXrQSrJQj9HEukuNIoiWpPnQIgrcHuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGRauT0Uc=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422610,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAUv5ogGdlj9IQ7mgnsvlWg2J+89GozyMa1TvDcX0fFN58RM5V601mJHR8513CukU3+VSzpXFSdYugpImrTM7jDLhAm77p2L2eH+tnlXCelhWtYNMPTvY4WfVUiRzB1CHAP4dQfLfUsfzmSuABc160EqyUI/RxLpLjSKIlqT50CIK3B7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkWdA5oW"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
  "id": -576460752303422610,
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAUv5ogGdlj9IQ7mgnsvlWg2J+89GozyMa1TvDcX0fFN58RM5V601mJHR8513CukU3+VSzpXFSdYugpImrTM7jDLhAm77p2L2eH+tnlXCelhWtYNMPTvY4WfVUiRzB1CHAP4dQfLfUsfzmSuABc160EqyUI/RxLpLjSKIlqT50CIK3B7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkWdA5oW",
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_Z+If/cFjC/wcYiM050WoJrLvkhk/xQTgjc8WVsONsUrMXEcJ"
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAUv5ogGdlj9IQ7mgnsvlWg2J+89GozyMa1TvDcX0fFN58RM5V601mJHR8513CukU3+VSzpXFSdYugpImrTM7jDLhAm77p2L2eH+tnlXCelhWtYNMPTvY4WfVUiRzB1CHAP4dQfLfUsfzmSuABc160EqyUI/RxLpLjSKIlqT50CIK3B7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkWdA5oW",
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAUv5ogGdlj9IQ7mgnsvlWg2J+89GozyMa1TvDcX0fFN58RM5V601mJHR8513CukU3+VSzpXFSdYugpImrTM7jDLhAm77p2L2eH+tnlXCelhWtYNMPTvY4WfVUiRzB1CHAP4dQfLfUsfzmSuABc160EqyUI/RxLpLjSKIlqT50CIK3B7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkWdA5oW",
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAUv5ogGdlj9IQ7mgnsvlWg2J+89GozyMa1TvDcX0fFN58RM5V601mJHR8513CukU3+VSzpXFSdYugpImrTM7jDLhAm77p2L2eH+tnlXCelhWtYNMPTvY4WfVUiRzB1CHAP4dQfLfUsfzmSuABc160EqyUI/RxLpLjSKIlqT50CIK3B7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkWdA5oW",
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "message": {
        "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "message": {
        "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
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
  "id": -576460752303422609,
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
  "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
  "id": -576460752303422609,
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "state": "tx_+QENCwH4hLhAUv5ogGdlj9IQ7mgnsvlWg2J+89GozyMa1TvDcX0fFN58RM5V601mJHR8513CukU3+VSzpXFSdYugpImrTM7jDLhAm77p2L2eH+tnlXCelhWtYNMPTvY4WfVUiRzB1CHAP4dQfLfUsfzmSuABc160EqyUI/RxLpLjSKIlqT50CIK3B7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkWdA5oW"
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "state": "tx_+QENCwH4hLhAUv5ogGdlj9IQ7mgnsvlWg2J+89GozyMa1TvDcX0fFN58RM5V601mJHR8513CukU3+VSzpXFSdYugpImrTM7jDLhAm77p2L2eH+tnlXCelhWtYNMPTvY4WfVUiRzB1CHAP4dQfLfUsfzmSuABc160EqyUI/RxLpLjSKIlqT50CIK3B7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkWdA5oW"
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "poi": "pi_+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAiWN1V"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422608,
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
  "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
  "id": -576460752303422608,
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpOcZvNIhEwrMKj/2JYaVCvyoMOJVmkCnv6Ty7xiwR5kAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyhu34cE=",
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
  "id": -576460752303422607,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDi553o1P/kOWBfxk5CgG89hRi7nNaH++cmIReGl+7XlspLt9hNK9PxAZ8E7J4/rGwru4DGuUjXxq5KdsyJw2YJuEj4RjkCoQaTnGbzSIRMKzCo/9iWGlQr8qDDiVZpAp7+k8u8YsEeZAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspFVfEP"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
  "id": -576460752303422607,
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDi553o1P/kOWBfxk5CgG89hRi7nNaH++cmIReGl+7XlspLt9hNK9PxAZ8E7J4/rGwru4DGuUjXxq5KdsyJw2YJuEj4RjkCoQaTnGbzSIRMKzCo/9iWGlQr8qDDiVZpAp7+k8u8YsEeZAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspFVfEP",
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
  "id": -576460752303422606,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBoZA2kGunSn7uqayATFaGI5eousOkcXpVtwgCSCJrvKZIv+CnX3Knp7+luHiCWl/UUw1mlPOKzDfQu+00jCmIHuEDi553o1P/kOWBfxk5CgG89hRi7nNaH++cmIReGl+7XlspLt9hNK9PxAZ8E7J4/rGwru4DGuUjXxq5KdsyJw2YJuEj4RjkCoQaTnGbzSIRMKzCo/9iWGlQr8qDDiVZpAp7+k8u8YsEeZAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoFSXtQ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
  "id": -576460752303422606,
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "state": "tx_+NILAfiEuEBoZA2kGunSn7uqayATFaGI5eousOkcXpVtwgCSCJrvKZIv+CnX3Knp7+luHiCWl/UUw1mlPOKzDfQu+00jCmIHuEDi553o1P/kOWBfxk5CgG89hRi7nNaH++cmIReGl+7XlspLt9hNK9PxAZ8E7J4/rGwru4DGuUjXxq5KdsyJw2YJuEj4RjkCoQaTnGbzSIRMKzCo/9iWGlQr8qDDiVZpAp7+k8u8YsEeZAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoFSXtQ"
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "state": "tx_+NILAfiEuEBoZA2kGunSn7uqayATFaGI5eousOkcXpVtwgCSCJrvKZIv+CnX3Knp7+luHiCWl/UUw1mlPOKzDfQu+00jCmIHuEDi553o1P/kOWBfxk5CgG89hRi7nNaH++cmIReGl+7XlspLt9hNK9PxAZ8E7J4/rGwru4DGuUjXxq5KdsyJw2YJuEj4RjkCoQaTnGbzSIRMKzCo/9iWGlQr8qDDiVZpAp7+k8u8YsEeZAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoFSXtQ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422605,
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
  "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
  "id": -576460752303422605,
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
  "id": -576460752303422604,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
  "id": -576460752303422604,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBoZA2kGunSn7uqayATFaGI5eousOkcXpVtwgCSCJrvKZIv+CnX3Knp7+luHiCWl/UUw1mlPOKzDfQu+00jCmIHuEDi553o1P/kOWBfxk5CgG89hRi7nNaH++cmIReGl+7XlspLt9hNK9PxAZ8E7J4/rGwru4DGuUjXxq5KdsyJw2YJuEj4RjkCoQaTnGbzSIRMKzCo/9iWGlQr8qDDiVZpAp7+k8u8YsEeZAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoFSXtQ",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBoZA2kGunSn7uqayATFaGI5eousOkcXpVtwgCSCJrvKZIv+CnX3Knp7+luHiCWl/UUw1mlPOKzDfQu+00jCmIHuEDi553o1P/kOWBfxk5CgG89hRi7nNaH++cmIReGl+7XlspLt9hNK9PxAZ8E7J4/rGwru4DGuUjXxq5KdsyJw2YJuEj4RjkCoQaTnGbzSIRMKzCo/9iWGlQr8qDDiVZpAp7+k8u8YsEeZAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoFSXtQ",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBoZA2kGunSn7uqayATFaGI5eousOkcXpVtwgCSCJrvKZIv+CnX3Knp7+luHiCWl/UUw1mlPOKzDfQu+00jCmIHuEDi553o1P/kOWBfxk5CgG89hRi7nNaH++cmIReGl+7XlspLt9hNK9PxAZ8E7J4/rGwru4DGuUjXxq5KdsyJw2YJuEj4RjkCoQaTnGbzSIRMKzCo/9iWGlQr8qDDiVZpAp7+k8u8YsEeZAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoFSXtQ",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
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
  "id": -576460752303422603,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {
    "fee": 123456789876543
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
  "id": -576460752303422603,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBpOcZvNIhEwrMKj/2JYaVCvyoMOJVmkCnv6Ty7xiwR5koQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuEBoZA2kGunSn7uqayATFaGI5eousOkcXpVtwgCSCJrvKZIv+CnX3Knp7+luHiCWl/UUw1mlPOKzDfQu+00jCmIHuEDi553o1P/kOWBfxk5CgG89hRi7nNaH++cmIReGl+7XlspLt9hNK9PxAZ8E7J4/rGwru4DGuUjXxq5KdsyJw2YJuEj4RjkCoQaTnGbzSIRMKzCo/9iWGlQr8qDDiVZpAp7+k8u8YsEeZAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsq5AUz5AUk8AfkBP/kBPKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vkBGPhPoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdU7aA0rg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYvKCgEAhj+qJSJf/vh0oA7skHySTMTme58T75lYKvbk28pqCBuIk+JBbWtfrmv2+FGAgICAgICgDkgxLMEMXcRIbAXvXp0bwE+Divd/xlFEEvTFzDIBd1SAgKAgj3dA/8LX90RfkRWFqwEmw1brTAhYrDknh6Y4pb0crYCAgICAgID4T6Agj3dA/8LX90RfkRWFqwEmw1brTAhYrDknh6Y4pb0cre2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgALAwMDAwACGcEiGGw8/R2VfpXY=",
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
  "method": "channels.slash_sign",
  "params": {
    "signed_tx": "tx_+QLACwH4QrhAapCf2JztZMTcaXIbulg9/dTbgju6gFOzF4TwNBcmKndkTakEa5JSa+l5uAEBKmp82Yp8DHbZbX4lz9UUSXO3BbkCd/kCdDcBoQaTnGbzSIRMKzCo/9iWGlQr8qDDiVZpAp7+k8u8YsEeZKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAaGQNpBrp0p+7qmsgExWhiOXqLrDpHF6VbcIAkgia7ymSL/gp19yp6e/pbh4glpf1FMNZpTzisw30LvtNIwpiB7hA4ued6NT/5DlgX8ZOQoBvPYUYu5zWh/vnJiEXhpfu15bKS7fYTSvT8QGfBOyeP6xsK7uAxrlI18auSnbMicNmCbhI+EY5AqEGk5xm80iETCswqP/YlhpUK/Kgw4lWaQKe/pPLvGLBHmQCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhnBIhhsPP0ctu7dS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAapCf2JztZMTcaXIbulg9/dTbgju6gFOzF4TwNBcmKndkTakEa5JSa+l5uAEBKmp82Yp8DHbZbX4lz9UUSXO3BbkCd/kCdDcBoQaTnGbzSIRMKzCo/9iWGlQr8qDDiVZpAp7+k8u8YsEeZKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAaGQNpBrp0p+7qmsgExWhiOXqLrDpHF6VbcIAkgia7ymSL/gp19yp6e/pbh4glpf1FMNZpTzisw30LvtNIwpiB7hA4ued6NT/5DlgX8ZOQoBvPYUYu5zWh/vnJiEXhpfu15bKS7fYTSvT8QGfBOyeP6xsK7uAxrlI18auSnbMicNmCbhI+EY5AqEGk5xm80iETCswqP/YlhpUK/Kgw4lWaQKe/pPLvGLBHmQCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhnBIhhsPP0ctu7dS",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAapCf2JztZMTcaXIbulg9/dTbgju6gFOzF4TwNBcmKndkTakEa5JSa+l5uAEBKmp82Yp8DHbZbX4lz9UUSXO3BbkCd/kCdDcBoQaTnGbzSIRMKzCo/9iWGlQr8qDDiVZpAp7+k8u8YsEeZKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAaGQNpBrp0p+7qmsgExWhiOXqLrDpHF6VbcIAkgia7ymSL/gp19yp6e/pbh4glpf1FMNZpTzisw30LvtNIwpiB7hA4ued6NT/5DlgX8ZOQoBvPYUYu5zWh/vnJiEXhpfu15bKS7fYTSvT8QGfBOyeP6xsK7uAxrlI18auSnbMicNmCbhI+EY5AqEGk5xm80iETCswqP/YlhpUK/Kgw4lWaQKe/pPLvGLBHmQCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhnBIhhsPP0ctu7dS",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBpOcZvNIhEwrMKj/2JYaVCvyoMOJVmkCnv6Ty7xiwR5koQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/6GJGE5yoACAIYPXtZ/KAAdVmS3wg==",
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
    "signed_tx": "tx_+KcLAfhCuEBAo6aZWqy3aY0h9LYUvdfzvVRn3oZa5/E4yqTP/fE3NSpPfTPNe1RBEQP0DRJVsPRpAnNmFhG08A5Zbofuo1MMuF/4XTgBoQaTnGbzSIRMKzCo/9iWGlQr8qDDiVZpAp7+k8u8YsEeZKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAHWsorsw="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBAo6aZWqy3aY0h9LYUvdfzvVRn3oZa5/E4yqTP/fE3NSpPfTPNe1RBEQP0DRJVsPRpAnNmFhG08A5Zbofuo1MMuF/4XTgBoQaTnGbzSIRMKzCo/9iWGlQr8qDDiVZpAp7+k8u8YsEeZKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAHWsorsw=",
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBAo6aZWqy3aY0h9LYUvdfzvVRn3oZa5/E4yqTP/fE3NSpPfTPNe1RBEQP0DRJVsPRpAnNmFhG08A5Zbofuo1MMuF/4XTgBoQaTnGbzSIRMKzCo/9iWGlQr8qDDiVZpAp7+k8u8YsEeZKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAHWsorsw=",
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
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
    "channel_id": "ch_281XN3mCLXHgi8pfYb6LC9JpXgRPoGFoj6gEirp65J7VVeoDeT",
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
      "fsm_id": "ba_/YdXuNpz9VWvdlAB3AxBm9SJFG3kaXbOM9s99b/mGi+mkSM6"
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
      "fsm_id": "ba_kJyNIpMHGztBIFQ6Yr6nt3BHq3bcR3UfvACjuzn2ZfJurC2M"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZILe/04g==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422602,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEA9ikBnKU2gO/Jz6wo1o8PKSPRSvmlKtRiapCciCJqLeVxRF365gxiZ1JykvGbawDnWFOC4PR65bc+f+UhlceICuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGSDKbcVA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422602,
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_kJyNIpMHGztBIFQ6Yr6nt3BHq3bcR3UfvACjuzn2ZfJurC2M"
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEA9ikBnKU2gO/Jz6wo1o8PKSPRSvmlKtRiapCciCJqLeVxRF365gxiZ1JykvGbawDnWFOC4PR65bc+f+UhlceICuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGSDKbcVA=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422601,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAPYpAZylNoDvyc+sKNaPDykj0Ur5pSrUYmqQnIgiai3lcURd+uYMYmdScpLxm2sA51hTguD0euW3Pn/lIZXHiArhAstsCFdV3RvOGMzUEVrpKFMvPe69YOrMwUCg5H+QdxNYfd/sobHThnVWsxYkF6qwBgAAXBpcjp2frIgTASc3iDbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rkjhj9Xc"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
  "id": -576460752303422601,
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAPYpAZylNoDvyc+sKNaPDykj0Ur5pSrUYmqQnIgiai3lcURd+uYMYmdScpLxm2sA51hTguD0euW3Pn/lIZXHiArhAstsCFdV3RvOGMzUEVrpKFMvPe69YOrMwUCg5H+QdxNYfd/sobHThnVWsxYkF6qwBgAAXBpcjp2frIgTASc3iDbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rkjhj9Xc",
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_/YdXuNpz9VWvdlAB3AxBm9SJFG3kaXbOM9s99b/mGi+mkSM6"
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAPYpAZylNoDvyc+sKNaPDykj0Ur5pSrUYmqQnIgiai3lcURd+uYMYmdScpLxm2sA51hTguD0euW3Pn/lIZXHiArhAstsCFdV3RvOGMzUEVrpKFMvPe69YOrMwUCg5H+QdxNYfd/sobHThnVWsxYkF6qwBgAAXBpcjp2frIgTASc3iDbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rkjhj9Xc",
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAPYpAZylNoDvyc+sKNaPDykj0Ur5pSrUYmqQnIgiai3lcURd+uYMYmdScpLxm2sA51hTguD0euW3Pn/lIZXHiArhAstsCFdV3RvOGMzUEVrpKFMvPe69YOrMwUCg5H+QdxNYfd/sobHThnVWsxYkF6qwBgAAXBpcjp2frIgTASc3iDbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rkjhj9Xc",
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAPYpAZylNoDvyc+sKNaPDykj0Ur5pSrUYmqQnIgiai3lcURd+uYMYmdScpLxm2sA51hTguD0euW3Pn/lIZXHiArhAstsCFdV3RvOGMzUEVrpKFMvPe69YOrMwUCg5H+QdxNYfd/sobHThnVWsxYkF6qwBgAAXBpcjp2frIgTASc3iDbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rkjhj9Xc",
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "message": {
        "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "message": {
        "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
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
  "id": -576460752303422600,
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
  "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
  "id": -576460752303422600,
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "state": "tx_+QENCwH4hLhAPYpAZylNoDvyc+sKNaPDykj0Ur5pSrUYmqQnIgiai3lcURd+uYMYmdScpLxm2sA51hTguD0euW3Pn/lIZXHiArhAstsCFdV3RvOGMzUEVrpKFMvPe69YOrMwUCg5H+QdxNYfd/sobHThnVWsxYkF6qwBgAAXBpcjp2frIgTASc3iDbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rkjhj9Xc"
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "state": "tx_+QENCwH4hLhAPYpAZylNoDvyc+sKNaPDykj0Ur5pSrUYmqQnIgiai3lcURd+uYMYmdScpLxm2sA51hTguD0euW3Pn/lIZXHiArhAstsCFdV3RvOGMzUEVrpKFMvPe69YOrMwUCg5H+QdxNYfd/sobHThnVWsxYkF6qwBgAAXBpcjp2frIgTASc3iDbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rkjhj9Xc"
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "poi": "pi_+QFJPAH5AT/5ATygI1TOawXA7wlbYopS508bJNd3OZAvJ7C4tW4ONZhVGm/5ARj4dKAjVM5rBcDvCVtiilLnTxsk13c5kC8nsLi1bg41mFUab/hRgICAgICAoJnfodLDZS3PAMd+2Dirf+Y0DrFjnbmdVABf7RJQiFFGgICgyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXOAgICAgICA+E+gmd+h0sNlLc8Ax37YOKt/5jQOsWOduZ1UAF/tElCIUUbtoDSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bi8oKAQCGP6olIl//+E+gyQyD4cA4rNk2VJgCQ9hrdF4TiYSlXeU9zWzM67yoNXPtoDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoABwMDAwMAiWN1V"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422599,
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
  "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
  "id": -576460752303422599,
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBk2XSOoYITl/p0jDlF2sqGG2GiD+JpcxgwZ4tZC4mrq4AqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyjLyP/w=",
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
  "id": -576460752303422598,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEATI+MhZsptz4kreexz+wzAiii5dFaPZYIMl65LAPh0FAsMj7H9h8Ia5cPjc8Sn3tAllNigpDrsV8Drz9cXdcsCuEj4RjkCoQZNl0jqGCE5f6dIw5RdrKhhthog/iaXMYMGeLWQuJq6uAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspY6D4y"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
  "id": -576460752303422598,
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "signed_tx": "tx_+JALAfhCuEATI+MhZsptz4kreexz+wzAiii5dFaPZYIMl65LAPh0FAsMj7H9h8Ia5cPjc8Sn3tAllNigpDrsV8Drz9cXdcsCuEj4RjkCoQZNl0jqGCE5f6dIw5RdrKhhthog/iaXMYMGeLWQuJq6uAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspY6D4y",
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
  "id": -576460752303422597,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEATI+MhZsptz4kreexz+wzAiii5dFaPZYIMl65LAPh0FAsMj7H9h8Ia5cPjc8Sn3tAllNigpDrsV8Drz9cXdcsCuECAYfv/AbAE9cAoGV8jYj9RDaNIfLPZ6E1dgB0VQafVSwnbG+5xOvzY9MCLufsduW7MRvDPPy4jGKeGv41JE3kNuEj4RjkCoQZNl0jqGCE5f6dIw5RdrKhhthog/iaXMYMGeLWQuJq6uAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp1tfM4"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
  "id": -576460752303422597,
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "state": "tx_+NILAfiEuEATI+MhZsptz4kreexz+wzAiii5dFaPZYIMl65LAPh0FAsMj7H9h8Ia5cPjc8Sn3tAllNigpDrsV8Drz9cXdcsCuECAYfv/AbAE9cAoGV8jYj9RDaNIfLPZ6E1dgB0VQafVSwnbG+5xOvzY9MCLufsduW7MRvDPPy4jGKeGv41JE3kNuEj4RjkCoQZNl0jqGCE5f6dIw5RdrKhhthog/iaXMYMGeLWQuJq6uAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp1tfM4"
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "state": "tx_+NILAfiEuEATI+MhZsptz4kreexz+wzAiii5dFaPZYIMl65LAPh0FAsMj7H9h8Ia5cPjc8Sn3tAllNigpDrsV8Drz9cXdcsCuECAYfv/AbAE9cAoGV8jYj9RDaNIfLPZ6E1dgB0VQafVSwnbG+5xOvzY9MCLufsduW7MRvDPPy4jGKeGv41JE3kNuEj4RjkCoQZNl0jqGCE5f6dIw5RdrKhhthog/iaXMYMGeLWQuJq6uAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp1tfM4"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422596,
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
  "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
  "id": -576460752303422596,
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
  "id": -576460752303422595,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
  "id": -576460752303422595,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEATI+MhZsptz4kreexz+wzAiii5dFaPZYIMl65LAPh0FAsMj7H9h8Ia5cPjc8Sn3tAllNigpDrsV8Drz9cXdcsCuECAYfv/AbAE9cAoGV8jYj9RDaNIfLPZ6E1dgB0VQafVSwnbG+5xOvzY9MCLufsduW7MRvDPPy4jGKeGv41JE3kNuEj4RjkCoQZNl0jqGCE5f6dIw5RdrKhhthog/iaXMYMGeLWQuJq6uAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp1tfM4",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEATI+MhZsptz4kreexz+wzAiii5dFaPZYIMl65LAPh0FAsMj7H9h8Ia5cPjc8Sn3tAllNigpDrsV8Drz9cXdcsCuECAYfv/AbAE9cAoGV8jYj9RDaNIfLPZ6E1dgB0VQafVSwnbG+5xOvzY9MCLufsduW7MRvDPPy4jGKeGv41JE3kNuEj4RjkCoQZNl0jqGCE5f6dIw5RdrKhhthog/iaXMYMGeLWQuJq6uAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp1tfM4",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEATI+MhZsptz4kreexz+wzAiii5dFaPZYIMl65LAPh0FAsMj7H9h8Ia5cPjc8Sn3tAllNigpDrsV8Drz9cXdcsCuECAYfv/AbAE9cAoGV8jYj9RDaNIfLPZ6E1dgB0VQafVSwnbG+5xOvzY9MCLufsduW7MRvDPPy4jGKeGv41JE3kNuEj4RjkCoQZNl0jqGCE5f6dIw5RdrKhhthog/iaXMYMGeLWQuJq6uAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsp1tfM4",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
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
  "id": -576460752303422594,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {
    "fee": 123456789876543
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
  "id": -576460752303422594,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBk2XSOoYITl/p0jDlF2sqGG2GiD+JpcxgwZ4tZC4mrq4oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwobjU+NILAfiEuEATI+MhZsptz4kreexz+wzAiii5dFaPZYIMl65LAPh0FAsMj7H9h8Ia5cPjc8Sn3tAllNigpDrsV8Drz9cXdcsCuECAYfv/AbAE9cAoGV8jYj9RDaNIfLPZ6E1dgB0VQafVSwnbG+5xOvzY9MCLufsduW7MRvDPPy4jGKeGv41JE3kNuEj4RjkCoQZNl0jqGCE5f6dIw5RdrKhhthog/iaXMYMGeLWQuJq6uAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsq5AUz5AUk8AfkBP/kBPKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vkBGPhPoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdU7aA0rg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYvKCgEAhj+qJSJf/vh0oA7skHySTMTme58T75lYKvbk28pqCBuIk+JBbWtfrmv2+FGAgICAgICgDkgxLMEMXcRIbAXvXp0bwE+Divd/xlFEEvTFzDIBd1SAgKAgj3dA/8LX90RfkRWFqwEmw1brTAhYrDknh6Y4pb0crYCAgICAgID4T6Agj3dA/8LX90RfkRWFqwEmw1brTAhYrDknh6Y4pb0cre2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgALAwMDAwACGcEiGGw8/HgjIUDM=",
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
  "method": "channels.slash_sign",
  "params": {
    "signed_tx": "tx_+QLACwH4QrhAN+7hONSeYNZACfA3vLmNAFUEErZRHjRO96zSJdhDjSC8cuTDgERopPCORpIfyGAq1JTVpfDIba9EdBX53VMPAbkCd/kCdDcBoQZNl0jqGCE5f6dIw5RdrKhhthog/iaXMYMGeLWQuJq6uKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAEyPjIWbKbc+JK3nsc/sMwIoouXRWj2WCDJeuSwD4dBQLDI+x/YfCGuXD43PEp97QJZTYoKQ67FfA68/XF3XLArhAgGH7/wGwBPXAKBlfI2I/UQ2jSHyz2ehNXYAdFUGn1UsJ2xvucTr82PTAi7n7HbluzEbwzz8uIxinhr+NSRN5DbhI+EY5AqEGTZdI6hghOX+nSMOUXayoYbYaIP4mlzGDBni1kLiaurgCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhnBIhhsPPx543iQw"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAN+7hONSeYNZACfA3vLmNAFUEErZRHjRO96zSJdhDjSC8cuTDgERopPCORpIfyGAq1JTVpfDIba9EdBX53VMPAbkCd/kCdDcBoQZNl0jqGCE5f6dIw5RdrKhhthog/iaXMYMGeLWQuJq6uKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAEyPjIWbKbc+JK3nsc/sMwIoouXRWj2WCDJeuSwD4dBQLDI+x/YfCGuXD43PEp97QJZTYoKQ67FfA68/XF3XLArhAgGH7/wGwBPXAKBlfI2I/UQ2jSHyz2ehNXYAdFUGn1UsJ2xvucTr82PTAi7n7HbluzEbwzz8uIxinhr+NSRN5DbhI+EY5AqEGTZdI6hghOX+nSMOUXayoYbYaIP4mlzGDBni1kLiaurgCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhnBIhhsPPx543iQw",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAN+7hONSeYNZACfA3vLmNAFUEErZRHjRO96zSJdhDjSC8cuTDgERopPCORpIfyGAq1JTVpfDIba9EdBX53VMPAbkCd/kCdDcBoQZNl0jqGCE5f6dIw5RdrKhhthog/iaXMYMGeLWQuJq6uKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAEyPjIWbKbc+JK3nsc/sMwIoouXRWj2WCDJeuSwD4dBQLDI+x/YfCGuXD43PEp97QJZTYoKQ67FfA68/XF3XLArhAgGH7/wGwBPXAKBlfI2I/UQ2jSHyz2ehNXYAdFUGn1UsJ2xvucTr82PTAi7n7HbluzEbwzz8uIxinhr+NSRN5DbhI+EY5AqEGTZdI6hghOX+nSMOUXayoYbYaIP4mlzGDBni1kLiaurgCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhnBIhhsPPx543iQw",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBk2XSOoYITl/p0jDlF2sqGG2GiD+JpcxgwZ4tZC4mrq4oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/6GJGE5yoACAIYPXtZ/KAAfqUqU3g==",
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
    "signed_tx": "tx_+KcLAfhCuEA1rDhp/2+/tZsYwOZf1CxeVed3jwjueJDGN5TgzeqqBgCHKYU4v+83I41v39Dgovv+nPfBYapc69DBrCYNudwCuF/4XTgBoQZNl0jqGCE5f6dIw5RdrKhhthog/iaXMYMGeLWQuJq6uKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAH5v0rF8="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEA1rDhp/2+/tZsYwOZf1CxeVed3jwjueJDGN5TgzeqqBgCHKYU4v+83I41v39Dgovv+nPfBYapc69DBrCYNudwCuF/4XTgBoQZNl0jqGCE5f6dIw5RdrKhhthog/iaXMYMGeLWQuJq6uKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAH5v0rF8=",
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEA1rDhp/2+/tZsYwOZf1CxeVed3jwjueJDGN5TgzeqqBgCHKYU4v+83I41v39Dgovv+nPfBYapc69DBrCYNudwCuF/4XTgBoQZNl0jqGCE5f6dIw5RdrKhhthog/iaXMYMGeLWQuJq6uKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAH5v0rF8=",
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
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
    "channel_id": "ch_bAxVpGGschpsuP54yEpxQU3NuSQfof9k7pUZ8kLDPnQ3k47ei",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
