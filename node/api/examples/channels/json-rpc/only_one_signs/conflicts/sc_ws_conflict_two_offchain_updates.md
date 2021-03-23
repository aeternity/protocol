
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
  "method": "channels.update.new",
  "params": {
    "amount": 2,
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

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlRYmNqkvcvEtN/pE2pJ74JKZZc4xz2LwbCd5kGnTdNrAqCyPuq+gQA2a6qmnwMyrfvY3kyHmlBoHoJrMzYXSPbNfJhCJX8=",
      "updates": [
        {
          "amount": 2,
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
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDBa/i5RerkJ7GTgj5sAa+Bxe5Lg9p5kSIBkd/TSvsFa32Kp7mR9EdsknZ53fat08IOgmdZg+CHTfVdote7SZwKuEj4RjkCoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03TawKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQsqPwRRH"
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
      "round": 1
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
      "round": 1
    }
  },
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

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 2,
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlRYmNqkvcvEtN/pE2pJ74JKZZc4xz2LwbCd5kGnTdNrAqDdqOzEXWz8Y2itvyrEosD88v7VNFxfGdbGSLDDea6BYJganQw=",
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
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlRYmNqkvcvEtN/pE2pJ74JKZZc4xz2LwbCd5kGnTdNrAqDWrhhINTEoJLw82j9f9Bk+vNmSkxyPrGNp3wYPetMKfJADQOU=",
      "updates": [
        {
          "amount": 2,
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
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECfcDTvmKMmEURL1Bdy+5WpCcHjpQlL5j/wPEXODI+JpSMOS2fRJLI1uXBsHYXQZn2uo0jEejcAaKvgCdUPOGsCuEj4RjkCoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03TawKg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWDpmQHh"
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
      "round": 1
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
      "round": 1
    }
  },
  "version": 1
}
```
