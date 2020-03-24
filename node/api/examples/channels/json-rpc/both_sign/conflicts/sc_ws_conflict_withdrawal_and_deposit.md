
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

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBpszgN3bQJjlHjU5M5dfSksrvufO4jsNDPXuf3fDxTsGoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AIAhg/AoHKQAKDqgdNkuhddveVDE/es1N/fevZuJ9NTBtOGxk/KimI/YwJDE24ySA==",
      "updates": [
        {
          "amount": 2,
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
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEBgnHD2sxS8ja46f2twArvANmLiKqi7IT6LBR0Qjv5Vqzf40HgheCQAf0iQBoPhR8229N0xM9Tug/9vanOCWRYOuHT4cjMBoQabM4Dd20CY5R41OTOXX0pLK77nzuI7DQz17n93w8U7BqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACg6oHTZLoXXb3lQxP3rNTf33r2bifTUwbThsZPyopiP2MCQxQSvdw="
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

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzMwGhBpszgN3bQJjlHjU5M5dfSksrvufO4jsNDPXuf3fDxTsGoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gIAhg/FSIpYAKAJfKOkRYFmCfu9WWBbxU0n1wqMcA3FNf3vEd2/gK5qlQKBx9Lhy3g=",
      "updates": [
        {
          "amount": 2,
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
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+L0LAfhCuEBjNY1YrA8bhX6C6aSUGsagRE3n18v918jKyE1naGavYCSjU3paHvKOdNxLHgV7kmnjok8iRAA2f9r2yoMfNOIHuHX4czMBoQabM4Dd20CY5R41OTOXX0pLK77nzuI7DQz17n93w8U7BqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUiKWACgCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCgccxJZQo"
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
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzMwGhBpszgN3bQJjlHjU5M5dfSksrvufO4jsNDPXuf3fDxTsGoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gIAhg/FSIpYAKAJfKOkRYFmCfu9WWBbxU0n1wqMcA3FNf3vEd2/gK5qlQKBx9Lhy3g=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
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
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+L0LAfhCuEBjNY1YrA8bhX6C6aSUGsagRE3n18v918jKyE1naGavYCSjU3paHvKOdNxLHgV7kmnjok8iRAA2f9r2yoMfNOIHuHX4czMBoQabM4Dd20CY5R41OTOXX0pLK77nzuI7DQz17n93w8U7BqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUiKWACgCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCgccxJZQo"
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

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_2BMQYgssMhC6X6vrZ4vwdoqMo5yAasWyUCTqY1rB4MLtqYXZQU",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBpszgN3bQJjlHjU5M5dfSksrvufO4jsNDPXuf3fDxTsGoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AIAhg/AoHKQAKDqgdNkuhddveVDE/es1N/fevZuJ9NTBtOGxk/KimI/YwJDE24ySA==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
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
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEBgnHD2sxS8ja46f2twArvANmLiKqi7IT6LBR0Qjv5Vqzf40HgheCQAf0iQBoPhR8229N0xM9Tug/9vanOCWRYOuHT4cjMBoQabM4Dd20CY5R41OTOXX0pLK77nzuI7DQz17n93w8U7BqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACg6oHTZLoXXb3lQxP3rNTf33r2bifTUwbThsZPyopiP2MCQxQSvdw="
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
