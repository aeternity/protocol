
#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 1
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzMwGhBlRYmNqkvcvEtN/pE2pJ74JKZZc4xz2LwbCd5kGnTdNroQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQEAhg/FSIpYAKAanDVQGCuXPzlVQ+bKR+tVrSQ8cp/Sg8IGlohopMti0gKBxtmyUd0=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainDeposit"
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
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBlRYmNqkvcvEtN/pE2pJ74JKZZc4xz2LwbCd5kGnTdNroQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQIAhg/AoHKQAKBy7d2KOPanIgoeBduOtHrSep+GXgzluZAMk579K2VI8wJD0GN4BQ==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainDeposit"
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
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+L0LAfhCuEB3anmOY0fGiiD4wLkEbGSkStwDPaP6TGmAYkhRQYxU3Hm0jl8PJls1Co5Aa/sIw3C3OLnjMX9xYZhY0SAvoxcHuHX4czMBoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03Ta6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4EBAIYPxUiKWACgGpw1UBgrlz85VUPmykfrVa0kPHKf0oPCBpaIaKTLYtICgcY7NS4e"
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

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 1
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBlRYmNqkvcvEtN/pE2pJ74JKZZc4xz2LwbCd5kGnTdNroQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQEAhg/AoHKQAKDTZCPQLXnt5C2s8/L0OFe3FVSuITfnyN5H17qrGsaUsAJDX1dGkA==",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainDeposit"
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
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzMwGhBlRYmNqkvcvEtN/pE2pJ74JKZZc4xz2LwbCd5kGnTdNroQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQIAhg/FSIpYAKAPDv3EgYxO6pJCcB7FVjOvZgsDtaevvDl0iT9iRjxNjgKBxgrB10o=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainDeposit"
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
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEC7eRdogbvVChoTORX7TJvlIPqjfUTDgcVuDNPt2xDi2PPRTyiMqRpMzGEICpV/nlykFmRSOTCDDcn4hZTogpcDuHT4cjMBoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03Ta6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKEBAIYPwKBykACg02Qj0C157eQtrPPy9DhXtxVUriE358jeR9e6qxrGlLACQ8/HMOk="
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
