
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
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
    "channel_id": "ch_gVFMSZo5GDizRHSr6fWWKr2fVA7RYNiKvXU7KiHSGWNwZeVLJ",
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```
