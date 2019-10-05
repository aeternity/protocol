
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT&role=initiator
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT&role=responder
```

#### responder <--- node
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

#### responder info
> Received an WebSocket opening request

#### initiator <--- node
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

#### initiator info
> Received an WebSocket connection accepted

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAfNO8EGVVRoKbq3Lxj2WY6ZR+xj2jcGlcIhNerfki3mXhj+qJSJgAKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GJGE5yoAAAgoAhhAGeddIAMCgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0SD81Ifg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423334,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEC8Y6ctZXJudHhQRqAB3SKvCGTd1krwFC+SRHpFuYVQ0rPrUwkh6tHhjgRD+NqmpWv365NFrsnq6aH/0wsGRqcMuIP4gTIBoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y/qiUiYAChAfdjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNhiRhOcqAAAIKAIYQBnnXSADAoDXj090A/DMnCedVe1N9Z8lFvhGFs8xqY89cVUV0esLtEnIemEI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423334,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
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

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+MsLAfhCuEC8Y6ctZXJudHhQRqAB3SKvCGTd1krwFC+SRHpFuYVQ0rPrUwkh6tHhjgRD+NqmpWv365NFrsnq6aH/0wsGRqcMuIP4gTIBoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y/qiUiYAChAfdjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNhiRhOcqAAAIKAIYQBnnXSADAoDXj090A/DMnCedVe1N9Z8lFvhGFs8xqY89cVUV0esLtEnIemEI=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423333,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAforaKwuCU/04jbUf4iZjUKz/TI1SoPT3+U7IkhtIYCX+JTlLVBOZU/ZB9wgnTJ/pVYnTb1smGhjsbuegFU0+A7hAvGOnLWVybnR4UEagAd0irwhk3dZK8BQvkkR6RbmFUNKz61MJIerR4Y4EQ/japqVr9+uTRa7J6umh/9MLBkanDLiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7RKhXCZF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423333,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAforaKwuCU/04jbUf4iZjUKz/TI1SoPT3+U7IkhtIYCX+JTlLVBOZU/ZB9wgnTJ/pVYnTb1smGhjsbuegFU0+A7hAvGOnLWVybnR4UEagAd0irwhk3dZK8BQvkkR6RbmFUNKz61MJIerR4Y4EQ/japqVr9+uTRa7J6umh/9MLBkanDLiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7RKhXCZF",
      "type": "channel_create_tx"
    }
  },
  "version": 1
}
```

#### initiator <--- node
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

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAforaKwuCU/04jbUf4iZjUKz/TI1SoPT3+U7IkhtIYCX+JTlLVBOZU/ZB9wgnTJ/pVYnTb1smGhjsbuegFU0+A7hAvGOnLWVybnR4UEagAd0irwhk3dZK8BQvkkR6RbmFUNKz61MJIerR4Y4EQ/japqVr9+uTRa7J6umh/9MLBkanDLiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7RKhXCZF",
      "type": "channel_create_tx"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAforaKwuCU/04jbUf4iZjUKz/TI1SoPT3+U7IkhtIYCX+JTlLVBOZU/ZB9wgnTJ/pVYnTb1smGhjsbuegFU0+A7hAvGOnLWVybnR4UEagAd0irwhk3dZK8BQvkkR6RbmFUNKz61MJIerR4Y4EQ/japqVr9+uTRa7J6umh/9MLBkanDLiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7RKhXCZF",
      "type": "channel_create_tx"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAforaKwuCU/04jbUf4iZjUKz/TI1SoPT3+U7IkhtIYCX+JTlLVBOZU/ZB9wgnTJ/pVYnTb1smGhjsbuegFU0+A7hAvGOnLWVybnR4UEagAd0irwhk3dZK8BQvkkR6RbmFUNKz61MJIerR4Y4EQ/japqVr9+uTRa7J6umh/9MLBkanDLiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7RKhXCZF",
      "type": "channel_create_tx"
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
    "info": "Hello",
    "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "message": {
        "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
        "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
        "info": "Hello",
        "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
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
    "info": "Hello back",
    "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "message": {
        "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
        "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
        "info": "Hello back",
        "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423332,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
      "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
  "id": -576460752303423332,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
      "balance": 69999999999999
    },
    {
      "account": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Channel is `open` and ready to use

#### responder info
> Channel is `open` and ready to use

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "state": "tx_+QENCwH4hLhAforaKwuCU/04jbUf4iZjUKz/TI1SoPT3+U7IkhtIYCX+JTlLVBOZU/ZB9wgnTJ/pVYnTb1smGhjsbuegFU0+A7hAvGOnLWVybnR4UEagAd0irwhk3dZK8BQvkkR6RbmFUNKz61MJIerR4Y4EQ/japqVr9+uTRa7J6umh/9MLBkanDLiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7RKhXCZF"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "state": "tx_+QENCwH4hLhAforaKwuCU/04jbUf4iZjUKz/TI1SoPT3+U7IkhtIYCX+JTlLVBOZU/ZB9wgnTJ/pVYnTb1smGhjsbuegFU0+A7hAvGOnLWVybnR4UEagAd0irwhk3dZK8BQvkkR6RbmFUNKz61MJIerR4Y4EQ/japqVr9+uTRa7J6umh/9MLBkanDLiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7RKhXCZF"
    }
  },
  "version": 1
}
```
