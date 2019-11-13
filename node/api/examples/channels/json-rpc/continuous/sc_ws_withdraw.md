
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
  "method": "channels.withdraw",
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
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBlmo/bF2SGuaNndCiay1Jo8C4fvfrty8jMGJkQ+adt1boQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FQIAhg/AoHKQAKCrqnfKzIiWVHOBzfLr5rNELJOPLHdCEdiPdzAvTDJPTwQbDMD9Ng==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303423150,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEB09ag0d70Iifsq5OffjC6Ws8Cn80tgxmpSuhrQPlNyHjOdRmYbTElSIyu4Azd8Sflz+GiVPXIZkbhsA66moAIAuHT4cjQBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgq6p3ysyIllRzgc3y6+azRCyTjyx3QhHYj3cwL0wyT08EG7e0fJA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
  "id": -576460752303423150,
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEB09ag0d70Iifsq5OffjC6Ws8Cn80tgxmpSuhrQPlNyHjOdRmYbTElSIyu4Azd8Sflz+GiVPXIZkbhsA66moAIAuHT4cjQBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgq6p3ysyIllRzgc3y6+azRCyTjyx3QhHYj3cwL0wyT08EG7e0fJA=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303423149,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBRkCcl2OgzpP7DwQT0QrgnHotWA9KcV5d/hlZFdSZt1x7zBr9E1AUsLM6yyJlTpgIfoNrkQ5Tm7bQjnLOAJIwOuEB09ag0d70Iifsq5OffjC6Ws8Cn80tgxmpSuhrQPlNyHjOdRmYbTElSIyu4Azd8Sflz+GiVPXIZkbhsA66moAIAuHT4cjQBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgq6p3ysyIllRzgc3y6+azRCyTjyx3QhHYj3cwL0wyT08EG4UYrBU="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
  "id": -576460752303423149,
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
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEBRkCcl2OgzpP7DwQT0QrgnHotWA9KcV5d/hlZFdSZt1x7zBr9E1AUsLM6yyJlTpgIfoNrkQ5Tm7bQjnLOAJIwOuEB09ag0d70Iifsq5OffjC6Ws8Cn80tgxmpSuhrQPlNyHjOdRmYbTElSIyu4Azd8Sflz+GiVPXIZkbhsA66moAIAuHT4cjQBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgq6p3ysyIllRzgc3y6+azRCyTjyx3QhHYj3cwL0wyT08EG4UYrBU=",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEBRkCcl2OgzpP7DwQT0QrgnHotWA9KcV5d/hlZFdSZt1x7zBr9E1AUsLM6yyJlTpgIfoNrkQ5Tm7bQjnLOAJIwOuEB09ag0d70Iifsq5OffjC6Ws8Cn80tgxmpSuhrQPlNyHjOdRmYbTElSIyu4Azd8Sflz+GiVPXIZkbhsA66moAIAuHT4cjQBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgq6p3ysyIllRzgc3y6+azRCyTjyx3QhHYj3cwL0wyT08EG4UYrBU=",
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
      "tx": "tx_+P4LAfiEuEBRkCcl2OgzpP7DwQT0QrgnHotWA9KcV5d/hlZFdSZt1x7zBr9E1AUsLM6yyJlTpgIfoNrkQ5Tm7bQjnLOAJIwOuEB09ag0d70Iifsq5OffjC6Ws8Cn80tgxmpSuhrQPlNyHjOdRmYbTElSIyu4Azd8Sflz+GiVPXIZkbhsA66moAIAuHT4cjQBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgq6p3ysyIllRzgc3y6+azRCyTjyx3QhHYj3cwL0wyT08EG4UYrBU=",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBRkCcl2OgzpP7DwQT0QrgnHotWA9KcV5d/hlZFdSZt1x7zBr9E1AUsLM6yyJlTpgIfoNrkQ5Tm7bQjnLOAJIwOuEB09ag0d70Iifsq5OffjC6Ws8Cn80tgxmpSuhrQPlNyHjOdRmYbTElSIyu4Azd8Sflz+GiVPXIZkbhsA66moAIAuHT4cjQBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgq6p3ysyIllRzgc3y6+azRCyTjyx3QhHYj3cwL0wyT08EG4UYrBU=",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "state": "tx_+P4LAfiEuEBRkCcl2OgzpP7DwQT0QrgnHotWA9KcV5d/hlZFdSZt1x7zBr9E1AUsLM6yyJlTpgIfoNrkQ5Tm7bQjnLOAJIwOuEB09ag0d70Iifsq5OffjC6Ws8Cn80tgxmpSuhrQPlNyHjOdRmYbTElSIyu4Azd8Sflz+GiVPXIZkbhsA66moAIAuHT4cjQBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgq6p3ysyIllRzgc3y6+azRCyTjyx3QhHYj3cwL0wyT08EG4UYrBU="
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
      "state": "tx_+P4LAfiEuEBRkCcl2OgzpP7DwQT0QrgnHotWA9KcV5d/hlZFdSZt1x7zBr9E1AUsLM6yyJlTpgIfoNrkQ5Tm7bQjnLOAJIwOuEB09ag0d70Iifsq5OffjC6Ws8Cn80tgxmpSuhrQPlNyHjOdRmYbTElSIyu4Azd8Sflz+GiVPXIZkbhsA66moAIAuHT4cjQBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RUCAIYPwKBykACgq6p3ysyIllRzgc3y6+azRCyTjyx3QhHYj3cwL0wyT08EG4UYrBU="
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
  "method": "channels.withdraw",
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
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBlmo/bF2SGuaNndCiay1Jo8C4fvfrty8jMGJkQ+adt1boQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWvwIAhg/AoHKQAKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdgUKsb+isA==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303423148,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuED0BTvLuQMsRfJkS+tPkux6RKev6+dHkqTp84c/vEK2Ruccv1svB9tdFuAEMo3bO7GkVQG2dIATlvEmItbhzpoKuHT4cjQBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYFCpOTx24="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
  "id": -576460752303423148,
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "signed_tx": "tx_+LwLAfhCuED0BTvLuQMsRfJkS+tPkux6RKev6+dHkqTp84c/vEK2Ruccv1svB9tdFuAEMo3bO7GkVQG2dIATlvEmItbhzpoKuHT4cjQBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYFCpOTx24=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303423147,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBj9ingo4M1MOwzXQYzCZLiAx+Ep6eOMENGTaj0k7TJalokBH9Nxq4WKdVIygOl/EKPTjgMV51bQxJACBtQqlcLuED0BTvLuQMsRfJkS+tPkux6RKev6+dHkqTp84c/vEK2Ruccv1svB9tdFuAEMo3bO7GkVQG2dIATlvEmItbhzpoKuHT4cjQBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYFCo4GxA0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
  "id": -576460752303423147,
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
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEBj9ingo4M1MOwzXQYzCZLiAx+Ep6eOMENGTaj0k7TJalokBH9Nxq4WKdVIygOl/EKPTjgMV51bQxJACBtQqlcLuED0BTvLuQMsRfJkS+tPkux6RKev6+dHkqTp84c/vEK2Ruccv1svB9tdFuAEMo3bO7GkVQG2dIATlvEmItbhzpoKuHT4cjQBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYFCo4GxA0=",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEBj9ingo4M1MOwzXQYzCZLiAx+Ep6eOMENGTaj0k7TJalokBH9Nxq4WKdVIygOl/EKPTjgMV51bQxJACBtQqlcLuED0BTvLuQMsRfJkS+tPkux6RKev6+dHkqTp84c/vEK2Ruccv1svB9tdFuAEMo3bO7GkVQG2dIATlvEmItbhzpoKuHT4cjQBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYFCo4GxA0=",
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
      "tx": "tx_+P4LAfiEuEBj9ingo4M1MOwzXQYzCZLiAx+Ep6eOMENGTaj0k7TJalokBH9Nxq4WKdVIygOl/EKPTjgMV51bQxJACBtQqlcLuED0BTvLuQMsRfJkS+tPkux6RKev6+dHkqTp84c/vEK2Ruccv1svB9tdFuAEMo3bO7GkVQG2dIATlvEmItbhzpoKuHT4cjQBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYFCo4GxA0=",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBj9ingo4M1MOwzXQYzCZLiAx+Ep6eOMENGTaj0k7TJalokBH9Nxq4WKdVIygOl/EKPTjgMV51bQxJACBtQqlcLuED0BTvLuQMsRfJkS+tPkux6RKev6+dHkqTp84c/vEK2Ruccv1svB9tdFuAEMo3bO7GkVQG2dIATlvEmItbhzpoKuHT4cjQBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYFCo4GxA0=",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "state": "tx_+P4LAfiEuEBj9ingo4M1MOwzXQYzCZLiAx+Ep6eOMENGTaj0k7TJalokBH9Nxq4WKdVIygOl/EKPTjgMV51bQxJACBtQqlcLuED0BTvLuQMsRfJkS+tPkux6RKev6+dHkqTp84c/vEK2Ruccv1svB9tdFuAEMo3bO7GkVQG2dIATlvEmItbhzpoKuHT4cjQBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYFCo4GxA0="
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
      "state": "tx_+P4LAfiEuEBj9ingo4M1MOwzXQYzCZLiAx+Ep6eOMENGTaj0k7TJalokBH9Nxq4WKdVIygOl/EKPTjgMV51bQxJACBtQqlcLuED0BTvLuQMsRfJkS+tPkux6RKev6+dHkqTp84c/vEK2Ruccv1svB9tdFuAEMo3bO7GkVQG2dIATlvEmItbhzpoKuHT4cjQBoQZZqP2xdkhrmjZ3QomstSaPAuH7367cvIzBiZEPmnbdW6EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r8CAIYPwKBykACgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYFCo4GxA0="
    }
  },
  "version": 1
}
```
