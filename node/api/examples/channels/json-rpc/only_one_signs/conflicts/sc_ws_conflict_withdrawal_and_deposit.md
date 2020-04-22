
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
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
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
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+L0LAfhCuEAY2qLF5F9uyBBHxKd6MkDplEVHEB9YG0Z2VFR6l8R2X5KM1wUl/uABveNtEo6mmajaUmykDttvDghSVn8185kJuHX4czMBoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03Ta6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUiKWACgDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CgcYcT/2M"
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
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
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
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEBsMu2NcfowUnrpG/BwAuxtxYR7a9Fx9HHi1Kt2M8OJoJ9Uac9594NwcE0sTwAui6s9zTP5wo8VWnAEEr6pG5IEuHT4cjMBoQZUWJjapL3LxLTf6RNqSe+CSmWXOMc9i8GwneZBp03Ta6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgcu3dijj2pyIKHgXbjrR60nqfhl4M5bmQDJOe/StlSPMCQ0z/H9I="
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
