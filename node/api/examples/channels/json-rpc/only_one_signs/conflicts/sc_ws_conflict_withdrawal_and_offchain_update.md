
#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 1
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

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzNAGhBlRYmNqkvcvEtN/pE2pJ74JKZZc4xz2LwbCd5kGnTdNroQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQEAhg/FSIpYAKBc8Fq8vQL17QIQkeaDvyXfoKq018xDIX6JgEJwAOTDLgKBxqSA/C0=",
      "updates": [
        {
          "amount": 1,
          "op": "OffChainWithdrawal",
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
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+L0LAfhCuEAMgjbhcfbQDD5E0gbIUopOutAceV+KvLNFT2EwedawBEZEWqUyxJhiwovs9ez8wQIwX8v/4bmDWvWV1Wx8/TUNuHX4czQBoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03Ta6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4EBAIYPxUiKWACgXPBavL0C9e0CEJHmg78l36CqtNfMQyF+iYBCcADkwy4Cgca/7eqY"
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
  "method": "channels.withdraw",
  "params": {
    "amount": 1
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

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBlRYmNqkvcvEtN/pE2pJ74JKZZc4xz2LwbCd5kGnTdNroQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQEAhg/AoHKQAKAy0nTszKzf77lIkn5X+uulTvYIcbjAZzIHnwDMhDjrhwJDmGZcKw==",
      "updates": [
        {
          "amount": 1,
          "op": "OffChainWithdrawal",
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
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuECqBt2s4pXPaE0fjhDPxAL8X/OI4vziEoybxVcIwk2hUhnUfnxWUF4A2x5aWvIzgbKnkVDxrnKP3OxdoPafxCYHuHT4cjQBoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03Ta6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKEBAIYPwKBykACgMtJ07Mys3++5SJJ+V/rrpU72CHG4wGcyB58AzIQ464cCQyvFD/U="
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

#### initiator ---> node
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

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 1
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

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBlRYmNqkvcvEtN/pE2pJ74JKZZc4xz2LwbCd5kGnTdNroQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQEAhg/AoHKQAKAy0nTszKzf77lIkn5X+uulTvYIcbjAZzIHnwDMhDjrhwJDmGZcKw==",
      "updates": [
        {
          "amount": 1,
          "op": "OffChainWithdrawal",
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
    "signed_tx": "tx_+JALAfhCuEDwQuQOAvZ9ctfA6fgckiS1r9EpPE7rcicn1+OD0JmZJKTSlSOKAXrDcJZ/z7y2+oxGYrmLI67O2FUUu5HjQGgFuEj4RjkCoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03TawKgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXwqi+AH"
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
  "method": "channels.withdraw",
  "params": {
    "amount": 1
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

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_e9WS8RaZmcCFhk2vZyHM53z6FHrBvniXvrMjfRZkrUNDjVHKg",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzNAGhBlRYmNqkvcvEtN/pE2pJ74JKZZc4xz2LwbCd5kGnTdNroQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQEAhg/FSIpYAKBc8Fq8vQL17QIQkeaDvyXfoKq018xDIX6JgEJwAOTDLgKBxqSA/C0=",
      "updates": [
        {
          "amount": 1,
          "op": "OffChainWithdrawal",
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
    "signed_tx": "tx_+JALAfhCuECOBWkw6X3/hSfwhodp3PVXa7Mqo8vmCh5iY3AadOYZ3Bt6wpIVo+7Xlox383kz9dlwF0Ga9/3eMIdsMa+w3toOuEj4RjkCoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03TawKg1q4YSDUxKCS8PNo/X/QZPrzZkpMcj6xjad8GD3rTCnzPQoAK"
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
