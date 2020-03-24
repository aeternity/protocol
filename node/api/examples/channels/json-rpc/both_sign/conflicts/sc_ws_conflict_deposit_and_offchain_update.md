
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
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzMwGhBpszgN3bQJjlHjU5M5dfSksrvufO4jsNDPXuf3fDxTsGoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gEAhg/FSIpYAKC1alayfwslFfyACzwRJMXq2eZTSjSYytX31L7DbKLsCAKBx8JRu4M=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
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
    "signed_tx": "tx_+L0LAfhCuEDFtlh7Teg9w8yKy+TNq3ZRfDr/FTrV+81UTWd7D3v3Jar50Z5m6xR6srYmXBf+wAKxQMqa4NlZsp/ghiA/1ssBuHX4czMBoQabM4Dd20CY5R41OTOXX0pLK77nzuI7DQz17n93w8U7BqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YBAIYPxUiKWACgtWpWsn8LJRX8gAs8ESTF6tnmU0o0mMrV99S+w2yi7AgCgccqEnCQ"
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
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBpszgN3bQJjlHjU5M5dfSksrvufO4jsNDPXuf3fDxTsGoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AEAhg/AoHKQAKCoJj+bYKSyz0epQzKfEIWEyitN2y+r0RCSK1sHENlK2wJDHb+dEw==",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
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
    "signed_tx": "tx_+LwLAfhCuEDqn/8ALyLcEAiSpcVmn9CM0BU7yEuWJZOJ+l4ZjzbylfM/YPznbqQaW+ZXXM3JnyakAaXGK7OVZJoUJ7IBX5sJuHT4cjMBoQabM4Dd20CY5R41OTOXX0pLK77nzuI7DQz17n93w8U7BqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvABAIYPwKBykACgqCY/m2Ckss9HqUMynxCFhMorTdsvq9EQkitbBxDZStsCQ8At2lw="
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
  "method": "channels.update.new",
  "params": {
    "amount": 2,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBpszgN3bQJjlHjU5M5dfSksrvufO4jsNDPXuf3fDxTsGoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AEAhg/AoHKQAKCoJj+bYKSyz0epQzKfEIWEyitN2y+r0RCSK1sHENlK2wJDHb+dEw==",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
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
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEDqn/8ALyLcEAiSpcVmn9CM0BU7yEuWJZOJ+l4ZjzbylfM/YPznbqQaW+ZXXM3JnyakAaXGK7OVZJoUJ7IBX5sJuHT4cjMBoQabM4Dd20CY5R41OTOXX0pLK77nzuI7DQz17n93w8U7BqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvABAIYPwKBykACgqCY/m2Ckss9HqUMynxCFhMorTdsvq9EQkitbBxDZStsCQ8At2lw="
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
  "method": "channels.update.new",
  "params": {
    "amount": 2,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

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
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzMwGhBpszgN3bQJjlHjU5M5dfSksrvufO4jsNDPXuf3fDxTsGoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gEAhg/FSIpYAKC1alayfwslFfyACzwRJMXq2eZTSjSYytX31L7DbKLsCAKBx8JRu4M=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
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
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+L0LAfhCuEDFtlh7Teg9w8yKy+TNq3ZRfDr/FTrV+81UTWd7D3v3Jar50Z5m6xR6srYmXBf+wAKxQMqa4NlZsp/ghiA/1ssBuHX4czMBoQabM4Dd20CY5R41OTOXX0pLK77nzuI7DQz17n93w8U7BqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YBAIYPxUiKWACgtWpWsn8LJRX8gAs8ESTF6tnmU0o0mMrV99S+w2yi7AgCgccqEnCQ"
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
