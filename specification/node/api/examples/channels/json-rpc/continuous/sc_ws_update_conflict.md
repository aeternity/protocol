
#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
    "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhZew5Ookmw3Bs/7SN7rXCFZzENKi5rQeMppkg2nWdVaBqBAspkUHVc+kYM7Vvj4WOMGppoVtE+bix63giuF7Bmg15yJmV8=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainTransfer",
          "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhZew5Ookmw3Bs/7SN7rXCFZzENKi5rQeMppkg2nWdVaBqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8BwBMgI4=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainTransfer",
          "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
    "signed_tx": "tx_+JALAfhCuEDKpsaBLDcstJxEpGW7V6fZ/bBJMXuJBKAiKosRXHcM6j9yDJ60bF7RC+aF9QefQoA0jjPsLQhr2CLOTdSBx9wMuEj4RjkCoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWgagKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAdlhTNE"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBu6b2/YJ411NB8vmTN1xhQ6fzoY6QvYP+HMROy6L/ThOZx8WlIZDsvpx8Er+1gSZebHl2qEPPFF9+eqiB8mRgGuEj4RjkCoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWgagQLKZFB1XPpGDO1b4+FjjBqaaFbRPm4set4IrhewZoNdvaI+l"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
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
    "amount": 1,
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhZew5Ookmw3Bs/7SN7rXCFZzENKi5rQeMppkg2nWdVaBqArw56Yk/nuAn9SDD7EMYNf1i7BI0w+TO2mQGxnQbS3tsS0C2U=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
    "signed_tx": "tx_+JALAfhCuECrXf0L2KfvjnYeJkz02SpHNtywx+V9a4PguPBmh7UNcyiPXsm3s1Rj1cUH7xg3RZI/asglflCxQYN1+BDaaNINuEj4RjkCoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWgagK8OemJP57gJ/Ugw+xDGDX9YuwSNMPkztpkBsZ0G0t7YkeV/N"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhZew5Ookmw3Bs/7SN7rXCFZzENKi5rQeMppkg2nWdVaBqByGt2dmKTSdjs4orcgG9wHW0dJO5SSw9CsUxHzI5VTxaTySqw=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
    "signed_tx": "tx_+JALAfhCuEB5yKayz69HKtYG3q85gHIU6MxshAVEV+wkE5AkFrVEWaTyBS6WlcoOH9+jHWxrblBOB6eGEuNyhasyBeZdQp4PuEj4RjkCoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWgagchrdnZik0nY7OKK3IBvcB1tHSTuUksPQrFMR8yOVU8XlqD2X"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 5
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423146,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
  "id": -576460752303423146,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999999
    },
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhZew5Ookmw3Bs/7SN7rXCFZzENKi5rQeMppkg2nWdVaBqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8BwBMgI4=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainTransfer",
          "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
  "id": -576460752303423145,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "error": 147
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
  "id": -576460752303423145,
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423144,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
  "id": -576460752303423144,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999999
    },
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423143,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
  "id": -576460752303423143,
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator ---> node
```javascript
{
  "id": -576460752303423142,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### initiator closes WebSocket connection
