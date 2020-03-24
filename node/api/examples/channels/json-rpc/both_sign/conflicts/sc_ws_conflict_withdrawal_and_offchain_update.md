
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
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpszgN3bQJjlHjU5M5dfSksrvufO4jsNDPXuf3fDxTsGAqAh5YXSCzjC3C5f2KaHrz5Qp6zPFnxOBCDOm/SZojmZpSQDZh0=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzNAGhBpszgN3bQJjlHjU5M5dfSksrvufO4jsNDPXuf3fDxTsGoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gEAhg/FSIpYAKAKCxwnQ41jnFN2vnly1SF8Wk+btJswuZvrZdj8sEFe0AKBx46nyj0=",
      "updates": [
        {
          "amount": 1,
          "op": "OffChainWithdrawal",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
    "signed_tx": "tx_+L0LAfhCuEAhIHCoITw4uzPEXDXUZU/LsI7O4IP16HhbY0FU/ZrzdsIziCZg5W1yWmpWYGCDA6huVtxLvEj4UUPqI93WGccKuHX4czQBoQabM4Dd20CY5R41OTOXX0pLK77nzuI7DQz17n93w8U7BqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YBAIYPxUiKWACgCgscJ0ONY5xTdr55ctUhfFpPm7SbMLmb62XY/LBBXtACgcczemXx"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBeYdFgJvJG0ABO7Y6zZtR7yGb8alkqS5eye2TVg+POAnAoj2jDw30Hhhv+YwcjRS7EaEgDjJjGocbALZHPlrgLuEj4RjkCoQabM4Dd20CY5R41OTOXX0pLK77nzuI7DQz17n93w8U7BgKgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maX2IUQy"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
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
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
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
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpszgN3bQJjlHjU5M5dfSksrvufO4jsNDPXuf3fDxTsGAqBCVQ2rp/+y9mqPBXV6q9fbUVkXc5Dncw8tT8VJHJ/1gwW7J4Q=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBpszgN3bQJjlHjU5M5dfSksrvufO4jsNDPXuf3fDxTsGoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AEAhg/AoHKQAKAU0fbyfDlUjppBAJxIg2X00zQuv4X3LED0g5/T1x/tKQJDYJ9ckg==",
      "updates": [
        {
          "amount": 1,
          "op": "OffChainWithdrawal",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "signed_tx": "tx_+LwLAfhCuEAZg57T/N5RsiEKz+fqLfim9/LT3XQkKa80rlFckIX7kbHhx3EqUnlv204maIP6tJMGxZ3WVaKQg6+FSD3hAl4AuHT4cjQBoQabM4Dd20CY5R41OTOXX0pLK77nzuI7DQz17n93w8U7BqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvABAIYPwKBykACgFNH28nw5VI6aQQCcSINl9NM0Lr+F9yxA9IOf09cf7SkCQ+IRI0g="
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBdn17gD+MAS3hZbB8BM2u9gBbvIAbplIc+glvXVhKqhsQL0Rq9+rwRjYzA+doXFSZmkHTTj2r7EjhoUZmW2JEHuEj4RjkCoQabM4Dd20CY5R41OTOXX0pLK77nzuI7DQz17n93w8U7BgKgQlUNq6f/svZqjwV1eqvX21FZF3OQ53MPLU/FSRyf9YMoIRmE"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
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
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
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
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpszgN3bQJjlHjU5M5dfSksrvufO4jsNDPXuf3fDxTsGAqAh5YXSCzjC3C5f2KaHrz5Qp6zPFnxOBCDOm/SZojmZpSQDZh0=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBpszgN3bQJjlHjU5M5dfSksrvufO4jsNDPXuf3fDxTsGoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AEAhg/AoHKQAKAU0fbyfDlUjppBAJxIg2X00zQuv4X3LED0g5/T1x/tKQJDYJ9ckg==",
      "updates": [
        {
          "amount": 1,
          "op": "OffChainWithdrawal",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "signed_tx": "tx_+JALAfhCuEABQl10MOkPwjVTe2+DoJxMNal9WKEsj0AZy3NGzBURCqmJnBb0ZjEtyzEzjC5pOc57/Kz7vgSGAOFWPbrZIuULuEj4RjkCoQabM4Dd20CY5R41OTOXX0pLK77nzuI7DQz17n93w8U7BgKgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maVc3GX9"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEAZg57T/N5RsiEKz+fqLfim9/LT3XQkKa80rlFckIX7kbHhx3EqUnlv204maIP6tJMGxZ3WVaKQg6+FSD3hAl4AuHT4cjQBoQabM4Dd20CY5R41OTOXX0pLK77nzuI7DQz17n93w8U7BqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvABAIYPwKBykACgFNH28nw5VI6aQQCcSINl9NM0Lr+F9yxA9IOf09cf7SkCQ+IRI0g="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
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
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
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
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpszgN3bQJjlHjU5M5dfSksrvufO4jsNDPXuf3fDxTsGAqBCVQ2rp/+y9mqPBXV6q9fbUVkXc5Dncw8tT8VJHJ/1gwW7J4Q=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzNAGhBpszgN3bQJjlHjU5M5dfSksrvufO4jsNDPXuf3fDxTsGoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gEAhg/FSIpYAKAKCxwnQ41jnFN2vnly1SF8Wk+btJswuZvrZdj8sEFe0AKBx46nyj0=",
      "updates": [
        {
          "amount": 1,
          "op": "OffChainWithdrawal",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
    "signed_tx": "tx_+JALAfhCuEAnqtWYkxYakOtV2AvDbIiT9kYmdS5Cs9PzmyeN+oMUTLp1X92+QzS9rNk34HvH/khA1fX0HWhhDKJuNLRMD8oIuEj4RjkCoQabM4Dd20CY5R41OTOXX0pLK77nzuI7DQz17n93w8U7BgKgQlUNq6f/svZqjwV1eqvX21FZF3OQ53MPLU/FSRyf9YPvvMgY"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+L0LAfhCuEAhIHCoITw4uzPEXDXUZU/LsI7O4IP16HhbY0FU/ZrzdsIziCZg5W1yWmpWYGCDA6huVtxLvEj4UUPqI93WGccKuHX4czQBoQabM4Dd20CY5R41OTOXX0pLK77nzuI7DQz17n93w8U7BqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YBAIYPxUiKWACgCgscJ0ONY5xTdr55ctUhfFpPm7SbMLmb62XY/LBBXtACgcczemXx"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
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
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 1
    }
  },
  "version": 1
}
```
