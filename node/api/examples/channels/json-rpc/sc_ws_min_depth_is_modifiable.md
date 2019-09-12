
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR&lock_period=10&minimum_depth=3&minimum_depth_factor=1&&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT&role=initiator
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR&lock_period=10&minimum_depth=3&minimum_depth_factor=1&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT&role=responder
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAfNO8EGVVRoKbq3Lxj2WY6ZR+xj2jcGlcIhNerfki3mXhj+qJSJgAKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GJGE5yoAAAgoAhhAGeddIAMCgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0CW7SpLQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423486,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBTLVIa66rah9XroI6C7XqxW9tLuzZahUXThdjF0S25WjHNduY0te9ES+wE+XdT5shF8Hgq600lE5R84uiZoB0PuIP4gTIBoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y/qiUiYAChAfdjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNhiRhOcqAAAIKAIYQBnnXSADAoDXj090A/DMnCedVe1N9Z8lFvhGFs8xqY89cVUV0esLtAu00914="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423486,
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
      "signed_tx": "tx_+MsLAfhCuEBTLVIa66rah9XroI6C7XqxW9tLuzZahUXThdjF0S25WjHNduY0te9ES+wE+XdT5shF8Hgq600lE5R84uiZoB0PuIP4gTIBoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y/qiUiYAChAfdjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNhiRhOcqAAAIKAIYQBnnXSADAoDXj090A/DMnCedVe1N9Z8lFvhGFs8xqY89cVUV0esLtAu00914=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423485,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhASd1Nq7my5Ouge5mHoAvP7la7Bubc8rY4WEvu7dVxxhIBvqc7B7N9i/uxIvWn5EHRsl2r7S60Y3sCEzqK0TWfCrhAUy1SGuuq2ofV66COgu16sVvbS7s2WoVF04XYxdEtuVoxzXbmNLXvREvsBPl3U+bIRfB4KutNJROUfOLomaAdD7iD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QJ49Yrg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423485,
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
      "tx": "tx_+QENCwH4hLhASd1Nq7my5Ouge5mHoAvP7la7Bubc8rY4WEvu7dVxxhIBvqc7B7N9i/uxIvWn5EHRsl2r7S60Y3sCEzqK0TWfCrhAUy1SGuuq2ofV66COgu16sVvbS7s2WoVF04XYxdEtuVoxzXbmNLXvREvsBPl3U+bIRfB4KutNJROUfOLomaAdD7iD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QJ49Yrg",
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
      "tx": "tx_+QENCwH4hLhASd1Nq7my5Ouge5mHoAvP7la7Bubc8rY4WEvu7dVxxhIBvqc7B7N9i/uxIvWn5EHRsl2r7S60Y3sCEzqK0TWfCrhAUy1SGuuq2ofV66COgu16sVvbS7s2WoVF04XYxdEtuVoxzXbmNLXvREvsBPl3U+bIRfB4KutNJROUfOLomaAdD7iD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QJ49Yrg",
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
      "tx": "tx_+QENCwH4hLhASd1Nq7my5Ouge5mHoAvP7la7Bubc8rY4WEvu7dVxxhIBvqc7B7N9i/uxIvWn5EHRsl2r7S60Y3sCEzqK0TWfCrhAUy1SGuuq2ofV66COgu16sVvbS7s2WoVF04XYxdEtuVoxzXbmNLXvREvsBPl3U+bIRfB4KutNJROUfOLomaAdD7iD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QJ49Yrg",
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
      "tx": "tx_+QENCwH4hLhASd1Nq7my5Ouge5mHoAvP7la7Bubc8rY4WEvu7dVxxhIBvqc7B7N9i/uxIvWn5EHRsl2r7S60Y3sCEzqK0TWfCrhAUy1SGuuq2ofV66COgu16sVvbS7s2WoVF04XYxdEtuVoxzXbmNLXvREvsBPl3U+bIRfB4KutNJROUfOLomaAdD7iD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QJ49Yrg",
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "message": {
        "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "message": {
        "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
  "id": -576460752303423484,
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423484,
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "state": "tx_+QENCwH4hLhASd1Nq7my5Ouge5mHoAvP7la7Bubc8rY4WEvu7dVxxhIBvqc7B7N9i/uxIvWn5EHRsl2r7S60Y3sCEzqK0TWfCrhAUy1SGuuq2ofV66COgu16sVvbS7s2WoVF04XYxdEtuVoxzXbmNLXvREvsBPl3U+bIRfB4KutNJROUfOLomaAdD7iD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QJ49Yrg"
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "state": "tx_+QENCwH4hLhASd1Nq7my5Ouge5mHoAvP7la7Bubc8rY4WEvu7dVxxhIBvqc7B7N9i/uxIvWn5EHRsl2r7S60Y3sCEzqK0TWfCrhAUy1SGuuq2ofV66COgu16sVvbS7s2WoVF04XYxdEtuVoxzXbmNLXvREvsBPl3U+bIRfB4KutNJROUfOLomaAdD7iD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QJ49Yrg"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423483,
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423483,
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBn3XHhwdN+q1EM63Q9MvSk/kE8T+Cc6L7mkJf7zYwISMAqBBCOFlzgxrCKtRrQPx23phpiUnifrgJMUhpNa+5DFOwlmK/sA=",
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
  "id": -576460752303423482,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDlOdSVLC7LyL8PBtM5A6ue/qQ1+N6lxWkSddAJ48rAoTQ70pUDPmALA8RKgLen3Va1kh4IpNW5IL6UGQkrZGsDuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsKjrNkd"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423482,
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDlOdSVLC7LyL8PBtM5A6ue/qQ1+N6lxWkSddAJ48rAoTQ70pUDPmALA8RKgLen3Va1kh4IpNW5IL6UGQkrZGsDuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsKjrNkd",
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
  "id": -576460752303423481,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEC9o1PtFI44vw0tLLURwZXtNnoTTNR5g+V/W+w5B5zcpnYYbDR7qqvMb/2V2XFQNl1HBHOtAajTymgFYLAzsncJuEDlOdSVLC7LyL8PBtM5A6ue/qQ1+N6lxWkSddAJ48rAoTQ70pUDPmALA8RKgLen3Va1kh4IpNW5IL6UGQkrZGsDuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsIT7I+H"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423481,
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "state": "tx_+NILAfiEuEC9o1PtFI44vw0tLLURwZXtNnoTTNR5g+V/W+w5B5zcpnYYbDR7qqvMb/2V2XFQNl1HBHOtAajTymgFYLAzsncJuEDlOdSVLC7LyL8PBtM5A6ue/qQ1+N6lxWkSddAJ48rAoTQ70pUDPmALA8RKgLen3Va1kh4IpNW5IL6UGQkrZGsDuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsIT7I+H"
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "state": "tx_+NILAfiEuEC9o1PtFI44vw0tLLURwZXtNnoTTNR5g+V/W+w5B5zcpnYYbDR7qqvMb/2V2XFQNl1HBHOtAajTymgFYLAzsncJuEDlOdSVLC7LyL8PBtM5A6ue/qQ1+N6lxWkSddAJ48rAoTQ70pUDPmALA8RKgLen3Va1kh4IpNW5IL6UGQkrZGsDuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsIT7I+H"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423480,
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423480,
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
  "id": -576460752303423479,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423479,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEC9o1PtFI44vw0tLLURwZXtNnoTTNR5g+V/W+w5B5zcpnYYbDR7qqvMb/2V2XFQNl1HBHOtAajTymgFYLAzsncJuEDlOdSVLC7LyL8PBtM5A6ue/qQ1+N6lxWkSddAJ48rAoTQ70pUDPmALA8RKgLen3Va1kh4IpNW5IL6UGQkrZGsDuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAKgQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsIT7I+H",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAArDvQAGg807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiX/4rKrmw"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423478,
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423478,
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBn3XHhwdN+q1EM63Q9MvSk/kE8T+Cc6L7mkJf7zYwISMA6A149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7Z2J+9o=",
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
  "id": -576460752303423477,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECVWvtlZxh3xHXI7bRJ1ah+4139qua/0vIA8gAhK/1osiYlL8mE1RVKB6ydlmsifamUL81WdDhykNASuJyJH6UIuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu2OdNOt"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423477,
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "signed_tx": "tx_+JALAfhCuECVWvtlZxh3xHXI7bRJ1ah+4139qua/0vIA8gAhK/1osiYlL8mE1RVKB6ydlmsifamUL81WdDhykNASuJyJH6UIuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu2OdNOt",
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
  "id": -576460752303423476,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECVWvtlZxh3xHXI7bRJ1ah+4139qua/0vIA8gAhK/1osiYlL8mE1RVKB6ydlmsifamUL81WdDhykNASuJyJH6UIuEDdhOBTtoeRkMSdu3cK0vM/2FQG4823RImrZCrJzLwBInpLwRCHpoTVtdQJyohbmNtiyieo0ie9nAHo1mPqABUAuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu1i4Muj"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423476,
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "state": "tx_+NILAfiEuECVWvtlZxh3xHXI7bRJ1ah+4139qua/0vIA8gAhK/1osiYlL8mE1RVKB6ydlmsifamUL81WdDhykNASuJyJH6UIuEDdhOBTtoeRkMSdu3cK0vM/2FQG4823RImrZCrJzLwBInpLwRCHpoTVtdQJyohbmNtiyieo0ie9nAHo1mPqABUAuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu1i4Muj"
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "state": "tx_+NILAfiEuECVWvtlZxh3xHXI7bRJ1ah+4139qua/0vIA8gAhK/1osiYlL8mE1RVKB6ydlmsifamUL81WdDhykNASuJyJH6UIuEDdhOBTtoeRkMSdu3cK0vM/2FQG4823RImrZCrJzLwBInpLwRCHpoTVtdQJyohbmNtiyieo0ie9nAHo1mPqABUAuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu1i4Muj"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423475,
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423475,
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
  "id": -576460752303423474,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423474,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECVWvtlZxh3xHXI7bRJ1ah+4139qua/0vIA8gAhK/1osiYlL8mE1RVKB6ydlmsifamUL81WdDhykNASuJyJH6UIuEDdhOBTtoeRkMSdu3cK0vM/2FQG4823RImrZCrJzLwBInpLwRCHpoTVtdQJyohbmNtiyieo0ie9nAHo1mPqABUAuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAOgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu1i4Muj",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAAbDvQAGg807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiX/+PWk/e"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423473,
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423473,
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBn3XHhwdN+q1EM63Q9MvSk/kE8T+Cc6L7mkJf7zYwISMBKBD48upGMSQmUHkvAbXk8OLPb+iXSg8kxqzNfUkPoVMWasBiAU=",
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
  "id": -576460752303423472,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEARHUtL7aaZrz85GG6DcEsrs8FTvDfB1Ju5DSgrEGP4Gx456IQwhB1Paz3U0ncHiGg6pms0cot7XUXAhXRgJJYPuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjASgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFn6WHAa"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423472,
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEARHUtL7aaZrz85GG6DcEsrs8FTvDfB1Ju5DSgrEGP4Gx456IQwhB1Paz3U0ncHiGg6pms0cot7XUXAhXRgJJYPuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjASgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFn6WHAa",
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
  "id": -576460752303423471,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEARHUtL7aaZrz85GG6DcEsrs8FTvDfB1Ju5DSgrEGP4Gx456IQwhB1Paz3U0ncHiGg6pms0cot7XUXAhXRgJJYPuED9VSZstqMd4rban5igrYjntUQxcy8lfgHyXpXaTXQg6RM+iOevIrL8sC5N5YDb4Ug8iADVlrDMKZ7n8CEfkzYKuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjASgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFkZSkYg"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423471,
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "state": "tx_+NILAfiEuEARHUtL7aaZrz85GG6DcEsrs8FTvDfB1Ju5DSgrEGP4Gx456IQwhB1Paz3U0ncHiGg6pms0cot7XUXAhXRgJJYPuED9VSZstqMd4rban5igrYjntUQxcy8lfgHyXpXaTXQg6RM+iOevIrL8sC5N5YDb4Ug8iADVlrDMKZ7n8CEfkzYKuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjASgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFkZSkYg"
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "state": "tx_+NILAfiEuEARHUtL7aaZrz85GG6DcEsrs8FTvDfB1Ju5DSgrEGP4Gx456IQwhB1Paz3U0ncHiGg6pms0cot7XUXAhXRgJJYPuED9VSZstqMd4rban5igrYjntUQxcy8lfgHyXpXaTXQg6RM+iOevIrL8sC5N5YDb4Ug8iADVlrDMKZ7n8CEfkzYKuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjASgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFkZSkYg"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423470,
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423470,
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
  "id": -576460752303423469,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423469,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEARHUtL7aaZrz85GG6DcEsrs8FTvDfB1Ju5DSgrEGP4Gx456IQwhB1Paz3U0ncHiGg6pms0cot7XUXAhXRgJJYPuED9VSZstqMd4rban5igrYjntUQxcy8lfgHyXpXaTXQg6RM+iOevIrL8sC5N5YDb4Ug8iADVlrDMKZ7n8CEfkzYKuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjASgQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFkZSkYg",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAALDvQAGg807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiYAAzY13U"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423468,
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423468,
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBn3XHhwdN+q1EM63Q9MvSk/kE8T+Cc6L7mkJf7zYwISMBaA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QlsaCc=",
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
  "id": -576460752303423467,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBt+sL3pPAyUL6w4qEcWiA3D7c0zeeUzgknPkviLsJe49zlO9I7i1td+NnBDxfhem0fdngg4cY4l8c4izKSo2ENuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu3f8+eW"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423467,
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBt+sL3pPAyUL6w4qEcWiA3D7c0zeeUzgknPkviLsJe49zlO9I7i1td+NnBDxfhem0fdngg4cY4l8c4izKSo2ENuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu3f8+eW",
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
  "id": -576460752303423466,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBiZ23UkML9Oys1UkZ8lT/q9CBRfx4x5f1L2mspjJ2SQwdDo3cA63pXIKMkn7t5p52MyXy67d4EZODWbnjOa4YGuEBt+sL3pPAyUL6w4qEcWiA3D7c0zeeUzgknPkviLsJe49zlO9I7i1td+NnBDxfhem0fdngg4cY4l8c4izKSo2ENuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu2+KDNx"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423466,
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "state": "tx_+NILAfiEuEBiZ23UkML9Oys1UkZ8lT/q9CBRfx4x5f1L2mspjJ2SQwdDo3cA63pXIKMkn7t5p52MyXy67d4EZODWbnjOa4YGuEBt+sL3pPAyUL6w4qEcWiA3D7c0zeeUzgknPkviLsJe49zlO9I7i1td+NnBDxfhem0fdngg4cY4l8c4izKSo2ENuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu2+KDNx"
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "state": "tx_+NILAfiEuEBiZ23UkML9Oys1UkZ8lT/q9CBRfx4x5f1L2mspjJ2SQwdDo3cA63pXIKMkn7t5p52MyXy67d4EZODWbnjOa4YGuEBt+sL3pPAyUL6w4qEcWiA3D7c0zeeUzgknPkviLsJe49zlO9I7i1td+NnBDxfhem0fdngg4cY4l8c4izKSo2ENuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu2+KDNx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423465,
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423465,
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
  "id": -576460752303423464,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423464,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBiZ23UkML9Oys1UkZ8lT/q9CBRfx4x5f1L2mspjJ2SQwdDo3cA63pXIKMkn7t5p52MyXy67d4EZODWbnjOa4YGuEBt+sL3pPAyUL6w4qEcWiA3D7c0zeeUzgknPkviLsJe49zlO9I7i1td+NnBDxfhem0fdngg4cY4l8c4izKSo2ENuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAWgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu2+KDNx",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAAbDvQAGg807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiX/+PWk/e"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423463,
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423463,
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBn3XHhwdN+q1EM63Q9MvSk/kE8T+Cc6L7mkJf7zYwISMBqBD48upGMSQmUHkvAbXk8OLPb+iXSg8kxqzNfUkPoVMWXwE7s0=",
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
  "id": -576460752303423462,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDThNpX97BG2t1xF9eqX3Gii70bm6HiP/FCP/Cvg55efy0rNnARl//SRcOxGRYQ7U1jgtkmckyiPe9IE8T4Eo4LuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFm0psHd"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423462,
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDThNpX97BG2t1xF9eqX3Gii70bm6HiP/FCP/Cvg55efy0rNnARl//SRcOxGRYQ7U1jgtkmckyiPe9IE8T4Eo4LuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFm0psHd",
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
  "id": -576460752303423461,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBoR39OsCQo/xhdyXUKV1Ofv8C8FoywMgJ3w/nfjLltJLjNNUHH1YINAfuZ+I3XhJ3h/ylblj+n/ieeNPUBExYGuEDThNpX97BG2t1xF9eqX3Gii70bm6HiP/FCP/Cvg55efy0rNnARl//SRcOxGRYQ7U1jgtkmckyiPe9IE8T4Eo4LuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFnB0pGb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423461,
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "state": "tx_+NILAfiEuEBoR39OsCQo/xhdyXUKV1Ofv8C8FoywMgJ3w/nfjLltJLjNNUHH1YINAfuZ+I3XhJ3h/ylblj+n/ieeNPUBExYGuEDThNpX97BG2t1xF9eqX3Gii70bm6HiP/FCP/Cvg55efy0rNnARl//SRcOxGRYQ7U1jgtkmckyiPe9IE8T4Eo4LuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFnB0pGb"
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
    "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
    "data": {
      "state": "tx_+NILAfiEuEBoR39OsCQo/xhdyXUKV1Ofv8C8FoywMgJ3w/nfjLltJLjNNUHH1YINAfuZ+I3XhJ3h/ylblj+n/ieeNPUBExYGuEDThNpX97BG2t1xF9eqX3Gii70bm6HiP/FCP/Cvg55efy0rNnARl//SRcOxGRYQ7U1jgtkmckyiPe9IE8T4Eo4LuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFnB0pGb"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423460,
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
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423460,
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
  "id": -576460752303423459,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_xRRTRs1kT3bTvavUJHjNSjgfheGqqXan8u4GcwHEkba3FMFHo",
  "id": -576460752303423459,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBoR39OsCQo/xhdyXUKV1Ofv8C8FoywMgJ3w/nfjLltJLjNNUHH1YINAfuZ+I3XhJ3h/ylblj+n/ieeNPUBExYGuEDThNpX97BG2t1xF9eqX3Gii70bm6HiP/FCP/Cvg55efy0rNnARl//SRcOxGRYQ7U1jgtkmckyiPe9IE8T4Eo4LuEj4RjkCoQZ91x4cHTfqtRDOt0PTL0pP5BPE/gnOi+5pCX+82MCEjAagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFnB0pGb",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAALDvQAGg807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiYAAzY13U"
  },
  "version": 1
}
```
