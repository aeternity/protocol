
#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello",
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "message": {
        "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "info": "Hello",
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "message": {
        "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "info": "Hello back",
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
  "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "message": {
        "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "info": "Hello",
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "message": {
        "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "info": "Hello back",
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBjkQAV3GxRR4BiusSvEAoR+N+0QpPoE+Ui4RUVILIeNHoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQIAhg/AoHKQAKBy7d2KOPanIgoeBduOtHrSep+GXgzluZAMk579K2VI8wQzZsnYPQ==",
      "updates": [
        {
          "amount": 2,
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
  "id": -576460752303422837,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEDKRJz0bESkVNQGIStGYdghv+JwZ7O+XS/wTodjB4BGKlaWrn8iDdUhQFq4fDR4kH8rAi5rpPiyJjxgyOuAsNAGuHT4cjQBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgcu3dijj2pyIKHgXbjrR60nqfhl4M5bmQDJOe/StlSPMEM5kv8OY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
  "id": -576460752303422837,
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEDKRJz0bESkVNQGIStGYdghv+JwZ7O+XS/wTodjB4BGKlaWrn8iDdUhQFq4fDR4kH8rAi5rpPiyJjxgyOuAsNAGuHT4cjQBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgcu3dijj2pyIKHgXbjrR60nqfhl4M5bmQDJOe/StlSPMEM5kv8OY=",
      "updates": [
        {
          "amount": 2,
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
  "id": -576460752303422836,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBKisbL7BnKDrGaj4AJZG9eDPo3Rxm0UNpaWFVuvpnLUOC5NRR4TZX+EpJl5EnYRTzp+2hsRD2nTv5ORHW9d5MMuEDKRJz0bESkVNQGIStGYdghv+JwZ7O+XS/wTodjB4BGKlaWrn8iDdUhQFq4fDR4kH8rAi5rpPiyJjxgyOuAsNAGuHT4cjQBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgcu3dijj2pyIKHgXbjrR60nqfhl4M5bmQDJOe/StlSPMEM66fI7w="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
  "id": -576460752303422836,
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEBKisbL7BnKDrGaj4AJZG9eDPo3Rxm0UNpaWFVuvpnLUOC5NRR4TZX+EpJl5EnYRTzp+2hsRD2nTv5ORHW9d5MMuEDKRJz0bESkVNQGIStGYdghv+JwZ7O+XS/wTodjB4BGKlaWrn8iDdUhQFq4fDR4kH8rAi5rpPiyJjxgyOuAsNAGuHT4cjQBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgcu3dijj2pyIKHgXbjrR60nqfhl4M5bmQDJOe/StlSPMEM66fI7w=",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEBKisbL7BnKDrGaj4AJZG9eDPo3Rxm0UNpaWFVuvpnLUOC5NRR4TZX+EpJl5EnYRTzp+2hsRD2nTv5ORHW9d5MMuEDKRJz0bESkVNQGIStGYdghv+JwZ7O+XS/wTodjB4BGKlaWrn8iDdUhQFq4fDR4kH8rAi5rpPiyJjxgyOuAsNAGuHT4cjQBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgcu3dijj2pyIKHgXbjrR60nqfhl4M5bmQDJOe/StlSPMEM66fI7w=",
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
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "message": {
        "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "info": "Hello",
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "message": {
        "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "info": "Hello back",
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBKisbL7BnKDrGaj4AJZG9eDPo3Rxm0UNpaWFVuvpnLUOC5NRR4TZX+EpJl5EnYRTzp+2hsRD2nTv5ORHW9d5MMuEDKRJz0bESkVNQGIStGYdghv+JwZ7O+XS/wTodjB4BGKlaWrn8iDdUhQFq4fDR4kH8rAi5rpPiyJjxgyOuAsNAGuHT4cjQBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgcu3dijj2pyIKHgXbjrR60nqfhl4M5bmQDJOe/StlSPMEM66fI7w=",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBKisbL7BnKDrGaj4AJZG9eDPo3Rxm0UNpaWFVuvpnLUOC5NRR4TZX+EpJl5EnYRTzp+2hsRD2nTv5ORHW9d5MMuEDKRJz0bESkVNQGIStGYdghv+JwZ7O+XS/wTodjB4BGKlaWrn8iDdUhQFq4fDR4kH8rAi5rpPiyJjxgyOuAsNAGuHT4cjQBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgcu3dijj2pyIKHgXbjrR60nqfhl4M5bmQDJOe/StlSPMEM66fI7w=",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "state": "tx_+P4LAfiEuEBKisbL7BnKDrGaj4AJZG9eDPo3Rxm0UNpaWFVuvpnLUOC5NRR4TZX+EpJl5EnYRTzp+2hsRD2nTv5ORHW9d5MMuEDKRJz0bESkVNQGIStGYdghv+JwZ7O+XS/wTodjB4BGKlaWrn8iDdUhQFq4fDR4kH8rAi5rpPiyJjxgyOuAsNAGuHT4cjQBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgcu3dijj2pyIKHgXbjrR60nqfhl4M5bmQDJOe/StlSPMEM66fI7w="
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "state": "tx_+P4LAfiEuEBKisbL7BnKDrGaj4AJZG9eDPo3Rxm0UNpaWFVuvpnLUOC5NRR4TZX+EpJl5EnYRTzp+2hsRD2nTv5ORHW9d5MMuEDKRJz0bESkVNQGIStGYdghv+JwZ7O+XS/wTodjB4BGKlaWrn8iDdUhQFq4fDR4kH8rAi5rpPiyJjxgyOuAsNAGuHT4cjQBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgcu3dijj2pyIKHgXbjrR60nqfhl4M5bmQDJOe/StlSPMEM66fI7w="
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
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "message": {
        "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "info": "Hello",
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "message": {
        "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "info": "Hello back",
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
  "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "message": {
        "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "info": "Hello",
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "message": {
        "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "info": "Hello back",
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
    "amount": 2
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBjkQAV3GxRR4BiusSvEAoR+N+0QpPoE+Ui4RUVILIeNHoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQIAhg/AoHKQAKBk/wgc02xPFpin8ZqQbLoxNebwyc6eA+R5uowuCfW4RgUURJUS5Q==",
      "updates": [
        {
          "amount": 2,
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
  "id": -576460752303422835,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuECTFgldNzJwIaJslNh+h/wWr1iNj3T4cgofVC/ySSrrq6zj8f0VkYq8us9ovqTcBAEUVoZZYLF2NmsG9MspW/MPuHT4cjQBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYFFC7J+hw="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
  "id": -576460752303422835,
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "signed_tx": "tx_+LwLAfhCuECTFgldNzJwIaJslNh+h/wWr1iNj3T4cgofVC/ySSrrq6zj8f0VkYq8us9ovqTcBAEUVoZZYLF2NmsG9MspW/MPuHT4cjQBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYFFC7J+hw=",
      "updates": [
        {
          "amount": 2,
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
  "id": -576460752303422834,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBFkCk40dQu0t6vdaFAs82wqAGtXJXMEQdOKKnkGgNwGFhu0Vh0b2kt09Bb9c3NV2r6xDdsoEX2b/tppxlFOvoKuECTFgldNzJwIaJslNh+h/wWr1iNj3T4cgofVC/ySSrrq6zj8f0VkYq8us9ovqTcBAEUVoZZYLF2NmsG9MspW/MPuHT4cjQBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYFFNOlQ2k="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
  "id": -576460752303422834,
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEBFkCk40dQu0t6vdaFAs82wqAGtXJXMEQdOKKnkGgNwGFhu0Vh0b2kt09Bb9c3NV2r6xDdsoEX2b/tppxlFOvoKuECTFgldNzJwIaJslNh+h/wWr1iNj3T4cgofVC/ySSrrq6zj8f0VkYq8us9ovqTcBAEUVoZZYLF2NmsG9MspW/MPuHT4cjQBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYFFNOlQ2k=",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEBFkCk40dQu0t6vdaFAs82wqAGtXJXMEQdOKKnkGgNwGFhu0Vh0b2kt09Bb9c3NV2r6xDdsoEX2b/tppxlFOvoKuECTFgldNzJwIaJslNh+h/wWr1iNj3T4cgofVC/ySSrrq6zj8f0VkYq8us9ovqTcBAEUVoZZYLF2NmsG9MspW/MPuHT4cjQBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYFFNOlQ2k=",
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
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "message": {
        "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
        "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
        "info": "Hello",
        "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "message": {
        "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
        "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
        "info": "Hello back",
        "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBFkCk40dQu0t6vdaFAs82wqAGtXJXMEQdOKKnkGgNwGFhu0Vh0b2kt09Bb9c3NV2r6xDdsoEX2b/tppxlFOvoKuECTFgldNzJwIaJslNh+h/wWr1iNj3T4cgofVC/ySSrrq6zj8f0VkYq8us9ovqTcBAEUVoZZYLF2NmsG9MspW/MPuHT4cjQBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYFFNOlQ2k=",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBFkCk40dQu0t6vdaFAs82wqAGtXJXMEQdOKKnkGgNwGFhu0Vh0b2kt09Bb9c3NV2r6xDdsoEX2b/tppxlFOvoKuECTFgldNzJwIaJslNh+h/wWr1iNj3T4cgofVC/ySSrrq6zj8f0VkYq8us9ovqTcBAEUVoZZYLF2NmsG9MspW/MPuHT4cjQBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYFFNOlQ2k=",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "state": "tx_+P4LAfiEuEBFkCk40dQu0t6vdaFAs82wqAGtXJXMEQdOKKnkGgNwGFhu0Vh0b2kt09Bb9c3NV2r6xDdsoEX2b/tppxlFOvoKuECTFgldNzJwIaJslNh+h/wWr1iNj3T4cgofVC/ySSrrq6zj8f0VkYq8us9ovqTcBAEUVoZZYLF2NmsG9MspW/MPuHT4cjQBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYFFNOlQ2k="
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "state": "tx_+P4LAfiEuEBFkCk40dQu0t6vdaFAs82wqAGtXJXMEQdOKKnkGgNwGFhu0Vh0b2kt09Bb9c3NV2r6xDdsoEX2b/tppxlFOvoKuECTFgldNzJwIaJslNh+h/wWr1iNj3T4cgofVC/ySSrrq6zj8f0VkYq8us9ovqTcBAEUVoZZYLF2NmsG9MspW/MPuHT4cjQBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgZP8IHNNsTxaYp/GakGy6MTXm8MnOngPkebqMLgn1uEYFFNOlQ2k="
    }
  },
  "version": 1
}
```
