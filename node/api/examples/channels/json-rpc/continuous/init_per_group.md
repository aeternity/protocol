
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm&keep_running=false&lock_period=10&log_keep=25&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc&role=initiator
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_MZ4JE99LBEPjG4oITrNw99I6Y/MRvLjh3LbU9rLFYKS1mD16"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm&keep_running=false&lock_period=10&log_keep=25&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc&role=responder
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_/+tL3gzjMdyc6M6idxlr/ImZRloafr1Ls3MWkznu9OF5ZhwR"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAT8ftHGHr6cftnbuH3ep32k+LYAuot0+T9ibD+19T65whj+qJSJgAKEBMStFQ6OUP1GCZB6MtyVmwio20If1kN2VAOD5rye7X8eGJGE5yoAAAgoAhhAGeddIAMCgxbBf7c3Y8acHvN2Udyh7FDzMeR4dVzrpKkEoIxsQvd0BvZd7PQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423488,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAXj1crbcVKHmZl3hCGJY4ZMtNzlA9XQEGajg8BRA5/Z5KA0AKIxGOXnH80lfOEMOjHjSu3vedhOss3iKyQIm8GuIP4gTIBoQE/H7Rxh6+nH7Z27h93qd9pPi2ALqLdPk/Ymw/tfU+ucIY/qiUiYAChATErRUOjlD9RgmQejLclZsIqNtCH9ZDdlQDg+a8nu1/HhiRhOcqAAAIKAIYQBnnXSADAoMWwX+3N2PGnB7zdlHcoexQ8zHkeHVc66SpBKCMbEL3dAcvsQVk="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423488,
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_/+tL3gzjMdyc6M6idxlr/ImZRloafr1Ls3MWkznu9OF5ZhwR"
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEAXj1crbcVKHmZl3hCGJY4ZMtNzlA9XQEGajg8BRA5/Z5KA0AKIxGOXnH80lfOEMOjHjSu3vedhOss3iKyQIm8GuIP4gTIBoQE/H7Rxh6+nH7Z27h93qd9pPi2ALqLdPk/Ymw/tfU+ucIY/qiUiYAChATErRUOjlD9RgmQejLclZsIqNtCH9ZDdlQDg+a8nu1/HhiRhOcqAAAIKAIYQBnnXSADAoMWwX+3N2PGnB7zdlHcoexQ8zHkeHVc66SpBKCMbEL3dAcvsQVk=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423487,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAF49XK23FSh5mZd4QhiWOGTLTc5QPV0BBmo4PAUQOf2eSgNACiMRjl5x/NJXzhDDox40rt73nYTrLN4iskCJvBrhA9SxqM/EUAGvMFgojM+6UTAuoiApysb9eZxEcxU8YFMpvg9iXgc2V/nqLNDYh4HzUZOb/RNm3JgvOtxG7KxgmDriD+IEyAaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnCGP6olImAAoQExK0VDo5Q/UYJkHoy3JWbCKjbQh/WQ3ZUA4PmvJ7tfx4YkYTnKgAACCgCGEAZ510gAwKDFsF/tzdjxpwe83ZR3KHsUPMx5Hh1XOukqQSgjGxC93QHwGlZl"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
  "id": -576460752303423487,
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAF49XK23FSh5mZd4QhiWOGTLTc5QPV0BBmo4PAUQOf2eSgNACiMRjl5x/NJXzhDDox40rt73nYTrLN4iskCJvBrhA9SxqM/EUAGvMFgojM+6UTAuoiApysb9eZxEcxU8YFMpvg9iXgc2V/nqLNDYh4HzUZOb/RNm3JgvOtxG7KxgmDriD+IEyAaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnCGP6olImAAoQExK0VDo5Q/UYJkHoy3JWbCKjbQh/WQ3ZUA4PmvJ7tfx4YkYTnKgAACCgCGEAZ510gAwKDFsF/tzdjxpwe83ZR3KHsUPMx5Hh1XOukqQSgjGxC93QHwGlZl",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_MZ4JE99LBEPjG4oITrNw99I6Y/MRvLjh3LbU9rLFYKS1mD16"
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAF49XK23FSh5mZd4QhiWOGTLTc5QPV0BBmo4PAUQOf2eSgNACiMRjl5x/NJXzhDDox40rt73nYTrLN4iskCJvBrhA9SxqM/EUAGvMFgojM+6UTAuoiApysb9eZxEcxU8YFMpvg9iXgc2V/nqLNDYh4HzUZOb/RNm3JgvOtxG7KxgmDriD+IEyAaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnCGP6olImAAoQExK0VDo5Q/UYJkHoy3JWbCKjbQh/WQ3ZUA4PmvJ7tfx4YkYTnKgAACCgCGEAZ510gAwKDFsF/tzdjxpwe83ZR3KHsUPMx5Hh1XOukqQSgjGxC93QHwGlZl",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAF49XK23FSh5mZd4QhiWOGTLTc5QPV0BBmo4PAUQOf2eSgNACiMRjl5x/NJXzhDDox40rt73nYTrLN4iskCJvBrhA9SxqM/EUAGvMFgojM+6UTAuoiApysb9eZxEcxU8YFMpvg9iXgc2V/nqLNDYh4HzUZOb/RNm3JgvOtxG7KxgmDriD+IEyAaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnCGP6olImAAoQExK0VDo5Q/UYJkHoy3JWbCKjbQh/WQ3ZUA4PmvJ7tfx4YkYTnKgAACCgCGEAZ510gAwKDFsF/tzdjxpwe83ZR3KHsUPMx5Hh1XOukqQSgjGxC93QHwGlZl",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAF49XK23FSh5mZd4QhiWOGTLTc5QPV0BBmo4PAUQOf2eSgNACiMRjl5x/NJXzhDDox40rt73nYTrLN4iskCJvBrhA9SxqM/EUAGvMFgojM+6UTAuoiApysb9eZxEcxU8YFMpvg9iXgc2V/nqLNDYh4HzUZOb/RNm3JgvOtxG7KxgmDriD+IEyAaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnCGP6olImAAoQExK0VDo5Q/UYJkHoy3JWbCKjbQh/WQ3ZUA4PmvJ7tfx4YkYTnKgAACCgCGEAZ510gAwKDFsF/tzdjxpwe83ZR3KHsUPMx5Hh1XOukqQSgjGxC93QHwGlZl",
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
    "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "message": {
        "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
        "from": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
        "info": "Hello",
        "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
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
    "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "message": {
        "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
        "from": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc",
        "info": "Hello back",
        "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
      }
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
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
      "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
  "id": -576460752303423486,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
      "balance": 69999999999999
    },
    {
      "account": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "state": "tx_+QENCwH4hLhAF49XK23FSh5mZd4QhiWOGTLTc5QPV0BBmo4PAUQOf2eSgNACiMRjl5x/NJXzhDDox40rt73nYTrLN4iskCJvBrhA9SxqM/EUAGvMFgojM+6UTAuoiApysb9eZxEcxU8YFMpvg9iXgc2V/nqLNDYh4HzUZOb/RNm3JgvOtxG7KxgmDriD+IEyAaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnCGP6olImAAoQExK0VDo5Q/UYJkHoy3JWbCKjbQh/WQ3ZUA4PmvJ7tfx4YkYTnKgAACCgCGEAZ510gAwKDFsF/tzdjxpwe83ZR3KHsUPMx5Hh1XOukqQSgjGxC93QHwGlZl"
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "state": "tx_+QENCwH4hLhAF49XK23FSh5mZd4QhiWOGTLTc5QPV0BBmo4PAUQOf2eSgNACiMRjl5x/NJXzhDDox40rt73nYTrLN4iskCJvBrhA9SxqM/EUAGvMFgojM+6UTAuoiApysb9eZxEcxU8YFMpvg9iXgc2V/nqLNDYh4HzUZOb/RNm3JgvOtxG7KxgmDriD+IEyAaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnCGP6olImAAoQExK0VDo5Q/UYJkHoy3JWbCKjbQh/WQ3ZUA4PmvJ7tfx4YkYTnKgAACCgCGEAZ510gAwKDFsF/tzdjxpwe83ZR3KHsUPMx5Hh1XOukqQSgjGxC93QHwGlZl"
    }
  },
  "version": 1
}
```
