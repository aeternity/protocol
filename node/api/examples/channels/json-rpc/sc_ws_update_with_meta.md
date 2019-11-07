
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq&role=initiator&state_password=correct%20horse%20battery%20staple
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq&role=responder&state_password=correct%20horse%20battery%20staple
```

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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAXX5xEGNb2TVZxCqP4mnyJoQFQk5HMnkaCWK5Uw0Z/OBhj+qJSJgAKEBKPkV2+paxEKE/LqT4Z2c2boXyhbhFpM7BRzoT0olC1WGJGE5yoAAAgoAhhAGeddIAMCgMa2Ow82N3ii6czJnVTG7Bp9FcbmzOWAx7rJWzE0gjCYBNrERlA==",
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
    "signed_tx": "tx_+MsLAfhCuEDftTqXz0n+Eey8CppVupx3Ipee7YCmePNz/0gaBq4q/TnKmdFkf7XkviWDN3kS1zb16AVQf/+W7cCH8HMpNOkKuIP4gTIBoQF1+cRBjW9k1WcQqj+Jp8iaEBUJORzJ5GgliuVMNGfzgYY/qiUiYAChASj5FdvqWsRChPy6k+GdnNm6F8oW4RaTOwUc6E9KJQtVhiRhOcqAAAIKAIYQBnnXSADAoDGtjsPNjd4ounMyZ1UxuwafRXG5szlgMe6yVsxNIIwmAZ1/RmA="
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
    "channel_id": null,
    "data": {
      "event": "funding_created"
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
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+MsLAfhCuEDftTqXz0n+Eey8CppVupx3Ipee7YCmePNz/0gaBq4q/TnKmdFkf7XkviWDN3kS1zb16AVQf/+W7cCH8HMpNOkKuIP4gTIBoQF1+cRBjW9k1WcQqj+Jp8iaEBUJORzJ5GgliuVMNGfzgYY/qiUiYAChASj5FdvqWsRChPy6k+GdnNm6F8oW4RaTOwUc6E9KJQtVhiRhOcqAAAIKAIYQBnnXSADAoDGtjsPNjd4ounMyZ1UxuwafRXG5szlgMe6yVsxNIIwmAZ1/RmA=",
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
    "signed_tx": "tx_+QENCwH4hLhAo6L7NCk7rEmqLpJTfiYZkE8xNZEYxQKHTUpTseFnJingzoJr5Ffz8zRc/gmzmECDkGkRs/EJl3A1aRON+nO1D7hA37U6l89J/hHsvAqaVbqcdyKXnu2Apnjzc/9IGgauKv05ypnRZH+15L4lgzd5Etc29egFUH//lu3Ah/BzKTTpCriD+IEyAaEBdfnEQY1vZNVnEKo/iafImhAVCTkcyeRoJYrlTDRn84GGP6olImAAoQEo+RXb6lrEQoT8upPhnZzZuhfKFuEWkzsFHOhPSiULVYYkYTnKgAACCgCGEAZ510gAwKAxrY7DzY3eKLpzMmdVMbsGn0VxubM5YDHuslbMTSCMJgEldEuF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAo6L7NCk7rEmqLpJTfiYZkE8xNZEYxQKHTUpTseFnJingzoJr5Ffz8zRc/gmzmECDkGkRs/EJl3A1aRON+nO1D7hA37U6l89J/hHsvAqaVbqcdyKXnu2Apnjzc/9IGgauKv05ypnRZH+15L4lgzd5Etc29egFUH//lu3Ah/BzKTTpCriD+IEyAaEBdfnEQY1vZNVnEKo/iafImhAVCTkcyeRoJYrlTDRn84GGP6olImAAoQEo+RXb6lrEQoT8upPhnZzZuhfKFuEWkzsFHOhPSiULVYYkYTnKgAACCgCGEAZ510gAwKAxrY7DzY3eKLpzMmdVMbsGn0VxubM5YDHuslbMTSCMJgEldEuF",
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
    "channel_id": null,
    "data": {
      "event": "funding_signed"
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAo6L7NCk7rEmqLpJTfiYZkE8xNZEYxQKHTUpTseFnJingzoJr5Ffz8zRc/gmzmECDkGkRs/EJl3A1aRON+nO1D7hA37U6l89J/hHsvAqaVbqcdyKXnu2Apnjzc/9IGgauKv05ypnRZH+15L4lgzd5Etc29egFUH//lu3Ah/BzKTTpCriD+IEyAaEBdfnEQY1vZNVnEKo/iafImhAVCTkcyeRoJYrlTDRn84GGP6olImAAoQEo+RXb6lrEQoT8upPhnZzZuhfKFuEWkzsFHOhPSiULVYYkYTnKgAACCgCGEAZ510gAwKAxrY7DzY3eKLpzMmdVMbsGn0VxubM5YDHuslbMTSCMJgEldEuF",
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAo6L7NCk7rEmqLpJTfiYZkE8xNZEYxQKHTUpTseFnJingzoJr5Ffz8zRc/gmzmECDkGkRs/EJl3A1aRON+nO1D7hA37U6l89J/hHsvAqaVbqcdyKXnu2Apnjzc/9IGgauKv05ypnRZH+15L4lgzd5Etc29egFUH//lu3Ah/BzKTTpCriD+IEyAaEBdfnEQY1vZNVnEKo/iafImhAVCTkcyeRoJYrlTDRn84GGP6olImAAoQEo+RXb6lrEQoT8upPhnZzZuhfKFuEWkzsFHOhPSiULVYYkYTnKgAACCgCGEAZ510gAwKAxrY7DzY3eKLpzMmdVMbsGn0VxubM5YDHuslbMTSCMJgEldEuF",
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAo6L7NCk7rEmqLpJTfiYZkE8xNZEYxQKHTUpTseFnJingzoJr5Ffz8zRc/gmzmECDkGkRs/EJl3A1aRON+nO1D7hA37U6l89J/hHsvAqaVbqcdyKXnu2Apnjzc/9IGgauKv05ypnRZH+15L4lgzd5Etc29egFUH//lu3Ah/BzKTTpCriD+IEyAaEBdfnEQY1vZNVnEKo/iafImhAVCTkcyeRoJYrlTDRn84GGP6olImAAoQEo+RXb6lrEQoT8upPhnZzZuhfKFuEWkzsFHOhPSiULVYYkYTnKgAACCgCGEAZ510gAwKAxrY7DzY3eKLpzMmdVMbsGn0VxubM5YDHuslbMTSCMJgEldEuF",
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
    "to": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "message": {
        "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
        "from": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
        "info": "Hello",
        "to": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
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
    "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "message": {
        "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
        "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
        "info": "Hello back",
        "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423486,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
      "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423486,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
      "balance": 69999999999999
    },
    {
      "account": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "state": "tx_+QENCwH4hLhAo6L7NCk7rEmqLpJTfiYZkE8xNZEYxQKHTUpTseFnJingzoJr5Ffz8zRc/gmzmECDkGkRs/EJl3A1aRON+nO1D7hA37U6l89J/hHsvAqaVbqcdyKXnu2Apnjzc/9IGgauKv05ypnRZH+15L4lgzd5Etc29egFUH//lu3Ah/BzKTTpCriD+IEyAaEBdfnEQY1vZNVnEKo/iafImhAVCTkcyeRoJYrlTDRn84GGP6olImAAoQEo+RXb6lrEQoT8upPhnZzZuhfKFuEWkzsFHOhPSiULVYYkYTnKgAACCgCGEAZ510gAwKAxrY7DzY3eKLpzMmdVMbsGn0VxubM5YDHuslbMTSCMJgEldEuF"
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "state": "tx_+QENCwH4hLhAo6L7NCk7rEmqLpJTfiYZkE8xNZEYxQKHTUpTseFnJingzoJr5Ffz8zRc/gmzmECDkGkRs/EJl3A1aRON+nO1D7hA37U6l89J/hHsvAqaVbqcdyKXnu2Apnjzc/9IGgauKv05ypnRZH+15L4lgzd5Etc29egFUH//lu3Ah/BzKTTpCriD+IEyAaEBdfnEQY1vZNVnEKo/iafImhAVCTkcyeRoJYrlTDRn84GGP6olImAAoQEo+RXb6lrEQoT8upPhnZzZuhfKFuEWkzsFHOhPSiULVYYkYTnKgAACCgCGEAZ510gAwKAxrY7DzY3eKLpzMmdVMbsGn0VxubM5YDHuslbMTSCMJgEldEuF"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423485,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
      "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423485,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
      "balance": 69999999999999
    },
    {
      "account": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
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
    "from": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
    "meta": [
      "meta 1"
    ],
    "to": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
        "from": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
        "meta": [
          "meta 1"
        ],
        "to": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
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
    "to": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
        "to": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
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
    "from": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
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
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
        "from": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
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
    "from": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
    "meta": 17,
    "to": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
        "from": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
        "meta": 17,
        "to": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
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
    "from": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
    "meta": [
      "meta 1"
    ],
    "to": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvw6KWHatgOAmeZ/eAcwqr6wTGx+4peWnDSkWxICp5EIAqBxeYz1W70C1Un9FW+lC4kZv++37epUjVl3oE7Sx3lkEk1v8wI=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
          "op": "OffChainTransfer",
          "to": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
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
  "id": -576460752303423484,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED6HMGwWZsACCw3gq4UP1vyUfKNKe1tR3nn8VzhZhZfM/txBnqiBj2fObRP7t1oxZy/lU59CTFlNgZcf7DIk8sMuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAKgcXmM9Vu9AtVJ/RVvpQuJGb/vt+3qVI1Zd6BO0sd5ZBLm6a/D"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423484,
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "signed_tx": "tx_+JALAfhCuED6HMGwWZsACCw3gq4UP1vyUfKNKe1tR3nn8VzhZhZfM/txBnqiBj2fObRP7t1oxZy/lU59CTFlNgZcf7DIk8sMuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAKgcXmM9Vu9AtVJ/RVvpQuJGb/vt+3qVI1Zd6BO0sd5ZBLm6a/D",
      "updates": [
        {
          "amount": 1,
          "from": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
          "op": "OffChainTransfer",
          "to": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
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
  "id": -576460752303423483,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBzMCgZECcz40YeQq552DsV1Yf+yZ2jN4C5ZOGH2JYg1binrAbeRtNOebkvRdL7W4X0y6AE+0YT/MUWDuNgnCYCuED6HMGwWZsACCw3gq4UP1vyUfKNKe1tR3nn8VzhZhZfM/txBnqiBj2fObRP7t1oxZy/lU59CTFlNgZcf7DIk8sMuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAKgcXmM9Vu9AtVJ/RVvpQuJGb/vt+3qVI1Zd6BO0sd5ZBI3d7mP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423483,
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "state": "tx_+NILAfiEuEBzMCgZECcz40YeQq552DsV1Yf+yZ2jN4C5ZOGH2JYg1binrAbeRtNOebkvRdL7W4X0y6AE+0YT/MUWDuNgnCYCuED6HMGwWZsACCw3gq4UP1vyUfKNKe1tR3nn8VzhZhZfM/txBnqiBj2fObRP7t1oxZy/lU59CTFlNgZcf7DIk8sMuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAKgcXmM9Vu9AtVJ/RVvpQuJGb/vt+3qVI1Zd6BO0sd5ZBI3d7mP"
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "state": "tx_+NILAfiEuEBzMCgZECcz40YeQq552DsV1Yf+yZ2jN4C5ZOGH2JYg1binrAbeRtNOebkvRdL7W4X0y6AE+0YT/MUWDuNgnCYCuED6HMGwWZsACCw3gq4UP1vyUfKNKe1tR3nn8VzhZhZfM/txBnqiBj2fObRP7t1oxZy/lU59CTFlNgZcf7DIk8sMuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAKgcXmM9Vu9AtVJ/RVvpQuJGb/vt+3qVI1Zd6BO0sd5ZBI3d7mP"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423482,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
      "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423482,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
      "balance": 69999999999998
    },
    {
      "account": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423481,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423481,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBzMCgZECcz40YeQq552DsV1Yf+yZ2jN4C5ZOGH2JYg1binrAbeRtNOebkvRdL7W4X0y6AE+0YT/MUWDuNgnCYCuED6HMGwWZsACCw3gq4UP1vyUfKNKe1tR3nn8VzhZhZfM/txBnqiBj2fObRP7t1oxZy/lU59CTFlNgZcf7DIk8sMuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAKgcXmM9Vu9AtVJ/RVvpQuJGb/vt+3qVI1Zd6BO0sd5ZBI3d7mP",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaB1+cRBjW9k1WcQqj+Jp8iaEBUJORzJ5GgliuVMNGfzgYvKCgEAhj+qJSJf/rDvQAGgKPkV2+paxEKE/LqT4Z2c2boXyhbhFpM7BRzoT0olC1WLygoBAIYkYTnKgAKIht95"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423480,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
      "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423480,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
      "balance": 40000000000002
    },
    {
      "account": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
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
    "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
    "meta": [
      "meta 1"
    ],
    "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
        "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
        "meta": [
          "meta 1"
        ],
        "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
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
    "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
        "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
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
    "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
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
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
        "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
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
    "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
    "meta": 17,
    "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
        "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
        "meta": 17,
        "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
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
    "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
    "meta": [
      "meta 1"
    ],
    "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvw6KWHatgOAmeZ/eAcwqr6wTGx+4peWnDSkWxICp5EIA6AxrY7DzY3eKLpzMmdVMbsGn0VxubM5YDHuslbMTSCMJoMtbB8=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
          "op": "OffChainTransfer",
          "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
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
  "id": -576460752303423479,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA+Lc2B05SRZsRfdTxYdkCR7MLBLWAbvhW0yZibVc6hoUCDhBjms6D1R3uDZkuZbK4gUtA2MBIKx1ClpfV8IasLuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAOgMa2Ow82N3ii6czJnVTG7Bp9FcbmzOWAx7rJWzE0gjCZ0bbeK"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423479,
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA+Lc2B05SRZsRfdTxYdkCR7MLBLWAbvhW0yZibVc6hoUCDhBjms6D1R3uDZkuZbK4gUtA2MBIKx1ClpfV8IasLuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAOgMa2Ow82N3ii6czJnVTG7Bp9FcbmzOWAx7rJWzE0gjCZ0bbeK",
      "updates": [
        {
          "amount": 1,
          "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
          "op": "OffChainTransfer",
          "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
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
  "id": -576460752303423478,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA+Lc2B05SRZsRfdTxYdkCR7MLBLWAbvhW0yZibVc6hoUCDhBjms6D1R3uDZkuZbK4gUtA2MBIKx1ClpfV8IasLuEDaGnGNalp3zqFeTZRktJ6cfhsHJDmb+CfOSr++wGWJN4Vn5/nABmGr8BUk+/H3EpS2c7HbiSBM9tYq7SAHLikEuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAOgMa2Ow82N3ii6czJnVTG7Bp9FcbmzOWAx7rJWzE0gjCZOiF7G"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423478,
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "state": "tx_+NILAfiEuEA+Lc2B05SRZsRfdTxYdkCR7MLBLWAbvhW0yZibVc6hoUCDhBjms6D1R3uDZkuZbK4gUtA2MBIKx1ClpfV8IasLuEDaGnGNalp3zqFeTZRktJ6cfhsHJDmb+CfOSr++wGWJN4Vn5/nABmGr8BUk+/H3EpS2c7HbiSBM9tYq7SAHLikEuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAOgMa2Ow82N3ii6czJnVTG7Bp9FcbmzOWAx7rJWzE0gjCZOiF7G"
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "state": "tx_+NILAfiEuEA+Lc2B05SRZsRfdTxYdkCR7MLBLWAbvhW0yZibVc6hoUCDhBjms6D1R3uDZkuZbK4gUtA2MBIKx1ClpfV8IasLuEDaGnGNalp3zqFeTZRktJ6cfhsHJDmb+CfOSr++wGWJN4Vn5/nABmGr8BUk+/H3EpS2c7HbiSBM9tYq7SAHLikEuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAOgMa2Ow82N3ii6czJnVTG7Bp9FcbmzOWAx7rJWzE0gjCZOiF7G"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423477,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
      "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423477,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
      "balance": 40000000000001
    },
    {
      "account": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423476,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423476,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA+Lc2B05SRZsRfdTxYdkCR7MLBLWAbvhW0yZibVc6hoUCDhBjms6D1R3uDZkuZbK4gUtA2MBIKx1ClpfV8IasLuEDaGnGNalp3zqFeTZRktJ6cfhsHJDmb+CfOSr++wGWJN4Vn5/nABmGr8BUk+/H3EpS2c7HbiSBM9tYq7SAHLikEuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAOgMa2Ow82N3ii6czJnVTG7Bp9FcbmzOWAx7rJWzE0gjCZOiF7G",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaB1+cRBjW9k1WcQqj+Jp8iaEBUJORzJ5GgliuVMNGfzgYvKCgEAhj+qJSJf/7DvQAGgKPkV2+paxEKE/LqT4Z2c2boXyhbhFpM7BRzoT0olC1WLygoBAIYkYTnKgAEKyAQR"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423475,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
      "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423475,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
      "balance": 40000000000001
    },
    {
      "account": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
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
    "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
    "meta": [
      "meta 1"
    ],
    "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
        "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
        "meta": [
          "meta 1"
        ],
        "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
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
    "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
        "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
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
    "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
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
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
        "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
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
    "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
    "meta": 17,
    "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
        "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
        "meta": 17,
        "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
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
    "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
    "meta": [
      "meta 1"
    ],
    "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvw6KWHatgOAmeZ/eAcwqr6wTGx+4peWnDSkWxICp5EIBKBNmJP/z0xoP5ziCsI6zZLPHpVrCxMBqimWKroAGOs8WqRFLUU=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
          "op": "OffChainTransfer",
          "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
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
  "id": -576460752303423474,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBzLR3FxZPOVAHz2vEhQav6r+lAR7F34ejem2e5jF9I84ww+mQDNqeaW8drkrp/ddShZJGwu4ff/44iUdKWknIBuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCASgTZiT/89MaD+c4grCOs2Szx6VawsTAaopliq6ABjrPFoUV0BU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423474,
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBzLR3FxZPOVAHz2vEhQav6r+lAR7F34ejem2e5jF9I84ww+mQDNqeaW8drkrp/ddShZJGwu4ff/44iUdKWknIBuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCASgTZiT/89MaD+c4grCOs2Szx6VawsTAaopliq6ABjrPFoUV0BU",
      "updates": [
        {
          "amount": 1,
          "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
          "op": "OffChainTransfer",
          "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
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
  "id": -576460752303423473,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBzLR3FxZPOVAHz2vEhQav6r+lAR7F34ejem2e5jF9I84ww+mQDNqeaW8drkrp/ddShZJGwu4ff/44iUdKWknIBuECPfVDul0SHciTPhDKpjeX0DmKbsKmPo0F2wKtuH9CSQ+iqQrsk5JVJJ7UL3B8XjEo2Qx6Xv75kqvNDsTyK4+ANuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCASgTZiT/89MaD+c4grCOs2Szx6VawsTAaopliq6ABjrPFqbJai5"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423473,
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "state": "tx_+NILAfiEuEBzLR3FxZPOVAHz2vEhQav6r+lAR7F34ejem2e5jF9I84ww+mQDNqeaW8drkrp/ddShZJGwu4ff/44iUdKWknIBuECPfVDul0SHciTPhDKpjeX0DmKbsKmPo0F2wKtuH9CSQ+iqQrsk5JVJJ7UL3B8XjEo2Qx6Xv75kqvNDsTyK4+ANuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCASgTZiT/89MaD+c4grCOs2Szx6VawsTAaopliq6ABjrPFqbJai5"
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "state": "tx_+NILAfiEuEBzLR3FxZPOVAHz2vEhQav6r+lAR7F34ejem2e5jF9I84ww+mQDNqeaW8drkrp/ddShZJGwu4ff/44iUdKWknIBuECPfVDul0SHciTPhDKpjeX0DmKbsKmPo0F2wKtuH9CSQ+iqQrsk5JVJJ7UL3B8XjEo2Qx6Xv75kqvNDsTyK4+ANuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCASgTZiT/89MaD+c4grCOs2Szx6VawsTAaopliq6ABjrPFqbJai5"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423472,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
      "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423472,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
      "balance": 40000000000000
    },
    {
      "account": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423471,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423471,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBzLR3FxZPOVAHz2vEhQav6r+lAR7F34ejem2e5jF9I84ww+mQDNqeaW8drkrp/ddShZJGwu4ff/44iUdKWknIBuECPfVDul0SHciTPhDKpjeX0DmKbsKmPo0F2wKtuH9CSQ+iqQrsk5JVJJ7UL3B8XjEo2Qx6Xv75kqvNDsTyK4+ANuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCASgTZiT/89MaD+c4grCOs2Szx6VawsTAaopliq6ABjrPFqbJai5",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaB1+cRBjW9k1WcQqj+Jp8iaEBUJORzJ5GgliuVMNGfzgYvKCgEAhj+qJSJgALDvQAGgKPkV2+paxEKE/LqT4Z2c2boXyhbhFpM7BRzoT0olC1WLygoBAIYkYTnKgADmzFOS"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423470,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
      "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423470,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
      "balance": 70000000000000
    },
    {
      "account": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
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
    "from": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
    "meta": [
      "meta 1"
    ],
    "to": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
        "from": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
        "meta": [
          "meta 1"
        ],
        "to": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
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
    "to": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
        "to": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
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
    "from": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
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
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
        "from": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
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
    "from": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
    "meta": 17,
    "to": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
        "from": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
        "meta": 17,
        "to": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
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
    "from": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
    "meta": [
      "meta 1"
    ],
    "to": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvw6KWHatgOAmeZ/eAcwqr6wTGx+4peWnDSkWxICp5EIBaAxrY7DzY3eKLpzMmdVMbsGn0VxubM5YDHuslbMTSCMJtX6h+k=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
          "op": "OffChainTransfer",
          "to": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
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
  "id": -576460752303423469,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBX9MnYk+k9HAhX6f6XZgQtJ2FKD9ChHjKjNeefle5j7n24dPCWqejXGfB6Dwm9P3cu/Ik7TaeERYmQp+Myh4UIuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAWgMa2Ow82N3ii6czJnVTG7Bp9FcbmzOWAx7rJWzE0gjCZNI92q"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423469,
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBX9MnYk+k9HAhX6f6XZgQtJ2FKD9ChHjKjNeefle5j7n24dPCWqejXGfB6Dwm9P3cu/Ik7TaeERYmQp+Myh4UIuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAWgMa2Ow82N3ii6czJnVTG7Bp9FcbmzOWAx7rJWzE0gjCZNI92q",
      "updates": [
        {
          "amount": 1,
          "from": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
          "op": "OffChainTransfer",
          "to": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
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
  "id": -576460752303423468,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAY6Y7ApWGQIOYIbKLjJSaDVjYYJUHzeGcxvPrnLU5Lx7a1dNINflWWFCrL57V5Xdo6Ed2TvfQPNihK2BsWz/kNuEBX9MnYk+k9HAhX6f6XZgQtJ2FKD9ChHjKjNeefle5j7n24dPCWqejXGfB6Dwm9P3cu/Ik7TaeERYmQp+Myh4UIuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAWgMa2Ow82N3ii6czJnVTG7Bp9FcbmzOWAx7rJWzE0gjCY0B8Mw"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423468,
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "state": "tx_+NILAfiEuEAY6Y7ApWGQIOYIbKLjJSaDVjYYJUHzeGcxvPrnLU5Lx7a1dNINflWWFCrL57V5Xdo6Ed2TvfQPNihK2BsWz/kNuEBX9MnYk+k9HAhX6f6XZgQtJ2FKD9ChHjKjNeefle5j7n24dPCWqejXGfB6Dwm9P3cu/Ik7TaeERYmQp+Myh4UIuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAWgMa2Ow82N3ii6czJnVTG7Bp9FcbmzOWAx7rJWzE0gjCY0B8Mw"
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "state": "tx_+NILAfiEuEAY6Y7ApWGQIOYIbKLjJSaDVjYYJUHzeGcxvPrnLU5Lx7a1dNINflWWFCrL57V5Xdo6Ed2TvfQPNihK2BsWz/kNuEBX9MnYk+k9HAhX6f6XZgQtJ2FKD9ChHjKjNeefle5j7n24dPCWqejXGfB6Dwm9P3cu/Ik7TaeERYmQp+Myh4UIuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAWgMa2Ow82N3ii6czJnVTG7Bp9FcbmzOWAx7rJWzE0gjCY0B8Mw"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423467,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
      "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423467,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
      "balance": 69999999999999
    },
    {
      "account": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423466,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423466,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAY6Y7ApWGQIOYIbKLjJSaDVjYYJUHzeGcxvPrnLU5Lx7a1dNINflWWFCrL57V5Xdo6Ed2TvfQPNihK2BsWz/kNuEBX9MnYk+k9HAhX6f6XZgQtJ2FKD9ChHjKjNeefle5j7n24dPCWqejXGfB6Dwm9P3cu/Ik7TaeERYmQp+Myh4UIuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAWgMa2Ow82N3ii6czJnVTG7Bp9FcbmzOWAx7rJWzE0gjCY0B8Mw",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaB1+cRBjW9k1WcQqj+Jp8iaEBUJORzJ5GgliuVMNGfzgYvKCgEAhj+qJSJf/7DvQAGgKPkV2+paxEKE/LqT4Z2c2boXyhbhFpM7BRzoT0olC1WLygoBAIYkYTnKgAEKyAQR"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423465,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
      "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423465,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
      "balance": 40000000000001
    },
    {
      "account": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
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
    "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
    "meta": [
      "meta 1"
    ],
    "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
        "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
        "meta": [
          "meta 1"
        ],
        "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
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
    "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
        "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
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
    "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
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
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
        "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
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
    "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
    "meta": 17,
    "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
        "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
        "meta": 17,
        "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
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
    "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
    "meta": [
      "meta 1"
    ],
    "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvw6KWHatgOAmeZ/eAcwqr6wTGx+4peWnDSkWxICp5EIBqBNmJP/z0xoP5ziCsI6zZLPHpVrCxMBqimWKroAGOs8Wulv6ak=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
          "op": "OffChainTransfer",
          "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
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
  "id": -576460752303423464,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBcll7vW1/yNrl9w7Zq11DbvQkvYOn5qbpueXZnyikpgYbyjmyitDCkggnR4ByTON+obb4fRBeL14PqMAAPO2YDuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAagTZiT/89MaD+c4grCOs2Szx6VawsTAaopliq6ABjrPFrbd9Na"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423464,
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBcll7vW1/yNrl9w7Zq11DbvQkvYOn5qbpueXZnyikpgYbyjmyitDCkggnR4ByTON+obb4fRBeL14PqMAAPO2YDuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAagTZiT/89MaD+c4grCOs2Szx6VawsTAaopliq6ABjrPFrbd9Na",
      "updates": [
        {
          "amount": 1,
          "from": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
          "op": "OffChainTransfer",
          "to": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
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
  "id": -576460752303423463,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBcll7vW1/yNrl9w7Zq11DbvQkvYOn5qbpueXZnyikpgYbyjmyitDCkggnR4ByTON+obb4fRBeL14PqMAAPO2YDuECjtvLEIl2lQq4OCVQmGgEbc4cgV5L2Pv4+QbKAnT0hVvGOKE/ItFClhTYEmhf6iHLR7Ce2CUWnORAy+EdTgjQHuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAagTZiT/89MaD+c4grCOs2Szx6VawsTAaopliq6ABjrPFpVMPAN"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423463,
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "state": "tx_+NILAfiEuEBcll7vW1/yNrl9w7Zq11DbvQkvYOn5qbpueXZnyikpgYbyjmyitDCkggnR4ByTON+obb4fRBeL14PqMAAPO2YDuECjtvLEIl2lQq4OCVQmGgEbc4cgV5L2Pv4+QbKAnT0hVvGOKE/ItFClhTYEmhf6iHLR7Ce2CUWnORAy+EdTgjQHuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAagTZiT/89MaD+c4grCOs2Szx6VawsTAaopliq6ABjrPFpVMPAN"
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "state": "tx_+NILAfiEuEBcll7vW1/yNrl9w7Zq11DbvQkvYOn5qbpueXZnyikpgYbyjmyitDCkggnR4ByTON+obb4fRBeL14PqMAAPO2YDuECjtvLEIl2lQq4OCVQmGgEbc4cgV5L2Pv4+QbKAnT0hVvGOKE/ItFClhTYEmhf6iHLR7Ce2CUWnORAy+EdTgjQHuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAagTZiT/89MaD+c4grCOs2Szx6VawsTAaopliq6ABjrPFpVMPAN"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423462,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
      "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423462,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_K3boWaT4GXP2hENENPnVnCmJSHjeHbHaszkJQsNGuTWyD4PMq",
      "balance": 40000000000000
    },
    {
      "account": "ak_txXinM233n3S1TiLArz5NmGTQtxZoYnia29HU4dPjVS2bthQe",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423461,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423461,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBcll7vW1/yNrl9w7Zq11DbvQkvYOn5qbpueXZnyikpgYbyjmyitDCkggnR4ByTON+obb4fRBeL14PqMAAPO2YDuECjtvLEIl2lQq4OCVQmGgEbc4cgV5L2Pv4+QbKAnT0hVvGOKE/ItFClhTYEmhf6iHLR7Ce2CUWnORAy+EdTgjQHuEj4RjkCoQb8Oilh2rYDgJnmf3gHMKq+sExsfuKXlpw0pFsSAqeRCAagTZiT/89MaD+c4grCOs2Szx6VawsTAaopliq6ABjrPFpVMPAN",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaB1+cRBjW9k1WcQqj+Jp8iaEBUJORzJ5GgliuVMNGfzgYvKCgEAhj+qJSJgALDvQAGgKPkV2+paxEKE/LqT4Z2c2boXyhbhFpM7BRzoT0olC1WLygoBAIYkYTnKgADmzFOS"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423460,
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
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423460,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423459,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
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
    "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection
```

```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v5ohWNML7JzXkbpac69is9QzCn2YhYBhXWHrwnBirXQsDeSPB",
  "id": -576460752303423459,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```
