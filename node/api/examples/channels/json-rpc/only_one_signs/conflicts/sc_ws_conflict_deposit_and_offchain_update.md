
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
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBr2j/XUBXzrH54aoG8gkW2gNjecvMWiOVu/WAdbrUsbLAqAh5YXSCzjC3C5f2KaHrz5Qp6zPFnxOBCDOm/SZojmZpapI7+U=",
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
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzMwGhBr2j/XUBXzrH54aoG8gkW2gNjecvMWiOVu/WAdbrUsbLoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gEAhg/FSIpYAKC1alayfwslFfyACzwRJMXq2eZTSjSYytX31L7DbKLsCAKBxqJba/4=",
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
    "signed_tx": "tx_+L0LAfhCuECfhetniCz4HE90BVsrPdN+ZGLZE/ybjRpAfm3NplfCTOpGLI/YxSrKlRc868NOsAcCPP0a18BVr7OEehF9SskJuHX4czMBoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGy6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YBAIYPxUiKWACgtWpWsn8LJRX8gAs8ESTF6tnmU0o0mMrV99S+w2yi7AgCgcaDSCA6"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
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
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
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
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBr2j/XUBXzrH54aoG8gkW2gNjecvMWiOVu/WAdbrUsbLAqBCVQ2rp/+y9mqPBXV6q9fbUVkXc5Dncw8tT8VJHJ/1g9zs9fg=",
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
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBr2j/XUBXzrH54aoG8gkW2gNjecvMWiOVu/WAdbrUsbLoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AEAhg/AoHKQAKCoJj+bYKSyz0epQzKfEIWEyitN2y+r0RCSK1sHENlK2wJDDUYiZQ==",
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
    "signed_tx": "tx_+LwLAfhCuEDYZvougnEtLUSCT5qaGpIhiRyVTb1h/f9RqNNCkD+I9ptmfRnQ8Kb/UzQeoBiM6vfRhfaFPX1+Z0heXu2UeEAOuHT4cjMBoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGy6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvABAIYPwKBykACgqCY/m2Ckss9HqUMynxCFhMorTdsvq9EQkitbBxDZStsCQznLT4c="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
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
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
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
  "method": "channels.deposit",
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
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBr2j/XUBXzrH54aoG8gkW2gNjecvMWiOVu/WAdbrUsbLAqAh5YXSCzjC3C5f2KaHrz5Qp6zPFnxOBCDOm/SZojmZpapI7+U=",
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
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBr2j/XUBXzrH54aoG8gkW2gNjecvMWiOVu/WAdbrUsbLoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AEAhg/AoHKQAKCoJj+bYKSyz0epQzKfEIWEyitN2y+r0RCSK1sHENlK2wJDDUYiZQ==",
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
    "signed_tx": "tx_+JALAfhCuECDuzSJjzqg2q36B3PAm5eBky0cm0ALmLOH8Sripb5N8dzXtf1ySM190r31cwnBq2XQ0EzrohKQ79yWZvX8SsUBuEj4RjkCoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGywKgIeWF0gs4wtwuX9imh68+UKeszxZ8TgQgzpv0maI5maW4Rh5o"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
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
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
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
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBr2j/XUBXzrH54aoG8gkW2gNjecvMWiOVu/WAdbrUsbLAqBCVQ2rp/+y9mqPBXV6q9fbUVkXc5Dncw8tT8VJHJ/1g9zs9fg=",
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
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzMwGhBr2j/XUBXzrH54aoG8gkW2gNjecvMWiOVu/WAdbrUsbLoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gEAhg/FSIpYAKC1alayfwslFfyACzwRJMXq2eZTSjSYytX31L7DbKLsCAKBxqJba/4=",
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
    "signed_tx": "tx_+JALAfhCuED1iGrTLnZjJniombMN4H9Fz0rF/iLByQCtLGzhlETWJwQOFAIkXIqRDUD0Ywy4HzrqMP2uYK/WFbKsMAe8RSwPuEj4RjkCoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGywKgQlUNq6f/svZqjwV1eqvX21FZF3OQ53MPLU/FSRyf9YPr1ov5"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
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
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 1
    }
  },
  "version": 1
}
```
