
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "message": {
        "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "message": {
        "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
  "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "message": {
        "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "message": {
        "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBlmo/bF2SGuaNndCiay1Jo8C4fvfrty8jMGJkQ+adt1boQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FQIAhg/AoHKQAKBkHkp+5scV2OHwQbjEIZHR7qRYh9akzYCkDxPO9Ji42QIa/iCYYA==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainDeposit"
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
  "id": -576460752303423154,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEBSzOkCFYv25mTRLzlYqvbF1GoURx/kFhseVI25MIpGr8tWMqRR+t9Xpty/KF2d8X84ALnAeHKyAH74RJRDgB0DuHT4cjMBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgZB5KfubHFdjh8EG4xCGR0e6kWIfWpM2ApA8TzvSYuNkCGjtQ5Rk="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
  "id": -576460752303423154,
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEBSzOkCFYv25mTRLzlYqvbF1GoURx/kFhseVI25MIpGr8tWMqRR+t9Xpty/KF2d8X84ALnAeHKyAH74RJRDgB0DuHT4cjMBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgZB5KfubHFdjh8EG4xCGR0e6kWIfWpM2ApA8TzvSYuNkCGjtQ5Rk=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainDeposit"
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
  "id": -576460752303423153,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBSzOkCFYv25mTRLzlYqvbF1GoURx/kFhseVI25MIpGr8tWMqRR+t9Xpty/KF2d8X84ALnAeHKyAH74RJRDgB0DuEDvoY3U0hP83PTmvveCan5EoOr2fmmOVgQzeSB+7KG9YDvEXmofBvmE8cTvRIWQnQ4hRjtH7cw9cR7GgItwChsGuHT4cjMBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgZB5KfubHFdjh8EG4xCGR0e6kWIfWpM2ApA8TzvSYuNkCGj9Y2As="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
  "id": -576460752303423153,
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEBSzOkCFYv25mTRLzlYqvbF1GoURx/kFhseVI25MIpGr8tWMqRR+t9Xpty/KF2d8X84ALnAeHKyAH74RJRDgB0DuEDvoY3U0hP83PTmvveCan5EoOr2fmmOVgQzeSB+7KG9YDvEXmofBvmE8cTvRIWQnQ4hRjtH7cw9cR7GgItwChsGuHT4cjMBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgZB5KfubHFdjh8EG4xCGR0e6kWIfWpM2ApA8TzvSYuNkCGj9Y2As=",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEBSzOkCFYv25mTRLzlYqvbF1GoURx/kFhseVI25MIpGr8tWMqRR+t9Xpty/KF2d8X84ALnAeHKyAH74RJRDgB0DuEDvoY3U0hP83PTmvveCan5EoOr2fmmOVgQzeSB+7KG9YDvEXmofBvmE8cTvRIWQnQ4hRjtH7cw9cR7GgItwChsGuHT4cjMBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgZB5KfubHFdjh8EG4xCGR0e6kWIfWpM2ApA8TzvSYuNkCGj9Y2As=",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "message": {
        "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "message": {
        "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBSzOkCFYv25mTRLzlYqvbF1GoURx/kFhseVI25MIpGr8tWMqRR+t9Xpty/KF2d8X84ALnAeHKyAH74RJRDgB0DuEDvoY3U0hP83PTmvveCan5EoOr2fmmOVgQzeSB+7KG9YDvEXmofBvmE8cTvRIWQnQ4hRjtH7cw9cR7GgItwChsGuHT4cjMBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgZB5KfubHFdjh8EG4xCGR0e6kWIfWpM2ApA8TzvSYuNkCGj9Y2As=",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBSzOkCFYv25mTRLzlYqvbF1GoURx/kFhseVI25MIpGr8tWMqRR+t9Xpty/KF2d8X84ALnAeHKyAH74RJRDgB0DuEDvoY3U0hP83PTmvveCan5EoOr2fmmOVgQzeSB+7KG9YDvEXmofBvmE8cTvRIWQnQ4hRjtH7cw9cR7GgItwChsGuHT4cjMBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgZB5KfubHFdjh8EG4xCGR0e6kWIfWpM2ApA8TzvSYuNkCGj9Y2As=",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "state": "tx_+P4LAfiEuEBSzOkCFYv25mTRLzlYqvbF1GoURx/kFhseVI25MIpGr8tWMqRR+t9Xpty/KF2d8X84ALnAeHKyAH74RJRDgB0DuEDvoY3U0hP83PTmvveCan5EoOr2fmmOVgQzeSB+7KG9YDvEXmofBvmE8cTvRIWQnQ4hRjtH7cw9cR7GgItwChsGuHT4cjMBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgZB5KfubHFdjh8EG4xCGR0e6kWIfWpM2ApA8TzvSYuNkCGj9Y2As="
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "state": "tx_+P4LAfiEuEBSzOkCFYv25mTRLzlYqvbF1GoURx/kFhseVI25MIpGr8tWMqRR+t9Xpty/KF2d8X84ALnAeHKyAH74RJRDgB0DuEDvoY3U0hP83PTmvveCan5EoOr2fmmOVgQzeSB+7KG9YDvEXmofBvmE8cTvRIWQnQ4hRjtH7cw9cR7GgItwChsGuHT4cjMBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgZB5KfubHFdjh8EG4xCGR0e6kWIfWpM2ApA8TzvSYuNkCGj9Y2As="
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "message": {
        "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "message": {
        "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
  "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "message": {
        "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "message": {
        "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "amount": 2
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBlmo/bF2SGuaNndCiay1Jo8C4fvfrty8jMGJkQ+adt1boQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWvwIAhg/AoHKQAKDNmaSTSTRoRmnF+iQrsKYc2CmTrB5E7GNocruXEohWugMJYB4bVQ==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainDeposit"
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
  "id": -576460752303423152,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEDEQHqYUJNjzBxnGbmKVg9i/B2RNPSGtnWF7Ldamv7pJPkZudp5cSEI25ULUlnlBB0PotUbX2O/Cvgvqo8bfVwHuHT4cjMBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgzZmkk0k0aEZpxfokK7CmHNgpk6weROxjaHK7lxKIVroDCYKPCCo="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
  "id": -576460752303423152,
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEDEQHqYUJNjzBxnGbmKVg9i/B2RNPSGtnWF7Ldamv7pJPkZudp5cSEI25ULUlnlBB0PotUbX2O/Cvgvqo8bfVwHuHT4cjMBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgzZmkk0k0aEZpxfokK7CmHNgpk6weROxjaHK7lxKIVroDCYKPCCo=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainDeposit"
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
  "id": -576460752303423151,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEC0j91R37ZXyOdCmxkAulXE7eR7PhF+scJYEXlsZgdrTBuVjLwZ1GpRJnMIfg2VyJttFrTO3zutqIHhxwxp8csOuEDEQHqYUJNjzBxnGbmKVg9i/B2RNPSGtnWF7Ldamv7pJPkZudp5cSEI25ULUlnlBB0PotUbX2O/Cvgvqo8bfVwHuHT4cjMBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgzZmkk0k0aEZpxfokK7CmHNgpk6weROxjaHK7lxKIVroDCXMmzV8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
  "id": -576460752303423151,
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEC0j91R37ZXyOdCmxkAulXE7eR7PhF+scJYEXlsZgdrTBuVjLwZ1GpRJnMIfg2VyJttFrTO3zutqIHhxwxp8csOuEDEQHqYUJNjzBxnGbmKVg9i/B2RNPSGtnWF7Ldamv7pJPkZudp5cSEI25ULUlnlBB0PotUbX2O/Cvgvqo8bfVwHuHT4cjMBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgzZmkk0k0aEZpxfokK7CmHNgpk6weROxjaHK7lxKIVroDCXMmzV8=",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEC0j91R37ZXyOdCmxkAulXE7eR7PhF+scJYEXlsZgdrTBuVjLwZ1GpRJnMIfg2VyJttFrTO3zutqIHhxwxp8csOuEDEQHqYUJNjzBxnGbmKVg9i/B2RNPSGtnWF7Ldamv7pJPkZudp5cSEI25ULUlnlBB0PotUbX2O/Cvgvqo8bfVwHuHT4cjMBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgzZmkk0k0aEZpxfokK7CmHNgpk6weROxjaHK7lxKIVroDCXMmzV8=",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "message": {
        "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "message": {
        "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEC0j91R37ZXyOdCmxkAulXE7eR7PhF+scJYEXlsZgdrTBuVjLwZ1GpRJnMIfg2VyJttFrTO3zutqIHhxwxp8csOuEDEQHqYUJNjzBxnGbmKVg9i/B2RNPSGtnWF7Ldamv7pJPkZudp5cSEI25ULUlnlBB0PotUbX2O/Cvgvqo8bfVwHuHT4cjMBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgzZmkk0k0aEZpxfokK7CmHNgpk6weROxjaHK7lxKIVroDCXMmzV8=",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEC0j91R37ZXyOdCmxkAulXE7eR7PhF+scJYEXlsZgdrTBuVjLwZ1GpRJnMIfg2VyJttFrTO3zutqIHhxwxp8csOuEDEQHqYUJNjzBxnGbmKVg9i/B2RNPSGtnWF7Ldamv7pJPkZudp5cSEI25ULUlnlBB0PotUbX2O/Cvgvqo8bfVwHuHT4cjMBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgzZmkk0k0aEZpxfokK7CmHNgpk6weROxjaHK7lxKIVroDCXMmzV8=",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "state": "tx_+P4LAfiEuEC0j91R37ZXyOdCmxkAulXE7eR7PhF+scJYEXlsZgdrTBuVjLwZ1GpRJnMIfg2VyJttFrTO3zutqIHhxwxp8csOuEDEQHqYUJNjzBxnGbmKVg9i/B2RNPSGtnWF7Ldamv7pJPkZudp5cSEI25ULUlnlBB0PotUbX2O/Cvgvqo8bfVwHuHT4cjMBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgzZmkk0k0aEZpxfokK7CmHNgpk6weROxjaHK7lxKIVroDCXMmzV8="
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "state": "tx_+P4LAfiEuEC0j91R37ZXyOdCmxkAulXE7eR7PhF+scJYEXlsZgdrTBuVjLwZ1GpRJnMIfg2VyJttFrTO3zutqIHhxwxp8csOuEDEQHqYUJNjzBxnGbmKVg9i/B2RNPSGtnWF7Ldamv7pJPkZudp5cSEI25ULUlnlBB0PotUbX2O/Cvgvqo8bfVwHuHT4cjMBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgzZmkk0k0aEZpxfokK7CmHNgpk6weROxjaHK7lxKIVroDCXMmzV8="
    }
  },
  "version": 1
}
```
