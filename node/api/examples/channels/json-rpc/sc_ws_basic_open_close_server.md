
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAfNO8EGVVRoKbq3Lxj2WY6ZR+xj2jcGlcIhNerfki3mXhj+qJSJgAKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GJGE5yoAAAgoAhhAGeddIAMCgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0E1AF26Q==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423430,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDneAsMH5cxIDgHC9h2EQDwpHClCSQqP6ixWEBYP+Z4Ol2bs7XH78Tx+qCkh4loHx8LvbpZ170X6Yq6N5DJxBEKuIP4gTIBoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y/qiUiYAChAfdjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNhiRhOcqAAAIKAIYQBnnXSADAoDXj090A/DMnCedVe1N9Z8lFvhGFs8xqY89cVUV0esLtBHMvCtQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423430,
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
      "signed_tx": "tx_+MsLAfhCuEDneAsMH5cxIDgHC9h2EQDwpHClCSQqP6ixWEBYP+Z4Ol2bs7XH78Tx+qCkh4loHx8LvbpZ170X6Yq6N5DJxBEKuIP4gTIBoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y/qiUiYAChAfdjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNhiRhOcqAAAIKAIYQBnnXSADAoDXj090A/DMnCedVe1N9Z8lFvhGFs8xqY89cVUV0esLtBHMvCtQ=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423429,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAXrFipG0KAP1hXY5qNeJxghBBRUIQOFdflnNkV2bvThAvwuGdsiEjGj4pZhITL04k3WzD3Sw+Lz7iMSj5KT1iDLhA53gLDB+XMSA4BwvYdhEA8KRwpQkkKj+osVhAWD/meDpdm7O1x+/E8fqgpIeJaB8fC726Wde9F+mKujeQycQRCriD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QTMHAbe"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423429,
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
      "tx": "tx_+QENCwH4hLhAXrFipG0KAP1hXY5qNeJxghBBRUIQOFdflnNkV2bvThAvwuGdsiEjGj4pZhITL04k3WzD3Sw+Lz7iMSj5KT1iDLhA53gLDB+XMSA4BwvYdhEA8KRwpQkkKj+osVhAWD/meDpdm7O1x+/E8fqgpIeJaB8fC726Wde9F+mKujeQycQRCriD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QTMHAbe",
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
      "tx": "tx_+QENCwH4hLhAXrFipG0KAP1hXY5qNeJxghBBRUIQOFdflnNkV2bvThAvwuGdsiEjGj4pZhITL04k3WzD3Sw+Lz7iMSj5KT1iDLhA53gLDB+XMSA4BwvYdhEA8KRwpQkkKj+osVhAWD/meDpdm7O1x+/E8fqgpIeJaB8fC726Wde9F+mKujeQycQRCriD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QTMHAbe",
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
      "tx": "tx_+QENCwH4hLhAXrFipG0KAP1hXY5qNeJxghBBRUIQOFdflnNkV2bvThAvwuGdsiEjGj4pZhITL04k3WzD3Sw+Lz7iMSj5KT1iDLhA53gLDB+XMSA4BwvYdhEA8KRwpQkkKj+osVhAWD/meDpdm7O1x+/E8fqgpIeJaB8fC726Wde9F+mKujeQycQRCriD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QTMHAbe",
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
      "tx": "tx_+QENCwH4hLhAXrFipG0KAP1hXY5qNeJxghBBRUIQOFdflnNkV2bvThAvwuGdsiEjGj4pZhITL04k3WzD3Sw+Lz7iMSj5KT1iDLhA53gLDB+XMSA4BwvYdhEA8KRwpQkkKj+osVhAWD/meDpdm7O1x+/E8fqgpIeJaB8fC726Wde9F+mKujeQycQRCriD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QTMHAbe",
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "message": {
        "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "message": {
        "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
  "id": -576460752303423428,
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423428,
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "state": "tx_+QENCwH4hLhAXrFipG0KAP1hXY5qNeJxghBBRUIQOFdflnNkV2bvThAvwuGdsiEjGj4pZhITL04k3WzD3Sw+Lz7iMSj5KT1iDLhA53gLDB+XMSA4BwvYdhEA8KRwpQkkKj+osVhAWD/meDpdm7O1x+/E8fqgpIeJaB8fC726Wde9F+mKujeQycQRCriD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QTMHAbe"
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "state": "tx_+QENCwH4hLhAXrFipG0KAP1hXY5qNeJxghBBRUIQOFdflnNkV2bvThAvwuGdsiEjGj4pZhITL04k3WzD3Sw+Lz7iMSj5KT1iDLhA53gLDB+XMSA4BwvYdhEA8KRwpQkkKj+osVhAWD/meDpdm7O1x+/E8fqgpIeJaB8fC726Wde9F+mKujeQycQRCriD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QTMHAbe"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423427,
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423427,
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvwMqqcRa7U7qZOTU63p0Paz1myyd+R3XjT6HLFCPEOXAqBBCOFlzgxrCKtRrQPx23phpiUnifrgJMUhpNa+5DFOwk3/ZIQ=",
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
  "id": -576460752303423426,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA5pwBjy3W3cAwrdA128C4NFprCLVbJbEasum4xeD+7xgH0I35ESYsB+GrGKSy65N9zUHlk6v0HBAnTSmgUj48MuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsKVFaM6"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423426,
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA5pwBjy3W3cAwrdA128C4NFprCLVbJbEasum4xeD+7xgH0I35ESYsB+GrGKSy65N9zUHlk6v0HBAnTSmgUj48MuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsKVFaM6",
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
  "id": -576460752303423425,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA5pwBjy3W3cAwrdA128C4NFprCLVbJbEasum4xeD+7xgH0I35ESYsB+GrGKSy65N9zUHlk6v0HBAnTSmgUj48MuECFCL/oUT6ZGgIYm1IL8RjgszW4Dz9QalSGaOABs0J4In3+EjhYcAgPqAUg5adr4fFgZffUVDwMz2ZMYLcM+HUAuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsLLHID/"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423425,
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "state": "tx_+NILAfiEuEA5pwBjy3W3cAwrdA128C4NFprCLVbJbEasum4xeD+7xgH0I35ESYsB+GrGKSy65N9zUHlk6v0HBAnTSmgUj48MuECFCL/oUT6ZGgIYm1IL8RjgszW4Dz9QalSGaOABs0J4In3+EjhYcAgPqAUg5adr4fFgZffUVDwMz2ZMYLcM+HUAuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsLLHID/"
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "state": "tx_+NILAfiEuEA5pwBjy3W3cAwrdA128C4NFprCLVbJbEasum4xeD+7xgH0I35ESYsB+GrGKSy65N9zUHlk6v0HBAnTSmgUj48MuECFCL/oUT6ZGgIYm1IL8RjgszW4Dz9QalSGaOABs0J4In3+EjhYcAgPqAUg5adr4fFgZffUVDwMz2ZMYLcM+HUAuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsLLHID/"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423424,
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423424,
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
  "id": -576460752303423423,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423423,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA5pwBjy3W3cAwrdA128C4NFprCLVbJbEasum4xeD+7xgH0I35ESYsB+GrGKSy65N9zUHlk6v0HBAnTSmgUj48MuECFCL/oUT6ZGgIYm1IL8RjgszW4Dz9QalSGaOABs0J4In3+EjhYcAgPqAUg5adr4fFgZffUVDwMz2ZMYLcM+HUAuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsLLHID/",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAArDvQAGg807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiX/4rKrmw"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423422,
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423422,
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvwMqqcRa7U7qZOTU63p0Paz1myyd+R3XjT6HLFCPEOXA6A149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7Vs933k=",
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
  "id": -576460752303423421,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDBK/GQeII5qx6S8poDRvSmEECDeFqVucFargHypcvSGsHO4aLEgZg5IyLGNMUfh5vkPApV+Udfx+oGVsK9rD8JuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu08X8zn"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423421,
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDBK/GQeII5qx6S8poDRvSmEECDeFqVucFargHypcvSGsHO4aLEgZg5IyLGNMUfh5vkPApV+Udfx+oGVsK9rD8JuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu08X8zn",
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
  "id": -576460752303423420,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAQoyI1DSWa4RHNWPjmMTs+2nIC/nJnRHm+b8byxfkBTpovhG8BjUUX14lBQyGsip+VkpPnJl0omQDac4+fGkYPuEDBK/GQeII5qx6S8poDRvSmEECDeFqVucFargHypcvSGsHO4aLEgZg5IyLGNMUfh5vkPApV+Udfx+oGVsK9rD8JuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0V6SFE"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423420,
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "state": "tx_+NILAfiEuEAQoyI1DSWa4RHNWPjmMTs+2nIC/nJnRHm+b8byxfkBTpovhG8BjUUX14lBQyGsip+VkpPnJl0omQDac4+fGkYPuEDBK/GQeII5qx6S8poDRvSmEECDeFqVucFargHypcvSGsHO4aLEgZg5IyLGNMUfh5vkPApV+Udfx+oGVsK9rD8JuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0V6SFE"
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "state": "tx_+NILAfiEuEAQoyI1DSWa4RHNWPjmMTs+2nIC/nJnRHm+b8byxfkBTpovhG8BjUUX14lBQyGsip+VkpPnJl0omQDac4+fGkYPuEDBK/GQeII5qx6S8poDRvSmEECDeFqVucFargHypcvSGsHO4aLEgZg5IyLGNMUfh5vkPApV+Udfx+oGVsK9rD8JuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0V6SFE"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423419,
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423419,
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
  "id": -576460752303423418,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423418,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAQoyI1DSWa4RHNWPjmMTs+2nIC/nJnRHm+b8byxfkBTpovhG8BjUUX14lBQyGsip+VkpPnJl0omQDac4+fGkYPuEDBK/GQeII5qx6S8poDRvSmEECDeFqVucFargHypcvSGsHO4aLEgZg5IyLGNMUfh5vkPApV+Udfx+oGVsK9rD8JuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0V6SFE",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAAbDvQAGg807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiX/+PWk/e"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423417,
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423417,
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvwMqqcRa7U7qZOTU63p0Paz1myyd+R3XjT6HLFCPEOXBKBD48upGMSQmUHkvAbXk8OLPb+iXSg8kxqzNfUkPoVMWXdvDjM=",
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
  "id": -576460752303423416,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBEo/DWC+XxcxEQP6sUbB1EsvyXZcnk0lzGXoJ3TLDF/e4BzqWaZr2hgfvj2lv/zyp/aysQ6dwe4oyLmQdlp4EGuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwSgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFl2pioH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423416,
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBEo/DWC+XxcxEQP6sUbB1EsvyXZcnk0lzGXoJ3TLDF/e4BzqWaZr2hgfvj2lv/zyp/aysQ6dwe4oyLmQdlp4EGuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwSgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFl2pioH",
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
  "id": -576460752303423415,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBEo/DWC+XxcxEQP6sUbB1EsvyXZcnk0lzGXoJ3TLDF/e4BzqWaZr2hgfvj2lv/zyp/aysQ6dwe4oyLmQdlp4EGuED94lLDr4jyBfQOnzIyZBCsT2L4pme1uvsWJpP3at7I5NX/GmKY9ZJ4GqY0g0MMlwpP6LbWCADUWdjq1GddCj8HuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwSgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFl9LIEh"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423415,
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "state": "tx_+NILAfiEuEBEo/DWC+XxcxEQP6sUbB1EsvyXZcnk0lzGXoJ3TLDF/e4BzqWaZr2hgfvj2lv/zyp/aysQ6dwe4oyLmQdlp4EGuED94lLDr4jyBfQOnzIyZBCsT2L4pme1uvsWJpP3at7I5NX/GmKY9ZJ4GqY0g0MMlwpP6LbWCADUWdjq1GddCj8HuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwSgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFl9LIEh"
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "state": "tx_+NILAfiEuEBEo/DWC+XxcxEQP6sUbB1EsvyXZcnk0lzGXoJ3TLDF/e4BzqWaZr2hgfvj2lv/zyp/aysQ6dwe4oyLmQdlp4EGuED94lLDr4jyBfQOnzIyZBCsT2L4pme1uvsWJpP3at7I5NX/GmKY9ZJ4GqY0g0MMlwpP6LbWCADUWdjq1GddCj8HuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwSgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFl9LIEh"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423414,
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423414,
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
  "id": -576460752303423413,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423413,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBEo/DWC+XxcxEQP6sUbB1EsvyXZcnk0lzGXoJ3TLDF/e4BzqWaZr2hgfvj2lv/zyp/aysQ6dwe4oyLmQdlp4EGuED94lLDr4jyBfQOnzIyZBCsT2L4pme1uvsWJpP3at7I5NX/GmKY9ZJ4GqY0g0MMlwpP6LbWCADUWdjq1GddCj8HuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwSgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFl9LIEh",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAALDvQAGg807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiYAAzY13U"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423412,
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423412,
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvwMqqcRa7U7qZOTU63p0Paz1myyd+R3XjT6HLFCPEOXBaA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7WpexGo=",
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
  "id": -576460752303423411,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBdMYtJjQnMP84C92KX3XObB80SID32BGVSR1OGmFvN2lEyja8dFba7TkTS9xM0jNHw86IhVao39vxSSsj4fWILuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0GEnJq"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423411,
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBdMYtJjQnMP84C92KX3XObB80SID32BGVSR1OGmFvN2lEyja8dFba7TkTS9xM0jNHw86IhVao39vxSSsj4fWILuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0GEnJq",
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
  "id": -576460752303423410,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBdMYtJjQnMP84C92KX3XObB80SID32BGVSR1OGmFvN2lEyja8dFba7TkTS9xM0jNHw86IhVao39vxSSsj4fWILuED82jKogidmseQUG5+xzOIpDxBGaGbYbBcuGIwjGMgOCk6L9w9UtESxknctE4qzXHIKCbMsxAR4zmmo60/3/G4CuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0gAApJ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423410,
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "state": "tx_+NILAfiEuEBdMYtJjQnMP84C92KX3XObB80SID32BGVSR1OGmFvN2lEyja8dFba7TkTS9xM0jNHw86IhVao39vxSSsj4fWILuED82jKogidmseQUG5+xzOIpDxBGaGbYbBcuGIwjGMgOCk6L9w9UtESxknctE4qzXHIKCbMsxAR4zmmo60/3/G4CuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0gAApJ"
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "state": "tx_+NILAfiEuEBdMYtJjQnMP84C92KX3XObB80SID32BGVSR1OGmFvN2lEyja8dFba7TkTS9xM0jNHw86IhVao39vxSSsj4fWILuED82jKogidmseQUG5+xzOIpDxBGaGbYbBcuGIwjGMgOCk6L9w9UtESxknctE4qzXHIKCbMsxAR4zmmo60/3/G4CuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0gAApJ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423409,
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423409,
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
  "id": -576460752303423408,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423408,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBdMYtJjQnMP84C92KX3XObB80SID32BGVSR1OGmFvN2lEyja8dFba7TkTS9xM0jNHw86IhVao39vxSSsj4fWILuED82jKogidmseQUG5+xzOIpDxBGaGbYbBcuGIwjGMgOCk6L9w9UtESxknctE4qzXHIKCbMsxAR4zmmo60/3/G4CuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0gAApJ",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAAbDvQAGg807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiX/+PWk/e"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423407,
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423407,
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvwMqqcRa7U7qZOTU63p0Paz1myyd+R3XjT6HLFCPEOXBqBD48upGMSQmUHkvAbXk8OLPb+iXSg8kxqzNfUkPoVMWSV9Zgk=",
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
  "id": -576460752303423406,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA8rv4iCOhxJOAp7e7Vft9VdRzRNSrvYhsBKtoOqaWE+KGqKW7Qlhy7GR/CKfwdXG+IkMluQwAs7cS1Rl/jlxoNuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFkFohhc"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423406,
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA8rv4iCOhxJOAp7e7Vft9VdRzRNSrvYhsBKtoOqaWE+KGqKW7Qlhy7GR/CKfwdXG+IkMluQwAs7cS1Rl/jlxoNuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFkFohhc",
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
  "id": -576460752303423405,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAtRaqwTHo15+fWenOnS0hNYRDteuJ8jy5FQYy7MEW2HahG7HznTBti6bN5Eub9A1ELS7Xx64ofeEeS4mqzgWMFuEA8rv4iCOhxJOAp7e7Vft9VdRzRNSrvYhsBKtoOqaWE+KGqKW7Qlhy7GR/CKfwdXG+IkMluQwAs7cS1Rl/jlxoNuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFlicnEQ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423405,
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "state": "tx_+NILAfiEuEAtRaqwTHo15+fWenOnS0hNYRDteuJ8jy5FQYy7MEW2HahG7HznTBti6bN5Eub9A1ELS7Xx64ofeEeS4mqzgWMFuEA8rv4iCOhxJOAp7e7Vft9VdRzRNSrvYhsBKtoOqaWE+KGqKW7Qlhy7GR/CKfwdXG+IkMluQwAs7cS1Rl/jlxoNuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFlicnEQ"
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
    "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
    "data": {
      "state": "tx_+NILAfiEuEAtRaqwTHo15+fWenOnS0hNYRDteuJ8jy5FQYy7MEW2HahG7HznTBti6bN5Eub9A1ELS7Xx64ofeEeS4mqzgWMFuEA8rv4iCOhxJOAp7e7Vft9VdRzRNSrvYhsBKtoOqaWE+KGqKW7Qlhy7GR/CKfwdXG+IkMluQwAs7cS1Rl/jlxoNuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFlicnEQ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423404,
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
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423404,
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
  "id": -576460752303423403,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v1GQfDWhReV4JHE1pKi5PP196KNyKa9d4iQJ5r2v27bMXmq2N",
  "id": -576460752303423403,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAtRaqwTHo15+fWenOnS0hNYRDteuJ8jy5FQYy7MEW2HahG7HznTBti6bN5Eub9A1ELS7Xx64ofeEeS4mqzgWMFuEA8rv4iCOhxJOAp7e7Vft9VdRzRNSrvYhsBKtoOqaWE+KGqKW7Qlhy7GR/CKfwdXG+IkMluQwAs7cS1Rl/jlxoNuEj4RjkCoQb8DKqnEWu1O6mTk1Ot6dD2s9Zssnfkd140+hyxQjxDlwagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFlicnEQ",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAALDvQAGg807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiYAAzY13U"
  },
  "version": 1
}
```
