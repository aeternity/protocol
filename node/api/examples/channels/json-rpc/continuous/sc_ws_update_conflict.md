
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

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 2,
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlmo/bF2SGuaNndCiay1Jo8C4fvfrty8jMGJkQ+adt1bBqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt54mYNw=",
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

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlmo/bF2SGuaNndCiay1Jo8C4fvfrty8jMGJkQ+adt1bBqCo57fNqBzJCyJHwVtKvbBulGvI7njy2CIguwb3YS0wotnnzwk=",
      "updates": [
        {
          "amount": 2,
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
    "signed_tx": "tx_+JALAfhCuEC4VqT9PDq4+f96m10FGOY771ODK33ULpAAQq6IPB+ZRQmUXbqshh4fZ66f1GDsOToeq/D3+lx0DnFlHaAfHwQLuEj4RjkCoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdWwagc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cUbr4z"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBVYd7hTmsgubEvxHDzeeGn1fzlqRJZJ8pS/eT0DTpSuYR8W/kgSFmTsWDa7cZidmKZycR9Eh6xenR8B1+jLJcMuEj4RjkCoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdWwagqOe3zagcyQsiR8FbSr2wbpRryO548tgiILsG92EtMKLrUpyB"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
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
    "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 2,
    "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlmo/bF2SGuaNndCiay1Jo8C4fvfrty8jMGJkQ+adt1bBqBFhwcy1nQ5Bi3OEygVd2MWxy1qnVtAG2qKlPJORZgUAnLNa0Y=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
    "signed_tx": "tx_+JALAfhCuEC9XXIg50w606QIhz7zP7lJYreRiBhsOZ1jHdeg5MNNpU0LmjxO6lXe7S0zyReAmWozkcPoJR/CrkUSYwvesQEKuEj4RjkCoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdWwagRYcHMtZ0OQYtzhMoFXdjFsctap1bQBtqipTyTkWYFAIPbMxk"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlmo/bF2SGuaNndCiay1Jo8C4fvfrty8jMGJkQ+adt1bBqAQC2mRDJBuZy2f5shl3syNOoLwZ8gFKEnBvk6yFb0dV2ULv5E=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
    "signed_tx": "tx_+JALAfhCuEApvK0gUHOKU0eMOG6SJ/euapGIvO19MVbI8d96PHNyx80Ta1lV7hov4cS0JCFpTs5xrhxpuQUreu3LjLhW9NYAuEj4RjkCoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdWwagEAtpkQyQbmctn+bIZd7MjTqC8GfIBShJwb5OshW9HVdfSmqz"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423146,
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
  "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
  "id": -576460752303423146,
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlmo/bF2SGuaNndCiay1Jo8C4fvfrty8jMGJkQ+adt1bBqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt54mYNw=",
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
  "id": -576460752303423145,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "error": 147
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
  "id": -576460752303423145,
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
  "id": -576460752303423144,
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
  "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
  "id": -576460752303423144,
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

#### responder ---> node
```javascript
{
  "id": -576460752303423143,
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
  "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
  "id": -576460752303423143,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423142,
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
  "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
  "id": -576460752303423142,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```
