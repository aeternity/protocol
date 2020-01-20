
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
  "method": "channels.deposit",
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
      "method": "channels.deposit",
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
  "method": "channels.deposit",
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
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBmV3F8qHwm7xU8x22yKQLWC+6gL8XPoMYX+53e5gtWpBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79AIAhg/AoHKQAKA3ePtXpl0nTlSmIFMX673ar2a8b3bhiDQxLXkJPsN0IwcdJyMDJg==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainDeposit"
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
  "id": -576460752303423113,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEBKwc7dbQCDZfy6xouCB5dg5vQusFVY3aVCYeNCHX55HJZ3+/2tVrWxfThyQaBAT/F/XmY6LM5LLRdlqULEGNsNuHT4cjMBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgN3j7V6ZdJ05UpiBTF+u92q9mvG924Yg0MS15CT7DdCMHHW+wuNE="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423113,
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
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEBKwc7dbQCDZfy6xouCB5dg5vQusFVY3aVCYeNCHX55HJZ3+/2tVrWxfThyQaBAT/F/XmY6LM5LLRdlqULEGNsNuHT4cjMBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgN3j7V6ZdJ05UpiBTF+u92q9mvG924Yg0MS15CT7DdCMHHW+wuNE=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainDeposit"
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
  "id": -576460752303423112,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBKwc7dbQCDZfy6xouCB5dg5vQusFVY3aVCYeNCHX55HJZ3+/2tVrWxfThyQaBAT/F/XmY6LM5LLRdlqULEGNsNuEB8IUdVmHhfvz0SrNA3ztmCCZ5fOfQKfr5s8sJ1UTmpiU6XaUNHK7IfIi4qLUjfHDrA4Xlw5LDeQg08B822v3AJuHT4cjMBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgN3j7V6ZdJ05UpiBTF+u92q9mvG924Yg0MS15CT7DdCMHHTuBPQE="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423112,
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
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEBKwc7dbQCDZfy6xouCB5dg5vQusFVY3aVCYeNCHX55HJZ3+/2tVrWxfThyQaBAT/F/XmY6LM5LLRdlqULEGNsNuEB8IUdVmHhfvz0SrNA3ztmCCZ5fOfQKfr5s8sJ1UTmpiU6XaUNHK7IfIi4qLUjfHDrA4Xlw5LDeQg08B822v3AJuHT4cjMBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgN3j7V6ZdJ05UpiBTF+u92q9mvG924Yg0MS15CT7DdCMHHTuBPQE=",
      "type": "channel_deposit_tx"
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
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEBKwc7dbQCDZfy6xouCB5dg5vQusFVY3aVCYeNCHX55HJZ3+/2tVrWxfThyQaBAT/F/XmY6LM5LLRdlqULEGNsNuEB8IUdVmHhfvz0SrNA3ztmCCZ5fOfQKfr5s8sJ1UTmpiU6XaUNHK7IfIi4qLUjfHDrA4Xlw5LDeQg08B822v3AJuHT4cjMBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgN3j7V6ZdJ05UpiBTF+u92q9mvG924Yg0MS15CT7DdCMHHTuBPQE=",
      "type": "channel_deposit_tx"
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
      "tx": "tx_+P4LAfiEuEBKwc7dbQCDZfy6xouCB5dg5vQusFVY3aVCYeNCHX55HJZ3+/2tVrWxfThyQaBAT/F/XmY6LM5LLRdlqULEGNsNuEB8IUdVmHhfvz0SrNA3ztmCCZ5fOfQKfr5s8sJ1UTmpiU6XaUNHK7IfIi4qLUjfHDrA4Xlw5LDeQg08B822v3AJuHT4cjMBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgN3j7V6ZdJ05UpiBTF+u92q9mvG924Yg0MS15CT7DdCMHHTuBPQE=",
      "type": "channel_deposit_tx"
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
      "tx": "tx_+P4LAfiEuEBKwc7dbQCDZfy6xouCB5dg5vQusFVY3aVCYeNCHX55HJZ3+/2tVrWxfThyQaBAT/F/XmY6LM5LLRdlqULEGNsNuEB8IUdVmHhfvz0SrNA3ztmCCZ5fOfQKfr5s8sJ1UTmpiU6XaUNHK7IfIi4qLUjfHDrA4Xlw5LDeQg08B822v3AJuHT4cjMBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgN3j7V6ZdJ05UpiBTF+u92q9mvG924Yg0MS15CT7DdCMHHTuBPQE=",
      "type": "channel_deposit_tx"
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
      "event": "own_deposit_locked"
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
      "event": "own_deposit_locked"
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
      "event": "deposit_locked"
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
      "event": "deposit_locked"
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
      "state": "tx_+P4LAfiEuEBKwc7dbQCDZfy6xouCB5dg5vQusFVY3aVCYeNCHX55HJZ3+/2tVrWxfThyQaBAT/F/XmY6LM5LLRdlqULEGNsNuEB8IUdVmHhfvz0SrNA3ztmCCZ5fOfQKfr5s8sJ1UTmpiU6XaUNHK7IfIi4qLUjfHDrA4Xlw5LDeQg08B822v3AJuHT4cjMBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgN3j7V6ZdJ05UpiBTF+u92q9mvG924Yg0MS15CT7DdCMHHTuBPQE="
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
      "state": "tx_+P4LAfiEuEBKwc7dbQCDZfy6xouCB5dg5vQusFVY3aVCYeNCHX55HJZ3+/2tVrWxfThyQaBAT/F/XmY6LM5LLRdlqULEGNsNuEB8IUdVmHhfvz0SrNA3ztmCCZ5fOfQKfr5s8sJ1UTmpiU6XaUNHK7IfIi4qLUjfHDrA4Xlw5LDeQg08B822v3AJuHT4cjMBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgN3j7V6ZdJ05UpiBTF+u92q9mvG924Yg0MS15CT7DdCMHHTuBPQE="
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
  "method": "channels.deposit",
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
      "method": "channels.deposit",
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
  "method": "channels.deposit",
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
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBmV3F8qHwm7xU8x22yKQLWC+6gL8XPoMYX+53e5gtWpBoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEAIAhg/AoHKQAKAgDS0W1PKL8d0t9NVK5BF2+YJZNd+828YoVfMCAKj0VAgLtHQm+g==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainDeposit"
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
  "id": -576460752303423111,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEBrdduR1NAA/51nNkluijkqtLkTcFJMZhjAlxIzvCQqcgCeLvEXZHt7BJ1W2oQXiGrtpDjadi5H1ZPg4QijaeoEuHT4cjMBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgIA0tFtTyi/HdLfTVSuQRdvmCWTXfvNvGKFXzAgCo9FQIC4qvZZs="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423111,
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
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEBrdduR1NAA/51nNkluijkqtLkTcFJMZhjAlxIzvCQqcgCeLvEXZHt7BJ1W2oQXiGrtpDjadi5H1ZPg4QijaeoEuHT4cjMBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgIA0tFtTyi/HdLfTVSuQRdvmCWTXfvNvGKFXzAgCo9FQIC4qvZZs=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainDeposit"
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
  "id": -576460752303423110,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBrdduR1NAA/51nNkluijkqtLkTcFJMZhjAlxIzvCQqcgCeLvEXZHt7BJ1W2oQXiGrtpDjadi5H1ZPg4QijaeoEuEB0Re8jgJ4LwUmkzKAhv1iYE/wUFEEh6LhbYBRCkOJkDr8NQvgLpTnn+bpfG15vECel1sq7bzB43roehJS5lKsKuHT4cjMBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgIA0tFtTyi/HdLfTVSuQRdvmCWTXfvNvGKFXzAgCo9FQICxTjnn8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mgny4Q2cfYEGzZtNwX7rQqq574StZbGrvJGTkmiV9ZMVTaXwV",
  "id": -576460752303423110,
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
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEBrdduR1NAA/51nNkluijkqtLkTcFJMZhjAlxIzvCQqcgCeLvEXZHt7BJ1W2oQXiGrtpDjadi5H1ZPg4QijaeoEuEB0Re8jgJ4LwUmkzKAhv1iYE/wUFEEh6LhbYBRCkOJkDr8NQvgLpTnn+bpfG15vECel1sq7bzB43roehJS5lKsKuHT4cjMBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgIA0tFtTyi/HdLfTVSuQRdvmCWTXfvNvGKFXzAgCo9FQICxTjnn8=",
      "type": "channel_deposit_tx"
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
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEBrdduR1NAA/51nNkluijkqtLkTcFJMZhjAlxIzvCQqcgCeLvEXZHt7BJ1W2oQXiGrtpDjadi5H1ZPg4QijaeoEuEB0Re8jgJ4LwUmkzKAhv1iYE/wUFEEh6LhbYBRCkOJkDr8NQvgLpTnn+bpfG15vECel1sq7bzB43roehJS5lKsKuHT4cjMBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgIA0tFtTyi/HdLfTVSuQRdvmCWTXfvNvGKFXzAgCo9FQICxTjnn8=",
      "type": "channel_deposit_tx"
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
      "tx": "tx_+P4LAfiEuEBrdduR1NAA/51nNkluijkqtLkTcFJMZhjAlxIzvCQqcgCeLvEXZHt7BJ1W2oQXiGrtpDjadi5H1ZPg4QijaeoEuEB0Re8jgJ4LwUmkzKAhv1iYE/wUFEEh6LhbYBRCkOJkDr8NQvgLpTnn+bpfG15vECel1sq7bzB43roehJS5lKsKuHT4cjMBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgIA0tFtTyi/HdLfTVSuQRdvmCWTXfvNvGKFXzAgCo9FQICxTjnn8=",
      "type": "channel_deposit_tx"
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
      "tx": "tx_+P4LAfiEuEBrdduR1NAA/51nNkluijkqtLkTcFJMZhjAlxIzvCQqcgCeLvEXZHt7BJ1W2oQXiGrtpDjadi5H1ZPg4QijaeoEuEB0Re8jgJ4LwUmkzKAhv1iYE/wUFEEh6LhbYBRCkOJkDr8NQvgLpTnn+bpfG15vECel1sq7bzB43roehJS5lKsKuHT4cjMBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgIA0tFtTyi/HdLfTVSuQRdvmCWTXfvNvGKFXzAgCo9FQICxTjnn8=",
      "type": "channel_deposit_tx"
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
      "event": "own_deposit_locked"
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
      "event": "own_deposit_locked"
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
      "event": "deposit_locked"
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
      "event": "deposit_locked"
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
      "state": "tx_+P4LAfiEuEBrdduR1NAA/51nNkluijkqtLkTcFJMZhjAlxIzvCQqcgCeLvEXZHt7BJ1W2oQXiGrtpDjadi5H1ZPg4QijaeoEuEB0Re8jgJ4LwUmkzKAhv1iYE/wUFEEh6LhbYBRCkOJkDr8NQvgLpTnn+bpfG15vECel1sq7bzB43roehJS5lKsKuHT4cjMBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgIA0tFtTyi/HdLfTVSuQRdvmCWTXfvNvGKFXzAgCo9FQICxTjnn8="
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
      "state": "tx_+P4LAfiEuEBrdduR1NAA/51nNkluijkqtLkTcFJMZhjAlxIzvCQqcgCeLvEXZHt7BJ1W2oQXiGrtpDjadi5H1ZPg4QijaeoEuEB0Re8jgJ4LwUmkzKAhv1iYE/wUFEEh6LhbYBRCkOJkDr8NQvgLpTnn+bpfG15vECel1sq7bzB43roehJS5lKsKuHT4cjMBoQZldxfKh8Ju8VPMdtsikC1gvuoC/Fz6DGF/ud3uYLVqQaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgIA0tFtTyi/HdLfTVSuQRdvmCWTXfvNvGKFXzAgCo9FQICxTjnn8="
    }
  },
  "version": 1
}
```
