
#### initiator opens a WebSocket connection (2019-03-13 11:04:45.386)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=8&initiator_id=ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=4&responder_id=ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3&role=initiator&timeout_accept=100
```

#### initiator <--- node (2019-03-13 11:04:45.496)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```
