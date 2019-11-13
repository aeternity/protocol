
#### initiator info
> Failing update, insufficient balance

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 10000000000000000,
    "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
        "code": 1001,
        "message": "Insufficient balance"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 10000000000000000,
        "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
        "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator info
> Failing update, negative amount

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": -1,
    "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
        "code": 1002,
        "message": "Negative amount"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": -1,
        "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
        "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator info
> Failing update, invalid pubkeys

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_11111111111111111111111111111115rHyByZ",
    "to": "ak_11111111111111111111111111111115sBJATr"
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
        "code": 1003,
        "message": "Invalid pubkeys"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_11111111111111111111111111111115rHyByZ",
        "to": "ak_11111111111111111111111111111115sBJATr"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder info
> Failing update, insufficient balance

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 10000000000000000,
    "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
        "code": 1001,
        "message": "Insufficient balance"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 10000000000000000,
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
        "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder info
> Failing update, negative amount

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": -1,
    "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
        "code": 1002,
        "message": "Negative amount"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": -1,
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
        "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder info
> Failing update, invalid pubkeys

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_11111111111111111111111111111115sBJATr",
    "to": "ak_11111111111111111111111111111115rHyByZ"
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
        "code": 1003,
        "message": "Invalid pubkeys"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_11111111111111111111111111111115sBJATr",
        "to": "ak_11111111111111111111111111111115rHyByZ"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```
