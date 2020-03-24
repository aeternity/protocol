
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```
