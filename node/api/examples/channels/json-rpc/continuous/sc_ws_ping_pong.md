
#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```
