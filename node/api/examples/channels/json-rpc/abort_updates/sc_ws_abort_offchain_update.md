
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=initiator
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
      "fsm_id": "ba_izrkYRITzyDUi0ZoQtjsoRv2bTzFlFk+SctfWrIkwCHETxxU"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=responder
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
      "fsm_id": "ba_gF6g1cw9p1VOnoYap8OgObdH+QBFeauj51+hRNcS0xMuY+On"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnY5Te1nDQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422895,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAQ6Kj7mhC0M/RT7jdrP1WdiuZlKbJtW60WiR5OIUvY1LXC1wCsN69WTAsg576YpcxXJhWMG1gYFNVIzn/sGeYCuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2OexRVIw="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422895,
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
      "signed_tx": "tx_+MsLAfhCuEAQ6Kj7mhC0M/RT7jdrP1WdiuZlKbJtW60WiR5OIUvY1LXC1wCsN69WTAsg576YpcxXJhWMG1gYFNVIzn/sGeYCuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2OexRVIw=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422894,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAEOio+5oQtDP0U+43az9VnYrmZSmybVutFokeTiFL2NS1wtcArDevVkwLIOe+mKXMVyYVjBtYGBTVSM5/7BnmArhA2IGhqyp9wjLh0glJCY/cywSyZKMSQ/pH1Me/2w/QeQ0bE9MaY1EHi4p6RvxKJr2aIcPkWiyAxTrSQozqgCMiA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjlmD73J"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422894,
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
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAEOio+5oQtDP0U+43az9VnYrmZSmybVutFokeTiFL2NS1wtcArDevVkwLIOe+mKXMVyYVjBtYGBTVSM5/7BnmArhA2IGhqyp9wjLh0glJCY/cywSyZKMSQ/pH1Me/2w/QeQ0bE9MaY1EHi4p6RvxKJr2aIcPkWiyAxTrSQozqgCMiA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjlmD73J",
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
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAEOio+5oQtDP0U+43az9VnYrmZSmybVutFokeTiFL2NS1wtcArDevVkwLIOe+mKXMVyYVjBtYGBTVSM5/7BnmArhA2IGhqyp9wjLh0glJCY/cywSyZKMSQ/pH1Me/2w/QeQ0bE9MaY1EHi4p6RvxKJr2aIcPkWiyAxTrSQozqgCMiA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjlmD73J",
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
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAEOio+5oQtDP0U+43az9VnYrmZSmybVutFokeTiFL2NS1wtcArDevVkwLIOe+mKXMVyYVjBtYGBTVSM5/7BnmArhA2IGhqyp9wjLh0glJCY/cywSyZKMSQ/pH1Me/2w/QeQ0bE9MaY1EHi4p6RvxKJr2aIcPkWiyAxTrSQozqgCMiA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjlmD73J",
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
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAEOio+5oQtDP0U+43az9VnYrmZSmybVutFokeTiFL2NS1wtcArDevVkwLIOe+mKXMVyYVjBtYGBTVSM5/7BnmArhA2IGhqyp9wjLh0glJCY/cywSyZKMSQ/pH1Me/2w/QeQ0bE9MaY1EHi4p6RvxKJr2aIcPkWiyAxTrSQozqgCMiA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjlmD73J",
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
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
    "data": {
      "message": {
        "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
        "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
        "info": "Hello",
        "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
    "data": {
      "message": {
        "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
        "info": "Hello back",
        "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422893,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
  "id": -576460752303422893,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 69999999999999
    },
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
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
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
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
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
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
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
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
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
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
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
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
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
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
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
    "data": {
      "state": "tx_+QENCwH4hLhAEOio+5oQtDP0U+43az9VnYrmZSmybVutFokeTiFL2NS1wtcArDevVkwLIOe+mKXMVyYVjBtYGBTVSM5/7BnmArhA2IGhqyp9wjLh0glJCY/cywSyZKMSQ/pH1Me/2w/QeQ0bE9MaY1EHi4p6RvxKJr2aIcPkWiyAxTrSQozqgCMiA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjlmD73J"
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
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
    "data": {
      "state": "tx_+QENCwH4hLhAEOio+5oQtDP0U+43az9VnYrmZSmybVutFokeTiFL2NS1wtcArDevVkwLIOe+mKXMVyYVjBtYGBTVSM5/7BnmArhA2IGhqyp9wjLh0glJCY/cywSyZKMSQ/pH1Me/2w/QeQ0bE9MaY1EHi4p6RvxKJr2aIcPkWiyAxTrSQozqgCMiA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdjlmD73J"
    }
  },
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
    "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqTjAp4bpuUkqXXRoRFK6T/Mz6fuZIiF8oWIurT1r05IAqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt7uMIIg=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainTransfer",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
    "data": {
      "event": "aborted_update"
    }
  },
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
    "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqTjAp4bpuUkqXXRoRFK6T/Mz6fuZIiF8oWIurT1r05IAqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt7uMIIg=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainTransfer",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "error": 42
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
    "data": {
      "event": "aborted_update"
    }
  },
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
    "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqTjAp4bpuUkqXXRoRFK6T/Mz6fuZIiF8oWIurT1r05IAqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt7uMIIg=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainTransfer",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
  "id": -576460752303422892,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDotaWqduIOQd90WuV5//2zhkw/le/IMU2jGhAKB3Ovrp/kqsk4ncm+2p7WPghgj3Re88umHTuunVULKt3g2oYMuEj4RjkCoQak4wKeG6blJKl10aERSuk/zM+n7mSIhfKFiLq09a9OSAKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cU7/3d"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
  "id": -576460752303422892,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1018,
        "message": "Not allowed at current channel state"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update",
      "params": {
        "error": 42
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
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
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDotaWqduIOQd90WuV5//2zhkw/le/IMU2jGhAKB3Ovrp/kqsk4ncm+2p7WPghgj3Re88umHTuunVULKt3g2oYMuEj4RjkCoQak4wKeG6blJKl10aERSuk/zM+n7mSIhfKFiLq09a9OSAKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cU7/3d",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainTransfer",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "error": 42
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
    "data": {
      "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
      "error_code": 42,
      "error_msg": "unknown",
      "round": 1
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422891,
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
  "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
  "id": -576460752303422891,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422890,
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
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
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
  "channel_id": "ch_2Fcp32wxdUnr4EDRdGm3QFREdnrPB9grenJ6GExHFXpNwRDxDV",
  "id": -576460752303422890,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```
