
#### initiator ---> node (2019-03-13 11:05:36.493)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "hejsan",
    "to": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
  }
}
```

#### responder <--- node (2019-03-13 11:05:36.499)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "message": {
        "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
        "from": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
        "info": "hejsan",
        "to": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:05:36.500)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "svejsan",
    "to": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
  }
}
```

#### initiator <--- node (2019-03-13 11:05:36.506)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "message": {
        "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
        "from": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
        "info": "svejsan",
        "to": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:36.506)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "first message in a row",
    "to": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
  }
}
```

#### responder <--- node (2019-03-13 11:05:36.522)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "message": {
        "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
        "from": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
        "info": "first message in a row",
        "to": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:36.523)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "second message in a row",
    "to": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
  }
}
```

#### responder <--- node (2019-03-13 11:05:36.565)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "message": {
        "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
        "from": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
        "info": "second message in a row",
        "to": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:05:36.567)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "some message",
    "to": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
  }
}
```

#### initiator <--- node (2019-03-13 11:05:36.578)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "message": {
        "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
        "from": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
        "info": "some message",
        "to": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:05:36.580)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "other message",
    "to": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
  }
}
```

#### initiator <--- node (2019-03-13 11:05:36.613)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "message": {
        "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
        "from": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
        "info": "other message",
        "to": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
      }
    }
  },
  "version": 1
}
```
