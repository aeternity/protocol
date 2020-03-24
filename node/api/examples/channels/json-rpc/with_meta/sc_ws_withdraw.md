
#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "message": {
        "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "message": {
        "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello back",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "message": {
        "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "message": {
        "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello back",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBsbBWu/xVpTJkxB+RilACEVlef3ALvNKFwUfDi3K/R8eoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gIAhg/AoHKQAKB4yXcWHFqhu6fsEbgGSuCeFAwtDmmdUVEeQf/6j7Un4Ak2Ilt93Q==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "id": -576460752303422796,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEDJFrev6cKFZSXubvQdJERETs7uJrUarLY/k/Ue/mXswTfXLsGqberkgp3ZnoayijbARGev4krY8//x2dIOnsQHuHT4cjQBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgeMl3Fhxaobun7BG4BkrgnhQMLQ5pnVFRHkH/+o+1J+AJNpqToAY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422796,
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEDJFrev6cKFZSXubvQdJERETs7uJrUarLY/k/Ue/mXswTfXLsGqberkgp3ZnoayijbARGev4krY8//x2dIOnsQHuHT4cjQBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgeMl3Fhxaobun7BG4BkrgnhQMLQ5pnVFRHkH/+o+1J+AJNpqToAY=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "id": -576460752303422795,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuECI8/XaJROlMhznLhKyhTh43dBi6E8FIZ1CgXeAUKzbjybH8/xyodfRfx01zZXuA66oCtfDcFElC4+76fjzRUEGuEDJFrev6cKFZSXubvQdJERETs7uJrUarLY/k/Ue/mXswTfXLsGqberkgp3ZnoayijbARGev4krY8//x2dIOnsQHuHT4cjQBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgeMl3Fhxaobun7BG4BkrgnhQMLQ5pnVFRHkH/+o+1J+AJNq1THQI="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422795,
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuECI8/XaJROlMhznLhKyhTh43dBi6E8FIZ1CgXeAUKzbjybH8/xyodfRfx01zZXuA66oCtfDcFElC4+76fjzRUEGuEDJFrev6cKFZSXubvQdJERETs7uJrUarLY/k/Ue/mXswTfXLsGqberkgp3ZnoayijbARGev4krY8//x2dIOnsQHuHT4cjQBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgeMl3Fhxaobun7BG4BkrgnhQMLQ5pnVFRHkH/+o+1J+AJNq1THQI=",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuECI8/XaJROlMhznLhKyhTh43dBi6E8FIZ1CgXeAUKzbjybH8/xyodfRfx01zZXuA66oCtfDcFElC4+76fjzRUEGuEDJFrev6cKFZSXubvQdJERETs7uJrUarLY/k/Ue/mXswTfXLsGqberkgp3ZnoayijbARGev4krY8//x2dIOnsQHuHT4cjQBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgeMl3Fhxaobun7BG4BkrgnhQMLQ5pnVFRHkH/+o+1J+AJNq1THQI=",
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "message": {
        "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "message": {
        "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello back",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECI8/XaJROlMhznLhKyhTh43dBi6E8FIZ1CgXeAUKzbjybH8/xyodfRfx01zZXuA66oCtfDcFElC4+76fjzRUEGuEDJFrev6cKFZSXubvQdJERETs7uJrUarLY/k/Ue/mXswTfXLsGqberkgp3ZnoayijbARGev4krY8//x2dIOnsQHuHT4cjQBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgeMl3Fhxaobun7BG4BkrgnhQMLQ5pnVFRHkH/+o+1J+AJNq1THQI=",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECI8/XaJROlMhznLhKyhTh43dBi6E8FIZ1CgXeAUKzbjybH8/xyodfRfx01zZXuA66oCtfDcFElC4+76fjzRUEGuEDJFrev6cKFZSXubvQdJERETs7uJrUarLY/k/Ue/mXswTfXLsGqberkgp3ZnoayijbARGev4krY8//x2dIOnsQHuHT4cjQBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgeMl3Fhxaobun7BG4BkrgnhQMLQ5pnVFRHkH/+o+1J+AJNq1THQI=",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "state": "tx_+P4LAfiEuECI8/XaJROlMhznLhKyhTh43dBi6E8FIZ1CgXeAUKzbjybH8/xyodfRfx01zZXuA66oCtfDcFElC4+76fjzRUEGuEDJFrev6cKFZSXubvQdJERETs7uJrUarLY/k/Ue/mXswTfXLsGqberkgp3ZnoayijbARGev4krY8//x2dIOnsQHuHT4cjQBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgeMl3Fhxaobun7BG4BkrgnhQMLQ5pnVFRHkH/+o+1J+AJNq1THQI="
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "state": "tx_+P4LAfiEuECI8/XaJROlMhznLhKyhTh43dBi6E8FIZ1CgXeAUKzbjybH8/xyodfRfx01zZXuA66oCtfDcFElC4+76fjzRUEGuEDJFrev6cKFZSXubvQdJERETs7uJrUarLY/k/Ue/mXswTfXLsGqberkgp3ZnoayijbARGev4krY8//x2dIOnsQHuHT4cjQBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgeMl3Fhxaobun7BG4BkrgnhQMLQ5pnVFRHkH/+o+1J+AJNq1THQI="
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "message": {
        "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "message": {
        "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello back",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "message": {
        "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "message": {
        "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello back",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBsbBWu/xVpTJkxB+RilACEVlef3ALvNKFwUfDi3K/R8eoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AIAhg/AoHKQAKCPVbQrAfYXrWTP0iwmtWIe9nj7Tuv+WHg7LyUfwRTSMQoW4kCnXw==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "id": -576460752303422794,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEABciLCty3PAplJ4UzP3/TOJtRrt7x7q99as52AxbmuAPUHg8spUfHU4pewLgBK3B7GwxVljoJoYj6TgbZs6XYMuHT4cjQBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jEKFtQxDb4="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422794,
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEABciLCty3PAplJ4UzP3/TOJtRrt7x7q99as52AxbmuAPUHg8spUfHU4pewLgBK3B7GwxVljoJoYj6TgbZs6XYMuHT4cjQBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jEKFtQxDb4=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "id": -576460752303422793,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEABciLCty3PAplJ4UzP3/TOJtRrt7x7q99as52AxbmuAPUHg8spUfHU4pewLgBK3B7GwxVljoJoYj6TgbZs6XYMuECfkoAPj/PZfIvLt55BuLATIfR5rFSMsTN9MIv8tEDjs26gnxnKjd8c9YBZsiGw4DnOYPDDX7/FIeI2uSOJZLAEuHT4cjQBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jEKFsOd3j4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422793,
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEABciLCty3PAplJ4UzP3/TOJtRrt7x7q99as52AxbmuAPUHg8spUfHU4pewLgBK3B7GwxVljoJoYj6TgbZs6XYMuECfkoAPj/PZfIvLt55BuLATIfR5rFSMsTN9MIv8tEDjs26gnxnKjd8c9YBZsiGw4DnOYPDDX7/FIeI2uSOJZLAEuHT4cjQBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jEKFsOd3j4=",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEABciLCty3PAplJ4UzP3/TOJtRrt7x7q99as52AxbmuAPUHg8spUfHU4pewLgBK3B7GwxVljoJoYj6TgbZs6XYMuECfkoAPj/PZfIvLt55BuLATIfR5rFSMsTN9MIv8tEDjs26gnxnKjd8c9YBZsiGw4DnOYPDDX7/FIeI2uSOJZLAEuHT4cjQBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jEKFsOd3j4=",
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "message": {
        "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "message": {
        "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello back",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEABciLCty3PAplJ4UzP3/TOJtRrt7x7q99as52AxbmuAPUHg8spUfHU4pewLgBK3B7GwxVljoJoYj6TgbZs6XYMuECfkoAPj/PZfIvLt55BuLATIfR5rFSMsTN9MIv8tEDjs26gnxnKjd8c9YBZsiGw4DnOYPDDX7/FIeI2uSOJZLAEuHT4cjQBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jEKFsOd3j4=",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEABciLCty3PAplJ4UzP3/TOJtRrt7x7q99as52AxbmuAPUHg8spUfHU4pewLgBK3B7GwxVljoJoYj6TgbZs6XYMuECfkoAPj/PZfIvLt55BuLATIfR5rFSMsTN9MIv8tEDjs26gnxnKjd8c9YBZsiGw4DnOYPDDX7/FIeI2uSOJZLAEuHT4cjQBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jEKFsOd3j4=",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "state": "tx_+P4LAfiEuEABciLCty3PAplJ4UzP3/TOJtRrt7x7q99as52AxbmuAPUHg8spUfHU4pewLgBK3B7GwxVljoJoYj6TgbZs6XYMuECfkoAPj/PZfIvLt55BuLATIfR5rFSMsTN9MIv8tEDjs26gnxnKjd8c9YBZsiGw4DnOYPDDX7/FIeI2uSOJZLAEuHT4cjQBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jEKFsOd3j4="
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "state": "tx_+P4LAfiEuEABciLCty3PAplJ4UzP3/TOJtRrt7x7q99as52AxbmuAPUHg8spUfHU4pewLgBK3B7GwxVljoJoYj6TgbZs6XYMuECfkoAPj/PZfIvLt55BuLATIfR5rFSMsTN9MIv8tEDjs26gnxnKjd8c9YBZsiGw4DnOYPDDX7/FIeI2uSOJZLAEuHT4cjQBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jEKFsOd3j4="
    }
  },
  "version": 1
}
```
