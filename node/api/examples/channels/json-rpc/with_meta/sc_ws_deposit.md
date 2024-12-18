
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "message": {
        "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "message": {
        "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "message": {
        "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "message": {
        "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBpDUBO+a/RgR6K6WW8RXHQ34o4ijMezrRfbiY/TlTFODoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQIAhg/AoHKQAKArXHuXK6fNxw0V+DvBbsEO3zYWHaXsbcS/iCDCBbOzAQc1wJei+A==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
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
    "signed_tx": "tx_+LwLAfhCuECJOABQfaRUnnvcqjLrxCqceYrlNUUBLrKG6IUxRvfSyqOUl0AAVb0NysjDXDq6id2Rso85ULOG3yn1iAGIilgBuHT4cjMBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgK1x7lyunzccNFfg7wW7BDt82Fh2l7G3Ev4ggwgWzswEHNfpkYqM="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "signed_tx": "tx_+LwLAfhCuECJOABQfaRUnnvcqjLrxCqceYrlNUUBLrKG6IUxRvfSyqOUl0AAVb0NysjDXDq6id2Rso85ULOG3yn1iAGIilgBuHT4cjMBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgK1x7lyunzccNFfg7wW7BDt82Fh2l7G3Ev4ggwgWzswEHNfpkYqM=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
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
    "signed_tx": "tx_+P4LAfiEuEBnqi9qmHPS4kidLOMOX/8cgnxPs6lsH5EtdgniV2BnE76vawIUW2c572SkHqgoKHmtxJ049m9gsO3BYm+AdIkKuECJOABQfaRUnnvcqjLrxCqceYrlNUUBLrKG6IUxRvfSyqOUl0AAVb0NysjDXDq6id2Rso85ULOG3yn1iAGIilgBuHT4cjMBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgK1x7lyunzccNFfg7wW7BDt82Fh2l7G3Ev4ggwgWzswEHNVNDGoE="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEBnqi9qmHPS4kidLOMOX/8cgnxPs6lsH5EtdgniV2BnE76vawIUW2c572SkHqgoKHmtxJ049m9gsO3BYm+AdIkKuECJOABQfaRUnnvcqjLrxCqceYrlNUUBLrKG6IUxRvfSyqOUl0AAVb0NysjDXDq6id2Rso85ULOG3yn1iAGIilgBuHT4cjMBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgK1x7lyunzccNFfg7wW7BDt82Fh2l7G3Ev4ggwgWzswEHNVNDGoE=",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEBnqi9qmHPS4kidLOMOX/8cgnxPs6lsH5EtdgniV2BnE76vawIUW2c572SkHqgoKHmtxJ049m9gsO3BYm+AdIkKuECJOABQfaRUnnvcqjLrxCqceYrlNUUBLrKG6IUxRvfSyqOUl0AAVb0NysjDXDq6id2Rso85ULOG3yn1iAGIilgBuHT4cjMBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgK1x7lyunzccNFfg7wW7BDt82Fh2l7G3Ev4ggwgWzswEHNVNDGoE=",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "message": {
        "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "message": {
        "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBnqi9qmHPS4kidLOMOX/8cgnxPs6lsH5EtdgniV2BnE76vawIUW2c572SkHqgoKHmtxJ049m9gsO3BYm+AdIkKuECJOABQfaRUnnvcqjLrxCqceYrlNUUBLrKG6IUxRvfSyqOUl0AAVb0NysjDXDq6id2Rso85ULOG3yn1iAGIilgBuHT4cjMBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgK1x7lyunzccNFfg7wW7BDt82Fh2l7G3Ev4ggwgWzswEHNVNDGoE=",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBnqi9qmHPS4kidLOMOX/8cgnxPs6lsH5EtdgniV2BnE76vawIUW2c572SkHqgoKHmtxJ049m9gsO3BYm+AdIkKuECJOABQfaRUnnvcqjLrxCqceYrlNUUBLrKG6IUxRvfSyqOUl0AAVb0NysjDXDq6id2Rso85ULOG3yn1iAGIilgBuHT4cjMBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgK1x7lyunzccNFfg7wW7BDt82Fh2l7G3Ev4ggwgWzswEHNVNDGoE=",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "state": "tx_+P4LAfiEuEBnqi9qmHPS4kidLOMOX/8cgnxPs6lsH5EtdgniV2BnE76vawIUW2c572SkHqgoKHmtxJ049m9gsO3BYm+AdIkKuECJOABQfaRUnnvcqjLrxCqceYrlNUUBLrKG6IUxRvfSyqOUl0AAVb0NysjDXDq6id2Rso85ULOG3yn1iAGIilgBuHT4cjMBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgK1x7lyunzccNFfg7wW7BDt82Fh2l7G3Ev4ggwgWzswEHNVNDGoE="
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "state": "tx_+P4LAfiEuEBnqi9qmHPS4kidLOMOX/8cgnxPs6lsH5EtdgniV2BnE76vawIUW2c572SkHqgoKHmtxJ049m9gsO3BYm+AdIkKuECJOABQfaRUnnvcqjLrxCqceYrlNUUBLrKG6IUxRvfSyqOUl0AAVb0NysjDXDq6id2Rso85ULOG3yn1iAGIilgBuHT4cjMBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACgK1x7lyunzccNFfg7wW7BDt82Fh2l7G3Ev4ggwgWzswEHNVNDGoE="
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "message": {
        "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "message": {
        "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "message": {
        "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "message": {
        "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBpDUBO+a/RgR6K6WW8RXHQ34o4ijMezrRfbiY/TlTFODoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQIAhg/AoHKQAKDAgOmfzLTUKbEHjC3ytU2aauA8hBPCgkqSqca5IuDd0wgVn+WzZA==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
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
    "signed_tx": "tx_+LwLAfhCuECF7PIi1BXjh4PhYcLuOBw95FXmYoxNGc5mRwusVSWSdI4ealSxGKWsH6L4EdqwPVlUjaJ2FgkRpjRpJOqckU0GuHT4cjMBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgwIDpn8y01CmxB4wt8rVNmmrgPIQTwoJKkqnGuSLg3dMIFa8RxZM="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "signed_tx": "tx_+LwLAfhCuECF7PIi1BXjh4PhYcLuOBw95FXmYoxNGc5mRwusVSWSdI4ealSxGKWsH6L4EdqwPVlUjaJ2FgkRpjRpJOqckU0GuHT4cjMBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgwIDpn8y01CmxB4wt8rVNmmrgPIQTwoJKkqnGuSLg3dMIFa8RxZM=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
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
    "signed_tx": "tx_+P4LAfiEuEBy4V0B6cf2G3GQ3mmSN/+yAl5vD6q7wIv4npgHV+h4gYiobtoUG77hpl/wQ9qIrLWBnSdgGrbmK0TWhQbJWJUGuECF7PIi1BXjh4PhYcLuOBw95FXmYoxNGc5mRwusVSWSdI4ealSxGKWsH6L4EdqwPVlUjaJ2FgkRpjRpJOqckU0GuHT4cjMBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgwIDpn8y01CmxB4wt8rVNmmrgPIQTwoJKkqnGuSLg3dMIFbjsPWA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEBy4V0B6cf2G3GQ3mmSN/+yAl5vD6q7wIv4npgHV+h4gYiobtoUG77hpl/wQ9qIrLWBnSdgGrbmK0TWhQbJWJUGuECF7PIi1BXjh4PhYcLuOBw95FXmYoxNGc5mRwusVSWSdI4ealSxGKWsH6L4EdqwPVlUjaJ2FgkRpjRpJOqckU0GuHT4cjMBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgwIDpn8y01CmxB4wt8rVNmmrgPIQTwoJKkqnGuSLg3dMIFbjsPWA=",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEBy4V0B6cf2G3GQ3mmSN/+yAl5vD6q7wIv4npgHV+h4gYiobtoUG77hpl/wQ9qIrLWBnSdgGrbmK0TWhQbJWJUGuECF7PIi1BXjh4PhYcLuOBw95FXmYoxNGc5mRwusVSWSdI4ealSxGKWsH6L4EdqwPVlUjaJ2FgkRpjRpJOqckU0GuHT4cjMBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgwIDpn8y01CmxB4wt8rVNmmrgPIQTwoJKkqnGuSLg3dMIFbjsPWA=",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "message": {
        "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "message": {
        "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBy4V0B6cf2G3GQ3mmSN/+yAl5vD6q7wIv4npgHV+h4gYiobtoUG77hpl/wQ9qIrLWBnSdgGrbmK0TWhQbJWJUGuECF7PIi1BXjh4PhYcLuOBw95FXmYoxNGc5mRwusVSWSdI4ealSxGKWsH6L4EdqwPVlUjaJ2FgkRpjRpJOqckU0GuHT4cjMBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgwIDpn8y01CmxB4wt8rVNmmrgPIQTwoJKkqnGuSLg3dMIFbjsPWA=",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBy4V0B6cf2G3GQ3mmSN/+yAl5vD6q7wIv4npgHV+h4gYiobtoUG77hpl/wQ9qIrLWBnSdgGrbmK0TWhQbJWJUGuECF7PIi1BXjh4PhYcLuOBw95FXmYoxNGc5mRwusVSWSdI4ealSxGKWsH6L4EdqwPVlUjaJ2FgkRpjRpJOqckU0GuHT4cjMBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgwIDpn8y01CmxB4wt8rVNmmrgPIQTwoJKkqnGuSLg3dMIFbjsPWA=",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "state": "tx_+P4LAfiEuEBy4V0B6cf2G3GQ3mmSN/+yAl5vD6q7wIv4npgHV+h4gYiobtoUG77hpl/wQ9qIrLWBnSdgGrbmK0TWhQbJWJUGuECF7PIi1BXjh4PhYcLuOBw95FXmYoxNGc5mRwusVSWSdI4ealSxGKWsH6L4EdqwPVlUjaJ2FgkRpjRpJOqckU0GuHT4cjMBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgwIDpn8y01CmxB4wt8rVNmmrgPIQTwoJKkqnGuSLg3dMIFbjsPWA="
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "state": "tx_+P4LAfiEuEBy4V0B6cf2G3GQ3mmSN/+yAl5vD6q7wIv4npgHV+h4gYiobtoUG77hpl/wQ9qIrLWBnSdgGrbmK0TWhQbJWJUGuECF7PIi1BXjh4PhYcLuOBw95FXmYoxNGc5mRwusVSWSdI4ealSxGKWsH6L4EdqwPVlUjaJ2FgkRpjRpJOqckU0GuHT4cjMBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACgwIDpn8y01CmxB4wt8rVNmmrgPIQTwoJKkqnGuSLg3dMIFbjsPWA="
    }
  },
  "version": 1
}
```
