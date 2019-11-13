
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "message": {
        "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "message": {
        "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
      "method": "channels.deposit",
      "params": {
        "amount": "2"
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "message": {
        "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "message": {
        "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2,
    "meta": [
      "meta 1"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBvXwJiJ/s16obG8kx4Cw3ocyFwZ6OR5IExGcQ/wwdfShoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FQIAhg/AoHKQAKCQ+qhgYd50noYow8kr18pLvPVpSh3wOSteAe09PWO3KgcdLJeY2Q==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainDeposit"
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
  "id": -576460752303423113,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEDArwXKLXbbKaqD85NgBr+pcoi166iv1/u2SzdwWGVWNgP7xucITHBsVNYahRAUypEkrXJUf55Yo7LAgstGpDoHuHT4cjMBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgkPqoYGHedJ6GKMPJK9fKS7z1aUod8DkrXgHtPT1jtyoHHSQwqE4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423113,
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEDArwXKLXbbKaqD85NgBr+pcoi166iv1/u2SzdwWGVWNgP7xucITHBsVNYahRAUypEkrXJUf55Yo7LAgstGpDoHuHT4cjMBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgkPqoYGHedJ6GKMPJK9fKS7z1aUod8DkrXgHtPT1jtyoHHSQwqE4=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainDeposit"
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
  "id": -576460752303423112,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEDArwXKLXbbKaqD85NgBr+pcoi166iv1/u2SzdwWGVWNgP7xucITHBsVNYahRAUypEkrXJUf55Yo7LAgstGpDoHuEDSlrRW8xICFNxmVXysIAIINiuE5hl7xfP4Vi5DF4VTrozFpDLIwKRRQLVOw0lckctfAbwzBSlIhFK7FHVISzkIuHT4cjMBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgkPqoYGHedJ6GKMPJK9fKS7z1aUod8DkrXgHtPT1jtyoHHeUheac="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423112,
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEDArwXKLXbbKaqD85NgBr+pcoi166iv1/u2SzdwWGVWNgP7xucITHBsVNYahRAUypEkrXJUf55Yo7LAgstGpDoHuEDSlrRW8xICFNxmVXysIAIINiuE5hl7xfP4Vi5DF4VTrozFpDLIwKRRQLVOw0lckctfAbwzBSlIhFK7FHVISzkIuHT4cjMBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgkPqoYGHedJ6GKMPJK9fKS7z1aUod8DkrXgHtPT1jtyoHHeUheac=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEDArwXKLXbbKaqD85NgBr+pcoi166iv1/u2SzdwWGVWNgP7xucITHBsVNYahRAUypEkrXJUf55Yo7LAgstGpDoHuEDSlrRW8xICFNxmVXysIAIINiuE5hl7xfP4Vi5DF4VTrozFpDLIwKRRQLVOw0lckctfAbwzBSlIhFK7FHVISzkIuHT4cjMBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgkPqoYGHedJ6GKMPJK9fKS7z1aUod8DkrXgHtPT1jtyoHHeUheac=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "message": {
        "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "message": {
        "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
        "info": "Hello back",
        "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
      }
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEDArwXKLXbbKaqD85NgBr+pcoi166iv1/u2SzdwWGVWNgP7xucITHBsVNYahRAUypEkrXJUf55Yo7LAgstGpDoHuEDSlrRW8xICFNxmVXysIAIINiuE5hl7xfP4Vi5DF4VTrozFpDLIwKRRQLVOw0lckctfAbwzBSlIhFK7FHVISzkIuHT4cjMBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgkPqoYGHedJ6GKMPJK9fKS7z1aUod8DkrXgHtPT1jtyoHHeUheac=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEDArwXKLXbbKaqD85NgBr+pcoi166iv1/u2SzdwWGVWNgP7xucITHBsVNYahRAUypEkrXJUf55Yo7LAgstGpDoHuEDSlrRW8xICFNxmVXysIAIINiuE5hl7xfP4Vi5DF4VTrozFpDLIwKRRQLVOw0lckctfAbwzBSlIhFK7FHVISzkIuHT4cjMBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgkPqoYGHedJ6GKMPJK9fKS7z1aUod8DkrXgHtPT1jtyoHHeUheac=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "state": "tx_+P4LAfiEuEDArwXKLXbbKaqD85NgBr+pcoi166iv1/u2SzdwWGVWNgP7xucITHBsVNYahRAUypEkrXJUf55Yo7LAgstGpDoHuEDSlrRW8xICFNxmVXysIAIINiuE5hl7xfP4Vi5DF4VTrozFpDLIwKRRQLVOw0lckctfAbwzBSlIhFK7FHVISzkIuHT4cjMBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgkPqoYGHedJ6GKMPJK9fKS7z1aUod8DkrXgHtPT1jtyoHHeUheac="
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "state": "tx_+P4LAfiEuEDArwXKLXbbKaqD85NgBr+pcoi166iv1/u2SzdwWGVWNgP7xucITHBsVNYahRAUypEkrXJUf55Yo7LAgstGpDoHuEDSlrRW8xICFNxmVXysIAIINiuE5hl7xfP4Vi5DF4VTrozFpDLIwKRRQLVOw0lckctfAbwzBSlIhFK7FHVISzkIuHT4cjMBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgkPqoYGHedJ6GKMPJK9fKS7z1aUod8DkrXgHtPT1jtyoHHeUheac="
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
    "info": "Hello",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "message": {
        "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "message": {
        "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
        "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
        "info": "Hello back",
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
  "method": "channels.deposit",
  "params": {
    "amount": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
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
      "method": "channels.deposit",
      "params": {
        "amount": "2"
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
  "method": "channels.message",
  "params": {
    "info": "Hello",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "message": {
        "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "message": {
        "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
        "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
        "info": "Hello back",
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
  "method": "channels.deposit",
  "params": {
    "amount": 2,
    "meta": [
      "meta 1"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBvXwJiJ/s16obG8kx4Cw3ocyFwZ6OR5IExGcQ/wwdfShoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWvwIAhg/AoHKQAKBmVYZICeiy6DcnhxU6sH0mOAc8bkhiA5xyXQdbL+kSbwgLyhqUpg==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainDeposit"
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
  "id": -576460752303423111,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEBs0SsBwChmpsphWw6SXxdmnUYxox3eJ6xyPo6otHQ5t+TaqX7X+wMn7kHokmQlIp60Ca4DuFf1oeGdBNy86tEPuHT4cjMBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgZlWGSAnosug3J4cVOrB9JjgHPG5IYgOccl0HWy/pEm8IC1I6sOc="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423111,
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEBs0SsBwChmpsphWw6SXxdmnUYxox3eJ6xyPo6otHQ5t+TaqX7X+wMn7kHokmQlIp60Ca4DuFf1oeGdBNy86tEPuHT4cjMBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgZlWGSAnosug3J4cVOrB9JjgHPG5IYgOccl0HWy/pEm8IC1I6sOc=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainDeposit"
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
  "id": -576460752303423110,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBs0SsBwChmpsphWw6SXxdmnUYxox3eJ6xyPo6otHQ5t+TaqX7X+wMn7kHokmQlIp60Ca4DuFf1oeGdBNy86tEPuECr7+uHoeNKwIEV3Hyeky89zFxbsOomuRKon/e4spkQu8RGlFlODQQ/Zms35hnumc0HSULOwbwP1roT0KVhdbAKuHT4cjMBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgZlWGSAnosug3J4cVOrB9JjgHPG5IYgOccl0HWy/pEm8IC3KBqM4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423110,
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEBs0SsBwChmpsphWw6SXxdmnUYxox3eJ6xyPo6otHQ5t+TaqX7X+wMn7kHokmQlIp60Ca4DuFf1oeGdBNy86tEPuECr7+uHoeNKwIEV3Hyeky89zFxbsOomuRKon/e4spkQu8RGlFlODQQ/Zms35hnumc0HSULOwbwP1roT0KVhdbAKuHT4cjMBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgZlWGSAnosug3J4cVOrB9JjgHPG5IYgOccl0HWy/pEm8IC3KBqM4=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEBs0SsBwChmpsphWw6SXxdmnUYxox3eJ6xyPo6otHQ5t+TaqX7X+wMn7kHokmQlIp60Ca4DuFf1oeGdBNy86tEPuECr7+uHoeNKwIEV3Hyeky89zFxbsOomuRKon/e4spkQu8RGlFlODQQ/Zms35hnumc0HSULOwbwP1roT0KVhdbAKuHT4cjMBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgZlWGSAnosug3J4cVOrB9JjgHPG5IYgOccl0HWy/pEm8IC3KBqM4=",
      "type": "channel_deposit_tx"
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
    "info": "Hello",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "message": {
        "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "message": {
        "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
        "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
        "info": "Hello back",
        "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
      }
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBs0SsBwChmpsphWw6SXxdmnUYxox3eJ6xyPo6otHQ5t+TaqX7X+wMn7kHokmQlIp60Ca4DuFf1oeGdBNy86tEPuECr7+uHoeNKwIEV3Hyeky89zFxbsOomuRKon/e4spkQu8RGlFlODQQ/Zms35hnumc0HSULOwbwP1roT0KVhdbAKuHT4cjMBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgZlWGSAnosug3J4cVOrB9JjgHPG5IYgOccl0HWy/pEm8IC3KBqM4=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBs0SsBwChmpsphWw6SXxdmnUYxox3eJ6xyPo6otHQ5t+TaqX7X+wMn7kHokmQlIp60Ca4DuFf1oeGdBNy86tEPuECr7+uHoeNKwIEV3Hyeky89zFxbsOomuRKon/e4spkQu8RGlFlODQQ/Zms35hnumc0HSULOwbwP1roT0KVhdbAKuHT4cjMBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgZlWGSAnosug3J4cVOrB9JjgHPG5IYgOccl0HWy/pEm8IC3KBqM4=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "state": "tx_+P4LAfiEuEBs0SsBwChmpsphWw6SXxdmnUYxox3eJ6xyPo6otHQ5t+TaqX7X+wMn7kHokmQlIp60Ca4DuFf1oeGdBNy86tEPuECr7+uHoeNKwIEV3Hyeky89zFxbsOomuRKon/e4spkQu8RGlFlODQQ/Zms35hnumc0HSULOwbwP1roT0KVhdbAKuHT4cjMBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgZlWGSAnosug3J4cVOrB9JjgHPG5IYgOccl0HWy/pEm8IC3KBqM4="
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
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "state": "tx_+P4LAfiEuEBs0SsBwChmpsphWw6SXxdmnUYxox3eJ6xyPo6otHQ5t+TaqX7X+wMn7kHokmQlIp60Ca4DuFf1oeGdBNy86tEPuECr7+uHoeNKwIEV3Hyeky89zFxbsOomuRKon/e4spkQu8RGlFlODQQ/Zms35hnumc0HSULOwbwP1roT0KVhdbAKuHT4cjMBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgZlWGSAnosug3J4cVOrB9JjgHPG5IYgOccl0HWy/pEm8IC3KBqM4="
    }
  },
  "version": 1
}
```
