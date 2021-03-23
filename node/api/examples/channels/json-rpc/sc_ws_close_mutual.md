
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=246913579753086&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=246913579753086&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=initiator
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
      "fsm_id": "ba_tZGoJGoLBZ7OJQugTi1L/AykJLQGKAUodeowYhs8qX7ZTuoM"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=246913579753086&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=246913579753086&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=responder
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
      "fsm_id": "ba_xwoYP9kyewVypdglW1s6grxOJLLFislIRG2LBxHMa39x7AK4"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+BhuCRDDYefqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGG4JEMNh5+AgoAhhAGeddIAMCgPGIN9xHth97MX+yEr7qttDn+FuW/WeUCUUyhhoigLIQJqcF3oA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423311,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECkMEHVKBJtzjzOManRXsnwl+rohvvSBfmGArq8iPezGg79GgyVk9BTpuQ4R0m3zQS05kSPzfep8RXocVg79lwBuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYbgkQw2Hn6hAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhuCRDDYefgIKAIYQBnnXSADAoDxiDfcR7YfezF/shK+6rbQ5/hblv1nlAlFMoYaIoCyECcxZjeU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423311,
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_xwoYP9kyewVypdglW1s6grxOJLLFislIRG2LBxHMa39x7AK4"
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
    "data": {
      "signed_tx": "tx_+MsLAfhCuECkMEHVKBJtzjzOManRXsnwl+rohvvSBfmGArq8iPezGg79GgyVk9BTpuQ4R0m3zQS05kSPzfep8RXocVg79lwBuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYbgkQw2Hn6hAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhuCRDDYefgIKAIYQBnnXSADAoDxiDfcR7YfezF/shK+6rbQ5/hblv1nlAlFMoYaIoCyECcxZjeU=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423310,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAP80aO6K9Nlz/CLd3ZeUVmJ23gzfCRgQ4hmwNaYBKjnOfLdOAkUcSr70TRlcXcFYiduWG/HITb5+8kDxu95CWDrhApDBB1SgSbc48zjGp0V7J8Jfq6Ib70gX5hgK6vIj3sxoO/RoMlZPQU6bkOEdJt80EtOZEj833qfEV6HFYO/ZcAbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GG4JEMNh5+oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYbgkQw2Hn4CCgCGEAZ510gAwKA8Yg33Ee2H3sxf7ISvuq20Of4W5b9Z5QJRTKGGiKAshAnt2H4w"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
  "id": -576460752303423310,
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAP80aO6K9Nlz/CLd3ZeUVmJ23gzfCRgQ4hmwNaYBKjnOfLdOAkUcSr70TRlcXcFYiduWG/HITb5+8kDxu95CWDrhApDBB1SgSbc48zjGp0V7J8Jfq6Ib70gX5hgK6vIj3sxoO/RoMlZPQU6bkOEdJt80EtOZEj833qfEV6HFYO/ZcAbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GG4JEMNh5+oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYbgkQw2Hn4CCgCGEAZ510gAwKA8Yg33Ee2H3sxf7ISvuq20Of4W5b9Z5QJRTKGGiKAshAnt2H4w",
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_tZGoJGoLBZ7OJQugTi1L/AykJLQGKAUodeowYhs8qX7ZTuoM"
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAP80aO6K9Nlz/CLd3ZeUVmJ23gzfCRgQ4hmwNaYBKjnOfLdOAkUcSr70TRlcXcFYiduWG/HITb5+8kDxu95CWDrhApDBB1SgSbc48zjGp0V7J8Jfq6Ib70gX5hgK6vIj3sxoO/RoMlZPQU6bkOEdJt80EtOZEj833qfEV6HFYO/ZcAbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GG4JEMNh5+oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYbgkQw2Hn4CCgCGEAZ510gAwKA8Yg33Ee2H3sxf7ISvuq20Of4W5b9Z5QJRTKGGiKAshAnt2H4w",
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAP80aO6K9Nlz/CLd3ZeUVmJ23gzfCRgQ4hmwNaYBKjnOfLdOAkUcSr70TRlcXcFYiduWG/HITb5+8kDxu95CWDrhApDBB1SgSbc48zjGp0V7J8Jfq6Ib70gX5hgK6vIj3sxoO/RoMlZPQU6bkOEdJt80EtOZEj833qfEV6HFYO/ZcAbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GG4JEMNh5+oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYbgkQw2Hn4CCgCGEAZ510gAwKA8Yg33Ee2H3sxf7ISvuq20Of4W5b9Z5QJRTKGGiKAshAnt2H4w",
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAP80aO6K9Nlz/CLd3ZeUVmJ23gzfCRgQ4hmwNaYBKjnOfLdOAkUcSr70TRlcXcFYiduWG/HITb5+8kDxu95CWDrhApDBB1SgSbc48zjGp0V7J8Jfq6Ib70gX5hgK6vIj3sxoO/RoMlZPQU6bkOEdJt80EtOZEj833qfEV6HFYO/ZcAbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GG4JEMNh5+oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYbgkQw2Hn4CCgCGEAZ510gAwKA8Yg33Ee2H3sxf7ISvuq20Of4W5b9Z5QJRTKGGiKAshAnt2H4w",
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
    "data": {
      "message": {
        "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
    "data": {
      "message": {
        "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
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
  "id": -576460752303423309,
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
  "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
  "id": -576460752303423309,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 246913579753085
    },
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 246913579753087
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
    "data": {
      "state": "tx_+QENCwH4hLhAP80aO6K9Nlz/CLd3ZeUVmJ23gzfCRgQ4hmwNaYBKjnOfLdOAkUcSr70TRlcXcFYiduWG/HITb5+8kDxu95CWDrhApDBB1SgSbc48zjGp0V7J8Jfq6Ib70gX5hgK6vIj3sxoO/RoMlZPQU6bkOEdJt80EtOZEj833qfEV6HFYO/ZcAbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GG4JEMNh5+oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYbgkQw2Hn4CCgCGEAZ510gAwKA8Yg33Ee2H3sxf7ISvuq20Of4W5b9Z5QJRTKGGiKAshAnt2H4w"
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
    "data": {
      "state": "tx_+QENCwH4hLhAP80aO6K9Nlz/CLd3ZeUVmJ23gzfCRgQ4hmwNaYBKjnOfLdOAkUcSr70TRlcXcFYiduWG/HITb5+8kDxu95CWDrhApDBB1SgSbc48zjGp0V7J8Jfq6Ib70gX5hgK6vIj3sxoO/RoMlZPQU6bkOEdJt80EtOZEj833qfEV6HFYO/ZcAbiD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GG4JEMNh5+oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYbgkQw2Hn4CCgCGEAZ510gAwKA8Yg33Ee2H3sxf7ISvuq20Of4W5b9Z5QJRTKGGiKAshAnt2H4w"
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBp+hjqCjkzAQsKSFrB1YbBnfpreKWPpmcgDM+7zViow/oQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYbY4aD2in2G2OGg9op/AIYPXtZ/KAAK+oAP1A==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423308,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEAeM8kWakysUQ4/q2Jpnp8UtRj6Du9iJTyKhUTZT8AULHBx+/hAzz0nCYSyztmAjPxK2OG+79KIuvzPcj+V6ooKuF/4XTUBoQafoY6go5MwELCkhawdWGwZ36a3ilj6ZnIAzPu81YqMP6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GG2OGg9op9htjhoPaKfwCGD17WfygACtYYvSE="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
  "id": -576460752303423308,
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEAeM8kWakysUQ4/q2Jpnp8UtRj6Du9iJTyKhUTZT8AULHBx+/hAzz0nCYSyztmAjPxK2OG+79KIuvzPcj+V6ooKuF/4XTUBoQafoY6go5MwELCkhawdWGwZ36a3ilj6ZnIAzPu81YqMP6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GG2OGg9op9htjhoPaKfwCGD17WfygACtYYvSE=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423307,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEAeM8kWakysUQ4/q2Jpnp8UtRj6Du9iJTyKhUTZT8AULHBx+/hAzz0nCYSyztmAjPxK2OG+79KIuvzPcj+V6ooKuECQXJ0kc4uV8yIJrCxPqc04PbPmJD1ehSrPhiCoPopkLC3tNRgPSvwlOyAvVvDmjBFgFYAh6B7q7v5pYNxiywYJuF/4XTUBoQafoY6go5MwELCkhawdWGwZ36a3ilj6ZnIAzPu81YqMP6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GG2OGg9op9htjhoPaKfwCGD17WfygACqkyIS8="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
  "id": -576460752303423307,
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAeM8kWakysUQ4/q2Jpnp8UtRj6Du9iJTyKhUTZT8AULHBx+/hAzz0nCYSyztmAjPxK2OG+79KIuvzPcj+V6ooKuECQXJ0kc4uV8yIJrCxPqc04PbPmJD1ehSrPhiCoPopkLC3tNRgPSvwlOyAvVvDmjBFgFYAh6B7q7v5pYNxiywYJuF/4XTUBoQafoY6go5MwELCkhawdWGwZ36a3ilj6ZnIAzPu81YqMP6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GG2OGg9op9htjhoPaKfwCGD17WfygACqkyIS8=",
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAeM8kWakysUQ4/q2Jpnp8UtRj6Du9iJTyKhUTZT8AULHBx+/hAzz0nCYSyztmAjPxK2OG+79KIuvzPcj+V6ooKuECQXJ0kc4uV8yIJrCxPqc04PbPmJD1ehSrPhiCoPopkLC3tNRgPSvwlOyAvVvDmjBFgFYAh6B7q7v5pYNxiywYJuF/4XTUBoQafoY6go5MwELCkhawdWGwZ36a3ilj6ZnIAzPu81YqMP6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GG2OGg9op9htjhoPaKfwCGD17WfygACqkyIS8=",
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAeM8kWakysUQ4/q2Jpnp8UtRj6Du9iJTyKhUTZT8AULHBx+/hAzz0nCYSyztmAjPxK2OG+79KIuvzPcj+V6ooKuECQXJ0kc4uV8yIJrCxPqc04PbPmJD1ehSrPhiCoPopkLC3tNRgPSvwlOyAvVvDmjBFgFYAh6B7q7v5pYNxiywYJuF/4XTUBoQafoY6go5MwELCkhawdWGwZ36a3ilj6ZnIAzPu81YqMP6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GG2OGg9op9htjhoPaKfwCGD17WfygACqkyIS8=",
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAeM8kWakysUQ4/q2Jpnp8UtRj6Du9iJTyKhUTZT8AULHBx+/hAzz0nCYSyztmAjPxK2OG+79KIuvzPcj+V6ooKuECQXJ0kc4uV8yIJrCxPqc04PbPmJD1ehSrPhiCoPopkLC3tNRgPSvwlOyAvVvDmjBFgFYAh6B7q7v5pYNxiywYJuF/4XTUBoQafoY6go5MwELCkhawdWGwZ36a3ilj6ZnIAzPu81YqMP6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GG2OGg9op9htjhoPaKfwCGD17WfygACqkyIS8=",
      "type": "channel_close_mutual_tx"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=246913579753086&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=246913579753086&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=initiator
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
      "fsm_id": "ba_iQCitbFn1KwYUo3F62EPG3xUs5Qnj4RNqpzcFY2FAF9VI+vP"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=246913579753086&initiator_id=ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=246913579753086&responder_id=ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt&role=responder
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
      "fsm_id": "ba_PrQtJA9HHYj6mkHq7BsbyR3hXqOZUV+guAXQcec24eP8NzIn"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWSuDghi3tNLOnvuIVm5FIbC9Ikodk2/E4CKiamLla+BhuCRDDYefqEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGG4JEMNh5+AgoAhhAGeddIAMCgPGIN9xHth97MX+yEr7qttDn+FuW/WeUCUUyhhoigLIQLtQh97g==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423306,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBh59ISPv+TDpIfWA1pp8V/K5HYnvIV3baw8LWJWmpyCOWhKoLEoQhWsFm6v5alUdzhwuIRW6171L2IakeN56wKuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYbgkQw2Hn6hAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhuCRDDYefgIKAIYQBnnXSADAoDxiDfcR7YfezF/shK+6rbQ5/hblv1nlAlFMoYaIoCyECy87nRs="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423306,
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_PrQtJA9HHYj6mkHq7BsbyR3hXqOZUV+guAXQcec24eP8NzIn"
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEBh59ISPv+TDpIfWA1pp8V/K5HYnvIV3baw8LWJWmpyCOWhKoLEoQhWsFm6v5alUdzhwuIRW6171L2IakeN56wKuIP4gTIBoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgYbgkQw2Hn6hAZCzLjDKnaeAHIP2nS7DUNlYpkAMioUL3aUU7q4MKnChhuCRDDYefgIKAIYQBnnXSADAoDxiDfcR7YfezF/shK+6rbQ5/hblv1nlAlFMoYaIoCyECy87nRs=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423305,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAYefSEj7/kw6SH1gNaafFfyuR2J7yFd22sPC1iVpqcgjloSqCxKEIVrBZur+WpVHc4cLiEVute9S9iGpHjeesCrhA+ep/5U3aVb8l+ocla1ewgI/P1jkyLFjHzYUvplHVWg5Q9Jp/Czld5SJ7W9PoeClXlaJCbmG3pHbIegZuA/19A7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GG4JEMNh5+oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYbgkQw2Hn4CCgCGEAZ510gAwKA8Yg33Ee2H3sxf7ISvuq20Of4W5b9Z5QJRTKGGiKAshAu/j9YR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
  "id": -576460752303423305,
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAYefSEj7/kw6SH1gNaafFfyuR2J7yFd22sPC1iVpqcgjloSqCxKEIVrBZur+WpVHc4cLiEVute9S9iGpHjeesCrhA+ep/5U3aVb8l+ocla1ewgI/P1jkyLFjHzYUvplHVWg5Q9Jp/Czld5SJ7W9PoeClXlaJCbmG3pHbIegZuA/19A7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GG4JEMNh5+oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYbgkQw2Hn4CCgCGEAZ510gAwKA8Yg33Ee2H3sxf7ISvuq20Of4W5b9Z5QJRTKGGiKAshAu/j9YR",
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_iQCitbFn1KwYUo3F62EPG3xUs5Qnj4RNqpzcFY2FAF9VI+vP"
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAYefSEj7/kw6SH1gNaafFfyuR2J7yFd22sPC1iVpqcgjloSqCxKEIVrBZur+WpVHc4cLiEVute9S9iGpHjeesCrhA+ep/5U3aVb8l+ocla1ewgI/P1jkyLFjHzYUvplHVWg5Q9Jp/Czld5SJ7W9PoeClXlaJCbmG3pHbIegZuA/19A7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GG4JEMNh5+oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYbgkQw2Hn4CCgCGEAZ510gAwKA8Yg33Ee2H3sxf7ISvuq20Of4W5b9Z5QJRTKGGiKAshAu/j9YR",
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAYefSEj7/kw6SH1gNaafFfyuR2J7yFd22sPC1iVpqcgjloSqCxKEIVrBZur+WpVHc4cLiEVute9S9iGpHjeesCrhA+ep/5U3aVb8l+ocla1ewgI/P1jkyLFjHzYUvplHVWg5Q9Jp/Czld5SJ7W9PoeClXlaJCbmG3pHbIegZuA/19A7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GG4JEMNh5+oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYbgkQw2Hn4CCgCGEAZ510gAwKA8Yg33Ee2H3sxf7ISvuq20Of4W5b9Z5QJRTKGGiKAshAu/j9YR",
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAYefSEj7/kw6SH1gNaafFfyuR2J7yFd22sPC1iVpqcgjloSqCxKEIVrBZur+WpVHc4cLiEVute9S9iGpHjeesCrhA+ep/5U3aVb8l+ocla1ewgI/P1jkyLFjHzYUvplHVWg5Q9Jp/Czld5SJ7W9PoeClXlaJCbmG3pHbIegZuA/19A7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GG4JEMNh5+oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYbgkQw2Hn4CCgCGEAZ510gAwKA8Yg33Ee2H3sxf7ISvuq20Of4W5b9Z5QJRTKGGiKAshAu/j9YR",
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

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
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
    "channel_id": "ch_2DJZakV2rq1XSoiM1nXQaWnqW24Wzj4SZwrSdNnruMyv977jMW",
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
  "method": "channels.message",
  "params": {
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
    "data": {
      "message": {
        "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
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

#### responder closes WebSocket connection

#### initiator closes WebSocket connection

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
    "data": {
      "message": {
        "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
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
  "id": -576460752303423304,
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
  "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
  "id": -576460752303423304,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 246913579753085
    },
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 246913579753087
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
    "data": {
      "state": "tx_+QENCwH4hLhAYefSEj7/kw6SH1gNaafFfyuR2J7yFd22sPC1iVpqcgjloSqCxKEIVrBZur+WpVHc4cLiEVute9S9iGpHjeesCrhA+ep/5U3aVb8l+ocla1ewgI/P1jkyLFjHzYUvplHVWg5Q9Jp/Czld5SJ7W9PoeClXlaJCbmG3pHbIegZuA/19A7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GG4JEMNh5+oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYbgkQw2Hn4CCgCGEAZ510gAwKA8Yg33Ee2H3sxf7ISvuq20Of4W5b9Z5QJRTKGGiKAshAu/j9YR"
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
    "data": {
      "state": "tx_+QENCwH4hLhAYefSEj7/kw6SH1gNaafFfyuR2J7yFd22sPC1iVpqcgjloSqCxKEIVrBZur+WpVHc4cLiEVute9S9iGpHjeesCrhA+ep/5U3aVb8l+ocla1ewgI/P1jkyLFjHzYUvplHVWg5Q9Jp/Czld5SJ7W9PoeClXlaJCbmG3pHbIegZuA/19A7iD+IEyAaEBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GG4JEMNh5+oQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYbgkQw2Hn4CCgCGEAZ510gAwKA8Yg33Ee2H3sxf7ISvuq20Of4W5b9Z5QJRTKGGiKAshAu/j9YR"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBn4gAOJePHHekeIHeYsImXbn2nSrfxs1WoWy/MERf7YJoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYbY4aD2in2G2OGg9op/AIYPXtZ/KAADpFtJOg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423303,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEA1rYBpSvpp9chvd2KKvKvWytyYl6ypRDT0WV6MA/tMvbNd6wjiGl55V0y6DsfWrMiilEtQV4S9/2KkoT++5zcGuF/4XTUBoQZ+IADiXjxx3pHiB3mLCJl259p0q38bNVqFsvzBEX+2CaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGG2OGg9op9htjhoPaKfwCGD17WfygAA2Q5vok="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
  "id": -576460752303423303,
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
    "data": {
      "event": "shutdown"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEA1rYBpSvpp9chvd2KKvKvWytyYl6ypRDT0WV6MA/tMvbNd6wjiGl55V0y6DsfWrMiilEtQV4S9/2KkoT++5zcGuF/4XTUBoQZ+IADiXjxx3pHiB3mLCJl259p0q38bNVqFsvzBEX+2CaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGG2OGg9op9htjhoPaKfwCGD17WfygAA2Q5vok=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423302,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEA1rYBpSvpp9chvd2KKvKvWytyYl6ypRDT0WV6MA/tMvbNd6wjiGl55V0y6DsfWrMiilEtQV4S9/2KkoT++5zcGuEDINYQlbxDi4d/zMLEdr0lmJb5yJg/+3hih1fhY5L8nkoY3J/5PjQByLOk6bLR5suHMnp8zn4WcjmQx4ZdSUIEBuF/4XTUBoQZ+IADiXjxx3pHiB3mLCJl259p0q38bNVqFsvzBEX+2CaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGG2OGg9op9htjhoPaKfwCGD17WfygAA18d70Q="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
  "id": -576460752303423302,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEA1rYBpSvpp9chvd2KKvKvWytyYl6ypRDT0WV6MA/tMvbNd6wjiGl55V0y6DsfWrMiilEtQV4S9/2KkoT++5zcGuEDINYQlbxDi4d/zMLEdr0lmJb5yJg/+3hih1fhY5L8nkoY3J/5PjQByLOk6bLR5suHMnp8zn4WcjmQx4ZdSUIEBuF/4XTUBoQZ+IADiXjxx3pHiB3mLCJl259p0q38bNVqFsvzBEX+2CaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGG2OGg9op9htjhoPaKfwCGD17WfygAA18d70Q=",
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEA1rYBpSvpp9chvd2KKvKvWytyYl6ypRDT0WV6MA/tMvbNd6wjiGl55V0y6DsfWrMiilEtQV4S9/2KkoT++5zcGuEDINYQlbxDi4d/zMLEdr0lmJb5yJg/+3hih1fhY5L8nkoY3J/5PjQByLOk6bLR5suHMnp8zn4WcjmQx4ZdSUIEBuF/4XTUBoQZ+IADiXjxx3pHiB3mLCJl259p0q38bNVqFsvzBEX+2CaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGG2OGg9op9htjhoPaKfwCGD17WfygAA18d70Q=",
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEA1rYBpSvpp9chvd2KKvKvWytyYl6ypRDT0WV6MA/tMvbNd6wjiGl55V0y6DsfWrMiilEtQV4S9/2KkoT++5zcGuEDINYQlbxDi4d/zMLEdr0lmJb5yJg/+3hih1fhY5L8nkoY3J/5PjQByLOk6bLR5suHMnp8zn4WcjmQx4ZdSUIEBuF/4XTUBoQZ+IADiXjxx3pHiB3mLCJl259p0q38bNVqFsvzBEX+2CaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGG2OGg9op9htjhoPaKfwCGD17WfygAA18d70Q=",
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEA1rYBpSvpp9chvd2KKvKvWytyYl6ypRDT0WV6MA/tMvbNd6wjiGl55V0y6DsfWrMiilEtQV4S9/2KkoT++5zcGuEDINYQlbxDi4d/zMLEdr0lmJb5yJg/+3hih1fhY5L8nkoY3J/5PjQByLOk6bLR5suHMnp8zn4WcjmQx4ZdSUIEBuF/4XTUBoQZ+IADiXjxx3pHiB3mLCJl259p0q38bNVqFsvzBEX+2CaEBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKGG2OGg9op9htjhoPaKfwCGD17WfygAA18d70Q=",
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
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
    "channel_id": "ch_xYhGGBxGMdQwbQRafb25uKFkGHJxhJa9R6MHQDWXJdqY68ZrL",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
