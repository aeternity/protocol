
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_slash_%2F2618%5Binitiator44initiator%5D
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_slash_%2F2618%5Binitiator44initiator%5D
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAfNO8EGVVRoKbq3Lxj2WY6ZR+xj2jcGlcIhNerfki3mXhj+qJSJgAKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GJGE5yoAAAgoAhhAGeddIAMCgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0MSWSvZQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423382,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAmpCndGfpZgXzOVexwKayMq/khCx6id6CZC54bRYj+MKZUx7U3oNCTMLGqEAxVEo2LK2h9c8pZi+nVaHO0izQOuIP4gTIBoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y/qiUiYAChAfdjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNhiRhOcqAAAIKAIYQBnnXSADAoDXj090A/DMnCedVe1N9Z8lFvhGFs8xqY89cVUV0esLtDAynAzQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423382,
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
      "signed_tx": "tx_+MsLAfhCuEAmpCndGfpZgXzOVexwKayMq/khCx6id6CZC54bRYj+MKZUx7U3oNCTMLGqEAxVEo2LK2h9c8pZi+nVaHO0izQOuIP4gTIBoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y/qiUiYAChAfdjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNhiRhOcqAAAIKAIYQBnnXSADAoDXj090A/DMnCedVe1N9Z8lFvhGFs8xqY89cVUV0esLtDAynAzQ=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423381,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAJqQp3Rn6WYF8zlXscCmsjKv5IQseonegmQueG0WI/jCmVMe1N6DQkzCxqhAMVRKNiytofXPKWYvp1WhztIs0DrhAW357ctjIOqusWd/E5pXi9bIzuL7oVkbaPhDupnGm4t+hTaOGoFppOsCFiAHWNw4nhl18e2JT6tsRGqvBHZ7yBLiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QxqDB37"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423381,
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
      "tx": "tx_+QENCwH4hLhAJqQp3Rn6WYF8zlXscCmsjKv5IQseonegmQueG0WI/jCmVMe1N6DQkzCxqhAMVRKNiytofXPKWYvp1WhztIs0DrhAW357ctjIOqusWd/E5pXi9bIzuL7oVkbaPhDupnGm4t+hTaOGoFppOsCFiAHWNw4nhl18e2JT6tsRGqvBHZ7yBLiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QxqDB37",
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
      "tx": "tx_+QENCwH4hLhAJqQp3Rn6WYF8zlXscCmsjKv5IQseonegmQueG0WI/jCmVMe1N6DQkzCxqhAMVRKNiytofXPKWYvp1WhztIs0DrhAW357ctjIOqusWd/E5pXi9bIzuL7oVkbaPhDupnGm4t+hTaOGoFppOsCFiAHWNw4nhl18e2JT6tsRGqvBHZ7yBLiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QxqDB37",
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
      "tx": "tx_+QENCwH4hLhAJqQp3Rn6WYF8zlXscCmsjKv5IQseonegmQueG0WI/jCmVMe1N6DQkzCxqhAMVRKNiytofXPKWYvp1WhztIs0DrhAW357ctjIOqusWd/E5pXi9bIzuL7oVkbaPhDupnGm4t+hTaOGoFppOsCFiAHWNw4nhl18e2JT6tsRGqvBHZ7yBLiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QxqDB37",
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
      "tx": "tx_+QENCwH4hLhAJqQp3Rn6WYF8zlXscCmsjKv5IQseonegmQueG0WI/jCmVMe1N6DQkzCxqhAMVRKNiytofXPKWYvp1WhztIs0DrhAW357ctjIOqusWd/E5pXi9bIzuL7oVkbaPhDupnGm4t+hTaOGoFppOsCFiAHWNw4nhl18e2JT6tsRGqvBHZ7yBLiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QxqDB37",
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
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
    "data": {
      "message": {
        "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
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
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
    "data": {
      "message": {
        "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
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
  "id": -576460752303423380,
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
  "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
  "id": -576460752303423380,
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
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
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
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
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
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
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
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
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
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder info
> Channel is `open` and ready to use

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
    "data": {
      "state": "tx_+QENCwH4hLhAJqQp3Rn6WYF8zlXscCmsjKv5IQseonegmQueG0WI/jCmVMe1N6DQkzCxqhAMVRKNiytofXPKWYvp1WhztIs0DrhAW357ctjIOqusWd/E5pXi9bIzuL7oVkbaPhDupnGm4t+hTaOGoFppOsCFiAHWNw4nhl18e2JT6tsRGqvBHZ7yBLiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QxqDB37"
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
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
    "data": {
      "state": "tx_+QENCwH4hLhAJqQp3Rn6WYF8zlXscCmsjKv5IQseonegmQueG0WI/jCmVMe1N6DQkzCxqhAMVRKNiytofXPKWYvp1WhztIs0DrhAW357ctjIOqusWd/E5pXi9bIzuL7oVkbaPhDupnGm4t+hTaOGoFppOsCFiAHWNw4nhl18e2JT6tsRGqvBHZ7yBLiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QxqDB37"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
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
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
    "data": {
      "poi": "pi_+QGPPAH5AYX5AYKgzjPoxvF7i0Rogt3HkCECEP488lCJfxH/pjhMnAW0H175AV74dKBCtP1Hq2qT20MxrCfa6+4NtpcN4yYiF5Q49PWrKoAeWvhRgICAoF3LDUbbHv4PQYhz+7hhcxvJKCVkvdvZcT7v3lpcdhJogICAoOyT7A0xMr4xEpU8GaLKmoEzVli5CVJmhhDFgSb84h88gICAgICAgICA+E+gXcsNRtse/g9BiHP7uGFzG8koJWS929lxPu/eWlx2EmjtoCBO8EGVVRoKbq3Lxj2WY6ZR+xj2jcGlcIhNerfki3mXi8oKAQCGP6olIl//+ESgzjPoxvF7i0Rogt3HkCECEP488lCJfxH/pjhMnAW0H17iH6BCtP1Hq2qT20MxrCfa6+4NtpcN4yYiF5Q49PWrKoAeWvhPoOyT7A0xMr4xEpU8GaLKmoEzVli5CVJmhhDFgSb84h887aAgYzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAAcDAwMDAZfj5+A=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423379,
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
  "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
  "id": -576460752303423379,
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
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBnCgvo64Pb8TJon7OfHRH7s345rOstX6xLehjUXRNcg1AqBBCOFlzgxrCKtRrQPx23phpiUnifrgJMUhpNa+5DFOwjokcDY=",
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
  "id": -576460752303423378,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBtTuB20H4xw2AyFYtH19Xwg7SlTNlcX/0ke1H9iBhYBCYdny90bTw49syGCdzEl0aI4yLKH4XhIzDjGUeFBAMHuEj4RjkCoQZwoL6OuD2/EyaJ+znx0R+7N+OazrLV+sS3oY1F0TXINQKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsJyHv0A"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
  "id": -576460752303423378,
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
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
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
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBtTuB20H4xw2AyFYtH19Xwg7SlTNlcX/0ke1H9iBhYBCYdny90bTw49syGCdzEl0aI4yLKH4XhIzDjGUeFBAMHuEj4RjkCoQZwoL6OuD2/EyaJ+znx0R+7N+OazrLV+sS3oY1F0TXINQKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsJyHv0A",
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
  "id": -576460752303423377,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBtTuB20H4xw2AyFYtH19Xwg7SlTNlcX/0ke1H9iBhYBCYdny90bTw49syGCdzEl0aI4yLKH4XhIzDjGUeFBAMHuEC9yBEBv4BDnYmZMr5jDPwGZtrDei7z/OgrFPHx4PnW8/W2EPic2FVWKLk1et2brOsTW13EBldKcHSJHJPY1IUHuEj4RjkCoQZwoL6OuD2/EyaJ+znx0R+7N+OazrLV+sS3oY1F0TXINQKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsJNJXwa"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
  "id": -576460752303423377,
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
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
    "data": {
      "state": "tx_+NILAfiEuEBtTuB20H4xw2AyFYtH19Xwg7SlTNlcX/0ke1H9iBhYBCYdny90bTw49syGCdzEl0aI4yLKH4XhIzDjGUeFBAMHuEC9yBEBv4BDnYmZMr5jDPwGZtrDei7z/OgrFPHx4PnW8/W2EPic2FVWKLk1et2brOsTW13EBldKcHSJHJPY1IUHuEj4RjkCoQZwoL6OuD2/EyaJ+znx0R+7N+OazrLV+sS3oY1F0TXINQKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsJNJXwa"
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
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
    "data": {
      "state": "tx_+NILAfiEuEBtTuB20H4xw2AyFYtH19Xwg7SlTNlcX/0ke1H9iBhYBCYdny90bTw49syGCdzEl0aI4yLKH4XhIzDjGUeFBAMHuEC9yBEBv4BDnYmZMr5jDPwGZtrDei7z/OgrFPHx4PnW8/W2EPic2FVWKLk1et2brOsTW13EBldKcHSJHJPY1IUHuEj4RjkCoQZwoL6OuD2/EyaJ+znx0R+7N+OazrLV+sS3oY1F0TXINQKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsJNJXwa"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423376,
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
  "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
  "id": -576460752303423376,
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
  "id": -576460752303423375,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
  "id": -576460752303423375,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBtTuB20H4xw2AyFYtH19Xwg7SlTNlcX/0ke1H9iBhYBCYdny90bTw49syGCdzEl0aI4yLKH4XhIzDjGUeFBAMHuEC9yBEBv4BDnYmZMr5jDPwGZtrDei7z/OgrFPHx4PnW8/W2EPic2FVWKLk1et2brOsTW13EBldKcHSJHJPY1IUHuEj4RjkCoQZwoL6OuD2/EyaJ+znx0R+7N+OazrLV+sS3oY1F0TXINQKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsJNJXwa",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAArDvQAGg807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiX/4rKrmw"
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
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBtTuB20H4xw2AyFYtH19Xwg7SlTNlcX/0ke1H9iBhYBCYdny90bTw49syGCdzEl0aI4yLKH4XhIzDjGUeFBAMHuEC9yBEBv4BDnYmZMr5jDPwGZtrDei7z/OgrFPHx4PnW8/W2EPic2FVWKLk1et2brOsTW13EBldKcHSJHJPY1IUHuEj4RjkCoQZwoL6OuD2/EyaJ+znx0R+7N+OazrLV+sS3oY1F0TXINQKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsJNJXwa",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
    "data": {
      "event": "closing"
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
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBtTuB20H4xw2AyFYtH19Xwg7SlTNlcX/0ke1H9iBhYBCYdny90bTw49syGCdzEl0aI4yLKH4XhIzDjGUeFBAMHuEC9yBEBv4BDnYmZMr5jDPwGZtrDei7z/OgrFPHx4PnW8/W2EPic2FVWKLk1et2brOsTW13EBldKcHSJHJPY1IUHuEj4RjkCoQZwoL6OuD2/EyaJ+znx0R+7N+OazrLV+sS3oY1F0TXINQKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsJNJXwa",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
    "data": {
      "event": "closing"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423374,
  "jsonrpc": "2.0",
  "method": "channels.slash"
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
  "id": -576460752303423374,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
    "data": {
      "signed_tx": "tx_+QLDCwHAuQK9+QK6NwGhBnCgvo64Pb8TJon7OfHRH7s345rOstX6xLehjUXRNcg1oQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l7jU+NILAfiEuEBtTuB20H4xw2AyFYtH19Xwg7SlTNlcX/0ke1H9iBhYBCYdny90bTw49syGCdzEl0aI4yLKH4XhIzDjGUeFBAMHuEC9yBEBv4BDnYmZMr5jDPwGZtrDei7z/OgrFPHx4PnW8/W2EPic2FVWKLk1et2brOsTW13EBldKcHSJHJPY1IUHuEj4RjkCoQZwoL6OuD2/EyaJ+znx0R+7N+OazrLV+sS3oY1F0TXINQKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsK5AZL5AY88AfkBhfkBgqBIuiTbeL5vhSPHY5X+zOXJseAM3LqGMkK5czxVcsYFbPkBXvhPoCvsfdwTG8djghKoPa5m1PeOSWyP5O/XNfbpS5hH1m/k7aAgYzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAAvhPoC8UzXXFE4CGL9yd8T2/6ffkwtKnSTkptxq5HHERiW1Z7aAgTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4vKCgEAhj+qJSJf/vhEoEi6JNt4vm+FI8djlf7M5cmx4AzcuoYyQrlzPFVyxgVs4h+glgHe0F76KZrpqgkk5P0nuzwRHv4bam1ZFq39SUt8tRb4dKCWAd7QXvopmumqCSTk/Se7PBEe/htqbVkWrf1JS3y1FvhRgICAoC8UzXXFE4CGL9yd8T2/6ffkwtKnSTkptxq5HHERiW1ZgICAoCvsfdwTG8djghKoPa5m1PeOSWyP5O/XNfbpS5hH1m/kgICAgICAgICAwMDAwMAAhhpkvsqYAA40Orbi",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.slash_sign",
  "params": {
    "signed_tx": "tx_+QMGCwH4QrhAjDiYy9SuFgGcGdhvc1G50jjqXC8YV54BwfzqOtrGpWRt+lnh6upUKYO7N1vZicbvpFqccTCf+QbcR0sSoOpVDLkCvfkCujcBoQZwoL6OuD2/EyaJ+znx0R+7N+OazrLV+sS3oY1F0TXINaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZe41PjSCwH4hLhAbU7gdtB+McNgMhWLR9fV8IO0pUzZXF/9JHtR/YgYWAQmHZ8vdG08OPbMhgncxJdGiOMiyh+F4SMw4xlHhQQDB7hAvcgRAb+AQ52JmTK+Ywz8Bmbaw3ou8/zoKxTx8eD51vP1thD4nNhVVii5NXrdm6zrE1tdxAZXSnB0iRyT2NSFB7hI+EY5AqEGcKC+jrg9vxMmifs58dEfuzfjms6y1frEt6GNRdE1yDUCoEEI4WXODGsIq1GtA/HbemGmJSeJ+uAkxSGk1r7kMU7CuQGS+QGPPAH5AYX5AYKgSLok23i+b4Ujx2OV/szlybHgDNy6hjJCuXM8VXLGBWz5AV74T6Ar7H3cExvHY4ISqD2uZtT3jklsj+Tv1zX26UuYR9Zv5O2gIGMwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2LygoBAIYkYTnKgAL4T6AvFM11xROAhi/cnfE9v+n35MLSp0k5KbcauRxxEYltWe2gIE7wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiX/74RKBIuiTbeL5vhSPHY5X+zOXJseAM3LqGMkK5czxVcsYFbOIfoJYB3tBe+ima6aoJJOT9J7s8ER7+G2ptWRat/UlLfLUW+HSglgHe0F76KZrpqgkk5P0nuzwRHv4bam1ZFq39SUt8tRb4UYCAgKAvFM11xROAhi/cnfE9v+n35MLSp0k5KbcauRxxEYltWYCAgKAr7H3cExvHY4ISqD2uZtT3jklsj+Tv1zX26UuYR9Zv5ICAgICAgICAgMDAwMDAAIYaZL7KmAAOlG/7cw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QMGCwH4QrhAjDiYy9SuFgGcGdhvc1G50jjqXC8YV54BwfzqOtrGpWRt+lnh6upUKYO7N1vZicbvpFqccTCf+QbcR0sSoOpVDLkCvfkCujcBoQZwoL6OuD2/EyaJ+znx0R+7N+OazrLV+sS3oY1F0TXINaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZe41PjSCwH4hLhAbU7gdtB+McNgMhWLR9fV8IO0pUzZXF/9JHtR/YgYWAQmHZ8vdG08OPbMhgncxJdGiOMiyh+F4SMw4xlHhQQDB7hAvcgRAb+AQ52JmTK+Ywz8Bmbaw3ou8/zoKxTx8eD51vP1thD4nNhVVii5NXrdm6zrE1tdxAZXSnB0iRyT2NSFB7hI+EY5AqEGcKC+jrg9vxMmifs58dEfuzfjms6y1frEt6GNRdE1yDUCoEEI4WXODGsIq1GtA/HbemGmJSeJ+uAkxSGk1r7kMU7CuQGS+QGPPAH5AYX5AYKgSLok23i+b4Ujx2OV/szlybHgDNy6hjJCuXM8VXLGBWz5AV74T6Ar7H3cExvHY4ISqD2uZtT3jklsj+Tv1zX26UuYR9Zv5O2gIGMwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2LygoBAIYkYTnKgAL4T6AvFM11xROAhi/cnfE9v+n35MLSp0k5KbcauRxxEYltWe2gIE7wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiX/74RKBIuiTbeL5vhSPHY5X+zOXJseAM3LqGMkK5czxVcsYFbOIfoJYB3tBe+ima6aoJJOT9J7s8ER7+G2ptWRat/UlLfLUW+HSglgHe0F76KZrpqgkk5P0nuzwRHv4bam1ZFq39SUt8tRb4UYCAgKAvFM11xROAhi/cnfE9v+n35MLSp0k5KbcauRxxEYltWYCAgKAr7H3cExvHY4ISqD2uZtT3jklsj+Tv1zX26UuYR9Zv5ICAgICAgICAgMDAwMDAAIYaZL7KmAAOlG/7cw==",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QMGCwH4QrhAjDiYy9SuFgGcGdhvc1G50jjqXC8YV54BwfzqOtrGpWRt+lnh6upUKYO7N1vZicbvpFqccTCf+QbcR0sSoOpVDLkCvfkCujcBoQZwoL6OuD2/EyaJ+znx0R+7N+OazrLV+sS3oY1F0TXINaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZe41PjSCwH4hLhAbU7gdtB+McNgMhWLR9fV8IO0pUzZXF/9JHtR/YgYWAQmHZ8vdG08OPbMhgncxJdGiOMiyh+F4SMw4xlHhQQDB7hAvcgRAb+AQ52JmTK+Ywz8Bmbaw3ou8/zoKxTx8eD51vP1thD4nNhVVii5NXrdm6zrE1tdxAZXSnB0iRyT2NSFB7hI+EY5AqEGcKC+jrg9vxMmifs58dEfuzfjms6y1frEt6GNRdE1yDUCoEEI4WXODGsIq1GtA/HbemGmJSeJ+uAkxSGk1r7kMU7CuQGS+QGPPAH5AYX5AYKgSLok23i+b4Ujx2OV/szlybHgDNy6hjJCuXM8VXLGBWz5AV74T6Ar7H3cExvHY4ISqD2uZtT3jklsj+Tv1zX26UuYR9Zv5O2gIGMwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2LygoBAIYkYTnKgAL4T6AvFM11xROAhi/cnfE9v+n35MLSp0k5KbcauRxxEYltWe2gIE7wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiX/74RKBIuiTbeL5vhSPHY5X+zOXJseAM3LqGMkK5czxVcsYFbOIfoJYB3tBe+ima6aoJJOT9J7s8ER7+G2ptWRat/UlLfLUW+HSglgHe0F76KZrpqgkk5P0nuzwRHv4bam1ZFq39SUt8tRb4UYCAgKAvFM11xROAhi/cnfE9v+n35MLSp0k5KbcauRxxEYltWYCAgKAr7H3cExvHY4ISqD2uZtT3jklsj+Tv1zX26UuYR9Zv5ICAgICAgICAgMDAwMDAAIYaZL7KmAAOlG/7cw==",
      "type": "channel_slash_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBnCgvo64Pb8TJon7OfHRH7s345rOstX6xLehjUXRNcg1oQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYY/qiUiX/6GJGE5yoACAIYPXtZ/KAAE9WwQ7g==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423373,
  "jsonrpc": "2.0",
  "method": "channels.settle_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEB2lexaTgEKNbCznZuVrSmBgO3zUCO4OIE5/wpVYOPNAXCJ8FEEkns1QINHm47YuP83N14pAMuWpu91mvozg74DuF/4XTgBoQZwoL6OuD2/EyaJ+znx0R+7N+OazrLV+sS3oY1F0TXINaEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GP6olIl/+hiRhOcqAAgCGD17WfygABC19oZk="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
  "id": -576460752303423373,
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
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEB2lexaTgEKNbCznZuVrSmBgO3zUCO4OIE5/wpVYOPNAXCJ8FEEkns1QINHm47YuP83N14pAMuWpu91mvozg74DuF/4XTgBoQZwoL6OuD2/EyaJ+znx0R+7N+OazrLV+sS3oY1F0TXINaEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GP6olIl/+hiRhOcqAAgCGD17WfygABC19oZk=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEB2lexaTgEKNbCznZuVrSmBgO3zUCO4OIE5/wpVYOPNAXCJ8FEEkns1QINHm47YuP83N14pAMuWpu91mvozg74DuF/4XTgBoQZwoL6OuD2/EyaJ+znx0R+7N+OazrLV+sS3oY1F0TXINaEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GP6olIl/+hiRhOcqAAgCGD17WfygABC19oZk=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
    "data": {
      "event": "closed_confirmed"
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
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
    "data": {
      "event": "closed_confirmed"
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
    "channel_id": "ch_rbvsH7jnyYxy3z4FGf3HaybR9CeMgA5LVZVfcQd4iy4E1QL85",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_slash_%2F2618%5Binitiator44responder%5D
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_slash_%2F2618%5Binitiator44responder%5D
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAfNO8EGVVRoKbq3Lxj2WY6ZR+xj2jcGlcIhNerfki3mXhj+qJSJgAKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GJGE5yoAAAgoAhhAGeddIAMCgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0PI737pQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423372,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBibvPSvkPg26xe+4Vf7bxFQgourtWXGBBVXskw+1CC4bdYRPJF3mNQal7Si0FVK4I2hW464HEUSP4RP4Bot7oLuIP4gTIBoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y/qiUiYAChAfdjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNhiRhOcqAAAIKAIYQBnnXSADAoDXj090A/DMnCedVe1N9Z8lFvhGFs8xqY89cVUV0esLtD3c5ojI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423372,
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
      "signed_tx": "tx_+MsLAfhCuEBibvPSvkPg26xe+4Vf7bxFQgourtWXGBBVXskw+1CC4bdYRPJF3mNQal7Si0FVK4I2hW464HEUSP4RP4Bot7oLuIP4gTIBoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y/qiUiYAChAfdjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNhiRhOcqAAAIKAIYQBnnXSADAoDXj090A/DMnCedVe1N9Z8lFvhGFs8xqY89cVUV0esLtD3c5ojI=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423371,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAYm7z0r5D4NusXvuFX+28RUIKLq7VlxgQVV7JMPtQguG3WETyRd5jUGpe0otBVSuCNoVuOuBxFEj+ET+AaLe6C7hAawMkoNUdxV9n2o7c3Bu7U36BiytgI0IBAOd4JPUt891kslhascdaj+aWE2gseeLGS0DFJaFu8d+3Fz8YwArLALiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7Q854YWW"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423371,
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
      "tx": "tx_+QENCwH4hLhAYm7z0r5D4NusXvuFX+28RUIKLq7VlxgQVV7JMPtQguG3WETyRd5jUGpe0otBVSuCNoVuOuBxFEj+ET+AaLe6C7hAawMkoNUdxV9n2o7c3Bu7U36BiytgI0IBAOd4JPUt891kslhascdaj+aWE2gseeLGS0DFJaFu8d+3Fz8YwArLALiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7Q854YWW",
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
      "tx": "tx_+QENCwH4hLhAYm7z0r5D4NusXvuFX+28RUIKLq7VlxgQVV7JMPtQguG3WETyRd5jUGpe0otBVSuCNoVuOuBxFEj+ET+AaLe6C7hAawMkoNUdxV9n2o7c3Bu7U36BiytgI0IBAOd4JPUt891kslhascdaj+aWE2gseeLGS0DFJaFu8d+3Fz8YwArLALiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7Q854YWW",
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
      "tx": "tx_+QENCwH4hLhAYm7z0r5D4NusXvuFX+28RUIKLq7VlxgQVV7JMPtQguG3WETyRd5jUGpe0otBVSuCNoVuOuBxFEj+ET+AaLe6C7hAawMkoNUdxV9n2o7c3Bu7U36BiytgI0IBAOd4JPUt891kslhascdaj+aWE2gseeLGS0DFJaFu8d+3Fz8YwArLALiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7Q854YWW",
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
      "tx": "tx_+QENCwH4hLhAYm7z0r5D4NusXvuFX+28RUIKLq7VlxgQVV7JMPtQguG3WETyRd5jUGpe0otBVSuCNoVuOuBxFEj+ET+AaLe6C7hAawMkoNUdxV9n2o7c3Bu7U36BiytgI0IBAOd4JPUt891kslhascdaj+aWE2gseeLGS0DFJaFu8d+3Fz8YwArLALiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7Q854YWW",
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
    "data": {
      "message": {
        "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
    "data": {
      "message": {
        "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
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
  "id": -576460752303423370,
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
  "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
  "id": -576460752303423370,
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
    "data": {
      "state": "tx_+QENCwH4hLhAYm7z0r5D4NusXvuFX+28RUIKLq7VlxgQVV7JMPtQguG3WETyRd5jUGpe0otBVSuCNoVuOuBxFEj+ET+AaLe6C7hAawMkoNUdxV9n2o7c3Bu7U36BiytgI0IBAOd4JPUt891kslhascdaj+aWE2gseeLGS0DFJaFu8d+3Fz8YwArLALiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7Q854YWW"
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
    "data": {
      "state": "tx_+QENCwH4hLhAYm7z0r5D4NusXvuFX+28RUIKLq7VlxgQVV7JMPtQguG3WETyRd5jUGpe0otBVSuCNoVuOuBxFEj+ET+AaLe6C7hAawMkoNUdxV9n2o7c3Bu7U36BiytgI0IBAOd4JPUt891kslhascdaj+aWE2gseeLGS0DFJaFu8d+3Fz8YwArLALiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7Q854YWW"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
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
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
    "data": {
      "poi": "pi_+QGPPAH5AYX5AYKgzjPoxvF7i0Rogt3HkCECEP488lCJfxH/pjhMnAW0H175AV74dKBCtP1Hq2qT20MxrCfa6+4NtpcN4yYiF5Q49PWrKoAeWvhRgICAoF3LDUbbHv4PQYhz+7hhcxvJKCVkvdvZcT7v3lpcdhJogICAoOyT7A0xMr4xEpU8GaLKmoEzVli5CVJmhhDFgSb84h88gICAgICAgICA+E+gXcsNRtse/g9BiHP7uGFzG8koJWS929lxPu/eWlx2EmjtoCBO8EGVVRoKbq3Lxj2WY6ZR+xj2jcGlcIhNerfki3mXi8oKAQCGP6olIl//+ESgzjPoxvF7i0Rogt3HkCECEP488lCJfxH/pjhMnAW0H17iH6BCtP1Hq2qT20MxrCfa6+4NtpcN4yYiF5Q49PWrKoAeWvhPoOyT7A0xMr4xEpU8GaLKmoEzVli5CVJmhhDFgSb84h887aAgYzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAAcDAwMDAZfj5+A=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423369,
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
  "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
  "id": -576460752303423369,
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiY0EU5gnY6Q8TP9UEcehQxnRER+FxUwhGP41VO1yUqkAqBBCOFlzgxrCKtRrQPx23phpiUnifrgJMUhpNa+5DFOwgV8+d4=",
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
  "id": -576460752303423368,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA6toTDHcgKgSKJ+KsEXafYmRDlHzEZg/hyuYFS1mIA4ZLzuOEtB2DrrhoWYcJ7KrTehGiorXtF+XIH6CLFjpEMuEj4RjkCoQYmNBFOYJ2OkPEz/VBHHoUMZ0REfhcVMIRj+NVTtclKpAKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsKjaWfk"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
  "id": -576460752303423368,
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA6toTDHcgKgSKJ+KsEXafYmRDlHzEZg/hyuYFS1mIA4ZLzuOEtB2DrrhoWYcJ7KrTehGiorXtF+XIH6CLFjpEMuEj4RjkCoQYmNBFOYJ2OkPEz/VBHHoUMZ0REfhcVMIRj+NVTtclKpAKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsKjaWfk",
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
  "id": -576460752303423367,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA6toTDHcgKgSKJ+KsEXafYmRDlHzEZg/hyuYFS1mIA4ZLzuOEtB2DrrhoWYcJ7KrTehGiorXtF+XIH6CLFjpEMuEC9zDGVlR2A+o0TobL3R9ygpXuFLhg3L918gR2XLLyMzLXC27rJXD2Dx8q2uH5jJJ4cAlDwHPJWCqUBRhH5KfkOuEj4RjkCoQYmNBFOYJ2OkPEz/VBHHoUMZ0REfhcVMIRj+NVTtclKpAKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsJuShY/"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
  "id": -576460752303423367,
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
    "data": {
      "state": "tx_+NILAfiEuEA6toTDHcgKgSKJ+KsEXafYmRDlHzEZg/hyuYFS1mIA4ZLzuOEtB2DrrhoWYcJ7KrTehGiorXtF+XIH6CLFjpEMuEC9zDGVlR2A+o0TobL3R9ygpXuFLhg3L918gR2XLLyMzLXC27rJXD2Dx8q2uH5jJJ4cAlDwHPJWCqUBRhH5KfkOuEj4RjkCoQYmNBFOYJ2OkPEz/VBHHoUMZ0REfhcVMIRj+NVTtclKpAKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsJuShY/"
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
    "data": {
      "state": "tx_+NILAfiEuEA6toTDHcgKgSKJ+KsEXafYmRDlHzEZg/hyuYFS1mIA4ZLzuOEtB2DrrhoWYcJ7KrTehGiorXtF+XIH6CLFjpEMuEC9zDGVlR2A+o0TobL3R9ygpXuFLhg3L918gR2XLLyMzLXC27rJXD2Dx8q2uH5jJJ4cAlDwHPJWCqUBRhH5KfkOuEj4RjkCoQYmNBFOYJ2OkPEz/VBHHoUMZ0REfhcVMIRj+NVTtclKpAKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsJuShY/"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423366,
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
  "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
  "id": -576460752303423366,
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
  "id": -576460752303423365,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
  "id": -576460752303423365,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA6toTDHcgKgSKJ+KsEXafYmRDlHzEZg/hyuYFS1mIA4ZLzuOEtB2DrrhoWYcJ7KrTehGiorXtF+XIH6CLFjpEMuEC9zDGVlR2A+o0TobL3R9ygpXuFLhg3L918gR2XLLyMzLXC27rJXD2Dx8q2uH5jJJ4cAlDwHPJWCqUBRhH5KfkOuEj4RjkCoQYmNBFOYJ2OkPEz/VBHHoUMZ0REfhcVMIRj+NVTtclKpAKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsJuShY/",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAArDvQAGg807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiX/4rKrmw"
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEA6toTDHcgKgSKJ+KsEXafYmRDlHzEZg/hyuYFS1mIA4ZLzuOEtB2DrrhoWYcJ7KrTehGiorXtF+XIH6CLFjpEMuEC9zDGVlR2A+o0TobL3R9ygpXuFLhg3L918gR2XLLyMzLXC27rJXD2Dx8q2uH5jJJ4cAlDwHPJWCqUBRhH5KfkOuEj4RjkCoQYmNBFOYJ2OkPEz/VBHHoUMZ0REfhcVMIRj+NVTtclKpAKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsJuShY/",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
    "data": {
      "event": "closing"
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEA6toTDHcgKgSKJ+KsEXafYmRDlHzEZg/hyuYFS1mIA4ZLzuOEtB2DrrhoWYcJ7KrTehGiorXtF+XIH6CLFjpEMuEC9zDGVlR2A+o0TobL3R9ygpXuFLhg3L918gR2XLLyMzLXC27rJXD2Dx8q2uH5jJJ4cAlDwHPJWCqUBRhH5KfkOuEj4RjkCoQYmNBFOYJ2OkPEz/VBHHoUMZ0REfhcVMIRj+NVTtclKpAKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsJuShY/",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
    "data": {
      "event": "closing"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423364,
  "jsonrpc": "2.0",
  "method": "channels.slash"
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
  "id": -576460752303423364,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
    "data": {
      "signed_tx": "tx_+QLDCwHAuQK9+QK6NwGhBiY0EU5gnY6Q8TP9UEcehQxnRER+FxUwhGP41VO1yUqkoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTbjU+NILAfiEuEA6toTDHcgKgSKJ+KsEXafYmRDlHzEZg/hyuYFS1mIA4ZLzuOEtB2DrrhoWYcJ7KrTehGiorXtF+XIH6CLFjpEMuEC9zDGVlR2A+o0TobL3R9ygpXuFLhg3L918gR2XLLyMzLXC27rJXD2Dx8q2uH5jJJ4cAlDwHPJWCqUBRhH5KfkOuEj4RjkCoQYmNBFOYJ2OkPEz/VBHHoUMZ0REfhcVMIRj+NVTtclKpAKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsK5AZL5AY88AfkBhfkBgqBIuiTbeL5vhSPHY5X+zOXJseAM3LqGMkK5czxVcsYFbPkBXvhPoCvsfdwTG8djghKoPa5m1PeOSWyP5O/XNfbpS5hH1m/k7aAgYzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAAvhPoC8UzXXFE4CGL9yd8T2/6ffkwtKnSTkptxq5HHERiW1Z7aAgTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4vKCgEAhj+qJSJf/vhEoEi6JNt4vm+FI8djlf7M5cmx4AzcuoYyQrlzPFVyxgVs4h+glgHe0F76KZrpqgkk5P0nuzwRHv4bam1ZFq39SUt8tRb4dKCWAd7QXvopmumqCSTk/Se7PBEe/htqbVkWrf1JS3y1FvhRgICAoC8UzXXFE4CGL9yd8T2/6ffkwtKnSTkptxq5HHERiW1ZgICAoCvsfdwTG8djghKoPa5m1PeOSWyP5O/XNfbpS5hH1m/kgICAgICAgICAwMDAwMAAhhpkvsqYAAV/PuAs",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.slash_sign",
  "params": {
    "signed_tx": "tx_+QMGCwH4QrhArv7KQQYi1m0S5+DUE0UZa+l9gN2WGJl4TK3zGQ5SAgS3zJpAf/E6JUOxpmxak7yG9V0MyhH7Qv4FJ5kxyV3aA7kCvfkCujcBoQYmNBFOYJ2OkPEz/VBHHoUMZ0REfhcVMIRj+NVTtclKpKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE241PjSCwH4hLhAOraEwx3ICoEiifirBF2n2JkQ5R8xGYP4crmBUtZiAOGS87jhLQdg664aFmHCeyq03oRoqK17RflyB+gixY6RDLhAvcwxlZUdgPqNE6Gy90fcoKV7hS4YNy/dfIEdlyy8jMy1wtu6yVw9g8fKtrh+YySeHAJQ8BzyVgqlAUYR+Sn5DrhI+EY5AqEGJjQRTmCdjpDxM/1QRx6FDGdERH4XFTCEY/jVU7XJSqQCoEEI4WXODGsIq1GtA/HbemGmJSeJ+uAkxSGk1r7kMU7CuQGS+QGPPAH5AYX5AYKgSLok23i+b4Ujx2OV/szlybHgDNy6hjJCuXM8VXLGBWz5AV74T6Ar7H3cExvHY4ISqD2uZtT3jklsj+Tv1zX26UuYR9Zv5O2gIGMwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2LygoBAIYkYTnKgAL4T6AvFM11xROAhi/cnfE9v+n35MLSp0k5KbcauRxxEYltWe2gIE7wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiX/74RKBIuiTbeL5vhSPHY5X+zOXJseAM3LqGMkK5czxVcsYFbOIfoJYB3tBe+ima6aoJJOT9J7s8ER7+G2ptWRat/UlLfLUW+HSglgHe0F76KZrpqgkk5P0nuzwRHv4bam1ZFq39SUt8tRb4UYCAgKAvFM11xROAhi/cnfE9v+n35MLSp0k5KbcauRxxEYltWYCAgKAr7H3cExvHY4ISqD2uZtT3jklsj+Tv1zX26UuYR9Zv5ICAgICAgICAgMDAwMDAAIYaZL7KmAAFc80l+Q=="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QMGCwH4QrhArv7KQQYi1m0S5+DUE0UZa+l9gN2WGJl4TK3zGQ5SAgS3zJpAf/E6JUOxpmxak7yG9V0MyhH7Qv4FJ5kxyV3aA7kCvfkCujcBoQYmNBFOYJ2OkPEz/VBHHoUMZ0REfhcVMIRj+NVTtclKpKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE241PjSCwH4hLhAOraEwx3ICoEiifirBF2n2JkQ5R8xGYP4crmBUtZiAOGS87jhLQdg664aFmHCeyq03oRoqK17RflyB+gixY6RDLhAvcwxlZUdgPqNE6Gy90fcoKV7hS4YNy/dfIEdlyy8jMy1wtu6yVw9g8fKtrh+YySeHAJQ8BzyVgqlAUYR+Sn5DrhI+EY5AqEGJjQRTmCdjpDxM/1QRx6FDGdERH4XFTCEY/jVU7XJSqQCoEEI4WXODGsIq1GtA/HbemGmJSeJ+uAkxSGk1r7kMU7CuQGS+QGPPAH5AYX5AYKgSLok23i+b4Ujx2OV/szlybHgDNy6hjJCuXM8VXLGBWz5AV74T6Ar7H3cExvHY4ISqD2uZtT3jklsj+Tv1zX26UuYR9Zv5O2gIGMwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2LygoBAIYkYTnKgAL4T6AvFM11xROAhi/cnfE9v+n35MLSp0k5KbcauRxxEYltWe2gIE7wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiX/74RKBIuiTbeL5vhSPHY5X+zOXJseAM3LqGMkK5czxVcsYFbOIfoJYB3tBe+ima6aoJJOT9J7s8ER7+G2ptWRat/UlLfLUW+HSglgHe0F76KZrpqgkk5P0nuzwRHv4bam1ZFq39SUt8tRb4UYCAgKAvFM11xROAhi/cnfE9v+n35MLSp0k5KbcauRxxEYltWYCAgKAr7H3cExvHY4ISqD2uZtT3jklsj+Tv1zX26UuYR9Zv5ICAgICAgICAgMDAwMDAAIYaZL7KmAAFc80l+Q==",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QMGCwH4QrhArv7KQQYi1m0S5+DUE0UZa+l9gN2WGJl4TK3zGQ5SAgS3zJpAf/E6JUOxpmxak7yG9V0MyhH7Qv4FJ5kxyV3aA7kCvfkCujcBoQYmNBFOYJ2OkPEz/VBHHoUMZ0REfhcVMIRj+NVTtclKpKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE241PjSCwH4hLhAOraEwx3ICoEiifirBF2n2JkQ5R8xGYP4crmBUtZiAOGS87jhLQdg664aFmHCeyq03oRoqK17RflyB+gixY6RDLhAvcwxlZUdgPqNE6Gy90fcoKV7hS4YNy/dfIEdlyy8jMy1wtu6yVw9g8fKtrh+YySeHAJQ8BzyVgqlAUYR+Sn5DrhI+EY5AqEGJjQRTmCdjpDxM/1QRx6FDGdERH4XFTCEY/jVU7XJSqQCoEEI4WXODGsIq1GtA/HbemGmJSeJ+uAkxSGk1r7kMU7CuQGS+QGPPAH5AYX5AYKgSLok23i+b4Ujx2OV/szlybHgDNy6hjJCuXM8VXLGBWz5AV74T6Ar7H3cExvHY4ISqD2uZtT3jklsj+Tv1zX26UuYR9Zv5O2gIGMwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2LygoBAIYkYTnKgAL4T6AvFM11xROAhi/cnfE9v+n35MLSp0k5KbcauRxxEYltWe2gIE7wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiX/74RKBIuiTbeL5vhSPHY5X+zOXJseAM3LqGMkK5czxVcsYFbOIfoJYB3tBe+ima6aoJJOT9J7s8ER7+G2ptWRat/UlLfLUW+HSglgHe0F76KZrpqgkk5P0nuzwRHv4bam1ZFq39SUt8tRb4UYCAgKAvFM11xROAhi/cnfE9v+n35MLSp0k5KbcauRxxEYltWYCAgKAr7H3cExvHY4ISqD2uZtT3jklsj+Tv1zX26UuYR9Zv5ICAgICAgICAgMDAwMDAAIYaZL7KmAAFc80l+Q==",
      "type": "channel_slash_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBiY0EU5gnY6Q8TP9UEcehQxnRER+FxUwhGP41VO1yUqkoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYY/qiUiX/6GJGE5yoACAIYPXtZ/KAAGekflpQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423363,
  "jsonrpc": "2.0",
  "method": "channels.settle_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuECFSasF8lMnvHllA3pgmeo1Thlf1EJaRog9h0UTEtTv4b7fbzNbuVLWa9iqCyLwVKgs4YU5eRFGVaGal9Et4OUKuF/4XTgBoQYmNBFOYJ2OkPEz/VBHHoUMZ0REfhcVMIRj+NVTtclKpKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GP6olIl/+hiRhOcqAAgCGD17WfygABqCk+to="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
  "id": -576460752303423363,
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECFSasF8lMnvHllA3pgmeo1Thlf1EJaRog9h0UTEtTv4b7fbzNbuVLWa9iqCyLwVKgs4YU5eRFGVaGal9Et4OUKuF/4XTgBoQYmNBFOYJ2OkPEz/VBHHoUMZ0REfhcVMIRj+NVTtclKpKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GP6olIl/+hiRhOcqAAgCGD17WfygABqCk+to=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECFSasF8lMnvHllA3pgmeo1Thlf1EJaRog9h0UTEtTv4b7fbzNbuVLWa9iqCyLwVKgs4YU5eRFGVaGal9Et4OUKuF/4XTgBoQYmNBFOYJ2OkPEz/VBHHoUMZ0REfhcVMIRj+NVTtclKpKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GP6olIl/+hiRhOcqAAgCGD17WfygABqCk+to=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
    "data": {
      "event": "closed_confirmed"
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
    "data": {
      "event": "closed_confirmed"
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
    "channel_id": "ch_HprYs5JWSc4PEdzKjp452XZjEAfyxe8kwSVwDRnbEBAFGn9Nb",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```
