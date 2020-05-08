
#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "hejsan",
    "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "message": {
        "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
        "from": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
        "info": "hejsan",
        "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
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
    "info": "svejsan",
    "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "message": {
        "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
        "from": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc",
        "info": "svejsan",
        "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
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
    "info": "first message in a row",
    "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "message": {
        "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
        "from": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
        "info": "first message in a row",
        "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
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
    "info": "second message in a row",
    "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "message": {
        "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
        "from": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
        "info": "second message in a row",
        "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
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
    "info": "some message",
    "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "message": {
        "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
        "from": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc",
        "info": "some message",
        "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
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
    "info": "other message",
    "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "message": {
        "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
        "from": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc",
        "info": "other message",
        "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423471,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
      "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
  "id": -576460752303423471,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
      "balance": 69999999999999
    },
    {
      "account": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc",
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
    "from": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
    "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuErbkfh1o0Kle+dM27mB/wipGVUUudAVN7ro8unzZgRBqAzrQUdWvCQTFWw+4TYT/uqeVdIrHJXNUDwycCkGIf5fO6F0PM=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
          "op": "OffChainTransfer",
          "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
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
  "id": -576460752303423470,
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
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
  "id": -576460752303423470,
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
  "id": -576460752303423469,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
      "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
  "id": -576460752303423469,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
      "balance": 69999999999999
    },
    {
      "account": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423468,
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
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
  "id": -576460752303423468,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423467,
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
  "id": -576460752303423467,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
