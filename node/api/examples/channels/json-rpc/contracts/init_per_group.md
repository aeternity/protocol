
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_XpFyLK8EzYY3jGv6xUW37EKbXyrZHEbt8FcbQBqHYgdURY4id&lock_period=10&port=13216&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_KqsGwv5gbrMZJCTqD5dr596pc6UzmCazZCWjnsVdYfvpzwfRC&role=initiator
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_XpFyLK8EzYY3jGv6xUW37EKbXyrZHEbt8FcbQBqHYgdURY4id&lock_period=10&port=13216&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_KqsGwv5gbrMZJCTqD5dr596pc6UzmCazZCWjnsVdYfvpzwfRC&role=responder
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAUX4AM59ezJQa/ctdGGGRhM0xaW+dIAnj8NUHHHQioVXhj+qJSJgAKEBKsjGDzFPSdU/X7Q7Vtfd23V5gNLy/EH9oAVbQ3V66UGGJGE5yoAAAgoAhhAGeddIAMCgRDkqSyQ7hDBOsiL8q+900t9Vc2g3dB+3YAu4uU3ink8BkXDqnQ==",
      "updates": []
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
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAi0SZFmVmagqfZCSnpNBnKF1IGswsfjnxSFLkElV+zfCnUwPbYsZoMNd79mw4TZk2iKQcLjgbzPKCNrB0i5o0DuIP4gTIBoQFF+ADOfXsyUGv3LXRhhkYTNMWlvnSAJ4/DVBxx0IqFV4Y/qiUiYAChASrIxg8xT0nVP1+0O1bX3dt1eYDS8vxB/aAFW0N1eulBhiRhOcqAAAIKAIYQBnnXSADAoEQ5KkskO4QwTrIi/KvvdNLfVXNoN3Qft2ALuLlN4p5PAczToqk="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
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
      "signed_tx": "tx_+MsLAfhCuEAi0SZFmVmagqfZCSnpNBnKF1IGswsfjnxSFLkElV+zfCnUwPbYsZoMNd79mw4TZk2iKQcLjgbzPKCNrB0i5o0DuIP4gTIBoQFF+ADOfXsyUGv3LXRhhkYTNMWlvnSAJ4/DVBxx0IqFV4Y/qiUiYAChASrIxg8xT0nVP1+0O1bX3dt1eYDS8vxB/aAFW0N1eulBhiRhOcqAAAIKAIYQBnnXSADAoEQ5KkskO4QwTrIi/KvvdNLfVXNoN3Qft2ALuLlN4p5PAczToqk=",
      "updates": []
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
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAFsu//R7KAsnupz+iOcZTVhywUzSEVaaVQzkNXLOzIYGSBdd+/Wtwr9MaxgUpe+SfJ8EPrmbiBClHfiyZUSl7CLhAItEmRZlZmoKn2Qkp6TQZyhdSBrMLH458UhS5BJVfs3wp1MD22LGaDDXe/ZsOE2ZNoikHC44G8zygjawdIuaNA7iD+IEyAaEBRfgAzn17MlBr9y10YYZGEzTFpb50gCePw1QccdCKhVeGP6olImAAoQEqyMYPMU9J1T9ftDtW193bdXmA0vL8Qf2gBVtDdXrpQYYkYTnKgAACCgCGEAZ510gAwKBEOSpLJDuEME6yIvyr73TS31VzaDd0H7dgC7i5TeKeTwE0496E"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
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
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAFsu//R7KAsnupz+iOcZTVhywUzSEVaaVQzkNXLOzIYGSBdd+/Wtwr9MaxgUpe+SfJ8EPrmbiBClHfiyZUSl7CLhAItEmRZlZmoKn2Qkp6TQZyhdSBrMLH458UhS5BJVfs3wp1MD22LGaDDXe/ZsOE2ZNoikHC44G8zygjawdIuaNA7iD+IEyAaEBRfgAzn17MlBr9y10YYZGEzTFpb50gCePw1QccdCKhVeGP6olImAAoQEqyMYPMU9J1T9ftDtW193bdXmA0vL8Qf2gBVtDdXrpQYYkYTnKgAACCgCGEAZ510gAwKBEOSpLJDuEME6yIvyr73TS31VzaDd0H7dgC7i5TeKeTwE0496E",
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
    "channel_id": null,
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAFsu//R7KAsnupz+iOcZTVhywUzSEVaaVQzkNXLOzIYGSBdd+/Wtwr9MaxgUpe+SfJ8EPrmbiBClHfiyZUSl7CLhAItEmRZlZmoKn2Qkp6TQZyhdSBrMLH458UhS5BJVfs3wp1MD22LGaDDXe/ZsOE2ZNoikHC44G8zygjawdIuaNA7iD+IEyAaEBRfgAzn17MlBr9y10YYZGEzTFpb50gCePw1QccdCKhVeGP6olImAAoQEqyMYPMU9J1T9ftDtW193bdXmA0vL8Qf2gBVtDdXrpQYYkYTnKgAACCgCGEAZ510gAwKBEOSpLJDuEME6yIvyr73TS31VzaDd0H7dgC7i5TeKeTwE0496E",
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
    "channel_id": null,
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAFsu//R7KAsnupz+iOcZTVhywUzSEVaaVQzkNXLOzIYGSBdd+/Wtwr9MaxgUpe+SfJ8EPrmbiBClHfiyZUSl7CLhAItEmRZlZmoKn2Qkp6TQZyhdSBrMLH458UhS5BJVfs3wp1MD22LGaDDXe/ZsOE2ZNoikHC44G8zygjawdIuaNA7iD+IEyAaEBRfgAzn17MlBr9y10YYZGEzTFpb50gCePw1QccdCKhVeGP6olImAAoQEqyMYPMU9J1T9ftDtW193bdXmA0vL8Qf2gBVtDdXrpQYYkYTnKgAACCgCGEAZ510gAwKBEOSpLJDuEME6yIvyr73TS31VzaDd0H7dgC7i5TeKeTwE0496E",
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
    "channel_id": null,
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAFsu//R7KAsnupz+iOcZTVhywUzSEVaaVQzkNXLOzIYGSBdd+/Wtwr9MaxgUpe+SfJ8EPrmbiBClHfiyZUSl7CLhAItEmRZlZmoKn2Qkp6TQZyhdSBrMLH458UhS5BJVfs3wp1MD22LGaDDXe/ZsOE2ZNoikHC44G8zygjawdIuaNA7iD+IEyAaEBRfgAzn17MlBr9y10YYZGEzTFpb50gCePw1QccdCKhVeGP6olImAAoQEqyMYPMU9J1T9ftDtW193bdXmA0vL8Qf2gBVtDdXrpQYYkYTnKgAACCgCGEAZ510gAwKBEOSpLJDuEME6yIvyr73TS31VzaDd0H7dgC7i5TeKeTwE0496E",
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
    "to": "ak_KqsGwv5gbrMZJCTqD5dr596pc6UzmCazZCWjnsVdYfvpzwfRC"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_cL9FWbTivkCCp49R9FviYko5597Yve5ZYRvc9uMgRpdo8izVZ",
    "data": {
      "message": {
        "channel_id": "ch_cL9FWbTivkCCp49R9FviYko5597Yve5ZYRvc9uMgRpdo8izVZ",
        "from": "ak_XpFyLK8EzYY3jGv6xUW37EKbXyrZHEbt8FcbQBqHYgdURY4id",
        "info": "Hello",
        "to": "ak_KqsGwv5gbrMZJCTqD5dr596pc6UzmCazZCWjnsVdYfvpzwfRC"
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
    "to": "ak_XpFyLK8EzYY3jGv6xUW37EKbXyrZHEbt8FcbQBqHYgdURY4id"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_cL9FWbTivkCCp49R9FviYko5597Yve5ZYRvc9uMgRpdo8izVZ",
    "data": {
      "message": {
        "channel_id": "ch_cL9FWbTivkCCp49R9FviYko5597Yve5ZYRvc9uMgRpdo8izVZ",
        "from": "ak_KqsGwv5gbrMZJCTqD5dr596pc6UzmCazZCWjnsVdYfvpzwfRC",
        "info": "Hello back",
        "to": "ak_XpFyLK8EzYY3jGv6xUW37EKbXyrZHEbt8FcbQBqHYgdURY4id"
      }
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
      "ak_XpFyLK8EzYY3jGv6xUW37EKbXyrZHEbt8FcbQBqHYgdURY4id",
      "ak_KqsGwv5gbrMZJCTqD5dr596pc6UzmCazZCWjnsVdYfvpzwfRC"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_cL9FWbTivkCCp49R9FviYko5597Yve5ZYRvc9uMgRpdo8izVZ",
  "id": -576460752303423241,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_XpFyLK8EzYY3jGv6xUW37EKbXyrZHEbt8FcbQBqHYgdURY4id",
      "balance": 69999999999999
    },
    {
      "account": "ak_KqsGwv5gbrMZJCTqD5dr596pc6UzmCazZCWjnsVdYfvpzwfRC",
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
    "channel_id": "ch_cL9FWbTivkCCp49R9FviYko5597Yve5ZYRvc9uMgRpdo8izVZ",
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
    "channel_id": "ch_cL9FWbTivkCCp49R9FviYko5597Yve5ZYRvc9uMgRpdo8izVZ",
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
    "channel_id": "ch_cL9FWbTivkCCp49R9FviYko5597Yve5ZYRvc9uMgRpdo8izVZ",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_cL9FWbTivkCCp49R9FviYko5597Yve5ZYRvc9uMgRpdo8izVZ",
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
    "channel_id": "ch_cL9FWbTivkCCp49R9FviYko5597Yve5ZYRvc9uMgRpdo8izVZ",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_cL9FWbTivkCCp49R9FviYko5597Yve5ZYRvc9uMgRpdo8izVZ",
    "data": {
      "event": "open"
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
    "channel_id": "ch_cL9FWbTivkCCp49R9FviYko5597Yve5ZYRvc9uMgRpdo8izVZ",
    "data": {
      "state": "tx_+QENCwH4hLhAFsu//R7KAsnupz+iOcZTVhywUzSEVaaVQzkNXLOzIYGSBdd+/Wtwr9MaxgUpe+SfJ8EPrmbiBClHfiyZUSl7CLhAItEmRZlZmoKn2Qkp6TQZyhdSBrMLH458UhS5BJVfs3wp1MD22LGaDDXe/ZsOE2ZNoikHC44G8zygjawdIuaNA7iD+IEyAaEBRfgAzn17MlBr9y10YYZGEzTFpb50gCePw1QccdCKhVeGP6olImAAoQEqyMYPMU9J1T9ftDtW193bdXmA0vL8Qf2gBVtDdXrpQYYkYTnKgAACCgCGEAZ510gAwKBEOSpLJDuEME6yIvyr73TS31VzaDd0H7dgC7i5TeKeTwE0496E"
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
    "channel_id": "ch_cL9FWbTivkCCp49R9FviYko5597Yve5ZYRvc9uMgRpdo8izVZ",
    "data": {
      "state": "tx_+QENCwH4hLhAFsu//R7KAsnupz+iOcZTVhywUzSEVaaVQzkNXLOzIYGSBdd+/Wtwr9MaxgUpe+SfJ8EPrmbiBClHfiyZUSl7CLhAItEmRZlZmoKn2Qkp6TQZyhdSBrMLH458UhS5BJVfs3wp1MD22LGaDDXe/ZsOE2ZNoikHC44G8zygjawdIuaNA7iD+IEyAaEBRfgAzn17MlBr9y10YYZGEzTFpb50gCePw1QccdCKhVeGP6olImAAoQEqyMYPMU9J1T9ftDtW193bdXmA0vL8Qf2gBVtDdXrpQYYkYTnKgAACCgCGEAZ510gAwKBEOSpLJDuEME6yIvyr73TS31VzaDd0H7dgC7i5TeKeTwE0496E"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_KKPyt9qwFk4uohCuPxt2n6gPDqtY4DsiDbBZBUaPY2C8YN1zB&lock_period=10&port=12652&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2vYkbxgTk7DnP5QaRDRvpapwNBXRwNpDKBLY1DJ9bJDXeYnJcP&role=initiator
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_KKPyt9qwFk4uohCuPxt2n6gPDqtY4DsiDbBZBUaPY2C8YN1zB&lock_period=10&port=12652&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2vYkbxgTk7DnP5QaRDRvpapwNBXRwNpDKBLY1DJ9bJDXeYnJcP&role=responder
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhASmXZUrXyfPCgDpzHfon6sdfxwFceUmlzfEHpesW+YH5hj+qJSJgAKEB/Ug459gG2aimfvLcghEHZNlUitsR4wWL1G+I3MFHg9CGJGE5yoAAAgoAhhAGeddIAMCgwNB1REJFaw9iWiDCyIZFghWL8FS6I1km727CmjWVwl8BnLN6jg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422652,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBUoJFYZ0IfVA8VPYV7MAS+WLQx9w/sqFeSKmdMooDpDq363N+bQsNer47xWEQaddVARAdGIXyJ1OmSTeAWxD4MuIP4gTIBoQEpl2VK18nzwoA6cx36J+rHX8cBXHlJpc3xB6XrFvmB+YY/qiUiYAChAf1IOOfYBtmopn7y3IIRB2TZVIrbEeMFi9RviNzBR4PQhiRhOcqAAAIKAIYQBnnXSADAoMDQdURCRWsPYlogwsiGRYIVi/BUuiNZJu9uwpo1lcJfAfGQdvE="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422652,
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
      "signed_tx": "tx_+MsLAfhCuEBUoJFYZ0IfVA8VPYV7MAS+WLQx9w/sqFeSKmdMooDpDq363N+bQsNer47xWEQaddVARAdGIXyJ1OmSTeAWxD4MuIP4gTIBoQEpl2VK18nzwoA6cx36J+rHX8cBXHlJpc3xB6XrFvmB+YY/qiUiYAChAf1IOOfYBtmopn7y3IIRB2TZVIrbEeMFi9RviNzBR4PQhiRhOcqAAAIKAIYQBnnXSADAoMDQdURCRWsPYlogwsiGRYIVi/BUuiNZJu9uwpo1lcJfAfGQdvE=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422651,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAVKCRWGdCH1QPFT2FezAEvli0MfcP7KhXkipnTKKA6Q6t+tzfm0LDXq+O8VhEGnXVQEQHRiF8idTpkk3gFsQ+DLhAarkXSe9sy9ElBKuweTR3zjlqFDBkdG7zRIuIFUqfkU06+cBzImkN4OczlKgC4uETM0OZ66yzNTxxXU77n2BsCriD+IEyAaEBKZdlStfJ88KAOnMd+ifqx1/HAVx5SaXN8Qel6xb5gfmGP6olImAAoQH9SDjn2AbZqKZ+8tyCEQdk2VSK2xHjBYvUb4jcwUeD0IYkYTnKgAACCgCGEAZ510gAwKDA0HVEQkVrD2JaIMLIhkWCFYvwVLojWSbvbsKaNZXCXwEmxa11"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422651,
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
    "channel_id": null,
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAVKCRWGdCH1QPFT2FezAEvli0MfcP7KhXkipnTKKA6Q6t+tzfm0LDXq+O8VhEGnXVQEQHRiF8idTpkk3gFsQ+DLhAarkXSe9sy9ElBKuweTR3zjlqFDBkdG7zRIuIFUqfkU06+cBzImkN4OczlKgC4uETM0OZ66yzNTxxXU77n2BsCriD+IEyAaEBKZdlStfJ88KAOnMd+ifqx1/HAVx5SaXN8Qel6xb5gfmGP6olImAAoQH9SDjn2AbZqKZ+8tyCEQdk2VSK2xHjBYvUb4jcwUeD0IYkYTnKgAACCgCGEAZ510gAwKDA0HVEQkVrD2JaIMLIhkWCFYvwVLojWSbvbsKaNZXCXwEmxa11",
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
    "channel_id": null,
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAVKCRWGdCH1QPFT2FezAEvli0MfcP7KhXkipnTKKA6Q6t+tzfm0LDXq+O8VhEGnXVQEQHRiF8idTpkk3gFsQ+DLhAarkXSe9sy9ElBKuweTR3zjlqFDBkdG7zRIuIFUqfkU06+cBzImkN4OczlKgC4uETM0OZ66yzNTxxXU77n2BsCriD+IEyAaEBKZdlStfJ88KAOnMd+ifqx1/HAVx5SaXN8Qel6xb5gfmGP6olImAAoQH9SDjn2AbZqKZ+8tyCEQdk2VSK2xHjBYvUb4jcwUeD0IYkYTnKgAACCgCGEAZ510gAwKDA0HVEQkVrD2JaIMLIhkWCFYvwVLojWSbvbsKaNZXCXwEmxa11",
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
    "channel_id": null,
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAVKCRWGdCH1QPFT2FezAEvli0MfcP7KhXkipnTKKA6Q6t+tzfm0LDXq+O8VhEGnXVQEQHRiF8idTpkk3gFsQ+DLhAarkXSe9sy9ElBKuweTR3zjlqFDBkdG7zRIuIFUqfkU06+cBzImkN4OczlKgC4uETM0OZ66yzNTxxXU77n2BsCriD+IEyAaEBKZdlStfJ88KAOnMd+ifqx1/HAVx5SaXN8Qel6xb5gfmGP6olImAAoQH9SDjn2AbZqKZ+8tyCEQdk2VSK2xHjBYvUb4jcwUeD0IYkYTnKgAACCgCGEAZ510gAwKDA0HVEQkVrD2JaIMLIhkWCFYvwVLojWSbvbsKaNZXCXwEmxa11",
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
    "channel_id": null,
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAVKCRWGdCH1QPFT2FezAEvli0MfcP7KhXkipnTKKA6Q6t+tzfm0LDXq+O8VhEGnXVQEQHRiF8idTpkk3gFsQ+DLhAarkXSe9sy9ElBKuweTR3zjlqFDBkdG7zRIuIFUqfkU06+cBzImkN4OczlKgC4uETM0OZ66yzNTxxXU77n2BsCriD+IEyAaEBKZdlStfJ88KAOnMd+ifqx1/HAVx5SaXN8Qel6xb5gfmGP6olImAAoQH9SDjn2AbZqKZ+8tyCEQdk2VSK2xHjBYvUb4jcwUeD0IYkYTnKgAACCgCGEAZ510gAwKDA0HVEQkVrD2JaIMLIhkWCFYvwVLojWSbvbsKaNZXCXwEmxa11",
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
    "to": "ak_2vYkbxgTk7DnP5QaRDRvpapwNBXRwNpDKBLY1DJ9bJDXeYnJcP"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_Lw7acgRZDftvky9DaDmVizHTPtPyoj3fdigY8wGx3ACyYpecS",
    "data": {
      "message": {
        "channel_id": "ch_Lw7acgRZDftvky9DaDmVizHTPtPyoj3fdigY8wGx3ACyYpecS",
        "from": "ak_KKPyt9qwFk4uohCuPxt2n6gPDqtY4DsiDbBZBUaPY2C8YN1zB",
        "info": "Hello",
        "to": "ak_2vYkbxgTk7DnP5QaRDRvpapwNBXRwNpDKBLY1DJ9bJDXeYnJcP"
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
    "to": "ak_KKPyt9qwFk4uohCuPxt2n6gPDqtY4DsiDbBZBUaPY2C8YN1zB"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_Lw7acgRZDftvky9DaDmVizHTPtPyoj3fdigY8wGx3ACyYpecS",
    "data": {
      "message": {
        "channel_id": "ch_Lw7acgRZDftvky9DaDmVizHTPtPyoj3fdigY8wGx3ACyYpecS",
        "from": "ak_2vYkbxgTk7DnP5QaRDRvpapwNBXRwNpDKBLY1DJ9bJDXeYnJcP",
        "info": "Hello back",
        "to": "ak_KKPyt9qwFk4uohCuPxt2n6gPDqtY4DsiDbBZBUaPY2C8YN1zB"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422650,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_KKPyt9qwFk4uohCuPxt2n6gPDqtY4DsiDbBZBUaPY2C8YN1zB",
      "ak_2vYkbxgTk7DnP5QaRDRvpapwNBXRwNpDKBLY1DJ9bJDXeYnJcP"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lw7acgRZDftvky9DaDmVizHTPtPyoj3fdigY8wGx3ACyYpecS",
  "id": -576460752303422650,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_KKPyt9qwFk4uohCuPxt2n6gPDqtY4DsiDbBZBUaPY2C8YN1zB",
      "balance": 69999999999999
    },
    {
      "account": "ak_2vYkbxgTk7DnP5QaRDRvpapwNBXRwNpDKBLY1DJ9bJDXeYnJcP",
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
    "channel_id": "ch_Lw7acgRZDftvky9DaDmVizHTPtPyoj3fdigY8wGx3ACyYpecS",
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
    "channel_id": "ch_Lw7acgRZDftvky9DaDmVizHTPtPyoj3fdigY8wGx3ACyYpecS",
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
    "channel_id": "ch_Lw7acgRZDftvky9DaDmVizHTPtPyoj3fdigY8wGx3ACyYpecS",
    "data": {
      "event": "funding_locked"
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
    "channel_id": "ch_Lw7acgRZDftvky9DaDmVizHTPtPyoj3fdigY8wGx3ACyYpecS",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_Lw7acgRZDftvky9DaDmVizHTPtPyoj3fdigY8wGx3ACyYpecS",
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
    "channel_id": "ch_Lw7acgRZDftvky9DaDmVizHTPtPyoj3fdigY8wGx3ACyYpecS",
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
    "channel_id": "ch_Lw7acgRZDftvky9DaDmVizHTPtPyoj3fdigY8wGx3ACyYpecS",
    "data": {
      "state": "tx_+QENCwH4hLhAVKCRWGdCH1QPFT2FezAEvli0MfcP7KhXkipnTKKA6Q6t+tzfm0LDXq+O8VhEGnXVQEQHRiF8idTpkk3gFsQ+DLhAarkXSe9sy9ElBKuweTR3zjlqFDBkdG7zRIuIFUqfkU06+cBzImkN4OczlKgC4uETM0OZ66yzNTxxXU77n2BsCriD+IEyAaEBKZdlStfJ88KAOnMd+ifqx1/HAVx5SaXN8Qel6xb5gfmGP6olImAAoQH9SDjn2AbZqKZ+8tyCEQdk2VSK2xHjBYvUb4jcwUeD0IYkYTnKgAACCgCGEAZ510gAwKDA0HVEQkVrD2JaIMLIhkWCFYvwVLojWSbvbsKaNZXCXwEmxa11"
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
    "channel_id": "ch_Lw7acgRZDftvky9DaDmVizHTPtPyoj3fdigY8wGx3ACyYpecS",
    "data": {
      "state": "tx_+QENCwH4hLhAVKCRWGdCH1QPFT2FezAEvli0MfcP7KhXkipnTKKA6Q6t+tzfm0LDXq+O8VhEGnXVQEQHRiF8idTpkk3gFsQ+DLhAarkXSe9sy9ElBKuweTR3zjlqFDBkdG7zRIuIFUqfkU06+cBzImkN4OczlKgC4uETM0OZ66yzNTxxXU77n2BsCriD+IEyAaEBKZdlStfJ88KAOnMd+ifqx1/HAVx5SaXN8Qel6xb5gfmGP6olImAAoQH9SDjn2AbZqKZ+8tyCEQdk2VSK2xHjBYvUb4jcwUeD0IYkYTnKgAACCgCGEAZ510gAwKDA0HVEQkVrD2JaIMLIhkWCFYvwVLojWSbvbsKaNZXCXwEmxa11"
    }
  },
  "version": 1
}
```
