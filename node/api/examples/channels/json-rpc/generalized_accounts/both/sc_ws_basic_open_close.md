
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo&keep_running=false&lock_period=10&port=12524&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe&role=initiator
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
      "fsm_id": "ba_8R9pX+a3uFs+L4NJ2RQVY4C2TOdjWRp8sImIfyOUDLnWl8rr"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo&keep_running=false&lock_period=10&port=12524&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe&role=responder
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
      "fsm_id": "ba_kt2z8DM04GVNjfiKb0gByhKHA6/RVdXlF3kTWMjxlvDnW/Oa"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAdOnhoT/i0OTHdY4QW2nwyUhYueA8LbDq1hP8NKmaxajhj+qJSJgAKEBk6eIAf2Xgni733RBSJ08OWm78HQeEXBsbDhOiz6lQ/KGJGE5yoAAAgoAhhAGeddIAMCgtxt1z/oIixo9Zh4GY4HpgbJHVYqT0ci96JSfxiOnuskAYqYEbg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421189,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+NQLAcC4z/jNUQGhAdOnhoT/i0OTHdY4QW2nwyUhYueA8LbDq1hP8NKmaxajiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQHTp4aE/4tDkx3WOEFtp8MlIWLngPC2w6tYT/DSpmsWo4Y/qiUiYAChAZOniAH9l4J4u990QUidPDlpu/B0HhFwbGw4Tos+pUPyhiRhOcqAAAIKAIYQBnnXSADAoLcbdc/6CIsaPWYeBmOB6YGyR1WKk9HIveiUn8Yjp7rJAHi5HIA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421189,
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "fsm_id": "ba_kt2z8DM04GVNjfiKb0gByhKHA6/RVdXlF3kTWMjxlvDnW/Oa",
      "signed_tx": "tx_+NQLAcC4z/jNUQGhAdOnhoT/i0OTHdY4QW2nwyUhYueA8LbDq1hP8NKmaxajiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQHTp4aE/4tDkx3WOEFtp8MlIWLngPC2w6tYT/DSpmsWo4Y/qiUiYAChAZOniAH9l4J4u990QUidPDlpu/B0HhFwbGw4Tos+pUPyhiRhOcqAAAIKAIYQBnnXSADAoLcbdc/6CIsaPWYeBmOB6YGyR1WKk9HIveiUn8Yjp7rJAHi5HIA=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421188,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEiCwHAuQEc+QEZUQGhAZOniAH9l4J4u990QUidPDlpu/B0HhFwbGw4Tos+pUPyiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQHTp4aE/4tDkx3WOEFtp8MlIWLngPC2w6tYT/DSpmsWo4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEB06eGhP+LQ5Md1jhBbafDJSFi54DwtsOrWE/w0qZrFqOGP6olImAAoQGTp4gB/ZeCeLvfdEFInTw5abvwdB4RcGxsOE6LPqVD8oYkYTnKgAACCgCGEAZ510gAwKC3G3XP+giLGj1mHgZjgemBskdVipPRyL3olJ/GI6e6yQBgqlpx"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421188,
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEiCwHAuQEc+QEZUQGhAZOniAH9l4J4u990QUidPDlpu/B0HhFwbGw4Tos+pUPyiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQHTp4aE/4tDkx3WOEFtp8MlIWLngPC2w6tYT/DSpmsWo4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEB06eGhP+LQ5Md1jhBbafDJSFi54DwtsOrWE/w0qZrFqOGP6olImAAoQGTp4gB/ZeCeLvfdEFInTw5abvwdB4RcGxsOE6LPqVD8oYkYTnKgAACCgCGEAZ510gAwKC3G3XP+giLGj1mHgZjgemBskdVipPRyL3olJ/GI6e6yQBgqlpx",
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_8R9pX+a3uFs+L4NJ2RQVY4C2TOdjWRp8sImIfyOUDLnWl8rr"
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEiCwHAuQEc+QEZUQGhAZOniAH9l4J4u990QUidPDlpu/B0HhFwbGw4Tos+pUPyiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQHTp4aE/4tDkx3WOEFtp8MlIWLngPC2w6tYT/DSpmsWo4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEB06eGhP+LQ5Md1jhBbafDJSFi54DwtsOrWE/w0qZrFqOGP6olImAAoQGTp4gB/ZeCeLvfdEFInTw5abvwdB4RcGxsOE6LPqVD8oYkYTnKgAACCgCGEAZ510gAwKC3G3XP+giLGj1mHgZjgemBskdVipPRyL3olJ/GI6e6yQBgqlpx",
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEiCwHAuQEc+QEZUQGhAZOniAH9l4J4u990QUidPDlpu/B0HhFwbGw4Tos+pUPyiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQHTp4aE/4tDkx3WOEFtp8MlIWLngPC2w6tYT/DSpmsWo4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEB06eGhP+LQ5Md1jhBbafDJSFi54DwtsOrWE/w0qZrFqOGP6olImAAoQGTp4gB/ZeCeLvfdEFInTw5abvwdB4RcGxsOE6LPqVD8oYkYTnKgAACCgCGEAZ510gAwKC3G3XP+giLGj1mHgZjgemBskdVipPRyL3olJ/GI6e6yQBgqlpx",
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEiCwHAuQEc+QEZUQGhAZOniAH9l4J4u990QUidPDlpu/B0HhFwbGw4Tos+pUPyiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQHTp4aE/4tDkx3WOEFtp8MlIWLngPC2w6tYT/DSpmsWo4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEB06eGhP+LQ5Md1jhBbafDJSFi54DwtsOrWE/w0qZrFqOGP6olImAAoQGTp4gB/ZeCeLvfdEFInTw5abvwdB4RcGxsOE6LPqVD8oYkYTnKgAACCgCGEAZ510gAwKC3G3XP+giLGj1mHgZjgemBskdVipPRyL3olJ/GI6e6yQBgqlpx",
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
    "to": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "message": {
        "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
        "from": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
        "info": "Hello",
        "to": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
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
    "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "message": {
        "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
        "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
        "info": "Hello back",
        "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421187,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
      "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421187,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
      "balance": 69999999999999
    },
    {
      "account": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "state": "tx_+QEiCwHAuQEc+QEZUQGhAZOniAH9l4J4u990QUidPDlpu/B0HhFwbGw4Tos+pUPyiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQHTp4aE/4tDkx3WOEFtp8MlIWLngPC2w6tYT/DSpmsWo4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEB06eGhP+LQ5Md1jhBbafDJSFi54DwtsOrWE/w0qZrFqOGP6olImAAoQGTp4gB/ZeCeLvfdEFInTw5abvwdB4RcGxsOE6LPqVD8oYkYTnKgAACCgCGEAZ510gAwKC3G3XP+giLGj1mHgZjgemBskdVipPRyL3olJ/GI6e6yQBgqlpx"
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "state": "tx_+QEiCwHAuQEc+QEZUQGhAZOniAH9l4J4u990QUidPDlpu/B0HhFwbGw4Tos+pUPyiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQHTp4aE/4tDkx3WOEFtp8MlIWLngPC2w6tYT/DSpmsWo4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEB06eGhP+LQ5Md1jhBbafDJSFi54DwtsOrWE/w0qZrFqOGP6olImAAoQGTp4gB/ZeCeLvfdEFInTw5abvwdB4RcGxsOE6LPqVD8oYkYTnKgAACCgCGEAZ510gAwKC3G3XP+giLGj1mHgZjgemBskdVipPRyL3olJ/GI6e6yQBgqlpx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421186,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
      "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421186,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
      "balance": 69999999999999
    },
    {
      "account": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
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
    "from": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
    "to": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
        "from": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
        "to": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
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
    "to": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
        "to": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
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
    "from": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
        "from": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
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
    "from": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
    "meta": 17,
    "to": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
        "from": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
        "meta": 17,
        "to": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
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
    "from": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
    "to": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi1gsLGnMI5e7Z0qWGNSAmk0VALDUHaygAF3FicwwFU6AqBf6kqqlr3V1SD06yXJyoHDf9wohbFHepnAMRMUvCt8WvmuT0M=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
          "op": "OffChainTransfer",
          "to": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
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
  "id": -576460752303421185,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAdOnhoT/i0OTHdY4QW2nwyUhYueA8LbDq1hP8NKmaxajiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQYtYLCxpzCOXu2dKlhjUgJpNFQCw1B2soABdxYnMMBVOgKgX+pKqpa91dUg9OslycqBw3/cKIWxR3qZwDETFLwrfFpzPvOq"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421185,
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAdOnhoT/i0OTHdY4QW2nwyUhYueA8LbDq1hP8NKmaxajiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQYtYLCxpzCOXu2dKlhjUgJpNFQCw1B2soABdxYnMMBVOgKgX+pKqpa91dUg9OslycqBw3/cKIWxR3qZwDETFLwrfFpzPvOq",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
          "op": "OffChainTransfer",
          "to": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
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
  "id": -576460752303421184,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhAZOniAH9l4J4u990QUidPDlpu/B0HhFwbGw4Tos+pUPyiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQHTp4aE/4tDkx3WOEFtp8MlIWLngPC2w6tYT/DSpmsWo4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGLWCwsacwjl7tnSpYY1ICaTRUAsNQdrKAAXcWJzDAVToCoF/qSqqWvdXVIPTrJcnKgcN/3CiFsUd6mcAxExS8K3xaihgeuw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421184,
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAZOniAH9l4J4u990QUidPDlpu/B0HhFwbGw4Tos+pUPyiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQHTp4aE/4tDkx3WOEFtp8MlIWLngPC2w6tYT/DSpmsWo4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGLWCwsacwjl7tnSpYY1ICaTRUAsNQdrKAAXcWJzDAVToCoF/qSqqWvdXVIPTrJcnKgcN/3CiFsUd6mcAxExS8K3xaihgeuw=="
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAZOniAH9l4J4u990QUidPDlpu/B0HhFwbGw4Tos+pUPyiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQHTp4aE/4tDkx3WOEFtp8MlIWLngPC2w6tYT/DSpmsWo4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGLWCwsacwjl7tnSpYY1ICaTRUAsNQdrKAAXcWJzDAVToCoF/qSqqWvdXVIPTrJcnKgcN/3CiFsUd6mcAxExS8K3xaihgeuw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421183,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
      "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421183,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
      "balance": 69999999999998
    },
    {
      "account": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421182,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421182,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhAZOniAH9l4J4u990QUidPDlpu/B0HhFwbGw4Tos+pUPyiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQHTp4aE/4tDkx3WOEFtp8MlIWLngPC2w6tYT/DSpmsWo4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGLWCwsacwjl7tnSpYY1ICaTRUAsNQdrKAAXcWJzDAVToCoF/qSqqWvdXVIPTrJcnKgcN/3CiFsUd6mcAxExS8K3xaihgeuw==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDTp4aE/4tDkx3WOEFtp8MlIWLngPC2w6tYT/DSpmsWo4vKCgEAhj+qJSJf/rDvQAGgk6eIAf2Xgni733RBSJ08OWm78HQeEXBsbDhOiz6lQ/KLygoBAIYkYTnKgAI//D2F"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421181,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
      "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421181,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
      "balance": 40000000000002
    },
    {
      "account": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
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
    "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
    "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
        "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
        "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
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
    "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
        "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
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
    "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
        "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
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
    "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
    "meta": 17,
    "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
        "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
        "meta": 17,
        "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
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
    "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
    "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi1gsLGnMI5e7Z0qWGNSAmk0VALDUHaygAF3FicwwFU6A6C3G3XP+giLGj1mHgZjgemBskdVipPRyL3olJ/GI6e6ydjPGlA=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
          "op": "OffChainTransfer",
          "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
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
  "id": -576460752303421180,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAZOniAH9l4J4u990QUidPDlpu/B0HhFwbGw4Tos+pUPyiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQYtYLCxpzCOXu2dKlhjUgJpNFQCw1B2soABdxYnMMBVOgOgtxt1z/oIixo9Zh4GY4HpgbJHVYqT0ci96JSfxiOnuslJA/SD"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421180,
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAZOniAH9l4J4u990QUidPDlpu/B0HhFwbGw4Tos+pUPyiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQYtYLCxpzCOXu2dKlhjUgJpNFQCw1B2soABdxYnMMBVOgOgtxt1z/oIixo9Zh4GY4HpgbJHVYqT0ci96JSfxiOnuslJA/SD",
      "updates": [
        {
          "amount": 1,
          "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
          "op": "OffChainTransfer",
          "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
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
  "id": -576460752303421179,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhAdOnhoT/i0OTHdY4QW2nwyUhYueA8LbDq1hP8NKmaxajiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGTp4gB/ZeCeLvfdEFInTw5abvwdB4RcGxsOE6LPqVD8okrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGLWCwsacwjl7tnSpYY1ICaTRUAsNQdrKAAXcWJzDAVToDoLcbdc/6CIsaPWYeBmOB6YGyR1WKk9HIveiUn8Yjp7rJ/Kag3Q=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421179,
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAdOnhoT/i0OTHdY4QW2nwyUhYueA8LbDq1hP8NKmaxajiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGTp4gB/ZeCeLvfdEFInTw5abvwdB4RcGxsOE6LPqVD8okrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGLWCwsacwjl7tnSpYY1ICaTRUAsNQdrKAAXcWJzDAVToDoLcbdc/6CIsaPWYeBmOB6YGyR1WKk9HIveiUn8Yjp7rJ/Kag3Q=="
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAdOnhoT/i0OTHdY4QW2nwyUhYueA8LbDq1hP8NKmaxajiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGTp4gB/ZeCeLvfdEFInTw5abvwdB4RcGxsOE6LPqVD8okrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGLWCwsacwjl7tnSpYY1ICaTRUAsNQdrKAAXcWJzDAVToDoLcbdc/6CIsaPWYeBmOB6YGyR1WKk9HIveiUn8Yjp7rJ/Kag3Q=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421178,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
      "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421178,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
      "balance": 40000000000001
    },
    {
      "account": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421177,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421177,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhAdOnhoT/i0OTHdY4QW2nwyUhYueA8LbDq1hP8NKmaxajiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGTp4gB/ZeCeLvfdEFInTw5abvwdB4RcGxsOE6LPqVD8okrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGLWCwsacwjl7tnSpYY1ICaTRUAsNQdrKAAXcWJzDAVToDoLcbdc/6CIsaPWYeBmOB6YGyR1WKk9HIveiUn8Yjp7rJ/Kag3Q==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDTp4aE/4tDkx3WOEFtp8MlIWLngPC2w6tYT/DSpmsWo4vKCgEAhj+qJSJf/7DvQAGgk6eIAf2Xgni733RBSJ08OWm78HQeEXBsbDhOiz6lQ/KLygoBAIYkYTnKgAFYoqOK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421176,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
      "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421176,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
      "balance": 40000000000001
    },
    {
      "account": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
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
    "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
    "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
        "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
        "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
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
    "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
        "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
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
    "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
        "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
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
    "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
    "meta": 17,
    "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
        "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
        "meta": 17,
        "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
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
    "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
    "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi1gsLGnMI5e7Z0qWGNSAmk0VALDUHaygAF3FicwwFU6BKC49fHyE6Z0C/N0xSIPDApkwp8+rE3Itid8lSuOwGWgRRcXnEw=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
          "op": "OffChainTransfer",
          "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
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
  "id": -576460752303421175,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAZOniAH9l4J4u990QUidPDlpu/B0HhFwbGw4Tos+pUPyiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQYtYLCxpzCOXu2dKlhjUgJpNFQCw1B2soABdxYnMMBVOgSguPXx8hOmdAvzdMUiDwwKZMKfPqxNyLYnfJUrjsBloEVtQ7Ip"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421175,
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAZOniAH9l4J4u990QUidPDlpu/B0HhFwbGw4Tos+pUPyiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQYtYLCxpzCOXu2dKlhjUgJpNFQCw1B2soABdxYnMMBVOgSguPXx8hOmdAvzdMUiDwwKZMKfPqxNyLYnfJUrjsBloEVtQ7Ip",
      "updates": [
        {
          "amount": 1,
          "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
          "op": "OffChainTransfer",
          "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
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
  "id": -576460752303421174,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhAdOnhoT/i0OTHdY4QW2nwyUhYueA8LbDq1hP8NKmaxajiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGTp4gB/ZeCeLvfdEFInTw5abvwdB4RcGxsOE6LPqVD8okrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGLWCwsacwjl7tnSpYY1ICaTRUAsNQdrKAAXcWJzDAVToEoLj18fITpnQL83TFIg8MCmTCnz6sTci2J3yVK47AZaBFQ0O5ow=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421174,
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAdOnhoT/i0OTHdY4QW2nwyUhYueA8LbDq1hP8NKmaxajiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGTp4gB/ZeCeLvfdEFInTw5abvwdB4RcGxsOE6LPqVD8okrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGLWCwsacwjl7tnSpYY1ICaTRUAsNQdrKAAXcWJzDAVToEoLj18fITpnQL83TFIg8MCmTCnz6sTci2J3yVK47AZaBFQ0O5ow=="
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAdOnhoT/i0OTHdY4QW2nwyUhYueA8LbDq1hP8NKmaxajiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGTp4gB/ZeCeLvfdEFInTw5abvwdB4RcGxsOE6LPqVD8okrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGLWCwsacwjl7tnSpYY1ICaTRUAsNQdrKAAXcWJzDAVToEoLj18fITpnQL83TFIg8MCmTCnz6sTci2J3yVK47AZaBFQ0O5ow=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421173,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
      "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421173,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
      "balance": 40000000000000
    },
    {
      "account": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421172,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421172,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhAdOnhoT/i0OTHdY4QW2nwyUhYueA8LbDq1hP8NKmaxajiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGTp4gB/ZeCeLvfdEFInTw5abvwdB4RcGxsOE6LPqVD8okrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGLWCwsacwjl7tnSpYY1ICaTRUAsNQdrKAAXcWJzDAVToEoLj18fITpnQL83TFIg8MCmTCnz6sTci2J3yVK47AZaBFQ0O5ow==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDTp4aE/4tDkx3WOEFtp8MlIWLngPC2w6tYT/DSpmsWo4vKCgEAhj+qJSJgALDvQAGgk6eIAf2Xgni733RBSJ08OWm78HQeEXBsbDhOiz6lQ/KLygoBAIYkYTnKgABQn+wG"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421171,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
      "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421171,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
      "balance": 70000000000000
    },
    {
      "account": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
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
    "from": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
    "to": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
        "from": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
        "to": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
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
    "to": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
        "to": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
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
    "from": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
        "from": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
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
    "from": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
    "meta": 17,
    "to": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
        "from": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
        "meta": 17,
        "to": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
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
    "from": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
    "to": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi1gsLGnMI5e7Z0qWGNSAmk0VALDUHaygAF3FicwwFU6BaC3G3XP+giLGj1mHgZjgemBskdVipPRyL3olJ/GI6e6yQqv0U0=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
          "op": "OffChainTransfer",
          "to": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
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
  "id": -576460752303421170,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAdOnhoT/i0OTHdY4QW2nwyUhYueA8LbDq1hP8NKmaxajiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQYtYLCxpzCOXu2dKlhjUgJpNFQCw1B2soABdxYnMMBVOgWgtxt1z/oIixo9Zh4GY4HpgbJHVYqT0ci96JSfxiOnusl5P2Fw"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421170,
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAdOnhoT/i0OTHdY4QW2nwyUhYueA8LbDq1hP8NKmaxajiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQYtYLCxpzCOXu2dKlhjUgJpNFQCw1B2soABdxYnMMBVOgWgtxt1z/oIixo9Zh4GY4HpgbJHVYqT0ci96JSfxiOnusl5P2Fw",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
          "op": "OffChainTransfer",
          "to": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
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
  "id": -576460752303421169,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhAZOniAH9l4J4u990QUidPDlpu/B0HhFwbGw4Tos+pUPyiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQHTp4aE/4tDkx3WOEFtp8MlIWLngPC2w6tYT/DSpmsWo4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGLWCwsacwjl7tnSpYY1ICaTRUAsNQdrKAAXcWJzDAVToFoLcbdc/6CIsaPWYeBmOB6YGyR1WKk9HIveiUn8Yjp7rJ3Ak2sg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421169,
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAZOniAH9l4J4u990QUidPDlpu/B0HhFwbGw4Tos+pUPyiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQHTp4aE/4tDkx3WOEFtp8MlIWLngPC2w6tYT/DSpmsWo4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGLWCwsacwjl7tnSpYY1ICaTRUAsNQdrKAAXcWJzDAVToFoLcbdc/6CIsaPWYeBmOB6YGyR1WKk9HIveiUn8Yjp7rJ3Ak2sg=="
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAZOniAH9l4J4u990QUidPDlpu/B0HhFwbGw4Tos+pUPyiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQHTp4aE/4tDkx3WOEFtp8MlIWLngPC2w6tYT/DSpmsWo4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGLWCwsacwjl7tnSpYY1ICaTRUAsNQdrKAAXcWJzDAVToFoLcbdc/6CIsaPWYeBmOB6YGyR1WKk9HIveiUn8Yjp7rJ3Ak2sg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421168,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
      "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421168,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
      "balance": 69999999999999
    },
    {
      "account": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421167,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421167,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhAZOniAH9l4J4u990QUidPDlpu/B0HhFwbGw4Tos+pUPyiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQHTp4aE/4tDkx3WOEFtp8MlIWLngPC2w6tYT/DSpmsWo4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGLWCwsacwjl7tnSpYY1ICaTRUAsNQdrKAAXcWJzDAVToFoLcbdc/6CIsaPWYeBmOB6YGyR1WKk9HIveiUn8Yjp7rJ3Ak2sg==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDTp4aE/4tDkx3WOEFtp8MlIWLngPC2w6tYT/DSpmsWo4vKCgEAhj+qJSJf/7DvQAGgk6eIAf2Xgni733RBSJ08OWm78HQeEXBsbDhOiz6lQ/KLygoBAIYkYTnKgAFYoqOK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421166,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
      "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421166,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
      "balance": 40000000000001
    },
    {
      "account": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
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
    "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
    "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
        "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
        "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
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
    "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
        "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
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
    "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
        "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
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
    "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
    "meta": 17,
    "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
        "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
        "meta": 17,
        "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
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
    "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
    "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi1gsLGnMI5e7Z0qWGNSAmk0VALDUHaygAF3FicwwFU6BqC49fHyE6Z0C/N0xSIPDApkwp8+rE3Itid8lSuOwGWgRQGOuIA=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
          "op": "OffChainTransfer",
          "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
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
  "id": -576460752303421165,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAZOniAH9l4J4u990QUidPDlpu/B0HhFwbGw4Tos+pUPyiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQYtYLCxpzCOXu2dKlhjUgJpNFQCw1B2soABdxYnMMBVOgaguPXx8hOmdAvzdMUiDwwKZMKfPqxNyLYnfJUrjsBloEWr1PTf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421165,
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAZOniAH9l4J4u990QUidPDlpu/B0HhFwbGw4Tos+pUPyiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQYtYLCxpzCOXu2dKlhjUgJpNFQCw1B2soABdxYnMMBVOgaguPXx8hOmdAvzdMUiDwwKZMKfPqxNyLYnfJUrjsBloEWr1PTf",
      "updates": [
        {
          "amount": 1,
          "from": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
          "op": "OffChainTransfer",
          "to": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
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
  "id": -576460752303421164,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhAdOnhoT/i0OTHdY4QW2nwyUhYueA8LbDq1hP8NKmaxajiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGTp4gB/ZeCeLvfdEFInTw5abvwdB4RcGxsOE6LPqVD8okrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGLWCwsacwjl7tnSpYY1ICaTRUAsNQdrKAAXcWJzDAVToGoLj18fITpnQL83TFIg8MCmTCnz6sTci2J3yVK47AZaBF2TRu5w=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421164,
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAdOnhoT/i0OTHdY4QW2nwyUhYueA8LbDq1hP8NKmaxajiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGTp4gB/ZeCeLvfdEFInTw5abvwdB4RcGxsOE6LPqVD8okrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGLWCwsacwjl7tnSpYY1ICaTRUAsNQdrKAAXcWJzDAVToGoLj18fITpnQL83TFIg8MCmTCnz6sTci2J3yVK47AZaBF2TRu5w=="
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAdOnhoT/i0OTHdY4QW2nwyUhYueA8LbDq1hP8NKmaxajiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGTp4gB/ZeCeLvfdEFInTw5abvwdB4RcGxsOE6LPqVD8okrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGLWCwsacwjl7tnSpYY1ICaTRUAsNQdrKAAXcWJzDAVToGoLj18fITpnQL83TFIg8MCmTCnz6sTci2J3yVK47AZaBF2TRu5w=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421163,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
      "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421163,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_282dmeZALzDGfpiVNHZv3gmsT8HcUaJ58QZ7wNo9f4V82gtZfe",
      "balance": 40000000000000
    },
    {
      "account": "ak_2cDRo4PH9S3sgHWM8jYVjLCGRXpjPHBKLGshZmNNC6iaKC58zo",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421162,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421162,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhAdOnhoT/i0OTHdY4QW2nwyUhYueA8LbDq1hP8NKmaxajiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGTp4gB/ZeCeLvfdEFInTw5abvwdB4RcGxsOE6LPqVD8okrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGLWCwsacwjl7tnSpYY1ICaTRUAsNQdrKAAXcWJzDAVToGoLj18fITpnQL83TFIg8MCmTCnz6sTci2J3yVK47AZaBF2TRu5w==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDTp4aE/4tDkx3WOEFtp8MlIWLngPC2w6tYT/DSpmsWo4vKCgEAhj+qJSJgALDvQAGgk6eIAf2Xgni733RBSJ08OWm78HQeEXBsbDhOiz6lQ/KLygoBAIYkYTnKgABQn+wG"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421161,
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
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421161,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421160,
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
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
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
  "channel_id": "ch_Lz7WvkroupLwRCQfjGWCgSc6nHBChvFWEGnU8Ad881u5YK2X2",
  "id": -576460752303421160,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
