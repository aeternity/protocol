
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzNAGhBmWNK6aBbShPk6CRMTltOGiGAOZ3qfuG99dqNXQHI+TnoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQEAhg/FSIpYAKBc8Fq8vQL17QIQkeaDvyXfoKq018xDIX6JgEJwAOTDLgKBx9L0lRE=",
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
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBmWNK6aBbShPk6CRMTltOGiGAOZ3qfuG99dqNXQHI+TnoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQEAhg/AoHKQAKAy0nTszKzf77lIkn5X+uulTvYIcbjAZzIHnwDMhDjrhwJDSU0Pzw==",
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
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+L0LAfhCuED5j7K0KxkRbNRvPrgSzSheQOqiG4wurNiiBmShGJL4iKLdUOYLcceGLNqtbekpGJg4Ogtd3ppo89A/OznAdoANuHX4czQBoQZljSumgW0oT5OgkTE5bThohgDmd6n7hvfXajV0ByPk56EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4EBAIYPxUiKWACgXPBavL0C9e0CEJHmg78l36CqtNfMQyF+iYBCcADkwy4CgccZQWv8"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuED2qJDvCwl+okPJSNzoMjb2JL6TR3MSqKi6S/kTUI2aorRqJrXaDElryMxp1K9hNENiSyF4MJfhLo/CI5a+oUMAuHT4cjQBoQZljSumgW0oT5OgkTE5bThohgDmd6n7hvfXajV0ByPk56EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKEBAIYPwKBykACgMtJ07Mys3++5SJJ+V/rrpU72CHG4wGcyB58AzIQ464cCQxsabl8="
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBmWNK6aBbShPk6CRMTltOGiGAOZ3qfuG99dqNXQHI+TnoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQEAhg/AoHKQAKAy0nTszKzf77lIkn5X+uulTvYIcbjAZzIHnwDMhDjrhwJDSU0Pzw==",
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
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzNAGhBmWNK6aBbShPk6CRMTltOGiGAOZ3qfuG99dqNXQHI+TnoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQEAhg/FSIpYAKBc8Fq8vQL17QIQkeaDvyXfoKq018xDIX6JgEJwAOTDLgKBx9L0lRE=",
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
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuED2qJDvCwl+okPJSNzoMjb2JL6TR3MSqKi6S/kTUI2aorRqJrXaDElryMxp1K9hNENiSyF4MJfhLo/CI5a+oUMAuHT4cjQBoQZljSumgW0oT5OgkTE5bThohgDmd6n7hvfXajV0ByPk56EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKEBAIYPwKBykACgMtJ07Mys3++5SJJ+V/rrpU72CHG4wGcyB58AzIQ464cCQxsabl8="
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+L0LAfhCuED5j7K0KxkRbNRvPrgSzSheQOqiG4wurNiiBmShGJL4iKLdUOYLcceGLNqtbekpGJg4Ogtd3ppo89A/OznAdoANuHX4czQBoQZljSumgW0oT5OgkTE5bThohgDmd6n7hvfXajV0ByPk56EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4EBAIYPxUiKWACgXPBavL0C9e0CEJHmg78l36CqtNfMQyF+iYBCcADkwy4CgccZQWv8"
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

#### responder ---> node
```javascript
{
  "id": -576460752303421948,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
  "id": -576460752303421948,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421947,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
  "id": -576460752303421947,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
