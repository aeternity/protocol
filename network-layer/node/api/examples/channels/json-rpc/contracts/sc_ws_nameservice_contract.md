
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53dKC2lROKtx5QmPzneiW9Udx1TeyqGGDHEs7GHsmolxLh/PEKBes=",
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
  "id": -576460752303421635,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED4RldaXKkObvfTW+YWuuNVqLGqmFL+OCzRMazadl3Le7igWT3dA/Gu+U50AG9BCcsFl2KkRJdiWl0mSF+Az9kGuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3SgtpUTirceUJj853olvVHcdU3sqhhgxxLOxh7JqJcS4fxodt8n"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421635,
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
      "signed_tx": "tx_+JALAfhCuED4RldaXKkObvfTW+YWuuNVqLGqmFL+OCzRMazadl3Le7igWT3dA/Gu+U50AG9BCcsFl2KkRJdiWl0mSF+Az9kGuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3SgtpUTirceUJj853olvVHcdU3sqhhgxxLOxh7JqJcS4fxodt8n",
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
  "id": -576460752303421634,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDDPdi6OkkEjXBMqdnXL+aoPvCmxPEOI0MFYFsi1tA71O8jW/Sn/DgYDVfvdoE1YZLxR7+MmRvd3cHv1ikBBScAuED4RldaXKkObvfTW+YWuuNVqLGqmFL+OCzRMazadl3Le7igWT3dA/Gu+U50AG9BCcsFl2KkRJdiWl0mSF+Az9kGuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3SgtpUTirceUJj853olvVHcdU3sqhhgxxLOxh7JqJcS4fz5vtgr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421634,
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
      "state": "tx_+NILAfiEuEDDPdi6OkkEjXBMqdnXL+aoPvCmxPEOI0MFYFsi1tA71O8jW/Sn/DgYDVfvdoE1YZLxR7+MmRvd3cHv1ikBBScAuED4RldaXKkObvfTW+YWuuNVqLGqmFL+OCzRMazadl3Le7igWT3dA/Gu+U50AG9BCcsFl2KkRJdiWl0mSF+Az9kGuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3SgtpUTirceUJj853olvVHcdU3sqhhgxxLOxh7JqJcS4fz5vtgr"
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
      "state": "tx_+NILAfiEuEDDPdi6OkkEjXBMqdnXL+aoPvCmxPEOI0MFYFsi1tA71O8jW/Sn/DgYDVfvdoE1YZLxR7+MmRvd3cHv1ikBBScAuED4RldaXKkObvfTW+YWuuNVqLGqmFL+OCzRMazadl3Le7igWT3dA/Gu+U50AG9BCcsFl2KkRJdiWl0mSF+Az9kGuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3SgtpUTirceUJj853olvVHcdU3sqhhgxxLOxh7JqJcS4fz5vtgr"
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
    "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
    "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
      "caller_nonce": 117,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 117,
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
        "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
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
        "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
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
    "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
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
        "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
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
    "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53daAj8CFDNEMj+VWS0mjh90+9WwP5LZE2cf0q2xId773pJvbM1PM=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
  "id": -576460752303421633,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED7sW1z4SjLiJKCy1N9R/vwkmRDD2OR4TnmiK2TdB00SCVc2KYuLGcctSbXkK1ZmGjuZpdW6VsE5P4C1EB53EYDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3WgI/AhQzRDI/lVktJo4fdPvVsD+S2RNnH9KtsSHe+96SarL1l+"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421633,
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
      "signed_tx": "tx_+JALAfhCuED7sW1z4SjLiJKCy1N9R/vwkmRDD2OR4TnmiK2TdB00SCVc2KYuLGcctSbXkK1ZmGjuZpdW6VsE5P4C1EB53EYDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3WgI/AhQzRDI/lVktJo4fdPvVsD+S2RNnH9KtsSHe+96SarL1l+",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
  "id": -576460752303421632,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAzS9RfuCuvcmdKEgjXgBRpLHJIxOQhDe8ZebF9cDs9km1tdmAcvn0M0vaKjeq5bFc+LzvBeswN/tDokxyCMW0MuED7sW1z4SjLiJKCy1N9R/vwkmRDD2OR4TnmiK2TdB00SCVc2KYuLGcctSbXkK1ZmGjuZpdW6VsE5P4C1EB53EYDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3WgI/AhQzRDI/lVktJo4fdPvVsD+S2RNnH9KtsSHe+96SaFW+It"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421632,
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
      "state": "tx_+NILAfiEuEAzS9RfuCuvcmdKEgjXgBRpLHJIxOQhDe8ZebF9cDs9km1tdmAcvn0M0vaKjeq5bFc+LzvBeswN/tDokxyCMW0MuED7sW1z4SjLiJKCy1N9R/vwkmRDD2OR4TnmiK2TdB00SCVc2KYuLGcctSbXkK1ZmGjuZpdW6VsE5P4C1EB53EYDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3WgI/AhQzRDI/lVktJo4fdPvVsD+S2RNnH9KtsSHe+96SaFW+It"
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
      "state": "tx_+NILAfiEuEAzS9RfuCuvcmdKEgjXgBRpLHJIxOQhDe8ZebF9cDs9km1tdmAcvn0M0vaKjeq5bFc+LzvBeswN/tDokxyCMW0MuED7sW1z4SjLiJKCy1N9R/vwkmRDD2OR4TnmiK2TdB00SCVc2KYuLGcctSbXkK1ZmGjuZpdW6VsE5P4C1EB53EYDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3WgI/AhQzRDI/lVktJo4fdPvVsD+S2RNnH9KtsSHe+96SaFW+It"
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 117
  }
}
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
        "round": 117
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 117
  }
}
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
        "round": 117
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 117
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
      "caller_nonce": 117,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 117,
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 117
  }
}
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
        "round": 117
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 117
  }
}
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
        "round": 117
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 117
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
      "caller_nonce": 117,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 117,
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
    "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
    "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
      "caller_nonce": 118,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 118,
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
        "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
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
        "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
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
    "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
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
        "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
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
    "block_hash": "kh_2LnwzBzSLRxXtabbcGqE36K89gnXDc3E7rc9oZr1rv8op6RMXW",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53dqCplqx/kmj7WAdiJORhJJulusGOIO6tKbA4GX/tkGgkxyUr/zM=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
  "id": -576460752303421631,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBc/jxSZmjAe+PrbmvLkH3CLzAqj6Kyfid87vXm4VROjcwXa7YXgWYVNLlKzP4zuiIDMEhpPl2YP62KnYdEGlwCuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3agqZasf5Jo+1gHYiTkYSSbpbrBjiDurSmwOBl/7ZBoJMdDdvzQ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421631,
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
      "signed_tx": "tx_+JALAfhCuEBc/jxSZmjAe+PrbmvLkH3CLzAqj6Kyfid87vXm4VROjcwXa7YXgWYVNLlKzP4zuiIDMEhpPl2YP62KnYdEGlwCuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3agqZasf5Jo+1gHYiTkYSSbpbrBjiDurSmwOBl/7ZBoJMdDdvzQ",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
  "id": -576460752303421630,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBc/jxSZmjAe+PrbmvLkH3CLzAqj6Kyfid87vXm4VROjcwXa7YXgWYVNLlKzP4zuiIDMEhpPl2YP62KnYdEGlwCuEC4434OGqI+TBCyM9ZyPwL8Tb1fP19a7TWuVz/wpgvxjSgHUQtHU1xEj9ZDzarL7yAOsQJhlXly6YiS6SFexnANuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3agqZasf5Jo+1gHYiTkYSSbpbrBjiDurSmwOBl/7ZBoJMf56IbS"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421630,
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
      "state": "tx_+NILAfiEuEBc/jxSZmjAe+PrbmvLkH3CLzAqj6Kyfid87vXm4VROjcwXa7YXgWYVNLlKzP4zuiIDMEhpPl2YP62KnYdEGlwCuEC4434OGqI+TBCyM9ZyPwL8Tb1fP19a7TWuVz/wpgvxjSgHUQtHU1xEj9ZDzarL7yAOsQJhlXly6YiS6SFexnANuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3agqZasf5Jo+1gHYiTkYSSbpbrBjiDurSmwOBl/7ZBoJMf56IbS"
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
      "state": "tx_+NILAfiEuEBc/jxSZmjAe+PrbmvLkH3CLzAqj6Kyfid87vXm4VROjcwXa7YXgWYVNLlKzP4zuiIDMEhpPl2YP62KnYdEGlwCuEC4434OGqI+TBCyM9ZyPwL8Tb1fP19a7TWuVz/wpgvxjSgHUQtHU1xEj9ZDzarL7yAOsQJhlXly6YiS6SFexnANuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3agqZasf5Jo+1gHYiTkYSSbpbrBjiDurSmwOBl/7ZBoJMf56IbS"
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 118
  }
}
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
        "round": 118
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 118
  }
}
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
        "round": 118
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 118
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
      "caller_nonce": 118,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 118,
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 118
  }
}
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
        "round": 118
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 118
  }
}
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
        "round": 118
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 118
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
      "caller_nonce": 118,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 118,
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
      "caller_nonce": 119,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 119,
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53d6BGjaSjRPGkGfu2uoAVZX5p8+KlSpPCwviYB6MhJlJqrjs4Gzk=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
  "id": -576460752303421629,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAmqrvA5gGVXp0NpWD0tHo4qeu8SsLw0J1+h0dUOBL9YWjhD5vy1G5oalkqOTlQY7WGI4iuDVOqG66dD0UOlisIuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3egRo2ko0TxpBn7trqAFWV+afPipUqTwsL4mAejISZSaq62/V7p"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421629,
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
      "signed_tx": "tx_+JALAfhCuEAmqrvA5gGVXp0NpWD0tHo4qeu8SsLw0J1+h0dUOBL9YWjhD5vy1G5oalkqOTlQY7WGI4iuDVOqG66dD0UOlisIuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3egRo2ko0TxpBn7trqAFWV+afPipUqTwsL4mAejISZSaq62/V7p",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
  "id": -576460752303421628,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAmqrvA5gGVXp0NpWD0tHo4qeu8SsLw0J1+h0dUOBL9YWjhD5vy1G5oalkqOTlQY7WGI4iuDVOqG66dD0UOlisIuED6phPEuu6j9SOn6kBeKMi+8jwAsPQOh5umEL6s+39Xucic3r5Ia+QGto75Bh9OLPIAwTrHOZlm8ATGrPKvS0YJuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3egRo2ko0TxpBn7trqAFWV+afPipUqTwsL4mAejISZSaq4gcSFE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421628,
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
      "state": "tx_+NILAfiEuEAmqrvA5gGVXp0NpWD0tHo4qeu8SsLw0J1+h0dUOBL9YWjhD5vy1G5oalkqOTlQY7WGI4iuDVOqG66dD0UOlisIuED6phPEuu6j9SOn6kBeKMi+8jwAsPQOh5umEL6s+39Xucic3r5Ia+QGto75Bh9OLPIAwTrHOZlm8ATGrPKvS0YJuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3egRo2ko0TxpBn7trqAFWV+afPipUqTwsL4mAejISZSaq4gcSFE"
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
      "state": "tx_+NILAfiEuEAmqrvA5gGVXp0NpWD0tHo4qeu8SsLw0J1+h0dUOBL9YWjhD5vy1G5oalkqOTlQY7WGI4iuDVOqG66dD0UOlisIuED6phPEuu6j9SOn6kBeKMi+8jwAsPQOh5umEL6s+39Xucic3r5Ia+QGto75Bh9OLPIAwTrHOZlm8ATGrPKvS0YJuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3egRo2ko0TxpBn7trqAFWV+afPipUqTwsL4mAejISZSaq4gcSFE"
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 119
  }
}
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
        "round": 119
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 119
  }
}
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
        "round": 119
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 119
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
      "caller_nonce": 119,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 119,
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 119
  }
}
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
        "round": 119
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 119
  }
}
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
        "round": 119
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 119
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
      "caller_nonce": 119,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 119,
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
      "caller_nonce": 120,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 120,
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53eKAQR9oZX57H58PZrCZXmD9LPbKK71UvTgIh9Dm636KY7pfQTj4=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
  "id": -576460752303421627,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAFmmKKMWs0UyxnC4Dg6UTKLrXQMMd8Xh82h09d7+qJ1ZRFv6XQCuDPAYdnkXDdN/M9t6Wc2648S9vRLhU2Ti0LuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3igEEfaGV+ex+fD2awmV5g/Sz2yiu9VL04CIfQ5ut+imO4E4XzE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421627,
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
      "signed_tx": "tx_+JALAfhCuEAFmmKKMWs0UyxnC4Dg6UTKLrXQMMd8Xh82h09d7+qJ1ZRFv6XQCuDPAYdnkXDdN/M9t6Wc2648S9vRLhU2Ti0LuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3igEEfaGV+ex+fD2awmV5g/Sz2yiu9VL04CIfQ5ut+imO4E4XzE",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjlhY2NvdW50X3B1Ymtlee3Xmik=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
  "id": -576460752303421626,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAFmmKKMWs0UyxnC4Dg6UTKLrXQMMd8Xh82h09d7+qJ1ZRFv6XQCuDPAYdnkXDdN/M9t6Wc2648S9vRLhU2Ti0LuEDbD+tBKW2mvY7TSdLFIMTSylLy5/SOkG8Zu+9b9rtCN2lbpDd6Hj2+OHs36wSuHZAPn86y4N7eHlkThEW99x8PuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3igEEfaGV+ex+fD2awmV5g/Sz2yiu9VL04CIfQ5ut+imO41+I2O"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421626,
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
      "state": "tx_+NILAfiEuEAFmmKKMWs0UyxnC4Dg6UTKLrXQMMd8Xh82h09d7+qJ1ZRFv6XQCuDPAYdnkXDdN/M9t6Wc2648S9vRLhU2Ti0LuEDbD+tBKW2mvY7TSdLFIMTSylLy5/SOkG8Zu+9b9rtCN2lbpDd6Hj2+OHs36wSuHZAPn86y4N7eHlkThEW99x8PuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3igEEfaGV+ex+fD2awmV5g/Sz2yiu9VL04CIfQ5ut+imO41+I2O"
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
      "state": "tx_+NILAfiEuEAFmmKKMWs0UyxnC4Dg6UTKLrXQMMd8Xh82h09d7+qJ1ZRFv6XQCuDPAYdnkXDdN/M9t6Wc2648S9vRLhU2Ti0LuEDbD+tBKW2mvY7TSdLFIMTSylLy5/SOkG8Zu+9b9rtCN2lbpDd6Hj2+OHs36wSuHZAPn86y4N7eHlkThEW99x8PuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3igEEfaGV+ex+fD2awmV5g/Sz2yiu9VL04CIfQ5ut+imO41+I2O"
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 120
  }
}
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
        "round": 120
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 120
  }
}
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
        "round": 120
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 120
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
      "caller_nonce": 120,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 120,
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 120
  }
}
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
        "round": 120
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 120
  }
}
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
        "round": 120
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 120
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
      "caller_nonce": 120,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 120,
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
      "caller_nonce": 121,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 121,
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53eaBNuQjFJqV1WEcSsQnCqw70wmEVK1sEi+Hfs0gnL87cR7bB6qk=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
  "id": -576460752303421625,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDLipDfci1wfxYLQBJ/RO6g0DODRqK/jkAETI3D/plojnX+5/r4J8ykUF3R+uzKgHXQ6S7j0Lr39D/cdLF+zv4AuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3mgTbkIxSaldVhHErEJwqsO9MJhFStbBIvh37NIJy/O3Ec4LZXd"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421625,
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
      "signed_tx": "tx_+JALAfhCuEDLipDfci1wfxYLQBJ/RO6g0DODRqK/jkAETI3D/plojnX+5/r4J8ykUF3R+uzKgHXQ6S7j0Lr39D/cdLF+zv4AuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3mgTbkIxSaldVhHErEJwqsO9MJhFStbBIvh37NIJy/O3Ec4LZXd",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
  "id": -576460752303421624,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBDbp/KFbeVW7kXTZk1aVARxYHgA+3M6EvkIJoSQkFig2Yr0fN+cpiZUVLpWoMiNkgjMfPncze3gvbaTIR8QGYFuEDLipDfci1wfxYLQBJ/RO6g0DODRqK/jkAETI3D/plojnX+5/r4J8ykUF3R+uzKgHXQ6S7j0Lr39D/cdLF+zv4AuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3mgTbkIxSaldVhHErEJwqsO9MJhFStbBIvh37NIJy/O3EeAM+2Q"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421624,
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
      "state": "tx_+NILAfiEuEBDbp/KFbeVW7kXTZk1aVARxYHgA+3M6EvkIJoSQkFig2Yr0fN+cpiZUVLpWoMiNkgjMfPncze3gvbaTIR8QGYFuEDLipDfci1wfxYLQBJ/RO6g0DODRqK/jkAETI3D/plojnX+5/r4J8ykUF3R+uzKgHXQ6S7j0Lr39D/cdLF+zv4AuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3mgTbkIxSaldVhHErEJwqsO9MJhFStbBIvh37NIJy/O3EeAM+2Q"
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
      "state": "tx_+NILAfiEuEBDbp/KFbeVW7kXTZk1aVARxYHgA+3M6EvkIJoSQkFig2Yr0fN+cpiZUVLpWoMiNkgjMfPncze3gvbaTIR8QGYFuEDLipDfci1wfxYLQBJ/RO6g0DODRqK/jkAETI3D/plojnX+5/r4J8ykUF3R+uzKgHXQ6S7j0Lr39D/cdLF+zv4AuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3mgTbkIxSaldVhHErEJwqsO9MJhFStbBIvh37NIJy/O3EeAM+2Q"
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 121
  }
}
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
        "round": 121
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 121
  }
}
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
        "round": 121
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 121
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
      "caller_nonce": 121,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 121,
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 121
  }
}
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
        "round": 121
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 121
  }
}
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
        "round": 121
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 121
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
      "caller_nonce": 121,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 121,
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
      "caller_nonce": 122,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 122,
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53eqBPDpFhxP19HL+BcWrcp2V5GXnSickd39akCMCuHY2M/SrUkv0=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
  "id": -576460752303421623,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDwTwZPXXyikWKk/T3n7L5c6EZSm2qhzhar4YWkCszT/8LLDcSmv5cxYvYDgo71k+y7RWMIxvDrkAEZXYv+2J0IuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3qgTw6RYcT9fRy/gXFq3KdleRl50onJHd/WpAjArh2NjP28Gpbv"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421623,
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
      "signed_tx": "tx_+JALAfhCuEDwTwZPXXyikWKk/T3n7L5c6EZSm2qhzhar4YWkCszT/8LLDcSmv5cxYvYDgo71k+y7RWMIxvDrkAEZXYv+2J0IuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3qgTw6RYcT9fRy/gXFq3KdleRl50onJHd/WpAjArh2NjP28Gpbv",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbhlvcmFjbGWOBx0/",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
  "id": -576460752303421622,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECSfGbt/JvT6lMYhEBggysrBgC3+eAD83nnBaA8v6V1hyV+clCzDgzFJDe/oi6d31/g4227wbmQiH6DR9kBeoMCuEDwTwZPXXyikWKk/T3n7L5c6EZSm2qhzhar4YWkCszT/8LLDcSmv5cxYvYDgo71k+y7RWMIxvDrkAEZXYv+2J0IuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3qgTw6RYcT9fRy/gXFq3KdleRl50onJHd/WpAjArh2NjP2ZTj8A"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421622,
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
      "state": "tx_+NILAfiEuECSfGbt/JvT6lMYhEBggysrBgC3+eAD83nnBaA8v6V1hyV+clCzDgzFJDe/oi6d31/g4227wbmQiH6DR9kBeoMCuEDwTwZPXXyikWKk/T3n7L5c6EZSm2qhzhar4YWkCszT/8LLDcSmv5cxYvYDgo71k+y7RWMIxvDrkAEZXYv+2J0IuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3qgTw6RYcT9fRy/gXFq3KdleRl50onJHd/WpAjArh2NjP2ZTj8A"
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
      "state": "tx_+NILAfiEuECSfGbt/JvT6lMYhEBggysrBgC3+eAD83nnBaA8v6V1hyV+clCzDgzFJDe/oi6d31/g4227wbmQiH6DR9kBeoMCuEDwTwZPXXyikWKk/T3n7L5c6EZSm2qhzhar4YWkCszT/8LLDcSmv5cxYvYDgo71k+y7RWMIxvDrkAEZXYv+2J0IuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3qgTw6RYcT9fRy/gXFq3KdleRl50onJHd/WpAjArh2NjP2ZTj8A"
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 122
  }
}
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
        "round": 122
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 122
  }
}
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
        "round": 122
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 122
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
      "caller_nonce": 122,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 122,
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 122
  }
}
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
        "round": 122
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 122
  }
}
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
        "round": 122
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 122
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
      "caller_nonce": 122,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 122,
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
      "caller_nonce": 123,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 123,
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53e6AkFDxNwHX6SxafR/mgcJMYGvJTmEU55kAMW6xvTzN3TcVGYmA=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
  "id": -576460752303421621,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDgLgSQD5w1E95OYpWJW8Qfzws/mc9NCsPh2EjdVDw89oR9wbzn7rCod4j3A0QcGVDvp7PKOPDPoBPb1+3m1pcLuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3ugJBQ8TcB1+ksWn0f5oHCTGBryU5hFOeZADFusb08zd0251yX/"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421621,
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
      "signed_tx": "tx_+JALAfhCuEDgLgSQD5w1E95OYpWJW8Qfzws/mc9NCsPh2EjdVDw89oR9wbzn7rCod4j3A0QcGVDvp7PKOPDPoBPb1+3m1pcLuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3ugJBQ8TcB1+ksWn0f5oHCTGBryU5hFOeZADFusb08zd0251yX/",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
  "id": -576460752303421620,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBC8T0S8HaFe58ingeyHJOQhSh2+rPl2AVOn85BEEWL2m1yJAvZh3V3KzkY7Evk8Iz/QKeFL3Sr2f54K7reh3MNuEDgLgSQD5w1E95OYpWJW8Qfzws/mc9NCsPh2EjdVDw89oR9wbzn7rCod4j3A0QcGVDvp7PKOPDPoBPb1+3m1pcLuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3ugJBQ8TcB1+ksWn0f5oHCTGBryU5hFOeZADFusb08zd02vDEKK"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421620,
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
      "state": "tx_+NILAfiEuEBC8T0S8HaFe58ingeyHJOQhSh2+rPl2AVOn85BEEWL2m1yJAvZh3V3KzkY7Evk8Iz/QKeFL3Sr2f54K7reh3MNuEDgLgSQD5w1E95OYpWJW8Qfzws/mc9NCsPh2EjdVDw89oR9wbzn7rCod4j3A0QcGVDvp7PKOPDPoBPb1+3m1pcLuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3ugJBQ8TcB1+ksWn0f5oHCTGBryU5hFOeZADFusb08zd02vDEKK"
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
      "state": "tx_+NILAfiEuEBC8T0S8HaFe58ingeyHJOQhSh2+rPl2AVOn85BEEWL2m1yJAvZh3V3KzkY7Evk8Iz/QKeFL3Sr2f54K7reh3MNuEDgLgSQD5w1E95OYpWJW8Qfzws/mc9NCsPh2EjdVDw89oR9wbzn7rCod4j3A0QcGVDvp7PKOPDPoBPb1+3m1pcLuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3ugJBQ8TcB1+ksWn0f5oHCTGBryU5hFOeZADFusb08zd02vDEKK"
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 123
  }
}
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
        "round": 123
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 123
  }
}
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
        "round": 123
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 123
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
      "caller_nonce": 123,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 123,
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 123
  }
}
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
        "round": 123
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 123
  }
}
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
        "round": 123
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 123
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
      "caller_nonce": 123,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 123,
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
      "caller_nonce": 124,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 124,
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53fKBnigSm+O1TJu0ydLmbuuexEz3zVFeXY/iRYnEAEzYqItDyPPo=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
  "id": -576460752303421619,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAHw747IdxtX+ntPi7efCw+4nIlSNZfnnduhpsMb0r56bR2EoHi+FJElBSOcRiWfKHjsQsKKCpwOx2pa1+fGhcKuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3ygZ4oEpvjtUybtMnS5m7rnsRM981RXl2P4kWJxABM2KiK5x+0j"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421619,
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
      "signed_tx": "tx_+JALAfhCuEAHw747IdxtX+ntPi7efCw+4nIlSNZfnnduhpsMb0r56bR2EoHi+FJElBSOcRiWfKHjsQsKKCpwOx2pa1+fGhcKuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3ygZ4oEpvjtUybtMnS5m7rnsRM981RXl2P4kWJxABM2KiK5x+0j",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbjl1bmV4cGVjdGVkX2tleazlUXM=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
  "id": -576460752303421618,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAHw747IdxtX+ntPi7efCw+4nIlSNZfnnduhpsMb0r56bR2EoHi+FJElBSOcRiWfKHjsQsKKCpwOx2pa1+fGhcKuEBsULo1a9l4DmuPte0Hf0otsslfDLXMyvPsNIe+YNJyuFIozVMa5erny2bnUp+3FW/ArmWsgGIp+06ZmM5pEx0KuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3ygZ4oEpvjtUybtMnS5m7rnsRM981RXl2P4kWJxABM2KiLQ1twb"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421618,
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
      "state": "tx_+NILAfiEuEAHw747IdxtX+ntPi7efCw+4nIlSNZfnnduhpsMb0r56bR2EoHi+FJElBSOcRiWfKHjsQsKKCpwOx2pa1+fGhcKuEBsULo1a9l4DmuPte0Hf0otsslfDLXMyvPsNIe+YNJyuFIozVMa5erny2bnUp+3FW/ArmWsgGIp+06ZmM5pEx0KuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3ygZ4oEpvjtUybtMnS5m7rnsRM981RXl2P4kWJxABM2KiLQ1twb"
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
      "state": "tx_+NILAfiEuEAHw747IdxtX+ntPi7efCw+4nIlSNZfnnduhpsMb0r56bR2EoHi+FJElBSOcRiWfKHjsQsKKCpwOx2pa1+fGhcKuEBsULo1a9l4DmuPte0Hf0otsslfDLXMyvPsNIe+YNJyuFIozVMa5erny2bnUp+3FW/ArmWsgGIp+06ZmM5pEx0KuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3ygZ4oEpvjtUybtMnS5m7rnsRM981RXl2P4kWJxABM2KiLQ1twb"
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 124
  }
}
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
        "round": 124
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 124
  }
}
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
        "round": 124
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 124
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
      "caller_nonce": 124,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 124,
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 124
  }
}
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
        "round": 124
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 124
  }
}
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
        "round": 124
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 124
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
      "caller_nonce": 124,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 124,
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
      "caller_nonce": 125,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 125,
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53faC4ybMqdQ79BpwbjXBrDVn03nNIHczeUnJBuJfDYLnax5TtWSQ=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
  "id": -576460752303421617,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAmnYsOp7eaPLfBOpDNXs5so/KMbiE87BmbdBGOtdRdCMspKke/EM7XVqirgQ/QWHPhpkktHRo0xxfZacuvtOcEuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud32guMmzKnUO/QacG41waw1Z9N5zSB3M3lJyQbiXw2C52sc2I1ji"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421617,
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
      "signed_tx": "tx_+JALAfhCuEAmnYsOp7eaPLfBOpDNXs5so/KMbiE87BmbdBGOtdRdCMspKke/EM7XVqirgQ/QWHPhpkktHRo0xxfZacuvtOcEuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud32guMmzKnUO/QacG41waw1Z9N5zSB3M3lJyQbiXw2C52sc2I1ji",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
  "id": -576460752303421616,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAmnYsOp7eaPLfBOpDNXs5so/KMbiE87BmbdBGOtdRdCMspKke/EM7XVqirgQ/QWHPhpkktHRo0xxfZacuvtOcEuEBEzxJ3fkzFRxD33PrsVpGdh5E5l9RLQJI0tOsV/VeUnO25sGeMvuzsPMPV4aHq0T2ZWx9nvCR/f3WoMbkBoLQDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud32guMmzKnUO/QacG41waw1Z9N5zSB3M3lJyQbiXw2C52seP1mpl"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421616,
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
      "state": "tx_+NILAfiEuEAmnYsOp7eaPLfBOpDNXs5so/KMbiE87BmbdBGOtdRdCMspKke/EM7XVqirgQ/QWHPhpkktHRo0xxfZacuvtOcEuEBEzxJ3fkzFRxD33PrsVpGdh5E5l9RLQJI0tOsV/VeUnO25sGeMvuzsPMPV4aHq0T2ZWx9nvCR/f3WoMbkBoLQDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud32guMmzKnUO/QacG41waw1Z9N5zSB3M3lJyQbiXw2C52seP1mpl"
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
      "state": "tx_+NILAfiEuEAmnYsOp7eaPLfBOpDNXs5so/KMbiE87BmbdBGOtdRdCMspKke/EM7XVqirgQ/QWHPhpkktHRo0xxfZacuvtOcEuEBEzxJ3fkzFRxD33PrsVpGdh5E5l9RLQJI0tOsV/VeUnO25sGeMvuzsPMPV4aHq0T2ZWx9nvCR/f3WoMbkBoLQDuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud32guMmzKnUO/QacG41waw1Z9N5zSB3M3lJyQbiXw2C52seP1mpl"
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 125
  }
}
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
        "round": 125
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 125
  }
}
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
        "round": 125
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 125
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
      "caller_nonce": 125,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 125,
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 125
  }
}
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
        "round": 125
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 125
  }
}
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
        "round": 125
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 125
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
      "caller_nonce": 125,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 125,
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
      "caller_nonce": 126,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 126,
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
  }
}
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
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
        "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
        "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
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
    "block_hash": "kh_22chuKNQ7HbksdsvcVhtPMMExBg465VeoX3jf2Cv6EFmvNaQzS",
    "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb"
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53fqB32ufplTkVaiJ8BKYci4m88h3P5L1YntAzXRPdX2Mbi+wTPP8=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
  "id": -576460752303421615,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBG7EzpxzrrZYoNW1zyKMs2kJDDTpOvHu9mH0SSnTVGImzmloE5C6EvqakV4YZ+R/hQm1+5hm9LkNceDPKUW9QMuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud36gd9rn6ZU5FWoifASmHIuJvPIdz+S9WJ7QM10T3V9jG4ujKaJZ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421615,
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
      "signed_tx": "tx_+JALAfhCuEBG7EzpxzrrZYoNW1zyKMs2kJDDTpOvHu9mH0SSnTVGImzmloE5C6EvqakV4YZ+R/hQm1+5hm9LkNceDPKUW9QMuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud36gd9rn6ZU5FWoifASmHIuJvPIdz+S9WJ7QM10T3V9jG4ujKaJZ",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1S3ZCeFYzY2NrY0pwSy5jaGFpbi1taXNzaW5nX2tleVT5gIk=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
  "id": -576460752303421614,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBG7EzpxzrrZYoNW1zyKMs2kJDDTpOvHu9mH0SSnTVGImzmloE5C6EvqakV4YZ+R/hQm1+5hm9LkNceDPKUW9QMuECNUsR+j12xtKKeAVFDAbWFmxaMKYeHw0Auf0Y583kTkteNFItbmjMDjDdDNGtg3UfnCYNO0kvcy4L0sSYdNRAGuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud36gd9rn6ZU5FWoifASmHIuJvPIdz+S9WJ7QM10T3V9jG4tz5odi"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421614,
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
      "state": "tx_+NILAfiEuEBG7EzpxzrrZYoNW1zyKMs2kJDDTpOvHu9mH0SSnTVGImzmloE5C6EvqakV4YZ+R/hQm1+5hm9LkNceDPKUW9QMuECNUsR+j12xtKKeAVFDAbWFmxaMKYeHw0Auf0Y583kTkteNFItbmjMDjDdDNGtg3UfnCYNO0kvcy4L0sSYdNRAGuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud36gd9rn6ZU5FWoifASmHIuJvPIdz+S9WJ7QM10T3V9jG4tz5odi"
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
      "state": "tx_+NILAfiEuEBG7EzpxzrrZYoNW1zyKMs2kJDDTpOvHu9mH0SSnTVGImzmloE5C6EvqakV4YZ+R/hQm1+5hm9LkNceDPKUW9QMuECNUsR+j12xtKKeAVFDAbWFmxaMKYeHw0Auf0Y583kTkteNFItbmjMDjDdDNGtg3UfnCYNO0kvcy4L0sSYdNRAGuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud36gd9rn6ZU5FWoifASmHIuJvPIdz+S9WJ7QM10T3V9jG4tz5odi"
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 126
  }
}
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
        "round": 126
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 126
  }
}
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
        "round": 126
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 126
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
      "caller_nonce": 126,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 126,
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 126
  }
}
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
        "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
        "round": 126
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 126
  }
}
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
        "round": 126
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
    "round": 126
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
      "caller_nonce": 126,
      "contract_id": "ct_2gJGgYjC8JhvpQuU8LcbCPGrZZb7Quv4C7hhJiFGUTrseDDQkb",
      "gas_price": 1,
      "gas_used": 122,
      "height": 126,
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53f6AuBiAqp8KUkq/QHCmZ/m1D+JS8gNyGT3FPOfab+DB0lm2XmXA=",
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
  "id": -576460752303421613,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBnNEJAShM3NgQYSuJc5VKTRmsee6+4vKja0IpiI+ov2GDpChcDIPHJ/kuaqsPu4UU1p2/QL2JIdnlMwR/ZUsQEuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3+gLgYgKqfClJKv0Bwpmf5tQ/iUvIDchk9xTzn2m/gwdJbFwtyk"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421613,
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
      "signed_tx": "tx_+JALAfhCuEBnNEJAShM3NgQYSuJc5VKTRmsee6+4vKja0IpiI+ov2GDpChcDIPHJ/kuaqsPu4UU1p2/QL2JIdnlMwR/ZUsQEuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3+gLgYgKqfClJKv0Bwpmf5tQ/iUvIDchk9xTzn2m/gwdJbFwtyk",
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
  "id": -576460752303421612,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAOlRDagOO70G/h7WNtR09IRsn1LPAgmtv82dE//HoqIrmGAmJhe02l/hO6HqBCque0Tbc8WGNdkX4WwUiFOpgJuEBnNEJAShM3NgQYSuJc5VKTRmsee6+4vKja0IpiI+ov2GDpChcDIPHJ/kuaqsPu4UU1p2/QL2JIdnlMwR/ZUsQEuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3+gLgYgKqfClJKv0Bwpmf5tQ/iUvIDchk9xTzn2m/gwdJagW4sL"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421612,
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
      "state": "tx_+NILAfiEuEAOlRDagOO70G/h7WNtR09IRsn1LPAgmtv82dE//HoqIrmGAmJhe02l/hO6HqBCque0Tbc8WGNdkX4WwUiFOpgJuEBnNEJAShM3NgQYSuJc5VKTRmsee6+4vKja0IpiI+ov2GDpChcDIPHJ/kuaqsPu4UU1p2/QL2JIdnlMwR/ZUsQEuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3+gLgYgKqfClJKv0Bwpmf5tQ/iUvIDchk9xTzn2m/gwdJagW4sL"
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
      "state": "tx_+NILAfiEuEAOlRDagOO70G/h7WNtR09IRsn1LPAgmtv82dE//HoqIrmGAmJhe02l/hO6HqBCque0Tbc8WGNdkX4WwUiFOpgJuEBnNEJAShM3NgQYSuJc5VKTRmsee6+4vKja0IpiI+ov2GDpChcDIPHJ/kuaqsPu4UU1p2/QL2JIdnlMwR/ZUsQEuEj4RjkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud3+gLgYgKqfClJKv0Bwpmf5tQ/iUvIDchk9xTzn2m/gwdJagW4sL"
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
    "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
    "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
    "call_data": "ABCDEFG",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
      "caller_nonce": 128,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 128,
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
        "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
        "call_data": "ABCDEFG",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
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
        "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
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
    "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
    "call_data": "ABCDEFG",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
        "call_data": "ABCDEFG",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
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
        "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
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
    "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gYCgwk5zwVXYD8wxxyX6Q2UWRSE1MwtKauEoYTWMsYXNRoSZ7cbx",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
  "id": -576460752303421611,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEAevTrQxpt6fBvp8+AyR7Sl275cD1X3FC0RNELO26Pw79WorTFz4oBWtrI5wVLmihiG4fhPIL00zw5/UJipdVcGuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GAoMJOc8FV2A/MMccl+kNlFkUhNTMLSmrhKGE1jLGFzUaE9hInwg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421611,
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
      "signed_tx": "tx_+JELAfhCuEAevTrQxpt6fBvp8+AyR7Sl275cD1X3FC0RNELO26Pw79WorTFz4oBWtrI5wVLmihiG4fhPIL00zw5/UJipdVcGuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GAoMJOc8FV2A/MMccl+kNlFkUhNTMLSmrhKGE1jLGFzUaE9hInwg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
  "id": -576460752303421610,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAevTrQxpt6fBvp8+AyR7Sl275cD1X3FC0RNELO26Pw79WorTFz4oBWtrI5wVLmihiG4fhPIL00zw5/UJipdVcGuEC9lP9EvDlhI8Fk1ApHbQJ1zEwlVT22d5tLwUcq4D4xcpt1aC7fEKllqB04vyF4iDqr5nF+kUVCXq8IS4vY8ZUJuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GAoMJOc8FV2A/MMccl+kNlFkUhNTMLSmrhKGE1jLGFzUaEP0NKSQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421610,
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
      "state": "tx_+NMLAfiEuEAevTrQxpt6fBvp8+AyR7Sl275cD1X3FC0RNELO26Pw79WorTFz4oBWtrI5wVLmihiG4fhPIL00zw5/UJipdVcGuEC9lP9EvDlhI8Fk1ApHbQJ1zEwlVT22d5tLwUcq4D4xcpt1aC7fEKllqB04vyF4iDqr5nF+kUVCXq8IS4vY8ZUJuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GAoMJOc8FV2A/MMccl+kNlFkUhNTMLSmrhKGE1jLGFzUaEP0NKSQ=="
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
      "state": "tx_+NMLAfiEuEAevTrQxpt6fBvp8+AyR7Sl275cD1X3FC0RNELO26Pw79WorTFz4oBWtrI5wVLmihiG4fhPIL00zw5/UJipdVcGuEC9lP9EvDlhI8Fk1ApHbQJ1zEwlVT22d5tLwUcq4D4xcpt1aC7fEKllqB04vyF4iDqr5nF+kUVCXq8IS4vY8ZUJuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GAoMJOc8FV2A/MMccl+kNlFkUhNTMLSmrhKGE1jLGFzUaEP0NKSQ=="
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 128
  }
}
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
        "round": 128
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 128
  }
}
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
        "round": 128
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 128
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
      "caller_nonce": 128,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 128,
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 128
  }
}
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
        "round": 128
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 128
  }
}
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
        "round": 128
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 128
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
      "caller_nonce": 128,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 128,
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
    "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
    "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
    "call_data": "ABCDEFG",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
      "caller_nonce": 129,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 129,
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
        "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
        "call_data": "ABCDEFG",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
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
        "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
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
    "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
    "call_data": "ABCDEFG",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
        "call_data": "ABCDEFG",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
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
        "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
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
    "block_hash": "kh_63zEU7VVoExfQsZnkvbhmQxUi4BdXhNdx83j9NzzdJRNiBZ2o",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gYGg/9GIqLwPDmY+wH8+hJduGbr3l8p0pLfeBi6dAOkwKOqYoW7V",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
  "id": -576460752303421609,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuECcByVYYKSJdbia9wKCva4rkKTmYT//P6mH8w2dBFPJ6kyGs2/U5IsblLiboTX5RGW5sirC1ntOSLm6cubDwFMEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GBoP/RiKi8Dw5mPsB/PoSXbhm695fKdKS33gYunQDpMCjq8bK+Yg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421609,
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
      "signed_tx": "tx_+JELAfhCuECcByVYYKSJdbia9wKCva4rkKTmYT//P6mH8w2dBFPJ6kyGs2/U5IsblLiboTX5RGW5sirC1ntOSLm6cubDwFMEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GBoP/RiKi8Dw5mPsB/PoSXbhm695fKdKS33gYunQDpMCjq8bK+Yg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
  "id": -576460752303421608,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAwftV6LQCe5RU40RY/H3FaC5/TLhHdlqRibpbAZ5g5iQEUi3jFmQdFUQNLgSXqMYL/fv78mJX2oGZbyKOVUjoKuECcByVYYKSJdbia9wKCva4rkKTmYT//P6mH8w2dBFPJ6kyGs2/U5IsblLiboTX5RGW5sirC1ntOSLm6cubDwFMEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GBoP/RiKi8Dw5mPsB/PoSXbhm695fKdKS33gYunQDpMCjqqKVR+g=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421608,
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
      "state": "tx_+NMLAfiEuEAwftV6LQCe5RU40RY/H3FaC5/TLhHdlqRibpbAZ5g5iQEUi3jFmQdFUQNLgSXqMYL/fv78mJX2oGZbyKOVUjoKuECcByVYYKSJdbia9wKCva4rkKTmYT//P6mH8w2dBFPJ6kyGs2/U5IsblLiboTX5RGW5sirC1ntOSLm6cubDwFMEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GBoP/RiKi8Dw5mPsB/PoSXbhm695fKdKS33gYunQDpMCjqqKVR+g=="
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
      "state": "tx_+NMLAfiEuEAwftV6LQCe5RU40RY/H3FaC5/TLhHdlqRibpbAZ5g5iQEUi3jFmQdFUQNLgSXqMYL/fv78mJX2oGZbyKOVUjoKuECcByVYYKSJdbia9wKCva4rkKTmYT//P6mH8w2dBFPJ6kyGs2/U5IsblLiboTX5RGW5sirC1ntOSLm6cubDwFMEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GBoP/RiKi8Dw5mPsB/PoSXbhm695fKdKS33gYunQDpMCjqqKVR+g=="
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 129
  }
}
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
        "round": 129
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 129
  }
}
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
        "round": 129
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 129
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
      "caller_nonce": 129,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 129,
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 129
  }
}
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
        "round": 129
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 129
  }
}
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
        "round": 129
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 129
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
      "caller_nonce": 129,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 129,
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
      "caller_nonce": 130,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 130,
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gYKgM41grCTZOpL9S91BvsYZZV9wouNcsD6dM/TV85sjz7dDl/2q",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
  "id": -576460752303421607,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEDga7/SY+zyZsmuv7po/OZQ+m9ldLfzGHz52hs0xcuwO+RYhsmWLJyGPLheYJcE6a+RDeYBz4p7a7n3feQOsEACuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GCoDONYKwk2TqS/UvdQb7GGWVfcKLjXLA+nTP01fObI8+35ojzLA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421607,
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
      "signed_tx": "tx_+JELAfhCuEDga7/SY+zyZsmuv7po/OZQ+m9ldLfzGHz52hs0xcuwO+RYhsmWLJyGPLheYJcE6a+RDeYBz4p7a7n3feQOsEACuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GCoDONYKwk2TqS/UvdQb7GGWVfcKLjXLA+nTP01fObI8+35ojzLA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
  "id": -576460752303421606,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuECfn+fypAQiT+ohE6gTiS18a1km/CQp2sd/lYSNEsvLECAgxFzizFlzXU+8WOQRUTMWB/aWJL/qGfqrI6mxpiINuEDga7/SY+zyZsmuv7po/OZQ+m9ldLfzGHz52hs0xcuwO+RYhsmWLJyGPLheYJcE6a+RDeYBz4p7a7n3feQOsEACuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GCoDONYKwk2TqS/UvdQb7GGWVfcKLjXLA+nTP01fObI8+3ZxABEA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421606,
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
      "state": "tx_+NMLAfiEuECfn+fypAQiT+ohE6gTiS18a1km/CQp2sd/lYSNEsvLECAgxFzizFlzXU+8WOQRUTMWB/aWJL/qGfqrI6mxpiINuEDga7/SY+zyZsmuv7po/OZQ+m9ldLfzGHz52hs0xcuwO+RYhsmWLJyGPLheYJcE6a+RDeYBz4p7a7n3feQOsEACuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GCoDONYKwk2TqS/UvdQb7GGWVfcKLjXLA+nTP01fObI8+3ZxABEA=="
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
      "state": "tx_+NMLAfiEuECfn+fypAQiT+ohE6gTiS18a1km/CQp2sd/lYSNEsvLECAgxFzizFlzXU+8WOQRUTMWB/aWJL/qGfqrI6mxpiINuEDga7/SY+zyZsmuv7po/OZQ+m9ldLfzGHz52hs0xcuwO+RYhsmWLJyGPLheYJcE6a+RDeYBz4p7a7n3feQOsEACuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GCoDONYKwk2TqS/UvdQb7GGWVfcKLjXLA+nTP01fObI8+3ZxABEA=="
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 130
  }
}
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
        "round": 130
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 130
  }
}
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
        "round": 130
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 130
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
      "caller_nonce": 130,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 130,
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 130
  }
}
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
        "round": 130
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 130
  }
}
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
        "round": 130
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 130
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
      "caller_nonce": 130,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 130,
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
      "caller_nonce": 131,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 131,
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gYOgi0DjIOE9hwE0mW6l/AO8F5YHU6rpFtwpxr3soDzrzqEQFl8K",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
  "id": -576460752303421605,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEDk7oKDH8NEWFHpy6jzUV/IAGcHbL41K++9G2nDn5HbzREeQwkK01L9cf45QJp/+OdnP4BE3UWf97qhmuVQExAHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GDoItA4yDhPYcBNJlupfwDvBeWB1Oq6RbcKca97KA8686hWGZdfw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421605,
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
      "signed_tx": "tx_+JELAfhCuEDk7oKDH8NEWFHpy6jzUV/IAGcHbL41K++9G2nDn5HbzREeQwkK01L9cf45QJp/+OdnP4BE3UWf97qhmuVQExAHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GDoItA4yDhPYcBNJlupfwDvBeWB1Oq6RbcKca97KA8686hWGZdfw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjlhY2NvdW50X3B1YmtleYlkwp4=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
  "id": -576460752303421604,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEC8sIJVdKc1+ELPC1Urs6CpTJNP/AgsIzcVWlBT8bmRi1Y01eQuvq9bUAZ+86FtgES/S/x6dRR+lShiLK+Ks3IBuEDk7oKDH8NEWFHpy6jzUV/IAGcHbL41K++9G2nDn5HbzREeQwkK01L9cf45QJp/+OdnP4BE3UWf97qhmuVQExAHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GDoItA4yDhPYcBNJlupfwDvBeWB1Oq6RbcKca97KA8686hNGXZYg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421604,
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
      "state": "tx_+NMLAfiEuEC8sIJVdKc1+ELPC1Urs6CpTJNP/AgsIzcVWlBT8bmRi1Y01eQuvq9bUAZ+86FtgES/S/x6dRR+lShiLK+Ks3IBuEDk7oKDH8NEWFHpy6jzUV/IAGcHbL41K++9G2nDn5HbzREeQwkK01L9cf45QJp/+OdnP4BE3UWf97qhmuVQExAHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GDoItA4yDhPYcBNJlupfwDvBeWB1Oq6RbcKca97KA8686hNGXZYg=="
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
      "state": "tx_+NMLAfiEuEC8sIJVdKc1+ELPC1Urs6CpTJNP/AgsIzcVWlBT8bmRi1Y01eQuvq9bUAZ+86FtgES/S/x6dRR+lShiLK+Ks3IBuEDk7oKDH8NEWFHpy6jzUV/IAGcHbL41K++9G2nDn5HbzREeQwkK01L9cf45QJp/+OdnP4BE3UWf97qhmuVQExAHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GDoItA4yDhPYcBNJlupfwDvBeWB1Oq6RbcKca97KA8686hNGXZYg=="
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 131
  }
}
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
        "round": 131
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 131
  }
}
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
        "round": 131
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 131
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
      "caller_nonce": 131,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 131,
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 131
  }
}
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
        "round": 131
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 131
  }
}
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
        "round": 131
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 131
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
      "caller_nonce": 131,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 131,
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
      "caller_nonce": 132,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 132,
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gYSgtA2Jv66HEZ08YHuf9Ge8Z3ci++fUZuUwa41/M2FhiKNOreAr",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
  "id": -576460752303421603,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuECC4FwnQ2J+97mUzPHXTDAHhMNB0InS+XiXJcWIdWMIyO+paFwX4cbRzLrdRgGfpSBM8fUwJplPYRY7lkMcWyUDuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GEoLQNib+uhxGdPGB7n/RnvGd3Ivvn1GblMGuNfzNhYYijUeR9+Q=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421603,
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
      "signed_tx": "tx_+JELAfhCuECC4FwnQ2J+97mUzPHXTDAHhMNB0InS+XiXJcWIdWMIyO+paFwX4cbRzLrdRgGfpSBM8fUwJplPYRY7lkMcWyUDuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GEoLQNib+uhxGdPGB7n/RnvGd3Ivvn1GblMGuNfzNhYYijUeR9+Q==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
  "id": -576460752303421602,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuECC4FwnQ2J+97mUzPHXTDAHhMNB0InS+XiXJcWIdWMIyO+paFwX4cbRzLrdRgGfpSBM8fUwJplPYRY7lkMcWyUDuEDX1tjIBYFsnmfDEdbv8lUrr47Bfi+3iwIKsHYrrvOTrdfE3qVtKIAUC1g1tFbxOaUtpEnPttiIz+/Zftwt3g4NuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GEoLQNib+uhxGdPGB7n/RnvGd3Ivvn1GblMGuNfzNhYYijuuceiQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421602,
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
      "state": "tx_+NMLAfiEuECC4FwnQ2J+97mUzPHXTDAHhMNB0InS+XiXJcWIdWMIyO+paFwX4cbRzLrdRgGfpSBM8fUwJplPYRY7lkMcWyUDuEDX1tjIBYFsnmfDEdbv8lUrr47Bfi+3iwIKsHYrrvOTrdfE3qVtKIAUC1g1tFbxOaUtpEnPttiIz+/Zftwt3g4NuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GEoLQNib+uhxGdPGB7n/RnvGd3Ivvn1GblMGuNfzNhYYijuuceiQ=="
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
      "state": "tx_+NMLAfiEuECC4FwnQ2J+97mUzPHXTDAHhMNB0InS+XiXJcWIdWMIyO+paFwX4cbRzLrdRgGfpSBM8fUwJplPYRY7lkMcWyUDuEDX1tjIBYFsnmfDEdbv8lUrr47Bfi+3iwIKsHYrrvOTrdfE3qVtKIAUC1g1tFbxOaUtpEnPttiIz+/Zftwt3g4NuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GEoLQNib+uhxGdPGB7n/RnvGd3Ivvn1GblMGuNfzNhYYijuuceiQ=="
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 132
  }
}
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
        "round": 132
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 132
  }
}
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
        "round": 132
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 132
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
      "caller_nonce": 132,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 132,
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 132
  }
}
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
        "round": 132
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 132
  }
}
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
        "round": 132
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 132
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
      "caller_nonce": 132,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 132,
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
      "caller_nonce": 133,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 133,
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gYWgv/ID66x4kFBoj84C9LinbDmK9Tk8EO32weHSkLS8S+K9HzPk",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
  "id": -576460752303421601,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEBhDHx82ncztD3wpUBpcO62WP1m185Yi2ADGaOJjQb95cQ2B0sEcugbyyxG12P/YrZmL5hhcS4LI4podKnS9QgBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GFoL/yA+useJBQaI/OAvS4p2w5ivU5PBDt9sHh0pC0vEviXavKrg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421601,
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
      "signed_tx": "tx_+JELAfhCuEBhDHx82ncztD3wpUBpcO62WP1m185Yi2ADGaOJjQb95cQ2B0sEcugbyyxG12P/YrZmL5hhcS4LI4podKnS9QgBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GFoL/yA+useJBQaI/OAvS4p2w5ivU5PBDt9sHh0pC0vEviXavKrg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbhlvcmFjbGUYc0Xs",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
  "id": -576460752303421600,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAgQBcwbC6chbxIC9b1ga6R3PL7sOwhGRYR7Ylkl4lg73VJqPUEXBfx55XIhl/miAkFgv9lK7TG+Mjjw4H8CvILuEBhDHx82ncztD3wpUBpcO62WP1m185Yi2ADGaOJjQb95cQ2B0sEcugbyyxG12P/YrZmL5hhcS4LI4podKnS9QgBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GFoL/yA+useJBQaI/OAvS4p2w5ivU5PBDt9sHh0pC0vEviI3SL1g=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421600,
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
      "state": "tx_+NMLAfiEuEAgQBcwbC6chbxIC9b1ga6R3PL7sOwhGRYR7Ylkl4lg73VJqPUEXBfx55XIhl/miAkFgv9lK7TG+Mjjw4H8CvILuEBhDHx82ncztD3wpUBpcO62WP1m185Yi2ADGaOJjQb95cQ2B0sEcugbyyxG12P/YrZmL5hhcS4LI4podKnS9QgBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GFoL/yA+useJBQaI/OAvS4p2w5ivU5PBDt9sHh0pC0vEviI3SL1g=="
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
      "state": "tx_+NMLAfiEuEAgQBcwbC6chbxIC9b1ga6R3PL7sOwhGRYR7Ylkl4lg73VJqPUEXBfx55XIhl/miAkFgv9lK7TG+Mjjw4H8CvILuEBhDHx82ncztD3wpUBpcO62WP1m185Yi2ADGaOJjQb95cQ2B0sEcugbyyxG12P/YrZmL5hhcS4LI4podKnS9QgBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GFoL/yA+useJBQaI/OAvS4p2w5ivU5PBDt9sHh0pC0vEviI3SL1g=="
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 133
  }
}
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
        "round": 133
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 133
  }
}
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
        "round": 133
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 133
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
      "caller_nonce": 133,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 133,
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 133
  }
}
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
        "round": 133
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 133
  }
}
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
        "round": 133
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 133
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
      "caller_nonce": 133,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 133,
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
      "caller_nonce": 134,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 134,
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gYagBPS/UccL/AqZrKZoNzswT0jGmO0KwdOX7sVmu9j6c0MELJEX",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
  "id": -576460752303421599,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuED4pVzfLzoSmPDkIAv6RTSwReTum0l9MdNe/XpX06SrwfqS1a9UbF9E6PAed4F0E+YcnnBNDeLWNxrHPqU4WrkEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GGoAT0v1HHC/wKmaymaDc7ME9IxpjtCsHTl+7FZrvY+nNDx2UjoA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421599,
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
      "signed_tx": "tx_+JELAfhCuED4pVzfLzoSmPDkIAv6RTSwReTum0l9MdNe/XpX06SrwfqS1a9UbF9E6PAed4F0E+YcnnBNDeLWNxrHPqU4WrkEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GGoAT0v1HHC/wKmaymaDc7ME9IxpjtCsHTl+7FZrvY+nNDx2UjoA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
  "id": -576460752303421598,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEBKqw6obAP4lC/SljVtkNDU4TrU7t6EaE4YGuTAjC75IDUQQo4Ej4DVy7NDSrA4LN1BQg8nvOMfS5o6NPL0XngGuED4pVzfLzoSmPDkIAv6RTSwReTum0l9MdNe/XpX06SrwfqS1a9UbF9E6PAed4F0E+YcnnBNDeLWNxrHPqU4WrkEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GGoAT0v1HHC/wKmaymaDc7ME9IxpjtCsHTl+7FZrvY+nNDkTE5OA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421598,
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
      "state": "tx_+NMLAfiEuEBKqw6obAP4lC/SljVtkNDU4TrU7t6EaE4YGuTAjC75IDUQQo4Ej4DVy7NDSrA4LN1BQg8nvOMfS5o6NPL0XngGuED4pVzfLzoSmPDkIAv6RTSwReTum0l9MdNe/XpX06SrwfqS1a9UbF9E6PAed4F0E+YcnnBNDeLWNxrHPqU4WrkEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GGoAT0v1HHC/wKmaymaDc7ME9IxpjtCsHTl+7FZrvY+nNDkTE5OA=="
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
      "state": "tx_+NMLAfiEuEBKqw6obAP4lC/SljVtkNDU4TrU7t6EaE4YGuTAjC75IDUQQo4Ej4DVy7NDSrA4LN1BQg8nvOMfS5o6NPL0XngGuED4pVzfLzoSmPDkIAv6RTSwReTum0l9MdNe/XpX06SrwfqS1a9UbF9E6PAed4F0E+YcnnBNDeLWNxrHPqU4WrkEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GGoAT0v1HHC/wKmaymaDc7ME9IxpjtCsHTl+7FZrvY+nNDkTE5OA=="
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 134
  }
}
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
        "round": 134
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 134
  }
}
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
        "round": 134
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 134
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
      "caller_nonce": 134,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 134,
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 134
  }
}
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
        "round": 134
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 134
  }
}
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
        "round": 134
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 134
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
      "caller_nonce": 134,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 134,
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
      "caller_nonce": 135,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 135,
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gYegyxsCVF0qkrkPEn5f7+rmPTUKUJ8QkbdpJRYVXMO7eVPpwm0D",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
  "id": -576460752303421597,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEBgvfX8OEXFiPBhT1tIQ5DtVhD0ZFVWG2wqoyjrGrqA3sROXPNaSUB7Jb8rWlu8DzOpnmdjZbOMK1Qs9AalIC0DuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GHoMsbAlRdKpK5DxJ+X+/q5j01ClCfEJG3aSUWFVzDu3lTuAvVRg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421597,
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
      "signed_tx": "tx_+JELAfhCuEBgvfX8OEXFiPBhT1tIQ5DtVhD0ZFVWG2wqoyjrGrqA3sROXPNaSUB7Jb8rWlu8DzOpnmdjZbOMK1Qs9AalIC0DuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GHoMsbAlRdKpK5DxJ+X+/q5j01ClCfEJG3aSUWFVzDu3lTuAvVRg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbjl1bmV4cGVjdGVkX2tleUqnW4I=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
  "id": -576460752303421596,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAOk5mG6n0hFDvbCFUswGvPBIJk5uYYX1La0/BS3vtbGX1hGLUYWq+SCFeY7Pe/1ag4PBedPDcvWxYMFU5zDcwPuEBgvfX8OEXFiPBhT1tIQ5DtVhD0ZFVWG2wqoyjrGrqA3sROXPNaSUB7Jb8rWlu8DzOpnmdjZbOMK1Qs9AalIC0DuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GHoMsbAlRdKpK5DxJ+X+/q5j01ClCfEJG3aSUWFVzDu3lTvxwj/Q=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421596,
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
      "state": "tx_+NMLAfiEuEAOk5mG6n0hFDvbCFUswGvPBIJk5uYYX1La0/BS3vtbGX1hGLUYWq+SCFeY7Pe/1ag4PBedPDcvWxYMFU5zDcwPuEBgvfX8OEXFiPBhT1tIQ5DtVhD0ZFVWG2wqoyjrGrqA3sROXPNaSUB7Jb8rWlu8DzOpnmdjZbOMK1Qs9AalIC0DuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GHoMsbAlRdKpK5DxJ+X+/q5j01ClCfEJG3aSUWFVzDu3lTvxwj/Q=="
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
      "state": "tx_+NMLAfiEuEAOk5mG6n0hFDvbCFUswGvPBIJk5uYYX1La0/BS3vtbGX1hGLUYWq+SCFeY7Pe/1ag4PBedPDcvWxYMFU5zDcwPuEBgvfX8OEXFiPBhT1tIQ5DtVhD0ZFVWG2wqoyjrGrqA3sROXPNaSUB7Jb8rWlu8DzOpnmdjZbOMK1Qs9AalIC0DuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GHoMsbAlRdKpK5DxJ+X+/q5j01ClCfEJG3aSUWFVzDu3lTvxwj/Q=="
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 135
  }
}
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
        "round": 135
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 135
  }
}
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
        "round": 135
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 135
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
      "caller_nonce": 135,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 135,
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 135
  }
}
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
        "round": 135
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 135
  }
}
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
        "round": 135
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 135
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
      "caller_nonce": 135,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 135,
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
      "caller_nonce": 136,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 136,
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gYigprlJ1uMAHMsF504IgTql9uQ1Ok4L0E//xUmhHbKQoO3EDHhK",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
  "id": -576460752303421595,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEAbiqV4mfui8lw2QOJAYuHIgfyP/mGhzYq8F1dk/ZXbfjbrNLJBSWbr14DNiSDisPssx6+i3dp5BDjmbu3GTn4EuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GIoKa5SdbjABzLBedOCIE6pfbkNTpOC9BP/8VJoR2ykKDtNV540A=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421595,
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
      "signed_tx": "tx_+JELAfhCuEAbiqV4mfui8lw2QOJAYuHIgfyP/mGhzYq8F1dk/ZXbfjbrNLJBSWbr14DNiSDisPssx6+i3dp5BDjmbu3GTn4EuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GIoKa5SdbjABzLBedOCIE6pfbkNTpOC9BP/8VJoR2ykKDtNV540A==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
  "id": -576460752303421594,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAbiqV4mfui8lw2QOJAYuHIgfyP/mGhzYq8F1dk/ZXbfjbrNLJBSWbr14DNiSDisPssx6+i3dp5BDjmbu3GTn4EuEAflioJCAP4k4eCUHNXTJlLG1sNV0o2oq3ELKL+KJpj94ni0bte2MW5ZS8XbHBFAWCJalurZ6stpi47gqJuynQMuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GIoKa5SdbjABzLBedOCIE6pfbkNTpOC9BP/8VJoR2ykKDtsXbNgw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421594,
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
      "state": "tx_+NMLAfiEuEAbiqV4mfui8lw2QOJAYuHIgfyP/mGhzYq8F1dk/ZXbfjbrNLJBSWbr14DNiSDisPssx6+i3dp5BDjmbu3GTn4EuEAflioJCAP4k4eCUHNXTJlLG1sNV0o2oq3ELKL+KJpj94ni0bte2MW5ZS8XbHBFAWCJalurZ6stpi47gqJuynQMuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GIoKa5SdbjABzLBedOCIE6pfbkNTpOC9BP/8VJoR2ykKDtsXbNgw=="
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
      "state": "tx_+NMLAfiEuEAbiqV4mfui8lw2QOJAYuHIgfyP/mGhzYq8F1dk/ZXbfjbrNLJBSWbr14DNiSDisPssx6+i3dp5BDjmbu3GTn4EuEAflioJCAP4k4eCUHNXTJlLG1sNV0o2oq3ELKL+KJpj94ni0bte2MW5ZS8XbHBFAWCJalurZ6stpi47gqJuynQMuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GIoKa5SdbjABzLBedOCIE6pfbkNTpOC9BP/8VJoR2ykKDtsXbNgw=="
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 136
  }
}
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
        "round": 136
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 136
  }
}
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
        "round": 136
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 136
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
      "caller_nonce": 136,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 136,
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 136
  }
}
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
        "round": 136
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 136
  }
}
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
        "round": 136
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 136
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
      "caller_nonce": 136,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 136,
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
      "caller_nonce": 137,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 137,
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "ABCDEFG",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
  }
}
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "ABCDEFG",
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
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
        "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
        "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
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
    "block_hash": "kh_2SDj72kreaP7TFJQQEA7oaCovsnmYAj146XV2fy8fmLZK1poxS",
    "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gYmgwF4Ktn8rMqQO6VroqG0qOQ0betW2vBb30Z7X8CprzrpIjuyQ",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
  "id": -576460752303421593,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEAOlbWPwBmU35jSXUteGO5HCCim7UWi3/LAiN6UmxQp07pTYdwEW5GiHjDY3l3m+rF5TIadno5JsB2a/7yVonEGuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GJoMBeCrZ/KzKkDula6KhtKjkNG3rVtrwW99Ge1/Aqa866c2kzRQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421593,
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
      "signed_tx": "tx_+JELAfhCuEAOlbWPwBmU35jSXUteGO5HCCim7UWi3/LAiN6UmxQp07pTYdwEW5GiHjDY3l3m+rF5TIadno5JsB2a/7yVonEGuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GJoMBeCrZ/KzKkDula6KhtKjkNG3rVtrwW99Ge1/Aqa866c2kzRQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1eXNwNXg1a1pTaERHeS5jaGFpbi1taXNzaW5nX2tleVI1Ux0=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
  "id": -576460752303421592,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAOlbWPwBmU35jSXUteGO5HCCim7UWi3/LAiN6UmxQp07pTYdwEW5GiHjDY3l3m+rF5TIadno5JsB2a/7yVonEGuECoUZz/yWarsW9xeqBNprihoX7ImFgKqHY66HLO8nsNsB2ulZyFKOEAyugR+fpVtfPRcuR35DjSMhWaP4X/G/wOuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GJoMBeCrZ/KzKkDula6KhtKjkNG3rVtrwW99Ge1/Aqa866stE+PQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421592,
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
      "state": "tx_+NMLAfiEuEAOlbWPwBmU35jSXUteGO5HCCim7UWi3/LAiN6UmxQp07pTYdwEW5GiHjDY3l3m+rF5TIadno5JsB2a/7yVonEGuECoUZz/yWarsW9xeqBNprihoX7ImFgKqHY66HLO8nsNsB2ulZyFKOEAyugR+fpVtfPRcuR35DjSMhWaP4X/G/wOuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GJoMBeCrZ/KzKkDula6KhtKjkNG3rVtrwW99Ge1/Aqa866stE+PQ=="
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
      "state": "tx_+NMLAfiEuEAOlbWPwBmU35jSXUteGO5HCCim7UWi3/LAiN6UmxQp07pTYdwEW5GiHjDY3l3m+rF5TIadno5JsB2a/7yVonEGuECoUZz/yWarsW9xeqBNprihoX7ImFgKqHY66HLO8nsNsB2ulZyFKOEAyugR+fpVtfPRcuR35DjSMhWaP4X/G/wOuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GJoMBeCrZ/KzKkDula6KhtKjkNG3rVtrwW99Ge1/Aqa866stE+PQ=="
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 137
  }
}
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
        "round": 137
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 137
  }
}
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
        "round": 137
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 137
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
      "caller_nonce": 137,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 137,
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 137
  }
}
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
        "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
        "round": 137
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 137
  }
}
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
        "round": 137
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
    "round": 137
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
      "caller_nonce": 137,
      "contract_id": "ct_GmPw3tuAVKkPwZgPPNhVKWATZdWtHkBsbc5dkNm67diaSoiox",
      "gas_price": 1,
      "gas_used": 122,
      "height": 137,
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gYqgPCt9BxkAYxWuuqcQHXaWo4T2OLA5v8108yQ/vE7mSy06960K",
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
  "id": -576460752303421591,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuECzYIoZWuB5FOVoT+LmPXt+jd8ruPvAGbSVh1Kj28xx/9LXnJpqZYuEmt/lxMESCn6XFjLx6niozVIR45UUB9sFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GKoDwrfQcZAGMVrrqnEB12lqOE9jiwOb/NdPMkP7xO5kstIJW8Og=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421591,
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
      "signed_tx": "tx_+JELAfhCuECzYIoZWuB5FOVoT+LmPXt+jd8ruPvAGbSVh1Kj28xx/9LXnJpqZYuEmt/lxMESCn6XFjLx6niozVIR45UUB9sFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GKoDwrfQcZAGMVrrqnEB12lqOE9jiwOb/NdPMkP7xO5kstIJW8Og==",
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
  "id": -576460752303421590,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEBM93z5K+3JD/9S4cib8s+H+ScK51pIfoMlxWL4ehMqeCjw1e4Aow0T8cHrlp1wVHFRTdtKdk4R3Z8x4aRs/UEDuECzYIoZWuB5FOVoT+LmPXt+jd8ruPvAGbSVh1Kj28xx/9LXnJpqZYuEmt/lxMESCn6XFjLx6niozVIR45UUB9sFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GKoDwrfQcZAGMVrrqnEB12lqOE9jiwOb/NdPMkP7xO5kstKGav0g=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421590,
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
      "state": "tx_+NMLAfiEuEBM93z5K+3JD/9S4cib8s+H+ScK51pIfoMlxWL4ehMqeCjw1e4Aow0T8cHrlp1wVHFRTdtKdk4R3Z8x4aRs/UEDuECzYIoZWuB5FOVoT+LmPXt+jd8ruPvAGbSVh1Kj28xx/9LXnJpqZYuEmt/lxMESCn6XFjLx6niozVIR45UUB9sFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GKoDwrfQcZAGMVrrqnEB12lqOE9jiwOb/NdPMkP7xO5kstKGav0g=="
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
      "state": "tx_+NMLAfiEuEBM93z5K+3JD/9S4cib8s+H+ScK51pIfoMlxWL4ehMqeCjw1e4Aow0T8cHrlp1wVHFRTdtKdk4R3Z8x4aRs/UEDuECzYIoZWuB5FOVoT+LmPXt+jd8ruPvAGbSVh1Kj28xx/9LXnJpqZYuEmt/lxMESCn6XFjLx6niozVIR45UUB9sFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GKoDwrfQcZAGMVrrqnEB12lqOE9jiwOb/NdPMkP7xO5kstKGav0g=="
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
    "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
    "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
    "call_data": "ABCDEFG",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
      "caller_nonce": 139,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 139,
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
        "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
        "call_data": "ABCDEFG",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
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
        "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
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
    "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
    "call_data": "ABCDEFG",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
        "call_data": "ABCDEFG",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
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
        "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
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
    "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gYugyeRgdLNAHlvTu0MDD4Pg5qMltHhAadXqVM1mqhbvLMfxNTZs",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
  "id": -576460752303421589,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEDOkiA365EPs/kqHkK7sKqLPRw1qm6vqFVpFxFHBoRmeCcGE/Z6A8G7Zpy/nVvDPbJbrJpQxVwIB0XMd74ACyoOuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GLoMnkYHSzQB5b07tDAw+D4OajJbR4QGnV6lTNZqoW7yzHEELVow=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421589,
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
      "signed_tx": "tx_+JELAfhCuEDOkiA365EPs/kqHkK7sKqLPRw1qm6vqFVpFxFHBoRmeCcGE/Z6A8G7Zpy/nVvDPbJbrJpQxVwIB0XMd74ACyoOuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GLoMnkYHSzQB5b07tDAw+D4OajJbR4QGnV6lTNZqoW7yzHEELVow==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
  "id": -576460752303421588,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEB9VTtHOiT7gohaU309smSJwVW5AZANNPX7gOrRG63AE2laiUBQAYuU8uZXnJkJf/1uVj6oTz20tHIVz7pho2IHuEDOkiA365EPs/kqHkK7sKqLPRw1qm6vqFVpFxFHBoRmeCcGE/Z6A8G7Zpy/nVvDPbJbrJpQxVwIB0XMd74ACyoOuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GLoMnkYHSzQB5b07tDAw+D4OajJbR4QGnV6lTNZqoW7yzHLCoW8w=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421588,
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
      "state": "tx_+NMLAfiEuEB9VTtHOiT7gohaU309smSJwVW5AZANNPX7gOrRG63AE2laiUBQAYuU8uZXnJkJf/1uVj6oTz20tHIVz7pho2IHuEDOkiA365EPs/kqHkK7sKqLPRw1qm6vqFVpFxFHBoRmeCcGE/Z6A8G7Zpy/nVvDPbJbrJpQxVwIB0XMd74ACyoOuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GLoMnkYHSzQB5b07tDAw+D4OajJbR4QGnV6lTNZqoW7yzHLCoW8w=="
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
      "state": "tx_+NMLAfiEuEB9VTtHOiT7gohaU309smSJwVW5AZANNPX7gOrRG63AE2laiUBQAYuU8uZXnJkJf/1uVj6oTz20tHIVz7pho2IHuEDOkiA365EPs/kqHkK7sKqLPRw1qm6vqFVpFxFHBoRmeCcGE/Z6A8G7Zpy/nVvDPbJbrJpQxVwIB0XMd74ACyoOuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GLoMnkYHSzQB5b07tDAw+D4OajJbR4QGnV6lTNZqoW7yzHLCoW8w=="
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 139
  }
}
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
        "round": 139
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 139
  }
}
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
        "round": 139
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 139
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
      "caller_nonce": 139,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 139,
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 139
  }
}
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
        "round": 139
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 139
  }
}
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
        "round": 139
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 139
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
      "caller_nonce": 139,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 139,
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
    "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
    "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
    "call_data": "ABCDEFG",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
      "caller_nonce": 140,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 140,
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
        "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
        "call_data": "ABCDEFG",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
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
        "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
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
    "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
    "call_data": "ABCDEFG",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
        "call_data": "ABCDEFG",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
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
        "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
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
    "block_hash": "kh_YhoLLpBNBxvATCXmkNmfgJYAnpvLLvSipr6KG7JKFLtSWPru3",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gYyg2vJfiVLlljpZLn4wYMwSPB0kVWkFcz+okKv8HPhnWdz5Q07l",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
  "id": -576460752303421587,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEDWIVg34ejQvtSX9TsgNYgPnRefLmJCn0ogTmfLU/GVY6ZLrd3RRlQTm4k9XiODYexs6VIN8Q+xTsniLyHAXHgAuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GMoNryX4lS5ZY6WS5+MGDMEjwdJFVpBXM/qJCr/Bz4Z1nc2hmrDg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421587,
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
      "signed_tx": "tx_+JELAfhCuEDWIVg34ejQvtSX9TsgNYgPnRefLmJCn0ogTmfLU/GVY6ZLrd3RRlQTm4k9XiODYexs6VIN8Q+xTsniLyHAXHgAuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GMoNryX4lS5ZY6WS5+MGDMEjwdJFVpBXM/qJCr/Bz4Z1nc2hmrDg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
  "id": -576460752303421586,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEDWIVg34ejQvtSX9TsgNYgPnRefLmJCn0ogTmfLU/GVY6ZLrd3RRlQTm4k9XiODYexs6VIN8Q+xTsniLyHAXHgAuEDw7UB1QvxNb/ViN3KhL/5UR8WYmLI1MoButoUW1ikqVmCmI9xDGnbq8lIyiQKvULYq8lLGr+b07E+Rb/zXNosIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GMoNryX4lS5ZY6WS5+MGDMEjwdJFVpBXM/qJCr/Bz4Z1ncqBsVkQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421586,
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
      "state": "tx_+NMLAfiEuEDWIVg34ejQvtSX9TsgNYgPnRefLmJCn0ogTmfLU/GVY6ZLrd3RRlQTm4k9XiODYexs6VIN8Q+xTsniLyHAXHgAuEDw7UB1QvxNb/ViN3KhL/5UR8WYmLI1MoButoUW1ikqVmCmI9xDGnbq8lIyiQKvULYq8lLGr+b07E+Rb/zXNosIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GMoNryX4lS5ZY6WS5+MGDMEjwdJFVpBXM/qJCr/Bz4Z1ncqBsVkQ=="
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
      "state": "tx_+NMLAfiEuEDWIVg34ejQvtSX9TsgNYgPnRefLmJCn0ogTmfLU/GVY6ZLrd3RRlQTm4k9XiODYexs6VIN8Q+xTsniLyHAXHgAuEDw7UB1QvxNb/ViN3KhL/5UR8WYmLI1MoButoUW1ikqVmCmI9xDGnbq8lIyiQKvULYq8lLGr+b07E+Rb/zXNosIuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GMoNryX4lS5ZY6WS5+MGDMEjwdJFVpBXM/qJCr/Bz4Z1ncqBsVkQ=="
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 140
  }
}
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
        "round": 140
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 140
  }
}
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
        "round": 140
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 140
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
      "caller_nonce": 140,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 140,
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 140
  }
}
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
        "round": 140
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 140
  }
}
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
        "round": 140
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 140
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
      "caller_nonce": 140,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 140,
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "ABCDEFG",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
      "caller_nonce": 141,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 141,
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "ABCDEFG",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "ABCDEFG",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "ABCDEFG",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gY2gRx/YgOWtMQ0v0cAr93gc5S0JmQz/iyWzKx6QKNdU5le2cE6/",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
  "id": -576460752303421585,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEBZgxB8G9hXTroO6hToGslMeeR9nBbycBCnU/Qk5tzy4Dw8SCYv+ZEyzj0iRswIMxYM//4aS/AEkE9haHsiEw8IuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GNoEcf2IDlrTENL9HAK/d4HOUtCZkM/4slsysekCjXVOZX3CSpvQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421585,
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
      "signed_tx": "tx_+JELAfhCuEBZgxB8G9hXTroO6hToGslMeeR9nBbycBCnU/Qk5tzy4Dw8SCYv+ZEyzj0iRswIMxYM//4aS/AEkE9haHsiEw8IuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GNoEcf2IDlrTENL9HAK/d4HOUtCZkM/4slsysekCjXVOZX3CSpvQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
  "id": -576460752303421584,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEBZgxB8G9hXTroO6hToGslMeeR9nBbycBCnU/Qk5tzy4Dw8SCYv+ZEyzj0iRswIMxYM//4aS/AEkE9haHsiEw8IuECOiblLHD3lGDKzVKMVdWYiZmyUWn95XEsSxewHG8lwiO45a4eANz0trlr/sqxsN/R3r2DWiVYtF01NgPOTyPYCuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GNoEcf2IDlrTENL9HAK/d4HOUtCZkM/4slsysekCjXVOZX/vW9qg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421584,
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
      "state": "tx_+NMLAfiEuEBZgxB8G9hXTroO6hToGslMeeR9nBbycBCnU/Qk5tzy4Dw8SCYv+ZEyzj0iRswIMxYM//4aS/AEkE9haHsiEw8IuECOiblLHD3lGDKzVKMVdWYiZmyUWn95XEsSxewHG8lwiO45a4eANz0trlr/sqxsN/R3r2DWiVYtF01NgPOTyPYCuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GNoEcf2IDlrTENL9HAK/d4HOUtCZkM/4slsysekCjXVOZX/vW9qg=="
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
      "state": "tx_+NMLAfiEuEBZgxB8G9hXTroO6hToGslMeeR9nBbycBCnU/Qk5tzy4Dw8SCYv+ZEyzj0iRswIMxYM//4aS/AEkE9haHsiEw8IuECOiblLHD3lGDKzVKMVdWYiZmyUWn95XEsSxewHG8lwiO45a4eANz0trlr/sqxsN/R3r2DWiVYtF01NgPOTyPYCuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GNoEcf2IDlrTENL9HAK/d4HOUtCZkM/4slsysekCjXVOZX/vW9qg=="
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 141
  }
}
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
        "round": 141
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 141
  }
}
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
        "round": 141
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 141
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
      "caller_nonce": 141,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 141,
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 141
  }
}
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
        "round": 141
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 141
  }
}
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
        "round": 141
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 141
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
      "caller_nonce": 141,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 141,
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "ABCDEFG",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
      "caller_nonce": 142,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 142,
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "ABCDEFG",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "ABCDEFG",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "ABCDEFG",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gY6gOK2uFjZjnyiTzlBJvOv/E/sp8WdRvxTw4G6Fo7esgn6FqBLZ",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
  "id": -576460752303421583,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEAi9SCEyXppAQDIMLKuSYSkSCjKZZ16GHtXi0DCJi4TyNv3kzoJh+RS99cQB2t/A6/5dlpln3Jzro5EZfsZ3u0DuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GOoDitrhY2Y58ok85QSbzr/xP7KfFnUb8U8OBuhaO3rIJ+9Vc1lg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421583,
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
      "signed_tx": "tx_+JELAfhCuEAi9SCEyXppAQDIMLKuSYSkSCjKZZ16GHtXi0DCJi4TyNv3kzoJh+RS99cQB2t/A6/5dlpln3Jzro5EZfsZ3u0DuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GOoDitrhY2Y58ok85QSbzr/xP7KfFnUb8U8OBuhaO3rIJ+9Vc1lg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjlhY2NvdW50X3B1Ymtleek2n3E=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
  "id": -576460752303421582,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAiCtJ04Tw6FTa3mXuC7DNFxlTh7/DDMthJuY+Jn3zpUCNaCRX/F5XHW6DpgZlmSOR/rA4voSHM7kYhiH6/vKkLuEAi9SCEyXppAQDIMLKuSYSkSCjKZZ16GHtXi0DCJi4TyNv3kzoJh+RS99cQB2t/A6/5dlpln3Jzro5EZfsZ3u0DuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GOoDitrhY2Y58ok85QSbzr/xP7KfFnUb8U8OBuhaO3rIJ+nY1+xQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421582,
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
      "state": "tx_+NMLAfiEuEAiCtJ04Tw6FTa3mXuC7DNFxlTh7/DDMthJuY+Jn3zpUCNaCRX/F5XHW6DpgZlmSOR/rA4voSHM7kYhiH6/vKkLuEAi9SCEyXppAQDIMLKuSYSkSCjKZZ16GHtXi0DCJi4TyNv3kzoJh+RS99cQB2t/A6/5dlpln3Jzro5EZfsZ3u0DuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GOoDitrhY2Y58ok85QSbzr/xP7KfFnUb8U8OBuhaO3rIJ+nY1+xQ=="
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
      "state": "tx_+NMLAfiEuEAiCtJ04Tw6FTa3mXuC7DNFxlTh7/DDMthJuY+Jn3zpUCNaCRX/F5XHW6DpgZlmSOR/rA4voSHM7kYhiH6/vKkLuEAi9SCEyXppAQDIMLKuSYSkSCjKZZ16GHtXi0DCJi4TyNv3kzoJh+RS99cQB2t/A6/5dlpln3Jzro5EZfsZ3u0DuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GOoDitrhY2Y58ok85QSbzr/xP7KfFnUb8U8OBuhaO3rIJ+nY1+xQ=="
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 142
  }
}
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
        "round": 142
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 142
  }
}
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
        "round": 142
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 142
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
      "caller_nonce": 142,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 142,
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 142
  }
}
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
        "round": 142
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 142
  }
}
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
        "round": 142
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 142
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
      "caller_nonce": 142,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 142,
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "ABCDEFG",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
      "caller_nonce": 143,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 143,
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "ABCDEFG",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "ABCDEFG",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "ABCDEFG",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gY+gUsv92g/LCQtXjazc8mrva1gGQZ9aV7U+I1r0DAF8ipQnmTvm",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
  "id": -576460752303421581,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEBXEazw8fJ2nFJpNxwLr9Qn25KaopjN5KTfkwDdp52UvcHmwg1kDO4e/s0ND0Hnvmp8x7BE/ASnmE/gulqdVxUNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GPoFLL/doPywkLV42s3PJq72tYBkGfWle1PiNa9AwBfIqUie4noA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421581,
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
      "signed_tx": "tx_+JELAfhCuEBXEazw8fJ2nFJpNxwLr9Qn25KaopjN5KTfkwDdp52UvcHmwg1kDO4e/s0ND0Hnvmp8x7BE/ASnmE/gulqdVxUNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GPoFLL/doPywkLV42s3PJq72tYBkGfWle1PiNa9AwBfIqUie4noA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
  "id": -576460752303421580,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEA43Udx7ATt0xx5l5vRZp9sKuzpKjBfYYaKPnbkifZJBArLxmu2Ba6GKNZ7PmeIG2/bN5ATMrZBphcQM3RUfeUKuEBXEazw8fJ2nFJpNxwLr9Qn25KaopjN5KTfkwDdp52UvcHmwg1kDO4e/s0ND0Hnvmp8x7BE/ASnmE/gulqdVxUNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GPoFLL/doPywkLV42s3PJq72tYBkGfWle1PiNa9AwBfIqUAjErnA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421580,
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
      "state": "tx_+NMLAfiEuEA43Udx7ATt0xx5l5vRZp9sKuzpKjBfYYaKPnbkifZJBArLxmu2Ba6GKNZ7PmeIG2/bN5ATMrZBphcQM3RUfeUKuEBXEazw8fJ2nFJpNxwLr9Qn25KaopjN5KTfkwDdp52UvcHmwg1kDO4e/s0ND0Hnvmp8x7BE/ASnmE/gulqdVxUNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GPoFLL/doPywkLV42s3PJq72tYBkGfWle1PiNa9AwBfIqUAjErnA=="
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
      "state": "tx_+NMLAfiEuEA43Udx7ATt0xx5l5vRZp9sKuzpKjBfYYaKPnbkifZJBArLxmu2Ba6GKNZ7PmeIG2/bN5ATMrZBphcQM3RUfeUKuEBXEazw8fJ2nFJpNxwLr9Qn25KaopjN5KTfkwDdp52UvcHmwg1kDO4e/s0ND0Hnvmp8x7BE/ASnmE/gulqdVxUNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GPoFLL/doPywkLV42s3PJq72tYBkGfWle1PiNa9AwBfIqUAjErnA=="
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 143
  }
}
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
        "round": 143
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 143
  }
}
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
        "round": 143
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 143
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
      "caller_nonce": 143,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 143,
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 143
  }
}
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
        "round": 143
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 143
  }
}
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
        "round": 143
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 143
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
      "caller_nonce": 143,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 143,
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "ABCDEFG",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
      "caller_nonce": 144,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 144,
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "ABCDEFG",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "ABCDEFG",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "ABCDEFG",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gZCg1mheSBM36Q8v+02VZ1+EsErL0D1O2Q76SmmOGUq3oPcoAyOp",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
  "id": -576460752303421579,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEAnLOD6AOQwaWnFy8p9O2dqTT47fll0sAUTnhTDVQYdhxcN8Bj8htWLbt2JjGPSAzL3nfTgMKT/1t23wUkmbAcCuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GQoNZoXkgTN+kPL/tNlWdfhLBKy9A9TtkO+kppjhlKt6D3AJCD0A=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421579,
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
      "signed_tx": "tx_+JELAfhCuEAnLOD6AOQwaWnFy8p9O2dqTT47fll0sAUTnhTDVQYdhxcN8Bj8htWLbt2JjGPSAzL3nfTgMKT/1t23wUkmbAcCuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GQoNZoXkgTN+kPL/tNlWdfhLBKy9A9TtkO+kppjhlKt6D3AJCD0A==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbhlvcmFjbGX/S3LA",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
  "id": -576460752303421578,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAnLOD6AOQwaWnFy8p9O2dqTT47fll0sAUTnhTDVQYdhxcN8Bj8htWLbt2JjGPSAzL3nfTgMKT/1t23wUkmbAcCuEDbWrIeXVtTWWlRH3TOrH39CQ8EHc9c2DdSmTfAw0Urkj4XIxtVo4qlsRDSuIZorHR40A+hMnK1hfWfUzDL8Y0MuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GQoNZoXkgTN+kPL/tNlWdfhLBKy9A9TtkO+kppjhlKt6D3SW3u3g=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421578,
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
      "state": "tx_+NMLAfiEuEAnLOD6AOQwaWnFy8p9O2dqTT47fll0sAUTnhTDVQYdhxcN8Bj8htWLbt2JjGPSAzL3nfTgMKT/1t23wUkmbAcCuEDbWrIeXVtTWWlRH3TOrH39CQ8EHc9c2DdSmTfAw0Urkj4XIxtVo4qlsRDSuIZorHR40A+hMnK1hfWfUzDL8Y0MuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GQoNZoXkgTN+kPL/tNlWdfhLBKy9A9TtkO+kppjhlKt6D3SW3u3g=="
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
      "state": "tx_+NMLAfiEuEAnLOD6AOQwaWnFy8p9O2dqTT47fll0sAUTnhTDVQYdhxcN8Bj8htWLbt2JjGPSAzL3nfTgMKT/1t23wUkmbAcCuEDbWrIeXVtTWWlRH3TOrH39CQ8EHc9c2DdSmTfAw0Urkj4XIxtVo4qlsRDSuIZorHR40A+hMnK1hfWfUzDL8Y0MuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GQoNZoXkgTN+kPL/tNlWdfhLBKy9A9TtkO+kppjhlKt6D3SW3u3g=="
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 144
  }
}
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
        "round": 144
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 144
  }
}
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
        "round": 144
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 144
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
      "caller_nonce": 144,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 144,
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 144
  }
}
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
        "round": 144
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 144
  }
}
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
        "round": 144
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 144
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
      "caller_nonce": 144,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 144,
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "ABCDEFG",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
      "caller_nonce": 145,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 145,
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "ABCDEFG",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "ABCDEFG",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "ABCDEFG",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gZGgisTc0mJP32Jp4KnTM2hdrPMC1szj15k1M86B2H3cG1vwpkYD",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
  "id": -576460752303421577,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuECmaPPVtoT1armugePBToJmJe7lPNpKV9o32Za2f9hBUbxvZn4NXf5ImiX0ztBR7CXIsCfc4XQhXsepv3300SoDuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GRoIrE3NJiT99iaeCp0zNoXazzAtbM49eZNTPOgdh93Btbs0+rYw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421577,
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
      "signed_tx": "tx_+JELAfhCuECmaPPVtoT1armugePBToJmJe7lPNpKV9o32Za2f9hBUbxvZn4NXf5ImiX0ztBR7CXIsCfc4XQhXsepv3300SoDuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GRoIrE3NJiT99iaeCp0zNoXazzAtbM49eZNTPOgdh93Btbs0+rYw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
  "id": -576460752303421576,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEB+K4fLojZRxRpcJStaZt1rNTq/MxKssgiKPkBmeiZmktHyYRtB0AXCkZ8l+rX9jotX3JCP2gGuWG0dRrszAY0JuECmaPPVtoT1armugePBToJmJe7lPNpKV9o32Za2f9hBUbxvZn4NXf5ImiX0ztBR7CXIsCfc4XQhXsepv3300SoDuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GRoIrE3NJiT99iaeCp0zNoXazzAtbM49eZNTPOgdh93BtbN+7b/A=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421576,
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
      "state": "tx_+NMLAfiEuEB+K4fLojZRxRpcJStaZt1rNTq/MxKssgiKPkBmeiZmktHyYRtB0AXCkZ8l+rX9jotX3JCP2gGuWG0dRrszAY0JuECmaPPVtoT1armugePBToJmJe7lPNpKV9o32Za2f9hBUbxvZn4NXf5ImiX0ztBR7CXIsCfc4XQhXsepv3300SoDuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GRoIrE3NJiT99iaeCp0zNoXazzAtbM49eZNTPOgdh93BtbN+7b/A=="
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
      "state": "tx_+NMLAfiEuEB+K4fLojZRxRpcJStaZt1rNTq/MxKssgiKPkBmeiZmktHyYRtB0AXCkZ8l+rX9jotX3JCP2gGuWG0dRrszAY0JuECmaPPVtoT1armugePBToJmJe7lPNpKV9o32Za2f9hBUbxvZn4NXf5ImiX0ztBR7CXIsCfc4XQhXsepv3300SoDuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GRoIrE3NJiT99iaeCp0zNoXazzAtbM49eZNTPOgdh93BtbN+7b/A=="
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 145
  }
}
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
        "round": 145
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 145
  }
}
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
        "round": 145
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 145
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
      "caller_nonce": 145,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 145,
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 145
  }
}
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
        "round": 145
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 145
  }
}
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
        "round": 145
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 145
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
      "caller_nonce": 145,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 145,
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "ABCDEFG",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
      "caller_nonce": 146,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 146,
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "ABCDEFG",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "ABCDEFG",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "ABCDEFG",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gZKgrDtnhsAbQGVL4prk6AwbfgFNF8PmbN6cFLRj8PXznbNjPbho",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
  "id": -576460752303421575,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEDI047QXhU0cxZnwKhx6JUyMwSoYNIij8ORqoUyioMC9mD0+UqeCUHifEcGL+dgrl2caE5eoCOlIwkpn/bXF10OuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GSoKw7Z4bAG0BlS+Ka5OgMG34BTRfD5mzenBS0Y/D1852zw72iBw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421575,
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
      "signed_tx": "tx_+JELAfhCuEDI047QXhU0cxZnwKhx6JUyMwSoYNIij8ORqoUyioMC9mD0+UqeCUHifEcGL+dgrl2caE5eoCOlIwkpn/bXF10OuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GSoKw7Z4bAG0BlS+Ka5OgMG34BTRfD5mzenBS0Y/D1852zw72iBw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbjl1bmV4cGVjdGVkX2tlebeE4+8=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
  "id": -576460752303421574,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEA6fPJg7U9vYQ/PzjB0M9GkXvwafUParbnWiocUMVVkZLvHaOqpmnwBnO8PKb+yIgeVZ3FzjJeahHeb+NRyv7sCuEDI047QXhU0cxZnwKhx6JUyMwSoYNIij8ORqoUyioMC9mD0+UqeCUHifEcGL+dgrl2caE5eoCOlIwkpn/bXF10OuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GSoKw7Z4bAG0BlS+Ka5OgMG34BTRfD5mzenBS0Y/D1852z1MtWfQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421574,
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
      "state": "tx_+NMLAfiEuEA6fPJg7U9vYQ/PzjB0M9GkXvwafUParbnWiocUMVVkZLvHaOqpmnwBnO8PKb+yIgeVZ3FzjJeahHeb+NRyv7sCuEDI047QXhU0cxZnwKhx6JUyMwSoYNIij8ORqoUyioMC9mD0+UqeCUHifEcGL+dgrl2caE5eoCOlIwkpn/bXF10OuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GSoKw7Z4bAG0BlS+Ka5OgMG34BTRfD5mzenBS0Y/D1852z1MtWfQ=="
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
      "state": "tx_+NMLAfiEuEA6fPJg7U9vYQ/PzjB0M9GkXvwafUParbnWiocUMVVkZLvHaOqpmnwBnO8PKb+yIgeVZ3FzjJeahHeb+NRyv7sCuEDI047QXhU0cxZnwKhx6JUyMwSoYNIij8ORqoUyioMC9mD0+UqeCUHifEcGL+dgrl2caE5eoCOlIwkpn/bXF10OuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GSoKw7Z4bAG0BlS+Ka5OgMG34BTRfD5mzenBS0Y/D1852z1MtWfQ=="
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 146
  }
}
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
        "round": 146
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 146
  }
}
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
        "round": 146
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 146
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
      "caller_nonce": 146,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 146,
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 146
  }
}
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
        "round": 146
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 146
  }
}
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
        "round": 146
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 146
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
      "caller_nonce": 146,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 146,
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "ABCDEFG",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
      "caller_nonce": 147,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 147,
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "ABCDEFG",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "ABCDEFG",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "ABCDEFG",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gZOgBd4qaHmJEgH8uCcWRy7ptP8nQqSW1vBuKzQeBuC/Vvu4Brl2",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
  "id": -576460752303421573,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEBcL7y4bNq0iFNnFSpqZu9KIv8zkKFUNpuWKvgXrQ1hV0Z50v6fZi21i9qJqmHOFMqBnUtqDj7hPhx4i62FkUQOuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GToAXeKmh5iRIB/LgnFkcu6bT/J0Kkltbwbis0Hgbgv1b7O4D6cQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421573,
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
      "signed_tx": "tx_+JELAfhCuEBcL7y4bNq0iFNnFSpqZu9KIv8zkKFUNpuWKvgXrQ1hV0Z50v6fZi21i9qJqmHOFMqBnUtqDj7hPhx4i62FkUQOuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GToAXeKmh5iRIB/LgnFkcu6bT/J0Kkltbwbis0Hgbgv1b7O4D6cQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
  "id": -576460752303421572,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEBcL7y4bNq0iFNnFSpqZu9KIv8zkKFUNpuWKvgXrQ1hV0Z50v6fZi21i9qJqmHOFMqBnUtqDj7hPhx4i62FkUQOuEDS4iDA86H+GFevpHmz8GbCx/pAssNqy6OJR8zggyYyzfIZOa5k/QeR4RRAjPO4uoji/6iCJSIDkzML4IH4ZNIHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GToAXeKmh5iRIB/LgnFkcu6bT/J0Kkltbwbis0Hgbgv1b7p8Xn1A=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421572,
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
      "state": "tx_+NMLAfiEuEBcL7y4bNq0iFNnFSpqZu9KIv8zkKFUNpuWKvgXrQ1hV0Z50v6fZi21i9qJqmHOFMqBnUtqDj7hPhx4i62FkUQOuEDS4iDA86H+GFevpHmz8GbCx/pAssNqy6OJR8zggyYyzfIZOa5k/QeR4RRAjPO4uoji/6iCJSIDkzML4IH4ZNIHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GToAXeKmh5iRIB/LgnFkcu6bT/J0Kkltbwbis0Hgbgv1b7p8Xn1A=="
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
      "state": "tx_+NMLAfiEuEBcL7y4bNq0iFNnFSpqZu9KIv8zkKFUNpuWKvgXrQ1hV0Z50v6fZi21i9qJqmHOFMqBnUtqDj7hPhx4i62FkUQOuEDS4iDA86H+GFevpHmz8GbCx/pAssNqy6OJR8zggyYyzfIZOa5k/QeR4RRAjPO4uoji/6iCJSIDkzML4IH4ZNIHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GToAXeKmh5iRIB/LgnFkcu6bT/J0Kkltbwbis0Hgbgv1b7p8Xn1A=="
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 147
  }
}
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
        "round": 147
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 147
  }
}
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
        "round": 147
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 147
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
      "caller_nonce": 147,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 147,
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 147
  }
}
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
        "round": 147
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 147
  }
}
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
        "round": 147
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 147
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
      "caller_nonce": 147,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 147,
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "ABCDEFG",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
      "caller_nonce": 148,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 148,
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "ABCDEFG",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "ABCDEFG",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
  }
}
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "ABCDEFG",
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
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
        "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
        "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
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
    "block_hash": "kh_2uJdX49biJg549VnWHc3WT94EnbT3vV3dUU5nCVWqPT71PN3kT",
    "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gZSgBfoFmHlmsmGTjZ4kozBj0tprjksolwmGPFEARv3XwJJT9NfS",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
  "id": -576460752303421571,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuED3PQJzFfRWRF0TRoDylvJK/dFRVZbVPrOLDKwqXfr3Dz8tjVgpxNOSdLO+LK2hpqqYUDy9U3VItZEvuuVc7dgNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GUoAX6BZh5ZrJhk42eJKMwY9Laa45LKJcJhjxRAEb918CSr9lBRg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421571,
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
      "signed_tx": "tx_+JELAfhCuED3PQJzFfRWRF0TRoDylvJK/dFRVZbVPrOLDKwqXfr3Dz8tjVgpxNOSdLO+LK2hpqqYUDy9U3VItZEvuuVc7dgNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GUoAX6BZh5ZrJhk42eJKMwY9Laa45LKJcJhjxRAEb918CSr9lBRg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzMnZNUUpaRk5uM1hZaC5jaGFpbi1taXNzaW5nX2tleWXURlY=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
  "id": -576460752303421570,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuECoNgH1Hy/QNgZrxq+QreNNzAr4NUQX2peTjLPJt3iQpcc/jLwod82hGFLy0uDe2u3KHEGikMPW5eEvAzIBX38OuED3PQJzFfRWRF0TRoDylvJK/dFRVZbVPrOLDKwqXfr3Dz8tjVgpxNOSdLO+LK2hpqqYUDy9U3VItZEvuuVc7dgNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GUoAX6BZh5ZrJhk42eJKMwY9Laa45LKJcJhjxRAEb918CSk1Tw7g=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421570,
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
      "state": "tx_+NMLAfiEuECoNgH1Hy/QNgZrxq+QreNNzAr4NUQX2peTjLPJt3iQpcc/jLwod82hGFLy0uDe2u3KHEGikMPW5eEvAzIBX38OuED3PQJzFfRWRF0TRoDylvJK/dFRVZbVPrOLDKwqXfr3Dz8tjVgpxNOSdLO+LK2hpqqYUDy9U3VItZEvuuVc7dgNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GUoAX6BZh5ZrJhk42eJKMwY9Laa45LKJcJhjxRAEb918CSk1Tw7g=="
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
      "state": "tx_+NMLAfiEuECoNgH1Hy/QNgZrxq+QreNNzAr4NUQX2peTjLPJt3iQpcc/jLwod82hGFLy0uDe2u3KHEGikMPW5eEvAzIBX38OuED3PQJzFfRWRF0TRoDylvJK/dFRVZbVPrOLDKwqXfr3Dz8tjVgpxNOSdLO+LK2hpqqYUDy9U3VItZEvuuVc7dgNuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GUoAX6BZh5ZrJhk42eJKMwY9Laa45LKJcJhjxRAEb918CSk1Tw7g=="
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 148
  }
}
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
        "round": 148
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 148
  }
}
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
        "round": 148
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 148
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
      "caller_nonce": 148,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 148,
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 148
  }
}
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
        "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
        "round": 148
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 148
  }
}
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
        "round": 148
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
    "round": 148
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
      "caller_nonce": 148,
      "contract_id": "ct_erizTPeUG3aEPebWvKuKH5B4qa4fduJcTkuk8ht6Z9GoRbXcB",
      "gas_price": 1,
      "gas_used": 122,
      "height": 148,
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gZWgtlxPWCZ4juwG+8YFrjQgHh/LBGrqpUwvwBKgJ4jVoIkQVlh5",
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
  "id": -576460752303421569,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEDmuT0Ba2oWIK9jhCjGfkChMuUvRD/SZ2LuUiCAHbqxvpsn02i+XnNw0j9J+IHrIOFc1oQAY4xg8XVPWgE7D/8BuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GVoLZcT1gmeI7sBvvGBa40IB4fywRq6qVML8ASoCeI1aCJayKTiQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421569,
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
      "signed_tx": "tx_+JELAfhCuEDmuT0Ba2oWIK9jhCjGfkChMuUvRD/SZ2LuUiCAHbqxvpsn02i+XnNw0j9J+IHrIOFc1oQAY4xg8XVPWgE7D/8BuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GVoLZcT1gmeI7sBvvGBa40IB4fywRq6qVML8ASoCeI1aCJayKTiQ==",
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
  "id": -576460752303421568,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEByUntvm4aaaoAEQRNSyKewxlkfjAm2jrU6Gba3QP7b6WWcZeihQrpB0fiyO4WQ02ERcE5yd3pgvyJFwCFx5IEAuEDmuT0Ba2oWIK9jhCjGfkChMuUvRD/SZ2LuUiCAHbqxvpsn02i+XnNw0j9J+IHrIOFc1oQAY4xg8XVPWgE7D/8BuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GVoLZcT1gmeI7sBvvGBa40IB4fywRq6qVML8ASoCeI1aCJRiwBpw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421568,
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
      "state": "tx_+NMLAfiEuEByUntvm4aaaoAEQRNSyKewxlkfjAm2jrU6Gba3QP7b6WWcZeihQrpB0fiyO4WQ02ERcE5yd3pgvyJFwCFx5IEAuEDmuT0Ba2oWIK9jhCjGfkChMuUvRD/SZ2LuUiCAHbqxvpsn02i+XnNw0j9J+IHrIOFc1oQAY4xg8XVPWgE7D/8BuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GVoLZcT1gmeI7sBvvGBa40IB4fywRq6qVML8ASoCeI1aCJRiwBpw=="
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
      "state": "tx_+NMLAfiEuEByUntvm4aaaoAEQRNSyKewxlkfjAm2jrU6Gba3QP7b6WWcZeihQrpB0fiyO4WQ02ERcE5yd3pgvyJFwCFx5IEAuEDmuT0Ba2oWIK9jhCjGfkChMuUvRD/SZ2LuUiCAHbqxvpsn02i+XnNw0j9J+IHrIOFc1oQAY4xg8XVPWgE7D/8BuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GVoLZcT1gmeI7sBvvGBa40IB4fywRq6qVML8ASoCeI1aCJRiwBpw=="
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
    "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
    "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
      "caller_nonce": 150,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 150,
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
        "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
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
        "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
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
    "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
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
        "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
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
    "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gZag5bbgQmrQP6Oe9hjcWa3a80h0SHBukk4uwW/WKfcuq2yF/cbN",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
  "id": -576460752303421567,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEDm0SzX1xyA7J1qNcLrh+PiwJ26O+Lm6JIS6S0K77X31oktKtF1DM44M+WrURbvH2VznG8HnXcv0AveQ0uA3PABuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GWoOW24EJq0D+jnvYY3Fmt2vNIdEhwbpJOLsFv1in3LqtswOYlhQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421567,
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
      "signed_tx": "tx_+JELAfhCuEDm0SzX1xyA7J1qNcLrh+PiwJ26O+Lm6JIS6S0K77X31oktKtF1DM44M+WrURbvH2VznG8HnXcv0AveQ0uA3PABuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GWoOW24EJq0D+jnvYY3Fmt2vNIdEhwbpJOLsFv1in3LqtswOYlhQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
  "id": -576460752303421566,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEByKoYS1CqWO1zvQt32KtlUCax+ur8DNlS7dYPpKWlAhdjYHi+PIxg3+FPukgNL84Ztc1lJlUI57ZQu+TCrbPwLuEDm0SzX1xyA7J1qNcLrh+PiwJ26O+Lm6JIS6S0K77X31oktKtF1DM44M+WrURbvH2VznG8HnXcv0AveQ0uA3PABuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GWoOW24EJq0D+jnvYY3Fmt2vNIdEhwbpJOLsFv1in3Lqts8HHnpQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421566,
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
      "state": "tx_+NMLAfiEuEByKoYS1CqWO1zvQt32KtlUCax+ur8DNlS7dYPpKWlAhdjYHi+PIxg3+FPukgNL84Ztc1lJlUI57ZQu+TCrbPwLuEDm0SzX1xyA7J1qNcLrh+PiwJ26O+Lm6JIS6S0K77X31oktKtF1DM44M+WrURbvH2VznG8HnXcv0AveQ0uA3PABuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GWoOW24EJq0D+jnvYY3Fmt2vNIdEhwbpJOLsFv1in3Lqts8HHnpQ=="
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
      "state": "tx_+NMLAfiEuEByKoYS1CqWO1zvQt32KtlUCax+ur8DNlS7dYPpKWlAhdjYHi+PIxg3+FPukgNL84Ztc1lJlUI57ZQu+TCrbPwLuEDm0SzX1xyA7J1qNcLrh+PiwJ26O+Lm6JIS6S0K77X31oktKtF1DM44M+WrURbvH2VznG8HnXcv0AveQ0uA3PABuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GWoOW24EJq0D+jnvYY3Fmt2vNIdEhwbpJOLsFv1in3Lqts8HHnpQ=="
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 150
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
        "round": 150
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 150
  }
}
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
        "round": 150
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 150
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
      "caller_nonce": 150,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 150,
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 150
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
        "round": 150
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 150
  }
}
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
        "round": 150
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 150
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
      "caller_nonce": 150,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 150,
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
    "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
    "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
      "caller_nonce": 151,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 151,
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
        "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
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
        "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
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
    "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
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
        "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
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
    "block_hash": "kh_4eeCe8RS7UN1xsX7MKiFvu5suunJXtHxoT1hPdqeatiryDYAR",
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gZegd7bbngB3IGd/eG8o2hcGbmAuqT8SzD74Nlb0whq2FAfB8nAC",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
  "id": -576460752303421565,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEAPdDPva73K+KpiGvaxDfHTxG+gS81c892wULUkwBWy/oe/ghfvUZNtrGBcnfuTqeiR/7i1SYtNTkv7pa6FxFsJuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GXoHe2254AdyBnf3hvKNoXBm5gLqk/Esw++DZW9MIathQHPOdb1g=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421565,
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
      "signed_tx": "tx_+JELAfhCuEAPdDPva73K+KpiGvaxDfHTxG+gS81c892wULUkwBWy/oe/ghfvUZNtrGBcnfuTqeiR/7i1SYtNTkv7pa6FxFsJuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GXoHe2254AdyBnf3hvKNoXBm5gLqk/Esw++DZW9MIathQHPOdb1g==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
  "id": -576460752303421564,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAPdDPva73K+KpiGvaxDfHTxG+gS81c892wULUkwBWy/oe/ghfvUZNtrGBcnfuTqeiR/7i1SYtNTkv7pa6FxFsJuECHmBdM0PPkeTsKThoTz3wOc3U9KHkSiE7QnUVSHJoT/VFk2bjdHHFPvStpEfXFnxGFrG1YW15MwhR835LfiSkCuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GXoHe2254AdyBnf3hvKNoXBm5gLqk/Esw++DZW9MIathQHx1V1NA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421564,
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
      "state": "tx_+NMLAfiEuEAPdDPva73K+KpiGvaxDfHTxG+gS81c892wULUkwBWy/oe/ghfvUZNtrGBcnfuTqeiR/7i1SYtNTkv7pa6FxFsJuECHmBdM0PPkeTsKThoTz3wOc3U9KHkSiE7QnUVSHJoT/VFk2bjdHHFPvStpEfXFnxGFrG1YW15MwhR835LfiSkCuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GXoHe2254AdyBnf3hvKNoXBm5gLqk/Esw++DZW9MIathQHx1V1NA=="
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
      "state": "tx_+NMLAfiEuEAPdDPva73K+KpiGvaxDfHTxG+gS81c892wULUkwBWy/oe/ghfvUZNtrGBcnfuTqeiR/7i1SYtNTkv7pa6FxFsJuECHmBdM0PPkeTsKThoTz3wOc3U9KHkSiE7QnUVSHJoT/VFk2bjdHHFPvStpEfXFnxGFrG1YW15MwhR835LfiSkCuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GXoHe2254AdyBnf3hvKNoXBm5gLqk/Esw++DZW9MIathQHx1V1NA=="
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 151
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
        "round": 151
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 151
  }
}
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
        "round": 151
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 151
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
      "caller_nonce": 151,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 151,
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 151
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
        "round": 151
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 151
  }
}
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
        "round": 151
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 151
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
      "caller_nonce": 151,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 151,
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
      "caller_nonce": 152,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 152,
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gZigqhB5/drVGGAkBCWzHGpxdYvlcrQWRcXUyZoFJ+CFpIYFQi1m",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
  "id": -576460752303421563,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEBIaGBuaCABAairYevhpynTsOBPKyJn+nIcMTgnhAA/rACZyVLPOE1foaZ2sZJFNyAWFezD8IAPak3qr8Rb/WMAuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GYoKoQef3a1RhgJAQlsxxqcXWL5XK0FkXF1MmaBSfghaSGK6vAQA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421563,
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
      "signed_tx": "tx_+JELAfhCuEBIaGBuaCABAairYevhpynTsOBPKyJn+nIcMTgnhAA/rACZyVLPOE1foaZ2sZJFNyAWFezD8IAPak3qr8Rb/WMAuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GYoKoQef3a1RhgJAQlsxxqcXWL5XK0FkXF1MmaBSfghaSGK6vAQA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
  "id": -576460752303421562,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEBIaGBuaCABAairYevhpynTsOBPKyJn+nIcMTgnhAA/rACZyVLPOE1foaZ2sZJFNyAWFezD8IAPak3qr8Rb/WMAuEBUNCEj1uSRT2O6B23vaT8RvCQtzJDMJ67W3d3h9NEGI+OA7NkgkhWW6pYMygsc2UNhs2i5Il4f+hhOwYeDAc8OuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GYoKoQef3a1RhgJAQlsxxqcXWL5XK0FkXF1MmaBSfghaSGt5uQNA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421562,
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
      "state": "tx_+NMLAfiEuEBIaGBuaCABAairYevhpynTsOBPKyJn+nIcMTgnhAA/rACZyVLPOE1foaZ2sZJFNyAWFezD8IAPak3qr8Rb/WMAuEBUNCEj1uSRT2O6B23vaT8RvCQtzJDMJ67W3d3h9NEGI+OA7NkgkhWW6pYMygsc2UNhs2i5Il4f+hhOwYeDAc8OuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GYoKoQef3a1RhgJAQlsxxqcXWL5XK0FkXF1MmaBSfghaSGt5uQNA=="
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
      "state": "tx_+NMLAfiEuEBIaGBuaCABAairYevhpynTsOBPKyJn+nIcMTgnhAA/rACZyVLPOE1foaZ2sZJFNyAWFezD8IAPak3qr8Rb/WMAuEBUNCEj1uSRT2O6B23vaT8RvCQtzJDMJ67W3d3h9NEGI+OA7NkgkhWW6pYMygsc2UNhs2i5Il4f+hhOwYeDAc8OuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GYoKoQef3a1RhgJAQlsxxqcXWL5XK0FkXF1MmaBSfghaSGt5uQNA=="
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 152
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
        "round": 152
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 152
  }
}
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
        "round": 152
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 152
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
      "caller_nonce": 152,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 152,
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 152
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
        "round": 152
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 152
  }
}
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
        "round": 152
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 152
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
      "caller_nonce": 152,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 152,
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
      "caller_nonce": 153,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 153,
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gZmg3LcSvKXDC1HPOSaSuDRe5Qvmtw4Cape5QFUC6d8kEtqXFTwD",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
  "id": -576460752303421561,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEAbpdpoCRfl51KWRvOis2CYnJl8b0DbBEJTNvizOebBBLkOPCCgOUfy2TWQO35aTq5qgmrmw5Q7GxeyRREO2k0CuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GZoNy3ErylwwtRzzkmkrg0XuUL5rcOAmqXuUBVAunfJBLaiaurJg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421561,
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
      "signed_tx": "tx_+JELAfhCuEAbpdpoCRfl51KWRvOis2CYnJl8b0DbBEJTNvizOebBBLkOPCCgOUfy2TWQO35aTq5qgmrmw5Q7GxeyRREO2k0CuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GZoNy3ErylwwtRzzkmkrg0XuUL5rcOAmqXuUBVAunfJBLaiaurJg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjlhY2NvdW50X3B1YmtleYhD/Kg=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
  "id": -576460752303421560,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAbpdpoCRfl51KWRvOis2CYnJl8b0DbBEJTNvizOebBBLkOPCCgOUfy2TWQO35aTq5qgmrmw5Q7GxeyRREO2k0CuEDKfZVa7p+egTkXB9/zF7s+Syti5eyGytkpgneP2xYMxKEMhjpZujpNX1M9+jeAfzLVUU5BRlG/vC5fZhHyV4gFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GZoNy3ErylwwtRzzkmkrg0XuUL5rcOAmqXuUBVAunfJBLa1ZU5iA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421560,
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
      "state": "tx_+NMLAfiEuEAbpdpoCRfl51KWRvOis2CYnJl8b0DbBEJTNvizOebBBLkOPCCgOUfy2TWQO35aTq5qgmrmw5Q7GxeyRREO2k0CuEDKfZVa7p+egTkXB9/zF7s+Syti5eyGytkpgneP2xYMxKEMhjpZujpNX1M9+jeAfzLVUU5BRlG/vC5fZhHyV4gFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GZoNy3ErylwwtRzzkmkrg0XuUL5rcOAmqXuUBVAunfJBLa1ZU5iA=="
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
      "state": "tx_+NMLAfiEuEAbpdpoCRfl51KWRvOis2CYnJl8b0DbBEJTNvizOebBBLkOPCCgOUfy2TWQO35aTq5qgmrmw5Q7GxeyRREO2k0CuEDKfZVa7p+egTkXB9/zF7s+Syti5eyGytkpgneP2xYMxKEMhjpZujpNX1M9+jeAfzLVUU5BRlG/vC5fZhHyV4gFuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GZoNy3ErylwwtRzzkmkrg0XuUL5rcOAmqXuUBVAunfJBLa1ZU5iA=="
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 153
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
        "round": 153
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 153
  }
}
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
        "round": 153
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 153
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
      "caller_nonce": 153,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 153,
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 153
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
        "round": 153
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 153
  }
}
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
        "round": 153
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 153
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
      "caller_nonce": 153,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 153,
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
      "caller_nonce": 154,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 154,
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gZqgHnib7/1lY47okuQWrE30NqBPQLzJ3RKH9VBWFt9Qi1DKjB9B",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
  "id": -576460752303421559,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEDqKRRdlZu3BPqjK13UCR0+XH4MB4eGz6cX7j9iSnG4xiCwOYBE6ggbQsDI0IXAP5QXNbzlE/DMPJP55c38y6AEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GaoB54m+/9ZWOO6JLkFqxN9DagT0C8yd0Sh/VQVhbfUItQ8VLJ2Q=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421559,
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
      "signed_tx": "tx_+JELAfhCuEDqKRRdlZu3BPqjK13UCR0+XH4MB4eGz6cX7j9iSnG4xiCwOYBE6ggbQsDI0IXAP5QXNbzlE/DMPJP55c38y6AEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GaoB54m+/9ZWOO6JLkFqxN9DagT0C8yd0Sh/VQVhbfUItQ8VLJ2Q==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
  "id": -576460752303421558,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEDUws8WPVfg0iJyxEqyi4lHua8G1AnK2eQ+cgMXBFGjsNH/FOXRK+cEM/TyaKdJBMQvsH/nbHTWYWwf+nf062cGuEDqKRRdlZu3BPqjK13UCR0+XH4MB4eGz6cX7j9iSnG4xiCwOYBE6ggbQsDI0IXAP5QXNbzlE/DMPJP55c38y6AEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GaoB54m+/9ZWOO6JLkFqxN9DagT0C8yd0Sh/VQVhbfUItQYw/PxQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421558,
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
      "state": "tx_+NMLAfiEuEDUws8WPVfg0iJyxEqyi4lHua8G1AnK2eQ+cgMXBFGjsNH/FOXRK+cEM/TyaKdJBMQvsH/nbHTWYWwf+nf062cGuEDqKRRdlZu3BPqjK13UCR0+XH4MB4eGz6cX7j9iSnG4xiCwOYBE6ggbQsDI0IXAP5QXNbzlE/DMPJP55c38y6AEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GaoB54m+/9ZWOO6JLkFqxN9DagT0C8yd0Sh/VQVhbfUItQYw/PxQ=="
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
      "state": "tx_+NMLAfiEuEDUws8WPVfg0iJyxEqyi4lHua8G1AnK2eQ+cgMXBFGjsNH/FOXRK+cEM/TyaKdJBMQvsH/nbHTWYWwf+nf062cGuEDqKRRdlZu3BPqjK13UCR0+XH4MB4eGz6cX7j9iSnG4xiCwOYBE6ggbQsDI0IXAP5QXNbzlE/DMPJP55c38y6AEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GaoB54m+/9ZWOO6JLkFqxN9DagT0C8yd0Sh/VQVhbfUItQYw/PxQ=="
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 154
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
        "round": 154
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 154
  }
}
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
        "round": 154
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 154
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
      "caller_nonce": 154,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 154,
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 154
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
        "round": 154
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 154
  }
}
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
        "round": 154
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 154
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
      "caller_nonce": 154,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 154,
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
      "caller_nonce": 155,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 155,
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gZugwF5v2rnpDRCsUUDyDuHDouEmhvb5OLM8MOa6uHejTgEFUcPB",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
  "id": -576460752303421557,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuECrMPXPmhl26WjRphJwmct+PUj2NnmgbBm3pISrB5n7aEZoxMrtvzYPW1+xB/uWgrQEFP9z1ixVvYMH0eNruiMHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GboMBeb9q56Q0QrFFA8g7hw6LhJob2+TizPDDmurh3o04BtkY8+w=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421557,
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
      "signed_tx": "tx_+JELAfhCuECrMPXPmhl26WjRphJwmct+PUj2NnmgbBm3pISrB5n7aEZoxMrtvzYPW1+xB/uWgrQEFP9z1ixVvYMH0eNruiMHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GboMBeb9q56Q0QrFFA8g7hw6LhJob2+TizPDDmurh3o04BtkY8+w==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbhlvcmFjbGXRGvUq",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
  "id": -576460752303421556,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAsbTd/6Yu2M0BgiiYnvALKS/UI67DDdYkl0RBQnhGmhUheGwz5F94csDvNqzZLjCHvvb3i9UmApu+NZwXdEycDuECrMPXPmhl26WjRphJwmct+PUj2NnmgbBm3pISrB5n7aEZoxMrtvzYPW1+xB/uWgrQEFP9z1ixVvYMH0eNruiMHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GboMBeb9q56Q0QrFFA8g7hw6LhJob2+TizPDDmurh3o04BJwcEvA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421556,
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
      "state": "tx_+NMLAfiEuEAsbTd/6Yu2M0BgiiYnvALKS/UI67DDdYkl0RBQnhGmhUheGwz5F94csDvNqzZLjCHvvb3i9UmApu+NZwXdEycDuECrMPXPmhl26WjRphJwmct+PUj2NnmgbBm3pISrB5n7aEZoxMrtvzYPW1+xB/uWgrQEFP9z1ixVvYMH0eNruiMHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GboMBeb9q56Q0QrFFA8g7hw6LhJob2+TizPDDmurh3o04BJwcEvA=="
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
      "state": "tx_+NMLAfiEuEAsbTd/6Yu2M0BgiiYnvALKS/UI67DDdYkl0RBQnhGmhUheGwz5F94csDvNqzZLjCHvvb3i9UmApu+NZwXdEycDuECrMPXPmhl26WjRphJwmct+PUj2NnmgbBm3pISrB5n7aEZoxMrtvzYPW1+xB/uWgrQEFP9z1ixVvYMH0eNruiMHuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GboMBeb9q56Q0QrFFA8g7hw6LhJob2+TizPDDmurh3o04BJwcEvA=="
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 155
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
        "round": 155
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 155
  }
}
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
        "round": 155
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 155
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
      "caller_nonce": 155,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 155,
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 155
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
        "round": 155
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 155
  }
}
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
        "round": 155
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 155
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
      "caller_nonce": 155,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 155,
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
      "caller_nonce": 156,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 156,
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gZygjSaOJ8kr/AkxQP8K/oE2cuAXIp4k7nuV6L1cEixcExhgAUvP",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
  "id": -576460752303421555,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEAkoasgkpZD11UG64ip9N4CGO4xhiItyYpBJqU0/YlQsPU1t4x9szKYzt1ILvcopEXu47ceqpRu3IKMQzoQ3wIEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GcoI0mjifJK/wJMUD/Cv6BNnLgFyKeJO57lei9XBIsXBMYmQ6mEw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421555,
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
      "signed_tx": "tx_+JELAfhCuEAkoasgkpZD11UG64ip9N4CGO4xhiItyYpBJqU0/YlQsPU1t4x9szKYzt1ILvcopEXu47ceqpRu3IKMQzoQ3wIEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GcoI0mjifJK/wJMUD/Cv6BNnLgFyKeJO57lei9XBIsXBMYmQ6mEw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
  "id": -576460752303421554,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAkoasgkpZD11UG64ip9N4CGO4xhiItyYpBJqU0/YlQsPU1t4x9szKYzt1ILvcopEXu47ceqpRu3IKMQzoQ3wIEuED/XsnNKkZWELgdJHH5JTur2kNzEVVgIMOWVeT5E67FNQkTXXAy9MTozwfBa7Xa8Y196mJzARc4TtW8ebsBuLgEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GcoI0mjifJK/wJMUD/Cv6BNnLgFyKeJO57lei9XBIsXBMYzWB4AQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421554,
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
      "state": "tx_+NMLAfiEuEAkoasgkpZD11UG64ip9N4CGO4xhiItyYpBJqU0/YlQsPU1t4x9szKYzt1ILvcopEXu47ceqpRu3IKMQzoQ3wIEuED/XsnNKkZWELgdJHH5JTur2kNzEVVgIMOWVeT5E67FNQkTXXAy9MTozwfBa7Xa8Y196mJzARc4TtW8ebsBuLgEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GcoI0mjifJK/wJMUD/Cv6BNnLgFyKeJO57lei9XBIsXBMYzWB4AQ=="
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
      "state": "tx_+NMLAfiEuEAkoasgkpZD11UG64ip9N4CGO4xhiItyYpBJqU0/YlQsPU1t4x9szKYzt1ILvcopEXu47ceqpRu3IKMQzoQ3wIEuED/XsnNKkZWELgdJHH5JTur2kNzEVVgIMOWVeT5E67FNQkTXXAy9MTozwfBa7Xa8Y196mJzARc4TtW8ebsBuLgEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GcoI0mjifJK/wJMUD/Cv6BNnLgFyKeJO57lei9XBIsXBMYzWB4AQ=="
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 156
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
        "round": 156
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 156
  }
}
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
        "round": 156
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 156
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
      "caller_nonce": 156,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 156,
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 156
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
        "round": 156
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 156
  }
}
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
        "round": 156
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 156
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
      "caller_nonce": 156,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 156,
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
      "caller_nonce": 157,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 157,
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
        "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gZ2g4b+fSmP41hZBiw/0+I3wbLj4VpFE56GYQiE5+qMAZcCWRa6w",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
  "id": -576460752303421553,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuED9yPqfrUvuH1i1dow3440peo055w87zs+Gs9Fe0HVGlz4Xun3NJT9uZB2sOs8Q4Bt6WEVGDyNu9g40WKzA8aIGuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GdoOG/n0pj+NYWQYsP9PiN8Gy4+FaRROehmEIhOfqjAGXAyTSFIQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421553,
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
      "signed_tx": "tx_+JELAfhCuED9yPqfrUvuH1i1dow3440peo055w87zs+Gs9Fe0HVGlz4Xun3NJT9uZB2sOs8Q4Bt6WEVGDyNu9g40WKzA8aIGuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GdoOG/n0pj+NYWQYsP9PiN8Gy4+FaRROehmEIhOfqjAGXAyTSFIQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbjl1bmV4cGVjdGVkX2tleYh23nQ=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
  "id": -576460752303421552,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEBzvRRmLrZSIEyLZFbZrGT/Z0C74Wl5zrh+7aOl4I7U/Dbtu5wji1EyLEEXr18td4AmarjWHkZf1SJYS1pDv6MOuED9yPqfrUvuH1i1dow3440peo055w87zs+Gs9Fe0HVGlz4Xun3NJT9uZB2sOs8Q4Bt6WEVGDyNu9g40WKzA8aIGuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GdoOG/n0pj+NYWQYsP9PiN8Gy4+FaRROehmEIhOfqjAGXAUJWHTA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421552,
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
      "state": "tx_+NMLAfiEuEBzvRRmLrZSIEyLZFbZrGT/Z0C74Wl5zrh+7aOl4I7U/Dbtu5wji1EyLEEXr18td4AmarjWHkZf1SJYS1pDv6MOuED9yPqfrUvuH1i1dow3440peo055w87zs+Gs9Fe0HVGlz4Xun3NJT9uZB2sOs8Q4Bt6WEVGDyNu9g40WKzA8aIGuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GdoOG/n0pj+NYWQYsP9PiN8Gy4+FaRROehmEIhOfqjAGXAUJWHTA=="
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
      "state": "tx_+NMLAfiEuEBzvRRmLrZSIEyLZFbZrGT/Z0C74Wl5zrh+7aOl4I7U/Dbtu5wji1EyLEEXr18td4AmarjWHkZf1SJYS1pDv6MOuED9yPqfrUvuH1i1dow3440peo055w87zs+Gs9Fe0HVGlz4Xun3NJT9uZB2sOs8Q4Bt6WEVGDyNu9g40WKzA8aIGuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GdoOG/n0pj+NYWQYsP9PiN8Gy4+FaRROehmEIhOfqjAGXAUJWHTA=="
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 157
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
        "round": 157
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 157
  }
}
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
        "round": 157
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 157
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
      "caller_nonce": 157,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 157,
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 157
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
        "round": 157
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 157
  }
}
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
        "round": 157
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 157
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
      "caller_nonce": 157,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 157,
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
    "block_hash": "kh_nTjny4hWV15gwiiEqYPcmabb1GfPG4vKNA2BYNjNqFNUqW1w2",
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
      "caller_nonce": 158,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 158,
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gZ6gGDCYTOEW8v37lcc4fLNmeZfau7I/nNJcoyWN/6TIQQLgjVy3",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
  "id": -576460752303421551,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEBxA8uNIqjArpnUgrY9bNYCnwyNU+lSN+rbPL5YqmZSBUoBGxGBU4y0nMsUvNUJoIPpE84EeRNP5ekvAHgYGAgDuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GeoBgwmEzhFvL9+5XHOHyzZnmX2ruyP5zSXKMljf+kyEECWmu01g=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421551,
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
      "signed_tx": "tx_+JELAfhCuEBxA8uNIqjArpnUgrY9bNYCnwyNU+lSN+rbPL5YqmZSBUoBGxGBU4y0nMsUvNUJoIPpE84EeRNP5ekvAHgYGAgDuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GeoBgwmEzhFvL9+5XHOHyzZnmX2ruyP5zSXKMljf+kyEECWmu01g==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
          "call_stack": [],
          "caller_id": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
          "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
  "id": -576460752303421550,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEBxA8uNIqjArpnUgrY9bNYCnwyNU+lSN+rbPL5YqmZSBUoBGxGBU4y0nMsUvNUJoIPpE84EeRNP5ekvAHgYGAgDuEB1gALiWTw3NVT/7aq85YbD0Hfb0eFMzWUs9mBJgcWoylNoizFp742uGGAa7VASyb5ajxbweSo3rlSEx0swbVwEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GeoBgwmEzhFvL9+5XHOHyzZnmX2ruyP5zSXKMljf+kyEEC6hSO7A=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421550,
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
      "state": "tx_+NMLAfiEuEBxA8uNIqjArpnUgrY9bNYCnwyNU+lSN+rbPL5YqmZSBUoBGxGBU4y0nMsUvNUJoIPpE84EeRNP5ekvAHgYGAgDuEB1gALiWTw3NVT/7aq85YbD0Hfb0eFMzWUs9mBJgcWoylNoizFp742uGGAa7VASyb5ajxbweSo3rlSEx0swbVwEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GeoBgwmEzhFvL9+5XHOHyzZnmX2ruyP5zSXKMljf+kyEEC6hSO7A=="
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
      "state": "tx_+NMLAfiEuEBxA8uNIqjArpnUgrY9bNYCnwyNU+lSN+rbPL5YqmZSBUoBGxGBU4y0nMsUvNUJoIPpE84EeRNP5ekvAHgYGAgDuEB1gALiWTw3NVT/7aq85YbD0Hfb0eFMzWUs9mBJgcWoylNoizFp742uGGAa7VASyb5ajxbweSo3rlSEx0swbVwEuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GeoBgwmEzhFvL9+5XHOHyzZnmX2ruyP5zSXKMljf+kyEEC6hSO7A=="
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 158
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
        "round": 158
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 158
  }
}
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
        "round": 158
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 158
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
      "caller_nonce": 158,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 158,
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 158
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
        "round": 158
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 158
  }
}
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
        "round": 158
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 158
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
      "caller_nonce": 158,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 158,
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
      "caller_nonce": 159,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 159,
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
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
        "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
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
    "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBi9R6GIOfOwKXcXW2YkWO7k28fP9ikPEkRN07GJpmi53gZ+gxc0xJwUb7PNnI3yoexk1HX/kYpKIDU6yErORlVKRnRvK3cq5",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
  "id": -576460752303421549,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuECBMP2wO1oF4Qe1HNhX7tUTUUouy0qx3mHNC4oNvOJgxb1XfSMJgK/eux1lIwwEwqBtDDeLMnMb9fHKoGxtZAkBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GfoMXNMScFG+zzZyN8qHsZNR1/5GKSiA1OshKzkZVSkZ0b3rIx8w=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421549,
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
      "signed_tx": "tx_+JELAfhCuECBMP2wO1oF4Qe1HNhX7tUTUUouy0qx3mHNC4oNvOJgxb1XfSMJgK/eux1lIwwEwqBtDDeLMnMb9fHKoGxtZAkBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GfoMXNMScFG+zzZyN8qHsZNR1/5GKSiA1OshKzkZVSkZ0b3rIx8w==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FDY2ViOTNrVXFXc3ltai5jaGFpbi1taXNzaW5nX2tleebxHYo=",
          "call_stack": [],
          "caller_id": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
          "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
  "id": -576460752303421548,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEAKYlFiBck19k4FuP4+Pyi7LqK88enD0xRqn9K/u8LzHKRSGsdRAav9+xrVUVGSscqyNfNLmGWJJAiyfmtWChQGuECBMP2wO1oF4Qe1HNhX7tUTUUouy0qx3mHNC4oNvOJgxb1XfSMJgK/eux1lIwwEwqBtDDeLMnMb9fHKoGxtZAkBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GfoMXNMScFG+zzZyN8qHsZNR1/5GKSiA1OshKzkZVSkZ0bXBcCYQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421548,
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
      "state": "tx_+NMLAfiEuEAKYlFiBck19k4FuP4+Pyi7LqK88enD0xRqn9K/u8LzHKRSGsdRAav9+xrVUVGSscqyNfNLmGWJJAiyfmtWChQGuECBMP2wO1oF4Qe1HNhX7tUTUUouy0qx3mHNC4oNvOJgxb1XfSMJgK/eux1lIwwEwqBtDDeLMnMb9fHKoGxtZAkBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GfoMXNMScFG+zzZyN8qHsZNR1/5GKSiA1OshKzkZVSkZ0bXBcCYQ=="
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
      "state": "tx_+NMLAfiEuEAKYlFiBck19k4FuP4+Pyi7LqK88enD0xRqn9K/u8LzHKRSGsdRAav9+xrVUVGSscqyNfNLmGWJJAiyfmtWChQGuECBMP2wO1oF4Qe1HNhX7tUTUUouy0qx3mHNC4oNvOJgxb1XfSMJgK/eux1lIwwEwqBtDDeLMnMb9fHKoGxtZAkBuEn4RzkCoQYvUehiDnzsCl3F1tmJFju5NvHz/YpDxJETdOxiaZoud4GfoMXNMScFG+zzZyN8qHsZNR1/5GKSiA1OshKzkZVSkZ0bXBcCYQ=="
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 159
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
        "round": 159
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 159
  }
}
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
        "round": 159
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 159
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
      "caller_nonce": 159,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 159,
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 159
  }
}
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
        "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
        "round": 159
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "round": 159
  }
}
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
        "round": 159
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
    "round": 159
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
      "caller_nonce": 159,
      "contract_id": "ct_2NVvA7W9qwQqqNnbtQ6nsSYKXfDThTBNSmZPBqRwyjxkbssAu5",
      "gas_price": 1,
      "gas_used": 122,
      "height": 159,
      "log": [],
      "return_type": "ok",
      "return_value": "cb_f3HLyas="
    }
  },
  "version": 1
}
```
