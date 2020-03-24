
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEEoA4ACOiZMSAyEvUfTBmb+H+WG1vSXbaCqJqRVJi3Nhs5iHKVqw==",
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
  "id": -576460752303421347,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEC5bIbO1ZsiE4eRaT71XOHxxKtYLf49S6ggehzqFieSXXgkjrOO1+JBVV6HSvxbL4lnfsYWX/rL/p8sk/GRD6UPuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBBKAOAAjomTEgMhL1H0wZm/h/lhtb0l22gqiakVSYtzYbOe4/JPs="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEC5bIbO1ZsiE4eRaT71XOHxxKtYLf49S6ggehzqFieSXXgkjrOO1+JBVV6HSvxbL4lnfsYWX/rL/p8sk/GRD6UPuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBBKAOAAjomTEgMhL1H0wZm/h/lhtb0l22gqiakVSYtzYbOe4/JPs=",
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
  "id": -576460752303421346,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEBGQ3Zb8aI9s1oXfsnl/zVhRoTPilK9izmtNg7NOXpLwlyH5/jQa2bl/BJLhh0Fagmcf8bWemkfpuqR+HJNQ8UPuEC5bIbO1ZsiE4eRaT71XOHxxKtYLf49S6ggehzqFieSXXgkjrOO1+JBVV6HSvxbL4lnfsYWX/rL/p8sk/GRD6UPuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBBKAOAAjomTEgMhL1H0wZm/h/lhtb0l22gqiakVSYtzYbOc7mUXo="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEBGQ3Zb8aI9s1oXfsnl/zVhRoTPilK9izmtNg7NOXpLwlyH5/jQa2bl/BJLhh0Fagmcf8bWemkfpuqR+HJNQ8UPuEC5bIbO1ZsiE4eRaT71XOHxxKtYLf49S6ggehzqFieSXXgkjrOO1+JBVV6HSvxbL4lnfsYWX/rL/p8sk/GRD6UPuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBBKAOAAjomTEgMhL1H0wZm/h/lhtb0l22gqiakVSYtzYbOc7mUXo="
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
      "state": "tx_+NQLAfiEuEBGQ3Zb8aI9s1oXfsnl/zVhRoTPilK9izmtNg7NOXpLwlyH5/jQa2bl/BJLhh0Fagmcf8bWemkfpuqR+HJNQ8UPuEC5bIbO1ZsiE4eRaT71XOHxxKtYLf49S6ggehzqFieSXXgkjrOO1+JBVV6HSvxbL4lnfsYWX/rL/p8sk/GRD6UPuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBBKAOAAjomTEgMhL1H0wZm/h/lhtb0l22gqiakVSYtzYbOc7mUXo="
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEFoKbkmDMYuxnqxM6BLMWA8FdQP/OlaCzqRMDGWMl3d32R08mvjg==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
  "id": -576460752303421345,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEDABWOCmAV8Ovv0zutGMUvkn8bKQOZtuU/UpUqS+oZRjalHemHnvKz4NoS5893kllphXUtFt5Se0NunH+8JOUwHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBBaCm5JgzGLsZ6sTOgSzFgPBXUD/zpWgs6kTAxljJd3d9kaPAND4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEDABWOCmAV8Ovv0zutGMUvkn8bKQOZtuU/UpUqS+oZRjalHemHnvKz4NoS5893kllphXUtFt5Se0NunH+8JOUwHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBBaCm5JgzGLsZ6sTOgSzFgPBXUD/zpWgs6kTAxljJd3d9kaPAND4=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
  "id": -576460752303421344,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEBa9L5uj5S76cFFT0CO86u2dAZ6CsdOZgrj8x+S3MeqG+AUpPyTf2Fx5DY+4Gx3W4/VqiKdLSgWaxp2u8bccqcJuEDABWOCmAV8Ovv0zutGMUvkn8bKQOZtuU/UpUqS+oZRjalHemHnvKz4NoS5893kllphXUtFt5Se0NunH+8JOUwHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBBaCm5JgzGLsZ6sTOgSzFgPBXUD/zpWgs6kTAxljJd3d9kcUhpiA="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEBa9L5uj5S76cFFT0CO86u2dAZ6CsdOZgrj8x+S3MeqG+AUpPyTf2Fx5DY+4Gx3W4/VqiKdLSgWaxp2u8bccqcJuEDABWOCmAV8Ovv0zutGMUvkn8bKQOZtuU/UpUqS+oZRjalHemHnvKz4NoS5893kllphXUtFt5Se0NunH+8JOUwHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBBaCm5JgzGLsZ6sTOgSzFgPBXUD/zpWgs6kTAxljJd3d9kcUhpiA="
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
      "state": "tx_+NQLAfiEuEBa9L5uj5S76cFFT0CO86u2dAZ6CsdOZgrj8x+S3MeqG+AUpPyTf2Fx5DY+4Gx3W4/VqiKdLSgWaxp2u8bccqcJuEDABWOCmAV8Ovv0zutGMUvkn8bKQOZtuU/UpUqS+oZRjalHemHnvKz4NoS5893kllphXUtFt5Se0NunH+8JOUwHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBBaCm5JgzGLsZ6sTOgSzFgPBXUD/zpWgs6kTAxljJd3d9kcUhpiA="
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
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
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
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
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
      "caller_nonce": 262,
      "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
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
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
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
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
  }
}
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
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
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
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
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
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEGoD9FEMx8RutidqQHiRQ57MoWTCSQAbmiJMKRkWaHp6Hrgmy45A==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEAPwG5jvVb3ez/xpS+l7kiI5eRZV77sWkekZsR7E8FhAEbldQ8Lko5oN+NuZwmcRVov5uwHk77fjvY8XCjo5ocAuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBBqA/RRDMfEbrYnakB4kUOezKFkwkkAG5oiTCkZFmh6eh60FA4gk="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEAPwG5jvVb3ez/xpS+l7kiI5eRZV77sWkekZsR7E8FhAEbldQ8Lko5oN+NuZwmcRVov5uwHk77fjvY8XCjo5ocAuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBBqA/RRDMfEbrYnakB4kUOezKFkwkkAG5oiTCkZFmh6eh60FA4gk=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEAPwG5jvVb3ez/xpS+l7kiI5eRZV77sWkekZsR7E8FhAEbldQ8Lko5oN+NuZwmcRVov5uwHk77fjvY8XCjo5ocAuEAS1Ty3w1ph5fwvpXeR8HpSI+1fJ178Ba9/TqAaLzCjaTqfj+IMOeKI8y9zhrrD/bIzGx2lDhP9ZYGS8BxfOscCuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBBqA/RRDMfEbrYnakB4kUOezKFkwkkAG5oiTCkZFmh6eh6zGDC9c="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEAPwG5jvVb3ez/xpS+l7kiI5eRZV77sWkekZsR7E8FhAEbldQ8Lko5oN+NuZwmcRVov5uwHk77fjvY8XCjo5ocAuEAS1Ty3w1ph5fwvpXeR8HpSI+1fJ178Ba9/TqAaLzCjaTqfj+IMOeKI8y9zhrrD/bIzGx2lDhP9ZYGS8BxfOscCuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBBqA/RRDMfEbrYnakB4kUOezKFkwkkAG5oiTCkZFmh6eh6zGDC9c="
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
      "state": "tx_+NQLAfiEuEAPwG5jvVb3ez/xpS+l7kiI5eRZV77sWkekZsR7E8FhAEbldQ8Lko5oN+NuZwmcRVov5uwHk77fjvY8XCjo5ocAuEAS1Ty3w1ph5fwvpXeR8HpSI+1fJ178Ba9/TqAaLzCjaTqfj+IMOeKI8y9zhrrD/bIzGx2lDhP9ZYGS8BxfOscCuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBBqA/RRDMfEbrYnakB4kUOezKFkwkkAG5oiTCkZFmh6eh6zGDC9c="
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
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
    "round": 262
  }
}
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
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 262
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 262,
      "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
    "round": 262
  }
}
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
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 262
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 262,
      "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
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
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
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
      "caller_nonce": 263,
      "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
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
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
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
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
  }
}
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
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
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
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
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
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEHoLE7nEfwOWQdbPzuF491W5qxCVQzHLtWQADDPxNtBYZKx12nnw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEBbjVR/ZqSIsjw5dwVYn/CUipz8pQtXMy5Ns/4ePo0/6CXIYynTH7LOiGMg/VC1AWN5A54eHK3r+nGSVJKIax4EuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBB6CxO5xH8DlkHWz87hePdVuasQlUMxy7VkAAwz8TbQWGSmXz9to="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEBbjVR/ZqSIsjw5dwVYn/CUipz8pQtXMy5Ns/4ePo0/6CXIYynTH7LOiGMg/VC1AWN5A54eHK3r+nGSVJKIax4EuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBB6CxO5xH8DlkHWz87hePdVuasQlUMxy7VkAAwz8TbQWGSmXz9to=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEBOknyB7plI3sbWNj8NTS44TLy89axEXiM51xDcf3cZQWwOr+3T333rJp1RYUG0EJkzpz32C+yQkXi980vpYHkMuEBbjVR/ZqSIsjw5dwVYn/CUipz8pQtXMy5Ns/4ePo0/6CXIYynTH7LOiGMg/VC1AWN5A54eHK3r+nGSVJKIax4EuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBB6CxO5xH8DlkHWz87hePdVuasQlUMxy7VkAAwz8TbQWGSs2eGfw="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEBOknyB7plI3sbWNj8NTS44TLy89axEXiM51xDcf3cZQWwOr+3T333rJp1RYUG0EJkzpz32C+yQkXi980vpYHkMuEBbjVR/ZqSIsjw5dwVYn/CUipz8pQtXMy5Ns/4ePo0/6CXIYynTH7LOiGMg/VC1AWN5A54eHK3r+nGSVJKIax4EuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBB6CxO5xH8DlkHWz87hePdVuasQlUMxy7VkAAwz8TbQWGSs2eGfw="
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
      "state": "tx_+NQLAfiEuEBOknyB7plI3sbWNj8NTS44TLy89axEXiM51xDcf3cZQWwOr+3T333rJp1RYUG0EJkzpz32C+yQkXi980vpYHkMuEBbjVR/ZqSIsjw5dwVYn/CUipz8pQtXMy5Ns/4ePo0/6CXIYynTH7LOiGMg/VC1AWN5A54eHK3r+nGSVJKIax4EuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBB6CxO5xH8DlkHWz87hePdVuasQlUMxy7VkAAwz8TbQWGSs2eGfw="
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
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
    "round": 263
  }
}
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
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 263
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 263,
      "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
    "round": 263
  }
}
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
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 263
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 263,
      "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
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
      "caller_nonce": 264,
      "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
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
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEIoBtYE/OBB7ooz4pOBqOch2XQEBDIB7IYYh3VWk3SN5F//T0ssw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEA5UgA16dSV9UKbR09gsKVAImlBIwXdNETXVYYDrvi+D4dN1Q8pqB6F/GziUiKWbSxl63YCqYpdFn0TQK9m55YIuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBCKAbWBPzgQe6KM+KTgajnIdl0BAQyAeyGGId1VpN0jeRf7jIgxE="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEA5UgA16dSV9UKbR09gsKVAImlBIwXdNETXVYYDrvi+D4dN1Q8pqB6F/GziUiKWbSxl63YCqYpdFn0TQK9m55YIuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBCKAbWBPzgQe6KM+KTgajnIdl0BAQyAeyGGId1VpN0jeRf7jIgxE=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEA5UgA16dSV9UKbR09gsKVAImlBIwXdNETXVYYDrvi+D4dN1Q8pqB6F/GziUiKWbSxl63YCqYpdFn0TQK9m55YIuEBYmnEWKCzUJJ4eU1Sh/gomycD8ovMAKVBjis8mO4K4MhnO+hoJA60fIjbS1nymeShIixsEU3mr4Y91tdfBXl8FuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBCKAbWBPzgQe6KM+KTgajnIdl0BAQyAeyGGId1VpN0jeRf9ucgOQ="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEA5UgA16dSV9UKbR09gsKVAImlBIwXdNETXVYYDrvi+D4dN1Q8pqB6F/GziUiKWbSxl63YCqYpdFn0TQK9m55YIuEBYmnEWKCzUJJ4eU1Sh/gomycD8ovMAKVBjis8mO4K4MhnO+hoJA60fIjbS1nymeShIixsEU3mr4Y91tdfBXl8FuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBCKAbWBPzgQe6KM+KTgajnIdl0BAQyAeyGGId1VpN0jeRf9ucgOQ="
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
      "state": "tx_+NQLAfiEuEA5UgA16dSV9UKbR09gsKVAImlBIwXdNETXVYYDrvi+D4dN1Q8pqB6F/GziUiKWbSxl63YCqYpdFn0TQK9m55YIuEBYmnEWKCzUJJ4eU1Sh/gomycD8ovMAKVBjis8mO4K4MhnO+hoJA60fIjbS1nymeShIixsEU3mr4Y91tdfBXl8FuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBCKAbWBPzgQe6KM+KTgajnIdl0BAQyAeyGGId1VpN0jeRf9ucgOQ="
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
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
    "round": 264
  }
}
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
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 264
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 264,
      "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
    "round": 264
  }
}
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
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 264
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 264,
      "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
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
      "caller_nonce": 265,
      "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
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
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
  }
}
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
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
        "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
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
    "block_hash": "kh_2TFxwPY93pQYwbqFtvuFM82uj3FmcULFbhPn2cqnVJu6WroqP5",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEJoKaOlPjQ/UDP1mAlSHKTJl4aRf6Tu4sLyn5L+Ojz/lJezN3ugg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEBkY6Sw7KjPMmpJ5grePQAOpVybZFfwD6DlxGoYBHs21Gq8kjVmp73QPcLkaYmARG2cAfGJNQZ3vCRgX/cZl74FuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBCaCmjpT40P1Az9ZgJUhykyZeGkX+k7uLC8p+S/jo8/5SXnliJ/4="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEBkY6Sw7KjPMmpJ5grePQAOpVybZFfwD6DlxGoYBHs21Gq8kjVmp73QPcLkaYmARG2cAfGJNQZ3vCRgX/cZl74FuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBCaCmjpT40P1Az9ZgJUhykyZeGkX+k7uLC8p+S/jo8/5SXnliJ/4=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEBkY6Sw7KjPMmpJ5grePQAOpVybZFfwD6DlxGoYBHs21Gq8kjVmp73QPcLkaYmARG2cAfGJNQZ3vCRgX/cZl74FuEDXRvk4PO5f7A6Lb03LaQTPhm99wNF+68OSKn12e+94auijg5q0u3g2PYcsYjh1p13w5Yvwn4KCzSkhzvoDciwCuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBCaCmjpT40P1Az9ZgJUhykyZeGkX+k7uLC8p+S/jo8/5SXuLvNys="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEBkY6Sw7KjPMmpJ5grePQAOpVybZFfwD6DlxGoYBHs21Gq8kjVmp73QPcLkaYmARG2cAfGJNQZ3vCRgX/cZl74FuEDXRvk4PO5f7A6Lb03LaQTPhm99wNF+68OSKn12e+94auijg5q0u3g2PYcsYjh1p13w5Yvwn4KCzSkhzvoDciwCuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBCaCmjpT40P1Az9ZgJUhykyZeGkX+k7uLC8p+S/jo8/5SXuLvNys="
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
      "state": "tx_+NQLAfiEuEBkY6Sw7KjPMmpJ5grePQAOpVybZFfwD6DlxGoYBHs21Gq8kjVmp73QPcLkaYmARG2cAfGJNQZ3vCRgX/cZl74FuEDXRvk4PO5f7A6Lb03LaQTPhm99wNF+68OSKn12e+94auijg5q0u3g2PYcsYjh1p13w5Yvwn4KCzSkhzvoDciwCuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBCaCmjpT40P1Az9ZgJUhykyZeGkX+k7uLC8p+S/jo8/5SXuLvNys="
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
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
    "round": 265
  }
}
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
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 265
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 265,
      "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
    "round": 265
  }
}
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
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 265
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 265,
      "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
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
      "caller_nonce": 266,
      "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
  }
}
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEKoFw4RcDWdVzFK0mkh5IHMMoehfMjcNxfXDIcyWe3Pa3ySgZCMg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEAPMMhPkri0RA62XcdzxUZaRw+3lR+tJF85yUOjVwBbZ+BrLN3CmqJla66swBpyG47AHbWU8+UR7A8yxsd+oLUMuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBCqBcOEXA1nVcxStJpIeSBzDKHoXzI3DcX1wyHMlntz2t8oh30D0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEAPMMhPkri0RA62XcdzxUZaRw+3lR+tJF85yUOjVwBbZ+BrLN3CmqJla66swBpyG47AHbWU8+UR7A8yxsd+oLUMuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBCqBcOEXA1nVcxStJpIeSBzDKHoXzI3DcX1wyHMlntz2t8oh30D0=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEAPMMhPkri0RA62XcdzxUZaRw+3lR+tJF85yUOjVwBbZ+BrLN3CmqJla66swBpyG47AHbWU8+UR7A8yxsd+oLUMuEBkjW+pn8L46sfbk9k3Aiut0GVN4MctZnX0hS2MqmojhfJSouodE0PPB3YrDAIKwKaqfdFeVF3+4nkyMLAEZwQHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBCqBcOEXA1nVcxStJpIeSBzDKHoXzI3DcX1wyHMlntz2t8hlPf1o="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEAPMMhPkri0RA62XcdzxUZaRw+3lR+tJF85yUOjVwBbZ+BrLN3CmqJla66swBpyG47AHbWU8+UR7A8yxsd+oLUMuEBkjW+pn8L46sfbk9k3Aiut0GVN4MctZnX0hS2MqmojhfJSouodE0PPB3YrDAIKwKaqfdFeVF3+4nkyMLAEZwQHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBCqBcOEXA1nVcxStJpIeSBzDKHoXzI3DcX1wyHMlntz2t8hlPf1o="
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
      "state": "tx_+NQLAfiEuEAPMMhPkri0RA62XcdzxUZaRw+3lR+tJF85yUOjVwBbZ+BrLN3CmqJla66swBpyG47AHbWU8+UR7A8yxsd+oLUMuEBkjW+pn8L46sfbk9k3Aiut0GVN4MctZnX0hS2MqmojhfJSouodE0PPB3YrDAIKwKaqfdFeVF3+4nkyMLAEZwQHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBCqBcOEXA1nVcxStJpIeSBzDKHoXzI3DcX1wyHMlntz2t8hlPf1o="
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
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
    "round": 266
  }
}
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
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 266
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 266,
      "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
    "round": 266
  }
}
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
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 266
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 266,
      "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
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
      "caller_nonce": 267,
      "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
  }
}
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggELoA3tAT1MSjgVpfoXwd6sbpe9IBFYHSWN3YrPsPXxXR43XQvarA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEBHq6x+zJga1ntK4QlSHEf7WrCHZZgY0sR5BxZUBfp3V1xACWllr4MKFxDKzO23TyLKMwlxfe3XYeLZFyz9qroGuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBC6AN7QE9TEo4FaX6F8HerG6XvSARWB0ljd2Kz7D18V0eN3nHQ6E="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEBHq6x+zJga1ntK4QlSHEf7WrCHZZgY0sR5BxZUBfp3V1xACWllr4MKFxDKzO23TyLKMwlxfe3XYeLZFyz9qroGuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBC6AN7QE9TEo4FaX6F8HerG6XvSARWB0ljd2Kz7D18V0eN3nHQ6E=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E2anIxWWs5aW1oaUJhVy5jaGFpbjlhY2NvdW50X3B1YmtlecDpX5k=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEBHq6x+zJga1ntK4QlSHEf7WrCHZZgY0sR5BxZUBfp3V1xACWllr4MKFxDKzO23TyLKMwlxfe3XYeLZFyz9qroGuECLuiFoYVDmo9+9vadMuxwnVyy8VZUN/TmzqlZB5aG46Rmen1ulcqVvoOzPYhMM2yKlbQY8Ec2BYGTiDPt4X8APuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBC6AN7QE9TEo4FaX6F8HerG6XvSARWB0ljd2Kz7D18V0eN3TFNWo="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEBHq6x+zJga1ntK4QlSHEf7WrCHZZgY0sR5BxZUBfp3V1xACWllr4MKFxDKzO23TyLKMwlxfe3XYeLZFyz9qroGuECLuiFoYVDmo9+9vadMuxwnVyy8VZUN/TmzqlZB5aG46Rmen1ulcqVvoOzPYhMM2yKlbQY8Ec2BYGTiDPt4X8APuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBC6AN7QE9TEo4FaX6F8HerG6XvSARWB0ljd2Kz7D18V0eN3TFNWo="
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
      "state": "tx_+NQLAfiEuEBHq6x+zJga1ntK4QlSHEf7WrCHZZgY0sR5BxZUBfp3V1xACWllr4MKFxDKzO23TyLKMwlxfe3XYeLZFyz9qroGuECLuiFoYVDmo9+9vadMuxwnVyy8VZUN/TmzqlZB5aG46Rmen1ulcqVvoOzPYhMM2yKlbQY8Ec2BYGTiDPt4X8APuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBC6AN7QE9TEo4FaX6F8HerG6XvSARWB0ljd2Kz7D18V0eN3TFNWo="
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
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
    "round": 267
  }
}
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
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 267
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 267,
      "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
    "round": 267
  }
}
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
        "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 267
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 267,
      "contract_id": "ct_2U3Da9mXSvDn6wFGgaUbvox9svqUzE1oHv8DmJa4qNr3ASy4yR",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
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
      "caller_nonce": 268,
      "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
  }
}
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEMoIHQ1QZyLSbGPKCOkB8p5hK3CuPGWId1dyYoSvWuAdlJqGWL/A==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEDd3iJW2XLKvTrBrQU9uUA0QqNiiG197qJ/1q6EnVr8dnm44HU5N+1sgnizj9RdSwlkAsa9ih2JhJb9LP0LvyUKuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBDKCB0NUGci0mxjygjpAfKeYStwrjxliHdXcmKEr1rgHZSf5v5RM="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEDd3iJW2XLKvTrBrQU9uUA0QqNiiG197qJ/1q6EnVr8dnm44HU5N+1sgnizj9RdSwlkAsa9ih2JhJb9LP0LvyUKuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBDKCB0NUGci0mxjygjpAfKeYStwrjxliHdXcmKEr1rgHZSf5v5RM=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEDd3iJW2XLKvTrBrQU9uUA0QqNiiG197qJ/1q6EnVr8dnm44HU5N+1sgnizj9RdSwlkAsa9ih2JhJb9LP0LvyUKuEDxuUsn3rMZEJgVKE66GNKRUOqFWVcn06BN+iJ1M8axVtYfdMzhEknj0M1MVznoYEZRJdqIF49LhpflRjWfsX0EuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBDKCB0NUGci0mxjygjpAfKeYStwrjxliHdXcmKEr1rgHZSawjqs0="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEDd3iJW2XLKvTrBrQU9uUA0QqNiiG197qJ/1q6EnVr8dnm44HU5N+1sgnizj9RdSwlkAsa9ih2JhJb9LP0LvyUKuEDxuUsn3rMZEJgVKE66GNKRUOqFWVcn06BN+iJ1M8axVtYfdMzhEknj0M1MVznoYEZRJdqIF49LhpflRjWfsX0EuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBDKCB0NUGci0mxjygjpAfKeYStwrjxliHdXcmKEr1rgHZSawjqs0="
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
      "state": "tx_+NQLAfiEuEDd3iJW2XLKvTrBrQU9uUA0QqNiiG197qJ/1q6EnVr8dnm44HU5N+1sgnizj9RdSwlkAsa9ih2JhJb9LP0LvyUKuEDxuUsn3rMZEJgVKE66GNKRUOqFWVcn06BN+iJ1M8axVtYfdMzhEknj0M1MVznoYEZRJdqIF49LhpflRjWfsX0EuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBDKCB0NUGci0mxjygjpAfKeYStwrjxliHdXcmKEr1rgHZSawjqs0="
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
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
    "round": 268
  }
}
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
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 268
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 268,
      "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
    "round": 268
  }
}
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
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 268
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 268,
      "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
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
      "caller_nonce": 269,
      "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
  }
}
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggENoKpNRSxw9h7dsMQ5cn1CGTZs5O5N46cWZdgNGDqgiEeeL4mWYA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEBAwoMssgWKB8T9jiCocjpo6p4Rawze3TDsDmqSgdad4g3E+9TOr/MVacgM9zUZ78PpScxT/a21q7CJoBtAqbQIuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBDaCqTUUscPYe3bDEOXJ9Qhk2bOTuTeOnFmXYDRg6oIhHntbn0Tc="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEBAwoMssgWKB8T9jiCocjpo6p4Rawze3TDsDmqSgdad4g3E+9TOr/MVacgM9zUZ78PpScxT/a21q7CJoBtAqbQIuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBDaCqTUUscPYe3bDEOXJ9Qhk2bOTuTeOnFmXYDRg6oIhHntbn0Tc=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoMEW9VgKNr69suLiWwllwCRtMFh1/us+bH943vggA4J8UTZqcjFZazlpbWhpQmFXLmNoYWluOWFjY291bnRfcHVia2V5eVnlHw==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEBAwoMssgWKB8T9jiCocjpo6p4Rawze3TDsDmqSgdad4g3E+9TOr/MVacgM9zUZ78PpScxT/a21q7CJoBtAqbQIuEBRTH7cBTDITMQnvgl/47N2C0IcoMOYgQeVRxs16fkdRIcXfARZVmoqSLCWZZQmizPm8rxWPHOIGVt/ZDs3szQKuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBDaCqTUUscPYe3bDEOXJ9Qhk2bOTuTeOnFmXYDRg6oIhHnrKanR4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEBAwoMssgWKB8T9jiCocjpo6p4Rawze3TDsDmqSgdad4g3E+9TOr/MVacgM9zUZ78PpScxT/a21q7CJoBtAqbQIuEBRTH7cBTDITMQnvgl/47N2C0IcoMOYgQeVRxs16fkdRIcXfARZVmoqSLCWZZQmizPm8rxWPHOIGVt/ZDs3szQKuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBDaCqTUUscPYe3bDEOXJ9Qhk2bOTuTeOnFmXYDRg6oIhHnrKanR4="
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
      "state": "tx_+NQLAfiEuEBAwoMssgWKB8T9jiCocjpo6p4Rawze3TDsDmqSgdad4g3E+9TOr/MVacgM9zUZ78PpScxT/a21q7CJoBtAqbQIuEBRTH7cBTDITMQnvgl/47N2C0IcoMOYgQeVRxs16fkdRIcXfARZVmoqSLCWZZQmizPm8rxWPHOIGVt/ZDs3szQKuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBDaCqTUUscPYe3bDEOXJ9Qhk2bOTuTeOnFmXYDRg6oIhHnrKanR4="
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
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
    "round": 269
  }
}
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
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 269
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 269,
      "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
    "round": 269
  }
}
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
        "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 269
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 269,
      "contract_id": "ct_2QZZC6URCWy1ESFuMaa7XDa9dKWvK9xqEJ1FEEK8aae2rrkikP",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEOoGmAryPvnciChaZ/iq4gnu5tk3pjf0+Bgyk0I+7sfjDzfi8+DQ==",
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
  "id": -576460752303421327,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuECl0bmAHhi9uEJ60JUYtycnwZQX5d3wrvpEZo7Sk7ks11CrSm8Al//DGwQmQay0o9WgSHr7meZDu9dSnm7lPpABuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBDqBpgK8j753IgoWmf4quIJ7ubZN6Y39PgYMpNCPu7H4w83WoQZ0="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuECl0bmAHhi9uEJ60JUYtycnwZQX5d3wrvpEZo7Sk7ks11CrSm8Al//DGwQmQay0o9WgSHr7meZDu9dSnm7lPpABuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBDqBpgK8j753IgoWmf4quIJ7ubZN6Y39PgYMpNCPu7H4w83WoQZ0=",
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
  "id": -576460752303421326,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuECl0bmAHhi9uEJ60JUYtycnwZQX5d3wrvpEZo7Sk7ks11CrSm8Al//DGwQmQay0o9WgSHr7meZDu9dSnm7lPpABuEDvp0Q1x8Et2s6ZM5UNpdsm/L1WsMGCDOLenwc+urdtLCG9EXFet76H2aKuNgFlE7MfSaolSXUBtn10OesEXtoEuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBDqBpgK8j753IgoWmf4quIJ7ubZN6Y39PgYMpNCPu7H4w88l6AwU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuECl0bmAHhi9uEJ60JUYtycnwZQX5d3wrvpEZo7Sk7ks11CrSm8Al//DGwQmQay0o9WgSHr7meZDu9dSnm7lPpABuEDvp0Q1x8Et2s6ZM5UNpdsm/L1WsMGCDOLenwc+urdtLCG9EXFet76H2aKuNgFlE7MfSaolSXUBtn10OesEXtoEuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBDqBpgK8j753IgoWmf4quIJ7ubZN6Y39PgYMpNCPu7H4w88l6AwU="
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
      "state": "tx_+NQLAfiEuECl0bmAHhi9uEJ60JUYtycnwZQX5d3wrvpEZo7Sk7ks11CrSm8Al//DGwQmQay0o9WgSHr7meZDu9dSnm7lPpABuEDvp0Q1x8Et2s6ZM5UNpdsm/L1WsMGCDOLenwc+urdtLCG9EXFet76H2aKuNgFlE7MfSaolSXUBtn10OesEXtoEuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBDqBpgK8j753IgoWmf4quIJ7ubZN6Y39PgYMpNCPu7H4w88l6AwU="
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEPoFcuo1M2Tr1iBkGXHAoylGkXonxr/XSNBNgeu0WGFMESRZsVzA==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
  "id": -576460752303421325,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEAgtVWD4qH9XfUre4iuSctjMbUdpcU/OXwsRIaWLCxr/W2tfNJ/nrxZah62Xd68ZVkSWRTr05IwlvG0UQoWMKQOuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBD6BXLqNTNk69YgZBlxwKMpRpF6J8a/10jQTYHrtFhhTBEhAu4HE="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEAgtVWD4qH9XfUre4iuSctjMbUdpcU/OXwsRIaWLCxr/W2tfNJ/nrxZah62Xd68ZVkSWRTr05IwlvG0UQoWMKQOuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBD6BXLqNTNk69YgZBlxwKMpRpF6J8a/10jQTYHrtFhhTBEhAu4HE=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
  "id": -576460752303421324,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEAgtVWD4qH9XfUre4iuSctjMbUdpcU/OXwsRIaWLCxr/W2tfNJ/nrxZah62Xd68ZVkSWRTr05IwlvG0UQoWMKQOuEDvYthFKnSM7KJaeRcAjrkyOmklkJwY0tAPiQX663Tj9/YTgy/QQ+X6bxQP7u6b1zW1Jxa7HZtJW49GMQz9oZsEuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBD6BXLqNTNk69YgZBlxwKMpRpF6J8a/10jQTYHrtFhhTBEu2A59I="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEAgtVWD4qH9XfUre4iuSctjMbUdpcU/OXwsRIaWLCxr/W2tfNJ/nrxZah62Xd68ZVkSWRTr05IwlvG0UQoWMKQOuEDvYthFKnSM7KJaeRcAjrkyOmklkJwY0tAPiQX663Tj9/YTgy/QQ+X6bxQP7u6b1zW1Jxa7HZtJW49GMQz9oZsEuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBD6BXLqNTNk69YgZBlxwKMpRpF6J8a/10jQTYHrtFhhTBEu2A59I="
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
      "state": "tx_+NQLAfiEuEAgtVWD4qH9XfUre4iuSctjMbUdpcU/OXwsRIaWLCxr/W2tfNJ/nrxZah62Xd68ZVkSWRTr05IwlvG0UQoWMKQOuEDvYthFKnSM7KJaeRcAjrkyOmklkJwY0tAPiQX663Tj9/YTgy/QQ+X6bxQP7u6b1zW1Jxa7HZtJW49GMQz9oZsEuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBD6BXLqNTNk69YgZBlxwKMpRpF6J8a/10jQTYHrtFhhTBEu2A59I="
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
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
      "caller_nonce": 272,
      "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
  }
}
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEQoAVoK8PqJN9QY+SaaMuHwBS/qyD+IQHo32+ya+5Mca9aoVGrWw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEDkLqQ9s5F4DjWvYip03Utn6+QhS+uZ2ADOi7rIDZdi1T8LrcHF+xZQ6jMd50o08oFGGT1RnHL/Rricmvpc/EoHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBEKAFaCvD6iTfUGPkmmjLh8AUv6sg/iEB6N9vsmvuTHGvWsgy/u0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEDkLqQ9s5F4DjWvYip03Utn6+QhS+uZ2ADOi7rIDZdi1T8LrcHF+xZQ6jMd50o08oFGGT1RnHL/Rricmvpc/EoHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBEKAFaCvD6iTfUGPkmmjLh8AUv6sg/iEB6N9vsmvuTHGvWsgy/u0=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEC6rFuXk0b2KviNT11cu10MNuBpxIGZIWOvW56iECW0cECM6ih5bAqrlVt4fQJogqvLxxaTAImHlWzUA58fMrYJuEDkLqQ9s5F4DjWvYip03Utn6+QhS+uZ2ADOi7rIDZdi1T8LrcHF+xZQ6jMd50o08oFGGT1RnHL/Rricmvpc/EoHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBEKAFaCvD6iTfUGPkmmjLh8AUv6sg/iEB6N9vsmvuTHGvWoVvXm8="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEC6rFuXk0b2KviNT11cu10MNuBpxIGZIWOvW56iECW0cECM6ih5bAqrlVt4fQJogqvLxxaTAImHlWzUA58fMrYJuEDkLqQ9s5F4DjWvYip03Utn6+QhS+uZ2ADOi7rIDZdi1T8LrcHF+xZQ6jMd50o08oFGGT1RnHL/Rricmvpc/EoHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBEKAFaCvD6iTfUGPkmmjLh8AUv6sg/iEB6N9vsmvuTHGvWoVvXm8="
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
      "state": "tx_+NQLAfiEuEC6rFuXk0b2KviNT11cu10MNuBpxIGZIWOvW56iECW0cECM6ih5bAqrlVt4fQJogqvLxxaTAImHlWzUA58fMrYJuEDkLqQ9s5F4DjWvYip03Utn6+QhS+uZ2ADOi7rIDZdi1T8LrcHF+xZQ6jMd50o08oFGGT1RnHL/Rricmvpc/EoHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBEKAFaCvD6iTfUGPkmmjLh8AUv6sg/iEB6N9vsmvuTHGvWoVvXm8="
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
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
    "round": 272
  }
}
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
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 272
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 272,
      "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
    "round": 272
  }
}
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
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 272
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 272,
      "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
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
      "caller_nonce": 273,
      "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
  }
}
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggERoNrQ2zXhMYgN3HaegmjuRQs7ReH8NulDAQ0PzrC+YsNuTw6rXw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEDT1kuePkBR33UQHGAccwk85cELWUYQxcKJkiGwd0MHPCnlqM6qviG0DRtaL9oI6a+c7aJeaY92RPDhFEbKC1sHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBEaDa0Ns14TGIDdx2noJo7kULO0Xh/DbpQwEND86wvmLDbhNp1ds="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEDT1kuePkBR33UQHGAccwk85cELWUYQxcKJkiGwd0MHPCnlqM6qviG0DRtaL9oI6a+c7aJeaY92RPDhFEbKC1sHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBEaDa0Ns14TGIDdx2noJo7kULO0Xh/DbpQwEND86wvmLDbhNp1ds=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEAQBQAky5L8R8AbniyOVk8M3g2RIgp3CwB8OyJet5o/owHaHvFuSJcakX0e0dPUETWvGE0+1fXTlQ5vn3oiQ14LuEDT1kuePkBR33UQHGAccwk85cELWUYQxcKJkiGwd0MHPCnlqM6qviG0DRtaL9oI6a+c7aJeaY92RPDhFEbKC1sHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBEaDa0Ns14TGIDdx2noJo7kULO0Xh/DbpQwEND86wvmLDbpMCn6A="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEAQBQAky5L8R8AbniyOVk8M3g2RIgp3CwB8OyJet5o/owHaHvFuSJcakX0e0dPUETWvGE0+1fXTlQ5vn3oiQ14LuEDT1kuePkBR33UQHGAccwk85cELWUYQxcKJkiGwd0MHPCnlqM6qviG0DRtaL9oI6a+c7aJeaY92RPDhFEbKC1sHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBEaDa0Ns14TGIDdx2noJo7kULO0Xh/DbpQwEND86wvmLDbpMCn6A="
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
      "state": "tx_+NQLAfiEuEAQBQAky5L8R8AbniyOVk8M3g2RIgp3CwB8OyJet5o/owHaHvFuSJcakX0e0dPUETWvGE0+1fXTlQ5vn3oiQ14LuEDT1kuePkBR33UQHGAccwk85cELWUYQxcKJkiGwd0MHPCnlqM6qviG0DRtaL9oI6a+c7aJeaY92RPDhFEbKC1sHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBEaDa0Ns14TGIDdx2noJo7kULO0Xh/DbpQwEND86wvmLDbpMCn6A="
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
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
    "round": 273
  }
}
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
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 273
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 273,
      "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
    "round": 273
  }
}
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
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 273
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 273,
      "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "ABCDEFG",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
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
      "caller_nonce": 274,
      "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "ABCDEFG",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "ABCDEFG",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
  }
}
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "ABCDEFG",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggESoOS1Qa1QpR1Me0VgwAWPDbfEcHiNRee5K9DxBrxfEujfiV0hZA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuECKTOQ1+QT06P73tRmTylN7DI9a15L/+i0+UjeRGoYq1/v+wK9rJRBbXdTtZDWX1sM3HB+d/YjiohoyB0H28mQJuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBEqDktUGtUKUdTHtFYMAFjw23xHB4jUXnuSvQ8Qa8XxLo35SY8TI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuECKTOQ1+QT06P73tRmTylN7DI9a15L/+i0+UjeRGoYq1/v+wK9rJRBbXdTtZDWX1sM3HB+d/YjiohoyB0H28mQJuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBEqDktUGtUKUdTHtFYMAFjw23xHB4jUXnuSvQ8Qa8XxLo35SY8TI=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEAdoMTyJKGcGbfKx5hxJOjfE3H9m3N+xXKnnkYwhwdCrlkA4G6JtzVGMTL7iiUgDfIUeTA7DDjoplypCyy2QRoHuECKTOQ1+QT06P73tRmTylN7DI9a15L/+i0+UjeRGoYq1/v+wK9rJRBbXdTtZDWX1sM3HB+d/YjiohoyB0H28mQJuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBEqDktUGtUKUdTHtFYMAFjw23xHB4jUXnuSvQ8Qa8XxLo34DIqD4="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEAdoMTyJKGcGbfKx5hxJOjfE3H9m3N+xXKnnkYwhwdCrlkA4G6JtzVGMTL7iiUgDfIUeTA7DDjoplypCyy2QRoHuECKTOQ1+QT06P73tRmTylN7DI9a15L/+i0+UjeRGoYq1/v+wK9rJRBbXdTtZDWX1sM3HB+d/YjiohoyB0H28mQJuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBEqDktUGtUKUdTHtFYMAFjw23xHB4jUXnuSvQ8Qa8XxLo34DIqD4="
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
      "state": "tx_+NQLAfiEuEAdoMTyJKGcGbfKx5hxJOjfE3H9m3N+xXKnnkYwhwdCrlkA4G6JtzVGMTL7iiUgDfIUeTA7DDjoplypCyy2QRoHuECKTOQ1+QT06P73tRmTylN7DI9a15L/+i0+UjeRGoYq1/v+wK9rJRBbXdTtZDWX1sM3HB+d/YjiohoyB0H28mQJuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBEqDktUGtUKUdTHtFYMAFjw23xHB4jUXnuSvQ8Qa8XxLo34DIqD4="
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
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
    "round": 274
  }
}
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
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 274
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 274,
      "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
    "round": 274
  }
}
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
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 274
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 274,
      "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "ABCDEFG",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
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
      "caller_nonce": 275,
      "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "ABCDEFG",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "ABCDEFG",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
  }
}
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "ABCDEFG",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
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
        "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
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
    "block_hash": "kh_2sw5ydVKHb3E1Efr7eUiCfWso3JKR2ENUfjGudsWXFuf4KtgJo",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEToB7JwieuF3CXljs2p/Mv3SdgHUfwXnc1yvGBGI9MflpTPf02iQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEBuJkQe4jgfO5o0zwzL4tcxwy1atjXrel0YPeVOsCRgcDZWYutaksdrntjMHC/OfMTzQ02eKckAarDr+DisgIEFuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBE6AeycInrhdwl5Y7NqfzL90nYB1H8F53NcrxgRiPTH5aU/2G5ZE="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEBuJkQe4jgfO5o0zwzL4tcxwy1atjXrel0YPeVOsCRgcDZWYutaksdrntjMHC/OfMTzQ02eKckAarDr+DisgIEFuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBE6AeycInrhdwl5Y7NqfzL90nYB1H8F53NcrxgRiPTH5aU/2G5ZE=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEBuJkQe4jgfO5o0zwzL4tcxwy1atjXrel0YPeVOsCRgcDZWYutaksdrntjMHC/OfMTzQ02eKckAarDr+DisgIEFuEB/44flnc4kKEKqguaKMTpm2o85goeimocard0gsTtEPPOgLKD1/4XEGhJmZ4HgqOPzbYLiyOOdlGzoqBZmUj8OuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBE6AeycInrhdwl5Y7NqfzL90nYB1H8F53NcrxgRiPTH5aU0HjRIM="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEBuJkQe4jgfO5o0zwzL4tcxwy1atjXrel0YPeVOsCRgcDZWYutaksdrntjMHC/OfMTzQ02eKckAarDr+DisgIEFuEB/44flnc4kKEKqguaKMTpm2o85goeimocard0gsTtEPPOgLKD1/4XEGhJmZ4HgqOPzbYLiyOOdlGzoqBZmUj8OuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBE6AeycInrhdwl5Y7NqfzL90nYB1H8F53NcrxgRiPTH5aU0HjRIM="
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
      "state": "tx_+NQLAfiEuEBuJkQe4jgfO5o0zwzL4tcxwy1atjXrel0YPeVOsCRgcDZWYutaksdrntjMHC/OfMTzQ02eKckAarDr+DisgIEFuEB/44flnc4kKEKqguaKMTpm2o85goeimocard0gsTtEPPOgLKD1/4XEGhJmZ4HgqOPzbYLiyOOdlGzoqBZmUj8OuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBE6AeycInrhdwl5Y7NqfzL90nYB1H8F53NcrxgRiPTH5aU0HjRIM="
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
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
    "round": 275
  }
}
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
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 275
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 275,
      "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
    "round": 275
  }
}
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
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 275
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 275,
      "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
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
      "caller_nonce": 276,
      "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
  }
}
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEUoP6APRrWH46KpxtPo1VX6ukkJFFF5PA3rY6vrL8aKdHynpmjzA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEB8qNLLw0lbXOrWarOyE2Xyzcg0D6WPgJ/qURKJVbJ2sfo+IHIBzU9VW7WqegcMd4wjq3cJpp13zfOwwi10B2QBuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBFKD+gD0a1h+OiqcbT6NVV+rpJCRRReTwN62Or6y/GinR8vkDzVY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEB8qNLLw0lbXOrWarOyE2Xyzcg0D6WPgJ/qURKJVbJ2sfo+IHIBzU9VW7WqegcMd4wjq3cJpp13zfOwwi10B2QBuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBFKD+gD0a1h+OiqcbT6NVV+rpJCRRReTwN62Or6y/GinR8vkDzVY=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEB8qNLLw0lbXOrWarOyE2Xyzcg0D6WPgJ/qURKJVbJ2sfo+IHIBzU9VW7WqegcMd4wjq3cJpp13zfOwwi10B2QBuEDKMgfKWFBqg/5U6a6tXDiwtBuamA9gU1yqVSnACdRmeXQx8OEIEyDT8BIb5FU3A45pspgfqu1TvcDx1K/I2EIPuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBFKD+gD0a1h+OiqcbT6NVV+rpJCRRReTwN62Or6y/GinR8lcBjr0="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEB8qNLLw0lbXOrWarOyE2Xyzcg0D6WPgJ/qURKJVbJ2sfo+IHIBzU9VW7WqegcMd4wjq3cJpp13zfOwwi10B2QBuEDKMgfKWFBqg/5U6a6tXDiwtBuamA9gU1yqVSnACdRmeXQx8OEIEyDT8BIb5FU3A45pspgfqu1TvcDx1K/I2EIPuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBFKD+gD0a1h+OiqcbT6NVV+rpJCRRReTwN62Or6y/GinR8lcBjr0="
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
      "state": "tx_+NQLAfiEuEB8qNLLw0lbXOrWarOyE2Xyzcg0D6WPgJ/qURKJVbJ2sfo+IHIBzU9VW7WqegcMd4wjq3cJpp13zfOwwi10B2QBuEDKMgfKWFBqg/5U6a6tXDiwtBuamA9gU1yqVSnACdRmeXQx8OEIEyDT8BIb5FU3A45pspgfqu1TvcDx1K/I2EIPuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBFKD+gD0a1h+OiqcbT6NVV+rpJCRRReTwN62Or6y/GinR8lcBjr0="
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
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
    "round": 276
  }
}
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
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 276
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 276,
      "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
    "round": 276
  }
}
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
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 276
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 276,
      "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
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
      "caller_nonce": 277,
      "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
  }
}
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEVoFFkjghILH4SkB7AJtghCVuqoJH/LCLpQnr+Nvn48wRVA/uD2Q==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuED8qnvFjwoz9KehYn4WWTSyRPlqy+Ri6NvQr/ItNypushsGLlnK4OrB+dQmB4yOq7b+1g29vxvmeIyFN9QTvy8EuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBFaBRZI4ISCx+EpAewCbYIQlbqqCR/ywi6UJ6/jb5+PMEVcqsxTY="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuED8qnvFjwoz9KehYn4WWTSyRPlqy+Ri6NvQr/ItNypushsGLlnK4OrB+dQmB4yOq7b+1g29vxvmeIyFN9QTvy8EuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBFaBRZI4ISCx+EpAewCbYIQlbqqCR/ywi6UJ6/jb5+PMEVcqsxTY=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1EzcHREekpIWVA3eEFmQi5jaGFpbjlhY2NvdW50X3B1YmtleScSoXM=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEAbkSHzlBL46idfmj368camGMdzjL7IYMlstZqOVn/U4HqzHlPl7J75Sk9TIbehWIzjSpGP7vkuIwZZpbOnmjMAuED8qnvFjwoz9KehYn4WWTSyRPlqy+Ri6NvQr/ItNypushsGLlnK4OrB+dQmB4yOq7b+1g29vxvmeIyFN9QTvy8EuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBFaBRZI4ISCx+EpAewCbYIQlbqqCR/ywi6UJ6/jb5+PMEVXswJ4s="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEAbkSHzlBL46idfmj368camGMdzjL7IYMlstZqOVn/U4HqzHlPl7J75Sk9TIbehWIzjSpGP7vkuIwZZpbOnmjMAuED8qnvFjwoz9KehYn4WWTSyRPlqy+Ri6NvQr/ItNypushsGLlnK4OrB+dQmB4yOq7b+1g29vxvmeIyFN9QTvy8EuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBFaBRZI4ISCx+EpAewCbYIQlbqqCR/ywi6UJ6/jb5+PMEVXswJ4s="
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
      "state": "tx_+NQLAfiEuEAbkSHzlBL46idfmj368camGMdzjL7IYMlstZqOVn/U4HqzHlPl7J75Sk9TIbehWIzjSpGP7vkuIwZZpbOnmjMAuED8qnvFjwoz9KehYn4WWTSyRPlqy+Ri6NvQr/ItNypushsGLlnK4OrB+dQmB4yOq7b+1g29vxvmeIyFN9QTvy8EuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBFaBRZI4ISCx+EpAewCbYIQlbqqCR/ywi6UJ6/jb5+PMEVXswJ4s="
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
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
    "round": 277
  }
}
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
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 277
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 277,
      "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
    "round": 277
  }
}
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
        "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 277
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 277,
      "contract_id": "ct_2mg2dmaqrkikzHqBSYAeD3w7wM2gBh1gBaWm6y5Fs7yMdnHxD7",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "ABCDEFG",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
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
      "caller_nonce": 278,
      "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "ABCDEFG",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "ABCDEFG",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
  }
}
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "ABCDEFG",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEWoOx52ERzMVwdDo3yDv6WyBUR4vY73N+kR1uKQiBybwpTL1NmCQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEDnrl+hikWTRrnXwWWag6lBcE5ByxV7NvojJT92rbsIsF5DG7QFiQWpXcRswurKVOuwBNe5BsGyv9Od208CdHEJuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBFqDsedhEczFcHQ6N8g7+lsgVEeL2O9zfpEdbikIgcm8KU88wREc="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEDnrl+hikWTRrnXwWWag6lBcE5ByxV7NvojJT92rbsIsF5DG7QFiQWpXcRswurKVOuwBNe5BsGyv9Od208CdHEJuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBFqDsedhEczFcHQ6N8g7+lsgVEeL2O9zfpEdbikIgcm8KU88wREc=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEAHKHMEBgpx8OXJH1hGqRJGrC77z7tqm75g0W87J6CYiM3XkokWm67cQVUi/8jj+AdkvAcrZQj25zwQtMrJHUUDuEDnrl+hikWTRrnXwWWag6lBcE5ByxV7NvojJT92rbsIsF5DG7QFiQWpXcRswurKVOuwBNe5BsGyv9Od208CdHEJuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBFqDsedhEczFcHQ6N8g7+lsgVEeL2O9zfpEdbikIgcm8KU0DMsfI="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEAHKHMEBgpx8OXJH1hGqRJGrC77z7tqm75g0W87J6CYiM3XkokWm67cQVUi/8jj+AdkvAcrZQj25zwQtMrJHUUDuEDnrl+hikWTRrnXwWWag6lBcE5ByxV7NvojJT92rbsIsF5DG7QFiQWpXcRswurKVOuwBNe5BsGyv9Od208CdHEJuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBFqDsedhEczFcHQ6N8g7+lsgVEeL2O9zfpEdbikIgcm8KU0DMsfI="
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
      "state": "tx_+NQLAfiEuEAHKHMEBgpx8OXJH1hGqRJGrC77z7tqm75g0W87J6CYiM3XkokWm67cQVUi/8jj+AdkvAcrZQj25zwQtMrJHUUDuEDnrl+hikWTRrnXwWWag6lBcE5ByxV7NvojJT92rbsIsF5DG7QFiQWpXcRswurKVOuwBNe5BsGyv9Od208CdHEJuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBFqDsedhEczFcHQ6N8g7+lsgVEeL2O9zfpEdbikIgcm8KU0DMsfI="
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
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
    "round": 278
  }
}
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
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 278
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 278,
      "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
    "round": 278
  }
}
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
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 278
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 278,
      "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "ABCDEFG",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
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
      "caller_nonce": 279,
      "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "ABCDEFG",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "ABCDEFG",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
  }
}
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "ABCDEFG",
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEXoP57JaJsVXvbRdRPFqFh5DjjNK3jIhSoACaP6rUH+SnTEbaPiw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEDDuFIy9Cx1Q4rnWciHeJThT+YxtbrUFrf4QteugKsE0qn4I0s2aJBp7/vzeYzK9A9C1TCtSggHKg4znJK8upsJuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBF6D+eyWibFV720XUTxahYeQ44zSt4yIUqAAmj+q1B/kp0+glCLg="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEDDuFIy9Cx1Q4rnWciHeJThT+YxtbrUFrf4QteugKsE0qn4I0s2aJBp7/vzeYzK9A9C1TCtSggHKg4znJK8upsJuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBF6D+eyWibFV720XUTxahYeQ44zSt4yIUqAAmj+q1B/kp0+glCLg=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoOkhogd5WFT1ykKiGj8OldiSFUCfeABWjXSvI8Es6dKqUTNwdER6SkhZUDd4QWZCLmNoYWluOWFjY291bnRfcHVia2V5vsIeDg==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuECTv4KLwLVrJYjvN7m9OlJF1BO3D4d50LYAbShMlqg95Uuig/Ohi7bpCPRQKGOsgNUIx3ArjeoRBkPwymd3qfwHuEDDuFIy9Cx1Q4rnWciHeJThT+YxtbrUFrf4QteugKsE0qn4I0s2aJBp7/vzeYzK9A9C1TCtSggHKg4znJK8upsJuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBF6D+eyWibFV720XUTxahYeQ44zSt4yIUqAAmj+q1B/kp0woIPbU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuECTv4KLwLVrJYjvN7m9OlJF1BO3D4d50LYAbShMlqg95Uuig/Ohi7bpCPRQKGOsgNUIx3ArjeoRBkPwymd3qfwHuEDDuFIy9Cx1Q4rnWciHeJThT+YxtbrUFrf4QteugKsE0qn4I0s2aJBp7/vzeYzK9A9C1TCtSggHKg4znJK8upsJuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBF6D+eyWibFV720XUTxahYeQ44zSt4yIUqAAmj+q1B/kp0woIPbU="
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
      "state": "tx_+NQLAfiEuECTv4KLwLVrJYjvN7m9OlJF1BO3D4d50LYAbShMlqg95Uuig/Ohi7bpCPRQKGOsgNUIx3ArjeoRBkPwymd3qfwHuEDDuFIy9Cx1Q4rnWciHeJThT+YxtbrUFrf4QteugKsE0qn4I0s2aJBp7/vzeYzK9A9C1TCtSggHKg4znJK8upsJuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBF6D+eyWibFV720XUTxahYeQ44zSt4yIUqAAmj+q1B/kp0woIPbU="
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
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
    "round": 279
  }
}
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
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 279
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 279,
      "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
    "round": 279
  }
}
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
        "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 279
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 279,
      "contract_id": "ct_27eRpQPeCsBmxsgcdPDv3Umt3pDoFJeS3X5GwgqSdXZgyoMtR3",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEYoG8NVuu/3UGyROiLpZEOlIdqiTZfQNxQTL/3UgrVrjxiQp4nSw==",
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
  "id": -576460752303421307,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEBqgyvBXrRETSm9xBNTqVwwcxnP4NYIoKT3zIOhxddPfCXPtyRoNuwp/+DlGMdJ/To/RNiNk2XDJXd13gXb2moGuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBGKBvDVbrv91BskToi6WRDpSHaok2X0DcUEy/91IK1a48Ys4Q+3w="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEBqgyvBXrRETSm9xBNTqVwwcxnP4NYIoKT3zIOhxddPfCXPtyRoNuwp/+DlGMdJ/To/RNiNk2XDJXd13gXb2moGuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBGKBvDVbrv91BskToi6WRDpSHaok2X0DcUEy/91IK1a48Ys4Q+3w=",
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
  "id": -576460752303421306,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEBqgyvBXrRETSm9xBNTqVwwcxnP4NYIoKT3zIOhxddPfCXPtyRoNuwp/+DlGMdJ/To/RNiNk2XDJXd13gXb2moGuEDtlYPbaWOw1gNLkJQgED3NxTUj3JREqaQkXnQCEXqHld3DYI4QVrpSYQy6zcH3yjulUzsQ+Os4GS0UE2vy42IHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBGKBvDVbrv91BskToi6WRDpSHaok2X0DcUEy/91IK1a48YvvfCj8="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEBqgyvBXrRETSm9xBNTqVwwcxnP4NYIoKT3zIOhxddPfCXPtyRoNuwp/+DlGMdJ/To/RNiNk2XDJXd13gXb2moGuEDtlYPbaWOw1gNLkJQgED3NxTUj3JREqaQkXnQCEXqHld3DYI4QVrpSYQy6zcH3yjulUzsQ+Os4GS0UE2vy42IHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBGKBvDVbrv91BskToi6WRDpSHaok2X0DcUEy/91IK1a48YvvfCj8="
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
      "state": "tx_+NQLAfiEuEBqgyvBXrRETSm9xBNTqVwwcxnP4NYIoKT3zIOhxddPfCXPtyRoNuwp/+DlGMdJ/To/RNiNk2XDJXd13gXb2moGuEDtlYPbaWOw1gNLkJQgED3NxTUj3JREqaQkXnQCEXqHld3DYI4QVrpSYQy6zcH3yjulUzsQ+Os4GS0UE2vy42IHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBGKBvDVbrv91BskToi6WRDpSHaok2X0DcUEy/91IK1a48YvvfCj8="
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEZoDwwVARq6zhKXsdJUVqWETUbiWHPF1mWMiP5CJ73ZLvduq7GvQ==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
  "id": -576460752303421305,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEAycEg+Lf01GX0uj4pvHDUvR4S2X6B8xth1+rzjMWW1Ej+49aJdEIB2fQiug5bQNw+KB7gRtDej+zam9eMGo8ICuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBGaA8MFQEaus4Sl7HSVFalhE1G4lhzxdZljIj+Qie92S73fdVBNU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEAycEg+Lf01GX0uj4pvHDUvR4S2X6B8xth1+rzjMWW1Ej+49aJdEIB2fQiug5bQNw+KB7gRtDej+zam9eMGo8ICuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBGaA8MFQEaus4Sl7HSVFalhE1G4lhzxdZljIj+Qie92S73fdVBNU=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
  "id": -576460752303421304,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEAycEg+Lf01GX0uj4pvHDUvR4S2X6B8xth1+rzjMWW1Ej+49aJdEIB2fQiug5bQNw+KB7gRtDej+zam9eMGo8ICuEC4yUuxithZgiMMcEku3q5nlNRMI2nlLHZhbqNxd7eSeF1arRhqrVTeewkxO+miW1g0mG/606cKgy88PvVFfTALuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBGaA8MFQEaus4Sl7HSVFalhE1G4lhzxdZljIj+Qie92S73ZpKiVI="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEAycEg+Lf01GX0uj4pvHDUvR4S2X6B8xth1+rzjMWW1Ej+49aJdEIB2fQiug5bQNw+KB7gRtDej+zam9eMGo8ICuEC4yUuxithZgiMMcEku3q5nlNRMI2nlLHZhbqNxd7eSeF1arRhqrVTeewkxO+miW1g0mG/606cKgy88PvVFfTALuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBGaA8MFQEaus4Sl7HSVFalhE1G4lhzxdZljIj+Qie92S73ZpKiVI="
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
      "state": "tx_+NQLAfiEuEAycEg+Lf01GX0uj4pvHDUvR4S2X6B8xth1+rzjMWW1Ej+49aJdEIB2fQiug5bQNw+KB7gRtDej+zam9eMGo8ICuEC4yUuxithZgiMMcEku3q5nlNRMI2nlLHZhbqNxd7eSeF1arRhqrVTeewkxO+miW1g0mG/606cKgy88PvVFfTALuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBGaA8MFQEaus4Sl7HSVFalhE1G4lhzxdZljIj+Qie92S73ZpKiVI="
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
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
      "caller_nonce": 282,
      "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
  }
}
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEaoK+1DwcR7TMy2gG+Uh73aW9j+LDFl8z4f3fejlbqPf0MD38wjw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEAhGXH8CJtqwBHhaxRQQRZTPeWDCbkW7MVqF2GQVhz/JAwl45tC+vgxh6sPsWeBkYfel6k8UPgu9FwyQSxS+zcNuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBGqCvtQ8HEe0zMtoBvlIe92lvY/iwxZfM+H933o5W6j39DNcQqII="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEAhGXH8CJtqwBHhaxRQQRZTPeWDCbkW7MVqF2GQVhz/JAwl45tC+vgxh6sPsWeBkYfel6k8UPgu9FwyQSxS+zcNuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBGqCvtQ8HEe0zMtoBvlIe92lvY/iwxZfM+H933o5W6j39DNcQqII=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEAhGXH8CJtqwBHhaxRQQRZTPeWDCbkW7MVqF2GQVhz/JAwl45tC+vgxh6sPsWeBkYfel6k8UPgu9FwyQSxS+zcNuEDqBElc+HVBRYiCw5fVr3djWQm5IndmT1CKbvmda5kGKl1mp+gR3n9bcoCYo4JFz9ay/YR8hnZmqHgdB8IpCCUNuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBGqCvtQ8HEe0zMtoBvlIe92lvY/iwxZfM+H933o5W6j39DG3mYYY="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEAhGXH8CJtqwBHhaxRQQRZTPeWDCbkW7MVqF2GQVhz/JAwl45tC+vgxh6sPsWeBkYfel6k8UPgu9FwyQSxS+zcNuEDqBElc+HVBRYiCw5fVr3djWQm5IndmT1CKbvmda5kGKl1mp+gR3n9bcoCYo4JFz9ay/YR8hnZmqHgdB8IpCCUNuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBGqCvtQ8HEe0zMtoBvlIe92lvY/iwxZfM+H933o5W6j39DG3mYYY="
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
      "state": "tx_+NQLAfiEuEAhGXH8CJtqwBHhaxRQQRZTPeWDCbkW7MVqF2GQVhz/JAwl45tC+vgxh6sPsWeBkYfel6k8UPgu9FwyQSxS+zcNuEDqBElc+HVBRYiCw5fVr3djWQm5IndmT1CKbvmda5kGKl1mp+gR3n9bcoCYo4JFz9ay/YR8hnZmqHgdB8IpCCUNuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBGqCvtQ8HEe0zMtoBvlIe92lvY/iwxZfM+H933o5W6j39DG3mYYY="
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
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
    "round": 282
  }
}
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
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 282
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 282,
      "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
    "round": 282
  }
}
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
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 282
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 282,
      "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
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
      "caller_nonce": 283,
      "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
  }
}
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEboCR0Nuikeo3uDLYVFpUzePpV30LEfn/+ClbN6NqaKFwKhxczWQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEABlG9QEWtNljdPvLHUB12JbcyezCNFgHGL3szqOh1bZ4ggWDErMV9yYoTbCV0iylMFK5fD2s6yYkz+v4Njwu8KuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBG6AkdDbopHqN7gy2FRaVM3j6Vd9CxH5//gpWzejamihcChLUaeQ="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEABlG9QEWtNljdPvLHUB12JbcyezCNFgHGL3szqOh1bZ4ggWDErMV9yYoTbCV0iylMFK5fD2s6yYkz+v4Njwu8KuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBG6AkdDbopHqN7gy2FRaVM3j6Vd9CxH5//gpWzejamihcChLUaeQ=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEABlG9QEWtNljdPvLHUB12JbcyezCNFgHGL3szqOh1bZ4ggWDErMV9yYoTbCV0iylMFK5fD2s6yYkz+v4Njwu8KuECb+iRlJXQ/O72OCex/JCxWorgVE4AiWVL1e1e93UurJsj/S5tDoVwUWldKVTjboLiRr4czhGYFezTT55kCOaYCuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBG6AkdDbopHqN7gy2FRaVM3j6Vd9CxH5//gpWzejamihcCgrjoiA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEABlG9QEWtNljdPvLHUB12JbcyezCNFgHGL3szqOh1bZ4ggWDErMV9yYoTbCV0iylMFK5fD2s6yYkz+v4Njwu8KuECb+iRlJXQ/O72OCex/JCxWorgVE4AiWVL1e1e93UurJsj/S5tDoVwUWldKVTjboLiRr4czhGYFezTT55kCOaYCuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBG6AkdDbopHqN7gy2FRaVM3j6Vd9CxH5//gpWzejamihcCgrjoiA="
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
      "state": "tx_+NQLAfiEuEABlG9QEWtNljdPvLHUB12JbcyezCNFgHGL3szqOh1bZ4ggWDErMV9yYoTbCV0iylMFK5fD2s6yYkz+v4Njwu8KuECb+iRlJXQ/O72OCex/JCxWorgVE4AiWVL1e1e93UurJsj/S5tDoVwUWldKVTjboLiRr4czhGYFezTT55kCOaYCuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBG6AkdDbopHqN7gy2FRaVM3j6Vd9CxH5//gpWzejamihcCgrjoiA="
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
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
    "round": 283
  }
}
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
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 283
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 283,
      "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
    "round": 283
  }
}
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
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 283
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 283,
      "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
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
      "caller_nonce": 284,
      "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
  }
}
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEcoNsd2tcwU8YrYDFDNAf75SGtyKxom95hlVn0RonXJeGiX0Z2IQ==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEBdRO0Yxkvtk1qMhNTjvJ5zUL0TSFQf3JHTCf/xuX79tbx1NuUSQ7gsBwDRlEm0YU/9+f5H70sp+lDwbockKoQLuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBHKDbHdrXMFPGK2AxQzQH++UhrcisaJveYZVZ9EaJ1yXhovsYfKo="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEBdRO0Yxkvtk1qMhNTjvJ5zUL0TSFQf3JHTCf/xuX79tbx1NuUSQ7gsBwDRlEm0YU/9+f5H70sp+lDwbockKoQLuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBHKDbHdrXMFPGK2AxQzQH++UhrcisaJveYZVZ9EaJ1yXhovsYfKo=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEBdRO0Yxkvtk1qMhNTjvJ5zUL0TSFQf3JHTCf/xuX79tbx1NuUSQ7gsBwDRlEm0YU/9+f5H70sp+lDwbockKoQLuEDvNoj0UxAa3pBFDjbJfCwYLV0Sktqrl2x+lahdOBmLcySNvyOutMEan6ZHSacvk1fsUGGpG614vWLLWj0c5ScJuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBHKDbHdrXMFPGK2AxQzQH++UhrcisaJveYZVZ9EaJ1yXhokKd194="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEBdRO0Yxkvtk1qMhNTjvJ5zUL0TSFQf3JHTCf/xuX79tbx1NuUSQ7gsBwDRlEm0YU/9+f5H70sp+lDwbockKoQLuEDvNoj0UxAa3pBFDjbJfCwYLV0Sktqrl2x+lahdOBmLcySNvyOutMEan6ZHSacvk1fsUGGpG614vWLLWj0c5ScJuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBHKDbHdrXMFPGK2AxQzQH++UhrcisaJveYZVZ9EaJ1yXhokKd194="
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
      "state": "tx_+NQLAfiEuEBdRO0Yxkvtk1qMhNTjvJ5zUL0TSFQf3JHTCf/xuX79tbx1NuUSQ7gsBwDRlEm0YU/9+f5H70sp+lDwbockKoQLuEDvNoj0UxAa3pBFDjbJfCwYLV0Sktqrl2x+lahdOBmLcySNvyOutMEan6ZHSacvk1fsUGGpG614vWLLWj0c5ScJuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBHKDbHdrXMFPGK2AxQzQH++UhrcisaJveYZVZ9EaJ1yXhokKd194="
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
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
    "round": 284
  }
}
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
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 284
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 284,
      "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
    "round": 284
  }
}
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
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 284
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 284,
      "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
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
      "caller_nonce": 285,
      "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
  }
}
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
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
        "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
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
    "block_hash": "kh_2nTKJn2Cvg8EV7WEUPCActLaF9xAiY3bWoS98bji2SewT1chGb",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEdoAqSlnBG+GBvi1hbiv4enG9PBzB/MYUwxAe3UloimASjVfPQCg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuED7CVVCvXeRicWMj17poXg7cr0WMWLX9MPNn3u/t/24Tx3b11zNR6JAXfZ7sF2TgWLTX2UczT5HFRWWnAKITtAKuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBHaAKkpZwRvhgb4tYW4r+HpxvTwcwfzGFMMQHt1JaIpgEoxBhMG4="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuED7CVVCvXeRicWMj17poXg7cr0WMWLX9MPNn3u/t/24Tx3b11zNR6JAXfZ7sF2TgWLTX2UczT5HFRWWnAKITtAKuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBHaAKkpZwRvhgb4tYW4r+HpxvTwcwfzGFMMQHt1JaIpgEoxBhMG4=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuECuMNy+SNUX8WPojcEK9ZrSSwNzNEP0VJaiZJNe2uSThBHyjhpTMdknsF9jJydggVAcOv90rYkC8bS3qG2i4TkJuED7CVVCvXeRicWMj17poXg7cr0WMWLX9MPNn3u/t/24Tx3b11zNR6JAXfZ7sF2TgWLTX2UczT5HFRWWnAKITtAKuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBHaAKkpZwRvhgb4tYW4r+HpxvTwcwfzGFMMQHt1JaIpgEo69qMzE="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuECuMNy+SNUX8WPojcEK9ZrSSwNzNEP0VJaiZJNe2uSThBHyjhpTMdknsF9jJydggVAcOv90rYkC8bS3qG2i4TkJuED7CVVCvXeRicWMj17poXg7cr0WMWLX9MPNn3u/t/24Tx3b11zNR6JAXfZ7sF2TgWLTX2UczT5HFRWWnAKITtAKuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBHaAKkpZwRvhgb4tYW4r+HpxvTwcwfzGFMMQHt1JaIpgEo69qMzE="
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
      "state": "tx_+NQLAfiEuECuMNy+SNUX8WPojcEK9ZrSSwNzNEP0VJaiZJNe2uSThBHyjhpTMdknsF9jJydggVAcOv90rYkC8bS3qG2i4TkJuED7CVVCvXeRicWMj17poXg7cr0WMWLX9MPNn3u/t/24Tx3b11zNR6JAXfZ7sF2TgWLTX2UczT5HFRWWnAKITtAKuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBHaAKkpZwRvhgb4tYW4r+HpxvTwcwfzGFMMQHt1JaIpgEo69qMzE="
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
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
    "round": 285
  }
}
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
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 285
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 285,
      "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
    "round": 285
  }
}
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
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 285
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 285,
      "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
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
      "caller_nonce": 286,
      "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
  }
}
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEeoITEZyX7B54bX4yuz9kBeEYREeTS9wiydEn1qMykWBrPXm216A==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEDhMPa9lGHf5qHIqqw4yHocpynRdNGmjbUcDelvn1QK0EvekQ13Gwu3hWY4pYvP/0YBULKWh8j4SGAvHRPBfbwNuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBHqCExGcl+weeG1+Mrs/ZAXhGERHk0vcIsnRJ9ajMpFgaz6oQbjg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEDhMPa9lGHf5qHIqqw4yHocpynRdNGmjbUcDelvn1QK0EvekQ13Gwu3hWY4pYvP/0YBULKWh8j4SGAvHRPBfbwNuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBHqCExGcl+weeG1+Mrs/ZAXhGERHk0vcIsnRJ9ajMpFgaz6oQbjg=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEB+lqsJXpfrsYWzJsFEGs4DFRcieHOQXPSWdMmfUesJKaGZ4EpE6ALVQf75YIydulJqAKz4FISuFaru2CnWCf8IuEDhMPa9lGHf5qHIqqw4yHocpynRdNGmjbUcDelvn1QK0EvekQ13Gwu3hWY4pYvP/0YBULKWh8j4SGAvHRPBfbwNuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBHqCExGcl+weeG1+Mrs/ZAXhGERHk0vcIsnRJ9ajMpFgaz03oIYE="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEB+lqsJXpfrsYWzJsFEGs4DFRcieHOQXPSWdMmfUesJKaGZ4EpE6ALVQf75YIydulJqAKz4FISuFaru2CnWCf8IuEDhMPa9lGHf5qHIqqw4yHocpynRdNGmjbUcDelvn1QK0EvekQ13Gwu3hWY4pYvP/0YBULKWh8j4SGAvHRPBfbwNuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBHqCExGcl+weeG1+Mrs/ZAXhGERHk0vcIsnRJ9ajMpFgaz03oIYE="
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
      "state": "tx_+NQLAfiEuEB+lqsJXpfrsYWzJsFEGs4DFRcieHOQXPSWdMmfUesJKaGZ4EpE6ALVQf75YIydulJqAKz4FISuFaru2CnWCf8IuEDhMPa9lGHf5qHIqqw4yHocpynRdNGmjbUcDelvn1QK0EvekQ13Gwu3hWY4pYvP/0YBULKWh8j4SGAvHRPBfbwNuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBHqCExGcl+weeG1+Mrs/ZAXhGERHk0vcIsnRJ9ajMpFgaz03oIYE="
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
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
    "round": 286
  }
}
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
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 286
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 286,
      "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
    "round": 286
  }
}
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
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 286
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 286,
      "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
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
      "caller_nonce": 287,
      "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
  }
}
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEfoOyooRiKmSC9yUJYzoRWQCmivtr5cn+xix5t5IDK1SxbDCIbig==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEBUYVzoB3MOIa/5VVgpH8KQNNvIwYc/6erIg8Hwsqcy06Ckfp9iSkf2IZe7U6i2as3h39zCeVuCce63Ga2w3OoNuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBH6DsqKEYipkgvclCWM6EVkApor7a+XJ/sYsebeSAytUsW2whXAw="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEBUYVzoB3MOIa/5VVgpH8KQNNvIwYc/6erIg8Hwsqcy06Ckfp9iSkf2IZe7U6i2as3h39zCeVuCce63Ga2w3OoNuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBH6DsqKEYipkgvclCWM6EVkApor7a+XJ/sYsebeSAytUsW2whXAw=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E1WUpXZ0VHNVVKTGJtVy5jaGFpbjlhY2NvdW50X3B1YmtleVTxSQA=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEBUYVzoB3MOIa/5VVgpH8KQNNvIwYc/6erIg8Hwsqcy06Ckfp9iSkf2IZe7U6i2as3h39zCeVuCce63Ga2w3OoNuEDYo8clURhxuwMbp+C74qy05QZ34CAYPIOrVFn3l8UPliSlanV39ZZemLkZ9qnvGRWwEm2C4uRPbHVvODYa6DILuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBH6DsqKEYipkgvclCWM6EVkApor7a+XJ/sYsebeSAytUsW4onEhI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEBUYVzoB3MOIa/5VVgpH8KQNNvIwYc/6erIg8Hwsqcy06Ckfp9iSkf2IZe7U6i2as3h39zCeVuCce63Ga2w3OoNuEDYo8clURhxuwMbp+C74qy05QZ34CAYPIOrVFn3l8UPliSlanV39ZZemLkZ9qnvGRWwEm2C4uRPbHVvODYa6DILuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBH6DsqKEYipkgvclCWM6EVkApor7a+XJ/sYsebeSAytUsW4onEhI="
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
      "state": "tx_+NQLAfiEuEBUYVzoB3MOIa/5VVgpH8KQNNvIwYc/6erIg8Hwsqcy06Ckfp9iSkf2IZe7U6i2as3h39zCeVuCce63Ga2w3OoNuEDYo8clURhxuwMbp+C74qy05QZ34CAYPIOrVFn3l8UPliSlanV39ZZemLkZ9qnvGRWwEm2C4uRPbHVvODYa6DILuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBH6DsqKEYipkgvclCWM6EVkApor7a+XJ/sYsebeSAytUsW4onEhI="
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
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
    "round": 287
  }
}
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
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 287
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 287,
      "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
    "round": 287
  }
}
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
        "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 287
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 287,
      "contract_id": "ct_2oBUcg6wvk1TcSfNyHYmkDGMNDn4huKhVVaAWTpTEGtB6AkT4y",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
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
      "caller_nonce": 288,
      "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
  }
}
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEgoDhPyD3PerCfJ3uPZTv1gkSgEru6jcLX9A+K/N7tbs5pDylBNw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEAz1Tz2Co7XYGDNQMoW1lm0dGEedgs/N6knwjCE2mz0BXWmAL09D2Mcn00F3XHoKC2OeqnBpWxuQNb7V4KyQVQMuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBIKA4T8g9z3qwnyd7j2U79YJEoBK7uo3C1/QPivze7W7OaaphUSc="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEAz1Tz2Co7XYGDNQMoW1lm0dGEedgs/N6knwjCE2mz0BXWmAL09D2Mcn00F3XHoKC2OeqnBpWxuQNb7V4KyQVQMuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBIKA4T8g9z3qwnyd7j2U79YJEoBK7uo3C1/QPivze7W7OaaphUSc=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEAz1Tz2Co7XYGDNQMoW1lm0dGEedgs/N6knwjCE2mz0BXWmAL09D2Mcn00F3XHoKC2OeqnBpWxuQNb7V4KyQVQMuEDRFJSehVHgv78zJDdJ7yJkCMiXD4cw2uWfwq8yPoR1Etb8Iz1AUqu+7Asu1n1psK6+yJ9rba1ul8xcXux/b4EKuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBIKA4T8g9z3qwnyd7j2U79YJEoBK7uo3C1/QPivze7W7OaflyXGk="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEAz1Tz2Co7XYGDNQMoW1lm0dGEedgs/N6knwjCE2mz0BXWmAL09D2Mcn00F3XHoKC2OeqnBpWxuQNb7V4KyQVQMuEDRFJSehVHgv78zJDdJ7yJkCMiXD4cw2uWfwq8yPoR1Etb8Iz1AUqu+7Asu1n1psK6+yJ9rba1ul8xcXux/b4EKuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBIKA4T8g9z3qwnyd7j2U79YJEoBK7uo3C1/QPivze7W7OaflyXGk="
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
      "state": "tx_+NQLAfiEuEAz1Tz2Co7XYGDNQMoW1lm0dGEedgs/N6knwjCE2mz0BXWmAL09D2Mcn00F3XHoKC2OeqnBpWxuQNb7V4KyQVQMuEDRFJSehVHgv78zJDdJ7yJkCMiXD4cw2uWfwq8yPoR1Etb8Iz1AUqu+7Asu1n1psK6+yJ9rba1ul8xcXux/b4EKuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBIKA4T8g9z3qwnyd7j2U79YJEoBK7uo3C1/QPivze7W7OaflyXGk="
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
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
    "round": 288
  }
}
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
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 288
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 288,
      "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
    "round": 288
  }
}
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
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 288
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 288,
      "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
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
      "caller_nonce": 289,
      "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "ABCDEFG",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
  }
}
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "ABCDEFG",
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEhoFKom/sB0fhUiERZQND25jC0rk01eUR4L5ZVCnLzPcbEfi455w==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuED6UlBUn1vNDKxlyx2oGfpXqm63S7ZbsFwynEHMRoids5SqfNdaoj5qRp9lHbLhHg/2QJnKghb4vP6AWfmVhP8FuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBIaBSqJv7AdH4VIhEWUDQ9uYwtK5NNXlEeC+WVQpy8z3GxAaPKGQ="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuED6UlBUn1vNDKxlyx2oGfpXqm63S7ZbsFwynEHMRoids5SqfNdaoj5qRp9lHbLhHg/2QJnKghb4vP6AWfmVhP8FuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBIaBSqJv7AdH4VIhEWUDQ9uYwtK5NNXlEeC+WVQpy8z3GxAaPKGQ=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoOyOCpHaAL+HxUJwUVkHvpraDWXWTOnpp31zZHeVkX0XUTVZSldnRUc1VUpMYm1XLmNoYWluOWFjY291bnRfcHVia2V5Wc+tdQ==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEBe8BxlxDJllaksI8TxlgQ8Qr77DETAE1CabuxV92zEKF5NKxpKirnSBhtHR2Imz06o6GDYTwr3OWkatSmMZAYAuED6UlBUn1vNDKxlyx2oGfpXqm63S7ZbsFwynEHMRoids5SqfNdaoj5qRp9lHbLhHg/2QJnKghb4vP6AWfmVhP8FuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBIaBSqJv7AdH4VIhEWUDQ9uYwtK5NNXlEeC+WVQpy8z3GxH0lazc="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEBe8BxlxDJllaksI8TxlgQ8Qr77DETAE1CabuxV92zEKF5NKxpKirnSBhtHR2Imz06o6GDYTwr3OWkatSmMZAYAuED6UlBUn1vNDKxlyx2oGfpXqm63S7ZbsFwynEHMRoids5SqfNdaoj5qRp9lHbLhHg/2QJnKghb4vP6AWfmVhP8FuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBIaBSqJv7AdH4VIhEWUDQ9uYwtK5NNXlEeC+WVQpy8z3GxH0lazc="
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
      "state": "tx_+NQLAfiEuEBe8BxlxDJllaksI8TxlgQ8Qr77DETAE1CabuxV92zEKF5NKxpKirnSBhtHR2Imz06o6GDYTwr3OWkatSmMZAYAuED6UlBUn1vNDKxlyx2oGfpXqm63S7ZbsFwynEHMRoids5SqfNdaoj5qRp9lHbLhHg/2QJnKghb4vP6AWfmVhP8FuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBIaBSqJv7AdH4VIhEWUDQ9uYwtK5NNXlEeC+WVQpy8z3GxH0lazc="
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
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
    "round": 289
  }
}
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
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 289
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 289,
      "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
    "round": 289
  }
}
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
        "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 289
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 289,
      "contract_id": "ct_2RNw6B2nFnDTzATfRRxv5LGXv2xfaGMXMD9Z5iCTVin3gqTnj2",
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEioK2DaysOJGZBvehE76cjeMB4hZESROgEIwJn1KpehU+DGrWdAQ==",
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
  "id": -576460752303421287,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEDJeRsOIeNJiE4y/5GsIe+YnzkjlY3BEdnCEwflfGfsZBNsjeWCmU4z+AmPmTTI0w5fQqqNeZHwRKB89DzjlY4PuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBIqCtg2srDiRmQb3oRO+nI3jAeIWREkToBCMCZ9SqXoVPgwdQLM8="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEDJeRsOIeNJiE4y/5GsIe+YnzkjlY3BEdnCEwflfGfsZBNsjeWCmU4z+AmPmTTI0w5fQqqNeZHwRKB89DzjlY4PuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBIqCtg2srDiRmQb3oRO+nI3jAeIWREkToBCMCZ9SqXoVPgwdQLM8=",
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
  "id": -576460752303421286,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEBix7dWX299kcFuVZOMYDDFO4Bwc02t5MIqz7Oo5oXmJ7wGWL6ShFC2r0eJ7APNWT+EQ0umCW6UQQ0xMsE/Ew4NuEDJeRsOIeNJiE4y/5GsIe+YnzkjlY3BEdnCEwflfGfsZBNsjeWCmU4z+AmPmTTI0w5fQqqNeZHwRKB89DzjlY4PuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBIqCtg2srDiRmQb3oRO+nI3jAeIWREkToBCMCZ9SqXoVPg14HP/s="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEBix7dWX299kcFuVZOMYDDFO4Bwc02t5MIqz7Oo5oXmJ7wGWL6ShFC2r0eJ7APNWT+EQ0umCW6UQQ0xMsE/Ew4NuEDJeRsOIeNJiE4y/5GsIe+YnzkjlY3BEdnCEwflfGfsZBNsjeWCmU4z+AmPmTTI0w5fQqqNeZHwRKB89DzjlY4PuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBIqCtg2srDiRmQb3oRO+nI3jAeIWREkToBCMCZ9SqXoVPg14HP/s="
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
      "state": "tx_+NQLAfiEuEBix7dWX299kcFuVZOMYDDFO4Bwc02t5MIqz7Oo5oXmJ7wGWL6ShFC2r0eJ7APNWT+EQ0umCW6UQQ0xMsE/Ew4NuEDJeRsOIeNJiE4y/5GsIe+YnzkjlY3BEdnCEwflfGfsZBNsjeWCmU4z+AmPmTTI0w5fQqqNeZHwRKB89DzjlY4PuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBIqCtg2srDiRmQb3oRO+nI3jAeIWREkToBCMCZ9SqXoVPg14HP/s="
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEjoJ70PwPGIZYB0QEiGsbb10EpQck65M/9doWQ8KKhdrWiX/EVKw==",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
  "id": -576460752303421285,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JILAfhCuEB6hE0NiTMcc91ZqpgDvg28FDdHqCPwA4mnKGEQ3rokEldyfOV6bKrlEXuC76MMYavpjxf7SEr0/g+KoOVLGV8FuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBI6Ce9D8DxiGWAdEBIhrG29dBKUHJOuTP/XaFkPCioXa1onxo0N8="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEB6hE0NiTMcc91ZqpgDvg28FDdHqCPwA4mnKGEQ3rokEldyfOV6bKrlEXuC76MMYavpjxf7SEr0/g+KoOVLGV8FuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBI6Ce9D8DxiGWAdEBIhrG29dBKUHJOuTP/XaFkPCioXa1onxo0N8=",
      "updates": [
        {
          "abi_version": 3,
          "call_data": "cb_KxFE1kQfP4oEp9E=",
          "code": "cb_+ItGA6Csy3JozRdXcB9XGjK/NKTZBXnERI+ujyie0Pd2CK5dCcC4Xrg4/kTWRB8ANwA3ABoOgj8BAz/+0ARcIwQ3A0cCd3cXDAEEDAECDAMADAEAAwD8EcTVlAk3And3FwCgLwIRRNZEHxFpbml0EdAEXCM5cmVtb3RlX3Jlc29sdmWCLwCFNC4yLjAAUHv/qQ==",
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
  "id": -576460752303421284,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NQLAfiEuEB6hE0NiTMcc91ZqpgDvg28FDdHqCPwA4mnKGEQ3rokEldyfOV6bKrlEXuC76MMYavpjxf7SEr0/g+KoOVLGV8FuED0LNiIH4I/3u6C5VQVkQzgbfhHc5av50DX47+ALKD5KTWCsEQ5qUtR0u6dltyq/RUC/iarSRDH6qxZqFaoTKoLuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBI6Ce9D8DxiGWAdEBIhrG29dBKUHJOuTP/XaFkPCioXa1orBFJPQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEB6hE0NiTMcc91ZqpgDvg28FDdHqCPwA4mnKGEQ3rokEldyfOV6bKrlEXuC76MMYavpjxf7SEr0/g+KoOVLGV8FuED0LNiIH4I/3u6C5VQVkQzgbfhHc5av50DX47+ALKD5KTWCsEQ5qUtR0u6dltyq/RUC/iarSRDH6qxZqFaoTKoLuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBI6Ce9D8DxiGWAdEBIhrG29dBKUHJOuTP/XaFkPCioXa1orBFJPQ="
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
      "state": "tx_+NQLAfiEuEB6hE0NiTMcc91ZqpgDvg28FDdHqCPwA4mnKGEQ3rokEldyfOV6bKrlEXuC76MMYavpjxf7SEr0/g+KoOVLGV8FuED0LNiIH4I/3u6C5VQVkQzgbfhHc5av50DX47+ALKD5KTWCsEQ5qUtR0u6dltyq/RUC/iarSRDH6qxZqFaoTKoLuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBI6Ce9D8DxiGWAdEBIhrG29dBKUHJOuTP/XaFkPCioXa1orBFJPQ="
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
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
      "caller_nonce": 292,
      "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
  }
}
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEkoAmBG5MIk9iRpcUq3KtKh7RU+1hWJiVMk6KSEyUL+6VADZZ5eg==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuECNnNMSvhsGmX9wo81VLJcGIf7iBlF1timmg0CPC2F3L1dO4vAVdWa/0QZZEpVsTNyHCWAc86IuyFxK15UG3LUKuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBJKAJgRuTCJPYkaXFKtyrSoe0VPtYViYlTJOikhMlC/ulQCORWp8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuECNnNMSvhsGmX9wo81VLJcGIf7iBlF1timmg0CPC2F3L1dO4vAVdWa/0QZZEpVsTNyHCWAc86IuyFxK15UG3LUKuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBJKAJgRuTCJPYkaXFKtyrSoe0VPtYViYlTJOikhMlC/ulQCORWp8=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuECNnNMSvhsGmX9wo81VLJcGIf7iBlF1timmg0CPC2F3L1dO4vAVdWa/0QZZEpVsTNyHCWAc86IuyFxK15UG3LUKuEDEyscCVRuDC0dHL7+j890QBtPAo1wfqH48Kc1iVNUaqZ8AaN60oTMkb1YL0CL5xwB7qfuXxwBBdV2XN8Vnv/4CuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBJKAJgRuTCJPYkaXFKtyrSoe0VPtYViYlTJOikhMlC/ulQPt4YFU="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuECNnNMSvhsGmX9wo81VLJcGIf7iBlF1timmg0CPC2F3L1dO4vAVdWa/0QZZEpVsTNyHCWAc86IuyFxK15UG3LUKuEDEyscCVRuDC0dHL7+j890QBtPAo1wfqH48Kc1iVNUaqZ8AaN60oTMkb1YL0CL5xwB7qfuXxwBBdV2XN8Vnv/4CuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBJKAJgRuTCJPYkaXFKtyrSoe0VPtYViYlTJOikhMlC/ulQPt4YFU="
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
      "state": "tx_+NQLAfiEuECNnNMSvhsGmX9wo81VLJcGIf7iBlF1timmg0CPC2F3L1dO4vAVdWa/0QZZEpVsTNyHCWAc86IuyFxK15UG3LUKuEDEyscCVRuDC0dHL7+j890QBtPAo1wfqH48Kc1iVNUaqZ8AaN60oTMkb1YL0CL5xwB7qfuXxwBBdV2XN8Vnv/4CuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBJKAJgRuTCJPYkaXFKtyrSoe0VPtYViYlTJOikhMlC/ulQPt4YFU="
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
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
    "round": 292
  }
}
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
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 292
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 292,
      "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
    "round": 292
  }
}
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
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 292
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 292,
      "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
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
      "caller_nonce": 293,
      "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
  }
}
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEloNygRr1Sxsh4HHQGv87i4f7IeDsMCFrmnSBzox1ao+JdRAAsNw==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEAXPy+nrDFfydu/V9YpcZyo7zeASa+uIZCLq96ncoaJ1q1OKCzpxAIIVbH0XM5Nr/qrrRtZbUJ47Zld7km1VeYMuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBJaDcoEa9UsbIeBx0Br/O4uH+yHg7DAha5p0gc6MdWqPiXd7FrXQ="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEAXPy+nrDFfydu/V9YpcZyo7zeASa+uIZCLq96ncoaJ1q1OKCzpxAIIVbH0XM5Nr/qrrRtZbUJ47Zld7km1VeYMuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBJaDcoEa9UsbIeBx0Br/O4uH+yHg7DAha5p0gc6MdWqPiXd7FrXQ=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEAXPy+nrDFfydu/V9YpcZyo7zeASa+uIZCLq96ncoaJ1q1OKCzpxAIIVbH0XM5Nr/qrrRtZbUJ47Zld7km1VeYMuEA6LSEdhIRyquZKScD48ApNUIjXsYaVnfDJ3h7gAsGaQOvZQCKlpmMtHRuZIs+GyuDkirx7VN5TLTq4iyZknJ0IuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBJaDcoEa9UsbIeBx0Br/O4uH+yHg7DAha5p0gc6MdWqPiXbpuVfA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEAXPy+nrDFfydu/V9YpcZyo7zeASa+uIZCLq96ncoaJ1q1OKCzpxAIIVbH0XM5Nr/qrrRtZbUJ47Zld7km1VeYMuEA6LSEdhIRyquZKScD48ApNUIjXsYaVnfDJ3h7gAsGaQOvZQCKlpmMtHRuZIs+GyuDkirx7VN5TLTq4iyZknJ0IuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBJaDcoEa9UsbIeBx0Br/O4uH+yHg7DAha5p0gc6MdWqPiXbpuVfA="
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
      "state": "tx_+NQLAfiEuEAXPy+nrDFfydu/V9YpcZyo7zeASa+uIZCLq96ncoaJ1q1OKCzpxAIIVbH0XM5Nr/qrrRtZbUJ47Zld7km1VeYMuEA6LSEdhIRyquZKScD48ApNUIjXsYaVnfDJ3h7gAsGaQOvZQCKlpmMtHRuZIs+GyuDkirx7VN5TLTq4iyZknJ0IuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBJaDcoEa9UsbIeBx0Br/O4uH+yHg7DAha5p0gc6MdWqPiXbpuVfA="
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
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
    "round": 293
  }
}
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
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 293
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 293,
      "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
    "round": 293
  }
}
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
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 293
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 293,
      "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "ABCDEFG",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
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
      "caller_nonce": 294,
      "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "ABCDEFG",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "ABCDEFG",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
  }
}
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "ABCDEFG",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEmoD6W8+3YfdvOg7W9O8ojGYD62mFJp57vV5Ej9EmBOUXLN3UvhA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEBnKtBBjfFKeWmKNBYxKT0t7UVfK9MRiq9BvXDQJFCF96LEO4XWzCF4yKfi1tGhoDsRAY1GxExqbLmJLQXSGeMPuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBJqA+lvPt2H3bzoO1vTvKIxmA+tphSaee71eRI/RJgTlFy6YrNHU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEBnKtBBjfFKeWmKNBYxKT0t7UVfK9MRiq9BvXDQJFCF96LEO4XWzCF4yKfi1tGhoDsRAY1GxExqbLmJLQXSGeMPuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBJqA+lvPt2H3bzoO1vTvKIxmA+tphSaee71eRI/RJgTlFy6YrNHU=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEBnKtBBjfFKeWmKNBYxKT0t7UVfK9MRiq9BvXDQJFCF96LEO4XWzCF4yKfi1tGhoDsRAY1GxExqbLmJLQXSGeMPuEBpyu4ta9HUFAxXWTEdO1NbahM1o/DbGuSL8Tni7bllMIFWeCXs71zgskORzxOdzQGMw7DsJegX83bOjuEilcoGuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBJqA+lvPt2H3bzoO1vTvKIxmA+tphSaee71eRI/RJgTlFy5JQJJ8="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEBnKtBBjfFKeWmKNBYxKT0t7UVfK9MRiq9BvXDQJFCF96LEO4XWzCF4yKfi1tGhoDsRAY1GxExqbLmJLQXSGeMPuEBpyu4ta9HUFAxXWTEdO1NbahM1o/DbGuSL8Tni7bllMIFWeCXs71zgskORzxOdzQGMw7DsJegX83bOjuEilcoGuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBJqA+lvPt2H3bzoO1vTvKIxmA+tphSaee71eRI/RJgTlFy5JQJJ8="
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
      "state": "tx_+NQLAfiEuEBnKtBBjfFKeWmKNBYxKT0t7UVfK9MRiq9BvXDQJFCF96LEO4XWzCF4yKfi1tGhoDsRAY1GxExqbLmJLQXSGeMPuEBpyu4ta9HUFAxXWTEdO1NbahM1o/DbGuSL8Tni7bllMIFWeCXs71zgskORzxOdzQGMw7DsJegX83bOjuEilcoGuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBJqA+lvPt2H3bzoO1vTvKIxmA+tphSaee71eRI/RJgTlFy5JQJJ8="
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
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
    "round": 294
  }
}
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
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 294
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 294,
      "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
    "round": 294
  }
}
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
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 294
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 294,
      "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "ABCDEFG",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
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
      "caller_nonce": 295,
      "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "ABCDEFG",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "ABCDEFG",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
  }
}
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "ABCDEFG",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
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
        "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
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
    "block_hash": "kh_FvLjnRcuWHKzTTNxKscgNXPijP8C6crb4oQxj5KPxuaKN7a7M",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEnoIbK+gt1Fn1wsuldrcH6XPYk2zrOIbDAS9xoFXtUPBqjaTzonA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEBLltWtK1+25pLPhTR8UcchrvRZYRc2FQDi7QchWc/xo3n1WzwSne0cV+ITnGdckWy2fmUrEn5Hsus8fh/8QxgKuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBJ6CGyvoLdRZ9cLLpXa3B+lz2JNs6ziGwwEvcaBV7VDwaoxUEjew="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEBLltWtK1+25pLPhTR8UcchrvRZYRc2FQDi7QchWc/xo3n1WzwSne0cV+ITnGdckWy2fmUrEn5Hsus8fh/8QxgKuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBJ6CGyvoLdRZ9cLLpXa3B+lz2JNs6ziGwwEvcaBV7VDwaoxUEjew=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEBLltWtK1+25pLPhTR8UcchrvRZYRc2FQDi7QchWc/xo3n1WzwSne0cV+ITnGdckWy2fmUrEn5Hsus8fh/8QxgKuECZA765TmeZWpwdwEmyQWT/NqRROIxZ63JZWcmJWkXq91dWkXHsgsy+zxJnVD4Xnp2j27QzfF+323LKBc6zEiMFuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBJ6CGyvoLdRZ9cLLpXa3B+lz2JNs6ziGwwEvcaBV7VDwao6z6i0A="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEBLltWtK1+25pLPhTR8UcchrvRZYRc2FQDi7QchWc/xo3n1WzwSne0cV+ITnGdckWy2fmUrEn5Hsus8fh/8QxgKuECZA765TmeZWpwdwEmyQWT/NqRROIxZ63JZWcmJWkXq91dWkXHsgsy+zxJnVD4Xnp2j27QzfF+323LKBc6zEiMFuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBJ6CGyvoLdRZ9cLLpXa3B+lz2JNs6ziGwwEvcaBV7VDwao6z6i0A="
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
      "state": "tx_+NQLAfiEuEBLltWtK1+25pLPhTR8UcchrvRZYRc2FQDi7QchWc/xo3n1WzwSne0cV+ITnGdckWy2fmUrEn5Hsus8fh/8QxgKuECZA765TmeZWpwdwEmyQWT/NqRROIxZ63JZWcmJWkXq91dWkXHsgsy+zxJnVD4Xnp2j27QzfF+323LKBc6zEiMFuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBJ6CGyvoLdRZ9cLLpXa3B+lz2JNs6ziGwwEvcaBV7VDwao6z6i0A="
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
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
    "round": 295
  }
}
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
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 295
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 295,
      "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
    "round": 295
  }
}
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
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 295
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 295,
      "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
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
      "caller_nonce": 296,
      "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
  }
}
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEooJfj0Zn3eElMssL+pUIMhbiC7feRBLBD62dcwhkCBmFHGggV9w==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEDWV6OVnG4QwfwXEJnZOJ8glUJirJeL/ka/96HOH5wjnQah6RZu95ttwPlyrD6tkAj7aJlspmYxDEzlcKk7PysOuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBKKCX49GZ93hJTLLC/qVCDIW4gu33kQSwQ+tnXMIZAgZhR7K3Y8s="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEDWV6OVnG4QwfwXEJnZOJ8glUJirJeL/ka/96HOH5wjnQah6RZu95ttwPlyrD6tkAj7aJlspmYxDEzlcKk7PysOuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBKKCX49GZ93hJTLLC/qVCDIW4gu33kQSwQ+tnXMIZAgZhR7K3Y8s=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEDWV6OVnG4QwfwXEJnZOJ8glUJirJeL/ka/96HOH5wjnQah6RZu95ttwPlyrD6tkAj7aJlspmYxDEzlcKk7PysOuED4NngIbpQsmURFcIJSjac6OBVsYtvn0uXFjnB6yTnSRZapOdHCsGa4OsGVYDYkrFyamhCxMJduqoNFv9NRKgQEuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBKKCX49GZ93hJTLLC/qVCDIW4gu33kQSwQ+tnXMIZAgZhR24Jb4Y="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEDWV6OVnG4QwfwXEJnZOJ8glUJirJeL/ka/96HOH5wjnQah6RZu95ttwPlyrD6tkAj7aJlspmYxDEzlcKk7PysOuED4NngIbpQsmURFcIJSjac6OBVsYtvn0uXFjnB6yTnSRZapOdHCsGa4OsGVYDYkrFyamhCxMJduqoNFv9NRKgQEuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBKKCX49GZ93hJTLLC/qVCDIW4gu33kQSwQ+tnXMIZAgZhR24Jb4Y="
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
      "state": "tx_+NQLAfiEuEDWV6OVnG4QwfwXEJnZOJ8glUJirJeL/ka/96HOH5wjnQah6RZu95ttwPlyrD6tkAj7aJlspmYxDEzlcKk7PysOuED4NngIbpQsmURFcIJSjac6OBVsYtvn0uXFjnB6yTnSRZapOdHCsGa4OsGVYDYkrFyamhCxMJduqoNFv9NRKgQEuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBKKCX49GZ93hJTLLC/qVCDIW4gu33kQSwQ+tnXMIZAgZhR24Jb4Y="
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
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
    "round": 296
  }
}
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
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 296
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 296,
      "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
    "round": 296
  }
}
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
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 296
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 296,
      "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
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
      "caller_nonce": 297,
      "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "ABCDEFG",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
  }
}
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "ABCDEFG",
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEpoIIvmrJ2xONhKwEG7q0dw+ebqj5Gc9NPU0E+1DhnDgWynPHKiA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEA9nqEox+MfN2YK3Fi5QBK8jFO5h/yQR3HOK2FpWFQKy3G9z5UJBZYryRyTgjMKmpL4GwqTaetXkcbLsv5N2xkHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBKaCCL5qydsTjYSsBBu6tHcPnm6o+RnPTT1NBPtQ4Zw4FsuxuKVA="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEA9nqEox+MfN2YK3Fi5QBK8jFO5h/yQR3HOK2FpWFQKy3G9z5UJBZYryRyTgjMKmpL4GwqTaetXkcbLsv5N2xkHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBKaCCL5qydsTjYSsBBu6tHcPnm6o+RnPTT1NBPtQ4Zw4FsuxuKVA=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 0,
          "call_data": "cb_KxHE1ZQJK1E4Q25hR2ZuN290ZGZTVC5jaGFpbjlhY2NvdW50X3B1YmtleaoHEAQ=",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEAOQxib3Xe9fWFKA/nqzUtjKpF/zLsND/8tDHUHaswxC/Yi8qyKpUpKFwGz2q5yl0n9MIuj6hJODLWWbRqnr6kBuEA9nqEox+MfN2YK3Fi5QBK8jFO5h/yQR3HOK2FpWFQKy3G9z5UJBZYryRyTgjMKmpL4GwqTaetXkcbLsv5N2xkHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBKaCCL5qydsTjYSsBBu6tHcPnm6o+RnPTT1NBPtQ4Zw4Fsg9vF/Y="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEAOQxib3Xe9fWFKA/nqzUtjKpF/zLsND/8tDHUHaswxC/Yi8qyKpUpKFwGz2q5yl0n9MIuj6hJODLWWbRqnr6kBuEA9nqEox+MfN2YK3Fi5QBK8jFO5h/yQR3HOK2FpWFQKy3G9z5UJBZYryRyTgjMKmpL4GwqTaetXkcbLsv5N2xkHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBKaCCL5qydsTjYSsBBu6tHcPnm6o+RnPTT1NBPtQ4Zw4Fsg9vF/Y="
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
      "state": "tx_+NQLAfiEuEAOQxib3Xe9fWFKA/nqzUtjKpF/zLsND/8tDHUHaswxC/Yi8qyKpUpKFwGz2q5yl0n9MIuj6hJODLWWbRqnr6kBuEA9nqEox+MfN2YK3Fi5QBK8jFO5h/yQR3HOK2FpWFQKy3G9z5UJBZYryRyTgjMKmpL4GwqTaetXkcbLsv5N2xkHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBKaCCL5qydsTjYSsBBu6tHcPnm6o+RnPTT1NBPtQ4Zw4Fsg9vF/Y="
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
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
    "round": 297
  }
}
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
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 297
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 297,
      "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
    "round": 297
  }
}
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
        "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 297
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 297,
      "contract_id": "ct_fZJ5qxN5nAMaiWwezbyAYtZ1xDoJZ5QBeUB5u7N2JemWexgfs",
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "ABCDEFG",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
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
      "caller_nonce": 298,
      "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "ABCDEFG",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "ABCDEFG",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
  }
}
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "ABCDEFG",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEqoMCmbsMrAoDAdFvyaYuIQvhbvQVH9DC93ioRN7qRSJwB/ChqAA==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEAaOqKC6UW3uIgb5h4gDA7aBQSwlvAqTfewLa3EjqWE4Ai9WBzN6YOXPaD/W1bE0T1dLraW7SMNPmtcWEtCfEYFuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBKqDApm7DKwKAwHRb8mmLiEL4W70FR/Qwvd4qETe6kUicAXIXOxU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEAaOqKC6UW3uIgb5h4gDA7aBQSwlvAqTfewLa3EjqWE4Ai9WBzN6YOXPaD/W1bE0T1dLraW7SMNPmtcWEtCfEYFuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBKqDApm7DKwKAwHRb8mmLiEL4W70FR/Qwvd4qETe6kUicAXIXOxU=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
          "call_stack": [],
          "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
          "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEAaOqKC6UW3uIgb5h4gDA7aBQSwlvAqTfewLa3EjqWE4Ai9WBzN6YOXPaD/W1bE0T1dLraW7SMNPmtcWEtCfEYFuEC/nngbjArrl230onsjxoyjmKF+VtrB6W1rI9AO6g7fJHYVZZzV+LG4E8ES8fd59YnGNV0am0c8KJUTSVuGKaYHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBKqDApm7DKwKAwHRb8mmLiEL4W70FR/Qwvd4qETe6kUicASctrOc="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEAaOqKC6UW3uIgb5h4gDA7aBQSwlvAqTfewLa3EjqWE4Ai9WBzN6YOXPaD/W1bE0T1dLraW7SMNPmtcWEtCfEYFuEC/nngbjArrl230onsjxoyjmKF+VtrB6W1rI9AO6g7fJHYVZZzV+LG4E8ES8fd59YnGNV0am0c8KJUTSVuGKaYHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBKqDApm7DKwKAwHRb8mmLiEL4W70FR/Qwvd4qETe6kUicASctrOc="
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
      "state": "tx_+NQLAfiEuEAaOqKC6UW3uIgb5h4gDA7aBQSwlvAqTfewLa3EjqWE4Ai9WBzN6YOXPaD/W1bE0T1dLraW7SMNPmtcWEtCfEYFuEC/nngbjArrl230onsjxoyjmKF+VtrB6W1rI9AO6g7fJHYVZZzV+LG4E8ES8fd59YnGNV0am0c8KJUTSVuGKaYHuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBKqDApm7DKwKAwHRb8mmLiEL4W70FR/Qwvd4qETe6kUicASctrOc="
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
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
    "round": 298
  }
}
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
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 298
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 298,
      "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
    "round": 298
  }
}
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
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ABCDEFG",
    "round": 298
  }
}
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
    "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_2QwJuWusUKsMsJZP2zGrdH31xTs5UtzHwtQgjxL9F1crCymTYi",
      "caller_nonce": 298,
      "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "ABCDEFG",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
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
      "caller_nonce": 299,
      "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "ABCDEFG",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
  "error": {
    "code": 3,
    "data": [
      {
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "ABCDEFG",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
  }
}
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "ABCDEFG",
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
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
        "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
        "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
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
    "block_hash": "kh_2vw1Rv6Tqs2qbdVYsLa8aEK2ibRB3J2enWZEt2qv1nq9AiL86f",
    "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm"
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
      "signed_tx": "tx_+E8LAcC4SvhIOQKhBkeFtMN3yJi5ojgL2kabgMHSaP6IFnCV23TDXLfIUF8RggEroCWiY9WcTDPxLtT/0mqlx2QtGAyK0jcPQBt94N0Pnsagky7vag==",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
          "gas": 1000000,
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
    "signed_tx": "tx_+JILAfhCuEB/WaG1xOWPHv99oZlX9gT8CIHJFS3+37l6oV7vg8uyxh6NTX/oguVo2hXIc9U17ouwTdnIGOXyA9WbYC/XyVkOuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBK6AlomPVnEwz8S7U/9JqpcdkLRgMitI3D0AbfeDdD57GoCXprl0="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
      "signed_tx": "tx_+JILAfhCuEB/WaG1xOWPHv99oZlX9gT8CIHJFS3+37l6oV7vg8uyxh6NTX/oguVo2hXIc9U17ouwTdnIGOXyA9WbYC/XyVkOuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBK6AlomPVnEwz8S7U/9JqpcdkLRgMitI3D0AbfeDdD57GoCXprl0=",
      "updates": [
        {
          "abi_version": 3,
          "amount": 20,
          "call_data": "cb_KxHQBFwjO58CoFeMRZXLxwTDHlR7uJviYxrxliCdt5Ux2jkyEL73xXU0UThDbmFHZm43b3RkZlNULmNoYWluOWFjY291bnRfcHVia2V5A/9gNA==",
          "call_stack": [],
          "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
          "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
          "gas": 1000000,
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
    "signed_tx": "tx_+NQLAfiEuEB/WaG1xOWPHv99oZlX9gT8CIHJFS3+37l6oV7vg8uyxh6NTX/oguVo2hXIc9U17ouwTdnIGOXyA9WbYC/XyVkOuED4wGkWQCXEdKrLkJNoauLH0Ap6x8MbB4/9OBLog7nNPLCHW01JNxzcLzOBMF3Y5ecMzL0EDKqX2FqP613PCOkFuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBK6AlomPVnEwz8S7U/9JqpcdkLRgMitI3D0AbfeDdD57GoBFcgJI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "state": "tx_+NQLAfiEuEB/WaG1xOWPHv99oZlX9gT8CIHJFS3+37l6oV7vg8uyxh6NTX/oguVo2hXIc9U17ouwTdnIGOXyA9WbYC/XyVkOuED4wGkWQCXEdKrLkJNoauLH0Ap6x8MbB4/9OBLog7nNPLCHW01JNxzcLzOBMF3Y5ecMzL0EDKqX2FqP613PCOkFuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBK6AlomPVnEwz8S7U/9JqpcdkLRgMitI3D0AbfeDdD57GoBFcgJI="
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
      "state": "tx_+NQLAfiEuEB/WaG1xOWPHv99oZlX9gT8CIHJFS3+37l6oV7vg8uyxh6NTX/oguVo2hXIc9U17ouwTdnIGOXyA9WbYC/XyVkOuED4wGkWQCXEdKrLkJNoauLH0Ap6x8MbB4/9OBLog7nNPLCHW01JNxzcLzOBMF3Y5ecMzL0EDKqX2FqP613PCOkFuEr4SDkCoQZHhbTDd8iYuaI4C9pGm4DB0mj+iBZwldt0w1y3yFBfEYIBK6AlomPVnEwz8S7U/9JqpcdkLRgMitI3D0AbfeDdD57GoBFcgJI="
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
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
    "round": 299
  }
}
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
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 299
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 299,
      "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
    "round": 299
  }
}
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
        "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ABCDEFG",
    "round": 299
  }
}
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
    "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
    "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
    "channel_id": "ch_YVwaAGzcUHCrTAzxS2Bwz1YoKvneG3YU5JtKSMKY7ugFsyFB5",
    "data": {
      "caller_id": "ak_E4vsydvYPV6U4srWKatNCjNUuEJxLPwqUXX8e7FURAwaMrxFq",
      "caller_nonce": 299,
      "contract_id": "ct_7d8Mjp1djqyX6mTBLJxmJkD5pXx1uUPG9ZJj2oKX4HyTkazLm",
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
