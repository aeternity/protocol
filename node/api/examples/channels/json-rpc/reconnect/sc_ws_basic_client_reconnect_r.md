
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2U2V8T4zSRLTVp5K3bsKsiQPAii7VvMSpxD95ybfA3zjCoWi3b&keep_running=false&lock_period=10&port=14035&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2uFSApTp2e4tMW1wkdi7KGG8z1rvmeK5F1b8Ng2iaEsawhu56t&role=initiator
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_wTv4wdihZfy8NMutoV/49cugBq5zyafFdjLAoVBgXSuTffUP"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2U2V8T4zSRLTVp5K3bsKsiQPAii7VvMSpxD95ybfA3zjCoWi3b&keep_running=false&lock_period=10&port=14035&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2uFSApTp2e4tMW1wkdi7KGG8z1rvmeK5F1b8Ng2iaEsawhu56t&role=responder
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_xkSVgiFx6074nbfvXoHQzVQLRSaECusBVNfQnjnjsR9yVO+D"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_open"
    }
  },
  "version": 1
}
```

#### responder info
> Received an WebSocket opening request

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_accept"
    }
  },
  "version": 1
}
```

#### initiator info
> Received an WebSocket connection accepted

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcEPn9wYW2WeUioPc0aitoAUhn4Ax/9xBaFbAsrOdjjMhj+qJSJgAKEB+lVh/1JOug59Vm1c+vAibQDj/BQPKb3keGhF4zJuJBGGJGE5yoAAAgoAhhAGeddIAMCg1L8DGd++jlpUYTNXUSswpxHX8sdCYQqWeBe+ygX0qb8DvehTvg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423002,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEADsH4OijwHsvg5OsFQYbC/yv9GMVOegS2SZ3BEfmTjMk93pJQP3Vs1hD1JxbyQU9qgDQYEbxNydSICA5yRKtYBuIP4gTIBoQHBD5/cGFtlnlIqD3NGoraAFIZ+AMf/cQWhWwLKznY4zIY/qiUiYAChAfpVYf9STroOfVZtXPrwIm0A4/wUDym95HhoReMybiQRhiRhOcqAAAIKAIYQBnnXSADAoNS/Axnfvo5aVGEzV1ErMKcR1/LHQmEKlngXvsoF9Km/Azsi8Z4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423002,
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
    "channel_id": null,
    "data": {
      "event": "funding_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+MsLAfhCuEADsH4OijwHsvg5OsFQYbC/yv9GMVOegS2SZ3BEfmTjMk93pJQP3Vs1hD1JxbyQU9qgDQYEbxNydSICA5yRKtYBuIP4gTIBoQHBD5/cGFtlnlIqD3NGoraAFIZ+AMf/cQWhWwLKznY4zIY/qiUiYAChAfpVYf9STroOfVZtXPrwIm0A4/wUDym95HhoReMybiQRhiRhOcqAAAIKAIYQBnnXSADAoNS/Axnfvo5aVGEzV1ErMKcR1/LHQmEKlngXvsoF9Km/Azsi8Z4=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423001,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAA7B+Doo8B7L4OTrBUGGwv8r/RjFTnoEtkmdwRH5k4zJPd6SUD91bNYQ9ScW8kFPaoA0GBG8TcnUiAgOckSrWAbhAiLKVV4CQ7gTMeLgolAsQaejDMYq1ec3ZqjuIPiWDXljitI2zrMV3jJH6nBR21IWtaF2YDExBUdzKviudLz5JD7iD+IEyAaEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGP6olImAAoQH6VWH/Uk66Dn1WbVz68CJtAOP8FA8pveR4aEXjMm4kEYYkYTnKgAACCgCGEAZ510gAwKDUvwMZ376OWlRhM1dRKzCnEdfyx0JhCpZ4F77KBfSpvwNBN3H9"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423001,
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
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAA7B+Doo8B7L4OTrBUGGwv8r/RjFTnoEtkmdwRH5k4zJPd6SUD91bNYQ9ScW8kFPaoA0GBG8TcnUiAgOckSrWAbhAiLKVV4CQ7gTMeLgolAsQaejDMYq1ec3ZqjuIPiWDXljitI2zrMV3jJH6nBR21IWtaF2YDExBUdzKviudLz5JD7iD+IEyAaEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGP6olImAAoQH6VWH/Uk66Dn1WbVz68CJtAOP8FA8pveR4aEXjMm4kEYYkYTnKgAACCgCGEAZ510gAwKDUvwMZ376OWlRhM1dRKzCnEdfyx0JhCpZ4F77KBfSpvwNBN3H9",
      "type": "channel_create_tx"
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
    "channel_id": null,
    "data": {
      "event": "funding_signed"
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
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAA7B+Doo8B7L4OTrBUGGwv8r/RjFTnoEtkmdwRH5k4zJPd6SUD91bNYQ9ScW8kFPaoA0GBG8TcnUiAgOckSrWAbhAiLKVV4CQ7gTMeLgolAsQaejDMYq1ec3ZqjuIPiWDXljitI2zrMV3jJH6nBR21IWtaF2YDExBUdzKviudLz5JD7iD+IEyAaEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGP6olImAAoQH6VWH/Uk66Dn1WbVz68CJtAOP8FA8pveR4aEXjMm4kEYYkYTnKgAACCgCGEAZ510gAwKDUvwMZ376OWlRhM1dRKzCnEdfyx0JhCpZ4F77KBfSpvwNBN3H9",
      "type": "channel_create_tx"
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
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAA7B+Doo8B7L4OTrBUGGwv8r/RjFTnoEtkmdwRH5k4zJPd6SUD91bNYQ9ScW8kFPaoA0GBG8TcnUiAgOckSrWAbhAiLKVV4CQ7gTMeLgolAsQaejDMYq1ec3ZqjuIPiWDXljitI2zrMV3jJH6nBR21IWtaF2YDExBUdzKviudLz5JD7iD+IEyAaEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGP6olImAAoQH6VWH/Uk66Dn1WbVz68CJtAOP8FA8pveR4aEXjMm4kEYYkYTnKgAACCgCGEAZ510gAwKDUvwMZ376OWlRhM1dRKzCnEdfyx0JhCpZ4F77KBfSpvwNBN3H9",
      "type": "channel_create_tx"
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
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAA7B+Doo8B7L4OTrBUGGwv8r/RjFTnoEtkmdwRH5k4zJPd6SUD91bNYQ9ScW8kFPaoA0GBG8TcnUiAgOckSrWAbhAiLKVV4CQ7gTMeLgolAsQaejDMYq1ec3ZqjuIPiWDXljitI2zrMV3jJH6nBR21IWtaF2YDExBUdzKviudLz5JD7iD+IEyAaEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGP6olImAAoQH6VWH/Uk66Dn1WbVz68CJtAOP8FA8pveR4aEXjMm4kEYYkYTnKgAACCgCGEAZ510gAwKDUvwMZ376OWlRhM1dRKzCnEdfyx0JhCpZ4F77KBfSpvwNBN3H9",
      "type": "channel_create_tx"
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
    "to": "ak_2uFSApTp2e4tMW1wkdi7KGG8z1rvmeK5F1b8Ng2iaEsawhu56t"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "message": {
        "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
        "from": "ak_2U2V8T4zSRLTVp5K3bsKsiQPAii7VvMSpxD95ybfA3zjCoWi3b",
        "info": "Hello",
        "to": "ak_2uFSApTp2e4tMW1wkdi7KGG8z1rvmeK5F1b8Ng2iaEsawhu56t"
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
    "to": "ak_2U2V8T4zSRLTVp5K3bsKsiQPAii7VvMSpxD95ybfA3zjCoWi3b"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "message": {
        "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
        "from": "ak_2uFSApTp2e4tMW1wkdi7KGG8z1rvmeK5F1b8Ng2iaEsawhu56t",
        "info": "Hello back",
        "to": "ak_2U2V8T4zSRLTVp5K3bsKsiQPAii7VvMSpxD95ybfA3zjCoWi3b"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423000,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2U2V8T4zSRLTVp5K3bsKsiQPAii7VvMSpxD95ybfA3zjCoWi3b",
      "ak_2uFSApTp2e4tMW1wkdi7KGG8z1rvmeK5F1b8Ng2iaEsawhu56t"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
  "id": -576460752303423000,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2U2V8T4zSRLTVp5K3bsKsiQPAii7VvMSpxD95ybfA3zjCoWi3b",
      "balance": 69999999999999
    },
    {
      "account": "ak_2uFSApTp2e4tMW1wkdi7KGG8z1rvmeK5F1b8Ng2iaEsawhu56t",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder info
> Channel is `open` and ready to use

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "state": "tx_+QENCwH4hLhAA7B+Doo8B7L4OTrBUGGwv8r/RjFTnoEtkmdwRH5k4zJPd6SUD91bNYQ9ScW8kFPaoA0GBG8TcnUiAgOckSrWAbhAiLKVV4CQ7gTMeLgolAsQaejDMYq1ec3ZqjuIPiWDXljitI2zrMV3jJH6nBR21IWtaF2YDExBUdzKviudLz5JD7iD+IEyAaEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGP6olImAAoQH6VWH/Uk66Dn1WbVz68CJtAOP8FA8pveR4aEXjMm4kEYYkYTnKgAACCgCGEAZ510gAwKDUvwMZ376OWlRhM1dRKzCnEdfyx0JhCpZ4F77KBfSpvwNBN3H9"
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
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "state": "tx_+QENCwH4hLhAA7B+Doo8B7L4OTrBUGGwv8r/RjFTnoEtkmdwRH5k4zJPd6SUD91bNYQ9ScW8kFPaoA0GBG8TcnUiAgOckSrWAbhAiLKVV4CQ7gTMeLgolAsQaejDMYq1ec3ZqjuIPiWDXljitI2zrMV3jJH6nBR21IWtaF2YDExBUdzKviudLz5JD7iD+IEyAaEBwQ+f3BhbZZ5SKg9zRqK2gBSGfgDH/3EFoVsCys52OMyGP6olImAAoQH6VWH/Uk66Dn1WbVz68CJtAOP8FA8pveR4aEXjMm4kEYYkYTnKgAACCgCGEAZ510gAwKDUvwMZ376OWlRhM1dRKzCnEdfyx0JhCpZ4F77KBfSpvwNBN3H9"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2U2V8T4zSRLTVp5K3bsKsiQPAii7VvMSpxD95ybfA3zjCoWi3b",
    "to": "ak_2uFSApTp2e4tMW1wkdi7KGG8z1rvmeK5F1b8Ng2iaEsawhu56t"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjndGdENR43i/ST/rbvZcsxtfpNcFXiSAZFSaexPrz5lAqDG9uRBBL/Aje12wpyVqdVWVpvtvHC+ayUmZO5M8rou4GqR8gM=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2U2V8T4zSRLTVp5K3bsKsiQPAii7VvMSpxD95ybfA3zjCoWi3b",
          "op": "OffChainTransfer",
          "to": "ak_2uFSApTp2e4tMW1wkdi7KGG8z1rvmeK5F1b8Ng2iaEsawhu56t"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED//YnZjXPvFJwJrL1YkOQ0nykqOb35AE8mqGezypB/pBaY/5je/Kca4FJj3ZsUkQMB9Y/gPopBbhaFD6IkE4kHuEj4RjkCoQY53RnRDUeN4v0k/6272XLMbX6TXBV4kgGRUmnsT68+ZQKgxvbkQQS/wI3tdsKclanVVlab7bxwvmslJmTuTPK6LuAG+Pco"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 1
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2U2V8T4zSRLTVp5K3bsKsiQPAii7VvMSpxD95ybfA3zjCoWi3b",
    "to": "ak_2uFSApTp2e4tMW1wkdi7KGG8z1rvmeK5F1b8Ng2iaEsawhu56t"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjndGdENR43i/ST/rbvZcsxtfpNcFXiSAZFSaexPrz5lAqDG9uRBBL/Aje12wpyVqdVWVpvtvHC+ayUmZO5M8rou4GqR8gM=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2U2V8T4zSRLTVp5K3bsKsiQPAii7VvMSpxD95ybfA3zjCoWi3b",
          "op": "OffChainTransfer",
          "to": "ak_2uFSApTp2e4tMW1wkdi7KGG8z1rvmeK5F1b8Ng2iaEsawhu56t"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBvD6e+dHFGddp5rD8NATiz+01r2CxyEHoCwxv1g3AMr5yB0KXhIWz6jSEH6C4CUHQZ8we64/SI35pW9WIc8tQBuED//YnZjXPvFJwJrL1YkOQ0nykqOb35AE8mqGezypB/pBaY/5je/Kca4FJj3ZsUkQMB9Y/gPopBbhaFD6IkE4kHuEj4RjkCoQY53RnRDUeN4v0k/6272XLMbX6TXBV4kgGRUmnsT68+ZQKgxvbkQQS/wI3tdsKclanVVlab7bxwvmslJmTuTPK6LuAwKJr1"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "state": "tx_+NILAfiEuEBvD6e+dHFGddp5rD8NATiz+01r2CxyEHoCwxv1g3AMr5yB0KXhIWz6jSEH6C4CUHQZ8we64/SI35pW9WIc8tQBuED//YnZjXPvFJwJrL1YkOQ0nykqOb35AE8mqGezypB/pBaY/5je/Kca4FJj3ZsUkQMB9Y/gPopBbhaFD6IkE4kHuEj4RjkCoQY53RnRDUeN4v0k/6272XLMbX6TXBV4kgGRUmnsT68+ZQKgxvbkQQS/wI3tdsKclanVVlab7bxwvmslJmTuTPK6LuAwKJr1"
    }
  },
  "version": 1
}
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq&host=localhost&offchain_tx=tx_%2BNILAfiEuEBvD6e%2BdHFGddp5rD8NATiz%2B01r2CxyEHoCwxv1g3AMr5yB0KXhIWz6jSEH6C4CUHQZ8we64%2FSI35pW9WIc8tQBuED%2F%2FYnZjXPvFJwJrL1YkOQ0nykqOb35AE8mqGezypB%2FpBaY%2F5je%2FKca4FJj3ZsUkQMB9Y%2FgPopBbhaFD6IkE4kHuEj4RjkCoQY53RnRDUeN4v0k%2F6272XLMbX6TXBV4kgGRUmnsT68%2BZQKgxvbkQQS%2FwI3tdsKclanVVlab7bxwvmslJmTuTPK6LuAwKJr1&port=14035&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 2000,
        "message": "Missing field: existing_fsm_id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq&existing_fsm_id=Invalid&host=localhost&offchain_tx=tx_%2BNILAfiEuEBvD6e%2BdHFGddp5rD8NATiz%2B01r2CxyEHoCwxv1g3AMr5yB0KXhIWz6jSEH6C4CUHQZ8we64%2FSI35pW9WIc8tQBuED%2F%2FYnZjXPvFJwJrL1YkOQ0nykqOb35AE8mqGezypB%2FpBaY%2F5je%2FKca4FJj3ZsUkQMB9Y%2FgPopBbhaFD6IkE4kHuEj4RjkCoQY53RnRDUeN4v0k%2F6272XLMbX6TXBV4kgGRUmnsT68%2BZQKgxvbkQQS%2FwI3tdsKclanVVlab7bxwvmslJmTuTPK6LuAwKJr1&port=14035&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq&existing_fsm_id=ba_wiQauGtfDABUMh8m&host=localhost&offchain_tx=tx_%2BNILAfiEuEBvD6e%2BdHFGddp5rD8NATiz%2B01r2CxyEHoCwxv1g3AMr5yB0KXhIWz6jSEH6C4CUHQZ8we64%2FSI35pW9WIc8tQBuED%2F%2FYnZjXPvFJwJrL1YkOQ0nykqOb35AE8mqGezypB%2FpBaY%2F5je%2FKca4FJj3ZsUkQMB9Y%2FgPopBbhaFD6IkE4kHuEj4RjkCoQY53RnRDUeN4v0k%2F6272XLMbX6TXBV4kgGRUmnsT68%2BZQKgxvbkQQS%2FwI3tdsKclanVVlab7bxwvmslJmTuTPK6LuAwKJr1&port=14035&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq&existing_fsm_id=ba_5sDiT6khUv5i%2FWhTKcteGkAdFyhN%2BwgybeOQcLVosRLkfKQi&host=localhost&offchain_tx=tx_%2BNILAfiEuEBvD6e%2BdHFGddp5rD8NATiz%2B01r2CxyEHoCwxv1g3AMr5yB0KXhIWz6jSEH6C4CUHQZ8we64%2FSI35pW9WIc8tQBuED%2F%2FYnZjXPvFJwJrL1YkOQ0nykqOb35AE8mqGezypB%2FpBaY%2F5je%2FKca4FJj3ZsUkQMB9Y%2FgPopBbhaFD6IkE4kHuEj4RjkCoQY53RnRDUeN4v0k%2F6272XLMbX6TXBV4kgGRUmnsT68%2BZQKgxvbkQQS%2FwI3tdsKclanVVlab7bxwvmslJmTuTPK6LuAwKJr1&port=14035&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1016,
        "message": "Invalid fsm id"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder closes WebSocket connection

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq&existing_fsm_id=ba_xkSVgiFx6074nbfvXoHQzVQLRSaECusBVNfQnjnjsR9yVO%2BD&offchain_tx=tx_%2BNILAfiEuEBvD6e%2BdHFGddp5rD8NATiz%2B01r2CxyEHoCwxv1g3AMr5yB0KXhIWz6jSEH6C4CUHQZ8we64%2FSI35pW9WIc8tQBuED%2F%2FYnZjXPvFJwJrL1YkOQ0nykqOb35AE8mqGezypB%2FpBaY%2F5je%2FKca4FJj3ZsUkQMB9Y%2FgPopBbhaFD6IkE4kHuEj4RjkCoQY53RnRDUeN4v0k%2F6272XLMbX6TXBV4kgGRUmnsT68%2BZQKgxvbkQQS%2FwI3tdsKclanVVlab7bxwvmslJmTuTPK6LuAwKJr1&port=14035&protocol=json-rpc&role=responder
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_xkSVgiFx6074nbfvXoHQzVQLRSaECusBVNfQnjnjsR9yVO+D"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBjndGdENR43i/ST/rbvZcsxtfpNcFXiSAZFSaexPrz5loQH6VWH/Uk66Dn1WbVz68CJtAOP8FA8pveR4aEXjMm4kEYY2kdavv/6GG0jrV+ACAIYSMJzlQAABNoDijQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422999,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEAj7bOoen74MVlAhEEUKoiKns8EnMpFgfQz7kI96J4SpsVT5LRDY0eZIwrGdnQHvUwoJlHRIc2dOyYZwkPDS88MuF/4XTUBoQY53RnRDUeN4v0k/6272XLMbX6TXBV4kgGRUmnsT68+ZaEB+lVh/1JOug59Vm1c+vAibQDj/BQPKb3keGhF4zJuJBGGNpHWr7/+hhtI61fgAgCGEjCc5UAAAX9nIX4="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
  "id": -576460752303422999,
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
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "event": "shutdown"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEAj7bOoen74MVlAhEEUKoiKns8EnMpFgfQz7kI96J4SpsVT5LRDY0eZIwrGdnQHvUwoJlHRIc2dOyYZwkPDS88MuF/4XTUBoQY53RnRDUeN4v0k/6272XLMbX6TXBV4kgGRUmnsT68+ZaEB+lVh/1JOug59Vm1c+vAibQDj/BQPKb3keGhF4zJuJBGGNpHWr7/+hhtI61fgAgCGEjCc5UAAAX9nIX4=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422998,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEAj7bOoen74MVlAhEEUKoiKns8EnMpFgfQz7kI96J4SpsVT5LRDY0eZIwrGdnQHvUwoJlHRIc2dOyYZwkPDS88MuECrWSFThn5MDAlV6rw0EWcR+kj2tw1M5KL/ggmYtCeGaNKrAYUbusIpZmVZuqeuCgPDUTOF7oQ6r7CO51v12SYIuF/4XTUBoQY53RnRDUeN4v0k/6272XLMbX6TXBV4kgGRUmnsT68+ZaEB+lVh/1JOug59Vm1c+vAibQDj/BQPKb3keGhF4zJuJBGGNpHWr7/+hhtI61fgAgCGEjCc5UAAARoXxzs="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
  "id": -576460752303422998,
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
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAj7bOoen74MVlAhEEUKoiKns8EnMpFgfQz7kI96J4SpsVT5LRDY0eZIwrGdnQHvUwoJlHRIc2dOyYZwkPDS88MuECrWSFThn5MDAlV6rw0EWcR+kj2tw1M5KL/ggmYtCeGaNKrAYUbusIpZmVZuqeuCgPDUTOF7oQ6r7CO51v12SYIuF/4XTUBoQY53RnRDUeN4v0k/6272XLMbX6TXBV4kgGRUmnsT68+ZaEB+lVh/1JOug59Vm1c+vAibQDj/BQPKb3keGhF4zJuJBGGNpHWr7/+hhtI61fgAgCGEjCc5UAAARoXxzs=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "event": "closing"
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
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAj7bOoen74MVlAhEEUKoiKns8EnMpFgfQz7kI96J4SpsVT5LRDY0eZIwrGdnQHvUwoJlHRIc2dOyYZwkPDS88MuECrWSFThn5MDAlV6rw0EWcR+kj2tw1M5KL/ggmYtCeGaNKrAYUbusIpZmVZuqeuCgPDUTOF7oQ6r7CO51v12SYIuF/4XTUBoQY53RnRDUeN4v0k/6272XLMbX6TXBV4kgGRUmnsT68+ZaEB+lVh/1JOug59Vm1c+vAibQDj/BQPKb3keGhF4zJuJBGGNpHWr7/+hhtI61fgAgCGEjCc5UAAARoXxzs=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "event": "closing"
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
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAj7bOoen74MVlAhEEUKoiKns8EnMpFgfQz7kI96J4SpsVT5LRDY0eZIwrGdnQHvUwoJlHRIc2dOyYZwkPDS88MuECrWSFThn5MDAlV6rw0EWcR+kj2tw1M5KL/ggmYtCeGaNKrAYUbusIpZmVZuqeuCgPDUTOF7oQ6r7CO51v12SYIuF/4XTUBoQY53RnRDUeN4v0k/6272XLMbX6TXBV4kgGRUmnsT68+ZaEB+lVh/1JOug59Vm1c+vAibQDj/BQPKb3keGhF4zJuJBGGNpHWr7/+hhtI61fgAgCGEjCc5UAAARoXxzs=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAj7bOoen74MVlAhEEUKoiKns8EnMpFgfQz7kI96J4SpsVT5LRDY0eZIwrGdnQHvUwoJlHRIc2dOyYZwkPDS88MuECrWSFThn5MDAlV6rw0EWcR+kj2tw1M5KL/ggmYtCeGaNKrAYUbusIpZmVZuqeuCgPDUTOF7oQ6r7CO51v12SYIuF/4XTUBoQY53RnRDUeN4v0k/6272XLMbX6TXBV4kgGRUmnsT68+ZaEB+lVh/1JOug59Vm1c+vAibQDj/BQPKb3keGhF4zJuJBGGNpHWr7/+hhtI61fgAgCGEjCc5UAAARoXxzs=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "event": "closed_confirmed"
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
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "event": "died"
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
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "event": "closed_confirmed"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_SV3twECQLHHQBNYt93LdGxhz6UVa9FSVriVT1FS9vRUMvXyBq",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection
