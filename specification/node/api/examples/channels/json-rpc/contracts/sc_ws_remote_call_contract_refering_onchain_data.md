
#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 3,
    "call_data": "cb_KxFE1kQfP4oEp9E=",
    "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
        "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
    "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
        "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
    "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
        "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
    "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEEoJThbWyyXyvhZe7hDgCTj6RvwTnv4FurmvAibEioYIMVHJSByw==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
  "id": -576460752303421347,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEAeUHH93p6F+SY4hnyAqUeQURs1PCc+8cEZU9PKdrGFhXxcp7Vk3uIDg5zsPirLiRFN/eVj6tgUNQEGQLFqiuYBuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBBKCU4W1ssl8r4WXu4Q4Ak4+kb8E57+Bbq5rwImxIqGCDFd5dEkY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421347,
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
      "signed_tx": "tx_+JILAfhCuEAeUHH93p6F+SY4hnyAqUeQURs1PCc+8cEZU9PKdrGFhXxcp7Vk3uIDg5zsPirLiRFN/eVj6tgUNQEGQLFqiuYBuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBBKCU4W1ssl8r4WXu4Q4Ak4+kb8E57+Bbq5rwImxIqGCDFd5dEkY=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
  "id": -576460752303421346,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEAeUHH93p6F+SY4hnyAqUeQURs1PCc+8cEZU9PKdrGFhXxcp7Vk3uIDg5zsPirLiRFN/eVj6tgUNQEGQLFqiuYBuECDpmNntjvCwMkv5hc1EqTmeL+d9X3txqBm9VT8/G8qq8RXPktE3dJb8tT5eYIIoSOpIQ01LHMNdvA7HUXjpEIFuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBBKCU4W1ssl8r4WXu4Q4Ak4+kb8E57+Bbq5rwImxIqGCDFazHewI="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421346,
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
      "state": "tx_+NQLAfiEuEAeUHH93p6F+SY4hnyAqUeQURs1PCc+8cEZU9PKdrGFhXxcp7Vk3uIDg5zsPirLiRFN/eVj6tgUNQEGQLFqiuYBuECDpmNntjvCwMkv5hc1EqTmeL+d9X3txqBm9VT8/G8qq8RXPktE3dJb8tT5eYIIoSOpIQ01LHMNdvA7HUXjpEIFuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBBKCU4W1ssl8r4WXu4Q4Ak4+kb8E57+Bbq5rwImxIqGCDFazHewI="
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
      "state": "tx_+NQLAfiEuEAeUHH93p6F+SY4hnyAqUeQURs1PCc+8cEZU9PKdrGFhXxcp7Vk3uIDg5zsPirLiRFN/eVj6tgUNQEGQLFqiuYBuECDpmNntjvCwMkv5hc1EqTmeL+d9X3txqBm9VT8/G8qq8RXPktE3dJb8tT5eYIIoSOpIQ01LHMNdvA7HUXjpEIFuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBBKCU4W1ssl8r4WXu4Q4Ak4+kb8E57+Bbq5rwImxIqGCDFazHewI="
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
    "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
        "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
    "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
        "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
    "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
        "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
    "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEFoAsAAhVMzTI+XXLvpN5O1GklklFHkRk9paM72bKQrRmbKGciog==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
  "id": -576460752303421345,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEBPR5WKsfJ1hJcS3vCESjZWVdKYao0Uwz3aOuLnMtnmPcPdWUXEakhKVHwCkyemlQ1USNoNndA3nJpuCp8b69wEuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBBaALAAIVTM0yPl1y76TeTtRpJZJRR5EZPaWjO9mykK0Zm8Ok9QY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421345,
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
      "signed_tx": "tx_+JILAfhCuEBPR5WKsfJ1hJcS3vCESjZWVdKYao0Uwz3aOuLnMtnmPcPdWUXEakhKVHwCkyemlQ1USNoNndA3nJpuCp8b69wEuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBBaALAAIVTM0yPl1y76TeTtRpJZJRR5EZPaWjO9mykK0Zm8Ok9QY=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
  "id": -576460752303421344,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEBPR5WKsfJ1hJcS3vCESjZWVdKYao0Uwz3aOuLnMtnmPcPdWUXEakhKVHwCkyemlQ1USNoNndA3nJpuCp8b69wEuEDzF2H/0/uYzdZ+facV+tytx2FFFXzTfZVbgN/pLOYncM5xJSVGiymGdgWd7PXELXLimPT+4wTMyqURVJub6MMJuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBBaALAAIVTM0yPl1y76TeTtRpJZJRR5EZPaWjO9mykK0Zm4bGaqY="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421344,
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
      "state": "tx_+NQLAfiEuEBPR5WKsfJ1hJcS3vCESjZWVdKYao0Uwz3aOuLnMtnmPcPdWUXEakhKVHwCkyemlQ1USNoNndA3nJpuCp8b69wEuEDzF2H/0/uYzdZ+facV+tytx2FFFXzTfZVbgN/pLOYncM5xJSVGiymGdgWd7PXELXLimPT+4wTMyqURVJub6MMJuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBBaALAAIVTM0yPl1y76TeTtRpJZJRR5EZPaWjO9mykK0Zm4bGaqY="
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
      "state": "tx_+NQLAfiEuEBPR5WKsfJ1hJcS3vCESjZWVdKYao0Uwz3aOuLnMtnmPcPdWUXEakhKVHwCkyemlQ1USNoNndA3nJpuCp8b69wEuEDzF2H/0/uYzdZ+facV+tytx2FFFXzTfZVbgN/pLOYncM5xJSVGiymGdgWd7PXELXLimPT+4wTMyqURVJub6MMJuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBBaALAAIVTM0yPl1y76TeTtRpJZJRR5EZPaWjO9mykK0Zm4bGaqY="
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
  }
}
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
  }
}
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "ABCDEFG",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
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
      "caller_nonce": 262,
      "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
      "gas_price": 1,
      "gas_used": 122,
      "height": 262,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "ABCDEFG",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
  }
}
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
  }
}
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "ABCDEFG",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
  }
}
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "ABCDEFG",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEGoJaPvc69F74U56XY9wJsCujwis7NkzYyILM97P/SHZSj5cawsA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
  "id": -576460752303421343,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEAXRqIThgtJgJgJdjIP8KTLSOQcmh/K14ET+l+kReBv/yaGFAeADvWI+MtDH/UkIANL0AecfaHhqbxXIiix7UgPuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBBqCWj73OvRe+FOel2PcCbAro8IrOzZM2MiCzPez/0h2Uo+CBSE0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421343,
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
      "signed_tx": "tx_+JILAfhCuEAXRqIThgtJgJgJdjIP8KTLSOQcmh/K14ET+l+kReBv/yaGFAeADvWI+MtDH/UkIANL0AecfaHhqbxXIiix7UgPuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBBqCWj73OvRe+FOel2PcCbAro8IrOzZM2MiCzPez/0h2Uo+CBSE0=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
  "id": -576460752303421342,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEAXRqIThgtJgJgJdjIP8KTLSOQcmh/K14ET+l+kReBv/yaGFAeADvWI+MtDH/UkIANL0AecfaHhqbxXIiix7UgPuEA5gvaxgD4ZEkdhKobBBf6B5EuF3kDrDaazANoFJ41KE7MbFu3XMsqnHEiLhBMTZ+SncgR346eVA7y0QjQXQ3wDuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBBqCWj73OvRe+FOel2PcCbAro8IrOzZM2MiCzPez/0h2Uo9CNmlU="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421342,
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
      "state": "tx_+NQLAfiEuEAXRqIThgtJgJgJdjIP8KTLSOQcmh/K14ET+l+kReBv/yaGFAeADvWI+MtDH/UkIANL0AecfaHhqbxXIiix7UgPuEA5gvaxgD4ZEkdhKobBBf6B5EuF3kDrDaazANoFJ41KE7MbFu3XMsqnHEiLhBMTZ+SncgR346eVA7y0QjQXQ3wDuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBBqCWj73OvRe+FOel2PcCbAro8IrOzZM2MiCzPez/0h2Uo9CNmlU="
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
      "state": "tx_+NQLAfiEuEAXRqIThgtJgJgJdjIP8KTLSOQcmh/K14ET+l+kReBv/yaGFAeADvWI+MtDH/UkIANL0AecfaHhqbxXIiix7UgPuEA5gvaxgD4ZEkdhKobBBf6B5EuF3kDrDaazANoFJ41KE7MbFu3XMsqnHEiLhBMTZ+SncgR346eVA7y0QjQXQ3wDuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBBqCWj73OvRe+FOel2PcCbAro8IrOzZM2MiCzPez/0h2Uo9CNmlU="
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
    "round": 262
  }
}
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
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
        "round": 262
      }
    }
  },
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
    "round": 262
  }
}
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
        "round": 262
      }
    }
  },
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
    "round": 262
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
      "caller_nonce": 262,
      "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
      "gas_price": 1,
      "gas_used": 122,
      "height": 262,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
    "round": 262
  }
}
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
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
        "round": 262
      }
    }
  },
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
    "round": 262
  }
}
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
        "round": 262
      }
    }
  },
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
    "round": 262
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
      "caller_nonce": 262,
      "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
      "gas_price": 1,
      "gas_used": 122,
      "height": 262,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
  }
}
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
  }
}
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "ABCDEFG",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
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
      "caller_nonce": 263,
      "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
      "gas_price": 1,
      "gas_used": 122,
      "height": 263,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "ABCDEFG",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
  }
}
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
  }
}
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "ABCDEFG",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
  }
}
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "ABCDEFG",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEHoGLWMdbm7GOIZqLsAm9DgRaJO0Eyq7htjRv64xhe9a4nPTk3Cg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
  "id": -576460752303421341,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEDpccJmXfHzt0aOv44eoFDFt8uJ4shqSzCVRQImHUZZht+LFdDH3K5GD5xpitkNVnibJ/D2lcBSCaTY3wwLHT4NuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBB6Bi1jHW5uxjiGai7AJvQ4EWiTtBMqu4bY0b+uMYXvWuJ5fd9ew="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421341,
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
      "signed_tx": "tx_+JILAfhCuEDpccJmXfHzt0aOv44eoFDFt8uJ4shqSzCVRQImHUZZht+LFdDH3K5GD5xpitkNVnibJ/D2lcBSCaTY3wwLHT4NuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBB6Bi1jHW5uxjiGai7AJvQ4EWiTtBMqu4bY0b+uMYXvWuJ5fd9ew=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
  "id": -576460752303421340,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEDpccJmXfHzt0aOv44eoFDFt8uJ4shqSzCVRQImHUZZht+LFdDH3K5GD5xpitkNVnibJ/D2lcBSCaTY3wwLHT4NuED222WpG0DlNJaShrpv1bBgA7yc6Xt2Xw7TvHZGJp2JfMHJ/MDtFgrxO64OXB4owyXBapQGL5tdl3KQzchQ4lsHuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBB6Bi1jHW5uxjiGai7AJvQ4EWiTtBMqu4bY0b+uMYXvWuJwdFNAw="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421340,
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
      "state": "tx_+NQLAfiEuEDpccJmXfHzt0aOv44eoFDFt8uJ4shqSzCVRQImHUZZht+LFdDH3K5GD5xpitkNVnibJ/D2lcBSCaTY3wwLHT4NuED222WpG0DlNJaShrpv1bBgA7yc6Xt2Xw7TvHZGJp2JfMHJ/MDtFgrxO64OXB4owyXBapQGL5tdl3KQzchQ4lsHuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBB6Bi1jHW5uxjiGai7AJvQ4EWiTtBMqu4bY0b+uMYXvWuJwdFNAw="
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
      "state": "tx_+NQLAfiEuEDpccJmXfHzt0aOv44eoFDFt8uJ4shqSzCVRQImHUZZht+LFdDH3K5GD5xpitkNVnibJ/D2lcBSCaTY3wwLHT4NuED222WpG0DlNJaShrpv1bBgA7yc6Xt2Xw7TvHZGJp2JfMHJ/MDtFgrxO64OXB4owyXBapQGL5tdl3KQzchQ4lsHuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBB6Bi1jHW5uxjiGai7AJvQ4EWiTtBMqu4bY0b+uMYXvWuJwdFNAw="
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
    "round": 263
  }
}
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
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
        "round": 263
      }
    }
  },
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
    "round": 263
  }
}
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
        "round": 263
      }
    }
  },
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
    "round": 263
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
      "caller_nonce": 263,
      "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
      "gas_price": 1,
      "gas_used": 122,
      "height": 263,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
    "round": 263
  }
}
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
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
        "round": 263
      }
    }
  },
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
    "round": 263
  }
}
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
        "round": 263
      }
    }
  },
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
    "round": 263
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
      "caller_nonce": 263,
      "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
      "gas_price": 1,
      "gas_used": 122,
      "height": 263,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
  }
}
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
  }
}
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "ABCDEFG",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
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
      "caller_nonce": 264,
      "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
      "gas_price": 1,
      "gas_used": 276,
      "height": 264,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "ABCDEFG",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
  }
}
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
  }
}
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "ABCDEFG",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
  }
}
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "ABCDEFG",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEIoM7Hp+y2AVeSi2VIEhU7kzT+J22t/NO3saaPQ41z7nGVUQ7keQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
  "id": -576460752303421339,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuECEKwFc3M32Y0PrOZpPvyBYxOUTEqzI4X2tly6aAoKn5D6OcSYoGGlMIDnCsudqxtb5EfXr6c307kKOi/QgKXkCuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBCKDOx6fstgFXkotlSBIVO5M0/idtrfzTt7Gmj0ONc+5xlR/Hc98="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421339,
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
      "signed_tx": "tx_+JILAfhCuECEKwFc3M32Y0PrOZpPvyBYxOUTEqzI4X2tly6aAoKn5D6OcSYoGGlMIDnCsudqxtb5EfXr6c307kKOi/QgKXkCuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBCKDOx6fstgFXkotlSBIVO5M0/idtrfzTt7Gmj0ONc+5xlR/Hc98=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
  "id": -576460752303421338,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuECEKwFc3M32Y0PrOZpPvyBYxOUTEqzI4X2tly6aAoKn5D6OcSYoGGlMIDnCsudqxtb5EfXr6c307kKOi/QgKXkCuECs7E/OJP+Ee/Cu89pB12+Y13pTcyQaMGDaKJjiMuCL9IXS+iq59O04AhQxsINixNSYBjejayAOJTC20C/S6WsMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBCKDOx6fstgFXkotlSBIVO5M0/idtrfzTt7Gmj0ONc+5xlT7qqxM="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421338,
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
      "state": "tx_+NQLAfiEuECEKwFc3M32Y0PrOZpPvyBYxOUTEqzI4X2tly6aAoKn5D6OcSYoGGlMIDnCsudqxtb5EfXr6c307kKOi/QgKXkCuECs7E/OJP+Ee/Cu89pB12+Y13pTcyQaMGDaKJjiMuCL9IXS+iq59O04AhQxsINixNSYBjejayAOJTC20C/S6WsMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBCKDOx6fstgFXkotlSBIVO5M0/idtrfzTt7Gmj0ONc+5xlT7qqxM="
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
      "state": "tx_+NQLAfiEuECEKwFc3M32Y0PrOZpPvyBYxOUTEqzI4X2tly6aAoKn5D6OcSYoGGlMIDnCsudqxtb5EfXr6c307kKOi/QgKXkCuECs7E/OJP+Ee/Cu89pB12+Y13pTcyQaMGDaKJjiMuCL9IXS+iq59O04AhQxsINixNSYBjejayAOJTC20C/S6WsMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBCKDOx6fstgFXkotlSBIVO5M0/idtrfzTt7Gmj0ONc+5xlT7qqxM="
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
    "round": 264
  }
}
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
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
        "round": 264
      }
    }
  },
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
    "round": 264
  }
}
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
        "round": 264
      }
    }
  },
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
    "round": 264
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
      "caller_nonce": 264,
      "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
      "gas_price": 1,
      "gas_used": 276,
      "height": 264,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
    "round": 264
  }
}
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
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
        "round": 264
      }
    }
  },
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
    "round": 264
  }
}
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
        "round": 264
      }
    }
  },
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
    "round": 264
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
      "caller_nonce": 264,
      "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
      "gas_price": 1,
      "gas_used": 276,
      "height": 264,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
  }
}
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
  }
}
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "ABCDEFG",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
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
      "caller_nonce": 265,
      "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
      "gas_price": 1,
      "gas_used": 276,
      "height": 265,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "ABCDEFG",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
  }
}
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
  }
}
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "ABCDEFG",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
  }
}
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "ABCDEFG",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEJoPu43jp/HkxKy/j5agNhcpuACOSZ8HiaBOvV2RSDdXfp8UwBHw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
  "id": -576460752303421337,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEB6srJmhuI2JDtgzBoD2OqgHbsN0M0HLFgQUPFIuSQEKazNSQmj7yKH3LscR8JvM1bg2F/1dsjQNFvDscuO7XIEuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBCaD7uN46fx5MSsv4+WoDYXKbgAjkmfB4mgTr1dkUg3V36dW31pU="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421337,
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
      "signed_tx": "tx_+JILAfhCuEB6srJmhuI2JDtgzBoD2OqgHbsN0M0HLFgQUPFIuSQEKazNSQmj7yKH3LscR8JvM1bg2F/1dsjQNFvDscuO7XIEuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBCaD7uN46fx5MSsv4+WoDYXKbgAjkmfB4mgTr1dkUg3V36dW31pU=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
  "id": -576460752303421336,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEB6srJmhuI2JDtgzBoD2OqgHbsN0M0HLFgQUPFIuSQEKazNSQmj7yKH3LscR8JvM1bg2F/1dsjQNFvDscuO7XIEuEC2FYYcWWiapRsf3A8nS94Uxt0ru8Efm1HdghigaprFqAfdBklW28E9pjeSJ90pLZjvrG68pcT7wXWmCR0YtjcAuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBCaD7uN46fx5MSsv4+WoDYXKbgAjkmfB4mgTr1dkUg3V36d5dwSw="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421336,
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
      "state": "tx_+NQLAfiEuEB6srJmhuI2JDtgzBoD2OqgHbsN0M0HLFgQUPFIuSQEKazNSQmj7yKH3LscR8JvM1bg2F/1dsjQNFvDscuO7XIEuEC2FYYcWWiapRsf3A8nS94Uxt0ru8Efm1HdghigaprFqAfdBklW28E9pjeSJ90pLZjvrG68pcT7wXWmCR0YtjcAuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBCaD7uN46fx5MSsv4+WoDYXKbgAjkmfB4mgTr1dkUg3V36d5dwSw="
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
      "state": "tx_+NQLAfiEuEB6srJmhuI2JDtgzBoD2OqgHbsN0M0HLFgQUPFIuSQEKazNSQmj7yKH3LscR8JvM1bg2F/1dsjQNFvDscuO7XIEuEC2FYYcWWiapRsf3A8nS94Uxt0ru8Efm1HdghigaprFqAfdBklW28E9pjeSJ90pLZjvrG68pcT7wXWmCR0YtjcAuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBCaD7uN46fx5MSsv4+WoDYXKbgAjkmfB4mgTr1dkUg3V36d5dwSw="
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
    "round": 265
  }
}
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
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
        "round": 265
      }
    }
  },
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
    "round": 265
  }
}
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
        "round": 265
      }
    }
  },
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
    "round": 265
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
      "caller_nonce": 265,
      "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
      "gas_price": 1,
      "gas_used": 276,
      "height": 265,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
    "round": 265
  }
}
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
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
        "round": 265
      }
    }
  },
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
    "round": 265
  }
}
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
        "round": 265
      }
    }
  },
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
    "round": 265
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
      "caller_nonce": 265,
      "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
      "gas_price": 1,
      "gas_used": 276,
      "height": 265,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "ABCDEFG",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
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
      "caller_nonce": 266,
      "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
      "gas_price": 1,
      "gas_used": 122,
      "height": 266,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "ABCDEFG",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "ABCDEFG",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "ABCDEFG",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEKoL1L4F9CiBIUwjCg1/N2D1uNYsmCIfEg2ZUjhS2pReqGGWpecg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
  "id": -576460752303421335,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuED+HMFJRKpv9FsayxMNA4ucgYNMb+v/MFSKwIqRH70KsFgckShSy/ckCggpn70caa0NXwfiNdEsuXbUY/eSe5cMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBCqC9S+BfQogSFMIwoNfzdg9bjWLJgiHxINmVI4UtqUXqhlxdelU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421335,
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
      "signed_tx": "tx_+JILAfhCuED+HMFJRKpv9FsayxMNA4ucgYNMb+v/MFSKwIqRH70KsFgckShSy/ckCggpn70caa0NXwfiNdEsuXbUY/eSe5cMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBCqC9S+BfQogSFMIwoNfzdg9bjWLJgiHxINmVI4UtqUXqhlxdelU=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
  "id": -576460752303421334,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEDLygHEx/gCSa3rFFxx6+8nuBYw3p7QPqzMFXZFb7IBB7ag5JrvM9DGxWBB4Dibnr+t4cRKyeCFNjhGFA1BwEYFuED+HMFJRKpv9FsayxMNA4ucgYNMb+v/MFSKwIqRH70KsFgckShSy/ckCggpn70caa0NXwfiNdEsuXbUY/eSe5cMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBCqC9S+BfQogSFMIwoNfzdg9bjWLJgiHxINmVI4UtqUXqhr5rJWQ="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421334,
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
      "state": "tx_+NQLAfiEuEDLygHEx/gCSa3rFFxx6+8nuBYw3p7QPqzMFXZFb7IBB7ag5JrvM9DGxWBB4Dibnr+t4cRKyeCFNjhGFA1BwEYFuED+HMFJRKpv9FsayxMNA4ucgYNMb+v/MFSKwIqRH70KsFgckShSy/ckCggpn70caa0NXwfiNdEsuXbUY/eSe5cMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBCqC9S+BfQogSFMIwoNfzdg9bjWLJgiHxINmVI4UtqUXqhr5rJWQ="
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
      "state": "tx_+NQLAfiEuEDLygHEx/gCSa3rFFxx6+8nuBYw3p7QPqzMFXZFb7IBB7ag5JrvM9DGxWBB4Dibnr+t4cRKyeCFNjhGFA1BwEYFuED+HMFJRKpv9FsayxMNA4ucgYNMb+v/MFSKwIqRH70KsFgckShSy/ckCggpn70caa0NXwfiNdEsuXbUY/eSe5cMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBCqC9S+BfQogSFMIwoNfzdg9bjWLJgiHxINmVI4UtqUXqhr5rJWQ="
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
    "round": 266
  }
}
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
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
        "round": 266
      }
    }
  },
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
    "round": 266
  }
}
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
        "round": 266
      }
    }
  },
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
    "round": 266
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
      "caller_nonce": 266,
      "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
      "gas_price": 1,
      "gas_used": 122,
      "height": 266,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
    "round": 266
  }
}
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
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
        "round": 266
      }
    }
  },
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
    "round": 266
  }
}
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
        "round": 266
      }
    }
  },
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
    "round": 266
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
      "caller_nonce": 266,
      "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
      "gas_price": 1,
      "gas_used": 122,
      "height": 266,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "ABCDEFG",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
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
      "caller_nonce": 267,
      "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
      "gas_price": 1,
      "gas_used": 122,
      "height": 267,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "ABCDEFG",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "ABCDEFG",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "ABCDEFG",
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggELoE0JBRMEx+9o5NYQJdxb4dliybiE+lSf1KMWvTA262NfDvizHA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
  "id": -576460752303421333,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEBK8YhAsKkkkGGj5LBZ+PDhvzrhi94Z55o98eiJBA9hBcVWYXDSd7gPwM5M3vR6MGP/3nOPwF8LOD/mO0/dzAIFuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBC6BNCQUTBMfvaOTWECXcW+HZYsm4hPpUn9SjFr0wNutjX1eNriI="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421333,
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
      "signed_tx": "tx_+JILAfhCuEBK8YhAsKkkkGGj5LBZ+PDhvzrhi94Z55o98eiJBA9hBcVWYXDSd7gPwM5M3vR6MGP/3nOPwF8LOD/mO0/dzAIFuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBC6BNCQUTBMfvaOTWECXcW+HZYsm4hPpUn9SjFr0wNutjX1eNriI=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4c2lYakhSQWFVUEdyQS5jaGFpbjlhY2NvdW50X3B1Ymtleaf3C+g=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
  "id": -576460752303421332,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEBK8YhAsKkkkGGj5LBZ+PDhvzrhi94Z55o98eiJBA9hBcVWYXDSd7gPwM5M3vR6MGP/3nOPwF8LOD/mO0/dzAIFuED61fmVk93nRZga5U0um8IZD+t8IWDM2IcSgcll6HNnJTcj8bCnO6uXbJfopc242pbysFGXRJxJ1YpG0aiwWzEIuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBC6BNCQUTBMfvaOTWECXcW+HZYsm4hPpUn9SjFr0wNutjXwN65gw="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421332,
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
      "state": "tx_+NQLAfiEuEBK8YhAsKkkkGGj5LBZ+PDhvzrhi94Z55o98eiJBA9hBcVWYXDSd7gPwM5M3vR6MGP/3nOPwF8LOD/mO0/dzAIFuED61fmVk93nRZga5U0um8IZD+t8IWDM2IcSgcll6HNnJTcj8bCnO6uXbJfopc242pbysFGXRJxJ1YpG0aiwWzEIuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBC6BNCQUTBMfvaOTWECXcW+HZYsm4hPpUn9SjFr0wNutjXwN65gw="
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
      "state": "tx_+NQLAfiEuEBK8YhAsKkkkGGj5LBZ+PDhvzrhi94Z55o98eiJBA9hBcVWYXDSd7gPwM5M3vR6MGP/3nOPwF8LOD/mO0/dzAIFuED61fmVk93nRZga5U0um8IZD+t8IWDM2IcSgcll6HNnJTcj8bCnO6uXbJfopc242pbysFGXRJxJ1YpG0aiwWzEIuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBC6BNCQUTBMfvaOTWECXcW+HZYsm4hPpUn9SjFr0wNutjXwN65gw="
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
    "round": 267
  }
}
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
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
        "round": 267
      }
    }
  },
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
    "round": 267
  }
}
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
        "round": 267
      }
    }
  },
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
    "round": 267
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
      "caller_nonce": 267,
      "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
      "gas_price": 1,
      "gas_used": 122,
      "height": 267,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
    "round": 267
  }
}
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
        "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
        "round": 267
      }
    }
  },
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
    "round": 267
  }
}
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
        "round": 267
      }
    }
  },
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
    "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
    "round": 267
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
      "caller_nonce": 267,
      "contract_id": "ct_DnL3af43xU3JSMDpykmzw62qSEYf38McoXmS1WhjizwsT22iZ",
      "gas_price": 1,
      "gas_used": 122,
      "height": 267,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "ABCDEFG",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
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
      "caller_nonce": 268,
      "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
      "gas_price": 1,
      "gas_used": 276,
      "height": 268,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "ABCDEFG",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "ABCDEFG",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "ABCDEFG",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEMoPJFoaxkWje8zYC/hCFv+NrKmhM6E9ZXoC9zBSopN+GiBDhWew==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
  "id": -576460752303421331,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEDAbeaATtWlK/L3yFyOAgF6quim3ceEmulcx5RzSUr1DTMiFwuV2q18MOHgwF19PZ6789kf9R3n3OnEo5zcFJIOuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBDKDyRaGsZFo3vM2Av4Qhb/jaypoTOhPWV6AvcwUqKTfhovBcyEQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421331,
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
      "signed_tx": "tx_+JILAfhCuEDAbeaATtWlK/L3yFyOAgF6quim3ceEmulcx5RzSUr1DTMiFwuV2q18MOHgwF19PZ6789kf9R3n3OnEo5zcFJIOuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBDKDyRaGsZFo3vM2Av4Qhb/jaypoTOhPWV6AvcwUqKTfhovBcyEQ=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
  "id": -576460752303421330,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEDAbeaATtWlK/L3yFyOAgF6quim3ceEmulcx5RzSUr1DTMiFwuV2q18MOHgwF19PZ6789kf9R3n3OnEo5zcFJIOuEDDWqqeO3x2lF0Gfl64B9hMJsdKuRfE3iI3PWApvC7DO5aSB1LY90it2szkVCun4VnMg+b0Z5VechEvHkrY5/kNuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBDKDyRaGsZFo3vM2Av4Qhb/jaypoTOhPWV6AvcwUqKTfhoirtPJ4="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421330,
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
      "state": "tx_+NQLAfiEuEDAbeaATtWlK/L3yFyOAgF6quim3ceEmulcx5RzSUr1DTMiFwuV2q18MOHgwF19PZ6789kf9R3n3OnEo5zcFJIOuEDDWqqeO3x2lF0Gfl64B9hMJsdKuRfE3iI3PWApvC7DO5aSB1LY90it2szkVCun4VnMg+b0Z5VechEvHkrY5/kNuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBDKDyRaGsZFo3vM2Av4Qhb/jaypoTOhPWV6AvcwUqKTfhoirtPJ4="
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
      "state": "tx_+NQLAfiEuEDAbeaATtWlK/L3yFyOAgF6quim3ceEmulcx5RzSUr1DTMiFwuV2q18MOHgwF19PZ6789kf9R3n3OnEo5zcFJIOuEDDWqqeO3x2lF0Gfl64B9hMJsdKuRfE3iI3PWApvC7DO5aSB1LY90it2szkVCun4VnMg+b0Z5VechEvHkrY5/kNuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBDKDyRaGsZFo3vM2Av4Qhb/jaypoTOhPWV6AvcwUqKTfhoirtPJ4="
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
    "round": 268
  }
}
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
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
        "round": 268
      }
    }
  },
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
    "round": 268
  }
}
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
        "round": 268
      }
    }
  },
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
    "round": 268
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
      "caller_nonce": 268,
      "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
      "gas_price": 1,
      "gas_used": 276,
      "height": 268,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
    "round": 268
  }
}
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
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
        "round": 268
      }
    }
  },
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
    "round": 268
  }
}
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
        "round": 268
      }
    }
  },
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
    "round": 268
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
      "caller_nonce": 268,
      "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
      "gas_price": 1,
      "gas_used": 276,
      "height": 268,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "ABCDEFG",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
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
      "caller_nonce": 269,
      "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
      "gas_price": 1,
      "gas_used": 276,
      "height": 269,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "ABCDEFG",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "ABCDEFG",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "ABCDEFG",
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggENoNAj86PkmSeAj71Szsov+p5x6FEG6uIBC3qtaWwmhfpr4Lo7LQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
  "id": -576460752303421329,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEAFhdg3UOb3pDsfpWx2XHIy9wKjyu9pwScVLigaxD0ffbgx7l8W8/F6QvOViGl416njsM4lZ9H3aAwrGlLmSBIBuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBDaDQI/Oj5JkngI+9Us7KL/qecehRBuriAQt6rWlsJoX6awDcTvY="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421329,
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
      "signed_tx": "tx_+JILAfhCuEAFhdg3UOb3pDsfpWx2XHIy9wKjyu9pwScVLigaxD0ffbgx7l8W8/F6QvOViGl416njsM4lZ9H3aAwrGlLmSBIBuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBDaDQI/Oj5JkngI+9Us7KL/qecehRBuriAQt6rWlsJoX6awDcTvY=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoB0FopmQpd4lLCVaq6ZT23G1GRXcDImEnucoVecplUEaUThzaVhqSFJBYVVQR3JBLmNoYWluOWFjY291bnRfcHVia2V5G+Eazg==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
  "id": -576460752303421328,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEAFhdg3UOb3pDsfpWx2XHIy9wKjyu9pwScVLigaxD0ffbgx7l8W8/F6QvOViGl416njsM4lZ9H3aAwrGlLmSBIBuECePz/U/cPuk/fWAMhHz0EaHFSPBJwbhQ+LmwUZQC6nGHMbaN0nIM+uVZcBWAFDsxplSOz9YDRgNh3B68TybZoMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBDaDQI/Oj5JkngI+9Us7KL/qecehRBuriAQt6rWlsJoX6azT88bo="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421328,
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
      "state": "tx_+NQLAfiEuEAFhdg3UOb3pDsfpWx2XHIy9wKjyu9pwScVLigaxD0ffbgx7l8W8/F6QvOViGl416njsM4lZ9H3aAwrGlLmSBIBuECePz/U/cPuk/fWAMhHz0EaHFSPBJwbhQ+LmwUZQC6nGHMbaN0nIM+uVZcBWAFDsxplSOz9YDRgNh3B68TybZoMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBDaDQI/Oj5JkngI+9Us7KL/qecehRBuriAQt6rWlsJoX6azT88bo="
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
      "state": "tx_+NQLAfiEuEAFhdg3UOb3pDsfpWx2XHIy9wKjyu9pwScVLigaxD0ffbgx7l8W8/F6QvOViGl416njsM4lZ9H3aAwrGlLmSBIBuECePz/U/cPuk/fWAMhHz0EaHFSPBJwbhQ+LmwUZQC6nGHMbaN0nIM+uVZcBWAFDsxplSOz9YDRgNh3B68TybZoMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBDaDQI/Oj5JkngI+9Us7KL/qecehRBuriAQt6rWlsJoX6azT88bo="
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
    "round": 269
  }
}
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
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
        "round": 269
      }
    }
  },
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
    "round": 269
  }
}
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
        "round": 269
      }
    }
  },
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
    "round": 269
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
      "caller_nonce": 269,
      "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
      "gas_price": 1,
      "gas_used": 276,
      "height": 269,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
    "round": 269
  }
}
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
        "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
        "round": 269
      }
    }
  },
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
    "round": 269
  }
}
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
        "round": 269
      }
    }
  },
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
    "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
    "round": 269
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
      "caller_nonce": 269,
      "contract_id": "ct_RZrDQ4kWkaE5LUZiE1r8S8QCbKYEDvSnyDBZXXx7xiqZXnuA6",
      "gas_price": 1,
      "gas_used": 276,
      "height": 269,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
        "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
    "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
        "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
    "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
        "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
    "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEOoOlxANsjpGDjevvIFLetzcZyRWJML5hHWE60TKibFANfAV+tdw==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
  "id": -576460752303421327,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEDRYLcC+MaJkWGO1QFxUDm1qnvfKbL0Grxvljbagmwbdcxu1JNlquTCp3/SebO+Rya72oLa8ZfD+vp6dEz+uV0NuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBDqDpcQDbI6Rg43r7yBS3rc3GckViTC+YR1hOtEyomxQDX/QOg60="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421327,
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
      "signed_tx": "tx_+JILAfhCuEDRYLcC+MaJkWGO1QFxUDm1qnvfKbL0Grxvljbagmwbdcxu1JNlquTCp3/SebO+Rya72oLa8ZfD+vp6dEz+uV0NuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBDqDpcQDbI6Rg43r7yBS3rc3GckViTC+YR1hOtEyomxQDX/QOg60=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
  "id": -576460752303421326,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEAJBKhtMWeDKqbroPkxSWgskCwDR1x/tG/Lgebm2DlL1lJHWm5y0VJrj+K5ScPrJpOErDWES8QEjptcDzBfn14HuEDRYLcC+MaJkWGO1QFxUDm1qnvfKbL0Grxvljbagmwbdcxu1JNlquTCp3/SebO+Rya72oLa8ZfD+vp6dEz+uV0NuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBDqDpcQDbI6Rg43r7yBS3rc3GckViTC+YR1hOtEyomxQDX7h0x84="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421326,
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
      "state": "tx_+NQLAfiEuEAJBKhtMWeDKqbroPkxSWgskCwDR1x/tG/Lgebm2DlL1lJHWm5y0VJrj+K5ScPrJpOErDWES8QEjptcDzBfn14HuEDRYLcC+MaJkWGO1QFxUDm1qnvfKbL0Grxvljbagmwbdcxu1JNlquTCp3/SebO+Rya72oLa8ZfD+vp6dEz+uV0NuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBDqDpcQDbI6Rg43r7yBS3rc3GckViTC+YR1hOtEyomxQDX7h0x84="
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
      "state": "tx_+NQLAfiEuEAJBKhtMWeDKqbroPkxSWgskCwDR1x/tG/Lgebm2DlL1lJHWm5y0VJrj+K5ScPrJpOErDWES8QEjptcDzBfn14HuEDRYLcC+MaJkWGO1QFxUDm1qnvfKbL0Grxvljbagmwbdcxu1JNlquTCp3/SebO+Rya72oLa8ZfD+vp6dEz+uV0NuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBDqDpcQDbI6Rg43r7yBS3rc3GckViTC+YR1hOtEyomxQDX7h0x84="
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
    "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
        "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
    "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
        "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
    "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
        "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
    "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEPoDLAS5wyZg/bNfB+bgA5Hso5CqeqQNa3zxhL29vk0tvST8+M6Q==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
  "id": -576460752303421325,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEDPLotOvqrZLDgQ2+Pj87LKp/yvl4Qm60YtFDnrui8u2w2H4jGlmYGGjt3VgOU2hT1iieyYOSKhnkd3NUVSJvQDuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBD6AywEucMmYP2zXwfm4AOR7KOQqnqkDWt88YS9vb5NLb0ksta7M="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421325,
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
      "signed_tx": "tx_+JILAfhCuEDPLotOvqrZLDgQ2+Pj87LKp/yvl4Qm60YtFDnrui8u2w2H4jGlmYGGjt3VgOU2hT1iieyYOSKhnkd3NUVSJvQDuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBD6AywEucMmYP2zXwfm4AOR7KOQqnqkDWt88YS9vb5NLb0ksta7M=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
  "id": -576460752303421324,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEBpv0YIBWyaLTSwGf+PswTM9MojS4MbdY1gw9x/u0IReeRj+VaieVVSdEaqJ5RAk2twLFBeW7WJz8GCSwzQal8CuEDPLotOvqrZLDgQ2+Pj87LKp/yvl4Qm60YtFDnrui8u2w2H4jGlmYGGjt3VgOU2hT1iieyYOSKhnkd3NUVSJvQDuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBD6AywEucMmYP2zXwfm4AOR7KOQqnqkDWt88YS9vb5NLb0j8p9sg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421324,
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
      "state": "tx_+NQLAfiEuEBpv0YIBWyaLTSwGf+PswTM9MojS4MbdY1gw9x/u0IReeRj+VaieVVSdEaqJ5RAk2twLFBeW7WJz8GCSwzQal8CuEDPLotOvqrZLDgQ2+Pj87LKp/yvl4Qm60YtFDnrui8u2w2H4jGlmYGGjt3VgOU2hT1iieyYOSKhnkd3NUVSJvQDuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBD6AywEucMmYP2zXwfm4AOR7KOQqnqkDWt88YS9vb5NLb0j8p9sg="
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
      "state": "tx_+NQLAfiEuEBpv0YIBWyaLTSwGf+PswTM9MojS4MbdY1gw9x/u0IReeRj+VaieVVSdEaqJ5RAk2twLFBeW7WJz8GCSwzQal8CuEDPLotOvqrZLDgQ2+Pj87LKp/yvl4Qm60YtFDnrui8u2w2H4jGlmYGGjt3VgOU2hT1iieyYOSKhnkd3NUVSJvQDuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBD6AywEucMmYP2zXwfm4AOR7KOQqnqkDWt88YS9vb5NLb0j8p9sg="
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
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
      "caller_nonce": 272,
      "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
      "gas_price": 1,
      "gas_used": 122,
      "height": 272,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEQoPdZVaB3ZNJOUId/bUuNCEknvujSLaufINI7qlk4QN0iZ4cX0A==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
  "id": -576460752303421323,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEAdzUYf9PhaKqma/ztUYS0q2kR8lHps6oVdxZDHwweN5FhzzRMsgvSoGCQK1FafG7pu/izUEiQ4yqWrxm41uQUEuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBEKD3WVWgd2TSTlCHf21LjQhJJ77o0i2rnyDSO6pZOEDdIvvyr9Y="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421323,
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
      "signed_tx": "tx_+JILAfhCuEAdzUYf9PhaKqma/ztUYS0q2kR8lHps6oVdxZDHwweN5FhzzRMsgvSoGCQK1FafG7pu/izUEiQ4yqWrxm41uQUEuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBEKD3WVWgd2TSTlCHf21LjQhJJ77o0i2rnyDSO6pZOEDdIvvyr9Y=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
  "id": -576460752303421322,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEAdzUYf9PhaKqma/ztUYS0q2kR8lHps6oVdxZDHwweN5FhzzRMsgvSoGCQK1FafG7pu/izUEiQ4yqWrxm41uQUEuEBzLhQDdIsit07PYgTFpNUZ9/Vu+r6hp2dI2bbjqDe2QHGaLAuFD+SQSgu7OlXBucUKaCUICw+OauinN8uYQRcNuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBEKD3WVWgd2TSTlCHf21LjQhJJ77o0i2rnyDSO6pZOEDdIlIjOFM="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421322,
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
      "state": "tx_+NQLAfiEuEAdzUYf9PhaKqma/ztUYS0q2kR8lHps6oVdxZDHwweN5FhzzRMsgvSoGCQK1FafG7pu/izUEiQ4yqWrxm41uQUEuEBzLhQDdIsit07PYgTFpNUZ9/Vu+r6hp2dI2bbjqDe2QHGaLAuFD+SQSgu7OlXBucUKaCUICw+OauinN8uYQRcNuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBEKD3WVWgd2TSTlCHf21LjQhJJ77o0i2rnyDSO6pZOEDdIlIjOFM="
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
      "state": "tx_+NQLAfiEuEAdzUYf9PhaKqma/ztUYS0q2kR8lHps6oVdxZDHwweN5FhzzRMsgvSoGCQK1FafG7pu/izUEiQ4yqWrxm41uQUEuEBzLhQDdIsit07PYgTFpNUZ9/Vu+r6hp2dI2bbjqDe2QHGaLAuFD+SQSgu7OlXBucUKaCUICw+OauinN8uYQRcNuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBEKD3WVWgd2TSTlCHf21LjQhJJ77o0i2rnyDSO6pZOEDdIlIjOFM="
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
    "round": 272
  }
}
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
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
        "round": 272
      }
    }
  },
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
    "round": 272
  }
}
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
        "round": 272
      }
    }
  },
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
    "round": 272
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
      "caller_nonce": 272,
      "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
      "gas_price": 1,
      "gas_used": 122,
      "height": 272,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
    "round": 272
  }
}
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
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
        "round": 272
      }
    }
  },
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
    "round": 272
  }
}
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
        "round": 272
      }
    }
  },
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
    "round": 272
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
      "caller_nonce": 272,
      "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
      "gas_price": 1,
      "gas_used": 122,
      "height": 272,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
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
      "caller_nonce": 273,
      "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
      "gas_price": 1,
      "gas_used": 122,
      "height": 273,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggERoLDxOKnT7nn4doXbk7yK2CrjGdWcquHn1kbs2XftB7UslFPrGA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
  "id": -576460752303421321,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuECBfawQQrRzo3SxIusdw4WApBFQI8Tn+QDKEcjXdaQeV1oq+xv96qDlN9fpIumOGHAdfUfb/rZbx3w9ZuxecGsGuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBEaCw8Tip0+55+HaF25O8itgq4xnVnKrh59ZG7Nl37Qe1LHxAoQw="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421321,
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
      "signed_tx": "tx_+JILAfhCuECBfawQQrRzo3SxIusdw4WApBFQI8Tn+QDKEcjXdaQeV1oq+xv96qDlN9fpIumOGHAdfUfb/rZbx3w9ZuxecGsGuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBEaCw8Tip0+55+HaF25O8itgq4xnVnKrh59ZG7Nl37Qe1LHxAoQw=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
  "id": -576460752303421320,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEBmq20CfKoehSHnVlG8WXZZ6dvQWpvgnEZ7+oZwJq6+jXyBkHFkVuXRe/kRxa8y11BzY3Hg3dqe5m7RUKWy0hcBuECBfawQQrRzo3SxIusdw4WApBFQI8Tn+QDKEcjXdaQeV1oq+xv96qDlN9fpIumOGHAdfUfb/rZbx3w9ZuxecGsGuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBEaCw8Tip0+55+HaF25O8itgq4xnVnKrh59ZG7Nl37Qe1LCVimfg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421320,
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
      "state": "tx_+NQLAfiEuEBmq20CfKoehSHnVlG8WXZZ6dvQWpvgnEZ7+oZwJq6+jXyBkHFkVuXRe/kRxa8y11BzY3Hg3dqe5m7RUKWy0hcBuECBfawQQrRzo3SxIusdw4WApBFQI8Tn+QDKEcjXdaQeV1oq+xv96qDlN9fpIumOGHAdfUfb/rZbx3w9ZuxecGsGuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBEaCw8Tip0+55+HaF25O8itgq4xnVnKrh59ZG7Nl37Qe1LCVimfg="
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
      "state": "tx_+NQLAfiEuEBmq20CfKoehSHnVlG8WXZZ6dvQWpvgnEZ7+oZwJq6+jXyBkHFkVuXRe/kRxa8y11BzY3Hg3dqe5m7RUKWy0hcBuECBfawQQrRzo3SxIusdw4WApBFQI8Tn+QDKEcjXdaQeV1oq+xv96qDlN9fpIumOGHAdfUfb/rZbx3w9ZuxecGsGuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBEaCw8Tip0+55+HaF25O8itgq4xnVnKrh59ZG7Nl37Qe1LCVimfg="
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
    "round": 273
  }
}
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
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
        "round": 273
      }
    }
  },
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
    "round": 273
  }
}
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
        "round": 273
      }
    }
  },
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
    "round": 273
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
      "caller_nonce": 273,
      "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
      "gas_price": 1,
      "gas_used": 122,
      "height": 273,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
    "round": 273
  }
}
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
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
        "round": 273
      }
    }
  },
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
    "round": 273
  }
}
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
        "round": 273
      }
    }
  },
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
    "round": 273
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
      "caller_nonce": 273,
      "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
      "gas_price": 1,
      "gas_used": 122,
      "height": 273,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "ABCDEFG",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
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
      "caller_nonce": 274,
      "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
      "gas_price": 1,
      "gas_used": 276,
      "height": 274,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "ABCDEFG",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "ABCDEFG",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "ABCDEFG",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggESoCjt7tPSkmW1qsGCjH4zRQau/CgNX0q8mr8W3RZprwlJkmLGow==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
  "id": -576460752303421319,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEDs3jfA15xY8FlILJOAhXtdIOQAU38ayc2u5OO5UDfsgPvLagnN7cKyfKrcHkD4i+fA3FJO5l939hFS9YIsrt0CuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBEqAo7e7T0pJltarBgox+M0UGrvwoDV9KvJq/Ft0Waa8JSQIk8OA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421319,
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
      "signed_tx": "tx_+JILAfhCuEDs3jfA15xY8FlILJOAhXtdIOQAU38ayc2u5OO5UDfsgPvLagnN7cKyfKrcHkD4i+fA3FJO5l939hFS9YIsrt0CuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBEqAo7e7T0pJltarBgox+M0UGrvwoDV9KvJq/Ft0Waa8JSQIk8OA=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
  "id": -576460752303421318,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEAlpHfx+mqJjWDt706eZ5N6N39NGS/THrSHSwMvTWwUT6SgOCqSuobhc+hi+PTdLaCld3taAiHRBS0NI1+2RAgFuEDs3jfA15xY8FlILJOAhXtdIOQAU38ayc2u5OO5UDfsgPvLagnN7cKyfKrcHkD4i+fA3FJO5l939hFS9YIsrt0CuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBEqAo7e7T0pJltarBgox+M0UGrvwoDV9KvJq/Ft0Waa8JSVXMKd4="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421318,
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
      "state": "tx_+NQLAfiEuEAlpHfx+mqJjWDt706eZ5N6N39NGS/THrSHSwMvTWwUT6SgOCqSuobhc+hi+PTdLaCld3taAiHRBS0NI1+2RAgFuEDs3jfA15xY8FlILJOAhXtdIOQAU38ayc2u5OO5UDfsgPvLagnN7cKyfKrcHkD4i+fA3FJO5l939hFS9YIsrt0CuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBEqAo7e7T0pJltarBgox+M0UGrvwoDV9KvJq/Ft0Waa8JSVXMKd4="
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
      "state": "tx_+NQLAfiEuEAlpHfx+mqJjWDt706eZ5N6N39NGS/THrSHSwMvTWwUT6SgOCqSuobhc+hi+PTdLaCld3taAiHRBS0NI1+2RAgFuEDs3jfA15xY8FlILJOAhXtdIOQAU38ayc2u5OO5UDfsgPvLagnN7cKyfKrcHkD4i+fA3FJO5l939hFS9YIsrt0CuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBEqAo7e7T0pJltarBgox+M0UGrvwoDV9KvJq/Ft0Waa8JSVXMKd4="
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
    "round": 274
  }
}
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
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
        "round": 274
      }
    }
  },
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
    "round": 274
  }
}
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
        "round": 274
      }
    }
  },
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
    "round": 274
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
      "caller_nonce": 274,
      "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
      "gas_price": 1,
      "gas_used": 276,
      "height": 274,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
    "round": 274
  }
}
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
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
        "round": 274
      }
    }
  },
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
    "round": 274
  }
}
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
        "round": 274
      }
    }
  },
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
    "round": 274
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
      "caller_nonce": 274,
      "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
      "gas_price": 1,
      "gas_used": 276,
      "height": 274,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "ABCDEFG",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
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
      "caller_nonce": 275,
      "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
      "gas_price": 1,
      "gas_used": 276,
      "height": 275,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "ABCDEFG",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "ABCDEFG",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
  }
}
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "ABCDEFG",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
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
        "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
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
    "block_hash": "kh_RKqsGbU6ogPQzQsCqxZakLAMQonJ1aFf8hFb6ZqJ4n4bfpQuN",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEToGYn/HZbGPptJqBJbv1AoaEIG1j5kyluAvkfTVZtVTxkUwP3tw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
  "id": -576460752303421317,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEDUZ89eqibM8jiOQNGXcAGrudaDn5/9ki5NT5QGSWARQweTX7uHTkIzJjWvbvqfY90zB3Hys0xrJ9GaAYIy830MuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBE6BmJ/x2Wxj6bSagSW79QKGhCBtY+ZMpbgL5H01WbVU8ZGstUnQ="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421317,
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
      "signed_tx": "tx_+JILAfhCuEDUZ89eqibM8jiOQNGXcAGrudaDn5/9ki5NT5QGSWARQweTX7uHTkIzJjWvbvqfY90zB3Hys0xrJ9GaAYIy830MuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBE6BmJ/x2Wxj6bSagSW79QKGhCBtY+ZMpbgL5H01WbVU8ZGstUnQ=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
  "id": -576460752303421316,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEBhttGIgBmuZj0tJ+arM8QvqVHqYgxBToLWPFsK2AUYZ8wiIBan/wyPFNXH5ulgqKv8Pf9Y9QwQjzVCCSdbmdsPuEDUZ89eqibM8jiOQNGXcAGrudaDn5/9ki5NT5QGSWARQweTX7uHTkIzJjWvbvqfY90zB3Hys0xrJ9GaAYIy830MuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBE6BmJ/x2Wxj6bSagSW79QKGhCBtY+ZMpbgL5H01WbVU8ZAJhMHc="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421316,
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
      "state": "tx_+NQLAfiEuEBhttGIgBmuZj0tJ+arM8QvqVHqYgxBToLWPFsK2AUYZ8wiIBan/wyPFNXH5ulgqKv8Pf9Y9QwQjzVCCSdbmdsPuEDUZ89eqibM8jiOQNGXcAGrudaDn5/9ki5NT5QGSWARQweTX7uHTkIzJjWvbvqfY90zB3Hys0xrJ9GaAYIy830MuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBE6BmJ/x2Wxj6bSagSW79QKGhCBtY+ZMpbgL5H01WbVU8ZAJhMHc="
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
      "state": "tx_+NQLAfiEuEBhttGIgBmuZj0tJ+arM8QvqVHqYgxBToLWPFsK2AUYZ8wiIBan/wyPFNXH5ulgqKv8Pf9Y9QwQjzVCCSdbmdsPuEDUZ89eqibM8jiOQNGXcAGrudaDn5/9ki5NT5QGSWARQweTX7uHTkIzJjWvbvqfY90zB3Hys0xrJ9GaAYIy830MuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBE6BmJ/x2Wxj6bSagSW79QKGhCBtY+ZMpbgL5H01WbVU8ZAJhMHc="
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
    "round": 275
  }
}
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
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
        "round": 275
      }
    }
  },
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
    "round": 275
  }
}
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
        "round": 275
      }
    }
  },
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
    "round": 275
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
      "caller_nonce": 275,
      "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
      "gas_price": 1,
      "gas_used": 276,
      "height": 275,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
    "round": 275
  }
}
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
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
        "round": 275
      }
    }
  },
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
    "round": 275
  }
}
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
        "round": 275
      }
    }
  },
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
    "round": 275
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
      "caller_nonce": 275,
      "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
      "gas_price": 1,
      "gas_used": 276,
      "height": 275,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
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
      "caller_nonce": 276,
      "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
      "gas_price": 1,
      "gas_used": 122,
      "height": 276,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEUoDBcnAWmfn7Xisn3WhkwxATQMYUmj4uZsM0CM/4ZXFec+JAS9Q==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
  "id": -576460752303421315,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEB0yTa05iruFn4fzcXBYCya3mBcsmEzDkSjtnAWMdys7gqIIiJeSmczQSYBITyDhlXqlX+cUa3V+OAf7v+6uWMIuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBFKAwXJwFpn5+14rJ91oZMMQE0DGFJo+LmbDNAjP+GVxXnCW/Dwg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421315,
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
      "signed_tx": "tx_+JILAfhCuEB0yTa05iruFn4fzcXBYCya3mBcsmEzDkSjtnAWMdys7gqIIiJeSmczQSYBITyDhlXqlX+cUa3V+OAf7v+6uWMIuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBFKAwXJwFpn5+14rJ91oZMMQE0DGFJo+LmbDNAjP+GVxXnCW/Dwg=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
  "id": -576460752303421314,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEB0yTa05iruFn4fzcXBYCya3mBcsmEzDkSjtnAWMdys7gqIIiJeSmczQSYBITyDhlXqlX+cUa3V+OAf7v+6uWMIuEB3MWOk/OQ8yPtoWLC+faLELbkWNlLeoer0q4kERkGDRNYt01+zXZF/iYz6Yy8fElAG6VER2DnklPF08ckkwhgJuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBFKAwXJwFpn5+14rJ91oZMMQE0DGFJo+LmbDNAjP+GVxXnF3ZAZ0="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421314,
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
      "state": "tx_+NQLAfiEuEB0yTa05iruFn4fzcXBYCya3mBcsmEzDkSjtnAWMdys7gqIIiJeSmczQSYBITyDhlXqlX+cUa3V+OAf7v+6uWMIuEB3MWOk/OQ8yPtoWLC+faLELbkWNlLeoer0q4kERkGDRNYt01+zXZF/iYz6Yy8fElAG6VER2DnklPF08ckkwhgJuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBFKAwXJwFpn5+14rJ91oZMMQE0DGFJo+LmbDNAjP+GVxXnF3ZAZ0="
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
      "state": "tx_+NQLAfiEuEB0yTa05iruFn4fzcXBYCya3mBcsmEzDkSjtnAWMdys7gqIIiJeSmczQSYBITyDhlXqlX+cUa3V+OAf7v+6uWMIuEB3MWOk/OQ8yPtoWLC+faLELbkWNlLeoer0q4kERkGDRNYt01+zXZF/iYz6Yy8fElAG6VER2DnklPF08ckkwhgJuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBFKAwXJwFpn5+14rJ91oZMMQE0DGFJo+LmbDNAjP+GVxXnF3ZAZ0="
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
    "round": 276
  }
}
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
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
        "round": 276
      }
    }
  },
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
    "round": 276
  }
}
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
        "round": 276
      }
    }
  },
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
    "round": 276
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
      "caller_nonce": 276,
      "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
      "gas_price": 1,
      "gas_used": 122,
      "height": 276,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
    "round": 276
  }
}
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
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
        "round": 276
      }
    }
  },
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
    "round": 276
  }
}
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
        "round": 276
      }
    }
  },
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
    "round": 276
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
      "caller_nonce": 276,
      "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
      "gas_price": 1,
      "gas_used": 122,
      "height": 276,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
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
      "caller_nonce": 277,
      "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
      "gas_price": 1,
      "gas_used": 122,
      "height": 277,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEVoHazrqEeC7nMRWqzKgFQWO0FnHjCWJG0QKqRcwRbvTqMvm+Cww==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
  "id": -576460752303421313,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuECtKv+G8cWtIiC1ZVvnX4sNtRzTH81NymomeiSYZvX15NxjzaG4TK05I+X7f4CKRO0Gl68xOgd0rRu/s3WWJuENuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBFaB2s66hHgu5zEVqsyoBUFjtBZx4wliRtECqkXMEW706jEAHzTQ="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421313,
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
      "signed_tx": "tx_+JILAfhCuECtKv+G8cWtIiC1ZVvnX4sNtRzTH81NymomeiSYZvX15NxjzaG4TK05I+X7f4CKRO0Gl68xOgd0rRu/s3WWJuENuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBFaB2s66hHgu5zEVqsyoBUFjtBZx4wliRtECqkXMEW706jEAHzTQ=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E3eEVGdG1CV3R3dFB4WC5jaGFpbjlhY2NvdW50X3B1YmtleVLyc+s=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
  "id": -576460752303421312,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuECf6n2cqTm0EQFs276VGiqyop0HuGgXRW01O9qpV8xkfa3Y0rKJMDboubZ24Wil22Z1eRX7OzbclTySFyL+axUGuECtKv+G8cWtIiC1ZVvnX4sNtRzTH81NymomeiSYZvX15NxjzaG4TK05I+X7f4CKRO0Gl68xOgd0rRu/s3WWJuENuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBFaB2s66hHgu5zEVqsyoBUFjtBZx4wliRtECqkXMEW706jGGmzDo="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421312,
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
      "state": "tx_+NQLAfiEuECf6n2cqTm0EQFs276VGiqyop0HuGgXRW01O9qpV8xkfa3Y0rKJMDboubZ24Wil22Z1eRX7OzbclTySFyL+axUGuECtKv+G8cWtIiC1ZVvnX4sNtRzTH81NymomeiSYZvX15NxjzaG4TK05I+X7f4CKRO0Gl68xOgd0rRu/s3WWJuENuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBFaB2s66hHgu5zEVqsyoBUFjtBZx4wliRtECqkXMEW706jGGmzDo="
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
      "state": "tx_+NQLAfiEuECf6n2cqTm0EQFs276VGiqyop0HuGgXRW01O9qpV8xkfa3Y0rKJMDboubZ24Wil22Z1eRX7OzbclTySFyL+axUGuECtKv+G8cWtIiC1ZVvnX4sNtRzTH81NymomeiSYZvX15NxjzaG4TK05I+X7f4CKRO0Gl68xOgd0rRu/s3WWJuENuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBFaB2s66hHgu5zEVqsyoBUFjtBZx4wliRtECqkXMEW706jGGmzDo="
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
    "round": 277
  }
}
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
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
        "round": 277
      }
    }
  },
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
    "round": 277
  }
}
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
        "round": 277
      }
    }
  },
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
    "round": 277
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
      "caller_nonce": 277,
      "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
      "gas_price": 1,
      "gas_used": 122,
      "height": 277,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
    "round": 277
  }
}
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
        "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
        "round": 277
      }
    }
  },
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
    "round": 277
  }
}
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
        "round": 277
      }
    }
  },
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
    "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
    "round": 277
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
      "caller_nonce": 277,
      "contract_id": "ct_4Bq2m7W82pXkoSpRbRyqr92xgeKqxJqnpCqLdMbVKLrNGpxdy",
      "gas_price": 1,
      "gas_used": 122,
      "height": 277,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
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
      "caller_nonce": 278,
      "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
      "gas_price": 1,
      "gas_used": 276,
      "height": 278,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEWoF+smdp489u3gy7ldNxADeEf6H77Og9qwlmgw7mnCHRRAIaZcg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
  "id": -576460752303421311,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuECJHX/TNjwwd4q20W4tQsuldOlZiTLZ2xbrYJ3xrBqTh2Zdc8AAD4ECBoX1B2CDuHeV0JLHWDJpSIfxY0AZm5cIuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBFqBfrJnaePPbt4Mu5XTcQA3hH+h++zoPasJZoMO5pwh0UXn2A08="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421311,
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
      "signed_tx": "tx_+JILAfhCuECJHX/TNjwwd4q20W4tQsuldOlZiTLZ2xbrYJ3xrBqTh2Zdc8AAD4ECBoX1B2CDuHeV0JLHWDJpSIfxY0AZm5cIuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBFqBfrJnaePPbt4Mu5XTcQA3hH+h++zoPasJZoMO5pwh0UXn2A08=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
  "id": -576460752303421310,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEB3n8Ab1X/158DFshl4bR9m0sRpjyCc8wEtdm8FH6Zaer/lSSJHnIGs63MwV+7i0/S6FaOa/wzUkrAuKqHQNYMKuECJHX/TNjwwd4q20W4tQsuldOlZiTLZ2xbrYJ3xrBqTh2Zdc8AAD4ECBoX1B2CDuHeV0JLHWDJpSIfxY0AZm5cIuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBFqBfrJnaePPbt4Mu5XTcQA3hH+h++zoPasJZoMO5pwh0UTcX7O0="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421310,
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
      "state": "tx_+NQLAfiEuEB3n8Ab1X/158DFshl4bR9m0sRpjyCc8wEtdm8FH6Zaer/lSSJHnIGs63MwV+7i0/S6FaOa/wzUkrAuKqHQNYMKuECJHX/TNjwwd4q20W4tQsuldOlZiTLZ2xbrYJ3xrBqTh2Zdc8AAD4ECBoX1B2CDuHeV0JLHWDJpSIfxY0AZm5cIuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBFqBfrJnaePPbt4Mu5XTcQA3hH+h++zoPasJZoMO5pwh0UTcX7O0="
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
      "state": "tx_+NQLAfiEuEB3n8Ab1X/158DFshl4bR9m0sRpjyCc8wEtdm8FH6Zaer/lSSJHnIGs63MwV+7i0/S6FaOa/wzUkrAuKqHQNYMKuECJHX/TNjwwd4q20W4tQsuldOlZiTLZ2xbrYJ3xrBqTh2Zdc8AAD4ECBoX1B2CDuHeV0JLHWDJpSIfxY0AZm5cIuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBFqBfrJnaePPbt4Mu5XTcQA3hH+h++zoPasJZoMO5pwh0UTcX7O0="
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
    "round": 278
  }
}
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
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
        "round": 278
      }
    }
  },
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
    "round": 278
  }
}
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
        "round": 278
      }
    }
  },
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
    "round": 278
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
      "caller_nonce": 278,
      "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
      "gas_price": 1,
      "gas_used": 276,
      "height": 278,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
    "round": 278
  }
}
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
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
        "round": 278
      }
    }
  },
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
    "round": 278
  }
}
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
        "round": 278
      }
    }
  },
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
    "round": 278
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
      "caller_nonce": 278,
      "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
      "gas_price": 1,
      "gas_used": 276,
      "height": 278,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
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
      "caller_nonce": 279,
      "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
      "gas_price": 1,
      "gas_used": 276,
      "height": 279,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEXoDz7d9ZAA3uf3quNhssK2IDY0k4xhw3e53EPfxtgcANrotq/2Q==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
  "id": -576460752303421309,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuECEUdZ+o2tlM8gC2jDnXg78vkDu7uTveqEeSMIFgmmZgKLruHUSn1FmH/RJ4pAremIWnjaVKp1mJvcumLaGgGgCuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBF6A8+3fWQAN7n96rjYbLCtiA2NJOMYcN3udxD38bYHADa1N/Poo="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421309,
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
      "signed_tx": "tx_+JILAfhCuECEUdZ+o2tlM8gC2jDnXg78vkDu7uTveqEeSMIFgmmZgKLruHUSn1FmH/RJ4pAremIWnjaVKp1mJvcumLaGgGgCuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBF6A8+3fWQAN7n96rjYbLCtiA2NJOMYcN3udxD38bYHADa1N/Poo=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoAc8W55bHgi6PW7qelYbzi/NsCoIDWLjXfF133nF8/mXUTd4RUZ0bUJXdHd0UHhYLmNoYWluOWFjY291bnRfcHVia2V5K4MlgA==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
  "id": -576460752303421308,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuECEUdZ+o2tlM8gC2jDnXg78vkDu7uTveqEeSMIFgmmZgKLruHUSn1FmH/RJ4pAremIWnjaVKp1mJvcumLaGgGgCuEDx1853MShnLhxgLpoAWJ8vTf4ZjUQtctnUtf75SJDsXHzES0Me/nwQTluTWcd1T8bNp3fxrXPepifgOT5F4/EAuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBF6A8+3fWQAN7n96rjYbLCtiA2NJOMYcN3udxD38bYHADa8hRgMY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421308,
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
      "state": "tx_+NQLAfiEuECEUdZ+o2tlM8gC2jDnXg78vkDu7uTveqEeSMIFgmmZgKLruHUSn1FmH/RJ4pAremIWnjaVKp1mJvcumLaGgGgCuEDx1853MShnLhxgLpoAWJ8vTf4ZjUQtctnUtf75SJDsXHzES0Me/nwQTluTWcd1T8bNp3fxrXPepifgOT5F4/EAuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBF6A8+3fWQAN7n96rjYbLCtiA2NJOMYcN3udxD38bYHADa8hRgMY="
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
      "state": "tx_+NQLAfiEuECEUdZ+o2tlM8gC2jDnXg78vkDu7uTveqEeSMIFgmmZgKLruHUSn1FmH/RJ4pAremIWnjaVKp1mJvcumLaGgGgCuEDx1853MShnLhxgLpoAWJ8vTf4ZjUQtctnUtf75SJDsXHzES0Me/nwQTluTWcd1T8bNp3fxrXPepifgOT5F4/EAuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBF6A8+3fWQAN7n96rjYbLCtiA2NJOMYcN3udxD38bYHADa8hRgMY="
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
    "round": 279
  }
}
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
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
        "round": 279
      }
    }
  },
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
    "round": 279
  }
}
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
        "round": 279
      }
    }
  },
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
    "round": 279
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
      "caller_nonce": 279,
      "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
      "gas_price": 1,
      "gas_used": 276,
      "height": 279,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
    "round": 279
  }
}
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
        "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
        "round": 279
      }
    }
  },
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
    "round": 279
  }
}
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
        "round": 279
      }
    }
  },
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
    "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
    "round": 279
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
      "caller_nonce": 279,
      "contract_id": "ct_JpgRrZF9uBNSUD7WTfVGoBEuEY3BYizMkUzwKCo2BiZq7iuAg",
      "gas_price": 1,
      "gas_used": 276,
      "height": 279,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
        "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
    "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
        "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
    "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
        "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
    "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEYoACpPDKeFoGTErLFfVR5lN7+Z2pcop6aibQxAl69jH8EwpApCw==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
  "id": -576460752303421307,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEBu8u6oM9CtTdc0J0VLx3wrmW4s4rFQQfohp1/M3f1F0L7UClH3iEEycPE+vF9/BqsgEXIRHWKEqhkwJ7a/vtEAuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBGKAAqTwynhaBkxKyxX1UeZTe/mdqXKKemom0MQJevYx/BAqiGtY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421307,
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
      "signed_tx": "tx_+JILAfhCuEBu8u6oM9CtTdc0J0VLx3wrmW4s4rFQQfohp1/M3f1F0L7UClH3iEEycPE+vF9/BqsgEXIRHWKEqhkwJ7a/vtEAuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBGKAAqTwynhaBkxKyxX1UeZTe/mdqXKKemom0MQJevYx/BAqiGtY=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
  "id": -576460752303421306,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEBO4fjaD1QuHYgw9Vfofk/hWbASSOHeuxq6ZDfUJhCnRJvzdn5Q9+VZ0aTASCPVoMPRJjmQ1EqPl09uZmjF0DECuEBu8u6oM9CtTdc0J0VLx3wrmW4s4rFQQfohp1/M3f1F0L7UClH3iEEycPE+vF9/BqsgEXIRHWKEqhkwJ7a/vtEAuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBGKAAqTwynhaBkxKyxX1UeZTe/mdqXKKemom0MQJevYx/BJxRDwg="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421306,
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
      "state": "tx_+NQLAfiEuEBO4fjaD1QuHYgw9Vfofk/hWbASSOHeuxq6ZDfUJhCnRJvzdn5Q9+VZ0aTASCPVoMPRJjmQ1EqPl09uZmjF0DECuEBu8u6oM9CtTdc0J0VLx3wrmW4s4rFQQfohp1/M3f1F0L7UClH3iEEycPE+vF9/BqsgEXIRHWKEqhkwJ7a/vtEAuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBGKAAqTwynhaBkxKyxX1UeZTe/mdqXKKemom0MQJevYx/BJxRDwg="
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
      "state": "tx_+NQLAfiEuEBO4fjaD1QuHYgw9Vfofk/hWbASSOHeuxq6ZDfUJhCnRJvzdn5Q9+VZ0aTASCPVoMPRJjmQ1EqPl09uZmjF0DECuEBu8u6oM9CtTdc0J0VLx3wrmW4s4rFQQfohp1/M3f1F0L7UClH3iEEycPE+vF9/BqsgEXIRHWKEqhkwJ7a/vtEAuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBGKAAqTwynhaBkxKyxX1UeZTe/mdqXKKemom0MQJevYx/BJxRDwg="
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
    "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
        "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
    "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
        "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
    "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
        "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
    "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEZoKypX9FOPIx6fYBypyhsA0CeOHMnRCfGIB0XTikaSwTVrWvDAA==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
  "id": -576460752303421305,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEDlmc0PII2/yi1h7Gm96vgmwZof39SeowNzsmXyUzprq1hjZoGQtOtZjNB0NNOMYN/YoF0m7vkoMwKyefvk5h4HuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBGaCsqV/RTjyMen2AcqcobANAnjhzJ0QnxiAdF04pGksE1UOg2Ls="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421305,
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
      "signed_tx": "tx_+JILAfhCuEDlmc0PII2/yi1h7Gm96vgmwZof39SeowNzsmXyUzprq1hjZoGQtOtZjNB0NNOMYN/YoF0m7vkoMwKyefvk5h4HuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBGaCsqV/RTjyMen2AcqcobANAnjhzJ0QnxiAdF04pGksE1UOg2Ls=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
  "id": -576460752303421304,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEC+vannu80ECQ0FNW8UpZttvKz/nQB4/XGMovAM6RKl6GeDsB8NXj7rp1fXVn/plyW1fbly3WaPDkEVwp0e5Z0NuEDlmc0PII2/yi1h7Gm96vgmwZof39SeowNzsmXyUzprq1hjZoGQtOtZjNB0NNOMYN/YoF0m7vkoMwKyefvk5h4HuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBGaCsqV/RTjyMen2AcqcobANAnjhzJ0QnxiAdF04pGksE1QRWODs="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421304,
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
      "state": "tx_+NQLAfiEuEC+vannu80ECQ0FNW8UpZttvKz/nQB4/XGMovAM6RKl6GeDsB8NXj7rp1fXVn/plyW1fbly3WaPDkEVwp0e5Z0NuEDlmc0PII2/yi1h7Gm96vgmwZof39SeowNzsmXyUzprq1hjZoGQtOtZjNB0NNOMYN/YoF0m7vkoMwKyefvk5h4HuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBGaCsqV/RTjyMen2AcqcobANAnjhzJ0QnxiAdF04pGksE1QRWODs="
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
      "state": "tx_+NQLAfiEuEC+vannu80ECQ0FNW8UpZttvKz/nQB4/XGMovAM6RKl6GeDsB8NXj7rp1fXVn/plyW1fbly3WaPDkEVwp0e5Z0NuEDlmc0PII2/yi1h7Gm96vgmwZof39SeowNzsmXyUzprq1hjZoGQtOtZjNB0NNOMYN/YoF0m7vkoMwKyefvk5h4HuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBGaCsqV/RTjyMen2AcqcobANAnjhzJ0QnxiAdF04pGksE1QRWODs="
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
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
      "caller_nonce": 282,
      "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
      "gas_price": 1,
      "gas_used": 122,
      "height": 282,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEaoPo/avyQKDqq5pJbwK5c5F1c91x9t86o8ggcnfbIQZeK035FLw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
  "id": -576460752303421303,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEANpc+lEgPvZPpnn4vy7ddr+60H4PpjIsP9LtufafNExX3tQ7xscpyeFtdnuTz8Ox9aEVGmYAdocJODqdmKxUMGuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBGqD6P2r8kCg6quaSW8CuXORdXPdcfbfOqPIIHJ32yEGXipRbBuI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421303,
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
      "signed_tx": "tx_+JILAfhCuEANpc+lEgPvZPpnn4vy7ddr+60H4PpjIsP9LtufafNExX3tQ7xscpyeFtdnuTz8Ox9aEVGmYAdocJODqdmKxUMGuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBGqD6P2r8kCg6quaSW8CuXORdXPdcfbfOqPIIHJ32yEGXipRbBuI=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
  "id": -576460752303421302,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEANpc+lEgPvZPpnn4vy7ddr+60H4PpjIsP9LtufafNExX3tQ7xscpyeFtdnuTz8Ox9aEVGmYAdocJODqdmKxUMGuEA/lWEr9+a29vG5H+5DIvW55vZ4jodbDaYNC33eoiPkAISSw5RgeiUgkdiD7ErrKZwg6gFbB5Dy26BCNzE/6DkAuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBGqD6P2r8kCg6quaSW8CuXORdXPdcfbfOqPIIHJ32yEGXiiuOQTc="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421302,
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
      "state": "tx_+NQLAfiEuEANpc+lEgPvZPpnn4vy7ddr+60H4PpjIsP9LtufafNExX3tQ7xscpyeFtdnuTz8Ox9aEVGmYAdocJODqdmKxUMGuEA/lWEr9+a29vG5H+5DIvW55vZ4jodbDaYNC33eoiPkAISSw5RgeiUgkdiD7ErrKZwg6gFbB5Dy26BCNzE/6DkAuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBGqD6P2r8kCg6quaSW8CuXORdXPdcfbfOqPIIHJ32yEGXiiuOQTc="
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
      "state": "tx_+NQLAfiEuEANpc+lEgPvZPpnn4vy7ddr+60H4PpjIsP9LtufafNExX3tQ7xscpyeFtdnuTz8Ox9aEVGmYAdocJODqdmKxUMGuEA/lWEr9+a29vG5H+5DIvW55vZ4jodbDaYNC33eoiPkAISSw5RgeiUgkdiD7ErrKZwg6gFbB5Dy26BCNzE/6DkAuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBGqD6P2r8kCg6quaSW8CuXORdXPdcfbfOqPIIHJ32yEGXiiuOQTc="
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
    "round": 282
  }
}
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
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
        "round": 282
      }
    }
  },
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
    "round": 282
  }
}
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
        "round": 282
      }
    }
  },
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
    "round": 282
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
      "caller_nonce": 282,
      "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
      "gas_price": 1,
      "gas_used": 122,
      "height": 282,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
    "round": 282
  }
}
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
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
        "round": 282
      }
    }
  },
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
    "round": 282
  }
}
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
        "round": 282
      }
    }
  },
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
    "round": 282
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
      "caller_nonce": 282,
      "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
      "gas_price": 1,
      "gas_used": 122,
      "height": 282,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
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
      "caller_nonce": 283,
      "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
      "gas_price": 1,
      "gas_used": 122,
      "height": 283,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEboGnTuPbJzWYYkSkYe9nUnDDVmdO3lgLfg7reP/g+dN/i+136Mg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
  "id": -576460752303421301,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEAQAGbQljDPxXRvFyy8CWZrySdpH6zZ4Tq5e+Ai7MUeh65/d0VQ7SBzYiK/Vkk7/Zz0II/RCNkSYXMxON3bKwQDuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBG6Bp07j2yc1mGJEpGHvZ1Jww1ZnTt5YC34O63j/4PnTf4pEBGX0="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421301,
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
      "signed_tx": "tx_+JILAfhCuEAQAGbQljDPxXRvFyy8CWZrySdpH6zZ4Tq5e+Ai7MUeh65/d0VQ7SBzYiK/Vkk7/Zz0II/RCNkSYXMxON3bKwQDuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBG6Bp07j2yc1mGJEpGHvZ1Jww1ZnTt5YC34O63j/4PnTf4pEBGX0=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
  "id": -576460752303421300,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEAQAGbQljDPxXRvFyy8CWZrySdpH6zZ4Tq5e+Ai7MUeh65/d0VQ7SBzYiK/Vkk7/Zz0II/RCNkSYXMxON3bKwQDuEBq/Rm36pm3SSQFrP7My+WcoJroqC2RUsr2WPMyrp7PJdPVRCelBsrI8G6LMAE8f1bV64ybeZPCi/EuiTQyp0oKuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBG6Bp07j2yc1mGJEpGHvZ1Jww1ZnTt5YC34O63j/4PnTf4ldyhhg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421300,
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
      "state": "tx_+NQLAfiEuEAQAGbQljDPxXRvFyy8CWZrySdpH6zZ4Tq5e+Ai7MUeh65/d0VQ7SBzYiK/Vkk7/Zz0II/RCNkSYXMxON3bKwQDuEBq/Rm36pm3SSQFrP7My+WcoJroqC2RUsr2WPMyrp7PJdPVRCelBsrI8G6LMAE8f1bV64ybeZPCi/EuiTQyp0oKuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBG6Bp07j2yc1mGJEpGHvZ1Jww1ZnTt5YC34O63j/4PnTf4ldyhhg="
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
      "state": "tx_+NQLAfiEuEAQAGbQljDPxXRvFyy8CWZrySdpH6zZ4Tq5e+Ai7MUeh65/d0VQ7SBzYiK/Vkk7/Zz0II/RCNkSYXMxON3bKwQDuEBq/Rm36pm3SSQFrP7My+WcoJroqC2RUsr2WPMyrp7PJdPVRCelBsrI8G6LMAE8f1bV64ybeZPCi/EuiTQyp0oKuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBG6Bp07j2yc1mGJEpGHvZ1Jww1ZnTt5YC34O63j/4PnTf4ldyhhg="
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
    "round": 283
  }
}
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
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
        "round": 283
      }
    }
  },
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
    "round": 283
  }
}
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
        "round": 283
      }
    }
  },
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
    "round": 283
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
      "caller_nonce": 283,
      "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
      "gas_price": 1,
      "gas_used": 122,
      "height": 283,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
    "round": 283
  }
}
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
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
        "round": 283
      }
    }
  },
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
    "round": 283
  }
}
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
        "round": 283
      }
    }
  },
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
    "round": 283
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
      "caller_nonce": 283,
      "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
      "gas_price": 1,
      "gas_used": 122,
      "height": 283,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
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
      "caller_nonce": 284,
      "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
      "gas_price": 1,
      "gas_used": 276,
      "height": 284,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEcoOb/E30wEhfX+Tk1t967ku+vD9aE+4Ep1OL9SJMjIgMKWT/x/w==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
  "id": -576460752303421299,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEBJHmiuXkbovqc2/19GMmiGH5JHjqZvIZXaGCXmcRtg4yzXI6hoSTxZO31RdUjmVvfbaVT18Kw4qjmlNbKw3eUDuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBHKDm/xN9MBIX1/k5Nbfeu5Lvrw/WhPuBKdTi/UiTIyIDCjed7r4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421299,
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
      "signed_tx": "tx_+JILAfhCuEBJHmiuXkbovqc2/19GMmiGH5JHjqZvIZXaGCXmcRtg4yzXI6hoSTxZO31RdUjmVvfbaVT18Kw4qjmlNbKw3eUDuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBHKDm/xN9MBIX1/k5Nbfeu5Lvrw/WhPuBKdTi/UiTIyIDCjed7r4=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
  "id": -576460752303421298,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEAspVXgx/9/BlegXzv6XOuTVFo/Pved31PP6iDk9+paRhjOw1dQn2RVMY5e9Lv0MQCGCqvax7EsTqKOnv1jxq8BuEBJHmiuXkbovqc2/19GMmiGH5JHjqZvIZXaGCXmcRtg4yzXI6hoSTxZO31RdUjmVvfbaVT18Kw4qjmlNbKw3eUDuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBHKDm/xN9MBIX1/k5Nbfeu5Lvrw/WhPuBKdTi/UiTIyIDCuPidBc="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421298,
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
      "state": "tx_+NQLAfiEuEAspVXgx/9/BlegXzv6XOuTVFo/Pved31PP6iDk9+paRhjOw1dQn2RVMY5e9Lv0MQCGCqvax7EsTqKOnv1jxq8BuEBJHmiuXkbovqc2/19GMmiGH5JHjqZvIZXaGCXmcRtg4yzXI6hoSTxZO31RdUjmVvfbaVT18Kw4qjmlNbKw3eUDuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBHKDm/xN9MBIX1/k5Nbfeu5Lvrw/WhPuBKdTi/UiTIyIDCuPidBc="
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
      "state": "tx_+NQLAfiEuEAspVXgx/9/BlegXzv6XOuTVFo/Pved31PP6iDk9+paRhjOw1dQn2RVMY5e9Lv0MQCGCqvax7EsTqKOnv1jxq8BuEBJHmiuXkbovqc2/19GMmiGH5JHjqZvIZXaGCXmcRtg4yzXI6hoSTxZO31RdUjmVvfbaVT18Kw4qjmlNbKw3eUDuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBHKDm/xN9MBIX1/k5Nbfeu5Lvrw/WhPuBKdTi/UiTIyIDCuPidBc="
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
    "round": 284
  }
}
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
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
        "round": 284
      }
    }
  },
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
    "round": 284
  }
}
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
        "round": 284
      }
    }
  },
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
    "round": 284
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
      "caller_nonce": 284,
      "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
      "gas_price": 1,
      "gas_used": 276,
      "height": 284,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
    "round": 284
  }
}
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
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
        "round": 284
      }
    }
  },
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
    "round": 284
  }
}
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
        "round": 284
      }
    }
  },
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
    "round": 284
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
      "caller_nonce": 284,
      "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
      "gas_price": 1,
      "gas_used": 276,
      "height": 284,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
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
      "caller_nonce": 285,
      "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
      "gas_price": 1,
      "gas_used": 276,
      "height": 285,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "ABCDEFG",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
  }
}
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "ABCDEFG",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
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
        "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
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
    "block_hash": "kh_2QEZzaWk9wbFg4r6ajn2cNmohLtjLqJ5nx3x2aFqz85uiVbJfP",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEdoJeCpM9d3e1CebgrOzV7KZ9iAiUZ2ChaCa/6tavYx6SufZ/8OQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
  "id": -576460752303421297,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEA234XWuzeHqS7Rn0XYzgh+zkZwEGhPIjXW4cwWUYQuWCj4BwuQ1ormcHnj7glDUNneitOfySUG7iSaOG6bc4sDuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBHaCXgqTPXd3tQnm4Kzs1eymfYgIlGdgoWgmv+rWr2MekrgdFrCM="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421297,
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
      "signed_tx": "tx_+JILAfhCuEA234XWuzeHqS7Rn0XYzgh+zkZwEGhPIjXW4cwWUYQuWCj4BwuQ1ormcHnj7glDUNneitOfySUG7iSaOG6bc4sDuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBHaCXgqTPXd3tQnm4Kzs1eymfYgIlGdgoWgmv+rWr2MekrgdFrCM=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
  "id": -576460752303421296,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEAZpCY9a7QJJZw6aO08yKy5AguwVC4G9KvwIZXxRVlySYK8UZHXMMzTK9xwdGdhkv533bCbaXJHViRzqvas95QNuEA234XWuzeHqS7Rn0XYzgh+zkZwEGhPIjXW4cwWUYQuWCj4BwuQ1ormcHnj7glDUNneitOfySUG7iSaOG6bc4sDuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBHaCXgqTPXd3tQnm4Kzs1eymfYgIlGdgoWgmv+rWr2MekrnDqzq8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421296,
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
      "state": "tx_+NQLAfiEuEAZpCY9a7QJJZw6aO08yKy5AguwVC4G9KvwIZXxRVlySYK8UZHXMMzTK9xwdGdhkv533bCbaXJHViRzqvas95QNuEA234XWuzeHqS7Rn0XYzgh+zkZwEGhPIjXW4cwWUYQuWCj4BwuQ1ormcHnj7glDUNneitOfySUG7iSaOG6bc4sDuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBHaCXgqTPXd3tQnm4Kzs1eymfYgIlGdgoWgmv+rWr2MekrnDqzq8="
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
      "state": "tx_+NQLAfiEuEAZpCY9a7QJJZw6aO08yKy5AguwVC4G9KvwIZXxRVlySYK8UZHXMMzTK9xwdGdhkv533bCbaXJHViRzqvas95QNuEA234XWuzeHqS7Rn0XYzgh+zkZwEGhPIjXW4cwWUYQuWCj4BwuQ1ormcHnj7glDUNneitOfySUG7iSaOG6bc4sDuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBHaCXgqTPXd3tQnm4Kzs1eymfYgIlGdgoWgmv+rWr2MekrnDqzq8="
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
    "round": 285
  }
}
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
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
        "round": 285
      }
    }
  },
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
    "round": 285
  }
}
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
        "round": 285
      }
    }
  },
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
    "round": 285
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
      "caller_nonce": 285,
      "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
      "gas_price": 1,
      "gas_used": 276,
      "height": 285,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
    "round": 285
  }
}
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
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
        "round": 285
      }
    }
  },
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
    "round": 285
  }
}
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
        "round": 285
      }
    }
  },
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
    "round": 285
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
      "caller_nonce": 285,
      "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
      "gas_price": 1,
      "gas_used": 276,
      "height": 285,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "ABCDEFG",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
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
      "caller_nonce": 286,
      "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
      "gas_price": 1,
      "gas_used": 122,
      "height": 286,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "ABCDEFG",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "ABCDEFG",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "ABCDEFG",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEeoG+yl0B2qWHeO7wxhpivjF3xm1M+RM7jFrpAgIFirtgGxh+UrQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
  "id": -576460752303421295,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEAUzHmU/DtzbMAWIaBBaJ51GffEYpYnMK8dU6gA4ZudjK4ciDY93oU8Bt4utImyLogrWCsgs9ohyNTRNolL5mEMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBHqBvspdAdqlh3ju8MYaYr4xd8ZtTPkTO4xa6QICBYq7YBozSHdU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421295,
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
      "signed_tx": "tx_+JILAfhCuEAUzHmU/DtzbMAWIaBBaJ51GffEYpYnMK8dU6gA4ZudjK4ciDY93oU8Bt4utImyLogrWCsgs9ohyNTRNolL5mEMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBHqBvspdAdqlh3ju8MYaYr4xd8ZtTPkTO4xa6QICBYq7YBozSHdU=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
  "id": -576460752303421294,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEATIcBkPbjZDGY83i0ABUix9znq5055fqJ7KXbmkjGC8/qAJa7CWOP81wHERnzVSH9ascxOuubr9G6Z2Q4V45gDuEAUzHmU/DtzbMAWIaBBaJ51GffEYpYnMK8dU6gA4ZudjK4ciDY93oU8Bt4utImyLogrWCsgs9ohyNTRNolL5mEMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBHqBvspdAdqlh3ju8MYaYr4xd8ZtTPkTO4xa6QICBYq7YBn7Av8g="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421294,
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
      "state": "tx_+NQLAfiEuEATIcBkPbjZDGY83i0ABUix9znq5055fqJ7KXbmkjGC8/qAJa7CWOP81wHERnzVSH9ascxOuubr9G6Z2Q4V45gDuEAUzHmU/DtzbMAWIaBBaJ51GffEYpYnMK8dU6gA4ZudjK4ciDY93oU8Bt4utImyLogrWCsgs9ohyNTRNolL5mEMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBHqBvspdAdqlh3ju8MYaYr4xd8ZtTPkTO4xa6QICBYq7YBn7Av8g="
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
      "state": "tx_+NQLAfiEuEATIcBkPbjZDGY83i0ABUix9znq5055fqJ7KXbmkjGC8/qAJa7CWOP81wHERnzVSH9ascxOuubr9G6Z2Q4V45gDuEAUzHmU/DtzbMAWIaBBaJ51GffEYpYnMK8dU6gA4ZudjK4ciDY93oU8Bt4utImyLogrWCsgs9ohyNTRNolL5mEMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBHqBvspdAdqlh3ju8MYaYr4xd8ZtTPkTO4xa6QICBYq7YBn7Av8g="
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
    "round": 286
  }
}
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
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
        "round": 286
      }
    }
  },
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
    "round": 286
  }
}
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
        "round": 286
      }
    }
  },
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
    "round": 286
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
      "caller_nonce": 286,
      "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
      "gas_price": 1,
      "gas_used": 122,
      "height": 286,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
    "round": 286
  }
}
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
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
        "round": 286
      }
    }
  },
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
    "round": 286
  }
}
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
        "round": 286
      }
    }
  },
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
    "round": 286
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
      "caller_nonce": 286,
      "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
      "gas_price": 1,
      "gas_used": 122,
      "height": 286,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "ABCDEFG",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
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
      "caller_nonce": 287,
      "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
      "gas_price": 1,
      "gas_used": 122,
      "height": 287,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "ABCDEFG",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "ABCDEFG",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "ABCDEFG",
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEfoMboJQtHC+IhFZyGzAKYWnUCMLkfQU/aRp1ZHpFBNchRqG5bEg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
  "id": -576460752303421293,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEBpi89V7SVC9gHkflVJNVOGJU4194rJIntSWSYx+k0WaQoIJJ0zO7GIgydgfm2t4QY+XLL4+YBBjpelXlqlh3gOuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBH6DG6CULRwviIRWchswCmFp1AjC5H0FP2kadWR6RQTXIUXhkQuY="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421293,
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
      "signed_tx": "tx_+JILAfhCuEBpi89V7SVC9gHkflVJNVOGJU4194rJIntSWSYx+k0WaQoIJJ0zO7GIgydgfm2t4QY+XLL4+YBBjpelXlqlh3gOuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBH6DG6CULRwviIRWchswCmFp1AjC5H0FP2kadWR6RQTXIUXhkQuY=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK01EODZSM2RhRW1XeTVhLmNoYWluOWFjY291bnRfcHVia2V5uAW0Zw==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
  "id": -576460752303421292,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEBpi89V7SVC9gHkflVJNVOGJU4194rJIntSWSYx+k0WaQoIJJ0zO7GIgydgfm2t4QY+XLL4+YBBjpelXlqlh3gOuEC1KmkQqzQ4FGJHOvxPDjQT2ljmM6OiiH99n6SRaQ9Wmn53p8ChiMWdje272pc3BLE7phRBYqsUVcrfOa8RrHYIuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBH6DG6CULRwviIRWchswCmFp1AjC5H0FP2kadWR6RQTXIUf7hQ8k="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421292,
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
      "state": "tx_+NQLAfiEuEBpi89V7SVC9gHkflVJNVOGJU4194rJIntSWSYx+k0WaQoIJJ0zO7GIgydgfm2t4QY+XLL4+YBBjpelXlqlh3gOuEC1KmkQqzQ4FGJHOvxPDjQT2ljmM6OiiH99n6SRaQ9Wmn53p8ChiMWdje272pc3BLE7phRBYqsUVcrfOa8RrHYIuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBH6DG6CULRwviIRWchswCmFp1AjC5H0FP2kadWR6RQTXIUf7hQ8k="
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
      "state": "tx_+NQLAfiEuEBpi89V7SVC9gHkflVJNVOGJU4194rJIntSWSYx+k0WaQoIJJ0zO7GIgydgfm2t4QY+XLL4+YBBjpelXlqlh3gOuEC1KmkQqzQ4FGJHOvxPDjQT2ljmM6OiiH99n6SRaQ9Wmn53p8ChiMWdje272pc3BLE7phRBYqsUVcrfOa8RrHYIuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBH6DG6CULRwviIRWchswCmFp1AjC5H0FP2kadWR6RQTXIUf7hQ8k="
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
    "round": 287
  }
}
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
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
        "round": 287
      }
    }
  },
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
    "round": 287
  }
}
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
        "round": 287
      }
    }
  },
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
    "round": 287
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
      "caller_nonce": 287,
      "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
      "gas_price": 1,
      "gas_used": 122,
      "height": 287,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
    "round": 287
  }
}
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
        "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
        "round": 287
      }
    }
  },
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
    "round": 287
  }
}
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
        "round": 287
      }
    }
  },
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
    "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
    "round": 287
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
      "caller_nonce": 287,
      "contract_id": "ct_23bFsfbaNQ2sYqtr2LCpwCNumx17w8PBkTf2qEBK8yUk3fJWHG",
      "gas_price": 1,
      "gas_used": 122,
      "height": 287,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "ABCDEFG",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
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
      "caller_nonce": 288,
      "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
      "gas_price": 1,
      "gas_used": 276,
      "height": 288,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "ABCDEFG",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "ABCDEFG",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "ABCDEFG",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEgoMyv3GnwbNinklPCRGj+YF29NhHiQ0dvnh2auBiBw3LIgBXdPA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
  "id": -576460752303421291,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuECULByww7ywi1uwNDpqiVbrAbRTV3N9kotfN1YSurRQj17smXfXahkIWYA6R/Bib8g6/MrB0zRTDnw9H+wc/T4LuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBIKDMr9xp8GzYp5JTwkRo/mBdvTYR4kNHb54dmrgYgcNyyBJnYwQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421291,
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
      "signed_tx": "tx_+JILAfhCuECULByww7ywi1uwNDpqiVbrAbRTV3N9kotfN1YSurRQj17smXfXahkIWYA6R/Bib8g6/MrB0zRTDnw9H+wc/T4LuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBIKDMr9xp8GzYp5JTwkRo/mBdvTYR4kNHb54dmrgYgcNyyBJnYwQ=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
  "id": -576460752303421290,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuECULByww7ywi1uwNDpqiVbrAbRTV3N9kotfN1YSurRQj17smXfXahkIWYA6R/Bib8g6/MrB0zRTDnw9H+wc/T4LuEDAnoymvPvhoWb/P9SUCDtREoIY2LoUfQ6YwyNtO+YJsyWYixQGUw7GNWiDUR7ShOIo5XFzE2BP9/lx8OkDZfMMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBIKDMr9xp8GzYp5JTwkRo/mBdvTYR4kNHb54dmrgYgcNyyNhT1Gk="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421290,
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
      "state": "tx_+NQLAfiEuECULByww7ywi1uwNDpqiVbrAbRTV3N9kotfN1YSurRQj17smXfXahkIWYA6R/Bib8g6/MrB0zRTDnw9H+wc/T4LuEDAnoymvPvhoWb/P9SUCDtREoIY2LoUfQ6YwyNtO+YJsyWYixQGUw7GNWiDUR7ShOIo5XFzE2BP9/lx8OkDZfMMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBIKDMr9xp8GzYp5JTwkRo/mBdvTYR4kNHb54dmrgYgcNyyNhT1Gk="
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
      "state": "tx_+NQLAfiEuECULByww7ywi1uwNDpqiVbrAbRTV3N9kotfN1YSurRQj17smXfXahkIWYA6R/Bib8g6/MrB0zRTDnw9H+wc/T4LuEDAnoymvPvhoWb/P9SUCDtREoIY2LoUfQ6YwyNtO+YJsyWYixQGUw7GNWiDUR7ShOIo5XFzE2BP9/lx8OkDZfMMuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBIKDMr9xp8GzYp5JTwkRo/mBdvTYR4kNHb54dmrgYgcNyyNhT1Gk="
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
    "round": 288
  }
}
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
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
        "round": 288
      }
    }
  },
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
    "round": 288
  }
}
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
        "round": 288
      }
    }
  },
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
    "round": 288
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
      "caller_nonce": 288,
      "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
      "gas_price": 1,
      "gas_used": 276,
      "height": 288,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
    "round": 288
  }
}
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
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
        "round": 288
      }
    }
  },
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
    "round": 288
  }
}
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
        "round": 288
      }
    }
  },
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
    "round": 288
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
      "caller_nonce": 288,
      "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
      "gas_price": 1,
      "gas_used": 276,
      "height": 288,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "ABCDEFG",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
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
      "caller_nonce": 289,
      "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
      "gas_price": 1,
      "gas_used": 276,
      "height": 289,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "ABCDEFG",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "ABCDEFG",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "ABCDEFG",
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEhoPlSXhEbGN/Fa+lWzFYysJf1KbGm7mqjlFMlZVSea7kaKxI0mA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
  "id": -576460752303421289,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEAxuXXHQs7zuTdWdV6mCrOgm3N0L7DMb6wiDtYZ0CIULetMkbzWZlpDE1uaDioH3jcZd//zkkXgfuhGwMKkpwAGuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBIaD5Ul4RGxjfxWvpVsxWMrCX9Smxpu5qo5RTJWVUnmu5GhuuyEc="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421289,
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
      "signed_tx": "tx_+JILAfhCuEAxuXXHQs7zuTdWdV6mCrOgm3N0L7DMb6wiDtYZ0CIULetMkbzWZlpDE1uaDioH3jcZd//zkkXgfuhGwMKkpwAGuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBIaD5Ul4RGxjfxWvpVsxWMrCX9Smxpu5qo5RTJWVUnmu5GhuuyEc=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoImUFDv7vZIzO6XMcL2+ZmRWofn2IO0k1XQFDY5uymeeTUQ4NlIzZGFFbVd5NWEuY2hhaW45YWNjb3VudF9wdWJrZXm+ewYu",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
  "id": -576460752303421288,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEAa69pE16J1XulmAyZtycMc+85WzGPjSA978qRfSapZAnSTSMPwRJG3s20SmrjJAbDIPaLOmrDH35JCHbNQLTQJuEAxuXXHQs7zuTdWdV6mCrOgm3N0L7DMb6wiDtYZ0CIULetMkbzWZlpDE1uaDioH3jcZd//zkkXgfuhGwMKkpwAGuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBIaD5Ul4RGxjfxWvpVsxWMrCX9Smxpu5qo5RTJWVUnmu5GvN1OsM="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421288,
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
      "state": "tx_+NQLAfiEuEAa69pE16J1XulmAyZtycMc+85WzGPjSA978qRfSapZAnSTSMPwRJG3s20SmrjJAbDIPaLOmrDH35JCHbNQLTQJuEAxuXXHQs7zuTdWdV6mCrOgm3N0L7DMb6wiDtYZ0CIULetMkbzWZlpDE1uaDioH3jcZd//zkkXgfuhGwMKkpwAGuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBIaD5Ul4RGxjfxWvpVsxWMrCX9Smxpu5qo5RTJWVUnmu5GvN1OsM="
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
      "state": "tx_+NQLAfiEuEAa69pE16J1XulmAyZtycMc+85WzGPjSA978qRfSapZAnSTSMPwRJG3s20SmrjJAbDIPaLOmrDH35JCHbNQLTQJuEAxuXXHQs7zuTdWdV6mCrOgm3N0L7DMb6wiDtYZ0CIULetMkbzWZlpDE1uaDioH3jcZd//zkkXgfuhGwMKkpwAGuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBIaD5Ul4RGxjfxWvpVsxWMrCX9Smxpu5qo5RTJWVUnmu5GvN1OsM="
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
    "round": 289
  }
}
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
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
        "round": 289
      }
    }
  },
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
    "round": 289
  }
}
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
        "round": 289
      }
    }
  },
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
    "round": 289
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
      "caller_nonce": 289,
      "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
      "gas_price": 1,
      "gas_used": 276,
      "height": 289,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
    "round": 289
  }
}
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
        "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
        "round": 289
      }
    }
  },
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
    "round": 289
  }
}
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
        "round": 289
      }
    }
  },
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
    "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
    "round": 289
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
      "caller_nonce": 289,
      "contract_id": "ct_UrUGBNz8RY6iD3CaMnpr6t3hYomZycF94uizu6inE9Z9tyvAe",
      "gas_price": 1,
      "gas_used": 276,
      "height": 289,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
        "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
    "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
        "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
    "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
        "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
    "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEioGvNNHVEDuonc5X4tEk5fD5MPKV9/zJm9bfHi/z9wW/p9qph7g==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
  "id": -576460752303421287,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEDcurJT3npvx6bn32vUohSItY+HiHY7T1PEmV+V6pShqchxJHMWMK/TAyFBTOYNhTcLPtnpPOxhR5X3ScoXoT8EuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBIqBrzTR1RA7qJ3OV+LRJOXw+TDylff8yZvW3x4v8/cFv6QUhiUw="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421287,
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
      "signed_tx": "tx_+JILAfhCuEDcurJT3npvx6bn32vUohSItY+HiHY7T1PEmV+V6pShqchxJHMWMK/TAyFBTOYNhTcLPtnpPOxhR5X3ScoXoT8EuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBIqBrzTR1RA7qJ3OV+LRJOXw+TDylff8yZvW3x4v8/cFv6QUhiUw=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
  "id": -576460752303421286,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEB37UBvK1iVwiKa5Z2vegsEQLYlwX2jiYYGc/fgLeUuOLPiBIcdVGTxCbk/YXK9uS5ugVw2X2JI/0cO4ULCoO8LuEDcurJT3npvx6bn32vUohSItY+HiHY7T1PEmV+V6pShqchxJHMWMK/TAyFBTOYNhTcLPtnpPOxhR5X3ScoXoT8EuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBIqBrzTR1RA7qJ3OV+LRJOXw+TDylff8yZvW3x4v8/cFv6cfty10="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421286,
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
      "state": "tx_+NQLAfiEuEB37UBvK1iVwiKa5Z2vegsEQLYlwX2jiYYGc/fgLeUuOLPiBIcdVGTxCbk/YXK9uS5ugVw2X2JI/0cO4ULCoO8LuEDcurJT3npvx6bn32vUohSItY+HiHY7T1PEmV+V6pShqchxJHMWMK/TAyFBTOYNhTcLPtnpPOxhR5X3ScoXoT8EuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBIqBrzTR1RA7qJ3OV+LRJOXw+TDylff8yZvW3x4v8/cFv6cfty10="
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
      "state": "tx_+NQLAfiEuEB37UBvK1iVwiKa5Z2vegsEQLYlwX2jiYYGc/fgLeUuOLPiBIcdVGTxCbk/YXK9uS5ugVw2X2JI/0cO4ULCoO8LuEDcurJT3npvx6bn32vUohSItY+HiHY7T1PEmV+V6pShqchxJHMWMK/TAyFBTOYNhTcLPtnpPOxhR5X3ScoXoT8EuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBIqBrzTR1RA7qJ3OV+LRJOXw+TDylff8yZvW3x4v8/cFv6cfty10="
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
    "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
        "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
    "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
        "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
    "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
        "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
    "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEjoPYCmpINScDX2blOpji9M7ulkEN6+5R9GsYe+ee6zLNi4g0YIg==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
  "id": -576460752303421285,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEARjnJSz4K7VVN4Zmp6OGK2TSz3K4tGsBmchgAgrwMfhMhxARanliv08uMZ/vZmnJk+PkTYJ87RwkhcRHd0qWABuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBI6D2ApqSDUnA19m5TqY4vTO7pZBDevuUfRrGHvnnusyzYlMk7K8="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421285,
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
      "signed_tx": "tx_+JILAfhCuEARjnJSz4K7VVN4Zmp6OGK2TSz3K4tGsBmchgAgrwMfhMhxARanliv08uMZ/vZmnJk+PkTYJ87RwkhcRHd0qWABuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBI6D2ApqSDUnA19m5TqY4vTO7pZBDevuUfRrGHvnnusyzYlMk7K8=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
  "id": -576460752303421284,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEARjnJSz4K7VVN4Zmp6OGK2TSz3K4tGsBmchgAgrwMfhMhxARanliv08uMZ/vZmnJk+PkTYJ87RwkhcRHd0qWABuECv/+KmPy1gUAYvcgRLpR25U2Ah1RXHJyHvEGLikrHzDscoUHsrXkJYOAuGdKl3BMCc+e4tofNgrt6RsLLLhW4IuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBI6D2ApqSDUnA19m5TqY4vTO7pZBDevuUfRrGHvnnusyzYmqPwEQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421284,
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
      "state": "tx_+NQLAfiEuEARjnJSz4K7VVN4Zmp6OGK2TSz3K4tGsBmchgAgrwMfhMhxARanliv08uMZ/vZmnJk+PkTYJ87RwkhcRHd0qWABuECv/+KmPy1gUAYvcgRLpR25U2Ah1RXHJyHvEGLikrHzDscoUHsrXkJYOAuGdKl3BMCc+e4tofNgrt6RsLLLhW4IuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBI6D2ApqSDUnA19m5TqY4vTO7pZBDevuUfRrGHvnnusyzYmqPwEQ="
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
      "state": "tx_+NQLAfiEuEARjnJSz4K7VVN4Zmp6OGK2TSz3K4tGsBmchgAgrwMfhMhxARanliv08uMZ/vZmnJk+PkTYJ87RwkhcRHd0qWABuECv/+KmPy1gUAYvcgRLpR25U2Ah1RXHJyHvEGLikrHzDscoUHsrXkJYOAuGdKl3BMCc+e4tofNgrt6RsLLLhW4IuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBI6D2ApqSDUnA19m5TqY4vTO7pZBDevuUfRrGHvnnusyzYmqPwEQ="
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
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
      "caller_nonce": 292,
      "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
      "gas_price": 1,
      "gas_used": 122,
      "height": 292,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEkoNrNrvFPmWI9o8rxmUZXEWR/GQdCsKFnHyJ/P2FgU8MZgXaGiA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
  "id": -576460752303421283,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEB17XIEWWWfc1qsfhT8g5brC6WrYgwltmGbiGYDc/HdyGYpS9emCUcFwaKq6lfeDhLzwqluKJWcgLQNFijD0SoHuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBJKDaza7xT5liPaPK8ZlGVxFkfxkHQrChZx8ifz9hYFPDGarHcz4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421283,
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
      "signed_tx": "tx_+JILAfhCuEB17XIEWWWfc1qsfhT8g5brC6WrYgwltmGbiGYDc/HdyGYpS9emCUcFwaKq6lfeDhLzwqluKJWcgLQNFijD0SoHuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBJKDaza7xT5liPaPK8ZlGVxFkfxkHQrChZx8ifz9hYFPDGarHcz4=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
  "id": -576460752303421282,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEAXxAWq93wEtEVTxL6l440CdQ3Vkbq1q85kWM0bju4KkKF52NrJDtdxI0/WxJYwU0gEnIDgsBOPAdG6m9sQ1toNuEB17XIEWWWfc1qsfhT8g5brC6WrYgwltmGbiGYDc/HdyGYpS9emCUcFwaKq6lfeDhLzwqluKJWcgLQNFijD0SoHuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBJKDaza7xT5liPaPK8ZlGVxFkfxkHQrChZx8ifz9hYFPDGWVjfds="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421282,
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
      "state": "tx_+NQLAfiEuEAXxAWq93wEtEVTxL6l440CdQ3Vkbq1q85kWM0bju4KkKF52NrJDtdxI0/WxJYwU0gEnIDgsBOPAdG6m9sQ1toNuEB17XIEWWWfc1qsfhT8g5brC6WrYgwltmGbiGYDc/HdyGYpS9emCUcFwaKq6lfeDhLzwqluKJWcgLQNFijD0SoHuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBJKDaza7xT5liPaPK8ZlGVxFkfxkHQrChZx8ifz9hYFPDGWVjfds="
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
      "state": "tx_+NQLAfiEuEAXxAWq93wEtEVTxL6l440CdQ3Vkbq1q85kWM0bju4KkKF52NrJDtdxI0/WxJYwU0gEnIDgsBOPAdG6m9sQ1toNuEB17XIEWWWfc1qsfhT8g5brC6WrYgwltmGbiGYDc/HdyGYpS9emCUcFwaKq6lfeDhLzwqluKJWcgLQNFijD0SoHuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBJKDaza7xT5liPaPK8ZlGVxFkfxkHQrChZx8ifz9hYFPDGWVjfds="
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
    "round": 292
  }
}
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
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
        "round": 292
      }
    }
  },
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
    "round": 292
  }
}
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
        "round": 292
      }
    }
  },
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
    "round": 292
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
      "caller_nonce": 292,
      "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
      "gas_price": 1,
      "gas_used": 122,
      "height": 292,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
    "round": 292
  }
}
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
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
        "round": 292
      }
    }
  },
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
    "round": 292
  }
}
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
        "round": 292
      }
    }
  },
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
    "round": 292
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
      "caller_nonce": 292,
      "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
      "gas_price": 1,
      "gas_used": 122,
      "height": 292,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
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
      "caller_nonce": 293,
      "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
      "gas_price": 1,
      "gas_used": 122,
      "height": 293,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEloMkpCvM97dXAiOZ4SQU+ajYhvDA/s/wpv/q6WHXo+mkgOrsewQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
  "id": -576460752303421281,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuECcQV2i73ANESyvCCOBdBitCJ/TCMOcDOyA56CcD9RWsPqkzjGITmM7rkoMS2HzAMsKLiWvSqupdGmDM1Fp8rcJuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBJaDJKQrzPe3VwIjmeEkFPmo2IbwwP7P8Kb/6ulh16PppIEmXZ3w="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421281,
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
      "signed_tx": "tx_+JILAfhCuECcQV2i73ANESyvCCOBdBitCJ/TCMOcDOyA56CcD9RWsPqkzjGITmM7rkoMS2HzAMsKLiWvSqupdGmDM1Fp8rcJuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBJaDJKQrzPe3VwIjmeEkFPmo2IbwwP7P8Kb/6ulh16PppIEmXZ3w=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
  "id": -576460752303421280,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuECcQV2i73ANESyvCCOBdBitCJ/TCMOcDOyA56CcD9RWsPqkzjGITmM7rkoMS2HzAMsKLiWvSqupdGmDM1Fp8rcJuED+Rrz6PniEObCUq7O4/m7qKk1xYvuZ4XeQCym/YyYn9fM4kw2+iIYEl7HkX40z+d27729Jb7UfpPoGECPq8jsAuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBJaDJKQrzPe3VwIjmeEkFPmo2IbwwP7P8Kb/6ulh16PppID25kbQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421280,
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
      "state": "tx_+NQLAfiEuECcQV2i73ANESyvCCOBdBitCJ/TCMOcDOyA56CcD9RWsPqkzjGITmM7rkoMS2HzAMsKLiWvSqupdGmDM1Fp8rcJuED+Rrz6PniEObCUq7O4/m7qKk1xYvuZ4XeQCym/YyYn9fM4kw2+iIYEl7HkX40z+d27729Jb7UfpPoGECPq8jsAuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBJaDJKQrzPe3VwIjmeEkFPmo2IbwwP7P8Kb/6ulh16PppID25kbQ="
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
      "state": "tx_+NQLAfiEuECcQV2i73ANESyvCCOBdBitCJ/TCMOcDOyA56CcD9RWsPqkzjGITmM7rkoMS2HzAMsKLiWvSqupdGmDM1Fp8rcJuED+Rrz6PniEObCUq7O4/m7qKk1xYvuZ4XeQCym/YyYn9fM4kw2+iIYEl7HkX40z+d27729Jb7UfpPoGECPq8jsAuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBJaDJKQrzPe3VwIjmeEkFPmo2IbwwP7P8Kb/6ulh16PppID25kbQ="
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
    "round": 293
  }
}
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
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
        "round": 293
      }
    }
  },
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
    "round": 293
  }
}
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
        "round": 293
      }
    }
  },
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
    "round": 293
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
      "caller_nonce": 293,
      "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
      "gas_price": 1,
      "gas_used": 122,
      "height": 293,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
    "round": 293
  }
}
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
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
        "round": 293
      }
    }
  },
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
    "round": 293
  }
}
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
        "round": 293
      }
    }
  },
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
    "round": 293
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
      "caller_nonce": 293,
      "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
      "gas_price": 1,
      "gas_used": 122,
      "height": 293,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
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
      "caller_nonce": 294,
      "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
      "gas_price": 1,
      "gas_used": 276,
      "height": 294,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEmoMUvQ7Cric/PGyzCohaRzJNAVkL0e0P/WrznHSRd53CTEyBl8Q==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
  "id": -576460752303421279,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEADfsabneJXejxRHd9db4uUgoMBQOv9FQ5xPa/MqzM/6rlSr0hYM/NFtJjaVi6wZvRU+KJQ2JFmIFxx8JL09AsJuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBJqDFL0Owq4nPzxsswqIWkcyTQFZC9HtD/1q85x0kXedwk58B5n0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421279,
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
      "signed_tx": "tx_+JILAfhCuEADfsabneJXejxRHd9db4uUgoMBQOv9FQ5xPa/MqzM/6rlSr0hYM/NFtJjaVi6wZvRU+KJQ2JFmIFxx8JL09AsJuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBJqDFL0Owq4nPzxsswqIWkcyTQFZC9HtD/1q85x0kXedwk58B5n0=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
  "id": -576460752303421278,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEADfsabneJXejxRHd9db4uUgoMBQOv9FQ5xPa/MqzM/6rlSr0hYM/NFtJjaVi6wZvRU+KJQ2JFmIFxx8JL09AsJuEAseQwHWEYlHGIhBcGZBdp2oYlapUB7vI4QsYENMVwBUgATL7MmR0hwp/zZ+tlk84XzvwNsUxXozHIJpljQ3roNuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBJqDFL0Owq4nPzxsswqIWkcyTQFZC9HtD/1q85x0kXedwk+TWBys="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421278,
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
      "state": "tx_+NQLAfiEuEADfsabneJXejxRHd9db4uUgoMBQOv9FQ5xPa/MqzM/6rlSr0hYM/NFtJjaVi6wZvRU+KJQ2JFmIFxx8JL09AsJuEAseQwHWEYlHGIhBcGZBdp2oYlapUB7vI4QsYENMVwBUgATL7MmR0hwp/zZ+tlk84XzvwNsUxXozHIJpljQ3roNuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBJqDFL0Owq4nPzxsswqIWkcyTQFZC9HtD/1q85x0kXedwk+TWBys="
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
      "state": "tx_+NQLAfiEuEADfsabneJXejxRHd9db4uUgoMBQOv9FQ5xPa/MqzM/6rlSr0hYM/NFtJjaVi6wZvRU+KJQ2JFmIFxx8JL09AsJuEAseQwHWEYlHGIhBcGZBdp2oYlapUB7vI4QsYENMVwBUgATL7MmR0hwp/zZ+tlk84XzvwNsUxXozHIJpljQ3roNuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBJqDFL0Owq4nPzxsswqIWkcyTQFZC9HtD/1q85x0kXedwk+TWBys="
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
    "round": 294
  }
}
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
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
        "round": 294
      }
    }
  },
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
    "round": 294
  }
}
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
        "round": 294
      }
    }
  },
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
    "round": 294
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
      "caller_nonce": 294,
      "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
      "gas_price": 1,
      "gas_used": 276,
      "height": 294,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
    "round": 294
  }
}
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
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
        "round": 294
      }
    }
  },
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
    "round": 294
  }
}
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
        "round": 294
      }
    }
  },
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
    "round": 294
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
      "caller_nonce": 294,
      "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
      "gas_price": 1,
      "gas_used": 276,
      "height": 294,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
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
      "caller_nonce": 295,
      "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
      "gas_price": 1,
      "gas_used": 276,
      "height": 295,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
  }
}
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
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
        "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
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
    "block_hash": "kh_hURye1gnVb5beZaQsiKGTuEpFdC3F4vnKKP35EM1YtXCDBUe7",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEnoFRAAeQNMgHH0NlU1RQzteajg5FRfNUHs3m3htf86WAsxifjKw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
  "id": -576460752303421277,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEBWSlG3lPlJ0HARydLn+Emrk38uR3q+Avs/otQ5rr4gtzigmyb4Z0SUNMFC1SUVUEVPnHHjL6PYMptPc8PL7IkBuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBJ6BUQAHkDTIBx9DZVNUUM7Xmo4ORUXzVB7N5t4bX/OlgLPRMQ+M="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421277,
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
      "signed_tx": "tx_+JILAfhCuEBWSlG3lPlJ0HARydLn+Emrk38uR3q+Avs/otQ5rr4gtzigmyb4Z0SUNMFC1SUVUEVPnHHjL6PYMptPc8PL7IkBuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBJ6BUQAHkDTIBx9DZVNUUM7Xmo4ORUXzVB7N5t4bX/OlgLPRMQ+M=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
  "id": -576460752303421276,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEBWSlG3lPlJ0HARydLn+Emrk38uR3q+Avs/otQ5rr4gtzigmyb4Z0SUNMFC1SUVUEVPnHHjL6PYMptPc8PL7IkBuEBdoiXTDQXXtJ/4ZKRy3ddFHsyXlGVHUM+/L9o0YYtzbeRODefc6VubMJVdUbrP9NrtwEjmhlreG82YYmKxOAkBuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBJ6BUQAHkDTIBx9DZVNUUM7Xmo4ORUXzVB7N5t4bX/OlgLAJJZks="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421276,
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
      "state": "tx_+NQLAfiEuEBWSlG3lPlJ0HARydLn+Emrk38uR3q+Avs/otQ5rr4gtzigmyb4Z0SUNMFC1SUVUEVPnHHjL6PYMptPc8PL7IkBuEBdoiXTDQXXtJ/4ZKRy3ddFHsyXlGVHUM+/L9o0YYtzbeRODefc6VubMJVdUbrP9NrtwEjmhlreG82YYmKxOAkBuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBJ6BUQAHkDTIBx9DZVNUUM7Xmo4ORUXzVB7N5t4bX/OlgLAJJZks="
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
      "state": "tx_+NQLAfiEuEBWSlG3lPlJ0HARydLn+Emrk38uR3q+Avs/otQ5rr4gtzigmyb4Z0SUNMFC1SUVUEVPnHHjL6PYMptPc8PL7IkBuEBdoiXTDQXXtJ/4ZKRy3ddFHsyXlGVHUM+/L9o0YYtzbeRODefc6VubMJVdUbrP9NrtwEjmhlreG82YYmKxOAkBuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBJ6BUQAHkDTIBx9DZVNUUM7Xmo4ORUXzVB7N5t4bX/OlgLAJJZks="
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
    "round": 295
  }
}
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
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
        "round": 295
      }
    }
  },
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
    "round": 295
  }
}
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
        "round": 295
      }
    }
  },
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
    "round": 295
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
      "caller_nonce": 295,
      "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
      "gas_price": 1,
      "gas_used": 276,
      "height": 295,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
    "round": 295
  }
}
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
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
        "round": 295
      }
    }
  },
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
    "round": 295
  }
}
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
        "round": 295
      }
    }
  },
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
    "round": 295
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
      "caller_nonce": 295,
      "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
      "gas_price": 1,
      "gas_used": 276,
      "height": 295,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
  }
}
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
  }
}
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
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
      "caller_nonce": 296,
      "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
      "gas_price": 1,
      "gas_used": 122,
      "height": 296,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
  }
}
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
  }
}
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
  }
}
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEooCEc+k4gbOYyQSvDQZArtHX2MpmOI/6WD8ZjrCnBsMoG8GleWQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
  "id": -576460752303421275,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEDxc0yEDTw+mYPwoODpaQXvcseRFmh2mVZJGpy1sNO3nBQwejHU9bkG8sjISBmj5QXO5loJhnIb8wsO0vYPHesKuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBKKAhHPpOIGzmMkErw0GQK7R19jKZjiP+lg/GY6wpwbDKBjb2HlI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421275,
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
      "signed_tx": "tx_+JILAfhCuEDxc0yEDTw+mYPwoODpaQXvcseRFmh2mVZJGpy1sNO3nBQwejHU9bkG8sjISBmj5QXO5loJhnIb8wsO0vYPHesKuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBKKAhHPpOIGzmMkErw0GQK7R19jKZjiP+lg/GY6wpwbDKBjb2HlI=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
  "id": -576460752303421274,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEDj44mXsCDTlp7vZLBDYLInxAbAhG2Yx/et5qs3hdklJ+/bHwopKh9/9qwBnsx/g+j5jjvV7XWlVZJixwQG+J4IuEDxc0yEDTw+mYPwoODpaQXvcseRFmh2mVZJGpy1sNO3nBQwejHU9bkG8sjISBmj5QXO5loJhnIb8wsO0vYPHesKuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBKKAhHPpOIGzmMkErw0GQK7R19jKZjiP+lg/GY6wpwbDKBmn/0qk="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421274,
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
      "state": "tx_+NQLAfiEuEDj44mXsCDTlp7vZLBDYLInxAbAhG2Yx/et5qs3hdklJ+/bHwopKh9/9qwBnsx/g+j5jjvV7XWlVZJixwQG+J4IuEDxc0yEDTw+mYPwoODpaQXvcseRFmh2mVZJGpy1sNO3nBQwejHU9bkG8sjISBmj5QXO5loJhnIb8wsO0vYPHesKuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBKKAhHPpOIGzmMkErw0GQK7R19jKZjiP+lg/GY6wpwbDKBmn/0qk="
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
      "state": "tx_+NQLAfiEuEDj44mXsCDTlp7vZLBDYLInxAbAhG2Yx/et5qs3hdklJ+/bHwopKh9/9qwBnsx/g+j5jjvV7XWlVZJixwQG+J4IuEDxc0yEDTw+mYPwoODpaQXvcseRFmh2mVZJGpy1sNO3nBQwejHU9bkG8sjISBmj5QXO5loJhnIb8wsO0vYPHesKuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBKKAhHPpOIGzmMkErw0GQK7R19jKZjiP+lg/GY6wpwbDKBmn/0qk="
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
    "round": 296
  }
}
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
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
        "round": 296
      }
    }
  },
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
    "round": 296
  }
}
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
        "round": 296
      }
    }
  },
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
    "round": 296
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
      "caller_nonce": 296,
      "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
      "gas_price": 1,
      "gas_used": 122,
      "height": 296,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
    "round": 296
  }
}
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
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
        "round": 296
      }
    }
  },
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
    "round": 296
  }
}
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
        "round": 296
      }
    }
  },
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
    "round": 296
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
      "caller_nonce": 296,
      "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
      "gas_price": 1,
      "gas_used": 122,
      "height": 296,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
  }
}
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
  }
}
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
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
      "caller_nonce": 297,
      "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
      "gas_price": 1,
      "gas_used": 122,
      "height": 297,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
  }
}
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
  }
}
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
  }
}
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEpoNrblybzfJ3/+o/ZZCN7xm5qVffrT93g8lBnliZnH7765SOYmA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
  "id": -576460752303421273,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuECyEbapnJLMUydyb79O2es5EkpSz+eNkAG4Ss8WuRKiLVjTBtS7W55XAFc2poVjcqgfUy6MyXq8Ak/y3xo1Gn4NuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBKaDa25cm83yd//qP2WQje8ZualX360/d4PJQZ5YmZx+++s3rTi4="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421273,
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
      "signed_tx": "tx_+JILAfhCuECyEbapnJLMUydyb79O2es5EkpSz+eNkAG4Ss8WuRKiLVjTBtS7W55XAFc2poVjcqgfUy6MyXq8Ak/y3xo1Gn4NuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBKaDa25cm83yd//qP2WQje8ZualX360/d4PJQZ5YmZx+++s3rTi4=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FCZWpBRnR6aHFGV0xWTS5jaGFpbjlhY2NvdW50X3B1YmtleX6ieDc=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
  "id": -576460752303421272,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuECyEbapnJLMUydyb79O2es5EkpSz+eNkAG4Ss8WuRKiLVjTBtS7W55XAFc2poVjcqgfUy6MyXq8Ak/y3xo1Gn4NuEDkwguRkkZ3IMzWALUMfiwjYSyg1/LnnJde2kOHF3Kl74QuIwmm1U8zviSveU7qO817a7+3YZJCkCpAWP6Ui2sCuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBKaDa25cm83yd//qP2WQje8ZualX360/d4PJQZ5YmZx+++i4FHeU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421272,
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
      "state": "tx_+NQLAfiEuECyEbapnJLMUydyb79O2es5EkpSz+eNkAG4Ss8WuRKiLVjTBtS7W55XAFc2poVjcqgfUy6MyXq8Ak/y3xo1Gn4NuEDkwguRkkZ3IMzWALUMfiwjYSyg1/LnnJde2kOHF3Kl74QuIwmm1U8zviSveU7qO817a7+3YZJCkCpAWP6Ui2sCuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBKaDa25cm83yd//qP2WQje8ZualX360/d4PJQZ5YmZx+++i4FHeU="
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
      "state": "tx_+NQLAfiEuECyEbapnJLMUydyb79O2es5EkpSz+eNkAG4Ss8WuRKiLVjTBtS7W55XAFc2poVjcqgfUy6MyXq8Ak/y3xo1Gn4NuEDkwguRkkZ3IMzWALUMfiwjYSyg1/LnnJde2kOHF3Kl74QuIwmm1U8zviSveU7qO817a7+3YZJCkCpAWP6Ui2sCuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBKaDa25cm83yd//qP2WQje8ZualX360/d4PJQZ5YmZx+++i4FHeU="
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
    "round": 297
  }
}
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
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
        "round": 297
      }
    }
  },
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
    "round": 297
  }
}
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
        "round": 297
      }
    }
  },
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
    "round": 297
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
      "caller_nonce": 297,
      "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
      "gas_price": 1,
      "gas_used": 122,
      "height": 297,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
    "round": 297
  }
}
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
        "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
        "round": 297
      }
    }
  },
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
    "round": 297
  }
}
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
        "round": 297
      }
    }
  },
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
    "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
    "round": 297
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
      "caller_nonce": 297,
      "contract_id": "ct_2TyRWY2JrQPGK7DZeiH2zMKJCQkUUH1XzJzGWD3o7pBk77jT1n",
      "gas_price": 1,
      "gas_used": 122,
      "height": 297,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
  }
}
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
  }
}
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
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
      "caller_nonce": 298,
      "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
      "gas_price": 1,
      "gas_used": 276,
      "height": 298,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
  }
}
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
  }
}
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
  }
}
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEqoG194NzmEGTu1Y3kGD1L8DnmsWduRTzGLguTYaO/D2q8iDdQxg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
  "id": -576460752303421271,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEDRbFBYPy18SOxn+bjAVqCaiKCshyNPig1ROwOCB+MbQ5WYk1WsGsUrG7uFhxqdbX/FSEq3KuiedapPXpmTOUYBuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBKqBtfeDc5hBk7tWN5Bg9S/A55rFnbkU8xi4Lk2Gjvw9qvNfjEVU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421271,
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
      "signed_tx": "tx_+JILAfhCuEDRbFBYPy18SOxn+bjAVqCaiKCshyNPig1ROwOCB+MbQ5WYk1WsGsUrG7uFhxqdbX/FSEq3KuiedapPXpmTOUYBuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBKqBtfeDc5hBk7tWN5Bg9S/A55rFnbkU8xi4Lk2Gjvw9qvNfjEVU=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
  "id": -576460752303421270,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEAKUHXwf+HNEPrsUNPSLKhwoqd0DllsNq0C51piIQzltMNQlTbwNazdVy220LoU9ngOH3TSsmuFDbuFYAIqr1wKuEDRbFBYPy18SOxn+bjAVqCaiKCshyNPig1ROwOCB+MbQ5WYk1WsGsUrG7uFhxqdbX/FSEq3KuiedapPXpmTOUYBuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBKqBtfeDc5hBk7tWN5Bg9S/A55rFnbkU8xi4Lk2Gjvw9qvHdMIaE="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421270,
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
      "state": "tx_+NQLAfiEuEAKUHXwf+HNEPrsUNPSLKhwoqd0DllsNq0C51piIQzltMNQlTbwNazdVy220LoU9ngOH3TSsmuFDbuFYAIqr1wKuEDRbFBYPy18SOxn+bjAVqCaiKCshyNPig1ROwOCB+MbQ5WYk1WsGsUrG7uFhxqdbX/FSEq3KuiedapPXpmTOUYBuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBKqBtfeDc5hBk7tWN5Bg9S/A55rFnbkU8xi4Lk2Gjvw9qvHdMIaE="
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
      "state": "tx_+NQLAfiEuEAKUHXwf+HNEPrsUNPSLKhwoqd0DllsNq0C51piIQzltMNQlTbwNazdVy220LoU9ngOH3TSsmuFDbuFYAIqr1wKuEDRbFBYPy18SOxn+bjAVqCaiKCshyNPig1ROwOCB+MbQ5WYk1WsGsUrG7uFhxqdbX/FSEq3KuiedapPXpmTOUYBuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBKqBtfeDc5hBk7tWN5Bg9S/A55rFnbkU8xi4Lk2Gjvw9qvHdMIaE="
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
    "round": 298
  }
}
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
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
        "round": 298
      }
    }
  },
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
    "round": 298
  }
}
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
        "round": 298
      }
    }
  },
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
    "round": 298
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
      "caller_nonce": 298,
      "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
      "gas_price": 1,
      "gas_used": 276,
      "height": 298,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
    "round": 298
  }
}
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
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
        "round": 298
      }
    }
  },
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
    "round": 298
  }
}
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
        "round": 298
      }
    }
  },
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
    "round": 298
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
      "caller_nonce": 298,
      "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
      "gas_price": 1,
      "gas_used": 276,
      "height": 298,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
  }
}
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
  }
}
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
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
      "caller_nonce": 299,
      "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
      "gas_price": 1,
      "gas_used": 276,
      "height": 299,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
  }
}
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
  }
}
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
  }
}
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
      }
    }
  },
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
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
        "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
        "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
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
    "block_hash": "kh_26VKu8k9P7kk6tquZdYYMHEQ7ed5KR4tchpjdZbRxqatFmFQhC",
    "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53ggEroBmp8MmM5iEqonBkhVYjXVVOPgZ6yIPSEfdnzhyCdZ1rqas/rA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
  "id": -576460752303421269,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEDLu17KYJ+ylcVwZroxu3X7sdnIQmkTUgoa8RuijMoi8nR+7FZeOnLwL9NU/A8Ic1vRyr6f6tJ2PqWYv7LQt54BuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBK6AZqfDJjOYhKqJwZIVWI11VTj4GesiD0hH3Z84cgnWdazuW75I="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421269,
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
      "signed_tx": "tx_+JILAfhCuEDLu17KYJ+ylcVwZroxu3X7sdnIQmkTUgoa8RuijMoi8nR+7FZeOnLwL9NU/A8Ic1vRyr6f6tJ2PqWYv7LQt54BuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBK6AZqfDJjOYhKqJwZIVWI11VTj4GesiD0hH3Z84cgnWdazuW75I=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoMDw7tKdfuiRM69ytDZhf2EEPqGnSQhqLFfvW6LiNeaxUUJlakFGdHpocUZXTFZNLmNoYWluOWFjY291bnRfcHVia2V50bglIw==",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
  "id": -576460752303421268,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEAVFaNM3xWvt8nS4PMEGjbSaBxWqPDDvq/9KUoego1WReN6mYk1a0064R1rrMTDM5wf5KXqmITJFKUPgT8sOVwNuEDLu17KYJ+ylcVwZroxu3X7sdnIQmkTUgoa8RuijMoi8nR+7FZeOnLwL9NU/A8Ic1vRyr6f6tJ2PqWYv7LQt54BuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBK6AZqfDJjOYhKqJwZIVWI11VTj4GesiD0hH3Z84cgnWda5o9BMI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421268,
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
      "state": "tx_+NQLAfiEuEAVFaNM3xWvt8nS4PMEGjbSaBxWqPDDvq/9KUoego1WReN6mYk1a0064R1rrMTDM5wf5KXqmITJFKUPgT8sOVwNuEDLu17KYJ+ylcVwZroxu3X7sdnIQmkTUgoa8RuijMoi8nR+7FZeOnLwL9NU/A8Ic1vRyr6f6tJ2PqWYv7LQt54BuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBK6AZqfDJjOYhKqJwZIVWI11VTj4GesiD0hH3Z84cgnWda5o9BMI="
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
      "state": "tx_+NQLAfiEuEAVFaNM3xWvt8nS4PMEGjbSaBxWqPDDvq/9KUoego1WReN6mYk1a0064R1rrMTDM5wf5KXqmITJFKUPgT8sOVwNuEDLu17KYJ+ylcVwZroxu3X7sdnIQmkTUgoa8RuijMoi8nR+7FZeOnLwL9NU/A8Ic1vRyr6f6tJ2PqWYv7LQt54BuEr4SDkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4IBK6AZqfDJjOYhKqJwZIVWI11VTj4GesiD0hH3Z84cgnWda5o9BMI="
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
    "round": 299
  }
}
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
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
        "round": 299
      }
    }
  },
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
    "round": 299
  }
}
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
        "round": 299
      }
    }
  },
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
    "round": 299
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
      "caller_nonce": 299,
      "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
      "gas_price": 1,
      "gas_used": 276,
      "height": 299,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
    "round": 299
  }
}
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
        "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
        "round": 299
      }
    }
  },
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
    "round": 299
  }
}
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
        "round": 299
      }
    }
  },
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
    "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
    "round": 299
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
      "caller_nonce": 299,
      "contract_id": "ct_2MXQevoiQXnJCjS5B5R6X9HsnYnnofiLnq6BuQXhk6GpQYRc12",
      "gas_price": 1,
      "gas_used": 276,
      "height": 299,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_/8CwV/U="
    }
  },
  "version": 1
}
```
