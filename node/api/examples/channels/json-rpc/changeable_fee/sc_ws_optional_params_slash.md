
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
      "fsm_id": "ba_Phpw2RQu5ix2AZbuTO/USnu0bKmERLwhSNZ/RklyCsoCNBJ6"
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
      "fsm_id": "ba_+ioiZlGrtUvsKIcZ5kNq4Pq33/WZQziaMfSdoblosWsttOKe"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtFcD5i5A==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422611,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDday6OpMSJ9NHlduzdrTSougOnhi8NnnETspeIgFpk2djWgf/we5zANGPrOO+gUbnjl2XYqM0Gj5I9l8DCB2gPuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LRWd4t/E="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422611,
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
    "data": {
      "fsm_id": "ba_+ioiZlGrtUvsKIcZ5kNq4Pq33/WZQziaMfSdoblosWsttOKe",
      "signed_tx": "tx_+MsLAfhCuEDday6OpMSJ9NHlduzdrTSougOnhi8NnnETspeIgFpk2djWgf/we5zANGPrOO+gUbnjl2XYqM0Gj5I9l8DCB2gPuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LRWd4t/E=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422610,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAEjvNAaqpKjTX24beZD+0iJNpE+ZLyISNPO2TtrzrsA0dxascEFrtAOtT9rloHwtxkOjftzlVGb/bwUw/cmNICrhA3WsujqTEifTR5Xbs3a00qLoDp4YvDZ5xE7KXiIBaZNnY1oH/8HucwDRj6zjvoFG545dl2KjNBo+SPZfAwgdoD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0UNkHuk"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
  "id": -576460752303422610,
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAEjvNAaqpKjTX24beZD+0iJNpE+ZLyISNPO2TtrzrsA0dxascEFrtAOtT9rloHwtxkOjftzlVGb/bwUw/cmNICrhA3WsujqTEifTR5Xbs3a00qLoDp4YvDZ5xE7KXiIBaZNnY1oH/8HucwDRj6zjvoFG545dl2KjNBo+SPZfAwgdoD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0UNkHuk",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_Phpw2RQu5ix2AZbuTO/USnu0bKmERLwhSNZ/RklyCsoCNBJ6"
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAEjvNAaqpKjTX24beZD+0iJNpE+ZLyISNPO2TtrzrsA0dxascEFrtAOtT9rloHwtxkOjftzlVGb/bwUw/cmNICrhA3WsujqTEifTR5Xbs3a00qLoDp4YvDZ5xE7KXiIBaZNnY1oH/8HucwDRj6zjvoFG545dl2KjNBo+SPZfAwgdoD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0UNkHuk",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAEjvNAaqpKjTX24beZD+0iJNpE+ZLyISNPO2TtrzrsA0dxascEFrtAOtT9rloHwtxkOjftzlVGb/bwUw/cmNICrhA3WsujqTEifTR5Xbs3a00qLoDp4YvDZ5xE7KXiIBaZNnY1oH/8HucwDRj6zjvoFG545dl2KjNBo+SPZfAwgdoD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0UNkHuk",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAEjvNAaqpKjTX24beZD+0iJNpE+ZLyISNPO2TtrzrsA0dxascEFrtAOtT9rloHwtxkOjftzlVGb/bwUw/cmNICrhA3WsujqTEifTR5Xbs3a00qLoDp4YvDZ5xE7KXiIBaZNnY1oH/8HucwDRj6zjvoFG545dl2KjNBo+SPZfAwgdoD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0UNkHuk",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
    "data": {
      "message": {
        "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
    "data": {
      "message": {
        "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
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
  "id": -576460752303422609,
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
  "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
  "id": -576460752303422609,
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
    "data": {
      "state": "tx_+QENCwH4hLhAEjvNAaqpKjTX24beZD+0iJNpE+ZLyISNPO2TtrzrsA0dxascEFrtAOtT9rloHwtxkOjftzlVGb/bwUw/cmNICrhA3WsujqTEifTR5Xbs3a00qLoDp4YvDZ5xE7KXiIBaZNnY1oH/8HucwDRj6zjvoFG545dl2KjNBo+SPZfAwgdoD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0UNkHuk"
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
    "data": {
      "state": "tx_+QENCwH4hLhAEjvNAaqpKjTX24beZD+0iJNpE+ZLyISNPO2TtrzrsA0dxascEFrtAOtT9rloHwtxkOjftzlVGb/bwUw/cmNICrhA3WsujqTEifTR5Xbs3a00qLoDp4YvDZ5xE7KXiIBaZNnY1oH/8HucwDRj6zjvoFG545dl2KjNBo+SPZfAwgdoD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0UNkHuk"
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
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
  "id": -576460752303422608,
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
  "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
  "id": -576460752303422608,
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBqCnI8a6HrLcB/I83zNnurQekb+5AzjOwTZjg5uSST7vAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAu9FsuA=",
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
  "id": -576460752303422607,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAAWlHsSLHRp/9nOiI7cr2PKKMh+lPJ0GYHRRkdtsDGStQ20Ih2MqGcQJuwNYUaYYM3D7yrbEAhXiB7qbjHIdELuEj4RjkCoQagpyPGuh6y3AfyPN8zZ7q0HpG/uQM4zsE2Y4Obkkk+7wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJWcJF7"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
  "id": -576460752303422607,
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAAWlHsSLHRp/9nOiI7cr2PKKMh+lPJ0GYHRRkdtsDGStQ20Ih2MqGcQJuwNYUaYYM3D7yrbEAhXiB7qbjHIdELuEj4RjkCoQagpyPGuh6y3AfyPN8zZ7q0HpG/uQM4zsE2Y4Obkkk+7wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJWcJF7",
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
  "id": -576460752303422606,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAAWlHsSLHRp/9nOiI7cr2PKKMh+lPJ0GYHRRkdtsDGStQ20Ih2MqGcQJuwNYUaYYM3D7yrbEAhXiB7qbjHIdELuEDaAg+v4EPS9BT7QOb/W7eU9h5dxuL4t0avURn2Ekoxel/SMLK+MeppVEUakrNugamLwuZ6alT7jWSZ9gEShL4FuEj4RjkCoQagpyPGuh6y3AfyPN8zZ7q0HpG/uQM4zsE2Y4Obkkk+7wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJhYXBv"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
  "id": -576460752303422606,
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
    "data": {
      "state": "tx_+NILAfiEuEAAWlHsSLHRp/9nOiI7cr2PKKMh+lPJ0GYHRRkdtsDGStQ20Ih2MqGcQJuwNYUaYYM3D7yrbEAhXiB7qbjHIdELuEDaAg+v4EPS9BT7QOb/W7eU9h5dxuL4t0avURn2Ekoxel/SMLK+MeppVEUakrNugamLwuZ6alT7jWSZ9gEShL4FuEj4RjkCoQagpyPGuh6y3AfyPN8zZ7q0HpG/uQM4zsE2Y4Obkkk+7wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJhYXBv"
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
    "data": {
      "state": "tx_+NILAfiEuEAAWlHsSLHRp/9nOiI7cr2PKKMh+lPJ0GYHRRkdtsDGStQ20Ih2MqGcQJuwNYUaYYM3D7yrbEAhXiB7qbjHIdELuEDaAg+v4EPS9BT7QOb/W7eU9h5dxuL4t0avURn2Ekoxel/SMLK+MeppVEUakrNugamLwuZ6alT7jWSZ9gEShL4FuEj4RjkCoQagpyPGuh6y3AfyPN8zZ7q0HpG/uQM4zsE2Y4Obkkk+7wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJhYXBv"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422605,
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
  "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
  "id": -576460752303422605,
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
  "id": -576460752303422604,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
  "id": -576460752303422604,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAAWlHsSLHRp/9nOiI7cr2PKKMh+lPJ0GYHRRkdtsDGStQ20Ih2MqGcQJuwNYUaYYM3D7yrbEAhXiB7qbjHIdELuEDaAg+v4EPS9BT7QOb/W7eU9h5dxuL4t0avURn2Ekoxel/SMLK+MeppVEUakrNugamLwuZ6alT7jWSZ9gEShL4FuEj4RjkCoQagpyPGuh6y3AfyPN8zZ7q0HpG/uQM4zsE2Y4Obkkk+7wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJhYXBv",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAAWlHsSLHRp/9nOiI7cr2PKKMh+lPJ0GYHRRkdtsDGStQ20Ih2MqGcQJuwNYUaYYM3D7yrbEAhXiB7qbjHIdELuEDaAg+v4EPS9BT7QOb/W7eU9h5dxuL4t0avURn2Ekoxel/SMLK+MeppVEUakrNugamLwuZ6alT7jWSZ9gEShL4FuEj4RjkCoQagpyPGuh6y3AfyPN8zZ7q0HpG/uQM4zsE2Y4Obkkk+7wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJhYXBv",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAAWlHsSLHRp/9nOiI7cr2PKKMh+lPJ0GYHRRkdtsDGStQ20Ih2MqGcQJuwNYUaYYM3D7yrbEAhXiB7qbjHIdELuEDaAg+v4EPS9BT7QOb/W7eU9h5dxuL4t0avURn2Ekoxel/SMLK+MeppVEUakrNugamLwuZ6alT7jWSZ9gEShL4FuEj4RjkCoQagpyPGuh6y3AfyPN8zZ7q0HpG/uQM4zsE2Y4Obkkk+7wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJhYXBv",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
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
  "id": -576460752303422603,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {
    "fee": 123456789876543
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
  "id": -576460752303422603,
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBqCnI8a6HrLcB/I83zNnurQekb+5AzjOwTZjg5uSST7voQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuEAAWlHsSLHRp/9nOiI7cr2PKKMh+lPJ0GYHRRkdtsDGStQ20Ih2MqGcQJuwNYUaYYM3D7yrbEAhXiB7qbjHIdELuEDaAg+v4EPS9BT7QOb/W7eU9h5dxuL4t0avURn2Ekoxel/SMLK+MeppVEUakrNugamLwuZ6alT7jWSZ9gEShL4FuEj4RjkCoQagpyPGuh6y3AfyPN8zZ7q0HpG/uQM4zsE2Y4Obkkk+7wKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgK5AUz5AUk8AfkBP/kBPKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfkBGPhPoA14eXtmmtAgLMK7im7vnzMyk+SGhjFI+PP0nFl1fwFz7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/vhPoKtpUvm9rk5XNeVeyl7wSwAT/ak5C0vFtqH2/EVPjkIA7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAvh0oN3FBkIf34tjXkNZtc8R2KYnFXRfwm1j0hrMi/Rgu+IJ+FGAgICAgKCraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAICAgICAoA14eXtmmtAgLMK7im7vnzMyk+SGhjFI+PP0nFl1fwFzgICAgIDAwMDAwACGcEiGGw8/R/Vp6GM=",
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
    "signed_tx": "tx_+QLACwH4QrhA/tnA4NXx9hPStOgELMODPdO9Vkr6y3df0EV6GyFidvyh8YTto63nRyt7GXbIr3kryiA94F0kzOvOGydfFPp1D7kCd/kCdDcBoQagpyPGuh6y3AfyPN8zZ7q0HpG/uQM4zsE2Y4Obkkk+76EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAAFpR7Eix0af/ZzoiO3K9jyijIfpTydBmB0UZHbbAxkrUNtCIdjKhnECbsDWFGmGDNw+8q2xAIV4ge6m4xyHRC7hA2gIPr+BD0vQU+0Dm/1u3lPYeXcbi+LdGr1EZ9hJKMXpf0jCyvjHqaVRFGpKzboGpi8LmempU+41kmfYBEoS+BbhI+EY5AqEGoKcjxroestwH8jzfM2e6tB6Rv7kDOM7BNmODm5JJPu8CoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhnBIhhsPP0dnRyxt"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhA/tnA4NXx9hPStOgELMODPdO9Vkr6y3df0EV6GyFidvyh8YTto63nRyt7GXbIr3kryiA94F0kzOvOGydfFPp1D7kCd/kCdDcBoQagpyPGuh6y3AfyPN8zZ7q0HpG/uQM4zsE2Y4Obkkk+76EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAAFpR7Eix0af/ZzoiO3K9jyijIfpTydBmB0UZHbbAxkrUNtCIdjKhnECbsDWFGmGDNw+8q2xAIV4ge6m4xyHRC7hA2gIPr+BD0vQU+0Dm/1u3lPYeXcbi+LdGr1EZ9hJKMXpf0jCyvjHqaVRFGpKzboGpi8LmempU+41kmfYBEoS+BbhI+EY5AqEGoKcjxroestwH8jzfM2e6tB6Rv7kDOM7BNmODm5JJPu8CoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhnBIhhsPP0dnRyxt",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhA/tnA4NXx9hPStOgELMODPdO9Vkr6y3df0EV6GyFidvyh8YTto63nRyt7GXbIr3kryiA94F0kzOvOGydfFPp1D7kCd/kCdDcBoQagpyPGuh6y3AfyPN8zZ7q0HpG/uQM4zsE2Y4Obkkk+76EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAAFpR7Eix0af/ZzoiO3K9jyijIfpTydBmB0UZHbbAxkrUNtCIdjKhnECbsDWFGmGDNw+8q2xAIV4ge6m4xyHRC7hA2gIPr+BD0vQU+0Dm/1u3lPYeXcbi+LdGr1EZ9hJKMXpf0jCyvjHqaVRFGpKzboGpi8LmempU+41kmfYBEoS+BbhI+EY5AqEGoKcjxroestwH8jzfM2e6tB6Rv7kDOM7BNmODm5JJPu8CoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhnBIhhsPP0dnRyxt",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBqCnI8a6HrLcB/I83zNnurQekb+5AzjOwTZjg5uSST7voQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/6GJGE5yoACAIYPXtZ/KAAdOx41MQ==",
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
    "signed_tx": "tx_+KcLAfhCuEAnICsnoPv6TXO2z8VgTj1bDEQpteOw4AfUqnvKLukRDQA7+L0i8ulMrapiR+SJXQrs4awjt+aI/k7HIe/YbYYAuF/4XTgBoQagpyPGuh6y3AfyPN8zZ7q0HpG/uQM4zsE2Y4Obkkk+76EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAHfzFveU="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEAnICsnoPv6TXO2z8VgTj1bDEQpteOw4AfUqnvKLukRDQA7+L0i8ulMrapiR+SJXQrs4awjt+aI/k7HIe/YbYYAuF/4XTgBoQagpyPGuh6y3AfyPN8zZ7q0HpG/uQM4zsE2Y4Obkkk+76EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAHfzFveU=",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEAnICsnoPv6TXO2z8VgTj1bDEQpteOw4AfUqnvKLukRDQA7+L0i8ulMrapiR+SJXQrs4awjt+aI/k7HIe/YbYYAuF/4XTgBoQagpyPGuh6y3AfyPN8zZ7q0HpG/uQM4zsE2Y4Obkkk+76EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAHfzFveU=",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
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
    "channel_id": "ch_2DkfRUQ2kgoWJFNfysXUnZNtdhJk7dvQhSub2ScHih4hQiQJFj",
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
      "fsm_id": "ba_WDCWGA7y35l++DPzBIvR7uH17i3NRiBpYu0kfYf5V/s8xypZ"
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
      "fsm_id": "ba_XuIyr8QdHbiW7/DiDxmY0der6bo6nO2PVAhpyhS5a2frEbcH"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtIPfWpTA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422602,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAQ8pAfA39/TNh8XIvIG9zcF8k5gSU+fEtuBChSQqd0aXCPhdWBAGFzhhlzR/MSgps1L5MhyOeitdp/q0Lf2jwBuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LSIX3uAw="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422602,
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
    "data": {
      "fsm_id": "ba_XuIyr8QdHbiW7/DiDxmY0der6bo6nO2PVAhpyhS5a2frEbcH",
      "signed_tx": "tx_+MsLAfhCuEAQ8pAfA39/TNh8XIvIG9zcF8k5gSU+fEtuBChSQqd0aXCPhdWBAGFzhhlzR/MSgps1L5MhyOeitdp/q0Lf2jwBuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LSIX3uAw=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422601,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhADzLKmXGOgVTiP9t2zXTl9IdYG5MeQzXig6zNS00ZBQT6Evi7xrH3/Q+Oq4DRzDXfx5EbmSxW/B7mM6SliqIOBLhAEPKQHwN/f0zYfFyLyBvc3BfJOYElPnxLbgQoUkKndGlwj4XVgQBhc4YZc0fzEoKbNS+TIcjnorXaf6tC39o8AbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0j2lCO5"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
  "id": -576460752303422601,
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhADzLKmXGOgVTiP9t2zXTl9IdYG5MeQzXig6zNS00ZBQT6Evi7xrH3/Q+Oq4DRzDXfx5EbmSxW/B7mM6SliqIOBLhAEPKQHwN/f0zYfFyLyBvc3BfJOYElPnxLbgQoUkKndGlwj4XVgQBhc4YZc0fzEoKbNS+TIcjnorXaf6tC39o8AbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0j2lCO5",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_WDCWGA7y35l++DPzBIvR7uH17i3NRiBpYu0kfYf5V/s8xypZ"
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhADzLKmXGOgVTiP9t2zXTl9IdYG5MeQzXig6zNS00ZBQT6Evi7xrH3/Q+Oq4DRzDXfx5EbmSxW/B7mM6SliqIOBLhAEPKQHwN/f0zYfFyLyBvc3BfJOYElPnxLbgQoUkKndGlwj4XVgQBhc4YZc0fzEoKbNS+TIcjnorXaf6tC39o8AbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0j2lCO5",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhADzLKmXGOgVTiP9t2zXTl9IdYG5MeQzXig6zNS00ZBQT6Evi7xrH3/Q+Oq4DRzDXfx5EbmSxW/B7mM6SliqIOBLhAEPKQHwN/f0zYfFyLyBvc3BfJOYElPnxLbgQoUkKndGlwj4XVgQBhc4YZc0fzEoKbNS+TIcjnorXaf6tC39o8AbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0j2lCO5",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhADzLKmXGOgVTiP9t2zXTl9IdYG5MeQzXig6zNS00ZBQT6Evi7xrH3/Q+Oq4DRzDXfx5EbmSxW/B7mM6SliqIOBLhAEPKQHwN/f0zYfFyLyBvc3BfJOYElPnxLbgQoUkKndGlwj4XVgQBhc4YZc0fzEoKbNS+TIcjnorXaf6tC39o8AbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0j2lCO5",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
    "data": {
      "message": {
        "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
    "data": {
      "message": {
        "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
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
  "id": -576460752303422600,
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
  "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
  "id": -576460752303422600,
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
    "data": {
      "state": "tx_+QENCwH4hLhADzLKmXGOgVTiP9t2zXTl9IdYG5MeQzXig6zNS00ZBQT6Evi7xrH3/Q+Oq4DRzDXfx5EbmSxW/B7mM6SliqIOBLhAEPKQHwN/f0zYfFyLyBvc3BfJOYElPnxLbgQoUkKndGlwj4XVgQBhc4YZc0fzEoKbNS+TIcjnorXaf6tC39o8AbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0j2lCO5"
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
    "data": {
      "state": "tx_+QENCwH4hLhADzLKmXGOgVTiP9t2zXTl9IdYG5MeQzXig6zNS00ZBQT6Evi7xrH3/Q+Oq4DRzDXfx5EbmSxW/B7mM6SliqIOBLhAEPKQHwN/f0zYfFyLyBvc3BfJOYElPnxLbgQoUkKndGlwj4XVgQBhc4YZc0fzEoKbNS+TIcjnorXaf6tC39o8AbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0j2lCO5"
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
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
  "id": -576460752303422599,
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
  "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
  "id": -576460752303422599,
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBr6Q3FqbEnf4kVWQ9JVv101bLgFyfX8jZ7hBus5cdTmhAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAvpWco0=",
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
  "id": -576460752303422598,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB96/n4vwQcZNV/oTjtPUmLwtqhs2B9t/tEeMTZXEAYBdQtvyDdgfsvSNdh9O2KCrpsH4xrGbJDUXc01ZyuNKINuEj4RjkCoQa+kNxamxJ3+JFVkPSVb9dNWy4Bcn1/I2e4QbrOXHU5oQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKgfN7p"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
  "id": -576460752303422598,
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB96/n4vwQcZNV/oTjtPUmLwtqhs2B9t/tEeMTZXEAYBdQtvyDdgfsvSNdh9O2KCrpsH4xrGbJDUXc01ZyuNKINuEj4RjkCoQa+kNxamxJ3+JFVkPSVb9dNWy4Bcn1/I2e4QbrOXHU5oQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKgfN7p",
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
  "id": -576460752303422597,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEB96/n4vwQcZNV/oTjtPUmLwtqhs2B9t/tEeMTZXEAYBdQtvyDdgfsvSNdh9O2KCrpsH4xrGbJDUXc01ZyuNKINuECFxgvdjfA5d6O/ju41S1U/xj9RfxMU9JJV6QlVHMSK/BaCYAdYIIMB39R9E3CzSjkib7j3S5jHTWMlSbbP+48KuEj4RjkCoQa+kNxamxJ3+JFVkPSVb9dNWy4Bcn1/I2e4QbrOXHU5oQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKhFruV"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
  "id": -576460752303422597,
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
    "data": {
      "state": "tx_+NILAfiEuEB96/n4vwQcZNV/oTjtPUmLwtqhs2B9t/tEeMTZXEAYBdQtvyDdgfsvSNdh9O2KCrpsH4xrGbJDUXc01ZyuNKINuECFxgvdjfA5d6O/ju41S1U/xj9RfxMU9JJV6QlVHMSK/BaCYAdYIIMB39R9E3CzSjkib7j3S5jHTWMlSbbP+48KuEj4RjkCoQa+kNxamxJ3+JFVkPSVb9dNWy4Bcn1/I2e4QbrOXHU5oQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKhFruV"
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
    "data": {
      "state": "tx_+NILAfiEuEB96/n4vwQcZNV/oTjtPUmLwtqhs2B9t/tEeMTZXEAYBdQtvyDdgfsvSNdh9O2KCrpsH4xrGbJDUXc01ZyuNKINuECFxgvdjfA5d6O/ju41S1U/xj9RfxMU9JJV6QlVHMSK/BaCYAdYIIMB39R9E3CzSjkib7j3S5jHTWMlSbbP+48KuEj4RjkCoQa+kNxamxJ3+JFVkPSVb9dNWy4Bcn1/I2e4QbrOXHU5oQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKhFruV"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422596,
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
  "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
  "id": -576460752303422596,
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
  "id": -576460752303422595,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
  "id": -576460752303422595,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEB96/n4vwQcZNV/oTjtPUmLwtqhs2B9t/tEeMTZXEAYBdQtvyDdgfsvSNdh9O2KCrpsH4xrGbJDUXc01ZyuNKINuECFxgvdjfA5d6O/ju41S1U/xj9RfxMU9JJV6QlVHMSK/BaCYAdYIIMB39R9E3CzSjkib7j3S5jHTWMlSbbP+48KuEj4RjkCoQa+kNxamxJ3+JFVkPSVb9dNWy4Bcn1/I2e4QbrOXHU5oQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKhFruV",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEB96/n4vwQcZNV/oTjtPUmLwtqhs2B9t/tEeMTZXEAYBdQtvyDdgfsvSNdh9O2KCrpsH4xrGbJDUXc01ZyuNKINuECFxgvdjfA5d6O/ju41S1U/xj9RfxMU9JJV6QlVHMSK/BaCYAdYIIMB39R9E3CzSjkib7j3S5jHTWMlSbbP+48KuEj4RjkCoQa+kNxamxJ3+JFVkPSVb9dNWy4Bcn1/I2e4QbrOXHU5oQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKhFruV",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEB96/n4vwQcZNV/oTjtPUmLwtqhs2B9t/tEeMTZXEAYBdQtvyDdgfsvSNdh9O2KCrpsH4xrGbJDUXc01ZyuNKINuECFxgvdjfA5d6O/ju41S1U/xj9RfxMU9JJV6QlVHMSK/BaCYAdYIIMB39R9E3CzSjkib7j3S5jHTWMlSbbP+48KuEj4RjkCoQa+kNxamxJ3+JFVkPSVb9dNWy4Bcn1/I2e4QbrOXHU5oQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKhFruV",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
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
  "id": -576460752303422594,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {
    "fee": 123456789876543
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
  "id": -576460752303422594,
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBr6Q3FqbEnf4kVWQ9JVv101bLgFyfX8jZ7hBus5cdTmhoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8LjU+NILAfiEuEB96/n4vwQcZNV/oTjtPUmLwtqhs2B9t/tEeMTZXEAYBdQtvyDdgfsvSNdh9O2KCrpsH4xrGbJDUXc01ZyuNKINuECFxgvdjfA5d6O/ju41S1U/xj9RfxMU9JJV6QlVHMSK/BaCYAdYIIMB39R9E3CzSjkib7j3S5jHTWMlSbbP+48KuEj4RjkCoQa+kNxamxJ3+JFVkPSVb9dNWy4Bcn1/I2e4QbrOXHU5oQKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgK5AUz5AUk8AfkBP/kBPKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfkBGPhPoA14eXtmmtAgLMK7im7vnzMyk+SGhjFI+PP0nFl1fwFz7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/vhPoKtpUvm9rk5XNeVeyl7wSwAT/ak5C0vFtqH2/EVPjkIA7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAvh0oN3FBkIf34tjXkNZtc8R2KYnFXRfwm1j0hrMi/Rgu+IJ+FGAgICAgKCraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAICAgICAoA14eXtmmtAgLMK7im7vnzMyk+SGhjFI+PP0nFl1fwFzgICAgIDAwMDAwACGcEiGGw8/Hsrytt8=",
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
    "signed_tx": "tx_+QLACwH4QrhAXcRy9ELWJ5NHOxKQK2ShD4gtUZ2hfdyQTf+wCziw8wd+5I9bGnk96fVQLglxL2dNc+shiUBZA5LxH76LDT8jCLkCd/kCdDcBoQa+kNxamxJ3+JFVkPSVb9dNWy4Bcn1/I2e4QbrOXHU5oaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAfev5+L8EHGTVf6E47T1Ji8LaobNgfbf7RHjE2VxAGAXULb8g3YH7L0jXYfTtigq6bB+MaxmyQ1F3NNWcrjSiDbhAhcYL3Y3wOXejv47uNUtVP8Y/UX8TFPSSVekJVRzEivwWgmAHWCCDAd/UfRNws0o5Im+490uYx01jJUm2z/uPCrhI+EY5AqEGvpDcWpsSd/iRVZD0lW/XTVsuAXJ9fyNnuEG6zlx1OaECoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhnBIhhsPPx4MoTtf"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAXcRy9ELWJ5NHOxKQK2ShD4gtUZ2hfdyQTf+wCziw8wd+5I9bGnk96fVQLglxL2dNc+shiUBZA5LxH76LDT8jCLkCd/kCdDcBoQa+kNxamxJ3+JFVkPSVb9dNWy4Bcn1/I2e4QbrOXHU5oaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAfev5+L8EHGTVf6E47T1Ji8LaobNgfbf7RHjE2VxAGAXULb8g3YH7L0jXYfTtigq6bB+MaxmyQ1F3NNWcrjSiDbhAhcYL3Y3wOXejv47uNUtVP8Y/UX8TFPSSVekJVRzEivwWgmAHWCCDAd/UfRNws0o5Im+490uYx01jJUm2z/uPCrhI+EY5AqEGvpDcWpsSd/iRVZD0lW/XTVsuAXJ9fyNnuEG6zlx1OaECoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhnBIhhsPPx4MoTtf",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAXcRy9ELWJ5NHOxKQK2ShD4gtUZ2hfdyQTf+wCziw8wd+5I9bGnk96fVQLglxL2dNc+shiUBZA5LxH76LDT8jCLkCd/kCdDcBoQa+kNxamxJ3+JFVkPSVb9dNWy4Bcn1/I2e4QbrOXHU5oaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAfev5+L8EHGTVf6E47T1Ji8LaobNgfbf7RHjE2VxAGAXULb8g3YH7L0jXYfTtigq6bB+MaxmyQ1F3NNWcrjSiDbhAhcYL3Y3wOXejv47uNUtVP8Y/UX8TFPSSVekJVRzEivwWgmAHWCCDAd/UfRNws0o5Im+490uYx01jJUm2z/uPCrhI+EY5AqEGvpDcWpsSd/iRVZD0lW/XTVsuAXJ9fyNnuEG6zlx1OaECoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhnBIhhsPPx4MoTtf",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBr6Q3FqbEnf4kVWQ9JVv101bLgFyfX8jZ7hBus5cdTmhoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/6GJGE5yoACAIYPXtZ/KAAflolYWQ==",
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
    "signed_tx": "tx_+KcLAfhCuEA3ZZxrbrHJKOHGJNbhWBtnWoxKIADg6pbCHI6hkALxFAwIeZvVYxS9IxaRAzI3+bUX3E326ekiaXpRTarN0cgNuF/4XTgBoQa+kNxamxJ3+JFVkPSVb9dNWy4Bcn1/I2e4QbrOXHU5oaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAH/0LjKA="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEA3ZZxrbrHJKOHGJNbhWBtnWoxKIADg6pbCHI6hkALxFAwIeZvVYxS9IxaRAzI3+bUX3E326ekiaXpRTarN0cgNuF/4XTgBoQa+kNxamxJ3+JFVkPSVb9dNWy4Bcn1/I2e4QbrOXHU5oaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAH/0LjKA=",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEA3ZZxrbrHJKOHGJNbhWBtnWoxKIADg6pbCHI6hkALxFAwIeZvVYxS9IxaRAzI3+bUX3E326ekiaXpRTarN0cgNuF/4XTgBoQa+kNxamxJ3+JFVkPSVb9dNWy4Bcn1/I2e4QbrOXHU5oaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAH/0LjKA=",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
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
    "channel_id": "ch_2SvkTGMQgEAJQMSqrWAMeHpWRZ3RKpAdGPwaQDX55ymoLEuxKE",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
