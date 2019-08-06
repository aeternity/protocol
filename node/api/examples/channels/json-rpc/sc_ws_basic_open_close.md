
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAfNO8EGVVRoKbq3Lxj2WY6ZR+xj2jcGlcIhNerfki3mXhj+qJSJgAKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GJGE5yoAAAgoAhhAGeddIAMCgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0Dy6cUnQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423458,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEB+SgfltYs2nDdEFhU4Z7vd6bJ8RBnRGw2wrSbmOGOv01NXmFEZyDa86KfZc0FsSqADh6mNyQ5EtALnd+RTrQoFuIP4gTIBoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y/qiUiYAChAfdjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNhiRhOcqAAAIKAIYQBnnXSADAoDXj090A/DMnCedVe1N9Z8lFvhGFs8xqY89cVUV0esLtA6G9PAM="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423458,
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
      "signed_tx": "tx_+MsLAfhCuEB+SgfltYs2nDdEFhU4Z7vd6bJ8RBnRGw2wrSbmOGOv01NXmFEZyDa86KfZc0FsSqADh6mNyQ5EtALnd+RTrQoFuIP4gTIBoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y/qiUiYAChAfdjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNhiRhOcqAAAIKAIYQBnnXSADAoDXj090A/DMnCedVe1N9Z8lFvhGFs8xqY89cVUV0esLtA6G9PAM=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423457,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAOsChD3RjCr2F/TBgRSzW4VLLDnvDoIRFj5zoi1sQvY9A0ihZOnO9wX/NKK5k2zIhhGQ3DOlh/eRPVpn9V63sArhAfkoH5bWLNpw3RBYVOGe73emyfEQZ0RsNsK0m5jhjr9NTV5hRGcg2vOin2XNBbEqgA4epjckORLQC53fkU60KBbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QP/2JdX"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423457,
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
      "tx": "tx_+QENCwH4hLhAOsChD3RjCr2F/TBgRSzW4VLLDnvDoIRFj5zoi1sQvY9A0ihZOnO9wX/NKK5k2zIhhGQ3DOlh/eRPVpn9V63sArhAfkoH5bWLNpw3RBYVOGe73emyfEQZ0RsNsK0m5jhjr9NTV5hRGcg2vOin2XNBbEqgA4epjckORLQC53fkU60KBbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QP/2JdX",
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
      "tx": "tx_+QENCwH4hLhAOsChD3RjCr2F/TBgRSzW4VLLDnvDoIRFj5zoi1sQvY9A0ihZOnO9wX/NKK5k2zIhhGQ3DOlh/eRPVpn9V63sArhAfkoH5bWLNpw3RBYVOGe73emyfEQZ0RsNsK0m5jhjr9NTV5hRGcg2vOin2XNBbEqgA4epjckORLQC53fkU60KBbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QP/2JdX",
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
      "tx": "tx_+QENCwH4hLhAOsChD3RjCr2F/TBgRSzW4VLLDnvDoIRFj5zoi1sQvY9A0ihZOnO9wX/NKK5k2zIhhGQ3DOlh/eRPVpn9V63sArhAfkoH5bWLNpw3RBYVOGe73emyfEQZ0RsNsK0m5jhjr9NTV5hRGcg2vOin2XNBbEqgA4epjckORLQC53fkU60KBbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QP/2JdX",
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
      "tx": "tx_+QENCwH4hLhAOsChD3RjCr2F/TBgRSzW4VLLDnvDoIRFj5zoi1sQvY9A0ihZOnO9wX/NKK5k2zIhhGQ3DOlh/eRPVpn9V63sArhAfkoH5bWLNpw3RBYVOGe73emyfEQZ0RsNsK0m5jhjr9NTV5hRGcg2vOin2XNBbEqgA4epjckORLQC53fkU60KBbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QP/2JdX",
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "message": {
        "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "message": {
        "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
  "id": -576460752303423456,
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423456,
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "state": "tx_+QENCwH4hLhAOsChD3RjCr2F/TBgRSzW4VLLDnvDoIRFj5zoi1sQvY9A0ihZOnO9wX/NKK5k2zIhhGQ3DOlh/eRPVpn9V63sArhAfkoH5bWLNpw3RBYVOGe73emyfEQZ0RsNsK0m5jhjr9NTV5hRGcg2vOin2XNBbEqgA4epjckORLQC53fkU60KBbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QP/2JdX"
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "state": "tx_+QENCwH4hLhAOsChD3RjCr2F/TBgRSzW4VLLDnvDoIRFj5zoi1sQvY9A0ihZOnO9wX/NKK5k2zIhhGQ3DOlh/eRPVpn9V63sArhAfkoH5bWLNpw3RBYVOGe73emyfEQZ0RsNsK0m5jhjr9NTV5hRGcg2vOin2XNBbEqgA4epjckORLQC53fkU60KBbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QP/2JdX"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423455,
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423455,
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmokqyJ/TFPIpXx+238m6ay+yCbfWbgc40jA+a/EtyftAqBBCOFlzgxrCKtRrQPx23phpiUnifrgJMUhpNa+5DFOwsfu+cI=",
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
  "id": -576460752303423454,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECjX5coHOEX4NzLJyMt0hopm9YkWYsxPHFUNqkuO2M0U3cmRNN3ClmnaMtoCa/hY82wvuwJIWP37eF9j88CBgUFuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsKuH0DS"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423454,
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "signed_tx": "tx_+JALAfhCuECjX5coHOEX4NzLJyMt0hopm9YkWYsxPHFUNqkuO2M0U3cmRNN3ClmnaMtoCa/hY82wvuwJIWP37eF9j88CBgUFuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsKuH0DS",
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
  "id": -576460752303423453,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECjX5coHOEX4NzLJyMt0hopm9YkWYsxPHFUNqkuO2M0U3cmRNN3ClmnaMtoCa/hY82wvuwJIWP37eF9j88CBgUFuEC/HrGDEcbG/lO6oPPk5WOQHM6XQEbNnKSZciZ6b5gbVW4QIF10KVug6IsRPYVfkI3LB3KBU3HeLUSXwD9FgBcGuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsJbOlnM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423453,
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "state": "tx_+NILAfiEuECjX5coHOEX4NzLJyMt0hopm9YkWYsxPHFUNqkuO2M0U3cmRNN3ClmnaMtoCa/hY82wvuwJIWP37eF9j88CBgUFuEC/HrGDEcbG/lO6oPPk5WOQHM6XQEbNnKSZciZ6b5gbVW4QIF10KVug6IsRPYVfkI3LB3KBU3HeLUSXwD9FgBcGuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsJbOlnM"
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "state": "tx_+NILAfiEuECjX5coHOEX4NzLJyMt0hopm9YkWYsxPHFUNqkuO2M0U3cmRNN3ClmnaMtoCa/hY82wvuwJIWP37eF9j88CBgUFuEC/HrGDEcbG/lO6oPPk5WOQHM6XQEbNnKSZciZ6b5gbVW4QIF10KVug6IsRPYVfkI3LB3KBU3HeLUSXwD9FgBcGuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsJbOlnM"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423452,
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423452,
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
  "id": -576460752303423451,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423451,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECjX5coHOEX4NzLJyMt0hopm9YkWYsxPHFUNqkuO2M0U3cmRNN3ClmnaMtoCa/hY82wvuwJIWP37eF9j88CBgUFuEC/HrGDEcbG/lO6oPPk5WOQHM6XQEbNnKSZciZ6b5gbVW4QIF10KVug6IsRPYVfkI3LB3KBU3HeLUSXwD9FgBcGuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsJbOlnM",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAArDvQAGg807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiX/4rKrmw"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423450,
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423450,
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmokqyJ/TFPIpXx+238m6ay+yCbfWbgc40jA+a/EtyftA6A149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7Vyd3hk=",
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
  "id": -576460752303423449,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED+BosvOC1SyLGV7lpXgogk4Gvec5hxOltEwVpnC1Hx57XPFceSua/DWvEUQDuQlHTbqOcJ8Bgo3JLdZshUx+oFuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu2BW/UN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423449,
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "signed_tx": "tx_+JALAfhCuED+BosvOC1SyLGV7lpXgogk4Gvec5hxOltEwVpnC1Hx57XPFceSua/DWvEUQDuQlHTbqOcJ8Bgo3JLdZshUx+oFuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu2BW/UN",
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
  "id": -576460752303423448,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBkun+/xnjcvuYYBg7AScB/pwFR5TeTe97IgQkGDE8uZ+rZT+e1ffIlFxlgLjMN4WX/YZEOIhjeQbt+LJEqENYMuED+BosvOC1SyLGV7lpXgogk4Gvec5hxOltEwVpnC1Hx57XPFceSua/DWvEUQDuQlHTbqOcJ8Bgo3JLdZshUx+oFuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu3IvKZv"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423448,
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "state": "tx_+NILAfiEuEBkun+/xnjcvuYYBg7AScB/pwFR5TeTe97IgQkGDE8uZ+rZT+e1ffIlFxlgLjMN4WX/YZEOIhjeQbt+LJEqENYMuED+BosvOC1SyLGV7lpXgogk4Gvec5hxOltEwVpnC1Hx57XPFceSua/DWvEUQDuQlHTbqOcJ8Bgo3JLdZshUx+oFuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu3IvKZv"
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "state": "tx_+NILAfiEuEBkun+/xnjcvuYYBg7AScB/pwFR5TeTe97IgQkGDE8uZ+rZT+e1ffIlFxlgLjMN4WX/YZEOIhjeQbt+LJEqENYMuED+BosvOC1SyLGV7lpXgogk4Gvec5hxOltEwVpnC1Hx57XPFceSua/DWvEUQDuQlHTbqOcJ8Bgo3JLdZshUx+oFuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu3IvKZv"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423447,
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423447,
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
  "id": -576460752303423446,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423446,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBkun+/xnjcvuYYBg7AScB/pwFR5TeTe97IgQkGDE8uZ+rZT+e1ffIlFxlgLjMN4WX/YZEOIhjeQbt+LJEqENYMuED+BosvOC1SyLGV7lpXgogk4Gvec5hxOltEwVpnC1Hx57XPFceSua/DWvEUQDuQlHTbqOcJ8Bgo3JLdZshUx+oFuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu3IvKZv",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAAbDvQAGg807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiX/+PWk/e"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423445,
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423445,
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmokqyJ/TFPIpXx+238m6ay+yCbfWbgc40jA+a/EtyftBKBD48upGMSQmUHkvAbXk8OLPb+iXSg8kxqzNfUkPoVMWZp4WqU=",
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
  "id": -576460752303423444,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC3JjtLws9OrX12GUdZEyxsnnwJ/hO+RFtzqVIiKpY8SOf6nfXILcCUNuCtb/O+idCxmH6C2/11SdX2Wh1bwhMJuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QSgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFm2RAxQ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423444,
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC3JjtLws9OrX12GUdZEyxsnnwJ/hO+RFtzqVIiKpY8SOf6nfXILcCUNuCtb/O+idCxmH6C2/11SdX2Wh1bwhMJuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QSgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFm2RAxQ",
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
  "id": -576460752303423443,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAyevQtw285Z7tNdxEQ8Pkthg4bmVoH5dInCqi1o3MwgDK8oXwUSle6gX4q/riLjR+GmyiHcWPJn2IFjUOkTVgKuEC3JjtLws9OrX12GUdZEyxsnnwJ/hO+RFtzqVIiKpY8SOf6nfXILcCUNuCtb/O+idCxmH6C2/11SdX2Wh1bwhMJuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QSgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFkXhCFf"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423443,
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "state": "tx_+NILAfiEuEAyevQtw285Z7tNdxEQ8Pkthg4bmVoH5dInCqi1o3MwgDK8oXwUSle6gX4q/riLjR+GmyiHcWPJn2IFjUOkTVgKuEC3JjtLws9OrX12GUdZEyxsnnwJ/hO+RFtzqVIiKpY8SOf6nfXILcCUNuCtb/O+idCxmH6C2/11SdX2Wh1bwhMJuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QSgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFkXhCFf"
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "state": "tx_+NILAfiEuEAyevQtw285Z7tNdxEQ8Pkthg4bmVoH5dInCqi1o3MwgDK8oXwUSle6gX4q/riLjR+GmyiHcWPJn2IFjUOkTVgKuEC3JjtLws9OrX12GUdZEyxsnnwJ/hO+RFtzqVIiKpY8SOf6nfXILcCUNuCtb/O+idCxmH6C2/11SdX2Wh1bwhMJuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QSgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFkXhCFf"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423442,
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423442,
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
  "id": -576460752303423441,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423441,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAyevQtw285Z7tNdxEQ8Pkthg4bmVoH5dInCqi1o3MwgDK8oXwUSle6gX4q/riLjR+GmyiHcWPJn2IFjUOkTVgKuEC3JjtLws9OrX12GUdZEyxsnnwJ/hO+RFtzqVIiKpY8SOf6nfXILcCUNuCtb/O+idCxmH6C2/11SdX2Wh1bwhMJuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QSgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFkXhCFf",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAALDvQAGg807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiYAAzY13U"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423440,
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423440,
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmokqyJ/TFPIpXx+238m6ay+yCbfWbgc40jA+a/EtyftBaA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7UDPCVQ=",
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
  "id": -576460752303423439,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC6znLtyKoeI7l0Apscn9RvwXurRqzh7I01yc8Dvq4vR1PVOATtxytUJ5I6YHL7l9wFGNR9rg6IfFOq2Msg0SEPuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0XI9+H"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423439,
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC6znLtyKoeI7l0Apscn9RvwXurRqzh7I01yc8Dvq4vR1PVOATtxytUJ5I6YHL7l9wFGNR9rg6IfFOq2Msg0SEPuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0XI9+H",
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
  "id": -576460752303423438,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAF9MGmbh7lFrwgjn/MHkkf4mzlJf93AVGROZk2O1t0d/CQoixjxCcIJohljY3b62+gwej4toNCdS6RMKHUDlkMuEC6znLtyKoeI7l0Apscn9RvwXurRqzh7I01yc8Dvq4vR1PVOATtxytUJ5I6YHL7l9wFGNR9rg6IfFOq2Msg0SEPuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu1igcw3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423438,
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "state": "tx_+NILAfiEuEAF9MGmbh7lFrwgjn/MHkkf4mzlJf93AVGROZk2O1t0d/CQoixjxCcIJohljY3b62+gwej4toNCdS6RMKHUDlkMuEC6znLtyKoeI7l0Apscn9RvwXurRqzh7I01yc8Dvq4vR1PVOATtxytUJ5I6YHL7l9wFGNR9rg6IfFOq2Msg0SEPuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu1igcw3"
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "state": "tx_+NILAfiEuEAF9MGmbh7lFrwgjn/MHkkf4mzlJf93AVGROZk2O1t0d/CQoixjxCcIJohljY3b62+gwej4toNCdS6RMKHUDlkMuEC6znLtyKoeI7l0Apscn9RvwXurRqzh7I01yc8Dvq4vR1PVOATtxytUJ5I6YHL7l9wFGNR9rg6IfFOq2Msg0SEPuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu1igcw3"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423437,
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423437,
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
  "id": -576460752303423436,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423436,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAF9MGmbh7lFrwgjn/MHkkf4mzlJf93AVGROZk2O1t0d/CQoixjxCcIJohljY3b62+gwej4toNCdS6RMKHUDlkMuEC6znLtyKoeI7l0Apscn9RvwXurRqzh7I01yc8Dvq4vR1PVOATtxytUJ5I6YHL7l9wFGNR9rg6IfFOq2Msg0SEPuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu1igcw3",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAAbDvQAGg807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiX/+PWk/e"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423435,
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423435,
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmokqyJ/TFPIpXx+238m6ay+yCbfWbgc40jA+a/EtyftBqBD48upGMSQmUHkvAbXk8OLPb+iXSg8kxqzNfUkPoVMWWGSRmE=",
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
  "id": -576460752303423434,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECA0r/FBwlYE+ywf/eAdINTh1E0wWPCbcw5xwHOtwO/a4R0Dhtvrjb3gnrOvKl6FoCm1rSSo/pRJD6D5V8fgJYGuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFnUEdGR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423434,
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "signed_tx": "tx_+JALAfhCuECA0r/FBwlYE+ywf/eAdINTh1E0wWPCbcw5xwHOtwO/a4R0Dhtvrjb3gnrOvKl6FoCm1rSSo/pRJD6D5V8fgJYGuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFnUEdGR",
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
  "id": -576460752303423433,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECA0r/FBwlYE+ywf/eAdINTh1E0wWPCbcw5xwHOtwO/a4R0Dhtvrjb3gnrOvKl6FoCm1rSSo/pRJD6D5V8fgJYGuEC6KTugU3ioymKpAiMb1scTZ+8RqFSCimp2yO0VirjgLMNp3sM83NN19BMbHSRxGUydihJ3af9VbO5CF66mjOUMuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFl0LGuo"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423433,
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "state": "tx_+NILAfiEuECA0r/FBwlYE+ywf/eAdINTh1E0wWPCbcw5xwHOtwO/a4R0Dhtvrjb3gnrOvKl6FoCm1rSSo/pRJD6D5V8fgJYGuEC6KTugU3ioymKpAiMb1scTZ+8RqFSCimp2yO0VirjgLMNp3sM83NN19BMbHSRxGUydihJ3af9VbO5CF66mjOUMuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFl0LGuo"
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
    "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
    "data": {
      "state": "tx_+NILAfiEuECA0r/FBwlYE+ywf/eAdINTh1E0wWPCbcw5xwHOtwO/a4R0Dhtvrjb3gnrOvKl6FoCm1rSSo/pRJD6D5V8fgJYGuEC6KTugU3ioymKpAiMb1scTZ+8RqFSCimp2yO0VirjgLMNp3sM83NN19BMbHSRxGUydihJ3af9VbO5CF66mjOUMuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFl0LGuo"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423432,
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
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423432,
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
  "id": -576460752303423431,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_okHcpyTvbkvo8eRNHuNDdE6FMV5CAirsmn7762Y4LuxwsocXT",
  "id": -576460752303423431,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECA0r/FBwlYE+ywf/eAdINTh1E0wWPCbcw5xwHOtwO/a4R0Dhtvrjb3gnrOvKl6FoCm1rSSo/pRJD6D5V8fgJYGuEC6KTugU3ioymKpAiMb1scTZ+8RqFSCimp2yO0VirjgLMNp3sM83NN19BMbHSRxGUydihJ3af9VbO5CF66mjOUMuEj4RjkCoQZqJKsif0xTyKV8ftt/Jumsvsgm31m4HONIwPmvxLcn7QagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFl0LGuo",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAALDvQAGg807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiYAAzY13U"
  },
  "version": 1
}
```
