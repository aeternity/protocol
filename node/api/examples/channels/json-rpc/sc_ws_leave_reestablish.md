
#### initiator opens a WebSocket connection (2019-03-13 11:05:03.620)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3&role=initiator
```

#### responder opens a WebSocket connection (2019-03-13 11:05:03.643)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3&role=responder
```

#### responder <--- node (2019-03-13 11:05:04.624)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_open"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:04.629)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_accept"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:04.654)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAV8Pkv8"
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:04.742)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_+MsLAfhCuEAZim9XZjYUTRhp5B31JfNwjP1gLFfI3EHw1Dn+J+YhdybHb/Yc1luATTUlav1QWLevg0ZeGws5wgBR6vJbj6QFuIP4gTIBoQEmB6t0j6CEj0TF7aBkfLKhLNj0/vfE3UYgZ2CLIgbnp4Y/qiUiYAChAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPhiRhOcqAAAIKAIYSMJzlQADAoODtFIhe84yV0+uaXXnfGCrRRApvdISmjmGVfhKf0nkoBel7jVA="
  }
}
```

#### responder <--- node (2019-03-13 11:05:04.759)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "funding_created"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:04.760)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAV8Pkv8"
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:05:04.761)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_+MsLAfhCuEDPGfdAQTEKxTjtDMcRfNL4XG4qJ2i0+bj1dYj84vkTeOsl/DzAn1U2NYXSmq27oAjTZJ4TqJrm8MoBDGgHdhUGuIP4gTIBoQEmB6t0j6CEj0TF7aBkfLKhLNj0/vfE3UYgZ2CLIgbnp4Y/qiUiYAChAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPhiRhOcqAAAIKAIYSMJzlQADAoODtFIhe84yV0+uaXXnfGCrRRApvdISmjmGVfhKf0nkoBZARDAc="
  }
}
```

#### responder <--- node (2019-03-13 11:05:04.774)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+QENCwH4hLhAGYpvV2Y2FE0YaeQd9SXzcIz9YCxXyNxB8NQ5/ifmIXcmx2/2HNZbgE01JWr9UFi3r4NGXhsLOcIAUeryW4+kBbhAzxn3QEExCsU47QzHEXzS+FxuKidotPm49XWI/OL5E3jrJfw8wJ9VNjWF0pqtu6AI02SeE6ia5vDKAQxoB3YVBriD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAXc1vn8"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:04.776)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "funding_signed"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:04.778)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+QENCwH4hLhAGYpvV2Y2FE0YaeQd9SXzcIz9YCxXyNxB8NQ5/ifmIXcmx2/2HNZbgE01JWr9UFi3r4NGXhsLOcIAUeryW4+kBbhAzxn3QEExCsU47QzHEXzS+FxuKidotPm49XWI/OL5E3jrJfw8wJ9VNjWF0pqtu6AI02SeE6ia5vDKAQxoB3YVBriD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAXc1vn8"
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:06.55)
```javascript
{
  "id": -576460752303423470,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
    ]
  }
}
```

#### initiator <--- node (2019-03-13 11:05:06.60)
```javascript
{
  "channel_id": null,
  "id": -576460752303423470,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "balance": 69999999999999
    },
    {
      "account": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:07.397)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:07.403)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:07.404)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:07.408)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:07.419)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:07.420)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "state": "tx_+QENCwH4hLhAGYpvV2Y2FE0YaeQd9SXzcIz9YCxXyNxB8NQ5/ifmIXcmx2/2HNZbgE01JWr9UFi3r4NGXhsLOcIAUeryW4+kBbhAzxn3QEExCsU47QzHEXzS+FxuKidotPm49XWI/OL5E3jrJfw8wJ9VNjWF0pqtu6AI02SeE6ia5vDKAQxoB3YVBriD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAXc1vn8"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:07.421)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:07.426)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "state": "tx_+QENCwH4hLhAGYpvV2Y2FE0YaeQd9SXzcIz9YCxXyNxB8NQ5/ifmIXcmx2/2HNZbgE01JWr9UFi3r4NGXhsLOcIAUeryW4+kBbhAzxn3QEExCsU47QzHEXzS+FxuKidotPm49XWI/OL5E3jrJfw8wJ9VNjWF0pqtu6AI02SeE6ia5vDKAQxoB3YVBriD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAXc1vn8"
    }
  },
  "version": 1
}
```

#### initiator: (2019-03-13 11:05:07.645)
> Funding has been confirmed locally on-chain

#### responder: (2019-03-13 11:05:07.645)
> Funding has been confirmed locally on-chain

#### initiator: (2019-03-13 11:05:07.646)
> Funding has been confirmed on-chain by other party

#### responder: (2019-03-13 11:05:07.646)
> Funding has been confirmed on-chain by other party

#### initiator: (2019-03-13 11:05:07.646)
> Channel is `open` and ready to use

#### responder: (2019-03-13 11:05:07.646)
> Channel is `open` and ready to use

#### initiator ---> node (2019-03-13 11:05:07.646)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {}
}
```

#### responder <--- node (2019-03-13 11:05:07.656)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "state": "tx_+QENCwH4hLhAGYpvV2Y2FE0YaeQd9SXzcIz9YCxXyNxB8NQ5/ifmIXcmx2/2HNZbgE01JWr9UFi3r4NGXhsLOcIAUeryW4+kBbhAzxn3QEExCsU47QzHEXzS+FxuKidotPm49XWI/OL5E3jrJfw8wJ9VNjWF0pqtu6AI02SeE6ia5vDKAQxoB3YVBriD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAXc1vn8"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:07.657)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:07.659)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "state": "tx_+QENCwH4hLhAGYpvV2Y2FE0YaeQd9SXzcIz9YCxXyNxB8NQ5/ifmIXcmx2/2HNZbgE01JWr9UFi3r4NGXhsLOcIAUeryW4+kBbhAzxn3QEExCsU47QzHEXzS+FxuKidotPm49XWI/OL5E3jrJfw8wJ9VNjWF0pqtu6AI02SeE6ia5vDKAQxoB3YVBriD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAXc1vn8"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:07.660)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder opens a WebSocket connection (2019-03-13 11:05:07.695)
```
ws://localhost:3014/channel?channel_reserve=2&existing_channel_id=ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV&initiator_amount=70000000000000&initiator_id=ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs&lock_period=10&offchain_tx=tx_%2BQENCwH4hLhAGYpvV2Y2FE0YaeQd9SXzcIz9YCxXyNxB8NQ5%2FifmIXcmx2%2F2HNZbgE01JWr9UFi3r4NGXhsLOcIAUeryW4%2BkBbhAzxn3QEExCsU47QzHEXzS%2BFxuKidotPm49XWI%2FOL5E3jrJfw8wJ9VNjWF0pqtu6AI02SeE6ia5vDKAQxoB3YVBriD%2BIEyAaEBJgerdI%2BghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX%2Fj6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAXc1vn8&port=12341&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3&role=responder
```

#### initiator opens a WebSocket connection (2019-03-13 11:05:07.724)
```
ws://localhost:3014/channel?channel_reserve=2&existing_channel_id=ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV&host=localhost&initiator_amount=70000000000000&initiator_id=ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs&lock_period=10&offchain_tx=tx_%2BQENCwH4hLhAGYpvV2Y2FE0YaeQd9SXzcIz9YCxXyNxB8NQ5%2FifmIXcmx2%2F2HNZbgE01JWr9UFi3r4NGXhsLOcIAUeryW4%2BkBbhAzxn3QEExCsU47QzHEXzS%2BFxuKidotPm49XWI%2FOL5E3jrJfw8wJ9VNjWF0pqtu6AI02SeE6ia5vDKAQxoB3YVBriD%2BIEyAaEBJgerdI%2BghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX%2Fj6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAXc1vn8&port=12341&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3&role=initiator
```

#### responder <--- node (2019-03-13 11:05:07.732)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_reestablished"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:07.734)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:07.736)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "state": "tx_+QENCwH4hLhAGYpvV2Y2FE0YaeQd9SXzcIz9YCxXyNxB8NQ5/ifmIXcmx2/2HNZbgE01JWr9UFi3r4NGXhsLOcIAUeryW4+kBbhAzxn3QEExCsU47QzHEXzS+FxuKidotPm49XWI/OL5E3jrJfw8wJ9VNjWF0pqtu6AI02SeE6ia5vDKAQxoB3YVBriD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAXc1vn8"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:07.738)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_reestablished"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:07.738)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:07.747)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "state": "tx_+QENCwH4hLhAGYpvV2Y2FE0YaeQd9SXzcIz9YCxXyNxB8NQ5/ifmIXcmx2/2HNZbgE01JWr9UFi3r4NGXhsLOcIAUeryW4+kBbhAzxn3QEExCsU47QzHEXzS+FxuKidotPm49XWI/OL5E3jrJfw8wJ9VNjWF0pqtu6AI02SeE6ia5vDKAQxoB3YVBriD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAXc1vn8"
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:07.748)
```javascript
{
  "id": -576460752303423469,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
    ]
  }
}
```

#### initiator <--- node (2019-03-13 11:05:07.753)
```javascript
{
  "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
  "id": -576460752303423469,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "balance": 69999999999999
    },
    {
      "account": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:07.753)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
    "to": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
  }
}
```

#### initiator <--- node (2019-03-13 11:05:07.766)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "tx": "tx_+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAC+E24S/hJggI6AaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56ehAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAaDbfGCXUMfw4lZS/r1ddw6JYAjcG83JwCYsD8jmhgKs0iT7yeY="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:07.767)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuEAiTpk3r2nxL2cAbcJ2vZRGFmHlBRM7nguN7NjlczFEqOtss7Cvh3nXna8WEY8FhGbFpG2y2n2jzbIx/04bZ6UKuJf4lTkBoQblSG+6EeU0frxZE9lGC2sNKQGdEocv/3udxRU5nP8d8AL4TbhL+EmCAjoBoQEmB6t0j6CEj0TF7aBkfLKhLNj0/vfE3UYgZ2CLIgbnp6EBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA208BoNt8YJdQx/DiVlL+vV13DolgCNwbzcnAJiwPyOaGAqzSiyiyVQ=="
  }
}
```

#### responder <--- node (2019-03-13 11:05:07.826)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:07.827)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "tx": "tx_+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAC+E24S/hJggI6AaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56ehAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAaDbfGCXUMfw4lZS/r1ddw6JYAjcG83JwCYsD8jmhgKs0iT7yeY="
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:05:07.828)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+N8LAfhCuEAQ+oQ/OUnu0LS6/FW/vqSgpOUR4G64WFpqvu7Ywjv6OFkcnmflJERZTgebPP9hg5PnzGkoS0i9CFmrLIi0bT4MuJf4lTkBoQblSG+6EeU0frxZE9lGC2sNKQGdEocv/3udxRU5nP8d8AL4TbhL+EmCAjoBoQEmB6t0j6CEj0TF7aBkfLKhLNj0/vfE3UYgZ2CLIgbnp6EBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA208BoNt8YJdQx/DiVlL+vV13DolgCNwbzcnAJiwPyOaGAqzSqQygXA=="
  }
}
```

#### responder <--- node (2019-03-13 11:05:07.857)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "state": "tx_+QEhCwH4hLhAEPqEPzlJ7tC0uvxVv76koKTlEeBuuFhaar7u2MI7+jhZHJ5n5SREWU4Hmzz/YYOT58xpKEtIvQhZqyyItG0+DLhAIk6ZN69p8S9nAG3Cdr2URhZh5QUTO54LjezY5XMxRKjrbLOwr4d5152vFhGPBYRmxaRtstp9o82yMf9OG2elCriX+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAC+E24S/hJggI6AaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56ehAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAaDbfGCXUMfw4lZS/r1ddw6JYAjcG83JwCYsD8jmhgKs0k8l2CA="
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:07.874)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "state": "tx_+QEhCwH4hLhAEPqEPzlJ7tC0uvxVv76koKTlEeBuuFhaar7u2MI7+jhZHJ5n5SREWU4Hmzz/YYOT58xpKEtIvQhZqyyItG0+DLhAIk6ZN69p8S9nAG3Cdr2URhZh5QUTO54LjezY5XMxRKjrbLOwr4d5152vFhGPBYRmxaRtstp9o82yMf9OG2elCriX+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAC+E24S/hJggI6AaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56ehAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAaDbfGCXUMfw4lZS/r1ddw6JYAjcG83JwCYsD8jmhgKs0k8l2CA="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:07.892)
```javascript
{
  "id": -576460752303423468,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
    ]
  }
}
```

#### initiator <--- node (2019-03-13 11:05:07.896)
```javascript
{
  "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
  "id": -576460752303423468,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "balance": 69999999999998
    },
    {
      "account": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:07.897)
```javascript
{
  "id": -576460752303423467,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node (2019-03-13 11:05:07.902)
```javascript
{
  "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
  "id": -576460752303423467,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAEPqEPzlJ7tC0uvxVv76koKTlEeBuuFhaar7u2MI7+jhZHJ5n5SREWU4Hmzz/YYOT58xpKEtIvQhZqyyItG0+DLhAIk6ZN69p8S9nAG3Cdr2URhZh5QUTO54LjezY5XMxRKjrbLOwr4d5152vFhGPBYRmxaRtstp9o82yMf9OG2elCriX+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAC+E24S/hJggI6AaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56ehAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAaDbfGCXUMfw4lZS/r1ddw6JYAjcG83JwCYsD8jmhgKs0k8l2CA=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4vKCgEAhiRhOcqAArDvQAGgJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eLygoBAIY/qiUiX/5NyGDh"
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:07.908)
```javascript
{
  "id": -576460752303423466,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
    ]
  }
}
```

#### initiator <--- node (2019-03-13 11:05:07.912)
```javascript
{
  "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
  "id": -576460752303423466,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "balance": 40000000000002
    },
    {
      "account": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "balance": 69999999999998
    }
  ],
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:05:07.913)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
    "to": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
  }
}
```

#### responder <--- node (2019-03-13 11:05:07.926)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "tx": "tx_+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAD+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KM0PDPA="
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:05:07.927)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuECLzpS6vKoae/O5xNaBxMS4VsbEzDV712YM7RCvaC2B5KnWkjbTwbVVtithKmbhBBAtCwjwdjzGgUrZjexlqXkJuJf4lTkBoQblSG+6EeU0frxZE9lGC2sNKQGdEocv/3udxRU5nP8d8AP4TbhL+EmCAjoBoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT6EBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cBoODtFIhe84yV0+uaXXnfGCrRRApvdISmjmGVfhKf0nkoW33p1w=="
  }
}
```

#### initiator <--- node (2019-03-13 11:05:07.962)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:07.963)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "tx": "tx_+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAD+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KM0PDPA="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:07.964)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+N8LAfhCuEA0rEQ+sN6jzvrSFnyLX422CSpYC1izt/hWQZ4IFrMTq3uUytNFnaYJT+fzXzK0YwNJP0Kuv/psnTFCuwp099oLuJf4lTkBoQblSG+6EeU0frxZE9lGC2sNKQGdEocv/3udxRU5nP8d8AP4TbhL+EmCAjoBoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT6EBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cBoODtFIhe84yV0+uaXXnfGCrRRApvdISmjmGVfhKf0nkonrNQAA=="
  }
}
```

#### initiator <--- node (2019-03-13 11:05:07.988)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "state": "tx_+QEhCwH4hLhANKxEPrDeo8760hZ8i1+NtgkqWAtYs7f4VkGeCBazE6t7lMrTRZ2mCU/n818ytGMDST9Crr/6bJ0xQrsKdPfaC7hAi86UuryqGnvzucTWgcTEuFbGxMw1e9dmDO0Qr2gtgeSp1pI208G1VbYrYSpm4QQQLQsI8HY8xoFK2Y3sZal5CbiX+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAD+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KNNiEKU="
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:08.11)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "state": "tx_+QEhCwH4hLhANKxEPrDeo8760hZ8i1+NtgkqWAtYs7f4VkGeCBazE6t7lMrTRZ2mCU/n818ytGMDST9Crr/6bJ0xQrsKdPfaC7hAi86UuryqGnvzucTWgcTEuFbGxMw1e9dmDO0Qr2gtgeSp1pI208G1VbYrYSpm4QQQLQsI8HY8xoFK2Y3sZal5CbiX+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAD+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KNNiEKU="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:08.20)
```javascript
{
  "id": -576460752303423465,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
    ]
  }
}
```

#### initiator <--- node (2019-03-13 11:05:08.24)
```javascript
{
  "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
  "id": -576460752303423465,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "balance": 40000000000001
    },
    {
      "account": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:08.25)
```javascript
{
  "id": -576460752303423464,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node (2019-03-13 11:05:08.29)
```javascript
{
  "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
  "id": -576460752303423464,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhANKxEPrDeo8760hZ8i1+NtgkqWAtYs7f4VkGeCBazE6t7lMrTRZ2mCU/n818ytGMDST9Crr/6bJ0xQrsKdPfaC7hAi86UuryqGnvzucTWgcTEuFbGxMw1e9dmDO0Qr2gtgeSp1pI208G1VbYrYSpm4QQQLQsI8HY8xoFK2Y3sZal5CbiX+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAD+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KNNiEKU=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4vKCgEAhiRhOcqAAbDvQAGgJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eLygoBAIY/qiUiX//8omNo"
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:08.35)
```javascript
{
  "id": -576460752303423463,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
    ]
  }
}
```

#### initiator <--- node (2019-03-13 11:05:08.48)
```javascript
{
  "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
  "id": -576460752303423463,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "balance": 40000000000001
    },
    {
      "account": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:05:08.49)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
    "to": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
  }
}
```

#### responder <--- node (2019-03-13 11:05:08.61)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "tx": "tx_+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAE+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaBtJeqayYNAxAR8VEb/US6Hb7IetZ7x8ND25z+UAJu3M6zOSDg="
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:05:08.62)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuEDe2Nsv77s+MYsojCjpR4w1rl9mWAYCvHXRjOW+a4xDMNGUp/GiZYeYxrAjgntneg6k4FpDwV4aMVNMEbkhHZoLuJf4lTkBoQblSG+6EeU0frxZE9lGC2sNKQGdEocv/3udxRU5nP8d8AT4TbhL+EmCAjoBoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT6EBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cBoG0l6prJg0DEBHxURv9RLodvsh61nvHw0PbnP5QAm7czKxiLFQ=="
  }
}
```

#### initiator <--- node (2019-03-13 11:05:08.100)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:08.101)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "tx": "tx_+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAE+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaBtJeqayYNAxAR8VEb/US6Hb7IetZ7x8ND25z+UAJu3M6zOSDg="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:08.102)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+N8LAfhCuEAVkRSdnrHa/bNHA/AoQjPqRedMV2Rh3EBc22NgwpP8tU22zSz2zlqc9yjHlXDXJ8dKy8aCBaUdox4avHVGdqULuJf4lTkBoQblSG+6EeU0frxZE9lGC2sNKQGdEocv/3udxRU5nP8d8AT4TbhL+EmCAjoBoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT6EBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cBoG0l6prJg0DEBHxURv9RLodvsh61nvHw0PbnP5QAm7czndfIzg=="
  }
}
```

#### initiator <--- node (2019-03-13 11:05:08.128)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "state": "tx_+QEhCwH4hLhAFZEUnZ6x2v2zRwPwKEIz6kXnTFdkYdxAXNtjYMKT/LVNts0s9s5anPcox5Vw1yfHSsvGggWlHaMeGrx1RnalC7hA3tjbL++7PjGLKIwo6UeMNa5fZlgGArx10YzlvmuMQzDRlKfxomWHmMawI4J7Z3oOpOBaQ8FeGjFTTBG5IR2aC7iX+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAE+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaBtJeqayYNAxAR8VEb/US6Hb7IetZ7x8ND25z+UAJu3Mxizy7k="
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:08.142)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "state": "tx_+QEhCwH4hLhAFZEUnZ6x2v2zRwPwKEIz6kXnTFdkYdxAXNtjYMKT/LVNts0s9s5anPcox5Vw1yfHSsvGggWlHaMeGrx1RnalC7hA3tjbL++7PjGLKIwo6UeMNa5fZlgGArx10YzlvmuMQzDRlKfxomWHmMawI4J7Z3oOpOBaQ8FeGjFTTBG5IR2aC7iX+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAE+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaBtJeqayYNAxAR8VEb/US6Hb7IetZ7x8ND25z+UAJu3Mxizy7k="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:08.151)
```javascript
{
  "id": -576460752303423462,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
    ]
  }
}
```

#### initiator <--- node (2019-03-13 11:05:08.156)
```javascript
{
  "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
  "id": -576460752303423462,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "balance": 40000000000000
    },
    {
      "account": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:08.156)
```javascript
{
  "id": -576460752303423461,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node (2019-03-13 11:05:08.162)
```javascript
{
  "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
  "id": -576460752303423461,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAFZEUnZ6x2v2zRwPwKEIz6kXnTFdkYdxAXNtjYMKT/LVNts0s9s5anPcox5Vw1yfHSsvGggWlHaMeGrx1RnalC7hA3tjbL++7PjGLKIwo6UeMNa5fZlgGArx10YzlvmuMQzDRlKfxomWHmMawI4J7Z3oOpOBaQ8FeGjFTTBG5IR2aC7iX+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAE+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaBtJeqayYNAxAR8VEb/US6Hb7IetZ7x8ND25z+UAJu3Mxizy7k=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4vKCgEAhiRhOcqAALDvQAGgJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eLygoBAIY/qiUiYADbIKsP"
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:08.174)
```javascript
{
  "id": -576460752303423460,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
    ]
  }
}
```

#### initiator <--- node (2019-03-13 11:05:08.183)
```javascript
{
  "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
  "id": -576460752303423460,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "balance": 70000000000000
    },
    {
      "account": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "balance": 40000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:08.184)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
    "to": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
  }
}
```

#### initiator <--- node (2019-03-13 11:05:08.197)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "tx": "tx_+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAF+E24S/hJggI6AaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56ehAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAaDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KJS2/ZQ="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:08.200)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuEB9gTnVEhco8ooV1fRQrYloZXI/AGtisPbj4rQlQES4FH9VqfpcIBmRCxPjXpOAP6bcg2uTEw02uSMWvHAwLZYBuJf4lTkBoQblSG+6EeU0frxZE9lGC2sNKQGdEocv/3udxRU5nP8d8AX4TbhL+EmCAjoBoQEmB6t0j6CEj0TF7aBkfLKhLNj0/vfE3UYgZ2CLIgbnp6EBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA208BoODtFIhe84yV0+uaXXnfGCrRRApvdISmjmGVfhKf0nko7leKuQ=="
  }
}
```

#### responder <--- node (2019-03-13 11:05:08.238)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:08.239)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "tx": "tx_+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAF+E24S/hJggI6AaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56ehAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAaDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KJS2/ZQ="
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:05:08.240)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+N8LAfhCuECImSNesghwrfdnkq7YTyft18b9RGfzsD+4j45Irl4X0VZz/LRXKwc4vME18VT+71Vx/jJd40x5uG9wDU86cqsCuJf4lTkBoQblSG+6EeU0frxZE9lGC2sNKQGdEocv/3udxRU5nP8d8AX4TbhL+EmCAjoBoQEmB6t0j6CEj0TF7aBkfLKhLNj0/vfE3UYgZ2CLIgbnp6EBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA208BoODtFIhe84yV0+uaXXnfGCrRRApvdISmjmGVfhKf0nkoku06vQ=="
  }
}
```

#### responder <--- node (2019-03-13 11:05:08.271)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "state": "tx_+QEhCwH4hLhAfYE51RIXKPKKFdX0UK2JaGVyPwBrYrD24+K0JUBEuBR/Van6XCAZkQsT416TgD+m3INrkxMNNrkjFrxwMC2WAbhAiJkjXrIIcK33Z5Ku2E8n7dfG/URn87A/uI+OSK5eF9FWc/y0VysHOLzBNfFU/u9Vcf4yXeNMebhvcA1POnKrAriX+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAF+E24S/hJggI6AaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56ehAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAaDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KPgpNek="
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:08.287)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "state": "tx_+QEhCwH4hLhAfYE51RIXKPKKFdX0UK2JaGVyPwBrYrD24+K0JUBEuBR/Van6XCAZkQsT416TgD+m3INrkxMNNrkjFrxwMC2WAbhAiJkjXrIIcK33Z5Ku2E8n7dfG/URn87A/uI+OSK5eF9FWc/y0VysHOLzBNfFU/u9Vcf4yXeNMebhvcA1POnKrAriX+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAF+E24S/hJggI6AaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56ehAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAaDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KPgpNek="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:08.297)
```javascript
{
  "id": -576460752303423459,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
    ]
  }
}
```

#### initiator <--- node (2019-03-13 11:05:08.302)
```javascript
{
  "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
  "id": -576460752303423459,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "balance": 69999999999999
    },
    {
      "account": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:08.302)
```javascript
{
  "id": -576460752303423458,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node (2019-03-13 11:05:08.308)
```javascript
{
  "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
  "id": -576460752303423458,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAfYE51RIXKPKKFdX0UK2JaGVyPwBrYrD24+K0JUBEuBR/Van6XCAZkQsT416TgD+m3INrkxMNNrkjFrxwMC2WAbhAiJkjXrIIcK33Z5Ku2E8n7dfG/URn87A/uI+OSK5eF9FWc/y0VysHOLzBNfFU/u9Vcf4yXeNMebhvcA1POnKrAriX+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAF+E24S/hJggI6AaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56ehAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAaDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KPgpNek=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4vKCgEAhiRhOcqAAbDvQAGgJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eLygoBAIY/qiUiX//8omNo"
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:08.313)
```javascript
{
  "id": -576460752303423457,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
    ]
  }
}
```

#### initiator <--- node (2019-03-13 11:05:08.318)
```javascript
{
  "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
  "id": -576460752303423457,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "balance": 40000000000001
    },
    {
      "account": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:05:08.319)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
    "to": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
  }
}
```

#### responder <--- node (2019-03-13 11:05:08.332)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "tx": "tx_+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAG+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaBtJeqayYNAxAR8VEb/US6Hb7IetZ7x8ND25z+UAJu3MzV4BOA="
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:05:08.333)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuECIh9GgRHqKevSHreZ+FlaJ5jCjvt6XSragwKFt4ieZjhq4v6PU1H2ZuSWfpTVc+bCCZQEsTAz6wVnEx33bsf0HuJf4lTkBoQblSG+6EeU0frxZE9lGC2sNKQGdEocv/3udxRU5nP8d8Ab4TbhL+EmCAjoBoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT6EBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cBoG0l6prJg0DEBHxURv9RLodvsh61nvHw0PbnP5QAm7czcL1irg=="
  }
}
```

#### initiator <--- node (2019-03-13 11:05:08.372)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:08.373)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "tx": "tx_+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAG+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaBtJeqayYNAxAR8VEb/US6Hb7IetZ7x8ND25z+UAJu3MzV4BOA="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:08.374)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+N8LAfhCuEB5KKXhf5p8Gnnz4ig+F5XDQkHmRXWkoXHmkd3nMnWoMDEhjOpCy7nS4oChkpOwZsQ0M7DtM3CdEYb3/u+mGMUEuJf4lTkBoQblSG+6EeU0frxZE9lGC2sNKQGdEocv/3udxRU5nP8d8Ab4TbhL+EmCAjoBoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT6EBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cBoG0l6prJg0DEBHxURv9RLodvsh61nvHw0PbnP5QAm7czdnh+6Q=="
  }
}
```

#### initiator <--- node (2019-03-13 11:05:08.400)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "state": "tx_+QEhCwH4hLhAeSil4X+afBp58+IoPheVw0JB5kV1pKFx5pHd5zJ1qDAxIYzqQsu50uKAoZKTsGbENDOw7TNwnRGG9/7vphjFBLhAiIfRoER6inr0h63mfhZWieYwo77el0q2oMChbeInmY4auL+j1NR9mbkln6U1XPmwgmUBLEwM+sFZxMd927H9B7iX+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAG+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaBtJeqayYNAxAR8VEb/US6Hb7IetZ7x8ND25z+UAJu3M5PN7OY="
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:08.413)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
    "data": {
      "state": "tx_+QEhCwH4hLhAeSil4X+afBp58+IoPheVw0JB5kV1pKFx5pHd5zJ1qDAxIYzqQsu50uKAoZKTsGbENDOw7TNwnRGG9/7vphjFBLhAiIfRoER6inr0h63mfhZWieYwo77el0q2oMChbeInmY4auL+j1NR9mbkln6U1XPmwgmUBLEwM+sFZxMd927H9B7iX+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAG+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaBtJeqayYNAxAR8VEb/US6Hb7IetZ7x8ND25z+UAJu3M5PN7OY="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:08.430)
```javascript
{
  "id": -576460752303423456,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
    ]
  }
}
```

#### initiator <--- node (2019-03-13 11:05:08.435)
```javascript
{
  "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
  "id": -576460752303423456,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "balance": 40000000000000
    },
    {
      "account": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:08.435)
```javascript
{
  "id": -576460752303423455,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node (2019-03-13 11:05:08.440)
```javascript
{
  "channel_id": "ch_2jyj55b88FUFo7jK3dEHgB4FyUFKnf3Q4nfYJPrxm6W2yU7poV",
  "id": -576460752303423455,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAeSil4X+afBp58+IoPheVw0JB5kV1pKFx5pHd5zJ1qDAxIYzqQsu50uKAoZKTsGbENDOw7TNwnRGG9/7vphjFBLhAiIfRoER6inr0h63mfhZWieYwo77el0q2oMChbeInmY4auL+j1NR9mbkln6U1XPmwgmUBLEwM+sFZxMd927H9B7iX+JU5AaEG5UhvuhHlNH68WRPZRgtrDSkBnRKHL/97ncUVOZz/HfAG+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaBtJeqayYNAxAR8VEb/US6Hb7IetZ7x8ND25z+UAJu3M5PN7OY=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4vKCgEAhiRhOcqAALDvQAGgJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eLygoBAIY/qiUiYADbIKsP"
  },
  "version": 1
}
```
