
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd&keep_running=false&lock_period=10&port=12524&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB&role=initiator
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
      "fsm_id": "ba_ZNu6g8JFn+Rw+TeWq4PnVv3Hk0z+omNnu5lmmmoJ4sYicfsy"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd&keep_running=false&lock_period=10&port=12524&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB&role=responder
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
      "fsm_id": "ba_OMMoB1N57jRwfxgi+jnzk/w7yPg1aUb2sNAGsb2OjFnx5BHK"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAVg+nzQh/goxvi/KYoh3Frht8p9SY3dI/sVmm5G4N9FLhj+qJSJgAKEBWF0bh5Dwq9KFV4hyWlLtXEa+rfdrUpntbxwSjGPRARqGJGE5yoAAAgoAhhAGeddIAMCgjAZJZMpcnn/ubEYu9e0Frelqduae/xVwvciJufrZXpcAlv9m5A==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421189,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+NQLAcC4z/jNUQGhAVg+nzQh/goxvi/KYoh3Frht8p9SY3dI/sVmm5G4N9FLiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQFYPp80If4KMb4vymKIdxa4bfKfUmN3SP7FZpuRuDfRS4Y/qiUiYAChAVhdG4eQ8KvShVeIclpS7VxGvq33a1KZ7W8cEoxj0QEahiRhOcqAAAIKAIYQBnnXSADAoIwGSWTKXJ5/7mxGLvXtBa3panbmnv8VcL3Iibn62V6XAJNjduw="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421189,
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_OMMoB1N57jRwfxgi+jnzk/w7yPg1aUb2sNAGsb2OjFnx5BHK"
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "signed_tx": "tx_+NQLAcC4z/jNUQGhAVg+nzQh/goxvi/KYoh3Frht8p9SY3dI/sVmm5G4N9FLiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQFYPp80If4KMb4vymKIdxa4bfKfUmN3SP7FZpuRuDfRS4Y/qiUiYAChAVhdG4eQ8KvShVeIclpS7VxGvq33a1KZ7W8cEoxj0QEahiRhOcqAAAIKAIYQBnnXSADAoIwGSWTKXJ5/7mxGLvXtBa3panbmnv8VcL3Iibn62V6XAJNjduw=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421188,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEiCwHAuQEc+QEZUQGhAVhdG4eQ8KvShVeIclpS7VxGvq33a1KZ7W8cEoxj0QEaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQFYPp80If4KMb4vymKIdxa4bfKfUmN3SP7FZpuRuDfRS4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBWD6fNCH+CjG+L8piiHcWuG3yn1Jjd0j+xWabkbg30UuGP6olImAAoQFYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGoYkYTnKgAACCgCGEAZ510gAwKCMBklkylyef+5sRi717QWt6Wp25p7/FXC9yIm5+tlelwBxjDU3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421188,
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEiCwHAuQEc+QEZUQGhAVhdG4eQ8KvShVeIclpS7VxGvq33a1KZ7W8cEoxj0QEaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQFYPp80If4KMb4vymKIdxa4bfKfUmN3SP7FZpuRuDfRS4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBWD6fNCH+CjG+L8piiHcWuG3yn1Jjd0j+xWabkbg30UuGP6olImAAoQFYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGoYkYTnKgAACCgCGEAZ510gAwKCMBklkylyef+5sRi717QWt6Wp25p7/FXC9yIm5+tlelwBxjDU3",
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_ZNu6g8JFn+Rw+TeWq4PnVv3Hk0z+omNnu5lmmmoJ4sYicfsy"
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEiCwHAuQEc+QEZUQGhAVhdG4eQ8KvShVeIclpS7VxGvq33a1KZ7W8cEoxj0QEaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQFYPp80If4KMb4vymKIdxa4bfKfUmN3SP7FZpuRuDfRS4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBWD6fNCH+CjG+L8piiHcWuG3yn1Jjd0j+xWabkbg30UuGP6olImAAoQFYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGoYkYTnKgAACCgCGEAZ510gAwKCMBklkylyef+5sRi717QWt6Wp25p7/FXC9yIm5+tlelwBxjDU3",
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEiCwHAuQEc+QEZUQGhAVhdG4eQ8KvShVeIclpS7VxGvq33a1KZ7W8cEoxj0QEaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQFYPp80If4KMb4vymKIdxa4bfKfUmN3SP7FZpuRuDfRS4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBWD6fNCH+CjG+L8piiHcWuG3yn1Jjd0j+xWabkbg30UuGP6olImAAoQFYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGoYkYTnKgAACCgCGEAZ510gAwKCMBklkylyef+5sRi717QWt6Wp25p7/FXC9yIm5+tlelwBxjDU3",
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEiCwHAuQEc+QEZUQGhAVhdG4eQ8KvShVeIclpS7VxGvq33a1KZ7W8cEoxj0QEaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQFYPp80If4KMb4vymKIdxa4bfKfUmN3SP7FZpuRuDfRS4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBWD6fNCH+CjG+L8piiHcWuG3yn1Jjd0j+xWabkbg30UuGP6olImAAoQFYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGoYkYTnKgAACCgCGEAZ510gAwKCMBklkylyef+5sRi717QWt6Wp25p7/FXC9yIm5+tlelwBxjDU3",
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
    "to": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "message": {
        "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
        "from": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
        "info": "Hello",
        "to": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
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
    "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "message": {
        "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
        "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
        "info": "Hello back",
        "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421187,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
      "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421187,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
      "balance": 69999999999999
    },
    {
      "account": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "event": "funding_locked"
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "state": "tx_+QEiCwHAuQEc+QEZUQGhAVhdG4eQ8KvShVeIclpS7VxGvq33a1KZ7W8cEoxj0QEaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQFYPp80If4KMb4vymKIdxa4bfKfUmN3SP7FZpuRuDfRS4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBWD6fNCH+CjG+L8piiHcWuG3yn1Jjd0j+xWabkbg30UuGP6olImAAoQFYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGoYkYTnKgAACCgCGEAZ510gAwKCMBklkylyef+5sRi717QWt6Wp25p7/FXC9yIm5+tlelwBxjDU3"
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Channel is `open` and ready to use

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "state": "tx_+QEiCwHAuQEc+QEZUQGhAVhdG4eQ8KvShVeIclpS7VxGvq33a1KZ7W8cEoxj0QEaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQFYPp80If4KMb4vymKIdxa4bfKfUmN3SP7FZpuRuDfRS4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBWD6fNCH+CjG+L8piiHcWuG3yn1Jjd0j+xWabkbg30UuGP6olImAAoQFYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGoYkYTnKgAACCgCGEAZ510gAwKCMBklkylyef+5sRi717QWt6Wp25p7/FXC9yIm5+tlelwBxjDU3"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421186,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
      "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421186,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
      "balance": 69999999999999
    },
    {
      "account": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
    "to": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
        "to": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "from": "ABCDEF",
    "to": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "from": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
        "to": "ABCDEF"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "from": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
    "meta": 17,
    "to": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
        "meta": 17,
        "to": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "from": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
    "to": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlyXMuxNULcih+dsw5pLl6amWvWc51vhMGkDsGhtsd3QAqDfZwQcZoSuZBLHVRJFyb3cgbSlepMKahC5PShfYvuypnltj4w=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
          "op": "OffChainTransfer",
          "to": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421185,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAVg+nzQh/goxvi/KYoh3Frht8p9SY3dI/sVmm5G4N9FLiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZclzLsTVC3IofnbMOaS5emplr1nOdb4TBpA7BobbHd0AKg32cEHGaErmQSx1USRcm93IG0pXqTCmoQuT0oX2L7sqZPlQMI"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421185,
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAVg+nzQh/goxvi/KYoh3Frht8p9SY3dI/sVmm5G4N9FLiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZclzLsTVC3IofnbMOaS5emplr1nOdb4TBpA7BobbHd0AKg32cEHGaErmQSx1USRcm93IG0pXqTCmoQuT0oX2L7sqZPlQMI",
      "updates": [
        {
          "amount": 1,
          "from": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
          "op": "OffChainTransfer",
          "to": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421184,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhAVhdG4eQ8KvShVeIclpS7VxGvq33a1KZ7W8cEoxj0QEaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQFYPp80If4KMb4vymKIdxa4bfKfUmN3SP7FZpuRuDfRS4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGXJcy7E1QtyKH52zDmkuXpqZa9ZznW+EwaQOwaG2x3dACoN9nBBxmhK5kEsdVEkXJvdyBtKV6kwpqELk9KF9i+7Km/ppDkA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421184,
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAVhdG4eQ8KvShVeIclpS7VxGvq33a1KZ7W8cEoxj0QEaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQFYPp80If4KMb4vymKIdxa4bfKfUmN3SP7FZpuRuDfRS4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGXJcy7E1QtyKH52zDmkuXpqZa9ZznW+EwaQOwaG2x3dACoN9nBBxmhK5kEsdVEkXJvdyBtKV6kwpqELk9KF9i+7Km/ppDkA=="
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAVhdG4eQ8KvShVeIclpS7VxGvq33a1KZ7W8cEoxj0QEaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQFYPp80If4KMb4vymKIdxa4bfKfUmN3SP7FZpuRuDfRS4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGXJcy7E1QtyKH52zDmkuXpqZa9ZznW+EwaQOwaG2x3dACoN9nBBxmhK5kEsdVEkXJvdyBtKV6kwpqELk9KF9i+7Km/ppDkA=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421183,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
      "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421183,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
      "balance": 69999999999998
    },
    {
      "account": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421182,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421182,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhAVhdG4eQ8KvShVeIclpS7VxGvq33a1KZ7W8cEoxj0QEaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQFYPp80If4KMb4vymKIdxa4bfKfUmN3SP7FZpuRuDfRS4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGXJcy7E1QtyKH52zDmkuXpqZa9ZznW+EwaQOwaG2x3dACoN9nBBxmhK5kEsdVEkXJvdyBtKV6kwpqELk9KF9i+7Km/ppDkA==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaBYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGovKCgEAhiRhOcqAArDvQAGgWD6fNCH+CjG+L8piiHcWuG3yn1Jjd0j+xWabkbg30UuLygoBAIY/qiUiX/6NLN/U"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421181,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
      "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421181,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
      "balance": 40000000000002
    },
    {
      "account": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
      "balance": 69999999999998
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
    "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
        "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
        "to": "ABCDEF"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
    "meta": 17,
    "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
        "meta": 17,
        "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
    "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlyXMuxNULcih+dsw5pLl6amWvWc51vhMGkDsGhtsd3QA6CMBklkylyef+5sRi717QWt6Wp25p7/FXC9yIm5+tlelxIRvuw=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
          "op": "OffChainTransfer",
          "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421180,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAVhdG4eQ8KvShVeIclpS7VxGvq33a1KZ7W8cEoxj0QEaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZclzLsTVC3IofnbMOaS5emplr1nOdb4TBpA7BobbHd0AOgjAZJZMpcnn/ubEYu9e0Frelqduae/xVwvciJufrZXpflLt5H"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421180,
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAVhdG4eQ8KvShVeIclpS7VxGvq33a1KZ7W8cEoxj0QEaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZclzLsTVC3IofnbMOaS5emplr1nOdb4TBpA7BobbHd0AOgjAZJZMpcnn/ubEYu9e0Frelqduae/xVwvciJufrZXpflLt5H",
      "updates": [
        {
          "amount": 1,
          "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
          "op": "OffChainTransfer",
          "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421179,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhAVg+nzQh/goxvi/KYoh3Frht8p9SY3dI/sVmm5G4N9FLiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQFYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGXJcy7E1QtyKH52zDmkuXpqZa9ZznW+EwaQOwaG2x3dADoIwGSWTKXJ5/7mxGLvXtBa3panbmnv8VcL3Iibn62V6XpQW2lA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421179,
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAVg+nzQh/goxvi/KYoh3Frht8p9SY3dI/sVmm5G4N9FLiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQFYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGXJcy7E1QtyKH52zDmkuXpqZa9ZznW+EwaQOwaG2x3dADoIwGSWTKXJ5/7mxGLvXtBa3panbmnv8VcL3Iibn62V6XpQW2lA=="
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAVg+nzQh/goxvi/KYoh3Frht8p9SY3dI/sVmm5G4N9FLiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQFYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGXJcy7E1QtyKH52zDmkuXpqZa9ZznW+EwaQOwaG2x3dADoIwGSWTKXJ5/7mxGLvXtBa3panbmnv8VcL3Iibn62V6XpQW2lA=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421178,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
      "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421178,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
      "balance": 40000000000001
    },
    {
      "account": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421177,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421177,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhAVg+nzQh/goxvi/KYoh3Frht8p9SY3dI/sVmm5G4N9FLiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQFYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGXJcy7E1QtyKH52zDmkuXpqZa9ZznW+EwaQOwaG2x3dADoIwGSWTKXJ5/7mxGLvXtBa3panbmnv8VcL3Iibn62V6XpQW2lA==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaBYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGovKCgEAhiRhOcqAAbDvQAGgWD6fNCH+CjG+L8piiHcWuG3yn1Jjd0j+xWabkbg30UuLygoBAIY/qiUiX//ltBjH"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421176,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
      "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421176,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
      "balance": 40000000000001
    },
    {
      "account": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
    "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
        "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
        "to": "ABCDEF"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
    "meta": 17,
    "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
        "meta": 17,
        "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
    "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlyXMuxNULcih+dsw5pLl6amWvWc51vhMGkDsGhtsd3QBKBc5RtXGOE5XlD6HD3wMkMNKF2Wk9psygwa3X+KwUR90IvTf+E=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
          "op": "OffChainTransfer",
          "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421175,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAVhdG4eQ8KvShVeIclpS7VxGvq33a1KZ7W8cEoxj0QEaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZclzLsTVC3IofnbMOaS5emplr1nOdb4TBpA7BobbHd0ASgXOUbVxjhOV5Q+hw98DJDDShdlpPabMoMGt1/isFEfdB02Urh"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421175,
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAVhdG4eQ8KvShVeIclpS7VxGvq33a1KZ7W8cEoxj0QEaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZclzLsTVC3IofnbMOaS5emplr1nOdb4TBpA7BobbHd0ASgXOUbVxjhOV5Q+hw98DJDDShdlpPabMoMGt1/isFEfdB02Urh",
      "updates": [
        {
          "amount": 1,
          "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
          "op": "OffChainTransfer",
          "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421174,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhAVg+nzQh/goxvi/KYoh3Frht8p9SY3dI/sVmm5G4N9FLiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQFYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGXJcy7E1QtyKH52zDmkuXpqZa9ZznW+EwaQOwaG2x3dAEoFzlG1cY4TleUPocPfAyQw0oXZaT2mzKDBrdf4rBRH3QySYyFg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421174,
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAVg+nzQh/goxvi/KYoh3Frht8p9SY3dI/sVmm5G4N9FLiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQFYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGXJcy7E1QtyKH52zDmkuXpqZa9ZznW+EwaQOwaG2x3dAEoFzlG1cY4TleUPocPfAyQw0oXZaT2mzKDBrdf4rBRH3QySYyFg=="
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAVg+nzQh/goxvi/KYoh3Frht8p9SY3dI/sVmm5G4N9FLiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQFYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGXJcy7E1QtyKH52zDmkuXpqZa9ZznW+EwaQOwaG2x3dAEoFzlG1cY4TleUPocPfAyQw0oXZaT2mzKDBrdf4rBRH3QySYyFg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421173,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
      "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421173,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
      "balance": 40000000000000
    },
    {
      "account": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421172,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421172,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhAVg+nzQh/goxvi/KYoh3Frht8p9SY3dI/sVmm5G4N9FLiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQFYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGXJcy7E1QtyKH52zDmkuXpqZa9ZznW+EwaQOwaG2x3dAEoFzlG1cY4TleUPocPfAyQw0oXZaT2mzKDBrdf4rBRH3QySYyFg==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaBYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGovKCgEAhiRhOcqAALDvQAGgWD6fNCH+CjG+L8piiHcWuG3yn1Jjd0j+xWabkbg30UuLygoBAIY/qiUiYAC8S6oW"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421171,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
      "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421171,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
      "balance": 70000000000000
    },
    {
      "account": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
      "balance": 40000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
    "to": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
        "to": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "from": "ABCDEF",
    "to": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "from": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
        "to": "ABCDEF"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "from": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
    "meta": 17,
    "to": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
        "meta": 17,
        "to": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "from": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
    "to": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlyXMuxNULcih+dsw5pLl6amWvWc51vhMGkDsGhtsd3QBaCMBklkylyef+5sRi717QWt6Wp25p7/FXC9yIm5+tlel2S7USk=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
          "op": "OffChainTransfer",
          "to": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421170,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAVg+nzQh/goxvi/KYoh3Frht8p9SY3dI/sVmm5G4N9FLiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZclzLsTVC3IofnbMOaS5emplr1nOdb4TBpA7BobbHd0AWgjAZJZMpcnn/ubEYu9e0Frelqduae/xVwvciJufrZXpcSrvxg"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421170,
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAVg+nzQh/goxvi/KYoh3Frht8p9SY3dI/sVmm5G4N9FLiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZclzLsTVC3IofnbMOaS5emplr1nOdb4TBpA7BobbHd0AWgjAZJZMpcnn/ubEYu9e0Frelqduae/xVwvciJufrZXpcSrvxg",
      "updates": [
        {
          "amount": 1,
          "from": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
          "op": "OffChainTransfer",
          "to": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421169,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhAVhdG4eQ8KvShVeIclpS7VxGvq33a1KZ7W8cEoxj0QEaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQFYPp80If4KMb4vymKIdxa4bfKfUmN3SP7FZpuRuDfRS4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGXJcy7E1QtyKH52zDmkuXpqZa9ZznW+EwaQOwaG2x3dAFoIwGSWTKXJ5/7mxGLvXtBa3panbmnv8VcL3Iibn62V6XcwyODg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421169,
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAVhdG4eQ8KvShVeIclpS7VxGvq33a1KZ7W8cEoxj0QEaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQFYPp80If4KMb4vymKIdxa4bfKfUmN3SP7FZpuRuDfRS4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGXJcy7E1QtyKH52zDmkuXpqZa9ZznW+EwaQOwaG2x3dAFoIwGSWTKXJ5/7mxGLvXtBa3panbmnv8VcL3Iibn62V6XcwyODg=="
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAVhdG4eQ8KvShVeIclpS7VxGvq33a1KZ7W8cEoxj0QEaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQFYPp80If4KMb4vymKIdxa4bfKfUmN3SP7FZpuRuDfRS4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGXJcy7E1QtyKH52zDmkuXpqZa9ZznW+EwaQOwaG2x3dAFoIwGSWTKXJ5/7mxGLvXtBa3panbmnv8VcL3Iibn62V6XcwyODg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421168,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
      "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421168,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
      "balance": 69999999999999
    },
    {
      "account": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421167,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421167,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhAVhdG4eQ8KvShVeIclpS7VxGvq33a1KZ7W8cEoxj0QEaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQFYPp80If4KMb4vymKIdxa4bfKfUmN3SP7FZpuRuDfRS4krEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGXJcy7E1QtyKH52zDmkuXpqZa9ZznW+EwaQOwaG2x3dAFoIwGSWTKXJ5/7mxGLvXtBa3panbmnv8VcL3Iibn62V6XcwyODg==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaBYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGovKCgEAhiRhOcqAAbDvQAGgWD6fNCH+CjG+L8piiHcWuG3yn1Jjd0j+xWabkbg30UuLygoBAIY/qiUiX//ltBjH"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421166,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
      "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421166,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
      "balance": 40000000000001
    },
    {
      "account": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
    "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
        "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
        "to": "ABCDEF"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
    "meta": 17,
    "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
        "meta": 17,
        "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
    "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlyXMuxNULcih+dsw5pLl6amWvWc51vhMGkDsGhtsd3QBqBc5RtXGOE5XlD6HD3wMkMNKF2Wk9psygwa3X+KwUR90LuRw0A=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
          "op": "OffChainTransfer",
          "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421165,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAVhdG4eQ8KvShVeIclpS7VxGvq33a1KZ7W8cEoxj0QEaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZclzLsTVC3IofnbMOaS5emplr1nOdb4TBpA7BobbHd0AagXOUbVxjhOV5Q+hw98DJDDShdlpPabMoMGt1/isFEfdAqSHU/"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421165,
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAVhdG4eQ8KvShVeIclpS7VxGvq33a1KZ7W8cEoxj0QEaiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZclzLsTVC3IofnbMOaS5emplr1nOdb4TBpA7BobbHd0AagXOUbVxjhOV5Q+hw98DJDDShdlpPabMoMGt1/isFEfdAqSHU/",
      "updates": [
        {
          "amount": 1,
          "from": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
          "op": "OffChainTransfer",
          "to": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421164,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhAVg+nzQh/goxvi/KYoh3Frht8p9SY3dI/sVmm5G4N9FLiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQFYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGXJcy7E1QtyKH52zDmkuXpqZa9ZznW+EwaQOwaG2x3dAGoFzlG1cY4TleUPocPfAyQw0oXZaT2mzKDBrdf4rBRH3Q9gkiBQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421164,
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAVg+nzQh/goxvi/KYoh3Frht8p9SY3dI/sVmm5G4N9FLiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQFYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGXJcy7E1QtyKH52zDmkuXpqZa9ZznW+EwaQOwaG2x3dAGoFzlG1cY4TleUPocPfAyQw0oXZaT2mzKDBrdf4rBRH3Q9gkiBQ=="
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAVg+nzQh/goxvi/KYoh3Frht8p9SY3dI/sVmm5G4N9FLiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQFYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGXJcy7E1QtyKH52zDmkuXpqZa9ZznW+EwaQOwaG2x3dAGoFzlG1cY4TleUPocPfAyQw0oXZaT2mzKDBrdf4rBRH3Q9gkiBQ=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421163,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
      "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421163,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_fv8fZjtbf8fxH8B1iqY4RxkLZ8JTjjrRCVEGGv3Y4W5TjnwHB",
      "balance": 40000000000000
    },
    {
      "account": "ak_fs6EmGDYByfXmnC7AUn6Lsoy3grUecciXbEFWjmqQuzb7CRVd",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421162,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421162,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhAVg+nzQh/goxvi/KYoh3Frht8p9SY3dI/sVmm5G4N9FLiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQFYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGokrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGXJcy7E1QtyKH52zDmkuXpqZa9ZznW+EwaQOwaG2x3dAGoFzlG1cY4TleUPocPfAyQw0oXZaT2mzKDBrdf4rBRH3Q9gkiBQ==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaBYXRuHkPCr0oVXiHJaUu1cRr6t92tSme1vHBKMY9EBGovKCgEAhiRhOcqAALDvQAGgWD6fNCH+CjG+L8piiHcWuG3yn1Jjd0j+xWabkbg30UuLygoBAIY/qiUiYAC8S6oW"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421161,
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
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421161,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421160,
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
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
    "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
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
  "channel_id": "ch_hn6yxSrNoLqHnyB2PnmEcchbJsuoi1f7qwma4t8RKbBRaWDaH",
  "id": -576460752303421160,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
