
#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_p5mwxAHVY4fqWNqYDvGLfTAWGGra3B4zuNQayyHZZwS9bKrRx",
    "to": "ak_2J29WNS9gzYvK6VWkQQqmAyUu8DH7zHQ1CaN2hZr8B7cxGKNZn"
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
    "from": "ak_p5mwxAHVY4fqWNqYDvGLfTAWGGra3B4zuNQayyHZZwS9bKrRx",
    "to": "ak_2J29WNS9gzYvK6VWkQQqmAyUu8DH7zHQ1CaN2hZr8B7cxGKNZn"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhjcsF+7d2H2XENBMWLFWxkxanu59jyy8nWth32/zpWIBqCPOsUCBsbXXrxKVrsXzeaqJhIzgRdIUBI98K+nHP7Rl158+gw=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_p5mwxAHVY4fqWNqYDvGLfTAWGGra3B4zuNQayyHZZwS9bKrRx",
          "op": "OffChainTransfer",
          "to": "ak_2J29WNS9gzYvK6VWkQQqmAyUu8DH7zHQ1CaN2hZr8B7cxGKNZn"
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
    "signed_tx": "tx_+JALAfhCuEAHhFxkddW3oNkI5rMaEtI/RX/uS4FsU19FF37uxQpFlijWqmKKjcXNoBuSr4m+YZ+t4eodYuEO3wLt0k54QjQMuEj4RjkCoQYY3LBfu3dh9lxDQTFixVsZMWp7ufY8svJ1rYd9v86ViAagjzrFAgbG1168Sla7F83mqiYSM4EXSFASPfCvpxz+0ZfVolHc"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhjcsF+7d2H2XENBMWLFWxkxanu59jyy8nWth32/zpWIBqBQsm+l/H53jPlpVUx70Z/f8Yk+i6NJO570hsLhB6tyA8k4GHs=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_p5mwxAHVY4fqWNqYDvGLfTAWGGra3B4zuNQayyHZZwS9bKrRx",
          "op": "OffChainTransfer",
          "to": "ak_2J29WNS9gzYvK6VWkQQqmAyUu8DH7zHQ1CaN2hZr8B7cxGKNZn"
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
    "signed_tx": "tx_+JALAfhCuEC57/WIQ1F8PYem3yyhUPqlCTdt65MAXDRbpWuxuq3vXI7OuQyxjQAMYesBcYBWmXnXHc1rAbwjI8/i/iURvzYEuEj4RjkCoQYY3LBfu3dh9lxDQTFixVsZMWp7ufY8svJ1rYd9v86ViAagULJvpfx+d4z5aVVMe9Gf3/GJPoujSTue9IbC4QercgNjKX9C"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
    "data": {
      "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
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
    "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
    "data": {
      "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
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
    "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
    "data": {
      "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
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
    "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
    "data": {
      "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
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
    "from": "ak_2J29WNS9gzYvK6VWkQQqmAyUu8DH7zHQ1CaN2hZr8B7cxGKNZn",
    "to": "ak_p5mwxAHVY4fqWNqYDvGLfTAWGGra3B4zuNQayyHZZwS9bKrRx"
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
    "from": "ak_2J29WNS9gzYvK6VWkQQqmAyUu8DH7zHQ1CaN2hZr8B7cxGKNZn",
    "to": "ak_p5mwxAHVY4fqWNqYDvGLfTAWGGra3B4zuNQayyHZZwS9bKrRx"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhjcsF+7d2H2XENBMWLFWxkxanu59jyy8nWth32/zpWIBqDAMok8CJN7O2sMaC8pK9kGEJHFYvNYsOJNMqQT8oD9CUg50kA=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2J29WNS9gzYvK6VWkQQqmAyUu8DH7zHQ1CaN2hZr8B7cxGKNZn",
          "op": "OffChainTransfer",
          "to": "ak_p5mwxAHVY4fqWNqYDvGLfTAWGGra3B4zuNQayyHZZwS9bKrRx"
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
    "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhjcsF+7d2H2XENBMWLFWxkxanu59jyy8nWth32/zpWIBqCKm1223mLB3IPi6z57CtYsUFq8fJaDbQCqifRKIoG+063vEMI=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2J29WNS9gzYvK6VWkQQqmAyUu8DH7zHQ1CaN2hZr8B7cxGKNZn",
          "op": "OffChainTransfer",
          "to": "ak_p5mwxAHVY4fqWNqYDvGLfTAWGGra3B4zuNQayyHZZwS9bKrRx"
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
    "signed_tx": "tx_+JALAfhCuEBp6SPJQ5ERZJFairMzueor38ta2pCwnC0UwrsKw9M64T94eCJFkk9k9UVYopZS1rG0E45wLG/cNll5HrsJClsDuEj4RjkCoQYY3LBfu3dh9lxDQTFixVsZMWp7ufY8svJ1rYd9v86ViAagwDKJPAiTeztrDGgvKSvZBhCRxWLzWLDiTTKkE/KA/QlNlSPU"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDldK1EP2Gn7hZySK9EwMEIFp0egfm/P7eGi9Pucjxdy1ZlRkCu8f9uqcWGLqvof9LMNm41eGbC/NEfRyDm8Z0MuEj4RjkCoQYY3LBfu3dh9lxDQTFixVsZMWp7ufY8svJ1rYd9v86ViAagiptdtt5iwdyD4us+ewrWLFBavHyWg20Aqon0SiKBvtOjgi13"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
    "data": {
      "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
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
    "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
    "data": {
      "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
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
    "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
    "data": {
      "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
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
    "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
    "data": {
      "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423253,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_p5mwxAHVY4fqWNqYDvGLfTAWGGra3B4zuNQayyHZZwS9bKrRx",
      "ak_2J29WNS9gzYvK6VWkQQqmAyUu8DH7zHQ1CaN2hZr8B7cxGKNZn"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
  "id": -576460752303423253,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_p5mwxAHVY4fqWNqYDvGLfTAWGGra3B4zuNQayyHZZwS9bKrRx",
      "balance": 69999999999999
    },
    {
      "account": "ak_2J29WNS9gzYvK6VWkQQqmAyUu8DH7zHQ1CaN2hZr8B7cxGKNZn",
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
    "from": "ak_p5mwxAHVY4fqWNqYDvGLfTAWGGra3B4zuNQayyHZZwS9bKrRx",
    "to": "ak_2J29WNS9gzYvK6VWkQQqmAyUu8DH7zHQ1CaN2hZr8B7cxGKNZn"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhjcsF+7d2H2XENBMWLFWxkxanu59jyy8nWth32/zpWIBqCPOsUCBsbXXrxKVrsXzeaqJhIzgRdIUBI98K+nHP7Rl158+gw=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_p5mwxAHVY4fqWNqYDvGLfTAWGGra3B4zuNQayyHZZwS9bKrRx",
          "op": "OffChainTransfer",
          "to": "ak_2J29WNS9gzYvK6VWkQQqmAyUu8DH7zHQ1CaN2hZr8B7cxGKNZn"
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
  "id": -576460752303423252,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "error": 147
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
  "id": -576460752303423252,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
    "data": {
      "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
      "error_code": 147,
      "error_msg": "user-defined",
      "round": 5
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423251,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_p5mwxAHVY4fqWNqYDvGLfTAWGGra3B4zuNQayyHZZwS9bKrRx",
      "ak_2J29WNS9gzYvK6VWkQQqmAyUu8DH7zHQ1CaN2hZr8B7cxGKNZn"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
  "id": -576460752303423251,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_p5mwxAHVY4fqWNqYDvGLfTAWGGra3B4zuNQayyHZZwS9bKrRx",
      "balance": 69999999999999
    },
    {
      "account": "ak_2J29WNS9gzYvK6VWkQQqmAyUu8DH7zHQ1CaN2hZr8B7cxGKNZn",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```

#### responder closes WebSocket connection
```

```
