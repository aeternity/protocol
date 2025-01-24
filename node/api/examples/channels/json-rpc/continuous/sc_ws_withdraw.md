
#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello",
    "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "message": {
        "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
        "from": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
        "info": "Hello",
        "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
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
    "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "message": {
        "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
        "from": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc",
        "info": "Hello back",
        "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
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
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "message": {
        "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
        "from": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
        "info": "Hello",
        "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
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
    "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "message": {
        "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
        "from": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc",
        "info": "Hello back",
        "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBuErbkfh1o0Kle+dM27mB/wipGVUUudAVN7ro8unzZgRoQE/H7Rxh6+nH7Z27h93qd9pPi2ALqLdPk/Ymw/tfU+ucAIAhg/AoHKQAKDFTbkRQpHlN7r9H2rQTDU8FYOVFe0uFueCBGGCA21z3wQDy4Jj4g==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
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
  "id": -576460752303423475,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEAjql0JaRplOz7LA6mTGqD9nDg5pvZzk6TI+hAiXN62a4sN1BeYT/7csD86rHs8XnndAuRyIDwu3Ul8W5WOT0EPuHT4cjQBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnACAIYPwKBykACgxU25EUKR5Te6/R9q0Ew1PBWDlRXtLhbnggRhggNtc98EAyFmgZA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
  "id": -576460752303423475,
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEAjql0JaRplOz7LA6mTGqD9nDg5pvZzk6TI+hAiXN62a4sN1BeYT/7csD86rHs8XnndAuRyIDwu3Ul8W5WOT0EPuHT4cjQBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnACAIYPwKBykACgxU25EUKR5Te6/R9q0Ew1PBWDlRXtLhbnggRhggNtc98EAyFmgZA=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
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
  "id": -576460752303423474,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEAjql0JaRplOz7LA6mTGqD9nDg5pvZzk6TI+hAiXN62a4sN1BeYT/7csD86rHs8XnndAuRyIDwu3Ul8W5WOT0EPuEB60D6mXZ+VR3PD+q27FsrQIuMZ2+aG/lJw3QfNDVRhnVlQPzEjXvwwbGq9oR5ya2DUmiXWWL7hFV0rFMKKfPQNuHT4cjQBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnACAIYPwKBykACgxU25EUKR5Te6/R9q0Ew1PBWDlRXtLhbnggRhggNtc98EA/zF0yc="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
  "id": -576460752303423474,
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEAjql0JaRplOz7LA6mTGqD9nDg5pvZzk6TI+hAiXN62a4sN1BeYT/7csD86rHs8XnndAuRyIDwu3Ul8W5WOT0EPuEB60D6mXZ+VR3PD+q27FsrQIuMZ2+aG/lJw3QfNDVRhnVlQPzEjXvwwbGq9oR5ya2DUmiXWWL7hFV0rFMKKfPQNuHT4cjQBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnACAIYPwKBykACgxU25EUKR5Te6/R9q0Ew1PBWDlRXtLhbnggRhggNtc98EA/zF0yc=",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEAjql0JaRplOz7LA6mTGqD9nDg5pvZzk6TI+hAiXN62a4sN1BeYT/7csD86rHs8XnndAuRyIDwu3Ul8W5WOT0EPuEB60D6mXZ+VR3PD+q27FsrQIuMZ2+aG/lJw3QfNDVRhnVlQPzEjXvwwbGq9oR5ya2DUmiXWWL7hFV0rFMKKfPQNuHT4cjQBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnACAIYPwKBykACgxU25EUKR5Te6/R9q0Ew1PBWDlRXtLhbnggRhggNtc98EA/zF0yc=",
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
    "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "message": {
        "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
        "from": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
        "info": "Hello",
        "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
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
    "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "message": {
        "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
        "from": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc",
        "info": "Hello back",
        "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAjql0JaRplOz7LA6mTGqD9nDg5pvZzk6TI+hAiXN62a4sN1BeYT/7csD86rHs8XnndAuRyIDwu3Ul8W5WOT0EPuEB60D6mXZ+VR3PD+q27FsrQIuMZ2+aG/lJw3QfNDVRhnVlQPzEjXvwwbGq9oR5ya2DUmiXWWL7hFV0rFMKKfPQNuHT4cjQBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnACAIYPwKBykACgxU25EUKR5Te6/R9q0Ew1PBWDlRXtLhbnggRhggNtc98EA/zF0yc=",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAjql0JaRplOz7LA6mTGqD9nDg5pvZzk6TI+hAiXN62a4sN1BeYT/7csD86rHs8XnndAuRyIDwu3Ul8W5WOT0EPuEB60D6mXZ+VR3PD+q27FsrQIuMZ2+aG/lJw3QfNDVRhnVlQPzEjXvwwbGq9oR5ya2DUmiXWWL7hFV0rFMKKfPQNuHT4cjQBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnACAIYPwKBykACgxU25EUKR5Te6/R9q0Ew1PBWDlRXtLhbnggRhggNtc98EA/zF0yc=",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "state": "tx_+P4LAfiEuEAjql0JaRplOz7LA6mTGqD9nDg5pvZzk6TI+hAiXN62a4sN1BeYT/7csD86rHs8XnndAuRyIDwu3Ul8W5WOT0EPuEB60D6mXZ+VR3PD+q27FsrQIuMZ2+aG/lJw3QfNDVRhnVlQPzEjXvwwbGq9oR5ya2DUmiXWWL7hFV0rFMKKfPQNuHT4cjQBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnACAIYPwKBykACgxU25EUKR5Te6/R9q0Ew1PBWDlRXtLhbnggRhggNtc98EA/zF0yc="
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "state": "tx_+P4LAfiEuEAjql0JaRplOz7LA6mTGqD9nDg5pvZzk6TI+hAiXN62a4sN1BeYT/7csD86rHs8XnndAuRyIDwu3Ul8W5WOT0EPuEB60D6mXZ+VR3PD+q27FsrQIuMZ2+aG/lJw3QfNDVRhnVlQPzEjXvwwbGq9oR5ya2DUmiXWWL7hFV0rFMKKfPQNuHT4cjQBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnACAIYPwKBykACgxU25EUKR5Te6/R9q0Ew1PBWDlRXtLhbnggRhggNtc98EA/zF0yc="
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
    "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "message": {
        "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
        "from": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc",
        "info": "Hello",
        "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
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
    "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "message": {
        "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
        "from": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
        "info": "Hello back",
        "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
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
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "message": {
        "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
        "from": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc",
        "info": "Hello",
        "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
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
    "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "message": {
        "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
        "from": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
        "info": "Hello back",
        "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBuErbkfh1o0Kle+dM27mB/wipGVUUudAVN7ro8unzZgRoQExK0VDo5Q/UYJkHoy3JWbCKjbQh/WQ3ZUA4PmvJ7tfxwIAhg/AoHKQAKDFsF/tzdjxpwe83ZR3KHsUPMx5Hh1XOukqQSgjGxC93QUCweyKtA==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
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
  "id": -576460752303423473,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEDOtSzFO5Yg//oyRNw7GuPgEdJsGwEPmZbRNEI0igcIei4eY+8+Leuh3jjhmvGXVFoZjv/ZeamZQosmtu3oJuEGuHT4cjQBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBMStFQ6OUP1GCZB6MtyVmwio20If1kN2VAOD5rye7X8cCAIYPwKBykACgxbBf7c3Y8acHvN2Udyh7FDzMeR4dVzrpKkEoIxsQvd0FAkV/1DY="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
  "id": -576460752303423473,
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEDOtSzFO5Yg//oyRNw7GuPgEdJsGwEPmZbRNEI0igcIei4eY+8+Leuh3jjhmvGXVFoZjv/ZeamZQosmtu3oJuEGuHT4cjQBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBMStFQ6OUP1GCZB6MtyVmwio20If1kN2VAOD5rye7X8cCAIYPwKBykACgxbBf7c3Y8acHvN2Udyh7FDzMeR4dVzrpKkEoIxsQvd0FAkV/1DY=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
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
  "id": -576460752303423472,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEA8r3mNIYVw10ujFjWYOkvxZTDchXoB982WQ1bN/Yb1CnvHmmyNciGgP+KtV7lGgloPJUy8i2oyT+bzSGIKHbEEuEDOtSzFO5Yg//oyRNw7GuPgEdJsGwEPmZbRNEI0igcIei4eY+8+Leuh3jjhmvGXVFoZjv/ZeamZQosmtu3oJuEGuHT4cjQBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBMStFQ6OUP1GCZB6MtyVmwio20If1kN2VAOD5rye7X8cCAIYPwKBykACgxbBf7c3Y8acHvN2Udyh7FDzMeR4dVzrpKkEoIxsQvd0FAr7ZAqQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
  "id": -576460752303423472,
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEA8r3mNIYVw10ujFjWYOkvxZTDchXoB982WQ1bN/Yb1CnvHmmyNciGgP+KtV7lGgloPJUy8i2oyT+bzSGIKHbEEuEDOtSzFO5Yg//oyRNw7GuPgEdJsGwEPmZbRNEI0igcIei4eY+8+Leuh3jjhmvGXVFoZjv/ZeamZQosmtu3oJuEGuHT4cjQBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBMStFQ6OUP1GCZB6MtyVmwio20If1kN2VAOD5rye7X8cCAIYPwKBykACgxbBf7c3Y8acHvN2Udyh7FDzMeR4dVzrpKkEoIxsQvd0FAr7ZAqQ=",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEA8r3mNIYVw10ujFjWYOkvxZTDchXoB982WQ1bN/Yb1CnvHmmyNciGgP+KtV7lGgloPJUy8i2oyT+bzSGIKHbEEuEDOtSzFO5Yg//oyRNw7GuPgEdJsGwEPmZbRNEI0igcIei4eY+8+Leuh3jjhmvGXVFoZjv/ZeamZQosmtu3oJuEGuHT4cjQBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBMStFQ6OUP1GCZB6MtyVmwio20If1kN2VAOD5rye7X8cCAIYPwKBykACgxbBf7c3Y8acHvN2Udyh7FDzMeR4dVzrpKkEoIxsQvd0FAr7ZAqQ=",
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
    "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "message": {
        "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
        "from": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc",
        "info": "Hello",
        "to": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm"
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
    "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "message": {
        "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
        "from": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
        "info": "Hello back",
        "to": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc"
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEA8r3mNIYVw10ujFjWYOkvxZTDchXoB982WQ1bN/Yb1CnvHmmyNciGgP+KtV7lGgloPJUy8i2oyT+bzSGIKHbEEuEDOtSzFO5Yg//oyRNw7GuPgEdJsGwEPmZbRNEI0igcIei4eY+8+Leuh3jjhmvGXVFoZjv/ZeamZQosmtu3oJuEGuHT4cjQBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBMStFQ6OUP1GCZB6MtyVmwio20If1kN2VAOD5rye7X8cCAIYPwKBykACgxbBf7c3Y8acHvN2Udyh7FDzMeR4dVzrpKkEoIxsQvd0FAr7ZAqQ=",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEA8r3mNIYVw10ujFjWYOkvxZTDchXoB982WQ1bN/Yb1CnvHmmyNciGgP+KtV7lGgloPJUy8i2oyT+bzSGIKHbEEuEDOtSzFO5Yg//oyRNw7GuPgEdJsGwEPmZbRNEI0igcIei4eY+8+Leuh3jjhmvGXVFoZjv/ZeamZQosmtu3oJuEGuHT4cjQBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBMStFQ6OUP1GCZB6MtyVmwio20If1kN2VAOD5rye7X8cCAIYPwKBykACgxbBf7c3Y8acHvN2Udyh7FDzMeR4dVzrpKkEoIxsQvd0FAr7ZAqQ=",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "state": "tx_+P4LAfiEuEA8r3mNIYVw10ujFjWYOkvxZTDchXoB982WQ1bN/Yb1CnvHmmyNciGgP+KtV7lGgloPJUy8i2oyT+bzSGIKHbEEuEDOtSzFO5Yg//oyRNw7GuPgEdJsGwEPmZbRNEI0igcIei4eY+8+Leuh3jjhmvGXVFoZjv/ZeamZQosmtu3oJuEGuHT4cjQBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBMStFQ6OUP1GCZB6MtyVmwio20If1kN2VAOD5rye7X8cCAIYPwKBykACgxbBf7c3Y8acHvN2Udyh7FDzMeR4dVzrpKkEoIxsQvd0FAr7ZAqQ="
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "state": "tx_+P4LAfiEuEA8r3mNIYVw10ujFjWYOkvxZTDchXoB982WQ1bN/Yb1CnvHmmyNciGgP+KtV7lGgloPJUy8i2oyT+bzSGIKHbEEuEDOtSzFO5Yg//oyRNw7GuPgEdJsGwEPmZbRNEI0igcIei4eY+8+Leuh3jjhmvGXVFoZjv/ZeamZQosmtu3oJuEGuHT4cjQBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBMStFQ6OUP1GCZB6MtyVmwio20If1kN2VAOD5rye7X8cCAIYPwKBykACgxbBf7c3Y8acHvN2Udyh7FDzMeR4dVzrpKkEoIxsQvd0FAr7ZAqQ="
    }
  },
  "version": 1
}
```
