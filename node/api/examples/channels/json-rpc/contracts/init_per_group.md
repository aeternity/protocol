
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2afubvL8UDGqFsteeTt5qnhrDLB9Ug8kD6FUjCrA2AD9zgWz5Y&keep_running=false&lock_period=10&port=13216&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2okQjdsLfaEJWTpFMRj1qMGBUHif6dbWveXg6bS3wqTbvPceiF&role=initiator
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_rdWPfzzu+YmlM++i0VsWkbgQiO4Bya5xLorwG8LXLUmTYJvJ"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2afubvL8UDGqFsteeTt5qnhrDLB9Ug8kD6FUjCrA2AD9zgWz5Y&keep_running=false&lock_period=10&port=13216&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2okQjdsLfaEJWTpFMRj1qMGBUHif6dbWveXg6bS3wqTbvPceiF&role=responder
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_D9oABJPbswDxxbvZTJAlEJ8hHbgSfYBeRyV8EVex3TNZ7EmO"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_open"
    }
  },
  "version": 1
}
```

#### responder info
> Received an WebSocket opening request

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_accept"
    }
  },
  "version": 1
}
```

#### initiator info
> Received an WebSocket connection accepted

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAdAmWGoZAtUf3YylfES2FplatBchIPRe8gTbWNdC3VRrhj+qJSJgAKEB7dgZRvEzn+d30DT4VlaAMxLs4Sh6jlvkNTgih2YRK+iGJGE5yoAAAgoAhhAGeddIAMCg2dipyd1qRwAa5Y8V0N8361esLjAAL52T5FF/KtWL8KUBN7g3Qw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422742,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBlyoe6NyVul2nzMHWcx5xUIUMtTfUmA+sU63Zf6nUutaMcsvIMRfZDiGibZ+wEQpgvQJRQVmj5KYU9enDpLYcLuIP4gTIBoQHQJlhqGQLVH92MpXxEthaZWrQXISD0XvIE21jXQt1Ua4Y/qiUiYAChAe3YGUbxM5/nd9A0+FZWgDMS7OEoeo5b5DU4IodmESvohiRhOcqAAAIKAIYQBnnXSADAoNnYqcndakcAGuWPFdDfN+tXrC4wAC+dk+RRfyrVi/ClAe1cNCU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422742,
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
    "channel_id": null,
    "data": {
      "event": "funding_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+MsLAfhCuEBlyoe6NyVul2nzMHWcx5xUIUMtTfUmA+sU63Zf6nUutaMcsvIMRfZDiGibZ+wEQpgvQJRQVmj5KYU9enDpLYcLuIP4gTIBoQHQJlhqGQLVH92MpXxEthaZWrQXISD0XvIE21jXQt1Ua4Y/qiUiYAChAe3YGUbxM5/nd9A0+FZWgDMS7OEoeo5b5DU4IodmESvohiRhOcqAAAIKAIYQBnnXSADAoNnYqcndakcAGuWPFdDfN+tXrC4wAC+dk+RRfyrVi/ClAe1cNCU=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422741,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAZcqHujclbpdp8zB1nMecVCFDLU31JgPrFOt2X+p1LrWjHLLyDEX2Q4hom2fsBEKYL0CUUFZo+SmFPXpw6S2HC7hAzGIbKxspHLxsf4bCaczAHxrvpjWvZuDJYQ1X388Y8jgE2JvQYNl/F3j5RTynP70uJODQsB9oOkzzhKAWjmFTBbiD+IEyAaEB0CZYahkC1R/djKV8RLYWmVq0FyEg9F7yBNtY10LdVGuGP6olImAAoQHt2BlG8TOf53fQNPhWVoAzEuzhKHqOW+Q1OCKHZhEr6IYkYTnKgAACCgCGEAZ510gAwKDZ2KnJ3WpHABrljxXQ3zfrV6wuMAAvnZPkUX8q1YvwpQGszrI2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422741,
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
    "channel_id": "ch_Khv8ShMXvZTSQbCafdWcGkpF6YyejTFKEVFU5rPCMTNkpHfnr",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAZcqHujclbpdp8zB1nMecVCFDLU31JgPrFOt2X+p1LrWjHLLyDEX2Q4hom2fsBEKYL0CUUFZo+SmFPXpw6S2HC7hAzGIbKxspHLxsf4bCaczAHxrvpjWvZuDJYQ1X388Y8jgE2JvQYNl/F3j5RTynP70uJODQsB9oOkzzhKAWjmFTBbiD+IEyAaEB0CZYahkC1R/djKV8RLYWmVq0FyEg9F7yBNtY10LdVGuGP6olImAAoQHt2BlG8TOf53fQNPhWVoAzEuzhKHqOW+Q1OCKHZhEr6IYkYTnKgAACCgCGEAZ510gAwKDZ2KnJ3WpHABrljxXQ3zfrV6wuMAAvnZPkUX8q1YvwpQGszrI2",
      "type": "channel_create_tx"
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
    "channel_id": null,
    "data": {
      "event": "funding_signed"
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
    "channel_id": "ch_Khv8ShMXvZTSQbCafdWcGkpF6YyejTFKEVFU5rPCMTNkpHfnr",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAZcqHujclbpdp8zB1nMecVCFDLU31JgPrFOt2X+p1LrWjHLLyDEX2Q4hom2fsBEKYL0CUUFZo+SmFPXpw6S2HC7hAzGIbKxspHLxsf4bCaczAHxrvpjWvZuDJYQ1X388Y8jgE2JvQYNl/F3j5RTynP70uJODQsB9oOkzzhKAWjmFTBbiD+IEyAaEB0CZYahkC1R/djKV8RLYWmVq0FyEg9F7yBNtY10LdVGuGP6olImAAoQHt2BlG8TOf53fQNPhWVoAzEuzhKHqOW+Q1OCKHZhEr6IYkYTnKgAACCgCGEAZ510gAwKDZ2KnJ3WpHABrljxXQ3zfrV6wuMAAvnZPkUX8q1YvwpQGszrI2",
      "type": "channel_create_tx"
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
    "channel_id": "ch_Khv8ShMXvZTSQbCafdWcGkpF6YyejTFKEVFU5rPCMTNkpHfnr",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAZcqHujclbpdp8zB1nMecVCFDLU31JgPrFOt2X+p1LrWjHLLyDEX2Q4hom2fsBEKYL0CUUFZo+SmFPXpw6S2HC7hAzGIbKxspHLxsf4bCaczAHxrvpjWvZuDJYQ1X388Y8jgE2JvQYNl/F3j5RTynP70uJODQsB9oOkzzhKAWjmFTBbiD+IEyAaEB0CZYahkC1R/djKV8RLYWmVq0FyEg9F7yBNtY10LdVGuGP6olImAAoQHt2BlG8TOf53fQNPhWVoAzEuzhKHqOW+Q1OCKHZhEr6IYkYTnKgAACCgCGEAZ510gAwKDZ2KnJ3WpHABrljxXQ3zfrV6wuMAAvnZPkUX8q1YvwpQGszrI2",
      "type": "channel_create_tx"
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
    "channel_id": "ch_Khv8ShMXvZTSQbCafdWcGkpF6YyejTFKEVFU5rPCMTNkpHfnr",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAZcqHujclbpdp8zB1nMecVCFDLU31JgPrFOt2X+p1LrWjHLLyDEX2Q4hom2fsBEKYL0CUUFZo+SmFPXpw6S2HC7hAzGIbKxspHLxsf4bCaczAHxrvpjWvZuDJYQ1X388Y8jgE2JvQYNl/F3j5RTynP70uJODQsB9oOkzzhKAWjmFTBbiD+IEyAaEB0CZYahkC1R/djKV8RLYWmVq0FyEg9F7yBNtY10LdVGuGP6olImAAoQHt2BlG8TOf53fQNPhWVoAzEuzhKHqOW+Q1OCKHZhEr6IYkYTnKgAACCgCGEAZ510gAwKDZ2KnJ3WpHABrljxXQ3zfrV6wuMAAvnZPkUX8q1YvwpQGszrI2",
      "type": "channel_create_tx"
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
    "to": "ak_2okQjdsLfaEJWTpFMRj1qMGBUHif6dbWveXg6bS3wqTbvPceiF"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_Khv8ShMXvZTSQbCafdWcGkpF6YyejTFKEVFU5rPCMTNkpHfnr",
    "data": {
      "message": {
        "channel_id": "ch_Khv8ShMXvZTSQbCafdWcGkpF6YyejTFKEVFU5rPCMTNkpHfnr",
        "from": "ak_2afubvL8UDGqFsteeTt5qnhrDLB9Ug8kD6FUjCrA2AD9zgWz5Y",
        "info": "Hello",
        "to": "ak_2okQjdsLfaEJWTpFMRj1qMGBUHif6dbWveXg6bS3wqTbvPceiF"
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
    "to": "ak_2afubvL8UDGqFsteeTt5qnhrDLB9Ug8kD6FUjCrA2AD9zgWz5Y"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_Khv8ShMXvZTSQbCafdWcGkpF6YyejTFKEVFU5rPCMTNkpHfnr",
    "data": {
      "message": {
        "channel_id": "ch_Khv8ShMXvZTSQbCafdWcGkpF6YyejTFKEVFU5rPCMTNkpHfnr",
        "from": "ak_2okQjdsLfaEJWTpFMRj1qMGBUHif6dbWveXg6bS3wqTbvPceiF",
        "info": "Hello back",
        "to": "ak_2afubvL8UDGqFsteeTt5qnhrDLB9Ug8kD6FUjCrA2AD9zgWz5Y"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422740,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2afubvL8UDGqFsteeTt5qnhrDLB9Ug8kD6FUjCrA2AD9zgWz5Y",
      "ak_2okQjdsLfaEJWTpFMRj1qMGBUHif6dbWveXg6bS3wqTbvPceiF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Khv8ShMXvZTSQbCafdWcGkpF6YyejTFKEVFU5rPCMTNkpHfnr",
  "id": -576460752303422740,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2afubvL8UDGqFsteeTt5qnhrDLB9Ug8kD6FUjCrA2AD9zgWz5Y",
      "balance": 69999999999999
    },
    {
      "account": "ak_2okQjdsLfaEJWTpFMRj1qMGBUHif6dbWveXg6bS3wqTbvPceiF",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_Khv8ShMXvZTSQbCafdWcGkpF6YyejTFKEVFU5rPCMTNkpHfnr",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_Khv8ShMXvZTSQbCafdWcGkpF6YyejTFKEVFU5rPCMTNkpHfnr",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_Khv8ShMXvZTSQbCafdWcGkpF6YyejTFKEVFU5rPCMTNkpHfnr",
    "data": {
      "event": "funding_locked"
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
    "channel_id": "ch_Khv8ShMXvZTSQbCafdWcGkpF6YyejTFKEVFU5rPCMTNkpHfnr",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### initiator info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_Khv8ShMXvZTSQbCafdWcGkpF6YyejTFKEVFU5rPCMTNkpHfnr",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Channel is `open` and ready to use

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_Khv8ShMXvZTSQbCafdWcGkpF6YyejTFKEVFU5rPCMTNkpHfnr",
    "data": {
      "state": "tx_+QENCwH4hLhAZcqHujclbpdp8zB1nMecVCFDLU31JgPrFOt2X+p1LrWjHLLyDEX2Q4hom2fsBEKYL0CUUFZo+SmFPXpw6S2HC7hAzGIbKxspHLxsf4bCaczAHxrvpjWvZuDJYQ1X388Y8jgE2JvQYNl/F3j5RTynP70uJODQsB9oOkzzhKAWjmFTBbiD+IEyAaEB0CZYahkC1R/djKV8RLYWmVq0FyEg9F7yBNtY10LdVGuGP6olImAAoQHt2BlG8TOf53fQNPhWVoAzEuzhKHqOW+Q1OCKHZhEr6IYkYTnKgAACCgCGEAZ510gAwKDZ2KnJ3WpHABrljxXQ3zfrV6wuMAAvnZPkUX8q1YvwpQGszrI2"
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
    "channel_id": "ch_Khv8ShMXvZTSQbCafdWcGkpF6YyejTFKEVFU5rPCMTNkpHfnr",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_Khv8ShMXvZTSQbCafdWcGkpF6YyejTFKEVFU5rPCMTNkpHfnr",
    "data": {
      "state": "tx_+QENCwH4hLhAZcqHujclbpdp8zB1nMecVCFDLU31JgPrFOt2X+p1LrWjHLLyDEX2Q4hom2fsBEKYL0CUUFZo+SmFPXpw6S2HC7hAzGIbKxspHLxsf4bCaczAHxrvpjWvZuDJYQ1X388Y8jgE2JvQYNl/F3j5RTynP70uJODQsB9oOkzzhKAWjmFTBbiD+IEyAaEB0CZYahkC1R/djKV8RLYWmVq0FyEg9F7yBNtY10LdVGuGP6olImAAoQHt2BlG8TOf53fQNPhWVoAzEuzhKHqOW+Q1OCKHZhEr6IYkYTnKgAACCgCGEAZ510gAwKDZ2KnJ3WpHABrljxXQ3zfrV6wuMAAvnZPkUX8q1YvwpQGszrI2"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_25sx8ZB6s29etgQkD3rw75tcWjRCMVoNAGdnERb6USS1kDNt2p&keep_running=false&lock_period=10&port=12652&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2WtPbZWpy6M2PvWy5qjf2vJj6mnaJwyBSF8tfZkRc7JaF1FrMn&role=initiator
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_Wo6t+xfcZAbg2/Nhwz8HFv3PwkJdz5qa/cqqrSR9nYo0JACy"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_25sx8ZB6s29etgQkD3rw75tcWjRCMVoNAGdnERb6USS1kDNt2p&keep_running=false&lock_period=10&port=12652&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2WtPbZWpy6M2PvWy5qjf2vJj6mnaJwyBSF8tfZkRc7JaF1FrMn&role=responder
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_4XPufwmJMXQ2YAIdMUE7j7L1hJJGJVEoA5hL6+LK7fT8DyQ/"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_open"
    }
  },
  "version": 1
}
```

#### responder info
> Received an WebSocket opening request

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_accept"
    }
  },
  "version": 1
}
```

#### initiator info
> Received an WebSocket connection accepted

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAY7F8luzRYUwlzbPXWmClOf7FVwS5ulg7kfMAl+rVsp6hj+qJSJgAKEBx45Ud7P20+P9AM494X1K1pS1uUbyHIpEI4wTQU7Ii+GGJGE5yoAAAgoAhhAGeddIAMCg/n2I6du0zfeCVr5CT4I6/nXKQNXurk2LzLGEAT2+yoABuGZ/hw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422095,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECXiKtnWp5QpRUzn76BQ1qOZNHqm1KpM6F7knNCF9pLRd8CUdKlmyu1wwibyITKIxmZFMy7eZNZVDkr0Rhx+SALuIP4gTIBoQGOxfJbs0WFMJc2z11pgpTn+xVcEubpYO5HzAJfq1bKeoY/qiUiYAChAceOVHez9tPj/QDOPeF9StaUtblG8hyKRCOME0FOyIvhhiRhOcqAAAIKAIYQBnnXSADAoP59iOnbtM33gla+Qk+COv51ykDV7q5Ni8yxhAE9vsqAAStI13E="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422095,
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
    "channel_id": null,
    "data": {
      "event": "funding_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+MsLAfhCuECXiKtnWp5QpRUzn76BQ1qOZNHqm1KpM6F7knNCF9pLRd8CUdKlmyu1wwibyITKIxmZFMy7eZNZVDkr0Rhx+SALuIP4gTIBoQGOxfJbs0WFMJc2z11pgpTn+xVcEubpYO5HzAJfq1bKeoY/qiUiYAChAceOVHez9tPj/QDOPeF9StaUtblG8hyKRCOME0FOyIvhhiRhOcqAAAIKAIYQBnnXSADAoP59iOnbtM33gla+Qk+COv51ykDV7q5Ni8yxhAE9vsqAAStI13E=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422094,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhASkMiHcivYSnMzn+ME7+o/i4lp7T5p2BLxMnTp+MlX0uVHXjt6BbPY6p/vKe3WCgAZGS5smRPBfEVEXH3XMLzCbhAl4irZ1qeUKUVM5++gUNajmTR6ptSqTOhe5JzQhfaS0XfAlHSpZsrtcMIm8iEyiMZmRTMu3mTWVQ5K9EYcfkgC7iD+IEyAaEBjsXyW7NFhTCXNs9daYKU5/sVXBLm6WDuR8wCX6tWynqGP6olImAAoQHHjlR3s/bT4/0Azj3hfUrWlLW5RvIcikQjjBNBTsiL4YYkYTnKgAACCgCGEAZ510gAwKD+fYjp27TN94JWvkJPgjr+dcpA1e6uTYvMsYQBPb7KgAF2s+Wv"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422094,
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
    "channel_id": "ch_UQhHAzo1A1NNa4dYzNL1XNGFuFdTKSTy4Ct3H7pN7SH3jpN9G",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhASkMiHcivYSnMzn+ME7+o/i4lp7T5p2BLxMnTp+MlX0uVHXjt6BbPY6p/vKe3WCgAZGS5smRPBfEVEXH3XMLzCbhAl4irZ1qeUKUVM5++gUNajmTR6ptSqTOhe5JzQhfaS0XfAlHSpZsrtcMIm8iEyiMZmRTMu3mTWVQ5K9EYcfkgC7iD+IEyAaEBjsXyW7NFhTCXNs9daYKU5/sVXBLm6WDuR8wCX6tWynqGP6olImAAoQHHjlR3s/bT4/0Azj3hfUrWlLW5RvIcikQjjBNBTsiL4YYkYTnKgAACCgCGEAZ510gAwKD+fYjp27TN94JWvkJPgjr+dcpA1e6uTYvMsYQBPb7KgAF2s+Wv",
      "type": "channel_create_tx"
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
    "channel_id": null,
    "data": {
      "event": "funding_signed"
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
    "channel_id": "ch_UQhHAzo1A1NNa4dYzNL1XNGFuFdTKSTy4Ct3H7pN7SH3jpN9G",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhASkMiHcivYSnMzn+ME7+o/i4lp7T5p2BLxMnTp+MlX0uVHXjt6BbPY6p/vKe3WCgAZGS5smRPBfEVEXH3XMLzCbhAl4irZ1qeUKUVM5++gUNajmTR6ptSqTOhe5JzQhfaS0XfAlHSpZsrtcMIm8iEyiMZmRTMu3mTWVQ5K9EYcfkgC7iD+IEyAaEBjsXyW7NFhTCXNs9daYKU5/sVXBLm6WDuR8wCX6tWynqGP6olImAAoQHHjlR3s/bT4/0Azj3hfUrWlLW5RvIcikQjjBNBTsiL4YYkYTnKgAACCgCGEAZ510gAwKD+fYjp27TN94JWvkJPgjr+dcpA1e6uTYvMsYQBPb7KgAF2s+Wv",
      "type": "channel_create_tx"
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
    "channel_id": "ch_UQhHAzo1A1NNa4dYzNL1XNGFuFdTKSTy4Ct3H7pN7SH3jpN9G",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhASkMiHcivYSnMzn+ME7+o/i4lp7T5p2BLxMnTp+MlX0uVHXjt6BbPY6p/vKe3WCgAZGS5smRPBfEVEXH3XMLzCbhAl4irZ1qeUKUVM5++gUNajmTR6ptSqTOhe5JzQhfaS0XfAlHSpZsrtcMIm8iEyiMZmRTMu3mTWVQ5K9EYcfkgC7iD+IEyAaEBjsXyW7NFhTCXNs9daYKU5/sVXBLm6WDuR8wCX6tWynqGP6olImAAoQHHjlR3s/bT4/0Azj3hfUrWlLW5RvIcikQjjBNBTsiL4YYkYTnKgAACCgCGEAZ510gAwKD+fYjp27TN94JWvkJPgjr+dcpA1e6uTYvMsYQBPb7KgAF2s+Wv",
      "type": "channel_create_tx"
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
    "channel_id": "ch_UQhHAzo1A1NNa4dYzNL1XNGFuFdTKSTy4Ct3H7pN7SH3jpN9G",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhASkMiHcivYSnMzn+ME7+o/i4lp7T5p2BLxMnTp+MlX0uVHXjt6BbPY6p/vKe3WCgAZGS5smRPBfEVEXH3XMLzCbhAl4irZ1qeUKUVM5++gUNajmTR6ptSqTOhe5JzQhfaS0XfAlHSpZsrtcMIm8iEyiMZmRTMu3mTWVQ5K9EYcfkgC7iD+IEyAaEBjsXyW7NFhTCXNs9daYKU5/sVXBLm6WDuR8wCX6tWynqGP6olImAAoQHHjlR3s/bT4/0Azj3hfUrWlLW5RvIcikQjjBNBTsiL4YYkYTnKgAACCgCGEAZ510gAwKD+fYjp27TN94JWvkJPgjr+dcpA1e6uTYvMsYQBPb7KgAF2s+Wv",
      "type": "channel_create_tx"
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
    "to": "ak_2WtPbZWpy6M2PvWy5qjf2vJj6mnaJwyBSF8tfZkRc7JaF1FrMn"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_UQhHAzo1A1NNa4dYzNL1XNGFuFdTKSTy4Ct3H7pN7SH3jpN9G",
    "data": {
      "message": {
        "channel_id": "ch_UQhHAzo1A1NNa4dYzNL1XNGFuFdTKSTy4Ct3H7pN7SH3jpN9G",
        "from": "ak_25sx8ZB6s29etgQkD3rw75tcWjRCMVoNAGdnERb6USS1kDNt2p",
        "info": "Hello",
        "to": "ak_2WtPbZWpy6M2PvWy5qjf2vJj6mnaJwyBSF8tfZkRc7JaF1FrMn"
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
    "to": "ak_25sx8ZB6s29etgQkD3rw75tcWjRCMVoNAGdnERb6USS1kDNt2p"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_UQhHAzo1A1NNa4dYzNL1XNGFuFdTKSTy4Ct3H7pN7SH3jpN9G",
    "data": {
      "message": {
        "channel_id": "ch_UQhHAzo1A1NNa4dYzNL1XNGFuFdTKSTy4Ct3H7pN7SH3jpN9G",
        "from": "ak_2WtPbZWpy6M2PvWy5qjf2vJj6mnaJwyBSF8tfZkRc7JaF1FrMn",
        "info": "Hello back",
        "to": "ak_25sx8ZB6s29etgQkD3rw75tcWjRCMVoNAGdnERb6USS1kDNt2p"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422093,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_25sx8ZB6s29etgQkD3rw75tcWjRCMVoNAGdnERb6USS1kDNt2p",
      "ak_2WtPbZWpy6M2PvWy5qjf2vJj6mnaJwyBSF8tfZkRc7JaF1FrMn"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_UQhHAzo1A1NNa4dYzNL1XNGFuFdTKSTy4Ct3H7pN7SH3jpN9G",
  "id": -576460752303422093,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_25sx8ZB6s29etgQkD3rw75tcWjRCMVoNAGdnERb6USS1kDNt2p",
      "balance": 69999999999999
    },
    {
      "account": "ak_2WtPbZWpy6M2PvWy5qjf2vJj6mnaJwyBSF8tfZkRc7JaF1FrMn",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_UQhHAzo1A1NNa4dYzNL1XNGFuFdTKSTy4Ct3H7pN7SH3jpN9G",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_UQhHAzo1A1NNa4dYzNL1XNGFuFdTKSTy4Ct3H7pN7SH3jpN9G",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_UQhHAzo1A1NNa4dYzNL1XNGFuFdTKSTy4Ct3H7pN7SH3jpN9G",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_UQhHAzo1A1NNa4dYzNL1XNGFuFdTKSTy4Ct3H7pN7SH3jpN9G",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_UQhHAzo1A1NNa4dYzNL1XNGFuFdTKSTy4Ct3H7pN7SH3jpN9G",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_UQhHAzo1A1NNa4dYzNL1XNGFuFdTKSTy4Ct3H7pN7SH3jpN9G",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder info
> Channel is `open` and ready to use

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_UQhHAzo1A1NNa4dYzNL1XNGFuFdTKSTy4Ct3H7pN7SH3jpN9G",
    "data": {
      "state": "tx_+QENCwH4hLhASkMiHcivYSnMzn+ME7+o/i4lp7T5p2BLxMnTp+MlX0uVHXjt6BbPY6p/vKe3WCgAZGS5smRPBfEVEXH3XMLzCbhAl4irZ1qeUKUVM5++gUNajmTR6ptSqTOhe5JzQhfaS0XfAlHSpZsrtcMIm8iEyiMZmRTMu3mTWVQ5K9EYcfkgC7iD+IEyAaEBjsXyW7NFhTCXNs9daYKU5/sVXBLm6WDuR8wCX6tWynqGP6olImAAoQHHjlR3s/bT4/0Azj3hfUrWlLW5RvIcikQjjBNBTsiL4YYkYTnKgAACCgCGEAZ510gAwKD+fYjp27TN94JWvkJPgjr+dcpA1e6uTYvMsYQBPb7KgAF2s+Wv"
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
    "channel_id": "ch_UQhHAzo1A1NNa4dYzNL1XNGFuFdTKSTy4Ct3H7pN7SH3jpN9G",
    "data": {
      "state": "tx_+QENCwH4hLhASkMiHcivYSnMzn+ME7+o/i4lp7T5p2BLxMnTp+MlX0uVHXjt6BbPY6p/vKe3WCgAZGS5smRPBfEVEXH3XMLzCbhAl4irZ1qeUKUVM5++gUNajmTR6ptSqTOhe5JzQhfaS0XfAlHSpZsrtcMIm8iEyiMZmRTMu3mTWVQ5K9EYcfkgC7iD+IEyAaEBjsXyW7NFhTCXNs9daYKU5/sVXBLm6WDuR8wCX6tWynqGP6olImAAoQHHjlR3s/bT4/0Azj3hfUrWlLW5RvIcikQjjBNBTsiL4YYkYTnKgAACCgCGEAZ510gAwKD+fYjp27TN94JWvkJPgjr+dcpA1e6uTYvMsYQBPb7KgAF2s+Wv"
    }
  },
  "version": 1
}
```
