
#### initiator opens a WebSocket connection (2019-03-13 11:05:08.795)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3&role=initiator
```

#### responder opens a WebSocket connection (2019-03-13 11:05:08.820)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3&role=responder
```

#### responder <--- node (2019-03-13 11:05:09.809)
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

#### initiator <--- node (2019-03-13 11:05:09.817)
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

#### initiator <--- node (2019-03-13 11:05:09.847)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAb78uaa"
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:09.945)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_+MsLAfhCuEAamqQtci3PGoorUVkl1hm1aA71z7i7WHaboGwLLQnZJrZEAge+edzs6c1q3hyLtUZ9MBte4wlXjvCal7n4pv8EuIP4gTIBoQEmB6t0j6CEj0TF7aBkfLKhLNj0/vfE3UYgZ2CLIgbnp4Y/qiUiYAChAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPhiRhOcqAAAIKAIYSMJzlQADAoODtFIhe84yV0+uaXXnfGCrRRApvdISmjmGVfhKf0nkoBgnW5ac="
  }
}
```

#### responder <--- node (2019-03-13 11:05:09.961)
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

#### responder <--- node (2019-03-13 11:05:09.963)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAb78uaa"
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:05:09.972)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_+MsLAfhCuEDg3xX5Lqf9DNkUVPaCzMu5/Z1Df4mmy8kFTyTIHuKWWSA3S529vl8wBGyJkr9gVeXmKCh3T/VtJ/8fJPdrixIIuIP4gTIBoQEmB6t0j6CEj0TF7aBkfLKhLNj0/vfE3UYgZ2CLIgbnp4Y/qiUiYAChAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPhiRhOcqAAAIKAIYSMJzlQADAoODtFIhe84yV0+uaXXnfGCrRRApvdISmjmGVfhKf0nkoBr/cDFk="
  }
}
```

#### initiator <--- node (2019-03-13 11:05:09.985)
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

#### responder <--- node (2019-03-13 11:05:09.985)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+QENCwH4hLhAGpqkLXItzxqKK1FZJdYZtWgO9c+4u1h2m6BsCy0J2Sa2RAIHvnnc7OnNat4ci7VGfTAbXuMJV47wmpe5+Kb/BLhA4N8V+S6n/QzZFFT2gszLuf2dQ3+JpsvJBU8kyB7illkgN0udvb5fMARsiZK/YFXl5igod0/1bSf/HyT3a4sSCLiD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAaeIBEd"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:09.986)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+QENCwH4hLhAGpqkLXItzxqKK1FZJdYZtWgO9c+4u1h2m6BsCy0J2Sa2RAIHvnnc7OnNat4ci7VGfTAbXuMJV47wmpe5+Kb/BLhA4N8V+S6n/QzZFFT2gszLuf2dQ3+JpsvJBU8kyB7illkgN0udvb5fMARsiZK/YFXl5igod0/1bSf/HyT3a4sSCLiD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAaeIBEd"
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:11.9)
```javascript
{
  "id": -576460752303423454,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
    ]
  }
}
```

#### initiator <--- node (2019-03-13 11:05:11.19)
```javascript
{
  "channel_id": null,
  "id": -576460752303423454,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "balance": 69999999999999
    },
    {
      "account": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:12.220)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:12.222)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:12.228)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:12.231)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:12.242)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:12.246)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "state": "tx_+QENCwH4hLhAGpqkLXItzxqKK1FZJdYZtWgO9c+4u1h2m6BsCy0J2Sa2RAIHvnnc7OnNat4ci7VGfTAbXuMJV47wmpe5+Kb/BLhA4N8V+S6n/QzZFFT2gszLuf2dQ3+JpsvJBU8kyB7illkgN0udvb5fMARsiZK/YFXl5igod0/1bSf/HyT3a4sSCLiD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAaeIBEd"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:12.246)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:12.252)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "state": "tx_+QENCwH4hLhAGpqkLXItzxqKK1FZJdYZtWgO9c+4u1h2m6BsCy0J2Sa2RAIHvnnc7OnNat4ci7VGfTAbXuMJV47wmpe5+Kb/BLhA4N8V+S6n/QzZFFT2gszLuf2dQ3+JpsvJBU8kyB7illkgN0udvb5fMARsiZK/YFXl5igod0/1bSf/HyT3a4sSCLiD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAaeIBEd"
    }
  },
  "version": 1
}
```

#### initiator: (2019-03-13 11:05:13.588)
> Funding has been confirmed locally on-chain

#### responder: (2019-03-13 11:05:13.588)
> Funding has been confirmed locally on-chain

#### responder: (2019-03-13 11:05:13.588)
> Funding has been confirmed on-chain by other party

#### initiator: (2019-03-13 11:05:13.588)
> Funding has been confirmed on-chain by other party

#### responder: (2019-03-13 11:05:13.588)
> Channel is `open` and ready to use

#### initiator: (2019-03-13 11:05:13.588)
> Channel is `open` and ready to use
