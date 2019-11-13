
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
  "method": "channels.withdraw",
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
      "method": "channels.withdraw",
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
  "method": "channels.withdraw",
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
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBvXwJiJ/s16obG8kx4Cw3ocyFwZ6OR5IExGcQ/wwdfShoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FQIAhg/AoHKQAKD45g1hmERA3CWgwkPfzGWOoTngAqIHb6JbTz4LeaBjIAkeKSs0RA==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
  "id": -576460752303423109,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEApcjK5bdOFFZbvnbJNE0GTgn9wbqxciB4u4WVd0AycoLOwyIRM6Z+EM44ClQbY2NL+/g2mSxajyq4ek/3s2j0NuHT4cjQBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACg+OYNYZhEQNwloMJD38xljqE54AKiB2+iW08+C3mgYyAJHl18Ms8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423109,
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
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEApcjK5bdOFFZbvnbJNE0GTgn9wbqxciB4u4WVd0AycoLOwyIRM6Z+EM44ClQbY2NL+/g2mSxajyq4ek/3s2j0NuHT4cjQBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACg+OYNYZhEQNwloMJD38xljqE54AKiB2+iW08+C3mgYyAJHl18Ms8=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
  "id": -576460752303423108,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEACfzAB44ngVrYjT/P501zks/DFYGYtrTPko5ApAd3obtYecQkMM/xxFLRsPx5jPvjYrnjLldhskojJz5mYiTUEuEApcjK5bdOFFZbvnbJNE0GTgn9wbqxciB4u4WVd0AycoLOwyIRM6Z+EM44ClQbY2NL+/g2mSxajyq4ek/3s2j0NuHT4cjQBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACg+OYNYZhEQNwloMJD38xljqE54AKiB2+iW08+C3mgYyAJHlexGNQ="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423108,
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
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEACfzAB44ngVrYjT/P501zks/DFYGYtrTPko5ApAd3obtYecQkMM/xxFLRsPx5jPvjYrnjLldhskojJz5mYiTUEuEApcjK5bdOFFZbvnbJNE0GTgn9wbqxciB4u4WVd0AycoLOwyIRM6Z+EM44ClQbY2NL+/g2mSxajyq4ek/3s2j0NuHT4cjQBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACg+OYNYZhEQNwloMJD38xljqE54AKiB2+iW08+C3mgYyAJHlexGNQ=",
      "type": "channel_withdraw_tx"
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
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEACfzAB44ngVrYjT/P501zks/DFYGYtrTPko5ApAd3obtYecQkMM/xxFLRsPx5jPvjYrnjLldhskojJz5mYiTUEuEApcjK5bdOFFZbvnbJNE0GTgn9wbqxciB4u4WVd0AycoLOwyIRM6Z+EM44ClQbY2NL+/g2mSxajyq4ek/3s2j0NuHT4cjQBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACg+OYNYZhEQNwloMJD38xljqE54AKiB2+iW08+C3mgYyAJHlexGNQ=",
      "type": "channel_withdraw_tx"
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
      "tx": "tx_+P4LAfiEuEACfzAB44ngVrYjT/P501zks/DFYGYtrTPko5ApAd3obtYecQkMM/xxFLRsPx5jPvjYrnjLldhskojJz5mYiTUEuEApcjK5bdOFFZbvnbJNE0GTgn9wbqxciB4u4WVd0AycoLOwyIRM6Z+EM44ClQbY2NL+/g2mSxajyq4ek/3s2j0NuHT4cjQBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACg+OYNYZhEQNwloMJD38xljqE54AKiB2+iW08+C3mgYyAJHlexGNQ=",
      "type": "channel_withdraw_tx"
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
      "tx": "tx_+P4LAfiEuEACfzAB44ngVrYjT/P501zks/DFYGYtrTPko5ApAd3obtYecQkMM/xxFLRsPx5jPvjYrnjLldhskojJz5mYiTUEuEApcjK5bdOFFZbvnbJNE0GTgn9wbqxciB4u4WVd0AycoLOwyIRM6Z+EM44ClQbY2NL+/g2mSxajyq4ek/3s2j0NuHT4cjQBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACg+OYNYZhEQNwloMJD38xljqE54AKiB2+iW08+C3mgYyAJHlexGNQ=",
      "type": "channel_withdraw_tx"
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
      "event": "own_withdraw_locked"
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
      "event": "own_withdraw_locked"
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
      "event": "withdraw_locked"
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
      "event": "withdraw_locked"
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
      "state": "tx_+P4LAfiEuEACfzAB44ngVrYjT/P501zks/DFYGYtrTPko5ApAd3obtYecQkMM/xxFLRsPx5jPvjYrnjLldhskojJz5mYiTUEuEApcjK5bdOFFZbvnbJNE0GTgn9wbqxciB4u4WVd0AycoLOwyIRM6Z+EM44ClQbY2NL+/g2mSxajyq4ek/3s2j0NuHT4cjQBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACg+OYNYZhEQNwloMJD38xljqE54AKiB2+iW08+C3mgYyAJHlexGNQ="
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
      "state": "tx_+P4LAfiEuEACfzAB44ngVrYjT/P501zks/DFYGYtrTPko5ApAd3obtYecQkMM/xxFLRsPx5jPvjYrnjLldhskojJz5mYiTUEuEApcjK5bdOFFZbvnbJNE0GTgn9wbqxciB4u4WVd0AycoLOwyIRM6Z+EM44ClQbY2NL+/g2mSxajyq4ek/3s2j0NuHT4cjQBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACg+OYNYZhEQNwloMJD38xljqE54AKiB2+iW08+C3mgYyAJHlexGNQ="
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
  "method": "channels.withdraw",
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
      "method": "channels.withdraw",
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
  "method": "channels.withdraw",
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
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBvXwJiJ/s16obG8kx4Cw3ocyFwZ6OR5IExGcQ/wwdfShoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWvwIAhg/AoHKQAKBFhwcy1nQ5Bi3OEygVd2MWxy1qnVtAG2qKlPJORZgUAgoMoy5iAQ==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
  "id": -576460752303423107,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuECcfi6cHp8vlfUijno/xdM8W5NAk1UwKHlmdjcUSsu26F/yxaTCCyG9FfFjn30WLdaEQROqTq+zZsrxMgLIS1UJuHT4cjQBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAIKDLfKDMU="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423107,
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
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "signed_tx": "tx_+LwLAfhCuECcfi6cHp8vlfUijno/xdM8W5NAk1UwKHlmdjcUSsu26F/yxaTCCyG9FfFjn30WLdaEQROqTq+zZsrxMgLIS1UJuHT4cjQBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAIKDLfKDMU=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
  "id": -576460752303423106,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuECcfi6cHp8vlfUijno/xdM8W5NAk1UwKHlmdjcUSsu26F/yxaTCCyG9FfFjn30WLdaEQROqTq+zZsrxMgLIS1UJuEDR/BYunVgIXOxyug6MZp9sMZvBYIEa07jsFxbAl0FLTiWfAVOMyxcXjB5n0+vOSslcFIHtoT/jOH+0Eph1VUUJuHT4cjQBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAIKDFIOURs="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
  "id": -576460752303423106,
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
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuECcfi6cHp8vlfUijno/xdM8W5NAk1UwKHlmdjcUSsu26F/yxaTCCyG9FfFjn30WLdaEQROqTq+zZsrxMgLIS1UJuEDR/BYunVgIXOxyug6MZp9sMZvBYIEa07jsFxbAl0FLTiWfAVOMyxcXjB5n0+vOSslcFIHtoT/jOH+0Eph1VUUJuHT4cjQBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAIKDFIOURs=",
      "type": "channel_withdraw_tx"
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
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuECcfi6cHp8vlfUijno/xdM8W5NAk1UwKHlmdjcUSsu26F/yxaTCCyG9FfFjn30WLdaEQROqTq+zZsrxMgLIS1UJuEDR/BYunVgIXOxyug6MZp9sMZvBYIEa07jsFxbAl0FLTiWfAVOMyxcXjB5n0+vOSslcFIHtoT/jOH+0Eph1VUUJuHT4cjQBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAIKDFIOURs=",
      "type": "channel_withdraw_tx"
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

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2sKABFFA9ZcxS5UEb47Lu7VtcrYgxUcAdrpTnXNhzdtJ7Raxar",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECcfi6cHp8vlfUijno/xdM8W5NAk1UwKHlmdjcUSsu26F/yxaTCCyG9FfFjn30WLdaEQROqTq+zZsrxMgLIS1UJuEDR/BYunVgIXOxyug6MZp9sMZvBYIEa07jsFxbAl0FLTiWfAVOMyxcXjB5n0+vOSslcFIHtoT/jOH+0Eph1VUUJuHT4cjQBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAIKDFIOURs=",
      "type": "channel_withdraw_tx"
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
      "tx": "tx_+P4LAfiEuECcfi6cHp8vlfUijno/xdM8W5NAk1UwKHlmdjcUSsu26F/yxaTCCyG9FfFjn30WLdaEQROqTq+zZsrxMgLIS1UJuEDR/BYunVgIXOxyug6MZp9sMZvBYIEa07jsFxbAl0FLTiWfAVOMyxcXjB5n0+vOSslcFIHtoT/jOH+0Eph1VUUJuHT4cjQBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAIKDFIOURs=",
      "type": "channel_withdraw_tx"
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
      "event": "own_withdraw_locked"
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
      "event": "own_withdraw_locked"
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
      "event": "withdraw_locked"
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
      "event": "withdraw_locked"
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
      "state": "tx_+P4LAfiEuECcfi6cHp8vlfUijno/xdM8W5NAk1UwKHlmdjcUSsu26F/yxaTCCyG9FfFjn30WLdaEQROqTq+zZsrxMgLIS1UJuEDR/BYunVgIXOxyug6MZp9sMZvBYIEa07jsFxbAl0FLTiWfAVOMyxcXjB5n0+vOSslcFIHtoT/jOH+0Eph1VUUJuHT4cjQBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAIKDFIOURs="
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
      "state": "tx_+P4LAfiEuECcfi6cHp8vlfUijno/xdM8W5NAk1UwKHlmdjcUSsu26F/yxaTCCyG9FfFjn30WLdaEQROqTq+zZsrxMgLIS1UJuEDR/BYunVgIXOxyug6MZp9sMZvBYIEa07jsFxbAl0FLTiWfAVOMyxcXjB5n0+vOSslcFIHtoT/jOH+0Eph1VUUJuHT4cjQBoQb18CYif7NeqGxvJMeAsN6HMhcGejkeSBMRnEP8MHX0oaEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAIKDFIOURs="
    }
  },
  "version": 1
}
```
