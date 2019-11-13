
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_a1oMS2x8NiLCHTHCPye3ypP7wz4wKG6G1K3DTZPEtaXDX1aGX&keep_running=false&lock_period=10&port=13216&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_m1btDGXGo6QZRmeNBhyJJymaRh51aCuq5hwcFYTD9VB1x9kph&role=initiator
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
      "fsm_id": "ba_a6iA8Q6DgrUQ8ck/akPMWGxBcWXhfsmXDYI4balBlfW2IRhl"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_a1oMS2x8NiLCHTHCPye3ypP7wz4wKG6G1K3DTZPEtaXDX1aGX&keep_running=false&lock_period=10&port=13216&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_m1btDGXGo6QZRmeNBhyJJymaRh51aCuq5hwcFYTD9VB1x9kph&role=responder
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
      "fsm_id": "ba_gB37sl/RRosKawyW3F8/kUdZH0CsdNy6dyKE4VqUQaciVoYD"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAUr2OhP/8lOgqmEcT7hZY1CL40uDLzmMOfUOLb/eHvjghj+qJSJgAKEBY+5RSYaWB89hm3QGPHnLjZBBjYxX/rZ6AcTM1QLPzMyGJGE5yoAAAgoAhhAGeddIAMCgYBLB2I8kubm08zPK3UWUeVBr337ilkRnORyOL0+lfjYB/qzi8A==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422742,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDebGidEfdZ6nolzuwYCjolNTMP2UTCjguYD8KST3IgEw7ileEp4EFuoWBFKhMyh0CR9GnqssqdrspNeeaBel4OuIP4gTIBoQFK9joT//JToKphHE+4WWNQi+NLgy85jDn1Di2/3h744IY/qiUiYAChAWPuUUmGlgfPYZt0Bjx5y42QQY2MV/62egHEzNUCz8zMhiRhOcqAAAIKAIYQBnnXSADAoGASwdiPJLm5tPMzyt1FlHlQa99+4pZEZzkcji9PpX42AQBLYkg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422742,
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
      "signed_tx": "tx_+MsLAfhCuEDebGidEfdZ6nolzuwYCjolNTMP2UTCjguYD8KST3IgEw7ileEp4EFuoWBFKhMyh0CR9GnqssqdrspNeeaBel4OuIP4gTIBoQFK9joT//JToKphHE+4WWNQi+NLgy85jDn1Di2/3h744IY/qiUiYAChAWPuUUmGlgfPYZt0Bjx5y42QQY2MV/62egHEzNUCz8zMhiRhOcqAAAIKAIYQBnnXSADAoGASwdiPJLm5tPMzyt1FlHlQa99+4pZEZzkcji9PpX42AQBLYkg=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422741,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAko8U5e5lZZFq6VAXByBFZqWiLnKvbrBQA/REsFJCHlOyoUJIkPd+CKauaelahoqodkxc9qS9C42afMwgvCFGAbhA3mxonRH3Wep6Jc7sGAo6JTUzD9lEwo4LmA/Ckk9yIBMO4pXhKeBBbqFgRSoTModAkfRp6rLKna7KTXnmgXpeDriD+IEyAaEBSvY6E//yU6CqYRxPuFljUIvjS4MvOYw59Q4tv94e+OCGP6olImAAoQFj7lFJhpYHz2GbdAY8ecuNkEGNjFf+tnoBxMzVAs/MzIYkYTnKgAACCgCGEAZ510gAwKBgEsHYjyS5ubTzM8rdRZR5UGvffuKWRGc5HI4vT6V+NgFT6/bp"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422741,
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
    "channel_id": "ch_2k968MKEmTDtzGH23s5bCC5nBMwPBZEMKQJcyiviLFQnkitKJs",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAko8U5e5lZZFq6VAXByBFZqWiLnKvbrBQA/REsFJCHlOyoUJIkPd+CKauaelahoqodkxc9qS9C42afMwgvCFGAbhA3mxonRH3Wep6Jc7sGAo6JTUzD9lEwo4LmA/Ckk9yIBMO4pXhKeBBbqFgRSoTModAkfRp6rLKna7KTXnmgXpeDriD+IEyAaEBSvY6E//yU6CqYRxPuFljUIvjS4MvOYw59Q4tv94e+OCGP6olImAAoQFj7lFJhpYHz2GbdAY8ecuNkEGNjFf+tnoBxMzVAs/MzIYkYTnKgAACCgCGEAZ510gAwKBgEsHYjyS5ubTzM8rdRZR5UGvffuKWRGc5HI4vT6V+NgFT6/bp",
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
    "channel_id": "ch_2k968MKEmTDtzGH23s5bCC5nBMwPBZEMKQJcyiviLFQnkitKJs",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAko8U5e5lZZFq6VAXByBFZqWiLnKvbrBQA/REsFJCHlOyoUJIkPd+CKauaelahoqodkxc9qS9C42afMwgvCFGAbhA3mxonRH3Wep6Jc7sGAo6JTUzD9lEwo4LmA/Ckk9yIBMO4pXhKeBBbqFgRSoTModAkfRp6rLKna7KTXnmgXpeDriD+IEyAaEBSvY6E//yU6CqYRxPuFljUIvjS4MvOYw59Q4tv94e+OCGP6olImAAoQFj7lFJhpYHz2GbdAY8ecuNkEGNjFf+tnoBxMzVAs/MzIYkYTnKgAACCgCGEAZ510gAwKBgEsHYjyS5ubTzM8rdRZR5UGvffuKWRGc5HI4vT6V+NgFT6/bp",
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
    "channel_id": "ch_2k968MKEmTDtzGH23s5bCC5nBMwPBZEMKQJcyiviLFQnkitKJs",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAko8U5e5lZZFq6VAXByBFZqWiLnKvbrBQA/REsFJCHlOyoUJIkPd+CKauaelahoqodkxc9qS9C42afMwgvCFGAbhA3mxonRH3Wep6Jc7sGAo6JTUzD9lEwo4LmA/Ckk9yIBMO4pXhKeBBbqFgRSoTModAkfRp6rLKna7KTXnmgXpeDriD+IEyAaEBSvY6E//yU6CqYRxPuFljUIvjS4MvOYw59Q4tv94e+OCGP6olImAAoQFj7lFJhpYHz2GbdAY8ecuNkEGNjFf+tnoBxMzVAs/MzIYkYTnKgAACCgCGEAZ510gAwKBgEsHYjyS5ubTzM8rdRZR5UGvffuKWRGc5HI4vT6V+NgFT6/bp",
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
    "channel_id": "ch_2k968MKEmTDtzGH23s5bCC5nBMwPBZEMKQJcyiviLFQnkitKJs",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAko8U5e5lZZFq6VAXByBFZqWiLnKvbrBQA/REsFJCHlOyoUJIkPd+CKauaelahoqodkxc9qS9C42afMwgvCFGAbhA3mxonRH3Wep6Jc7sGAo6JTUzD9lEwo4LmA/Ckk9yIBMO4pXhKeBBbqFgRSoTModAkfRp6rLKna7KTXnmgXpeDriD+IEyAaEBSvY6E//yU6CqYRxPuFljUIvjS4MvOYw59Q4tv94e+OCGP6olImAAoQFj7lFJhpYHz2GbdAY8ecuNkEGNjFf+tnoBxMzVAs/MzIYkYTnKgAACCgCGEAZ510gAwKBgEsHYjyS5ubTzM8rdRZR5UGvffuKWRGc5HI4vT6V+NgFT6/bp",
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
    "to": "ak_m1btDGXGo6QZRmeNBhyJJymaRh51aCuq5hwcFYTD9VB1x9kph"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2k968MKEmTDtzGH23s5bCC5nBMwPBZEMKQJcyiviLFQnkitKJs",
    "data": {
      "message": {
        "channel_id": "ch_2k968MKEmTDtzGH23s5bCC5nBMwPBZEMKQJcyiviLFQnkitKJs",
        "from": "ak_a1oMS2x8NiLCHTHCPye3ypP7wz4wKG6G1K3DTZPEtaXDX1aGX",
        "info": "Hello",
        "to": "ak_m1btDGXGo6QZRmeNBhyJJymaRh51aCuq5hwcFYTD9VB1x9kph"
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
    "to": "ak_a1oMS2x8NiLCHTHCPye3ypP7wz4wKG6G1K3DTZPEtaXDX1aGX"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2k968MKEmTDtzGH23s5bCC5nBMwPBZEMKQJcyiviLFQnkitKJs",
    "data": {
      "message": {
        "channel_id": "ch_2k968MKEmTDtzGH23s5bCC5nBMwPBZEMKQJcyiviLFQnkitKJs",
        "from": "ak_m1btDGXGo6QZRmeNBhyJJymaRh51aCuq5hwcFYTD9VB1x9kph",
        "info": "Hello back",
        "to": "ak_a1oMS2x8NiLCHTHCPye3ypP7wz4wKG6G1K3DTZPEtaXDX1aGX"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422740,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_a1oMS2x8NiLCHTHCPye3ypP7wz4wKG6G1K3DTZPEtaXDX1aGX",
      "ak_m1btDGXGo6QZRmeNBhyJJymaRh51aCuq5hwcFYTD9VB1x9kph"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2k968MKEmTDtzGH23s5bCC5nBMwPBZEMKQJcyiviLFQnkitKJs",
  "id": -576460752303422740,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_a1oMS2x8NiLCHTHCPye3ypP7wz4wKG6G1K3DTZPEtaXDX1aGX",
      "balance": 69999999999999
    },
    {
      "account": "ak_m1btDGXGo6QZRmeNBhyJJymaRh51aCuq5hwcFYTD9VB1x9kph",
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
    "channel_id": "ch_2k968MKEmTDtzGH23s5bCC5nBMwPBZEMKQJcyiviLFQnkitKJs",
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
    "channel_id": "ch_2k968MKEmTDtzGH23s5bCC5nBMwPBZEMKQJcyiviLFQnkitKJs",
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
    "channel_id": "ch_2k968MKEmTDtzGH23s5bCC5nBMwPBZEMKQJcyiviLFQnkitKJs",
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
    "channel_id": "ch_2k968MKEmTDtzGH23s5bCC5nBMwPBZEMKQJcyiviLFQnkitKJs",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2k968MKEmTDtzGH23s5bCC5nBMwPBZEMKQJcyiviLFQnkitKJs",
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
    "channel_id": "ch_2k968MKEmTDtzGH23s5bCC5nBMwPBZEMKQJcyiviLFQnkitKJs",
    "data": {
      "state": "tx_+QENCwH4hLhAko8U5e5lZZFq6VAXByBFZqWiLnKvbrBQA/REsFJCHlOyoUJIkPd+CKauaelahoqodkxc9qS9C42afMwgvCFGAbhA3mxonRH3Wep6Jc7sGAo6JTUzD9lEwo4LmA/Ckk9yIBMO4pXhKeBBbqFgRSoTModAkfRp6rLKna7KTXnmgXpeDriD+IEyAaEBSvY6E//yU6CqYRxPuFljUIvjS4MvOYw59Q4tv94e+OCGP6olImAAoQFj7lFJhpYHz2GbdAY8ecuNkEGNjFf+tnoBxMzVAs/MzIYkYTnKgAACCgCGEAZ510gAwKBgEsHYjyS5ubTzM8rdRZR5UGvffuKWRGc5HI4vT6V+NgFT6/bp"
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
    "channel_id": "ch_2k968MKEmTDtzGH23s5bCC5nBMwPBZEMKQJcyiviLFQnkitKJs",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2k968MKEmTDtzGH23s5bCC5nBMwPBZEMKQJcyiviLFQnkitKJs",
    "data": {
      "state": "tx_+QENCwH4hLhAko8U5e5lZZFq6VAXByBFZqWiLnKvbrBQA/REsFJCHlOyoUJIkPd+CKauaelahoqodkxc9qS9C42afMwgvCFGAbhA3mxonRH3Wep6Jc7sGAo6JTUzD9lEwo4LmA/Ckk9yIBMO4pXhKeBBbqFgRSoTModAkfRp6rLKna7KTXnmgXpeDriD+IEyAaEBSvY6E//yU6CqYRxPuFljUIvjS4MvOYw59Q4tv94e+OCGP6olImAAoQFj7lFJhpYHz2GbdAY8ecuNkEGNjFf+tnoBxMzVAs/MzIYkYTnKgAACCgCGEAZ510gAwKBgEsHYjyS5ubTzM8rdRZR5UGvffuKWRGc5HI4vT6V+NgFT6/bp"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_ToTwgaj2gj3ywRxw4SVxdp5yfo1VFPdhmZrxFDvi7TWNDqjFf&keep_running=false&lock_period=10&port=12652&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_xkES7FG88KRnpeEarPxXFLwyf4BLRN25dvmGbLTAvqNadg7C3&role=initiator
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
      "fsm_id": "ba_qqKXsHc2JpoXGjp3qLLVKMbPnbNEqQgfNOIdJzv3Rb1UJn39"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_ToTwgaj2gj3ywRxw4SVxdp5yfo1VFPdhmZrxFDvi7TWNDqjFf&keep_running=false&lock_period=10&port=12652&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_xkES7FG88KRnpeEarPxXFLwyf4BLRN25dvmGbLTAvqNadg7C3&role=responder
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
      "fsm_id": "ba_NB6qAuM9dx9hNvAFLlbr64bVf2NJTLTVx3C2TbrQdeR7iMpH"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhATza7rQmDK8CexwwJlylXzc7XxOvnSl1v+HRAz2zCWnshj+qJSJgAKEBfpOhzOXBmVIVrButCzs24Y4esppgKEsmQunUJKkRHnaGJGE5yoAAAgoAhhAGeddIAMCgDpA3u8cl68ymkHjZmwSh8hwZZ1KjSYnCP0f3YcsRGX4Bak95vg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422095,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAaw+jfgp12s/jZ9gavinToEjVTQhYUF70OkccmU6mvpI6PApUlYQ7xOCRsA4t0u94EJH6bZRghGPVp78Xl5UoGuIP4gTIBoQE82u60JgyvAnscMCZcpV83O18Tr50pdb/h0QM9swlp7IY/qiUiYAChAX6ToczlwZlSFawbrQs7NuGOHrKaYChLJkLp1CSpER52hiRhOcqAAAIKAIYQBnnXSADAoA6QN7vHJevMppB42ZsEofIcGWdSo0mJwj9H92HLERl+Abn/73M="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422095,
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
      "signed_tx": "tx_+MsLAfhCuEAaw+jfgp12s/jZ9gavinToEjVTQhYUF70OkccmU6mvpI6PApUlYQ7xOCRsA4t0u94EJH6bZRghGPVp78Xl5UoGuIP4gTIBoQE82u60JgyvAnscMCZcpV83O18Tr50pdb/h0QM9swlp7IY/qiUiYAChAX6ToczlwZlSFawbrQs7NuGOHrKaYChLJkLp1CSpER52hiRhOcqAAAIKAIYQBnnXSADAoA6QN7vHJevMppB42ZsEofIcGWdSo0mJwj9H92HLERl+Abn/73M=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422094,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAGsPo34KddrP42fYGr4p06BI1U0IWFBe9DpHHJlOpr6SOjwKVJWEO8TgkbAOLdLveBCR+m2UYIRj1ae/F5eVKBrhAL1mRVnwS0jIV6lNB3Pua6GApN0Y7opiHVqEWIEdQ6mf+MQSBGxH8E6bOXqxvW+UaAvgTrjlQD3CoQsz0wrIFCLiD+IEyAaEBPNrutCYMrwJ7HDAmXKVfNztfE6+dKXW/4dEDPbMJaeyGP6olImAAoQF+k6HM5cGZUhWsG60LOzbhjh6ymmAoSyZC6dQkqREedoYkYTnKgAACCgCGEAZ510gAwKAOkDe7xyXrzKaQeNmbBKHyHBlnUqNJicI/R/dhyxEZfgFvTwBj"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422094,
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
    "channel_id": "ch_wLHXJk7VxuAJbhmExzM1vujxJJ92d22TdKmYDVy19XbMuHdEc",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAGsPo34KddrP42fYGr4p06BI1U0IWFBe9DpHHJlOpr6SOjwKVJWEO8TgkbAOLdLveBCR+m2UYIRj1ae/F5eVKBrhAL1mRVnwS0jIV6lNB3Pua6GApN0Y7opiHVqEWIEdQ6mf+MQSBGxH8E6bOXqxvW+UaAvgTrjlQD3CoQsz0wrIFCLiD+IEyAaEBPNrutCYMrwJ7HDAmXKVfNztfE6+dKXW/4dEDPbMJaeyGP6olImAAoQF+k6HM5cGZUhWsG60LOzbhjh6ymmAoSyZC6dQkqREedoYkYTnKgAACCgCGEAZ510gAwKAOkDe7xyXrzKaQeNmbBKHyHBlnUqNJicI/R/dhyxEZfgFvTwBj",
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
    "channel_id": "ch_wLHXJk7VxuAJbhmExzM1vujxJJ92d22TdKmYDVy19XbMuHdEc",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAGsPo34KddrP42fYGr4p06BI1U0IWFBe9DpHHJlOpr6SOjwKVJWEO8TgkbAOLdLveBCR+m2UYIRj1ae/F5eVKBrhAL1mRVnwS0jIV6lNB3Pua6GApN0Y7opiHVqEWIEdQ6mf+MQSBGxH8E6bOXqxvW+UaAvgTrjlQD3CoQsz0wrIFCLiD+IEyAaEBPNrutCYMrwJ7HDAmXKVfNztfE6+dKXW/4dEDPbMJaeyGP6olImAAoQF+k6HM5cGZUhWsG60LOzbhjh6ymmAoSyZC6dQkqREedoYkYTnKgAACCgCGEAZ510gAwKAOkDe7xyXrzKaQeNmbBKHyHBlnUqNJicI/R/dhyxEZfgFvTwBj",
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
    "channel_id": "ch_wLHXJk7VxuAJbhmExzM1vujxJJ92d22TdKmYDVy19XbMuHdEc",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAGsPo34KddrP42fYGr4p06BI1U0IWFBe9DpHHJlOpr6SOjwKVJWEO8TgkbAOLdLveBCR+m2UYIRj1ae/F5eVKBrhAL1mRVnwS0jIV6lNB3Pua6GApN0Y7opiHVqEWIEdQ6mf+MQSBGxH8E6bOXqxvW+UaAvgTrjlQD3CoQsz0wrIFCLiD+IEyAaEBPNrutCYMrwJ7HDAmXKVfNztfE6+dKXW/4dEDPbMJaeyGP6olImAAoQF+k6HM5cGZUhWsG60LOzbhjh6ymmAoSyZC6dQkqREedoYkYTnKgAACCgCGEAZ510gAwKAOkDe7xyXrzKaQeNmbBKHyHBlnUqNJicI/R/dhyxEZfgFvTwBj",
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
    "channel_id": "ch_wLHXJk7VxuAJbhmExzM1vujxJJ92d22TdKmYDVy19XbMuHdEc",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAGsPo34KddrP42fYGr4p06BI1U0IWFBe9DpHHJlOpr6SOjwKVJWEO8TgkbAOLdLveBCR+m2UYIRj1ae/F5eVKBrhAL1mRVnwS0jIV6lNB3Pua6GApN0Y7opiHVqEWIEdQ6mf+MQSBGxH8E6bOXqxvW+UaAvgTrjlQD3CoQsz0wrIFCLiD+IEyAaEBPNrutCYMrwJ7HDAmXKVfNztfE6+dKXW/4dEDPbMJaeyGP6olImAAoQF+k6HM5cGZUhWsG60LOzbhjh6ymmAoSyZC6dQkqREedoYkYTnKgAACCgCGEAZ510gAwKAOkDe7xyXrzKaQeNmbBKHyHBlnUqNJicI/R/dhyxEZfgFvTwBj",
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
    "to": "ak_xkES7FG88KRnpeEarPxXFLwyf4BLRN25dvmGbLTAvqNadg7C3"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_wLHXJk7VxuAJbhmExzM1vujxJJ92d22TdKmYDVy19XbMuHdEc",
    "data": {
      "message": {
        "channel_id": "ch_wLHXJk7VxuAJbhmExzM1vujxJJ92d22TdKmYDVy19XbMuHdEc",
        "from": "ak_ToTwgaj2gj3ywRxw4SVxdp5yfo1VFPdhmZrxFDvi7TWNDqjFf",
        "info": "Hello",
        "to": "ak_xkES7FG88KRnpeEarPxXFLwyf4BLRN25dvmGbLTAvqNadg7C3"
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
    "to": "ak_ToTwgaj2gj3ywRxw4SVxdp5yfo1VFPdhmZrxFDvi7TWNDqjFf"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_wLHXJk7VxuAJbhmExzM1vujxJJ92d22TdKmYDVy19XbMuHdEc",
    "data": {
      "message": {
        "channel_id": "ch_wLHXJk7VxuAJbhmExzM1vujxJJ92d22TdKmYDVy19XbMuHdEc",
        "from": "ak_xkES7FG88KRnpeEarPxXFLwyf4BLRN25dvmGbLTAvqNadg7C3",
        "info": "Hello back",
        "to": "ak_ToTwgaj2gj3ywRxw4SVxdp5yfo1VFPdhmZrxFDvi7TWNDqjFf"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422093,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_ToTwgaj2gj3ywRxw4SVxdp5yfo1VFPdhmZrxFDvi7TWNDqjFf",
      "ak_xkES7FG88KRnpeEarPxXFLwyf4BLRN25dvmGbLTAvqNadg7C3"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_wLHXJk7VxuAJbhmExzM1vujxJJ92d22TdKmYDVy19XbMuHdEc",
  "id": -576460752303422093,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_ToTwgaj2gj3ywRxw4SVxdp5yfo1VFPdhmZrxFDvi7TWNDqjFf",
      "balance": 69999999999999
    },
    {
      "account": "ak_xkES7FG88KRnpeEarPxXFLwyf4BLRN25dvmGbLTAvqNadg7C3",
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
    "channel_id": "ch_wLHXJk7VxuAJbhmExzM1vujxJJ92d22TdKmYDVy19XbMuHdEc",
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
    "channel_id": "ch_wLHXJk7VxuAJbhmExzM1vujxJJ92d22TdKmYDVy19XbMuHdEc",
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
    "channel_id": "ch_wLHXJk7VxuAJbhmExzM1vujxJJ92d22TdKmYDVy19XbMuHdEc",
    "data": {
      "event": "funding_locked"
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
    "channel_id": "ch_wLHXJk7VxuAJbhmExzM1vujxJJ92d22TdKmYDVy19XbMuHdEc",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_wLHXJk7VxuAJbhmExzM1vujxJJ92d22TdKmYDVy19XbMuHdEc",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_wLHXJk7VxuAJbhmExzM1vujxJJ92d22TdKmYDVy19XbMuHdEc",
    "data": {
      "state": "tx_+QENCwH4hLhAGsPo34KddrP42fYGr4p06BI1U0IWFBe9DpHHJlOpr6SOjwKVJWEO8TgkbAOLdLveBCR+m2UYIRj1ae/F5eVKBrhAL1mRVnwS0jIV6lNB3Pua6GApN0Y7opiHVqEWIEdQ6mf+MQSBGxH8E6bOXqxvW+UaAvgTrjlQD3CoQsz0wrIFCLiD+IEyAaEBPNrutCYMrwJ7HDAmXKVfNztfE6+dKXW/4dEDPbMJaeyGP6olImAAoQF+k6HM5cGZUhWsG60LOzbhjh6ymmAoSyZC6dQkqREedoYkYTnKgAACCgCGEAZ510gAwKAOkDe7xyXrzKaQeNmbBKHyHBlnUqNJicI/R/dhyxEZfgFvTwBj"
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
    "channel_id": "ch_wLHXJk7VxuAJbhmExzM1vujxJJ92d22TdKmYDVy19XbMuHdEc",
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
    "channel_id": "ch_wLHXJk7VxuAJbhmExzM1vujxJJ92d22TdKmYDVy19XbMuHdEc",
    "data": {
      "state": "tx_+QENCwH4hLhAGsPo34KddrP42fYGr4p06BI1U0IWFBe9DpHHJlOpr6SOjwKVJWEO8TgkbAOLdLveBCR+m2UYIRj1ae/F5eVKBrhAL1mRVnwS0jIV6lNB3Pua6GApN0Y7opiHVqEWIEdQ6mf+MQSBGxH8E6bOXqxvW+UaAvgTrjlQD3CoQsz0wrIFCLiD+IEyAaEBPNrutCYMrwJ7HDAmXKVfNztfE6+dKXW/4dEDPbMJaeyGP6olImAAoQF+k6HM5cGZUhWsG60LOzbhjh6ymmAoSyZC6dQkqREedoYkYTnKgAACCgCGEAZ510gAwKAOkDe7xyXrzKaQeNmbBKHyHBlnUqNJicI/R/dhyxEZfgFvTwBj"
    }
  },
  "version": 1
}
```
