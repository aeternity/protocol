
#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpszgN3bQJjlHjU5M5dfSksrvufO4jsNDPXuf3fDxTsGAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAocc1H8=",
      "updates": [
        {
          "amount": 1,
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

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBMubrYl6bpw2+xmdCOAQIcURn8VF1OG8KM3fQ7Cad6acXeCqDbvFMRP6DsLiMwwpczCRJI6goSyamGeSnXC5IBuEj4RjkCoQabM4Dd20CY5R41OTOXX0pLK77nzuI7DQz17n93w8U7BgKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIA+Bot"
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

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpszgN3bQJjlHjU5M5dfSksrvufO4jsNDPXuf3fDxTsGAqCPVbQrAfYXrWTP0iwmtWIe9nj7Tuv+WHg7LyUfwRTSMRPBBuY=",
      "updates": [
        {
          "amount": 1,
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

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED2R00ftpv/9sUiQlQH2zTo986zx77KnNGVZmPQhar8G3ON0/jnbFnVoRUrqCqkckVX91j0QnQKyJQi24P4yTELuEj4RjkCoQabM4Dd20CY5R41OTOXX0pLK77nzuI7DQz17n93w8U7BgKgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jEeLuMO"
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
