
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
      "fsm_id": "ba_e7PvjrzU9ZgSG7+O9dMaOTqi1Z4uFr8IxU39gwOkd0XTw00u"
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
      "fsm_id": "ba_ScOAZ1RpQWSFR6Lf5xKlZQw5n01+FcCxAu3R4LKS5FVor78d"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZdFk0GTA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422519,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDV1jA8lQqx9Iv9X/RVpgWLY5F4U8/doPjo2OfIX/yd+xO2MvsxbKWuSmvKwt1WQTwhmiHUToG9kt6rRKF+RLoFuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGXTiTP5A="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422519,
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_ScOAZ1RpQWSFR6Lf5xKlZQw5n01+FcCxAu3R4LKS5FVor78d"
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEDV1jA8lQqx9Iv9X/RVpgWLY5F4U8/doPjo2OfIX/yd+xO2MvsxbKWuSmvKwt1WQTwhmiHUToG9kt6rRKF+RLoFuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGXTiTP5A=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422518,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAHVaUCaFT2O5glc/pNdtGXBLeCILjnXPZ+sWXamaqH5jZCYnvxHGf7//bWmwOw8dZWEagb0PmKyyEAfYygsPtALhA1dYwPJUKsfSL/V/0VaYFi2OReFPP3aD46NjnyF/8nfsTtjL7MWylrkprysLdVkE8IZoh1E6BvZLeq0ShfkS6BbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rl3SOE1E"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
  "id": -576460752303422518,
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAHVaUCaFT2O5glc/pNdtGXBLeCILjnXPZ+sWXamaqH5jZCYnvxHGf7//bWmwOw8dZWEagb0PmKyyEAfYygsPtALhA1dYwPJUKsfSL/V/0VaYFi2OReFPP3aD46NjnyF/8nfsTtjL7MWylrkprysLdVkE8IZoh1E6BvZLeq0ShfkS6BbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rl3SOE1E",
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_e7PvjrzU9ZgSG7+O9dMaOTqi1Z4uFr8IxU39gwOkd0XTw00u"
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAHVaUCaFT2O5glc/pNdtGXBLeCILjnXPZ+sWXamaqH5jZCYnvxHGf7//bWmwOw8dZWEagb0PmKyyEAfYygsPtALhA1dYwPJUKsfSL/V/0VaYFi2OReFPP3aD46NjnyF/8nfsTtjL7MWylrkprysLdVkE8IZoh1E6BvZLeq0ShfkS6BbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rl3SOE1E",
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAHVaUCaFT2O5glc/pNdtGXBLeCILjnXPZ+sWXamaqH5jZCYnvxHGf7//bWmwOw8dZWEagb0PmKyyEAfYygsPtALhA1dYwPJUKsfSL/V/0VaYFi2OReFPP3aD46NjnyF/8nfsTtjL7MWylrkprysLdVkE8IZoh1E6BvZLeq0ShfkS6BbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rl3SOE1E",
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAHVaUCaFT2O5glc/pNdtGXBLeCILjnXPZ+sWXamaqH5jZCYnvxHGf7//bWmwOw8dZWEagb0PmKyyEAfYygsPtALhA1dYwPJUKsfSL/V/0VaYFi2OReFPP3aD46NjnyF/8nfsTtjL7MWylrkprysLdVkE8IZoh1E6BvZLeq0ShfkS6BbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rl3SOE1E",
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
    "data": {
      "message": {
        "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
    "data": {
      "message": {
        "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
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
  "id": -576460752303422517,
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
  "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
  "id": -576460752303422517,
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
    "data": {
      "state": "tx_+QENCwH4hLhAHVaUCaFT2O5glc/pNdtGXBLeCILjnXPZ+sWXamaqH5jZCYnvxHGf7//bWmwOw8dZWEagb0PmKyyEAfYygsPtALhA1dYwPJUKsfSL/V/0VaYFi2OReFPP3aD46NjnyF/8nfsTtjL7MWylrkprysLdVkE8IZoh1E6BvZLeq0ShfkS6BbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rl3SOE1E"
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
    "data": {
      "state": "tx_+QENCwH4hLhAHVaUCaFT2O5glc/pNdtGXBLeCILjnXPZ+sWXamaqH5jZCYnvxHGf7//bWmwOw8dZWEagb0PmKyyEAfYygsPtALhA1dYwPJUKsfSL/V/0VaYFi2OReFPP3aD46NjnyF/8nfsTtjL7MWylrkprysLdVkE8IZoh1E6BvZLeq0ShfkS6BbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4Rl3SOE1E"
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
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
  "id": -576460752303422516,
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
  "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
  "id": -576460752303422516,
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkV5Mxo720vTJ7NmllGZqT7jjw4h8mH19SlwN844tccQAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyilgBzk=",
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
  "id": -576460752303422515,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECp0HmM27jQMmpCUk+0S0odJgTyWw1L6Le+JxItZkSOF+bIyY+zh/PhgT7mGiIP4PVM8YYs/Ukj+trS1oQzVFAJuEj4RjkCoQZFeTMaO9tL0yezZpZRmak+448OIfJh9fUpcDfOOLXHEAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsryQ+yr"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
  "id": -576460752303422515,
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
    "data": {
      "signed_tx": "tx_+JALAfhCuECp0HmM27jQMmpCUk+0S0odJgTyWw1L6Le+JxItZkSOF+bIyY+zh/PhgT7mGiIP4PVM8YYs/Ukj+trS1oQzVFAJuEj4RjkCoQZFeTMaO9tL0yezZpZRmak+448OIfJh9fUpcDfOOLXHEAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsryQ+yr",
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
  "id": -576460752303422514,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECp0HmM27jQMmpCUk+0S0odJgTyWw1L6Le+JxItZkSOF+bIyY+zh/PhgT7mGiIP4PVM8YYs/Ukj+trS1oQzVFAJuEDt6EktYNTt64ONZ8zBZjsnSIgt8fjlwfNysijMO0D1IpBOxnugzhQq3lb1hWtLClE3fqc/aIodAWpFd99+3aEGuEj4RjkCoQZFeTMaO9tL0yezZpZRmak+448OIfJh9fUpcDfOOLXHEAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqYLGSg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
  "id": -576460752303422514,
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
    "data": {
      "state": "tx_+NILAfiEuECp0HmM27jQMmpCUk+0S0odJgTyWw1L6Le+JxItZkSOF+bIyY+zh/PhgT7mGiIP4PVM8YYs/Ukj+trS1oQzVFAJuEDt6EktYNTt64ONZ8zBZjsnSIgt8fjlwfNysijMO0D1IpBOxnugzhQq3lb1hWtLClE3fqc/aIodAWpFd99+3aEGuEj4RjkCoQZFeTMaO9tL0yezZpZRmak+448OIfJh9fUpcDfOOLXHEAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqYLGSg"
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
    "data": {
      "state": "tx_+NILAfiEuECp0HmM27jQMmpCUk+0S0odJgTyWw1L6Le+JxItZkSOF+bIyY+zh/PhgT7mGiIP4PVM8YYs/Ukj+trS1oQzVFAJuEDt6EktYNTt64ONZ8zBZjsnSIgt8fjlwfNysijMO0D1IpBOxnugzhQq3lb1hWtLClE3fqc/aIodAWpFd99+3aEGuEj4RjkCoQZFeTMaO9tL0yezZpZRmak+448OIfJh9fUpcDfOOLXHEAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqYLGSg"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422513,
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
  "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
  "id": -576460752303422513,
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
  "id": -576460752303422512,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
  "id": -576460752303422512,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECp0HmM27jQMmpCUk+0S0odJgTyWw1L6Le+JxItZkSOF+bIyY+zh/PhgT7mGiIP4PVM8YYs/Ukj+trS1oQzVFAJuEDt6EktYNTt64ONZ8zBZjsnSIgt8fjlwfNysijMO0D1IpBOxnugzhQq3lb1hWtLClE3fqc/aIodAWpFd99+3aEGuEj4RjkCoQZFeTMaO9tL0yezZpZRmak+448OIfJh9fUpcDfOOLXHEAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqYLGSg",
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECp0HmM27jQMmpCUk+0S0odJgTyWw1L6Le+JxItZkSOF+bIyY+zh/PhgT7mGiIP4PVM8YYs/Ukj+trS1oQzVFAJuEDt6EktYNTt64ONZ8zBZjsnSIgt8fjlwfNysijMO0D1IpBOxnugzhQq3lb1hWtLClE3fqc/aIodAWpFd99+3aEGuEj4RjkCoQZFeTMaO9tL0yezZpZRmak+448OIfJh9fUpcDfOOLXHEAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqYLGSg",
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECp0HmM27jQMmpCUk+0S0odJgTyWw1L6Le+JxItZkSOF+bIyY+zh/PhgT7mGiIP4PVM8YYs/Ukj+trS1oQzVFAJuEDt6EktYNTt64ONZ8zBZjsnSIgt8fjlwfNysijMO0D1IpBOxnugzhQq3lb1hWtLClE3fqc/aIodAWpFd99+3aEGuEj4RjkCoQZFeTMaO9tL0yezZpZRmak+448OIfJh9fUpcDfOOLXHEAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqYLGSg",
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
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
  "id": -576460752303422511,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {
    "gas_price": 1000001234
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
  "id": -576460752303422511,
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBkV5Mxo720vTJ7NmllGZqT7jjw4h8mH19SlwN844tccQoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuECp0HmM27jQMmpCUk+0S0odJgTyWw1L6Le+JxItZkSOF+bIyY+zh/PhgT7mGiIP4PVM8YYs/Ukj+trS1oQzVFAJuEDt6EktYNTt64ONZ8zBZjsnSIgt8fjlwfNysijMO0D1IpBOxnugzhQq3lb1hWtLClE3fqc/aIodAWpFd99+3aEGuEj4RjkCoQZFeTMaO9tL0yezZpZRmak+448OIfJh9fUpcDfOOLXHEAKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsq5AUz5AUk8AfkBP/kBPKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vkBGPhPoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdU7aA0rg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYvKCgEAhj+qJSJf/vh0oA7skHySTMTme58T75lYKvbk28pqCBuIk+JBbWtfrmv2+FGAgICAgICgDkgxLMEMXcRIbAXvXp0bwE+Divd/xlFEEvTFzDIBd1SAgKAgj3dA/8LX90RfkRWFqwEmw1brTAhYrDknh6Y4pb0crYCAgICAgID4T6Agj3dA/8LX90RfkRWFqwEmw1brTAhYrDknh6Y4pb0cre2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgALAwMDAwACGGR7KUfkIX7Fd0hk=",
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
    "signed_tx": "tx_+QLACwH4QrhA8FEb90yDJ9DtUVSfMva3269znCmzj3QpgnaODmrP1EULP+d+gmeD6gJfZWVn3v/0BK0qS00we8VMuCaG/AknD7kCd/kCdDcBoQZFeTMaO9tL0yezZpZRmak+448OIfJh9fUpcDfOOLXHEKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAqdB5jNu40DJqQlJPtEtKHSYE8lsNS+i3vicSLWZEjhfmyMmPs4fz4YE+5hoiD+D1TPGGLP1JI/ra0taEM1RQCbhA7ehJLWDU7euDjWfMwWY7J0iILfH45cHzcrIozDtA9SKQTsZ7oM4UKt5W9YVrSwpRN36nP2iKHQFqRXffft2hBrhI+EY5AqEGRXkzGjvbS9Mns2aWUZmpPuOPDiHyYfX1KXA3zji1xxACoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhhkeylH5CF8KQkg2"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhA8FEb90yDJ9DtUVSfMva3269znCmzj3QpgnaODmrP1EULP+d+gmeD6gJfZWVn3v/0BK0qS00we8VMuCaG/AknD7kCd/kCdDcBoQZFeTMaO9tL0yezZpZRmak+448OIfJh9fUpcDfOOLXHEKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAqdB5jNu40DJqQlJPtEtKHSYE8lsNS+i3vicSLWZEjhfmyMmPs4fz4YE+5hoiD+D1TPGGLP1JI/ra0taEM1RQCbhA7ehJLWDU7euDjWfMwWY7J0iILfH45cHzcrIozDtA9SKQTsZ7oM4UKt5W9YVrSwpRN36nP2iKHQFqRXffft2hBrhI+EY5AqEGRXkzGjvbS9Mns2aWUZmpPuOPDiHyYfX1KXA3zji1xxACoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhhkeylH5CF8KQkg2",
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhA8FEb90yDJ9DtUVSfMva3269znCmzj3QpgnaODmrP1EULP+d+gmeD6gJfZWVn3v/0BK0qS00we8VMuCaG/AknD7kCd/kCdDcBoQZFeTMaO9tL0yezZpZRmak+448OIfJh9fUpcDfOOLXHEKEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4G41PjSCwH4hLhAqdB5jNu40DJqQlJPtEtKHSYE8lsNS+i3vicSLWZEjhfmyMmPs4fz4YE+5hoiD+D1TPGGLP1JI/ra0taEM1RQCbhA7ehJLWDU7euDjWfMwWY7J0iILfH45cHzcrIozDtA9SKQTsZ7oM4UKt5W9YVrSwpRN36nP2iKHQFqRXffft2hBrhI+EY5AqEGRXkzGjvbS9Mns2aWUZmpPuOPDiHyYfX1KXA3zji1xxACoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhhkeylH5CF8KQkg2",
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBkV5Mxo720vTJ7NmllGZqT7jjw4h8mH19SlwN844tccQoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/6GJGE5yoACAIYPXtZ/KAAndPDozA==",
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
    "signed_tx": "tx_+KcLAfhCuEDzUYerJUsyXvJYQq8ErTrdd3aFO/32wMVB27/GztR42VryBFhvs3ErhNfchtRiQerVu2bwEjluYQRvMBGYQboKuF/4XTgBoQZFeTMaO9tL0yezZpZRmak+448OIfJh9fUpcDfOOLXHEKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAJ9xTDak="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDzUYerJUsyXvJYQq8ErTrdd3aFO/32wMVB27/GztR42VryBFhvs3ErhNfchtRiQerVu2bwEjluYQRvMBGYQboKuF/4XTgBoQZFeTMaO9tL0yezZpZRmak+448OIfJh9fUpcDfOOLXHEKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAJ9xTDak=",
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDzUYerJUsyXvJYQq8ErTrdd3aFO/32wMVB27/GztR42VryBFhvs3ErhNfchtRiQerVu2bwEjluYQRvMBGYQboKuF/4XTgBoQZFeTMaO9tL0yezZpZRmak+448OIfJh9fUpcDfOOLXHEKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAJ9xTDak=",
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
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
    "channel_id": "ch_Xbc8WP2b4fZsw5d6yhWsiUCd8HDWRhdmAzLnCtdYJxiRYDbwb",
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
      "fsm_id": "ba_nogQvPLytdpHXOw9PFJM88gigrHv7XOYocsWESqAWlhGBfj7"
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
      "fsm_id": "ba_0pr9Mh9QOBWlhJ9XrySFJXn2eV0k8wZW0BCd2Luewi08Y59j"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+Bhj+qJSJgAKEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGJGE5yoAAAgoAhhAGeddIAMCgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEZgdj9/9Q==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422510,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBv83zPtvsHyuH4xDb/80t+z46RciyZGfY9/HgxsbIW+K1yAzpxtAdc34XmmTQu1+SAflXysIFp8sHZ3cM5qWQIuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGYMiKgKc="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422510,
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_0pr9Mh9QOBWlhJ9XrySFJXn2eV0k8wZW0BCd2Luewi08Y59j"
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEBv83zPtvsHyuH4xDb/80t+z46RciyZGfY9/HgxsbIW+K1yAzpxtAdc34XmmTQu1+SAflXysIFp8sHZ3cM5qWQIuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYY/qiUiYAChAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhiRhOcqAAAIKAIYQBnnXSADAoGT/CBzTbE8WmKfxmpBsujE15vDJzp4D5Hm6jC4J9bhGYMiKgKc=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422509,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAbYh/9k/6mZ50eR4KZJYhwo3eLugkbp7Nbf/EypswQUp6LOvDsP00i/jpefAMR9o7TAsrHubb1NkCvFhiG9wMBLhAb/N8z7b7B8rh+MQ2//NLfs+OkXIsmRn2Pfx4MbGyFvitcgM6cbQHXN+F5pk0LtfkgH5V8rCBafLB2d3DOalkCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmDi1/DH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
  "id": -576460752303422509,
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAbYh/9k/6mZ50eR4KZJYhwo3eLugkbp7Nbf/EypswQUp6LOvDsP00i/jpefAMR9o7TAsrHubb1NkCvFhiG9wMBLhAb/N8z7b7B8rh+MQ2//NLfs+OkXIsmRn2Pfx4MbGyFvitcgM6cbQHXN+F5pk0LtfkgH5V8rCBafLB2d3DOalkCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmDi1/DH",
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_nogQvPLytdpHXOw9PFJM88gigrHv7XOYocsWESqAWlhGBfj7"
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAbYh/9k/6mZ50eR4KZJYhwo3eLugkbp7Nbf/EypswQUp6LOvDsP00i/jpefAMR9o7TAsrHubb1NkCvFhiG9wMBLhAb/N8z7b7B8rh+MQ2//NLfs+OkXIsmRn2Pfx4MbGyFvitcgM6cbQHXN+F5pk0LtfkgH5V8rCBafLB2d3DOalkCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmDi1/DH",
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAbYh/9k/6mZ50eR4KZJYhwo3eLugkbp7Nbf/EypswQUp6LOvDsP00i/jpefAMR9o7TAsrHubb1NkCvFhiG9wMBLhAb/N8z7b7B8rh+MQ2//NLfs+OkXIsmRn2Pfx4MbGyFvitcgM6cbQHXN+F5pk0LtfkgH5V8rCBafLB2d3DOalkCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmDi1/DH",
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAbYh/9k/6mZ50eR4KZJYhwo3eLugkbp7Nbf/EypswQUp6LOvDsP00i/jpefAMR9o7TAsrHubb1NkCvFhiG9wMBLhAb/N8z7b7B8rh+MQ2//NLfs+OkXIsmRn2Pfx4MbGyFvitcgM6cbQHXN+F5pk0LtfkgH5V8rCBafLB2d3DOalkCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmDi1/DH",
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "message": {
        "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "message": {
        "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
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
  "id": -576460752303422508,
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
  "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
  "id": -576460752303422508,
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "state": "tx_+QENCwH4hLhAbYh/9k/6mZ50eR4KZJYhwo3eLugkbp7Nbf/EypswQUp6LOvDsP00i/jpefAMR9o7TAsrHubb1NkCvFhiG9wMBLhAb/N8z7b7B8rh+MQ2//NLfs+OkXIsmRn2Pfx4MbGyFvitcgM6cbQHXN+F5pk0LtfkgH5V8rCBafLB2d3DOalkCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmDi1/DH"
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "state": "tx_+QENCwH4hLhAbYh/9k/6mZ50eR4KZJYhwo3eLugkbp7Nbf/EypswQUp6LOvDsP00i/jpefAMR9o7TAsrHubb1NkCvFhiG9wMBLhAb/N8z7b7B8rh+MQ2//NLfs+OkXIsmRn2Pfx4MbGyFvitcgM6cbQHXN+F5pk0LtfkgH5V8rCBafLB2d3DOalkCLiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GGP6olImAAoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYYkYTnKgAACCgCGEAZ510gAwKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RmDi1/DH"
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
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
  "id": -576460752303422507,
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
  "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
  "id": -576460752303422507,
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBszyrCLf0bV6JW/7cM+/sZchpxSHoDYhDorrwqRpqhc5AqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyuWYBbI=",
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
  "id": -576460752303422506,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB1SqVc3waPg9njX7thQi6RwHQBq9M8GzY0MbkmFBT4X4SunzgyLGLgQcyUW6lguPDVZnefzcaulz3mmzEc+zoLuEj4RjkCoQbM8qwi39G1eiVv+3DPv7GXIacUh6A2IQ6K68KkaaoXOQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrYQLSG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
  "id": -576460752303422506,
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB1SqVc3waPg9njX7thQi6RwHQBq9M8GzY0MbkmFBT4X4SunzgyLGLgQcyUW6lguPDVZnefzcaulz3mmzEc+zoLuEj4RjkCoQbM8qwi39G1eiVv+3DPv7GXIacUh6A2IQ6K68KkaaoXOQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrYQLSG",
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
  "id": -576460752303422505,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA5DHQ1EbWNGv1Hfa51BAf/C+2Ru8OT772vckSb0lllLygcHZN+LpVjYqIBZKq299wvrFZKqB6Cd1t640Ms4+YDuEB1SqVc3waPg9njX7thQi6RwHQBq9M8GzY0MbkmFBT4X4SunzgyLGLgQcyUW6lguPDVZnefzcaulz3mmzEc+zoLuEj4RjkCoQbM8qwi39G1eiVv+3DPv7GXIacUh6A2IQ6K68KkaaoXOQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspUQdW2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
  "id": -576460752303422505,
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "state": "tx_+NILAfiEuEA5DHQ1EbWNGv1Hfa51BAf/C+2Ru8OT772vckSb0lllLygcHZN+LpVjYqIBZKq299wvrFZKqB6Cd1t640Ms4+YDuEB1SqVc3waPg9njX7thQi6RwHQBq9M8GzY0MbkmFBT4X4SunzgyLGLgQcyUW6lguPDVZnefzcaulz3mmzEc+zoLuEj4RjkCoQbM8qwi39G1eiVv+3DPv7GXIacUh6A2IQ6K68KkaaoXOQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspUQdW2"
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "state": "tx_+NILAfiEuEA5DHQ1EbWNGv1Hfa51BAf/C+2Ru8OT772vckSb0lllLygcHZN+LpVjYqIBZKq299wvrFZKqB6Cd1t640Ms4+YDuEB1SqVc3waPg9njX7thQi6RwHQBq9M8GzY0MbkmFBT4X4SunzgyLGLgQcyUW6lguPDVZnefzcaulz3mmzEc+zoLuEj4RjkCoQbM8qwi39G1eiVv+3DPv7GXIacUh6A2IQ6K68KkaaoXOQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspUQdW2"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422504,
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
  "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
  "id": -576460752303422504,
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
  "id": -576460752303422503,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
  "id": -576460752303422503,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA5DHQ1EbWNGv1Hfa51BAf/C+2Ru8OT772vckSb0lllLygcHZN+LpVjYqIBZKq299wvrFZKqB6Cd1t640Ms4+YDuEB1SqVc3waPg9njX7thQi6RwHQBq9M8GzY0MbkmFBT4X4SunzgyLGLgQcyUW6lguPDVZnefzcaulz3mmzEc+zoLuEj4RjkCoQbM8qwi39G1eiVv+3DPv7GXIacUh6A2IQ6K68KkaaoXOQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspUQdW2",
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEA5DHQ1EbWNGv1Hfa51BAf/C+2Ru8OT772vckSb0lllLygcHZN+LpVjYqIBZKq299wvrFZKqB6Cd1t640Ms4+YDuEB1SqVc3waPg9njX7thQi6RwHQBq9M8GzY0MbkmFBT4X4SunzgyLGLgQcyUW6lguPDVZnefzcaulz3mmzEc+zoLuEj4RjkCoQbM8qwi39G1eiVv+3DPv7GXIacUh6A2IQ6K68KkaaoXOQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspUQdW2",
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEA5DHQ1EbWNGv1Hfa51BAf/C+2Ru8OT772vckSb0lllLygcHZN+LpVjYqIBZKq299wvrFZKqB6Cd1t640Ms4+YDuEB1SqVc3waPg9njX7thQi6RwHQBq9M8GzY0MbkmFBT4X4SunzgyLGLgQcyUW6lguPDVZnefzcaulz3mmzEc+zoLuEj4RjkCoQbM8qwi39G1eiVv+3DPv7GXIacUh6A2IQ6K68KkaaoXOQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspUQdW2",
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
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
  "id": -576460752303422502,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {
    "gas_price": 1000001234
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
  "id": -576460752303422502,
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBszyrCLf0bV6JW/7cM+/sZchpxSHoDYhDorrwqRpqhc5oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwobjU+NILAfiEuEA5DHQ1EbWNGv1Hfa51BAf/C+2Ru8OT772vckSb0lllLygcHZN+LpVjYqIBZKq299wvrFZKqB6Cd1t640Ms4+YDuEB1SqVc3waPg9njX7thQi6RwHQBq9M8GzY0MbkmFBT4X4SunzgyLGLgQcyUW6lguPDVZnefzcaulz3mmzEc+zoLuEj4RjkCoQbM8qwi39G1eiVv+3DPv7GXIacUh6A2IQ6K68KkaaoXOQKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsq5AUz5AUk8AfkBP/kBPKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vkBGPhPoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdU7aA0rg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYvKCgEAhj+qJSJf/vh0oA7skHySTMTme58T75lYKvbk28pqCBuIk+JBbWtfrmv2+FGAgICAgICgDkgxLMEMXcRIbAXvXp0bwE+Divd/xlFEEvTFzDIBd1SAgKAgj3dA/8LX90RfkRWFqwEmw1brTAhYrDknh6Y4pb0crYCAgICAgID4T6Agj3dA/8LX90RfkRWFqwEmw1brTAhYrDknh6Y4pb0cre2gMLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGLygoBAIYkYTnKgALAwMDAwACGGR7KUfkIKJ3ImHU=",
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
    "signed_tx": "tx_+QLACwH4QrhAtyMbs8z+IY6ZE0FmquRuI1FmRU6q+ORVNEd0ODyNcUlTsiIT5qRO1FzTuPBW3DU49wqa2Zd+w5CHj/OGuDioDLkCd/kCdDcBoQbM8qwi39G1eiVv+3DPv7GXIacUh6A2IQ6K68KkaaoXOaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAOQx0NRG1jRr9R32udQQH/wvtkbvDk++9r3JEm9JZZS8oHB2Tfi6VY2KiAWSqtvfcL6xWSqgegndbeuNDLOPmA7hAdUqlXN8Gj4PZ41+7YUIukcB0AavTPBs2NDG5JhQU+F+Erp84Mixi4EHMlFupYLjw1WZ3n83Grpc95psxHPs6C7hI+EY5AqEGzPKsIt/RtXolb/twz7+xlyGnFIegNiEOiuvCpGmqFzkCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhhkeylH5CCj4PZTT"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAtyMbs8z+IY6ZE0FmquRuI1FmRU6q+ORVNEd0ODyNcUlTsiIT5qRO1FzTuPBW3DU49wqa2Zd+w5CHj/OGuDioDLkCd/kCdDcBoQbM8qwi39G1eiVv+3DPv7GXIacUh6A2IQ6K68KkaaoXOaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAOQx0NRG1jRr9R32udQQH/wvtkbvDk++9r3JEm9JZZS8oHB2Tfi6VY2KiAWSqtvfcL6xWSqgegndbeuNDLOPmA7hAdUqlXN8Gj4PZ41+7YUIukcB0AavTPBs2NDG5JhQU+F+Erp84Mixi4EHMlFupYLjw1WZ3n83Grpc95psxHPs6C7hI+EY5AqEGzPKsIt/RtXolb/twz7+xlyGnFIegNiEOiuvCpGmqFzkCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhhkeylH5CCj4PZTT",
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAtyMbs8z+IY6ZE0FmquRuI1FmRU6q+ORVNEd0ODyNcUlTsiIT5qRO1FzTuPBW3DU49wqa2Zd+w5CHj/OGuDioDLkCd/kCdDcBoQbM8qwi39G1eiVv+3DPv7GXIacUh6A2IQ6K68KkaaoXOaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKG41PjSCwH4hLhAOQx0NRG1jRr9R32udQQH/wvtkbvDk++9r3JEm9JZZS8oHB2Tfi6VY2KiAWSqtvfcL6xWSqgegndbeuNDLOPmA7hAdUqlXN8Gj4PZ41+7YUIukcB0AavTPBs2NDG5JhQU+F+Erp84Mixi4EHMlFupYLjw1WZ3n83Grpc95psxHPs6C7hI+EY5AqEGzPKsIt/RtXolb/twz7+xlyGnFIegNiEOiuvCpGmqFzkCoKZiatQjxa4uE8erIz3jJClST+bk165xkgd5qy7dB0LKuQFM+QFJPAH5AT/5ATygDuyQfJJMxOZ7nxPvmVgq9uTbymoIG4iT4kFta1+ua/b5ARj4T6AOSDEswQxdxEhsBe9enRvAT4OK93/GUUQS9MXMMgF3VO2gNK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/74dKAO7JB8kkzE5nufE++ZWCr25NvKaggbiJPiQW1rX65r9vhRgICAgICAoA5IMSzBDF3ESGwF716dG8BPg4r3f8ZRRBL0xcwyAXdUgICgII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK2AgICAgICA+E+gII93QP/C1/dEX5EVhasBJsNW60wIWKw5J4emOKW9HK3toDCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChi8oKAQCGJGE5yoACwMDAwMAAhhkeylH5CCj4PZTT",
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBszyrCLf0bV6JW/7cM+/sZchpxSHoDYhDorrwqRpqhc5oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYY/qiUiX/6GJGE5yoACAIYPXtZ/KAApqya+CA==",
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
    "signed_tx": "tx_+KcLAfhCuECoQlbgoq8GdVFSZ7pP1De03rdVzRdZb9sjyFQL8/3xxURX0heBWLpuli7lEeCaS5uT7TZzpxeqeyvLMRRLCJ0GuF/4XTgBoQbM8qwi39G1eiVv+3DPv7GXIacUh6A2IQ6K68KkaaoXOaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAKYNHefA="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECoQlbgoq8GdVFSZ7pP1De03rdVzRdZb9sjyFQL8/3xxURX0heBWLpuli7lEeCaS5uT7TZzpxeqeyvLMRRLCJ0GuF/4XTgBoQbM8qwi39G1eiVv+3DPv7GXIacUh6A2IQ6K68KkaaoXOaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAKYNHefA=",
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECoQlbgoq8GdVFSZ7pP1De03rdVzRdZb9sjyFQL8/3xxURX0heBWLpuli7lEeCaS5uT7TZzpxeqeyvLMRRLCJ0GuF/4XTgBoQbM8qwi39G1eiVv+3DPv7GXIacUh6A2IQ6K68KkaaoXOaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGGP6olIl/+hiRhOcqAAgCGD17WfygAKYNHefA=",
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
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
    "channel_id": "ch_2ZG7xoEkpZvHJ2fByjNhNjjcTFertZ7UmsuNZrSte7HnW3Na2k",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
