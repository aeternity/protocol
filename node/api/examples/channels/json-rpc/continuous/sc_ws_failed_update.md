
#### initiator info
> Failing update, insufficient balance

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 10000000000000000,
    "from": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
    "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
        "from": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
        "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
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
    "from": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
    "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
        "from": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
        "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
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
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "from": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc",
    "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
        "from": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc",
        "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
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
    "from": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc",
    "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
        "from": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc",
        "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
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
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
