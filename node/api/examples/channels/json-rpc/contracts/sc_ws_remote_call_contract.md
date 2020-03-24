
#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 3,
    "call_data": "cb_KxFE1kQfP4oEp9E=",
    "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
    "deposit": "1",
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfP4oEp9E=",
        "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
        "deposit": "1",
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
    "vm_version": "1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfP4oEp9E=",
        "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
        "deposit": 10,
        "vm_version": "1"
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
    "abi_version": "1",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": "1",
        "call_data": "cb_KxFE1kQfP4oEp9E=",
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgdSgo7UNsIPwrO6puiAgo+Vsg5ZXn8qrNg0ULJosqsReiNPGv80t",
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
  "id": -576460752303421443,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEANi9+ctYj5Z30VQ/eIsYOhPJ7NciORoUBEFacASt5O+k1DtOOHZB0GarqumtriTKb3JzNmf1RbOlTE9ytRk4UEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHUoKO1DbCD8KzuqbogIKPlbIOWV5/KqzYNFCyaLKrEXojT2ZG8hA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421443,
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
      "signed_tx": "tx_+JELAfhCuEANi9+ctYj5Z30VQ/eIsYOhPJ7NciORoUBEFacASt5O+k1DtOOHZB0GarqumtriTKb3JzNmf1RbOlTE9ytRk4UEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHUoKO1DbCD8KzuqbogIKPlbIOWV5/KqzYNFCyaLKrEXojT2ZG8hA==",
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
  "id": -576460752303421442,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEANi9+ctYj5Z30VQ/eIsYOhPJ7NciORoUBEFacASt5O+k1DtOOHZB0GarqumtriTKb3JzNmf1RbOlTE9ytRk4UEuEBxAh8UTeIIXJECcNQhD20m8OaP1gq58XVSO9Bcv+LqlbLzuOEG5r3Z/BmjgVumKgTVd9PgIuUvbapXOFgJAo8NuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHUoKO1DbCD8KzuqbogIKPlbIOWV5/KqzYNFCyaLKrEXojTP2tQHQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421442,
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
      "state": "tx_+NMLAfiEuEANi9+ctYj5Z30VQ/eIsYOhPJ7NciORoUBEFacASt5O+k1DtOOHZB0GarqumtriTKb3JzNmf1RbOlTE9ytRk4UEuEBxAh8UTeIIXJECcNQhD20m8OaP1gq58XVSO9Bcv+LqlbLzuOEG5r3Z/BmjgVumKgTVd9PgIuUvbapXOFgJAo8NuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHUoKO1DbCD8KzuqbogIKPlbIOWV5/KqzYNFCyaLKrEXojTP2tQHQ=="
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
      "state": "tx_+NMLAfiEuEANi9+ctYj5Z30VQ/eIsYOhPJ7NciORoUBEFacASt5O+k1DtOOHZB0GarqumtriTKb3JzNmf1RbOlTE9ytRk4UEuEBxAh8UTeIIXJECcNQhD20m8OaP1gq58XVSO9Bcv+LqlbLzuOEG5r3Z/BmjgVumKgTVd9PgIuUvbapXOFgJAo8NuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHUoKO1DbCD8KzuqbogIKPlbIOWV5/KqzYNFCyaLKrEXojTP2tQHQ=="
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
    "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
    "deposit": "1",
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfP4oEp9E=",
        "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
        "deposit": "1",
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
    "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
    "deposit": 10,
    "vm_version": "1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfP4oEp9E=",
        "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
        "deposit": 10,
        "vm_version": "1"
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
    "abi_version": "1",
    "call_data": "cb_KxFE1kQfP4oEp9E=",
    "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": "1",
        "call_data": "cb_KxFE1kQfP4oEp9E=",
        "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
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
    "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgdWgM9JTfk9o3pfcwoEsLe7nX1I+Y8bnmqJKb8cn6G3yJ140xe9s",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
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
  "id": -576460752303421441,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEBm9w2yauK4gncMUZrZrORyjvCSQbjM9fOLBVObeCaT3eN36iUUoN8VUclUCJcJU9uy9hVV8IfvU6SU6ZcEeV8LuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHVoDPSU35PaN6X3MKBLC3u519SPmPG55qiSm/HJ+ht8ideegJwrA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421441,
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
      "signed_tx": "tx_+JELAfhCuEBm9w2yauK4gncMUZrZrORyjvCSQbjM9fOLBVObeCaT3eN36iUUoN8VUclUCJcJU9uy9hVV8IfvU6SU6ZcEeV8LuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHVoDPSU35PaN6X3MKBLC3u519SPmPG55qiSm/HJ+ht8ideegJwrA==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
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
  "id": -576460752303421440,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAI0DEikJMkDsEv1yuDGwx6c4fwT/CcqIT1roGS+ZY4Z9XhFWGIZwNvBBow6c/RoYkMZ9HmHKnxzMwCAVPy5RIKuEBm9w2yauK4gncMUZrZrORyjvCSQbjM9fOLBVObeCaT3eN36iUUoN8VUclUCJcJU9uy9hVV8IfvU6SU6ZcEeV8LuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHVoDPSU35PaN6X3MKBLC3u519SPmPG55qiSm/HJ+ht8idePkmh4A=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421440,
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
      "state": "tx_+NMLAfiEuEAI0DEikJMkDsEv1yuDGwx6c4fwT/CcqIT1roGS+ZY4Z9XhFWGIZwNvBBow6c/RoYkMZ9HmHKnxzMwCAVPy5RIKuEBm9w2yauK4gncMUZrZrORyjvCSQbjM9fOLBVObeCaT3eN36iUUoN8VUclUCJcJU9uy9hVV8IfvU6SU6ZcEeV8LuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHVoDPSU35PaN6X3MKBLC3u519SPmPG55qiSm/HJ+ht8idePkmh4A=="
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
      "state": "tx_+NMLAfiEuEAI0DEikJMkDsEv1yuDGwx6c4fwT/CcqIT1roGS+ZY4Z9XhFWGIZwNvBBow6c/RoYkMZ9HmHKnxzMwCAVPy5RIKuEBm9w2yauK4gncMUZrZrORyjvCSQbjM9fOLBVObeCaT3eN36iUUoN8VUclUCJcJU9uy9hVV8IfvU6SU6ZcEeV8LuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHVoDPSU35PaN6X3MKBLC3u519SPmPG55qiSm/HJ+ht8idePkmh4A=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 214,
      "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
      "gas_price": 1,
      "gas_used": 11,
      "height": 214,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgdagLdtfeYaUkt9kX80tmyffjo32ULduy/Vxqa5QosSxvkYKhJD6",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
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
  "id": -576460752303421439,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEDj4yTJOFMQRnIfsoMIaMda8MoAMWyM9Mvp9BhXa+u3upxE+P0XPxSzrBOLvHL4bxzbxj5NI5B+8JTKHHnbaHAKuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHWoC3bX3mGlJLfZF/NLZsn346N9lC3bsv1camuUKLEsb5GxBgbMA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421439,
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
      "signed_tx": "tx_+JELAfhCuEDj4yTJOFMQRnIfsoMIaMda8MoAMWyM9Mvp9BhXa+u3upxE+P0XPxSzrBOLvHL4bxzbxj5NI5B+8JTKHHnbaHAKuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHWoC3bX3mGlJLfZF/NLZsn346N9lC3bsv1camuUKLEsb5GxBgbMA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
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
  "id": -576460752303421438,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEC0iblC/rpctdmckK9SNPMJkBdMxdVcmjVkT68S23QSIWBorg9Rh/4Yeu0yiF8rx7+qv43snVXjZj8uCK5QUnsPuEDj4yTJOFMQRnIfsoMIaMda8MoAMWyM9Mvp9BhXa+u3upxE+P0XPxSzrBOLvHL4bxzbxj5NI5B+8JTKHHnbaHAKuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHWoC3bX3mGlJLfZF/NLZsn346N9lC3bsv1camuUKLEsb5GmROXQA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421438,
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
      "state": "tx_+NMLAfiEuEC0iblC/rpctdmckK9SNPMJkBdMxdVcmjVkT68S23QSIWBorg9Rh/4Yeu0yiF8rx7+qv43snVXjZj8uCK5QUnsPuEDj4yTJOFMQRnIfsoMIaMda8MoAMWyM9Mvp9BhXa+u3upxE+P0XPxSzrBOLvHL4bxzbxj5NI5B+8JTKHHnbaHAKuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHWoC3bX3mGlJLfZF/NLZsn346N9lC3bsv1camuUKLEsb5GmROXQA=="
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
      "state": "tx_+NMLAfiEuEC0iblC/rpctdmckK9SNPMJkBdMxdVcmjVkT68S23QSIWBorg9Rh/4Yeu0yiF8rx7+qv43snVXjZj8uCK5QUnsPuEDj4yTJOFMQRnIfsoMIaMda8MoAMWyM9Mvp9BhXa+u3upxE+P0XPxSzrBOLvHL4bxzbxj5NI5B+8JTKHHnbaHAKuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHWoC3bX3mGlJLfZF/NLZsn346N9lC3bsv1camuUKLEsb5GmROXQA=="
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
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 214
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": 214
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 214
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 214
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 214
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
      "caller_nonce": 214,
      "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
      "gas_price": 1,
      "gas_used": 11,
      "height": 214,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 214
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": 214
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 214
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 214
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 214
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
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 214,
      "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
      "gas_price": 1,
      "gas_used": 11,
      "height": 214,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 215,
      "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
      "gas_price": 1,
      "gas_used": 11,
      "height": 215,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgdegfcYC9iSY52M6jZhFRuCKhp37ud6ODxB48LDo24i7hO8/N5SK",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
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
  "id": -576460752303421437,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuED1KEl9ldmuYmoZoWHjnxRgzXjZTZ1a8lW9o2MV4r6BVCujDTyjMgCQKth+jx6+W6FiovBK1xEgbD3D0Rs3DEAHuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHXoH3GAvYkmOdjOo2YRUbgioad+7nejg8QePCw6NuIu4Tvsxv+dQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421437,
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
      "signed_tx": "tx_+JELAfhCuED1KEl9ldmuYmoZoWHjnxRgzXjZTZ1a8lW9o2MV4r6BVCujDTyjMgCQKth+jx6+W6FiovBK1xEgbD3D0Rs3DEAHuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHXoH3GAvYkmOdjOo2YRUbgioad+7nejg8QePCw6NuIu4Tvsxv+dQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
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
  "id": -576460752303421436,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuECio7pZqusU7ukXKo2dVF7pfBww2UKRej8gafWJswkDsGvK1skRg+2HbqRYDIATIbBwqpUzR8ZzbfjzhwVnlk0JuED1KEl9ldmuYmoZoWHjnxRgzXjZTZ1a8lW9o2MV4r6BVCujDTyjMgCQKth+jx6+W6FiovBK1xEgbD3D0Rs3DEAHuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHXoH3GAvYkmOdjOo2YRUbgioad+7nejg8QePCw6NuIu4TvHIc8bg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421436,
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
      "state": "tx_+NMLAfiEuECio7pZqusU7ukXKo2dVF7pfBww2UKRej8gafWJswkDsGvK1skRg+2HbqRYDIATIbBwqpUzR8ZzbfjzhwVnlk0JuED1KEl9ldmuYmoZoWHjnxRgzXjZTZ1a8lW9o2MV4r6BVCujDTyjMgCQKth+jx6+W6FiovBK1xEgbD3D0Rs3DEAHuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHXoH3GAvYkmOdjOo2YRUbgioad+7nejg8QePCw6NuIu4TvHIc8bg=="
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
      "state": "tx_+NMLAfiEuECio7pZqusU7ukXKo2dVF7pfBww2UKRej8gafWJswkDsGvK1skRg+2HbqRYDIATIbBwqpUzR8ZzbfjzhwVnlk0JuED1KEl9ldmuYmoZoWHjnxRgzXjZTZ1a8lW9o2MV4r6BVCujDTyjMgCQKth+jx6+W6FiovBK1xEgbD3D0Rs3DEAHuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHXoH3GAvYkmOdjOo2YRUbgioad+7nejg8QePCw6NuIu4TvHIc8bg=="
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 215
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": 215
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 215
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 215
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 215
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
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 215,
      "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
      "gas_price": 1,
      "gas_used": 11,
      "height": 215,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
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
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 215
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": 215
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 215
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 215
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 215
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
      "caller_nonce": 215,
      "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
      "gas_price": 1,
      "gas_used": 11,
      "height": 215,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 216,
      "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
      "gas_price": 1,
      "gas_used": 11,
      "height": 216,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Rgdig1MZrWYDmpfXuhF0BTKHwjXAiXbUX8+H0le0zBEaM6SkXpl3v",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
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
  "id": -576460752303421435,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuED67wNbU2kpRGera/ddNQfEbgs3GcTQZgv8SkNqQK7qVSyPXewyhlo42KzJw317IsZBRmsfI++HKKNfloJPcdAOuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHYoNTGa1mA5qX17oRdAUyh8I1wIl21F/Ph9JXtMwRGjOkpwbfVLg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421435,
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
      "signed_tx": "tx_+JELAfhCuED67wNbU2kpRGera/ddNQfEbgs3GcTQZgv8SkNqQK7qVSyPXewyhlo42KzJw317IsZBRmsfI++HKKNfloJPcdAOuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHYoNTGa1mA5qX17oRdAUyh8I1wIl21F/Ph9JXtMwRGjOkpwbfVLg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
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
  "id": -576460752303421434,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEBPbRndXF3NxEC8qQbCpxWrHzixgtkdj80yRasVUKCD5t0TzqMiT0GwdpNXX7HA+x/cGeTCEhvU2ql82AjLHa0OuED67wNbU2kpRGera/ddNQfEbgs3GcTQZgv8SkNqQK7qVSyPXewyhlo42KzJw317IsZBRmsfI++HKKNfloJPcdAOuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHYoNTGa1mA5qX17oRdAUyh8I1wIl21F/Ph9JXtMwRGjOkp+0gshw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421434,
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
      "state": "tx_+NMLAfiEuEBPbRndXF3NxEC8qQbCpxWrHzixgtkdj80yRasVUKCD5t0TzqMiT0GwdpNXX7HA+x/cGeTCEhvU2ql82AjLHa0OuED67wNbU2kpRGera/ddNQfEbgs3GcTQZgv8SkNqQK7qVSyPXewyhlo42KzJw317IsZBRmsfI++HKKNfloJPcdAOuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHYoNTGa1mA5qX17oRdAUyh8I1wIl21F/Ph9JXtMwRGjOkp+0gshw=="
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
      "state": "tx_+NMLAfiEuEBPbRndXF3NxEC8qQbCpxWrHzixgtkdj80yRasVUKCD5t0TzqMiT0GwdpNXX7HA+x/cGeTCEhvU2ql82AjLHa0OuED67wNbU2kpRGera/ddNQfEbgs3GcTQZgv8SkNqQK7qVSyPXewyhlo42KzJw317IsZBRmsfI++HKKNfloJPcdAOuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHYoNTGa1mA5qX17oRdAUyh8I1wIl21F/Ph9JXtMwRGjOkp+0gshw=="
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
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 216
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": 216
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 216
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 216
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 216
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
      "caller_nonce": 216,
      "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
      "gas_price": 1,
      "gas_used": 11,
      "height": 216,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 216
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": 216
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 216
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 216
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 216
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
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 216,
      "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
      "gas_price": 1,
      "gas_used": 11,
      "height": 216,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 217,
      "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
      "gas_price": 1,
      "gas_used": 11,
      "height": 217,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Rgdmg8BpIjRP0eMGU4yD1Wf56UIgUgrlfwyDbNr4LRCsf83ZWNhws",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
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
  "id": -576460752303421433,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuECFcPOHykioIy1yisy6b10GBrWePmt1t4TvxfD6JCsTiQZLmPzUhUm+C+UPO8qynu9IDFlwn3PP1RmIT7HCXWcGuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHZoPAaSI0T9HjBlOMg9Vn+elCIFIK5X8Mg2za+C0QrH/N2XmISow=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421433,
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
      "signed_tx": "tx_+JELAfhCuECFcPOHykioIy1yisy6b10GBrWePmt1t4TvxfD6JCsTiQZLmPzUhUm+C+UPO8qynu9IDFlwn3PP1RmIT7HCXWcGuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHZoPAaSI0T9HjBlOMg9Vn+elCIFIK5X8Mg2za+C0QrH/N2XmISow==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
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
  "id": -576460752303421432,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEA+LNMm3qYyYQI1qsxGiW8DKBeAgeA1yWddMBKr17IWys/PaeMf6lD6HT7fBdh8sPrPmAT2bXnPA6neqi4CoiMJuECFcPOHykioIy1yisy6b10GBrWePmt1t4TvxfD6JCsTiQZLmPzUhUm+C+UPO8qynu9IDFlwn3PP1RmIT7HCXWcGuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHZoPAaSI0T9HjBlOMg9Vn+elCIFIK5X8Mg2za+C0QrH/N2kAWYiw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421432,
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
      "state": "tx_+NMLAfiEuEA+LNMm3qYyYQI1qsxGiW8DKBeAgeA1yWddMBKr17IWys/PaeMf6lD6HT7fBdh8sPrPmAT2bXnPA6neqi4CoiMJuECFcPOHykioIy1yisy6b10GBrWePmt1t4TvxfD6JCsTiQZLmPzUhUm+C+UPO8qynu9IDFlwn3PP1RmIT7HCXWcGuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHZoPAaSI0T9HjBlOMg9Vn+elCIFIK5X8Mg2za+C0QrH/N2kAWYiw=="
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
      "state": "tx_+NMLAfiEuEA+LNMm3qYyYQI1qsxGiW8DKBeAgeA1yWddMBKr17IWys/PaeMf6lD6HT7fBdh8sPrPmAT2bXnPA6neqi4CoiMJuECFcPOHykioIy1yisy6b10GBrWePmt1t4TvxfD6JCsTiQZLmPzUhUm+C+UPO8qynu9IDFlwn3PP1RmIT7HCXWcGuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHZoPAaSI0T9HjBlOMg9Vn+elCIFIK5X8Mg2za+C0QrH/N2kAWYiw=="
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 217
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": 217
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 217
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 217
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 217
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
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 217,
      "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
      "gas_price": 1,
      "gas_used": 11,
      "height": 217,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
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
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 217
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": 217
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 217
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 217
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 217
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
      "caller_nonce": 217,
      "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
      "gas_price": 1,
      "gas_used": 11,
      "height": 217,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 218,
      "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
      "gas_price": 1,
      "gas_used": 165,
      "height": 218,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Rgdqg8cEnamdMZ3Iutzsquv+whNId9kXbT47rUfxdgNM/sDyIbqH3",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
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
  "id": -576460752303421431,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEDWwdFba0LS7YANI/vONo3SOpk5BVmdRIqgTIAlnVRmlM1fvLydJQD3W7Eal391EtpxmeHu9oWcqcIj1YwLCqwHuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHaoPHBJ2pnTGdyLrc7Krr/sITSHfZF20+O61H8XYDTP7A8qpliAA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421431,
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
      "signed_tx": "tx_+JELAfhCuEDWwdFba0LS7YANI/vONo3SOpk5BVmdRIqgTIAlnVRmlM1fvLydJQD3W7Eal391EtpxmeHu9oWcqcIj1YwLCqwHuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHaoPHBJ2pnTGdyLrc7Krr/sITSHfZF20+O61H8XYDTP7A8qpliAA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
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
  "id": -576460752303421430,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEDWTlKhIqXOrfnWETi4DM+odKy935Vom6GYooJyrxK33SnSyf2pW4kpKbs9uhA1I3RvRcL1r3oHniyWabViMhYGuEDWwdFba0LS7YANI/vONo3SOpk5BVmdRIqgTIAlnVRmlM1fvLydJQD3W7Eal391EtpxmeHu9oWcqcIj1YwLCqwHuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHaoPHBJ2pnTGdyLrc7Krr/sITSHfZF20+O61H8XYDTP7A86QS8fg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421430,
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
      "state": "tx_+NMLAfiEuEDWTlKhIqXOrfnWETi4DM+odKy935Vom6GYooJyrxK33SnSyf2pW4kpKbs9uhA1I3RvRcL1r3oHniyWabViMhYGuEDWwdFba0LS7YANI/vONo3SOpk5BVmdRIqgTIAlnVRmlM1fvLydJQD3W7Eal391EtpxmeHu9oWcqcIj1YwLCqwHuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHaoPHBJ2pnTGdyLrc7Krr/sITSHfZF20+O61H8XYDTP7A86QS8fg=="
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
      "state": "tx_+NMLAfiEuEDWTlKhIqXOrfnWETi4DM+odKy935Vom6GYooJyrxK33SnSyf2pW4kpKbs9uhA1I3RvRcL1r3oHniyWabViMhYGuEDWwdFba0LS7YANI/vONo3SOpk5BVmdRIqgTIAlnVRmlM1fvLydJQD3W7Eal391EtpxmeHu9oWcqcIj1YwLCqwHuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHaoPHBJ2pnTGdyLrc7Krr/sITSHfZF20+O61H8XYDTP7A86QS8fg=="
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
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": 218
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
        "round": 218
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 218
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 218
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": 218
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
      "caller_nonce": 218,
      "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
      "gas_price": 1,
      "gas_used": 165,
      "height": 218,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": 218
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
        "round": 218
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 218
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 218
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": 218
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
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 218,
      "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
      "gas_price": 1,
      "gas_used": 165,
      "height": 218,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 219,
      "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
      "gas_price": 1,
      "gas_used": 165,
      "height": 219,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgdugxVR3FwE/UZvRWbVwHt1rUA8zbeWP3yGxhp4wWvXNwgSVN69P",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
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
  "id": -576460752303421429,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEB2NTpaYuCJ/xpjeocqW2X6cBJOPvIaGtGrPEMM94ATKEK3ogIt3MYdCKXDXN3/iyyDZrqm3cw0IFmlX5AWrNcPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHboMVUdxcBP1Gb0Vm1cB7da1APM23lj98hsYaeMFr1zcIE9Zjj+A=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421429,
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
      "signed_tx": "tx_+JELAfhCuEB2NTpaYuCJ/xpjeocqW2X6cBJOPvIaGtGrPEMM94ATKEK3ogIt3MYdCKXDXN3/iyyDZrqm3cw0IFmlX5AWrNcPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHboMVUdxcBP1Gb0Vm1cB7da1APM23lj98hsYaeMFr1zcIE9Zjj+A==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVCfRItc=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
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
  "id": -576460752303421428,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEB2NTpaYuCJ/xpjeocqW2X6cBJOPvIaGtGrPEMM94ATKEK3ogIt3MYdCKXDXN3/iyyDZrqm3cw0IFmlX5AWrNcPuECh5GSBh9/lcAdstx7ly+ZExBXpRgPStchPRqMPlo0rG1SkmdUIDEMOzyct6f3cxoe3wRsP8uvWT3MIt2uRbcIDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHboMVUdxcBP1Gb0Vm1cB7da1APM23lj98hsYaeMFr1zcIEKEcjqg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421428,
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
      "state": "tx_+NMLAfiEuEB2NTpaYuCJ/xpjeocqW2X6cBJOPvIaGtGrPEMM94ATKEK3ogIt3MYdCKXDXN3/iyyDZrqm3cw0IFmlX5AWrNcPuECh5GSBh9/lcAdstx7ly+ZExBXpRgPStchPRqMPlo0rG1SkmdUIDEMOzyct6f3cxoe3wRsP8uvWT3MIt2uRbcIDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHboMVUdxcBP1Gb0Vm1cB7da1APM23lj98hsYaeMFr1zcIEKEcjqg=="
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
      "state": "tx_+NMLAfiEuEB2NTpaYuCJ/xpjeocqW2X6cBJOPvIaGtGrPEMM94ATKEK3ogIt3MYdCKXDXN3/iyyDZrqm3cw0IFmlX5AWrNcPuECh5GSBh9/lcAdstx7ly+ZExBXpRgPStchPRqMPlo0rG1SkmdUIDEMOzyct6f3cxoe3wRsP8uvWT3MIt2uRbcIDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHboMVUdxcBP1Gb0Vm1cB7da1APM23lj98hsYaeMFr1zcIEKEcjqg=="
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": 219
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
        "round": 219
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 219
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 219
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": 219
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
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 219,
      "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
      "gas_price": 1,
      "gas_used": 165,
      "height": 219,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
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
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": 219
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
        "round": 219
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 219
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 219
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": 219
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
      "caller_nonce": 219,
      "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
      "gas_price": 1,
      "gas_used": 165,
      "height": 219,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 220,
      "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
      "gas_price": 1,
      "gas_used": 165,
      "height": 220,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgdygdyUbXPa7gWnYiJE70IUxpQMFYQY7BqECpv95kpVshdgRD2NW",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
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
  "id": -576460752303421427,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuECnft9ZCPlAyI+82I1qRG1MbwFhkY7P+4vuBb0f3b8m00M5+aKQ3UeUjNnGJoOKHrPsPu1K36uzzIDQ7i9u7jEBuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHcoHclG1z2u4Fp2IiRO9CFMaUDBWEGOwahAqb/eZKVbIXYIXAGfg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421427,
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
      "signed_tx": "tx_+JELAfhCuECnft9ZCPlAyI+82I1qRG1MbwFhkY7P+4vuBb0f3b8m00M5+aKQ3UeUjNnGJoOKHrPsPu1K36uzzIDQ7i9u7jEBuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHcoHclG1z2u4Fp2IiRO9CFMaUDBWEGOwahAqb/eZKVbIXYIXAGfg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
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
  "id": -576460752303421426,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuECnft9ZCPlAyI+82I1qRG1MbwFhkY7P+4vuBb0f3b8m00M5+aKQ3UeUjNnGJoOKHrPsPu1K36uzzIDQ7i9u7jEBuEDVnVxY7t8fdYQviVUjZM92NWvr4VXI1VZev8gZMo6xrC7jo42iYwyCOsomXrMGfj8s40dnGV60X7p6OhH05TILuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHcoHclG1z2u4Fp2IiRO9CFMaUDBWEGOwahAqb/eZKVbIXYnTrmCQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421426,
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
      "state": "tx_+NMLAfiEuECnft9ZCPlAyI+82I1qRG1MbwFhkY7P+4vuBb0f3b8m00M5+aKQ3UeUjNnGJoOKHrPsPu1K36uzzIDQ7i9u7jEBuEDVnVxY7t8fdYQviVUjZM92NWvr4VXI1VZev8gZMo6xrC7jo42iYwyCOsomXrMGfj8s40dnGV60X7p6OhH05TILuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHcoHclG1z2u4Fp2IiRO9CFMaUDBWEGOwahAqb/eZKVbIXYnTrmCQ=="
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
      "state": "tx_+NMLAfiEuECnft9ZCPlAyI+82I1qRG1MbwFhkY7P+4vuBb0f3b8m00M5+aKQ3UeUjNnGJoOKHrPsPu1K36uzzIDQ7i9u7jEBuEDVnVxY7t8fdYQviVUjZM92NWvr4VXI1VZev8gZMo6xrC7jo42iYwyCOsomXrMGfj8s40dnGV60X7p6OhH05TILuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHcoHclG1z2u4Fp2IiRO9CFMaUDBWEGOwahAqb/eZKVbIXYnTrmCQ=="
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
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": 220
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
        "round": 220
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 220
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 220
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": 220
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
      "caller_nonce": 220,
      "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
      "gas_price": 1,
      "gas_used": 165,
      "height": 220,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": 220
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
        "round": 220
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 220
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 220
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": 220
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
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 220,
      "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
      "gas_price": 1,
      "gas_used": 165,
      "height": 220,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 221,
      "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
      "gas_price": 1,
      "gas_used": 165,
      "height": 221,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Rgd2gBnzi5IQ1HvivSlc4grVqeiJzEfDHhM/hqDrUjMmE6CO0f3d8",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
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
  "id": -576460752303421425,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEBtF0eS+AgXTRpGq9FlbK+BayTLXeP27X9FSoQyTMVWPEXqZ6UeMjAOaks9d2TLAyLNjch65CRWTiwnC2lPO0oCuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHdoAZ84uSENR74r0pXOIK1anoicxHwx4TP4ag61IzJhOgjZM75YQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421425,
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
      "signed_tx": "tx_+JELAfhCuEBtF0eS+AgXTRpGq9FlbK+BayTLXeP27X9FSoQyTMVWPEXqZ6UeMjAOaks9d2TLAyLNjch65CRWTiwnC2lPO0oCuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHdoAZ84uSENR74r0pXOIK1anoicxHwx4TP4ag61IzJhOgjZM75YQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoCaIPxcic2kqbLL/lkoadjjdStxdGVtIAGBeOlxXMTWrVrvp0Ys=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
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
  "id": -576460752303421424,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEBtF0eS+AgXTRpGq9FlbK+BayTLXeP27X9FSoQyTMVWPEXqZ6UeMjAOaks9d2TLAyLNjch65CRWTiwnC2lPO0oCuEB5dJVXZtlECVe4niLgyOhd+2kXZ/OAD2FzEFdeOU+8GtDegLLvnNT69/I8FzSGvyrSJdoZEuD9J5i4ghhaHugPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHdoAZ84uSENR74r0pXOIK1anoicxHwx4TP4ag61IzJhOgj8oCxIg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421424,
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
      "state": "tx_+NMLAfiEuEBtF0eS+AgXTRpGq9FlbK+BayTLXeP27X9FSoQyTMVWPEXqZ6UeMjAOaks9d2TLAyLNjch65CRWTiwnC2lPO0oCuEB5dJVXZtlECVe4niLgyOhd+2kXZ/OAD2FzEFdeOU+8GtDegLLvnNT69/I8FzSGvyrSJdoZEuD9J5i4ghhaHugPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHdoAZ84uSENR74r0pXOIK1anoicxHwx4TP4ag61IzJhOgj8oCxIg=="
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
      "state": "tx_+NMLAfiEuEBtF0eS+AgXTRpGq9FlbK+BayTLXeP27X9FSoQyTMVWPEXqZ6UeMjAOaks9d2TLAyLNjch65CRWTiwnC2lPO0oCuEB5dJVXZtlECVe4niLgyOhd+2kXZ/OAD2FzEFdeOU+8GtDegLLvnNT69/I8FzSGvyrSJdoZEuD9J5i4ghhaHugPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHdoAZ84uSENR74r0pXOIK1anoicxHwx4TP4ag61IzJhOgj8oCxIg=="
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": 221
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
        "round": 221
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 221
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 221
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": 221
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
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 221,
      "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
      "gas_price": 1,
      "gas_used": 165,
      "height": 221,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
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
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": 221
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
        "round": 221
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 221
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 221
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
    "round": 221
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
      "caller_nonce": 221,
      "contract_id": "ct_Di9GymjBNxf5CS4brH5d43bxgpqF9AFW7fiLsAThNKYJ8JWcK",
      "gas_price": 1,
      "gas_used": 165,
      "height": 221,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 222,
      "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
      "gas_price": 1,
      "gas_used": 11,
      "height": 222,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Rgd6gtM7Pe4jIp9b2pKvMsijFKBRPSoAiAQ9Iz6gP1KLLteZ12az1",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
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
  "id": -576460752303421423,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuECLYZAEyV0092e+VC7TA2JingZJhW08eBrNVRBe77PKk19d58cfV4Pp3uAL2AEcOxHXi4k/CxWWQAo/oPTbM8oFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHeoLTOz3uIyKfW9qSrzLIoxSgUT0qAIgEPSM+oD9Siy7XmX+HSxA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421423,
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
      "signed_tx": "tx_+JELAfhCuECLYZAEyV0092e+VC7TA2JingZJhW08eBrNVRBe77PKk19d58cfV4Pp3uAL2AEcOxHXi4k/CxWWQAo/oPTbM8oFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHeoLTOz3uIyKfW9qSrzLIoxSgUT0qAIgEPSM+oD9Siy7XmX+HSxA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
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
  "id": -576460752303421422,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEBrkiE2F/CLqRdc/VAiqSnMxX8TmOyRJTVAEou7r8zcxPBH5nGVbH/9glyRyPb1uL17Xqi7/f5xDfb10nOMF1oNuECLYZAEyV0092e+VC7TA2JingZJhW08eBrNVRBe77PKk19d58cfV4Pp3uAL2AEcOxHXi4k/CxWWQAo/oPTbM8oFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHeoLTOz3uIyKfW9qSrzLIoxSgUT0qAIgEPSM+oD9Siy7XmiHUVOg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421422,
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
      "state": "tx_+NMLAfiEuEBrkiE2F/CLqRdc/VAiqSnMxX8TmOyRJTVAEou7r8zcxPBH5nGVbH/9glyRyPb1uL17Xqi7/f5xDfb10nOMF1oNuECLYZAEyV0092e+VC7TA2JingZJhW08eBrNVRBe77PKk19d58cfV4Pp3uAL2AEcOxHXi4k/CxWWQAo/oPTbM8oFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHeoLTOz3uIyKfW9qSrzLIoxSgUT0qAIgEPSM+oD9Siy7XmiHUVOg=="
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
      "state": "tx_+NMLAfiEuEBrkiE2F/CLqRdc/VAiqSnMxX8TmOyRJTVAEou7r8zcxPBH5nGVbH/9glyRyPb1uL17Xqi7/f5xDfb10nOMF1oNuECLYZAEyV0092e+VC7TA2JingZJhW08eBrNVRBe77PKk19d58cfV4Pp3uAL2AEcOxHXi4k/CxWWQAo/oPTbM8oFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHeoLTOz3uIyKfW9qSrzLIoxSgUT0qAIgEPSM+oD9Siy7XmiHUVOg=="
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
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 222
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": 222
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 222
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 222
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 222
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
      "caller_nonce": 222,
      "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
      "gas_price": 1,
      "gas_used": 11,
      "height": 222,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 222
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": 222
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 222
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 222
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 222
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
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 222,
      "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
      "gas_price": 1,
      "gas_used": 11,
      "height": 222,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 223,
      "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
      "gas_price": 1,
      "gas_used": 11,
      "height": 223,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Rgd+gwqE8+xIH4uRAYtaECOmz7A3lCzWrRJkfWMQvrjy1U8eZqyDl",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
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
  "id": -576460752303421421,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEA4/DO5gweu4kxDlIQ68lYP3e6osjgVJS9B2S/o3zi9IhAkatrSMCxzdEyTahM0I6wrbFmfZWryn5r2kK0Ls1cLuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHfoMKhPPsSB+LkQGLWhAjps+wN5Qs1q0SZH1jEL648tVPHXZdGgA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421421,
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
      "signed_tx": "tx_+JELAfhCuEA4/DO5gweu4kxDlIQ68lYP3e6osjgVJS9B2S/o3zi9IhAkatrSMCxzdEyTahM0I6wrbFmfZWryn5r2kK0Ls1cLuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHfoMKhPPsSB+LkQGLWhAjps+wN5Qs1q0SZH1jEL648tVPHXZdGgA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
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
  "id": -576460752303421420,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEA4/DO5gweu4kxDlIQ68lYP3e6osjgVJS9B2S/o3zi9IhAkatrSMCxzdEyTahM0I6wrbFmfZWryn5r2kK0Ls1cLuED2W7gsbipCfyVT0XR5igzw2PCpcP4k0uYv04AW/ofFxz2ZVwYKsK3hVGkFRT5KaBZrkE2XxnJdxYZTiyjBGZYCuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHfoMKhPPsSB+LkQGLWhAjps+wN5Qs1q0SZH1jEL648tVPHb39iLA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421420,
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
      "state": "tx_+NMLAfiEuEA4/DO5gweu4kxDlIQ68lYP3e6osjgVJS9B2S/o3zi9IhAkatrSMCxzdEyTahM0I6wrbFmfZWryn5r2kK0Ls1cLuED2W7gsbipCfyVT0XR5igzw2PCpcP4k0uYv04AW/ofFxz2ZVwYKsK3hVGkFRT5KaBZrkE2XxnJdxYZTiyjBGZYCuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHfoMKhPPsSB+LkQGLWhAjps+wN5Qs1q0SZH1jEL648tVPHb39iLA=="
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
      "state": "tx_+NMLAfiEuEA4/DO5gweu4kxDlIQ68lYP3e6osjgVJS9B2S/o3zi9IhAkatrSMCxzdEyTahM0I6wrbFmfZWryn5r2kK0Ls1cLuED2W7gsbipCfyVT0XR5igzw2PCpcP4k0uYv04AW/ofFxz2ZVwYKsK3hVGkFRT5KaBZrkE2XxnJdxYZTiyjBGZYCuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHfoMKhPPsSB+LkQGLWhAjps+wN5Qs1q0SZH1jEL648tVPHb39iLA=="
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 223
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": 223
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 223
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 223
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 223
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
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 223,
      "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
      "gas_price": 1,
      "gas_used": 11,
      "height": 223,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
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
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 223
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
        "round": 223
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 223
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 223
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
    "round": 223
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
      "caller_nonce": 223,
      "contract_id": "ct_HyFiJaamsj75dKmN94xdGwnnCC9bsUXTBMMoknrE7mwgfcRm6",
      "gas_price": 1,
      "gas_used": 11,
      "height": 223,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
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
    "deposit": "1",
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfP4oEp9E=",
        "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
        "deposit": "1",
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
    "call_data": "cb_KxFE1kQfP4oEp9E=",
    "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
    "deposit": 10,
    "vm_version": "1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfP4oEp9E=",
        "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
        "deposit": 10,
        "vm_version": "1"
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
    "abi_version": "1",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": "1",
        "call_data": "cb_KxFE1kQfP4oEp9E=",
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgeCgUkFYYnHgRi62kvCzG1ObQPs2NHt0SBM8BCiMi7S3XFLtw7Pg",
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
  "id": -576460752303421419,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuECQWpyW1N5yvE7tfsndizyVTQSyqpf+puBm5IldXCA8d3uWhRvs530PX3Lt/NzQRsvDXQgM+MiGDZ4x6znGy9MJuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHgoFJBWGJx4EYutpLwsxtTm0D7NjR7dEgTPAQojIu0t1xSd3VE3w=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421419,
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
      "signed_tx": "tx_+JELAfhCuECQWpyW1N5yvE7tfsndizyVTQSyqpf+puBm5IldXCA8d3uWhRvs530PX3Lt/NzQRsvDXQgM+MiGDZ4x6znGy9MJuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHgoFJBWGJx4EYutpLwsxtTm0D7NjR7dEgTPAQojIu0t1xSd3VE3w==",
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
  "id": -576460752303421418,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuECQWpyW1N5yvE7tfsndizyVTQSyqpf+puBm5IldXCA8d3uWhRvs530PX3Lt/NzQRsvDXQgM+MiGDZ4x6znGy9MJuECckBklqQADbiDzBvrQyoSP6nS6tGHeGH5oJ+GJxili2RoFubuPtiQuSLvj/M1bV0rlrYsUAnFWSAaUHDQugS4KuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHgoFJBWGJx4EYutpLwsxtTm0D7NjR7dEgTPAQojIu0t1xSYdzO/g=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421418,
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
      "state": "tx_+NMLAfiEuECQWpyW1N5yvE7tfsndizyVTQSyqpf+puBm5IldXCA8d3uWhRvs530PX3Lt/NzQRsvDXQgM+MiGDZ4x6znGy9MJuECckBklqQADbiDzBvrQyoSP6nS6tGHeGH5oJ+GJxili2RoFubuPtiQuSLvj/M1bV0rlrYsUAnFWSAaUHDQugS4KuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHgoFJBWGJx4EYutpLwsxtTm0D7NjR7dEgTPAQojIu0t1xSYdzO/g=="
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
      "state": "tx_+NMLAfiEuECQWpyW1N5yvE7tfsndizyVTQSyqpf+puBm5IldXCA8d3uWhRvs530PX3Lt/NzQRsvDXQgM+MiGDZ4x6znGy9MJuECckBklqQADbiDzBvrQyoSP6nS6tGHeGH5oJ+GJxili2RoFubuPtiQuSLvj/M1bV0rlrYsUAnFWSAaUHDQugS4KuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHgoFJBWGJx4EYutpLwsxtTm0D7NjR7dEgTPAQojIu0t1xSYdzO/g=="
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
    "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
    "deposit": "1",
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfP4oEp9E=",
        "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
        "deposit": "1",
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
    "call_data": "cb_KxFE1kQfP4oEp9E=",
    "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
    "deposit": 10,
    "vm_version": "1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfP4oEp9E=",
        "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
        "deposit": 10,
        "vm_version": "1"
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
    "abi_version": "1",
    "call_data": "cb_KxFE1kQfP4oEp9E=",
    "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": "1",
        "call_data": "cb_KxFE1kQfP4oEp9E=",
        "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
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
    "call_data": "cb_KxFE1kQfP4oEp9E=",
    "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgeGgHsRaBmhIm3cm0ExZf9xeWnGUoxXwkGRYnKcXaVLYlW5LQc+R",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
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
  "id": -576460752303421417,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEAZhL3vNbMKglsSWffR3/FJmce+fvd8ijGd1N5poJOjHmdHRBNwpPKv165v28n9VG62pm9wVl9e4B9fS8ImnU4PuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHhoB7EWgZoSJt3JtBMWX/cXlpxlKMV8JBkWJynF2lS2JVuw4rtSg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421417,
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
      "signed_tx": "tx_+JELAfhCuEAZhL3vNbMKglsSWffR3/FJmce+fvd8ijGd1N5poJOjHmdHRBNwpPKv165v28n9VG62pm9wVl9e4B9fS8ImnU4PuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHhoB7EWgZoSJt3JtBMWX/cXlpxlKMV8JBkWJynF2lS2JVuw4rtSg==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
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
  "id": -576460752303421416,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAZhL3vNbMKglsSWffR3/FJmce+fvd8ijGd1N5poJOjHmdHRBNwpPKv165v28n9VG62pm9wVl9e4B9fS8ImnU4PuEBhVQyHzwtYzZOy/ORVglrKt8vl44E4C7iXqvRJOKRXe8zZTMA3CtpdA8k321KnjJn9mmOysjB+RqYp3gW/STUOuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHhoB7EWgZoSJt3JtBMWX/cXlpxlKMV8JBkWJynF2lS2JVue3YYCw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421416,
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
      "state": "tx_+NMLAfiEuEAZhL3vNbMKglsSWffR3/FJmce+fvd8ijGd1N5poJOjHmdHRBNwpPKv165v28n9VG62pm9wVl9e4B9fS8ImnU4PuEBhVQyHzwtYzZOy/ORVglrKt8vl44E4C7iXqvRJOKRXe8zZTMA3CtpdA8k321KnjJn9mmOysjB+RqYp3gW/STUOuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHhoB7EWgZoSJt3JtBMWX/cXlpxlKMV8JBkWJynF2lS2JVue3YYCw=="
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
      "state": "tx_+NMLAfiEuEAZhL3vNbMKglsSWffR3/FJmce+fvd8ijGd1N5poJOjHmdHRBNwpPKv165v28n9VG62pm9wVl9e4B9fS8ImnU4PuEBhVQyHzwtYzZOy/ORVglrKt8vl44E4C7iXqvRJOKRXe8zZTMA3CtpdA8k321KnjJn9mmOysjB+RqYp3gW/STUOuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHhoB7EWgZoSJt3JtBMWX/cXlpxlKMV8JBkWJynF2lS2JVue3YYCw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 226,
      "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
      "gas_price": 1,
      "gas_used": 11,
      "height": 226,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgeKgtTi3750fVjekWbD4mj+NS7yVqbSVr4uu9vVesKxiDrcrl4lT",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
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
  "id": -576460752303421415,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEAZKj/WX0YVuCOIF5+w1kbl263/fbW2KwcXiv/r9AGUaAKz3GUEPyppcoUEvPHcMxbVecPF8UDmuruPDj386iYOuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHioLU4t++dH1Y3pFmw+Jo/jUu8lam0la+Lrvb1XrCsYg63DE4vLg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421415,
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
      "signed_tx": "tx_+JELAfhCuEAZKj/WX0YVuCOIF5+w1kbl263/fbW2KwcXiv/r9AGUaAKz3GUEPyppcoUEvPHcMxbVecPF8UDmuruPDj386iYOuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHioLU4t++dH1Y3pFmw+Jo/jUu8lam0la+Lrvb1XrCsYg63DE4vLg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
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
  "id": -576460752303421414,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAZKj/WX0YVuCOIF5+w1kbl263/fbW2KwcXiv/r9AGUaAKz3GUEPyppcoUEvPHcMxbVecPF8UDmuruPDj386iYOuECCfzMd13FliYiZKgB+jy7pr/evgpkzt+9349i38IlTs/H1F88/2S+mpYorqjWnnQi08zxeag7lVbcwOIkjyJILuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHioLU4t++dH1Y3pFmw+Jo/jUu8lam0la+Lrvb1XrCsYg63a3xCjw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421414,
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
      "state": "tx_+NMLAfiEuEAZKj/WX0YVuCOIF5+w1kbl263/fbW2KwcXiv/r9AGUaAKz3GUEPyppcoUEvPHcMxbVecPF8UDmuruPDj386iYOuECCfzMd13FliYiZKgB+jy7pr/evgpkzt+9349i38IlTs/H1F88/2S+mpYorqjWnnQi08zxeag7lVbcwOIkjyJILuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHioLU4t++dH1Y3pFmw+Jo/jUu8lam0la+Lrvb1XrCsYg63a3xCjw=="
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
      "state": "tx_+NMLAfiEuEAZKj/WX0YVuCOIF5+w1kbl263/fbW2KwcXiv/r9AGUaAKz3GUEPyppcoUEvPHcMxbVecPF8UDmuruPDj386iYOuECCfzMd13FliYiZKgB+jy7pr/evgpkzt+9349i38IlTs/H1F88/2S+mpYorqjWnnQi08zxeag7lVbcwOIkjyJILuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHioLU4t++dH1Y3pFmw+Jo/jUu8lam0la+Lrvb1XrCsYg63a3xCjw=="
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
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 226
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": 226
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 226
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 226
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 226
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
      "caller_nonce": 226,
      "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
      "gas_price": 1,
      "gas_used": 11,
      "height": 226,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 226
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": 226
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 226
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 226
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 226
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
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 226,
      "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
      "gas_price": 1,
      "gas_used": 11,
      "height": 226,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 227,
      "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
      "gas_price": 1,
      "gas_used": 11,
      "height": 227,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgeOgLw1UtV062CbzuLBe8dv6k2ENonHkj8L/yWhaIR+pW0TZUySo",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
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
  "id": -576460752303421413,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuED3IM3QejH1BxSJLejLN4aCqtdExdt682AX81t2USznIgMl5H6J1jtKJdM+Cy7yBUh126BZ7IUgtlViJ6DllQkFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHjoC8NVLVdOtgm87iwXvHb+pNhDaJx5I/C/8loWiEfqVtE4xg+TQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421413,
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
      "signed_tx": "tx_+JELAfhCuED3IM3QejH1BxSJLejLN4aCqtdExdt682AX81t2USznIgMl5H6J1jtKJdM+Cy7yBUh126BZ7IUgtlViJ6DllQkFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHjoC8NVLVdOtgm87iwXvHb+pNhDaJx5I/C/8loWiEfqVtE4xg+TQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
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
  "id": -576460752303421412,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAPLM0kt3oZRCwxDk08ro6x1q0WdXLxlF8jNscRZ1uKOxZLD2+sswLt+q4WanYxafLb+OLqbj0DkdsbpGNLMOIGuED3IM3QejH1BxSJLejLN4aCqtdExdt682AX81t2USznIgMl5H6J1jtKJdM+Cy7yBUh126BZ7IUgtlViJ6DllQkFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHjoC8NVLVdOtgm87iwXvHb+pNhDaJx5I/C/8loWiEfqVtEkZSLdA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421412,
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
      "state": "tx_+NMLAfiEuEAPLM0kt3oZRCwxDk08ro6x1q0WdXLxlF8jNscRZ1uKOxZLD2+sswLt+q4WanYxafLb+OLqbj0DkdsbpGNLMOIGuED3IM3QejH1BxSJLejLN4aCqtdExdt682AX81t2USznIgMl5H6J1jtKJdM+Cy7yBUh126BZ7IUgtlViJ6DllQkFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHjoC8NVLVdOtgm87iwXvHb+pNhDaJx5I/C/8loWiEfqVtEkZSLdA=="
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
      "state": "tx_+NMLAfiEuEAPLM0kt3oZRCwxDk08ro6x1q0WdXLxlF8jNscRZ1uKOxZLD2+sswLt+q4WanYxafLb+OLqbj0DkdsbpGNLMOIGuED3IM3QejH1BxSJLejLN4aCqtdExdt682AX81t2USznIgMl5H6J1jtKJdM+Cy7yBUh126BZ7IUgtlViJ6DllQkFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHjoC8NVLVdOtgm87iwXvHb+pNhDaJx5I/C/8loWiEfqVtEkZSLdA=="
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 227
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": 227
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 227
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 227
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 227
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
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 227,
      "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
      "gas_price": 1,
      "gas_used": 11,
      "height": 227,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
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
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 227
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": 227
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 227
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 227
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 227
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
      "caller_nonce": 227,
      "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
      "gas_price": 1,
      "gas_used": 11,
      "height": 227,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 228,
      "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
      "gas_price": 1,
      "gas_used": 11,
      "height": 228,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgeSgiRCXsH+eKB1qf4voshOXBdHR52vWTF8byIXJjxQssCwpoB5G",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
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
  "id": -576460752303421411,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuED5JsRvbHJd0RwhbB6OJdieUCBEhoqyqBC5Dr9nZDyCwPHYHCpQknIjvZ8Ejsp8WpqYCDUQ7M1CANieuJpmBEcIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHkoIkQl7B/nigdan+L6LITlwXR0edr1kxfG8iFyY8ULLAsPTm4RA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421411,
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
      "signed_tx": "tx_+JELAfhCuED5JsRvbHJd0RwhbB6OJdieUCBEhoqyqBC5Dr9nZDyCwPHYHCpQknIjvZ8Ejsp8WpqYCDUQ7M1CANieuJpmBEcIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHkoIkQl7B/nigdan+L6LITlwXR0edr1kxfG8iFyY8ULLAsPTm4RA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
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
  "id": -576460752303421410,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEBukAqmP/CFrS6zLHQdV+x+H7sfWsfplJixb5ldF7EV9/3y1q2T4z7layBF0VXHO/Z5s9e1PZAm7DxGYvQhJigHuED5JsRvbHJd0RwhbB6OJdieUCBEhoqyqBC5Dr9nZDyCwPHYHCpQknIjvZ8Ejsp8WpqYCDUQ7M1CANieuJpmBEcIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHkoIkQl7B/nigdan+L6LITlwXR0edr1kxfG8iFyY8ULLAs8waPqA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421410,
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
      "state": "tx_+NMLAfiEuEBukAqmP/CFrS6zLHQdV+x+H7sfWsfplJixb5ldF7EV9/3y1q2T4z7layBF0VXHO/Z5s9e1PZAm7DxGYvQhJigHuED5JsRvbHJd0RwhbB6OJdieUCBEhoqyqBC5Dr9nZDyCwPHYHCpQknIjvZ8Ejsp8WpqYCDUQ7M1CANieuJpmBEcIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHkoIkQl7B/nigdan+L6LITlwXR0edr1kxfG8iFyY8ULLAs8waPqA=="
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
      "state": "tx_+NMLAfiEuEBukAqmP/CFrS6zLHQdV+x+H7sfWsfplJixb5ldF7EV9/3y1q2T4z7layBF0VXHO/Z5s9e1PZAm7DxGYvQhJigHuED5JsRvbHJd0RwhbB6OJdieUCBEhoqyqBC5Dr9nZDyCwPHYHCpQknIjvZ8Ejsp8WpqYCDUQ7M1CANieuJpmBEcIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHkoIkQl7B/nigdan+L6LITlwXR0edr1kxfG8iFyY8ULLAs8waPqA=="
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
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 228
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": 228
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 228
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 228
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 228
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
      "caller_nonce": 228,
      "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
      "gas_price": 1,
      "gas_used": 11,
      "height": 228,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 228
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": 228
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 228
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 228
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 228
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
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 228,
      "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
      "gas_price": 1,
      "gas_used": 11,
      "height": 228,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 229,
      "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
      "gas_price": 1,
      "gas_used": 11,
      "height": 229,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgeWgWsAp2YV6x1MRMjOrJOlJ18GGYpDLIfoS+B4yDzfZpsOH0VjM",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
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
  "id": -576460752303421409,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuECgCTdvzz548O5OhQBU57pwxqvLYCp8nsn7cUwUBLPHpvTRQTDf42AB5GN0oKY3u0a7AXRpATCnwp7dUCJIqKEFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHloFrAKdmFesdTETIzqyTpSdfBhmKQyyH6EvgeMg832abD89up0g=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421409,
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
      "signed_tx": "tx_+JELAfhCuECgCTdvzz548O5OhQBU57pwxqvLYCp8nsn7cUwUBLPHpvTRQTDf42AB5GN0oKY3u0a7AXRpATCnwp7dUCJIqKEFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHloFrAKdmFesdTETIzqyTpSdfBhmKQyyH6EvgeMg832abD89up0g==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
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
  "id": -576460752303421408,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuECgCTdvzz548O5OhQBU57pwxqvLYCp8nsn7cUwUBLPHpvTRQTDf42AB5GN0oKY3u0a7AXRpATCnwp7dUCJIqKEFuEDA/TyToFtQoGBOjay0K8URyVJoukFOcBbYkGy3KECcQRtvOzdbk9CI+X2XV/CM7y1XJnDSmsuVaVQz1qUAleIPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHloFrAKdmFesdTETIzqyTpSdfBhmKQyyH6EvgeMg832abDtUeAgw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421408,
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
      "state": "tx_+NMLAfiEuECgCTdvzz548O5OhQBU57pwxqvLYCp8nsn7cUwUBLPHpvTRQTDf42AB5GN0oKY3u0a7AXRpATCnwp7dUCJIqKEFuEDA/TyToFtQoGBOjay0K8URyVJoukFOcBbYkGy3KECcQRtvOzdbk9CI+X2XV/CM7y1XJnDSmsuVaVQz1qUAleIPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHloFrAKdmFesdTETIzqyTpSdfBhmKQyyH6EvgeMg832abDtUeAgw=="
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
      "state": "tx_+NMLAfiEuECgCTdvzz548O5OhQBU57pwxqvLYCp8nsn7cUwUBLPHpvTRQTDf42AB5GN0oKY3u0a7AXRpATCnwp7dUCJIqKEFuEDA/TyToFtQoGBOjay0K8URyVJoukFOcBbYkGy3KECcQRtvOzdbk9CI+X2XV/CM7y1XJnDSmsuVaVQz1qUAleIPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHloFrAKdmFesdTETIzqyTpSdfBhmKQyyH6EvgeMg832abDtUeAgw=="
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 229
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": 229
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 229
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 229
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 229
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
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 229,
      "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
      "gas_price": 1,
      "gas_used": 11,
      "height": 229,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
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
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 229
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": 229
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 229
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 229
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 229
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
      "caller_nonce": 229,
      "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
      "gas_price": 1,
      "gas_used": 11,
      "height": 229,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 230,
      "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
      "gas_price": 1,
      "gas_used": 165,
      "height": 230,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Rgeag0c9xKh6nD5+3TRis4ugbRVQ+JOy3y0+7+6dsvBS0gwTJO5/f",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
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
  "id": -576460752303421407,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuECl492bklLjBtQN2QBkpNzcleQce4co1p8eJSNwAozzcUR+mYlE5oxd2JGOXtj9seXC21QPw0I8nJNtElTyjEMEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHmoNHPcSoepw+ft00YrOLoG0VUPiTst8tPu/unbLwUtIMEKodnoQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421407,
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
      "signed_tx": "tx_+JELAfhCuECl492bklLjBtQN2QBkpNzcleQce4co1p8eJSNwAozzcUR+mYlE5oxd2JGOXtj9seXC21QPw0I8nJNtElTyjEMEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHmoNHPcSoepw+ft00YrOLoG0VUPiTst8tPu/unbLwUtIMEKodnoQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
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
  "id": -576460752303421406,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEBFi7jxAGmBbRt1JAj8IDpYNelaht5nkpNquJqhS/uMNtKNfPzKpJlQ3E1kNBU7/ZZKQ56OtfPidiKa6qnIlRcFuECl492bklLjBtQN2QBkpNzcleQce4co1p8eJSNwAozzcUR+mYlE5oxd2JGOXtj9seXC21QPw0I8nJNtElTyjEMEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHmoNHPcSoepw+ft00YrOLoG0VUPiTst8tPu/unbLwUtIMEoRbdHg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421406,
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
      "state": "tx_+NMLAfiEuEBFi7jxAGmBbRt1JAj8IDpYNelaht5nkpNquJqhS/uMNtKNfPzKpJlQ3E1kNBU7/ZZKQ56OtfPidiKa6qnIlRcFuECl492bklLjBtQN2QBkpNzcleQce4co1p8eJSNwAozzcUR+mYlE5oxd2JGOXtj9seXC21QPw0I8nJNtElTyjEMEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHmoNHPcSoepw+ft00YrOLoG0VUPiTst8tPu/unbLwUtIMEoRbdHg=="
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
      "state": "tx_+NMLAfiEuEBFi7jxAGmBbRt1JAj8IDpYNelaht5nkpNquJqhS/uMNtKNfPzKpJlQ3E1kNBU7/ZZKQ56OtfPidiKa6qnIlRcFuECl492bklLjBtQN2QBkpNzcleQce4co1p8eJSNwAozzcUR+mYlE5oxd2JGOXtj9seXC21QPw0I8nJNtElTyjEMEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHmoNHPcSoepw+ft00YrOLoG0VUPiTst8tPu/unbLwUtIMEoRbdHg=="
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
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": 230
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
        "round": 230
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 230
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 230
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": 230
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
      "caller_nonce": 230,
      "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
      "gas_price": 1,
      "gas_used": 165,
      "height": 230,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": 230
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
        "round": 230
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 230
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 230
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": 230
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
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 230,
      "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
      "gas_price": 1,
      "gas_used": 165,
      "height": 230,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 231,
      "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
      "gas_price": 1,
      "gas_used": 165,
      "height": 231,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgeegWXuNiiQnsjpTOM1vGxPTOEESsknqV54ouQWTCu/qgTALH+pc",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
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
  "id": -576460752303421405,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEA69NCZzvb2j8rAeXagATBsrs7b2/P0tCpDxmNhvj9STmW0SHT84ss4XeTY6trQWjpuXuo7AahvMvz3HWrETbIKuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHnoFl7jYokJ7I6UzjNbxsT0zhBErJJ6leeKLkFkwrv6oEwxaoWyQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421405,
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
      "signed_tx": "tx_+JELAfhCuEA69NCZzvb2j8rAeXagATBsrs7b2/P0tCpDxmNhvj9STmW0SHT84ss4XeTY6trQWjpuXuo7AahvMvz3HWrETbIKuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHnoFl7jYokJ7I6UzjNbxsT0zhBErJJ6leeKLkFkwrv6oEwxaoWyQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVLglgy8=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
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
  "id": -576460752303421404,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEA69NCZzvb2j8rAeXagATBsrs7b2/P0tCpDxmNhvj9STmW0SHT84ss4XeTY6trQWjpuXuo7AahvMvz3HWrETbIKuEDT/tgQxOeGu2cgkeyktmU1DRwzF6UrSns2wQ0flUEU4CHBi3ovjX8fXw3W3jWjFH7X8e27yUGJcM9tzTQRDYEEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHnoFl7jYokJ7I6UzjNbxsT0zhBErJJ6leeKLkFkwrv6oEwaVsP/w=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421404,
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
      "state": "tx_+NMLAfiEuEA69NCZzvb2j8rAeXagATBsrs7b2/P0tCpDxmNhvj9STmW0SHT84ss4XeTY6trQWjpuXuo7AahvMvz3HWrETbIKuEDT/tgQxOeGu2cgkeyktmU1DRwzF6UrSns2wQ0flUEU4CHBi3ovjX8fXw3W3jWjFH7X8e27yUGJcM9tzTQRDYEEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHnoFl7jYokJ7I6UzjNbxsT0zhBErJJ6leeKLkFkwrv6oEwaVsP/w=="
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
      "state": "tx_+NMLAfiEuEA69NCZzvb2j8rAeXagATBsrs7b2/P0tCpDxmNhvj9STmW0SHT84ss4XeTY6trQWjpuXuo7AahvMvz3HWrETbIKuEDT/tgQxOeGu2cgkeyktmU1DRwzF6UrSns2wQ0flUEU4CHBi3ovjX8fXw3W3jWjFH7X8e27yUGJcM9tzTQRDYEEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHnoFl7jYokJ7I6UzjNbxsT0zhBErJJ6leeKLkFkwrv6oEwaVsP/w=="
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": 231
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
        "round": 231
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 231
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 231
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": 231
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
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 231,
      "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
      "gas_price": 1,
      "gas_used": 165,
      "height": 231,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
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
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": 231
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
        "round": 231
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 231
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 231
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": 231
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
      "caller_nonce": 231,
      "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
      "gas_price": 1,
      "gas_used": 165,
      "height": 231,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 232,
      "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
      "gas_price": 1,
      "gas_used": 165,
      "height": 232,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Rgeig/8TPQP+G2UbwHTJrwaCbiVKKAFModkqyaeUb96N2UGoaDNLA",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
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
  "id": -576460752303421403,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEC7quTZhUF8/dtgaqJFO41GKMLR/l1QVkR/1WGKDMrRIDNudcLyC8uhlpprM+wvH8qnxYO7RbR5dLq63d7lREYHuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHooP/Ez0D/htlG8B0ya8Ggm4lSigBTKHZKsmnlG/ejdlBqEaJpLw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421403,
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
      "signed_tx": "tx_+JELAfhCuEC7quTZhUF8/dtgaqJFO41GKMLR/l1QVkR/1WGKDMrRIDNudcLyC8uhlpprM+wvH8qnxYO7RbR5dLq63d7lREYHuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHooP/Ez0D/htlG8B0ya8Ggm4lSigBTKHZKsmnlG/ejdlBqEaJpLw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
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
  "id": -576460752303421402,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEC7quTZhUF8/dtgaqJFO41GKMLR/l1QVkR/1WGKDMrRIDNudcLyC8uhlpprM+wvH8qnxYO7RbR5dLq63d7lREYHuEDxypvWsxAATyuzRVm0W6UMI1uO2uRUrYhXpRRRAShzzU3hhQMoivUX2rakjLd5XLzcRXkY/qU1t5RVptCaOSMIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHooP/Ez0D/htlG8B0ya8Ggm4lSigBTKHZKsmnlG/ejdlBq6oiZzg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421402,
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
      "state": "tx_+NMLAfiEuEC7quTZhUF8/dtgaqJFO41GKMLR/l1QVkR/1WGKDMrRIDNudcLyC8uhlpprM+wvH8qnxYO7RbR5dLq63d7lREYHuEDxypvWsxAATyuzRVm0W6UMI1uO2uRUrYhXpRRRAShzzU3hhQMoivUX2rakjLd5XLzcRXkY/qU1t5RVptCaOSMIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHooP/Ez0D/htlG8B0ya8Ggm4lSigBTKHZKsmnlG/ejdlBq6oiZzg=="
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
      "state": "tx_+NMLAfiEuEC7quTZhUF8/dtgaqJFO41GKMLR/l1QVkR/1WGKDMrRIDNudcLyC8uhlpprM+wvH8qnxYO7RbR5dLq63d7lREYHuEDxypvWsxAATyuzRVm0W6UMI1uO2uRUrYhXpRRRAShzzU3hhQMoivUX2rakjLd5XLzcRXkY/qU1t5RVptCaOSMIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHooP/Ez0D/htlG8B0ya8Ggm4lSigBTKHZKsmnlG/ejdlBq6oiZzg=="
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
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": 232
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
        "round": 232
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 232
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 232
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": 232
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
      "caller_nonce": 232,
      "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
      "gas_price": 1,
      "gas_used": 165,
      "height": 232,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": 232
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
        "round": 232
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 232
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 232
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": 232
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
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 232,
      "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
      "gas_price": 1,
      "gas_used": 165,
      "height": 232,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 233,
      "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
      "gas_price": 1,
      "gas_used": 165,
      "height": 233,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgemgXqkVL16vRt2R05OqQGHpYdzyhW4E0GGynL3qzseugN+t+Nr9",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
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
  "id": -576460752303421401,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEAjBc1AagFimAqUyk3v42m/0mUdA7BXnak63U0KPRrygO5OSi8eVKx6YVcDfeQz/8t1Xg0LB6mDRVVOanyUcG0MuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHpoF6pFS9er0bdkdOTqkBh6WHc8oVuBNBhspy96s7HroDftKcf7g=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421401,
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
      "signed_tx": "tx_+JELAfhCuEAjBc1AagFimAqUyk3v42m/0mUdA7BXnak63U0KPRrygO5OSi8eVKx6YVcDfeQz/8t1Xg0LB6mDRVVOanyUcG0MuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHpoF6pFS9er0bdkdOTqkBh6WHc8oVuBNBhspy96s7HroDftKcf7g==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoDiegbERyA/dZV9Hexv0nNd5mxPjbfZRz87smiDME5EFVmGIECg=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
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
  "id": -576460752303421400,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAjBc1AagFimAqUyk3v42m/0mUdA7BXnak63U0KPRrygO5OSi8eVKx6YVcDfeQz/8t1Xg0LB6mDRVVOanyUcG0MuEDTZuszS8NbMsulLY6dY22Lb71ltDZ7v6QCnl6MbmTzWkGTKvvwkPRC9+PISPnAb60emq/rg9xOu5VCW65mCFYJuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHpoF6pFS9er0bdkdOTqkBh6WHc8oVuBNBhspy96s7HroDf6Vw2zA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421400,
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
      "state": "tx_+NMLAfiEuEAjBc1AagFimAqUyk3v42m/0mUdA7BXnak63U0KPRrygO5OSi8eVKx6YVcDfeQz/8t1Xg0LB6mDRVVOanyUcG0MuEDTZuszS8NbMsulLY6dY22Lb71ltDZ7v6QCnl6MbmTzWkGTKvvwkPRC9+PISPnAb60emq/rg9xOu5VCW65mCFYJuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHpoF6pFS9er0bdkdOTqkBh6WHc8oVuBNBhspy96s7HroDf6Vw2zA=="
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
      "state": "tx_+NMLAfiEuEAjBc1AagFimAqUyk3v42m/0mUdA7BXnak63U0KPRrygO5OSi8eVKx6YVcDfeQz/8t1Xg0LB6mDRVVOanyUcG0MuEDTZuszS8NbMsulLY6dY22Lb71ltDZ7v6QCnl6MbmTzWkGTKvvwkPRC9+PISPnAb60emq/rg9xOu5VCW65mCFYJuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHpoF6pFS9er0bdkdOTqkBh6WHc8oVuBNBhspy96s7HroDf6Vw2zA=="
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": 233
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
        "round": 233
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 233
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 233
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": 233
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
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 233,
      "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
      "gas_price": 1,
      "gas_used": 165,
      "height": 233,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
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
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": 233
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
        "round": 233
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 233
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 233
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
    "round": 233
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
      "caller_nonce": 233,
      "contract_id": "ct_2RPosfFKCFd4mTuLGiasrvmJ5dN15CHLBut6stbyZurVx4v2Av",
      "gas_price": 1,
      "gas_used": 165,
      "height": 233,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 234,
      "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
      "gas_price": 1,
      "gas_used": 11,
      "height": 234,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgeqgGwScswMk5M+ShZIx+XIcVNip7UanUS8aomirgsJJaKWC800y",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
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
  "id": -576460752303421399,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuECYcSCAOo4LqlWlI078hOQykjpGqFO80H/WbLto8LbOdoe+tSDoV/d3UyZouoOh2p+XBUuh7Dp6CxlTYImYWlEEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHqoBsEnLMDJOTPkoWSMflyHFTYqe1Gp1EvGqJoq4LCSWilaWIYvg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421399,
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
      "signed_tx": "tx_+JELAfhCuECYcSCAOo4LqlWlI078hOQykjpGqFO80H/WbLto8LbOdoe+tSDoV/d3UyZouoOh2p+XBUuh7Dp6CxlTYImYWlEEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHqoBsEnLMDJOTPkoWSMflyHFTYqe1Gp1EvGqJoq4LCSWilaWIYvg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
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
  "id": -576460752303421398,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAFM7UbK2TMtUH1Y4nHI0P+eZl2OTgEDS1UZ5C9jdteZnOqOYV0LL0i4+7rgrcI6ao3k5YgKc9TopEZ93sKRscFuECYcSCAOo4LqlWlI078hOQykjpGqFO80H/WbLto8LbOdoe+tSDoV/d3UyZouoOh2p+XBUuh7Dp6CxlTYImYWlEEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHqoBsEnLMDJOTPkoWSMflyHFTYqe1Gp1EvGqJoq4LCSWil8hDqXA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421398,
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
      "state": "tx_+NMLAfiEuEAFM7UbK2TMtUH1Y4nHI0P+eZl2OTgEDS1UZ5C9jdteZnOqOYV0LL0i4+7rgrcI6ao3k5YgKc9TopEZ93sKRscFuECYcSCAOo4LqlWlI078hOQykjpGqFO80H/WbLto8LbOdoe+tSDoV/d3UyZouoOh2p+XBUuh7Dp6CxlTYImYWlEEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHqoBsEnLMDJOTPkoWSMflyHFTYqe1Gp1EvGqJoq4LCSWil8hDqXA=="
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
      "state": "tx_+NMLAfiEuEAFM7UbK2TMtUH1Y4nHI0P+eZl2OTgEDS1UZ5C9jdteZnOqOYV0LL0i4+7rgrcI6ao3k5YgKc9TopEZ93sKRscFuECYcSCAOo4LqlWlI078hOQykjpGqFO80H/WbLto8LbOdoe+tSDoV/d3UyZouoOh2p+XBUuh7Dp6CxlTYImYWlEEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHqoBsEnLMDJOTPkoWSMflyHFTYqe1Gp1EvGqJoq4LCSWil8hDqXA=="
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
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 234
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": 234
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 234
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 234
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 234
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
      "caller_nonce": 234,
      "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
      "gas_price": 1,
      "gas_used": 11,
      "height": 234,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 234
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": 234
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 234
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 234
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 234
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
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 234,
      "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
      "gas_price": 1,
      "gas_used": 11,
      "height": 234,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 235,
      "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
      "gas_price": 1,
      "gas_used": 11,
      "height": 235,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Rgeug9tJizilocuZhHH5WeCTz7KmpMCvLD7U43qjRifsdvRQNbSA/",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
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
  "id": -576460752303421397,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEAubxiNgVinRzibkvMkdrCxIXsY/eNFrwwXOdUfKhisiYd37oSuNHMereHsv2OQqtbr1bJpsjVAgOp7ZGkLgyoJuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHroPbSYs4paHLmYRx+Vngk8+ypqTAryw+1ON6o0Yn7Hb0URor1CQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421397,
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
      "signed_tx": "tx_+JELAfhCuEAubxiNgVinRzibkvMkdrCxIXsY/eNFrwwXOdUfKhisiYd37oSuNHMereHsv2OQqtbr1bJpsjVAgOp7ZGkLgyoJuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHroPbSYs4paHLmYRx+Vngk8+ypqTAryw+1ON6o0Yn7Hb0URor1CQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
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
  "id": -576460752303421396,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAubxiNgVinRzibkvMkdrCxIXsY/eNFrwwXOdUfKhisiYd37oSuNHMereHsv2OQqtbr1bJpsjVAgOp7ZGkLgyoJuEDAfSk0+/d2AIjkFDdC28aS1h2ZTvwgnJVJN0unGNujTLgt3GZvt+1H9h0ptnPiW4WOip4AR23HX7EPf2acI8AJuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHroPbSYs4paHLmYRx+Vngk8+ypqTAryw+1ON6o0Yn7Hb0UfN7i2A=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421396,
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
      "state": "tx_+NMLAfiEuEAubxiNgVinRzibkvMkdrCxIXsY/eNFrwwXOdUfKhisiYd37oSuNHMereHsv2OQqtbr1bJpsjVAgOp7ZGkLgyoJuEDAfSk0+/d2AIjkFDdC28aS1h2ZTvwgnJVJN0unGNujTLgt3GZvt+1H9h0ptnPiW4WOip4AR23HX7EPf2acI8AJuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHroPbSYs4paHLmYRx+Vngk8+ypqTAryw+1ON6o0Yn7Hb0UfN7i2A=="
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
      "state": "tx_+NMLAfiEuEAubxiNgVinRzibkvMkdrCxIXsY/eNFrwwXOdUfKhisiYd37oSuNHMereHsv2OQqtbr1bJpsjVAgOp7ZGkLgyoJuEDAfSk0+/d2AIjkFDdC28aS1h2ZTvwgnJVJN0unGNujTLgt3GZvt+1H9h0ptnPiW4WOip4AR23HX7EPf2acI8AJuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHroPbSYs4paHLmYRx+Vngk8+ypqTAryw+1ON6o0Yn7Hb0UfN7i2A=="
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 235
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": 235
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 235
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 235
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 235
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
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 235,
      "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
      "gas_price": 1,
      "gas_used": 11,
      "height": 235,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
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
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 235
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
        "round": 235
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 235
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 235
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
    "round": 235
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
      "caller_nonce": 235,
      "contract_id": "ct_RwG7iFWsiK8sa9hs2dKjy4jKxbit1L6yxhXpLBxd5WPT4tgBP",
      "gas_price": 1,
      "gas_used": 11,
      "height": 235,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
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
    "deposit": "1",
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfP4oEp9E=",
        "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
        "deposit": "1",
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
    "vm_version": "1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfP4oEp9E=",
        "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
        "deposit": 10,
        "vm_version": "1"
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
    "abi_version": "1",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": "1",
        "call_data": "cb_KxFE1kQfP4oEp9E=",
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgeygT1jerGj8g8eq84iIx/69OZ0bnLsRJW1iiy2mX8lhJuozGmVX",
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
  "id": -576460752303421395,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuED8OUJdNTD3aIyKRBLkLyPZhgn0zaugvkPR1PNWggeDuenUUsBsDyN0ilOZe8bCFaQjE0FVIQHPU01ytVlmGW8FuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHsoE9Y3qxo/IPHqvOIiMf+vTmdG5y7ESVtYostpl/JYSbqCpwnaQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421395,
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
      "signed_tx": "tx_+JELAfhCuED8OUJdNTD3aIyKRBLkLyPZhgn0zaugvkPR1PNWggeDuenUUsBsDyN0ilOZe8bCFaQjE0FVIQHPU01ytVlmGW8FuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHsoE9Y3qxo/IPHqvOIiMf+vTmdG5y7ESVtYostpl/JYSbqCpwnaQ==",
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
  "id": -576460752303421394,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAclM4G+/zLie+F5uhAAhDR9UJpn1luIPgkZ0xSbHHA6dPwpJ1Z+Oez+cwC7EHmJMuDQHLGucJJPUJM4E7/sgALuED8OUJdNTD3aIyKRBLkLyPZhgn0zaugvkPR1PNWggeDuenUUsBsDyN0ilOZe8bCFaQjE0FVIQHPU01ytVlmGW8FuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHsoE9Y3qxo/IPHqvOIiMf+vTmdG5y7ESVtYostpl/JYSbqZ5v01w=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421394,
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
      "state": "tx_+NMLAfiEuEAclM4G+/zLie+F5uhAAhDR9UJpn1luIPgkZ0xSbHHA6dPwpJ1Z+Oez+cwC7EHmJMuDQHLGucJJPUJM4E7/sgALuED8OUJdNTD3aIyKRBLkLyPZhgn0zaugvkPR1PNWggeDuenUUsBsDyN0ilOZe8bCFaQjE0FVIQHPU01ytVlmGW8FuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHsoE9Y3qxo/IPHqvOIiMf+vTmdG5y7ESVtYostpl/JYSbqZ5v01w=="
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
      "state": "tx_+NMLAfiEuEAclM4G+/zLie+F5uhAAhDR9UJpn1luIPgkZ0xSbHHA6dPwpJ1Z+Oez+cwC7EHmJMuDQHLGucJJPUJM4E7/sgALuED8OUJdNTD3aIyKRBLkLyPZhgn0zaugvkPR1PNWggeDuenUUsBsDyN0ilOZe8bCFaQjE0FVIQHPU01ytVlmGW8FuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHsoE9Y3qxo/IPHqvOIiMf+vTmdG5y7ESVtYostpl/JYSbqZ5v01w=="
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
    "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
    "deposit": "1",
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfP4oEp9E=",
        "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
        "deposit": "1",
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
    "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
    "deposit": 10,
    "vm_version": "1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfP4oEp9E=",
        "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
        "deposit": 10,
        "vm_version": "1"
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
    "abi_version": "1",
    "call_data": "cb_KxFE1kQfP4oEp9E=",
    "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": "1",
        "call_data": "cb_KxFE1kQfP4oEp9E=",
        "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
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
    "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Rge2gCWZMTmopjT1CVJTPnySHd+1mP6S4AhSvypoKadtP0yTEtAbL",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
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
  "id": -576460752303421393,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuECiFBjrg+e21OVuXLAbmZx9DP2scm8aKOaDdIC+gxE19/OvN/rNbUn4jN+RvKROcnpFFPYoNg2dPjgqYLnYuEIAuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHtoAlmTE5qKY09QlSUz58kh3ftZj+kuAIUr8qaCmnbT9MkDRI96Q=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421393,
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
      "signed_tx": "tx_+JELAfhCuECiFBjrg+e21OVuXLAbmZx9DP2scm8aKOaDdIC+gxE19/OvN/rNbUn4jN+RvKROcnpFFPYoNg2dPjgqYLnYuEIAuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHtoAlmTE5qKY09QlSUz58kh3ftZj+kuAIUr8qaCmnbT9MkDRI96Q==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
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
  "id": -576460752303421392,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuECiFBjrg+e21OVuXLAbmZx9DP2scm8aKOaDdIC+gxE19/OvN/rNbUn4jN+RvKROcnpFFPYoNg2dPjgqYLnYuEIAuEDnvo1JhpT2cDGPlCZsent9jhCs7gMwg5BIgMm26TFPgDjQQH09QklJih5UfGUQvka7cI8X1pgHAEQ3kbo09PAPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHtoAlmTE5qKY09QlSUz58kh3ftZj+kuAIUr8qaCmnbT9MkNre4aA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421392,
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
      "state": "tx_+NMLAfiEuECiFBjrg+e21OVuXLAbmZx9DP2scm8aKOaDdIC+gxE19/OvN/rNbUn4jN+RvKROcnpFFPYoNg2dPjgqYLnYuEIAuEDnvo1JhpT2cDGPlCZsent9jhCs7gMwg5BIgMm26TFPgDjQQH09QklJih5UfGUQvka7cI8X1pgHAEQ3kbo09PAPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHtoAlmTE5qKY09QlSUz58kh3ftZj+kuAIUr8qaCmnbT9MkNre4aA=="
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
      "state": "tx_+NMLAfiEuECiFBjrg+e21OVuXLAbmZx9DP2scm8aKOaDdIC+gxE19/OvN/rNbUn4jN+RvKROcnpFFPYoNg2dPjgqYLnYuEIAuEDnvo1JhpT2cDGPlCZsent9jhCs7gMwg5BIgMm26TFPgDjQQH09QklJih5UfGUQvka7cI8X1pgHAEQ3kbo09PAPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHtoAlmTE5qKY09QlSUz58kh3ftZj+kuAIUr8qaCmnbT9MkNre4aA=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 238,
      "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
      "gas_price": 1,
      "gas_used": 11,
      "height": 238,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Rge6gGOPwmOr4jed/9+c028XoKUEOUqy2AhffHZ+Cu4Ny1DH8jO4S",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
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
  "id": -576460752303421391,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEASPz5Y4eqANKnCPaUB7xiVe7HiWzHLb+rbCbO0e1bMOEOisDMgHJga6ndNaX1ZiamkY0lwKM82aLzOKPu4QNUGuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHuoBjj8Jjq+I3nf/fnNNvF6ClBDlKstgIX3x2fgruDctQxhxOikQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421391,
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
      "signed_tx": "tx_+JELAfhCuEASPz5Y4eqANKnCPaUB7xiVe7HiWzHLb+rbCbO0e1bMOEOisDMgHJga6ndNaX1ZiamkY0lwKM82aLzOKPu4QNUGuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHuoBjj8Jjq+I3nf/fnNNvF6ClBDlKstgIX3x2fgruDctQxhxOikQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
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
  "id": -576460752303421390,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEASPz5Y4eqANKnCPaUB7xiVe7HiWzHLb+rbCbO0e1bMOEOisDMgHJga6ndNaX1ZiamkY0lwKM82aLzOKPu4QNUGuEDP6j30p3pMmMphF++v1eczNBgCt2BewQ80+dhXP2njvjqRQGc8zy6f0bE98M4Y5bh6w+dXpkV9JfVQ5qBJ1+gFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHuoBjj8Jjq+I3nf/fnNNvF6ClBDlKstgIX3x2fgruDctQxYAyDQw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421390,
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
      "state": "tx_+NMLAfiEuEASPz5Y4eqANKnCPaUB7xiVe7HiWzHLb+rbCbO0e1bMOEOisDMgHJga6ndNaX1ZiamkY0lwKM82aLzOKPu4QNUGuEDP6j30p3pMmMphF++v1eczNBgCt2BewQ80+dhXP2njvjqRQGc8zy6f0bE98M4Y5bh6w+dXpkV9JfVQ5qBJ1+gFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHuoBjj8Jjq+I3nf/fnNNvF6ClBDlKstgIX3x2fgruDctQxYAyDQw=="
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
      "state": "tx_+NMLAfiEuEASPz5Y4eqANKnCPaUB7xiVe7HiWzHLb+rbCbO0e1bMOEOisDMgHJga6ndNaX1ZiamkY0lwKM82aLzOKPu4QNUGuEDP6j30p3pMmMphF++v1eczNBgCt2BewQ80+dhXP2njvjqRQGc8zy6f0bE98M4Y5bh6w+dXpkV9JfVQ5qBJ1+gFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHuoBjj8Jjq+I3nf/fnNNvF6ClBDlKstgIX3x2fgruDctQxYAyDQw=="
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 238
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": 238
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 238
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 238
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 238
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
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 238,
      "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
      "gas_price": 1,
      "gas_used": 11,
      "height": 238,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
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
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 238
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": 238
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 238
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 238
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 238
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
      "caller_nonce": 238,
      "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
      "gas_price": 1,
      "gas_used": 11,
      "height": 238,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 239,
      "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
      "gas_price": 1,
      "gas_used": 11,
      "height": 239,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Rge+g0eyfLQoiOn1pXg2wd6t2f/ZWN5v62g4gbZJqTZZzvFnrPncT",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
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
  "id": -576460752303421389,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEDX3fuN1jjhOA4H4KbSCBW73iDbhnoU3rYetynKnZNc2iQqjeFRKC5Vrp/RYq/nhLnoRpzgB3PupWQmH6KB0NcFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHvoNHsny0KIjp9aV4NsHerdn/2Vjeb+toOIG2Sak2Wc7xZD3cJig=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421389,
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
      "signed_tx": "tx_+JELAfhCuEDX3fuN1jjhOA4H4KbSCBW73iDbhnoU3rYetynKnZNc2iQqjeFRKC5Vrp/RYq/nhLnoRpzgB3PupWQmH6KB0NcFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHvoNHsny0KIjp9aV4NsHerdn/2Vjeb+toOIG2Sak2Wc7xZD3cJig==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
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
  "id": -576460752303421388,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEBqiGT+BIMWjTlljBJCsLE6Ohil2dPsv+Dnb5jDtITAJzJM1oQUT+zFlcAQoLJ+uFUWc7D/X7wQdcSkObveJ/8MuEDX3fuN1jjhOA4H4KbSCBW73iDbhnoU3rYetynKnZNc2iQqjeFRKC5Vrp/RYq/nhLnoRpzgB3PupWQmH6KB0NcFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHvoNHsny0KIjp9aV4NsHerdn/2Vjeb+toOIG2Sak2Wc7xZLjeTSA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421388,
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
      "state": "tx_+NMLAfiEuEBqiGT+BIMWjTlljBJCsLE6Ohil2dPsv+Dnb5jDtITAJzJM1oQUT+zFlcAQoLJ+uFUWc7D/X7wQdcSkObveJ/8MuEDX3fuN1jjhOA4H4KbSCBW73iDbhnoU3rYetynKnZNc2iQqjeFRKC5Vrp/RYq/nhLnoRpzgB3PupWQmH6KB0NcFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHvoNHsny0KIjp9aV4NsHerdn/2Vjeb+toOIG2Sak2Wc7xZLjeTSA=="
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
      "state": "tx_+NMLAfiEuEBqiGT+BIMWjTlljBJCsLE6Ohil2dPsv+Dnb5jDtITAJzJM1oQUT+zFlcAQoLJ+uFUWc7D/X7wQdcSkObveJ/8MuEDX3fuN1jjhOA4H4KbSCBW73iDbhnoU3rYetynKnZNc2iQqjeFRKC5Vrp/RYq/nhLnoRpzgB3PupWQmH6KB0NcFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHvoNHsny0KIjp9aV4NsHerdn/2Vjeb+toOIG2Sak2Wc7xZLjeTSA=="
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
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 239
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": 239
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 239
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 239
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 239
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
      "caller_nonce": 239,
      "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
      "gas_price": 1,
      "gas_used": 11,
      "height": 239,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 239
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": 239
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 239
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 239
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 239
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
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 239,
      "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
      "gas_price": 1,
      "gas_used": 11,
      "height": 239,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 240,
      "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
      "gas_price": 1,
      "gas_used": 11,
      "height": 240,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgfCg4wAKWCSab+G3KwR/MMzRv7CoV6NA06caCDiKkv1fd8wUgAYz",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
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
  "id": -576460752303421387,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEC/krNdoFneurbqWFznQXQpAROUZZgUjk+mtdpb8f3Wf6zjAptCQ04jN0uxHDFLuHwFU2yaQF0Qsyzm1BxiaiEDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHwoOMAClgkmm/htysEfzDM0b+wqFejQNOnGgg4ipL9X3fM1wKP4g=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421387,
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
      "signed_tx": "tx_+JELAfhCuEC/krNdoFneurbqWFznQXQpAROUZZgUjk+mtdpb8f3Wf6zjAptCQ04jN0uxHDFLuHwFU2yaQF0Qsyzm1BxiaiEDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHwoOMAClgkmm/htysEfzDM0b+wqFejQNOnGgg4ipL9X3fM1wKP4g==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
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
  "id": -576460752303421386,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuECCh0HG/Haa+ZIsYCIGvlDAZUjKtYZXCWRcINnuf2g2XkEAK/J47YohvogEbiouKcJcn5Zby7TxjYmEVm3pOY4GuEC/krNdoFneurbqWFznQXQpAROUZZgUjk+mtdpb8f3Wf6zjAptCQ04jN0uxHDFLuHwFU2yaQF0Qsyzm1BxiaiEDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHwoOMAClgkmm/htysEfzDM0b+wqFejQNOnGgg4ipL9X3fMcEmhyQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421386,
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
      "state": "tx_+NMLAfiEuECCh0HG/Haa+ZIsYCIGvlDAZUjKtYZXCWRcINnuf2g2XkEAK/J47YohvogEbiouKcJcn5Zby7TxjYmEVm3pOY4GuEC/krNdoFneurbqWFznQXQpAROUZZgUjk+mtdpb8f3Wf6zjAptCQ04jN0uxHDFLuHwFU2yaQF0Qsyzm1BxiaiEDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHwoOMAClgkmm/htysEfzDM0b+wqFejQNOnGgg4ipL9X3fMcEmhyQ=="
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
      "state": "tx_+NMLAfiEuECCh0HG/Haa+ZIsYCIGvlDAZUjKtYZXCWRcINnuf2g2XkEAK/J47YohvogEbiouKcJcn5Zby7TxjYmEVm3pOY4GuEC/krNdoFneurbqWFznQXQpAROUZZgUjk+mtdpb8f3Wf6zjAptCQ04jN0uxHDFLuHwFU2yaQF0Qsyzm1BxiaiEDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHwoOMAClgkmm/htysEfzDM0b+wqFejQNOnGgg4ipL9X3fMcEmhyQ=="
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 240
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": 240
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 240
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 240
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 240
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
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 240,
      "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
      "gas_price": 1,
      "gas_used": 11,
      "height": 240,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
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
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 240
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": 240
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 240
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 240
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 240
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
      "caller_nonce": 240,
      "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
      "gas_price": 1,
      "gas_used": 11,
      "height": 240,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 241,
      "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
      "gas_price": 1,
      "gas_used": 11,
      "height": 241,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgfGgAj0/DLT5HuaQ4+VZnodmfu7/1MT4H+1DDKelzSvHk+BuyCWH",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
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
  "id": -576460752303421385,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuECqv2zYcl75h/EvSeHhakX+yCqVx648/QDHs9cQz6a2DBPWrZq8eK60MaEViNbV+2X5vt+zLIY+txsJ50xEAxMDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHxoAI9Pwy0+R7mkOPlWZ6HZn7u/9TE+B/tQwynpc0rx5PgdaCXWQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421385,
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
      "signed_tx": "tx_+JELAfhCuECqv2zYcl75h/EvSeHhakX+yCqVx648/QDHs9cQz6a2DBPWrZq8eK60MaEViNbV+2X5vt+zLIY+txsJ50xEAxMDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHxoAI9Pwy0+R7mkOPlWZ6HZn7u/9TE+B/tQwynpc0rx5PgdaCXWQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
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
  "id": -576460752303421384,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEASz0UEM+P62O8JCDt3AAT4h7M0hdh1Xif+4PAixwkTF1nFlyqNFVvSzuV8Pe/c0/SwmkqtRFJROVa+QhWe1EQGuECqv2zYcl75h/EvSeHhakX+yCqVx648/QDHs9cQz6a2DBPWrZq8eK60MaEViNbV+2X5vt+zLIY+txsJ50xEAxMDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHxoAI9Pwy0+R7mkOPlWZ6HZn7u/9TE+B/tQwynpc0rx5PgfvKREA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421384,
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
      "state": "tx_+NMLAfiEuEASz0UEM+P62O8JCDt3AAT4h7M0hdh1Xif+4PAixwkTF1nFlyqNFVvSzuV8Pe/c0/SwmkqtRFJROVa+QhWe1EQGuECqv2zYcl75h/EvSeHhakX+yCqVx648/QDHs9cQz6a2DBPWrZq8eK60MaEViNbV+2X5vt+zLIY+txsJ50xEAxMDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHxoAI9Pwy0+R7mkOPlWZ6HZn7u/9TE+B/tQwynpc0rx5PgfvKREA=="
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
      "state": "tx_+NMLAfiEuEASz0UEM+P62O8JCDt3AAT4h7M0hdh1Xif+4PAixwkTF1nFlyqNFVvSzuV8Pe/c0/SwmkqtRFJROVa+QhWe1EQGuECqv2zYcl75h/EvSeHhakX+yCqVx648/QDHs9cQz6a2DBPWrZq8eK60MaEViNbV+2X5vt+zLIY+txsJ50xEAxMDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHxoAI9Pwy0+R7mkOPlWZ6HZn7u/9TE+B/tQwynpc0rx5PgfvKREA=="
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
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 241
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": 241
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 241
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 241
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 241
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
      "caller_nonce": 241,
      "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
      "gas_price": 1,
      "gas_used": 11,
      "height": 241,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 241
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": 241
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 241
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 241
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 241
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
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 241,
      "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
      "gas_price": 1,
      "gas_used": 11,
      "height": 241,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 242,
      "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
      "gas_price": 1,
      "gas_used": 165,
      "height": 242,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgfKgE58yrx5ZGrOHEdqxDGMk+5E0m80BG8/agVHLdeXwiUAH0CZ5",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
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
  "id": -576460752303421383,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEDK75Y5jL29NHHibbRvDJji+HJySkLbVqBKmKPwNRCGM1mKB+TedszrQdxb4kvEe+mU6bvK6B7dciFlkff8yScMuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHyoBOfMq8eWRqzhxHasQxjJPuRNJvNARvP2oFRy3Xl8IlANY3lnw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421383,
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
      "signed_tx": "tx_+JELAfhCuEDK75Y5jL29NHHibbRvDJji+HJySkLbVqBKmKPwNRCGM1mKB+TedszrQdxb4kvEe+mU6bvK6B7dciFlkff8yScMuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHyoBOfMq8eWRqzhxHasQxjJPuRNJvNARvP2oFRy3Xl8IlANY3lnw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
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
  "id": -576460752303421382,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEDK75Y5jL29NHHibbRvDJji+HJySkLbVqBKmKPwNRCGM1mKB+TedszrQdxb4kvEe+mU6bvK6B7dciFlkff8yScMuEDVw8YqqImoMEbgzyYW5d5OecC10tWPVETgLkRUGQHaZoQ5ESm3TnE8PynkXPlk6cipdBPt88phiwGmidFxdCYNuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHyoBOfMq8eWRqzhxHasQxjJPuRNJvNARvP2oFRy3Xl8IlALu8OPw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421382,
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
      "state": "tx_+NMLAfiEuEDK75Y5jL29NHHibbRvDJji+HJySkLbVqBKmKPwNRCGM1mKB+TedszrQdxb4kvEe+mU6bvK6B7dciFlkff8yScMuEDVw8YqqImoMEbgzyYW5d5OecC10tWPVETgLkRUGQHaZoQ5ESm3TnE8PynkXPlk6cipdBPt88phiwGmidFxdCYNuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHyoBOfMq8eWRqzhxHasQxjJPuRNJvNARvP2oFRy3Xl8IlALu8OPw=="
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
      "state": "tx_+NMLAfiEuEDK75Y5jL29NHHibbRvDJji+HJySkLbVqBKmKPwNRCGM1mKB+TedszrQdxb4kvEe+mU6bvK6B7dciFlkff8yScMuEDVw8YqqImoMEbgzyYW5d5OecC10tWPVETgLkRUGQHaZoQ5ESm3TnE8PynkXPlk6cipdBPt88phiwGmidFxdCYNuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHyoBOfMq8eWRqzhxHasQxjJPuRNJvNARvP2oFRy3Xl8IlALu8OPw=="
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": 242
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
        "round": 242
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 242
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 242
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": 242
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
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 242,
      "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
      "gas_price": 1,
      "gas_used": 165,
      "height": 242,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
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
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": 242
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
        "round": 242
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 242
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 242
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": 242
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
      "caller_nonce": 242,
      "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
      "gas_price": 1,
      "gas_used": 165,
      "height": 242,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 243,
      "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
      "gas_price": 1,
      "gas_used": 165,
      "height": 243,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgfOg1pMN3n8HdtIaRrloBNYpvJuUxE4SkH9t5h0GXjo3SugVNiGW",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
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
  "id": -576460752303421381,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEAESHwJmLgtkELzEwX8XJGvGiw5/QxyBgtnG7OyR0KnMfb8yFQRUgAvDkXnxjkl8fNd0g7KYZ8V+EfkzP4tbAwHuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHzoNaTDd5/B3bSGka5aATWKbyblMROEpB/beYdBl46N0roPVbgZQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421381,
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
      "signed_tx": "tx_+JELAfhCuEAESHwJmLgtkELzEwX8XJGvGiw5/QxyBgtnG7OyR0KnMfb8yFQRUgAvDkXnxjkl8fNd0g7KYZ8V+EfkzP4tbAwHuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHzoNaTDd5/B3bSGka5aATWKbyblMROEpB/beYdBl46N0roPVbgZQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VJ8yVJQ=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
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
  "id": -576460752303421380,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAESHwJmLgtkELzEwX8XJGvGiw5/QxyBgtnG7OyR0KnMfb8yFQRUgAvDkXnxjkl8fNd0g7KYZ8V+EfkzP4tbAwHuEC3lfJ3SpJHxV+tFx7UteZcFz+Ncbykgxn2Aw/eLV9mV8asoi5whbqRu8X4z7+X0ivvyXQczhBSgDcU5Ja3TaMJuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHzoNaTDd5/B3bSGka5aATWKbyblMROEpB/beYdBl46N0roq49lvQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421380,
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
      "state": "tx_+NMLAfiEuEAESHwJmLgtkELzEwX8XJGvGiw5/QxyBgtnG7OyR0KnMfb8yFQRUgAvDkXnxjkl8fNd0g7KYZ8V+EfkzP4tbAwHuEC3lfJ3SpJHxV+tFx7UteZcFz+Ncbykgxn2Aw/eLV9mV8asoi5whbqRu8X4z7+X0ivvyXQczhBSgDcU5Ja3TaMJuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHzoNaTDd5/B3bSGka5aATWKbyblMROEpB/beYdBl46N0roq49lvQ=="
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
      "state": "tx_+NMLAfiEuEAESHwJmLgtkELzEwX8XJGvGiw5/QxyBgtnG7OyR0KnMfb8yFQRUgAvDkXnxjkl8fNd0g7KYZ8V+EfkzP4tbAwHuEC3lfJ3SpJHxV+tFx7UteZcFz+Ncbykgxn2Aw/eLV9mV8asoi5whbqRu8X4z7+X0ivvyXQczhBSgDcU5Ja3TaMJuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYHzoNaTDd5/B3bSGka5aATWKbyblMROEpB/beYdBl46N0roq49lvQ=="
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
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": 243
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
        "round": 243
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 243
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 243
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": 243
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
      "caller_nonce": 243,
      "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
      "gas_price": 1,
      "gas_used": 165,
      "height": 243,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": 243
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
        "round": 243
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 243
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 243
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": 243
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
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 243,
      "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
      "gas_price": 1,
      "gas_used": 165,
      "height": 243,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 244,
      "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
      "gas_price": 1,
      "gas_used": 165,
      "height": 244,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgfSgirIyhtx9+LwgLwcLQu0Us/FRf8LKzZ1ATl1Dc7LvpgVmH7n/",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
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
  "id": -576460752303421379,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEDtL063UiIaOqos9AMnPwPmuJGN1Y7IVP2lyypj8FcLE3LIHco6C2gD8vTooHqMk43pv+QEhWk0deo6mUIXpFgFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH0oIqyMobcffi8IC8HC0LtFLPxUX/Cys2dQE5dQ3Oy76YFH414mA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421379,
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
      "signed_tx": "tx_+JELAfhCuEDtL063UiIaOqos9AMnPwPmuJGN1Y7IVP2lyypj8FcLE3LIHco6C2gD8vTooHqMk43pv+QEhWk0deo6mUIXpFgFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH0oIqyMobcffi8IC8HC0LtFLPxUX/Cys2dQE5dQ3Oy76YFH414mA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
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
  "id": -576460752303421378,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAHckc1lOFrgksSygx0MN3qSyqxL/RkxTGxuAna5A5Ip2DPdKSMjBm6PWgIxD6HBkiUFM4b3igDkrw6fZvrKS4CuEDtL063UiIaOqos9AMnPwPmuJGN1Y7IVP2lyypj8FcLE3LIHco6C2gD8vTooHqMk43pv+QEhWk0deo6mUIXpFgFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH0oIqyMobcffi8IC8HC0LtFLPxUX/Cys2dQE5dQ3Oy76YFRFmwoQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421378,
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
      "state": "tx_+NMLAfiEuEAHckc1lOFrgksSygx0MN3qSyqxL/RkxTGxuAna5A5Ip2DPdKSMjBm6PWgIxD6HBkiUFM4b3igDkrw6fZvrKS4CuEDtL063UiIaOqos9AMnPwPmuJGN1Y7IVP2lyypj8FcLE3LIHco6C2gD8vTooHqMk43pv+QEhWk0deo6mUIXpFgFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH0oIqyMobcffi8IC8HC0LtFLPxUX/Cys2dQE5dQ3Oy76YFRFmwoQ=="
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
      "state": "tx_+NMLAfiEuEAHckc1lOFrgksSygx0MN3qSyqxL/RkxTGxuAna5A5Ip2DPdKSMjBm6PWgIxD6HBkiUFM4b3igDkrw6fZvrKS4CuEDtL063UiIaOqos9AMnPwPmuJGN1Y7IVP2lyypj8FcLE3LIHco6C2gD8vTooHqMk43pv+QEhWk0deo6mUIXpFgFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH0oIqyMobcffi8IC8HC0LtFLPxUX/Cys2dQE5dQ3Oy76YFRFmwoQ=="
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": 244
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
        "round": 244
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 244
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 244
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": 244
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
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 244,
      "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
      "gas_price": 1,
      "gas_used": 165,
      "height": 244,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
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
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": 244
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
        "round": 244
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 244
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 244
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": 244
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
      "caller_nonce": 244,
      "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
      "gas_price": 1,
      "gas_used": 165,
      "height": 244,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 245,
      "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
      "gas_price": 1,
      "gas_used": 165,
      "height": 245,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgfWgV7mhxnq8mSOQWoHCaSCgh4TNWyyEHxV5ii9gqVhz4S3baSs+",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
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
  "id": -576460752303421377,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEAuReAOZFnJmzf2qiUAz0AwMSpVx/9b0/I4kp4Pi1WXaYw+D0U052hcwg8OiBXArX93zPcJtnWeDKH9RzWZYzgEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH1oFe5ocZ6vJkjkFqBwmkgoIeEzVsshB8VeYovYKlYc+EtBxuQPw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421377,
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
      "signed_tx": "tx_+JELAfhCuEAuReAOZFnJmzf2qiUAz0AwMSpVx/9b0/I4kp4Pi1WXaYw+D0U052hcwg8OiBXArX93zPcJtnWeDKH9RzWZYzgEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH1oFe5ocZ6vJkjkFqBwmkgoIeEzVsshB8VeYovYKlYc+EtBxuQPw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoHIaIRMMHwsRAfJmk9MU3RMc2rF4mIJTsuBBSYPUG+i7VrsPXYc=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
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
  "id": -576460752303421376,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAuReAOZFnJmzf2qiUAz0AwMSpVx/9b0/I4kp4Pi1WXaYw+D0U052hcwg8OiBXArX93zPcJtnWeDKH9RzWZYzgEuECRbk9qdAPRM6755cMODWR9ag/o/qnxfPAwh2OHY9pBPpwfVPG1ANIvZxEIiWdzwQM14+R441tSY6wVRBZHWpcJuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH1oFe5ocZ6vJkjkFqBwmkgoIeEzVsshB8VeYovYKlYc+EtC4rDCw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421376,
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
      "state": "tx_+NMLAfiEuEAuReAOZFnJmzf2qiUAz0AwMSpVx/9b0/I4kp4Pi1WXaYw+D0U052hcwg8OiBXArX93zPcJtnWeDKH9RzWZYzgEuECRbk9qdAPRM6755cMODWR9ag/o/qnxfPAwh2OHY9pBPpwfVPG1ANIvZxEIiWdzwQM14+R441tSY6wVRBZHWpcJuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH1oFe5ocZ6vJkjkFqBwmkgoIeEzVsshB8VeYovYKlYc+EtC4rDCw=="
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
      "state": "tx_+NMLAfiEuEAuReAOZFnJmzf2qiUAz0AwMSpVx/9b0/I4kp4Pi1WXaYw+D0U052hcwg8OiBXArX93zPcJtnWeDKH9RzWZYzgEuECRbk9qdAPRM6755cMODWR9ag/o/qnxfPAwh2OHY9pBPpwfVPG1ANIvZxEIiWdzwQM14+R441tSY6wVRBZHWpcJuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH1oFe5ocZ6vJkjkFqBwmkgoIeEzVsshB8VeYovYKlYc+EtC4rDCw=="
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
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": 245
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
        "round": 245
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 245
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 245
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": 245
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
      "caller_nonce": 245,
      "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
      "gas_price": 1,
      "gas_used": 165,
      "height": 245,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": 245
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
        "round": 245
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 245
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 245
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
    "round": 245
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
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 245,
      "contract_id": "ct_fBjhYCxRNQHwKkwqG6j8wwyZ1wn341YYDfPB8wSpfGdCbvrRh",
      "gas_price": 1,
      "gas_used": 165,
      "height": 245,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 246,
      "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
      "gas_price": 1,
      "gas_used": 11,
      "height": 246,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Rgfag+PXQtofMXCfMt1bRYoglPIVU734iStCBmPq4WHsuYaF2LIIm",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
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
  "id": -576460752303421375,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEByHeM08uGGm5u6/7Ro7d21bpHqeBaDcL8el88O4TSZQlYANKOogo9V9rOBtwlV8o6iDK/v1DJxNxggqzjoZTEDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH2oPj10LaHzFwnzLdW0WKIJTyFVO9+IkrQgZj6uFh7LmGhKyDGow=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421375,
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
      "signed_tx": "tx_+JELAfhCuEByHeM08uGGm5u6/7Ro7d21bpHqeBaDcL8el88O4TSZQlYANKOogo9V9rOBtwlV8o6iDK/v1DJxNxggqzjoZTEDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH2oPj10LaHzFwnzLdW0WKIJTyFVO9+IkrQgZj6uFh7LmGhKyDGow==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
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
  "id": -576460752303421374,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEBwG7tq/0nTJN6N8enZePXL4k+k3W3zSo9roykCvAzD6PT6HSmAgEhfDVlKUH4KNyn/zAUOKtLcVncHxe8qvdEMuEByHeM08uGGm5u6/7Ro7d21bpHqeBaDcL8el88O4TSZQlYANKOogo9V9rOBtwlV8o6iDK/v1DJxNxggqzjoZTEDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH2oPj10LaHzFwnzLdW0WKIJTyFVO9+IkrQgZj6uFh7LmGhGJABXw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421374,
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
      "state": "tx_+NMLAfiEuEBwG7tq/0nTJN6N8enZePXL4k+k3W3zSo9roykCvAzD6PT6HSmAgEhfDVlKUH4KNyn/zAUOKtLcVncHxe8qvdEMuEByHeM08uGGm5u6/7Ro7d21bpHqeBaDcL8el88O4TSZQlYANKOogo9V9rOBtwlV8o6iDK/v1DJxNxggqzjoZTEDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH2oPj10LaHzFwnzLdW0WKIJTyFVO9+IkrQgZj6uFh7LmGhGJABXw=="
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
      "state": "tx_+NMLAfiEuEBwG7tq/0nTJN6N8enZePXL4k+k3W3zSo9roykCvAzD6PT6HSmAgEhfDVlKUH4KNyn/zAUOKtLcVncHxe8qvdEMuEByHeM08uGGm5u6/7Ro7d21bpHqeBaDcL8el88O4TSZQlYANKOogo9V9rOBtwlV8o6iDK/v1DJxNxggqzjoZTEDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH2oPj10LaHzFwnzLdW0WKIJTyFVO9+IkrQgZj6uFh7LmGhGJABXw=="
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 246
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": 246
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 246
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 246
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 246
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
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 246,
      "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
      "gas_price": 1,
      "gas_used": 11,
      "height": 246,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
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
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 246
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": 246
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 246
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 246
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 246
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
      "caller_nonce": 246,
      "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
      "gas_price": 1,
      "gas_used": 11,
      "height": 246,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 247,
      "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
      "gas_price": 1,
      "gas_used": 11,
      "height": 247,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Rgfegzm+nn4pRMhOedJvL30XAPFIxz07DdaMKq9ksOEUL5wzCvhEE",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
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
  "id": -576460752303421373,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEB7AZeYRP7du3rWJI86e4CJkrrIaIV5KOcn1M5LKPv7WokyPmGvnRZ8oUtHoaDl/W7KsKvozxR4ChoK9RUfj9cCuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH3oM5vp5+KUTITnnSby99FwDxSMc9Ow3WjCqvZLDhFC+cM4diuYQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421373,
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
      "signed_tx": "tx_+JELAfhCuEB7AZeYRP7du3rWJI86e4CJkrrIaIV5KOcn1M5LKPv7WokyPmGvnRZ8oUtHoaDl/W7KsKvozxR4ChoK9RUfj9cCuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH3oM5vp5+KUTITnnSby99FwDxSMc9Ow3WjCqvZLDhFC+cM4diuYQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
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
  "id": -576460752303421372,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEBR0WWWmDznKBlXoZ8q1tWYy1LGAZ8hMibNWRJfkb9eJQSSnbvnUFljr1rqAVx+dACYZmPx+BpsdeR4C+r7F8sGuEB7AZeYRP7du3rWJI86e4CJkrrIaIV5KOcn1M5LKPv7WokyPmGvnRZ8oUtHoaDl/W7KsKvozxR4ChoK9RUfj9cCuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH3oM5vp5+KUTITnnSby99FwDxSMc9Ow3WjCqvZLDhFC+cMUYMfzA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421372,
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
      "state": "tx_+NMLAfiEuEBR0WWWmDznKBlXoZ8q1tWYy1LGAZ8hMibNWRJfkb9eJQSSnbvnUFljr1rqAVx+dACYZmPx+BpsdeR4C+r7F8sGuEB7AZeYRP7du3rWJI86e4CJkrrIaIV5KOcn1M5LKPv7WokyPmGvnRZ8oUtHoaDl/W7KsKvozxR4ChoK9RUfj9cCuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH3oM5vp5+KUTITnnSby99FwDxSMc9Ow3WjCqvZLDhFC+cMUYMfzA=="
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
      "state": "tx_+NMLAfiEuEBR0WWWmDznKBlXoZ8q1tWYy1LGAZ8hMibNWRJfkb9eJQSSnbvnUFljr1rqAVx+dACYZmPx+BpsdeR4C+r7F8sGuEB7AZeYRP7du3rWJI86e4CJkrrIaIV5KOcn1M5LKPv7WokyPmGvnRZ8oUtHoaDl/W7KsKvozxR4ChoK9RUfj9cCuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH3oM5vp5+KUTITnnSby99FwDxSMc9Ow3WjCqvZLDhFC+cMUYMfzA=="
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
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 247
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": 247
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 247
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 247
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 247
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
      "caller_nonce": 247,
      "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
      "gas_price": 1,
      "gas_used": 11,
      "height": 247,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 247
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
        "round": 247
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 247
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 247
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
    "round": 247
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
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 247,
      "contract_id": "ct_sFat8ZtQGzDJhkQz8YspWXVxEt6u5qgAkt8eNoh3hozSnwTQN",
      "gas_price": 1,
      "gas_used": 11,
      "height": 247,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
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
    "deposit": "1",
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfP4oEp9E=",
        "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
        "deposit": "1",
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
    "call_data": "cb_KxFE1kQfP4oEp9E=",
    "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
    "deposit": 10,
    "vm_version": "1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfP4oEp9E=",
        "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
        "deposit": 10,
        "vm_version": "1"
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
    "abi_version": "1",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": "1",
        "call_data": "cb_KxFE1kQfP4oEp9E=",
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgfighvovvoDf7C3sIsUGuTWbUdxAPqmCmJyDWcK4VNA6ghSPabym",
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
  "id": -576460752303421371,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuECSu9JEdAuISZ1csK8Uc68wK23x83+C944KqiV+zhmf8fKY8IRhxMzo7nc0IWTfabIwkjZBsxjNFzXxURe9210MuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH4oIb6L76A3+wt7CLFBrk1m1HcQD6pgpicg1nCuFTQOoIUzz66rA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421371,
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
      "signed_tx": "tx_+JELAfhCuECSu9JEdAuISZ1csK8Uc68wK23x83+C944KqiV+zhmf8fKY8IRhxMzo7nc0IWTfabIwkjZBsxjNFzXxURe9210MuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH4oIb6L76A3+wt7CLFBrk1m1HcQD6pgpicg1nCuFTQOoIUzz66rA==",
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
  "id": -576460752303421370,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuECSu9JEdAuISZ1csK8Uc68wK23x83+C944KqiV+zhmf8fKY8IRhxMzo7nc0IWTfabIwkjZBsxjNFzXxURe9210MuECrUplq9EhnnTh/ovglDY4vuu0YYFN8O6u5fdspixYaPgWc2kQahjy1jAS3BSoRSgPNWcjTScG91yWy7Q8+p6IIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH4oIb6L76A3+wt7CLFBrk1m1HcQD6pgpicg1nCuFTQOoIUZWQSdA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421370,
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
      "state": "tx_+NMLAfiEuECSu9JEdAuISZ1csK8Uc68wK23x83+C944KqiV+zhmf8fKY8IRhxMzo7nc0IWTfabIwkjZBsxjNFzXxURe9210MuECrUplq9EhnnTh/ovglDY4vuu0YYFN8O6u5fdspixYaPgWc2kQahjy1jAS3BSoRSgPNWcjTScG91yWy7Q8+p6IIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH4oIb6L76A3+wt7CLFBrk1m1HcQD6pgpicg1nCuFTQOoIUZWQSdA=="
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
      "state": "tx_+NMLAfiEuECSu9JEdAuISZ1csK8Uc68wK23x83+C944KqiV+zhmf8fKY8IRhxMzo7nc0IWTfabIwkjZBsxjNFzXxURe9210MuECrUplq9EhnnTh/ovglDY4vuu0YYFN8O6u5fdspixYaPgWc2kQahjy1jAS3BSoRSgPNWcjTScG91yWy7Q8+p6IIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH4oIb6L76A3+wt7CLFBrk1m1HcQD6pgpicg1nCuFTQOoIUZWQSdA=="
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
    "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
    "deposit": "1",
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfP4oEp9E=",
        "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
        "deposit": "1",
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
    "call_data": "cb_KxFE1kQfP4oEp9E=",
    "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
    "deposit": 10,
    "vm_version": "1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": 3,
        "call_data": "cb_KxFE1kQfP4oEp9E=",
        "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
        "deposit": 10,
        "vm_version": "1"
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
    "abi_version": "1",
    "call_data": "cb_KxFE1kQfP4oEp9E=",
    "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new_contract",
      "params": {
        "abi_version": "1",
        "call_data": "cb_KxFE1kQfP4oEp9E=",
        "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
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
    "call_data": "cb_KxFE1kQfP4oEp9E=",
    "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgfmgQiQ2cGIZkVWG/9sPKSK3Kin5FJezHshceqPdAZf6meb+DtEl",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
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
  "id": -576460752303421369,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuED9QZ5riCov/Ac6JIe67yb7pjvlaK9R5bp2WjQ+FWpIxlzdQXwb0VlGBxNRCuklFv/X+/KEr8ZnrR0Jr2Rn/aEMuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH5oEIkNnBiGZFVhv/bDykityop+RSXsx7IXHqj3QGX+pnmf6kQlQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421369,
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
      "signed_tx": "tx_+JELAfhCuED9QZ5riCov/Ac6JIe67yb7pjvlaK9R5bp2WjQ+FWpIxlzdQXwb0VlGBxNRCuklFv/X+/KEr8ZnrR0Jr2Rn/aEMuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH5oEIkNnBiGZFVhv/bDykityop+RSXsx7IXHqj3QGX+pnmf6kQlQ==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
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
  "id": -576460752303421368,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEDwJ1El4lzWEDhCW2JCeS88//fDw3kXJyauJvpw8enY/2jJOHKrVofeQt2IgueOLjGywVRWK9pYhzSrF7ug3CoAuED9QZ5riCov/Ac6JIe67yb7pjvlaK9R5bp2WjQ+FWpIxlzdQXwb0VlGBxNRCuklFv/X+/KEr8ZnrR0Jr2Rn/aEMuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH5oEIkNnBiGZFVhv/bDykityop+RSXsx7IXHqj3QGX+pnmK9Imag=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421368,
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
      "state": "tx_+NMLAfiEuEDwJ1El4lzWEDhCW2JCeS88//fDw3kXJyauJvpw8enY/2jJOHKrVofeQt2IgueOLjGywVRWK9pYhzSrF7ug3CoAuED9QZ5riCov/Ac6JIe67yb7pjvlaK9R5bp2WjQ+FWpIxlzdQXwb0VlGBxNRCuklFv/X+/KEr8ZnrR0Jr2Rn/aEMuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH5oEIkNnBiGZFVhv/bDykityop+RSXsx7IXHqj3QGX+pnmK9Imag=="
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
      "state": "tx_+NMLAfiEuEDwJ1El4lzWEDhCW2JCeS88//fDw3kXJyauJvpw8enY/2jJOHKrVofeQt2IgueOLjGywVRWK9pYhzSrF7ug3CoAuED9QZ5riCov/Ac6JIe67yb7pjvlaK9R5bp2WjQ+FWpIxlzdQXwb0VlGBxNRCuklFv/X+/KEr8ZnrR0Jr2Rn/aEMuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH5oEIkNnBiGZFVhv/bDykityop+RSXsx7IXHqj3QGX+pnmK9Imag=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 250,
      "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
      "gas_price": 1,
      "gas_used": 11,
      "height": 250,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Rgfqgezsrr3FeOmc5ATsTcTabk0KZXcFVTQIxtpciIqMrtMMOKeaz",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
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
  "id": -576460752303421367,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEDStLdhy+NtHgPFOpEWWEr6TWN+7YlcCQ6S3FhUzPaulLJbP1WbhDxv6D2ve2SONyxXFc8t7+qB/mV8ULrtld0HuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH6oHs7K69xXjpnOQE7E3E2m5NCmV3BVU0CMbaXIiKjK7TDDU4cRw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421367,
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
      "signed_tx": "tx_+JELAfhCuEDStLdhy+NtHgPFOpEWWEr6TWN+7YlcCQ6S3FhUzPaulLJbP1WbhDxv6D2ve2SONyxXFc8t7+qB/mV8ULrtld0HuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH6oHs7K69xXjpnOQE7E3E2m5NCmV3BVU0CMbaXIiKjK7TDDU4cRw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
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
  "id": -576460752303421366,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEDStLdhy+NtHgPFOpEWWEr6TWN+7YlcCQ6S3FhUzPaulLJbP1WbhDxv6D2ve2SONyxXFc8t7+qB/mV8ULrtld0HuED4ZmvtfdSRIY4KoxV1tE39gfd71ekzJ9xnWR+SrUdAEUx/M4l+T2zyNywaNkPap3OJOM7C3MtBTqvnmOUChOAGuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH6oHs7K69xXjpnOQE7E3E2m5NCmV3BVU0CMbaXIiKjK7TDFpvRbQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421366,
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
      "state": "tx_+NMLAfiEuEDStLdhy+NtHgPFOpEWWEr6TWN+7YlcCQ6S3FhUzPaulLJbP1WbhDxv6D2ve2SONyxXFc8t7+qB/mV8ULrtld0HuED4ZmvtfdSRIY4KoxV1tE39gfd71ekzJ9xnWR+SrUdAEUx/M4l+T2zyNywaNkPap3OJOM7C3MtBTqvnmOUChOAGuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH6oHs7K69xXjpnOQE7E3E2m5NCmV3BVU0CMbaXIiKjK7TDFpvRbQ=="
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
      "state": "tx_+NMLAfiEuEDStLdhy+NtHgPFOpEWWEr6TWN+7YlcCQ6S3FhUzPaulLJbP1WbhDxv6D2ve2SONyxXFc8t7+qB/mV8ULrtld0HuED4ZmvtfdSRIY4KoxV1tE39gfd71ekzJ9xnWR+SrUdAEUx/M4l+T2zyNywaNkPap3OJOM7C3MtBTqvnmOUChOAGuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH6oHs7K69xXjpnOQE7E3E2m5NCmV3BVU0CMbaXIiKjK7TDFpvRbQ=="
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 250
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": 250
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 250
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 250
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 250
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
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 250,
      "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
      "gas_price": 1,
      "gas_used": 11,
      "height": 250,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
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
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 250
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": 250
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 250
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 250
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 250
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
      "caller_nonce": 250,
      "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
      "gas_price": 1,
      "gas_used": 11,
      "height": 250,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 251,
      "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
      "gas_price": 1,
      "gas_used": 11,
      "height": 251,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxTlg6/6",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxTlg6/6",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgfugFyKRrHWeBs7Bl4GtqaBKTkARg1IFjwsSs0LBbF9x5AKSjPSf",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
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
  "id": -576460752303421365,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuECcoXddPWsRUfCTxrdyTDBkB+QeLCg/i28xyvzZEJR4WmHJPXrsUvjTJbc3d2fQar+DV22vEMYQ8cs6yF6eJ90DuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH7oBcikax1ngbOwZeBramgSk5AEYNSBY8LErNCwWxfceQCl3o5vA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421365,
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
      "signed_tx": "tx_+JELAfhCuECcoXddPWsRUfCTxrdyTDBkB+QeLCg/i28xyvzZEJR4WmHJPXrsUvjTJbc3d2fQar+DV22vEMYQ8cs6yF6eJ90DuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH7oBcikax1ngbOwZeBramgSk5AEYNSBY8LErNCwWxfceQCl3o5vA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
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
  "id": -576460752303421364,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEASudMHiVJwZkLq+mvb9b9tZcchPihrSNLPx+6DHTJR18wWAIWthR0sjz/2SbewRg7tc8qLnJ9dgTTfcODAGDcLuECcoXddPWsRUfCTxrdyTDBkB+QeLCg/i28xyvzZEJR4WmHJPXrsUvjTJbc3d2fQar+DV22vEMYQ8cs6yF6eJ90DuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH7oBcikax1ngbOwZeBramgSk5AEYNSBY8LErNCwWxfceQC88E9rg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421364,
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
      "state": "tx_+NMLAfiEuEASudMHiVJwZkLq+mvb9b9tZcchPihrSNLPx+6DHTJR18wWAIWthR0sjz/2SbewRg7tc8qLnJ9dgTTfcODAGDcLuECcoXddPWsRUfCTxrdyTDBkB+QeLCg/i28xyvzZEJR4WmHJPXrsUvjTJbc3d2fQar+DV22vEMYQ8cs6yF6eJ90DuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH7oBcikax1ngbOwZeBramgSk5AEYNSBY8LErNCwWxfceQC88E9rg=="
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
      "state": "tx_+NMLAfiEuEASudMHiVJwZkLq+mvb9b9tZcchPihrSNLPx+6DHTJR18wWAIWthR0sjz/2SbewRg7tc8qLnJ9dgTTfcODAGDcLuECcoXddPWsRUfCTxrdyTDBkB+QeLCg/i28xyvzZEJR4WmHJPXrsUvjTJbc3d2fQar+DV22vEMYQ8cs6yF6eJ90DuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH7oBcikax1ngbOwZeBramgSk5AEYNSBY8LErNCwWxfceQC88E9rg=="
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
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 251
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": 251
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 251
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 251
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 251
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
      "caller_nonce": 251,
      "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
      "gas_price": 1,
      "gas_used": 11,
      "height": 251,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 251
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": 251
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 251
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 251
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 251
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
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 251,
      "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
      "gas_price": 1,
      "gas_used": 11,
      "height": 251,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_FNcD09o="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 252,
      "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
      "gas_price": 1,
      "gas_used": 11,
      "height": 252,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgfygAgNLWPHhPlp2UOSUWj9HseV0KdcKESeyoBX6tOIjJjZVQBxS",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
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
  "id": -576460752303421363,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuECP6sdCjyba3PRamj+1abrWUJNGu94aba08cFl68klZBxDhouW8qx7PydfLpptCCERYkr1kUyckNPU+d1otcvYIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH8oAIDS1jx4T5adlDklFo/R7HldCnXChEnsqAV+rTiIyY2BEEYIg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421363,
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
      "signed_tx": "tx_+JELAfhCuECP6sdCjyba3PRamj+1abrWUJNGu94aba08cFl68klZBxDhouW8qx7PydfLpptCCERYkr1kUyckNPU+d1otcvYIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH8oAIDS1jx4T5adlDklFo/R7HldCnXChEnsqAV+rTiIyY2BEEYIg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
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
  "id": -576460752303421362,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEB3ydq7ykv60BMkZDbDncSSzFchaOYRt7pM7R45gny4dRDZpBhHNmxVbwHlBajx513OSYRy7NW0kv3hcCEQY+sKuECP6sdCjyba3PRamj+1abrWUJNGu94aba08cFl68klZBxDhouW8qx7PydfLpptCCERYkr1kUyckNPU+d1otcvYIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH8oAIDS1jx4T5adlDklFo/R7HldCnXChEnsqAV+rTiIyY2N1TmfA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421362,
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
      "state": "tx_+NMLAfiEuEB3ydq7ykv60BMkZDbDncSSzFchaOYRt7pM7R45gny4dRDZpBhHNmxVbwHlBajx513OSYRy7NW0kv3hcCEQY+sKuECP6sdCjyba3PRamj+1abrWUJNGu94aba08cFl68klZBxDhouW8qx7PydfLpptCCERYkr1kUyckNPU+d1otcvYIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH8oAIDS1jx4T5adlDklFo/R7HldCnXChEnsqAV+rTiIyY2N1TmfA=="
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
      "state": "tx_+NMLAfiEuEB3ydq7ykv60BMkZDbDncSSzFchaOYRt7pM7R45gny4dRDZpBhHNmxVbwHlBajx513OSYRy7NW0kv3hcCEQY+sKuECP6sdCjyba3PRamj+1abrWUJNGu94aba08cFl68klZBxDhouW8qx7PydfLpptCCERYkr1kUyckNPU+d1otcvYIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH8oAIDS1jx4T5adlDklFo/R7HldCnXChEnsqAV+rTiIyY2N1TmfA=="
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 252
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": 252
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 252
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 252
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 252
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
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 252,
      "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
      "gas_price": 1,
      "gas_used": 11,
      "height": 252,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
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
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 252
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": 252
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 252
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 252
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 252
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
      "caller_nonce": 252,
      "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
      "gas_price": 1,
      "gas_used": 11,
      "height": 252,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 253,
      "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
      "gas_price": 1,
      "gas_used": 11,
      "height": 253,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxbivrGI",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxbivrGI",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Rgf2gacANfCsS7ai3q+rucYbOPwtmrEg2mkNpEMauUXJIV+lntCHG",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
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
  "id": -576460752303421361,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEB78xNRbMYDdL/aZyHZkd73Y5d8NEjYq4brNZHzN5LQycHCkx8ZQY3KnJ46k3JHrAEl1VFQF/EToQkAGuKY9LwJuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH9oGnADXwrEu2ot6vq7nGGzj8LZqxINppDaRDGrlFySFfpl2rAvQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421361,
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
      "signed_tx": "tx_+JELAfhCuEB78xNRbMYDdL/aZyHZkd73Y5d8NEjYq4brNZHzN5LQycHCkx8ZQY3KnJ46k3JHrAEl1VFQF/EToQkAGuKY9LwJuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH9oGnADXwrEu2ot6vq7nGGzj8LZqxINppDaRDGrlFySFfpl2rAvQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
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
  "id": -576460752303421360,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEB5Pam/QyAg7lT8UjPD1hdNU+G/tP2gTbqZu7kGK3UyhQOT9oJlzd4tM5HRbrikCisMDv9FUQ83ii1L8AGn4NsBuEB78xNRbMYDdL/aZyHZkd73Y5d8NEjYq4brNZHzN5LQycHCkx8ZQY3KnJ46k3JHrAEl1VFQF/EToQkAGuKY9LwJuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH9oGnADXwrEu2ot6vq7nGGzj8LZqxINppDaRDGrlFySFfpJAOFfw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421360,
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
      "state": "tx_+NMLAfiEuEB5Pam/QyAg7lT8UjPD1hdNU+G/tP2gTbqZu7kGK3UyhQOT9oJlzd4tM5HRbrikCisMDv9FUQ83ii1L8AGn4NsBuEB78xNRbMYDdL/aZyHZkd73Y5d8NEjYq4brNZHzN5LQycHCkx8ZQY3KnJ46k3JHrAEl1VFQF/EToQkAGuKY9LwJuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH9oGnADXwrEu2ot6vq7nGGzj8LZqxINppDaRDGrlFySFfpJAOFfw=="
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
      "state": "tx_+NMLAfiEuEB5Pam/QyAg7lT8UjPD1hdNU+G/tP2gTbqZu7kGK3UyhQOT9oJlzd4tM5HRbrikCisMDv9FUQ83ii1L8AGn4NsBuEB78xNRbMYDdL/aZyHZkd73Y5d8NEjYq4brNZHzN5LQycHCkx8ZQY3KnJ46k3JHrAEl1VFQF/EToQkAGuKY9LwJuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH9oGnADXwrEu2ot6vq7nGGzj8LZqxINppDaRDGrlFySFfpJAOFfw=="
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
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 253
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": 253
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 253
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 253
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 253
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
      "caller_nonce": 253,
      "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
      "gas_price": 1,
      "gas_used": 11,
      "height": 253,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 253
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": 253
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 253
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 253
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 253
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
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 253,
      "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
      "gas_price": 1,
      "gas_used": 11,
      "height": 253,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Fs8pdG0="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 254,
      "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
      "gas_price": 1,
      "gas_used": 165,
      "height": 254,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Rgf6gTCJqq/cWi8DnIt47cSu5MShxp4qUMq9rjrtAMC7ea6Hk6vF1",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
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
  "id": -576460752303421359,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuECDp3Ny/kBfEYu7XVUEsXlBLxpQzeCTfPid87a1Y08nPCfQgymRON2PdePtwCkjWUdP+e8E9bw2B86T8NDiu8oEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH+oEwiaqv3FovA5yLeO3EruTEocaeKlDKva467QDAu3muhF8xBKg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421359,
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
      "signed_tx": "tx_+JELAfhCuECDp3Ny/kBfEYu7XVUEsXlBLxpQzeCTfPid87a1Y08nPCfQgymRON2PdePtwCkjWUdP+e8E9bw2B86T8NDiu8oEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH+oEwiaqv3FovA5yLeO3EruTEocaeKlDKva467QDAu3muhF8xBKg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
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
  "id": -576460752303421358,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEBXuWFsuG3JMymWHz305DbPLA5D4rvUfIS+fG+Oq99xQ/A8piq94U3HzysqV4EPJw7D/OhvoKNgzwByACUSfIwBuECDp3Ny/kBfEYu7XVUEsXlBLxpQzeCTfPid87a1Y08nPCfQgymRON2PdePtwCkjWUdP+e8E9bw2B86T8NDiu8oEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH+oEwiaqv3FovA5yLeO3EruTEocaeKlDKva467QDAu3muhBrQfdA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421358,
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
      "state": "tx_+NMLAfiEuEBXuWFsuG3JMymWHz305DbPLA5D4rvUfIS+fG+Oq99xQ/A8piq94U3HzysqV4EPJw7D/OhvoKNgzwByACUSfIwBuECDp3Ny/kBfEYu7XVUEsXlBLxpQzeCTfPid87a1Y08nPCfQgymRON2PdePtwCkjWUdP+e8E9bw2B86T8NDiu8oEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH+oEwiaqv3FovA5yLeO3EruTEocaeKlDKva467QDAu3muhBrQfdA=="
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
      "state": "tx_+NMLAfiEuEBXuWFsuG3JMymWHz305DbPLA5D4rvUfIS+fG+Oq99xQ/A8piq94U3HzysqV4EPJw7D/OhvoKNgzwByACUSfIwBuECDp3Ny/kBfEYu7XVUEsXlBLxpQzeCTfPid87a1Y08nPCfQgymRON2PdePtwCkjWUdP+e8E9bw2B86T8NDiu8oEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH+oEwiaqv3FovA5yLeO3EruTEocaeKlDKva467QDAu3muhBrQfdA=="
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": 254
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
        "round": 254
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 254
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 254
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": 254
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
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 254,
      "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
      "gas_price": 1,
      "gas_used": 165,
      "height": 254,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
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
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": 254
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
        "round": 254
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 254
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 254
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": 254
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
      "caller_nonce": 254,
      "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
      "gas_price": 1,
      "gas_used": 165,
      "height": 254,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 255,
      "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
      "gas_price": 1,
      "gas_used": 165,
      "height": 255,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Rgf+g+435Z8TUC1OvoEvOgO2IGZyneeMY7tR3F1JfgMSqAMDk24Xz",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
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
  "id": -576460752303421357,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuECBeh9JrN+SvImhxurp7X/w9REGW8v5KLBVGq2Ihs3W2g0dsmfXnI5jeKKx83yaSdEjbOgJ8C6azK59d0ECzZwIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH/oPuN+WfE1AtTr6BLzoDtiBmcp3njGO7UdxdSX4DEqgDAMceUyg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421357,
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
      "signed_tx": "tx_+JELAfhCuECBeh9JrN+SvImhxurp7X/w9REGW8v5KLBVGq2Ihs3W2g0dsmfXnI5jeKKx83yaSdEjbOgJ8C6azK59d0ECzZwIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH/oPuN+WfE1AtTr6BLzoDtiBmcp3njGO7UdxdSX4DEqgDAMceUyg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VKzK/Pk=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
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
  "id": -576460752303421356,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuECBeh9JrN+SvImhxurp7X/w9REGW8v5KLBVGq2Ihs3W2g0dsmfXnI5jeKKx83yaSdEjbOgJ8C6azK59d0ECzZwIuEDCjPo9Okmyf0afDXkw9Y+wLwqzYIv9do2HiSVSQfFFp3WPhUlO1CgLLQadYcZVyXXl/JArni/KjIQtFkQMuekNuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH/oPuN+WfE1AtTr6BLzoDtiBmcp3njGO7UdxdSX4DEqgDA/eivqQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421356,
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
      "state": "tx_+NMLAfiEuECBeh9JrN+SvImhxurp7X/w9REGW8v5KLBVGq2Ihs3W2g0dsmfXnI5jeKKx83yaSdEjbOgJ8C6azK59d0ECzZwIuEDCjPo9Okmyf0afDXkw9Y+wLwqzYIv9do2HiSVSQfFFp3WPhUlO1CgLLQadYcZVyXXl/JArni/KjIQtFkQMuekNuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH/oPuN+WfE1AtTr6BLzoDtiBmcp3njGO7UdxdSX4DEqgDA/eivqQ=="
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
      "state": "tx_+NMLAfiEuECBeh9JrN+SvImhxurp7X/w9REGW8v5KLBVGq2Ihs3W2g0dsmfXnI5jeKKx83yaSdEjbOgJ8C6azK59d0ECzZwIuEDCjPo9Okmyf0afDXkw9Y+wLwqzYIv9do2HiSVSQfFFp3WPhUlO1CgLLQadYcZVyXXl/JArni/KjIQtFkQMuekNuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYH/oPuN+WfE1AtTr6BLzoDtiBmcp3njGO7UdxdSX4DEqgDA/eivqQ=="
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
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": 255
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
        "round": 255
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 255
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 255
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": 255
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
      "caller_nonce": 255,
      "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
      "gas_price": 1,
      "gas_used": 165,
      "height": 255,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": 255
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
        "round": 255
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 255
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 255
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": 255
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
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 255,
      "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
      "gas_price": 1,
      "gas_used": 165,
      "height": 255,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_VNLOFXc="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 256,
      "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
      "gas_price": 1,
      "gas_used": 165,
      "height": 256,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEAoLfBrGYyVKgN85yUsSoWfccSfSzeEv3Ap43oTpk3Ken70TwUOg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
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
  "id": -576460752303421355,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEBElP+wEGIcspflKifdvNEktMbwbR5jBiWslIcRr87xrPBMmc/nQ994y9axTrcrP/LGQCZdovHMLJDS4R7PMzoLuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBAKC3waxmMlSoDfOclLEqFn3HEn0s3hL9wKeN6E6ZNynp+zFgbtI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421355,
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
      "signed_tx": "tx_+JILAfhCuEBElP+wEGIcspflKifdvNEktMbwbR5jBiWslIcRr87xrPBMmc/nQ994y9axTrcrP/LGQCZdovHMLJDS4R7PMzoLuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBAKC3waxmMlSoDfOclLEqFn3HEn0s3hL9wKeN6E6ZNynp+zFgbtI=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
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
  "id": -576460752303421354,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEAeCwRUCrpR17T+R5449aPTpxr4+phGh6bdxCueqjxm3wyCq7Vo9pqABdVkdZ13HD9921YT7iahLS+kF5osaRIJuEBElP+wEGIcspflKifdvNEktMbwbR5jBiWslIcRr87xrPBMmc/nQ994y9axTrcrP/LGQCZdovHMLJDS4R7PMzoLuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBAKC3waxmMlSoDfOclLEqFn3HEn0s3hL9wKeN6E6ZNynp+7wfQYM="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421354,
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
      "state": "tx_+NQLAfiEuEAeCwRUCrpR17T+R5449aPTpxr4+phGh6bdxCueqjxm3wyCq7Vo9pqABdVkdZ13HD9921YT7iahLS+kF5osaRIJuEBElP+wEGIcspflKifdvNEktMbwbR5jBiWslIcRr87xrPBMmc/nQ994y9axTrcrP/LGQCZdovHMLJDS4R7PMzoLuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBAKC3waxmMlSoDfOclLEqFn3HEn0s3hL9wKeN6E6ZNynp+7wfQYM="
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
      "state": "tx_+NQLAfiEuEAeCwRUCrpR17T+R5449aPTpxr4+phGh6bdxCueqjxm3wyCq7Vo9pqABdVkdZ13HD9921YT7iahLS+kF5osaRIJuEBElP+wEGIcspflKifdvNEktMbwbR5jBiWslIcRr87xrPBMmc/nQ994y9axTrcrP/LGQCZdovHMLJDS4R7PMzoLuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBAKC3waxmMlSoDfOclLEqFn3HEn0s3hL9wKeN6E6ZNynp+7wfQYM="
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": 256
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
        "round": 256
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 256
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 256
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": 256
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
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 256,
      "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
      "gas_price": 1,
      "gas_used": 165,
      "height": 256,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
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
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": 256
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
        "round": 256
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 256
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 256
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": 256
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
      "caller_nonce": 256,
      "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
      "gas_price": 1,
      "gas_used": 165,
      "height": 256,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 257,
      "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
      "gas_price": 1,
      "gas_used": 165,
      "height": 257,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "ABCDEFG",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "ABCDEFG",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 20,
        "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 20,
    "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEBoJfBtYvfQFGQT5P2+utn6oWcC24WANenLl87SQWuiKnFA5yFvQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
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
  "id": -576460752303421353,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuECNJmNzZvKma2qM5akPeaeSMGYxYzcLpey6VEVgF+RDSONGMvwTwXEmd2+zRvSkD9IRotewqw+oF7GGdwuS7N8FuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBAaCXwbWL30BRkE+T9vrrZ+qFnAtuFgDXpy5fO0kFroipxRUnYqE="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421353,
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
      "signed_tx": "tx_+JILAfhCuECNJmNzZvKma2qM5akPeaeSMGYxYzcLpey6VEVgF+RDSONGMvwTwXEmd2+zRvSkD9IRotewqw+oF7GGdwuS7N8FuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBAaCXwbWL30BRkE+T9vrrZ+qFnAtuFgDXpy5fO0kFroipxRUnYqE=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoMB1nS9NpzEK9gCf7Geuv/+s3f2jyhDP28nPrBPrmEQ/VvkPGZY=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
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
  "id": -576460752303421352,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEBE+7PQsWlraqrbPZYYKn0dkvlAkwrmT0CDie1Az/nBCScniw+INK/tyVs36eAX+d9ZWjr+JsuL/K0Adc2bepgBuECNJmNzZvKma2qM5akPeaeSMGYxYzcLpey6VEVgF+RDSONGMvwTwXEmd2+zRvSkD9IRotewqw+oF7GGdwuS7N8FuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBAaCXwbWL30BRkE+T9vrrZ+qFnAtuFgDXpy5fO0kFroipxRIasJU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421352,
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
      "state": "tx_+NQLAfiEuEBE+7PQsWlraqrbPZYYKn0dkvlAkwrmT0CDie1Az/nBCScniw+INK/tyVs36eAX+d9ZWjr+JsuL/K0Adc2bepgBuECNJmNzZvKma2qM5akPeaeSMGYxYzcLpey6VEVgF+RDSONGMvwTwXEmd2+zRvSkD9IRotewqw+oF7GGdwuS7N8FuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBAaCXwbWL30BRkE+T9vrrZ+qFnAtuFgDXpy5fO0kFroipxRIasJU="
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
      "state": "tx_+NQLAfiEuEBE+7PQsWlraqrbPZYYKn0dkvlAkwrmT0CDie1Az/nBCScniw+INK/tyVs36eAX+d9ZWjr+JsuL/K0Adc2bepgBuECNJmNzZvKma2qM5akPeaeSMGYxYzcLpey6VEVgF+RDSONGMvwTwXEmd2+zRvSkD9IRotewqw+oF7GGdwuS7N8FuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBAaCXwbWL30BRkE+T9vrrZ+qFnAtuFgDXpy5fO0kFroipxRIasJU="
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
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": 257
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
        "round": 257
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 257
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 257
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": 257
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
      "caller_nonce": 257,
      "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
      "gas_price": 1,
      "gas_used": 165,
      "height": 257,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": 257
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
        "round": 257
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 257
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 257
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
    "round": 257
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
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 257,
      "contract_id": "ct_vHpfW2q4wT6iDWwBtbHhLEGNn1kAwL4p6ZjA19YMLh7UcRfed",
      "gas_price": 1,
      "gas_used": 165,
      "height": 257,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_Vl4/10M="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 258,
      "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
      "gas_price": 1,
      "gas_used": 11,
      "height": 258,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggECoNoN1oegzUk1CsNgJGFMxlQ85o0GOXthZUGMNf5mCPaKYgIjpQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
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
  "id": -576460752303421351,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEBgnYfmembRzo0lw/clUQQtXujuXPLDIDdPmR2x62B7qwqnDtFYU8QTNpTjDyQ6t3VV6tTcmV5K2kRpuoN/McUNuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBAqDaDdaHoM1JNQrDYCRhTMZUPOaNBjl7YWVBjDX+Zgj2ioqYXNg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421351,
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
      "signed_tx": "tx_+JILAfhCuEBgnYfmembRzo0lw/clUQQtXujuXPLDIDdPmR2x62B7qwqnDtFYU8QTNpTjDyQ6t3VV6tTcmV5K2kRpuoN/McUNuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBAqDaDdaHoM1JNQrDYCRhTMZUPOaNBjl7YWVBjDX+Zgj2ioqYXNg=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
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
  "id": -576460752303421350,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEAjr0LCQcwYjIjXhyM1A3/LEQ8V2aeTFG7yCd4NpM4NOXDNXwoAfoSE+Q/dSfy9V8LlQZbEjskg5JJIH7g98YUFuEBgnYfmembRzo0lw/clUQQtXujuXPLDIDdPmR2x62B7qwqnDtFYU8QTNpTjDyQ6t3VV6tTcmV5K2kRpuoN/McUNuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBAqDaDdaHoM1JNQrDYCRhTMZUPOaNBjl7YWVBjDX+Zgj2ikT6xDE="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421350,
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
      "state": "tx_+NQLAfiEuEAjr0LCQcwYjIjXhyM1A3/LEQ8V2aeTFG7yCd4NpM4NOXDNXwoAfoSE+Q/dSfy9V8LlQZbEjskg5JJIH7g98YUFuEBgnYfmembRzo0lw/clUQQtXujuXPLDIDdPmR2x62B7qwqnDtFYU8QTNpTjDyQ6t3VV6tTcmV5K2kRpuoN/McUNuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBAqDaDdaHoM1JNQrDYCRhTMZUPOaNBjl7YWVBjDX+Zgj2ikT6xDE="
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
      "state": "tx_+NQLAfiEuEAjr0LCQcwYjIjXhyM1A3/LEQ8V2aeTFG7yCd4NpM4NOXDNXwoAfoSE+Q/dSfy9V8LlQZbEjskg5JJIH7g98YUFuEBgnYfmembRzo0lw/clUQQtXujuXPLDIDdPmR2x62B7qwqnDtFYU8QTNpTjDyQ6t3VV6tTcmV5K2kRpuoN/McUNuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBAqDaDdaHoM1JNQrDYCRhTMZUPOaNBjl7YWVBjDX+Zgj2ikT6xDE="
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 258
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": 258
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 258
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 258
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 258
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
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 258,
      "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
      "gas_price": 1,
      "gas_used": 11,
      "height": 258,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
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
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 258
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": 258
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 258
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
        "contract_id": "ABCDEFG",
        "round": 258
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 258
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
      "caller_nonce": 258,
      "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
      "gas_price": 1,
      "gas_used": 11,
      "height": 258,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 259,
      "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
      "gas_price": 1,
      "gas_used": 11,
      "height": 259,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
    }
  },
  "version": 1
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.dry_run.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": "1",
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": "1",
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": "1",
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": "1",
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "ABCDEFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
        "code": 1009,
        "message": "Broken encoding: contract bytearray"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "ABCDEFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ABCDEFG"
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.call_contract",
      "params": {
        "abi_version": 3,
        "amount": 0,
        "call_data": "cb_KxG4F37sGxg+DKMp",
        "contract_id": "ABCDEFG"
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
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 3,
    "amount": 0,
    "call_data": "cb_KxG4F37sGxg+DKMp",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEDoNsca3R8jMs5HzRYDq2R9LkewPaLBT0ii/hu1J0wRcysZxBdZQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
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
  "id": -576460752303421349,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuECZkBllso4TeenMcxSjHiU6MWGiRTzpx+GQM3zdqeLby/Wm773SL0s81lHbJ75q3EMPa6Q0thvARP6NWYkkT5IFuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBA6DbHGt0fIzLOR80WA6tkfS5HsD2iwU9Iov4btSdMEXMrGXQJwE="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421349,
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
      "signed_tx": "tx_+JILAfhCuECZkBllso4TeenMcxSjHiU6MWGiRTzpx+GQM3zdqeLby/Wm773SL0s81lHbJ75q3EMPa6Q0thvARP6NWYkkT5IFuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBA6DbHGt0fIzLOR80WA6tkfS5HsD2iwU9Iov4btSdMEXMrGXQJwE=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
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
  "id": -576460752303421348,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuECZkBllso4TeenMcxSjHiU6MWGiRTzpx+GQM3zdqeLby/Wm773SL0s81lHbJ75q3EMPa6Q0thvARP6NWYkkT5IFuED8Xho6fIJRLrEnCxxp1MU2F91/cVo1uccZceJq8cl9EfRBuvIqfzzRFciH7TIfiqyW3c0wmkc528N++KjZcBIDuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBA6DbHGt0fIzLOR80WA6tkfS5HsD2iwU9Iov4btSdMEXMrOw0S0A="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "id": -576460752303421348,
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
      "state": "tx_+NQLAfiEuECZkBllso4TeenMcxSjHiU6MWGiRTzpx+GQM3zdqeLby/Wm773SL0s81lHbJ75q3EMPa6Q0thvARP6NWYkkT5IFuED8Xho6fIJRLrEnCxxp1MU2F91/cVo1uccZceJq8cl9EfRBuvIqfzzRFciH7TIfiqyW3c0wmkc528N++KjZcBIDuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBA6DbHGt0fIzLOR80WA6tkfS5HsD2iwU9Iov4btSdMEXMrOw0S0A="
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
      "state": "tx_+NQLAfiEuECZkBllso4TeenMcxSjHiU6MWGiRTzpx+GQM3zdqeLby/Wm773SL0s81lHbJ75q3EMPa6Q0thvARP6NWYkkT5IFuED8Xho6fIJRLrEnCxxp1MU2F91/cVo1uccZceJq8cl9EfRBuvIqfzzRFciH7TIfiqyW3c0wmkc528N++KjZcBIDuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBA6DbHGt0fIzLOR80WA6tkfS5HsD2iwU9Iov4btSdMEXMrOw0S0A="
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
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 259
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": 259
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 259
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 259
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 259
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
      "caller_nonce": 259,
      "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
      "gas_price": 1,
      "gas_used": 11,
      "height": 259,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": "2"
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
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": "2"
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ABCEDFG",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 259
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
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ABCEDFG",
        "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
        "round": 259
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 259
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
        "code": 1006,
        "message": "Broken encoding: contract pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.get.contract_call",
      "params": {
        "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
        "contract_id": "ABCDEFG",
        "round": 259
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
  "method": "channels.get.contract_call",
  "params": {
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
    "round": 259
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
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 259,
      "contract_id": "ct_2Tm7qMqX96L5fWWGYsKYHVF7BM4afe74vjXqTXf7pa4zE1seT1",
      "gas_price": 1,
      "gas_used": 11,
      "height": 259,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_GMKQhBA="
    }
  },
  "version": 1
}
```
