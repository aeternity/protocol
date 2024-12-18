
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
  "method": "channels.withdraw",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBpDUBO+a/RgR6K6WW8RXHQ34o4ijMezrRfbiY/TlTFODoQFkrg4IYt7TSzp77iFZuRSGwvSJKHZNvxOAiompi5WvgQIAhg/AoHKQAKCWhsjpbZHG8XnUbdvab6gh4mhTL80UmhkKQ2AJ5YTL/wk2XdNS0Q==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
    "signed_tx": "tx_+LwLAfhCuECw7fr3fxa99Bj3LwefHu2Y201J+fSEiy5Gr7RhZm/I0EsTGDXMlOhn1lfZtpPeZKUP7PMuEVNHPV4Qi/OYJdcKuHT4cjQBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACglobI6W2RxvF51G3b2m+oIeJoUy/NFJoZCkNgCeWEy/8JNkFbCjg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "signed_tx": "tx_+LwLAfhCuECw7fr3fxa99Bj3LwefHu2Y201J+fSEiy5Gr7RhZm/I0EsTGDXMlOhn1lfZtpPeZKUP7PMuEVNHPV4Qi/OYJdcKuHT4cjQBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACglobI6W2RxvF51G3b2m+oIeJoUy/NFJoZCkNgCeWEy/8JNkFbCjg=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
    "signed_tx": "tx_+P4LAfiEuEAOX8aOcx9KpwV18HAZNrsTHjwc4+jurSRTKtuP8zG9LetT7tW1b8m+7LyUtiUPm4G59G13R9sxQyIPBKsCCzIPuECw7fr3fxa99Bj3LwefHu2Y201J+fSEiy5Gr7RhZm/I0EsTGDXMlOhn1lfZtpPeZKUP7PMuEVNHPV4Qi/OYJdcKuHT4cjQBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACglobI6W2RxvF51G3b2m+oIeJoUy/NFJoZCkNgCeWEy/8JNhlaCmk="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEAOX8aOcx9KpwV18HAZNrsTHjwc4+jurSRTKtuP8zG9LetT7tW1b8m+7LyUtiUPm4G59G13R9sxQyIPBKsCCzIPuECw7fr3fxa99Bj3LwefHu2Y201J+fSEiy5Gr7RhZm/I0EsTGDXMlOhn1lfZtpPeZKUP7PMuEVNHPV4Qi/OYJdcKuHT4cjQBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACglobI6W2RxvF51G3b2m+oIeJoUy/NFJoZCkNgCeWEy/8JNhlaCmk=",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEAOX8aOcx9KpwV18HAZNrsTHjwc4+jurSRTKtuP8zG9LetT7tW1b8m+7LyUtiUPm4G59G13R9sxQyIPBKsCCzIPuECw7fr3fxa99Bj3LwefHu2Y201J+fSEiy5Gr7RhZm/I0EsTGDXMlOhn1lfZtpPeZKUP7PMuEVNHPV4Qi/OYJdcKuHT4cjQBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACglobI6W2RxvF51G3b2m+oIeJoUy/NFJoZCkNgCeWEy/8JNhlaCmk=",
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
      "tx": "tx_+P4LAfiEuEAOX8aOcx9KpwV18HAZNrsTHjwc4+jurSRTKtuP8zG9LetT7tW1b8m+7LyUtiUPm4G59G13R9sxQyIPBKsCCzIPuECw7fr3fxa99Bj3LwefHu2Y201J+fSEiy5Gr7RhZm/I0EsTGDXMlOhn1lfZtpPeZKUP7PMuEVNHPV4Qi/OYJdcKuHT4cjQBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACglobI6W2RxvF51G3b2m+oIeJoUy/NFJoZCkNgCeWEy/8JNhlaCmk=",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAOX8aOcx9KpwV18HAZNrsTHjwc4+jurSRTKtuP8zG9LetT7tW1b8m+7LyUtiUPm4G59G13R9sxQyIPBKsCCzIPuECw7fr3fxa99Bj3LwefHu2Y201J+fSEiy5Gr7RhZm/I0EsTGDXMlOhn1lfZtpPeZKUP7PMuEVNHPV4Qi/OYJdcKuHT4cjQBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACglobI6W2RxvF51G3b2m+oIeJoUy/NFJoZCkNgCeWEy/8JNhlaCmk=",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "state": "tx_+P4LAfiEuEAOX8aOcx9KpwV18HAZNrsTHjwc4+jurSRTKtuP8zG9LetT7tW1b8m+7LyUtiUPm4G59G13R9sxQyIPBKsCCzIPuECw7fr3fxa99Bj3LwefHu2Y201J+fSEiy5Gr7RhZm/I0EsTGDXMlOhn1lfZtpPeZKUP7PMuEVNHPV4Qi/OYJdcKuHT4cjQBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACglobI6W2RxvF51G3b2m+oIeJoUy/NFJoZCkNgCeWEy/8JNhlaCmk="
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
      "state": "tx_+P4LAfiEuEAOX8aOcx9KpwV18HAZNrsTHjwc4+jurSRTKtuP8zG9LetT7tW1b8m+7LyUtiUPm4G59G13R9sxQyIPBKsCCzIPuECw7fr3fxa99Bj3LwefHu2Y201J+fSEiy5Gr7RhZm/I0EsTGDXMlOhn1lfZtpPeZKUP7PMuEVNHPV4Qi/OYJdcKuHT4cjQBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBZK4OCGLe00s6e+4hWbkUhsL0iSh2Tb8TgIqJqYuVr4ECAIYPwKBykACglobI6W2RxvF51G3b2m+oIeJoUy/NFJoZCkNgCeWEy/8JNhlaCmk="
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
  "method": "channels.withdraw",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBpDUBO+a/RgR6K6WW8RXHQ34o4ijMezrRfbiY/TlTFODoQGQsy4wyp2ngByD9p0uw1DZWKZADIqFC92lFO6uDCpwoQIAhg/AoHKQAKDdqOzEXWz8Y2itvyrEosD88v7VNFxfGdbGSLDDea6BYAoW1Z5BZQ==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
    "signed_tx": "tx_+LwLAfhCuEB+fAzXrZHzGMCsg0Bdp30400Zmyq3VzG036QFkE+QntlIFZwfXTlC9ufISn70Kgrk87TKjsQXIWjDh430frUELuHT4cjQBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAKFiUA97s="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEB+fAzXrZHzGMCsg0Bdp30400Zmyq3VzG036QFkE+QntlIFZwfXTlC9ufISn70Kgrk87TKjsQXIWjDh430frUELuHT4cjQBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAKFiUA97s=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
    "signed_tx": "tx_+P4LAfiEuEB+fAzXrZHzGMCsg0Bdp30400Zmyq3VzG036QFkE+QntlIFZwfXTlC9ufISn70Kgrk87TKjsQXIWjDh430frUELuEDb9dQhxnOUyzhISA2IOFTxh4pb4AcdWnd1ak3aKGFKIbjfC4xHzli3yUEFp1SfRg+9ULHnPYxskk4AH7J7njMMuHT4cjQBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAKFjy9REU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEB+fAzXrZHzGMCsg0Bdp30400Zmyq3VzG036QFkE+QntlIFZwfXTlC9ufISn70Kgrk87TKjsQXIWjDh430frUELuEDb9dQhxnOUyzhISA2IOFTxh4pb4AcdWnd1ak3aKGFKIbjfC4xHzli3yUEFp1SfRg+9ULHnPYxskk4AH7J7njMMuHT4cjQBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAKFjy9REU=",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEB+fAzXrZHzGMCsg0Bdp30400Zmyq3VzG036QFkE+QntlIFZwfXTlC9ufISn70Kgrk87TKjsQXIWjDh430frUELuEDb9dQhxnOUyzhISA2IOFTxh4pb4AcdWnd1ak3aKGFKIbjfC4xHzli3yUEFp1SfRg+9ULHnPYxskk4AH7J7njMMuHT4cjQBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAKFjy9REU=",
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
      "tx": "tx_+P4LAfiEuEB+fAzXrZHzGMCsg0Bdp30400Zmyq3VzG036QFkE+QntlIFZwfXTlC9ufISn70Kgrk87TKjsQXIWjDh430frUELuEDb9dQhxnOUyzhISA2IOFTxh4pb4AcdWnd1ak3aKGFKIbjfC4xHzli3yUEFp1SfRg+9ULHnPYxskk4AH7J7njMMuHT4cjQBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAKFjy9REU=",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEB+fAzXrZHzGMCsg0Bdp30400Zmyq3VzG036QFkE+QntlIFZwfXTlC9ufISn70Kgrk87TKjsQXIWjDh430frUELuEDb9dQhxnOUyzhISA2IOFTxh4pb4AcdWnd1ak3aKGFKIbjfC4xHzli3yUEFp1SfRg+9ULHnPYxskk4AH7J7njMMuHT4cjQBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAKFjy9REU=",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
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
    "channel_id": "ch_26nSdswHFxLJvkpi3MG72AcqwJjMsgh5eHn5iHn4TuzviB1DMb",
    "data": {
      "state": "tx_+P4LAfiEuEB+fAzXrZHzGMCsg0Bdp30400Zmyq3VzG036QFkE+QntlIFZwfXTlC9ufISn70Kgrk87TKjsQXIWjDh430frUELuEDb9dQhxnOUyzhISA2IOFTxh4pb4AcdWnd1ak3aKGFKIbjfC4xHzli3yUEFp1SfRg+9ULHnPYxskk4AH7J7njMMuHT4cjQBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAKFjy9REU="
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
      "state": "tx_+P4LAfiEuEB+fAzXrZHzGMCsg0Bdp30400Zmyq3VzG036QFkE+QntlIFZwfXTlC9ufISn70Kgrk87TKjsQXIWjDh430frUELuEDb9dQhxnOUyzhISA2IOFTxh4pb4AcdWnd1ak3aKGFKIbjfC4xHzli3yUEFp1SfRg+9ULHnPYxskk4AH7J7njMMuHT4cjQBoQaQ1ATvmv0YEeiullvEVx0N+KOIozHs60X24mP05UxTg6EBkLMuMMqdp4Acg/adLsNQ2VimQAyKhQvdpRTurgwqcKECAIYPwKBykACg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWAKFjy9REU="
    }
  },
  "version": 1
}
```
