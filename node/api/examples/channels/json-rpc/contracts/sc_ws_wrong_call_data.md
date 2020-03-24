
#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 3,
    "call_data": "cb_KxG4F37sGwIZEGMb",
    "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
    "deposit": 10,
    "vm_version": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1007,
        "message": "Contract init failed"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxG4F37sGwIZEGMb",
        "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
        "deposit": 10,
        "vm_version": 7
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
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 3,
    "call_data": "cb_KxG4F37sGwIZEGMb",
    "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
    "deposit": 10,
    "vm_version": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1007,
        "message": "Contract init failed"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxG4F37sGwIZEGMb",
        "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
        "deposit": 10,
        "vm_version": 7
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
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 3,
    "call_data": "cb_KxG4F37sGwIZEGMb",
    "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
    "deposit": 10,
    "vm_version": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1007,
        "message": "Contract init failed"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxG4F37sGwIZEGMb",
        "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
        "deposit": 10,
        "vm_version": 7
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
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 3,
    "call_data": "cb_KxG4F37sGwIZEGMb",
    "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
    "deposit": 10,
    "vm_version": 7
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1007,
        "message": "Contract init failed"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxG4F37sGwIZEGMb",
        "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
        "deposit": 10,
        "vm_version": 7
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
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 3,
    "call_data": "cb_KxFE1kQfP4oEp9E=",
    "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
    "deposit": 10,
    "vm_version": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEsoBtKaseUX3SIsopvva0tPQ9P2xg9YSBCeHEaSHZWxaT2rQGbkA==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "vm_version": 7
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
  "id": -576460752303421267,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEAnSaX62kU3CUb5I5swB7pvKKJWb0HhFrKfxO1+F9imw5+zLe2J7ob6JpphKh4XhMOSaScTE0eSxPwJgNoOorgIuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBLKAbSmrHlF90iLKKb72tLT0PT9sYPWEgQnhxGkh2VsWk9iKsb1w="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421267,
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JILAfhCuEAnSaX62kU3CUb5I5swB7pvKKJWb0HhFrKfxO1+F9imw5+zLe2J7ob6JpphKh4XhMOSaScTE0eSxPwJgNoOorgIuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBLKAbSmrHlF90iLKKb72tLT0PT9sYPWEgQnhxGkh2VsWk9iKsb1w=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "vm_version": 7
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
  "id": -576460752303421266,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEAnSaX62kU3CUb5I5swB7pvKKJWb0HhFrKfxO1+F9imw5+zLe2J7ob6JpphKh4XhMOSaScTE0eSxPwJgNoOorgIuECWoqY1sfmHorpVpx9rUzPzLwTLeIz40gGl5yMWcezv1jWDCJk0g9bymJcQCu2gAQUPPeeu6CQZVyS7CV4ZKMcNuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBLKAbSmrHlF90iLKKb72tLT0PT9sYPWEgQnhxGkh2VsWk9jZfdF0="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421266,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEAnSaX62kU3CUb5I5swB7pvKKJWb0HhFrKfxO1+F9imw5+zLe2J7ob6JpphKh4XhMOSaScTE0eSxPwJgNoOorgIuECWoqY1sfmHorpVpx9rUzPzLwTLeIz40gGl5yMWcezv1jWDCJk0g9bymJcQCu2gAQUPPeeu6CQZVyS7CV4ZKMcNuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBLKAbSmrHlF90iLKKb72tLT0PT9sYPWEgQnhxGkh2VsWk9jZfdF0="
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEAnSaX62kU3CUb5I5swB7pvKKJWb0HhFrKfxO1+F9imw5+zLe2J7ob6JpphKh4XhMOSaScTE0eSxPwJgNoOorgIuECWoqY1sfmHorpVpx9rUzPzLwTLeIz40gGl5yMWcezv1jWDCJk0g9bymJcQCu2gAQUPPeeu6CQZVyS7CV4ZKMcNuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBLKAbSmrHlF90iLKKb72tLT0PT9sYPWEgQnhxGkh2VsWk9jZfdF0="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 1,
    "call_data": "cb_KxFLBQ6pKwIEOyoYQQ==",
    "contract_id": "ct_2BB53ALak22dWL7fXPrc5ihqK6eUpVrGLA8mU8RicJRcrZTUK5"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEtoI0jpo2IIAOybHqhHsRpKDfHGhEhymoe4elPazbA/3u/RInKdw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 1,
          "call_data": "cb_KxFLBQ6pKwIEOyoYQQ==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2BB53ALak22dWL7fXPrc5ihqK6eUpVrGLA8mU8RicJRcrZTUK5",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421265,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEBj8qQeXhItuXBK/5llR/44u4cqH6GEdmIkgvrgJEs0jobc/aRYBApd3OCzfv704ZRbrSJjMdm3bseXQ1TrwZoKuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBLaCNI6aNiCADsmx6oR7EaSg3xxoRIcpqHuHpT2s2wP97v4xe+1c="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421265,
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JILAfhCuEBj8qQeXhItuXBK/5llR/44u4cqH6GEdmIkgvrgJEs0jobc/aRYBApd3OCzfv704ZRbrSJjMdm3bseXQ1TrwZoKuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBLaCNI6aNiCADsmx6oR7EaSg3xxoRIcpqHuHpT2s2wP97v4xe+1c=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 1,
          "call_data": "cb_KxFLBQ6pKwIEOyoYQQ==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2BB53ALak22dWL7fXPrc5ihqK6eUpVrGLA8mU8RicJRcrZTUK5",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421264,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEBj8qQeXhItuXBK/5llR/44u4cqH6GEdmIkgvrgJEs0jobc/aRYBApd3OCzfv704ZRbrSJjMdm3bseXQ1TrwZoKuEBkDsz/q9X/JBhff4ylyVbTfqmdASSJFNQKeRIGRYdv2qjLR+Z/I9yKxzWH8pPSN69GE7iFZCj4E7nzCvhpNpAJuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBLaCNI6aNiCADsmx6oR7EaSg3xxoRIcpqHuHpT2s2wP97vwzpdjE="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421264,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEBj8qQeXhItuXBK/5llR/44u4cqH6GEdmIkgvrgJEs0jobc/aRYBApd3OCzfv704ZRbrSJjMdm3bseXQ1TrwZoKuEBkDsz/q9X/JBhff4ylyVbTfqmdASSJFNQKeRIGRYdv2qjLR+Z/I9yKxzWH8pPSN69GE7iFZCj4E7nzCvhpNpAJuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBLaCNI6aNiCADsmx6oR7EaSg3xxoRIcpqHuHpT2s2wP97vwzpdjE="
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEBj8qQeXhItuXBK/5llR/44u4cqH6GEdmIkgvrgJEs0jobc/aRYBApd3OCzfv704ZRbrSJjMdm3bseXQ1TrwZoKuEBkDsz/q9X/JBhff4ylyVbTfqmdASSJFNQKeRIGRYdv2qjLR+Z/I9yKxzWH8pPSN69GE7iFZCj4E7nzCvhpNpAJuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBLaCNI6aNiCADsmx6oR7EaSg3xxoRIcpqHuHpT2s2wP97vwzpdjE="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2BB53ALak22dWL7fXPrc5ihqK6eUpVrGLA8mU8RicJRcrZTUK5",
    "round": 301
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 301,
      "contract_id": "ct_2BB53ALak22dWL7fXPrc5ihqK6eUpVrGLA8mU8RicJRcrZTUK5",
      "gas_price": 1,
      "gas_used": 1000000,
      "height": 301,
      "log": [],
      "return_type": "error",
      "return_value": "cb_VHJ5aW5nIHRvIGNhbGwgdW5kZWZpbmVkIGZ1bmN0aW9uOiA8PDc1LDUsMTQsMTY5Pj7zlATR"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 3,
    "call_data": "cb_KxFE1kQfP4oEp9E=",
    "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
    "deposit": 10,
    "vm_version": 7
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEuoANB/e7WTIhLc3shiXx0LpqQaHUq5u/4qMM5gp8iDp4L4I2ZBw==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "vm_version": 7
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
  "id": -576460752303421263,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEBMANXz0hmWuuK97HTgkS9l2hW+oUh9q6k7Zo5f/glkWgh8q7vdNypA+6H9Ns4z7QZGP7pPcvGSkUZCf5iRlS4LuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBLqADQf3u1kyIS3N7IYl8dC6akGh1Kubv+KjDOYKfIg6eC0Z+aHI="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421263,
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JILAfhCuEBMANXz0hmWuuK97HTgkS9l2hW+oUh9q6k7Zo5f/glkWgh8q7vdNypA+6H9Ns4z7QZGP7pPcvGSkUZCf5iRlS4LuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBLqADQf3u1kyIS3N7IYl8dC6akGh1Kubv+KjDOYKfIg6eC0Z+aHI=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "vm_version": 7
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
  "id": -576460752303421262,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEAd3UHAuQWVhwuFA3yCPJezRRrBWqQcIst7bSTfkrNgtZlAMYCP/B3aPOapQIK6ppSQse9BeN9OjxFxWJk116AGuEBMANXz0hmWuuK97HTgkS9l2hW+oUh9q6k7Zo5f/glkWgh8q7vdNypA+6H9Ns4z7QZGP7pPcvGSkUZCf5iRlS4LuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBLqADQf3u1kyIS3N7IYl8dC6akGh1Kubv+KjDOYKfIg6eC801JfA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421262,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEAd3UHAuQWVhwuFA3yCPJezRRrBWqQcIst7bSTfkrNgtZlAMYCP/B3aPOapQIK6ppSQse9BeN9OjxFxWJk116AGuEBMANXz0hmWuuK97HTgkS9l2hW+oUh9q6k7Zo5f/glkWgh8q7vdNypA+6H9Ns4z7QZGP7pPcvGSkUZCf5iRlS4LuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBLqADQf3u1kyIS3N7IYl8dC6akGh1Kubv+KjDOYKfIg6eC801JfA="
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEAd3UHAuQWVhwuFA3yCPJezRRrBWqQcIst7bSTfkrNgtZlAMYCP/B3aPOapQIK6ppSQse9BeN9OjxFxWJk116AGuEBMANXz0hmWuuK97HTgkS9l2hW+oUh9q6k7Zo5f/glkWgh8q7vdNypA+6H9Ns4z7QZGP7pPcvGSkUZCf5iRlS4LuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBLqADQf3u1kyIS3N7IYl8dC6akGh1Kubv+KjDOYKfIg6eC801JfA="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 1,
    "call_data": "cb_KxFLBQ6pKwIEOyoYQQ==",
    "contract_id": "ct_jfsQ66NTUgWc3Jr5fT2KJKRVJCFD2AmEhrhQ6jW6UEZJbrUDK"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEvoFfibaBZC6YD42z5J4juNHSlKY/rWTZRqvSnllrxIQQ86vIdcg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 1,
          "call_data": "cb_KxFLBQ6pKwIEOyoYQQ==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_jfsQ66NTUgWc3Jr5fT2KJKRVJCFD2AmEhrhQ6jW6UEZJbrUDK",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421261,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuECJvGrIODlmlQ0UBCE9Md3hJ9X2HXR1JBbz6x1hn6ldhLXM2XbGCGq3+M+VVrdSteXt1+vqotByGwrfZm+bLCcKuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBL6BX4m2gWQumA+Ns+SeI7jR0pSmP61k2Uar0p5Za8SEEPB/8tQI="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421261,
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JILAfhCuECJvGrIODlmlQ0UBCE9Md3hJ9X2HXR1JBbz6x1hn6ldhLXM2XbGCGq3+M+VVrdSteXt1+vqotByGwrfZm+bLCcKuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBL6BX4m2gWQumA+Ns+SeI7jR0pSmP61k2Uar0p5Za8SEEPB/8tQI=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 1,
          "call_data": "cb_KxFLBQ6pKwIEOyoYQQ==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_jfsQ66NTUgWc3Jr5fT2KJKRVJCFD2AmEhrhQ6jW6UEZJbrUDK",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421260,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuECJvGrIODlmlQ0UBCE9Md3hJ9X2HXR1JBbz6x1hn6ldhLXM2XbGCGq3+M+VVrdSteXt1+vqotByGwrfZm+bLCcKuED3IS9ZCLJymT5Xk8UjDvZzoDyKH1XOyWVWDu5MduFOdQF4QZAus1bWBXgiR989M0ri3+E9+VfZaLN+J+1LfSYBuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBL6BX4m2gWQumA+Ns+SeI7jR0pSmP61k2Uar0p5Za8SEEPC+lCZ0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421260,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuECJvGrIODlmlQ0UBCE9Md3hJ9X2HXR1JBbz6x1hn6ldhLXM2XbGCGq3+M+VVrdSteXt1+vqotByGwrfZm+bLCcKuED3IS9ZCLJymT5Xk8UjDvZzoDyKH1XOyWVWDu5MduFOdQF4QZAus1bWBXgiR989M0ri3+E9+VfZaLN+J+1LfSYBuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBL6BX4m2gWQumA+Ns+SeI7jR0pSmP61k2Uar0p5Za8SEEPC+lCZ0="
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuECJvGrIODlmlQ0UBCE9Md3hJ9X2HXR1JBbz6x1hn6ldhLXM2XbGCGq3+M+VVrdSteXt1+vqotByGwrfZm+bLCcKuED3IS9ZCLJymT5Xk8UjDvZzoDyKH1XOyWVWDu5MduFOdQF4QZAus1bWBXgiR989M0ri3+E9+VfZaLN+J+1LfSYBuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBL6BX4m2gWQumA+Ns+SeI7jR0pSmP61k2Uar0p5Za8SEEPC+lCZ0="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_jfsQ66NTUgWc3Jr5fT2KJKRVJCFD2AmEhrhQ6jW6UEZJbrUDK",
    "round": 303
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 303,
      "contract_id": "ct_jfsQ66NTUgWc3Jr5fT2KJKRVJCFD2AmEhrhQ6jW6UEZJbrUDK",
      "gas_price": 1,
      "gas_used": 1000000,
      "height": 303,
      "log": [],
      "return_type": "error",
      "return_value": "cb_VHJ5aW5nIHRvIGNhbGwgdW5kZWZpbmVkIGZ1bmN0aW9uOiA8PDc1LDUsMTQsMTY5Pj7zlATR"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 3,
    "call_data": "cb_KxFE1kQfP4oEp9E=",
    "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
    "deposit": 10,
    "vm_version": 7
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEwoIh+B9Q7SzojqjyS3LdB3Qm5rt4ZUokfm0j5nwCPB0xBNdEbYA==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "vm_version": 7
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
  "id": -576460752303421259,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEDxulbaUc0uKH2zH1qYC3gbWPCv7vezRzgy+fwB/xj6H3wC/puJJ4sPR1QmsvgykKJ32rldFq6lGuEuuySuZKgMuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBMKCIfgfUO0s6I6o8kty3Qd0Jua7eGVKJH5tI+Z8AjwdMQXpuWaM="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421259,
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JILAfhCuEDxulbaUc0uKH2zH1qYC3gbWPCv7vezRzgy+fwB/xj6H3wC/puJJ4sPR1QmsvgykKJ32rldFq6lGuEuuySuZKgMuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBMKCIfgfUO0s6I6o8kty3Qd0Jua7eGVKJH5tI+Z8AjwdMQXpuWaM=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "vm_version": 7
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
  "id": -576460752303421258,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEBZywvcuATdyJsHqFb+JJSUhqzTSUUlWa5X1POVZvNA3WZnwnPwvwVQ1anF2DapQr6Y9/krP/EelC+aMrHgqL4LuEDxulbaUc0uKH2zH1qYC3gbWPCv7vezRzgy+fwB/xj6H3wC/puJJ4sPR1QmsvgykKJ32rldFq6lGuEuuySuZKgMuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBMKCIfgfUO0s6I6o8kty3Qd0Jua7eGVKJH5tI+Z8AjwdMQV3Nqmw="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421258,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEBZywvcuATdyJsHqFb+JJSUhqzTSUUlWa5X1POVZvNA3WZnwnPwvwVQ1anF2DapQr6Y9/krP/EelC+aMrHgqL4LuEDxulbaUc0uKH2zH1qYC3gbWPCv7vezRzgy+fwB/xj6H3wC/puJJ4sPR1QmsvgykKJ32rldFq6lGuEuuySuZKgMuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBMKCIfgfUO0s6I6o8kty3Qd0Jua7eGVKJH5tI+Z8AjwdMQV3Nqmw="
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEBZywvcuATdyJsHqFb+JJSUhqzTSUUlWa5X1POVZvNA3WZnwnPwvwVQ1anF2DapQr6Y9/krP/EelC+aMrHgqL4LuEDxulbaUc0uKH2zH1qYC3gbWPCv7vezRzgy+fwB/xj6H3wC/puJJ4sPR1QmsvgykKJ32rldFq6lGuEuuySuZKgMuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBMKCIfgfUO0s6I6o8kty3Qd0Jua7eGVKJH5tI+Z8AjwdMQV3Nqmw="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 1,
    "call_data": "cb_KxFLBQ6pKwIEOyoYQQ==",
    "contract_id": "ct_2fL4bSwG4NbEpeLP3AxasopLi7igQTUQS7bNXt7jyLsYVgb6GK"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggExoK9pxzzolTDOFdVcO25vQXc8tgtAuH+boQrdhC6A/KA+tLJdHQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 1,
          "call_data": "cb_KxFLBQ6pKwIEOyoYQQ==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2fL4bSwG4NbEpeLP3AxasopLi7igQTUQS7bNXt7jyLsYVgb6GK",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421257,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEBYuCXEebSPXcdZVjNr0Zf+JyonNrppteVr1AX76uas94Jp0HCGHoZN5vLj2aKFMc4UCaalehYg08Dg342a52MCuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBMaCvacc86JUwzhXVXDtub0F3PLYLQLh/m6EK3YQugPygPjbIsNk="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421257,
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JILAfhCuEBYuCXEebSPXcdZVjNr0Zf+JyonNrppteVr1AX76uas94Jp0HCGHoZN5vLj2aKFMc4UCaalehYg08Dg342a52MCuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBMaCvacc86JUwzhXVXDtub0F3PLYLQLh/m6EK3YQugPygPjbIsNk=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 1,
          "call_data": "cb_KxFLBQ6pKwIEOyoYQQ==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2fL4bSwG4NbEpeLP3AxasopLi7igQTUQS7bNXt7jyLsYVgb6GK",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421256,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEBYuCXEebSPXcdZVjNr0Zf+JyonNrppteVr1AX76uas94Jp0HCGHoZN5vLj2aKFMc4UCaalehYg08Dg342a52MCuEDGHkjLwM2X2J4PVIxj6Mt2MEzSyfEj5g4QGIxsHMUsVAbPJqiZ8YcYB/AgpsZL/8UxJKpHJfIxDgbW5UHr5koEuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBMaCvacc86JUwzhXVXDtub0F3PLYLQLh/m6EK3YQugPygPgqfs24="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421256,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEBYuCXEebSPXcdZVjNr0Zf+JyonNrppteVr1AX76uas94Jp0HCGHoZN5vLj2aKFMc4UCaalehYg08Dg342a52MCuEDGHkjLwM2X2J4PVIxj6Mt2MEzSyfEj5g4QGIxsHMUsVAbPJqiZ8YcYB/AgpsZL/8UxJKpHJfIxDgbW5UHr5koEuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBMaCvacc86JUwzhXVXDtub0F3PLYLQLh/m6EK3YQugPygPgqfs24="
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEBYuCXEebSPXcdZVjNr0Zf+JyonNrppteVr1AX76uas94Jp0HCGHoZN5vLj2aKFMc4UCaalehYg08Dg342a52MCuEDGHkjLwM2X2J4PVIxj6Mt2MEzSyfEj5g4QGIxsHMUsVAbPJqiZ8YcYB/AgpsZL/8UxJKpHJfIxDgbW5UHr5koEuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBMaCvacc86JUwzhXVXDtub0F3PLYLQLh/m6EK3YQugPygPgqfs24="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2fL4bSwG4NbEpeLP3AxasopLi7igQTUQS7bNXt7jyLsYVgb6GK",
    "round": 305
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 305,
      "contract_id": "ct_2fL4bSwG4NbEpeLP3AxasopLi7igQTUQS7bNXt7jyLsYVgb6GK",
      "gas_price": 1,
      "gas_used": 1000000,
      "height": 305,
      "log": [],
      "return_type": "error",
      "return_value": "cb_VHJ5aW5nIHRvIGNhbGwgdW5kZWZpbmVkIGZ1bmN0aW9uOiA8PDc1LDUsMTQsMTY5Pj7zlATR"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 3,
    "call_data": "cb_KxFE1kQfP4oEp9E=",
    "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
    "deposit": 10,
    "vm_version": 7
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEyoPHoDJ/RgBw7Ip4DlYomYlea1RY+AGBB6ucDXGxAEyR5LYgImQ==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "vm_version": 7
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
  "id": -576460752303421255,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEC+9j1WD7ZDPqXRHoZgPfqvuuhW4nK0hSISQNs+ljs3hIi59tCLKAYuLmZfy1zWy4vKsECGT7nQLL39kB/hxKwHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBMqDx6Ayf0YAcOyKeA5WKJmJXmtUWPgBgQernA1xsQBMkefVSIpg="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421255,
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JILAfhCuEC+9j1WD7ZDPqXRHoZgPfqvuuhW4nK0hSISQNs+ljs3hIi59tCLKAYuLmZfy1zWy4vKsECGT7nQLL39kB/hxKwHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBMqDx6Ayf0YAcOyKeA5WKJmJXmtUWPgBgQernA1xsQBMkefVSIpg=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "vm_version": 7
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
  "id": -576460752303421254,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEAQl0fMiqrDCpDSOxLuuk6QVAZyG1HdOS+2D9nGbqw43yl22uXg61Y4diPXz1pSr/tAH5yBuATfSLgVB6CQK6EGuEC+9j1WD7ZDPqXRHoZgPfqvuuhW4nK0hSISQNs+ljs3hIi59tCLKAYuLmZfy1zWy4vKsECGT7nQLL39kB/hxKwHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBMqDx6Ayf0YAcOyKeA5WKJmJXmtUWPgBgQernA1xsQBMkeVifZ64="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421254,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEAQl0fMiqrDCpDSOxLuuk6QVAZyG1HdOS+2D9nGbqw43yl22uXg61Y4diPXz1pSr/tAH5yBuATfSLgVB6CQK6EGuEC+9j1WD7ZDPqXRHoZgPfqvuuhW4nK0hSISQNs+ljs3hIi59tCLKAYuLmZfy1zWy4vKsECGT7nQLL39kB/hxKwHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBMqDx6Ayf0YAcOyKeA5WKJmJXmtUWPgBgQernA1xsQBMkeVifZ64="
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEAQl0fMiqrDCpDSOxLuuk6QVAZyG1HdOS+2D9nGbqw43yl22uXg61Y4diPXz1pSr/tAH5yBuATfSLgVB6CQK6EGuEC+9j1WD7ZDPqXRHoZgPfqvuuhW4nK0hSISQNs+ljs3hIi59tCLKAYuLmZfy1zWy4vKsECGT7nQLL39kB/hxKwHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBMqDx6Ayf0YAcOyKeA5WKJmJXmtUWPgBgQernA1xsQBMkeVifZ64="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 1,
    "call_data": "cb_KxFLBQ6pKwIEOyoYQQ==",
    "contract_id": "ct_2WAaaN6XYLwa2YMfB3giaRbcT1UYz3z9ZcxmFkZLAzsfSLMMWJ"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEzoNS7IE6Yrgtxr83M+xiG57x0Wdi+z7Zu2yHI5S/BL7tWx7TpjA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 1,
          "call_data": "cb_KxFLBQ6pKwIEOyoYQQ==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2WAaaN6XYLwa2YMfB3giaRbcT1UYz3z9ZcxmFkZLAzsfSLMMWJ",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421253,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEAA1O7wnBRsyZfQd80WBM3ll0m8/k8rwqLsn0g/9qVKxrHci0Yugf0jJEwUgKjAhbddoj1TKg1qmA3ZPlWP3t4AuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBM6DUuyBOmK4Lca/NzPsYhue8dFnYvs+2btshyOUvwS+7VqpCFP0="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421253,
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+JILAfhCuEAA1O7wnBRsyZfQd80WBM3ll0m8/k8rwqLsn0g/9qVKxrHci0Yugf0jJEwUgKjAhbddoj1TKg1qmA3ZPlWP3t4AuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBM6DUuyBOmK4Lca/NzPsYhue8dFnYvs+2btshyOUvwS+7VqpCFP0=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 1,
          "call_data": "cb_KxFLBQ6pKwIEOyoYQQ==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2WAaaN6XYLwa2YMfB3giaRbcT1UYz3z9ZcxmFkZLAzsfSLMMWJ",
          "gas": 1000000,
          "gas_price": 1,
          "op": "OffChainCallContract"
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
  "id": -576460752303421252,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEAA1O7wnBRsyZfQd80WBM3ll0m8/k8rwqLsn0g/9qVKxrHci0Yugf0jJEwUgKjAhbddoj1TKg1qmA3ZPlWP3t4AuEAVJHU+UBjOy2KI7YxNpx98Qrsx84Yv1lA07RTfu6+G+bWG5GTWUdeHmVuqugPqtF5yURBXDj2nU97vtV1oEHsOuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBM6DUuyBOmK4Lca/NzPsYhue8dFnYvs+2btshyOUvwS+7Vi6CEyU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421252,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEAA1O7wnBRsyZfQd80WBM3ll0m8/k8rwqLsn0g/9qVKxrHci0Yugf0jJEwUgKjAhbddoj1TKg1qmA3ZPlWP3t4AuEAVJHU+UBjOy2KI7YxNpx98Qrsx84Yv1lA07RTfu6+G+bWG5GTWUdeHmVuqugPqtF5yURBXDj2nU97vtV1oEHsOuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBM6DUuyBOmK4Lca/NzPsYhue8dFnYvs+2btshyOUvwS+7Vi6CEyU="
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEAA1O7wnBRsyZfQd80WBM3ll0m8/k8rwqLsn0g/9qVKxrHci0Yugf0jJEwUgKjAhbddoj1TKg1qmA3ZPlWP3t4AuEAVJHU+UBjOy2KI7YxNpx98Qrsx84Yv1lA07RTfu6+G+bWG5GTWUdeHmVuqugPqtF5yURBXDj2nU97vtV1oEHsOuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBM6DUuyBOmK4Lca/NzPsYhue8dFnYvs+2btshyOUvwS+7Vi6CEyU="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2WAaaN6XYLwa2YMfB3giaRbcT1UYz3z9ZcxmFkZLAzsfSLMMWJ",
    "round": 307
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.contract_call.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 307,
      "contract_id": "ct_2WAaaN6XYLwa2YMfB3giaRbcT1UYz3z9ZcxmFkZLAzsfSLMMWJ",
      "gas_price": 1,
      "gas_used": 1000000,
      "height": 307,
      "log": [],
      "return_type": "error",
      "return_value": "cb_VHJ5aW5nIHRvIGNhbGwgdW5kZWZpbmVkIGZ1bmN0aW9uOiA8PDc1LDUsMTQsMTY5Pj7zlATR"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421251,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421251,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421250,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421250,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
