
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE&keep_running=false&lock_period=10&port=13454&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM&role=initiator
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
      "fsm_id": "ba_wooVEbZ3rpEDvW3gcuaruEchQCi0iljLUZxtrG5mLRPeBwci"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE&keep_running=false&lock_period=10&port=13454&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM&role=responder
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
      "fsm_id": "ba_I7nfyqNP/E2hvlISzH4gdz23IIcxIU0JXkVSqpZe6kzTXRy0"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQhj+qJSJgAKEBpyrgV0ecoGps0o0kkhhMGtn/7pBm4tCeKvbz40nJ6/uGJGE5yoAAAgoAhhAGeddIAMCgapprnYloxKMfgfsyOiCvFXbT+GDAzGPEkPv3x4xkXeYA/MNMGw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422185,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+QFuCwHAuQFo+QFlUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiK+IgLAcC4g/iBMgGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQhj+qJSJgAKEBpyrgV0ecoGps0o0kkhhMGtn/7pBm4tCeKvbz40nJ6/uGJGE5yoAAAgoAhhAGeddIAMCgapprnYloxKMfgfsyOiCvFXbT+GDAzGPEkPv3x4xkXeYADfc+5g=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422185,
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
      "signed_tx": "tx_+QFuCwHAuQFo+QFlUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiK+IgLAcC4g/iBMgGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQhj+qJSJgAKEBpyrgV0ecoGps0o0kkhhMGtn/7pBm4tCeKvbz40nJ6/uGJGE5yoAAAgoAhhAGeddIAMCgapprnYloxKMfgfsyOiCvFXbT+GDAzGPEkPv3x4xkXeYADfc+5g==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422184,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QGxCwHAuQGr+QGoUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEDX4t9DXGIsMpkLFhRbNylMxVt1NJjsVXcSfzP4PnErKdk1Ix8UxIw1Zafp8szRN8rmIughlYes/ZZDpLftQWQFuIP4gTIBoQGituX1BJMEj6RjCOOGBOjsnO2GfHq91PSlRfuMJ/WKUIY/qiUiYAChAacq4FdHnKBqbNKNJJIYTBrZ/+6QZuLQnir28+NJyev7hiRhOcqAAAIKAIYQBnnXSADAoGqaa52JaMSjH4H7MjogrxV20/hgwMxjxJD798eMZF3mAFd7bOg="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422184,
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEDX4t9DXGIsMpkLFhRbNylMxVt1NJjsVXcSfzP4PnErKdk1Ix8UxIw1Zafp8szRN8rmIughlYes/ZZDpLftQWQFuIP4gTIBoQGituX1BJMEj6RjCOOGBOjsnO2GfHq91PSlRfuMJ/WKUIY/qiUiYAChAacq4FdHnKBqbNKNJJIYTBrZ/+6QZuLQnir28+NJyev7hiRhOcqAAAIKAIYQBnnXSADAoGqaa52JaMSjH4H7MjogrxV20/hgwMxjxJD798eMZF3mAFd7bOg=",
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEDX4t9DXGIsMpkLFhRbNylMxVt1NJjsVXcSfzP4PnErKdk1Ix8UxIw1Zafp8szRN8rmIughlYes/ZZDpLftQWQFuIP4gTIBoQGituX1BJMEj6RjCOOGBOjsnO2GfHq91PSlRfuMJ/WKUIY/qiUiYAChAacq4FdHnKBqbNKNJJIYTBrZ/+6QZuLQnir28+NJyev7hiRhOcqAAAIKAIYQBnnXSADAoGqaa52JaMSjH4H7MjogrxV20/hgwMxjxJD798eMZF3mAFd7bOg=",
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEDX4t9DXGIsMpkLFhRbNylMxVt1NJjsVXcSfzP4PnErKdk1Ix8UxIw1Zafp8szRN8rmIughlYes/ZZDpLftQWQFuIP4gTIBoQGituX1BJMEj6RjCOOGBOjsnO2GfHq91PSlRfuMJ/WKUIY/qiUiYAChAacq4FdHnKBqbNKNJJIYTBrZ/+6QZuLQnir28+NJyev7hiRhOcqAAAIKAIYQBnnXSADAoGqaa52JaMSjH4H7MjogrxV20/hgwMxjxJD798eMZF3mAFd7bOg=",
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEDX4t9DXGIsMpkLFhRbNylMxVt1NJjsVXcSfzP4PnErKdk1Ix8UxIw1Zafp8szRN8rmIughlYes/ZZDpLftQWQFuIP4gTIBoQGituX1BJMEj6RjCOOGBOjsnO2GfHq91PSlRfuMJ/WKUIY/qiUiYAChAacq4FdHnKBqbNKNJJIYTBrZ/+6QZuLQnir28+NJyev7hiRhOcqAAAIKAIYQBnnXSADAoGqaa52JaMSjH4H7MjogrxV20/hgwMxjxJD798eMZF3mAFd7bOg=",
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
    "to": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "message": {
        "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
        "from": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
        "info": "Hello",
        "to": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
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
    "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "message": {
        "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
        "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
        "info": "Hello back",
        "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422183,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
      "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422183,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
      "balance": 69999999999999
    },
    {
      "account": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "state": "tx_+QGxCwHAuQGr+QGoUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEDX4t9DXGIsMpkLFhRbNylMxVt1NJjsVXcSfzP4PnErKdk1Ix8UxIw1Zafp8szRN8rmIughlYes/ZZDpLftQWQFuIP4gTIBoQGituX1BJMEj6RjCOOGBOjsnO2GfHq91PSlRfuMJ/WKUIY/qiUiYAChAacq4FdHnKBqbNKNJJIYTBrZ/+6QZuLQnir28+NJyev7hiRhOcqAAAIKAIYQBnnXSADAoGqaa52JaMSjH4H7MjogrxV20/hgwMxjxJD798eMZF3mAFd7bOg="
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "state": "tx_+QGxCwHAuQGr+QGoUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEDX4t9DXGIsMpkLFhRbNylMxVt1NJjsVXcSfzP4PnErKdk1Ix8UxIw1Zafp8szRN8rmIughlYes/ZZDpLftQWQFuIP4gTIBoQGituX1BJMEj6RjCOOGBOjsnO2GfHq91PSlRfuMJ/WKUIY/qiUiYAChAacq4FdHnKBqbNKNJJIYTBrZ/+6QZuLQnir28+NJyev7hiRhOcqAAAIKAIYQBnnXSADAoGqaa52JaMSjH4H7MjogrxV20/hgwMxjxJD798eMZF3mAFd7bOg="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422182,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
      "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422182,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
      "balance": 69999999999999
    },
    {
      "account": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
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
    "from": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
    "to": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "error": {
    "code": 3,
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
        "from": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
        "to": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
      }
    }
  },
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
    "to": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "error": {
    "code": 3,
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
        "to": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
      }
    }
  },
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
    "from": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "error": {
    "code": 3,
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
        "from": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
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
    "from": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
    "meta": 17,
    "to": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
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
        "from": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
        "meta": 17,
        "to": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
      }
    }
  },
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
    "from": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
    "to": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqRdrvRM/oHlZ2Ax4uTCsMyPGn/hjYt6j8lFC8iIcK6vAqBpXRwPPFsaVM/ufRm4aHxBBtDqlbxLuuNO57oMMnTVKrtXzBY=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
          "op": "OffChainTransfer",
          "to": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422181,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBqRdrvRM/oHlZ2Ax4uTCsMyPGn/hjYt6j8lFC8iIcK6vAqBpXRwPPFsaVM/ufRm4aHxBBtDqlbxLuuNO57oMMnTVKmUlbeo="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422181,
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBqRdrvRM/oHlZ2Ax4uTCsMyPGn/hjYt6j8lFC8iIcK6vAqBpXRwPPFsaVM/ufRm4aHxBBtDqlbxLuuNO57oMMnTVKmUlbeo=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
          "op": "OffChainTransfer",
          "to": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422180,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDxfG4+ANOIEFwxnoiEqpLJUbyR9380yeOiG/s2H2mbAtOypOs7BWSFiV/Byz87rb52tFGzUh+43astRsdCgkgPuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwKgaV0cDzxbGlTP7n0ZuGh8QQbQ6pW8S7rjTue6DDJ01Srl8kS+"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422180,
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDxfG4+ANOIEFwxnoiEqpLJUbyR9380yeOiG/s2H2mbAtOypOs7BWSFiV/Byz87rb52tFGzUh+43astRsdCgkgPuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwKgaV0cDzxbGlTP7n0ZuGh8QQbQ6pW8S7rjTue6DDJ01Srl8kS+"
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDxfG4+ANOIEFwxnoiEqpLJUbyR9380yeOiG/s2H2mbAtOypOs7BWSFiV/Byz87rb52tFGzUh+43astRsdCgkgPuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwKgaV0cDzxbGlTP7n0ZuGh8QQbQ6pW8S7rjTue6DDJ01Srl8kS+"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422179,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
      "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422179,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
      "balance": 69999999999998
    },
    {
      "account": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422178,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422178,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDxfG4+ANOIEFwxnoiEqpLJUbyR9380yeOiG/s2H2mbAtOypOs7BWSFiV/Byz87rb52tFGzUh+43astRsdCgkgPuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwKgaV0cDzxbGlTP7n0ZuGh8QQbQ6pW8S7rjTue6DDJ01Srl8kS+",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCnKuBXR5ygamzSjSSSGEwa2f/ukGbi0J4q9vPjScnr+4vKCgEAhiRhOcqAArDvQAGgorbl9QSTBI+kYwjjhgTo7Jzthnx6vdT0pUX7jCf1ilCLygoBAIY/qiUiX/52pA2D"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422177,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
      "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422177,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
      "balance": 40000000000002
    },
    {
      "account": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
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
    "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
    "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "error": {
    "code": 3,
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
        "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
        "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
      }
    }
  },
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
    "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "error": {
    "code": 3,
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
        "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
      }
    }
  },
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
    "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "error": {
    "code": 3,
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
        "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
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
    "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
    "meta": 17,
    "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
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
        "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
        "meta": 17,
        "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
      }
    }
  },
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
    "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
    "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqRdrvRM/oHlZ2Ax4uTCsMyPGn/hjYt6j8lFC8iIcK6vA6BqmmudiWjEox+B+zI6IK8VdtP4YMDMY8SQ+/fHjGRd5vsIv4k=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
          "op": "OffChainTransfer",
          "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422176,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDSYApzque6V0jnsMCgXtC+aJefq01aM+dSQHGTQD7md6L2oxsBXZGeBKJxBLkAOXXXkfoEXyIUwR4newVRblMFuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwOgapprnYloxKMfgfsyOiCvFXbT+GDAzGPEkPv3x4xkXeaKX3w9"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422176,
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDSYApzque6V0jnsMCgXtC+aJefq01aM+dSQHGTQD7md6L2oxsBXZGeBKJxBLkAOXXXkfoEXyIUwR4newVRblMFuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwOgapprnYloxKMfgfsyOiCvFXbT+GDAzGPEkPv3x4xkXeaKX3w9",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
          "op": "OffChainTransfer",
          "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422175,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDSYApzque6V0jnsMCgXtC+aJefq01aM+dSQHGTQD7md6L2oxsBXZGeBKJxBLkAOXXXkfoEXyIUwR4newVRblMFuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwOgapprnYloxKMfgfsyOiCvFXbT+GDAzGPEkPv3x4xkXeZmgnF3"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422175,
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDSYApzque6V0jnsMCgXtC+aJefq01aM+dSQHGTQD7md6L2oxsBXZGeBKJxBLkAOXXXkfoEXyIUwR4newVRblMFuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwOgapprnYloxKMfgfsyOiCvFXbT+GDAzGPEkPv3x4xkXeZmgnF3"
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDSYApzque6V0jnsMCgXtC+aJefq01aM+dSQHGTQD7md6L2oxsBXZGeBKJxBLkAOXXXkfoEXyIUwR4newVRblMFuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwOgapprnYloxKMfgfsyOiCvFXbT+GDAzGPEkPv3x4xkXeZmgnF3"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422174,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
      "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422174,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
      "balance": 40000000000001
    },
    {
      "account": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422173,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422173,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDSYApzque6V0jnsMCgXtC+aJefq01aM+dSQHGTQD7md6L2oxsBXZGeBKJxBLkAOXXXkfoEXyIUwR4newVRblMFuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwOgapprnYloxKMfgfsyOiCvFXbT+GDAzGPEkPv3x4xkXeZmgnF3",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCnKuBXR5ygamzSjSSSGEwa2f/ukGbi0J4q9vPjScnr+4vKCgEAhiRhOcqAAbDvQAGgorbl9QSTBI+kYwjjhgTo7Jzthnx6vdT0pUX7jCf1ilCLygoBAIY/qiUiX/8UfMYG"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422172,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
      "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422172,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
      "balance": 40000000000001
    },
    {
      "account": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
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
    "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
    "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "error": {
    "code": 3,
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
        "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
        "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
      }
    }
  },
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
    "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "error": {
    "code": 3,
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
        "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
      }
    }
  },
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
    "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "error": {
    "code": 3,
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
        "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
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
    "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
    "meta": 17,
    "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
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
        "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
        "meta": 17,
        "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
      }
    }
  },
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
    "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
    "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqRdrvRM/oHlZ2Ax4uTCsMyPGn/hjYt6j8lFC8iIcK6vBKCUJvOw/WpyX0xrHgBbonHyxzpGU8y3+xdohttt0+kKvzTV2lA=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
          "op": "OffChainTransfer",
          "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422171,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAFGtJiGVRHdCQGb2t05pg3YGarR/Xi1f8oHxdTseZEiE+N6ZxNRFUwJaJNNcPQoIu0zBf//U7titzD6eHUkSMKuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwSglCbzsP1qcl9Max4AW6Jx8sc6RlPMt/sXaIbbbdPpCr+t4eJH"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422171,
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAFGtJiGVRHdCQGb2t05pg3YGarR/Xi1f8oHxdTseZEiE+N6ZxNRFUwJaJNNcPQoIu0zBf//U7titzD6eHUkSMKuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwSglCbzsP1qcl9Max4AW6Jx8sc6RlPMt/sXaIbbbdPpCr+t4eJH",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
          "op": "OffChainTransfer",
          "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422170,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAFGtJiGVRHdCQGb2t05pg3YGarR/Xi1f8oHxdTseZEiE+N6ZxNRFUwJaJNNcPQoIu0zBf//U7titzD6eHUkSMKuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwSglCbzsP1qcl9Max4AW6Jx8sc6RlPMt/sXaIbbbdPpCr8d/ZvG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422170,
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAFGtJiGVRHdCQGb2t05pg3YGarR/Xi1f8oHxdTseZEiE+N6ZxNRFUwJaJNNcPQoIu0zBf//U7titzD6eHUkSMKuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwSglCbzsP1qcl9Max4AW6Jx8sc6RlPMt/sXaIbbbdPpCr8d/ZvG"
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAFGtJiGVRHdCQGb2t05pg3YGarR/Xi1f8oHxdTseZEiE+N6ZxNRFUwJaJNNcPQoIu0zBf//U7titzD6eHUkSMKuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwSglCbzsP1qcl9Max4AW6Jx8sc6RlPMt/sXaIbbbdPpCr8d/ZvG"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422169,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
      "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422169,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
      "balance": 40000000000000
    },
    {
      "account": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422168,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422168,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAFGtJiGVRHdCQGb2t05pg3YGarR/Xi1f8oHxdTseZEiE+N6ZxNRFUwJaJNNcPQoIu0zBf//U7titzD6eHUkSMKuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwSglCbzsP1qcl9Max4AW6Jx8sc6RlPMt/sXaIbbbdPpCr8d/ZvG",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCnKuBXR5ygamzSjSSSGEwa2f/ukGbi0J4q9vPjScnr+4vKCgEAhiRhOcqAALDvQAGgorbl9QSTBI+kYwjjhgTo7Jzthnx6vdT0pUX7jCf1ilCLygoBAIY/qiUiYABUuDag"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422167,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
      "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422167,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
      "balance": 70000000000000
    },
    {
      "account": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
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
    "from": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
    "to": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "error": {
    "code": 3,
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
        "from": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
        "to": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
      }
    }
  },
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
    "to": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "error": {
    "code": 3,
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
        "to": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
      }
    }
  },
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
    "from": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "error": {
    "code": 3,
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
        "from": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
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
    "from": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
    "meta": 17,
    "to": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
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
        "from": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
        "meta": 17,
        "to": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
      }
    }
  },
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
    "from": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
    "to": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqRdrvRM/oHlZ2Ax4uTCsMyPGn/hjYt6j8lFC8iIcK6vBaBqmmudiWjEox+B+zI6IK8VdtP4YMDMY8SQ+/fHjGRd5ow8vWg=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
          "op": "OffChainTransfer",
          "to": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422166,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBqRdrvRM/oHlZ2Ax4uTCsMyPGn/hjYt6j8lFC8iIcK6vBaBqmmudiWjEox+B+zI6IK8VdtP4YMDMY8SQ+/fHjGRd5mh0MGM="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422166,
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBqRdrvRM/oHlZ2Ax4uTCsMyPGn/hjYt6j8lFC8iIcK6vBaBqmmudiWjEox+B+zI6IK8VdtP4YMDMY8SQ+/fHjGRd5mh0MGM=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
          "op": "OffChainTransfer",
          "to": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422165,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECFmgX9HEmYMjmHOaWRhTNASa3oOu1fdXqUJAXSbgXTwY1koDeihKm/Gd378IshnX91guggxiET1jc0gxX+Qd4OuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwWgapprnYloxKMfgfsyOiCvFXbT+GDAzGPEkPv3x4xkXeYSKqMN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422165,
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECFmgX9HEmYMjmHOaWRhTNASa3oOu1fdXqUJAXSbgXTwY1koDeihKm/Gd378IshnX91guggxiET1jc0gxX+Qd4OuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwWgapprnYloxKMfgfsyOiCvFXbT+GDAzGPEkPv3x4xkXeYSKqMN"
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECFmgX9HEmYMjmHOaWRhTNASa3oOu1fdXqUJAXSbgXTwY1koDeihKm/Gd378IshnX91guggxiET1jc0gxX+Qd4OuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwWgapprnYloxKMfgfsyOiCvFXbT+GDAzGPEkPv3x4xkXeYSKqMN"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422164,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
      "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422164,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
      "balance": 69999999999999
    },
    {
      "account": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422163,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422163,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECFmgX9HEmYMjmHOaWRhTNASa3oOu1fdXqUJAXSbgXTwY1koDeihKm/Gd378IshnX91guggxiET1jc0gxX+Qd4OuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwWgapprnYloxKMfgfsyOiCvFXbT+GDAzGPEkPv3x4xkXeYSKqMN",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCnKuBXR5ygamzSjSSSGEwa2f/ukGbi0J4q9vPjScnr+4vKCgEAhiRhOcqAAbDvQAGgorbl9QSTBI+kYwjjhgTo7Jzthnx6vdT0pUX7jCf1ilCLygoBAIY/qiUiX/8UfMYG"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422162,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
      "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422162,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
      "balance": 40000000000001
    },
    {
      "account": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
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
    "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
    "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "error": {
    "code": 3,
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
        "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
        "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
      }
    }
  },
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
    "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "error": {
    "code": 3,
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
        "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
      }
    }
  },
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
    "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "error": {
    "code": 3,
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
        "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
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
    "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
    "meta": 17,
    "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
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
        "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
        "meta": 17,
        "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
      }
    }
  },
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
    "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
    "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqRdrvRM/oHlZ2Ax4uTCsMyPGn/hjYt6j8lFC8iIcK6vBqCUJvOw/WpyX0xrHgBbonHyxzpGU8y3+xdohttt0+kKv8FJbcU=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
          "op": "OffChainTransfer",
          "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422161,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECbVSDZnx7aFoGDndPYtMH0FiTyZmUD/5aTR2VtXq8nvsgICb8BZcERGzXQD0lmxwLrQtdR1pQ1DEiDtBamnMIIuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwaglCbzsP1qcl9Max4AW6Jx8sc6RlPMt/sXaIbbbdPpCr9yz6gO"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422161,
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "signed_tx": "tx_+JALAfhCuECbVSDZnx7aFoGDndPYtMH0FiTyZmUD/5aTR2VtXq8nvsgICb8BZcERGzXQD0lmxwLrQtdR1pQ1DEiDtBamnMIIuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwaglCbzsP1qcl9Max4AW6Jx8sc6RlPMt/sXaIbbbdPpCr9yz6gO",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
          "op": "OffChainTransfer",
          "to": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422160,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECbVSDZnx7aFoGDndPYtMH0FiTyZmUD/5aTR2VtXq8nvsgICb8BZcERGzXQD0lmxwLrQtdR1pQ1DEiDtBamnMIIuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwaglCbzsP1qcl9Max4AW6Jx8sc6RlPMt/sXaIbbbdPpCr8LvPOm"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422160,
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECbVSDZnx7aFoGDndPYtMH0FiTyZmUD/5aTR2VtXq8nvsgICb8BZcERGzXQD0lmxwLrQtdR1pQ1DEiDtBamnMIIuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwaglCbzsP1qcl9Max4AW6Jx8sc6RlPMt/sXaIbbbdPpCr8LvPOm"
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECbVSDZnx7aFoGDndPYtMH0FiTyZmUD/5aTR2VtXq8nvsgICb8BZcERGzXQD0lmxwLrQtdR1pQ1DEiDtBamnMIIuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwaglCbzsP1qcl9Max4AW6Jx8sc6RlPMt/sXaIbbbdPpCr8LvPOm"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422159,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
      "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422159,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2Gd51KEa5YQWsRz3kVAQbH9sw9s7MLm69iWpY83RgB4VQS11CM",
      "balance": 40000000000000
    },
    {
      "account": "ak_2EfKghfEd4qTFJJtAaNpHTZmisBz36p97cwgWayFf7Bewe3REE",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422158,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422158,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAaK25fUEkwSPpGMI44YE6Oyc7YZ8er3U9KVF+4wn9YpQuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECbVSDZnx7aFoGDndPYtMH0FiTyZmUD/5aTR2VtXq8nvsgICb8BZcERGzXQD0lmxwLrQtdR1pQ1DEiDtBamnMIIuEj4RjkCoQakXa70TP6B5WdgMeLkwrDMjxp/4Y2Leo/JRQvIiHCurwaglCbzsP1qcl9Max4AW6Jx8sc6RlPMt/sXaIbbbdPpCr8LvPOm",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCnKuBXR5ygamzSjSSSGEwa2f/ukGbi0J4q9vPjScnr+4vKCgEAhiRhOcqAALDvQAGgorbl9QSTBI+kYwjjhgTo7Jzthnx6vdT0pUX7jCf1ilCLygoBAIY/qiUiYABUuDag"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422157,
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
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422157,
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
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
    "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422156,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### responder closes WebSocket connection

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2FPWSc9nQETCbXPUSdSpcJoC9F8FiGaJB5YwPmow6TVUPEt3LF",
  "id": -576460752303422156,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg&keep_running=false&lock_period=10&port=12890&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ&role=initiator
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
      "fsm_id": "ba_mU9ccUYBvg+opVa5SQYqYD+21/R0ckfkyKZ96nmT4GOADVO7"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg&keep_running=false&lock_period=10&port=12890&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ&role=responder
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
      "fsm_id": "ba_I547a8jQiaCTEtMotesv02lawhUtId5fkPEe93fF/67aJjvO"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJhj+qJSJgAKEBn94n4uvunCYrqNE+7ogF+ey+Hcl3hhSTjOYB1i5QhxOGJGE5yoAAAgoAhhAGeddIAMCgm3fBBpgSag3eNODu2NzSPs/IIJJfLdCH/gz+ewaYSGkAs3Q4Ww==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421538,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+NQLAcC4z/jNUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQGl2oEFU3Xj/WWlEE5nOFZ88MydiSlOtNi5XJ3EEpBbyYY/qiUiYAChAZ/eJ+Lr7pwmK6jRPu6IBfnsvh3Jd4YUk4zmAdYuUIcThiRhOcqAAAIKAIYQBnnXSADAoJt3wQaYEmoN3jTg7tjc0j7PyCCSXy3Qh/4M/nsGmEhpAGKrqkI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421538,
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
      "signed_tx": "tx_+NQLAcC4z/jNUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQGl2oEFU3Xj/WWlEE5nOFZ88MydiSlOtNi5XJ3EEpBbyYY/qiUiYAChAZ/eJ+Lr7pwmK6jRPu6IBfnsvh3Jd4YUk4zmAdYuUIcThiRhOcqAAAIKAIYQBnnXSADAoJt3wQaYEmoN3jTg7tjc0j7PyCCSXy3Qh/4M/nsGmEhpAGKrqkI=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421537,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEZCwHAuQET+QEQUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAqAO3dwmxtWTgtRpngT6VaGHE5xdo9N+mHOThcqCY6Dw4QP/16Y8o4XKtUglo9+oVxl4lPxxB3HDQNlV7jjQEDLiD+IEyAaEBpdqBBVN14/1lpRBOZzhWfPDMnYkpTrTYuVydxBKQW8mGP6olImAAoQGf3ifi6+6cJiuo0T7uiAX57L4dyXeGFJOM5gHWLlCHE4YkYTnKgAACCgCGEAZ510gAwKCbd8EGmBJqDd404O7Y3NI+z8ggkl8t0If+DP57BphIaQCOoHVQ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421537,
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAqAO3dwmxtWTgtRpngT6VaGHE5xdo9N+mHOThcqCY6Dw4QP/16Y8o4XKtUglo9+oVxl4lPxxB3HDQNlV7jjQEDLiD+IEyAaEBpdqBBVN14/1lpRBOZzhWfPDMnYkpTrTYuVydxBKQW8mGP6olImAAoQGf3ifi6+6cJiuo0T7uiAX57L4dyXeGFJOM5gHWLlCHE4YkYTnKgAACCgCGEAZ510gAwKCbd8EGmBJqDd404O7Y3NI+z8ggkl8t0If+DP57BphIaQCOoHVQ",
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAqAO3dwmxtWTgtRpngT6VaGHE5xdo9N+mHOThcqCY6Dw4QP/16Y8o4XKtUglo9+oVxl4lPxxB3HDQNlV7jjQEDLiD+IEyAaEBpdqBBVN14/1lpRBOZzhWfPDMnYkpTrTYuVydxBKQW8mGP6olImAAoQGf3ifi6+6cJiuo0T7uiAX57L4dyXeGFJOM5gHWLlCHE4YkYTnKgAACCgCGEAZ510gAwKCbd8EGmBJqDd404O7Y3NI+z8ggkl8t0If+DP57BphIaQCOoHVQ",
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAqAO3dwmxtWTgtRpngT6VaGHE5xdo9N+mHOThcqCY6Dw4QP/16Y8o4XKtUglo9+oVxl4lPxxB3HDQNlV7jjQEDLiD+IEyAaEBpdqBBVN14/1lpRBOZzhWfPDMnYkpTrTYuVydxBKQW8mGP6olImAAoQGf3ifi6+6cJiuo0T7uiAX57L4dyXeGFJOM5gHWLlCHE4YkYTnKgAACCgCGEAZ510gAwKCbd8EGmBJqDd404O7Y3NI+z8ggkl8t0If+DP57BphIaQCOoHVQ",
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAqAO3dwmxtWTgtRpngT6VaGHE5xdo9N+mHOThcqCY6Dw4QP/16Y8o4XKtUglo9+oVxl4lPxxB3HDQNlV7jjQEDLiD+IEyAaEBpdqBBVN14/1lpRBOZzhWfPDMnYkpTrTYuVydxBKQW8mGP6olImAAoQGf3ifi6+6cJiuo0T7uiAX57L4dyXeGFJOM5gHWLlCHE4YkYTnKgAACCgCGEAZ510gAwKCbd8EGmBJqDd404O7Y3NI+z8ggkl8t0If+DP57BphIaQCOoHVQ",
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
    "to": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "message": {
        "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
        "from": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
        "info": "Hello",
        "to": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
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
    "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "message": {
        "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
        "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
        "info": "Hello back",
        "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421536,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
      "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421536,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
      "balance": 69999999999999
    },
    {
      "account": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "state": "tx_+QEZCwHAuQET+QEQUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAqAO3dwmxtWTgtRpngT6VaGHE5xdo9N+mHOThcqCY6Dw4QP/16Y8o4XKtUglo9+oVxl4lPxxB3HDQNlV7jjQEDLiD+IEyAaEBpdqBBVN14/1lpRBOZzhWfPDMnYkpTrTYuVydxBKQW8mGP6olImAAoQGf3ifi6+6cJiuo0T7uiAX57L4dyXeGFJOM5gHWLlCHE4YkYTnKgAACCgCGEAZ510gAwKCbd8EGmBJqDd404O7Y3NI+z8ggkl8t0If+DP57BphIaQCOoHVQ"
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "state": "tx_+QEZCwHAuQET+QEQUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAqAO3dwmxtWTgtRpngT6VaGHE5xdo9N+mHOThcqCY6Dw4QP/16Y8o4XKtUglo9+oVxl4lPxxB3HDQNlV7jjQEDLiD+IEyAaEBpdqBBVN14/1lpRBOZzhWfPDMnYkpTrTYuVydxBKQW8mGP6olImAAoQGf3ifi6+6cJiuo0T7uiAX57L4dyXeGFJOM5gHWLlCHE4YkYTnKgAACCgCGEAZ510gAwKCbd8EGmBJqDd404O7Y3NI+z8ggkl8t0If+DP57BphIaQCOoHVQ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421535,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
      "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421535,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
      "balance": 69999999999999
    },
    {
      "account": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
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
    "from": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
    "to": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "error": {
    "code": 3,
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
        "from": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
        "to": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
      }
    }
  },
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
    "to": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "error": {
    "code": 3,
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
        "to": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
      }
    }
  },
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
    "from": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "error": {
    "code": 3,
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
        "from": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
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
    "from": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
    "meta": 17,
    "to": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
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
        "from": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
        "meta": 17,
        "to": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
      }
    }
  },
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
    "from": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
    "to": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqXaZk8d8hV0ZDQdcqkSzowr/DCmtpjKAOCZ0/Jb1Qv1AqA/GT7qzHF2R0wNJ4KvdPiga7NeV4mynlPnm9acactyLqq2J8M=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
          "op": "OffChainTransfer",
          "to": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421534,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQal2mZPHfIVdGQ0HXKpEs6MK/wwpraYygDgmdPyW9UL9QKgPxk+6sxxdkdMDSeCr3T4oGuzXleJsp5T55vWnGnLci6LLKHO"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421534,
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQal2mZPHfIVdGQ0HXKpEs6MK/wwpraYygDgmdPyW9UL9QKgPxk+6sxxdkdMDSeCr3T4oGuzXleJsp5T55vWnGnLci6LLKHO",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
          "op": "OffChainTransfer",
          "to": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421533,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAv/E8AG9QumP/YymO7g0pWaLiTUNObatNzcinyZ7PV11BtZ0cyLciVlC7BZAw6gaJ9bIgY7GoukjUJ1iahnAgDbhI+EY5AqEGpdpmTx3yFXRkNB1yqRLOjCv8MKa2mMoA4JnT8lvVC/UCoD8ZPurMcXZHTA0ngq90+KBrs15XibKeU+eb1pxpy3Ius55Pww=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421533,
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAv/E8AG9QumP/YymO7g0pWaLiTUNObatNzcinyZ7PV11BtZ0cyLciVlC7BZAw6gaJ9bIgY7GoukjUJ1iahnAgDbhI+EY5AqEGpdpmTx3yFXRkNB1yqRLOjCv8MKa2mMoA4JnT8lvVC/UCoD8ZPurMcXZHTA0ngq90+KBrs15XibKeU+eb1pxpy3Ius55Pww=="
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAv/E8AG9QumP/YymO7g0pWaLiTUNObatNzcinyZ7PV11BtZ0cyLciVlC7BZAw6gaJ9bIgY7GoukjUJ1iahnAgDbhI+EY5AqEGpdpmTx3yFXRkNB1yqRLOjCv8MKa2mMoA4JnT8lvVC/UCoD8ZPurMcXZHTA0ngq90+KBrs15XibKeU+eb1pxpy3Ius55Pww=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421532,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
      "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421532,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
      "balance": 69999999999998
    },
    {
      "account": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421531,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421531,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAv/E8AG9QumP/YymO7g0pWaLiTUNObatNzcinyZ7PV11BtZ0cyLciVlC7BZAw6gaJ9bIgY7GoukjUJ1iahnAgDbhI+EY5AqEGpdpmTx3yFXRkNB1yqRLOjCv8MKa2mMoA4JnT8lvVC/UCoD8ZPurMcXZHTA0ngq90+KBrs15XibKeU+eb1pxpy3Ius55Pww==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCl2oEFU3Xj/WWlEE5nOFZ88MydiSlOtNi5XJ3EEpBbyYvKCgEAhj+qJSJf/rDvQAGgn94n4uvunCYrqNE+7ogF+ey+Hcl3hhSTjOYB1i5QhxOLygoBAIYkYTnKgAJeHgDq"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421530,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
      "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421530,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
      "balance": 40000000000002
    },
    {
      "account": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
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
    "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
    "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "error": {
    "code": 3,
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
        "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
        "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
      }
    }
  },
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
    "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "error": {
    "code": 3,
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
        "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
      }
    }
  },
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
    "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "error": {
    "code": 3,
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
        "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
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
    "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
    "meta": 17,
    "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
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
        "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
        "meta": 17,
        "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
      }
    }
  },
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
    "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
    "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqXaZk8d8hV0ZDQdcqkSzowr/DCmtpjKAOCZ0/Jb1Qv1A6Cbd8EGmBJqDd404O7Y3NI+z8ggkl8t0If+DP57BphIaUR4grw=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
          "op": "OffChainTransfer",
          "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421529,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDpdEYB3JVXuEt8DzY6s1jc8XWbE2OVEytxt9lK/mEOg78sWMG6U/4oKhRLw/AOSAOJMCaELnlpb/BSyrqL7aIJuEj4RjkCoQal2mZPHfIVdGQ0HXKpEs6MK/wwpraYygDgmdPyW9UL9QOgm3fBBpgSag3eNODu2NzSPs/IIJJfLdCH/gz+ewaYSGni7U27"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421529,
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDpdEYB3JVXuEt8DzY6s1jc8XWbE2OVEytxt9lK/mEOg78sWMG6U/4oKhRLw/AOSAOJMCaELnlpb/BSyrqL7aIJuEj4RjkCoQal2mZPHfIVdGQ0HXKpEs6MK/wwpraYygDgmdPyW9UL9QOgm3fBBpgSag3eNODu2NzSPs/IIJJfLdCH/gz+ewaYSGni7U27",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
          "op": "OffChainTransfer",
          "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421528,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA6XRGAdyVV7hLfA82OrNY3PF1mxNjlRMrcbfZSv5hDoO/LFjBulP+KCoUS8PwDkgDiTAmhC55aW/wUsq6i+2iCbhI+EY5AqEGpdpmTx3yFXRkNB1yqRLOjCv8MKa2mMoA4JnT8lvVC/UDoJt3wQaYEmoN3jTg7tjc0j7PyCCSXy3Qh/4M/nsGmEhpapOT+w=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421528,
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA6XRGAdyVV7hLfA82OrNY3PF1mxNjlRMrcbfZSv5hDoO/LFjBulP+KCoUS8PwDkgDiTAmhC55aW/wUsq6i+2iCbhI+EY5AqEGpdpmTx3yFXRkNB1yqRLOjCv8MKa2mMoA4JnT8lvVC/UDoJt3wQaYEmoN3jTg7tjc0j7PyCCSXy3Qh/4M/nsGmEhpapOT+w=="
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA6XRGAdyVV7hLfA82OrNY3PF1mxNjlRMrcbfZSv5hDoO/LFjBulP+KCoUS8PwDkgDiTAmhC55aW/wUsq6i+2iCbhI+EY5AqEGpdpmTx3yFXRkNB1yqRLOjCv8MKa2mMoA4JnT8lvVC/UDoJt3wQaYEmoN3jTg7tjc0j7PyCCSXy3Qh/4M/nsGmEhpapOT+w=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421527,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
      "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421527,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
      "balance": 40000000000001
    },
    {
      "account": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421526,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421526,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA6XRGAdyVV7hLfA82OrNY3PF1mxNjlRMrcbfZSv5hDoO/LFjBulP+KCoUS8PwDkgDiTAmhC55aW/wUsq6i+2iCbhI+EY5AqEGpdpmTx3yFXRkNB1yqRLOjCv8MKa2mMoA4JnT8lvVC/UDoJt3wQaYEmoN3jTg7tjc0j7PyCCSXy3Qh/4M/nsGmEhpapOT+w==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCl2oEFU3Xj/WWlEE5nOFZ88MydiSlOtNi5XJ3EEpBbyYvKCgEAhj+qJSJf/7DvQAGgn94n4uvunCYrqNE+7ogF+ey+Hcl3hhSTjOYB1i5QhxOLygoBAIYkYTnKgAEEBL98"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421525,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
      "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421525,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
      "balance": 40000000000001
    },
    {
      "account": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
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
    "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
    "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "error": {
    "code": 3,
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
        "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
        "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
      }
    }
  },
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
    "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "error": {
    "code": 3,
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
        "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
      }
    }
  },
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
    "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "error": {
    "code": 3,
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
        "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
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
    "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
    "meta": 17,
    "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
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
        "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
        "meta": 17,
        "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
      }
    }
  },
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
    "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
    "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqXaZk8d8hV0ZDQdcqkSzowr/DCmtpjKAOCZ0/Jb1Qv1BKDoYmjZZY4hDmrn0ksrOEgz1Aixygxmce0TVZP9skdqnWdQdR8=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
          "op": "OffChainTransfer",
          "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421524,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDu7reogLnpgnSuKvh7OjGyFvxA7LXnazNaKn+FZF1oxJ/2B6muXZAsl87Ld4LAiZHcR50wq0sD95XpGavzFXgBuEj4RjkCoQal2mZPHfIVdGQ0HXKpEs6MK/wwpraYygDgmdPyW9UL9QSg6GJo2WWOIQ5q59JLKzhIM9QIscoMZnHtE1WT/bJHap0x50W2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421524,
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDu7reogLnpgnSuKvh7OjGyFvxA7LXnazNaKn+FZF1oxJ/2B6muXZAsl87Ld4LAiZHcR50wq0sD95XpGavzFXgBuEj4RjkCoQal2mZPHfIVdGQ0HXKpEs6MK/wwpraYygDgmdPyW9UL9QSg6GJo2WWOIQ5q59JLKzhIM9QIscoMZnHtE1WT/bJHap0x50W2",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
          "op": "OffChainTransfer",
          "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421523,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA7u63qIC56YJ0rir4ezoxshb8QOy152szWip/hWRdaMSf9geprl2QLJfOy3eCwImR3EedMKtLA/eV6Rmr8xV4AbhI+EY5AqEGpdpmTx3yFXRkNB1yqRLOjCv8MKa2mMoA4JnT8lvVC/UEoOhiaNlljiEOaufSSys4SDPUCLHKDGZx7RNVk/2yR2qdJolM8A=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421523,
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA7u63qIC56YJ0rir4ezoxshb8QOy152szWip/hWRdaMSf9geprl2QLJfOy3eCwImR3EedMKtLA/eV6Rmr8xV4AbhI+EY5AqEGpdpmTx3yFXRkNB1yqRLOjCv8MKa2mMoA4JnT8lvVC/UEoOhiaNlljiEOaufSSys4SDPUCLHKDGZx7RNVk/2yR2qdJolM8A=="
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA7u63qIC56YJ0rir4ezoxshb8QOy152szWip/hWRdaMSf9geprl2QLJfOy3eCwImR3EedMKtLA/eV6Rmr8xV4AbhI+EY5AqEGpdpmTx3yFXRkNB1yqRLOjCv8MKa2mMoA4JnT8lvVC/UEoOhiaNlljiEOaufSSys4SDPUCLHKDGZx7RNVk/2yR2qdJolM8A=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421522,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
      "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421522,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
      "balance": 40000000000000
    },
    {
      "account": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421521,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421521,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA7u63qIC56YJ0rir4ezoxshb8QOy152szWip/hWRdaMSf9geprl2QLJfOy3eCwImR3EedMKtLA/eV6Rmr8xV4AbhI+EY5AqEGpdpmTx3yFXRkNB1yqRLOjCv8MKa2mMoA4JnT8lvVC/UEoOhiaNlljiEOaufSSys4SDPUCLHKDGZx7RNVk/2yR2qdJolM8A==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCl2oEFU3Xj/WWlEE5nOFZ88MydiSlOtNi5XJ3EEpBbyYvKCgEAhj+qJSJgALDvQAGgn94n4uvunCYrqNE+7ogF+ey+Hcl3hhSTjOYB1i5QhxOLygoBAIYkYTnKgAAHJl44"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421520,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
      "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421520,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
      "balance": 70000000000000
    },
    {
      "account": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
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
    "from": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
    "to": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "error": {
    "code": 3,
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
        "from": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
        "to": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
      }
    }
  },
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
    "to": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "error": {
    "code": 3,
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
        "to": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
      }
    }
  },
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
    "from": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "error": {
    "code": 3,
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
        "from": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
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
    "from": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
    "meta": 17,
    "to": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
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
        "from": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
        "meta": 17,
        "to": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
      }
    }
  },
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
    "from": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
    "to": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqXaZk8d8hV0ZDQdcqkSzowr/DCmtpjKAOCZ0/Jb1Qv1BaCbd8EGmBJqDd404O7Y3NI+z8ggkl8t0If+DP57BphIaZfQ4rg=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
          "op": "OffChainTransfer",
          "to": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421519,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQal2mZPHfIVdGQ0HXKpEs6MK/wwpraYygDgmdPyW9UL9QWgm3fBBpgSag3eNODu2NzSPs/IIJJfLdCH/gz+ewaYSGnSWacM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421519,
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQal2mZPHfIVdGQ0HXKpEs6MK/wwpraYygDgmdPyW9UL9QWgm3fBBpgSag3eNODu2NzSPs/IIJJfLdCH/gz+ewaYSGnSWacM",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
          "op": "OffChainTransfer",
          "to": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421518,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAp778uehBXkafY1ADfFhxcEb5GzbjBrJXLPmyMRyADQ5YPv60mIKL5nnKEUTJ+KWZ2jL0N8aCgJO2hd0JTE+RB7hI+EY5AqEGpdpmTx3yFXRkNB1yqRLOjCv8MKa2mMoA4JnT8lvVC/UFoJt3wQaYEmoN3jTg7tjc0j7PyCCSXy3Qh/4M/nsGmEhpxO+POw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421518,
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAp778uehBXkafY1ADfFhxcEb5GzbjBrJXLPmyMRyADQ5YPv60mIKL5nnKEUTJ+KWZ2jL0N8aCgJO2hd0JTE+RB7hI+EY5AqEGpdpmTx3yFXRkNB1yqRLOjCv8MKa2mMoA4JnT8lvVC/UFoJt3wQaYEmoN3jTg7tjc0j7PyCCSXy3Qh/4M/nsGmEhpxO+POw=="
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAp778uehBXkafY1ADfFhxcEb5GzbjBrJXLPmyMRyADQ5YPv60mIKL5nnKEUTJ+KWZ2jL0N8aCgJO2hd0JTE+RB7hI+EY5AqEGpdpmTx3yFXRkNB1yqRLOjCv8MKa2mMoA4JnT8lvVC/UFoJt3wQaYEmoN3jTg7tjc0j7PyCCSXy3Qh/4M/nsGmEhpxO+POw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421517,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
      "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421517,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
      "balance": 69999999999999
    },
    {
      "account": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421516,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421516,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAp778uehBXkafY1ADfFhxcEb5GzbjBrJXLPmyMRyADQ5YPv60mIKL5nnKEUTJ+KWZ2jL0N8aCgJO2hd0JTE+RB7hI+EY5AqEGpdpmTx3yFXRkNB1yqRLOjCv8MKa2mMoA4JnT8lvVC/UFoJt3wQaYEmoN3jTg7tjc0j7PyCCSXy3Qh/4M/nsGmEhpxO+POw==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCl2oEFU3Xj/WWlEE5nOFZ88MydiSlOtNi5XJ3EEpBbyYvKCgEAhj+qJSJf/7DvQAGgn94n4uvunCYrqNE+7ogF+ey+Hcl3hhSTjOYB1i5QhxOLygoBAIYkYTnKgAEEBL98"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421515,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
      "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421515,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
      "balance": 40000000000001
    },
    {
      "account": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
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
    "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
    "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "error": {
    "code": 3,
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
        "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
        "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
      }
    }
  },
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
    "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "error": {
    "code": 3,
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
        "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
      }
    }
  },
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
    "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "error": {
    "code": 3,
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
        "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
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
    "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
    "meta": 17,
    "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
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
        "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
        "meta": 17,
        "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
      }
    }
  },
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
    "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
    "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqXaZk8d8hV0ZDQdcqkSzowr/DCmtpjKAOCZ0/Jb1Qv1BqDoYmjZZY4hDmrn0ksrOEgz1Aixygxmce0TVZP9skdqnXu5FTU=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
          "op": "OffChainTransfer",
          "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421514,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC441DPD2g+C2tmGoG9kXbzq/IWpx+XPlarqkheKAmGSy3gPIUi+L28SPX6B0/+VdLuF6GsZctZqMXfO/hsyRsFuEj4RjkCoQal2mZPHfIVdGQ0HXKpEs6MK/wwpraYygDgmdPyW9UL9Qag6GJo2WWOIQ5q59JLKzhIM9QIscoMZnHtE1WT/bJHap0dbvGI"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421514,
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC441DPD2g+C2tmGoG9kXbzq/IWpx+XPlarqkheKAmGSy3gPIUi+L28SPX6B0/+VdLuF6GsZctZqMXfO/hsyRsFuEj4RjkCoQal2mZPHfIVdGQ0HXKpEs6MK/wwpraYygDgmdPyW9UL9Qag6GJo2WWOIQ5q59JLKzhIM9QIscoMZnHtE1WT/bJHap0dbvGI",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
          "op": "OffChainTransfer",
          "to": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421513,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAuONQzw9oPgtrZhqBvZF286vyFqcflz5Wq6pIXigJhkst4DyFIvi9vEj1+gdP/lXS7hehrGXLWajF3zv4bMkbBbhI+EY5AqEGpdpmTx3yFXRkNB1yqRLOjCv8MKa2mMoA4JnT8lvVC/UGoOhiaNlljiEOaufSSys4SDPUCLHKDGZx7RNVk/2yR2qdsOTmBQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421513,
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAuONQzw9oPgtrZhqBvZF286vyFqcflz5Wq6pIXigJhkst4DyFIvi9vEj1+gdP/lXS7hehrGXLWajF3zv4bMkbBbhI+EY5AqEGpdpmTx3yFXRkNB1yqRLOjCv8MKa2mMoA4JnT8lvVC/UGoOhiaNlljiEOaufSSys4SDPUCLHKDGZx7RNVk/2yR2qdsOTmBQ=="
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAuONQzw9oPgtrZhqBvZF286vyFqcflz5Wq6pIXigJhkst4DyFIvi9vEj1+gdP/lXS7hehrGXLWajF3zv4bMkbBbhI+EY5AqEGpdpmTx3yFXRkNB1yqRLOjCv8MKa2mMoA4JnT8lvVC/UGoOhiaNlljiEOaufSSys4SDPUCLHKDGZx7RNVk/2yR2qdsOTmBQ=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421512,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
      "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421512,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2DQcHH1WaQK3Xua2kYst1drtuJ6dr2MeK8ER5CU4eD4RXxwmfQ",
      "balance": 40000000000000
    },
    {
      "account": "ak_2G3WLhVMSftmCscRpSuDnu21hx8qSPJA6JK9QYSuoMNefM29mg",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421511,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421511,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAaXagQVTdeP9ZaUQTmc4VnzwzJ2JKU602LlcncQSkFvJiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAuONQzw9oPgtrZhqBvZF286vyFqcflz5Wq6pIXigJhkst4DyFIvi9vEj1+gdP/lXS7hehrGXLWajF3zv4bMkbBbhI+EY5AqEGpdpmTx3yFXRkNB1yqRLOjCv8MKa2mMoA4JnT8lvVC/UGoOhiaNlljiEOaufSSys4SDPUCLHKDGZx7RNVk/2yR2qdsOTmBQ==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCl2oEFU3Xj/WWlEE5nOFZ88MydiSlOtNi5XJ3EEpBbyYvKCgEAhj+qJSJgALDvQAGgn94n4uvunCYrqNE+7ogF+ey+Hcl3hhSTjOYB1i5QhxOLygoBAIYkYTnKgAAHJl44"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421510,
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
  "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
  "id": -576460752303421510,
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
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421509,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### initiator closes WebSocket connection

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2G3Vjg7ki9S6wjYqBv1eTQfKqUEjkPfrAUN6fPEEN3ANzhsmvt",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection
