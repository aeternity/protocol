
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
  "method": "channels.deposit",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBuErbkfh1o0Kle+dM27mB/wipGVUUudAVN7ro8unzZgRoQE/H7Rxh6+nH7Z27h93qd9pPi2ALqLdPk/Ymw/tfU+ucAIAhg/AoHKQAKAOSm8rqji2JZq9RZX5v5YpHm0qCc5hHsCB8mzKxMiWuwICUyRQmw==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
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
  "id": -576460752303423479,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEBT4q+Z8cWnbk0l1UDcY9ZOZKfxlXDMaDz4nOxNa5Cx4D3vif8+3ZO0jCjr0z6J1AR7TnAD+CT4Sp5ehoESuNcGuHT4cjMBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnACAIYPwKBykACgDkpvK6o4tiWavUWV+b+WKR5tKgnOYR7AgfJsysTIlrsCAkPDa0s="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
  "id": -576460752303423479,
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEBT4q+Z8cWnbk0l1UDcY9ZOZKfxlXDMaDz4nOxNa5Cx4D3vif8+3ZO0jCjr0z6J1AR7TnAD+CT4Sp5ehoESuNcGuHT4cjMBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnACAIYPwKBykACgDkpvK6o4tiWavUWV+b+WKR5tKgnOYR7AgfJsysTIlrsCAkPDa0s=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_UoR1YCEdi7nvn23NhnqzFNbVUdArJRh2qFCgpizjVXQcYmhrm",
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
  "id": -576460752303423478,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBT4q+Z8cWnbk0l1UDcY9ZOZKfxlXDMaDz4nOxNa5Cx4D3vif8+3ZO0jCjr0z6J1AR7TnAD+CT4Sp5ehoESuNcGuEDUCIGnlBKGvxrqdmiCEqo4/1pomIL7JDW1+PA9re/eONCvVbG7jAaoXZ3vnIHKeJoRF+P7sPsvFo9rJWxa0c4GuHT4cjMBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnACAIYPwKBykACgDkpvK6o4tiWavUWV+b+WKR5tKgnOYR7AgfJsysTIlrsCAryqKIg="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
  "id": -576460752303423478,
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
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEBT4q+Z8cWnbk0l1UDcY9ZOZKfxlXDMaDz4nOxNa5Cx4D3vif8+3ZO0jCjr0z6J1AR7TnAD+CT4Sp5ehoESuNcGuEDUCIGnlBKGvxrqdmiCEqo4/1pomIL7JDW1+PA9re/eONCvVbG7jAaoXZ3vnIHKeJoRF+P7sPsvFo9rJWxa0c4GuHT4cjMBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnACAIYPwKBykACgDkpvK6o4tiWavUWV+b+WKR5tKgnOYR7AgfJsysTIlrsCAryqKIg=",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEBT4q+Z8cWnbk0l1UDcY9ZOZKfxlXDMaDz4nOxNa5Cx4D3vif8+3ZO0jCjr0z6J1AR7TnAD+CT4Sp5ehoESuNcGuEDUCIGnlBKGvxrqdmiCEqo4/1pomIL7JDW1+PA9re/eONCvVbG7jAaoXZ3vnIHKeJoRF+P7sPsvFo9rJWxa0c4GuHT4cjMBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnACAIYPwKBykACgDkpvK6o4tiWavUWV+b+WKR5tKgnOYR7AgfJsysTIlrsCAryqKIg=",
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
      "tx": "tx_+P4LAfiEuEBT4q+Z8cWnbk0l1UDcY9ZOZKfxlXDMaDz4nOxNa5Cx4D3vif8+3ZO0jCjr0z6J1AR7TnAD+CT4Sp5ehoESuNcGuEDUCIGnlBKGvxrqdmiCEqo4/1pomIL7JDW1+PA9re/eONCvVbG7jAaoXZ3vnIHKeJoRF+P7sPsvFo9rJWxa0c4GuHT4cjMBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnACAIYPwKBykACgDkpvK6o4tiWavUWV+b+WKR5tKgnOYR7AgfJsysTIlrsCAryqKIg=",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBT4q+Z8cWnbk0l1UDcY9ZOZKfxlXDMaDz4nOxNa5Cx4D3vif8+3ZO0jCjr0z6J1AR7TnAD+CT4Sp5ehoESuNcGuEDUCIGnlBKGvxrqdmiCEqo4/1pomIL7JDW1+PA9re/eONCvVbG7jAaoXZ3vnIHKeJoRF+P7sPsvFo9rJWxa0c4GuHT4cjMBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnACAIYPwKBykACgDkpvK6o4tiWavUWV+b+WKR5tKgnOYR7AgfJsysTIlrsCAryqKIg=",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "state": "tx_+P4LAfiEuEBT4q+Z8cWnbk0l1UDcY9ZOZKfxlXDMaDz4nOxNa5Cx4D3vif8+3ZO0jCjr0z6J1AR7TnAD+CT4Sp5ehoESuNcGuEDUCIGnlBKGvxrqdmiCEqo4/1pomIL7JDW1+PA9re/eONCvVbG7jAaoXZ3vnIHKeJoRF+P7sPsvFo9rJWxa0c4GuHT4cjMBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnACAIYPwKBykACgDkpvK6o4tiWavUWV+b+WKR5tKgnOYR7AgfJsysTIlrsCAryqKIg="
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
      "state": "tx_+P4LAfiEuEBT4q+Z8cWnbk0l1UDcY9ZOZKfxlXDMaDz4nOxNa5Cx4D3vif8+3ZO0jCjr0z6J1AR7TnAD+CT4Sp5ehoESuNcGuEDUCIGnlBKGvxrqdmiCEqo4/1pomIL7JDW1+PA9re/eONCvVbG7jAaoXZ3vnIHKeJoRF+P7sPsvFo9rJWxa0c4GuHT4cjMBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBPx+0cYevpx+2du4fd6nfaT4tgC6i3T5P2JsP7X1PrnACAIYPwKBykACgDkpvK6o4tiWavUWV+b+WKR5tKgnOYR7AgfJsysTIlrsCAryqKIg="
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
  "method": "channels.deposit",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBuErbkfh1o0Kle+dM27mB/wipGVUUudAVN7ro8unzZgRoQExK0VDo5Q/UYJkHoy3JWbCKjbQh/WQ3ZUA4PmvJ7tfxwIAhg/AoHKQAKBY6vY07oNquboEjG/uLVNKqdCoFtQXwUBh2SqUph8hEwMBD1nM0g==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc",
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
  "id": -576460752303423477,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEBBm+CG1DPoqQBx56YRmDBDUhHyTG3a1yPIAbxPhH/W2Po0/4pjOKfq9QRpGmhf/lEvVOzcVqKmwhQp+JZ/wPcDuHT4cjMBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBMStFQ6OUP1GCZB6MtyVmwio20If1kN2VAOD5rye7X8cCAIYPwKBykACgWOr2NO6Darm6BIxv7i1TSqnQqBbUF8FAYdkqlKYfIRMDAdvPjkk="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
  "id": -576460752303423477,
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEBBm+CG1DPoqQBx56YRmDBDUhHyTG3a1yPIAbxPhH/W2Po0/4pjOKfq9QRpGmhf/lEvVOzcVqKmwhQp+JZ/wPcDuHT4cjMBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBMStFQ6OUP1GCZB6MtyVmwio20If1kN2VAOD5rye7X8cCAIYPwKBykACgWOr2NO6Darm6BIxv7i1TSqnQqBbUF8FAYdkqlKYfIRMDAdvPjkk=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_NexVZwWbxFovveSeQcfsuBEHgEuBAskimEQNjT78BV5c7ZmTc",
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
  "id": -576460752303423476,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEAKk/oXZyukDDbOUk+hTbgKfI+HHRpucD+jTtv8K+kaYBYbls+Cn2UaeO4KuDawBFJ8rAa3yU5QSKYsFsrDRdgBuEBBm+CG1DPoqQBx56YRmDBDUhHyTG3a1yPIAbxPhH/W2Po0/4pjOKfq9QRpGmhf/lEvVOzcVqKmwhQp+JZ/wPcDuHT4cjMBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBMStFQ6OUP1GCZB6MtyVmwio20If1kN2VAOD5rye7X8cCAIYPwKBykACgWOr2NO6Darm6BIxv7i1TSqnQqBbUF8FAYdkqlKYfIRMDAQkIqKc="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
  "id": -576460752303423476,
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
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEAKk/oXZyukDDbOUk+hTbgKfI+HHRpucD+jTtv8K+kaYBYbls+Cn2UaeO4KuDawBFJ8rAa3yU5QSKYsFsrDRdgBuEBBm+CG1DPoqQBx56YRmDBDUhHyTG3a1yPIAbxPhH/W2Po0/4pjOKfq9QRpGmhf/lEvVOzcVqKmwhQp+JZ/wPcDuHT4cjMBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBMStFQ6OUP1GCZB6MtyVmwio20If1kN2VAOD5rye7X8cCAIYPwKBykACgWOr2NO6Darm6BIxv7i1TSqnQqBbUF8FAYdkqlKYfIRMDAQkIqKc=",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEAKk/oXZyukDDbOUk+hTbgKfI+HHRpucD+jTtv8K+kaYBYbls+Cn2UaeO4KuDawBFJ8rAa3yU5QSKYsFsrDRdgBuEBBm+CG1DPoqQBx56YRmDBDUhHyTG3a1yPIAbxPhH/W2Po0/4pjOKfq9QRpGmhf/lEvVOzcVqKmwhQp+JZ/wPcDuHT4cjMBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBMStFQ6OUP1GCZB6MtyVmwio20If1kN2VAOD5rye7X8cCAIYPwKBykACgWOr2NO6Darm6BIxv7i1TSqnQqBbUF8FAYdkqlKYfIRMDAQkIqKc=",
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
      "tx": "tx_+P4LAfiEuEAKk/oXZyukDDbOUk+hTbgKfI+HHRpucD+jTtv8K+kaYBYbls+Cn2UaeO4KuDawBFJ8rAa3yU5QSKYsFsrDRdgBuEBBm+CG1DPoqQBx56YRmDBDUhHyTG3a1yPIAbxPhH/W2Po0/4pjOKfq9QRpGmhf/lEvVOzcVqKmwhQp+JZ/wPcDuHT4cjMBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBMStFQ6OUP1GCZB6MtyVmwio20If1kN2VAOD5rye7X8cCAIYPwKBykACgWOr2NO6Darm6BIxv7i1TSqnQqBbUF8FAYdkqlKYfIRMDAQkIqKc=",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAKk/oXZyukDDbOUk+hTbgKfI+HHRpucD+jTtv8K+kaYBYbls+Cn2UaeO4KuDawBFJ8rAa3yU5QSKYsFsrDRdgBuEBBm+CG1DPoqQBx56YRmDBDUhHyTG3a1yPIAbxPhH/W2Po0/4pjOKfq9QRpGmhf/lEvVOzcVqKmwhQp+JZ/wPcDuHT4cjMBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBMStFQ6OUP1GCZB6MtyVmwio20If1kN2VAOD5rye7X8cCAIYPwKBykACgWOr2NO6Darm6BIxv7i1TSqnQqBbUF8FAYdkqlKYfIRMDAQkIqKc=",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
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
    "channel_id": "ch_2iAf5bSGD3QEJXSwg5mGE6ghVvn99vjs6AuX8TxhXcQt2U4c4V",
    "data": {
      "state": "tx_+P4LAfiEuEAKk/oXZyukDDbOUk+hTbgKfI+HHRpucD+jTtv8K+kaYBYbls+Cn2UaeO4KuDawBFJ8rAa3yU5QSKYsFsrDRdgBuEBBm+CG1DPoqQBx56YRmDBDUhHyTG3a1yPIAbxPhH/W2Po0/4pjOKfq9QRpGmhf/lEvVOzcVqKmwhQp+JZ/wPcDuHT4cjMBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBMStFQ6OUP1GCZB6MtyVmwio20If1kN2VAOD5rye7X8cCAIYPwKBykACgWOr2NO6Darm6BIxv7i1TSqnQqBbUF8FAYdkqlKYfIRMDAQkIqKc="
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
      "state": "tx_+P4LAfiEuEAKk/oXZyukDDbOUk+hTbgKfI+HHRpucD+jTtv8K+kaYBYbls+Cn2UaeO4KuDawBFJ8rAa3yU5QSKYsFsrDRdgBuEBBm+CG1DPoqQBx56YRmDBDUhHyTG3a1yPIAbxPhH/W2Po0/4pjOKfq9QRpGmhf/lEvVOzcVqKmwhQp+JZ/wPcDuHT4cjMBoQbhK25H4daNCpXvnTNu5gf8IqRlVFLnQFTe66PLp82YEaEBMStFQ6OUP1GCZB6MtyVmwio20If1kN2VAOD5rye7X8cCAIYPwKBykACgWOr2NO6Darm6BIxv7i1TSqnQqBbUF8FAYdkqlKYfIRMDAQkIqKc="
    }
  },
  "version": 1
}
```
