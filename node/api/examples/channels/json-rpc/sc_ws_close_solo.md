
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_close_solo_%2F2607%5Binitiator%5D
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_close_solo_%2F2607%5Binitiator%5D
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAfNO8EGVVRoKbq3Lxj2WY6ZR+xj2jcGlcIhNerfki3mXhj+qJSJgAKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GJGE5yoAAAgoAhhAGeddIAMCgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0IC2ZozQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423392,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECh77lThfOTKqEf7eYAYnH4JPZ47h0ap40EZT90W8188gaGaIqeFvSarZ1puU3jQa7f5Vbd+HSTX1V2hFkHyyoDuIP4gTIBoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y/qiUiYAChAfdjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNhiRhOcqAAAIKAIYQBnnXSADAoDXj090A/DMnCedVe1N9Z8lFvhGFs8xqY89cVUV0esLtCIjjcd0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423392,
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
      "signed_tx": "tx_+MsLAfhCuECh77lThfOTKqEf7eYAYnH4JPZ47h0ap40EZT90W8188gaGaIqeFvSarZ1puU3jQa7f5Vbd+HSTX1V2hFkHyyoDuIP4gTIBoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y/qiUiYAChAfdjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNhiRhOcqAAAIKAIYQBnnXSADAoDXj090A/DMnCedVe1N9Z8lFvhGFs8xqY89cVUV0esLtCIjjcd0=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423391,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAoe+5U4XzkyqhH+3mAGJx+CT2eO4dGqeNBGU/dFvNfPIGhmiKnhb0mq2dablN40Gu3+VW3fh0k19VdoRZB8sqA7hAv+Q1RI1HmKEaS+PFthWWFhGTzZGQJ5kHE1b5W3sUTGGF9yFIJHHteK/O88M97RNXMTjQFndwUghud3XVeDodDbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QiXkao5"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423391,
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
      "tx": "tx_+QENCwH4hLhAoe+5U4XzkyqhH+3mAGJx+CT2eO4dGqeNBGU/dFvNfPIGhmiKnhb0mq2dablN40Gu3+VW3fh0k19VdoRZB8sqA7hAv+Q1RI1HmKEaS+PFthWWFhGTzZGQJ5kHE1b5W3sUTGGF9yFIJHHteK/O88M97RNXMTjQFndwUghud3XVeDodDbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QiXkao5",
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
      "tx": "tx_+QENCwH4hLhAoe+5U4XzkyqhH+3mAGJx+CT2eO4dGqeNBGU/dFvNfPIGhmiKnhb0mq2dablN40Gu3+VW3fh0k19VdoRZB8sqA7hAv+Q1RI1HmKEaS+PFthWWFhGTzZGQJ5kHE1b5W3sUTGGF9yFIJHHteK/O88M97RNXMTjQFndwUghud3XVeDodDbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QiXkao5",
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
      "tx": "tx_+QENCwH4hLhAoe+5U4XzkyqhH+3mAGJx+CT2eO4dGqeNBGU/dFvNfPIGhmiKnhb0mq2dablN40Gu3+VW3fh0k19VdoRZB8sqA7hAv+Q1RI1HmKEaS+PFthWWFhGTzZGQJ5kHE1b5W3sUTGGF9yFIJHHteK/O88M97RNXMTjQFndwUghud3XVeDodDbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QiXkao5",
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
      "tx": "tx_+QENCwH4hLhAoe+5U4XzkyqhH+3mAGJx+CT2eO4dGqeNBGU/dFvNfPIGhmiKnhb0mq2dablN40Gu3+VW3fh0k19VdoRZB8sqA7hAv+Q1RI1HmKEaS+PFthWWFhGTzZGQJ5kHE1b5W3sUTGGF9yFIJHHteK/O88M97RNXMTjQFndwUghud3XVeDodDbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QiXkao5",
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
    "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
    "data": {
      "message": {
        "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
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
    "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
    "data": {
      "message": {
        "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
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
  "id": -576460752303423390,
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
  "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
  "id": -576460752303423390,
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
    "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
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
    "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
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
    "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
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
    "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
    "data": {
      "event": "open"
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
    "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Channel is `open` and ready to use

#### initiator info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
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
    "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
    "data": {
      "state": "tx_+QENCwH4hLhAoe+5U4XzkyqhH+3mAGJx+CT2eO4dGqeNBGU/dFvNfPIGhmiKnhb0mq2dablN40Gu3+VW3fh0k19VdoRZB8sqA7hAv+Q1RI1HmKEaS+PFthWWFhGTzZGQJ5kHE1b5W3sUTGGF9yFIJHHteK/O88M97RNXMTjQFndwUghud3XVeDodDbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QiXkao5"
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
    "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
    "data": {
      "state": "tx_+QENCwH4hLhAoe+5U4XzkyqhH+3mAGJx+CT2eO4dGqeNBGU/dFvNfPIGhmiKnhb0mq2dablN40Gu3+VW3fh0k19VdoRZB8sqA7hAv+Q1RI1HmKEaS+PFthWWFhGTzZGQJ5kHE1b5W3sUTGGF9yFIJHHteK/O88M97RNXMTjQFndwUghud3XVeDodDbiD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QiXkao5"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
    "data": {
      "signed_tx": "tx_+QHuCwHAuQHo+QHlNgGhBv/dD7/GyR7rcE9Q8JWyyLg1pTh/0/B5djm3dLEvtZ3SoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4C5AZL5AY88AfkBhfkBgqDOM+jG8XuLRGiC3ceQIQIQ/jzyUIl/Ef+mOEycBbQfXvkBXvh0oEK0/UerapPbQzGsJ9rr7g22lw3jJiIXlDj09asqgB5a+FGAgICgXcsNRtse/g9BiHP7uGFzG8koJWS929lxPu/eWlx2EmiAgICg7JPsDTEyvjESlTwZosqagTNWWLkJUmaGEMWBJvziHzyAgICAgICAgID4T6Bdyw1G2x7+D0GIc/u4YXMbySglZL3b2XE+795aXHYSaO2gIE7wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiX//4RKDOM+jG8XuLRGiC3ceQIQIQ/jzyUIl/Ef+mOEycBbQfXuIfoEK0/UerapPbQzGsJ9rr7g22lw3jJiIXlDj09asqgB5a+E+g7JPsDTEyvjESlTwZosqagTNWWLkJUmaGEMWBJvziHzztoCBjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNi8oKAQCGJGE5yoABwMDAwMAAhhaE4wEwAAlui2h6",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423389,
  "jsonrpc": "2.0",
  "method": "channels.close_solo_sign",
  "params": {
    "signed_tx": "tx_+QIxCwH4QrhAHIlve+HYsRZtK3wl/uqtLHUMF64QYp468kAsXTzPMlfgCreTfgQzW+WI/a0m6hP1mPayeg/e6HYo03tu7FjWDbkB6PkB5TYBoQb/3Q+/xske63BPUPCVssi4NaU4f9PweXY5t3SxL7Wd0qEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeAuQGS+QGPPAH5AYX5AYKgzjPoxvF7i0Rogt3HkCECEP488lCJfxH/pjhMnAW0H175AV74dKBCtP1Hq2qT20MxrCfa6+4NtpcN4yYiF5Q49PWrKoAeWvhRgICAoF3LDUbbHv4PQYhz+7hhcxvJKCVkvdvZcT7v3lpcdhJogICAoOyT7A0xMr4xEpU8GaLKmoEzVli5CVJmhhDFgSb84h88gICAgICAgICA+E+gXcsNRtse/g9BiHP7uGFzG8koJWS929lxPu/eWlx2EmjtoCBO8EGVVRoKbq3Lxj2WY6ZR+xj2jcGlcIhNerfki3mXi8oKAQCGP6olIl//+ESgzjPoxvF7i0Rogt3HkCECEP488lCJfxH/pjhMnAW0H17iH6BCtP1Hq2qT20MxrCfa6+4NtpcN4yYiF5Q49PWrKoAeWvhPoOyT7A0xMr4xEpU8GaLKmoEzVli5CVJmhhDFgSb84h887aAgYzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAAcDAwMDAAIYWhOMBMAAJ9RzV6g=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
  "id": -576460752303423389,
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
    "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QIxCwH4QrhAHIlve+HYsRZtK3wl/uqtLHUMF64QYp468kAsXTzPMlfgCreTfgQzW+WI/a0m6hP1mPayeg/e6HYo03tu7FjWDbkB6PkB5TYBoQb/3Q+/xske63BPUPCVssi4NaU4f9PweXY5t3SxL7Wd0qEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeAuQGS+QGPPAH5AYX5AYKgzjPoxvF7i0Rogt3HkCECEP488lCJfxH/pjhMnAW0H175AV74dKBCtP1Hq2qT20MxrCfa6+4NtpcN4yYiF5Q49PWrKoAeWvhRgICAoF3LDUbbHv4PQYhz+7hhcxvJKCVkvdvZcT7v3lpcdhJogICAoOyT7A0xMr4xEpU8GaLKmoEzVli5CVJmhhDFgSb84h88gICAgICAgICA+E+gXcsNRtse/g9BiHP7uGFzG8koJWS929lxPu/eWlx2EmjtoCBO8EGVVRoKbq3Lxj2WY6ZR+xj2jcGlcIhNerfki3mXi8oKAQCGP6olIl//+ESgzjPoxvF7i0Rogt3HkCECEP488lCJfxH/pjhMnAW0H17iH6BCtP1Hq2qT20MxrCfa6+4NtpcN4yYiF5Q49PWrKoAeWvhPoOyT7A0xMr4xEpU8GaLKmoEzVli5CVJmhhDFgSb84h887aAgYzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAAcDAwMDAAIYWhOMBMAAJ9RzV6g==",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
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
    "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QIxCwH4QrhAHIlve+HYsRZtK3wl/uqtLHUMF64QYp468kAsXTzPMlfgCreTfgQzW+WI/a0m6hP1mPayeg/e6HYo03tu7FjWDbkB6PkB5TYBoQb/3Q+/xske63BPUPCVssi4NaU4f9PweXY5t3SxL7Wd0qEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeAuQGS+QGPPAH5AYX5AYKgzjPoxvF7i0Rogt3HkCECEP488lCJfxH/pjhMnAW0H175AV74dKBCtP1Hq2qT20MxrCfa6+4NtpcN4yYiF5Q49PWrKoAeWvhRgICAoF3LDUbbHv4PQYhz+7hhcxvJKCVkvdvZcT7v3lpcdhJogICAoOyT7A0xMr4xEpU8GaLKmoEzVli5CVJmhhDFgSb84h88gICAgICAgICA+E+gXcsNRtse/g9BiHP7uGFzG8koJWS929lxPu/eWlx2EmjtoCBO8EGVVRoKbq3Lxj2WY6ZR+xj2jcGlcIhNerfki3mXi8oKAQCGP6olIl//+ESgzjPoxvF7i0Rogt3HkCECEP488lCJfxH/pjhMnAW0H17iH6BCtP1Hq2qT20MxrCfa6+4NtpcN4yYiF5Q49PWrKoAeWvhPoOyT7A0xMr4xEpU8GaLKmoEzVli5CVJmhhDFgSb84h887aAgYzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAAcDAwMDAAIYWhOMBMAAJ9RzV6g==",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
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
    "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBv/dD7/GyR7rcE9Q8JWyyLg1pTh/0/B5djm3dLEvtZ3SoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYY/qiUiX/+GJGE5yoABAIYPXtZ/KAACTNCJwA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423388,
  "jsonrpc": "2.0",
  "method": "channels.settle_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEATQY5NXeQL7eQQf8b7D74GYgg3J6Ut5GzpE5uy3JhYIAWdBewavjhk1UZjw2DuK6bDdItEBl+9ezQVQKCK4BEGuF/4XTgBoQb/3Q+/xske63BPUPCVssi4NaU4f9PweXY5t3SxL7Wd0qEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GP6olIl//hiRhOcqAAQCGD17WfygAArcKg8A="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
  "id": -576460752303423388,
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
    "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEATQY5NXeQL7eQQf8b7D74GYgg3J6Ut5GzpE5uy3JhYIAWdBewavjhk1UZjw2DuK6bDdItEBl+9ezQVQKCK4BEGuF/4XTgBoQb/3Q+/xske63BPUPCVssi4NaU4f9PweXY5t3SxL7Wd0qEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GP6olIl//hiRhOcqAAQCGD17WfygAArcKg8A=",
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
    "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEATQY5NXeQL7eQQf8b7D74GYgg3J6Ut5GzpE5uy3JhYIAWdBewavjhk1UZjw2DuK6bDdItEBl+9ezQVQKCK4BEGuF/4XTgBoQb/3Q+/xske63BPUPCVssi4NaU4f9PweXY5t3SxL7Wd0qEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GP6olIl//hiRhOcqAAQCGD17WfygAArcKg8A=",
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
    "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
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
    "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
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
    "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
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
    "channel_id": "ch_2wgh31g2DABy443qB7VWQE9WEm4kAtXeWUNjQ5tJH9iuUQX4vt",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_close_solo_%2F2607%5Bresponder%5D
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_close_solo_%2F2607%5Bresponder%5D
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAfNO8EGVVRoKbq3Lxj2WY6ZR+xj2jcGlcIhNerfki3mXhj+qJSJgAKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2GJGE5yoAAAgoAhhAGeddIAMCgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0KfOvy2w==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423387,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECeTwOmxmN85jg8OElwD2ZRWkorBd0GPa5VXvXx9nOZld2y17dog0j5Iciqjs+/cLvwZ5g7uF+eBhPDOmFbkJsPuIP4gTIBoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y/qiUiYAChAfdjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNhiRhOcqAAAIKAIYQBnnXSADAoDXj090A/DMnCedVe1N9Z8lFvhGFs8xqY89cVUV0esLtCo9tl4s="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423387,
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
      "signed_tx": "tx_+MsLAfhCuECeTwOmxmN85jg8OElwD2ZRWkorBd0GPa5VXvXx9nOZld2y17dog0j5Iciqjs+/cLvwZ5g7uF+eBhPDOmFbkJsPuIP4gTIBoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y/qiUiYAChAfdjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNhiRhOcqAAAIKAIYQBnnXSADAoDXj090A/DMnCedVe1N9Z8lFvhGFs8xqY89cVUV0esLtCo9tl4s=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423386,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhADZdVH6Umo63ZxWUtl+ximRkfl/Eq7CKkxSvPnJHxI/sXTsngYwsqZkDky87qTTRMX6Xzk1SZeFVqa+YsvY5AAbhAnk8DpsZjfOY4PDhJcA9mUVpKKwXdBj2uVV718fZzmZXdste3aINI+SHIqo7Pv3C78GeYO7hfngYTwzphW5CbD7iD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QqId4hL"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423386,
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
      "tx": "tx_+QENCwH4hLhADZdVH6Umo63ZxWUtl+ximRkfl/Eq7CKkxSvPnJHxI/sXTsngYwsqZkDky87qTTRMX6Xzk1SZeFVqa+YsvY5AAbhAnk8DpsZjfOY4PDhJcA9mUVpKKwXdBj2uVV718fZzmZXdste3aINI+SHIqo7Pv3C78GeYO7hfngYTwzphW5CbD7iD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QqId4hL",
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
      "tx": "tx_+QENCwH4hLhADZdVH6Umo63ZxWUtl+ximRkfl/Eq7CKkxSvPnJHxI/sXTsngYwsqZkDky87qTTRMX6Xzk1SZeFVqa+YsvY5AAbhAnk8DpsZjfOY4PDhJcA9mUVpKKwXdBj2uVV718fZzmZXdste3aINI+SHIqo7Pv3C78GeYO7hfngYTwzphW5CbD7iD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QqId4hL",
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
      "tx": "tx_+QENCwH4hLhADZdVH6Umo63ZxWUtl+ximRkfl/Eq7CKkxSvPnJHxI/sXTsngYwsqZkDky87qTTRMX6Xzk1SZeFVqa+YsvY5AAbhAnk8DpsZjfOY4PDhJcA9mUVpKKwXdBj2uVV718fZzmZXdste3aINI+SHIqo7Pv3C78GeYO7hfngYTwzphW5CbD7iD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QqId4hL",
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
      "tx": "tx_+QENCwH4hLhADZdVH6Umo63ZxWUtl+ximRkfl/Eq7CKkxSvPnJHxI/sXTsngYwsqZkDky87qTTRMX6Xzk1SZeFVqa+YsvY5AAbhAnk8DpsZjfOY4PDhJcA9mUVpKKwXdBj2uVV718fZzmZXdste3aINI+SHIqo7Pv3C78GeYO7hfngYTwzphW5CbD7iD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QqId4hL",
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
    "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
    "data": {
      "message": {
        "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
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
    "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
    "data": {
      "message": {
        "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
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
  "id": -576460752303423385,
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
  "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
  "id": -576460752303423385,
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
    "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
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
    "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
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
    "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
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
    "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
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
    "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
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
    "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
    "data": {
      "state": "tx_+QENCwH4hLhADZdVH6Umo63ZxWUtl+ximRkfl/Eq7CKkxSvPnJHxI/sXTsngYwsqZkDky87qTTRMX6Xzk1SZeFVqa+YsvY5AAbhAnk8DpsZjfOY4PDhJcA9mUVpKKwXdBj2uVV718fZzmZXdste3aINI+SHIqo7Pv3C78GeYO7hfngYTwzphW5CbD7iD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QqId4hL"
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
    "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
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
    "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
    "data": {
      "state": "tx_+QENCwH4hLhADZdVH6Umo63ZxWUtl+ximRkfl/Eq7CKkxSvPnJHxI/sXTsngYwsqZkDky87qTTRMX6Xzk1SZeFVqa+YsvY5AAbhAnk8DpsZjfOY4PDhJcA9mUVpKKwXdBj2uVV718fZzmZXdste3aINI+SHIqo7Pv3C78GeYO7hfngYTwzphW5CbD7iD+IEyAaEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olImAAoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYYkYTnKgAACCgCGEAZ510gAwKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QqId4hL"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
    "data": {
      "signed_tx": "tx_+QHuCwHAuQHo+QHlNgGhBsGc5p76MsgRR/JGbQ16aTZIlE8ZkJDr2E2D3aGouuP6oQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYC5AZL5AY88AfkBhfkBgqDOM+jG8XuLRGiC3ceQIQIQ/jzyUIl/Ef+mOEycBbQfXvkBXvh0oEK0/UerapPbQzGsJ9rr7g22lw3jJiIXlDj09asqgB5a+FGAgICgXcsNRtse/g9BiHP7uGFzG8koJWS929lxPu/eWlx2EmiAgICg7JPsDTEyvjESlTwZosqagTNWWLkJUmaGEMWBJvziHzyAgICAgICAgID4T6Bdyw1G2x7+D0GIc/u4YXMbySglZL3b2XE+795aXHYSaO2gIE7wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeLygoBAIY/qiUiX//4RKDOM+jG8XuLRGiC3ceQIQIQ/jzyUIl/Ef+mOEycBbQfXuIfoEK0/UerapPbQzGsJ9rr7g22lw3jJiIXlDj09asqgB5a+E+g7JPsDTEyvjESlTwZosqagTNWWLkJUmaGEMWBJvziHzztoCBjMFzzMxnZCGDCskL+iyZzvT+IEpT6nkWHXLN+JWBNi8oKAQCGJGE5yoABwMDAwMAAhhaE4wEwAAPeJfOn",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423384,
  "jsonrpc": "2.0",
  "method": "channels.close_solo_sign",
  "params": {
    "signed_tx": "tx_+QIxCwH4QrhAV0CAAz1f+s5rC/56iudDYLI2WYcLt2iUZL0WrzT8GqSwLc5MDUAk/zgDl7hqD8r5pHujPuiSn3SKnukWrdKQBLkB6PkB5TYBoQbBnOae+jLIEUfyRm0Nemk2SJRPGZCQ69hNg92hqLrj+qEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2AuQGS+QGPPAH5AYX5AYKgzjPoxvF7i0Rogt3HkCECEP488lCJfxH/pjhMnAW0H175AV74dKBCtP1Hq2qT20MxrCfa6+4NtpcN4yYiF5Q49PWrKoAeWvhRgICAoF3LDUbbHv4PQYhz+7hhcxvJKCVkvdvZcT7v3lpcdhJogICAoOyT7A0xMr4xEpU8GaLKmoEzVli5CVJmhhDFgSb84h88gICAgICAgICA+E+gXcsNRtse/g9BiHP7uGFzG8koJWS929lxPu/eWlx2EmjtoCBO8EGVVRoKbq3Lxj2WY6ZR+xj2jcGlcIhNerfki3mXi8oKAQCGP6olIl//+ESgzjPoxvF7i0Rogt3HkCECEP488lCJfxH/pjhMnAW0H17iH6BCtP1Hq2qT20MxrCfa6+4NtpcN4yYiF5Q49PWrKoAeWvhPoOyT7A0xMr4xEpU8GaLKmoEzVli5CVJmhhDFgSb84h887aAgYzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAAcDAwMDAAIYWhOMBMAADivDfVg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
  "id": -576460752303423384,
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
    "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QIxCwH4QrhAV0CAAz1f+s5rC/56iudDYLI2WYcLt2iUZL0WrzT8GqSwLc5MDUAk/zgDl7hqD8r5pHujPuiSn3SKnukWrdKQBLkB6PkB5TYBoQbBnOae+jLIEUfyRm0Nemk2SJRPGZCQ69hNg92hqLrj+qEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2AuQGS+QGPPAH5AYX5AYKgzjPoxvF7i0Rogt3HkCECEP488lCJfxH/pjhMnAW0H175AV74dKBCtP1Hq2qT20MxrCfa6+4NtpcN4yYiF5Q49PWrKoAeWvhRgICAoF3LDUbbHv4PQYhz+7hhcxvJKCVkvdvZcT7v3lpcdhJogICAoOyT7A0xMr4xEpU8GaLKmoEzVli5CVJmhhDFgSb84h88gICAgICAgICA+E+gXcsNRtse/g9BiHP7uGFzG8koJWS929lxPu/eWlx2EmjtoCBO8EGVVRoKbq3Lxj2WY6ZR+xj2jcGlcIhNerfki3mXi8oKAQCGP6olIl//+ESgzjPoxvF7i0Rogt3HkCECEP488lCJfxH/pjhMnAW0H17iH6BCtP1Hq2qT20MxrCfa6+4NtpcN4yYiF5Q49PWrKoAeWvhPoOyT7A0xMr4xEpU8GaLKmoEzVli5CVJmhhDFgSb84h887aAgYzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAAcDAwMDAAIYWhOMBMAADivDfVg==",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
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
    "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QIxCwH4QrhAV0CAAz1f+s5rC/56iudDYLI2WYcLt2iUZL0WrzT8GqSwLc5MDUAk/zgDl7hqD8r5pHujPuiSn3SKnukWrdKQBLkB6PkB5TYBoQbBnOae+jLIEUfyRm0Nemk2SJRPGZCQ69hNg92hqLrj+qEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE2AuQGS+QGPPAH5AYX5AYKgzjPoxvF7i0Rogt3HkCECEP488lCJfxH/pjhMnAW0H175AV74dKBCtP1Hq2qT20MxrCfa6+4NtpcN4yYiF5Q49PWrKoAeWvhRgICAoF3LDUbbHv4PQYhz+7hhcxvJKCVkvdvZcT7v3lpcdhJogICAoOyT7A0xMr4xEpU8GaLKmoEzVli5CVJmhhDFgSb84h88gICAgICAgICA+E+gXcsNRtse/g9BiHP7uGFzG8koJWS929lxPu/eWlx2EmjtoCBO8EGVVRoKbq3Lxj2WY6ZR+xj2jcGlcIhNerfki3mXi8oKAQCGP6olIl//+ESgzjPoxvF7i0Rogt3HkCECEP488lCJfxH/pjhMnAW0H17iH6BCtP1Hq2qT20MxrCfa6+4NtpcN4yYiF5Q49PWrKoAeWvhPoOyT7A0xMr4xEpU8GaLKmoEzVli5CVJmhhDFgSb84h887aAgYzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTYvKCgEAhiRhOcqAAcDAwMDAAIYWhOMBMAADivDfVg==",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
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
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBsGc5p76MsgRR/JGbQ16aTZIlE8ZkJDr2E2D3aGouuP6oQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5l4Y/qiUiX/+GJGE5yoABAIYPXtZ/KAALs4fbeA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423383,
  "jsonrpc": "2.0",
  "method": "channels.settle_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEC2RaTLcqJujUurwp+1u8l9LvPgxhahaMAsrfmxduyVkxhsvrF5JBhgRuwCn/c/8qMGLr21BiPdS7cfToM1O8kBuF/4XTgBoQbBnOae+jLIEUfyRm0Nemk2SJRPGZCQ69hNg92hqLrj+qEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olIl//hiRhOcqAAQCGD17WfygAC8aM/Gk="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
  "id": -576460752303423383,
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
    "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEC2RaTLcqJujUurwp+1u8l9LvPgxhahaMAsrfmxduyVkxhsvrF5JBhgRuwCn/c/8qMGLr21BiPdS7cfToM1O8kBuF/4XTgBoQbBnOae+jLIEUfyRm0Nemk2SJRPGZCQ69hNg92hqLrj+qEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olIl//hiRhOcqAAQCGD17WfygAC8aM/Gk=",
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
    "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEC2RaTLcqJujUurwp+1u8l9LvPgxhahaMAsrfmxduyVkxhsvrF5JBhgRuwCn/c/8qMGLr21BiPdS7cfToM1O8kBuF/4XTgBoQbBnOae+jLIEUfyRm0Nemk2SJRPGZCQ69hNg92hqLrj+qEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZeGP6olIl//hiRhOcqAAQCGD17WfygAC8aM/Gk=",
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
    "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
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
    "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
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
    "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
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
    "channel_id": "ch_2UGajEm2i2HbrCbwvyRaBcmRHzuVVArFU6MRrhfGPXhvBtHtKH",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```
