
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_j9m9TB7mgnPJ18dqjts5CzaDLN25CEtwbGrZC8QMryphUKpQX&lock_period=10&port=13216&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2ToRTR6fWZUCj4ouc9obS52zi56W6JS4NsvvB54429AenaPRnN&role=initiator
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_j9m9TB7mgnPJ18dqjts5CzaDLN25CEtwbGrZC8QMryphUKpQX&lock_period=10&port=13216&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2ToRTR6fWZUCj4ouc9obS52zi56W6JS4NsvvB54429AenaPRnN&role=responder
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAV+1iTDF3CJ2MD2ZRzRUARwsA4lcQP38p0r9Mo16XXF4hj+qJSJgAKEBwIyz+io937CGxh84LuA01TO5kU6pOZTaDcDyWmIhVsuGJGE5yoAAAgoAhhAGeddIAMCgrgqQCNm5KCk8x3CUIXjWEW5ZRBrkpz4NUPyvUdO2+yEBg6h2Hw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423313,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECXhrtak3AAyNqMmWETMN8B4z2IyesTLaYlKXA6hSHjcZi94l91qzrWVbaRtIm7rVoUmYAMPBhBrbspXW/m/R0FuIP4gTIBoQFftYkwxdwidjA9mUc0VAEcLAOJXED9/KdK/TKNel1xeIY/qiUiYAChAcCMs/oqPd+whsYfOC7gNNUzuZFOqTmU2g3A8lpiIVbLhiRhOcqAAAIKAIYQBnnXSADAoK4KkAjZuSgpPMdwlCF41hFuWUQa5Kc+DVD8r1HTtvshAZ9qLL8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423313,
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
      "signed_tx": "tx_+MsLAfhCuECXhrtak3AAyNqMmWETMN8B4z2IyesTLaYlKXA6hSHjcZi94l91qzrWVbaRtIm7rVoUmYAMPBhBrbspXW/m/R0FuIP4gTIBoQFftYkwxdwidjA9mUc0VAEcLAOJXED9/KdK/TKNel1xeIY/qiUiYAChAcCMs/oqPd+whsYfOC7gNNUzuZFOqTmU2g3A8lpiIVbLhiRhOcqAAAIKAIYQBnnXSADAoK4KkAjZuSgpPMdwlCF41hFuWUQa5Kc+DVD8r1HTtvshAZ9qLL8=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423312,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAVn5jcXdhyU1hbYfBwZf+1AcEWSpOQs/d+kNmu3yBIjoQVLLh1tHwMhVAA+LVVmfNcduN2L9KQg1rD8ATz/ZmALhAl4a7WpNwAMjajJlhEzDfAeM9iMnrEy2mJSlwOoUh43GYveJfdas61lW2kbSJu61aFJmADDwYQa27KV1v5v0dBbiD+IEyAaEBX7WJMMXcInYwPZlHNFQBHCwDiVxA/fynSv0yjXpdcXiGP6olImAAoQHAjLP6Kj3fsIbGHzgu4DTVM7mRTqk5lNoNwPJaYiFWy4YkYTnKgAACCgCGEAZ510gAwKCuCpAI2bkoKTzHcJQheNYRbllEGuSnPg1Q/K9R07b7IQHMcCai"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423312,
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
      "tx": "tx_+QENCwH4hLhAVn5jcXdhyU1hbYfBwZf+1AcEWSpOQs/d+kNmu3yBIjoQVLLh1tHwMhVAA+LVVmfNcduN2L9KQg1rD8ATz/ZmALhAl4a7WpNwAMjajJlhEzDfAeM9iMnrEy2mJSlwOoUh43GYveJfdas61lW2kbSJu61aFJmADDwYQa27KV1v5v0dBbiD+IEyAaEBX7WJMMXcInYwPZlHNFQBHCwDiVxA/fynSv0yjXpdcXiGP6olImAAoQHAjLP6Kj3fsIbGHzgu4DTVM7mRTqk5lNoNwPJaYiFWy4YkYTnKgAACCgCGEAZ510gAwKCuCpAI2bkoKTzHcJQheNYRbllEGuSnPg1Q/K9R07b7IQHMcCai",
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
      "tx": "tx_+QENCwH4hLhAVn5jcXdhyU1hbYfBwZf+1AcEWSpOQs/d+kNmu3yBIjoQVLLh1tHwMhVAA+LVVmfNcduN2L9KQg1rD8ATz/ZmALhAl4a7WpNwAMjajJlhEzDfAeM9iMnrEy2mJSlwOoUh43GYveJfdas61lW2kbSJu61aFJmADDwYQa27KV1v5v0dBbiD+IEyAaEBX7WJMMXcInYwPZlHNFQBHCwDiVxA/fynSv0yjXpdcXiGP6olImAAoQHAjLP6Kj3fsIbGHzgu4DTVM7mRTqk5lNoNwPJaYiFWy4YkYTnKgAACCgCGEAZ510gAwKCuCpAI2bkoKTzHcJQheNYRbllEGuSnPg1Q/K9R07b7IQHMcCai",
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
      "tx": "tx_+QENCwH4hLhAVn5jcXdhyU1hbYfBwZf+1AcEWSpOQs/d+kNmu3yBIjoQVLLh1tHwMhVAA+LVVmfNcduN2L9KQg1rD8ATz/ZmALhAl4a7WpNwAMjajJlhEzDfAeM9iMnrEy2mJSlwOoUh43GYveJfdas61lW2kbSJu61aFJmADDwYQa27KV1v5v0dBbiD+IEyAaEBX7WJMMXcInYwPZlHNFQBHCwDiVxA/fynSv0yjXpdcXiGP6olImAAoQHAjLP6Kj3fsIbGHzgu4DTVM7mRTqk5lNoNwPJaYiFWy4YkYTnKgAACCgCGEAZ510gAwKCuCpAI2bkoKTzHcJQheNYRbllEGuSnPg1Q/K9R07b7IQHMcCai",
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
      "tx": "tx_+QENCwH4hLhAVn5jcXdhyU1hbYfBwZf+1AcEWSpOQs/d+kNmu3yBIjoQVLLh1tHwMhVAA+LVVmfNcduN2L9KQg1rD8ATz/ZmALhAl4a7WpNwAMjajJlhEzDfAeM9iMnrEy2mJSlwOoUh43GYveJfdas61lW2kbSJu61aFJmADDwYQa27KV1v5v0dBbiD+IEyAaEBX7WJMMXcInYwPZlHNFQBHCwDiVxA/fynSv0yjXpdcXiGP6olImAAoQHAjLP6Kj3fsIbGHzgu4DTVM7mRTqk5lNoNwPJaYiFWy4YkYTnKgAACCgCGEAZ510gAwKCuCpAI2bkoKTzHcJQheNYRbllEGuSnPg1Q/K9R07b7IQHMcCai",
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
    "to": "ak_2ToRTR6fWZUCj4ouc9obS52zi56W6JS4NsvvB54429AenaPRnN"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2Q7ba7rxB3A8okj8kc9PBvrNRDLmFBYdrWS6bc85hAgZ4bMJM9",
    "data": {
      "message": {
        "channel_id": "ch_2Q7ba7rxB3A8okj8kc9PBvrNRDLmFBYdrWS6bc85hAgZ4bMJM9",
        "from": "ak_j9m9TB7mgnPJ18dqjts5CzaDLN25CEtwbGrZC8QMryphUKpQX",
        "info": "Hello",
        "to": "ak_2ToRTR6fWZUCj4ouc9obS52zi56W6JS4NsvvB54429AenaPRnN"
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
    "to": "ak_j9m9TB7mgnPJ18dqjts5CzaDLN25CEtwbGrZC8QMryphUKpQX"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2Q7ba7rxB3A8okj8kc9PBvrNRDLmFBYdrWS6bc85hAgZ4bMJM9",
    "data": {
      "message": {
        "channel_id": "ch_2Q7ba7rxB3A8okj8kc9PBvrNRDLmFBYdrWS6bc85hAgZ4bMJM9",
        "from": "ak_2ToRTR6fWZUCj4ouc9obS52zi56W6JS4NsvvB54429AenaPRnN",
        "info": "Hello back",
        "to": "ak_j9m9TB7mgnPJ18dqjts5CzaDLN25CEtwbGrZC8QMryphUKpQX"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423311,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_j9m9TB7mgnPJ18dqjts5CzaDLN25CEtwbGrZC8QMryphUKpQX",
      "ak_2ToRTR6fWZUCj4ouc9obS52zi56W6JS4NsvvB54429AenaPRnN"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Q7ba7rxB3A8okj8kc9PBvrNRDLmFBYdrWS6bc85hAgZ4bMJM9",
  "id": -576460752303423311,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_j9m9TB7mgnPJ18dqjts5CzaDLN25CEtwbGrZC8QMryphUKpQX",
      "balance": 69999999999999
    },
    {
      "account": "ak_2ToRTR6fWZUCj4ouc9obS52zi56W6JS4NsvvB54429AenaPRnN",
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
    "channel_id": "ch_2Q7ba7rxB3A8okj8kc9PBvrNRDLmFBYdrWS6bc85hAgZ4bMJM9",
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
    "channel_id": "ch_2Q7ba7rxB3A8okj8kc9PBvrNRDLmFBYdrWS6bc85hAgZ4bMJM9",
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
    "channel_id": "ch_2Q7ba7rxB3A8okj8kc9PBvrNRDLmFBYdrWS6bc85hAgZ4bMJM9",
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
    "channel_id": "ch_2Q7ba7rxB3A8okj8kc9PBvrNRDLmFBYdrWS6bc85hAgZ4bMJM9",
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
    "channel_id": "ch_2Q7ba7rxB3A8okj8kc9PBvrNRDLmFBYdrWS6bc85hAgZ4bMJM9",
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
    "channel_id": "ch_2Q7ba7rxB3A8okj8kc9PBvrNRDLmFBYdrWS6bc85hAgZ4bMJM9",
    "data": {
      "state": "tx_+QENCwH4hLhAVn5jcXdhyU1hbYfBwZf+1AcEWSpOQs/d+kNmu3yBIjoQVLLh1tHwMhVAA+LVVmfNcduN2L9KQg1rD8ATz/ZmALhAl4a7WpNwAMjajJlhEzDfAeM9iMnrEy2mJSlwOoUh43GYveJfdas61lW2kbSJu61aFJmADDwYQa27KV1v5v0dBbiD+IEyAaEBX7WJMMXcInYwPZlHNFQBHCwDiVxA/fynSv0yjXpdcXiGP6olImAAoQHAjLP6Kj3fsIbGHzgu4DTVM7mRTqk5lNoNwPJaYiFWy4YkYTnKgAACCgCGEAZ510gAwKCuCpAI2bkoKTzHcJQheNYRbllEGuSnPg1Q/K9R07b7IQHMcCai"
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
    "channel_id": "ch_2Q7ba7rxB3A8okj8kc9PBvrNRDLmFBYdrWS6bc85hAgZ4bMJM9",
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
    "channel_id": "ch_2Q7ba7rxB3A8okj8kc9PBvrNRDLmFBYdrWS6bc85hAgZ4bMJM9",
    "data": {
      "state": "tx_+QENCwH4hLhAVn5jcXdhyU1hbYfBwZf+1AcEWSpOQs/d+kNmu3yBIjoQVLLh1tHwMhVAA+LVVmfNcduN2L9KQg1rD8ATz/ZmALhAl4a7WpNwAMjajJlhEzDfAeM9iMnrEy2mJSlwOoUh43GYveJfdas61lW2kbSJu61aFJmADDwYQa27KV1v5v0dBbiD+IEyAaEBX7WJMMXcInYwPZlHNFQBHCwDiVxA/fynSv0yjXpdcXiGP6olImAAoQHAjLP6Kj3fsIbGHzgu4DTVM7mRTqk5lNoNwPJaYiFWy4YkYTnKgAACCgCGEAZ510gAwKCuCpAI2bkoKTzHcJQheNYRbllEGuSnPg1Q/K9R07b7IQHMcCai"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2e8k6kVseNQWJBWNUK6cLb1n9CEGL6Lx3kDJze2jL4Pfnttkg4&lock_period=10&port=12652&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_KrbQ9aetAqfPC8AdiUpD9XYayLmte5RqzRcRRvzqApksFQKUc&role=initiator
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2e8k6kVseNQWJBWNUK6cLb1n9CEGL6Lx3kDJze2jL4Pfnttkg4&lock_period=10&port=12652&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_KrbQ9aetAqfPC8AdiUpD9XYayLmte5RqzRcRRvzqApksFQKUc&role=responder
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAdgDIwZgljXZOrMl/VV64oxoL0svPvuFA44gM+uhdH1Phj+qJSJgAKEBKtANbvvGxHYt5ueuowO2kzR0ly/jdnkYtXlurYb/t3aGJGE5yoAAAgoAhhAGeddIAMCg0M/td+HI/3cuplRMElYI8h8kd7+Zk4GmAN9w69CPr70BvJ/9oQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422402,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBqiJd0BbnERxdynGOG70QUC/sKkrHlRAZonsBrLJjNKOG3VpOx6yZfQOIy6AmrhEndg3eHbKzb0MM79NSVQ3EFuIP4gTIBoQHYAyMGYJY12TqzJf1VeuKMaC9LLz77hQOOIDProXR9T4Y/qiUiYAChASrQDW77xsR2LebnrqMDtpM0dJcv43Z5GLV5bq2G/7d2hiRhOcqAAAIKAIYQBnnXSADAoNDP7XfhyP93LqZUTBJWCPIfJHe/mZOBpgDfcOvQj6+9AdWWp0o="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422402,
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
      "signed_tx": "tx_+MsLAfhCuEBqiJd0BbnERxdynGOG70QUC/sKkrHlRAZonsBrLJjNKOG3VpOx6yZfQOIy6AmrhEndg3eHbKzb0MM79NSVQ3EFuIP4gTIBoQHYAyMGYJY12TqzJf1VeuKMaC9LLz77hQOOIDProXR9T4Y/qiUiYAChASrQDW77xsR2LebnrqMDtpM0dJcv43Z5GLV5bq2G/7d2hiRhOcqAAAIKAIYQBnnXSADAoNDP7XfhyP93LqZUTBJWCPIfJHe/mZOBpgDfcOvQj6+9AdWWp0o=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422401,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhALFI29kWMJNktBzqeUtyyPwsGG5LAT/ENL5PdxiZw+IcjH+TNr7V6J+a9xubI572nsj21qYHkX2Ow2aH4ibXDDbhAaoiXdAW5xEcXcpxjhu9EFAv7CpKx5UQGaJ7AayyYzSjht1aTsesmX0DiMugJq4RJ3YN3h2ys29DDO/TUlUNxBbiD+IEyAaEB2AMjBmCWNdk6syX9VXrijGgvSy8++4UDjiAz66F0fU+GP6olImAAoQEq0A1u+8bEdi3m566jA7aTNHSXL+N2eRi1eW6thv+3doYkYTnKgAACCgCGEAZ510gAwKDQz+134cj/dy6mVEwSVgjyHyR3v5mTgaYA33Dr0I+vvQGQUnME"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422401,
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
      "tx": "tx_+QENCwH4hLhALFI29kWMJNktBzqeUtyyPwsGG5LAT/ENL5PdxiZw+IcjH+TNr7V6J+a9xubI572nsj21qYHkX2Ow2aH4ibXDDbhAaoiXdAW5xEcXcpxjhu9EFAv7CpKx5UQGaJ7AayyYzSjht1aTsesmX0DiMugJq4RJ3YN3h2ys29DDO/TUlUNxBbiD+IEyAaEB2AMjBmCWNdk6syX9VXrijGgvSy8++4UDjiAz66F0fU+GP6olImAAoQEq0A1u+8bEdi3m566jA7aTNHSXL+N2eRi1eW6thv+3doYkYTnKgAACCgCGEAZ510gAwKDQz+134cj/dy6mVEwSVgjyHyR3v5mTgaYA33Dr0I+vvQGQUnME",
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
      "tx": "tx_+QENCwH4hLhALFI29kWMJNktBzqeUtyyPwsGG5LAT/ENL5PdxiZw+IcjH+TNr7V6J+a9xubI572nsj21qYHkX2Ow2aH4ibXDDbhAaoiXdAW5xEcXcpxjhu9EFAv7CpKx5UQGaJ7AayyYzSjht1aTsesmX0DiMugJq4RJ3YN3h2ys29DDO/TUlUNxBbiD+IEyAaEB2AMjBmCWNdk6syX9VXrijGgvSy8++4UDjiAz66F0fU+GP6olImAAoQEq0A1u+8bEdi3m566jA7aTNHSXL+N2eRi1eW6thv+3doYkYTnKgAACCgCGEAZ510gAwKDQz+134cj/dy6mVEwSVgjyHyR3v5mTgaYA33Dr0I+vvQGQUnME",
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
      "tx": "tx_+QENCwH4hLhALFI29kWMJNktBzqeUtyyPwsGG5LAT/ENL5PdxiZw+IcjH+TNr7V6J+a9xubI572nsj21qYHkX2Ow2aH4ibXDDbhAaoiXdAW5xEcXcpxjhu9EFAv7CpKx5UQGaJ7AayyYzSjht1aTsesmX0DiMugJq4RJ3YN3h2ys29DDO/TUlUNxBbiD+IEyAaEB2AMjBmCWNdk6syX9VXrijGgvSy8++4UDjiAz66F0fU+GP6olImAAoQEq0A1u+8bEdi3m566jA7aTNHSXL+N2eRi1eW6thv+3doYkYTnKgAACCgCGEAZ510gAwKDQz+134cj/dy6mVEwSVgjyHyR3v5mTgaYA33Dr0I+vvQGQUnME",
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
      "tx": "tx_+QENCwH4hLhALFI29kWMJNktBzqeUtyyPwsGG5LAT/ENL5PdxiZw+IcjH+TNr7V6J+a9xubI572nsj21qYHkX2Ow2aH4ibXDDbhAaoiXdAW5xEcXcpxjhu9EFAv7CpKx5UQGaJ7AayyYzSjht1aTsesmX0DiMugJq4RJ3YN3h2ys29DDO/TUlUNxBbiD+IEyAaEB2AMjBmCWNdk6syX9VXrijGgvSy8++4UDjiAz66F0fU+GP6olImAAoQEq0A1u+8bEdi3m566jA7aTNHSXL+N2eRi1eW6thv+3doYkYTnKgAACCgCGEAZ510gAwKDQz+134cj/dy6mVEwSVgjyHyR3v5mTgaYA33Dr0I+vvQGQUnME",
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
    "to": "ak_KrbQ9aetAqfPC8AdiUpD9XYayLmte5RqzRcRRvzqApksFQKUc"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2KQmcen7viT2NGzLyzfNrtJxw3LMb5hW4hwkuamA3JULMtohp5",
    "data": {
      "message": {
        "channel_id": "ch_2KQmcen7viT2NGzLyzfNrtJxw3LMb5hW4hwkuamA3JULMtohp5",
        "from": "ak_2e8k6kVseNQWJBWNUK6cLb1n9CEGL6Lx3kDJze2jL4Pfnttkg4",
        "info": "Hello",
        "to": "ak_KrbQ9aetAqfPC8AdiUpD9XYayLmte5RqzRcRRvzqApksFQKUc"
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
    "to": "ak_2e8k6kVseNQWJBWNUK6cLb1n9CEGL6Lx3kDJze2jL4Pfnttkg4"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2KQmcen7viT2NGzLyzfNrtJxw3LMb5hW4hwkuamA3JULMtohp5",
    "data": {
      "message": {
        "channel_id": "ch_2KQmcen7viT2NGzLyzfNrtJxw3LMb5hW4hwkuamA3JULMtohp5",
        "from": "ak_KrbQ9aetAqfPC8AdiUpD9XYayLmte5RqzRcRRvzqApksFQKUc",
        "info": "Hello back",
        "to": "ak_2e8k6kVseNQWJBWNUK6cLb1n9CEGL6Lx3kDJze2jL4Pfnttkg4"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422400,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2e8k6kVseNQWJBWNUK6cLb1n9CEGL6Lx3kDJze2jL4Pfnttkg4",
      "ak_KrbQ9aetAqfPC8AdiUpD9XYayLmte5RqzRcRRvzqApksFQKUc"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2KQmcen7viT2NGzLyzfNrtJxw3LMb5hW4hwkuamA3JULMtohp5",
  "id": -576460752303422400,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2e8k6kVseNQWJBWNUK6cLb1n9CEGL6Lx3kDJze2jL4Pfnttkg4",
      "balance": 69999999999999
    },
    {
      "account": "ak_KrbQ9aetAqfPC8AdiUpD9XYayLmte5RqzRcRRvzqApksFQKUc",
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
    "channel_id": "ch_2KQmcen7viT2NGzLyzfNrtJxw3LMb5hW4hwkuamA3JULMtohp5",
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
    "channel_id": "ch_2KQmcen7viT2NGzLyzfNrtJxw3LMb5hW4hwkuamA3JULMtohp5",
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
    "channel_id": "ch_2KQmcen7viT2NGzLyzfNrtJxw3LMb5hW4hwkuamA3JULMtohp5",
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
    "channel_id": "ch_2KQmcen7viT2NGzLyzfNrtJxw3LMb5hW4hwkuamA3JULMtohp5",
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
    "channel_id": "ch_2KQmcen7viT2NGzLyzfNrtJxw3LMb5hW4hwkuamA3JULMtohp5",
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
    "channel_id": "ch_2KQmcen7viT2NGzLyzfNrtJxw3LMb5hW4hwkuamA3JULMtohp5",
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
    "channel_id": "ch_2KQmcen7viT2NGzLyzfNrtJxw3LMb5hW4hwkuamA3JULMtohp5",
    "data": {
      "state": "tx_+QENCwH4hLhALFI29kWMJNktBzqeUtyyPwsGG5LAT/ENL5PdxiZw+IcjH+TNr7V6J+a9xubI572nsj21qYHkX2Ow2aH4ibXDDbhAaoiXdAW5xEcXcpxjhu9EFAv7CpKx5UQGaJ7AayyYzSjht1aTsesmX0DiMugJq4RJ3YN3h2ys29DDO/TUlUNxBbiD+IEyAaEB2AMjBmCWNdk6syX9VXrijGgvSy8++4UDjiAz66F0fU+GP6olImAAoQEq0A1u+8bEdi3m566jA7aTNHSXL+N2eRi1eW6thv+3doYkYTnKgAACCgCGEAZ510gAwKDQz+134cj/dy6mVEwSVgjyHyR3v5mTgaYA33Dr0I+vvQGQUnME"
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
    "channel_id": "ch_2KQmcen7viT2NGzLyzfNrtJxw3LMb5hW4hwkuamA3JULMtohp5",
    "data": {
      "state": "tx_+QENCwH4hLhALFI29kWMJNktBzqeUtyyPwsGG5LAT/ENL5PdxiZw+IcjH+TNr7V6J+a9xubI572nsj21qYHkX2Ow2aH4ibXDDbhAaoiXdAW5xEcXcpxjhu9EFAv7CpKx5UQGaJ7AayyYzSjht1aTsesmX0DiMugJq4RJ3YN3h2ys29DDO/TUlUNxBbiD+IEyAaEB2AMjBmCWNdk6syX9VXrijGgvSy8++4UDjiAz66F0fU+GP6olImAAoQEq0A1u+8bEdi3m566jA7aTNHSXL+N2eRi1eW6thv+3doYkYTnKgAACCgCGEAZ510gAwKDQz+134cj/dy6mVEwSVgjyHyR3v5mTgaYA33Dr0I+vvQGQUnME"
    }
  },
  "version": 1
}
```
