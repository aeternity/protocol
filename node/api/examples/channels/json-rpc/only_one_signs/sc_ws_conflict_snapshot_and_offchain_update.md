
#### initiator ---> node
```javascript
{
  "id": -576460752303421963,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
  "id": -576460752303421963,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999999
    },
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
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
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlRYmNqkvcvEtN/pE2pJ74JKZZc4xz2LwbCd5kGnTdNrAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyow1kCU=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainTransfer",
          "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
  "id": -576460752303421962,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDBa/i5RerkJ7GTgj5sAa+Bxe5Lg9p5kSIBkd/TSvsFa32Kp7mR9EdsknZ53fat08IOgmdZg+CHTfVdote7SZwKuEj4RjkCoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03TawKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqPwRRH"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
  "id": -576460752303421962,
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
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
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
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDBa/i5RerkJ7GTgj5sAa+Bxe5Lg9p5kSIBkd/TSvsFa32Kp7mR9EdsknZ53fat08IOgmdZg+CHTfVdote7SZwKuEj4RjkCoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03TawKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqPwRRH",
      "updates": [
        {
          "amount": 1,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainTransfer",
          "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
  "id": -576460752303421961,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAXWgtzTV/A7CVowPVgGf3A+MNBpdVTyo86+OcyXKrq0rw91BorymFdnO7CcsnySNdrNuIw927/3oQ/85QfnhoPuEDBa/i5RerkJ7GTgj5sAa+Bxe5Lg9p5kSIBkd/TSvsFa32Kp7mR9EdsknZ53fat08IOgmdZg+CHTfVdote7SZwKuEj4RjkCoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03TawKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoO5xEp"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
  "id": -576460752303421961,
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
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "state": "tx_+NILAfiEuEAXWgtzTV/A7CVowPVgGf3A+MNBpdVTyo86+OcyXKrq0rw91BorymFdnO7CcsnySNdrNuIw927/3oQ/85QfnhoPuEDBa/i5RerkJ7GTgj5sAa+Bxe5Lg9p5kSIBkd/TSvsFa32Kp7mR9EdsknZ53fat08IOgmdZg+CHTfVdote7SZwKuEj4RjkCoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03TawKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoO5xEp"
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
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "state": "tx_+NILAfiEuEAXWgtzTV/A7CVowPVgGf3A+MNBpdVTyo86+OcyXKrq0rw91BorymFdnO7CcsnySNdrNuIw927/3oQ/85QfnhoPuEDBa/i5RerkJ7GTgj5sAa+Bxe5Lg9p5kSIBkd/TSvsFa32Kp7mR9EdsknZ53fat08IOgmdZg+CHTfVdote7SZwKuEj4RjkCoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03TawKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoO5xEp"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421960,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
  "id": -576460752303421960,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999998
    },
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421959,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
  "id": -576460752303421959,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAXWgtzTV/A7CVowPVgGf3A+MNBpdVTyo86+OcyXKrq0rw91BorymFdnO7CcsnySNdrNuIw927/3oQ/85QfnhoPuEDBa/i5RerkJ7GTgj5sAa+Bxe5Lg9p5kSIBkd/TSvsFa32Kp7mR9EdsknZ53fat08IOgmdZg+CHTfVdote7SZwKuEj4RjkCoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03TawKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsoO5xEp",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAArDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX/6cxp+Z"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421958,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
  "id": -576460752303421958,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000002
    },
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
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
    "amount": 1,
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlRYmNqkvcvEtN/pE2pJ74JKZZc4xz2LwbCd5kGnTdNrA6Bk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RkxUbyw=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
          "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "id": -576460752303421957,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBuAJSV2LikNWrGPNlk1fjIlxkxczc64RAdVXNvHzbuDuQlBlXcnDAqRyODcPJDrCdSw7rAbKMCpdE2aL99uvMOuEj4RjkCoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03TawOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaPAcVy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
  "id": -576460752303421957,
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
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
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
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBuAJSV2LikNWrGPNlk1fjIlxkxczc64RAdVXNvHzbuDuQlBlXcnDAqRyODcPJDrCdSw7rAbKMCpdE2aL99uvMOuEj4RjkCoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03TawOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEaPAcVy",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
          "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "id": -576460752303421956,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBuAJSV2LikNWrGPNlk1fjIlxkxczc64RAdVXNvHzbuDuQlBlXcnDAqRyODcPJDrCdSw7rAbKMCpdE2aL99uvMOuEDVzLxtVTdo/GnxiAbOCLuX1/QR8W8kiXKXoWnoXL1FjEjqWgqIU1mB89BPtQKy5qGlIUmL19S90WnMmdOFJNkAuEj4RjkCoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03TawOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbpyq3J"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
  "id": -576460752303421956,
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
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "state": "tx_+NILAfiEuEBuAJSV2LikNWrGPNlk1fjIlxkxczc64RAdVXNvHzbuDuQlBlXcnDAqRyODcPJDrCdSw7rAbKMCpdE2aL99uvMOuEDVzLxtVTdo/GnxiAbOCLuX1/QR8W8kiXKXoWnoXL1FjEjqWgqIU1mB89BPtQKy5qGlIUmL19S90WnMmdOFJNkAuEj4RjkCoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03TawOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbpyq3J"
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
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "state": "tx_+NILAfiEuEBuAJSV2LikNWrGPNlk1fjIlxkxczc64RAdVXNvHzbuDuQlBlXcnDAqRyODcPJDrCdSw7rAbKMCpdE2aL99uvMOuEDVzLxtVTdo/GnxiAbOCLuX1/QR8W8kiXKXoWnoXL1FjEjqWgqIU1mB89BPtQKy5qGlIUmL19S90WnMmdOFJNkAuEj4RjkCoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03TawOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbpyq3J"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421955,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
  "id": -576460752303421955,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
      "balance": 40000000000001
    },
    {
      "account": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421954,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
  "id": -576460752303421954,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBuAJSV2LikNWrGPNlk1fjIlxkxczc64RAdVXNvHzbuDuQlBlXcnDAqRyODcPJDrCdSw7rAbKMCpdE2aL99uvMOuEDVzLxtVTdo/GnxiAbOCLuX1/QR8W8kiXKXoWnoXL1FjEjqWgqIU1mB89BPtQKy5qGlIUmL19S90WnMmdOFJNkAuEj4RjkCoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03TawOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEbpyq3J",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoYvKCgEAhiRhOcqAAbDvQAGgZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4GLygoBAIY/qiUiX//wlybK"
  },
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
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlRYmNqkvcvEtN/pE2pJ74JKZZc4xz2LwbCd5kGnTdNrBKCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCynZL+y0=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainTransfer",
          "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBlRYmNqkvcvEtN/pE2pJ74JKZZc4xz2LwbCd5kGnTdNroQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwobjU+NILAfiEuEBuAJSV2LikNWrGPNlk1fjIlxkxczc64RAdVXNvHzbuDuQlBlXcnDAqRyODcPJDrCdSw7rAbKMCpdE2aL99uvMOuEDVzLxtVTdo/GnxiAbOCLuX1/QR8W8kiXKXoWnoXL1FjEjqWgqIU1mB89BPtQKy5qGlIUmL19S90WnMmdOFJNkAuEj4RjkCoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03TawOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYAhhMG0SswAEPUgYQe",
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
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBc1zOuu7X5xlSnz3J2S89sPwlIyM9+aIPG5EYLuerxHlNivH4IIpVPsKTO9LWYbA9JfewD41My4D7Syv66XFIEuEj4RjkCoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03TawSgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsrBYZdv"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 3
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 3
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlRYmNqkvcvEtN/pE2pJ74JKZZc4xz2LwbCd5kGnTdNrBKDdqOzEXWz8Y2itvyrEosD88v7VNFxfGdbGSLDDea6BYP3VT0M=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
          "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "signed_tx": "tx_+QEvCwHAuQEp+QEmOwGhBlRYmNqkvcvEtN/pE2pJ74JKZZc4xz2LwbCd5kGnTdNroQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgbjU+NILAfiEuEBuAJSV2LikNWrGPNlk1fjIlxkxczc64RAdVXNvHzbuDuQlBlXcnDAqRyODcPJDrCdSw7rAbKMCpdE2aL99uvMOuEDVzLxtVTdo/GnxiAbOCLuX1/QR8W8kiXKXoWnoXL1FjEjqWgqIU1mB89BPtQKy5qGlIUmL19S90WnMmdOFJNkAuEj4RjkCoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03TawOgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYAhhMLeUL4AIHGTpx9Hg==",
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
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECqBWBSilwbYsaMhxne/y2rEdZ8IeHkGxv5KggIIkxed1E1ykwnP1vDwHVTIlSpcwf3a5aR8U9FUwKIniAc2ncCuEj4RjkCoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03TawSg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWDtGlTC"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 3
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 3
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421953,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
  "id": -576460752303421953,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421952,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
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
  "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
  "id": -576460752303421952,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
