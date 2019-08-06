
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAfNO8EGVVRoKbq3Lxj2WY6ZR+xj2jcGlcIhNerfki3mXhj+qJSJgAKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GJGE5yoAAAgoAhhAGeddIAMCgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0Rhp1EJQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423362,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBwY6eVlOd3Q76UVdeY3K+AJlxsEU05Lc5VJbIKbYjBxEl63QA9WxYubLhHcAeRnOAvaTecKLUJzq1mXjOsgkMJuIP4gTIBoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y/qiUiYAChAfdjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNhiRhOcqAAAIKAIYQBnnXSADAoDXj090A/DMnCedVe1N9Z8lFvhGFs8xqY89cVUV0esLtEUd2CJ4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423362,
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
      "signed_tx": "tx_+MsLAfhCuEBwY6eVlOd3Q76UVdeY3K+AJlxsEU05Lc5VJbIKbYjBxEl63QA9WxYubLhHcAeRnOAvaTecKLUJzq1mXjOsgkMJuIP4gTIBoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y/qiUiYAChAfdjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNhiRhOcqAAAIKAIYQBnnXSADAoDXj090A/DMnCedVe1N9Z8lFvhGFs8xqY89cVUV0esLtEUd2CJ4=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423361,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhADfIkBcHV2PR+28Osw3Hju1ZM3JJjTcpCo0UXjndAgw1IVLwWwUULK5cqM5wada6VOVTU/KikPIp+z1LcwhElD7hAcGOnlZTnd0O+lFXXmNyvgCZcbBFNOS3OVSWyCm2IwcRJet0APVsWLmy4R3AHkZzgL2k3nCi1Cc6tZl4zrIJDCbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7RHAczNu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423361,
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
      "tx": "tx_+QENCwH4hLhADfIkBcHV2PR+28Osw3Hju1ZM3JJjTcpCo0UXjndAgw1IVLwWwUULK5cqM5wada6VOVTU/KikPIp+z1LcwhElD7hAcGOnlZTnd0O+lFXXmNyvgCZcbBFNOS3OVSWyCm2IwcRJet0APVsWLmy4R3AHkZzgL2k3nCi1Cc6tZl4zrIJDCbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7RHAczNu",
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
      "tx": "tx_+QENCwH4hLhADfIkBcHV2PR+28Osw3Hju1ZM3JJjTcpCo0UXjndAgw1IVLwWwUULK5cqM5wada6VOVTU/KikPIp+z1LcwhElD7hAcGOnlZTnd0O+lFXXmNyvgCZcbBFNOS3OVSWyCm2IwcRJet0APVsWLmy4R3AHkZzgL2k3nCi1Cc6tZl4zrIJDCbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7RHAczNu",
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
      "tx": "tx_+QENCwH4hLhADfIkBcHV2PR+28Osw3Hju1ZM3JJjTcpCo0UXjndAgw1IVLwWwUULK5cqM5wada6VOVTU/KikPIp+z1LcwhElD7hAcGOnlZTnd0O+lFXXmNyvgCZcbBFNOS3OVSWyCm2IwcRJet0APVsWLmy4R3AHkZzgL2k3nCi1Cc6tZl4zrIJDCbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7RHAczNu",
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
      "tx": "tx_+QENCwH4hLhADfIkBcHV2PR+28Osw3Hju1ZM3JJjTcpCo0UXjndAgw1IVLwWwUULK5cqM5wada6VOVTU/KikPIp+z1LcwhElD7hAcGOnlZTnd0O+lFXXmNyvgCZcbBFNOS3OVSWyCm2IwcRJet0APVsWLmy4R3AHkZzgL2k3nCi1Cc6tZl4zrIJDCbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7RHAczNu",
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
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "message": {
        "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
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
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "message": {
        "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
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
  "id": -576460752303423360,
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
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423360,
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
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
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
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
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
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
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
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
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
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
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
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
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
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "state": "tx_+QENCwH4hLhADfIkBcHV2PR+28Osw3Hju1ZM3JJjTcpCo0UXjndAgw1IVLwWwUULK5cqM5wada6VOVTU/KikPIp+z1LcwhElD7hAcGOnlZTnd0O+lFXXmNyvgCZcbBFNOS3OVSWyCm2IwcRJet0APVsWLmy4R3AHkZzgL2k3nCi1Cc6tZl4zrIJDCbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7RHAczNu"
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
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "state": "tx_+QENCwH4hLhADfIkBcHV2PR+28Osw3Hju1ZM3JJjTcpCo0UXjndAgw1IVLwWwUULK5cqM5wada6VOVTU/KikPIp+z1LcwhElD7hAcGOnlZTnd0O+lFXXmNyvgCZcbBFNOS3OVSWyCm2IwcRJet0APVsWLmy4R3AHkZzgL2k3nCi1Cc6tZl4zrIJDCbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7RHAczNu"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "state": "tx_+QENCwH4hLhADfIkBcHV2PR+28Osw3Hju1ZM3JJjTcpCo0UXjndAgw1IVLwWwUULK5cqM5wada6VOVTU/KikPIp+z1LcwhElD7hAcGOnlZTnd0O+lFXXmNyvgCZcbBFNOS3OVSWyCm2IwcRJet0APVsWLmy4R3AHkZzgL2k3nCi1Cc6tZl4zrIJDCbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7RHAczNu"
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
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
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
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "state": "tx_+QENCwH4hLhADfIkBcHV2PR+28Osw3Hju1ZM3JJjTcpCo0UXjndAgw1IVLwWwUULK5cqM5wada6VOVTU/KikPIp+z1LcwhElD7hAcGOnlZTnd0O+lFXXmNyvgCZcbBFNOS3OVSWyCm2IwcRJet0APVsWLmy4R3AHkZzgL2k3nCi1Cc6tZl4zrIJDCbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7RHAczNu"
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
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm&offchain_tx=tx_%2BQENCwH4hLhADfIkBcHV2PR%2B28Osw3Hju1ZM3JJjTcpCo0UXjndAgw1IVLwWwUULK5cqM5wada6VOVTU%2FKikPIp%2Bz1LcwhElD7hAcGOnlZTnd0O%2BlFXXmNyvgCZcbBFNOS3OVSWyCm2IwcRJet0APVsWLmy4R3AHkZzgL2k3nCi1Cc6tZl4zrIJDCbiD%2BIEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t%2BSLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC%2Fosmc70%2FiBKU%2Bp5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7RHAczNu&port=13180&protocol=json-rpc&role=responder
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm&host=localhost&offchain_tx=tx_%2BQENCwH4hLhADfIkBcHV2PR%2B28Osw3Hju1ZM3JJjTcpCo0UXjndAgw1IVLwWwUULK5cqM5wada6VOVTU%2FKikPIp%2Bz1LcwhElD7hAcGOnlZTnd0O%2BlFXXmNyvgCZcbBFNOS3OVSWyCm2IwcRJet0APVsWLmy4R3AHkZzgL2k3nCi1Cc6tZl4zrIJDCbiD%2BIEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t%2BSLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC%2Fosmc70%2FiBKU%2Bp5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7RHAczNu&port=13180&protocol=json-rpc&role=initiator
```

#### responder <--- node
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

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "state": "tx_+QENCwH4hLhADfIkBcHV2PR+28Osw3Hju1ZM3JJjTcpCo0UXjndAgw1IVLwWwUULK5cqM5wada6VOVTU/KikPIp+z1LcwhElD7hAcGOnlZTnd0O+lFXXmNyvgCZcbBFNOS3OVSWyCm2IwcRJet0APVsWLmy4R3AHkZzgL2k3nCi1Cc6tZl4zrIJDCbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7RHAczNu"
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
      "event": "channel_reestablished"
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
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Channel is `open` and ready to use

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "state": "tx_+QENCwH4hLhADfIkBcHV2PR+28Osw3Hju1ZM3JJjTcpCo0UXjndAgw1IVLwWwUULK5cqM5wada6VOVTU/KikPIp+z1LcwhElD7hAcGOnlZTnd0O+lFXXmNyvgCZcbBFNOS3OVSWyCm2IwcRJet0APVsWLmy4R3AHkZzgL2k3nCi1Cc6tZl4zrIJDCbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7RHAczNu"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423359,
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
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423359,
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

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
    "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
        "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "from": "ABCDEF",
    "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
        "to": "ABCDEF"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
    "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlFvv2t1eZYDuFpWq9+0AqiDS3ojAu/Mpl3g/whsdGhIAqBBCOFlzgxrCKtRrQPx23phpiUnifrgJMUhpNa+5DFOwvOTeyw=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
          "op": "OffChainTransfer",
          "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
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
  "id": -576460752303423358,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAjG9lASpfiStL6nfKXrEQa9tIqwg/gxjBL2AIOUwZfXXajlGNeA9mibHwj22Rod6wUFi/9PsXsO4qBQqDKF/YFuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsKtilmZ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423358,
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
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAjG9lASpfiStL6nfKXrEQa9tIqwg/gxjBL2AIOUwZfXXajlGNeA9mibHwj22Rod6wUFi/9PsXsO4qBQqDKF/YFuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsKtilmZ",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
          "op": "OffChainTransfer",
          "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423357,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAjG9lASpfiStL6nfKXrEQa9tIqwg/gxjBL2AIOUwZfXXajlGNeA9mibHwj22Rod6wUFi/9PsXsO4qBQqDKF/YFuEBUOA6i2A1Q4LV4BYRPziGPcDG3OflYae1bgmVjWn1KjGZVpnbMiReT3XA8gtfR3yHzk9S0TFhUzF1+b5RgXuULuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsIpWgnd"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423357,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "state": "tx_+NILAfiEuEAjG9lASpfiStL6nfKXrEQa9tIqwg/gxjBL2AIOUwZfXXajlGNeA9mibHwj22Rod6wUFi/9PsXsO4qBQqDKF/YFuEBUOA6i2A1Q4LV4BYRPziGPcDG3OflYae1bgmVjWn1KjGZVpnbMiReT3XA8gtfR3yHzk9S0TFhUzF1+b5RgXuULuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsIpWgnd"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "state": "tx_+NILAfiEuEAjG9lASpfiStL6nfKXrEQa9tIqwg/gxjBL2AIOUwZfXXajlGNeA9mibHwj22Rod6wUFi/9PsXsO4qBQqDKF/YFuEBUOA6i2A1Q4LV4BYRPziGPcDG3OflYae1bgmVjWn1KjGZVpnbMiReT3XA8gtfR3yHzk9S0TFhUzF1+b5RgXuULuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsIpWgnd"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423356,
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
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423356,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
      "balance": 69999999999998
    },
    {
      "account": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423355,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423355,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAjG9lASpfiStL6nfKXrEQa9tIqwg/gxjBL2AIOUwZfXXajlGNeA9mibHwj22Rod6wUFi/9PsXsO4qBQqDKF/YFuEBUOA6i2A1Q4LV4BYRPziGPcDG3OflYae1bgmVjWn1KjGZVpnbMiReT3XA8gtfR3yHzk9S0TFhUzF1+b5RgXuULuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsIpWgnd",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAArDvQAGg807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiX/4rKrmw"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423354,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
      "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423354,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
      "balance": 40000000000002
    },
    {
      "account": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
      "balance": 69999999999998
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
    "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
        "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
        "to": "ABCDEF"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
    "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlFvv2t1eZYDuFpWq9+0AqiDS3ojAu/Mpl3g/whsdGhIA6A149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7fl348Y=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
          "op": "OffChainTransfer",
          "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423353,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECirZn12m5h/K90yr30IiuVtM6/2YWJfwSuKDhEgSWEvUIoVJ8UnJLCDGIvtc8wFp6Jx4/8JElyTohT1AnR+4gFuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu1QNj1a"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423353,
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
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "signed_tx": "tx_+JALAfhCuECirZn12m5h/K90yr30IiuVtM6/2YWJfwSuKDhEgSWEvUIoVJ8UnJLCDGIvtc8wFp6Jx4/8JElyTohT1AnR+4gFuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu1QNj1a",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
          "op": "OffChainTransfer",
          "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
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
  "id": -576460752303423352,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEB+35llmo8qhDn3zvAlyETEgNEGL6wm0wQTvCBoYPTeiw5xTXUFojvzaLlD0U5kjNwOzR4m4LtZ++B/LeO32mQIuECirZn12m5h/K90yr30IiuVtM6/2YWJfwSuKDhEgSWEvUIoVJ8UnJLCDGIvtc8wFp6Jx4/8JElyTohT1AnR+4gFuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu08GEn/"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423352,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "state": "tx_+NILAfiEuEB+35llmo8qhDn3zvAlyETEgNEGL6wm0wQTvCBoYPTeiw5xTXUFojvzaLlD0U5kjNwOzR4m4LtZ++B/LeO32mQIuECirZn12m5h/K90yr30IiuVtM6/2YWJfwSuKDhEgSWEvUIoVJ8UnJLCDGIvtc8wFp6Jx4/8JElyTohT1AnR+4gFuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu08GEn/"
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
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "state": "tx_+NILAfiEuEB+35llmo8qhDn3zvAlyETEgNEGL6wm0wQTvCBoYPTeiw5xTXUFojvzaLlD0U5kjNwOzR4m4LtZ++B/LeO32mQIuECirZn12m5h/K90yr30IiuVtM6/2YWJfwSuKDhEgSWEvUIoVJ8UnJLCDGIvtc8wFp6Jx4/8JElyTohT1AnR+4gFuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu08GEn/"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423351,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
      "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423351,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
      "balance": 40000000000001
    },
    {
      "account": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423350,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423350,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEB+35llmo8qhDn3zvAlyETEgNEGL6wm0wQTvCBoYPTeiw5xTXUFojvzaLlD0U5kjNwOzR4m4LtZ++B/LeO32mQIuECirZn12m5h/K90yr30IiuVtM6/2YWJfwSuKDhEgSWEvUIoVJ8UnJLCDGIvtc8wFp6Jx4/8JElyTohT1AnR+4gFuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu08GEn/",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAAbDvQAGg807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiX/+PWk/e"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423349,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
      "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423349,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
      "balance": 40000000000001
    },
    {
      "account": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
    "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
        "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
        "to": "ABCDEF"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
    "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlFvv2t1eZYDuFpWq9+0AqiDS3ojAu/Mpl3g/whsdGhIBKBD48upGMSQmUHkvAbXk8OLPb+iXSg8kxqzNfUkPoVMWZaQdnc=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
          "op": "OffChainTransfer",
          "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423348,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDFhBrucgJQJaKOEREvsNxGdapj1zPrHIWT/LbGonmA80uwcLPzLrpugYWInKZ67U6mtRXMLknc2vWGovsPL+EPuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSASgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFmgkIOq"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423348,
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
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDFhBrucgJQJaKOEREvsNxGdapj1zPrHIWT/LbGonmA80uwcLPzLrpugYWInKZ67U6mtRXMLknc2vWGovsPL+EPuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSASgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFmgkIOq",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
          "op": "OffChainTransfer",
          "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
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
  "id": -576460752303423347,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECW7bEy7kr1N+IY6Qmrmp+7vO0O89sc0xu+Edb2V052ojsoAV4mIVy2mTBD7nThmzz4ZgQzMdTYowFImdUddnwMuEDFhBrucgJQJaKOEREvsNxGdapj1zPrHIWT/LbGonmA80uwcLPzLrpugYWInKZ67U6mtRXMLknc2vWGovsPL+EPuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSASgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFnlsB4Q"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423347,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "state": "tx_+NILAfiEuECW7bEy7kr1N+IY6Qmrmp+7vO0O89sc0xu+Edb2V052ojsoAV4mIVy2mTBD7nThmzz4ZgQzMdTYowFImdUddnwMuEDFhBrucgJQJaKOEREvsNxGdapj1zPrHIWT/LbGonmA80uwcLPzLrpugYWInKZ67U6mtRXMLknc2vWGovsPL+EPuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSASgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFnlsB4Q"
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
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "state": "tx_+NILAfiEuECW7bEy7kr1N+IY6Qmrmp+7vO0O89sc0xu+Edb2V052ojsoAV4mIVy2mTBD7nThmzz4ZgQzMdTYowFImdUddnwMuEDFhBrucgJQJaKOEREvsNxGdapj1zPrHIWT/LbGonmA80uwcLPzLrpugYWInKZ67U6mtRXMLknc2vWGovsPL+EPuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSASgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFnlsB4Q"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423346,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
      "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423346,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
      "balance": 40000000000000
    },
    {
      "account": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423345,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423345,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECW7bEy7kr1N+IY6Qmrmp+7vO0O89sc0xu+Edb2V052ojsoAV4mIVy2mTBD7nThmzz4ZgQzMdTYowFImdUddnwMuEDFhBrucgJQJaKOEREvsNxGdapj1zPrHIWT/LbGonmA80uwcLPzLrpugYWInKZ67U6mtRXMLknc2vWGovsPL+EPuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSASgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFnlsB4Q",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAALDvQAGg807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiYAAzY13U"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423344,
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
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423344,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
      "balance": 70000000000000
    },
    {
      "account": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
      "balance": 40000000000000
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
    "amount": "1",
    "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
    "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
        "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "from": "ABCDEF",
    "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
        "to": "ABCDEF"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
    "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlFvv2t1eZYDuFpWq9+0AqiDS3ojAu/Mpl3g/whsdGhIBaA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QSDQ3c=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
          "op": "OffChainTransfer",
          "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
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
  "id": -576460752303423343,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBLKuBCAP8OIGauT9pZKc0e9rHHkeYBvHTyqjf7CFiP7SNzgNNch3kMZTqXPUO5Z7BZq8oyp3mCvkff9N3wOR0JuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0Qvuu4"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423343,
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
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBLKuBCAP8OIGauT9pZKc0e9rHHkeYBvHTyqjf7CFiP7SNzgNNch3kMZTqXPUO5Z7BZq8oyp3mCvkff9N3wOR0JuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0Qvuu4",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
          "op": "OffChainTransfer",
          "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423342,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBLKuBCAP8OIGauT9pZKc0e9rHHkeYBvHTyqjf7CFiP7SNzgNNch3kMZTqXPUO5Z7BZq8oyp3mCvkff9N3wOR0JuEBlu4ZDhkV7zFRczDJPZuny3dfcRhU4rDrHhanAw1qERUThdCoheT9SusZIEtKV8eGk3bSZoI6DNPdyPLl7gJcOuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu38JLcY"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423342,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "state": "tx_+NILAfiEuEBLKuBCAP8OIGauT9pZKc0e9rHHkeYBvHTyqjf7CFiP7SNzgNNch3kMZTqXPUO5Z7BZq8oyp3mCvkff9N3wOR0JuEBlu4ZDhkV7zFRczDJPZuny3dfcRhU4rDrHhanAw1qERUThdCoheT9SusZIEtKV8eGk3bSZoI6DNPdyPLl7gJcOuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu38JLcY"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "state": "tx_+NILAfiEuEBLKuBCAP8OIGauT9pZKc0e9rHHkeYBvHTyqjf7CFiP7SNzgNNch3kMZTqXPUO5Z7BZq8oyp3mCvkff9N3wOR0JuEBlu4ZDhkV7zFRczDJPZuny3dfcRhU4rDrHhanAw1qERUThdCoheT9SusZIEtKV8eGk3bSZoI6DNPdyPLl7gJcOuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu38JLcY"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423341,
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
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423341,
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

#### initiator ---> node
```javascript
{
  "id": -576460752303423340,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423340,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBLKuBCAP8OIGauT9pZKc0e9rHHkeYBvHTyqjf7CFiP7SNzgNNch3kMZTqXPUO5Z7BZq8oyp3mCvkff9N3wOR0JuEBlu4ZDhkV7zFRczDJPZuny3dfcRhU4rDrHhanAw1qERUThdCoheT9SusZIEtKV8eGk3bSZoI6DNPdyPLl7gJcOuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu38JLcY",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAAbDvQAGg807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiX/+PWk/e"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423339,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
      "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423339,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
      "balance": 40000000000001
    },
    {
      "account": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
    "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
        "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
        "to": "ABCDEF"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
    "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlFvv2t1eZYDuFpWq9+0AqiDS3ojAu/Mpl3g/whsdGhIBqBD48upGMSQmUHkvAbXk8OLPb+iXSg8kxqzNfUkPoVMWbhkenw=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
          "op": "OffChainTransfer",
          "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423338,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECir8gZaOdMoEWW7mihYm2dGW2T52TzY/hWyLXKuAvQvL5NNUxm/tPCvlqK7/4OuWBe/tDGtlQDvZZ8Bq6ZNBsNuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFmuIAil"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423338,
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
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "signed_tx": "tx_+JALAfhCuECir8gZaOdMoEWW7mihYm2dGW2T52TzY/hWyLXKuAvQvL5NNUxm/tPCvlqK7/4OuWBe/tDGtlQDvZZ8Bq6ZNBsNuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFmuIAil",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
          "op": "OffChainTransfer",
          "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
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
  "id": -576460752303423337,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBAwR7Sg7/af5DsY592wRmfMel8DymoKq6/xXnpsIazMJ0qF/9BtnFFsFZZKlo0rd1L7jTtrCh3QrwExzYf9GgDuECir8gZaOdMoEWW7mihYm2dGW2T52TzY/hWyLXKuAvQvL5NNUxm/tPCvlqK7/4OuWBe/tDGtlQDvZZ8Bq6ZNBsNuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFmEuBtv"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423337,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "state": "tx_+NILAfiEuEBAwR7Sg7/af5DsY592wRmfMel8DymoKq6/xXnpsIazMJ0qF/9BtnFFsFZZKlo0rd1L7jTtrCh3QrwExzYf9GgDuECir8gZaOdMoEWW7mihYm2dGW2T52TzY/hWyLXKuAvQvL5NNUxm/tPCvlqK7/4OuWBe/tDGtlQDvZZ8Bq6ZNBsNuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFmEuBtv"
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
    "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
    "data": {
      "state": "tx_+NILAfiEuEBAwR7Sg7/af5DsY592wRmfMel8DymoKq6/xXnpsIazMJ0qF/9BtnFFsFZZKlo0rd1L7jTtrCh3QrwExzYf9GgDuECir8gZaOdMoEWW7mihYm2dGW2T52TzY/hWyLXKuAvQvL5NNUxm/tPCvlqK7/4OuWBe/tDGtlQDvZZ8Bq6ZNBsNuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFmEuBtv"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423336,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
      "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423336,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
      "balance": 40000000000000
    },
    {
      "account": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423335,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_csBpGh7p7b5S8fiGvmZbMXAYeLTm9TN6pxY5c1ZHjLZszTXwm",
  "id": -576460752303423335,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBAwR7Sg7/af5DsY592wRmfMel8DymoKq6/xXnpsIazMJ0qF/9BtnFFsFZZKlo0rd1L7jTtrCh3QrwExzYf9GgDuECir8gZaOdMoEWW7mihYm2dGW2T52TzY/hWyLXKuAvQvL5NNUxm/tPCvlqK7/4OuWBe/tDGtlQDvZZ8Bq6ZNBsNuEj4RjkCoQZRb79rdXmWA7haVqvftAKog0t6IwLvzKZd4P8IbHRoSAagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFmEuBtv",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAALDvQAGg807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiYAAzY13U"
  },
  "version": 1
}
```
