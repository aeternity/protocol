
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RdKBwCJ505ieyrvXWr3paShKVC0/f8exBN35nOQJizGBTnaSYHSo=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
  "id": -576460752303421635,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED8XuMf4PN6AtEsSWS4MHmaoDibYO8VtFnk7XaOauy5SnOPVrTYcI2X0hpdBcGWj7HSdlljvXEOdS/4saVaoRwLuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXSgcAiedOYnsq711q96WkoSlQtP3/HsQTd+ZzkCYsxgU52CCx3G"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JALAfhCuED8XuMf4PN6AtEsSWS4MHmaoDibYO8VtFnk7XaOauy5SnOPVrTYcI2X0hpdBcGWj7HSdlljvXEOdS/4saVaoRwLuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXSgcAiedOYnsq711q96WkoSlQtP3/HsQTd+ZzkCYsxgU52CCx3G",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
  "id": -576460752303421634,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDDVF6DUHL+vELaIbiTiHU7cliRzyVWcY7IgWtOmn0XGL61tF3ZqJ6ORZ7c3uzITMfHwdTt83LGRCCDOa/VcuoEuED8XuMf4PN6AtEsSWS4MHmaoDibYO8VtFnk7XaOauy5SnOPVrTYcI2X0hpdBcGWj7HSdlljvXEOdS/4saVaoRwLuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXSgcAiedOYnsq711q96WkoSlQtP3/HsQTd+ZzkCYsxgU53q4xQH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEDDVF6DUHL+vELaIbiTiHU7cliRzyVWcY7IgWtOmn0XGL61tF3ZqJ6ORZ7c3uzITMfHwdTt83LGRCCDOa/VcuoEuED8XuMf4PN6AtEsSWS4MHmaoDibYO8VtFnk7XaOauy5SnOPVrTYcI2X0hpdBcGWj7HSdlljvXEOdS/4saVaoRwLuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXSgcAiedOYnsq711q96WkoSlQtP3/HsQTd+ZzkCYsxgU53q4xQH"
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
      "state": "tx_+NILAfiEuEDDVF6DUHL+vELaIbiTiHU7cliRzyVWcY7IgWtOmn0XGL61tF3ZqJ6ORZ7c3uzITMfHwdTt83LGRCCDOa/VcuoEuED8XuMf4PN6AtEsSWS4MHmaoDibYO8VtFnk7XaOauy5SnOPVrTYcI2X0hpdBcGWj7HSdlljvXEOdS/4saVaoRwLuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXSgcAiedOYnsq711q96WkoSlQtP3/HsQTd+ZzkCYsxgU53q4xQH"
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
    "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
    "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
      "caller_nonce": 117,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
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
        "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
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
    "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
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
        "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
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
    "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RdaBXUilZn1Obm8vaCd8q3mplZBdQxfAq1xrQ5U6NMW/+Uvkiiac=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
          "gas": 1000000,
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
    "signed_tx": "tx_+JALAfhCuECRBijfL0af5eqzOwRy2T0KXdmMGkh8zGYBlT6AyBaYGV6lqIIVJTr1/4Yu8ko2Lr3taO4/WWYbfb5ANRmJt7oGuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXWgV1IpWZ9Tm5vL2gnfKt5qZWQXUMXwKtca0OVOjTFv/lJdd7kT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JALAfhCuECRBijfL0af5eqzOwRy2T0KXdmMGkh8zGYBlT6AyBaYGV6lqIIVJTr1/4Yu8ko2Lr3taO4/WWYbfb5ANRmJt7oGuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXWgV1IpWZ9Tm5vL2gnfKt5qZWQXUMXwKtca0OVOjTFv/lJdd7kT",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
          "gas": 1000000,
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
    "signed_tx": "tx_+NILAfiEuECRBijfL0af5eqzOwRy2T0KXdmMGkh8zGYBlT6AyBaYGV6lqIIVJTr1/4Yu8ko2Lr3taO4/WWYbfb5ANRmJt7oGuECXa4u0CovTosFLPEAKod86LU6TgkyCJLuPU6Whr3fMMbG8gKarKjXhS9l4bbEoFhWTsc+9FUe9n8I1VV50nkwDuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXWgV1IpWZ9Tm5vL2gnfKt5qZWQXUMXwKtca0OVOjTFv/lJcBZBU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuECRBijfL0af5eqzOwRy2T0KXdmMGkh8zGYBlT6AyBaYGV6lqIIVJTr1/4Yu8ko2Lr3taO4/WWYbfb5ANRmJt7oGuECXa4u0CovTosFLPEAKod86LU6TgkyCJLuPU6Whr3fMMbG8gKarKjXhS9l4bbEoFhWTsc+9FUe9n8I1VV50nkwDuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXWgV1IpWZ9Tm5vL2gnfKt5qZWQXUMXwKtca0OVOjTFv/lJcBZBU"
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
      "state": "tx_+NILAfiEuECRBijfL0af5eqzOwRy2T0KXdmMGkh8zGYBlT6AyBaYGV6lqIIVJTr1/4Yu8ko2Lr3taO4/WWYbfb5ANRmJt7oGuECXa4u0CovTosFLPEAKod86LU6TgkyCJLuPU6Whr3fMMbG8gKarKjXhS9l4bbEoFhWTsc+9FUe9n8I1VV50nkwDuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXWgV1IpWZ9Tm5vL2gnfKt5qZWQXUMXwKtca0OVOjTFv/lJcBZBU"
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
    "round": 117
  }
}
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 117
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 117,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
    "round": 117
  }
}
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 117
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 117,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
    "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
      "caller_nonce": 118,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
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
        "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
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
    "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
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
        "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
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
    "block_hash": "kh_hQjNqJSuFuZLwDSHhdTy68wYrRB4hynfraaGmpYbE11x2GMzp",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RdqDVNS4dsXlOEs0xv4eS1EAF2V9C816zY4LuBWyXCHctmnlxMCA=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
          "gas": 1000000,
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
    "signed_tx": "tx_+JALAfhCuEBIFFfrupqX6K8quBt3sUuJU5jjRt2xsXLgg5XA1uD1ZOwzgbk+tdBiNaLv7TLzYPqT7cG/OBTpva6vmqIblWsOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXag1TUuHbF5ThLNMb+HktRABdlfQvNes2OC7gVslwh3LZoJjjhe"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JALAfhCuEBIFFfrupqX6K8quBt3sUuJU5jjRt2xsXLgg5XA1uD1ZOwzgbk+tdBiNaLv7TLzYPqT7cG/OBTpva6vmqIblWsOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXag1TUuHbF5ThLNMb+HktRABdlfQvNes2OC7gVslwh3LZoJjjhe",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
          "gas": 1000000,
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
    "signed_tx": "tx_+NILAfiEuEBGWtvHwFJ0R0sGxrYMYm2S2HuIVrNaPRshOVO45S87gHxZ/qBBnlvr1Zf+9x5v4UrsnsfXEgJYj1Rp7urU7Y0DuEBIFFfrupqX6K8quBt3sUuJU5jjRt2xsXLgg5XA1uD1ZOwzgbk+tdBiNaLv7TLzYPqT7cG/OBTpva6vmqIblWsOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXag1TUuHbF5ThLNMb+HktRABdlfQvNes2OC7gVslwh3LZoS4ez1"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBGWtvHwFJ0R0sGxrYMYm2S2HuIVrNaPRshOVO45S87gHxZ/qBBnlvr1Zf+9x5v4UrsnsfXEgJYj1Rp7urU7Y0DuEBIFFfrupqX6K8quBt3sUuJU5jjRt2xsXLgg5XA1uD1ZOwzgbk+tdBiNaLv7TLzYPqT7cG/OBTpva6vmqIblWsOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXag1TUuHbF5ThLNMb+HktRABdlfQvNes2OC7gVslwh3LZoS4ez1"
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
      "state": "tx_+NILAfiEuEBGWtvHwFJ0R0sGxrYMYm2S2HuIVrNaPRshOVO45S87gHxZ/qBBnlvr1Zf+9x5v4UrsnsfXEgJYj1Rp7urU7Y0DuEBIFFfrupqX6K8quBt3sUuJU5jjRt2xsXLgg5XA1uD1ZOwzgbk+tdBiNaLv7TLzYPqT7cG/OBTpva6vmqIblWsOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXag1TUuHbF5ThLNMb+HktRABdlfQvNes2OC7gVslwh3LZoS4ez1"
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
    "round": 118
  }
}
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 118
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 118,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
    "round": 118
  }
}
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 118
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 118,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
      "caller_nonce": 119,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Rd6DH1kbBRwgWG7kJFnSIL9oYRavtygJkngXrbbHJdw9RWWJedfI=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
          "gas": 1000000,
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
    "signed_tx": "tx_+JALAfhCuEADE2zO4uIgsMYs+hclvgwWfLZ+7QomAqS4sAu/PY3+97CoGqVvfCblKPMuFOtM3yld3tmobFLm9viWT+ndOGEOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXegx9ZGwUcIFhu5CRZ0iC/aGEWr7coCZJ4F622xyXcPUVnaLxib"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JALAfhCuEADE2zO4uIgsMYs+hclvgwWfLZ+7QomAqS4sAu/PY3+97CoGqVvfCblKPMuFOtM3yld3tmobFLm9viWT+ndOGEOuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXegx9ZGwUcIFhu5CRZ0iC/aGEWr7coCZJ4F622xyXcPUVnaLxib",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
          "gas": 1000000,
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
    "signed_tx": "tx_+NILAfiEuEADE2zO4uIgsMYs+hclvgwWfLZ+7QomAqS4sAu/PY3+97CoGqVvfCblKPMuFOtM3yld3tmobFLm9viWT+ndOGEOuEDUguU4RJHXJSbqKa7rpU8EvqMcMw6eT7tchpkOY/atqJ0AoHz+nNiOxHWczsFJ1PlAmUou/6vkN6IEDhNfIbwMuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXegx9ZGwUcIFhu5CRZ0iC/aGEWr7coCZJ4F622xyXcPUVnjfUIE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEADE2zO4uIgsMYs+hclvgwWfLZ+7QomAqS4sAu/PY3+97CoGqVvfCblKPMuFOtM3yld3tmobFLm9viWT+ndOGEOuEDUguU4RJHXJSbqKa7rpU8EvqMcMw6eT7tchpkOY/atqJ0AoHz+nNiOxHWczsFJ1PlAmUou/6vkN6IEDhNfIbwMuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXegx9ZGwUcIFhu5CRZ0iC/aGEWr7coCZJ4F622xyXcPUVnjfUIE"
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
      "state": "tx_+NILAfiEuEADE2zO4uIgsMYs+hclvgwWfLZ+7QomAqS4sAu/PY3+97CoGqVvfCblKPMuFOtM3yld3tmobFLm9viWT+ndOGEOuEDUguU4RJHXJSbqKa7rpU8EvqMcMw6eT7tchpkOY/atqJ0AoHz+nNiOxHWczsFJ1PlAmUou/6vkN6IEDhNfIbwMuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXegx9ZGwUcIFhu5CRZ0iC/aGEWr7coCZJ4F622xyXcPUVnjfUIE"
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
    "round": 119
  }
}
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 119
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 119,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
    "round": 119
  }
}
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 119
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 119,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
      "caller_nonce": 120,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8ReKBYs9uqNklBPwWxqrGrqVeu6AbfJUw0HyXySSsP6+Wa8rmPQoE=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
          "gas": 1000000,
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
    "signed_tx": "tx_+JALAfhCuEAsxqySwYIVvHJ4yC4rT0wCUh8WtzBtbrGwxzeX0i5mCchV0jmWhz4YdEquLfhjR4HUBDhdiIN4+RA+IkmoRFoEuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXigWLPbqjZJQT8Fsaqxq6lXrugG3yVMNB8l8kkrD+vlmvJ9uoqK"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JALAfhCuEAsxqySwYIVvHJ4yC4rT0wCUh8WtzBtbrGwxzeX0i5mCchV0jmWhz4YdEquLfhjR4HUBDhdiIN4+RA+IkmoRFoEuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXigWLPbqjZJQT8Fsaqxq6lXrugG3yVMNB8l8kkrD+vlmvJ9uoqK",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjlhY2NvdW50X3B1YmtledlDVjc=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
          "gas": 1000000,
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
    "signed_tx": "tx_+NILAfiEuEAktAeAnIgKil86dbbGkKUU/5vuD7v2u7iLSFErQ/HSAKrFtdpwmZcRLgahfNW4prSMwOyjz2yG1JVnTsoMlRwPuEAsxqySwYIVvHJ4yC4rT0wCUh8WtzBtbrGwxzeX0i5mCchV0jmWhz4YdEquLfhjR4HUBDhdiIN4+RA+IkmoRFoEuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXigWLPbqjZJQT8Fsaqxq6lXrugG3yVMNB8l8kkrD+vlmvLGPvc+"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAktAeAnIgKil86dbbGkKUU/5vuD7v2u7iLSFErQ/HSAKrFtdpwmZcRLgahfNW4prSMwOyjz2yG1JVnTsoMlRwPuEAsxqySwYIVvHJ4yC4rT0wCUh8WtzBtbrGwxzeX0i5mCchV0jmWhz4YdEquLfhjR4HUBDhdiIN4+RA+IkmoRFoEuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXigWLPbqjZJQT8Fsaqxq6lXrugG3yVMNB8l8kkrD+vlmvLGPvc+"
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
      "state": "tx_+NILAfiEuEAktAeAnIgKil86dbbGkKUU/5vuD7v2u7iLSFErQ/HSAKrFtdpwmZcRLgahfNW4prSMwOyjz2yG1JVnTsoMlRwPuEAsxqySwYIVvHJ4yC4rT0wCUh8WtzBtbrGwxzeX0i5mCchV0jmWhz4YdEquLfhjR4HUBDhdiIN4+RA+IkmoRFoEuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXigWLPbqjZJQT8Fsaqxq6lXrugG3yVMNB8l8kkrD+vlmvLGPvc+"
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
    "round": 120
  }
}
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 120
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 120,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
    "round": 120
  }
}
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 120
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 120,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
      "caller_nonce": 121,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8ReaAsve5bU2MzVuHsNtaJcGtoS/1NIhtxg7YTuKy7laVacYTpFus=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
          "gas": 1000000,
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
    "signed_tx": "tx_+JALAfhCuECx/QMAYKznd7fvPKstNS4cBLvK+mA5bS/czE+YxEJhHCKQFpJIC3B1VUA9rpb3eV73Im+h8lY6ifZlJNcQuyIIuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXmgLL3uW1NjM1bh7DbWiXBraEv9TSIbcYO2E7isu5WlWnFPp02A"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JALAfhCuECx/QMAYKznd7fvPKstNS4cBLvK+mA5bS/czE+YxEJhHCKQFpJIC3B1VUA9rpb3eV73Im+h8lY6ifZlJNcQuyIIuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXmgLL3uW1NjM1bh7DbWiXBraEv9TSIbcYO2E7isu5WlWnFPp02A",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
          "gas": 1000000,
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
    "signed_tx": "tx_+NILAfiEuECVbP846fiexNXXKCCogTT4eLNggpQaYmGH2tm+e1Pq2frf2paGPisMaHDEEP3iQ27car0gARgOuw0dzHWAhSYFuECx/QMAYKznd7fvPKstNS4cBLvK+mA5bS/czE+YxEJhHCKQFpJIC3B1VUA9rpb3eV73Im+h8lY6ifZlJNcQuyIIuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXmgLL3uW1NjM1bh7DbWiXBraEv9TSIbcYO2E7isu5WlWnEeobvb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuECVbP846fiexNXXKCCogTT4eLNggpQaYmGH2tm+e1Pq2frf2paGPisMaHDEEP3iQ27car0gARgOuw0dzHWAhSYFuECx/QMAYKznd7fvPKstNS4cBLvK+mA5bS/czE+YxEJhHCKQFpJIC3B1VUA9rpb3eV73Im+h8lY6ifZlJNcQuyIIuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXmgLL3uW1NjM1bh7DbWiXBraEv9TSIbcYO2E7isu5WlWnEeobvb"
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
      "state": "tx_+NILAfiEuECVbP846fiexNXXKCCogTT4eLNggpQaYmGH2tm+e1Pq2frf2paGPisMaHDEEP3iQ27car0gARgOuw0dzHWAhSYFuECx/QMAYKznd7fvPKstNS4cBLvK+mA5bS/czE+YxEJhHCKQFpJIC3B1VUA9rpb3eV73Im+h8lY6ifZlJNcQuyIIuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXmgLL3uW1NjM1bh7DbWiXBraEv9TSIbcYO2E7isu5WlWnEeobvb"
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
    "round": 121
  }
}
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 121
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 121,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
    "round": 121
  }
}
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 121
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 121,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
      "caller_nonce": 122,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8ReqDtHiD+XBGBty12bZ38yzQN2HpY97JAYRNuFYfakmUPcbeurTM=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
          "gas": 1000000,
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
    "signed_tx": "tx_+JALAfhCuEBL94sa7T2BhsOsR0fDtVXIEHoH0DXTCbZgSAgrZLadUwUnE2utwEfcSZLR5rpYYejmdf2bASCDC7EM/3jIv7QIuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXqg7R4g/lwRgbctdm2d/Ms0Ddh6WPeyQGETbhWH2pJlD3GeFv8W"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JALAfhCuEBL94sa7T2BhsOsR0fDtVXIEHoH0DXTCbZgSAgrZLadUwUnE2utwEfcSZLR5rpYYejmdf2bASCDC7EM/3jIv7QIuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXqg7R4g/lwRgbctdm2d/Ms0Ddh6WPeyQGETbhWH2pJlD3GeFv8W",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbhlvcmFjbGUxMhii",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
          "gas": 1000000,
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
    "signed_tx": "tx_+NILAfiEuEBL94sa7T2BhsOsR0fDtVXIEHoH0DXTCbZgSAgrZLadUwUnE2utwEfcSZLR5rpYYejmdf2bASCDC7EM/3jIv7QIuEC7Zdx8aHND6kzOABff03uSYKlnyeipGgW/se8nlxZD6u9xLkJRB+P+blnvr51UCe3W0nPtQKVlXd0bgoj2UKsCuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXqg7R4g/lwRgbctdm2d/Ms0Ddh6WPeyQGETbhWH2pJlD3HWJSMk"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBL94sa7T2BhsOsR0fDtVXIEHoH0DXTCbZgSAgrZLadUwUnE2utwEfcSZLR5rpYYejmdf2bASCDC7EM/3jIv7QIuEC7Zdx8aHND6kzOABff03uSYKlnyeipGgW/se8nlxZD6u9xLkJRB+P+blnvr51UCe3W0nPtQKVlXd0bgoj2UKsCuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXqg7R4g/lwRgbctdm2d/Ms0Ddh6WPeyQGETbhWH2pJlD3HWJSMk"
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
      "state": "tx_+NILAfiEuEBL94sa7T2BhsOsR0fDtVXIEHoH0DXTCbZgSAgrZLadUwUnE2utwEfcSZLR5rpYYejmdf2bASCDC7EM/3jIv7QIuEC7Zdx8aHND6kzOABff03uSYKlnyeipGgW/se8nlxZD6u9xLkJRB+P+blnvr51UCe3W0nPtQKVlXd0bgoj2UKsCuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXqg7R4g/lwRgbctdm2d/Ms0Ddh6WPeyQGETbhWH2pJlD3HWJSMk"
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
    "round": 122
  }
}
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 122
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 122,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
    "round": 122
  }
}
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 122
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 122,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
      "caller_nonce": 123,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Re6DiJtLXU6De3e1LyYtSVJ6JG4JVZNmd4D9XoNT3MMuCdDNR5IQ=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
          "gas": 1000000,
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
    "signed_tx": "tx_+JALAfhCuEDkKjjxH9UdFU8wCnbko5346BZsGbZGNamzbgBUw4UAUYu9wJQpBqzNzoIV/ynDTjMZtKhFwuanuHTh8qTGmOAAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXug4ibS11Og3t3tS8mLUlSeiRuCVWTZneA/V6DU9zDLgnQCraG+"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JALAfhCuEDkKjjxH9UdFU8wCnbko5346BZsGbZGNamzbgBUw4UAUYu9wJQpBqzNzoIV/ynDTjMZtKhFwuanuHTh8qTGmOAAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXug4ibS11Og3t3tS8mLUlSeiRuCVWTZneA/V6DU9zDLgnQCraG+",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
          "gas": 1000000,
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
    "signed_tx": "tx_+NILAfiEuEDayAlau+LTJmbfhrTGLzAvKD0Rj8Pe2n9gJTgXZqjFVl9d4gMiKBX0zScum1GZqSIuuaN0mHSANjtUtLmP7J4NuEDkKjjxH9UdFU8wCnbko5346BZsGbZGNamzbgBUw4UAUYu9wJQpBqzNzoIV/ynDTjMZtKhFwuanuHTh8qTGmOAAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXug4ibS11Og3t3tS8mLUlSeiRuCVWTZneA/V6DU9zDLgnRlvDIC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEDayAlau+LTJmbfhrTGLzAvKD0Rj8Pe2n9gJTgXZqjFVl9d4gMiKBX0zScum1GZqSIuuaN0mHSANjtUtLmP7J4NuEDkKjjxH9UdFU8wCnbko5346BZsGbZGNamzbgBUw4UAUYu9wJQpBqzNzoIV/ynDTjMZtKhFwuanuHTh8qTGmOAAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXug4ibS11Og3t3tS8mLUlSeiRuCVWTZneA/V6DU9zDLgnRlvDIC"
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
      "state": "tx_+NILAfiEuEDayAlau+LTJmbfhrTGLzAvKD0Rj8Pe2n9gJTgXZqjFVl9d4gMiKBX0zScum1GZqSIuuaN0mHSANjtUtLmP7J4NuEDkKjjxH9UdFU8wCnbko5346BZsGbZGNamzbgBUw4UAUYu9wJQpBqzNzoIV/ynDTjMZtKhFwuanuHTh8qTGmOAAuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXug4ibS11Og3t3tS8mLUlSeiRuCVWTZneA/V6DU9zDLgnRlvDIC"
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
    "round": 123
  }
}
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 123
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 123,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
    "round": 123
  }
}
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 123
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 123,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
      "caller_nonce": 124,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RfKDxrMi5ll2j63rzQGyeg1qXalraVhcrFU9KChoqJGdNUcYpaRA=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
          "gas": 1000000,
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
    "signed_tx": "tx_+JALAfhCuEDd+vxqj6xrB7O8+GLKy2wpQ5yMnmdQDxHjPoAxqZbQ40QD9HdQXyYGdLYlJBeGUzMURRQXbuisk9Onv9vpsIMJuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXyg8azIuZZdo+t680BsnoNal2pa2lYXKxVPSgoaKiRnTVEgwzGQ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JALAfhCuEDd+vxqj6xrB7O8+GLKy2wpQ5yMnmdQDxHjPoAxqZbQ40QD9HdQXyYGdLYlJBeGUzMURRQXbuisk9Onv9vpsIMJuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXyg8azIuZZdo+t680BsnoNal2pa2lYXKxVPSgoaKiRnTVEgwzGQ",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbjl1bmV4cGVjdGVkX2tleWBJk2s=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
          "gas": 1000000,
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
    "signed_tx": "tx_+NILAfiEuEBuCHrO4capVyxJkoH57ARq1P+eW5k9YP3jyA2/vrSUBMIcOVYJdIt6gppWnRt7Q4xPDXhrL220HRfXlKfU2P0DuEDd+vxqj6xrB7O8+GLKy2wpQ5yMnmdQDxHjPoAxqZbQ40QD9HdQXyYGdLYlJBeGUzMURRQXbuisk9Onv9vpsIMJuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXyg8azIuZZdo+t680BsnoNal2pa2lYXKxVPSgoaKiRnTVE3ghhl"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEBuCHrO4capVyxJkoH57ARq1P+eW5k9YP3jyA2/vrSUBMIcOVYJdIt6gppWnRt7Q4xPDXhrL220HRfXlKfU2P0DuEDd+vxqj6xrB7O8+GLKy2wpQ5yMnmdQDxHjPoAxqZbQ40QD9HdQXyYGdLYlJBeGUzMURRQXbuisk9Onv9vpsIMJuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXyg8azIuZZdo+t680BsnoNal2pa2lYXKxVPSgoaKiRnTVE3ghhl"
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
      "state": "tx_+NILAfiEuEBuCHrO4capVyxJkoH57ARq1P+eW5k9YP3jyA2/vrSUBMIcOVYJdIt6gppWnRt7Q4xPDXhrL220HRfXlKfU2P0DuEDd+vxqj6xrB7O8+GLKy2wpQ5yMnmdQDxHjPoAxqZbQ40QD9HdQXyYGdLYlJBeGUzMURRQXbuisk9Onv9vpsIMJuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEXyg8azIuZZdo+t680BsnoNal2pa2lYXKxVPSgoaKiRnTVE3ghhl"
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
    "round": 124
  }
}
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 124
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 124,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
    "round": 124
  }
}
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 124
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 124,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
      "caller_nonce": 125,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RfaDdX9O7Gs+DEngsazimBFcoEugdhBE2iQGyta0IEsEWyW9LsSg=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
          "gas": 1000000,
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
    "signed_tx": "tx_+JALAfhCuEAnvKSF8zfdK44EfwpkHR4boYdYbX3JR1rD61Nq6xlcfEMvMj4CPzEBPaN7TtV6XfO8M7GJ8/mwAEg+8h+GfGUJuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEX2g3V/TuxrPgxJ4LGs4pgRXKBLoHYQRNokBsrWtCBLBFskuEVtZ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JALAfhCuEAnvKSF8zfdK44EfwpkHR4boYdYbX3JR1rD61Nq6xlcfEMvMj4CPzEBPaN7TtV6XfO8M7GJ8/mwAEg+8h+GfGUJuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEX2g3V/TuxrPgxJ4LGs4pgRXKBLoHYQRNokBsrWtCBLBFskuEVtZ",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
          "gas": 1000000,
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
    "signed_tx": "tx_+NILAfiEuEAnvKSF8zfdK44EfwpkHR4boYdYbX3JR1rD61Nq6xlcfEMvMj4CPzEBPaN7TtV6XfO8M7GJ8/mwAEg+8h+GfGUJuEAugWhu9Mr2t3irWgcUAafcY+FQXWXwv7X67RNM7ab1sFg75YLVyOur/1TtUmrTwyblrmn5ZycDNvq3rBWlyzkFuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEX2g3V/TuxrPgxJ4LGs4pgRXKBLoHYQRNokBsrWtCBLBFslZvOvg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAnvKSF8zfdK44EfwpkHR4boYdYbX3JR1rD61Nq6xlcfEMvMj4CPzEBPaN7TtV6XfO8M7GJ8/mwAEg+8h+GfGUJuEAugWhu9Mr2t3irWgcUAafcY+FQXWXwv7X67RNM7ab1sFg75YLVyOur/1TtUmrTwyblrmn5ZycDNvq3rBWlyzkFuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEX2g3V/TuxrPgxJ4LGs4pgRXKBLoHYQRNokBsrWtCBLBFslZvOvg"
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
      "state": "tx_+NILAfiEuEAnvKSF8zfdK44EfwpkHR4boYdYbX3JR1rD61Nq6xlcfEMvMj4CPzEBPaN7TtV6XfO8M7GJ8/mwAEg+8h+GfGUJuEAugWhu9Mr2t3irWgcUAafcY+FQXWXwv7X67RNM7ab1sFg75YLVyOur/1TtUmrTwyblrmn5ZycDNvq3rBWlyzkFuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEX2g3V/TuxrPgxJ4LGs4pgRXKBLoHYQRNokBsrWtCBLBFslZvOvg"
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
    "round": 125
  }
}
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 125
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 125,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
    "round": 125
  }
}
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 125
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 125,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
      "caller_nonce": 126,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
  }
}
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
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
        "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
        "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
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
    "block_hash": "kh_Qv6psn99gbcMo5dxUmFWrgkwRAaUmhapQ93koDYuWH8jpqUpC",
    "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX"
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RfqANkeYhSu6Fkf7nr19VJXlv29fTFTVxTFP3AxXvox51cSeCcwM=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
          "gas": 1000000,
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
    "signed_tx": "tx_+JALAfhCuEA59ikRJ0/NYDUeneGfXSCyNSFHh3jYkCTsymNRf73I1+DAFGeKeEhzubwOO6A+Qt8g1hGNLEqKBuWE7hvibc0FuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEX6gDZHmIUruhZH+569fVSV5b9vX0xU1cUxT9wMV76MedXGrNrZG"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JALAfhCuEA59ikRJ0/NYDUeneGfXSCyNSFHh3jYkCTsymNRf73I1+DAFGeKeEhzubwOO6A+Qt8g1hGNLEqKBuWE7hvibc0FuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEX6gDZHmIUruhZH+569fVSV5b9vX0xU1cUxT9wMV76MedXGrNrZG",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1FFQ293cVNCMTFlOTU1WC5jaGFpbi1taXNzaW5nX2tleT7eeY8=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
          "gas": 1000000,
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
    "signed_tx": "tx_+NILAfiEuEA59ikRJ0/NYDUeneGfXSCyNSFHh3jYkCTsymNRf73I1+DAFGeKeEhzubwOO6A+Qt8g1hGNLEqKBuWE7hvibc0FuEDAdswNrFwHvamQhlKUqldH+Q2xCrKf9BD7SkrfPQkKggFBhETUKyxvyAdzEy9WXeZGNH2L3lMptqyPB3rQxFMCuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEX6gDZHmIUruhZH+569fVSV5b9vX0xU1cUxT9wMV76MedXEo6hgQ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEA59ikRJ0/NYDUeneGfXSCyNSFHh3jYkCTsymNRf73I1+DAFGeKeEhzubwOO6A+Qt8g1hGNLEqKBuWE7hvibc0FuEDAdswNrFwHvamQhlKUqldH+Q2xCrKf9BD7SkrfPQkKggFBhETUKyxvyAdzEy9WXeZGNH2L3lMptqyPB3rQxFMCuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEX6gDZHmIUruhZH+569fVSV5b9vX0xU1cUxT9wMV76MedXEo6hgQ"
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
      "state": "tx_+NILAfiEuEA59ikRJ0/NYDUeneGfXSCyNSFHh3jYkCTsymNRf73I1+DAFGeKeEhzubwOO6A+Qt8g1hGNLEqKBuWE7hvibc0FuEDAdswNrFwHvamQhlKUqldH+Q2xCrKf9BD7SkrfPQkKggFBhETUKyxvyAdzEy9WXeZGNH2L3lMptqyPB3rQxFMCuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEX6gDZHmIUruhZH+569fVSV5b9vX0xU1cUxT9wMV76MedXEo6hgQ"
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
    "round": 126
  }
}
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 126
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 126,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
    "round": 126
  }
}
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
        "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 126
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 126,
      "contract_id": "ct_fiwr3WLynyJcZ3rwsxzx2tYAdD5TRaQ4Ta3TLNdu8X41KpCcX",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8Rf6BWJDqtpjGHIH/rZL0E7G4hpPWPH2c2u96j+6upmT2RXmziffs=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
  "id": -576460752303421613,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAVab6Cb+lwXreafocIME3xrI9oJcNuTLwaQlw5ubYMACuQa/Mv6Tzk1rsZaM+31l3t5bNffrTbAE1gSUfka14EuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEX+gViQ6raYxhyB/62S9BOxuIaT1jx9nNrveo/urqZk9kV41Xkl7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JALAfhCuEAVab6Cb+lwXreafocIME3xrI9oJcNuTLwaQlw5ubYMACuQa/Mv6Tzk1rsZaM+31l3t5bNffrTbAE1gSUfka14EuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEX+gViQ6raYxhyB/62S9BOxuIaT1jx9nNrveo/urqZk9kV41Xkl7",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
  "id": -576460752303421612,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAVab6Cb+lwXreafocIME3xrI9oJcNuTLwaQlw5ubYMACuQa/Mv6Tzk1rsZaM+31l3t5bNffrTbAE1gSUfka14EuEDvMXXk6ObRCRapqkDoSOhwJSP/VCLCuzK8V0k0Nn9dZNHHYevhhgW7ZQyYdUER3ptffuwizDmENlqX6dUc47cDuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEX+gViQ6raYxhyB/62S9BOxuIaT1jx9nNrveo/urqZk9kV5XfNuI"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NILAfiEuEAVab6Cb+lwXreafocIME3xrI9oJcNuTLwaQlw5ubYMACuQa/Mv6Tzk1rsZaM+31l3t5bNffrTbAE1gSUfka14EuEDvMXXk6ObRCRapqkDoSOhwJSP/VCLCuzK8V0k0Nn9dZNHHYevhhgW7ZQyYdUER3ptffuwizDmENlqX6dUc47cDuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEX+gViQ6raYxhyB/62S9BOxuIaT1jx9nNrveo/urqZk9kV5XfNuI"
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
      "state": "tx_+NILAfiEuEAVab6Cb+lwXreafocIME3xrI9oJcNuTLwaQlw5ubYMACuQa/Mv6Tzk1rsZaM+31l3t5bNffrTbAE1gSUfka14EuEDvMXXk6ObRCRapqkDoSOhwJSP/VCLCuzK8V0k0Nn9dZNHHYevhhgW7ZQyYdUER3ptffuwizDmENlqX6dUc47cDuEj4RjkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEX+gViQ6raYxhyB/62S9BOxuIaT1jx9nNrveo/urqZk9kV5XfNuI"
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
    "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
    "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
    "call_data": "ABCDEFG",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
      "caller_nonce": 128,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
        "call_data": "ABCDEFG",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
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
        "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
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
    "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
    "call_data": "ABCDEFG",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
        "call_data": "ABCDEFG",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
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
        "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
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
    "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgYCgC+cr8mvhdR6ZEb3MnQ5eqwSfU+Tlv9K9Pbcd+Kh72jRa4PPG",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEDE0RSGHJB4sHC3Q0mEiGkdPjRL4iL9Kp+CfU9k/Twj2UfGCLnh9di82khq7D8V7V3AxE2ci5pu2CN70jxFoWkMuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGAoAvnK/Jr4XUemRG9zJ0OXqsEn1Pk5b/SvT23Hfioe9o0KRJF6w=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEDE0RSGHJB4sHC3Q0mEiGkdPjRL4iL9Kp+CfU9k/Twj2UfGCLnh9di82khq7D8V7V3AxE2ci5pu2CN70jxFoWkMuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGAoAvnK/Jr4XUemRG9zJ0OXqsEn1Pk5b/SvT23Hfioe9o0KRJF6w==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEA4Le7fCoaqbL2uEG/oUNLY6pXnvRhwac+IubpYcJ9xFGgmKY7Cov0Kp5PL1zsbzua4qWW4uKcruIg4Y3tqpY8NuEDE0RSGHJB4sHC3Q0mEiGkdPjRL4iL9Kp+CfU9k/Twj2UfGCLnh9di82khq7D8V7V3AxE2ci5pu2CN70jxFoWkMuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGAoAvnK/Jr4XUemRG9zJ0OXqsEn1Pk5b/SvT23Hfioe9o0jzagnw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEA4Le7fCoaqbL2uEG/oUNLY6pXnvRhwac+IubpYcJ9xFGgmKY7Cov0Kp5PL1zsbzua4qWW4uKcruIg4Y3tqpY8NuEDE0RSGHJB4sHC3Q0mEiGkdPjRL4iL9Kp+CfU9k/Twj2UfGCLnh9di82khq7D8V7V3AxE2ci5pu2CN70jxFoWkMuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGAoAvnK/Jr4XUemRG9zJ0OXqsEn1Pk5b/SvT23Hfioe9o0jzagnw=="
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
      "state": "tx_+NMLAfiEuEA4Le7fCoaqbL2uEG/oUNLY6pXnvRhwac+IubpYcJ9xFGgmKY7Cov0Kp5PL1zsbzua4qWW4uKcruIg4Y3tqpY8NuEDE0RSGHJB4sHC3Q0mEiGkdPjRL4iL9Kp+CfU9k/Twj2UfGCLnh9di82khq7D8V7V3AxE2ci5pu2CN70jxFoWkMuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGAoAvnK/Jr4XUemRG9zJ0OXqsEn1Pk5b/SvT23Hfioe9o0jzagnw=="
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
    "round": 128
  }
}
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 128
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 128,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
    "round": 128
  }
}
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 128
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 128,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
    "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
    "call_data": "ABCDEFG",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
      "caller_nonce": 129,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
        "call_data": "ABCDEFG",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
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
        "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
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
    "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
    "call_data": "ABCDEFG",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
        "call_data": "ABCDEFG",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
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
        "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
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
    "block_hash": "kh_D9ioxGj1RaPVYMKor5PMLhKpnyiBkfT6VqG234pXivtG9gxE7",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgYGgmbFT3ETmrHkZITN3kucIrpMxjI2BgHsdNztVdpiJN1D+dHR/",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEDft68681T2f0dcB84kSdzL4S70lk4yo6lB7AXjVbeE+x4Ax9lZmLFzz0bLbNKgQ0PIb66M2JV804tEsV9v1jMCuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGBoJmxU9xE5qx5GSEzd5LnCK6TMYyNgYB7HTc7VXaYiTdQmGQDig=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEDft68681T2f0dcB84kSdzL4S70lk4yo6lB7AXjVbeE+x4Ax9lZmLFzz0bLbNKgQ0PIb66M2JV804tEsV9v1jMCuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGBoJmxU9xE5qx5GSEzd5LnCK6TMYyNgYB7HTc7VXaYiTdQmGQDig==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEDYmlenCbNh0/5k0LofBi2+EgNHI9+Qva+8i1IwnV+aQ3KGDWA1L/NOlro4PmWorEQhYpLqmvbTQ/icL5lkAosMuEDft68681T2f0dcB84kSdzL4S70lk4yo6lB7AXjVbeE+x4Ax9lZmLFzz0bLbNKgQ0PIb66M2JV804tEsV9v1jMCuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGBoJmxU9xE5qx5GSEzd5LnCK6TMYyNgYB7HTc7VXaYiTdQntlF7A=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEDYmlenCbNh0/5k0LofBi2+EgNHI9+Qva+8i1IwnV+aQ3KGDWA1L/NOlro4PmWorEQhYpLqmvbTQ/icL5lkAosMuEDft68681T2f0dcB84kSdzL4S70lk4yo6lB7AXjVbeE+x4Ax9lZmLFzz0bLbNKgQ0PIb66M2JV804tEsV9v1jMCuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGBoJmxU9xE5qx5GSEzd5LnCK6TMYyNgYB7HTc7VXaYiTdQntlF7A=="
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
      "state": "tx_+NMLAfiEuEDYmlenCbNh0/5k0LofBi2+EgNHI9+Qva+8i1IwnV+aQ3KGDWA1L/NOlro4PmWorEQhYpLqmvbTQ/icL5lkAosMuEDft68681T2f0dcB84kSdzL4S70lk4yo6lB7AXjVbeE+x4Ax9lZmLFzz0bLbNKgQ0PIb66M2JV804tEsV9v1jMCuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGBoJmxU9xE5qx5GSEzd5LnCK6TMYyNgYB7HTc7VXaYiTdQntlF7A=="
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
    "round": 129
  }
}
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 129
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 129,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
    "round": 129
  }
}
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 129
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 129,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "ABCDEFG",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
      "caller_nonce": 130,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "ABCDEFG",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "ABCDEFG",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "ABCDEFG",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgYKgX5vnJ3EI+afqMyybHjji/fskAjHe9AaJ/0l1YNcppGQSmBVg",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEB7dcCpYx9BmYFkIuSPg+Rg3y3aoBCxU6O/UsPEDC3CVkABUX2lPSeqjUXaFCcV1gLmKJdeakU/BL9h9T6ow9oKuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGCoF+b5ydxCPmn6jMsmx444v37JAIx3vQGif9JdWDXKaRkM6XfrQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEB7dcCpYx9BmYFkIuSPg+Rg3y3aoBCxU6O/UsPEDC3CVkABUX2lPSeqjUXaFCcV1gLmKJdeakU/BL9h9T6ow9oKuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGCoF+b5ydxCPmn6jMsmx444v37JAIx3vQGif9JdWDXKaRkM6XfrQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEB7dcCpYx9BmYFkIuSPg+Rg3y3aoBCxU6O/UsPEDC3CVkABUX2lPSeqjUXaFCcV1gLmKJdeakU/BL9h9T6ow9oKuECX6TPjnEdy3N383hyC5jCz9Jvx/UxwUYlDmp8XJQVsWAwA5iJm1EKLbyUcBFlhUpWb/bhWasEFsyHn0i2TiMENuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGCoF+b5ydxCPmn6jMsmx444v37JAIx3vQGif9JdWDXKaRk5J+qDA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEB7dcCpYx9BmYFkIuSPg+Rg3y3aoBCxU6O/UsPEDC3CVkABUX2lPSeqjUXaFCcV1gLmKJdeakU/BL9h9T6ow9oKuECX6TPjnEdy3N383hyC5jCz9Jvx/UxwUYlDmp8XJQVsWAwA5iJm1EKLbyUcBFlhUpWb/bhWasEFsyHn0i2TiMENuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGCoF+b5ydxCPmn6jMsmx444v37JAIx3vQGif9JdWDXKaRk5J+qDA=="
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
      "state": "tx_+NMLAfiEuEB7dcCpYx9BmYFkIuSPg+Rg3y3aoBCxU6O/UsPEDC3CVkABUX2lPSeqjUXaFCcV1gLmKJdeakU/BL9h9T6ow9oKuECX6TPjnEdy3N383hyC5jCz9Jvx/UxwUYlDmp8XJQVsWAwA5iJm1EKLbyUcBFlhUpWb/bhWasEFsyHn0i2TiMENuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGCoF+b5ydxCPmn6jMsmx444v37JAIx3vQGif9JdWDXKaRk5J+qDA=="
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
    "round": 130
  }
}
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 130
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 130,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
    "round": 130
  }
}
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 130
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 130,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "ABCDEFG",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
      "caller_nonce": 131,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "ABCDEFG",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "ABCDEFG",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "ABCDEFG",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgYOgcpim3LzUVcJEQECyQ9EgFfJWJbyPwxRH3ZP7TO1ZkddHFI1y",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEDvTUvsXFFPSvR3anQPhra1wXSDa6nRz8t5mG/NlTEsuOBaHQ242rO3cQIO27X8vhIrU0iX2/OGO1MefZq14WEEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGDoHKYpty81FXCREBAskPRIBXyViW8j8MUR92T+0ztWZHXs3Bk/A=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEDvTUvsXFFPSvR3anQPhra1wXSDa6nRz8t5mG/NlTEsuOBaHQ242rO3cQIO27X8vhIrU0iX2/OGO1MefZq14WEEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGDoHKYpty81FXCREBAskPRIBXyViW8j8MUR92T+0ztWZHXs3Bk/A==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjlhY2NvdW50X3B1Ymtlecn9L64=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEAnlPvkqIaGTbkKajYiE8QR9x27EJbY53jGikMqrJk/8GohRCYiboF17YJ7ObT0BlKQGhrPtRX42khp0RsmaMUMuEDvTUvsXFFPSvR3anQPhra1wXSDa6nRz8t5mG/NlTEsuOBaHQ242rO3cQIO27X8vhIrU0iX2/OGO1MefZq14WEEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGDoHKYpty81FXCREBAskPRIBXyViW8j8MUR92T+0ztWZHXttTa5g=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEAnlPvkqIaGTbkKajYiE8QR9x27EJbY53jGikMqrJk/8GohRCYiboF17YJ7ObT0BlKQGhrPtRX42khp0RsmaMUMuEDvTUvsXFFPSvR3anQPhra1wXSDa6nRz8t5mG/NlTEsuOBaHQ242rO3cQIO27X8vhIrU0iX2/OGO1MefZq14WEEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGDoHKYpty81FXCREBAskPRIBXyViW8j8MUR92T+0ztWZHXttTa5g=="
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
      "state": "tx_+NMLAfiEuEAnlPvkqIaGTbkKajYiE8QR9x27EJbY53jGikMqrJk/8GohRCYiboF17YJ7ObT0BlKQGhrPtRX42khp0RsmaMUMuEDvTUvsXFFPSvR3anQPhra1wXSDa6nRz8t5mG/NlTEsuOBaHQ242rO3cQIO27X8vhIrU0iX2/OGO1MefZq14WEEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGDoHKYpty81FXCREBAskPRIBXyViW8j8MUR92T+0ztWZHXttTa5g=="
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
    "round": 131
  }
}
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 131
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 131,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
    "round": 131
  }
}
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 131
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 131,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "ABCDEFG",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
      "caller_nonce": 132,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "ABCDEFG",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "ABCDEFG",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "ABCDEFG",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgYSgS5XPWXV167hp0TWo994UzkVr7+PpQL/7gz2VtIMia8GqSTnA",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuED5+zVz1xy3qE6InFA6IT1lra5kDsCW60fmIMkVF5rBs8Wj3o2yHjIdX52GpN+yZPDdfFZycLJglARBtsPuaSsIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGEoEuVz1l1deu4adE1qPfeFM5Fa+/j6UC/+4M9lbSDImvBxu1n9w=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuED5+zVz1xy3qE6InFA6IT1lra5kDsCW60fmIMkVF5rBs8Wj3o2yHjIdX52GpN+yZPDdfFZycLJglARBtsPuaSsIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGEoEuVz1l1deu4adE1qPfeFM5Fa+/j6UC/+4M9lbSDImvBxu1n9w==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEATamT1HX5cPGyWlyLfdOjdAHTpc6CXAMFSBZJPApgEW/C7vzfeQ8Zr395CCNOIY9rQ59NHD2etkObDd8eMLc0CuED5+zVz1xy3qE6InFA6IT1lra5kDsCW60fmIMkVF5rBs8Wj3o2yHjIdX52GpN+yZPDdfFZycLJglARBtsPuaSsIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGEoEuVz1l1deu4adE1qPfeFM5Fa+/j6UC/+4M9lbSDImvBb874CA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEATamT1HX5cPGyWlyLfdOjdAHTpc6CXAMFSBZJPApgEW/C7vzfeQ8Zr395CCNOIY9rQ59NHD2etkObDd8eMLc0CuED5+zVz1xy3qE6InFA6IT1lra5kDsCW60fmIMkVF5rBs8Wj3o2yHjIdX52GpN+yZPDdfFZycLJglARBtsPuaSsIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGEoEuVz1l1deu4adE1qPfeFM5Fa+/j6UC/+4M9lbSDImvBb874CA=="
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
      "state": "tx_+NMLAfiEuEATamT1HX5cPGyWlyLfdOjdAHTpc6CXAMFSBZJPApgEW/C7vzfeQ8Zr395CCNOIY9rQ59NHD2etkObDd8eMLc0CuED5+zVz1xy3qE6InFA6IT1lra5kDsCW60fmIMkVF5rBs8Wj3o2yHjIdX52GpN+yZPDdfFZycLJglARBtsPuaSsIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGEoEuVz1l1deu4adE1qPfeFM5Fa+/j6UC/+4M9lbSDImvBb874CA=="
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
    "round": 132
  }
}
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 132
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 132,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
    "round": 132
  }
}
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 132
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 132,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "ABCDEFG",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
      "caller_nonce": 133,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "ABCDEFG",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "ABCDEFG",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "ABCDEFG",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgYWgmcWk/Z4ITklQVTgLEfsG9ipkbyFKR/m9HdqLFDS+mpa+dlGA",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEC5huxwVbiK87x47cZDWsCf3ygII9RD6mTDAOUmUi/moU1xXpmNtMZ3H/HbhudKtuupY+UGUu7sgF6/b/i3P1oLuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGFoJnFpP2eCE5JUFU4CxH7BvYqZG8hSkf5vR3aixQ0vpqW7+2eeg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEC5huxwVbiK87x47cZDWsCf3ygII9RD6mTDAOUmUi/moU1xXpmNtMZ3H/HbhudKtuupY+UGUu7sgF6/b/i3P1oLuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGFoJnFpP2eCE5JUFU4CxH7BvYqZG8hSkf5vR3aixQ0vpqW7+2eeg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbhlvcmFjbGXU7i2p",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEA//b+bztj/xMjCcJkD9286CLMvGQjXUAGbYHS0t6TIjr70noqaIMZwOO7Q7Pm9iT6vW+Xaql3bbD7uzV7hof4OuEC5huxwVbiK87x47cZDWsCf3ygII9RD6mTDAOUmUi/moU1xXpmNtMZ3H/HbhudKtuupY+UGUu7sgF6/b/i3P1oLuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGFoJnFpP2eCE5JUFU4CxH7BvYqZG8hSkf5vR3aixQ0vpqWSqIzEw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEA//b+bztj/xMjCcJkD9286CLMvGQjXUAGbYHS0t6TIjr70noqaIMZwOO7Q7Pm9iT6vW+Xaql3bbD7uzV7hof4OuEC5huxwVbiK87x47cZDWsCf3ygII9RD6mTDAOUmUi/moU1xXpmNtMZ3H/HbhudKtuupY+UGUu7sgF6/b/i3P1oLuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGFoJnFpP2eCE5JUFU4CxH7BvYqZG8hSkf5vR3aixQ0vpqWSqIzEw=="
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
      "state": "tx_+NMLAfiEuEA//b+bztj/xMjCcJkD9286CLMvGQjXUAGbYHS0t6TIjr70noqaIMZwOO7Q7Pm9iT6vW+Xaql3bbD7uzV7hof4OuEC5huxwVbiK87x47cZDWsCf3ygII9RD6mTDAOUmUi/moU1xXpmNtMZ3H/HbhudKtuupY+UGUu7sgF6/b/i3P1oLuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGFoJnFpP2eCE5JUFU4CxH7BvYqZG8hSkf5vR3aixQ0vpqWSqIzEw=="
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
    "round": 133
  }
}
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 133
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 133,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
    "round": 133
  }
}
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 133
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 133,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "ABCDEFG",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
      "caller_nonce": 134,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "ABCDEFG",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "ABCDEFG",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "ABCDEFG",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgYagVSf3AKU7APxigETJnk7aP4ceS90HETbCNvlD3diABg+4nC0C",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuECOnrn0PeWHneFoDjbGZZCAX6aN4wbM5UAuGRDeZc0Ds04r94Sux7cecKMfcAdzqReXhzw22+nbXzZMPhz4c7MFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGGoFUn9wClOwD8YoBEyZ5O2j+HHkvdBxE2wjb5Q93YgAYPgC3LeA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuECOnrn0PeWHneFoDjbGZZCAX6aN4wbM5UAuGRDeZc0Ds04r94Sux7cecKMfcAdzqReXhzw22+nbXzZMPhz4c7MFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGGoFUn9wClOwD8YoBEyZ5O2j+HHkvdBxE2wjb5Q93YgAYPgC3LeA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuECOnrn0PeWHneFoDjbGZZCAX6aN4wbM5UAuGRDeZc0Ds04r94Sux7cecKMfcAdzqReXhzw22+nbXzZMPhz4c7MFuEDatMErUbt987cdHMP9IC4788KBQ7mJsEUDLIrJSZK+LnfLhYlY6oYinicRy1qr6yTx7UHXC4o6jzLzCX68YQsEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGGoFUn9wClOwD8YoBEyZ5O2j+HHkvdBxE2wjb5Q93YgAYPXhu6Qw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuECOnrn0PeWHneFoDjbGZZCAX6aN4wbM5UAuGRDeZc0Ds04r94Sux7cecKMfcAdzqReXhzw22+nbXzZMPhz4c7MFuEDatMErUbt987cdHMP9IC4788KBQ7mJsEUDLIrJSZK+LnfLhYlY6oYinicRy1qr6yTx7UHXC4o6jzLzCX68YQsEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGGoFUn9wClOwD8YoBEyZ5O2j+HHkvdBxE2wjb5Q93YgAYPXhu6Qw=="
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
      "state": "tx_+NMLAfiEuECOnrn0PeWHneFoDjbGZZCAX6aN4wbM5UAuGRDeZc0Ds04r94Sux7cecKMfcAdzqReXhzw22+nbXzZMPhz4c7MFuEDatMErUbt987cdHMP9IC4788KBQ7mJsEUDLIrJSZK+LnfLhYlY6oYinicRy1qr6yTx7UHXC4o6jzLzCX68YQsEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGGoFUn9wClOwD8YoBEyZ5O2j+HHkvdBxE2wjb5Q93YgAYPXhu6Qw=="
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
    "round": 134
  }
}
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 134
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 134,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
    "round": 134
  }
}
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 134
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 134,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "ABCDEFG",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
      "caller_nonce": 135,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "ABCDEFG",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "ABCDEFG",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "ABCDEFG",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgYegm6GplDQvvzXZHgSx10GozhEjGJGbPebbBmd+Solo7CHGbzOT",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEC8XWvEtxOMtVncdmRc3ZR018hQeU+TPLfNmCw+o+AIT6wu/xyA89j2cw/kJrsOQoipVleklu3kEFRZ7ef5+aIPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGHoJuhqZQ0L7812R4EsddBqM4RIxiRmz3m2wZnfkqJaOwhJO1KpA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEC8XWvEtxOMtVncdmRc3ZR018hQeU+TPLfNmCw+o+AIT6wu/xyA89j2cw/kJrsOQoipVleklu3kEFRZ7ef5+aIPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGHoJuhqZQ0L7812R4EsddBqM4RIxiRmz3m2wZnfkqJaOwhJO1KpA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbjl1bmV4cGVjdGVkX2tleX/1s1c=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEA+ILnqjj7bN+e1WNUiXtuAdKmtE39aIgDci/tLr5j+ForS0npk5ezVYdlMZevopbBcfoFaCRa3Xg6btxNPDgcPuEC8XWvEtxOMtVncdmRc3ZR018hQeU+TPLfNmCw+o+AIT6wu/xyA89j2cw/kJrsOQoipVleklu3kEFRZ7ef5+aIPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGHoJuhqZQ0L7812R4EsddBqM4RIxiRmz3m2wZnfkqJaOwh14eDtg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEA+ILnqjj7bN+e1WNUiXtuAdKmtE39aIgDci/tLr5j+ForS0npk5ezVYdlMZevopbBcfoFaCRa3Xg6btxNPDgcPuEC8XWvEtxOMtVncdmRc3ZR018hQeU+TPLfNmCw+o+AIT6wu/xyA89j2cw/kJrsOQoipVleklu3kEFRZ7ef5+aIPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGHoJuhqZQ0L7812R4EsddBqM4RIxiRmz3m2wZnfkqJaOwh14eDtg=="
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
      "state": "tx_+NMLAfiEuEA+ILnqjj7bN+e1WNUiXtuAdKmtE39aIgDci/tLr5j+ForS0npk5ezVYdlMZevopbBcfoFaCRa3Xg6btxNPDgcPuEC8XWvEtxOMtVncdmRc3ZR018hQeU+TPLfNmCw+o+AIT6wu/xyA89j2cw/kJrsOQoipVleklu3kEFRZ7ef5+aIPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGHoJuhqZQ0L7812R4EsddBqM4RIxiRmz3m2wZnfkqJaOwh14eDtg=="
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
    "round": 135
  }
}
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 135
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 135,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
    "round": 135
  }
}
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 135
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 135,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "ABCDEFG",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
      "caller_nonce": 136,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "ABCDEFG",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "ABCDEFG",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "ABCDEFG",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgYigodY2qMTZorIOV1s9hl78gZkp+QXm5N0KSdS1iD9gLOrlgL0t",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEB2Kt+6UZAIhZtBLUyUFQ5TtljbpwYKwIRL5E/681YIbAN3fyhMA7by32gc4MY2iZIaJFx11Zqekn8dTXSIiIEOuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGIoKHWNqjE2aKyDldbPYZe/IGZKfkF5uTdCknUtYg/YCzqvHyoUA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEB2Kt+6UZAIhZtBLUyUFQ5TtljbpwYKwIRL5E/681YIbAN3fyhMA7by32gc4MY2iZIaJFx11Zqekn8dTXSIiIEOuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGIoKHWNqjE2aKyDldbPYZe/IGZKfkF5uTdCknUtYg/YCzqvHyoUA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEAZrhGWBnFx+PNbHcHthi2JzdleMpr8WF3McXjQCFuliOvloTwIKpUvCctbqGyTF0udqZfjjWWRT+lCLteDMecLuEB2Kt+6UZAIhZtBLUyUFQ5TtljbpwYKwIRL5E/681YIbAN3fyhMA7by32gc4MY2iZIaJFx11Zqekn8dTXSIiIEOuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGIoKHWNqjE2aKyDldbPYZe/IGZKfkF5uTdCknUtYg/YCzqaVTvgw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEAZrhGWBnFx+PNbHcHthi2JzdleMpr8WF3McXjQCFuliOvloTwIKpUvCctbqGyTF0udqZfjjWWRT+lCLteDMecLuEB2Kt+6UZAIhZtBLUyUFQ5TtljbpwYKwIRL5E/681YIbAN3fyhMA7by32gc4MY2iZIaJFx11Zqekn8dTXSIiIEOuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGIoKHWNqjE2aKyDldbPYZe/IGZKfkF5uTdCknUtYg/YCzqaVTvgw=="
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
      "state": "tx_+NMLAfiEuEAZrhGWBnFx+PNbHcHthi2JzdleMpr8WF3McXjQCFuliOvloTwIKpUvCctbqGyTF0udqZfjjWWRT+lCLteDMecLuEB2Kt+6UZAIhZtBLUyUFQ5TtljbpwYKwIRL5E/681YIbAN3fyhMA7by32gc4MY2iZIaJFx11Zqekn8dTXSIiIEOuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGIoKHWNqjE2aKyDldbPYZe/IGZKfkF5uTdCknUtYg/YCzqaVTvgw=="
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
    "round": 136
  }
}
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 136
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 136,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
    "round": 136
  }
}
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 136
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 136,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "ABCDEFG",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
      "caller_nonce": 137,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "ABCDEFG",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "ABCDEFG",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
  }
}
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "ABCDEFG",
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
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
        "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
        "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
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
    "block_hash": "kh_YGVsu6NmyaWgaoW8mMKGypV3AawcEjdk1bEhhFqZzvLzkEm7z",
    "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgYmguXvCbkLutUJWAxYOEaPNT/fynDIRcfwsU0yT8GYV1l6E7NWC",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEBhhzG9KoNk4OEZI7uyIL3H6yvXluyXNgrmvEuy/OrJ2WDFL9ScpCnmo3AMmhEmNXYa8Sx7w5VowAgMOYRFxH0GuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGJoLl7wm5C7rVCVgMWDhGjzU/38pwyEXH8LFNMk/BmFdZe6f5GUQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEBhhzG9KoNk4OEZI7uyIL3H6yvXluyXNgrmvEuy/OrJ2WDFL9ScpCnmo3AMmhEmNXYa8Sx7w5VowAgMOYRFxH0GuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGJoLl7wm5C7rVCVgMWDhGjzU/38pwyEXH8LFNMk/BmFdZe6f5GUQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1dmNQYXdHR2p0bWZodS5jaGFpbi1taXNzaW5nX2tleUlkjes=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEBhhzG9KoNk4OEZI7uyIL3H6yvXluyXNgrmvEuy/OrJ2WDFL9ScpCnmo3AMmhEmNXYa8Sx7w5VowAgMOYRFxH0GuECA+rogr+jt0+7CnQP3HLDV7WcC5AXnvEXLt/aFEZkgkmEm9z4+/n6/12rgRRfKKEIZG4Mxi2wcK9IBtedD/7APuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGJoLl7wm5C7rVCVgMWDhGjzU/38pwyEXH8LFNMk/BmFdZe7sCasQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEBhhzG9KoNk4OEZI7uyIL3H6yvXluyXNgrmvEuy/OrJ2WDFL9ScpCnmo3AMmhEmNXYa8Sx7w5VowAgMOYRFxH0GuECA+rogr+jt0+7CnQP3HLDV7WcC5AXnvEXLt/aFEZkgkmEm9z4+/n6/12rgRRfKKEIZG4Mxi2wcK9IBtedD/7APuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGJoLl7wm5C7rVCVgMWDhGjzU/38pwyEXH8LFNMk/BmFdZe7sCasQ=="
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
      "state": "tx_+NMLAfiEuEBhhzG9KoNk4OEZI7uyIL3H6yvXluyXNgrmvEuy/OrJ2WDFL9ScpCnmo3AMmhEmNXYa8Sx7w5VowAgMOYRFxH0GuECA+rogr+jt0+7CnQP3HLDV7WcC5AXnvEXLt/aFEZkgkmEm9z4+/n6/12rgRRfKKEIZG4Mxi2wcK9IBtedD/7APuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGJoLl7wm5C7rVCVgMWDhGjzU/38pwyEXH8LFNMk/BmFdZe7sCasQ=="
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
    "round": 137
  }
}
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 137
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 137,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
    "round": 137
  }
}
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
        "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 137
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 137,
      "contract_id": "ct_SemwKh8Lguqms5EzQ4mAWEy9YdSuND8tBqeC5HeEnzA6XQiWT",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgYqgO7lH9kDQ8jO3a80dq4XEEVfzAVyPBtC098ahpccxaq0gv0vo",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
  "id": -576460752303421591,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuEADg+tmuI9elXI9vEax1baw0waQnC9tFXXw8CdKTwK85osgkq4SBcNC1MjNYjJO06Do/T1GO2FMRZNuSjHxsREKuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGKoDu5R/ZA0PIzt2vNHauFxBFX8wFcjwbQtPfGoaXHMWqt8WR9Fw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEADg+tmuI9elXI9vEax1baw0waQnC9tFXXw8CdKTwK85osgkq4SBcNC1MjNYjJO06Do/T1GO2FMRZNuSjHxsREKuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGKoDu5R/ZA0PIzt2vNHauFxBFX8wFcjwbQtPfGoaXHMWqt8WR9Fw==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
  "id": -576460752303421590,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEADg+tmuI9elXI9vEax1baw0waQnC9tFXXw8CdKTwK85osgkq4SBcNC1MjNYjJO06Do/T1GO2FMRZNuSjHxsREKuEBTXnFHoXTaF6P5/DHPDWipMI6rEzFQRtLcRuEOa0PD/HX9RkIud/Lju92bbK+T7Mha41yhs0s7/5SJVRYjf1YGuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGKoDu5R/ZA0PIzt2vNHauFxBFX8wFcjwbQtPfGoaXHMWqtLtzM0g=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEADg+tmuI9elXI9vEax1baw0waQnC9tFXXw8CdKTwK85osgkq4SBcNC1MjNYjJO06Do/T1GO2FMRZNuSjHxsREKuEBTXnFHoXTaF6P5/DHPDWipMI6rEzFQRtLcRuEOa0PD/HX9RkIud/Lju92bbK+T7Mha41yhs0s7/5SJVRYjf1YGuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGKoDu5R/ZA0PIzt2vNHauFxBFX8wFcjwbQtPfGoaXHMWqtLtzM0g=="
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
      "state": "tx_+NMLAfiEuEADg+tmuI9elXI9vEax1baw0waQnC9tFXXw8CdKTwK85osgkq4SBcNC1MjNYjJO06Do/T1GO2FMRZNuSjHxsREKuEBTXnFHoXTaF6P5/DHPDWipMI6rEzFQRtLcRuEOa0PD/HX9RkIud/Lju92bbK+T7Mha41yhs0s7/5SJVRYjf1YGuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGKoDu5R/ZA0PIzt2vNHauFxBFX8wFcjwbQtPfGoaXHMWqtLtzM0g=="
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
    "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
    "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
    "call_data": "ABCDEFG",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
      "caller_nonce": 139,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
        "call_data": "ABCDEFG",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
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
        "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
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
    "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
    "call_data": "ABCDEFG",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
        "call_data": "ABCDEFG",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
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
        "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
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
    "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgYugkPWWJuyFTq0hZkp/bCIvFEpV4bknBGOrwYXTkpts8abxqeoP",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEDSforWXAATS4grgSIjtZ+H/63yPKCDMzKldY0+QM/GHMSYv2v1a1+qlIUKiGFxuGXusfayX7PSjyv8PVkJgZUFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGLoJD1libshU6tIWZKf2wiLxRKVeG5JwRjq8GF05KbbPGmYAw48g=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEDSforWXAATS4grgSIjtZ+H/63yPKCDMzKldY0+QM/GHMSYv2v1a1+qlIUKiGFxuGXusfayX7PSjyv8PVkJgZUFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGLoJD1libshU6tIWZKf2wiLxRKVeG5JwRjq8GF05KbbPGmYAw48g==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEC7ZfTHfofxhkCI5UHFEGEWg1WG6/dMDH9goSFpd5UziV8HUlQcYH7uUopO6D8W2SDXW4V5BOA7BMSd6UL8W3IEuEDSforWXAATS4grgSIjtZ+H/63yPKCDMzKldY0+QM/GHMSYv2v1a1+qlIUKiGFxuGXusfayX7PSjyv8PVkJgZUFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGLoJD1libshU6tIWZKf2wiLxRKVeG5JwRjq8GF05KbbPGmv5um4g=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEC7ZfTHfofxhkCI5UHFEGEWg1WG6/dMDH9goSFpd5UziV8HUlQcYH7uUopO6D8W2SDXW4V5BOA7BMSd6UL8W3IEuEDSforWXAATS4grgSIjtZ+H/63yPKCDMzKldY0+QM/GHMSYv2v1a1+qlIUKiGFxuGXusfayX7PSjyv8PVkJgZUFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGLoJD1libshU6tIWZKf2wiLxRKVeG5JwRjq8GF05KbbPGmv5um4g=="
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
      "state": "tx_+NMLAfiEuEC7ZfTHfofxhkCI5UHFEGEWg1WG6/dMDH9goSFpd5UziV8HUlQcYH7uUopO6D8W2SDXW4V5BOA7BMSd6UL8W3IEuEDSforWXAATS4grgSIjtZ+H/63yPKCDMzKldY0+QM/GHMSYv2v1a1+qlIUKiGFxuGXusfayX7PSjyv8PVkJgZUFuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGLoJD1libshU6tIWZKf2wiLxRKVeG5JwRjq8GF05KbbPGmv5um4g=="
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
    "round": 139
  }
}
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 139
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 139,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
    "round": 139
  }
}
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 139
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 139,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
    "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
    "call_data": "ABCDEFG",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
      "caller_nonce": 140,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
        "call_data": "ABCDEFG",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
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
        "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
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
    "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
    "call_data": "ABCDEFG",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
        "call_data": "ABCDEFG",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
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
        "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
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
    "block_hash": "kh_i3xphSbz4yEoCHhXzbKYSRJNE9jdmLKNWuuTRmMA7ykYwh1Yp",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgYyg6wW8QDIyo98uscxwNlAn6LjI8gns08CM7N7hsPADFbbHrbWh",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEBYAb1bBhQI+cTi92xYKJjEDICfMUXVc1VUxi4NmUcrlpyfsWQ5tCZe2lNs/aMwK7aJQDtkf0qXEdvxFzKhzgkPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGMoOsFvEAyMqPfLrHMcDZQJ+i4yPIJ7NPAjOze4bDwAxW2lSulgg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEBYAb1bBhQI+cTi92xYKJjEDICfMUXVc1VUxi4NmUcrlpyfsWQ5tCZe2lNs/aMwK7aJQDtkf0qXEdvxFzKhzgkPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGMoOsFvEAyMqPfLrHMcDZQJ+i4yPIJ7NPAjOze4bDwAxW2lSulgg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEBYAb1bBhQI+cTi92xYKJjEDICfMUXVc1VUxi4NmUcrlpyfsWQ5tCZe2lNs/aMwK7aJQDtkf0qXEdvxFzKhzgkPuEBYg7enad4FpL8lNSRN4N6G0gFQj85Ou/ZMkMRto9ndQMECNyLgT4wujTOaMWBa3aVDBQ/7AbVwKLFFdR5pHT0JuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGMoOsFvEAyMqPfLrHMcDZQJ+i4yPIJ7NPAjOze4bDwAxW27mw7hQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEBYAb1bBhQI+cTi92xYKJjEDICfMUXVc1VUxi4NmUcrlpyfsWQ5tCZe2lNs/aMwK7aJQDtkf0qXEdvxFzKhzgkPuEBYg7enad4FpL8lNSRN4N6G0gFQj85Ou/ZMkMRto9ndQMECNyLgT4wujTOaMWBa3aVDBQ/7AbVwKLFFdR5pHT0JuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGMoOsFvEAyMqPfLrHMcDZQJ+i4yPIJ7NPAjOze4bDwAxW27mw7hQ=="
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
      "state": "tx_+NMLAfiEuEBYAb1bBhQI+cTi92xYKJjEDICfMUXVc1VUxi4NmUcrlpyfsWQ5tCZe2lNs/aMwK7aJQDtkf0qXEdvxFzKhzgkPuEBYg7enad4FpL8lNSRN4N6G0gFQj85Ou/ZMkMRto9ndQMECNyLgT4wujTOaMWBa3aVDBQ/7AbVwKLFFdR5pHT0JuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGMoOsFvEAyMqPfLrHMcDZQJ+i4yPIJ7NPAjOze4bDwAxW27mw7hQ=="
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
    "round": 140
  }
}
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 140
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 140,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
    "round": 140
  }
}
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 140
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 140,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "ABCDEFG",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
      "caller_nonce": 141,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "ABCDEFG",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "ABCDEFG",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "ABCDEFG",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgY2gGnBKIxU+v6EK77KMG14zsQTcgRnjLX3cr7d809Z0ghCSIgMX",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEAQeAgtlJmQQY0aESijlFM5ZkAuRZrQU8fEh1kd5QdcN+75itivp2RVOcn1tG0dQCV4XZdhZOJdOF0gEhcpC90GuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGNoBpwSiMVPr+hCu+yjBteM7EE3IEZ4y193K+3fNPWdIIQi1Raww=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEAQeAgtlJmQQY0aESijlFM5ZkAuRZrQU8fEh1kd5QdcN+75itivp2RVOcn1tG0dQCV4XZdhZOJdOF0gEhcpC90GuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGNoBpwSiMVPr+hCu+yjBteM7EE3IEZ4y193K+3fNPWdIIQi1Raww==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEAQeAgtlJmQQY0aESijlFM5ZkAuRZrQU8fEh1kd5QdcN+75itivp2RVOcn1tG0dQCV4XZdhZOJdOF0gEhcpC90GuECJXlRQv/8oI3ToNtYxJ9PBcBo/DcOJi3Zp/2ASyvREDPO78JUU02MOSZxkIrHjsQZ58oatTDx0oU2POJxfOSABuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGNoBpwSiMVPr+hCu+yjBteM7EE3IEZ4y193K+3fNPWdIIQlC/YAA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEAQeAgtlJmQQY0aESijlFM5ZkAuRZrQU8fEh1kd5QdcN+75itivp2RVOcn1tG0dQCV4XZdhZOJdOF0gEhcpC90GuECJXlRQv/8oI3ToNtYxJ9PBcBo/DcOJi3Zp/2ASyvREDPO78JUU02MOSZxkIrHjsQZ58oatTDx0oU2POJxfOSABuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGNoBpwSiMVPr+hCu+yjBteM7EE3IEZ4y193K+3fNPWdIIQlC/YAA=="
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
      "state": "tx_+NMLAfiEuEAQeAgtlJmQQY0aESijlFM5ZkAuRZrQU8fEh1kd5QdcN+75itivp2RVOcn1tG0dQCV4XZdhZOJdOF0gEhcpC90GuECJXlRQv/8oI3ToNtYxJ9PBcBo/DcOJi3Zp/2ASyvREDPO78JUU02MOSZxkIrHjsQZ58oatTDx0oU2POJxfOSABuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGNoBpwSiMVPr+hCu+yjBteM7EE3IEZ4y193K+3fNPWdIIQlC/YAA=="
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
    "round": 141
  }
}
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 141
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 141,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
    "round": 141
  }
}
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 141
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 141,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "ABCDEFG",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
      "caller_nonce": 142,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "ABCDEFG",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "ABCDEFG",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "ABCDEFG",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgY6gdagIiXRph/QZWbHcN5oI1TxIipbfSISoAglNTpOKEtue6cAb",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEAqYDGCKG8J7Ac6qaF/fDqICO1NzIFr4u3vY+Hky4KYm/KDk4MC1IH4WL/aruJyLdeWTQKJUdhQS614OPBt+ZEOuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGOoHWoCIl0aYf0GVmx3DeaCNU8SIqW30iEqAIJTU6TihLb8i3XuQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEAqYDGCKG8J7Ac6qaF/fDqICO1NzIFr4u3vY+Hky4KYm/KDk4MC1IH4WL/aruJyLdeWTQKJUdhQS614OPBt+ZEOuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGOoHWoCIl0aYf0GVmx3DeaCNU8SIqW30iEqAIJTU6TihLb8i3XuQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjlhY2NvdW50X3B1YmtleQSUPIE=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEAqYDGCKG8J7Ac6qaF/fDqICO1NzIFr4u3vY+Hky4KYm/KDk4MC1IH4WL/aruJyLdeWTQKJUdhQS614OPBt+ZEOuEC4aB6SwaEUo9Rb4ST07/ec/C/dAHwW73HQusqyuyiQfK1/+94uNO6502umD6uZnr2sabfo2vqZNfrX2X5AHcsHuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGOoHWoCIl0aYf0GVmx3DeaCNU8SIqW30iEqAIJTU6TihLbpxf0cQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEAqYDGCKG8J7Ac6qaF/fDqICO1NzIFr4u3vY+Hky4KYm/KDk4MC1IH4WL/aruJyLdeWTQKJUdhQS614OPBt+ZEOuEC4aB6SwaEUo9Rb4ST07/ec/C/dAHwW73HQusqyuyiQfK1/+94uNO6502umD6uZnr2sabfo2vqZNfrX2X5AHcsHuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGOoHWoCIl0aYf0GVmx3DeaCNU8SIqW30iEqAIJTU6TihLbpxf0cQ=="
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
      "state": "tx_+NMLAfiEuEAqYDGCKG8J7Ac6qaF/fDqICO1NzIFr4u3vY+Hky4KYm/KDk4MC1IH4WL/aruJyLdeWTQKJUdhQS614OPBt+ZEOuEC4aB6SwaEUo9Rb4ST07/ec/C/dAHwW73HQusqyuyiQfK1/+94uNO6502umD6uZnr2sabfo2vqZNfrX2X5AHcsHuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGOoHWoCIl0aYf0GVmx3DeaCNU8SIqW30iEqAIJTU6TihLbpxf0cQ=="
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
    "round": 142
  }
}
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 142
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 142,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
    "round": 142
  }
}
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 142
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 142,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "ABCDEFG",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
      "caller_nonce": 143,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "ABCDEFG",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "ABCDEFG",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "ABCDEFG",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgY+gGZNIReeCbY8Kh1wb3m5hU+lERH/hUXaJFSmt0+/M+YoGxa8f",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEDx0NqVzqT9His3NaN7StwoEc+i5m/XAUDjpPX8OlqaRiYWtdTJfFtMlEr63BDFCnHBYcbNaV4Zv/cKb2XZnZMDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGPoBmTSEXngm2PCodcG95uYVPpRER/4VF2iRUprdPvzPmKMuU6TA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEDx0NqVzqT9His3NaN7StwoEc+i5m/XAUDjpPX8OlqaRiYWtdTJfFtMlEr63BDFCnHBYcbNaV4Zv/cKb2XZnZMDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGPoBmTSEXngm2PCodcG95uYVPpRER/4VF2iRUprdPvzPmKMuU6TA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEAXe87TjVuoFXrL6xZ898HW9joYGQDU1WdjiPBBurb0/XxivXtH2rMR2a0T1HhKWJpbqZ/BBXBWT4qFk8o5Ce8KuEDx0NqVzqT9His3NaN7StwoEc+i5m/XAUDjpPX8OlqaRiYWtdTJfFtMlEr63BDFCnHBYcbNaV4Zv/cKb2XZnZMDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGPoBmTSEXngm2PCodcG95uYVPpRER/4VF2iRUprdPvzPmKVj/llw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEAXe87TjVuoFXrL6xZ898HW9joYGQDU1WdjiPBBurb0/XxivXtH2rMR2a0T1HhKWJpbqZ/BBXBWT4qFk8o5Ce8KuEDx0NqVzqT9His3NaN7StwoEc+i5m/XAUDjpPX8OlqaRiYWtdTJfFtMlEr63BDFCnHBYcbNaV4Zv/cKb2XZnZMDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGPoBmTSEXngm2PCodcG95uYVPpRER/4VF2iRUprdPvzPmKVj/llw=="
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
      "state": "tx_+NMLAfiEuEAXe87TjVuoFXrL6xZ898HW9joYGQDU1WdjiPBBurb0/XxivXtH2rMR2a0T1HhKWJpbqZ/BBXBWT4qFk8o5Ce8KuEDx0NqVzqT9His3NaN7StwoEc+i5m/XAUDjpPX8OlqaRiYWtdTJfFtMlEr63BDFCnHBYcbNaV4Zv/cKb2XZnZMDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGPoBmTSEXngm2PCodcG95uYVPpRER/4VF2iRUprdPvzPmKVj/llw=="
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
    "round": 143
  }
}
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 143
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 143,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
    "round": 143
  }
}
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 143
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 143,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "ABCDEFG",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
      "caller_nonce": 144,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "ABCDEFG",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "ABCDEFG",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "ABCDEFG",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgZCgxQBWtrxz0tAJKQ1Xu/a8QjEUw0VYIO5wNsdmPEAr/U8nTUXB",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEAgPuWp08Dq/+2QIHdYS6ghRB1U/D7Qm/BjRA1gXSsvpOPM5lnZ6dM+l1hv2iaedJLG1EKUVM3jndmGuSca2VECuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGQoMUAVra8c9LQCSkNV7v2vEIxFMNFWCDucDbHZjxAK/1P0k31xQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEAgPuWp08Dq/+2QIHdYS6ghRB1U/D7Qm/BjRA1gXSsvpOPM5lnZ6dM+l1hv2iaedJLG1EKUVM3jndmGuSca2VECuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGQoMUAVra8c9LQCSkNV7v2vEIxFMNFWCDucDbHZjxAK/1P0k31xQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbhlvcmFjbGWZaIdx",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEAPmX6EM3ZDLK9Tzo3Y1Xsvm71nFa5jFksm3+Bg9rcRJ9+caAq+AJRhabrTWZ+ro6dvM35yPVmZJ/BZtveb61sHuEAgPuWp08Dq/+2QIHdYS6ghRB1U/D7Qm/BjRA1gXSsvpOPM5lnZ6dM+l1hv2iaedJLG1EKUVM3jndmGuSca2VECuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGQoMUAVra8c9LQCSkNV7v2vEIxFMNFWCDucDbHZjxAK/1P01aVDw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEAPmX6EM3ZDLK9Tzo3Y1Xsvm71nFa5jFksm3+Bg9rcRJ9+caAq+AJRhabrTWZ+ro6dvM35yPVmZJ/BZtveb61sHuEAgPuWp08Dq/+2QIHdYS6ghRB1U/D7Qm/BjRA1gXSsvpOPM5lnZ6dM+l1hv2iaedJLG1EKUVM3jndmGuSca2VECuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGQoMUAVra8c9LQCSkNV7v2vEIxFMNFWCDucDbHZjxAK/1P01aVDw=="
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
      "state": "tx_+NMLAfiEuEAPmX6EM3ZDLK9Tzo3Y1Xsvm71nFa5jFksm3+Bg9rcRJ9+caAq+AJRhabrTWZ+ro6dvM35yPVmZJ/BZtveb61sHuEAgPuWp08Dq/+2QIHdYS6ghRB1U/D7Qm/BjRA1gXSsvpOPM5lnZ6dM+l1hv2iaedJLG1EKUVM3jndmGuSca2VECuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGQoMUAVra8c9LQCSkNV7v2vEIxFMNFWCDucDbHZjxAK/1P01aVDw=="
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
    "round": 144
  }
}
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 144
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 144,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
    "round": 144
  }
}
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 144
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 144,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "ABCDEFG",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
      "caller_nonce": 145,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "ABCDEFG",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "ABCDEFG",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "ABCDEFG",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgZGgLXzQXHXdFSjRR5xGWuOr+WWLJiZi58dyDuS+5X8RB55IeqUY",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEDiWjgfbE0Pn/Nv0cE17PwkgL+Kazw9/xedF81z5z/RN4jY5+cWYlHOwT7ZmvnBTUgTySix7v5LwF4fR+VOtiYIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGRoC180Fx13RUo0UecRlrjq/lliyYmYufHcg7kvuV/EQee8V79pA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEDiWjgfbE0Pn/Nv0cE17PwkgL+Kazw9/xedF81z5z/RN4jY5+cWYlHOwT7ZmvnBTUgTySix7v5LwF4fR+VOtiYIuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGRoC180Fx13RUo0UecRlrjq/lliyYmYufHcg7kvuV/EQee8V79pA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEDiWjgfbE0Pn/Nv0cE17PwkgL+Kazw9/xedF81z5z/RN4jY5+cWYlHOwT7ZmvnBTUgTySix7v5LwF4fR+VOtiYIuED5DL00hqX/4FqlalIigdabYrFrMefBMYKMxt/z5AnusJiYhJ8Z+5KzPgMzhVOzJLmtA16Tj4j9pVGfzkvVZkoDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGRoC180Fx13RUo0UecRlrjq/lliyYmYufHcg7kvuV/EQeemO2yVQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEDiWjgfbE0Pn/Nv0cE17PwkgL+Kazw9/xedF81z5z/RN4jY5+cWYlHOwT7ZmvnBTUgTySix7v5LwF4fR+VOtiYIuED5DL00hqX/4FqlalIigdabYrFrMefBMYKMxt/z5AnusJiYhJ8Z+5KzPgMzhVOzJLmtA16Tj4j9pVGfzkvVZkoDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGRoC180Fx13RUo0UecRlrjq/lliyYmYufHcg7kvuV/EQeemO2yVQ=="
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
      "state": "tx_+NMLAfiEuEDiWjgfbE0Pn/Nv0cE17PwkgL+Kazw9/xedF81z5z/RN4jY5+cWYlHOwT7ZmvnBTUgTySix7v5LwF4fR+VOtiYIuED5DL00hqX/4FqlalIigdabYrFrMefBMYKMxt/z5AnusJiYhJ8Z+5KzPgMzhVOzJLmtA16Tj4j9pVGfzkvVZkoDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGRoC180Fx13RUo0UecRlrjq/lliyYmYufHcg7kvuV/EQeemO2yVQ=="
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
    "round": 145
  }
}
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 145
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 145,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
    "round": 145
  }
}
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 145
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 145,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "ABCDEFG",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
      "caller_nonce": 146,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "ABCDEFG",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "ABCDEFG",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "ABCDEFG",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgZKg7Ny+vjixuAzbgk+P7vLPIWSSxm/4WEzn+aI+bTXOVmQ/P60J",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEDJnX35+pQxHWw0gmNNoIiUhcOSAkqjHs5L+WGVhocvc45HiY9/+zzHZrR4jlOI/Sr3fZODmTxZutOaVfE5kokKuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGSoOzcvr44sbgM24JPj+7yzyFkksZv+FhM5/miPm01zlZkHyUBgg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEDJnX35+pQxHWw0gmNNoIiUhcOSAkqjHs5L+WGVhocvc45HiY9/+zzHZrR4jlOI/Sr3fZODmTxZutOaVfE5kokKuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGSoOzcvr44sbgM24JPj+7yzyFkksZv+FhM5/miPm01zlZkHyUBgg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbjl1bmV4cGVjdGVkX2tlebM+qwQ=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEBKXPDi/arT9qJ1wZUbfIitnJnQTXGpFfr+qNDcuMID/ImzsgYVlwicMyDjMUafg9aZ57mgFQAJBG81a7ND1DQIuEDJnX35+pQxHWw0gmNNoIiUhcOSAkqjHs5L+WGVhocvc45HiY9/+zzHZrR4jlOI/Sr3fZODmTxZutOaVfE5kokKuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGSoOzcvr44sbgM24JPj+7yzyFkksZv+FhM5/miPm01zlZksKYvaw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEBKXPDi/arT9qJ1wZUbfIitnJnQTXGpFfr+qNDcuMID/ImzsgYVlwicMyDjMUafg9aZ57mgFQAJBG81a7ND1DQIuEDJnX35+pQxHWw0gmNNoIiUhcOSAkqjHs5L+WGVhocvc45HiY9/+zzHZrR4jlOI/Sr3fZODmTxZutOaVfE5kokKuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGSoOzcvr44sbgM24JPj+7yzyFkksZv+FhM5/miPm01zlZksKYvaw=="
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
      "state": "tx_+NMLAfiEuEBKXPDi/arT9qJ1wZUbfIitnJnQTXGpFfr+qNDcuMID/ImzsgYVlwicMyDjMUafg9aZ57mgFQAJBG81a7ND1DQIuEDJnX35+pQxHWw0gmNNoIiUhcOSAkqjHs5L+WGVhocvc45HiY9/+zzHZrR4jlOI/Sr3fZODmTxZutOaVfE5kokKuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGSoOzcvr44sbgM24JPj+7yzyFkksZv+FhM5/miPm01zlZksKYvaw=="
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
    "round": 146
  }
}
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 146
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 146,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
    "round": 146
  }
}
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 146
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 146,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "ABCDEFG",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
      "caller_nonce": 147,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "ABCDEFG",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "ABCDEFG",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "ABCDEFG",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgZOgHipP5Y4Os/RDSKuwE6deSnqM/lT8DDMvePBgBImYyMmKgsRZ",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEA1VoiJT2vWF3SjACatZwTyKCzNwpRyLIEQEIl04eKoKx3Qh5cj0ZTMC1V/ryT1hV6Q2/H3KsgHMwVBNl5wO44NuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGToB4qT+WODrP0Q0irsBOnXkp6jP5U/AwzL3jwYASJmMjJNUQjcg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEA1VoiJT2vWF3SjACatZwTyKCzNwpRyLIEQEIl04eKoKx3Qh5cj0ZTMC1V/ryT1hV6Q2/H3KsgHMwVBNl5wO44NuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGToB4qT+WODrP0Q0irsBOnXkp6jP5U/AwzL3jwYASJmMjJNUQjcg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEA1VoiJT2vWF3SjACatZwTyKCzNwpRyLIEQEIl04eKoKx3Qh5cj0ZTMC1V/ryT1hV6Q2/H3KsgHMwVBNl5wO44NuEDu5Et8aUToV+UkBybE0Tu0NekXprWFtla/0UQQpO2tYSuQKWzavhTCWRuYp8FuIQoGbDNS3f7Gjq+pAMpusDcGuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGToB4qT+WODrP0Q0irsBOnXkp6jP5U/AwzL3jwYASJmMjJ7kRcuQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEA1VoiJT2vWF3SjACatZwTyKCzNwpRyLIEQEIl04eKoKx3Qh5cj0ZTMC1V/ryT1hV6Q2/H3KsgHMwVBNl5wO44NuEDu5Et8aUToV+UkBybE0Tu0NekXprWFtla/0UQQpO2tYSuQKWzavhTCWRuYp8FuIQoGbDNS3f7Gjq+pAMpusDcGuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGToB4qT+WODrP0Q0irsBOnXkp6jP5U/AwzL3jwYASJmMjJ7kRcuQ=="
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
      "state": "tx_+NMLAfiEuEA1VoiJT2vWF3SjACatZwTyKCzNwpRyLIEQEIl04eKoKx3Qh5cj0ZTMC1V/ryT1hV6Q2/H3KsgHMwVBNl5wO44NuEDu5Et8aUToV+UkBybE0Tu0NekXprWFtla/0UQQpO2tYSuQKWzavhTCWRuYp8FuIQoGbDNS3f7Gjq+pAMpusDcGuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGToB4qT+WODrP0Q0irsBOnXkp6jP5U/AwzL3jwYASJmMjJ7kRcuQ=="
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
    "round": 147
  }
}
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 147
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 147,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
    "round": 147
  }
}
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 147
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 147,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "ABCDEFG",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
      "caller_nonce": 148,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "ABCDEFG",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "ABCDEFG",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
  }
}
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "ABCDEFG",
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
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
        "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
        "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
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
    "block_hash": "kh_fiduoWpfBNYbj9dvvsSxgTFpHjL7W8RGVKZAN9Fdu54X4fe8a",
    "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgZSgbW6KrY8c+oPLkbU4X210SanUZzoPgNc7ycNszNG8rYI+A9KZ",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuED8Mf3YNjUbj1HZOs0ONqyaqJuQoW4I/6eEQG8XkLhjuJmtN1iLd0bWTfel9c6Gw/TjOUbEIeS03LArDGjs1OAPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGUoG1uiq2PHPqDy5G1OF9tdEmp1Gc6D4DXO8nDbMzRvK2Cja0mvA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuED8Mf3YNjUbj1HZOs0ONqyaqJuQoW4I/6eEQG8XkLhjuJmtN1iLd0bWTfel9c6Gw/TjOUbEIeS03LArDGjs1OAPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGUoG1uiq2PHPqDy5G1OF9tdEmp1Gc6D4DXO8nDbMzRvK2Cja0mvA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzUVdlZHRxWkhUOWJpei5jaGFpbi1taXNzaW5nX2tleXAFQww=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEAS11vNpj1nYLLl7uHbgaSX1RFjEvToojqWoKMeHoRS60uZyupc0ybhcQKN28DBnxR0/Zy+sLwQ6hNMv04B2O0DuED8Mf3YNjUbj1HZOs0ONqyaqJuQoW4I/6eEQG8XkLhjuJmtN1iLd0bWTfel9c6Gw/TjOUbEIeS03LArDGjs1OAPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGUoG1uiq2PHPqDy5G1OF9tdEmp1Gc6D4DXO8nDbMzRvK2CXeTXuQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEAS11vNpj1nYLLl7uHbgaSX1RFjEvToojqWoKMeHoRS60uZyupc0ybhcQKN28DBnxR0/Zy+sLwQ6hNMv04B2O0DuED8Mf3YNjUbj1HZOs0ONqyaqJuQoW4I/6eEQG8XkLhjuJmtN1iLd0bWTfel9c6Gw/TjOUbEIeS03LArDGjs1OAPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGUoG1uiq2PHPqDy5G1OF9tdEmp1Gc6D4DXO8nDbMzRvK2CXeTXuQ=="
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
      "state": "tx_+NMLAfiEuEAS11vNpj1nYLLl7uHbgaSX1RFjEvToojqWoKMeHoRS60uZyupc0ybhcQKN28DBnxR0/Zy+sLwQ6hNMv04B2O0DuED8Mf3YNjUbj1HZOs0ONqyaqJuQoW4I/6eEQG8XkLhjuJmtN1iLd0bWTfel9c6Gw/TjOUbEIeS03LArDGjs1OAPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGUoG1uiq2PHPqDy5G1OF9tdEmp1Gc6D4DXO8nDbMzRvK2CXeTXuQ=="
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
    "round": 148
  }
}
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 148
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 148,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
    "round": 148
  }
}
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
        "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 148
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 148,
      "contract_id": "ct_WEvUof1KzQJY185XTj7xQnKMxwpYaR9fXwJ29Ft6TcuadtekM",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgZWgEUQBLHV8mmfF1Mal6kqN++GDxhlKjL3XhTDRtJZwzFo3CYdD",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
  "id": -576460752303421569,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JELAfhCuECWERmZpqkjY5RK6irQA1Nf7wU6vJhUT+0iGbrjkbW5j0EplHmFFwGQdC07mxlgsS4j3qS+OI0FHPBUyOU3x6gAuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGVoBFEASx1fJpnxdTGpepKjfvhg8YZSoy914Uw0bSWcMxa1djI6A=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuECWERmZpqkjY5RK6irQA1Nf7wU6vJhUT+0iGbrjkbW5j0EplHmFFwGQdC07mxlgsS4j3qS+OI0FHPBUyOU3x6gAuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGVoBFEASx1fJpnxdTGpepKjfvhg8YZSoy914Uw0bSWcMxa1djI6A==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+IBGA6BsGymMnQIcKm3lCSkS5gQduehLTL4xBAac1k1AgJNAk8C4U7H+RNZEHwA3ADcAGg6CPwEDP/7E1ZQJBDcCd3cXbdQAAocCNwA3AXcIPAIEAQN/AQP/nS8CEUTWRB8RaW5pdBHE1ZQJLWNhbl9yZXNvbHZlgi8AhTQuMi4wAJyUnzs=",
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
  "id": -576460752303421568,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NMLAfiEuEARIbnIAeUoVQNny3ZtWhNsm6W+ueHKmJECqfM2xbBMckP/PRQtVXT2oqDEOMV8Fvp4/EmyEVwce4MvgTT0Vm8FuECWERmZpqkjY5RK6irQA1Nf7wU6vJhUT+0iGbrjkbW5j0EplHmFFwGQdC07mxlgsS4j3qS+OI0FHPBUyOU3x6gAuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGVoBFEASx1fJpnxdTGpepKjfvhg8YZSoy914Uw0bSWcMxayq0qpQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEARIbnIAeUoVQNny3ZtWhNsm6W+ueHKmJECqfM2xbBMckP/PRQtVXT2oqDEOMV8Fvp4/EmyEVwce4MvgTT0Vm8FuECWERmZpqkjY5RK6irQA1Nf7wU6vJhUT+0iGbrjkbW5j0EplHmFFwGQdC07mxlgsS4j3qS+OI0FHPBUyOU3x6gAuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGVoBFEASx1fJpnxdTGpepKjfvhg8YZSoy914Uw0bSWcMxayq0qpQ=="
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
      "state": "tx_+NMLAfiEuEARIbnIAeUoVQNny3ZtWhNsm6W+ueHKmJECqfM2xbBMckP/PRQtVXT2oqDEOMV8Fvp4/EmyEVwce4MvgTT0Vm8FuECWERmZpqkjY5RK6irQA1Nf7wU6vJhUT+0iGbrjkbW5j0EplHmFFwGQdC07mxlgsS4j3qS+OI0FHPBUyOU3x6gAuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGVoBFEASx1fJpnxdTGpepKjfvhg8YZSoy914Uw0bSWcMxayq0qpQ=="
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
    "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
    "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
    "call_data": "ABCDEFG",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
      "caller_nonce": 150,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
        "call_data": "ABCDEFG",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
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
        "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
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
    "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
    "call_data": "ABCDEFG",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
        "call_data": "ABCDEFG",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
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
        "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
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
    "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgZagZIIcXw5WjvS5pE60mbZa0++fHB0vhq4YbpBvhAxEEUtbHP6g",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEAd/XRRdcbx1QGv0rJZoU9/q2kDOSRWE00dhu4RqXEW+4JHA4h12jW36tvRnwM5EtcSK3Dep7V+OJOvApBPFjEGuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGWoGSCHF8OVo70uaROtJm2WtPvnxwdL4auGG6Qb4QMRBFLtxnKPA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEAd/XRRdcbx1QGv0rJZoU9/q2kDOSRWE00dhu4RqXEW+4JHA4h12jW36tvRnwM5EtcSK3Dep7V+OJOvApBPFjEGuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGWoGSCHF8OVo70uaROtJm2WtPvnxwdL4auGG6Qb4QMRBFLtxnKPA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEAd/XRRdcbx1QGv0rJZoU9/q2kDOSRWE00dhu4RqXEW+4JHA4h12jW36tvRnwM5EtcSK3Dep7V+OJOvApBPFjEGuEByY8jnvJ4KJcej3GBZiklQS3ZFJNPgmrxPs55rkGE1w4IYOpn3PvBOUTT2vKvi/IN7zScNYia20tY/ut53y7sPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGWoGSCHF8OVo70uaROtJm2WtPvnxwdL4auGG6Qb4QMRBFLqWRY0A=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEAd/XRRdcbx1QGv0rJZoU9/q2kDOSRWE00dhu4RqXEW+4JHA4h12jW36tvRnwM5EtcSK3Dep7V+OJOvApBPFjEGuEByY8jnvJ4KJcej3GBZiklQS3ZFJNPgmrxPs55rkGE1w4IYOpn3PvBOUTT2vKvi/IN7zScNYia20tY/ut53y7sPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGWoGSCHF8OVo70uaROtJm2WtPvnxwdL4auGG6Qb4QMRBFLqWRY0A=="
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
      "state": "tx_+NMLAfiEuEAd/XRRdcbx1QGv0rJZoU9/q2kDOSRWE00dhu4RqXEW+4JHA4h12jW36tvRnwM5EtcSK3Dep7V+OJOvApBPFjEGuEByY8jnvJ4KJcej3GBZiklQS3ZFJNPgmrxPs55rkGE1w4IYOpn3PvBOUTT2vKvi/IN7zScNYia20tY/ut53y7sPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGWoGSCHF8OVo70uaROtJm2WtPvnxwdL4auGG6Qb4QMRBFLqWRY0A=="
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
    "round": 150
  }
}
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 150
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 150,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
    "round": 150
  }
}
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 150
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 150,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
    "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
    "call_data": "ABCDEFG",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
      "caller_nonce": 151,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
        "call_data": "ABCDEFG",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
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
        "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
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
    "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
    "call_data": "ABCDEFG",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
        "call_data": "ABCDEFG",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
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
        "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
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
    "block_hash": "kh_24NDqAcjXzEX7PYM8vRNUABt5t7BmzdZ2KvK89P4p45o25AaXq",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgZegHhl6oUP3LALdYHxpwrgmR2swEDPaQdWTyLLQh54Gkg+ZF4Os",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEAjMD6mk9lmvIusN4gqf8ed1RN70HLVxR9fpgEWSRtUFjWoVUb8CMDAQLMTvGdLswQJQWnnQTssRMHdOQV5SIwEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGXoB4ZeqFD9ywC3WB8acK4JkdrMBAz2kHVk8iy0IeeBpIP1Em3OQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEAjMD6mk9lmvIusN4gqf8ed1RN70HLVxR9fpgEWSRtUFjWoVUb8CMDAQLMTvGdLswQJQWnnQTssRMHdOQV5SIwEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGXoB4ZeqFD9ywC3WB8acK4JkdrMBAz2kHVk8iy0IeeBpIP1Em3OQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEAjMD6mk9lmvIusN4gqf8ed1RN70HLVxR9fpgEWSRtUFjWoVUb8CMDAQLMTvGdLswQJQWnnQTssRMHdOQV5SIwEuECfE7fqtCXuZshTSuMUZh2Cw9X4ebVy/fUC6E1zQx5X5pO7zazoFcWLl3M8iFHeEnxGKylR2/QRIsPE99D/Yl4FuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGXoB4ZeqFD9ywC3WB8acK4JkdrMBAz2kHVk8iy0IeeBpIP9hNK8Q=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEAjMD6mk9lmvIusN4gqf8ed1RN70HLVxR9fpgEWSRtUFjWoVUb8CMDAQLMTvGdLswQJQWnnQTssRMHdOQV5SIwEuECfE7fqtCXuZshTSuMUZh2Cw9X4ebVy/fUC6E1zQx5X5pO7zazoFcWLl3M8iFHeEnxGKylR2/QRIsPE99D/Yl4FuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGXoB4ZeqFD9ywC3WB8acK4JkdrMBAz2kHVk8iy0IeeBpIP9hNK8Q=="
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
      "state": "tx_+NMLAfiEuEAjMD6mk9lmvIusN4gqf8ed1RN70HLVxR9fpgEWSRtUFjWoVUb8CMDAQLMTvGdLswQJQWnnQTssRMHdOQV5SIwEuECfE7fqtCXuZshTSuMUZh2Cw9X4ebVy/fUC6E1zQx5X5pO7zazoFcWLl3M8iFHeEnxGKylR2/QRIsPE99D/Yl4FuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGXoB4ZeqFD9ywC3WB8acK4JkdrMBAz2kHVk8iy0IeeBpIP9hNK8Q=="
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
    "round": 151
  }
}
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 151
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 151,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
    "round": 151
  }
}
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 151
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 151,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "ABCDEFG",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
      "caller_nonce": 152,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "ABCDEFG",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "ABCDEFG",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "ABCDEFG",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgZiggvGc6wnKc/dFFWa/MYhr9uELsgBvBoajreV1fgLtSN3N6A5m",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEDVGO+/FpanEiXXhyJ3j1BbB2BSJSTartTdEFzJ/TGaXqs0VBVLgZUsVP0EhYywkeLTSpMjc5mOkqNCR+W6SVsPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGYoILxnOsJynP3RRVmvzGIa/bhC7IAbwaGo63ldX4C7UjdFk8p3w=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEDVGO+/FpanEiXXhyJ3j1BbB2BSJSTartTdEFzJ/TGaXqs0VBVLgZUsVP0EhYywkeLTSpMjc5mOkqNCR+W6SVsPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGYoILxnOsJynP3RRVmvzGIa/bhC7IAbwaGo63ldX4C7UjdFk8p3w==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEA9je9IZx6747VQFVUtyqhwACwLA6pN68o5UYn3KdarfbPe7z4FRJ3koU36wy80lTfTWk878La9LO2PZVmUJ/8CuEDVGO+/FpanEiXXhyJ3j1BbB2BSJSTartTdEFzJ/TGaXqs0VBVLgZUsVP0EhYywkeLTSpMjc5mOkqNCR+W6SVsPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGYoILxnOsJynP3RRVmvzGIa/bhC7IAbwaGo63ldX4C7Ujd3Lxotg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEA9je9IZx6747VQFVUtyqhwACwLA6pN68o5UYn3KdarfbPe7z4FRJ3koU36wy80lTfTWk878La9LO2PZVmUJ/8CuEDVGO+/FpanEiXXhyJ3j1BbB2BSJSTartTdEFzJ/TGaXqs0VBVLgZUsVP0EhYywkeLTSpMjc5mOkqNCR+W6SVsPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGYoILxnOsJynP3RRVmvzGIa/bhC7IAbwaGo63ldX4C7Ujd3Lxotg=="
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
      "state": "tx_+NMLAfiEuEA9je9IZx6747VQFVUtyqhwACwLA6pN68o5UYn3KdarfbPe7z4FRJ3koU36wy80lTfTWk878La9LO2PZVmUJ/8CuEDVGO+/FpanEiXXhyJ3j1BbB2BSJSTartTdEFzJ/TGaXqs0VBVLgZUsVP0EhYywkeLTSpMjc5mOkqNCR+W6SVsPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGYoILxnOsJynP3RRVmvzGIa/bhC7IAbwaGo63ldX4C7Ujd3Lxotg=="
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
    "round": 152
  }
}
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 152
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 152,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
    "round": 152
  }
}
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 152
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 152,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "ABCDEFG",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
      "caller_nonce": 153,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "ABCDEFG",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "ABCDEFG",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "ABCDEFG",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgZmgooGpLNkcQyQMv4/Og8aHr1U/Wa5ngsK+gYOSVceF8826Vstu",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEAqqlBZkmuvA/eitjO7y6i3at9/igiXfKCEsa37wc1IL+KUV0RIzSGVrvT8NKXefsIF6hRwlGPkaLqZhSQJmLYHuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGZoKKBqSzZHEMkDL+PzoPGh69VP1muZ4LCvoGDklXHhfPN1tTTAA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEAqqlBZkmuvA/eitjO7y6i3at9/igiXfKCEsa37wc1IL+KUV0RIzSGVrvT8NKXefsIF6hRwlGPkaLqZhSQJmLYHuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGZoKKBqSzZHEMkDL+PzoPGh69VP1muZ4LCvoGDklXHhfPN1tTTAA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjlhY2NvdW50X3B1YmtleX+X2d0=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEAqqlBZkmuvA/eitjO7y6i3at9/igiXfKCEsa37wc1IL+KUV0RIzSGVrvT8NKXefsIF6hRwlGPkaLqZhSQJmLYHuEBBTz4bPxbzxGne4boDhq7dFkBxS4KcQ6rrnEa9noEeRYm6+tqwlocDimSWyCXPrfiIJLtxwZju5SCNYpaGoGYPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGZoKKBqSzZHEMkDL+PzoPGh69VP1muZ4LCvoGDklXHhfPNpgNRNA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEAqqlBZkmuvA/eitjO7y6i3at9/igiXfKCEsa37wc1IL+KUV0RIzSGVrvT8NKXefsIF6hRwlGPkaLqZhSQJmLYHuEBBTz4bPxbzxGne4boDhq7dFkBxS4KcQ6rrnEa9noEeRYm6+tqwlocDimSWyCXPrfiIJLtxwZju5SCNYpaGoGYPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGZoKKBqSzZHEMkDL+PzoPGh69VP1muZ4LCvoGDklXHhfPNpgNRNA=="
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
      "state": "tx_+NMLAfiEuEAqqlBZkmuvA/eitjO7y6i3at9/igiXfKCEsa37wc1IL+KUV0RIzSGVrvT8NKXefsIF6hRwlGPkaLqZhSQJmLYHuEBBTz4bPxbzxGne4boDhq7dFkBxS4KcQ6rrnEa9noEeRYm6+tqwlocDimSWyCXPrfiIJLtxwZju5SCNYpaGoGYPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGZoKKBqSzZHEMkDL+PzoPGh69VP1muZ4LCvoGDklXHhfPNpgNRNA=="
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
    "round": 153
  }
}
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 153
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 153,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
    "round": 153
  }
}
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 153
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 153,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "ABCDEFG",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
      "caller_nonce": 154,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "ABCDEFG",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "ABCDEFG",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "ABCDEFG",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgZqgCebwQiP67kXoSg8AmCaWa9ezR2xflfFayUxITZ2znBejnvnY",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuECf40hF516Q6BBIA+mMOMY9PvTQ3fcL5XLdblty+ddWwMbOnC7AAQNm5Yzq4RGmVKli/UlkEKui34LHdfwMHjMDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGaoAnm8EIj+u5F6EoPAJgmlmvXs0dsX5XxWslMSE2ds5wXmSOLCQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuECf40hF516Q6BBIA+mMOMY9PvTQ3fcL5XLdblty+ddWwMbOnC7AAQNm5Yzq4RGmVKli/UlkEKui34LHdfwMHjMDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGaoAnm8EIj+u5F6EoPAJgmlmvXs0dsX5XxWslMSE2ds5wXmSOLCQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEB8r/pi9acGNlsp5rta+0wedJlkE2CPTn1wlOIPojz9FrVY2ZbG+NYc0pGmyfeno2v3OEGY3Dp3EQNNHz5SUuUJuECf40hF516Q6BBIA+mMOMY9PvTQ3fcL5XLdblty+ddWwMbOnC7AAQNm5Yzq4RGmVKli/UlkEKui34LHdfwMHjMDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGaoAnm8EIj+u5F6EoPAJgmlmvXs0dsX5XxWslMSE2ds5wXqzP2Cg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEB8r/pi9acGNlsp5rta+0wedJlkE2CPTn1wlOIPojz9FrVY2ZbG+NYc0pGmyfeno2v3OEGY3Dp3EQNNHz5SUuUJuECf40hF516Q6BBIA+mMOMY9PvTQ3fcL5XLdblty+ddWwMbOnC7AAQNm5Yzq4RGmVKli/UlkEKui34LHdfwMHjMDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGaoAnm8EIj+u5F6EoPAJgmlmvXs0dsX5XxWslMSE2ds5wXqzP2Cg=="
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
      "state": "tx_+NMLAfiEuEB8r/pi9acGNlsp5rta+0wedJlkE2CPTn1wlOIPojz9FrVY2ZbG+NYc0pGmyfeno2v3OEGY3Dp3EQNNHz5SUuUJuECf40hF516Q6BBIA+mMOMY9PvTQ3fcL5XLdblty+ddWwMbOnC7AAQNm5Yzq4RGmVKli/UlkEKui34LHdfwMHjMDuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGaoAnm8EIj+u5F6EoPAJgmlmvXs0dsX5XxWslMSE2ds5wXqzP2Cg=="
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
    "round": 154
  }
}
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 154
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 154,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
    "round": 154
  }
}
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 154
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 154,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "ABCDEFG",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
      "caller_nonce": 155,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "ABCDEFG",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "ABCDEFG",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "ABCDEFG",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgZugmt/Mj6M9vCwRBafYCv5wb3M7hB+6ZrRabIjdGXxsFxTis76s",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEDGUx9PDeRXgz9gOCESXFz36onBAPfgFZFt/hlcbNG++4k93uhNdju/Y1i7y7fqjbq/6pE7nIX1KKmzugXN9zgEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGboJrfzI+jPbwsEQWn2Ar+cG9zO4Qfuma0WmyI3Rl8bBcUwFgprA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEDGUx9PDeRXgz9gOCESXFz36onBAPfgFZFt/hlcbNG++4k93uhNdju/Y1i7y7fqjbq/6pE7nIX1KKmzugXN9zgEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGboJrfzI+jPbwsEQWn2Ar+cG9zO4Qfuma0WmyI3Rl8bBcUwFgprA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbhlvcmFjbGWPJvZ7",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEAcTEWGdnUG6Kq4jstNn1OX/u0CQW4K7BSDUrjCUSd+sjTxaQPTpAI9oChlmXnvxUUoHn9lG2ZpXA0bdJoMZLkOuEDGUx9PDeRXgz9gOCESXFz36onBAPfgFZFt/hlcbNG++4k93uhNdju/Y1i7y7fqjbq/6pE7nIX1KKmzugXN9zgEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGboJrfzI+jPbwsEQWn2Ar+cG9zO4Qfuma0WmyI3Rl8bBcUEapGGQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEAcTEWGdnUG6Kq4jstNn1OX/u0CQW4K7BSDUrjCUSd+sjTxaQPTpAI9oChlmXnvxUUoHn9lG2ZpXA0bdJoMZLkOuEDGUx9PDeRXgz9gOCESXFz36onBAPfgFZFt/hlcbNG++4k93uhNdju/Y1i7y7fqjbq/6pE7nIX1KKmzugXN9zgEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGboJrfzI+jPbwsEQWn2Ar+cG9zO4Qfuma0WmyI3Rl8bBcUEapGGQ=="
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
      "state": "tx_+NMLAfiEuEAcTEWGdnUG6Kq4jstNn1OX/u0CQW4K7BSDUrjCUSd+sjTxaQPTpAI9oChlmXnvxUUoHn9lG2ZpXA0bdJoMZLkOuEDGUx9PDeRXgz9gOCESXFz36onBAPfgFZFt/hlcbNG++4k93uhNdju/Y1i7y7fqjbq/6pE7nIX1KKmzugXN9zgEuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGboJrfzI+jPbwsEQWn2Ar+cG9zO4Qfuma0WmyI3Rl8bBcUEapGGQ=="
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
    "round": 155
  }
}
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 155
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 155,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
    "round": 155
  }
}
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 155
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 155,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "ABCDEFG",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
      "caller_nonce": 156,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "ABCDEFG",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "ABCDEFG",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "ABCDEFG",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgZygNnawxtaOb3qBYymqwceRqj9z+nD9UMiYOXxs33zNl6j0+fJR",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEBknSkvSzxxyR4oYqooCTc3af20MKHKyjYXwqjrabVeD1H05JFsvUMAyr2bCm5LAWS5l79nu0pJpCkcxIj7iQQBuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGcoDZ2sMbWjm96gWMpqsHHkao/c/pw/VDImDl8bN98zZeo4uas3g=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEBknSkvSzxxyR4oYqooCTc3af20MKHKyjYXwqjrabVeD1H05JFsvUMAyr2bCm5LAWS5l79nu0pJpCkcxIj7iQQBuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGcoDZ2sMbWjm96gWMpqsHHkao/c/pw/VDImDl8bN98zZeo4uas3g==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEBknSkvSzxxyR4oYqooCTc3af20MKHKyjYXwqjrabVeD1H05JFsvUMAyr2bCm5LAWS5l79nu0pJpCkcxIj7iQQBuEDmTXKtLARBUt3tQqrGzAnfOILW/iS59ATc5UkWKr+YG+FSW6WqQgaH4RsAuY6maUS/+UllM3m4Sl3S7QSSe7kMuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGcoDZ2sMbWjm96gWMpqsHHkao/c/pw/VDImDl8bN98zZeo9LmCeg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEBknSkvSzxxyR4oYqooCTc3af20MKHKyjYXwqjrabVeD1H05JFsvUMAyr2bCm5LAWS5l79nu0pJpCkcxIj7iQQBuEDmTXKtLARBUt3tQqrGzAnfOILW/iS59ATc5UkWKr+YG+FSW6WqQgaH4RsAuY6maUS/+UllM3m4Sl3S7QSSe7kMuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGcoDZ2sMbWjm96gWMpqsHHkao/c/pw/VDImDl8bN98zZeo9LmCeg=="
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
      "state": "tx_+NMLAfiEuEBknSkvSzxxyR4oYqooCTc3af20MKHKyjYXwqjrabVeD1H05JFsvUMAyr2bCm5LAWS5l79nu0pJpCkcxIj7iQQBuEDmTXKtLARBUt3tQqrGzAnfOILW/iS59ATc5UkWKr+YG+FSW6WqQgaH4RsAuY6maUS/+UllM3m4Sl3S7QSSe7kMuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGcoDZ2sMbWjm96gWMpqsHHkao/c/pw/VDImDl8bN98zZeo9LmCeg=="
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
    "round": 156
  }
}
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 156
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 156,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
    "round": 156
  }
}
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 156
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 156,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "ABCDEFG",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
      "caller_nonce": 157,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "ABCDEFG",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "ABCDEFG",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "ABCDEFG",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgZ2gQsHODUOG/dvrKGR1aew4YnxOpLid/7hR+V8F1XEvqdUzGtsM",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuECJbSxTd43AZdzWZJ5FvZu1Fv6U0KbTSdPPp5ur3vjz6rWjnET8y4RGPPovg6FQ3KJ6YbmXGaqOH2fw6ibqIs0CuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGdoELBzg1Dhv3b6yhkdWnsOGJ8TqS4nf+4UflfBdVxL6nVNv91jQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuECJbSxTd43AZdzWZJ5FvZu1Fv6U0KbTSdPPp5ur3vjz6rWjnET8y4RGPPovg6FQ3KJ6YbmXGaqOH2fw6ibqIs0CuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGdoELBzg1Dhv3b6yhkdWnsOGJ8TqS4nf+4UflfBdVxL6nVNv91jQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbjl1bmV4cGVjdGVkX2tleTFtuCk=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEBfLLaPUhnJilCABkH+LJWjt2VWfYULBTUClpFVwxFWcSDSzV1oP7oWvxnC2PVtsu6SRbRjTjY61a8mdzYlyCEPuECJbSxTd43AZdzWZJ5FvZu1Fv6U0KbTSdPPp5ur3vjz6rWjnET8y4RGPPovg6FQ3KJ6YbmXGaqOH2fw6ibqIs0CuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGdoELBzg1Dhv3b6yhkdWnsOGJ8TqS4nf+4UflfBdVxL6nV2vw0kw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEBfLLaPUhnJilCABkH+LJWjt2VWfYULBTUClpFVwxFWcSDSzV1oP7oWvxnC2PVtsu6SRbRjTjY61a8mdzYlyCEPuECJbSxTd43AZdzWZJ5FvZu1Fv6U0KbTSdPPp5ur3vjz6rWjnET8y4RGPPovg6FQ3KJ6YbmXGaqOH2fw6ibqIs0CuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGdoELBzg1Dhv3b6yhkdWnsOGJ8TqS4nf+4UflfBdVxL6nV2vw0kw=="
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
      "state": "tx_+NMLAfiEuEBfLLaPUhnJilCABkH+LJWjt2VWfYULBTUClpFVwxFWcSDSzV1oP7oWvxnC2PVtsu6SRbRjTjY61a8mdzYlyCEPuECJbSxTd43AZdzWZJ5FvZu1Fv6U0KbTSdPPp5ur3vjz6rWjnET8y4RGPPovg6FQ3KJ6YbmXGaqOH2fw6ibqIs0CuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGdoELBzg1Dhv3b6yhkdWnsOGJ8TqS4nf+4UflfBdVxL6nV2vw0kw=="
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
    "round": 157
  }
}
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 157
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 157,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
    "round": 157
  }
}
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 157
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 157,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "ABCDEFG",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
      "caller_nonce": 158,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "ABCDEFG",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "ABCDEFG",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "ABCDEFG",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgZ6gJ5Avryo+8eOUiYj3oytNSHLXrKW2Isedp1dMM/avCb1kMmvv",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuECNVvbsQjfXPqyDyDD+AeAVSIAfz2/pRA4kg4ZYuEMQMA6Ns3dEFgfjCIVIIYscloEsW4rf6vPElWPUFal99eYHuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGeoCeQL68qPvHjlImI96MrTUhy16yltiLHnadXTDP2rwm9Dg8wKw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuECNVvbsQjfXPqyDyDD+AeAVSIAfz2/pRA4kg4ZYuEMQMA6Ns3dEFgfjCIVIIYscloEsW4rf6vPElWPUFal99eYHuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGeoCeQL68qPvHjlImI96MrTUhy16yltiLHnadXTDP2rwm9Dg8wKw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuECNVvbsQjfXPqyDyDD+AeAVSIAfz2/pRA4kg4ZYuEMQMA6Ns3dEFgfjCIVIIYscloEsW4rf6vPElWPUFal99eYHuECcuPB+pbUSv37YskJORk22mLxPxgfMsSswlHbnFddi7PQ31OFiVRLIZFFEEtLn1iB5Y1txgt/XXERr1JU/ZFwNuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGeoCeQL68qPvHjlImI96MrTUhy16yltiLHnadXTDP2rwm9zcQOUg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuECNVvbsQjfXPqyDyDD+AeAVSIAfz2/pRA4kg4ZYuEMQMA6Ns3dEFgfjCIVIIYscloEsW4rf6vPElWPUFal99eYHuECcuPB+pbUSv37YskJORk22mLxPxgfMsSswlHbnFddi7PQ31OFiVRLIZFFEEtLn1iB5Y1txgt/XXERr1JU/ZFwNuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGeoCeQL68qPvHjlImI96MrTUhy16yltiLHnadXTDP2rwm9zcQOUg=="
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
      "state": "tx_+NMLAfiEuECNVvbsQjfXPqyDyDD+AeAVSIAfz2/pRA4kg4ZYuEMQMA6Ns3dEFgfjCIVIIYscloEsW4rf6vPElWPUFal99eYHuECcuPB+pbUSv37YskJORk22mLxPxgfMsSswlHbnFddi7PQ31OFiVRLIZFFEEtLn1iB5Y1txgt/XXERr1JU/ZFwNuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGeoCeQL68qPvHjlImI96MrTUhy16yltiLHnadXTDP2rwm9zcQOUg=="
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
    "round": 158
  }
}
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 158
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 158,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
    "round": 158
  }
}
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 158
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 158,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "ABCDEFG",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
      "caller_nonce": 159,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "ABCDEFG",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "ABCDEFG",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "ABCDEFG",
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4"
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
      "signed_tx": "tx_+E4LAcC4SfhHOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RgZ+gH9spgmkVG8qrLrR+QOZHvWgnkY2FngsyixIlvvxrEcGw56Wb",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
          "gas": 1000000,
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
    "signed_tx": "tx_+JELAfhCuEDKG+p71BDh7/VzLnqaT6xVuDOfrDJBA66fhMzKSNyOaqdFV6v9cqwJxysEnC3X+Gcc1ShUirtgMdGliFS6tVYPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGfoB/bKYJpFRvKqy60fkDmR71oJ5GNhZ4LMosSJb78axHBT4pG0g=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JELAfhCuEDKG+p71BDh7/VzLnqaT6xVuDOfrDJBA66fhMzKSNyOaqdFV6v9cqwJxysEnC3X+Gcc1ShUirtgMdGliFS6tVYPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGfoB/bKYJpFRvKqy60fkDmR71oJ5GNhZ4LMosSJb78axHBT4pG0g==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4NWh5emFNM2IzUmJ2WC5jaGFpbi1taXNzaW5nX2tleQU1wf4=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
          "gas": 1000000,
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
    "signed_tx": "tx_+NMLAfiEuEBSEcj26VrPBf5qy439pp3tNiLjaoEH0J3u/6JGa5lfVcA5B9TMt2woluNlqLh804LJM4OiD7AAhpKL5mpdHQsFuEDKG+p71BDh7/VzLnqaT6xVuDOfrDJBA66fhMzKSNyOaqdFV6v9cqwJxysEnC3X+Gcc1ShUirtgMdGliFS6tVYPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGfoB/bKYJpFRvKqy60fkDmR71oJ5GNhZ4LMosSJb78axHBE72O5w=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NMLAfiEuEBSEcj26VrPBf5qy439pp3tNiLjaoEH0J3u/6JGa5lfVcA5B9TMt2woluNlqLh804LJM4OiD7AAhpKL5mpdHQsFuEDKG+p71BDh7/VzLnqaT6xVuDOfrDJBA66fhMzKSNyOaqdFV6v9cqwJxysEnC3X+Gcc1ShUirtgMdGliFS6tVYPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGfoB/bKYJpFRvKqy60fkDmR71oJ5GNhZ4LMosSJb78axHBE72O5w=="
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
      "state": "tx_+NMLAfiEuEBSEcj26VrPBf5qy439pp3tNiLjaoEH0J3u/6JGa5lfVcA5B9TMt2woluNlqLh804LJM4OiD7AAhpKL5mpdHQsFuEDKG+p71BDh7/VzLnqaT6xVuDOfrDJBA66fhMzKSNyOaqdFV6v9cqwJxysEnC3X+Gcc1ShUirtgMdGliFS6tVYPuEn4RzkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYGfoB/bKYJpFRvKqy60fkDmR71oJ5GNhZ4LMosSJb78axHBE72O5w=="
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
    "round": 159
  }
}
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 159
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 159,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
    "round": 159
  }
}
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
        "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 159
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 159,
      "contract_id": "ct_Yw7WppWrBWNpTYzUzXaxpzMUBuAyaqzyCgGxBXdoz4G5du1b4",
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
