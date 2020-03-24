
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
  "method": "channels.deposit",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBsbBWu/xVpTJkxB+RilACEVlef3ALvNKFwUfDi3K/R8eoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gIAhg/AoHKQAKAuNBkYM2w2YPol6xwZpwflWttGQAqq9sYCjINAwa3QDQc1n5rbpw==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
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
  "id": -576460752303422800,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuECNvsKh8c84BM7+ZAXQEacLtskvb2yu/NkKxG6X5WoH0A8HzVM6nJvQBInodXkckkZPW+QtqkXcDwjtfpygR/kDuHT4cjMBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgLjQZGDNsNmD6JescGacH5VrbRkAKqvbGAoyDQMGt0A0HNYa8rUI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422800,
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "signed_tx": "tx_+LwLAfhCuECNvsKh8c84BM7+ZAXQEacLtskvb2yu/NkKxG6X5WoH0A8HzVM6nJvQBInodXkckkZPW+QtqkXcDwjtfpygR/kDuHT4cjMBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgLjQZGDNsNmD6JescGacH5VrbRkAKqvbGAoyDQMGt0A0HNYa8rUI=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
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
  "id": -576460752303422799,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuECNvsKh8c84BM7+ZAXQEacLtskvb2yu/NkKxG6X5WoH0A8HzVM6nJvQBInodXkckkZPW+QtqkXcDwjtfpygR/kDuECn3w8yUlT1bmSdNr4eQl6SybGPf2jWNL18m4owfk3iInn4oxTNPXtl/QvgRYsS39pdZ+nfUZ0zyxkC8oSV64YOuHT4cjMBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgLjQZGDNsNmD6JescGacH5VrbRkAKqvbGAoyDQMGt0A0HNRn9FMg="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422799,
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
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuECNvsKh8c84BM7+ZAXQEacLtskvb2yu/NkKxG6X5WoH0A8HzVM6nJvQBInodXkckkZPW+QtqkXcDwjtfpygR/kDuECn3w8yUlT1bmSdNr4eQl6SybGPf2jWNL18m4owfk3iInn4oxTNPXtl/QvgRYsS39pdZ+nfUZ0zyxkC8oSV64YOuHT4cjMBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgLjQZGDNsNmD6JescGacH5VrbRkAKqvbGAoyDQMGt0A0HNRn9FMg=",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuECNvsKh8c84BM7+ZAXQEacLtskvb2yu/NkKxG6X5WoH0A8HzVM6nJvQBInodXkckkZPW+QtqkXcDwjtfpygR/kDuECn3w8yUlT1bmSdNr4eQl6SybGPf2jWNL18m4owfk3iInn4oxTNPXtl/QvgRYsS39pdZ+nfUZ0zyxkC8oSV64YOuHT4cjMBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgLjQZGDNsNmD6JescGacH5VrbRkAKqvbGAoyDQMGt0A0HNRn9FMg=",
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
      "tx": "tx_+P4LAfiEuECNvsKh8c84BM7+ZAXQEacLtskvb2yu/NkKxG6X5WoH0A8HzVM6nJvQBInodXkckkZPW+QtqkXcDwjtfpygR/kDuECn3w8yUlT1bmSdNr4eQl6SybGPf2jWNL18m4owfk3iInn4oxTNPXtl/QvgRYsS39pdZ+nfUZ0zyxkC8oSV64YOuHT4cjMBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgLjQZGDNsNmD6JescGacH5VrbRkAKqvbGAoyDQMGt0A0HNRn9FMg=",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECNvsKh8c84BM7+ZAXQEacLtskvb2yu/NkKxG6X5WoH0A8HzVM6nJvQBInodXkckkZPW+QtqkXcDwjtfpygR/kDuECn3w8yUlT1bmSdNr4eQl6SybGPf2jWNL18m4owfk3iInn4oxTNPXtl/QvgRYsS39pdZ+nfUZ0zyxkC8oSV64YOuHT4cjMBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgLjQZGDNsNmD6JescGacH5VrbRkAKqvbGAoyDQMGt0A0HNRn9FMg=",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "state": "tx_+P4LAfiEuECNvsKh8c84BM7+ZAXQEacLtskvb2yu/NkKxG6X5WoH0A8HzVM6nJvQBInodXkckkZPW+QtqkXcDwjtfpygR/kDuECn3w8yUlT1bmSdNr4eQl6SybGPf2jWNL18m4owfk3iInn4oxTNPXtl/QvgRYsS39pdZ+nfUZ0zyxkC8oSV64YOuHT4cjMBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgLjQZGDNsNmD6JescGacH5VrbRkAKqvbGAoyDQMGt0A0HNRn9FMg="
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
      "state": "tx_+P4LAfiEuECNvsKh8c84BM7+ZAXQEacLtskvb2yu/NkKxG6X5WoH0A8HzVM6nJvQBInodXkckkZPW+QtqkXcDwjtfpygR/kDuECn3w8yUlT1bmSdNr4eQl6SybGPf2jWNL18m4owfk3iInn4oxTNPXtl/QvgRYsS39pdZ+nfUZ0zyxkC8oSV64YOuHT4cjMBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgLjQZGDNsNmD6JescGacH5VrbRkAKqvbGAoyDQMGt0A0HNRn9FMg="
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
  "method": "channels.deposit",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBsbBWu/xVpTJkxB+RilACEVlef3ALvNKFwUfDi3K/R8eoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AIAhg/AoHKQAKD+fxSqIANFrWFpl6S37H+AxDURixyA8pYVqNituUz3HwgVZcl8Dw==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
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
  "id": -576460752303422798,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEAHMlnEYWhmYdpFvLoRuS2HHU91TAc4V7XRhCepZyZIQlBuLup4KwUuUpEFl5lejJjitkACUg9Ugu6gCzUmXQcFuHT4cjMBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACg/n8UqiADRa1haZekt+x/gMQ1EYscgPKWFajYrblM9x8IFc5pRLo="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422798,
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEAHMlnEYWhmYdpFvLoRuS2HHU91TAc4V7XRhCepZyZIQlBuLup4KwUuUpEFl5lejJjitkACUg9Ugu6gCzUmXQcFuHT4cjMBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACg/n8UqiADRa1haZekt+x/gMQ1EYscgPKWFajYrblM9x8IFc5pRLo=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
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
  "id": -576460752303422797,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEAHMlnEYWhmYdpFvLoRuS2HHU91TAc4V7XRhCepZyZIQlBuLup4KwUuUpEFl5lejJjitkACUg9Ugu6gCzUmXQcFuECE2IQ6V8mcxQdXMq5cx/g3kdQkyr3B/oVNvXFjgVAex6hxKvXhUI/niTUQRAqQxeNi1ePp4hQSUqDQSqyxkKYPuHT4cjMBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACg/n8UqiADRa1haZekt+x/gMQ1EYscgPKWFajYrblM9x8IFe+NKEc="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
  "id": -576460752303422797,
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
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEAHMlnEYWhmYdpFvLoRuS2HHU91TAc4V7XRhCepZyZIQlBuLup4KwUuUpEFl5lejJjitkACUg9Ugu6gCzUmXQcFuECE2IQ6V8mcxQdXMq5cx/g3kdQkyr3B/oVNvXFjgVAex6hxKvXhUI/niTUQRAqQxeNi1ePp4hQSUqDQSqyxkKYPuHT4cjMBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACg/n8UqiADRa1haZekt+x/gMQ1EYscgPKWFajYrblM9x8IFe+NKEc=",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEAHMlnEYWhmYdpFvLoRuS2HHU91TAc4V7XRhCepZyZIQlBuLup4KwUuUpEFl5lejJjitkACUg9Ugu6gCzUmXQcFuECE2IQ6V8mcxQdXMq5cx/g3kdQkyr3B/oVNvXFjgVAex6hxKvXhUI/niTUQRAqQxeNi1ePp4hQSUqDQSqyxkKYPuHT4cjMBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACg/n8UqiADRa1haZekt+x/gMQ1EYscgPKWFajYrblM9x8IFe+NKEc=",
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
      "tx": "tx_+P4LAfiEuEAHMlnEYWhmYdpFvLoRuS2HHU91TAc4V7XRhCepZyZIQlBuLup4KwUuUpEFl5lejJjitkACUg9Ugu6gCzUmXQcFuECE2IQ6V8mcxQdXMq5cx/g3kdQkyr3B/oVNvXFjgVAex6hxKvXhUI/niTUQRAqQxeNi1ePp4hQSUqDQSqyxkKYPuHT4cjMBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACg/n8UqiADRa1haZekt+x/gMQ1EYscgPKWFajYrblM9x8IFe+NKEc=",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAHMlnEYWhmYdpFvLoRuS2HHU91TAc4V7XRhCepZyZIQlBuLup4KwUuUpEFl5lejJjitkACUg9Ugu6gCzUmXQcFuECE2IQ6V8mcxQdXMq5cx/g3kdQkyr3B/oVNvXFjgVAex6hxKvXhUI/niTUQRAqQxeNi1ePp4hQSUqDQSqyxkKYPuHT4cjMBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACg/n8UqiADRa1haZekt+x/gMQ1EYscgPKWFajYrblM9x8IFe+NKEc=",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
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
    "channel_id": "ch_2WXwMpXo4kgqEYsUeBjmxDJpNVaqZvXXHPCs9bjBy4eXBQqWDD",
    "data": {
      "state": "tx_+P4LAfiEuEAHMlnEYWhmYdpFvLoRuS2HHU91TAc4V7XRhCepZyZIQlBuLup4KwUuUpEFl5lejJjitkACUg9Ugu6gCzUmXQcFuECE2IQ6V8mcxQdXMq5cx/g3kdQkyr3B/oVNvXFjgVAex6hxKvXhUI/niTUQRAqQxeNi1ePp4hQSUqDQSqyxkKYPuHT4cjMBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACg/n8UqiADRa1haZekt+x/gMQ1EYscgPKWFajYrblM9x8IFe+NKEc="
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
      "state": "tx_+P4LAfiEuEAHMlnEYWhmYdpFvLoRuS2HHU91TAc4V7XRhCepZyZIQlBuLup4KwUuUpEFl5lejJjitkACUg9Ugu6gCzUmXQcFuECE2IQ6V8mcxQdXMq5cx/g3kdQkyr3B/oVNvXFjgVAex6hxKvXhUI/niTUQRAqQxeNi1ePp4hQSUqDQSqyxkKYPuHT4cjMBoQbGwVrv8VaUyZMQfkYpQAhFZXn9wC7zShcFHw4tyv0fHqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACg/n8UqiADRa1haZekt+x/gMQ1EYscgPKWFajYrblM9x8IFe+NKEc="
    }
  },
  "version": 1
}
```
