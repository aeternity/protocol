
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEsoKtvMv1pCQdp6MFqekWXBL7IS1c3c6gWs39Z4O4jBsR3mdThdA==",
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
  "id": -576460752303421267,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEDib89/esJQdA6Iku+BaeTgGqBYJnAmkOQwHToYI8rHkcKeVPhEQ6/qZiKSMsgt0mEgx48CzXNkleNKbnO9/VAFuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBLKCrbzL9aQkHaejBanpFlwS+yEtXN3OoFrN/WeDuIwbEdz/Nli8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "signed_tx": "tx_+JILAfhCuEDib89/esJQdA6Iku+BaeTgGqBYJnAmkOQwHToYI8rHkcKeVPhEQ6/qZiKSMsgt0mEgx48CzXNkleNKbnO9/VAFuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBLKCrbzL9aQkHaejBanpFlwS+yEtXN3OoFrN/WeDuIwbEdz/Nli8=",
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
  "id": -576460752303421266,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEDPNF95n/RPxa4c3X0oYBvvEshiIxJH15umhA+X688zPuUBjQ5/B/g4ApehpFZrdwNQngA9+z+kIRey2R9fztcDuEDib89/esJQdA6Iku+BaeTgGqBYJnAmkOQwHToYI8rHkcKeVPhEQ6/qZiKSMsgt0mEgx48CzXNkleNKbnO9/VAFuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBLKCrbzL9aQkHaejBanpFlwS+yEtXN3OoFrN/WeDuIwbEd5FhbI4="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NQLAfiEuEDPNF95n/RPxa4c3X0oYBvvEshiIxJH15umhA+X688zPuUBjQ5/B/g4ApehpFZrdwNQngA9+z+kIRey2R9fztcDuEDib89/esJQdA6Iku+BaeTgGqBYJnAmkOQwHToYI8rHkcKeVPhEQ6/qZiKSMsgt0mEgx48CzXNkleNKbnO9/VAFuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBLKCrbzL9aQkHaejBanpFlwS+yEtXN3OoFrN/WeDuIwbEd5FhbI4="
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
      "state": "tx_+NQLAfiEuEDPNF95n/RPxa4c3X0oYBvvEshiIxJH15umhA+X688zPuUBjQ5/B/g4ApehpFZrdwNQngA9+z+kIRey2R9fztcDuEDib89/esJQdA6Iku+BaeTgGqBYJnAmkOQwHToYI8rHkcKeVPhEQ6/qZiKSMsgt0mEgx48CzXNkleNKbnO9/VAFuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBLKCrbzL9aQkHaejBanpFlwS+yEtXN3OoFrN/WeDuIwbEd5FhbI4="
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
    "contract_id": "ct_2QXiPEuRnBEmXBAaztbLhXEwrsNkgr26pkkRHrYGV2THRVmPJD"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEtoB7y7zB2AnL88qIqD2OsJvqcTAe/dZ/gJ6qDZB6dz1iCTcQocg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 1,
          "call_data": "cb_KxFLBQ6pKwIEOyoYQQ==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2QXiPEuRnBEmXBAaztbLhXEwrsNkgr26pkkRHrYGV2THRVmPJD",
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
    "signed_tx": "tx_+JILAfhCuEA5FJq72QoFNrClEqfedXT8p6TNUpwZoFGzKTsHArwMPcwVdG69Hgd1YoJ00UTlumOOHwuh2MZW5nfHfiz3/H0IuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBLaAe8u8wdgJy/PKiKg9jrCb6nEwHv3Wf4Ceqg2Qenc9YgtJm8A4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "signed_tx": "tx_+JILAfhCuEA5FJq72QoFNrClEqfedXT8p6TNUpwZoFGzKTsHArwMPcwVdG69Hgd1YoJ00UTlumOOHwuh2MZW5nfHfiz3/H0IuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBLaAe8u8wdgJy/PKiKg9jrCb6nEwHv3Wf4Ceqg2Qenc9YgtJm8A4=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 1,
          "call_data": "cb_KxFLBQ6pKwIEOyoYQQ==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2QXiPEuRnBEmXBAaztbLhXEwrsNkgr26pkkRHrYGV2THRVmPJD",
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
    "signed_tx": "tx_+NQLAfiEuEA5FJq72QoFNrClEqfedXT8p6TNUpwZoFGzKTsHArwMPcwVdG69Hgd1YoJ00UTlumOOHwuh2MZW5nfHfiz3/H0IuED81sodW+H+ua2zARtAWrvBPP56+XnTf/RSMjq1r8vo91tG8j1KDqlCSH3tpxO97xKBIIeYaxqsh0EsNwzWIbYBuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBLaAe8u8wdgJy/PKiKg9jrCb6nEwHv3Wf4Ceqg2Qenc9Ygi8Dzm4="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NQLAfiEuEA5FJq72QoFNrClEqfedXT8p6TNUpwZoFGzKTsHArwMPcwVdG69Hgd1YoJ00UTlumOOHwuh2MZW5nfHfiz3/H0IuED81sodW+H+ua2zARtAWrvBPP56+XnTf/RSMjq1r8vo91tG8j1KDqlCSH3tpxO97xKBIIeYaxqsh0EsNwzWIbYBuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBLaAe8u8wdgJy/PKiKg9jrCb6nEwHv3Wf4Ceqg2Qenc9Ygi8Dzm4="
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
      "state": "tx_+NQLAfiEuEA5FJq72QoFNrClEqfedXT8p6TNUpwZoFGzKTsHArwMPcwVdG69Hgd1YoJ00UTlumOOHwuh2MZW5nfHfiz3/H0IuED81sodW+H+ua2zARtAWrvBPP56+XnTf/RSMjq1r8vo91tG8j1KDqlCSH3tpxO97xKBIIeYaxqsh0EsNwzWIbYBuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBLaAe8u8wdgJy/PKiKg9jrCb6nEwHv3Wf4Ceqg2Qenc9Ygi8Dzm4="
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
    "contract_id": "ct_2QXiPEuRnBEmXBAaztbLhXEwrsNkgr26pkkRHrYGV2THRVmPJD",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 301,
      "contract_id": "ct_2QXiPEuRnBEmXBAaztbLhXEwrsNkgr26pkkRHrYGV2THRVmPJD",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEuoA5+Oy6lYR5AJSHLGFUq3i1RDbbf2kAghK6V+wIXziXJGt6+9w==",
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
  "id": -576460752303421263,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEAq0RcQL0y1MGe3l25sUAl0FNX6yPDxMeyogj3mKY9gFQpXre3zoTcD7jNpvFl05JEi1u25Y2yZuurlHWOraNcBuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBLqAOfjsupWEeQCUhyxhVKt4tUQ2239pAIISulfsCF84lyVBV9uc="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "signed_tx": "tx_+JILAfhCuEAq0RcQL0y1MGe3l25sUAl0FNX6yPDxMeyogj3mKY9gFQpXre3zoTcD7jNpvFl05JEi1u25Y2yZuurlHWOraNcBuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBLqAOfjsupWEeQCUhyxhVKt4tUQ2239pAIISulfsCF84lyVBV9uc=",
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
  "id": -576460752303421262,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEAq0RcQL0y1MGe3l25sUAl0FNX6yPDxMeyogj3mKY9gFQpXre3zoTcD7jNpvFl05JEi1u25Y2yZuurlHWOraNcBuEDR5Z31e2o9SP2oKHGxhCTp5x4Rk9UZHnc79LkwQzWJU+vteZMhR/Dec0M89Igg7923BY3wvcofYSUKZkOlzY0BuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBLqAOfjsupWEeQCUhyxhVKt4tUQ2239pAIISulfsCF84lyXOPXJ8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NQLAfiEuEAq0RcQL0y1MGe3l25sUAl0FNX6yPDxMeyogj3mKY9gFQpXre3zoTcD7jNpvFl05JEi1u25Y2yZuurlHWOraNcBuEDR5Z31e2o9SP2oKHGxhCTp5x4Rk9UZHnc79LkwQzWJU+vteZMhR/Dec0M89Igg7923BY3wvcofYSUKZkOlzY0BuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBLqAOfjsupWEeQCUhyxhVKt4tUQ2239pAIISulfsCF84lyXOPXJ8="
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
      "state": "tx_+NQLAfiEuEAq0RcQL0y1MGe3l25sUAl0FNX6yPDxMeyogj3mKY9gFQpXre3zoTcD7jNpvFl05JEi1u25Y2yZuurlHWOraNcBuEDR5Z31e2o9SP2oKHGxhCTp5x4Rk9UZHnc79LkwQzWJU+vteZMhR/Dec0M89Igg7923BY3wvcofYSUKZkOlzY0BuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBLqAOfjsupWEeQCUhyxhVKt4tUQ2239pAIISulfsCF84lyXOPXJ8="
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
    "contract_id": "ct_2iTYMd5dSUHsLyhBtPeD7m1GCZHVn4aaU5QUtSrGEkBKHyBgn3"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEvoA3pueTZE+Tvac09ws6rymxC0yKZ4nW5J6hUfJ5k/EYc2A99mQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 1,
          "call_data": "cb_KxFLBQ6pKwIEOyoYQQ==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2iTYMd5dSUHsLyhBtPeD7m1GCZHVn4aaU5QUtSrGEkBKHyBgn3",
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
    "signed_tx": "tx_+JILAfhCuEA0RqLpWBUdAI9KiZsoQvISVNNlilAZPj8prVQE/6PGuxveg5jZameQ8W62IjE43h21aeVYwlcWPiuLdFcU6kkPuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBL6AN6bnk2RPk72nNPcLOq8psQtMimeJ1uSeoVHyeZPxGHKWXYMA="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "signed_tx": "tx_+JILAfhCuEA0RqLpWBUdAI9KiZsoQvISVNNlilAZPj8prVQE/6PGuxveg5jZameQ8W62IjE43h21aeVYwlcWPiuLdFcU6kkPuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBL6AN6bnk2RPk72nNPcLOq8psQtMimeJ1uSeoVHyeZPxGHKWXYMA=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 1,
          "call_data": "cb_KxFLBQ6pKwIEOyoYQQ==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2iTYMd5dSUHsLyhBtPeD7m1GCZHVn4aaU5QUtSrGEkBKHyBgn3",
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
    "signed_tx": "tx_+NQLAfiEuEA0RqLpWBUdAI9KiZsoQvISVNNlilAZPj8prVQE/6PGuxveg5jZameQ8W62IjE43h21aeVYwlcWPiuLdFcU6kkPuECfJ/Gn1fENKRouaXmKaBVSeqHhG50HtZqqddjhzIj/40U1yw3vJorhWaaRWxw/0dQcU2P/Dczj9+bq1M+YG5AOuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBL6AN6bnk2RPk72nNPcLOq8psQtMimeJ1uSeoVHyeZPxGHNqt5W4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NQLAfiEuEA0RqLpWBUdAI9KiZsoQvISVNNlilAZPj8prVQE/6PGuxveg5jZameQ8W62IjE43h21aeVYwlcWPiuLdFcU6kkPuECfJ/Gn1fENKRouaXmKaBVSeqHhG50HtZqqddjhzIj/40U1yw3vJorhWaaRWxw/0dQcU2P/Dczj9+bq1M+YG5AOuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBL6AN6bnk2RPk72nNPcLOq8psQtMimeJ1uSeoVHyeZPxGHNqt5W4="
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
      "state": "tx_+NQLAfiEuEA0RqLpWBUdAI9KiZsoQvISVNNlilAZPj8prVQE/6PGuxveg5jZameQ8W62IjE43h21aeVYwlcWPiuLdFcU6kkPuECfJ/Gn1fENKRouaXmKaBVSeqHhG50HtZqqddjhzIj/40U1yw3vJorhWaaRWxw/0dQcU2P/Dczj9+bq1M+YG5AOuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBL6AN6bnk2RPk72nNPcLOq8psQtMimeJ1uSeoVHyeZPxGHNqt5W4="
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
    "contract_id": "ct_2iTYMd5dSUHsLyhBtPeD7m1GCZHVn4aaU5QUtSrGEkBKHyBgn3",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 303,
      "contract_id": "ct_2iTYMd5dSUHsLyhBtPeD7m1GCZHVn4aaU5QUtSrGEkBKHyBgn3",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEwoKKaDo72zWVOj5OTTK04D/S0yqY/C24+SFAXuK8r2GLnqgrKJQ==",
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
  "id": -576460752303421259,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEDQLv/Oaf2lPK9aYbKbL/rfZMXK9AdN2LlwyqAbJh61GU8WunSNNKnBorDcwnzYeE9cMwPN7AC6ymT1NoPfPbkMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBMKCimg6O9s1lTo+Tk0ytOA/0tMqmPwtuPkhQF7ivK9hi5z4VLA4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "signed_tx": "tx_+JILAfhCuEDQLv/Oaf2lPK9aYbKbL/rfZMXK9AdN2LlwyqAbJh61GU8WunSNNKnBorDcwnzYeE9cMwPN7AC6ymT1NoPfPbkMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBMKCimg6O9s1lTo+Tk0ytOA/0tMqmPwtuPkhQF7ivK9hi5z4VLA4=",
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
  "id": -576460752303421258,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEC8PchaqC+N4V473E4EMhCyXZEHBbKaVOFokw1eNGv4Gv5RnsYHNxJqISSewPsH7JGSvKR7s0ob1xSO6o1/DrYFuEDQLv/Oaf2lPK9aYbKbL/rfZMXK9AdN2LlwyqAbJh61GU8WunSNNKnBorDcwnzYeE9cMwPN7AC6ymT1NoPfPbkMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBMKCimg6O9s1lTo+Tk0ytOA/0tMqmPwtuPkhQF7ivK9hi5+rfns0="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NQLAfiEuEC8PchaqC+N4V473E4EMhCyXZEHBbKaVOFokw1eNGv4Gv5RnsYHNxJqISSewPsH7JGSvKR7s0ob1xSO6o1/DrYFuEDQLv/Oaf2lPK9aYbKbL/rfZMXK9AdN2LlwyqAbJh61GU8WunSNNKnBorDcwnzYeE9cMwPN7AC6ymT1NoPfPbkMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBMKCimg6O9s1lTo+Tk0ytOA/0tMqmPwtuPkhQF7ivK9hi5+rfns0="
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
      "state": "tx_+NQLAfiEuEC8PchaqC+N4V473E4EMhCyXZEHBbKaVOFokw1eNGv4Gv5RnsYHNxJqISSewPsH7JGSvKR7s0ob1xSO6o1/DrYFuEDQLv/Oaf2lPK9aYbKbL/rfZMXK9AdN2LlwyqAbJh61GU8WunSNNKnBorDcwnzYeE9cMwPN7AC6ymT1NoPfPbkMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBMKCimg6O9s1lTo+Tk0ytOA/0tMqmPwtuPkhQF7ivK9hi5+rfns0="
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
    "contract_id": "ct_DUYqERhpCQshuNtwLTeoq4zZZ9BH3Cfh4tuYuDTZAXaB89poW"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggExoFZlTAqHHREYRqLRv1aLY1vyrBt292RSaxnTgSnLUaaxsddnpA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 1,
          "call_data": "cb_KxFLBQ6pKwIEOyoYQQ==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_DUYqERhpCQshuNtwLTeoq4zZZ9BH3Cfh4tuYuDTZAXaB89poW",
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
    "signed_tx": "tx_+JILAfhCuEA/Kff2xWXNaJ4YyEy3NVrh4MKQCJmYBpxLuTPyElPoYPh897hyuO5rishODwt8t6wF4ScoUAZjfF0OQj6FQvEKuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBMaBWZUwKhx0RGEai0b9Wi2Nb8qwbdvdkUmsZ04Epy1GmsXfVPRU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "signed_tx": "tx_+JILAfhCuEA/Kff2xWXNaJ4YyEy3NVrh4MKQCJmYBpxLuTPyElPoYPh897hyuO5rishODwt8t6wF4ScoUAZjfF0OQj6FQvEKuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBMaBWZUwKhx0RGEai0b9Wi2Nb8qwbdvdkUmsZ04Epy1GmsXfVPRU=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 1,
          "call_data": "cb_KxFLBQ6pKwIEOyoYQQ==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_DUYqERhpCQshuNtwLTeoq4zZZ9BH3Cfh4tuYuDTZAXaB89poW",
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
    "signed_tx": "tx_+NQLAfiEuEA/Kff2xWXNaJ4YyEy3NVrh4MKQCJmYBpxLuTPyElPoYPh897hyuO5rishODwt8t6wF4ScoUAZjfF0OQj6FQvEKuEB5iMt6k4EkT6HuawHKdaT0HPxjBUbOwoqt4ZKrJOD9+SRWIcSUHkn8L63OMVqh0V60IfCuYTDlYafvp6qTM5wDuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBMaBWZUwKhx0RGEai0b9Wi2Nb8qwbdvdkUmsZ04Epy1GmsVUM4N8="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NQLAfiEuEA/Kff2xWXNaJ4YyEy3NVrh4MKQCJmYBpxLuTPyElPoYPh897hyuO5rishODwt8t6wF4ScoUAZjfF0OQj6FQvEKuEB5iMt6k4EkT6HuawHKdaT0HPxjBUbOwoqt4ZKrJOD9+SRWIcSUHkn8L63OMVqh0V60IfCuYTDlYafvp6qTM5wDuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBMaBWZUwKhx0RGEai0b9Wi2Nb8qwbdvdkUmsZ04Epy1GmsVUM4N8="
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
      "state": "tx_+NQLAfiEuEA/Kff2xWXNaJ4YyEy3NVrh4MKQCJmYBpxLuTPyElPoYPh897hyuO5rishODwt8t6wF4ScoUAZjfF0OQj6FQvEKuEB5iMt6k4EkT6HuawHKdaT0HPxjBUbOwoqt4ZKrJOD9+SRWIcSUHkn8L63OMVqh0V60IfCuYTDlYafvp6qTM5wDuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBMaBWZUwKhx0RGEai0b9Wi2Nb8qwbdvdkUmsZ04Epy1GmsVUM4N8="
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
    "contract_id": "ct_DUYqERhpCQshuNtwLTeoq4zZZ9BH3Cfh4tuYuDTZAXaB89poW",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "caller_nonce": 305,
      "contract_id": "ct_DUYqERhpCQshuNtwLTeoq4zZZ9BH3Cfh4tuYuDTZAXaB89poW",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEyoAhhdjrkJIjV5Ry0XocOLotML/Z2VXRNiihfc1O9/nnF9/wgXg==",
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
  "id": -576460752303421255,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEASjG9tf7CHKYdMLvFIrkSelJ5ta0HCGdivDDOlCgAKAzKNwEPNGsoe9Ydjn6M9Cut2j5FQ40ttiAd5MBOCNzsAuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBMqAIYXY65CSI1eUctF6HDi6LTC/2dlV0TYooX3NTvf55xWV9NkU="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "signed_tx": "tx_+JILAfhCuEASjG9tf7CHKYdMLvFIrkSelJ5ta0HCGdivDDOlCgAKAzKNwEPNGsoe9Ydjn6M9Cut2j5FQ40ttiAd5MBOCNzsAuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBMqAIYXY65CSI1eUctF6HDi6LTC/2dlV0TYooX3NTvf55xWV9NkU=",
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
  "id": -576460752303421254,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEASjG9tf7CHKYdMLvFIrkSelJ5ta0HCGdivDDOlCgAKAzKNwEPNGsoe9Ydjn6M9Cut2j5FQ40ttiAd5MBOCNzsAuECcOAEz3PfrD6wfkZtYU8wX7SmpK7WTKlnoX0w2Ob8gAqVvdVYvSVv6ho1Ni1soukHgMrDpBqAH4TmWdCY/4mYFuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBMqAIYXY65CSI1eUctF6HDi6LTC/2dlV0TYooX3NTvf55xVk/s2s="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NQLAfiEuEASjG9tf7CHKYdMLvFIrkSelJ5ta0HCGdivDDOlCgAKAzKNwEPNGsoe9Ydjn6M9Cut2j5FQ40ttiAd5MBOCNzsAuECcOAEz3PfrD6wfkZtYU8wX7SmpK7WTKlnoX0w2Ob8gAqVvdVYvSVv6ho1Ni1soukHgMrDpBqAH4TmWdCY/4mYFuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBMqAIYXY65CSI1eUctF6HDi6LTC/2dlV0TYooX3NTvf55xVk/s2s="
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
      "state": "tx_+NQLAfiEuEASjG9tf7CHKYdMLvFIrkSelJ5ta0HCGdivDDOlCgAKAzKNwEPNGsoe9Ydjn6M9Cut2j5FQ40ttiAd5MBOCNzsAuECcOAEz3PfrD6wfkZtYU8wX7SmpK7WTKlnoX0w2Ob8gAqVvdVYvSVv6ho1Ni1soukHgMrDpBqAH4TmWdCY/4mYFuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBMqAIYXY65CSI1eUctF6HDi6LTC/2dlV0TYooX3NTvf55xVk/s2s="
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
    "contract_id": "ct_W9Tdbjgngtd1oAwqMg7MnxiaY29DUF7BC6Uzv49CTc8B34Esc"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEzoKjPyWgOyNj3klt7ZvTkwwWLhUgt/gJPQ3vsVeeEpqHkFFuMoA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 1,
          "call_data": "cb_KxFLBQ6pKwIEOyoYQQ==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_W9Tdbjgngtd1oAwqMg7MnxiaY29DUF7BC6Uzv49CTc8B34Esc",
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
    "signed_tx": "tx_+JILAfhCuEBlt6iedzldmNuV7JqvDulmyeNxdEF30WAxUJd2ExMVFOeRChqxG+BPeUljjUETcR6Pyzcmt7Ch6M0xcIsJLGgNuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBM6Coz8loDsjY95Jbe2b05MMFi4VILf4CT0N77FXnhKah5LBF97c="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
      "signed_tx": "tx_+JILAfhCuEBlt6iedzldmNuV7JqvDulmyeNxdEF30WAxUJd2ExMVFOeRChqxG+BPeUljjUETcR6Pyzcmt7Ch6M0xcIsJLGgNuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBM6Coz8loDsjY95Jbe2b05MMFi4VILf4CT0N77FXnhKah5LBF97c=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 1,
          "call_data": "cb_KxFLBQ6pKwIEOyoYQQ==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_W9Tdbjgngtd1oAwqMg7MnxiaY29DUF7BC6Uzv49CTc8B34Esc",
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
    "signed_tx": "tx_+NQLAfiEuEBEK5HDic7Spc4c2h3s4g0Xy8exkn8Gf9oYC0AptUhs4xyGBFxHnYURv7PIlncSplIyHWqYjbnQbLywyihu7RcNuEBlt6iedzldmNuV7JqvDulmyeNxdEF30WAxUJd2ExMVFOeRChqxG+BPeUljjUETcR6Pyzcmt7Ch6M0xcIsJLGgNuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBM6Coz8loDsjY95Jbe2b05MMFi4VILf4CT0N77FXnhKah5DSDWxg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+NQLAfiEuEBEK5HDic7Spc4c2h3s4g0Xy8exkn8Gf9oYC0AptUhs4xyGBFxHnYURv7PIlncSplIyHWqYjbnQbLywyihu7RcNuEBlt6iedzldmNuV7JqvDulmyeNxdEF30WAxUJd2ExMVFOeRChqxG+BPeUljjUETcR6Pyzcmt7Ch6M0xcIsJLGgNuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBM6Coz8loDsjY95Jbe2b05MMFi4VILf4CT0N77FXnhKah5DSDWxg="
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
      "state": "tx_+NQLAfiEuEBEK5HDic7Spc4c2h3s4g0Xy8exkn8Gf9oYC0AptUhs4xyGBFxHnYURv7PIlncSplIyHWqYjbnQbLywyihu7RcNuEBlt6iedzldmNuV7JqvDulmyeNxdEF30WAxUJd2ExMVFOeRChqxG+BPeUljjUETcR6Pyzcmt7Ch6M0xcIsJLGgNuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBM6Coz8loDsjY95Jbe2b05MMFi4VILf4CT0N77FXnhKah5DSDWxg="
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
    "contract_id": "ct_W9Tdbjgngtd1oAwqMg7MnxiaY29DUF7BC6Uzv49CTc8B34Esc",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
      "caller_nonce": 307,
      "contract_id": "ct_W9Tdbjgngtd1oAwqMg7MnxiaY29DUF7BC6Uzv49CTc8B34Esc",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421250,
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
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection
