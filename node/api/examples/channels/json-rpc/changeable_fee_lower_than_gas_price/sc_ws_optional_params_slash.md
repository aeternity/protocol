
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator
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
      "fsm_id": "ba_pvQs6fXh9U6jwbHyoaw2qlFvBsGDMEhRXLhL6/xTlkPCj6gS"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder
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
      "fsm_id": "ba_LDU2BntA9/AEn5TquTvUiLoQOzWBC2An9nrclL/qLKr1f1nh"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBjX57noo=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422335,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEBJ9qQccyAT9ucGYWYVwLj5hvGPACyLtIFHQ7GqX9GEOtCjOAF3YIgRlc2XEvvqBG2CiT7oCOEc4PEvfNa0B9wLuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgY3e1i20"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422335,
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "fsm_id": "ba_LDU2BntA9/AEn5TquTvUiLoQOzWBC2An9nrclL/qLKr1f1nh",
      "signed_tx": "tx_+MwLAfhCuEBJ9qQccyAT9ucGYWYVwLj5hvGPACyLtIFHQ7GqX9GEOtCjOAF3YIgRlc2XEvvqBG2CiT7oCOEc4PEvfNa0B9wLuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgY3e1i20",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422334,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAAslKsfmqV3E7ZkbQ6SsEgaWkuM889U0JaUkbHVj8t3xNekSCegZEYlJdhBLMkcwwCQLgJ1Jb2mjI3MIYh2SFC7hASfakHHMgE/bnBmFmFcC4+YbxjwAsi7SBR0Oxql/RhDrQozgBd2CIEZXNlxL76gRtgok+6AjhHODxL3zWtAfcC7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GNiFCVhQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
  "id": -576460752303422334,
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAAslKsfmqV3E7ZkbQ6SsEgaWkuM889U0JaUkbHVj8t3xNekSCegZEYlJdhBLMkcwwCQLgJ1Jb2mjI3MIYh2SFC7hASfakHHMgE/bnBmFmFcC4+YbxjwAsi7SBR0Oxql/RhDrQozgBd2CIEZXNlxL76gRtgok+6AjhHODxL3zWtAfcC7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GNiFCVhQ==",
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_pvQs6fXh9U6jwbHyoaw2qlFvBsGDMEhRXLhL6/xTlkPCj6gS"
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAAslKsfmqV3E7ZkbQ6SsEgaWkuM889U0JaUkbHVj8t3xNekSCegZEYlJdhBLMkcwwCQLgJ1Jb2mjI3MIYh2SFC7hASfakHHMgE/bnBmFmFcC4+YbxjwAsi7SBR0Oxql/RhDrQozgBd2CIEZXNlxL76gRtgok+6AjhHODxL3zWtAfcC7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GNiFCVhQ==",
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAAslKsfmqV3E7ZkbQ6SsEgaWkuM889U0JaUkbHVj8t3xNekSCegZEYlJdhBLMkcwwCQLgJ1Jb2mjI3MIYh2SFC7hASfakHHMgE/bnBmFmFcC4+YbxjwAsi7SBR0Oxql/RhDrQozgBd2CIEZXNlxL76gRtgok+6AjhHODxL3zWtAfcC7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GNiFCVhQ==",
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAAslKsfmqV3E7ZkbQ6SsEgaWkuM889U0JaUkbHVj8t3xNekSCegZEYlJdhBLMkcwwCQLgJ1Jb2mjI3MIYh2SFC7hASfakHHMgE/bnBmFmFcC4+YbxjwAsi7SBR0Oxql/RhDrQozgBd2CIEZXNlxL76gRtgok+6AjhHODxL3zWtAfcC7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GNiFCVhQ==",
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "message": {
        "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "message": {
        "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello back",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422333,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
  "id": -576460752303422333,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999999
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "state": "tx_+QEOCwH4hLhAAslKsfmqV3E7ZkbQ6SsEgaWkuM889U0JaUkbHVj8t3xNekSCegZEYlJdhBLMkcwwCQLgJ1Jb2mjI3MIYh2SFC7hASfakHHMgE/bnBmFmFcC4+YbxjwAsi7SBR0Oxql/RhDrQozgBd2CIEZXNlxL76gRtgok+6AjhHODxL3zWtAfcC7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GNiFCVhQ=="
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "state": "tx_+QEOCwH4hLhAAslKsfmqV3E7ZkbQ6SsEgaWkuM889U0JaUkbHVj8t3xNekSCegZEYlJdhBLMkcwwCQLgJ1Jb2mjI3MIYh2SFC7hASfakHHMgE/bnBmFmFcC4+YbxjwAsi7SBR0Oxql/RhDrQozgBd2CIEZXNlxL76gRtgok+6AjhHODxL3zWtAfcC7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GNiFCVhQ=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "poi": "pi_+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMBXVz9I"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422332,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
  "id": -576460752303422332,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999999
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
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
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBv75aW5FwGUmkZmWYjQjTbfvTN6puo/+mhOST69qLk7YAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAidmoEc=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "id": -576460752303422331,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDl7Qczzhw0oDSQSKyJSRZ8OJNyrgrq9LOvQQcuaSduSMTQbLk0Ot1dLhWMkXnXGhOr1eRfVgEbUV3JX0isi3wHuEj4RjkCoQb++WluRcBlJpGZlmI0I02370zeqbqP/poTkk+vai5O2AKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKHdl3Z"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
  "id": -576460752303422331,
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDl7Qczzhw0oDSQSKyJSRZ8OJNyrgrq9LOvQQcuaSduSMTQbLk0Ot1dLhWMkXnXGhOr1eRfVgEbUV3JX0isi3wHuEj4RjkCoQb++WluRcBlJpGZlmI0I02370zeqbqP/poTkk+vai5O2AKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKHdl3Z",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "id": -576460752303422330,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBKB0e9YChvaPtc7SUNyl+3fih4Ouzj/4va/GGheIbW7LW/KSH3Evc5/h9TK9Qju7xwYpNmonZ7yWTJ0pHNIccGuEDl7Qczzhw0oDSQSKyJSRZ8OJNyrgrq9LOvQQcuaSduSMTQbLk0Ot1dLhWMkXnXGhOr1eRfVgEbUV3JX0isi3wHuEj4RjkCoQb++WluRcBlJpGZlmI0I02370zeqbqP/poTkk+vai5O2AKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLzyM/3"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
  "id": -576460752303422330,
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "state": "tx_+NILAfiEuEBKB0e9YChvaPtc7SUNyl+3fih4Ouzj/4va/GGheIbW7LW/KSH3Evc5/h9TK9Qju7xwYpNmonZ7yWTJ0pHNIccGuEDl7Qczzhw0oDSQSKyJSRZ8OJNyrgrq9LOvQQcuaSduSMTQbLk0Ot1dLhWMkXnXGhOr1eRfVgEbUV3JX0isi3wHuEj4RjkCoQb++WluRcBlJpGZlmI0I02370zeqbqP/poTkk+vai5O2AKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLzyM/3"
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "state": "tx_+NILAfiEuEBKB0e9YChvaPtc7SUNyl+3fih4Ouzj/4va/GGheIbW7LW/KSH3Evc5/h9TK9Qju7xwYpNmonZ7yWTJ0pHNIccGuEDl7Qczzhw0oDSQSKyJSRZ8OJNyrgrq9LOvQQcuaSduSMTQbLk0Ot1dLhWMkXnXGhOr1eRfVgEbUV3JX0isi3wHuEj4RjkCoQb++WluRcBlJpGZlmI0I02370zeqbqP/poTkk+vai5O2AKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLzyM/3"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422329,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
  "id": -576460752303422329,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999998
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422328,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
  "id": -576460752303422328,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBKB0e9YChvaPtc7SUNyl+3fih4Ouzj/4va/GGheIbW7LW/KSH3Evc5/h9TK9Qju7xwYpNmonZ7yWTJ0pHNIccGuEDl7Qczzhw0oDSQSKyJSRZ8OJNyrgrq9LOvQQcuaSduSMTQbLk0Ot1dLhWMkXnXGhOr1eRfVgEbUV3JX0isi3wHuEj4RjkCoQb++WluRcBlJpGZlmI0I02370zeqbqP/poTkk+vai5O2AKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLzyM/3",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBKB0e9YChvaPtc7SUNyl+3fih4Ouzj/4va/GGheIbW7LW/KSH3Evc5/h9TK9Qju7xwYpNmonZ7yWTJ0pHNIccGuEDl7Qczzhw0oDSQSKyJSRZ8OJNyrgrq9LOvQQcuaSduSMTQbLk0Ot1dLhWMkXnXGhOr1eRfVgEbUV3JX0isi3wHuEj4RjkCoQb++WluRcBlJpGZlmI0I02370zeqbqP/poTkk+vai5O2AKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLzyM/3",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBKB0e9YChvaPtc7SUNyl+3fih4Ouzj/4va/GGheIbW7LW/KSH3Evc5/h9TK9Qju7xwYpNmonZ7yWTJ0pHNIccGuEDl7Qczzhw0oDSQSKyJSRZ8OJNyrgrq9LOvQQcuaSduSMTQbLk0Ot1dLhWMkXnXGhOr1eRfVgEbUV3JX0isi3wHuEj4RjkCoQb++WluRcBlJpGZlmI0I02370zeqbqP/poTkk+vai5O2AKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLzyM/3",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "event": "closing"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422327,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {
    "fee": 1,
    "gas_price": 1000001234
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
  "id": -576460752303422327,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "signed_tx": "tx_+QJ+CwHAuQJ4+QJ1NwGhBv75aW5FwGUmkZmWYjQjTbfvTN6puo/+mhOST69qLk7YoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuEBKB0e9YChvaPtc7SUNyl+3fih4Ouzj/4va/GGheIbW7LW/KSH3Evc5/h9TK9Qju7xwYpNmonZ7yWTJ0pHNIccGuEDl7Qczzhw0oDSQSKyJSRZ8OJNyrgrq9LOvQQcuaSduSMTQbLk0Ot1dLhWMkXnXGhOr1eRfVgEbUV3JX0isi3wHuEj4RjkCoQb++WluRcBlJpGZlmI0I02370zeqbqP/poTkk+vai5O2AKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgK5AUz5AUk8AfkBP/kBPKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfkBGPhPoA14eXtmmtAgLMK7im7vnzMyk+SGhjFI+PP0nFl1fwFz7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/vhPoKtpUvm9rk5XNeVeyl7wSwAT/ak5C0vFtqH2/EVPjkIA7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAvh0oN3FBkIf34tjXkNZtc8R2KYnFXRfwm1j0hrMi/Rgu+IJ+FGAgICAgKCraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAICAgICAoA14eXtmmtAgLMK7im7vnzMyk+SGhjFI+PP0nFl1fwFzgICAgIDAwMDAwACGGSNyaiFwgY90Qcgk",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.slash_sign",
  "params": {
    "signed_tx": "tx_+QLBCwH4QrhARD5kdLiXySgEDsiRs7lKYydzL9k981wmG28mdJSbprOUCOI+4iI9lgMo12Ib/O72VZKdPP+H/J6db9DJ3mspCbkCePkCdTcBoQb++WluRcBlJpGZlmI0I02370zeqbqP/poTkk+vai5O2KEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhASgdHvWAob2j7XO0lDcpft34oeDrs4/+L2vxhoXiG1uy1vykh9xL3Of4fUyvUI7u8cGKTZqJ2e8lkydKRzSHHBrhA5e0HM84cNKA0kEisiUkWfDiTcq4K6vSzr0EHLmknbkjE0Gy5NDrdXS4VjJF51xoTq9XkX1YBG1FdyV9IrIt8B7hI+EY5AqEG/vlpbkXAZSaRmZZiNCNNt+9M3qm6j/6aE5JPr2ouTtgCoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhhkjcmohcIGPCKt00g=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLBCwH4QrhARD5kdLiXySgEDsiRs7lKYydzL9k981wmG28mdJSbprOUCOI+4iI9lgMo12Ib/O72VZKdPP+H/J6db9DJ3mspCbkCePkCdTcBoQb++WluRcBlJpGZlmI0I02370zeqbqP/poTkk+vai5O2KEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhASgdHvWAob2j7XO0lDcpft34oeDrs4/+L2vxhoXiG1uy1vykh9xL3Of4fUyvUI7u8cGKTZqJ2e8lkydKRzSHHBrhA5e0HM84cNKA0kEisiUkWfDiTcq4K6vSzr0EHLmknbkjE0Gy5NDrdXS4VjJF51xoTq9XkX1YBG1FdyV9IrIt8B7hI+EY5AqEG/vlpbkXAZSaRmZZiNCNNt+9M3qm6j/6aE5JPr2ouTtgCoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhhkjcmohcIGPCKt00g==",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLBCwH4QrhARD5kdLiXySgEDsiRs7lKYydzL9k981wmG28mdJSbprOUCOI+4iI9lgMo12Ib/O72VZKdPP+H/J6db9DJ3mspCbkCePkCdTcBoQb++WluRcBlJpGZlmI0I02370zeqbqP/poTkk+vai5O2KEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhASgdHvWAob2j7XO0lDcpft34oeDrs4/+L2vxhoXiG1uy1vykh9xL3Of4fUyvUI7u8cGKTZqJ2e8lkydKRzSHHBrhA5e0HM84cNKA0kEisiUkWfDiTcq4K6vSzr0EHLmknbkjE0Gy5NDrdXS4VjJF51xoTq9XkX1YBG1FdyV9IrIt8B7hI+EY5AqEG/vlpbkXAZSaRmZZiNCNNt+9M3qm6j/6aE5JPr2ouTtgCoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhhkjcmohcIGPCKt00g==",
      "type": "channel_slash_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBv75aW5FwGUmkZmWYjQjTbfvTN6puo/+mhOST69qLk7YoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/6GJGE5yoACAIYPXtZ/KAA76Lm6Bw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEADrXSiUGmdYcsv8ZvliGRoTcICAxlDIuXBRQa0If13GvbtpUwpnFM9tZgtL+qxariyZmDvX06Ao9AUku29+eYNuF/4XTgBoQb++WluRcBlJpGZlmI0I02370zeqbqP/poTkk+vai5O2KEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAO55N+8Q="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEADrXSiUGmdYcsv8ZvliGRoTcICAxlDIuXBRQa0If13GvbtpUwpnFM9tZgtL+qxariyZmDvX06Ao9AUku29+eYNuF/4XTgBoQb++WluRcBlJpGZlmI0I02370zeqbqP/poTkk+vai5O2KEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAO55N+8Q=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEADrXSiUGmdYcsv8ZvliGRoTcICAxlDIuXBRQa0If13GvbtpUwpnFM9tZgtL+qxariyZmDvX06Ao9AUku29+eYNuF/4XTgBoQb++WluRcBlJpGZlmI0I02370zeqbqP/poTkk+vai5O2KEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAO55N+8Q=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "event": "closed_confirmed"
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
    "channel_id": "ch_2wHyaCqVz9VGzM29nR4twizftCyXV8YQmamEPGZChDpHJav7ea",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator
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
      "fsm_id": "ba_UTTMOPkDp1J8clTTESF2ZAzo+6CCgq/0zK+wiPge0QB16GDg"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder
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
      "fsm_id": "ba_RBbUVlDGtx6oBLJsONTUFq3ex1VBUJrCkA9M+74OVYDMxmGG"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBkDQ9yew=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422326,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEBQd/8zS9lMCwsZysntlHALg0gdt1ePE+F84TsyUzA2Hw6eMchKhiHKounFJ1s/WD31Yaja/aYNS+Hb4Y69nFYMuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgZDGSV03"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422326,
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "fsm_id": "ba_RBbUVlDGtx6oBLJsONTUFq3ex1VBUJrCkA9M+74OVYDMxmGG",
      "signed_tx": "tx_+MwLAfhCuEBQd/8zS9lMCwsZysntlHALg0gdt1ePE+F84TsyUzA2Hw6eMchKhiHKounFJ1s/WD31Yaja/aYNS+Hb4Y69nFYMuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgZDGSV03",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422325,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAUHf/M0vZTAsLGcrJ7ZRwC4NIHbdXjxPhfOE7MlMwNh8OnjHISoYhyqLpxSdbP1g99WGo2v2mDUvh2+GOvZxWDLhAy3y/FQHKVpZXSJj4xVtDqPbQLGBI662bGvD9veagtfQCGFPOUcsljwQbd4uanL3u04ZYbwINGOpe4TghPlocBriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GQO7yKTg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
  "id": -576460752303422325,
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAUHf/M0vZTAsLGcrJ7ZRwC4NIHbdXjxPhfOE7MlMwNh8OnjHISoYhyqLpxSdbP1g99WGo2v2mDUvh2+GOvZxWDLhAy3y/FQHKVpZXSJj4xVtDqPbQLGBI662bGvD9veagtfQCGFPOUcsljwQbd4uanL3u04ZYbwINGOpe4TghPlocBriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GQO7yKTg==",
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_UTTMOPkDp1J8clTTESF2ZAzo+6CCgq/0zK+wiPge0QB16GDg"
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAUHf/M0vZTAsLGcrJ7ZRwC4NIHbdXjxPhfOE7MlMwNh8OnjHISoYhyqLpxSdbP1g99WGo2v2mDUvh2+GOvZxWDLhAy3y/FQHKVpZXSJj4xVtDqPbQLGBI662bGvD9veagtfQCGFPOUcsljwQbd4uanL3u04ZYbwINGOpe4TghPlocBriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GQO7yKTg==",
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAUHf/M0vZTAsLGcrJ7ZRwC4NIHbdXjxPhfOE7MlMwNh8OnjHISoYhyqLpxSdbP1g99WGo2v2mDUvh2+GOvZxWDLhAy3y/FQHKVpZXSJj4xVtDqPbQLGBI662bGvD9veagtfQCGFPOUcsljwQbd4uanL3u04ZYbwINGOpe4TghPlocBriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GQO7yKTg==",
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAUHf/M0vZTAsLGcrJ7ZRwC4NIHbdXjxPhfOE7MlMwNh8OnjHISoYhyqLpxSdbP1g99WGo2v2mDUvh2+GOvZxWDLhAy3y/FQHKVpZXSJj4xVtDqPbQLGBI662bGvD9veagtfQCGFPOUcsljwQbd4uanL3u04ZYbwINGOpe4TghPlocBriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GQO7yKTg==",
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "message": {
        "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "message": {
        "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello back",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422324,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
  "id": -576460752303422324,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999999
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "state": "tx_+QEOCwH4hLhAUHf/M0vZTAsLGcrJ7ZRwC4NIHbdXjxPhfOE7MlMwNh8OnjHISoYhyqLpxSdbP1g99WGo2v2mDUvh2+GOvZxWDLhAy3y/FQHKVpZXSJj4xVtDqPbQLGBI662bGvD9veagtfQCGFPOUcsljwQbd4uanL3u04ZYbwINGOpe4TghPlocBriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GQO7yKTg=="
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "state": "tx_+QEOCwH4hLhAUHf/M0vZTAsLGcrJ7ZRwC4NIHbdXjxPhfOE7MlMwNh8OnjHISoYhyqLpxSdbP1g99WGo2v2mDUvh2+GOvZxWDLhAy3y/FQHKVpZXSJj4xVtDqPbQLGBI662bGvD9veagtfQCGFPOUcsljwQbd4uanL3u04ZYbwINGOpe4TghPlocBriE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GQO7yKTg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "poi": "pi_+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMBXVz9I"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422323,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
  "id": -576460752303422323,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999999
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
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
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqI+Or0cd/At92sr2wUVst1ug1Hx5eNEIMQ2ewspGqghAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAt/AM1A=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "id": -576460752303422322,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDWT+cOZg0t1IetIrTi3u4gMPDNqjl/1YCH4wBr4jxunbsfv7HXsvQ6/WSQVfjbdHRZ8mhpy3lpUcR6LxU4Wa4IuEj4RjkCoQaiPjq9HHfwLfdrK9sFFbLdboNR8eXjRCDENnsLKRqoIQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKT2rFj"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
  "id": -576460752303422322,
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDWT+cOZg0t1IetIrTi3u4gMPDNqjl/1YCH4wBr4jxunbsfv7HXsvQ6/WSQVfjbdHRZ8mhpy3lpUcR6LxU4Wa4IuEj4RjkCoQaiPjq9HHfwLfdrK9sFFbLdboNR8eXjRCDENnsLKRqoIQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKT2rFj",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "id": -576460752303422321,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAUJQU232Lb105kBXsW3TWyPjzmVGF+cCEb1xl6ujAEA/2QAEsSxY4DdOQHBM35zhdDsP7c3nU6N0vFohqpR38MuEDWT+cOZg0t1IetIrTi3u4gMPDNqjl/1YCH4wBr4jxunbsfv7HXsvQ6/WSQVfjbdHRZ8mhpy3lpUcR6LxU4Wa4IuEj4RjkCoQaiPjq9HHfwLfdrK9sFFbLdboNR8eXjRCDENnsLKRqoIQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLtCrmp"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
  "id": -576460752303422321,
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "state": "tx_+NILAfiEuEAUJQU232Lb105kBXsW3TWyPjzmVGF+cCEb1xl6ujAEA/2QAEsSxY4DdOQHBM35zhdDsP7c3nU6N0vFohqpR38MuEDWT+cOZg0t1IetIrTi3u4gMPDNqjl/1YCH4wBr4jxunbsfv7HXsvQ6/WSQVfjbdHRZ8mhpy3lpUcR6LxU4Wa4IuEj4RjkCoQaiPjq9HHfwLfdrK9sFFbLdboNR8eXjRCDENnsLKRqoIQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLtCrmp"
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "state": "tx_+NILAfiEuEAUJQU232Lb105kBXsW3TWyPjzmVGF+cCEb1xl6ujAEA/2QAEsSxY4DdOQHBM35zhdDsP7c3nU6N0vFohqpR38MuEDWT+cOZg0t1IetIrTi3u4gMPDNqjl/1YCH4wBr4jxunbsfv7HXsvQ6/WSQVfjbdHRZ8mhpy3lpUcR6LxU4Wa4IuEj4RjkCoQaiPjq9HHfwLfdrK9sFFbLdboNR8eXjRCDENnsLKRqoIQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLtCrmp"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422320,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
  "id": -576460752303422320,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999998
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422319,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
  "id": -576460752303422319,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAUJQU232Lb105kBXsW3TWyPjzmVGF+cCEb1xl6ujAEA/2QAEsSxY4DdOQHBM35zhdDsP7c3nU6N0vFohqpR38MuEDWT+cOZg0t1IetIrTi3u4gMPDNqjl/1YCH4wBr4jxunbsfv7HXsvQ6/WSQVfjbdHRZ8mhpy3lpUcR6LxU4Wa4IuEj4RjkCoQaiPjq9HHfwLfdrK9sFFbLdboNR8eXjRCDENnsLKRqoIQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLtCrmp",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAUJQU232Lb105kBXsW3TWyPjzmVGF+cCEb1xl6ujAEA/2QAEsSxY4DdOQHBM35zhdDsP7c3nU6N0vFohqpR38MuEDWT+cOZg0t1IetIrTi3u4gMPDNqjl/1YCH4wBr4jxunbsfv7HXsvQ6/WSQVfjbdHRZ8mhpy3lpUcR6LxU4Wa4IuEj4RjkCoQaiPjq9HHfwLfdrK9sFFbLdboNR8eXjRCDENnsLKRqoIQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLtCrmp",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAUJQU232Lb105kBXsW3TWyPjzmVGF+cCEb1xl6ujAEA/2QAEsSxY4DdOQHBM35zhdDsP7c3nU6N0vFohqpR38MuEDWT+cOZg0t1IetIrTi3u4gMPDNqjl/1YCH4wBr4jxunbsfv7HXsvQ6/WSQVfjbdHRZ8mhpy3lpUcR6LxU4Wa4IuEj4RjkCoQaiPjq9HHfwLfdrK9sFFbLdboNR8eXjRCDENnsLKRqoIQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLtCrmp",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "event": "closing"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422318,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {
    "fee": 1,
    "gas_price": 1000001234
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
  "id": -576460752303422318,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBqI+Or0cd/At92sr2wUVst1ug1Hx5eNEIMQ2ewspGqghoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8LjU+NILAfiEuEAUJQU232Lb105kBXsW3TWyPjzmVGF+cCEb1xl6ujAEA/2QAEsSxY4DdOQHBM35zhdDsP7c3nU6N0vFohqpR38MuEDWT+cOZg0t1IetIrTi3u4gMPDNqjl/1YCH4wBr4jxunbsfv7HXsvQ6/WSQVfjbdHRZ8mhpy3lpUcR6LxU4Wa4IuEj4RjkCoQaiPjq9HHfwLfdrK9sFFbLdboNR8eXjRCDENnsLKRqoIQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgK5AUz5AUk8AfkBP/kBPKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfkBGPhPoA14eXtmmtAgLMK7im7vnzMyk+SGhjFI+PP0nFl1fwFz7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/vhPoKtpUvm9rk5XNeVeyl7wSwAT/ak5C0vFtqH2/EVPjkIA7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAvh0oN3FBkIf34tjXkNZtc8R2KYnFXRfwm1j0hrMi/Rgu+IJ+FGAgICAgKCraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAICAgICAoA14eXtmmtAgLMK7im7vnzMyk+SGhjFI+PP0nFl1fwFzgICAgIDAwMDAwACGGR7KUfkIPOlqBAM=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.slash_sign",
  "params": {
    "signed_tx": "tx_+QLACwH4QrhAKzm6ipEoWFGtnVQnvVjbvWCupRusjesmxLlnUl+85ddNce7EuW9kTS+vlwjOKr4+kZhHImKndmBwz72F62VsC7kCd/kCdDcBoQaiPjq9HHfwLfdrK9sFFbLdboNR8eXjRCDENnsLKRqoIaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAFCUFNt9i29dOZAV7Ft01sj485lRhfnAhG9cZerowBAP9kABLEsWOA3TkBwTN+c4XQ7D+3N51OjdLxaIaqUd/DLhA1k/nDmYNLdSHrSK04t7uIDDwzao5f9WAh+MAa+I8bp27H7+x17L0Ov1kkFX423R0WfJoact5aVHEei8VOFmuCLhI+EY5AqEGoj46vRx38C33ayvbBRWy3W6DUfHl40QgxDZ7CykaqCECoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhhkeylH5CDwGW2nE"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAKzm6ipEoWFGtnVQnvVjbvWCupRusjesmxLlnUl+85ddNce7EuW9kTS+vlwjOKr4+kZhHImKndmBwz72F62VsC7kCd/kCdDcBoQaiPjq9HHfwLfdrK9sFFbLdboNR8eXjRCDENnsLKRqoIaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAFCUFNt9i29dOZAV7Ft01sj485lRhfnAhG9cZerowBAP9kABLEsWOA3TkBwTN+c4XQ7D+3N51OjdLxaIaqUd/DLhA1k/nDmYNLdSHrSK04t7uIDDwzao5f9WAh+MAa+I8bp27H7+x17L0Ov1kkFX423R0WfJoact5aVHEei8VOFmuCLhI+EY5AqEGoj46vRx38C33ayvbBRWy3W6DUfHl40QgxDZ7CykaqCECoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhhkeylH5CDwGW2nE",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAKzm6ipEoWFGtnVQnvVjbvWCupRusjesmxLlnUl+85ddNce7EuW9kTS+vlwjOKr4+kZhHImKndmBwz72F62VsC7kCd/kCdDcBoQaiPjq9HHfwLfdrK9sFFbLdboNR8eXjRCDENnsLKRqoIaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAFCUFNt9i29dOZAV7Ft01sj485lRhfnAhG9cZerowBAP9kABLEsWOA3TkBwTN+c4XQ7D+3N51OjdLxaIaqUd/DLhA1k/nDmYNLdSHrSK04t7uIDDwzao5f9WAh+MAa+I8bp27H7+x17L0Ov1kkFX423R0WfJoact5aVHEei8VOFmuCLhI+EY5AqEGoj46vRx38C33ayvbBRWy3W6DUfHl40QgxDZ7CykaqCECoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhhkeylH5CDwGW2nE",
      "type": "channel_slash_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBqI+Or0cd/At92sr2wUVst1ug1Hx5eNEIMQ2ewspGqghoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/6GJGE5yoACAIYPXtZ/KAA9ZqZ8+g==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEApZr28x2NR+j420+jxKf+WTVCvqZ1qnasDVH5xHfDdwfr3n+CU8UIIAYA+7GkM54fUnrdlKnFz38DsO3uRbHgHuF/4XTgBoQaiPjq9HHfwLfdrK9sFFbLdboNR8eXjRCDENnsLKRqoIaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAPU0g3hw="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEApZr28x2NR+j420+jxKf+WTVCvqZ1qnasDVH5xHfDdwfr3n+CU8UIIAYA+7GkM54fUnrdlKnFz38DsO3uRbHgHuF/4XTgBoQaiPjq9HHfwLfdrK9sFFbLdboNR8eXjRCDENnsLKRqoIaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAPU0g3hw=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEApZr28x2NR+j420+jxKf+WTVCvqZ1qnasDVH5xHfDdwfr3n+CU8UIIAYA+7GkM54fUnrdlKnFz38DsO3uRbHgHuF/4XTgBoQaiPjq9HHfwLfdrK9sFFbLdboNR8eXjRCDENnsLKRqoIaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAPU0g3hw=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "event": "closed_confirmed"
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
    "channel_id": "ch_2ETHM3r1oCm8ofv2SNMh6A2F87RdwZDJjukpp6PP1iaPbg2iuC",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator closes WebSocket connection
