
#### initiator opens a WebSocket connection (2019-03-13 11:04:50.983)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3&role=initiator
```

#### responder opens a WebSocket connection (2019-03-13 11:04:51.1)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3&role=responder
```

#### responder <--- node (2019-03-13 11:04:51.995)
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

#### initiator <--- node (2019-03-13 11:04:52.1)
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

#### initiator <--- node (2019-03-13 11:04:52.23)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAIyD4QZ"
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:52.108)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_+MsLAfhCuEAq60ovlnYklY352YttvFi25vuZWivlSq+zlZxlAUteUBQssKCX4xxeZzYJeJV3iYYMV22irFQh/WoybKWEuLMOuIP4gTIBoQEmB6t0j6CEj0TF7aBkfLKhLNj0/vfE3UYgZ2CLIgbnp4Y/qiUiYAChAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPhiRhOcqAAAIKAIYSMJzlQADAoODtFIhe84yV0+uaXXnfGCrRRApvdISmjmGVfhKf0nkoAiwCIRc="
  }
}
```

#### responder <--- node (2019-03-13 11:04:52.132)
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

#### responder <--- node (2019-03-13 11:04:52.134)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAIyD4QZ"
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:04:52.135)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_+MsLAfhCuEAwjK5KD2uzHZCAPTj7j1iVUoSSMuRZ9xBVjiQ7UEJNt+5Bw9HgbE0Fe4THYc4zs8OY6uiM3ZJ++UkNJeDRyEoFuIP4gTIBoQEmB6t0j6CEj0TF7aBkfLKhLNj0/vfE3UYgZ2CLIgbnp4Y/qiUiYAChAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPhiRhOcqAAAIKAIYSMJzlQADAoODtFIhe84yV0+uaXXnfGCrRRApvdISmjmGVfhKf0nkoAq2CnqE="
  }
}
```

#### responder <--- node (2019-03-13 11:04:52.163)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+QENCwH4hLhAKutKL5Z2JJWN+dmLbbxYtub7mVor5Uqvs5WcZQFLXlAULLCgl+McXmc2CXiVd4mGDFdtoqxUIf1qMmylhLizDrhAMIyuSg9rsx2QgD04+49YlVKEkjLkWfcQVY4kO1BCTbfuQcPR4GxNBXuEx2HOM7PDmOrojN2SfvlJDSXg0chKBbiD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAIPqGwB"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:04:52.165)
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

#### initiator <--- node (2019-03-13 11:04:52.167)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+QENCwH4hLhAKutKL5Z2JJWN+dmLbbxYtub7mVor5Uqvs5WcZQFLXlAULLCgl+McXmc2CXiVd4mGDFdtoqxUIf1qMmylhLizDrhAMIyuSg9rsx2QgD04+49YlVKEkjLkWfcQVY4kO1BCTbfuQcPR4GxNBXuEx2HOM7PDmOrojN2SfvlJDSXg0chKBbiD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAIPqGwB"
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:52.861)
```javascript
{
  "id": -576460752303423472,
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

#### initiator <--- node (2019-03-13 11:04:52.871)
```javascript
{
  "channel_id": null,
  "id": -576460752303423472,
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

#### initiator <--- node (2019-03-13 11:04:53.692)
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

#### responder <--- node (2019-03-13 11:04:53.693)
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

#### responder <--- node (2019-03-13 11:04:53.694)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_23DUr69XBGjd6ijGcKh1cfLaBueUG5KpVAn7jbnYPtBqqGW5TQ",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:04:53.696)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_23DUr69XBGjd6ijGcKh1cfLaBueUG5KpVAn7jbnYPtBqqGW5TQ",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:04:53.710)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_23DUr69XBGjd6ijGcKh1cfLaBueUG5KpVAn7jbnYPtBqqGW5TQ",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:04:53.712)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_23DUr69XBGjd6ijGcKh1cfLaBueUG5KpVAn7jbnYPtBqqGW5TQ",
    "data": {
      "state": "tx_+QENCwH4hLhAKutKL5Z2JJWN+dmLbbxYtub7mVor5Uqvs5WcZQFLXlAULLCgl+McXmc2CXiVd4mGDFdtoqxUIf1qMmylhLizDrhAMIyuSg9rsx2QgD04+49YlVKEkjLkWfcQVY4kO1BCTbfuQcPR4GxNBXuEx2HOM7PDmOrojN2SfvlJDSXg0chKBbiD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAIPqGwB"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:04:53.713)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_23DUr69XBGjd6ijGcKh1cfLaBueUG5KpVAn7jbnYPtBqqGW5TQ",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:04:53.716)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_23DUr69XBGjd6ijGcKh1cfLaBueUG5KpVAn7jbnYPtBqqGW5TQ",
    "data": {
      "state": "tx_+QENCwH4hLhAKutKL5Z2JJWN+dmLbbxYtub7mVor5Uqvs5WcZQFLXlAULLCgl+McXmc2CXiVd4mGDFdtoqxUIf1qMmylhLizDrhAMIyuSg9rsx2QgD04+49YlVKEkjLkWfcQVY4kO1BCTbfuQcPR4GxNBXuEx2HOM7PDmOrojN2SfvlJDSXg0chKBbiD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAIPqGwB"
    }
  },
  "version": 1
}
```

#### initiator: (2019-03-13 11:04:55.2)
> Funding has been confirmed locally on-chain

#### responder: (2019-03-13 11:04:55.2)
> Funding has been confirmed locally on-chain

#### initiator: (2019-03-13 11:04:55.2)
> Funding has been confirmed on-chain by other party

#### responder: (2019-03-13 11:04:55.2)
> Funding has been confirmed on-chain by other party

#### initiator: (2019-03-13 11:04:55.2)
> Channel is `open` and ready to use

#### responder: (2019-03-13 11:04:55.2)
> Channel is `open` and ready to use

#### initiator ---> node (2019-03-13 11:04:55.117)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### initiator <--- node (2019-03-13 11:04:55.138)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_23DUr69XBGjd6ijGcKh1cfLaBueUG5KpVAn7jbnYPtBqqGW5TQ",
    "data": {
      "tx": "tx_+F01AaEGiLnV3UlmPgZF5mVfuWUneIltOTlU4oPFxxHlmGAZyFyhASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenhjaR1q+//4YbSOtX4AEAhhIwnOVAAAOFsluT"
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:55.154)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "tx": "tx_+KcLAfhCuECfkjKrMFj6vPuv4G3j2OQXFYX+uTHp/gx6UuStmOIqEISsyAzohnD3MrT7P4TvE+q2FJhH22s1KynCzkkZAjkIuF/4XTUBoQaIudXdSWY+BkXmZV+5ZSd4iW05OVTig8XHEeWYYBnIXKEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGNpHWr7//hhtI61fgAQCGEjCc5UAAA5qOidQ="
  }
}
```

#### responder <--- node (2019-03-13 11:04:55.186)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_23DUr69XBGjd6ijGcKh1cfLaBueUG5KpVAn7jbnYPtBqqGW5TQ",
    "data": {
      "tx": "tx_+F01AaEGiLnV3UlmPgZF5mVfuWUneIltOTlU4oPFxxHlmGAZyFyhASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenhjaR1q+//4YbSOtX4AEAhhIwnOVAAAOFsluT"
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:04:55.187)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "tx": "tx_+KcLAfhCuEDM8gM1tqd0WjtpxNP9VS4zl82/4f85qVSB5NrdLBowGK7UMyNv7vX4pjkwa9fLVYfCRQ17P0W8eOkVWNLE6PMEuF/4XTUBoQaIudXdSWY+BkXmZV+5ZSd4iW05OVTig8XHEeWYYBnIXKEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGNpHWr7//hhtI61fgAQCGEjCc5UAAA1V3754="
  }
}
```

#### responder <--- node (2019-03-13 11:04:55.210)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_23DUr69XBGjd6ijGcKh1cfLaBueUG5KpVAn7jbnYPtBqqGW5TQ",
    "data": {
      "tx": "tx_+OkLAfiEuECfkjKrMFj6vPuv4G3j2OQXFYX+uTHp/gx6UuStmOIqEISsyAzohnD3MrT7P4TvE+q2FJhH22s1KynCzkkZAjkIuEDM8gM1tqd0WjtpxNP9VS4zl82/4f85qVSB5NrdLBowGK7UMyNv7vX4pjkwa9fLVYfCRQ17P0W8eOkVWNLE6PMEuF/4XTUBoQaIudXdSWY+BkXmZV+5ZSd4iW05OVTig8XHEeWYYBnIXKEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGNpHWr7//hhtI61fgAQCGEjCc5UAAA1q2wi0="
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:04:55.210)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_23DUr69XBGjd6ijGcKh1cfLaBueUG5KpVAn7jbnYPtBqqGW5TQ",
    "data": {
      "event": "close_mutual"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:04:55.211)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_23DUr69XBGjd6ijGcKh1cfLaBueUG5KpVAn7jbnYPtBqqGW5TQ",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:04:55.253)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_23DUr69XBGjd6ijGcKh1cfLaBueUG5KpVAn7jbnYPtBqqGW5TQ",
    "data": {
      "tx": "tx_+OkLAfiEuECfkjKrMFj6vPuv4G3j2OQXFYX+uTHp/gx6UuStmOIqEISsyAzohnD3MrT7P4TvE+q2FJhH22s1KynCzkkZAjkIuEDM8gM1tqd0WjtpxNP9VS4zl82/4f85qVSB5NrdLBowGK7UMyNv7vX4pjkwa9fLVYfCRQ17P0W8eOkVWNLE6PMEuF/4XTUBoQaIudXdSWY+BkXmZV+5ZSd4iW05OVTig8XHEeWYYBnIXKEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGNpHWr7//hhtI61fgAQCGEjCc5UAAA1q2wi0="
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:04:55.256)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_23DUr69XBGjd6ijGcKh1cfLaBueUG5KpVAn7jbnYPtBqqGW5TQ",
    "data": {
      "event": "close_mutual"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:04:55.257)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_23DUr69XBGjd6ijGcKh1cfLaBueUG5KpVAn7jbnYPtBqqGW5TQ",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection (2019-03-13 11:04:57.38)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3&role=initiator
```

#### responder opens a WebSocket connection (2019-03-13 11:04:57.56)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3&role=responder
```

#### responder <--- node (2019-03-13 11:04:58.29)
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

#### initiator <--- node (2019-03-13 11:04:58.41)
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

#### initiator <--- node (2019-03-13 11:04:58.61)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAS9GqWH"
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:58.184)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_+MsLAfhCuECkw2zV5lw6EfJEGQR6LqhAnvymJUcRCX+r9NB/xPUOGY7aGyTWfxtnYWgNWjDz54JMQH8PXu8taBu7K7ot/VsGuIP4gTIBoQEmB6t0j6CEj0TF7aBkfLKhLNj0/vfE3UYgZ2CLIgbnp4Y/qiUiYAChAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPhiRhOcqAAAIKAIYSMJzlQADAoODtFIhe84yV0+uaXXnfGCrRRApvdISmjmGVfhKf0nkoBJXjWK0="
  }
}
```

#### responder <--- node (2019-03-13 11:04:58.226)
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

#### responder <--- node (2019-03-13 11:04:58.228)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAS9GqWH"
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:04:58.229)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_+MsLAfhCuEC/lGsitLgpbO9N4ENdCRlCPd7JZ87YN/4myNuDqbRbjqyxEduZwCobAd2PxMcP2hCAxAs/2FeHBpFcBI13njAPuIP4gTIBoQEmB6t0j6CEj0TF7aBkfLKhLNj0/vfE3UYgZ2CLIgbnp4Y/qiUiYAChAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPhiRhOcqAAAIKAIYSMJzlQADAoODtFIhe84yV0+uaXXnfGCrRRApvdISmjmGVfhKf0nkoBDmGPN0="
  }
}
```

#### initiator <--- node (2019-03-13 11:04:58.242)
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

#### responder <--- node (2019-03-13 11:04:58.243)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+QENCwH4hLhApMNs1eZcOhHyRBkEei6oQJ78piVHEQl/q/TQf8T1DhmO2hsk1n8bZ2FoDVow8+eCTEB/D17vLWgbuyu6Lf1bBrhAv5RrIrS4KWzvTeBDXQkZQj3eyWfO2Df+Jsjbg6m0W46ssRHbmcAqGwHdj8THD9oQgMQLP9hXhwaRXASNd54wD7iD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAQUMe3X"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:04:58.246)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+QENCwH4hLhApMNs1eZcOhHyRBkEei6oQJ78piVHEQl/q/TQf8T1DhmO2hsk1n8bZ2FoDVow8+eCTEB/D17vLWgbuyu6Lf1bBrhAv5RrIrS4KWzvTeBDXQkZQj3eyWfO2Df+Jsjbg6m0W46ssRHbmcAqGwHdj8THD9oQgMQLP9hXhwaRXASNd54wD7iD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAQUMe3X"
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:59.926)
```javascript
{
  "id": -576460752303423471,
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

#### initiator <--- node (2019-03-13 11:04:59.932)
```javascript
{
  "channel_id": null,
  "id": -576460752303423471,
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

#### initiator <--- node (2019-03-13 11:05:00.656)
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

#### responder <--- node (2019-03-13 11:05:00.659)
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

#### responder <--- node (2019-03-13 11:05:00.660)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_CA98M5i46wsNRMSCoW1cx77GgmRzNpN3MHwV7CH9npYej8bdD",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:00.661)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_CA98M5i46wsNRMSCoW1cx77GgmRzNpN3MHwV7CH9npYej8bdD",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:00.688)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_CA98M5i46wsNRMSCoW1cx77GgmRzNpN3MHwV7CH9npYej8bdD",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:00.694)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_CA98M5i46wsNRMSCoW1cx77GgmRzNpN3MHwV7CH9npYej8bdD",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:00.697)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_CA98M5i46wsNRMSCoW1cx77GgmRzNpN3MHwV7CH9npYej8bdD",
    "data": {
      "state": "tx_+QENCwH4hLhApMNs1eZcOhHyRBkEei6oQJ78piVHEQl/q/TQf8T1DhmO2hsk1n8bZ2FoDVow8+eCTEB/D17vLWgbuyu6Lf1bBrhAv5RrIrS4KWzvTeBDXQkZQj3eyWfO2Df+Jsjbg6m0W46ssRHbmcAqGwHdj8THD9oQgMQLP9hXhwaRXASNd54wD7iD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAQUMe3X"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:00.698)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_CA98M5i46wsNRMSCoW1cx77GgmRzNpN3MHwV7CH9npYej8bdD",
    "data": {
      "state": "tx_+QENCwH4hLhApMNs1eZcOhHyRBkEei6oQJ78piVHEQl/q/TQf8T1DhmO2hsk1n8bZ2FoDVow8+eCTEB/D17vLWgbuyu6Lf1bBrhAv5RrIrS4KWzvTeBDXQkZQj3eyWfO2Df+Jsjbg6m0W46ssRHbmcAqGwHdj8THD9oQgMQLP9hXhwaRXASNd54wD7iD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAQUMe3X"
    }
  },
  "version": 1
}
```

#### initiator: (2019-03-13 11:05:01.76)
> Funding has been confirmed locally on-chain

#### responder: (2019-03-13 11:05:01.76)
> Funding has been confirmed locally on-chain

#### initiator: (2019-03-13 11:05:01.76)
> Funding has been confirmed on-chain by other party

#### responder: (2019-03-13 11:05:01.77)
> Funding has been confirmed on-chain by other party

#### initiator: (2019-03-13 11:05:01.77)
> Channel is `open` and ready to use

#### responder: (2019-03-13 11:05:01.77)
> Channel is `open` and ready to use

#### responder ---> node (2019-03-13 11:05:01.197)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### responder <--- node (2019-03-13 11:05:01.215)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_CA98M5i46wsNRMSCoW1cx77GgmRzNpN3MHwV7CH9npYej8bdD",
    "data": {
      "tx": "tx_+F01AaEGGVWs3L2/myUdqfuF5Jh8zm4Q4e12EFSUI0+chF77V8uhAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPhjaR1q+//4YbSOtX4AEAhhIwnOVAAAG+YGz3"
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:05:01.216)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "tx": "tx_+KcLAfhCuEBK4HNK3ovwcC+X0UulcdbmKcpiylleHyxacdAytnG4SlPcsho/ZKJ9oj15K/vq1ElOJUkrDV+bImA0cWkhjNwPuF/4XTUBoQYZVazcvb+bJR2p+4XkmHzObhDh7XYQVJQjT5yEXvtXy6EBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+GNpHWr7//hhtI61fgAQCGEjCc5UAAAeqGGYU="
  }
}
```

#### initiator <--- node (2019-03-13 11:05:01.266)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_CA98M5i46wsNRMSCoW1cx77GgmRzNpN3MHwV7CH9npYej8bdD",
    "data": {
      "tx": "tx_+F01AaEGGVWs3L2/myUdqfuF5Jh8zm4Q4e12EFSUI0+chF77V8uhAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPhjaR1q+//4YbSOtX4AEAhhIwnOVAAAG+YGz3"
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:01.267)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "tx": "tx_+KcLAfhCuEDYVpJ/YyVT3QX+3ERPrsWyz++PQ7IOD+OReXwfUHG2X8eoThISk5abdPb25mtLchWr0Cb1YM9tOg6yB7hiLjsFuF/4XTUBoQYZVazcvb+bJR2p+4XkmHzObhDh7XYQVJQjT5yEXvtXy6EBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+GNpHWr7//hhtI61fgAQCGEjCc5UAAAaItjCo="
  }
}
```

#### initiator <--- node (2019-03-13 11:05:01.286)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_CA98M5i46wsNRMSCoW1cx77GgmRzNpN3MHwV7CH9npYej8bdD",
    "data": {
      "tx": "tx_+OkLAfiEuEBK4HNK3ovwcC+X0UulcdbmKcpiylleHyxacdAytnG4SlPcsho/ZKJ9oj15K/vq1ElOJUkrDV+bImA0cWkhjNwPuEDYVpJ/YyVT3QX+3ERPrsWyz++PQ7IOD+OReXwfUHG2X8eoThISk5abdPb25mtLchWr0Cb1YM9tOg6yB7hiLjsFuF/4XTUBoQYZVazcvb+bJR2p+4XkmHzObhDh7XYQVJQjT5yEXvtXy6EBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+GNpHWr7//hhtI61fgAQCGEjCc5UAAAX4kt7A="
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:01.287)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_CA98M5i46wsNRMSCoW1cx77GgmRzNpN3MHwV7CH9npYej8bdD",
    "data": {
      "event": "close_mutual"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:01.287)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_CA98M5i46wsNRMSCoW1cx77GgmRzNpN3MHwV7CH9npYej8bdD",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:01.324)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_CA98M5i46wsNRMSCoW1cx77GgmRzNpN3MHwV7CH9npYej8bdD",
    "data": {
      "tx": "tx_+OkLAfiEuEBK4HNK3ovwcC+X0UulcdbmKcpiylleHyxacdAytnG4SlPcsho/ZKJ9oj15K/vq1ElOJUkrDV+bImA0cWkhjNwPuEDYVpJ/YyVT3QX+3ERPrsWyz++PQ7IOD+OReXwfUHG2X8eoThISk5abdPb25mtLchWr0Cb1YM9tOg6yB7hiLjsFuF/4XTUBoQYZVazcvb+bJR2p+4XkmHzObhDh7XYQVJQjT5yEXvtXy6EBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+GNpHWr7//hhtI61fgAQCGEjCc5UAAAX4kt7A="
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:01.325)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_CA98M5i46wsNRMSCoW1cx77GgmRzNpN3MHwV7CH9npYej8bdD",
    "data": {
      "event": "close_mutual"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:01.326)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_CA98M5i46wsNRMSCoW1cx77GgmRzNpN3MHwV7CH9npYej8bdD",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```
