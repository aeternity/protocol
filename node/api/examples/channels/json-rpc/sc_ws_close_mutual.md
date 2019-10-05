
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAfNO8EGVVRoKbq3Lxj2WY6ZR+xj2jcGlcIhNerfki3mXhj+qJSJgAKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GJGE5yoAAAgoAhhAGeddIAMCgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0FJpLjag==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423402,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECEo6AIjtxcgE7rqK/pidb7p1OQKSBOZ721Lcb3zql8Rb6dCr3RnijZ5+eAbWkEVhIN3UV6DbC4TdH8SDVZag0HuIP4gTIBoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y/qiUiYAChAfdjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNhiRhOcqAAAIKAIYQBnnXSADAoDXj090A/DMnCedVe1N9Z8lFvhGFs8xqY89cVUV0esLtBYpIGfc="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423402,
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
      "signed_tx": "tx_+MsLAfhCuECEo6AIjtxcgE7rqK/pidb7p1OQKSBOZ721Lcb3zql8Rb6dCr3RnijZ5+eAbWkEVhIN3UV6DbC4TdH8SDVZag0HuIP4gTIBoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y/qiUiYAChAfdjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNhiRhOcqAAAIKAIYQBnnXSADAoDXj090A/DMnCedVe1N9Z8lFvhGFs8xqY89cVUV0esLtBYpIGfc=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423401,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAUNcCNMlEurA1a/zpyb+NkaMpNAvWA75ZMEbUhtQK7zZlvbgEDWGWQpK+XVAC44T3rQRNkiWw/JkRhqc3TcAuAbhAhKOgCI7cXIBO66iv6YnW+6dTkCkgTme9tS3G986pfEW+nQq90Z4o2efngG1pBFYSDd1Feg2wuE3R/Eg1WWoNB7iD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QWHpX31"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423401,
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
      "tx": "tx_+QENCwH4hLhAUNcCNMlEurA1a/zpyb+NkaMpNAvWA75ZMEbUhtQK7zZlvbgEDWGWQpK+XVAC44T3rQRNkiWw/JkRhqc3TcAuAbhAhKOgCI7cXIBO66iv6YnW+6dTkCkgTme9tS3G986pfEW+nQq90Z4o2efngG1pBFYSDd1Feg2wuE3R/Eg1WWoNB7iD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QWHpX31",
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
      "tx": "tx_+QENCwH4hLhAUNcCNMlEurA1a/zpyb+NkaMpNAvWA75ZMEbUhtQK7zZlvbgEDWGWQpK+XVAC44T3rQRNkiWw/JkRhqc3TcAuAbhAhKOgCI7cXIBO66iv6YnW+6dTkCkgTme9tS3G986pfEW+nQq90Z4o2efngG1pBFYSDd1Feg2wuE3R/Eg1WWoNB7iD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QWHpX31",
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
      "tx": "tx_+QENCwH4hLhAUNcCNMlEurA1a/zpyb+NkaMpNAvWA75ZMEbUhtQK7zZlvbgEDWGWQpK+XVAC44T3rQRNkiWw/JkRhqc3TcAuAbhAhKOgCI7cXIBO66iv6YnW+6dTkCkgTme9tS3G986pfEW+nQq90Z4o2efngG1pBFYSDd1Feg2wuE3R/Eg1WWoNB7iD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QWHpX31",
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
      "tx": "tx_+QENCwH4hLhAUNcCNMlEurA1a/zpyb+NkaMpNAvWA75ZMEbUhtQK7zZlvbgEDWGWQpK+XVAC44T3rQRNkiWw/JkRhqc3TcAuAbhAhKOgCI7cXIBO66iv6YnW+6dTkCkgTme9tS3G986pfEW+nQq90Z4o2efngG1pBFYSDd1Feg2wuE3R/Eg1WWoNB7iD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QWHpX31",
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
    "channel_id": "ch_2puPsTnWkZJMHUGXQPBPbUEbst2P2xJN1NaWJKBQZd8VTaPC2m",
    "data": {
      "message": {
        "channel_id": "ch_2puPsTnWkZJMHUGXQPBPbUEbst2P2xJN1NaWJKBQZd8VTaPC2m",
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
    "channel_id": "ch_2puPsTnWkZJMHUGXQPBPbUEbst2P2xJN1NaWJKBQZd8VTaPC2m",
    "data": {
      "message": {
        "channel_id": "ch_2puPsTnWkZJMHUGXQPBPbUEbst2P2xJN1NaWJKBQZd8VTaPC2m",
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
  "id": -576460752303423400,
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
  "channel_id": "ch_2puPsTnWkZJMHUGXQPBPbUEbst2P2xJN1NaWJKBQZd8VTaPC2m",
  "id": -576460752303423400,
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

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2puPsTnWkZJMHUGXQPBPbUEbst2P2xJN1NaWJKBQZd8VTaPC2m",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2puPsTnWkZJMHUGXQPBPbUEbst2P2xJN1NaWJKBQZd8VTaPC2m",
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
    "channel_id": "ch_2puPsTnWkZJMHUGXQPBPbUEbst2P2xJN1NaWJKBQZd8VTaPC2m",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2puPsTnWkZJMHUGXQPBPbUEbst2P2xJN1NaWJKBQZd8VTaPC2m",
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
    "channel_id": "ch_2puPsTnWkZJMHUGXQPBPbUEbst2P2xJN1NaWJKBQZd8VTaPC2m",
    "data": {
      "state": "tx_+QENCwH4hLhAUNcCNMlEurA1a/zpyb+NkaMpNAvWA75ZMEbUhtQK7zZlvbgEDWGWQpK+XVAC44T3rQRNkiWw/JkRhqc3TcAuAbhAhKOgCI7cXIBO66iv6YnW+6dTkCkgTme9tS3G986pfEW+nQq90Z4o2efngG1pBFYSDd1Feg2wuE3R/Eg1WWoNB7iD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QWHpX31"
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
    "channel_id": "ch_2puPsTnWkZJMHUGXQPBPbUEbst2P2xJN1NaWJKBQZd8VTaPC2m",
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
    "channel_id": "ch_2puPsTnWkZJMHUGXQPBPbUEbst2P2xJN1NaWJKBQZd8VTaPC2m",
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
    "channel_id": "ch_2puPsTnWkZJMHUGXQPBPbUEbst2P2xJN1NaWJKBQZd8VTaPC2m",
    "data": {
      "state": "tx_+QENCwH4hLhAUNcCNMlEurA1a/zpyb+NkaMpNAvWA75ZMEbUhtQK7zZlvbgEDWGWQpK+XVAC44T3rQRNkiWw/JkRhqc3TcAuAbhAhKOgCI7cXIBO66iv6YnW+6dTkCkgTme9tS3G986pfEW+nQq90Z4o2efngG1pBFYSDd1Feg2wuE3R/Eg1WWoNB7iD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QWHpX31"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_2puPsTnWkZJMHUGXQPBPbUEbst2P2xJN1NaWJKBQZd8VTaPC2m",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBvB3bVXtWZLmMB6TzpESfPJH1QpVApSdo7RX3NX7qtnCoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y2kdavv/+GG0jrV+ABAIYSMJzlQAAG285U5w==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423399,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEB/PjqnETF6d63FrfWBmBJT+pt1im7Tf8XQcR5Y3STdFhanhQIyKwI5on1AxuG2VSpB2/4oa9iwpMEVEfeJODgKuF/4XTUBoQbwd21V7VmS5jAek86REnzyR9UKVQKUnaO0V9zV+6rZwqEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGNpHWr7//hhtI61fgAQCGEjCc5UAABlWCaWs="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2puPsTnWkZJMHUGXQPBPbUEbst2P2xJN1NaWJKBQZd8VTaPC2m",
  "id": -576460752303423399,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_2puPsTnWkZJMHUGXQPBPbUEbst2P2xJN1NaWJKBQZd8VTaPC2m",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEB/PjqnETF6d63FrfWBmBJT+pt1im7Tf8XQcR5Y3STdFhanhQIyKwI5on1AxuG2VSpB2/4oa9iwpMEVEfeJODgKuF/4XTUBoQbwd21V7VmS5jAek86REnzyR9UKVQKUnaO0V9zV+6rZwqEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGNpHWr7//hhtI61fgAQCGEjCc5UAABlWCaWs=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423398,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEB/PjqnETF6d63FrfWBmBJT+pt1im7Tf8XQcR5Y3STdFhanhQIyKwI5on1AxuG2VSpB2/4oa9iwpMEVEfeJODgKuEDAaJ71bCBjPKLxbPbF38cWEdKB9n5lvaoTmL8MLnxQqoZnBoMIQbKMJqOycn/+g7kQ/hbXo9PCRzO6aC4dSqUPuF/4XTUBoQbwd21V7VmS5jAek86REnzyR9UKVQKUnaO0V9zV+6rZwqEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGNpHWr7//hhtI61fgAQCGEjCc5UAABrZNph8="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2puPsTnWkZJMHUGXQPBPbUEbst2P2xJN1NaWJKBQZd8VTaPC2m",
  "id": -576460752303423398,
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
    "channel_id": "ch_2puPsTnWkZJMHUGXQPBPbUEbst2P2xJN1NaWJKBQZd8VTaPC2m",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEB/PjqnETF6d63FrfWBmBJT+pt1im7Tf8XQcR5Y3STdFhanhQIyKwI5on1AxuG2VSpB2/4oa9iwpMEVEfeJODgKuEDAaJ71bCBjPKLxbPbF38cWEdKB9n5lvaoTmL8MLnxQqoZnBoMIQbKMJqOycn/+g7kQ/hbXo9PCRzO6aC4dSqUPuF/4XTUBoQbwd21V7VmS5jAek86REnzyR9UKVQKUnaO0V9zV+6rZwqEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGNpHWr7//hhtI61fgAQCGEjCc5UAABrZNph8=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_2puPsTnWkZJMHUGXQPBPbUEbst2P2xJN1NaWJKBQZd8VTaPC2m",
    "data": {
      "event": "close_mutual"
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
    "channel_id": "ch_2puPsTnWkZJMHUGXQPBPbUEbst2P2xJN1NaWJKBQZd8VTaPC2m",
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
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2puPsTnWkZJMHUGXQPBPbUEbst2P2xJN1NaWJKBQZd8VTaPC2m",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEB/PjqnETF6d63FrfWBmBJT+pt1im7Tf8XQcR5Y3STdFhanhQIyKwI5on1AxuG2VSpB2/4oa9iwpMEVEfeJODgKuEDAaJ71bCBjPKLxbPbF38cWEdKB9n5lvaoTmL8MLnxQqoZnBoMIQbKMJqOycn/+g7kQ/hbXo9PCRzO6aC4dSqUPuF/4XTUBoQbwd21V7VmS5jAek86REnzyR9UKVQKUnaO0V9zV+6rZwqEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGNpHWr7//hhtI61fgAQCGEjCc5UAABrZNph8=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_2puPsTnWkZJMHUGXQPBPbUEbst2P2xJN1NaWJKBQZd8VTaPC2m",
    "data": {
      "event": "close_mutual"
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
    "channel_id": "ch_2puPsTnWkZJMHUGXQPBPbUEbst2P2xJN1NaWJKBQZd8VTaPC2m",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAfNO8EGVVRoKbq3Lxj2WY6ZR+xj2jcGlcIhNerfki3mXhj+qJSJgAKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GJGE5yoAAAgoAhhAGeddIAMCgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0HH49L6Q==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423397,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECdcgxpc/THSZkNUVtHvqcpTpwVf1N+OXj0d90IMMVJrgUYfsLjJXQ4qu3LcCWBvPtRa5dKZFOBljYC8qZ7KwkMuIP4gTIBoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y/qiUiYAChAfdjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNhiRhOcqAAAIKAIYQBnnXSADAoDXj090A/DMnCedVe1N9Z8lFvhGFs8xqY89cVUV0esLtB5E3kjY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423397,
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
      "signed_tx": "tx_+MsLAfhCuECdcgxpc/THSZkNUVtHvqcpTpwVf1N+OXj0d90IMMVJrgUYfsLjJXQ4qu3LcCWBvPtRa5dKZFOBljYC8qZ7KwkMuIP4gTIBoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y/qiUiYAChAfdjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNhiRhOcqAAAIKAIYQBnnXSADAoDXj090A/DMnCedVe1N9Z8lFvhGFs8xqY89cVUV0esLtB5E3kjY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423396,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAGJFJzcxL/BvO8N93RmVtlPCuzlMzdk09AwjunrXq2FV8eWgyzB2CKAs7TuQovUIFntkYqFt715lg6AR5Rgy0A7hAnXIMaXP0x0mZDVFbR76nKU6cFX9Tfjl49HfdCDDFSa4FGH7C4yV0OKrty3Algbz7UWuXSmRTgZY2AvKmeysJDLiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QfFpczM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423396,
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
      "tx": "tx_+QENCwH4hLhAGJFJzcxL/BvO8N93RmVtlPCuzlMzdk09AwjunrXq2FV8eWgyzB2CKAs7TuQovUIFntkYqFt715lg6AR5Rgy0A7hAnXIMaXP0x0mZDVFbR76nKU6cFX9Tfjl49HfdCDDFSa4FGH7C4yV0OKrty3Algbz7UWuXSmRTgZY2AvKmeysJDLiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QfFpczM",
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
      "tx": "tx_+QENCwH4hLhAGJFJzcxL/BvO8N93RmVtlPCuzlMzdk09AwjunrXq2FV8eWgyzB2CKAs7TuQovUIFntkYqFt715lg6AR5Rgy0A7hAnXIMaXP0x0mZDVFbR76nKU6cFX9Tfjl49HfdCDDFSa4FGH7C4yV0OKrty3Algbz7UWuXSmRTgZY2AvKmeysJDLiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QfFpczM",
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
      "tx": "tx_+QENCwH4hLhAGJFJzcxL/BvO8N93RmVtlPCuzlMzdk09AwjunrXq2FV8eWgyzB2CKAs7TuQovUIFntkYqFt715lg6AR5Rgy0A7hAnXIMaXP0x0mZDVFbR76nKU6cFX9Tfjl49HfdCDDFSa4FGH7C4yV0OKrty3Algbz7UWuXSmRTgZY2AvKmeysJDLiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QfFpczM",
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
      "tx": "tx_+QENCwH4hLhAGJFJzcxL/BvO8N93RmVtlPCuzlMzdk09AwjunrXq2FV8eWgyzB2CKAs7TuQovUIFntkYqFt715lg6AR5Rgy0A7hAnXIMaXP0x0mZDVFbR76nKU6cFX9Tfjl49HfdCDDFSa4FGH7C4yV0OKrty3Algbz7UWuXSmRTgZY2AvKmeysJDLiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QfFpczM",
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
    "channel_id": "ch_nquMjp3rkJUcoqMzh51eYoN7gvdoz62pRVM8XNTRNET4pQrNu",
    "data": {
      "message": {
        "channel_id": "ch_nquMjp3rkJUcoqMzh51eYoN7gvdoz62pRVM8XNTRNET4pQrNu",
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
    "channel_id": "ch_nquMjp3rkJUcoqMzh51eYoN7gvdoz62pRVM8XNTRNET4pQrNu",
    "data": {
      "message": {
        "channel_id": "ch_nquMjp3rkJUcoqMzh51eYoN7gvdoz62pRVM8XNTRNET4pQrNu",
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
  "id": -576460752303423395,
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
  "channel_id": "ch_nquMjp3rkJUcoqMzh51eYoN7gvdoz62pRVM8XNTRNET4pQrNu",
  "id": -576460752303423395,
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
    "channel_id": "ch_nquMjp3rkJUcoqMzh51eYoN7gvdoz62pRVM8XNTRNET4pQrNu",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_nquMjp3rkJUcoqMzh51eYoN7gvdoz62pRVM8XNTRNET4pQrNu",
    "data": {
      "event": "funding_locked"
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
    "channel_id": "ch_nquMjp3rkJUcoqMzh51eYoN7gvdoz62pRVM8XNTRNET4pQrNu",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_nquMjp3rkJUcoqMzh51eYoN7gvdoz62pRVM8XNTRNET4pQrNu",
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
    "channel_id": "ch_nquMjp3rkJUcoqMzh51eYoN7gvdoz62pRVM8XNTRNET4pQrNu",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_nquMjp3rkJUcoqMzh51eYoN7gvdoz62pRVM8XNTRNET4pQrNu",
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
    "channel_id": "ch_nquMjp3rkJUcoqMzh51eYoN7gvdoz62pRVM8XNTRNET4pQrNu",
    "data": {
      "state": "tx_+QENCwH4hLhAGJFJzcxL/BvO8N93RmVtlPCuzlMzdk09AwjunrXq2FV8eWgyzB2CKAs7TuQovUIFntkYqFt715lg6AR5Rgy0A7hAnXIMaXP0x0mZDVFbR76nKU6cFX9Tfjl49HfdCDDFSa4FGH7C4yV0OKrty3Algbz7UWuXSmRTgZY2AvKmeysJDLiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QfFpczM"
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
    "channel_id": "ch_nquMjp3rkJUcoqMzh51eYoN7gvdoz62pRVM8XNTRNET4pQrNu",
    "data": {
      "state": "tx_+QENCwH4hLhAGJFJzcxL/BvO8N93RmVtlPCuzlMzdk09AwjunrXq2FV8eWgyzB2CKAs7TuQovUIFntkYqFt715lg6AR5Rgy0A7hAnXIMaXP0x0mZDVFbR76nKU6cFX9Tfjl49HfdCDDFSa4FGH7C4yV0OKrty3Algbz7UWuXSmRTgZY2AvKmeysJDLiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QfFpczM"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_nquMjp3rkJUcoqMzh51eYoN7gvdoz62pRVM8XNTRNET4pQrNu",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBmgXrNM1RhznlO5jgGloctA/+oezAzAOXF09N5IEbPmGoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYY2kdavv/+GG0jrV+ABAIYSMJzlQAABH30WPA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423394,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEAN3AXWtijDhmyAF3mrU1e0w3+LkBrq2qmQxHAqffYdOd+FaQ2A6JhJefzSmfky1ySM1hmaFazdAnPu7QwTH6cDuF/4XTUBoQZoF6zTNUYc55TuY4BpaHLQP/qHswMwDlxdPTeSBGz5hqEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GNpHWr7//hhtI61fgAQCGEjCc5UAAAS91lV0="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_nquMjp3rkJUcoqMzh51eYoN7gvdoz62pRVM8XNTRNET4pQrNu",
  "id": -576460752303423394,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_nquMjp3rkJUcoqMzh51eYoN7gvdoz62pRVM8XNTRNET4pQrNu",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEAN3AXWtijDhmyAF3mrU1e0w3+LkBrq2qmQxHAqffYdOd+FaQ2A6JhJefzSmfky1ySM1hmaFazdAnPu7QwTH6cDuF/4XTUBoQZoF6zTNUYc55TuY4BpaHLQP/qHswMwDlxdPTeSBGz5hqEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GNpHWr7//hhtI61fgAQCGEjCc5UAAAS91lV0=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423393,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEAN3AXWtijDhmyAF3mrU1e0w3+LkBrq2qmQxHAqffYdOd+FaQ2A6JhJefzSmfky1ySM1hmaFazdAnPu7QwTH6cDuEAjAVdmQqPwV95LBNa3BK03HvTpD5Th6irF5hTHPplqevFFhiS5yYLxslMNB/Pw9ItQujDvFyzPqG9nDUELLGoAuF/4XTUBoQZoF6zTNUYc55TuY4BpaHLQP/qHswMwDlxdPTeSBGz5hqEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GNpHWr7//hhtI61fgAQCGEjCc5UAAAXAkSSQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_nquMjp3rkJUcoqMzh51eYoN7gvdoz62pRVM8XNTRNET4pQrNu",
  "id": -576460752303423393,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_nquMjp3rkJUcoqMzh51eYoN7gvdoz62pRVM8XNTRNET4pQrNu",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAN3AXWtijDhmyAF3mrU1e0w3+LkBrq2qmQxHAqffYdOd+FaQ2A6JhJefzSmfky1ySM1hmaFazdAnPu7QwTH6cDuEAjAVdmQqPwV95LBNa3BK03HvTpD5Th6irF5hTHPplqevFFhiS5yYLxslMNB/Pw9ItQujDvFyzPqG9nDUELLGoAuF/4XTUBoQZoF6zTNUYc55TuY4BpaHLQP/qHswMwDlxdPTeSBGz5hqEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GNpHWr7//hhtI61fgAQCGEjCc5UAAAXAkSSQ=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_nquMjp3rkJUcoqMzh51eYoN7gvdoz62pRVM8XNTRNET4pQrNu",
    "data": {
      "event": "close_mutual"
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
    "channel_id": "ch_nquMjp3rkJUcoqMzh51eYoN7gvdoz62pRVM8XNTRNET4pQrNu",
    "data": {
      "event": "died"
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
    "channel_id": "ch_nquMjp3rkJUcoqMzh51eYoN7gvdoz62pRVM8XNTRNET4pQrNu",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAN3AXWtijDhmyAF3mrU1e0w3+LkBrq2qmQxHAqffYdOd+FaQ2A6JhJefzSmfky1ySM1hmaFazdAnPu7QwTH6cDuEAjAVdmQqPwV95LBNa3BK03HvTpD5Th6irF5hTHPplqevFFhiS5yYLxslMNB/Pw9ItQujDvFyzPqG9nDUELLGoAuF/4XTUBoQZoF6zTNUYc55TuY4BpaHLQP/qHswMwDlxdPTeSBGz5hqEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GNpHWr7//hhtI61fgAQCGEjCc5UAAAXAkSSQ=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_nquMjp3rkJUcoqMzh51eYoN7gvdoz62pRVM8XNTRNET4pQrNu",
    "data": {
      "event": "close_mutual"
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
    "channel_id": "ch_nquMjp3rkJUcoqMzh51eYoN7gvdoz62pRVM8XNTRNET4pQrNu",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```
