
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
  "method": "channels.deposit",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBjkQAV3GxRR4BiusSvEAoR+N+0QpPoE+Ui4RUVILIeNHoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQIAhg/AoHKQAKAPDv3EgYxO6pJCcB7FVjOvZgsDtaevvDl0iT9iRjxNjgIyiGr8GQ==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
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
  "id": -576460752303422841,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEBMpSzbUe7Em/Mb0Md6haDLqPGIt+pXCoxJbiuw9972K5Lrh8xQkiHuCu3b8fzIbkOjDN1NNclHNph2C4kpgWgJuHT4cjMBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CMr0egck="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
  "id": -576460752303422841,
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEBMpSzbUe7Em/Mb0Md6haDLqPGIt+pXCoxJbiuw9972K5Lrh8xQkiHuCu3b8fzIbkOjDN1NNclHNph2C4kpgWgJuHT4cjMBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CMr0egck=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
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
  "id": -576460752303422840,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEArSUAKgqMh/HsLftJOwLAkTY0I7bUSDajEE8DG1t/uoIJsSqmaSi/FTu8Eb9j4ecspDSqrte4dm+wPCTGuU88EuEBMpSzbUe7Em/Mb0Md6haDLqPGIt+pXCoxJbiuw9972K5Lrh8xQkiHuCu3b8fzIbkOjDN1NNclHNph2C4kpgWgJuHT4cjMBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CMsyKdZ4="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
  "id": -576460752303422840,
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
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEArSUAKgqMh/HsLftJOwLAkTY0I7bUSDajEE8DG1t/uoIJsSqmaSi/FTu8Eb9j4ecspDSqrte4dm+wPCTGuU88EuEBMpSzbUe7Em/Mb0Md6haDLqPGIt+pXCoxJbiuw9972K5Lrh8xQkiHuCu3b8fzIbkOjDN1NNclHNph2C4kpgWgJuHT4cjMBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CMsyKdZ4=",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEArSUAKgqMh/HsLftJOwLAkTY0I7bUSDajEE8DG1t/uoIJsSqmaSi/FTu8Eb9j4ecspDSqrte4dm+wPCTGuU88EuEBMpSzbUe7Em/Mb0Md6haDLqPGIt+pXCoxJbiuw9972K5Lrh8xQkiHuCu3b8fzIbkOjDN1NNclHNph2C4kpgWgJuHT4cjMBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CMsyKdZ4=",
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
      "tx": "tx_+P4LAfiEuEArSUAKgqMh/HsLftJOwLAkTY0I7bUSDajEE8DG1t/uoIJsSqmaSi/FTu8Eb9j4ecspDSqrte4dm+wPCTGuU88EuEBMpSzbUe7Em/Mb0Md6haDLqPGIt+pXCoxJbiuw9972K5Lrh8xQkiHuCu3b8fzIbkOjDN1NNclHNph2C4kpgWgJuHT4cjMBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CMsyKdZ4=",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEArSUAKgqMh/HsLftJOwLAkTY0I7bUSDajEE8DG1t/uoIJsSqmaSi/FTu8Eb9j4ecspDSqrte4dm+wPCTGuU88EuEBMpSzbUe7Em/Mb0Md6haDLqPGIt+pXCoxJbiuw9972K5Lrh8xQkiHuCu3b8fzIbkOjDN1NNclHNph2C4kpgWgJuHT4cjMBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CMsyKdZ4=",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "state": "tx_+P4LAfiEuEArSUAKgqMh/HsLftJOwLAkTY0I7bUSDajEE8DG1t/uoIJsSqmaSi/FTu8Eb9j4ecspDSqrte4dm+wPCTGuU88EuEBMpSzbUe7Em/Mb0Md6haDLqPGIt+pXCoxJbiuw9972K5Lrh8xQkiHuCu3b8fzIbkOjDN1NNclHNph2C4kpgWgJuHT4cjMBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CMsyKdZ4="
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
      "state": "tx_+P4LAfiEuEArSUAKgqMh/HsLftJOwLAkTY0I7bUSDajEE8DG1t/uoIJsSqmaSi/FTu8Eb9j4ecspDSqrte4dm+wPCTGuU88EuEBMpSzbUe7Em/Mb0Md6haDLqPGIt+pXCoxJbiuw9972K5Lrh8xQkiHuCu3b8fzIbkOjDN1NNclHNph2C4kpgWgJuHT4cjMBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgDw79xIGMTuqSQnAexVYzr2YLA7Wnr7w5dIk/YkY8TY4CMsyKdZ4="
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
  "method": "channels.deposit",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBjkQAV3GxRR4BiusSvEAoR+N+0QpPoE+Ui4RUVILIeNHoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQIAhg/AoHKQAKBY8rhhwx3FNZzZtoqk4aiWG2eYbpEkfYl8gYb5T3SICgMTkCnY8w==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
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
  "id": -576460752303422839,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuECTFo9inBoBxHDOr7FnM+rDH3xLfifuVXbe1HdvpI8fXBjMUJffhIiE07D8MjgEkrEQ25+ZG6gwrIP3RluMIrEGuHT4cjMBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDE31h7NM="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
  "id": -576460752303422839,
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "signed_tx": "tx_+LwLAfhCuECTFo9inBoBxHDOr7FnM+rDH3xLfifuVXbe1HdvpI8fXBjMUJffhIiE07D8MjgEkrEQ25+ZG6gwrIP3RluMIrEGuHT4cjMBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDE31h7NM=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
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
  "id": -576460752303422838,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuECTFo9inBoBxHDOr7FnM+rDH3xLfifuVXbe1HdvpI8fXBjMUJffhIiE07D8MjgEkrEQ25+ZG6gwrIP3RluMIrEGuEDtmMDpexszmRtHo+RG+3PkkZLzea0RNhKuutNtSL2h1SwQHucxXQfT3X0hjlknwSZH9I7R+wPwlq1/uDVInQgNuHT4cjMBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDE8kWc10="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
  "id": -576460752303422838,
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
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuECTFo9inBoBxHDOr7FnM+rDH3xLfifuVXbe1HdvpI8fXBjMUJffhIiE07D8MjgEkrEQ25+ZG6gwrIP3RluMIrEGuEDtmMDpexszmRtHo+RG+3PkkZLzea0RNhKuutNtSL2h1SwQHucxXQfT3X0hjlknwSZH9I7R+wPwlq1/uDVInQgNuHT4cjMBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDE8kWc10=",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuECTFo9inBoBxHDOr7FnM+rDH3xLfifuVXbe1HdvpI8fXBjMUJffhIiE07D8MjgEkrEQ25+ZG6gwrIP3RluMIrEGuEDtmMDpexszmRtHo+RG+3PkkZLzea0RNhKuutNtSL2h1SwQHucxXQfT3X0hjlknwSZH9I7R+wPwlq1/uDVInQgNuHT4cjMBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDE8kWc10=",
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
      "tx": "tx_+P4LAfiEuECTFo9inBoBxHDOr7FnM+rDH3xLfifuVXbe1HdvpI8fXBjMUJffhIiE07D8MjgEkrEQ25+ZG6gwrIP3RluMIrEGuEDtmMDpexszmRtHo+RG+3PkkZLzea0RNhKuutNtSL2h1SwQHucxXQfT3X0hjlknwSZH9I7R+wPwlq1/uDVInQgNuHT4cjMBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDE8kWc10=",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECTFo9inBoBxHDOr7FnM+rDH3xLfifuVXbe1HdvpI8fXBjMUJffhIiE07D8MjgEkrEQ25+ZG6gwrIP3RluMIrEGuEDtmMDpexszmRtHo+RG+3PkkZLzea0RNhKuutNtSL2h1SwQHucxXQfT3X0hjlknwSZH9I7R+wPwlq1/uDVInQgNuHT4cjMBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDE8kWc10=",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
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
    "channel_id": "ch_S8axer1izndZW5nt5Qi7e8gZsjDFi13S64RZkWSFzHYmUi3PJ",
    "data": {
      "state": "tx_+P4LAfiEuECTFo9inBoBxHDOr7FnM+rDH3xLfifuVXbe1HdvpI8fXBjMUJffhIiE07D8MjgEkrEQ25+ZG6gwrIP3RluMIrEGuEDtmMDpexszmRtHo+RG+3PkkZLzea0RNhKuutNtSL2h1SwQHucxXQfT3X0hjlknwSZH9I7R+wPwlq1/uDVInQgNuHT4cjMBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDE8kWc10="
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
      "state": "tx_+P4LAfiEuECTFo9inBoBxHDOr7FnM+rDH3xLfifuVXbe1HdvpI8fXBjMUJffhIiE07D8MjgEkrEQ25+ZG6gwrIP3RluMIrEGuEDtmMDpexszmRtHo+RG+3PkkZLzea0RNhKuutNtSL2h1SwQHucxXQfT3X0hjlknwSZH9I7R+wPwlq1/uDVInQgNuHT4cjMBoQY5EAFdxsUUeAYrrErxAKEfjftEKT6BPlIuEVFSCyHjR6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgWPK4YcMdxTWc2baKpOGolhtnmG6RJH2JfIGG+U90iAoDE8kWc10="
    }
  },
  "version": 1
}
```
