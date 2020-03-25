
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmWNK6aBbShPk6CRMTltOGiGAOZ3qfuG99dqNXQHI+TnAqCyPuq+gQA2a6qmnwMyrfvY3kyHmlBoHoJrMzYXSPbNfOBz3I8=",
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
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAxuAhwq5s44/ym96QALIdYGERoITUJTaZL4r5hZKfe32zzeKsBQAo22x+TiE29oA09xoqvITv+hdpezk9VMa8CuEj4RjkCoQZljSumgW0oT5OgkTE5bThohgDmd6n7hvfXajV0ByPk5wKgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXzD8+qW"
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmWNK6aBbShPk6CRMTltOGiGAOZ3qfuG99dqNXQHI+TnAqDWrhhINTEoJLw82j9f9Bk+vNmSkxyPrGNp3wYPetMKfGuqKV4=",
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
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEALY5WoWnCoRqxZr7aE04XjMu9+7kQCVsQK3GePnzW/uWuP6Fru3WlLfBie/I7h7rU4cWH6EBAjWTkSgbp8SpMFuEj4RjkCoQZljSumgW0oT5OgkTE5bThohgDmd6n7hvfXajV0ByPk5wKg1q4YSDUxKCS8PNo/X/QZPrzZkpMcj6xjad8GD3rTCny2HOSg"
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
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmWNK6aBbShPk6CRMTltOGiGAOZ3qfuG99dqNXQHI+TnAqCyPuq+gQA2a6qmnwMyrfvY3kyHmlBoHoJrMzYXSPbNfOBz3I8=",
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
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBuImWQzWSFnHHt4i8Wn5fh91vhjBdBmWE149wRsWoC0x2kBx+vamXc8ADNVPPYy7GbfD87YZKqx/BA6TxtovYMuEj4RjkCoQZljSumgW0oT5OgkTE5bThohgDmd6n7hvfXajV0ByPk5wKgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXybEAf8"
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmWNK6aBbShPk6CRMTltOGiGAOZ3qfuG99dqNXQHI+TnAqDWrhhINTEoJLw82j9f9Bk+vNmSkxyPrGNp3wYPetMKfGuqKV4=",
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
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBGcQumQvw8ShAgoc9kHCzCM8Si+wxTY8ZbdVuUwQfpg4+dy7VPKlL7Tz6ubwnG5rlfJf+9NR6LJge5eRnXdGEJuEj4RjkCoQZljSumgW0oT5OgkTE5bThohgDmd6n7hvfXajV0ByPk5wKg1q4YSDUxKCS8PNo/X/QZPrzZkpMcj6xjad8GD3rTCnzBuMnL"
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
