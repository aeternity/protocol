
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gdSgT7W6Js3e8051/Eo8lO0zqIFaQJ1kjy3G9iP+8p/FAv7YdcaB",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "signed_tx": "tx_+JELAfhCuEBeshYVx7vkvebKoEr39NdH4J5RN7GRDfrt7jP533UT2DN/XFnjMGI5ObHMTsPTidsQqHc+9PMws5VPEOrT7IwNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HUoE+1uibN3vNOdfxKPJTtM6iBWkCdZI8txvYj/vKfxQL+IskCGQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEBeshYVx7vkvebKoEr39NdH4J5RN7GRDfrt7jP533UT2DN/XFnjMGI5ObHMTsPTidsQqHc+9PMws5VPEOrT7IwNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HUoE+1uibN3vNOdfxKPJTtM6iBWkCdZI8txvYj/vKfxQL+IskCGQ==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "signed_tx": "tx_+NMLAfiEuEAjLPtCmrsx40zy0Q+tveD+fZU8UKlPmoPQz1CxMFUac2z4LXMR7/gGAdAeBmr1k7bDHFhqBhnINFCayl77HLoDuEBeshYVx7vkvebKoEr39NdH4J5RN7GRDfrt7jP533UT2DN/XFnjMGI5ObHMTsPTidsQqHc+9PMws5VPEOrT7IwNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HUoE+1uibN3vNOdfxKPJTtM6iBWkCdZI8txvYj/vKfxQL+Fxoqhw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEAjLPtCmrsx40zy0Q+tveD+fZU8UKlPmoPQz1CxMFUac2z4LXMR7/gGAdAeBmr1k7bDHFhqBhnINFCayl77HLoDuEBeshYVx7vkvebKoEr39NdH4J5RN7GRDfrt7jP533UT2DN/XFnjMGI5ObHMTsPTidsQqHc+9PMws5VPEOrT7IwNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HUoE+1uibN3vNOdfxKPJTtM6iBWkCdZI8txvYj/vKfxQL+Fxoqhw=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEAjLPtCmrsx40zy0Q+tveD+fZU8UKlPmoPQz1CxMFUac2z4LXMR7/gGAdAeBmr1k7bDHFhqBhnINFCayl77HLoDuEBeshYVx7vkvebKoEr39NdH4J5RN7GRDfrt7jP533UT2DN/XFnjMGI5ObHMTsPTidsQqHc+9PMws5VPEOrT7IwNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HUoE+1uibN3vNOdfxKPJTtM6iBWkCdZI8txvYj/vKfxQL+Fxoqhw=="
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gdWgqm4zE9zcARf0D9L/amtR/3quGZsrFgIRNrvLymLbsPRjXP9s",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "signed_tx": "tx_+JELAfhCuEDilmFRrysMg+ZMSTvP/KTq8CEidC+cjRyZkA8ZNhV0ZO3GvUFB6StQhYvr7mSXtu8iYSN0ufd1hukOMorua/0MuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HVoKpuMxPc3AEX9A/S/2prUf96rhmbKxYCETa7y8pi27D0paCSbQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEDilmFRrysMg+ZMSTvP/KTq8CEidC+cjRyZkA8ZNhV0ZO3GvUFB6StQhYvr7mSXtu8iYSN0ufd1hukOMorua/0MuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HVoKpuMxPc3AEX9A/S/2prUf96rhmbKxYCETa7y8pi27D0paCSbQ==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "signed_tx": "tx_+NMLAfiEuEDJbPeMlxvcOBrYybOSoYqT2kYd/cMAsVyZXiVh2Vi4UI/UtEcQK+u2FcPDP2KsqmL0gBTJlLwnrJ/W9gy0lN8IuEDilmFRrysMg+ZMSTvP/KTq8CEidC+cjRyZkA8ZNhV0ZO3GvUFB6StQhYvr7mSXtu8iYSN0ufd1hukOMorua/0MuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HVoKpuMxPc3AEX9A/S/2prUf96rhmbKxYCETa7y8pi27D0s/pwZw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEDJbPeMlxvcOBrYybOSoYqT2kYd/cMAsVyZXiVh2Vi4UI/UtEcQK+u2FcPDP2KsqmL0gBTJlLwnrJ/W9gy0lN8IuEDilmFRrysMg+ZMSTvP/KTq8CEidC+cjRyZkA8ZNhV0ZO3GvUFB6StQhYvr7mSXtu8iYSN0ufd1hukOMorua/0MuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HVoKpuMxPc3AEX9A/S/2prUf96rhmbKxYCETa7y8pi27D0s/pwZw=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEDJbPeMlxvcOBrYybOSoYqT2kYd/cMAsVyZXiVh2Vi4UI/UtEcQK+u2FcPDP2KsqmL0gBTJlLwnrJ/W9gy0lN8IuEDilmFRrysMg+ZMSTvP/KTq8CEidC+cjRyZkA8ZNhV0ZO3GvUFB6StQhYvr7mSXtu8iYSN0ufd1hukOMorua/0MuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HVoKpuMxPc3AEX9A/S/2prUf96rhmbKxYCETa7y8pi27D0s/pwZw=="
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 214,
      "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gdagvhv4N7DhakmtKrPl0bZn+AomYDCvgkXEAYKNTQTAADw6IH9z",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "signed_tx": "tx_+JELAfhCuECpCHdJDkU5hXe5iBnsizPDn7mMy9eEv7MyNfKG8kbphkVTQa39aLTA+mAS6hsH1GAqfqcADPrpqST9m3OmNzcFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HWoL4b+Dew4WpJrSqz5dG2Z/gKJmAwr4JFxAGCjU0EwAA8YivG8g=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuECpCHdJDkU5hXe5iBnsizPDn7mMy9eEv7MyNfKG8kbphkVTQa39aLTA+mAS6hsH1GAqfqcADPrpqST9m3OmNzcFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HWoL4b+Dew4WpJrSqz5dG2Z/gKJmAwr4JFxAGCjU0EwAA8YivG8g==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "signed_tx": "tx_+NMLAfiEuEBP77MxKwiNAhS9hOUfFbs39iIdRY0chvP4qzdQtgW1bPzbAVJReZdqfAeXWYwMtXmKeNSTM3edvlI8DE8fgasMuECpCHdJDkU5hXe5iBnsizPDn7mMy9eEv7MyNfKG8kbphkVTQa39aLTA+mAS6hsH1GAqfqcADPrpqST9m3OmNzcFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HWoL4b+Dew4WpJrSqz5dG2Z/gKJmAwr4JFxAGCjU0EwAA8Bm5Wqw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBP77MxKwiNAhS9hOUfFbs39iIdRY0chvP4qzdQtgW1bPzbAVJReZdqfAeXWYwMtXmKeNSTM3edvlI8DE8fgasMuECpCHdJDkU5hXe5iBnsizPDn7mMy9eEv7MyNfKG8kbphkVTQa39aLTA+mAS6hsH1GAqfqcADPrpqST9m3OmNzcFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HWoL4b+Dew4WpJrSqz5dG2Z/gKJmAwr4JFxAGCjU0EwAA8Bm5Wqw=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBP77MxKwiNAhS9hOUfFbs39iIdRY0chvP4qzdQtgW1bPzbAVJReZdqfAeXWYwMtXmKeNSTM3edvlI8DE8fgasMuECpCHdJDkU5hXe5iBnsizPDn7mMy9eEv7MyNfKG8kbphkVTQa39aLTA+mAS6hsH1GAqfqcADPrpqST9m3OmNzcFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HWoL4b+Dew4WpJrSqz5dG2Z/gKJmAwr4JFxAGCjU0EwAA8Bm5Wqw=="
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": 214
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 214
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 214,
      "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": 214
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 214
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 214,
      "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 215,
      "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gdeg6O06FYHVVdSMeY0hfIYA3ZM3j9phivExXql4w+uHRe5ZAJwl",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "signed_tx": "tx_+JELAfhCuECFNk49VRVguqUecU233FVohEtZ4FZ1i0gqYBRo1Y5Phd5KfgLv5o33NpvTjXvS01z9dC7p3JuyRSzSxFwoScAFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HXoOjtOhWB1VXUjHmNIXyGAN2TN4/aYYrxMV6peMPrh0Xudsfu1w=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuECFNk49VRVguqUecU233FVohEtZ4FZ1i0gqYBRo1Y5Phd5KfgLv5o33NpvTjXvS01z9dC7p3JuyRSzSxFwoScAFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HXoOjtOhWB1VXUjHmNIXyGAN2TN4/aYYrxMV6peMPrh0Xudsfu1w==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "signed_tx": "tx_+NMLAfiEuEBB7VesSXwpQfvXDs7mT58AsS2DmbxM2fKCW7Hz0tz/f/vOX2XtTIXsuM0tiKZEcO0pjO98S5BENUm+5igt4eEKuECFNk49VRVguqUecU233FVohEtZ4FZ1i0gqYBRo1Y5Phd5KfgLv5o33NpvTjXvS01z9dC7p3JuyRSzSxFwoScAFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HXoOjtOhWB1VXUjHmNIXyGAN2TN4/aYYrxMV6peMPrh0Xuq0utmA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBB7VesSXwpQfvXDs7mT58AsS2DmbxM2fKCW7Hz0tz/f/vOX2XtTIXsuM0tiKZEcO0pjO98S5BENUm+5igt4eEKuECFNk49VRVguqUecU233FVohEtZ4FZ1i0gqYBRo1Y5Phd5KfgLv5o33NpvTjXvS01z9dC7p3JuyRSzSxFwoScAFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HXoOjtOhWB1VXUjHmNIXyGAN2TN4/aYYrxMV6peMPrh0Xuq0utmA=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBB7VesSXwpQfvXDs7mT58AsS2DmbxM2fKCW7Hz0tz/f/vOX2XtTIXsuM0tiKZEcO0pjO98S5BENUm+5igt4eEKuECFNk49VRVguqUecU233FVohEtZ4FZ1i0gqYBRo1Y5Phd5KfgLv5o33NpvTjXvS01z9dC7p3JuyRSzSxFwoScAFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HXoOjtOhWB1VXUjHmNIXyGAN2TN4/aYYrxMV6peMPrh0Xuq0utmA=="
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": 215
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 215
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 215,
      "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": 215
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 215
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 215,
      "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 216,
      "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gdigWS21t6AA3QscAD8QQ6u49ala6PFwA2ZjlIaJvB3sxdXoMFib",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "signed_tx": "tx_+JELAfhCuEDvTo6G7OGISzau5nB/iRANcefx702rrWF64pA/CUAWAViHhaRI7lrkOnoCKCvQWsQ/Df5zxVah2u8/HSwOuGwCuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HYoFkttbegAN0LHAA/EEOruPWpWujxcANmY5SGibwd7MXVnvZA4Q=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEDvTo6G7OGISzau5nB/iRANcefx702rrWF64pA/CUAWAViHhaRI7lrkOnoCKCvQWsQ/Df5zxVah2u8/HSwOuGwCuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HYoFkttbegAN0LHAA/EEOruPWpWujxcANmY5SGibwd7MXVnvZA4Q==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "signed_tx": "tx_+NMLAfiEuECIbyZe0wCYxHlh+Sf81h3HrZPkcEFOgyqGafBs20LRGVxY4rnYzuoCfUi17nOMKckfzXutLVnDj+fyE7+MbxEIuEDvTo6G7OGISzau5nB/iRANcefx702rrWF64pA/CUAWAViHhaRI7lrkOnoCKCvQWsQ/Df5zxVah2u8/HSwOuGwCuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HYoFkttbegAN0LHAA/EEOruPWpWujxcANmY5SGibwd7MXVJtdK4Q=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuECIbyZe0wCYxHlh+Sf81h3HrZPkcEFOgyqGafBs20LRGVxY4rnYzuoCfUi17nOMKckfzXutLVnDj+fyE7+MbxEIuEDvTo6G7OGISzau5nB/iRANcefx702rrWF64pA/CUAWAViHhaRI7lrkOnoCKCvQWsQ/Df5zxVah2u8/HSwOuGwCuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HYoFkttbegAN0LHAA/EEOruPWpWujxcANmY5SGibwd7MXVJtdK4Q=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuECIbyZe0wCYxHlh+Sf81h3HrZPkcEFOgyqGafBs20LRGVxY4rnYzuoCfUi17nOMKckfzXutLVnDj+fyE7+MbxEIuEDvTo6G7OGISzau5nB/iRANcefx702rrWF64pA/CUAWAViHhaRI7lrkOnoCKCvQWsQ/Df5zxVah2u8/HSwOuGwCuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HYoFkttbegAN0LHAA/EEOruPWpWujxcANmY5SGibwd7MXVJtdK4Q=="
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": 216
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 216
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 216,
      "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": 216
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 216
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 216,
      "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 217,
      "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gdmgTgDgp+7DEGfrhNXvz6R7ZJf17e4BJKmrgcTX9uJZ8oVx61II",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "signed_tx": "tx_+JELAfhCuEBzmSFk84G1zN9jM+aA5nSzQZ0/hFwGBw+RXdNlYM5o2XLEZu71tT5g+BJ6XcvVFtKBNW4iRe5NvY+nn+be3ocIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HZoE4A4KfuwxBn64TV78+ke2SX9e3uASSpq4HE1/biWfKF/IYowA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEBzmSFk84G1zN9jM+aA5nSzQZ0/hFwGBw+RXdNlYM5o2XLEZu71tT5g+BJ6XcvVFtKBNW4iRe5NvY+nn+be3ocIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HZoE4A4KfuwxBn64TV78+ke2SX9e3uASSpq4HE1/biWfKF/IYowA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "signed_tx": "tx_+NMLAfiEuEBzmSFk84G1zN9jM+aA5nSzQZ0/hFwGBw+RXdNlYM5o2XLEZu71tT5g+BJ6XcvVFtKBNW4iRe5NvY+nn+be3ocIuECxahFpjS+ksyQ3YBAkb4B7mXsBQ8Nj8igXXZSvLZ7s4eO4NUPlrg8BDvEFUsKUdmwnPfDLHIyf526KQ3yUojcMuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HZoE4A4KfuwxBn64TV78+ke2SX9e3uASSpq4HE1/biWfKFN9DUIg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBzmSFk84G1zN9jM+aA5nSzQZ0/hFwGBw+RXdNlYM5o2XLEZu71tT5g+BJ6XcvVFtKBNW4iRe5NvY+nn+be3ocIuECxahFpjS+ksyQ3YBAkb4B7mXsBQ8Nj8igXXZSvLZ7s4eO4NUPlrg8BDvEFUsKUdmwnPfDLHIyf526KQ3yUojcMuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HZoE4A4KfuwxBn64TV78+ke2SX9e3uASSpq4HE1/biWfKFN9DUIg=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBzmSFk84G1zN9jM+aA5nSzQZ0/hFwGBw+RXdNlYM5o2XLEZu71tT5g+BJ6XcvVFtKBNW4iRe5NvY+nn+be3ocIuECxahFpjS+ksyQ3YBAkb4B7mXsBQ8Nj8igXXZSvLZ7s4eO4NUPlrg8BDvEFUsKUdmwnPfDLHIyf526KQ3yUojcMuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HZoE4A4KfuwxBn64TV78+ke2SX9e3uASSpq4HE1/biWfKFN9DUIg=="
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": 217
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 217
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 217,
      "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": 217
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 217
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 217,
      "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
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
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 218,
      "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gdqgEq6aOoC/kh9xqVtcGh4x0RZ0xStZtmWHVuvvCbhjwRLAH32V",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "signed_tx": "tx_+JELAfhCuECxDkyIxCv/DXWonfofJHtiYvgTtkhLhNIsLOH9rHESq5PIT/iFHeCEXYbgWuPVlzRH27ndE3lf7rbqFAHsYYcPuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HaoBKumjqAv5IfcalbXBoeMdEWdMUrWbZlh1br7wm4Y8ES/iSu4Q=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuECxDkyIxCv/DXWonfofJHtiYvgTtkhLhNIsLOH9rHESq5PIT/iFHeCEXYbgWuPVlzRH27ndE3lf7rbqFAHsYYcPuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HaoBKumjqAv5IfcalbXBoeMdEWdMUrWbZlh1br7wm4Y8ES/iSu4Q==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "signed_tx": "tx_+NMLAfiEuEA8CVx/HRT1D5pPxMGm/8QJko/5YRB8vkwmxGOelDSt+VBr+I/wZrJdQkYzDIjBAxmV01PxklIpwTVgE0ES1T8CuECxDkyIxCv/DXWonfofJHtiYvgTtkhLhNIsLOH9rHESq5PIT/iFHeCEXYbgWuPVlzRH27ndE3lf7rbqFAHsYYcPuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HaoBKumjqAv5IfcalbXBoeMdEWdMUrWbZlh1br7wm4Y8ESrxMUlw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEA8CVx/HRT1D5pPxMGm/8QJko/5YRB8vkwmxGOelDSt+VBr+I/wZrJdQkYzDIjBAxmV01PxklIpwTVgE0ES1T8CuECxDkyIxCv/DXWonfofJHtiYvgTtkhLhNIsLOH9rHESq5PIT/iFHeCEXYbgWuPVlzRH27ndE3lf7rbqFAHsYYcPuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HaoBKumjqAv5IfcalbXBoeMdEWdMUrWbZlh1br7wm4Y8ESrxMUlw=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEA8CVx/HRT1D5pPxMGm/8QJko/5YRB8vkwmxGOelDSt+VBr+I/wZrJdQkYzDIjBAxmV01PxklIpwTVgE0ES1T8CuECxDkyIxCv/DXWonfofJHtiYvgTtkhLhNIsLOH9rHESq5PIT/iFHeCEXYbgWuPVlzRH27ndE3lf7rbqFAHsYYcPuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HaoBKumjqAv5IfcalbXBoeMdEWdMUrWbZlh1br7wm4Y8ESrxMUlw=="
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
    "round": 218
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 218
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 218,
      "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
    "round": 218
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 218
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 218,
      "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
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
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 219,
      "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gdugNarlbnPnGuqiFtKKOYKiFxO0jWifQCsYiT9vJGuY80caPPX2",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "signed_tx": "tx_+JELAfhCuECmpIPxDZfZnrqgbQP72Qr4q4gp64njxLeHghse4UAMTM/s16n5MAL3kHK3l9bkdTE+GotvyX3uAXfuunl1n2IEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HboDWq5W5z5xrqohbSijmCohcTtI1on0ArGIk/byRrmPNHmrD7gw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuECmpIPxDZfZnrqgbQP72Qr4q4gp64njxLeHghse4UAMTM/s16n5MAL3kHK3l9bkdTE+GotvyX3uAXfuunl1n2IEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HboDWq5W5z5xrqohbSijmCohcTtI1on0ArGIk/byRrmPNHmrD7gw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8VJfP+mM=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "signed_tx": "tx_+NMLAfiEuECmpIPxDZfZnrqgbQP72Qr4q4gp64njxLeHghse4UAMTM/s16n5MAL3kHK3l9bkdTE+GotvyX3uAXfuunl1n2IEuEDDpBeGNxTKfZ6X/LPIaH7EOx7LP+6MlVMVpZGsbof8xrtDKeaQXVvo7KGythqIzPwqWfjlYnW82NBWzNivDrwNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HboDWq5W5z5xrqohbSijmCohcTtI1on0ArGIk/byRrmPNHMOEiow=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuECmpIPxDZfZnrqgbQP72Qr4q4gp64njxLeHghse4UAMTM/s16n5MAL3kHK3l9bkdTE+GotvyX3uAXfuunl1n2IEuEDDpBeGNxTKfZ6X/LPIaH7EOx7LP+6MlVMVpZGsbof8xrtDKeaQXVvo7KGythqIzPwqWfjlYnW82NBWzNivDrwNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HboDWq5W5z5xrqohbSijmCohcTtI1on0ArGIk/byRrmPNHMOEiow=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuECmpIPxDZfZnrqgbQP72Qr4q4gp64njxLeHghse4UAMTM/s16n5MAL3kHK3l9bkdTE+GotvyX3uAXfuunl1n2IEuEDDpBeGNxTKfZ6X/LPIaH7EOx7LP+6MlVMVpZGsbof8xrtDKeaQXVvo7KGythqIzPwqWfjlYnW82NBWzNivDrwNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HboDWq5W5z5xrqohbSijmCohcTtI1on0ArGIk/byRrmPNHMOEiow=="
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
    "round": 219
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 219
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 219,
      "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
    "round": 219
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 219
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 219,
      "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
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
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 220,
      "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gdyg48En3MS3L1BszWPlTob/caax5Wmy3NGtOblW27eUxbIo1zAg",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "signed_tx": "tx_+JELAfhCuEAW6aJDDFk0MlhgljKEyZmRssG3bWcCRTrx3VKPrPcw42G2Ni6sgk4I+y8as1nvEGu/EUUy2W4v9XQSQBqtgvkPuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HcoOPBJ9zEty9QbM1j5U6G/3GmseVpstzRrTm5Vtu3lMWyP2YmlA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEAW6aJDDFk0MlhgljKEyZmRssG3bWcCRTrx3VKPrPcw42G2Ni6sgk4I+y8as1nvEGu/EUUy2W4v9XQSQBqtgvkPuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HcoOPBJ9zEty9QbM1j5U6G/3GmseVpstzRrTm5Vtu3lMWyP2YmlA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "signed_tx": "tx_+NMLAfiEuEAW6aJDDFk0MlhgljKEyZmRssG3bWcCRTrx3VKPrPcw42G2Ni6sgk4I+y8as1nvEGu/EUUy2W4v9XQSQBqtgvkPuED769UJBrtkMwUsX4RUHz1XlF6XAOa5UWwNUISQee1hrW0yUQV9KWMe7V6dLXC2qYAvGZqeb3Hu98oWYo4qkCUIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HcoOPBJ9zEty9QbM1j5U6G/3GmseVpstzRrTm5Vtu3lMWyY3HUEA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEAW6aJDDFk0MlhgljKEyZmRssG3bWcCRTrx3VKPrPcw42G2Ni6sgk4I+y8as1nvEGu/EUUy2W4v9XQSQBqtgvkPuED769UJBrtkMwUsX4RUHz1XlF6XAOa5UWwNUISQee1hrW0yUQV9KWMe7V6dLXC2qYAvGZqeb3Hu98oWYo4qkCUIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HcoOPBJ9zEty9QbM1j5U6G/3GmseVpstzRrTm5Vtu3lMWyY3HUEA=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEAW6aJDDFk0MlhgljKEyZmRssG3bWcCRTrx3VKPrPcw42G2Ni6sgk4I+y8as1nvEGu/EUUy2W4v9XQSQBqtgvkPuED769UJBrtkMwUsX4RUHz1XlF6XAOa5UWwNUISQee1hrW0yUQV9KWMe7V6dLXC2qYAvGZqeb3Hu98oWYo4qkCUIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HcoOPBJ9zEty9QbM1j5U6G/3GmseVpstzRrTm5Vtu3lMWyY3HUEA=="
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
    "round": 220
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 220
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 220,
      "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
    "round": 220
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 220
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 220,
      "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
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
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 221,
      "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
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
    "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gd2gBuce5wlgdazxYBe0d31Ju9XENmVb18cGulprR3HwYMoyoBnW",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "signed_tx": "tx_+JELAfhCuECnHAavi43ObiGpCWvijvr1r2SZu+z/1N3DIsNYw7+OnMl3S8y94GGVNWd6SapVXi9vRlnzAR1cGEOpO7zYB7oLuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HdoAbnHucJYHWs8WAXtHd9SbvVxDZlW9fHBrpaa0dx8GDKb2PT4A=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuECnHAavi43ObiGpCWvijvr1r2SZu+z/1N3DIsNYw7+OnMl3S8y94GGVNWd6SapVXi9vRlnzAR1cGEOpO7zYB7oLuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HdoAbnHucJYHWs8WAXtHd9SbvVxDZlW9fHBrpaa0dx8GDKb2PT4A==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoGxzQ9HM4rCWGpF4N6R5t2MEaNp3MFLfnc2tZS5bl3f8Vub1ivc=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "signed_tx": "tx_+NMLAfiEuECMFkKQ95B7OZKGGXMyQ8Jk/EVsJ5aUJUwPo4lStBKr6JtzLs/KE8x4gIFd/JORttakxhHtFUTODYl5Kw3cDSAKuECnHAavi43ObiGpCWvijvr1r2SZu+z/1N3DIsNYw7+OnMl3S8y94GGVNWd6SapVXi9vRlnzAR1cGEOpO7zYB7oLuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HdoAbnHucJYHWs8WAXtHd9SbvVxDZlW9fHBrpaa0dx8GDKdwSTYg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuECMFkKQ95B7OZKGGXMyQ8Jk/EVsJ5aUJUwPo4lStBKr6JtzLs/KE8x4gIFd/JORttakxhHtFUTODYl5Kw3cDSAKuECnHAavi43ObiGpCWvijvr1r2SZu+z/1N3DIsNYw7+OnMl3S8y94GGVNWd6SapVXi9vRlnzAR1cGEOpO7zYB7oLuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HdoAbnHucJYHWs8WAXtHd9SbvVxDZlW9fHBrpaa0dx8GDKdwSTYg=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuECMFkKQ95B7OZKGGXMyQ8Jk/EVsJ5aUJUwPo4lStBKr6JtzLs/KE8x4gIFd/JORttakxhHtFUTODYl5Kw3cDSAKuECnHAavi43ObiGpCWvijvr1r2SZu+z/1N3DIsNYw7+OnMl3S8y94GGVNWd6SapVXi9vRlnzAR1cGEOpO7zYB7oLuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HdoAbnHucJYHWs8WAXtHd9SbvVxDZlW9fHBrpaa0dx8GDKdwSTYg=="
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
    "round": 221
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 221
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 221,
      "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
    "round": 221
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 221
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 221,
      "contract_id": "ct_23L3Diz7sYsvmXZZ64gAUuZtwQAPg4nuC1HmMfnQE91Sxa2sVc",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 222,
      "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gd6gy9YQhn4jJdV4zeeJJTmjel5J93Y5+XGynpFBQA8LNs9h1RlJ",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "signed_tx": "tx_+JELAfhCuEA4o/tLpH7yH+DvvgPdyWAgTLLLZj9f/PtSyR9WaKy2JdUtPZRQRVSOS9CAykGH5uQkQwi+GPJPXyZF6+Ou/eoBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HeoMvWEIZ+IyXVeM3niSU5o3peSfd2Oflxsp6RQUAPCzbPTv0A/Q=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEA4o/tLpH7yH+DvvgPdyWAgTLLLZj9f/PtSyR9WaKy2JdUtPZRQRVSOS9CAykGH5uQkQwi+GPJPXyZF6+Ou/eoBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HeoMvWEIZ+IyXVeM3niSU5o3peSfd2Oflxsp6RQUAPCzbPTv0A/Q==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "signed_tx": "tx_+NMLAfiEuEA4o/tLpH7yH+DvvgPdyWAgTLLLZj9f/PtSyR9WaKy2JdUtPZRQRVSOS9CAykGH5uQkQwi+GPJPXyZF6+Ou/eoBuECzHM+rZMg81WBlexQnLL4NiB19XqK/52XlY9Ei2EAvIV0IV3gO4sTSHH7GkE8nYvsaIUp/ky7ijpWiNveqBFANuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HeoMvWEIZ+IyXVeM3niSU5o3peSfd2Oflxsp6RQUAPCzbP/YI7bA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEA4o/tLpH7yH+DvvgPdyWAgTLLLZj9f/PtSyR9WaKy2JdUtPZRQRVSOS9CAykGH5uQkQwi+GPJPXyZF6+Ou/eoBuECzHM+rZMg81WBlexQnLL4NiB19XqK/52XlY9Ei2EAvIV0IV3gO4sTSHH7GkE8nYvsaIUp/ky7ijpWiNveqBFANuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HeoMvWEIZ+IyXVeM3niSU5o3peSfd2Oflxsp6RQUAPCzbP/YI7bA=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEA4o/tLpH7yH+DvvgPdyWAgTLLLZj9f/PtSyR9WaKy2JdUtPZRQRVSOS9CAykGH5uQkQwi+GPJPXyZF6+Ou/eoBuECzHM+rZMg81WBlexQnLL4NiB19XqK/52XlY9Ei2EAvIV0IV3gO4sTSHH7GkE8nYvsaIUp/ky7ijpWiNveqBFANuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HeoMvWEIZ+IyXVeM3niSU5o3peSfd2Oflxsp6RQUAPCzbP/YI7bA=="
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": 222
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 222
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 222,
      "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": 222
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 222
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 222,
      "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 223,
      "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gd+gRRT8doQWDMkzgL6qEkFGdAavEZ/Hz9RWY89bK860P+FiJiDC",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "signed_tx": "tx_+JELAfhCuEB8Z3i8GWIJyLyzT1VQAYlYcKcpGRtUw8QYYyTwf3VqSy+Y2qptvShKKFobhS6KHwBzHI3hnbA3a5zQg42r3AUKuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HfoEUU/HaEFgzJM4C+qhJBRnQGrxGfx8/UVmPPWyvOtD/hgFf7UA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEB8Z3i8GWIJyLyzT1VQAYlYcKcpGRtUw8QYYyTwf3VqSy+Y2qptvShKKFobhS6KHwBzHI3hnbA3a5zQg42r3AUKuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HfoEUU/HaEFgzJM4C+qhJBRnQGrxGfx8/UVmPPWyvOtD/hgFf7UA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "signed_tx": "tx_+NMLAfiEuEB8Z3i8GWIJyLyzT1VQAYlYcKcpGRtUw8QYYyTwf3VqSy+Y2qptvShKKFobhS6KHwBzHI3hnbA3a5zQg42r3AUKuEDKRG+ffW8rayMbXaf78lD5yA1MKfM5xj8LxJ+VCNpqOleuwhIDobUq2AYvTXTCcTRs+FpfKdWLf2qJD0SLf9QMuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HfoEUU/HaEFgzJM4C+qhJBRnQGrxGfx8/UVmPPWyvOtD/hKKTF4A=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEB8Z3i8GWIJyLyzT1VQAYlYcKcpGRtUw8QYYyTwf3VqSy+Y2qptvShKKFobhS6KHwBzHI3hnbA3a5zQg42r3AUKuEDKRG+ffW8rayMbXaf78lD5yA1MKfM5xj8LxJ+VCNpqOleuwhIDobUq2AYvTXTCcTRs+FpfKdWLf2qJD0SLf9QMuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HfoEUU/HaEFgzJM4C+qhJBRnQGrxGfx8/UVmPPWyvOtD/hKKTF4A=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEB8Z3i8GWIJyLyzT1VQAYlYcKcpGRtUw8QYYyTwf3VqSy+Y2qptvShKKFobhS6KHwBzHI3hnbA3a5zQg42r3AUKuEDKRG+ffW8rayMbXaf78lD5yA1MKfM5xj8LxJ+VCNpqOleuwhIDobUq2AYvTXTCcTRs+FpfKdWLf2qJD0SLf9QMuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HfoEUU/HaEFgzJM4C+qhJBRnQGrxGfx8/UVmPPWyvOtD/hKKTF4A=="
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": 223
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 223
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 223,
      "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
    "round": 223
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 223
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 223,
      "contract_id": "ct_pmDYCqMTYPkZHHM3y5mrRP1Fc9PR8Rn6PnNktY8x5ukjzascM",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53geCgrIfWSjJUBCmFViZvM7OEun3839BZbyuEfUIy4MxiM58Og9GY",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "signed_tx": "tx_+JELAfhCuEAFDWnLwZ7W8lw1ePRwiSaH2tZkc0d8myQ7SiC6PQ1uqci7wbUF3Kt8jPAGC4ErW60x/oLsN7g/1+1AvkVGVZAIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HgoKyH1koyVAQphVYmbzOzhLp9/N/QWW8rhH1CMuDMYjOfTyLCEw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEAFDWnLwZ7W8lw1ePRwiSaH2tZkc0d8myQ7SiC6PQ1uqci7wbUF3Kt8jPAGC4ErW60x/oLsN7g/1+1AvkVGVZAIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HgoKyH1koyVAQphVYmbzOzhLp9/N/QWW8rhH1CMuDMYjOfTyLCEw==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "signed_tx": "tx_+NMLAfiEuEAFDWnLwZ7W8lw1ePRwiSaH2tZkc0d8myQ7SiC6PQ1uqci7wbUF3Kt8jPAGC4ErW60x/oLsN7g/1+1AvkVGVZAIuEAqauM0Ksxz6Xh1Y5EP+TccwE8yrAfR1WDVIq0SXDT2iqD5g+oeps0plIxSuaE1xm0jbskeBCg8+HLpfz3IFdcIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HgoKyH1koyVAQphVYmbzOzhLp9/N/QWW8rhH1CMuDMYjOfLcUVbQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEAFDWnLwZ7W8lw1ePRwiSaH2tZkc0d8myQ7SiC6PQ1uqci7wbUF3Kt8jPAGC4ErW60x/oLsN7g/1+1AvkVGVZAIuEAqauM0Ksxz6Xh1Y5EP+TccwE8yrAfR1WDVIq0SXDT2iqD5g+oeps0plIxSuaE1xm0jbskeBCg8+HLpfz3IFdcIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HgoKyH1koyVAQphVYmbzOzhLp9/N/QWW8rhH1CMuDMYjOfLcUVbQ=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEAFDWnLwZ7W8lw1ePRwiSaH2tZkc0d8myQ7SiC6PQ1uqci7wbUF3Kt8jPAGC4ErW60x/oLsN7g/1+1AvkVGVZAIuEAqauM0Ksxz6Xh1Y5EP+TccwE8yrAfR1WDVIq0SXDT2iqD5g+oeps0plIxSuaE1xm0jbskeBCg8+HLpfz3IFdcIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HgoKyH1koyVAQphVYmbzOzhLp9/N/QWW8rhH1CMuDMYjOfLcUVbQ=="
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53geGgaAa/yo5T0Dx4Yse+GnyLwgDglnN0opttcX8NdAHfsj+D0Imr",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "signed_tx": "tx_+JELAfhCuEB4Ro8mjjPb0PQGJOLM8GkP+cMrny+4diiJP6Z5aLS/GsMPdMMH1A3vYuELQFX3bWPEz/CtWAEZRbVwL4OQT2YJuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HhoGgGv8qOU9A8eGLHvhp8i8IA4JZzdKKbbXF/DXQB37I/coZCiQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEB4Ro8mjjPb0PQGJOLM8GkP+cMrny+4diiJP6Z5aLS/GsMPdMMH1A3vYuELQFX3bWPEz/CtWAEZRbVwL4OQT2YJuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HhoGgGv8qOU9A8eGLHvhp8i8IA4JZzdKKbbXF/DXQB37I/coZCiQ==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "signed_tx": "tx_+NMLAfiEuEAc74tEkCjwb5qX9G+DZF3p6cwyE9XRKNQa4i/XsY9+/P9OFI5fn+7mI0HGXL92+bfnfMgqYfxC0mTSBacw+mUHuEB4Ro8mjjPb0PQGJOLM8GkP+cMrny+4diiJP6Z5aLS/GsMPdMMH1A3vYuELQFX3bWPEz/CtWAEZRbVwL4OQT2YJuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HhoGgGv8qOU9A8eGLHvhp8i8IA4JZzdKKbbXF/DXQB37I/h7k94w=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEAc74tEkCjwb5qX9G+DZF3p6cwyE9XRKNQa4i/XsY9+/P9OFI5fn+7mI0HGXL92+bfnfMgqYfxC0mTSBacw+mUHuEB4Ro8mjjPb0PQGJOLM8GkP+cMrny+4diiJP6Z5aLS/GsMPdMMH1A3vYuELQFX3bWPEz/CtWAEZRbVwL4OQT2YJuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HhoGgGv8qOU9A8eGLHvhp8i8IA4JZzdKKbbXF/DXQB37I/h7k94w=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEAc74tEkCjwb5qX9G+DZF3p6cwyE9XRKNQa4i/XsY9+/P9OFI5fn+7mI0HGXL92+bfnfMgqYfxC0mTSBacw+mUHuEB4Ro8mjjPb0PQGJOLM8GkP+cMrny+4diiJP6Z5aLS/GsMPdMMH1A3vYuELQFX3bWPEz/CtWAEZRbVwL4OQT2YJuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HhoGgGv8qOU9A8eGLHvhp8i8IA4JZzdKKbbXF/DXQB37I/h7k94w=="
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 226,
      "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53geKgb9qKEHme+QBU6tnYS+07aK+iBZdBUKb8orDG/iNwwWiroDsx",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "signed_tx": "tx_+JELAfhCuEDyllxDyPZcwalhT1vqzaAJ78gJvYjotBXjMrjojhQtR8S/tSponVPxp3RMjKjoqL0G8lMZWPL+qimoU0IHG/EHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HioG/aihB5nvkAVOrZ2EvtO2ivogWXQVCm/KKwxv4jcMFolivMKw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEDyllxDyPZcwalhT1vqzaAJ78gJvYjotBXjMrjojhQtR8S/tSponVPxp3RMjKjoqL0G8lMZWPL+qimoU0IHG/EHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HioG/aihB5nvkAVOrZ2EvtO2ivogWXQVCm/KKwxv4jcMFolivMKw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "signed_tx": "tx_+NMLAfiEuEBu3YCjBh7RVjdE2GG254qX8cWQqDKf5MTRAu7ksxZfqRN4RnFfSsYvYDjBn5gHo3m1bKL1s8xT+y5/d385tQAGuEDyllxDyPZcwalhT1vqzaAJ78gJvYjotBXjMrjojhQtR8S/tSponVPxp3RMjKjoqL0G8lMZWPL+qimoU0IHG/EHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HioG/aihB5nvkAVOrZ2EvtO2ivogWXQVCm/KKwxv4jcMFoB1iMyA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBu3YCjBh7RVjdE2GG254qX8cWQqDKf5MTRAu7ksxZfqRN4RnFfSsYvYDjBn5gHo3m1bKL1s8xT+y5/d385tQAGuEDyllxDyPZcwalhT1vqzaAJ78gJvYjotBXjMrjojhQtR8S/tSponVPxp3RMjKjoqL0G8lMZWPL+qimoU0IHG/EHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HioG/aihB5nvkAVOrZ2EvtO2ivogWXQVCm/KKwxv4jcMFoB1iMyA=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBu3YCjBh7RVjdE2GG254qX8cWQqDKf5MTRAu7ksxZfqRN4RnFfSsYvYDjBn5gHo3m1bKL1s8xT+y5/d385tQAGuEDyllxDyPZcwalhT1vqzaAJ78gJvYjotBXjMrjojhQtR8S/tSponVPxp3RMjKjoqL0G8lMZWPL+qimoU0IHG/EHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HioG/aihB5nvkAVOrZ2EvtO2ivogWXQVCm/KKwxv4jcMFoB1iMyA=="
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": 226
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 226
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 226,
      "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": 226
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 226
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 226,
      "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 227,
      "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53geOg1qAks22rOKljxGQgZpp78PZx+d5RaSm5A2yycVbx65kKaPoN",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "signed_tx": "tx_+JELAfhCuECIPhcOqMU/1WzVTMohTEPoUycXceINU0nYLBY6lcVCUAe1U/GID45jvP+PwENpATbwJZLNUx+wt6SaqmHsQJUBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HjoNagJLNtqzipY8RkIGaae/D2cfneUWkpuQNssnFW8euZ4F67Vw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuECIPhcOqMU/1WzVTMohTEPoUycXceINU0nYLBY6lcVCUAe1U/GID45jvP+PwENpATbwJZLNUx+wt6SaqmHsQJUBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HjoNagJLNtqzipY8RkIGaae/D2cfneUWkpuQNssnFW8euZ4F67Vw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "signed_tx": "tx_+NMLAfiEuEB5rJqQ+ysFOaRavTqfC88IqGiVXGbDZc+UHOD1deQAp3CZUCgowr/oyKRzFD/2T4ppTmFKVX3Dayx3r66ZEmILuECIPhcOqMU/1WzVTMohTEPoUycXceINU0nYLBY6lcVCUAe1U/GID45jvP+PwENpATbwJZLNUx+wt6SaqmHsQJUBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HjoNagJLNtqzipY8RkIGaae/D2cfneUWkpuQNssnFW8euZbqjqbw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEB5rJqQ+ysFOaRavTqfC88IqGiVXGbDZc+UHOD1deQAp3CZUCgowr/oyKRzFD/2T4ppTmFKVX3Dayx3r66ZEmILuECIPhcOqMU/1WzVTMohTEPoUycXceINU0nYLBY6lcVCUAe1U/GID45jvP+PwENpATbwJZLNUx+wt6SaqmHsQJUBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HjoNagJLNtqzipY8RkIGaae/D2cfneUWkpuQNssnFW8euZbqjqbw=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEB5rJqQ+ysFOaRavTqfC88IqGiVXGbDZc+UHOD1deQAp3CZUCgowr/oyKRzFD/2T4ppTmFKVX3Dayx3r66ZEmILuECIPhcOqMU/1WzVTMohTEPoUycXceINU0nYLBY6lcVCUAe1U/GID45jvP+PwENpATbwJZLNUx+wt6SaqmHsQJUBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HjoNagJLNtqzipY8RkIGaae/D2cfneUWkpuQNssnFW8euZbqjqbw=="
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": 227
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 227
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 227,
      "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": 227
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 227
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 227,
      "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 228,
      "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53geSg6ORnlmOHyz+djrBzD/gu9PFr5a40DENPlDsQ8sm/FYr5IncC",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "signed_tx": "tx_+JELAfhCuECBPcQBqEOSdywJOj9lz/Lz08dB+DKBpDORlQXR3pi0ohRTBpaRSZYQWOk0Guwl9alFLrBBX38tiYPzVpAROOMDuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HkoOjkZ5Zjh8s/nY6wcw/4LvTxa+WuNAxDT5Q7EPLJvxWK3fJyKw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuECBPcQBqEOSdywJOj9lz/Lz08dB+DKBpDORlQXR3pi0ohRTBpaRSZYQWOk0Guwl9alFLrBBX38tiYPzVpAROOMDuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HkoOjkZ5Zjh8s/nY6wcw/4LvTxa+WuNAxDT5Q7EPLJvxWK3fJyKw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "signed_tx": "tx_+NMLAfiEuEAxRoaDsO5ck2qL+f+HdYvSn1cdP/Zkf2t9iO+PnWaXecKhuL10ww2sbxngVNa8YqEG94Uo4VBENjyIwWv+ld4PuECBPcQBqEOSdywJOj9lz/Lz08dB+DKBpDORlQXR3pi0ohRTBpaRSZYQWOk0Guwl9alFLrBBX38tiYPzVpAROOMDuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HkoOjkZ5Zjh8s/nY6wcw/4LvTxa+WuNAxDT5Q7EPLJvxWKwi5h1w=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEAxRoaDsO5ck2qL+f+HdYvSn1cdP/Zkf2t9iO+PnWaXecKhuL10ww2sbxngVNa8YqEG94Uo4VBENjyIwWv+ld4PuECBPcQBqEOSdywJOj9lz/Lz08dB+DKBpDORlQXR3pi0ohRTBpaRSZYQWOk0Guwl9alFLrBBX38tiYPzVpAROOMDuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HkoOjkZ5Zjh8s/nY6wcw/4LvTxa+WuNAxDT5Q7EPLJvxWKwi5h1w=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEAxRoaDsO5ck2qL+f+HdYvSn1cdP/Zkf2t9iO+PnWaXecKhuL10ww2sbxngVNa8YqEG94Uo4VBENjyIwWv+ld4PuECBPcQBqEOSdywJOj9lz/Lz08dB+DKBpDORlQXR3pi0ohRTBpaRSZYQWOk0Guwl9alFLrBBX38tiYPzVpAROOMDuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HkoOjkZ5Zjh8s/nY6wcw/4LvTxa+WuNAxDT5Q7EPLJvxWKwi5h1w=="
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": 228
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 228
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 228,
      "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": 228
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 228
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 228,
      "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 229,
      "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53geWggEBdrbA9EYM05Cc00wMpbZ9tN9Fokxg/3oGwmI+B8o6xw4rZ",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "signed_tx": "tx_+JELAfhCuEB6dzF2COlxZEL7SkeohkgQW2gEgByYGA/anqdIqIUrC1gGeFhplOBgfmR50pT15hCFwmisthyulR99JtLfGSoAuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HloIBAXa2wPRGDNOQnNNMDKW2fbTfRaJMYP96BsJiPgfKOM8hGbQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEB6dzF2COlxZEL7SkeohkgQW2gEgByYGA/anqdIqIUrC1gGeFhplOBgfmR50pT15hCFwmisthyulR99JtLfGSoAuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HloIBAXa2wPRGDNOQnNNMDKW2fbTfRaJMYP96BsJiPgfKOM8hGbQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "signed_tx": "tx_+NMLAfiEuEBUzuqQByVog3VJ5llSr4NFUWvRMaBWsGWNPQWWffzNftIiF+y7XRwnaz9yWDPM0hGRoxmmwd8PGt0Gd8Z31DkFuEB6dzF2COlxZEL7SkeohkgQW2gEgByYGA/anqdIqIUrC1gGeFhplOBgfmR50pT15hCFwmisthyulR99JtLfGSoAuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HloIBAXa2wPRGDNOQnNNMDKW2fbTfRaJMYP96BsJiPgfKOOPa7vw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBUzuqQByVog3VJ5llSr4NFUWvRMaBWsGWNPQWWffzNftIiF+y7XRwnaz9yWDPM0hGRoxmmwd8PGt0Gd8Z31DkFuEB6dzF2COlxZEL7SkeohkgQW2gEgByYGA/anqdIqIUrC1gGeFhplOBgfmR50pT15hCFwmisthyulR99JtLfGSoAuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HloIBAXa2wPRGDNOQnNNMDKW2fbTfRaJMYP96BsJiPgfKOOPa7vw=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBUzuqQByVog3VJ5llSr4NFUWvRMaBWsGWNPQWWffzNftIiF+y7XRwnaz9yWDPM0hGRoxmmwd8PGt0Gd8Z31DkFuEB6dzF2COlxZEL7SkeohkgQW2gEgByYGA/anqdIqIUrC1gGeFhplOBgfmR50pT15hCFwmisthyulR99JtLfGSoAuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HloIBAXa2wPRGDNOQnNNMDKW2fbTfRaJMYP96BsJiPgfKOOPa7vw=="
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": 229
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 229
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 229,
      "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": 229
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 229
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 229,
      "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
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
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 230,
      "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53geagoDC96iqBapemj1AS6Mq9p1292AhoRUHE5HHmOvjCVAh0VaR/",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "signed_tx": "tx_+JELAfhCuEBOf9pP3gmV1+6ri44RGEvEHZarvmt3L86cTHv3l3LqmZTUHgsBg8a1VvA/zPFJX+7tq2Fiw5O9XcjZhQIRFGcLuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HmoKAwveoqgWqXpo9QEujKvaddvdgIaEVBxORx5jr4wlQI/zLsMA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEBOf9pP3gmV1+6ri44RGEvEHZarvmt3L86cTHv3l3LqmZTUHgsBg8a1VvA/zPFJX+7tq2Fiw5O9XcjZhQIRFGcLuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HmoKAwveoqgWqXpo9QEujKvaddvdgIaEVBxORx5jr4wlQI/zLsMA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "signed_tx": "tx_+NMLAfiEuEBOf9pP3gmV1+6ri44RGEvEHZarvmt3L86cTHv3l3LqmZTUHgsBg8a1VvA/zPFJX+7tq2Fiw5O9XcjZhQIRFGcLuEC4VdnQqRX7jTMXmf4WR0RVfoEIRQO/ODgyiGgGuGiEk8hqWWfqAEii1UcJkHvA3+Nv91yvMgA+zrtTNlS5uJYNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HmoKAwveoqgWqXpo9QEujKvaddvdgIaEVBxORx5jr4wlQIuzAHPg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBOf9pP3gmV1+6ri44RGEvEHZarvmt3L86cTHv3l3LqmZTUHgsBg8a1VvA/zPFJX+7tq2Fiw5O9XcjZhQIRFGcLuEC4VdnQqRX7jTMXmf4WR0RVfoEIRQO/ODgyiGgGuGiEk8hqWWfqAEii1UcJkHvA3+Nv91yvMgA+zrtTNlS5uJYNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HmoKAwveoqgWqXpo9QEujKvaddvdgIaEVBxORx5jr4wlQIuzAHPg=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBOf9pP3gmV1+6ri44RGEvEHZarvmt3L86cTHv3l3LqmZTUHgsBg8a1VvA/zPFJX+7tq2Fiw5O9XcjZhQIRFGcLuEC4VdnQqRX7jTMXmf4WR0RVfoEIRQO/ODgyiGgGuGiEk8hqWWfqAEii1UcJkHvA3+Nv91yvMgA+zrtTNlS5uJYNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HmoKAwveoqgWqXpo9QEujKvaddvdgIaEVBxORx5jr4wlQIuzAHPg=="
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
    "round": 230
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 230
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 230,
      "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
    "round": 230
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 230
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 230,
      "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
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
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 231,
      "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53geegDcLqbNLhVsAZjVaZ9pwf56NTVZFYrMKCaFdWWk8t0985OJpf",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "signed_tx": "tx_+JELAfhCuEDNhzKr2BJZduortOgfFlvVOpi2+3i/q+xvTtvxRbcHuxjcDcMW4xgx2380LbL8nguggl1sF6mAvSW+WhOVObkBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HnoA3C6mzS4VbAGY1WmfacH+ejU1WRWKzCgmhXVlpPLdPfJ8vG1g=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEDNhzKr2BJZduortOgfFlvVOpi2+3i/q+xvTtvxRbcHuxjcDcMW4xgx2380LbL8nguggl1sF6mAvSW+WhOVObkBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HnoA3C6mzS4VbAGY1WmfacH+ejU1WRWKzCgmhXVlpPLdPfJ8vG1g==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVPtFIHQ=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "signed_tx": "tx_+NMLAfiEuEDILgD/RKM1JF9nquNVgjrL/FQwKO4yMb6kYeo3YdrvoOJJCTMs9i9osZmmXI8zKQRgFl8o1FGdXvlpa4M7BQoOuEDNhzKr2BJZduortOgfFlvVOpi2+3i/q+xvTtvxRbcHuxjcDcMW4xgx2380LbL8nguggl1sF6mAvSW+WhOVObkBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HnoA3C6mzS4VbAGY1WmfacH+ejU1WRWKzCgmhXVlpPLdPfbM19XQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEDILgD/RKM1JF9nquNVgjrL/FQwKO4yMb6kYeo3YdrvoOJJCTMs9i9osZmmXI8zKQRgFl8o1FGdXvlpa4M7BQoOuEDNhzKr2BJZduortOgfFlvVOpi2+3i/q+xvTtvxRbcHuxjcDcMW4xgx2380LbL8nguggl1sF6mAvSW+WhOVObkBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HnoA3C6mzS4VbAGY1WmfacH+ejU1WRWKzCgmhXVlpPLdPfbM19XQ=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEDILgD/RKM1JF9nquNVgjrL/FQwKO4yMb6kYeo3YdrvoOJJCTMs9i9osZmmXI8zKQRgFl8o1FGdXvlpa4M7BQoOuEDNhzKr2BJZduortOgfFlvVOpi2+3i/q+xvTtvxRbcHuxjcDcMW4xgx2380LbL8nguggl1sF6mAvSW+WhOVObkBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HnoA3C6mzS4VbAGY1WmfacH+ejU1WRWKzCgmhXVlpPLdPfbM19XQ=="
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
    "round": 231
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 231
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 231,
      "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
    "round": 231
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 231
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 231,
      "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
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
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 232,
      "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53geigDfnveFvKu9GGx+scjcZY9Z6DNV9t2OL1DvPi5MuknsnM03oi",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "signed_tx": "tx_+JELAfhCuEAEjBQM3osa1oCMUUTfGJEWV80o46uTxXLYm1x6SHvAbHzI0XM7pRDdn/HdvMPL236GqIi/7GwfCGGiMjR93x0AuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HooA3573hbyrvRhsfrHI3GWPWegzVfbdji9Q7z4uTLpJ7J5cGjSw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEAEjBQM3osa1oCMUUTfGJEWV80o46uTxXLYm1x6SHvAbHzI0XM7pRDdn/HdvMPL236GqIi/7GwfCGGiMjR93x0AuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HooA3573hbyrvRhsfrHI3GWPWegzVfbdji9Q7z4uTLpJ7J5cGjSw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "signed_tx": "tx_+NMLAfiEuEAEjBQM3osa1oCMUUTfGJEWV80o46uTxXLYm1x6SHvAbHzI0XM7pRDdn/HdvMPL236GqIi/7GwfCGGiMjR93x0AuEDeQVadFQP1H19fW62h7HAR1iA3zR4PAYtrdSl71hERmhc8/mjNiIqkBXHT9J/7fQBcZV+/FWO5vsL1xzYJVugPuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HooA3573hbyrvRhsfrHI3GWPWegzVfbdji9Q7z4uTLpJ7JPDbj+Q=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEAEjBQM3osa1oCMUUTfGJEWV80o46uTxXLYm1x6SHvAbHzI0XM7pRDdn/HdvMPL236GqIi/7GwfCGGiMjR93x0AuEDeQVadFQP1H19fW62h7HAR1iA3zR4PAYtrdSl71hERmhc8/mjNiIqkBXHT9J/7fQBcZV+/FWO5vsL1xzYJVugPuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HooA3573hbyrvRhsfrHI3GWPWegzVfbdji9Q7z4uTLpJ7JPDbj+Q=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEAEjBQM3osa1oCMUUTfGJEWV80o46uTxXLYm1x6SHvAbHzI0XM7pRDdn/HdvMPL236GqIi/7GwfCGGiMjR93x0AuEDeQVadFQP1H19fW62h7HAR1iA3zR4PAYtrdSl71hERmhc8/mjNiIqkBXHT9J/7fQBcZV+/FWO5vsL1xzYJVugPuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HooA3573hbyrvRhsfrHI3GWPWegzVfbdji9Q7z4uTLpJ7JPDbj+Q=="
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
    "round": 232
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 232
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 232,
      "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
    "round": 232
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 232
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 232,
      "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
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
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 233,
      "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
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
    "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gemg6dvPpXtJVl+7WvxU93kiP9f/EG4VOVnD1oRZQPF1z0/Xnr+C",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "signed_tx": "tx_+JELAfhCuEDt9LR6jC6DiDKDoVUPKxAtc+0M2J92sI0seuU1KZ9qN6Vd4E5sk4ZLgV64Q89pKlBQKkf6g6Qd+OY5s80+ySoDuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HpoOnbz6V7SVZfu1r8VPd5Ij/X/xBuFTlZw9aEWUDxdc9PH0npJw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEDt9LR6jC6DiDKDoVUPKxAtc+0M2J92sI0seuU1KZ9qN6Vd4E5sk4ZLgV64Q89pKlBQKkf6g6Qd+OY5s80+ySoDuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HpoOnbz6V7SVZfu1r8VPd5Ij/X/xBuFTlZw9aEWUDxdc9PH0npJw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoFKi6bPJPZ+1ZyzQ6+FevFfnMCXCWJ/IwjROPmmovsSjVljyyf8=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "signed_tx": "tx_+NMLAfiEuEDeq8eIh8GwOs6QMzHHxVTTypu3pX0hnkSXK6O5wB3MY/jPS3WAo1L6TDLhsgO/n9tLxPD7botStElDbSf2phECuEDt9LR6jC6DiDKDoVUPKxAtc+0M2J92sI0seuU1KZ9qN6Vd4E5sk4ZLgV64Q89pKlBQKkf6g6Qd+OY5s80+ySoDuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HpoOnbz6V7SVZfu1r8VPd5Ij/X/xBuFTlZw9aEWUDxdc9Pf6HcCg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEDeq8eIh8GwOs6QMzHHxVTTypu3pX0hnkSXK6O5wB3MY/jPS3WAo1L6TDLhsgO/n9tLxPD7botStElDbSf2phECuEDt9LR6jC6DiDKDoVUPKxAtc+0M2J92sI0seuU1KZ9qN6Vd4E5sk4ZLgV64Q89pKlBQKkf6g6Qd+OY5s80+ySoDuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HpoOnbz6V7SVZfu1r8VPd5Ij/X/xBuFTlZw9aEWUDxdc9Pf6HcCg=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEDeq8eIh8GwOs6QMzHHxVTTypu3pX0hnkSXK6O5wB3MY/jPS3WAo1L6TDLhsgO/n9tLxPD7botStElDbSf2phECuEDt9LR6jC6DiDKDoVUPKxAtc+0M2J92sI0seuU1KZ9qN6Vd4E5sk4ZLgV64Q89pKlBQKkf6g6Qd+OY5s80+ySoDuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HpoOnbz6V7SVZfu1r8VPd5Ij/X/xBuFTlZw9aEWUDxdc9Pf6HcCg=="
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
    "round": 233
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 233
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 233,
      "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
    "round": 233
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 233
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 233,
      "contract_id": "ct_o4yUnyDZ3Mx4MM43PYjeqT2EfBEwYJk7Ag7bYGYpvmzwYvov6",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 234,
      "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53geqgllKoUrD1g/JY+/kPIO84IeINiN5mtQovLovlxhYMl0xOwPra",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "signed_tx": "tx_+JELAfhCuEDWtEoXpEG6pHINa8hbZ0QgFSCcK/Ld67IvUGsyPB6aHIW63SLzwv/FKy0f+2N1lSNcPOR1Mllpwen1qwgl1+QNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HqoJZSqFKw9YPyWPv5DyDvOCHiDYjeZrUKLy6L5cYWDJdMALxKzA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEDWtEoXpEG6pHINa8hbZ0QgFSCcK/Ld67IvUGsyPB6aHIW63SLzwv/FKy0f+2N1lSNcPOR1Mllpwen1qwgl1+QNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HqoJZSqFKw9YPyWPv5DyDvOCHiDYjeZrUKLy6L5cYWDJdMALxKzA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "signed_tx": "tx_+NMLAfiEuEBwEHQy4dQIbBO1HbQ/xcpFQErKEZjjOUx0kU1tQfxA6pCnAOIWr5hFd4/0SwBL0mENHzuc/N3MagWK/a6n2mQAuEDWtEoXpEG6pHINa8hbZ0QgFSCcK/Ld67IvUGsyPB6aHIW63SLzwv/FKy0f+2N1lSNcPOR1Mllpwen1qwgl1+QNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HqoJZSqFKw9YPyWPv5DyDvOCHiDYjeZrUKLy6L5cYWDJdMeaFhpA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBwEHQy4dQIbBO1HbQ/xcpFQErKEZjjOUx0kU1tQfxA6pCnAOIWr5hFd4/0SwBL0mENHzuc/N3MagWK/a6n2mQAuEDWtEoXpEG6pHINa8hbZ0QgFSCcK/Ld67IvUGsyPB6aHIW63SLzwv/FKy0f+2N1lSNcPOR1Mllpwen1qwgl1+QNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HqoJZSqFKw9YPyWPv5DyDvOCHiDYjeZrUKLy6L5cYWDJdMeaFhpA=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBwEHQy4dQIbBO1HbQ/xcpFQErKEZjjOUx0kU1tQfxA6pCnAOIWr5hFd4/0SwBL0mENHzuc/N3MagWK/a6n2mQAuEDWtEoXpEG6pHINa8hbZ0QgFSCcK/Ld67IvUGsyPB6aHIW63SLzwv/FKy0f+2N1lSNcPOR1Mllpwen1qwgl1+QNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HqoJZSqFKw9YPyWPv5DyDvOCHiDYjeZrUKLy6L5cYWDJdMeaFhpA=="
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": 234
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 234
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 234,
      "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": 234
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 234
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 234,
      "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 235,
      "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53geugiDvhYho/fzBpr8ABL0urEzH34qx5AXUOIgdOrXYOLU1R8hGg",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "signed_tx": "tx_+JELAfhCuEDNbNEzArQjafCCrhs+ABADEQqReVPZ6PL4gv5y5l7fjTfLDkDt2k1Jt1YFVIb0FOBchlzxiq098cZ5pWWP/n0MuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HroIg74WIaP38waa/AAS9LqxMx9+KseQF1DiIHTq12Di1NcAjX0A=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEDNbNEzArQjafCCrhs+ABADEQqReVPZ6PL4gv5y5l7fjTfLDkDt2k1Jt1YFVIb0FOBchlzxiq098cZ5pWWP/n0MuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HroIg74WIaP38waa/AAS9LqxMx9+KseQF1DiIHTq12Di1NcAjX0A==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "signed_tx": "tx_+NMLAfiEuEBzDkcsEwC1Ru9Qg3tQOSfRaPz0ASshIaZSBQLDh3ZBCsnGfGU3PbC7eJ6LGLnBP4nYkKc36xAPnD7ufzQQx8gHuEDNbNEzArQjafCCrhs+ABADEQqReVPZ6PL4gv5y5l7fjTfLDkDt2k1Jt1YFVIb0FOBchlzxiq098cZ5pWWP/n0MuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HroIg74WIaP38waa/AAS9LqxMx9+KseQF1DiIHTq12Di1NECJGVQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBzDkcsEwC1Ru9Qg3tQOSfRaPz0ASshIaZSBQLDh3ZBCsnGfGU3PbC7eJ6LGLnBP4nYkKc36xAPnD7ufzQQx8gHuEDNbNEzArQjafCCrhs+ABADEQqReVPZ6PL4gv5y5l7fjTfLDkDt2k1Jt1YFVIb0FOBchlzxiq098cZ5pWWP/n0MuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HroIg74WIaP38waa/AAS9LqxMx9+KseQF1DiIHTq12Di1NECJGVQ=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBzDkcsEwC1Ru9Qg3tQOSfRaPz0ASshIaZSBQLDh3ZBCsnGfGU3PbC7eJ6LGLnBP4nYkKc36xAPnD7ufzQQx8gHuEDNbNEzArQjafCCrhs+ABADEQqReVPZ6PL4gv5y5l7fjTfLDkDt2k1Jt1YFVIb0FOBchlzxiq098cZ5pWWP/n0MuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HroIg74WIaP38waa/AAS9LqxMx9+KseQF1DiIHTq12Di1NECJGVQ=="
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": 235
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 235
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 235,
      "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
    "round": 235
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 235
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 235,
      "contract_id": "ct_dPqTDYWMmgZMPuLWY1bsnj5mwkbV3e5jj7T3QWoVa5U1v58yi",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53geygFG/tDKs8IWtEwTlIXLIshjyUWy7TNLfp1vu3fC4WroW4ooyD",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "signed_tx": "tx_+JELAfhCuECZo9J1h/75lRhFxst2aElzHlgjImKDeN4j6u2INOVzIR7P2kXfiUTNTxD7KsAI01XtKXeCmJ46dNyz3yivYTMGuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HsoBRv7QyrPCFrRME5SFyyLIY8lFsu0zS36db7t3wuFq6FZCxkmA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuECZo9J1h/75lRhFxst2aElzHlgjImKDeN4j6u2INOVzIR7P2kXfiUTNTxD7KsAI01XtKXeCmJ46dNyz3yivYTMGuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HsoBRv7QyrPCFrRME5SFyyLIY8lFsu0zS36db7t3wuFq6FZCxkmA==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "signed_tx": "tx_+NMLAfiEuECZo9J1h/75lRhFxst2aElzHlgjImKDeN4j6u2INOVzIR7P2kXfiUTNTxD7KsAI01XtKXeCmJ46dNyz3yivYTMGuEDKYoiUXS5tCrv8aagf8PfZ0b3wqCDThrfCUVMB/qQmKmhPefvI1Vp/2aUYMFS8b4rcZgtW5TLm+jOivcWhBigHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HsoBRv7QyrPCFrRME5SFyyLIY8lFsu0zS36db7t3wuFq6FsR2koA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuECZo9J1h/75lRhFxst2aElzHlgjImKDeN4j6u2INOVzIR7P2kXfiUTNTxD7KsAI01XtKXeCmJ46dNyz3yivYTMGuEDKYoiUXS5tCrv8aagf8PfZ0b3wqCDThrfCUVMB/qQmKmhPefvI1Vp/2aUYMFS8b4rcZgtW5TLm+jOivcWhBigHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HsoBRv7QyrPCFrRME5SFyyLIY8lFsu0zS36db7t3wuFq6FsR2koA=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuECZo9J1h/75lRhFxst2aElzHlgjImKDeN4j6u2INOVzIR7P2kXfiUTNTxD7KsAI01XtKXeCmJ46dNyz3yivYTMGuEDKYoiUXS5tCrv8aagf8PfZ0b3wqCDThrfCUVMB/qQmKmhPefvI1Vp/2aUYMFS8b4rcZgtW5TLm+jOivcWhBigHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HsoBRv7QyrPCFrRME5SFyyLIY8lFsu0zS36db7t3wuFq6FsR2koA=="
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ge2gBVFN7zHiti4f/P2xM+XClo+u18eQv7snrEnq4TxXxfqt/HUl",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "signed_tx": "tx_+JELAfhCuECg6ZbVT4i5RF4KRRxtZbO2zU2wIXQmpNjIEvos7qOEcsdPa3jrYvUjzZPDgkIWC62ukmzHqYA0geWKvpt36MQDuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HtoAVRTe8x4rYuH/z9sTPlwpaPrtfHkL+7J6xJ6uE8V8X68BFqgg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuECg6ZbVT4i5RF4KRRxtZbO2zU2wIXQmpNjIEvos7qOEcsdPa3jrYvUjzZPDgkIWC62ukmzHqYA0geWKvpt36MQDuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HtoAVRTe8x4rYuH/z9sTPlwpaPrtfHkL+7J6xJ6uE8V8X68BFqgg==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "signed_tx": "tx_+NMLAfiEuECg6ZbVT4i5RF4KRRxtZbO2zU2wIXQmpNjIEvos7qOEcsdPa3jrYvUjzZPDgkIWC62ukmzHqYA0geWKvpt36MQDuEDqAwqpSPtlfS9QwQWQDTeymk2832JGMtC0TVbKSgoVhb8oQa35w1to7uhql/Zb59Ef4/wa0UqqiS1TKJUeRiMHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HtoAVRTe8x4rYuH/z9sTPlwpaPrtfHkL+7J6xJ6uE8V8X6sRQkig=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuECg6ZbVT4i5RF4KRRxtZbO2zU2wIXQmpNjIEvos7qOEcsdPa3jrYvUjzZPDgkIWC62ukmzHqYA0geWKvpt36MQDuEDqAwqpSPtlfS9QwQWQDTeymk2832JGMtC0TVbKSgoVhb8oQa35w1to7uhql/Zb59Ef4/wa0UqqiS1TKJUeRiMHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HtoAVRTe8x4rYuH/z9sTPlwpaPrtfHkL+7J6xJ6uE8V8X6sRQkig=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuECg6ZbVT4i5RF4KRRxtZbO2zU2wIXQmpNjIEvos7qOEcsdPa3jrYvUjzZPDgkIWC62ukmzHqYA0geWKvpt36MQDuEDqAwqpSPtlfS9QwQWQDTeymk2832JGMtC0TVbKSgoVhb8oQa35w1to7uhql/Zb59Ef4/wa0UqqiS1TKJUeRiMHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HtoAVRTe8x4rYuH/z9sTPlwpaPrtfHkL+7J6xJ6uE8V8X6sRQkig=="
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 238,
      "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ge6gSnDP2XMI4uGuJjMoEat2odMdAVrypTzHxOcniUG+4mKZpU3o",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "signed_tx": "tx_+JELAfhCuED74bzlsZjm5uTRlPP4waAICby+FQQxlo2Ghag6FiLjPGsmTNBiU1ukX37xGfa4KUI/3x/Qg5zRf6BgfE3hLZ0DuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HuoEpwz9lzCOLhriYzKBGrdqHTHQFa8qU8x8TnJ4lBvuJiqyoGVw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuED74bzlsZjm5uTRlPP4waAICby+FQQxlo2Ghag6FiLjPGsmTNBiU1ukX37xGfa4KUI/3x/Qg5zRf6BgfE3hLZ0DuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HuoEpwz9lzCOLhriYzKBGrdqHTHQFa8qU8x8TnJ4lBvuJiqyoGVw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "signed_tx": "tx_+NMLAfiEuEC8alPwZIWygmxiKLsabJGFf9mFNcL9+OJgAjxNZAAam8klxUs2WidHwDcmWwm2YzDJ2Sho7Bv1D+MF98+YrY0NuED74bzlsZjm5uTRlPP4waAICby+FQQxlo2Ghag6FiLjPGsmTNBiU1ukX37xGfa4KUI/3x/Qg5zRf6BgfE3hLZ0DuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HuoEpwz9lzCOLhriYzKBGrdqHTHQFa8qU8x8TnJ4lBvuJimxF6FQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEC8alPwZIWygmxiKLsabJGFf9mFNcL9+OJgAjxNZAAam8klxUs2WidHwDcmWwm2YzDJ2Sho7Bv1D+MF98+YrY0NuED74bzlsZjm5uTRlPP4waAICby+FQQxlo2Ghag6FiLjPGsmTNBiU1ukX37xGfa4KUI/3x/Qg5zRf6BgfE3hLZ0DuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HuoEpwz9lzCOLhriYzKBGrdqHTHQFa8qU8x8TnJ4lBvuJimxF6FQ=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEC8alPwZIWygmxiKLsabJGFf9mFNcL9+OJgAjxNZAAam8klxUs2WidHwDcmWwm2YzDJ2Sho7Bv1D+MF98+YrY0NuED74bzlsZjm5uTRlPP4waAICby+FQQxlo2Ghag6FiLjPGsmTNBiU1ukX37xGfa4KUI/3x/Qg5zRf6BgfE3hLZ0DuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HuoEpwz9lzCOLhriYzKBGrdqHTHQFa8qU8x8TnJ4lBvuJimxF6FQ=="
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": 238
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 238
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 238,
      "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": 238
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 238
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 238,
      "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 239,
      "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ge+gghMtSL1yThBDGEMiym/lcdH2LMQukjLW16iAGF3MzFX+AoAl",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "signed_tx": "tx_+JELAfhCuECZ0DVeQAW0jSQgSHpUQ0BEHCjNhhXXVpjcJiWKVLDl1qh7335OHuFHnzmoKadfKnM7vd2AW95WMgNSgen29cwIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HvoIITLUi9ck4QQxhDIspv5XHR9izELpIy1teogBhdzMxVHJPVLQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuECZ0DVeQAW0jSQgSHpUQ0BEHCjNhhXXVpjcJiWKVLDl1qh7335OHuFHnzmoKadfKnM7vd2AW95WMgNSgen29cwIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HvoIITLUi9ck4QQxhDIspv5XHR9izELpIy1teogBhdzMxVHJPVLQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "signed_tx": "tx_+NMLAfiEuECEnN1jTO7tZWHOEiV5KT1kRhAFXGfsfUBwVoBAMVngEI/fAx8T6UBkPCfN7cbLwgG3RI7M/U8zstpFhJkiEhgFuECZ0DVeQAW0jSQgSHpUQ0BEHCjNhhXXVpjcJiWKVLDl1qh7335OHuFHnzmoKadfKnM7vd2AW95WMgNSgen29cwIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HvoIITLUi9ck4QQxhDIspv5XHR9izELpIy1teogBhdzMxVzoQQvQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuECEnN1jTO7tZWHOEiV5KT1kRhAFXGfsfUBwVoBAMVngEI/fAx8T6UBkPCfN7cbLwgG3RI7M/U8zstpFhJkiEhgFuECZ0DVeQAW0jSQgSHpUQ0BEHCjNhhXXVpjcJiWKVLDl1qh7335OHuFHnzmoKadfKnM7vd2AW95WMgNSgen29cwIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HvoIITLUi9ck4QQxhDIspv5XHR9izELpIy1teogBhdzMxVzoQQvQ=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuECEnN1jTO7tZWHOEiV5KT1kRhAFXGfsfUBwVoBAMVngEI/fAx8T6UBkPCfN7cbLwgG3RI7M/U8zstpFhJkiEhgFuECZ0DVeQAW0jSQgSHpUQ0BEHCjNhhXXVpjcJiWKVLDl1qh7335OHuFHnzmoKadfKnM7vd2AW95WMgNSgen29cwIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HvoIITLUi9ck4QQxhDIspv5XHR9izELpIy1teogBhdzMxVzoQQvQ=="
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": 239
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 239
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 239,
      "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": 239
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 239
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 239,
      "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 240,
      "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gfCgGjG7pZulNWaEcbrXTn97fs/srZ6b0TvpY/eSvRTsBXLYoGcM",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "signed_tx": "tx_+JELAfhCuEA1aNXKewjO+A7ZNTfMuRY8mo0Vcbuz+lJ6l1/qMENyhSC7PAzc9M7xtLUaC9YgKVur/PxsI1GKONFMC+UblSMCuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HwoBoxu6WbpTVmhHG6105/e37P7K2em9E76WP3kr0U7AVyzp4b2w=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEA1aNXKewjO+A7ZNTfMuRY8mo0Vcbuz+lJ6l1/qMENyhSC7PAzc9M7xtLUaC9YgKVur/PxsI1GKONFMC+UblSMCuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HwoBoxu6WbpTVmhHG6105/e37P7K2em9E76WP3kr0U7AVyzp4b2w==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "signed_tx": "tx_+NMLAfiEuEA1aNXKewjO+A7ZNTfMuRY8mo0Vcbuz+lJ6l1/qMENyhSC7PAzc9M7xtLUaC9YgKVur/PxsI1GKONFMC+UblSMCuEDyYJaKBeFTWTn5RfnbgjXFBo/DU3eWIkPMggFV4xiewatGb8SW4qzPUxmjOCStxwu7V4Qc+/ORv8ffny5is6gFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HwoBoxu6WbpTVmhHG6105/e37P7K2em9E76WP3kr0U7AVyrwpzEA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEA1aNXKewjO+A7ZNTfMuRY8mo0Vcbuz+lJ6l1/qMENyhSC7PAzc9M7xtLUaC9YgKVur/PxsI1GKONFMC+UblSMCuEDyYJaKBeFTWTn5RfnbgjXFBo/DU3eWIkPMggFV4xiewatGb8SW4qzPUxmjOCStxwu7V4Qc+/ORv8ffny5is6gFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HwoBoxu6WbpTVmhHG6105/e37P7K2em9E76WP3kr0U7AVyrwpzEA=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEA1aNXKewjO+A7ZNTfMuRY8mo0Vcbuz+lJ6l1/qMENyhSC7PAzc9M7xtLUaC9YgKVur/PxsI1GKONFMC+UblSMCuEDyYJaKBeFTWTn5RfnbgjXFBo/DU3eWIkPMggFV4xiewatGb8SW4qzPUxmjOCStxwu7V4Qc+/ORv8ffny5is6gFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HwoBoxu6WbpTVmhHG6105/e37P7K2em9E76WP3kr0U7AVyrwpzEA=="
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": 240
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 240
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 240,
      "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": 240
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 240
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 240,
      "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 241,
      "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gfGgmN1YJ5EV18aj8voYTu8zVgdORIXD1IYDE+OjHOWJmjpbKA7V",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "signed_tx": "tx_+JELAfhCuEDsVwP0r8R8l3XcbfTHkVGvkvg2me6idOu68hvnUApCZh58nxEFZtVVWtDYS+Hb4jFldWIL6bbTJsNdf97Q3koFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HxoJjdWCeRFdfGo/L6GE7vM1YHTkSFw9SGAxPjoxzliZo6mgp9DA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEDsVwP0r8R8l3XcbfTHkVGvkvg2me6idOu68hvnUApCZh58nxEFZtVVWtDYS+Hb4jFldWIL6bbTJsNdf97Q3koFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HxoJjdWCeRFdfGo/L6GE7vM1YHTkSFw9SGAxPjoxzliZo6mgp9DA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "signed_tx": "tx_+NMLAfiEuEB0rdqa0yRM7jtI72Ni7j+RhfnTwBULu43cluqY217I0WVhIlB6CUu3h75k1CexdS8YocpvwskiXV4xeDopGegKuEDsVwP0r8R8l3XcbfTHkVGvkvg2me6idOu68hvnUApCZh58nxEFZtVVWtDYS+Hb4jFldWIL6bbTJsNdf97Q3koFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HxoJjdWCeRFdfGo/L6GE7vM1YHTkSFw9SGAxPjoxzliZo6oKXXcQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEB0rdqa0yRM7jtI72Ni7j+RhfnTwBULu43cluqY217I0WVhIlB6CUu3h75k1CexdS8YocpvwskiXV4xeDopGegKuEDsVwP0r8R8l3XcbfTHkVGvkvg2me6idOu68hvnUApCZh58nxEFZtVVWtDYS+Hb4jFldWIL6bbTJsNdf97Q3koFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HxoJjdWCeRFdfGo/L6GE7vM1YHTkSFw9SGAxPjoxzliZo6oKXXcQ=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEB0rdqa0yRM7jtI72Ni7j+RhfnTwBULu43cluqY217I0WVhIlB6CUu3h75k1CexdS8YocpvwskiXV4xeDopGegKuEDsVwP0r8R8l3XcbfTHkVGvkvg2me6idOu68hvnUApCZh58nxEFZtVVWtDYS+Hb4jFldWIL6bbTJsNdf97Q3koFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HxoJjdWCeRFdfGo/L6GE7vM1YHTkSFw9SGAxPjoxzliZo6oKXXcQ=="
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": 241
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 241
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 241,
      "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": 241
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 241
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 241,
      "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
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
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 242,
      "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gfKgkHhCmB/3fUbx0p7Xm5PBdb6nAvVUWAgQSza+B5gvyxR6T/gz",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "signed_tx": "tx_+JELAfhCuEAbqxESO0iOhu7iOnNJ+r/OUOP7qz5YOL6a0eNxRI0LESG9MOrH0D13A5f3MadfOmw1c4T8WY9BB55f/bhfKlQIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HyoJB4Qpgf931G8dKe15uTwXW+pwL1VFgIEEs2vgeYL8sUJHnBUg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEAbqxESO0iOhu7iOnNJ+r/OUOP7qz5YOL6a0eNxRI0LESG9MOrH0D13A5f3MadfOmw1c4T8WY9BB55f/bhfKlQIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HyoJB4Qpgf931G8dKe15uTwXW+pwL1VFgIEEs2vgeYL8sUJHnBUg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "signed_tx": "tx_+NMLAfiEuEAbqxESO0iOhu7iOnNJ+r/OUOP7qz5YOL6a0eNxRI0LESG9MOrH0D13A5f3MadfOmw1c4T8WY9BB55f/bhfKlQIuEDqQtC6O2e/RkPAdWuAee7RoUGqWRT/NzQWLaRvDr3OA9hSS6fmf346isbfYgDMMdU2X/rh8V6lNwNigTPh+6oKuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HyoJB4Qpgf931G8dKe15uTwXW+pwL1VFgIEEs2vgeYL8sU1393JA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEAbqxESO0iOhu7iOnNJ+r/OUOP7qz5YOL6a0eNxRI0LESG9MOrH0D13A5f3MadfOmw1c4T8WY9BB55f/bhfKlQIuEDqQtC6O2e/RkPAdWuAee7RoUGqWRT/NzQWLaRvDr3OA9hSS6fmf346isbfYgDMMdU2X/rh8V6lNwNigTPh+6oKuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HyoJB4Qpgf931G8dKe15uTwXW+pwL1VFgIEEs2vgeYL8sU1393JA=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEAbqxESO0iOhu7iOnNJ+r/OUOP7qz5YOL6a0eNxRI0LESG9MOrH0D13A5f3MadfOmw1c4T8WY9BB55f/bhfKlQIuEDqQtC6O2e/RkPAdWuAee7RoUGqWRT/NzQWLaRvDr3OA9hSS6fmf346isbfYgDMMdU2X/rh8V6lNwNigTPh+6oKuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HyoJB4Qpgf931G8dKe15uTwXW+pwL1VFgIEEs2vgeYL8sU1393JA=="
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
    "round": 242
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 242
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 242,
      "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
    "round": 242
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 242
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 242,
      "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
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
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 243,
      "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gfOgULhP5MJz1ZeZUJLMv0s4iIEyKNFXPho87U1IhP4v2MuaYvbc",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "signed_tx": "tx_+JELAfhCuEAdHFum1apNDd0793VcR+7S/7LG3pmAgB8AGPP/f+H1qzNCEgRo47rc5bMmaipPakswqnU9sJZPPaQKKfsaEc8OuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HzoFC4T+TCc9WXmVCSzL9LOIiBMijRVz4aPO1NSIT+L9jLzzCLYw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEAdHFum1apNDd0793VcR+7S/7LG3pmAgB8AGPP/f+H1qzNCEgRo47rc5bMmaipPakswqnU9sJZPPaQKKfsaEc8OuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HzoFC4T+TCc9WXmVCSzL9LOIiBMijRVz4aPO1NSIT+L9jLzzCLYw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVAmwIZE=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "signed_tx": "tx_+NMLAfiEuEAdHFum1apNDd0793VcR+7S/7LG3pmAgB8AGPP/f+H1qzNCEgRo47rc5bMmaipPakswqnU9sJZPPaQKKfsaEc8OuEAod0lUIOu3bwgjfd1dw5Ieuc3pi3XtFlrX6Ov/vvUwQ3Lls3asnPLpp6uIKiKNWDdRzvyHxlIm+ysMR9mv4UsHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HzoFC4T+TCc9WXmVCSzL9LOIiBMijRVz4aPO1NSIT+L9jLc7KyQg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEAdHFum1apNDd0793VcR+7S/7LG3pmAgB8AGPP/f+H1qzNCEgRo47rc5bMmaipPakswqnU9sJZPPaQKKfsaEc8OuEAod0lUIOu3bwgjfd1dw5Ieuc3pi3XtFlrX6Ov/vvUwQ3Lls3asnPLpp6uIKiKNWDdRzvyHxlIm+ysMR9mv4UsHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HzoFC4T+TCc9WXmVCSzL9LOIiBMijRVz4aPO1NSIT+L9jLc7KyQg=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEAdHFum1apNDd0793VcR+7S/7LG3pmAgB8AGPP/f+H1qzNCEgRo47rc5bMmaipPakswqnU9sJZPPaQKKfsaEc8OuEAod0lUIOu3bwgjfd1dw5Ieuc3pi3XtFlrX6Ov/vvUwQ3Lls3asnPLpp6uIKiKNWDdRzvyHxlIm+ysMR9mv4UsHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4HzoFC4T+TCc9WXmVCSzL9LOIiBMijRVz4aPO1NSIT+L9jLc7KyQg=="
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
    "round": 243
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 243
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 243,
      "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
    "round": 243
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 243
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 243,
      "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
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
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 244,
      "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gfSg/obA/xf9n+2uf6r2ZaoVAJtxVD40+Srw16JLO+lMhUX5bAyK",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "signed_tx": "tx_+JELAfhCuEAeq3uCJJZsWty/zRrD239bf14a2S1DoeZJzcGtJvyJZwfQ3vAX7DsnSqOXo4Af9qKctR1d7M+VsOHlCpJw7hUOuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H0oP6GwP8X/Z/trn+q9mWqFQCbcVQ+NPkq8NeiSzvpTIVFnxEdSQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEAeq3uCJJZsWty/zRrD239bf14a2S1DoeZJzcGtJvyJZwfQ3vAX7DsnSqOXo4Af9qKctR1d7M+VsOHlCpJw7hUOuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H0oP6GwP8X/Z/trn+q9mWqFQCbcVQ+NPkq8NeiSzvpTIVFnxEdSQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "signed_tx": "tx_+NMLAfiEuEAPdG5t3Dc5RPWHtyovec1tU6eOg3drFZACKqZUVOeaD1EfI2Xn7X5KRpIew7JnKPtQAKzAQw8dg9Z5a62i3mYDuEAeq3uCJJZsWty/zRrD239bf14a2S1DoeZJzcGtJvyJZwfQ3vAX7DsnSqOXo4Af9qKctR1d7M+VsOHlCpJw7hUOuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H0oP6GwP8X/Z/trn+q9mWqFQCbcVQ+NPkq8NeiSzvpTIVFe/oJ1g=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEAPdG5t3Dc5RPWHtyovec1tU6eOg3drFZACKqZUVOeaD1EfI2Xn7X5KRpIew7JnKPtQAKzAQw8dg9Z5a62i3mYDuEAeq3uCJJZsWty/zRrD239bf14a2S1DoeZJzcGtJvyJZwfQ3vAX7DsnSqOXo4Af9qKctR1d7M+VsOHlCpJw7hUOuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H0oP6GwP8X/Z/trn+q9mWqFQCbcVQ+NPkq8NeiSzvpTIVFe/oJ1g=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEAPdG5t3Dc5RPWHtyovec1tU6eOg3drFZACKqZUVOeaD1EfI2Xn7X5KRpIew7JnKPtQAKzAQw8dg9Z5a62i3mYDuEAeq3uCJJZsWty/zRrD239bf14a2S1DoeZJzcGtJvyJZwfQ3vAX7DsnSqOXo4Af9qKctR1d7M+VsOHlCpJw7hUOuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H0oP6GwP8X/Z/trn+q9mWqFQCbcVQ+NPkq8NeiSzvpTIVFe/oJ1g=="
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
    "round": 244
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 244
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 244,
      "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
    "round": 244
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 244
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 244,
      "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
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
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 245,
      "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
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
    "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gfWgiDOTy7fCy7mwh8WyAiNrFFx+6U1uJPQSILNedXLsCwTCyN/e",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "signed_tx": "tx_+JELAfhCuEAT/MHdSyBA9jReaogZBsKRD+6lGLzCqRCkpKmnccqK4c15tZLODboj1/R+zeQxFs7ICWSDIxu4fbCNcNeFQ0oDuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H1oIgzk8u3wsu5sIfFsgIjaxRcfulNbiT0EiCzXnVy7AsEgVlP8Q=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEAT/MHdSyBA9jReaogZBsKRD+6lGLzCqRCkpKmnccqK4c15tZLODboj1/R+zeQxFs7ICWSDIxu4fbCNcNeFQ0oDuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H1oIgzk8u3wsu5sIfFsgIjaxRcfulNbiT0EiCzXnVy7AsEgVlP8Q==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoN3DhRa+wiN1a5S58RtLbMUq7yWX9pPw+5Au6u5dqj4pVr/pU5c=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "signed_tx": "tx_+NMLAfiEuEAT/MHdSyBA9jReaogZBsKRD+6lGLzCqRCkpKmnccqK4c15tZLODboj1/R+zeQxFs7ICWSDIxu4fbCNcNeFQ0oDuECkQqK/Lh1QlIpZZjNLnn+aM8jJDGyQGmNBiHMsExU3ccyllkZ34FVneZTG9/v2R8GsThJ5Gp8N9ud1LFqlYNcIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H1oIgzk8u3wsu5sIfFsgIjaxRcfulNbiT0EiCzXnVy7AsEsKPMaA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEAT/MHdSyBA9jReaogZBsKRD+6lGLzCqRCkpKmnccqK4c15tZLODboj1/R+zeQxFs7ICWSDIxu4fbCNcNeFQ0oDuECkQqK/Lh1QlIpZZjNLnn+aM8jJDGyQGmNBiHMsExU3ccyllkZ34FVneZTG9/v2R8GsThJ5Gp8N9ud1LFqlYNcIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H1oIgzk8u3wsu5sIfFsgIjaxRcfulNbiT0EiCzXnVy7AsEsKPMaA=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEAT/MHdSyBA9jReaogZBsKRD+6lGLzCqRCkpKmnccqK4c15tZLODboj1/R+zeQxFs7ICWSDIxu4fbCNcNeFQ0oDuECkQqK/Lh1QlIpZZjNLnn+aM8jJDGyQGmNBiHMsExU3ccyllkZ34FVneZTG9/v2R8GsThJ5Gp8N9ud1LFqlYNcIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H1oIgzk8u3wsu5sIfFsgIjaxRcfulNbiT0EiCzXnVy7AsEsKPMaA=="
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
    "round": 245
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 245
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 245,
      "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
    "round": 245
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 245
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 245,
      "contract_id": "ct_DW7JJaXXfmwNbgMCWGVoN3BDxnD33nb5tdHn4j9ZkQLVpWLTT",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 246,
      "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gfagePZ4JqO/CACURUUKTuJRoVEJmlrSc96W7YgOb/+CX3tqGFVX",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "signed_tx": "tx_+JELAfhCuEB2JGq3i4GOimR2sr1YBHuKoYnUBJBqxW2Hn8iZauuBuxUG12TJh1/qCEc16VvKz7wvJCAQlR4whs+H3B5K0roKuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H2oHj2eCajvwgAlEVFCk7iUaFRCZpa0nPelu2IDm//gl97NkR5MQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEB2JGq3i4GOimR2sr1YBHuKoYnUBJBqxW2Hn8iZauuBuxUG12TJh1/qCEc16VvKz7wvJCAQlR4whs+H3B5K0roKuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H2oHj2eCajvwgAlEVFCk7iUaFRCZpa0nPelu2IDm//gl97NkR5MQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "signed_tx": "tx_+NMLAfiEuEB2JGq3i4GOimR2sr1YBHuKoYnUBJBqxW2Hn8iZauuBuxUG12TJh1/qCEc16VvKz7wvJCAQlR4whs+H3B5K0roKuED3iRzRKT0lfoD7iki9tlfhYz1deovXMALdakExJG5kPFTJ7AcvuLqUc30tOD9hbduN3/p/l5Jr/p006cZYRQ8LuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H2oHj2eCajvwgAlEVFCk7iUaFRCZpa0nPelu2IDm//gl97MG3nGA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEB2JGq3i4GOimR2sr1YBHuKoYnUBJBqxW2Hn8iZauuBuxUG12TJh1/qCEc16VvKz7wvJCAQlR4whs+H3B5K0roKuED3iRzRKT0lfoD7iki9tlfhYz1deovXMALdakExJG5kPFTJ7AcvuLqUc30tOD9hbduN3/p/l5Jr/p006cZYRQ8LuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H2oHj2eCajvwgAlEVFCk7iUaFRCZpa0nPelu2IDm//gl97MG3nGA=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEB2JGq3i4GOimR2sr1YBHuKoYnUBJBqxW2Hn8iZauuBuxUG12TJh1/qCEc16VvKz7wvJCAQlR4whs+H3B5K0roKuED3iRzRKT0lfoD7iki9tlfhYz1deovXMALdakExJG5kPFTJ7AcvuLqUc30tOD9hbduN3/p/l5Jr/p006cZYRQ8LuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H2oHj2eCajvwgAlEVFCk7iUaFRCZpa0nPelu2IDm//gl97MG3nGA=="
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": 246
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 246
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 246,
      "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": 246
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 246
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 246,
      "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 247,
      "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gfeg1U9czy2iv8J6u0IvuPm0FDv0HqtYebQfrYG/TINC2HZAIlOg",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "signed_tx": "tx_+JELAfhCuEDKK6v8Kz0hPrQdgw3lK0cH3NLjZ3VLAh+Djim2CQAmx791fmtGNApioSKsZWszYhFRuFkMsZaiaIMdYqgUC0AIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H3oNVPXM8tor/CertCL7j5tBQ79B6rWHm0H62Bv0yDQth2UUhUbQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEDKK6v8Kz0hPrQdgw3lK0cH3NLjZ3VLAh+Djim2CQAmx791fmtGNApioSKsZWszYhFRuFkMsZaiaIMdYqgUC0AIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H3oNVPXM8tor/CertCL7j5tBQ79B6rWHm0H62Bv0yDQth2UUhUbQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "signed_tx": "tx_+NMLAfiEuEBLmYF41wZyFt/TcPYqAJ/mofaOGKEpbtD/vP9LF/HxISuNvwynnx247HhAz/J5jJE3FHy70i6tdrwFwT2Wf1cHuEDKK6v8Kz0hPrQdgw3lK0cH3NLjZ3VLAh+Djim2CQAmx791fmtGNApioSKsZWszYhFRuFkMsZaiaIMdYqgUC0AIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H3oNVPXM8tor/CertCL7j5tBQ79B6rWHm0H62Bv0yDQth2UfmxbA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBLmYF41wZyFt/TcPYqAJ/mofaOGKEpbtD/vP9LF/HxISuNvwynnx247HhAz/J5jJE3FHy70i6tdrwFwT2Wf1cHuEDKK6v8Kz0hPrQdgw3lK0cH3NLjZ3VLAh+Djim2CQAmx791fmtGNApioSKsZWszYhFRuFkMsZaiaIMdYqgUC0AIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H3oNVPXM8tor/CertCL7j5tBQ79B6rWHm0H62Bv0yDQth2UfmxbA=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBLmYF41wZyFt/TcPYqAJ/mofaOGKEpbtD/vP9LF/HxISuNvwynnx247HhAz/J5jJE3FHy70i6tdrwFwT2Wf1cHuEDKK6v8Kz0hPrQdgw3lK0cH3NLjZ3VLAh+Djim2CQAmx791fmtGNApioSKsZWszYhFRuFkMsZaiaIMdYqgUC0AIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H3oNVPXM8tor/CertCL7j5tBQ79B6rWHm0H62Bv0yDQth2UfmxbA=="
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": 247
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 247
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 247,
      "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
    "round": 247
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 247
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 247,
      "contract_id": "ct_2gff8JYRZEpKD33KKrjhw7eWEANFN5LiQXzMFvKmsY9VGXUFku",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gfigo01gjVw9btjuxUYYCksja10W2ABIV0RLLAZVuVnx6eBW/R0k",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "signed_tx": "tx_+JELAfhCuEBH5wabs9hd8h161hAnTWPeXmeYbqOanhBX5Jyyk2SiMM1r8MHXO0onE+ronxuKMXgqTMH/0rnScFvTSLio4tQHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H4oKNNYI1cPW7Y7sVGGApLI2tdFtgASFdESywGVblZ8engdHBoIQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEBH5wabs9hd8h161hAnTWPeXmeYbqOanhBX5Jyyk2SiMM1r8MHXO0onE+ronxuKMXgqTMH/0rnScFvTSLio4tQHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H4oKNNYI1cPW7Y7sVGGApLI2tdFtgASFdESywGVblZ8engdHBoIQ==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+GZGA6AjCkIf8nA06kWznUewlO/mb+ZZlS2EaOxIL/ivjLd9tsC4OZ7+RNZEHwA3ADcAGg6CPwEDP/64F37sBDcBBwcBAQCWLwIRRNZEHxFpbml0EbgXfuwRbWFpboIvAIU0LjIuMADT5f3r",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "signed_tx": "tx_+NMLAfiEuEBH5wabs9hd8h161hAnTWPeXmeYbqOanhBX5Jyyk2SiMM1r8MHXO0onE+ronxuKMXgqTMH/0rnScFvTSLio4tQHuEDVHRYlEpoNTyI2+/TG/qKVa5qRyth//DLpHeUKGY512b3Wq+khvk4RSF0ISiliFnxYs9dbSWrXZ95ep2zJAtsAuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H4oKNNYI1cPW7Y7sVGGApLI2tdFtgASFdESywGVblZ8engiU/pYg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBH5wabs9hd8h161hAnTWPeXmeYbqOanhBX5Jyyk2SiMM1r8MHXO0onE+ronxuKMXgqTMH/0rnScFvTSLio4tQHuEDVHRYlEpoNTyI2+/TG/qKVa5qRyth//DLpHeUKGY512b3Wq+khvk4RSF0ISiliFnxYs9dbSWrXZ95ep2zJAtsAuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H4oKNNYI1cPW7Y7sVGGApLI2tdFtgASFdESywGVblZ8engiU/pYg=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBH5wabs9hd8h161hAnTWPeXmeYbqOanhBX5Jyyk2SiMM1r8MHXO0onE+ronxuKMXgqTMH/0rnScFvTSLio4tQHuEDVHRYlEpoNTyI2+/TG/qKVa5qRyth//DLpHeUKGY512b3Wq+khvk4RSF0ISiliFnxYs9dbSWrXZ95ep2zJAtsAuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H4oKNNYI1cPW7Y7sVGGApLI2tdFtgASFdESywGVblZ8engiU/pYg=="
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gfmgVoZtnJfBFzGMng0cfwdH+7kbRcJZuMVN/B4h68P92T6guH2H",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "signed_tx": "tx_+JELAfhCuEBB/y5KewzOykyT1FsFkWRvzrLmYE6K0BCMXizMhZ3A3HrkjZCkpNB+gZrq/fYKVSxqaCA8tbKsxgm4Mk/8g64FuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H5oFaGbZyXwRcxjJ4NHH8HR/u5G0XCWbjFTfweIevD/dk++QEd8g=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEBB/y5KewzOykyT1FsFkWRvzrLmYE6K0BCMXizMhZ3A3HrkjZCkpNB+gZrq/fYKVSxqaCA8tbKsxgm4Mk/8g64FuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H5oFaGbZyXwRcxjJ4NHH8HR/u5G0XCWbjFTfweIevD/dk++QEd8g==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+QFmRgOgSMtoepHJuxcgSqlB8eDrRkq/n67Nuw2lnGVwGeWmYFjAuQE4uNT+Er1R0wQ3AUcCNwAMAwAMAQADAPwRhXcGujcANwAA/i+GW9kENwFHAgcMAwAMAQADAPwRL4Zb2TcABwD+RNZEHwA3ADcAGg6CPwEDP/5nL98yADcCBwcHFBQAAgD+cTlAgQA3A0cCBwcHDAECDAEEDAMADAEABQD8EbgXfuw3AQcHAP5+LiJABDcCRwIHBwwBAgwDb4Im0AwDFAwBAAUA/BG4F37sNwEHBwD+v75R3AA3A0cCRwIHBwwBBAwBAAwDAAwBAgMA/BF+LiJANwJHAgcHALhdLwcREr1R0yVpbmNyZW1lbnQRL4Zb2Q1nZXQRRNZEHxFpbml0EWcv3zIRcGx1cxFxOUCBOWdhc19saW1pdF9jYWxsEX4uIkARY2FsbBG/vlHcLXN0YWdlZF9jYWxsgi8AhTQuMi4wAP0jW4I=",
          "deposit": 10,
          "op": "OffChainNewContract",
          "owner": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "signed_tx": "tx_+NMLAfiEuEBB/y5KewzOykyT1FsFkWRvzrLmYE6K0BCMXizMhZ3A3HrkjZCkpNB+gZrq/fYKVSxqaCA8tbKsxgm4Mk/8g64FuECpiAYR6owOG3pf6Mjq8qMfBKHhqzp3nb8qEhp5Bw/pKi2eigKIj4ZoSE9E4TQieartOn9D1wGNpftGXf1xgJEEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H5oFaGbZyXwRcxjJ4NHH8HR/u5G0XCWbjFTfweIevD/dk+BMaQJw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBB/y5KewzOykyT1FsFkWRvzrLmYE6K0BCMXizMhZ3A3HrkjZCkpNB+gZrq/fYKVSxqaCA8tbKsxgm4Mk/8g64FuECpiAYR6owOG3pf6Mjq8qMfBKHhqzp3nb8qEhp5Bw/pKi2eigKIj4ZoSE9E4TQieartOn9D1wGNpftGXf1xgJEEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H5oFaGbZyXwRcxjJ4NHH8HR/u5G0XCWbjFTfweIevD/dk+BMaQJw=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBB/y5KewzOykyT1FsFkWRvzrLmYE6K0BCMXizMhZ3A3HrkjZCkpNB+gZrq/fYKVSxqaCA8tbKsxgm4Mk/8g64FuECpiAYR6owOG3pf6Mjq8qMfBKHhqzp3nb8qEhp5Bw/pKi2eigKIj4ZoSE9E4TQieartOn9D1wGNpftGXf1xgJEEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H5oFaGbZyXwRcxjJ4NHH8HR/u5G0XCWbjFTfweIevD/dk+BMaQJw=="
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 250,
      "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gfqg0HcqIpgo8DYXcHwRYX5oPuFlddeFXcHqmHfOK1Wby/WwP8E7",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "signed_tx": "tx_+JELAfhCuEAmEyqtkjYKWEuxIWKhEEPeuWVZ9j/Hcrpz7it5uRFPX5ahsZZIHDADJXpdcQCpV1xaoCtkfaeW3FmEw4W3BMgBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H6oNB3KiKYKPA2F3B8EWF+aD7hZXXXhV3B6ph3zitVm8v1HIW19Q=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEAmEyqtkjYKWEuxIWKhEEPeuWVZ9j/Hcrpz7it5uRFPX5ahsZZIHDADJXpdcQCpV1xaoCtkfaeW3FmEw4W3BMgBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H6oNB3KiKYKPA2F3B8EWF+aD7hZXXXhV3B6ph3zitVm8v1HIW19Q==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "signed_tx": "tx_+NMLAfiEuEAK+5sRpY7LaieO+hQLyPB/IbVWgMGTr95P7Vs+OrLCBnJLQkDJNOxVTliUFiAi5cFRe+waUXmLSpKYKYSgaLQHuEAmEyqtkjYKWEuxIWKhEEPeuWVZ9j/Hcrpz7it5uRFPX5ahsZZIHDADJXpdcQCpV1xaoCtkfaeW3FmEw4W3BMgBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H6oNB3KiKYKPA2F3B8EWF+aD7hZXXXhV3B6ph3zitVm8v1cY+O8w=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEAK+5sRpY7LaieO+hQLyPB/IbVWgMGTr95P7Vs+OrLCBnJLQkDJNOxVTliUFiAi5cFRe+waUXmLSpKYKYSgaLQHuEAmEyqtkjYKWEuxIWKhEEPeuWVZ9j/Hcrpz7it5uRFPX5ahsZZIHDADJXpdcQCpV1xaoCtkfaeW3FmEw4W3BMgBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H6oNB3KiKYKPA2F3B8EWF+aD7hZXXXhV3B6ph3zitVm8v1cY+O8w=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEAK+5sRpY7LaieO+hQLyPB/IbVWgMGTr95P7Vs+OrLCBnJLQkDJNOxVTliUFiAi5cFRe+waUXmLSpKYKYSgaLQHuEAmEyqtkjYKWEuxIWKhEEPeuWVZ9j/Hcrpz7it5uRFPX5ahsZZIHDADJXpdcQCpV1xaoCtkfaeW3FmEw4W3BMgBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H6oNB3KiKYKPA2F3B8EWF+aD7hZXXXhV3B6ph3zitVm8v1cY+O8w=="
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": 250
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 250
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 250,
      "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": 250
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 250
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 250,
      "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 251,
      "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gfugdt6jZipoiJnotRB3Fb50g4PlT1qjXrbOnEIC1hC8uygzUrJA",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "signed_tx": "tx_+JELAfhCuEDpQNUQgHssDxX9K/cVVjn++phzG5pyXs1LCKAWYX+jMcApb7T4tc0kJPpvUacBfh9o7YSOwMjn0REoQriU470AuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H7oHbeo2YqaIiZ6LUQdxW+dIOD5U9ao162zpxCAtYQvLsoyQgmHw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEDpQNUQgHssDxX9K/cVVjn++phzG5pyXs1LCKAWYX+jMcApb7T4tc0kJPpvUacBfh9o7YSOwMjn0REoQriU470AuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H7oHbeo2YqaIiZ6LUQdxW+dIOD5U9ao162zpxCAtYQvLsoyQgmHw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxTlg6/6",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "signed_tx": "tx_+NMLAfiEuEBoeYgrx1UL9V6KrwmPcDC2dHhGaK4iy/iPf2FRRARNJU+Fl7lI0L0CehEzUnad+Nr0tc5/KMcMuFWue1fnv6ABuEDpQNUQgHssDxX9K/cVVjn++phzG5pyXs1LCKAWYX+jMcApb7T4tc0kJPpvUacBfh9o7YSOwMjn0REoQriU470AuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H7oHbeo2YqaIiZ6LUQdxW+dIOD5U9ao162zpxCAtYQvLsoHoY0kQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBoeYgrx1UL9V6KrwmPcDC2dHhGaK4iy/iPf2FRRARNJU+Fl7lI0L0CehEzUnad+Nr0tc5/KMcMuFWue1fnv6ABuEDpQNUQgHssDxX9K/cVVjn++phzG5pyXs1LCKAWYX+jMcApb7T4tc0kJPpvUacBfh9o7YSOwMjn0REoQriU470AuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H7oHbeo2YqaIiZ6LUQdxW+dIOD5U9ao162zpxCAtYQvLsoHoY0kQ=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBoeYgrx1UL9V6KrwmPcDC2dHhGaK4iy/iPf2FRRARNJU+Fl7lI0L0CehEzUnad+Nr0tc5/KMcMuFWue1fnv6ABuEDpQNUQgHssDxX9K/cVVjn++phzG5pyXs1LCKAWYX+jMcApb7T4tc0kJPpvUacBfh9o7YSOwMjn0REoQriU470AuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H7oHbeo2YqaIiZ6LUQdxW+dIOD5U9ao162zpxCAtYQvLsoHoY0kQ=="
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": 251
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 251
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 251,
      "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": 251
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 251
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 251,
      "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 252,
      "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gfygYsHCcuSRMIYUVbJtafk+aijBM4FjxQyfRZseJwgnkoyts0kg",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "signed_tx": "tx_+JELAfhCuECCesnwM3mMGDwHKObG6qBlEcNc2zQu8MDbqCp/PkMXFRtc4Vnu/kXR34+FsHJRS8n5W1oQzbrQD9KNVOkKYDcMuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H8oGLBwnLkkTCGFFWybWn5PmoowTOBY8UMn0WbHicIJ5KMGQ3cZQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuECCesnwM3mMGDwHKObG6qBlEcNc2zQu8MDbqCp/PkMXFRtc4Vnu/kXR34+FsHJRS8n5W1oQzbrQD9KNVOkKYDcMuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H8oGLBwnLkkTCGFFWybWn5PmoowTOBY8UMn0WbHicIJ5KMGQ3cZQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "signed_tx": "tx_+NMLAfiEuECCesnwM3mMGDwHKObG6qBlEcNc2zQu8MDbqCp/PkMXFRtc4Vnu/kXR34+FsHJRS8n5W1oQzbrQD9KNVOkKYDcMuEDWPU9GHBxknMVaxoAx20WEr7O3I4jRguySBCOSR7FtfnHX4CHaPesigbWobsjgRfFSYcpqUWKH1RP1Zhr3UyMFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H8oGLBwnLkkTCGFFWybWn5PmoowTOBY8UMn0WbHicIJ5KMHTordw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuECCesnwM3mMGDwHKObG6qBlEcNc2zQu8MDbqCp/PkMXFRtc4Vnu/kXR34+FsHJRS8n5W1oQzbrQD9KNVOkKYDcMuEDWPU9GHBxknMVaxoAx20WEr7O3I4jRguySBCOSR7FtfnHX4CHaPesigbWobsjgRfFSYcpqUWKH1RP1Zhr3UyMFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H8oGLBwnLkkTCGFFWybWn5PmoowTOBY8UMn0WbHicIJ5KMHTordw=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuECCesnwM3mMGDwHKObG6qBlEcNc2zQu8MDbqCp/PkMXFRtc4Vnu/kXR34+FsHJRS8n5W1oQzbrQD9KNVOkKYDcMuEDWPU9GHBxknMVaxoAx20WEr7O3I4jRguySBCOSR7FtfnHX4CHaPesigbWobsjgRfFSYcpqUWKH1RP1Zhr3UyMFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H8oGLBwnLkkTCGFFWybWn5PmoowTOBY8UMn0WbHicIJ5KMHTordw=="
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": 252
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 252
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 252,
      "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": 252
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 252
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 252,
      "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 253,
      "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gf2gARl4ZmKpHU37kqVkyLWL4U2IfLJWcukjnknVKHUrirP1470U",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "signed_tx": "tx_+JELAfhCuEBuqXgE3T8QoITdUMmIEj2k0oE7KhEqyqM1baAaAZWd9lBW/M+w+Y/9M02iTgwjUedyCaJih+Dx2Fx5nUzBmrwCuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H9oAEZeGZiqR1N+5KlZMi1i+FNiHyyVnLpI55J1Sh1K4qz7gO9dw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEBuqXgE3T8QoITdUMmIEj2k0oE7KhEqyqM1baAaAZWd9lBW/M+w+Y/9M02iTgwjUedyCaJih+Dx2Fx5nUzBmrwCuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H9oAEZeGZiqR1N+5KlZMi1i+FNiHyyVnLpI55J1Sh1K4qz7gO9dw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxbivrGI",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "signed_tx": "tx_+NMLAfiEuEBuqXgE3T8QoITdUMmIEj2k0oE7KhEqyqM1baAaAZWd9lBW/M+w+Y/9M02iTgwjUedyCaJih+Dx2Fx5nUzBmrwCuEC/KRHwwiEht2DWP07afDcEB7A2oAQ9elkvNKznH51drZB4qVnJeKeYNHovkkz53+Aj9ZrSK8Rg0RIrtog1zpQHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H9oAEZeGZiqR1N+5KlZMi1i+FNiHyyVnLpI55J1Sh1K4qzW2HUXQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBuqXgE3T8QoITdUMmIEj2k0oE7KhEqyqM1baAaAZWd9lBW/M+w+Y/9M02iTgwjUedyCaJih+Dx2Fx5nUzBmrwCuEC/KRHwwiEht2DWP07afDcEB7A2oAQ9elkvNKznH51drZB4qVnJeKeYNHovkkz53+Aj9ZrSK8Rg0RIrtog1zpQHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H9oAEZeGZiqR1N+5KlZMi1i+FNiHyyVnLpI55J1Sh1K4qzW2HUXQ=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBuqXgE3T8QoITdUMmIEj2k0oE7KhEqyqM1baAaAZWd9lBW/M+w+Y/9M02iTgwjUedyCaJih+Dx2Fx5nUzBmrwCuEC/KRHwwiEht2DWP07afDcEB7A2oAQ9elkvNKznH51drZB4qVnJeKeYNHovkkz53+Aj9ZrSK8Rg0RIrtog1zpQHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H9oAEZeGZiqR1N+5KlZMi1i+FNiHyyVnLpI55J1Sh1K4qzW2HUXQ=="
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": 253
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 253
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 253,
      "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": 253
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 253
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 253,
      "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
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
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 254,
      "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gf6gIyXgF3CmCDJlSW3efu5Su06FkXS6BPZK4qe0oB0/Z6lsc3/C",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "signed_tx": "tx_+JELAfhCuECT+M3OzHqTs4q4Y3IxxRWau5R2S4P8ds3lH7/H7lF7RFARoyI54XXP0Vjf2x9FQAqQJcMrVHzgsYcM7ftqi/AJuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H+oCMl4BdwpggyZUlt3n7uUrtOhZF0ugT2SuKntKAdP2epIFzNSA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuECT+M3OzHqTs4q4Y3IxxRWau5R2S4P8ds3lH7/H7lF7RFARoyI54XXP0Vjf2x9FQAqQJcMrVHzgsYcM7ftqi/AJuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H+oCMl4BdwpggyZUlt3n7uUrtOhZF0ugT2SuKntKAdP2epIFzNSA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "signed_tx": "tx_+NMLAfiEuECAzdgS3l7953GxOVi3qB1AfuzAFeKEBAUqUPOals2sOvIaEhjEUYuRyZNALesMM8uSBleohoh1LjH9zPfv8zIEuECT+M3OzHqTs4q4Y3IxxRWau5R2S4P8ds3lH7/H7lF7RFARoyI54XXP0Vjf2x9FQAqQJcMrVHzgsYcM7ftqi/AJuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H+oCMl4BdwpggyZUlt3n7uUrtOhZF0ugT2SuKntKAdP2epzpWTJQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuECAzdgS3l7953GxOVi3qB1AfuzAFeKEBAUqUPOals2sOvIaEhjEUYuRyZNALesMM8uSBleohoh1LjH9zPfv8zIEuECT+M3OzHqTs4q4Y3IxxRWau5R2S4P8ds3lH7/H7lF7RFARoyI54XXP0Vjf2x9FQAqQJcMrVHzgsYcM7ftqi/AJuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H+oCMl4BdwpggyZUlt3n7uUrtOhZF0ugT2SuKntKAdP2epzpWTJQ=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuECAzdgS3l7953GxOVi3qB1AfuzAFeKEBAUqUPOals2sOvIaEhjEUYuRyZNALesMM8uSBleohoh1LjH9zPfv8zIEuECT+M3OzHqTs4q4Y3IxxRWau5R2S4P8ds3lH7/H7lF7RFARoyI54XXP0Vjf2x9FQAqQJcMrVHzgsYcM7ftqi/AJuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H+oCMl4BdwpggyZUlt3n7uUrtOhZF0ugT2SuKntKAdP2epzpWTJQ=="
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
    "round": 254
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 254
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 254,
      "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
    "round": 254
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 254
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 254,
      "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
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
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 255,
      "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gf+g16FJ7HqrWhaWQmaKkAm78BHrjB6P//phynrZz8WUORaVDFEV",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "signed_tx": "tx_+JELAfhCuEDVoRPexdjNPs+Eg/VGa9MrvmqId+b2USgoY2jKoVx9P5JmqMIetmBn4jmWaeJpCUh14gaaPmbfCicRYfhDwAsKuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H/oNehSex6q1oWlkJmipAJu/AR64wej//6Ycp62c/FlDkWGpPdxg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JELAfhCuEDVoRPexdjNPs+Eg/VGa9MrvmqId+b2USgoY2jKoVx9P5JmqMIetmBn4jmWaeJpCUh14gaaPmbfCicRYfhDwAsKuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H/oNehSex6q1oWlkJmipAJu/AR64wej//6Ycp62c/FlDkWGpPdxg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVBQEDeA=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "signed_tx": "tx_+NMLAfiEuEBQo5Ba9dsOYyKXhJYt7O62XGyh1eM4FzWmHzCYjHHKvCloGuXLOIAvCy/rShYEUTWwzMB5l47Ln7yolcg/F5UIuEDVoRPexdjNPs+Eg/VGa9MrvmqId+b2USgoY2jKoVx9P5JmqMIetmBn4jmWaeJpCUh14gaaPmbfCicRYfhDwAsKuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H/oNehSex6q1oWlkJmipAJu/AR64wej//6Ycp62c/FlDkWs5MLag=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBQo5Ba9dsOYyKXhJYt7O62XGyh1eM4FzWmHzCYjHHKvCloGuXLOIAvCy/rShYEUTWwzMB5l47Ln7yolcg/F5UIuEDVoRPexdjNPs+Eg/VGa9MrvmqId+b2USgoY2jKoVx9P5JmqMIetmBn4jmWaeJpCUh14gaaPmbfCicRYfhDwAsKuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H/oNehSex6q1oWlkJmipAJu/AR64wej//6Ycp62c/FlDkWs5MLag=="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NMLAfiEuEBQo5Ba9dsOYyKXhJYt7O62XGyh1eM4FzWmHzCYjHHKvCloGuXLOIAvCy/rShYEUTWwzMB5l47Ln7yolcg/F5UIuEDVoRPexdjNPs+Eg/VGa9MrvmqId+b2USgoY2jKoVx9P5JmqMIetmBn4jmWaeJpCUh14gaaPmbfCicRYfhDwAsKuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4H/oNehSex6q1oWlkJmipAJu/AR64wej//6Ycp62c/FlDkWs5MLag=="
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
    "round": 255
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 255
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 255,
      "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
    "round": 255
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 255
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 255,
      "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
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
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 256,
      "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
    "contract_id": "ABCDEFG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEAoEuQrhSc7XWFCcyFabiVQkIjSBqdtnpPZJp9GBkkr4jzw7IEUQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "signed_tx": "tx_+JILAfhCuECA1lHXYyGdNo36Csm4VqGQdsxIKwWXSnwPlu/nBQc7qO2EX5zWDUeak3S25bxxbkTDSTqVV3YOUKTx0Zv1b+4CuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBAKBLkK4UnO11hQnMhWm4lUJCI0ganbZ6T2SafRgZJK+I88gdXBM="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JILAfhCuECA1lHXYyGdNo36Csm4VqGQdsxIKwWXSnwPlu/nBQc7qO2EX5zWDUeak3S25bxxbkTDSTqVV3YOUKTx0Zv1b+4CuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBAKBLkK4UnO11hQnMhWm4lUJCI0ganbZ6T2SafRgZJK+I88gdXBM=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "signed_tx": "tx_+NQLAfiEuECA1lHXYyGdNo36Csm4VqGQdsxIKwWXSnwPlu/nBQc7qO2EX5zWDUeak3S25bxxbkTDSTqVV3YOUKTx0Zv1b+4CuED6K4BcRPPc6GX6fKZJoc6YwAe2oPr6LCIAc9oL5nlpi8d4608tgjNGAhV5Q+UkOnmJXWcgWUdzecXk7ih62g0OuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBAKBLkK4UnO11hQnMhWm4lUJCI0ganbZ6T2SafRgZJK+I8+Y5zt4="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NQLAfiEuECA1lHXYyGdNo36Csm4VqGQdsxIKwWXSnwPlu/nBQc7qO2EX5zWDUeak3S25bxxbkTDSTqVV3YOUKTx0Zv1b+4CuED6K4BcRPPc6GX6fKZJoc6YwAe2oPr6LCIAc9oL5nlpi8d4608tgjNGAhV5Q+UkOnmJXWcgWUdzecXk7ih62g0OuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBAKBLkK4UnO11hQnMhWm4lUJCI0ganbZ6T2SafRgZJK+I8+Y5zt4="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NQLAfiEuECA1lHXYyGdNo36Csm4VqGQdsxIKwWXSnwPlu/nBQc7qO2EX5zWDUeak3S25bxxbkTDSTqVV3YOUKTx0Zv1b+4CuED6K4BcRPPc6GX6fKZJoc6YwAe2oPr6LCIAc9oL5nlpi8d4608tgjNGAhV5Q+UkOnmJXWcgWUdzecXk7ih62g0OuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBAKBLkK4UnO11hQnMhWm4lUJCI0ganbZ6T2SafRgZJK+I8+Y5zt4="
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
    "round": 256
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 256
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 256,
      "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
    "round": 256
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 256
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 256,
      "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
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
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 257,
      "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
      }
    }
  },
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
    "contract_id": "ABCDEFG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
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
    "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEBoM1lhKXQg3HPU2YvHeAve/SYs7U2qkpc2AZKlUzGSalR7qtCZQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "signed_tx": "tx_+JILAfhCuEBzROpowfI1+oRyS3kmk0r8E5IAvWB5h8LCvxytiu0Da+nAy3n5MpUJoMfNJ8xiefiuEQ/RwvL81d5UItqdHkkAuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBAaDNZYSl0INxz1NmLx3gL3v0mLO1NqpKXNgGSpVMxkmpUUPi43Y="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JILAfhCuEBzROpowfI1+oRyS3kmk0r8E5IAvWB5h8LCvxytiu0Da+nAy3n5MpUJoMfNJ8xiefiuEQ/RwvL81d5UItqdHkkAuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBAaDNZYSl0INxz1NmLx3gL3v0mLO1NqpKXNgGSpVMxkmpUUPi43Y=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxF+LiJAK58CoJRDFlj4MumYw8Yw0aVJmQg4DxKKUJ+7WzB2f51daA4oVvxAMwg=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "signed_tx": "tx_+NQLAfiEuEBzROpowfI1+oRyS3kmk0r8E5IAvWB5h8LCvxytiu0Da+nAy3n5MpUJoMfNJ8xiefiuEQ/RwvL81d5UItqdHkkAuEDizKRvtw6mDPDPTB00vgyR0k5k9p/ivaFzTEAjflnmu4Rcc29+LdA9R6zy0te3ussg6b1vrkxDBZqtXAhwwRAPuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBAaDNZYSl0INxz1NmLx3gL3v0mLO1NqpKXNgGSpVMxkmpUYgyyZU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NQLAfiEuEBzROpowfI1+oRyS3kmk0r8E5IAvWB5h8LCvxytiu0Da+nAy3n5MpUJoMfNJ8xiefiuEQ/RwvL81d5UItqdHkkAuEDizKRvtw6mDPDPTB00vgyR0k5k9p/ivaFzTEAjflnmu4Rcc29+LdA9R6zy0te3ussg6b1vrkxDBZqtXAhwwRAPuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBAaDNZYSl0INxz1NmLx3gL3v0mLO1NqpKXNgGSpVMxkmpUYgyyZU="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NQLAfiEuEBzROpowfI1+oRyS3kmk0r8E5IAvWB5h8LCvxytiu0Da+nAy3n5MpUJoMfNJ8xiefiuEQ/RwvL81d5UItqdHkkAuEDizKRvtw6mDPDPTB00vgyR0k5k9p/ivaFzTEAjflnmu4Rcc29+LdA9R6zy0te3ussg6b1vrkxDBZqtXAhwwRAPuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBAaDNZYSl0INxz1NmLx3gL3v0mLO1NqpKXNgGSpVMxkmpUYgyyZU="
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
    "round": 257
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 257
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 257,
      "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
    "round": 257
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 257
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 257,
      "contract_id": "ct_2HcSu2MsLdULMedgqyudkLfzVkfVcvVutphQnE3GEtJ6kGPMpN",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 258,
      "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggECoDKPTGqq/BbZoiruHb3PnbveiRu47cqaq6nZsGlIPF5VFW9X/Q==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "signed_tx": "tx_+JILAfhCuED/ASuqc2ip+rqyMWlYDMm8SG/wmsLlSCfmEJGTSjW1uCaM/2S5pY/VVo6+enPl15yBfjw/0qxz3CXefBJDmoUMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBAqAyj0xqqvwW2aIq7h29z5273okbuO3Kmqup2bBpSDxeVS+L+jA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JILAfhCuED/ASuqc2ip+rqyMWlYDMm8SG/wmsLlSCfmEJGTSjW1uCaM/2S5pY/VVo6+enPl15yBfjw/0qxz3CXefBJDmoUMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBAqAyj0xqqvwW2aIq7h29z5273okbuO3Kmqup2bBpSDxeVS+L+jA=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "signed_tx": "tx_+NQLAfiEuEAEdIMzaZ07FWULRzmo8hpzvEyLIezB2pyVVFOipA2oVsxyx7NolB0Vc4uXYRLeSMZxpQUGjPDNEpurQdEdK0wLuED/ASuqc2ip+rqyMWlYDMm8SG/wmsLlSCfmEJGTSjW1uCaM/2S5pY/VVo6+enPl15yBfjw/0qxz3CXefBJDmoUMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBAqAyj0xqqvwW2aIq7h29z5273okbuO3Kmqup2bBpSDxeVVzAhqY="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NQLAfiEuEAEdIMzaZ07FWULRzmo8hpzvEyLIezB2pyVVFOipA2oVsxyx7NolB0Vc4uXYRLeSMZxpQUGjPDNEpurQdEdK0wLuED/ASuqc2ip+rqyMWlYDMm8SG/wmsLlSCfmEJGTSjW1uCaM/2S5pY/VVo6+enPl15yBfjw/0qxz3CXefBJDmoUMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBAqAyj0xqqvwW2aIq7h29z5273okbuO3Kmqup2bBpSDxeVVzAhqY="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NQLAfiEuEAEdIMzaZ07FWULRzmo8hpzvEyLIezB2pyVVFOipA2oVsxyx7NolB0Vc4uXYRLeSMZxpQUGjPDNEpurQdEdK0wLuED/ASuqc2ip+rqyMWlYDMm8SG/wmsLlSCfmEJGTSjW1uCaM/2S5pY/VVo6+enPl15yBfjw/0qxz3CXefBJDmoUMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBAqAyj0xqqvwW2aIq7h29z5273okbuO3Kmqup2bBpSDxeVVzAhqY="
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": 258
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 258
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 258,
      "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": 258
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ABCDEFG",
    "round": 258
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
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
    "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 258,
      "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract.reply",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 259,
      "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
      }
    }
  },
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEDoEP1+AT04GFxPr6PX6RR6fTPgosrqn7l4MjfrAIcPKRgZ5Q0sA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "signed_tx": "tx_+JILAfhCuEDmAfL9VWC4ZQvVZPLCBDGpg0rFjZOiaqgvrsz5yLKlL8UVY0swMA7CwMsHHMEWXFsnggYKz/YXxIPygIyBXFMLuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBA6BD9fgE9OBhcT6+j1+kUen0z4KLK6p+5eDI36wCHDykYJblq4M="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+JILAfhCuEDmAfL9VWC4ZQvVZPLCBDGpg0rFjZOiaqgvrsz5yLKlL8UVY0swMA7CwMsHHMEWXFsnggYKz/YXxIPygIyBXFMLuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBA6BD9fgE9OBhcT6+j1+kUen0z4KLK6p+5eDI36wCHDykYJblq4M=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxG4F37sGxg+DKMp",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "signed_tx": "tx_+NQLAfiEuEDmAfL9VWC4ZQvVZPLCBDGpg0rFjZOiaqgvrsz5yLKlL8UVY0swMA7CwMsHHMEWXFsnggYKz/YXxIPygIyBXFMLuEDnIqDLumvR2hWaVNnqU2IZhKhOHleXoWJ5i56IP9D5dJWRdLMei51MkJQy/HzPMNumVu2g12q4haoauj2gJQMBuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBA6BD9fgE9OBhcT6+j1+kUen0z4KLK6p+5eDI36wCHDykYDl9JPk="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NQLAfiEuEDmAfL9VWC4ZQvVZPLCBDGpg0rFjZOiaqgvrsz5yLKlL8UVY0swMA7CwMsHHMEWXFsnggYKz/YXxIPygIyBXFMLuEDnIqDLumvR2hWaVNnqU2IZhKhOHleXoWJ5i56IP9D5dJWRdLMei51MkJQy/HzPMNumVu2g12q4haoauj2gJQMBuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBA6BD9fgE9OBhcT6+j1+kUen0z4KLK6p+5eDI36wCHDykYDl9JPk="
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NQLAfiEuEDmAfL9VWC4ZQvVZPLCBDGpg0rFjZOiaqgvrsz5yLKlL8UVY0swMA7CwMsHHMEWXFsnggYKz/YXxIPygIyBXFMLuEDnIqDLumvR2hWaVNnqU2IZhKhOHleXoWJ5i56IP9D5dJWRdLMei51MkJQy/HzPMNumVu2g12q4haoauj2gJQMBuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBA6BD9fgE9OBhcT6+j1+kUen0z4KLK6p+5eDI36wCHDykYDl9JPk="
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": 259
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 259
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 259,
      "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "error": {
    "code": 3,
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
    "round": 259
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ABCDEFG",
    "round": 259
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
        "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
    "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 259,
      "contract_id": "ct_28JA1XFvikCHNVu7t1jwq4x5mQoN6E2NVrhtgcG6LysjBeHaNb",
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
