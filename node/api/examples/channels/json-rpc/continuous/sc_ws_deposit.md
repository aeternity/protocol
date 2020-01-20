
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
  "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBhZew5Ookmw3Bs/7SN7rXCFZzENKi5rQeMppkg2nWdVaoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79AIAhg/AoHKQAKChXLDyVpEyqFjhIeWBI1DOO4boF2NOsTcvscbEzeU31gIaRxUOfg==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
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
  "id": -576460752303423154,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEC38YcvBrueZGChmC2ygJLrIQ2r335kAbldMjgq3OYf72MHG/DMDlaXTbMRwncfdEo3BJd5sfcwvPy00g5BZegBuHT4cjMBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgoVyw8laRMqhY4SHlgSNQzjuG6BdjTrE3L7HGxM3lN9YCGgsDM+0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
  "id": -576460752303423154,
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEC38YcvBrueZGChmC2ygJLrIQ2r335kAbldMjgq3OYf72MHG/DMDlaXTbMRwncfdEo3BJd5sfcwvPy00g5BZegBuHT4cjMBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgoVyw8laRMqhY4SHlgSNQzjuG6BdjTrE3L7HGxM3lN9YCGgsDM+0=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
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
  "id": -576460752303423153,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEC38YcvBrueZGChmC2ygJLrIQ2r335kAbldMjgq3OYf72MHG/DMDlaXTbMRwncfdEo3BJd5sfcwvPy00g5BZegBuED/ZX3iIry9ll9FZRRr5hLkj8x+EVBgXVO9LDXeah+JgI4V8JimFwvSUW42ZLgfWV5YFEFiYLetvrsvXlDU6oQHuHT4cjMBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgoVyw8laRMqhY4SHlgSNQzjuG6BdjTrE3L7HGxM3lN9YCGny8Jj8="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
  "id": -576460752303423153,
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEC38YcvBrueZGChmC2ygJLrIQ2r335kAbldMjgq3OYf72MHG/DMDlaXTbMRwncfdEo3BJd5sfcwvPy00g5BZegBuED/ZX3iIry9ll9FZRRr5hLkj8x+EVBgXVO9LDXeah+JgI4V8JimFwvSUW42ZLgfWV5YFEFiYLetvrsvXlDU6oQHuHT4cjMBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgoVyw8laRMqhY4SHlgSNQzjuG6BdjTrE3L7HGxM3lN9YCGny8Jj8=",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEC38YcvBrueZGChmC2ygJLrIQ2r335kAbldMjgq3OYf72MHG/DMDlaXTbMRwncfdEo3BJd5sfcwvPy00g5BZegBuED/ZX3iIry9ll9FZRRr5hLkj8x+EVBgXVO9LDXeah+JgI4V8JimFwvSUW42ZLgfWV5YFEFiYLetvrsvXlDU6oQHuHT4cjMBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgoVyw8laRMqhY4SHlgSNQzjuG6BdjTrE3L7HGxM3lN9YCGny8Jj8=",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEC38YcvBrueZGChmC2ygJLrIQ2r335kAbldMjgq3OYf72MHG/DMDlaXTbMRwncfdEo3BJd5sfcwvPy00g5BZegBuED/ZX3iIry9ll9FZRRr5hLkj8x+EVBgXVO9LDXeah+JgI4V8JimFwvSUW42ZLgfWV5YFEFiYLetvrsvXlDU6oQHuHT4cjMBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgoVyw8laRMqhY4SHlgSNQzjuG6BdjTrE3L7HGxM3lN9YCGny8Jj8=",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEC38YcvBrueZGChmC2ygJLrIQ2r335kAbldMjgq3OYf72MHG/DMDlaXTbMRwncfdEo3BJd5sfcwvPy00g5BZegBuED/ZX3iIry9ll9FZRRr5hLkj8x+EVBgXVO9LDXeah+JgI4V8JimFwvSUW42ZLgfWV5YFEFiYLetvrsvXlDU6oQHuHT4cjMBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgoVyw8laRMqhY4SHlgSNQzjuG6BdjTrE3L7HGxM3lN9YCGny8Jj8=",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "state": "tx_+P4LAfiEuEC38YcvBrueZGChmC2ygJLrIQ2r335kAbldMjgq3OYf72MHG/DMDlaXTbMRwncfdEo3BJd5sfcwvPy00g5BZegBuED/ZX3iIry9ll9FZRRr5hLkj8x+EVBgXVO9LDXeah+JgI4V8JimFwvSUW42ZLgfWV5YFEFiYLetvrsvXlDU6oQHuHT4cjMBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgoVyw8laRMqhY4SHlgSNQzjuG6BdjTrE3L7HGxM3lN9YCGny8Jj8="
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "state": "tx_+P4LAfiEuEC38YcvBrueZGChmC2ygJLrIQ2r335kAbldMjgq3OYf72MHG/DMDlaXTbMRwncfdEo3BJd5sfcwvPy00g5BZegBuED/ZX3iIry9ll9FZRRr5hLkj8x+EVBgXVO9LDXeah+JgI4V8JimFwvSUW42ZLgfWV5YFEFiYLetvrsvXlDU6oQHuHT4cjMBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgoVyw8laRMqhY4SHlgSNQzjuG6BdjTrE3L7HGxM3lN9YCGny8Jj8="
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
  "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBhZew5Ookmw3Bs/7SN7rXCFZzENKi5rQeMppkg2nWdVaoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEAIAhg/AoHKQAKB9/+NB55OhzzLOezHqwJrKqcohlQB0t7MzKXQVTQm6nwMJdBVQyQ==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
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
  "id": -576460752303423152,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEBF7zrylFFIUwhmlvvh5fZN2/F7KJIzeYlPTFwNw6MvGseex5LB1aO5r9VNqObVaUYG9xQiKfUfa6JDm55Zay4OuHT4cjMBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgff/jQeeToc8yznsx6sCayqnKIZUAdLezMyl0FU0Jup8DCZlK4Lo="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
  "id": -576460752303423152,
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEBF7zrylFFIUwhmlvvh5fZN2/F7KJIzeYlPTFwNw6MvGseex5LB1aO5r9VNqObVaUYG9xQiKfUfa6JDm55Zay4OuHT4cjMBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgff/jQeeToc8yznsx6sCayqnKIZUAdLezMyl0FU0Jup8DCZlK4Lo=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
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
  "id": -576460752303423151,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBF7zrylFFIUwhmlvvh5fZN2/F7KJIzeYlPTFwNw6MvGseex5LB1aO5r9VNqObVaUYG9xQiKfUfa6JDm55Zay4OuEDQyWpFDKY3FBcgtoQqj26xmVAQOAkSowyoIne0SC/NsoN6rkTZQdd2UrSWdYlc4GYgk3ihb28/wtW9kciAfbMAuHT4cjMBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgff/jQeeToc8yznsx6sCayqnKIZUAdLezMyl0FU0Jup8DCbdHw2M="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
  "id": -576460752303423151,
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEBF7zrylFFIUwhmlvvh5fZN2/F7KJIzeYlPTFwNw6MvGseex5LB1aO5r9VNqObVaUYG9xQiKfUfa6JDm55Zay4OuEDQyWpFDKY3FBcgtoQqj26xmVAQOAkSowyoIne0SC/NsoN6rkTZQdd2UrSWdYlc4GYgk3ihb28/wtW9kciAfbMAuHT4cjMBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgff/jQeeToc8yznsx6sCayqnKIZUAdLezMyl0FU0Jup8DCbdHw2M=",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEBF7zrylFFIUwhmlvvh5fZN2/F7KJIzeYlPTFwNw6MvGseex5LB1aO5r9VNqObVaUYG9xQiKfUfa6JDm55Zay4OuEDQyWpFDKY3FBcgtoQqj26xmVAQOAkSowyoIne0SC/NsoN6rkTZQdd2UrSWdYlc4GYgk3ihb28/wtW9kciAfbMAuHT4cjMBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgff/jQeeToc8yznsx6sCayqnKIZUAdLezMyl0FU0Jup8DCbdHw2M=",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "info": "Hello back",
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
      }
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBF7zrylFFIUwhmlvvh5fZN2/F7KJIzeYlPTFwNw6MvGseex5LB1aO5r9VNqObVaUYG9xQiKfUfa6JDm55Zay4OuEDQyWpFDKY3FBcgtoQqj26xmVAQOAkSowyoIne0SC/NsoN6rkTZQdd2UrSWdYlc4GYgk3ihb28/wtW9kciAfbMAuHT4cjMBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgff/jQeeToc8yznsx6sCayqnKIZUAdLezMyl0FU0Jup8DCbdHw2M=",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBF7zrylFFIUwhmlvvh5fZN2/F7KJIzeYlPTFwNw6MvGseex5LB1aO5r9VNqObVaUYG9xQiKfUfa6JDm55Zay4OuEDQyWpFDKY3FBcgtoQqj26xmVAQOAkSowyoIne0SC/NsoN6rkTZQdd2UrSWdYlc4GYgk3ihb28/wtW9kciAfbMAuHT4cjMBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgff/jQeeToc8yznsx6sCayqnKIZUAdLezMyl0FU0Jup8DCbdHw2M=",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "state": "tx_+P4LAfiEuEBF7zrylFFIUwhmlvvh5fZN2/F7KJIzeYlPTFwNw6MvGseex5LB1aO5r9VNqObVaUYG9xQiKfUfa6JDm55Zay4OuEDQyWpFDKY3FBcgtoQqj26xmVAQOAkSowyoIne0SC/NsoN6rkTZQdd2UrSWdYlc4GYgk3ihb28/wtW9kciAfbMAuHT4cjMBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgff/jQeeToc8yznsx6sCayqnKIZUAdLezMyl0FU0Jup8DCbdHw2M="
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "state": "tx_+P4LAfiEuEBF7zrylFFIUwhmlvvh5fZN2/F7KJIzeYlPTFwNw6MvGseex5LB1aO5r9VNqObVaUYG9xQiKfUfa6JDm55Zay4OuEDQyWpFDKY3FBcgtoQqj26xmVAQOAkSowyoIne0SC/NsoN6rkTZQdd2UrSWdYlc4GYgk3ihb28/wtW9kciAfbMAuHT4cjMBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgff/jQeeToc8yznsx6sCayqnKIZUAdLezMyl0FU0Jup8DCbdHw2M="
    }
  },
  "version": 1
}
```
