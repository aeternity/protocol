
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
      "fsm_id": "ba_edsDeEZf0AFk4cTK2ZN44QKhwABtNc5ppCMSwPOo0lOqnfkK"
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
      "fsm_id": "ba_MipVsl9pI1qNzgp157T3pzrAse/vXDT+xHA4gkIvRxcD6JhS"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYqGlTcvA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422930,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDFzL9BJ/XLybAR0feXba/gzyUDPULQgtiqHDkVha3Z9q3806ELhZkpNB6Mv+comjquD3x/muFCGC0okTZ1g8sMuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2KnEtXOg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422930,
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
      "signed_tx": "tx_+MsLAfhCuEDFzL9BJ/XLybAR0feXba/gzyUDPULQgtiqHDkVha3Z9q3806ELhZkpNB6Mv+comjquD3x/muFCGC0okTZ1g8sMuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2KnEtXOg=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422929,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAeXmHwFe0FN1Lasx+gxKmLvUCOdQYEd4C3GVnZTcWeJ5MfsZdC+RGk9Ec5xzJU4MRg6Xaryt9NcBNvyEZDFxOBLhAxcy/QSf1y8mwEdH3l22v4M8lAz1C0ILYqhw5FYWt2fat/NOhC4WZKTQejL/nKJo6rg98f5rhQhgtKJE2dYPLDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdirkfq99"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422929,
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
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAeXmHwFe0FN1Lasx+gxKmLvUCOdQYEd4C3GVnZTcWeJ5MfsZdC+RGk9Ec5xzJU4MRg6Xaryt9NcBNvyEZDFxOBLhAxcy/QSf1y8mwEdH3l22v4M8lAz1C0ILYqhw5FYWt2fat/NOhC4WZKTQejL/nKJo6rg98f5rhQhgtKJE2dYPLDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdirkfq99",
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
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAeXmHwFe0FN1Lasx+gxKmLvUCOdQYEd4C3GVnZTcWeJ5MfsZdC+RGk9Ec5xzJU4MRg6Xaryt9NcBNvyEZDFxOBLhAxcy/QSf1y8mwEdH3l22v4M8lAz1C0ILYqhw5FYWt2fat/NOhC4WZKTQejL/nKJo6rg98f5rhQhgtKJE2dYPLDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdirkfq99",
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
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAeXmHwFe0FN1Lasx+gxKmLvUCOdQYEd4C3GVnZTcWeJ5MfsZdC+RGk9Ec5xzJU4MRg6Xaryt9NcBNvyEZDFxOBLhAxcy/QSf1y8mwEdH3l22v4M8lAz1C0ILYqhw5FYWt2fat/NOhC4WZKTQejL/nKJo6rg98f5rhQhgtKJE2dYPLDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdirkfq99",
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
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAeXmHwFe0FN1Lasx+gxKmLvUCOdQYEd4C3GVnZTcWeJ5MfsZdC+RGk9Ec5xzJU4MRg6Xaryt9NcBNvyEZDFxOBLhAxcy/QSf1y8mwEdH3l22v4M8lAz1C0ILYqhw5FYWt2fat/NOhC4WZKTQejL/nKJo6rg98f5rhQhgtKJE2dYPLDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdirkfq99",
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
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
    "data": {
      "message": {
        "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
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
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
    "data": {
      "message": {
        "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
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
  "id": -576460752303422928,
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
  "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
  "id": -576460752303422928,
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

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
    "data": {
      "event": "own_funding_locked"
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
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### responder info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
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
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
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
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
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
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
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
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
    "data": {
      "state": "tx_+QENCwH4hLhAeXmHwFe0FN1Lasx+gxKmLvUCOdQYEd4C3GVnZTcWeJ5MfsZdC+RGk9Ec5xzJU4MRg6Xaryt9NcBNvyEZDFxOBLhAxcy/QSf1y8mwEdH3l22v4M8lAz1C0ILYqhw5FYWt2fat/NOhC4WZKTQejL/nKJo6rg98f5rhQhgtKJE2dYPLDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdirkfq99"
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
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
    "data": {
      "state": "tx_+QENCwH4hLhAeXmHwFe0FN1Lasx+gxKmLvUCOdQYEd4C3GVnZTcWeJ5MfsZdC+RGk9Ec5xzJU4MRg6Xaryt9NcBNvyEZDFxOBLhAxcy/QSf1y8mwEdH3l22v4M8lAz1C0ILYqhw5FYWt2fat/NOhC4WZKTQejL/nKJo6rg98f5rhQhgtKJE2dYPLDLiD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdirkfq99"
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
  "params": {
    "fee": 20000000000001
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBm//SfvMZUlX3nqorSXz0qY4a7r+zG/F74E1yzN3W0IfoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY2kdavv/6GG0jrV+ABAIYSMJzlQAEruFGdAQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422927,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEAdHKKHlEw4ufObWmKWtr+URQ7TZH+Z42wFopvJnsX8nE/vbVg0PRBRzuPwpR62aRQ7KZqnzb/4YrWo4cAd5a8DuF/4XTUBoQZv/0n7zGVJV956qK0l89KmOGu6/sxvxe+BNcszd1tCH6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7/+hhtI61fgAQCGEjCc5UABK1s9U3c="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
  "id": -576460752303422927,
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
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
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
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEAdHKKHlEw4ufObWmKWtr+URQ7TZH+Z42wFopvJnsX8nE/vbVg0PRBRzuPwpR62aRQ7KZqnzb/4YrWo4cAd5a8DuF/4XTUBoQZv/0n7zGVJV956qK0l89KmOGu6/sxvxe+BNcszd1tCH6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7/+hhtI61fgAQCGEjCc5UABK1s9U3c=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422926,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEAdHKKHlEw4ufObWmKWtr+URQ7TZH+Z42wFopvJnsX8nE/vbVg0PRBRzuPwpR62aRQ7KZqnzb/4YrWo4cAd5a8DuEDX6mTrDA+YIIx4fxxcObyD0R9Ri4gEkQUSfUVFI9eumGnWv/ByIloDalfH0DqqyQF7cCd3acekx0lILYXwVZgIuF/4XTUBoQZv/0n7zGVJV956qK0l89KmOGu6/sxvxe+BNcszd1tCH6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7/+hhtI61fgAQCGEjCc5UABKxFAfFY="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
  "id": -576460752303422926,
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
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAdHKKHlEw4ufObWmKWtr+URQ7TZH+Z42wFopvJnsX8nE/vbVg0PRBRzuPwpR62aRQ7KZqnzb/4YrWo4cAd5a8DuEDX6mTrDA+YIIx4fxxcObyD0R9Ri4gEkQUSfUVFI9eumGnWv/ByIloDalfH0DqqyQF7cCd3acekx0lILYXwVZgIuF/4XTUBoQZv/0n7zGVJV956qK0l89KmOGu6/sxvxe+BNcszd1tCH6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7/+hhtI61fgAQCGEjCc5UABKxFAfFY=",
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
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
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
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAdHKKHlEw4ufObWmKWtr+URQ7TZH+Z42wFopvJnsX8nE/vbVg0PRBRzuPwpR62aRQ7KZqnzb/4YrWo4cAd5a8DuEDX6mTrDA+YIIx4fxxcObyD0R9Ri4gEkQUSfUVFI9eumGnWv/ByIloDalfH0DqqyQF7cCd3acekx0lILYXwVZgIuF/4XTUBoQZv/0n7zGVJV956qK0l89KmOGu6/sxvxe+BNcszd1tCH6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7/+hhtI61fgAQCGEjCc5UABKxFAfFY=",
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
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
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
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAdHKKHlEw4ufObWmKWtr+URQ7TZH+Z42wFopvJnsX8nE/vbVg0PRBRzuPwpR62aRQ7KZqnzb/4YrWo4cAd5a8DuEDX6mTrDA+YIIx4fxxcObyD0R9Ri4gEkQUSfUVFI9eumGnWv/ByIloDalfH0DqqyQF7cCd3acekx0lILYXwVZgIuF/4XTUBoQZv/0n7zGVJV956qK0l89KmOGu6/sxvxe+BNcszd1tCH6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7/+hhtI61fgAQCGEjCc5UABKxFAfFY=",
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
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAdHKKHlEw4ufObWmKWtr+URQ7TZH+Z42wFopvJnsX8nE/vbVg0PRBRzuPwpR62aRQ7KZqnzb/4YrWo4cAd5a8DuEDX6mTrDA+YIIx4fxxcObyD0R9Ri4gEkQUSfUVFI9eumGnWv/ByIloDalfH0DqqyQF7cCd3acekx0lILYXwVZgIuF/4XTUBoQZv/0n7zGVJV956qK0l89KmOGu6/sxvxe+BNcszd1tCH6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7/+hhtI61fgAQCGEjCc5UABKxFAfFY=",
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
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
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
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
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
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
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
    "channel_id": "ch_rKpVEJSyZzWAEbrh4C1XwBKAASuVXXRs6vgCVGU5guq4xKDu9",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```

#### responder closes WebSocket connection
```

```
