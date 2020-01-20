
#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello",
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "message": {
        "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "info": "Hello",
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "message": {
        "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "info": "Hello back",
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
      }
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
    "amount": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.withdraw",
      "params": {
        "amount": "2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello",
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "message": {
        "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "info": "Hello",
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "message": {
        "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "info": "Hello back",
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
      }
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
    "amount": 2,
    "meta": [
      "meta 1"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBmV3F8qHwm7xU8x22yKQLWC+6gL8XPoMYX+53e5gtWpBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79AIAhg/AoHKQAKBMSARLSaHzo+h5n1ef+RLlEfjdC1m6OX2fxx0W5FSO9gkeIx3cEQ==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423109,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEDCV+OqAPziSetOu2PNpc5QwyeWRhdqn88q1T0xdkPYJqsSKe2lgWYksbDMhSGIYVWQA7xw88uhnK1hxcjDZ+IDuHT4cjQBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgTEgES0mh86PoeZ9Xn/kS5RH43QtZujl9n8cdFuRUjvYJHrnI6n4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423109,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEDCV+OqAPziSetOu2PNpc5QwyeWRhdqn88q1T0xdkPYJqsSKe2lgWYksbDMhSGIYVWQA7xw88uhnK1hxcjDZ+IDuHT4cjQBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgTEgES0mh86PoeZ9Xn/kS5RH43QtZujl9n8cdFuRUjvYJHrnI6n4=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423108,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEB1aFKLVrMb0FFh2DBWTU9ls4BV52ac59RfgvJ4obNHjzqvyuW2QxOo/KNGMjqh47udAbdl1sZUTgfHSllWvdoHuEDCV+OqAPziSetOu2PNpc5QwyeWRhdqn88q1T0xdkPYJqsSKe2lgWYksbDMhSGIYVWQA7xw88uhnK1hxcjDZ+IDuHT4cjQBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgTEgES0mh86PoeZ9Xn/kS5RH43QtZujl9n8cdFuRUjvYJHgvQLKc="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423108,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEB1aFKLVrMb0FFh2DBWTU9ls4BV52ac59RfgvJ4obNHjzqvyuW2QxOo/KNGMjqh47udAbdl1sZUTgfHSllWvdoHuEDCV+OqAPziSetOu2PNpc5QwyeWRhdqn88q1T0xdkPYJqsSKe2lgWYksbDMhSGIYVWQA7xw88uhnK1hxcjDZ+IDuHT4cjQBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgTEgES0mh86PoeZ9Xn/kS5RH43QtZujl9n8cdFuRUjvYJHgvQLKc=",
      "type": "channel_withdraw_tx"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEB1aFKLVrMb0FFh2DBWTU9ls4BV52ac59RfgvJ4obNHjzqvyuW2QxOo/KNGMjqh47udAbdl1sZUTgfHSllWvdoHuEDCV+OqAPziSetOu2PNpc5QwyeWRhdqn88q1T0xdkPYJqsSKe2lgWYksbDMhSGIYVWQA7xw88uhnK1hxcjDZ+IDuHT4cjQBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgTEgES0mh86PoeZ9Xn/kS5RH43QtZujl9n8cdFuRUjvYJHgvQLKc=",
      "type": "channel_withdraw_tx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello",
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "message": {
        "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "info": "Hello",
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "message": {
        "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "info": "Hello back",
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
      }
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEB1aFKLVrMb0FFh2DBWTU9ls4BV52ac59RfgvJ4obNHjzqvyuW2QxOo/KNGMjqh47udAbdl1sZUTgfHSllWvdoHuEDCV+OqAPziSetOu2PNpc5QwyeWRhdqn88q1T0xdkPYJqsSKe2lgWYksbDMhSGIYVWQA7xw88uhnK1hxcjDZ+IDuHT4cjQBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgTEgES0mh86PoeZ9Xn/kS5RH43QtZujl9n8cdFuRUjvYJHgvQLKc=",
      "type": "channel_withdraw_tx"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEB1aFKLVrMb0FFh2DBWTU9ls4BV52ac59RfgvJ4obNHjzqvyuW2QxOo/KNGMjqh47udAbdl1sZUTgfHSllWvdoHuEDCV+OqAPziSetOu2PNpc5QwyeWRhdqn88q1T0xdkPYJqsSKe2lgWYksbDMhSGIYVWQA7xw88uhnK1hxcjDZ+IDuHT4cjQBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgTEgES0mh86PoeZ9Xn/kS5RH43QtZujl9n8cdFuRUjvYJHgvQLKc=",
      "type": "channel_withdraw_tx"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "event": "own_withdraw_locked"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "event": "own_withdraw_locked"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "event": "withdraw_locked"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "event": "withdraw_locked"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "state": "tx_+P4LAfiEuEB1aFKLVrMb0FFh2DBWTU9ls4BV52ac59RfgvJ4obNHjzqvyuW2QxOo/KNGMjqh47udAbdl1sZUTgfHSllWvdoHuEDCV+OqAPziSetOu2PNpc5QwyeWRhdqn88q1T0xdkPYJqsSKe2lgWYksbDMhSGIYVWQA7xw88uhnK1hxcjDZ+IDuHT4cjQBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgTEgES0mh86PoeZ9Xn/kS5RH43QtZujl9n8cdFuRUjvYJHgvQLKc="
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "state": "tx_+P4LAfiEuEB1aFKLVrMb0FFh2DBWTU9ls4BV52ac59RfgvJ4obNHjzqvyuW2QxOo/KNGMjqh47udAbdl1sZUTgfHSllWvdoHuEDCV+OqAPziSetOu2PNpc5QwyeWRhdqn88q1T0xdkPYJqsSKe2lgWYksbDMhSGIYVWQA7xw88uhnK1hxcjDZ+IDuHT4cjQBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgTEgES0mh86PoeZ9Xn/kS5RH43QtZujl9n8cdFuRUjvYJHgvQLKc="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "message": {
        "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "info": "Hello",
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "message": {
        "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "info": "Hello back",
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
      }
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
    "amount": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.withdraw",
      "params": {
        "amount": "2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "message": {
        "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "info": "Hello",
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "message": {
        "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "info": "Hello back",
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
      }
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
    "amount": 2,
    "meta": [
      "meta 1"
    ]
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBmV3F8qHwm7xU8x22yKQLWC+6gL8XPoMYX+53e5gtWpBoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEAIAhg/AoHKQAKArw56Yk/nuAn9SDD7EMYNf1i7BI0w+TO2mQGxnQbS3tgoMgJPM0Q==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423107,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuECdnYtd6rBb/f3I7FGVFMvJIcka4qJfYYNA0RVvJZ81bLWdYZ56DFqw0uBV5PK2q1mwvBB7DoYEv+wga0GD4J4LuHT4cjQBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7YKDCeV8Mo="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423107,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
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
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "signed_tx": "tx_+LwLAfhCuECdnYtd6rBb/f3I7FGVFMvJIcka4qJfYYNA0RVvJZ81bLWdYZ56DFqw0uBV5PK2q1mwvBB7DoYEv+wga0GD4J4LuHT4cjQBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7YKDCeV8Mo=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
        },
        {
          "data": "meta 1",
          "op": "OffChainMeta"
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
  "id": -576460752303423106,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBVP/nE3Mks7IiTVbXprR5kdArrcZVGf2HORIlVD2fp6CyEnHXKQsc33XO74wePCc4N+E1seQ3k/g3HhZtCrF8OuECdnYtd6rBb/f3I7FGVFMvJIcka4qJfYYNA0RVvJZ81bLWdYZ56DFqw0uBV5PK2q1mwvBB7DoYEv+wga0GD4J4LuHT4cjQBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7YKDP5zmtU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423106,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEBVP/nE3Mks7IiTVbXprR5kdArrcZVGf2HORIlVD2fp6CyEnHXKQsc33XO74wePCc4N+E1seQ3k/g3HhZtCrF8OuECdnYtd6rBb/f3I7FGVFMvJIcka4qJfYYNA0RVvJZ81bLWdYZ56DFqw0uBV5PK2q1mwvBB7DoYEv+wga0GD4J4LuHT4cjQBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7YKDP5zmtU=",
      "type": "channel_withdraw_tx"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEBVP/nE3Mks7IiTVbXprR5kdArrcZVGf2HORIlVD2fp6CyEnHXKQsc33XO74wePCc4N+E1seQ3k/g3HhZtCrF8OuECdnYtd6rBb/f3I7FGVFMvJIcka4qJfYYNA0RVvJZ81bLWdYZ56DFqw0uBV5PK2q1mwvBB7DoYEv+wga0GD4J4LuHT4cjQBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7YKDP5zmtU=",
      "type": "channel_withdraw_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "message": {
        "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "info": "Hello",
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "message": {
        "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "info": "Hello back",
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
      }
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBVP/nE3Mks7IiTVbXprR5kdArrcZVGf2HORIlVD2fp6CyEnHXKQsc33XO74wePCc4N+E1seQ3k/g3HhZtCrF8OuECdnYtd6rBb/f3I7FGVFMvJIcka4qJfYYNA0RVvJZ81bLWdYZ56DFqw0uBV5PK2q1mwvBB7DoYEv+wga0GD4J4LuHT4cjQBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7YKDP5zmtU=",
      "type": "channel_withdraw_tx"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBVP/nE3Mks7IiTVbXprR5kdArrcZVGf2HORIlVD2fp6CyEnHXKQsc33XO74wePCc4N+E1seQ3k/g3HhZtCrF8OuECdnYtd6rBb/f3I7FGVFMvJIcka4qJfYYNA0RVvJZ81bLWdYZ56DFqw0uBV5PK2q1mwvBB7DoYEv+wga0GD4J4LuHT4cjQBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7YKDP5zmtU=",
      "type": "channel_withdraw_tx"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "event": "own_withdraw_locked"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "event": "own_withdraw_locked"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "event": "withdraw_locked"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "event": "withdraw_locked"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "state": "tx_+P4LAfiEuEBVP/nE3Mks7IiTVbXprR5kdArrcZVGf2HORIlVD2fp6CyEnHXKQsc33XO74wePCc4N+E1seQ3k/g3HhZtCrF8OuECdnYtd6rBb/f3I7FGVFMvJIcka4qJfYYNA0RVvJZ81bLWdYZ56DFqw0uBV5PK2q1mwvBB7DoYEv+wga0GD4J4LuHT4cjQBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7YKDP5zmtU="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "state": "tx_+P4LAfiEuEBVP/nE3Mks7IiTVbXprR5kdArrcZVGf2HORIlVD2fp6CyEnHXKQsc33XO74wePCc4N+E1seQ3k/g3HhZtCrF8OuECdnYtd6rBb/f3I7FGVFMvJIcka4qJfYYNA0RVvJZ81bLWdYZ56DFqw0uBV5PK2q1mwvBB7DoYEv+wga0GD4J4LuHT4cjQBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7YKDP5zmtU="
    }
  },
  "version": 1
}
```
