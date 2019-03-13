
#### initiator: (2019-03-13 11:05:36.348)
> Failing update, insufficient balance

#### initiator ---> node (2019-03-13 11:05:36.349)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 10000000000000000,
    "from": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
    "to": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
  }
}
```

#### initiator <--- node (2019-03-13 11:05:36.360)
```javascript
{
  "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
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
        "from": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
        "to": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator: (2019-03-13 11:05:36.360)
> Failing update, negative amount

#### initiator ---> node (2019-03-13 11:05:36.361)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": -1,
    "from": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
    "to": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
  }
}
```

#### initiator <--- node (2019-03-13 11:05:36.362)
```javascript
{
  "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
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
        "from": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
        "to": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator: (2019-03-13 11:05:36.362)
> Failing update, invalid pubkeys

#### initiator ---> node (2019-03-13 11:05:36.363)
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

#### initiator <--- node (2019-03-13 11:05:36.368)
```javascript
{
  "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
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

#### responder: (2019-03-13 11:05:36.369)
> Failing update, insufficient balance

#### responder ---> node (2019-03-13 11:05:36.369)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 10000000000000000,
    "from": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
    "to": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
  }
}
```

#### responder <--- node (2019-03-13 11:05:36.395)
```javascript
{
  "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
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
        "from": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
        "to": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder: (2019-03-13 11:05:36.409)
> Failing update, negative amount

#### responder ---> node (2019-03-13 11:05:36.409)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": -1,
    "from": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
    "to": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
  }
}
```

#### responder <--- node (2019-03-13 11:05:36.411)
```javascript
{
  "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
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
        "from": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
        "to": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder: (2019-03-13 11:05:36.412)
> Failing update, invalid pubkeys

#### responder ---> node (2019-03-13 11:05:36.413)
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

#### responder <--- node (2019-03-13 11:05:36.424)
```javascript
{
  "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
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
