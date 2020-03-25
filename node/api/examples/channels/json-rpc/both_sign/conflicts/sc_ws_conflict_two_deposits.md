
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzMwGhBmWNK6aBbShPk6CRMTltOGiGAOZ3qfuG99dqNXQHI+TnoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQEAhg/FSIpYAKAanDVQGCuXPzlVQ+bKR+tVrSQ8cp/Sg8IGlohopMti0gKBx9ExuJw=",
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBmWNK6aBbShPk6CRMTltOGiGAOZ3qfuG99dqNXQHI+TnoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQIAhg/AoHKQAKBy7d2KOPanIgoeBduOtHrSep+GXgzluZAMk579K2VI8wJDVQa5ZQ==",
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
    "signed_tx": "tx_+L0LAfhCuEA9ScwlsJrunrYoRc9IA1IL07kwAkxukxWtPNscECYayLoF4uOczZFmya1UBmUcj15GNlOt9izgpHucESw8Ef4BuHX4czMBoQZljSumgW0oT5OgkTE5bThohgDmd6n7hvfXajV0ByPk56EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4EBAIYPxUiKWACgGpw1UBgrlz85VUPmykfrVa0kPHKf0oPCBpaIaKTLYtICgcdGxzkD"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEA3WkFKstHVWnRx4CBvMCMdyQkFLN1CZbJYrVFdd4ilrFdbPWDJkT4+ZL0y8lZ1Ln8piaOd+X57TwdxNc0fei8CuHT4cjMBoQZljSumgW0oT5OgkTE5bThohgDmd6n7hvfXajV0ByPk56EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgcu3dijj2pyIKHgXbjrR60nqfhl4M5bmQDJOe/StlSPMCQ3G2Y7E="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
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
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBmWNK6aBbShPk6CRMTltOGiGAOZ3qfuG99dqNXQHI+TnoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQEAhg/AoHKQAKDTZCPQLXnt5C2s8/L0OFe3FVSuITfnyN5H17qrGsaUsAJDZ17s9A==",
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzMwGhBmWNK6aBbShPk6CRMTltOGiGAOZ3qfuG99dqNXQHI+TnoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQIAhg/FSIpYAKAPDv3EgYxO6pJCcB7FVjOvZgsDtaevvDl0iT9iRjxNjgKBxw9wOYQ=",
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
    "signed_tx": "tx_+LwLAfhCuEBknFBB3mXItT9k95xlw/j74sounkSqX9r7Q0dTnVRsWe2asm5OsV86wMinQhObqxj8lwX7FY5cyme/EXvSQc4NuHT4cjMBoQZljSumgW0oT5OgkTE5bThohgDmd6n7hvfXajV0ByPk56EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKEBAIYPwKBykACg02Qj0C157eQtrPPy9DhXtxVUriE358jeR9e6qxrGlLACQ4Jkpi4="
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+L0LAfhCuEB/6asL6oMzmXyf8oTKatzNqncsWnZCJqGqEG4+QtiHM3DPx19Xx64VdpP2aZvRg920PkebcXGb6UXS/WFqyBwKuHX4czMBoQZljSumgW0oT5OgkTE5bThohgDmd6n7hvfXajV0ByPk56EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPxUiKWACgDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4Cgcf8ASZ3"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 1
    }
  },
  "version": 1
}
```
