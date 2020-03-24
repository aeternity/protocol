
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
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzNAGhBr2j/XUBXzrH54aoG8gkW2gNjecvMWiOVu/WAdbrUsbLoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gEAhg/FSIpYAKAKCxwnQ41jnFN2vnly1SF8Wk+btJswuZvrZdj8sEFe0AKBxgAREBI=",
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
    "signed_tx": "tx_+L0LAfhCuEAj3araWrSr46wFYVyeQY/5gK348hTUE1MG1nmDonOH9El08SifWmDq63a2Q9AEWsUSefbh+6oa289/i0ClcFMOuHX4czQBoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGy6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YBAIYPxUiKWACgCgscJ0ONY5xTdr55ctUhfFpPm7SbMLmb62XY/LBBXtACgcaIgfIp"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "signed_tx": "tx_+L0LAfhCuEAj3araWrSr46wFYVyeQY/5gK348hTUE1MG1nmDonOH9El08SifWmDq63a2Q9AEWsUSefbh+6oa289/i0ClcFMOuHX4czQBoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGy6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YBAIYPxUiKWACgCgscJ0ONY5xTdr55ctUhfFpPm7SbMLmb62XY/LBBXtACgcaIgfIp",
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
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBr2j/XUBXzrH54aoG8gkW2gNjecvMWiOVu/WAdbrUsbLoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AEAhg/AoHKQAKAU0fbyfDlUjppBAJxIg2X00zQuv4X3LED0g5/T1x/tKQJD1totWg==",
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
    "signed_tx": "tx_+LwLAfhCuEAMDP7Q7iU7Z9FDseTmDld58/K9vmnqQL/sfUVI+tLgb15pZT7uCQD5EdLKf88wAxh6IA7U4iYc+gY9ASkilkULuHT4cjQBoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGy6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvABAIYPwKBykACgFNH28nw5VI6aQQCcSINl9NM0Lr+F9yxA9IOf09cf7SkCQ3cTfMM="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEAMDP7Q7iU7Z9FDseTmDld58/K9vmnqQL/sfUVI+tLgb15pZT7uCQD5EdLKf88wAxh6IA7U4iYc+gY9ASkilkULuHT4cjQBoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGy6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvABAIYPwKBykACgFNH28nw5VI6aQQCcSINl9NM0Lr+F9yxA9IOf09cf7SkCQ3cTfMM=",
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
