
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8&lock_period=10&port=13079&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ&role=initiator
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8&lock_period=10&port=13079&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ&role=responder
```

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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAWIkSd5WdpFzkPsC1nnT4DZII0KAbQjMu2h2vWfuU7bShj+qJSJgAKEB3HXwQV/nBYQFgWJnAiulow4d1j7ZvpLwQ1cQEGftEAWGJGE5yoAAAgoAhhAGeddIAMCgwSUHJTuULkCbgIm8cn3NUJbM9IKFe7X08v6+of6bcoQBLmRXMQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422458,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBCqt+ZRX/uGUQFLd6Y9I1pPlVSFYctUSObjDoWFm8aiZBPw8gnh5kjhzaO+IOMfS6Pys+n3WO7t3cZ8UdfeRsBuIP4gTIBoQFiJEneVnaRc5D7AtZ50+A2SCNCgG0IzLtodr1n7lO20oY/qiUiYAChAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFhiRhOcqAAAIKAIYQBnnXSADAoMElByU7lC5Am4CJvHJ9zVCWzPSChXu19PL+vqH+m3KEAcHnTSw="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422458,
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
      "signed_tx": "tx_+MsLAfhCuEBCqt+ZRX/uGUQFLd6Y9I1pPlVSFYctUSObjDoWFm8aiZBPw8gnh5kjhzaO+IOMfS6Pys+n3WO7t3cZ8UdfeRsBuIP4gTIBoQFiJEneVnaRc5D7AtZ50+A2SCNCgG0IzLtodr1n7lO20oY/qiUiYAChAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFhiRhOcqAAAIKAIYQBnnXSADAoMElByU7lC5Am4CJvHJ9zVCWzPSChXu19PL+vqH+m3KEAcHnTSw=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422457,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QGxCwHAuQGr+QGoUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEBCqt+ZRX/uGUQFLd6Y9I1pPlVSFYctUSObjDoWFm8aiZBPw8gnh5kjhzaO+IOMfS6Pys+n3WO7t3cZ8UdfeRsBuIP4gTIBoQFiJEneVnaRc5D7AtZ50+A2SCNCgG0IzLtodr1n7lO20oY/qiUiYAChAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFhiRhOcqAAAIKAIYQBnnXSADAoMElByU7lC5Am4CJvHJ9zVCWzPSChXu19PL+vqH+m3KEAajCFLI="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422457,
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
    "channel_id": null,
    "data": {
      "info": "funding_created",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEBCqt+ZRX/uGUQFLd6Y9I1pPlVSFYctUSObjDoWFm8aiZBPw8gnh5kjhzaO+IOMfS6Pys+n3WO7t3cZ8UdfeRsBuIP4gTIBoQFiJEneVnaRc5D7AtZ50+A2SCNCgG0IzLtodr1n7lO20oY/qiUiYAChAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFhiRhOcqAAAIKAIYQBnnXSADAoMElByU7lC5Am4CJvHJ9zVCWzPSChXu19PL+vqH+m3KEAajCFLI=",
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
    "channel_id": null,
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEBCqt+ZRX/uGUQFLd6Y9I1pPlVSFYctUSObjDoWFm8aiZBPw8gnh5kjhzaO+IOMfS6Pys+n3WO7t3cZ8UdfeRsBuIP4gTIBoQFiJEneVnaRc5D7AtZ50+A2SCNCgG0IzLtodr1n7lO20oY/qiUiYAChAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFhiRhOcqAAAIKAIYQBnnXSADAoMElByU7lC5Am4CJvHJ9zVCWzPSChXu19PL+vqH+m3KEAajCFLI=",
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
    "channel_id": null,
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEBCqt+ZRX/uGUQFLd6Y9I1pPlVSFYctUSObjDoWFm8aiZBPw8gnh5kjhzaO+IOMfS6Pys+n3WO7t3cZ8UdfeRsBuIP4gTIBoQFiJEneVnaRc5D7AtZ50+A2SCNCgG0IzLtodr1n7lO20oY/qiUiYAChAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFhiRhOcqAAAIKAIYQBnnXSADAoMElByU7lC5Am4CJvHJ9zVCWzPSChXu19PL+vqH+m3KEAajCFLI=",
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
    "channel_id": null,
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEBCqt+ZRX/uGUQFLd6Y9I1pPlVSFYctUSObjDoWFm8aiZBPw8gnh5kjhzaO+IOMfS6Pys+n3WO7t3cZ8UdfeRsBuIP4gTIBoQFiJEneVnaRc5D7AtZ50+A2SCNCgG0IzLtodr1n7lO20oY/qiUiYAChAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFhiRhOcqAAAIKAIYQBnnXSADAoMElByU7lC5Am4CJvHJ9zVCWzPSChXu19PL+vqH+m3KEAajCFLI=",
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
    "to": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "message": {
        "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
        "from": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
        "info": "Hello",
        "to": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ"
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
    "to": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "message": {
        "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
        "from": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
        "info": "Hello back",
        "to": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422456,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
      "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422456,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
      "balance": 69999999999999
    },
    {
      "account": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "state": "tx_+QGxCwHAuQGr+QGoUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEBCqt+ZRX/uGUQFLd6Y9I1pPlVSFYctUSObjDoWFm8aiZBPw8gnh5kjhzaO+IOMfS6Pys+n3WO7t3cZ8UdfeRsBuIP4gTIBoQFiJEneVnaRc5D7AtZ50+A2SCNCgG0IzLtodr1n7lO20oY/qiUiYAChAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFhiRhOcqAAAIKAIYQBnnXSADAoMElByU7lC5Am4CJvHJ9zVCWzPSChXu19PL+vqH+m3KEAajCFLI="
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "state": "tx_+QGxCwHAuQGr+QGoUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEBCqt+ZRX/uGUQFLd6Y9I1pPlVSFYctUSObjDoWFm8aiZBPw8gnh5kjhzaO+IOMfS6Pys+n3WO7t3cZ8UdfeRsBuIP4gTIBoQFiJEneVnaRc5D7AtZ50+A2SCNCgG0IzLtodr1n7lO20oY/qiUiYAChAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFhiRhOcqAAAIKAIYQBnnXSADAoMElByU7lC5Am4CJvHJ9zVCWzPSChXu19PL+vqH+m3KEAajCFLI="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422455,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
      "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422455,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
      "balance": 69999999999999
    },
    {
      "account": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
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
    "from": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
    "to": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "error": {
    "code": 3,
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
        "from": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
        "to": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ"
      }
    }
  },
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
    "to": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "error": {
    "code": 3,
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
        "to": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ"
      }
    }
  },
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
    "from": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "error": {
    "code": 3,
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
        "from": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
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
    "from": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
    "to": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvwwDq2UCkeZxJCpn+nl84pYnZDhN8FMeE1n+T5sUWJyAqBqk14+F0nhYhHZMwW/j7TcBVedCdI46oNsG3F41KIYQeJQmAI=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
          "op": "OffChainTransfer",
          "to": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ"
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
  "id": -576460752303422454,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAs2Jr044s3GAAt0FKnqws43wOuReLmGhGUWBmbfB+DJacCEsqMX5TEgKO0BiH7oUfXaEJTAErkudD+0wBR+1QOuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgKgapNePhdJ4WIR2TMFv4+03AVXnQnSOOqDbBtxeNSiGEHI2yIV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422454,
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAs2Jr044s3GAAt0FKnqws43wOuReLmGhGUWBmbfB+DJacCEsqMX5TEgKO0BiH7oUfXaEJTAErkudD+0wBR+1QOuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgKgapNePhdJ4WIR2TMFv4+03AVXnQnSOOqDbBtxeNSiGEHI2yIV",
      "updates": [
        {
          "amount": 1,
          "from": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
          "op": "OffChainTransfer",
          "to": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ"
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
  "id": -576460752303422453,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAs2Jr044s3GAAt0FKnqws43wOuReLmGhGUWBmbfB+DJacCEsqMX5TEgKO0BiH7oUfXaEJTAErkudD+0wBR+1QOuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgKgapNePhdJ4WIR2TMFv4+03AVXnQnSOOqDbBtxeNSiGEF0j0gy"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422453,
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAs2Jr044s3GAAt0FKnqws43wOuReLmGhGUWBmbfB+DJacCEsqMX5TEgKO0BiH7oUfXaEJTAErkudD+0wBR+1QOuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgKgapNePhdJ4WIR2TMFv4+03AVXnQnSOOqDbBtxeNSiGEF0j0gy"
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAs2Jr044s3GAAt0FKnqws43wOuReLmGhGUWBmbfB+DJacCEsqMX5TEgKO0BiH7oUfXaEJTAErkudD+0wBR+1QOuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgKgapNePhdJ4WIR2TMFv4+03AVXnQnSOOqDbBtxeNSiGEF0j0gy"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422452,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
      "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422452,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
      "balance": 69999999999998
    },
    {
      "account": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422451,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422451,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAs2Jr044s3GAAt0FKnqws43wOuReLmGhGUWBmbfB+DJacCEsqMX5TEgKO0BiH7oUfXaEJTAErkudD+0wBR+1QOuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgKgapNePhdJ4WIR2TMFv4+03AVXnQnSOOqDbBtxeNSiGEF0j0gy",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDcdfBBX+cFhAWBYmcCK6WjDh3WPtm+kvBDVxAQZ+0QBYvKCgEAhiRhOcqAArDvQAGgYiRJ3lZ2kXOQ+wLWedPgNkgjQoBtCMy7aHa9Z+5TttKLygoBAIY/qiUiX/6nPyz/"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422450,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
      "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422450,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
      "balance": 40000000000002
    },
    {
      "account": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
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
    "from": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
    "to": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "error": {
    "code": 3,
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
        "from": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
        "to": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
      }
    }
  },
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
    "to": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "error": {
    "code": 3,
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
        "to": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
      }
    }
  },
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
    "from": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "error": {
    "code": 3,
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
        "from": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
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
    "from": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
    "to": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvwwDq2UCkeZxJCpn+nl84pYnZDhN8FMeE1n+T5sUWJyA6DBJQclO5QuQJuAibxyfc1Qlsz0goV7tfTy/r6h/ptyhEI6Oto=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
          "op": "OffChainTransfer",
          "to": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
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
  "id": -576460752303422449,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBvwwDq2UCkeZxJCpn+nl84pYnZDhN8FMeE1n+T5sUWJyA6DBJQclO5QuQJuAibxyfc1Qlsz0goV7tfTy/r6h/ptyhKMJnlg="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422449,
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBvwwDq2UCkeZxJCpn+nl84pYnZDhN8FMeE1n+T5sUWJyA6DBJQclO5QuQJuAibxyfc1Qlsz0goV7tfTy/r6h/ptyhKMJnlg=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
          "op": "OffChainTransfer",
          "to": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
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
  "id": -576460752303422448,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAdY8FuteRMnUNobLwEmVw++RP+RWUx9+WRLDhLqtwpD1y/CY2LZY0sHIHHlUDV641s/QApFPjB7ZyJi5ghN34IuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgOgwSUHJTuULkCbgIm8cn3NUJbM9IKFe7X08v6+of6bcoTgTK0Z"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422448,
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAdY8FuteRMnUNobLwEmVw++RP+RWUx9+WRLDhLqtwpD1y/CY2LZY0sHIHHlUDV641s/QApFPjB7ZyJi5ghN34IuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgOgwSUHJTuULkCbgIm8cn3NUJbM9IKFe7X08v6+of6bcoTgTK0Z"
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAdY8FuteRMnUNobLwEmVw++RP+RWUx9+WRLDhLqtwpD1y/CY2LZY0sHIHHlUDV641s/QApFPjB7ZyJi5ghN34IuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgOgwSUHJTuULkCbgIm8cn3NUJbM9IKFe7X08v6+of6bcoTgTK0Z"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422447,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
      "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422447,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
      "balance": 40000000000001
    },
    {
      "account": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422446,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422446,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAdY8FuteRMnUNobLwEmVw++RP+RWUx9+WRLDhLqtwpD1y/CY2LZY0sHIHHlUDV641s/QApFPjB7ZyJi5ghN34IuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgOgwSUHJTuULkCbgIm8cn3NUJbM9IKFe7X08v6+of6bcoTgTK0Z",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDcdfBBX+cFhAWBYmcCK6WjDh3WPtm+kvBDVxAQZ+0QBYvKCgEAhiRhOcqAAbDvQAGgYiRJ3lZ2kXOQ+wLWedPgNkgjQoBtCMy7aHa9Z+5TttKLygoBAIY/qiUiX/++08Vx"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422445,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
      "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422445,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
      "balance": 40000000000001
    },
    {
      "account": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
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
    "from": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
    "to": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "error": {
    "code": 3,
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
        "from": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
        "to": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
      }
    }
  },
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
    "to": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "error": {
    "code": 3,
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
        "to": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
      }
    }
  },
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
    "from": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "error": {
    "code": 3,
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
        "from": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
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
    "from": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
    "to": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvwwDq2UCkeZxJCpn+nl84pYnZDhN8FMeE1n+T5sUWJyBKAYRk7w0I6XKg7sc5MMO5kexpdj3rWIQeRZrzOF0jrimUAX0Zo=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
          "op": "OffChainTransfer",
          "to": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
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
  "id": -576460752303422444,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBvwwDq2UCkeZxJCpn+nl84pYnZDhN8FMeE1n+T5sUWJyBKAYRk7w0I6XKg7sc5MMO5kexpdj3rWIQeRZrzOF0jrimfDilWk="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422444,
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBvwwDq2UCkeZxJCpn+nl84pYnZDhN8FMeE1n+T5sUWJyBKAYRk7w0I6XKg7sc5MMO5kexpdj3rWIQeRZrzOF0jrimfDilWk=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
          "op": "OffChainTransfer",
          "to": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
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
  "id": -576460752303422443,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEBivIw0WXNcyvArom0J55CFMDh7eeAxXN7totLJPdbpemnK6JxrdD8NopqWily6obCeKntP2fZ6e3GjNbyYTEsKuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgSgGEZO8NCOlyoO7HOTDDuZHsaXY961iEHkWa8zhdI64pmV3ZeS"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422443,
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEBivIw0WXNcyvArom0J55CFMDh7eeAxXN7totLJPdbpemnK6JxrdD8NopqWily6obCeKntP2fZ6e3GjNbyYTEsKuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgSgGEZO8NCOlyoO7HOTDDuZHsaXY961iEHkWa8zhdI64pmV3ZeS"
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEBivIw0WXNcyvArom0J55CFMDh7eeAxXN7totLJPdbpemnK6JxrdD8NopqWily6obCeKntP2fZ6e3GjNbyYTEsKuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgSgGEZO8NCOlyoO7HOTDDuZHsaXY961iEHkWa8zhdI64pmV3ZeS"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422442,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
      "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422442,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
      "balance": 40000000000000
    },
    {
      "account": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422441,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422441,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEBivIw0WXNcyvArom0J55CFMDh7eeAxXN7totLJPdbpemnK6JxrdD8NopqWily6obCeKntP2fZ6e3GjNbyYTEsKuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgSgGEZO8NCOlyoO7HOTDDuZHsaXY961iEHkWa8zhdI64pmV3ZeS",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDcdfBBX+cFhAWBYmcCK6WjDh3WPtm+kvBDVxAQZ+0QBYvKCgEAhiRhOcqAALDvQAGgYiRJ3lZ2kXOQ+wLWedPgNkgjQoBtCMy7aHa9Z+5TttKLygoBAIY/qiUiYACQIM3X"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422440,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
      "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422440,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
      "balance": 70000000000000
    },
    {
      "account": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
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
    "from": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
    "to": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "error": {
    "code": 3,
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
        "from": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
        "to": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ"
      }
    }
  },
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
    "to": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "error": {
    "code": 3,
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
        "to": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ"
      }
    }
  },
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
    "from": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "error": {
    "code": 3,
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
        "from": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
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
    "from": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
    "to": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvwwDq2UCkeZxJCpn+nl84pYnZDhN8FMeE1n+T5sUWJyBaDBJQclO5QuQJuAibxyfc1Qlsz0goV7tfTy/r6h/ptyhD8oi+8=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
          "op": "OffChainTransfer",
          "to": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ"
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
  "id": -576460752303422439,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECT3qqo4npjT/cghY/1O+rhYjGHU7N1u+lNAY/NyHou2WhJt5Nhqm4db0GkOtcsK99JHnS1q4XT2pgZXaDFbk8JuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgWgwSUHJTuULkCbgIm8cn3NUJbM9IKFe7X08v6+of6bcoScitkB"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422439,
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "signed_tx": "tx_+JALAfhCuECT3qqo4npjT/cghY/1O+rhYjGHU7N1u+lNAY/NyHou2WhJt5Nhqm4db0GkOtcsK99JHnS1q4XT2pgZXaDFbk8JuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgWgwSUHJTuULkCbgIm8cn3NUJbM9IKFe7X08v6+of6bcoScitkB",
      "updates": [
        {
          "amount": 1,
          "from": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
          "op": "OffChainTransfer",
          "to": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ"
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
  "id": -576460752303422438,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECT3qqo4npjT/cghY/1O+rhYjGHU7N1u+lNAY/NyHou2WhJt5Nhqm4db0GkOtcsK99JHnS1q4XT2pgZXaDFbk8JuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgWgwSUHJTuULkCbgIm8cn3NUJbM9IKFe7X08v6+of6bcoTXVrW5"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422438,
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECT3qqo4npjT/cghY/1O+rhYjGHU7N1u+lNAY/NyHou2WhJt5Nhqm4db0GkOtcsK99JHnS1q4XT2pgZXaDFbk8JuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgWgwSUHJTuULkCbgIm8cn3NUJbM9IKFe7X08v6+of6bcoTXVrW5"
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECT3qqo4npjT/cghY/1O+rhYjGHU7N1u+lNAY/NyHou2WhJt5Nhqm4db0GkOtcsK99JHnS1q4XT2pgZXaDFbk8JuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgWgwSUHJTuULkCbgIm8cn3NUJbM9IKFe7X08v6+of6bcoTXVrW5"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422437,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
      "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422437,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
      "balance": 69999999999999
    },
    {
      "account": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422436,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422436,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuECT3qqo4npjT/cghY/1O+rhYjGHU7N1u+lNAY/NyHou2WhJt5Nhqm4db0GkOtcsK99JHnS1q4XT2pgZXaDFbk8JuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgWgwSUHJTuULkCbgIm8cn3NUJbM9IKFe7X08v6+of6bcoTXVrW5",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDcdfBBX+cFhAWBYmcCK6WjDh3WPtm+kvBDVxAQZ+0QBYvKCgEAhiRhOcqAAbDvQAGgYiRJ3lZ2kXOQ+wLWedPgNkgjQoBtCMy7aHa9Z+5TttKLygoBAIY/qiUiX/++08Vx"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422435,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
      "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422435,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
      "balance": 40000000000001
    },
    {
      "account": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
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
    "from": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
    "to": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "error": {
    "code": 3,
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
        "from": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
        "to": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
      }
    }
  },
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
    "to": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "error": {
    "code": 3,
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
        "to": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
      }
    }
  },
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
    "from": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "error": {
    "code": 3,
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
        "from": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
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
    "from": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
    "to": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvwwDq2UCkeZxJCpn+nl84pYnZDhN8FMeE1n+T5sUWJyBqAYRk7w0I6XKg7sc5MMO5kexpdj3rWIQeRZrzOF0jrimQIfGaY=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
          "op": "OffChainTransfer",
          "to": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
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
  "id": -576460752303422434,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBvwwDq2UCkeZxJCpn+nl84pYnZDhN8FMeE1n+T5sUWJyBqAYRk7w0I6XKg7sc5MMO5kexpdj3rWIQeRZrzOF0jrimde3d40="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422434,
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBvwwDq2UCkeZxJCpn+nl84pYnZDhN8FMeE1n+T5sUWJyBqAYRk7w0I6XKg7sc5MMO5kexpdj3rWIQeRZrzOF0jrimde3d40=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
          "op": "OffChainTransfer",
          "to": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
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
  "id": -576460752303422433,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAa2ZL+camxYhvMQoESt91xKsZzd9kcOpjYRWGOZbnW5c+X+JKy3H4MVCweEZ/TF2ZDXxk8RGV/R/kP5PNGO4gPuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgagGEZO8NCOlyoO7HOTDDuZHsaXY961iEHkWa8zhdI64pmK5hJ7"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422433,
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAa2ZL+camxYhvMQoESt91xKsZzd9kcOpjYRWGOZbnW5c+X+JKy3H4MVCweEZ/TF2ZDXxk8RGV/R/kP5PNGO4gPuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgagGEZO8NCOlyoO7HOTDDuZHsaXY961iEHkWa8zhdI64pmK5hJ7"
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
    "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAa2ZL+camxYhvMQoESt91xKsZzd9kcOpjYRWGOZbnW5c+X+JKy3H4MVCweEZ/TF2ZDXxk8RGV/R/kP5PNGO4gPuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgagGEZO8NCOlyoO7HOTDDuZHsaXY961iEHkWa8zhdI64pmK5hJ7"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422432,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
      "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422432,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2g6NcVzj4cab1h5hhDHk6Fi3M4xkqQwEN7SVa7mmhebSesfHgZ",
      "balance": 40000000000000
    },
    {
      "account": "ak_kDuANhtxvab7z9p7qRMfnc2FSpdGxNNECrcqUXHsQQyna1HD8",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422431,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2v4oDtz8r3vb1QTPhGFe1u5h4pgt1CefmHkGzzUtgLbA2cLig2",
  "id": -576460752303422431,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAdx18EFf5wWEBYFiZwIrpaMOHdY+2b6S8ENXEBBn7RAFuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAa2ZL+camxYhvMQoESt91xKsZzd9kcOpjYRWGOZbnW5c+X+JKy3H4MVCweEZ/TF2ZDXxk8RGV/R/kP5PNGO4gPuEj4RjkCoQb8MA6tlApHmcSQqZ/p5fOKWJ2Q4TfBTHhNZ/k+bFFicgagGEZO8NCOlyoO7HOTDDuZHsaXY961iEHkWa8zhdI64pmK5hJ7",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDcdfBBX+cFhAWBYmcCK6WjDh3WPtm+kvBDVxAQZ+0QBYvKCgEAhiRhOcqAALDvQAGgYiRJ3lZ2kXOQ+wLWedPgNkgjQoBtCMy7aHa9Z+5TttKLygoBAIY/qiUiYACQIM3X"
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t&lock_period=10&port=12515&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k&role=initiator
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t&lock_period=10&port=12515&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k&role=responder
```

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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAYVhBnALhOR49eP3nH2Ihz43ytY1Cp9cJnpnpnVZ6hjjhj+qJSJgAKEBIWkMmQL20NbNDS+4AoAYbniyxc/OU80prXb/Khbul2mGJGE5yoAAAgoAhhAGeddIAMCgE/Vp/E5HZ7mqKHaXOgXkw7oXK+QKJrXxPKDRf5jE0VMBS/e+3g==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421547,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECXzj8giHDbkkt2Jm7vbQ4NqJGmUwNoVJOGuDFkKYIWAwlUi03l+Ilg/RBITx9zSZi+5GtbXLC9cAZxD+hr14oHuIP4gTIBoQGFYQZwC4TkePXj95x9iIc+N8rWNQqfXCZ6Z6Z1WeoY44Y/qiUiYAChASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdphiRhOcqAAAIKAIYQBnnXSADAoBP1afxOR2e5qih2lzoF5MO6FyvkCia18Tyg0X+YxNFTAYSWcOo="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421547,
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
      "signed_tx": "tx_+MsLAfhCuECXzj8giHDbkkt2Jm7vbQ4NqJGmUwNoVJOGuDFkKYIWAwlUi03l+Ilg/RBITx9zSZi+5GtbXLC9cAZxD+hr14oHuIP4gTIBoQGFYQZwC4TkePXj95x9iIc+N8rWNQqfXCZ6Z6Z1WeoY44Y/qiUiYAChASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdphiRhOcqAAAIKAIYQBnnXSADAoBP1afxOR2e5qih2lzoF5MO6FyvkCia18Tyg0X+YxNFTAYSWcOo=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421546,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEZCwHAuQET+QEQUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAl84/IIhw25JLdiZu720ODaiRplMDaFSThrgxZCmCFgMJVItN5fiJYP0QSE8fc0mYvuRrW1ywvXAGcQ/oa9eKB7iD+IEyAaEBhWEGcAuE5Hj14/ecfYiHPjfK1jUKn1wmememdVnqGOOGP6olImAAoQEhaQyZAvbQ1s0NL7gCgBhueLLFz85TzSmtdv8qFu6XaYYkYTnKgAACCgCGEAZ510gAwKAT9Wn8Tkdnuaoodpc6BeTDuhcr5AomtfE8oNF/mMTRUwECiDyk"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421546,
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
    "channel_id": null,
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAl84/IIhw25JLdiZu720ODaiRplMDaFSThrgxZCmCFgMJVItN5fiJYP0QSE8fc0mYvuRrW1ywvXAGcQ/oa9eKB7iD+IEyAaEBhWEGcAuE5Hj14/ecfYiHPjfK1jUKn1wmememdVnqGOOGP6olImAAoQEhaQyZAvbQ1s0NL7gCgBhueLLFz85TzSmtdv8qFu6XaYYkYTnKgAACCgCGEAZ510gAwKAT9Wn8Tkdnuaoodpc6BeTDuhcr5AomtfE8oNF/mMTRUwECiDyk",
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
    "channel_id": null,
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAl84/IIhw25JLdiZu720ODaiRplMDaFSThrgxZCmCFgMJVItN5fiJYP0QSE8fc0mYvuRrW1ywvXAGcQ/oa9eKB7iD+IEyAaEBhWEGcAuE5Hj14/ecfYiHPjfK1jUKn1wmememdVnqGOOGP6olImAAoQEhaQyZAvbQ1s0NL7gCgBhueLLFz85TzSmtdv8qFu6XaYYkYTnKgAACCgCGEAZ510gAwKAT9Wn8Tkdnuaoodpc6BeTDuhcr5AomtfE8oNF/mMTRUwECiDyk",
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
    "channel_id": null,
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAl84/IIhw25JLdiZu720ODaiRplMDaFSThrgxZCmCFgMJVItN5fiJYP0QSE8fc0mYvuRrW1ywvXAGcQ/oa9eKB7iD+IEyAaEBhWEGcAuE5Hj14/ecfYiHPjfK1jUKn1wmememdVnqGOOGP6olImAAoQEhaQyZAvbQ1s0NL7gCgBhueLLFz85TzSmtdv8qFu6XaYYkYTnKgAACCgCGEAZ510gAwKAT9Wn8Tkdnuaoodpc6BeTDuhcr5AomtfE8oNF/mMTRUwECiDyk",
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
    "channel_id": null,
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAl84/IIhw25JLdiZu720ODaiRplMDaFSThrgxZCmCFgMJVItN5fiJYP0QSE8fc0mYvuRrW1ywvXAGcQ/oa9eKB7iD+IEyAaEBhWEGcAuE5Hj14/ecfYiHPjfK1jUKn1wmememdVnqGOOGP6olImAAoQEhaQyZAvbQ1s0NL7gCgBhueLLFz85TzSmtdv8qFu6XaYYkYTnKgAACCgCGEAZ510gAwKAT9Wn8Tkdnuaoodpc6BeTDuhcr5AomtfE8oNF/mMTRUwECiDyk",
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
    "to": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "message": {
        "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
        "from": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
        "info": "Hello",
        "to": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k"
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
    "to": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "message": {
        "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
        "from": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
        "info": "Hello back",
        "to": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421545,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
      "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421545,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
      "balance": 69999999999999
    },
    {
      "account": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "event": "open"
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Channel is `open` and ready to use

#### responder info
> Channel is `open` and ready to use

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "state": "tx_+QEZCwHAuQET+QEQUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAl84/IIhw25JLdiZu720ODaiRplMDaFSThrgxZCmCFgMJVItN5fiJYP0QSE8fc0mYvuRrW1ywvXAGcQ/oa9eKB7iD+IEyAaEBhWEGcAuE5Hj14/ecfYiHPjfK1jUKn1wmememdVnqGOOGP6olImAAoQEhaQyZAvbQ1s0NL7gCgBhueLLFz85TzSmtdv8qFu6XaYYkYTnKgAACCgCGEAZ510gAwKAT9Wn8Tkdnuaoodpc6BeTDuhcr5AomtfE8oNF/mMTRUwECiDyk"
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "state": "tx_+QEZCwHAuQET+QEQUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAl84/IIhw25JLdiZu720ODaiRplMDaFSThrgxZCmCFgMJVItN5fiJYP0QSE8fc0mYvuRrW1ywvXAGcQ/oa9eKB7iD+IEyAaEBhWEGcAuE5Hj14/ecfYiHPjfK1jUKn1wmememdVnqGOOGP6olImAAoQEhaQyZAvbQ1s0NL7gCgBhueLLFz85TzSmtdv8qFu6XaYYkYTnKgAACCgCGEAZ510gAwKAT9Wn8Tkdnuaoodpc6BeTDuhcr5AomtfE8oNF/mMTRUwECiDyk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421544,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
      "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421544,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
      "balance": 69999999999999
    },
    {
      "account": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
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
    "from": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
    "to": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "error": {
    "code": 3,
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
        "from": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
        "to": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k"
      }
    }
  },
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
    "to": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "error": {
    "code": 3,
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
        "to": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k"
      }
    }
  },
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
    "from": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "error": {
    "code": 3,
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
        "from": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
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
    "from": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
    "to": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhRijPpQfLTEI44S8bcZuhs0b7THkHYfc2E9Y0B9o1fEAqDBSChvNu8vt+LG1a0KC1etoSsijDvkjnjXoy8VdorvMk7z8Dc=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
          "op": "OffChainTransfer",
          "to": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k"
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
  "id": -576460752303421543,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC5VVsLpiCqpRa5sJBu1n7PGUV2hsFG33C341EWpMR6NJewvTv+xcESElIolGxK5AoNO/g0ssgWw4X0EAFggN8GuEj4RjkCoQYUYoz6UHy0xCOOEvG3GbobNG+0x5B2H3NhPWNAfaNXxAKgwUgobzbvL7fixtWtCgtXraErIow75I5416MvFXaK7zJNgqT1"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421543,
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC5VVsLpiCqpRa5sJBu1n7PGUV2hsFG33C341EWpMR6NJewvTv+xcESElIolGxK5AoNO/g0ssgWw4X0EAFggN8GuEj4RjkCoQYUYoz6UHy0xCOOEvG3GbobNG+0x5B2H3NhPWNAfaNXxAKgwUgobzbvL7fixtWtCgtXraErIow75I5416MvFXaK7zJNgqT1",
      "updates": [
        {
          "amount": 1,
          "from": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
          "op": "OffChainTransfer",
          "to": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k"
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
  "id": -576460752303421542,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAuVVbC6YgqqUWubCQbtZ+zxlFdobBRt9wt+NRFqTEejSXsL07/sXBEhJSKJRsSuQKDTv4NLLIFsOF9BABYIDfBrhI+EY5AqEGFGKM+lB8tMQjjhLxtxm6GzRvtMeQdh9zYT1jQH2jV8QCoMFIKG827y+34sbVrQoLV62hKyKMO+SOeNejLxV2iu8yD0SujA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421542,
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAuVVbC6YgqqUWubCQbtZ+zxlFdobBRt9wt+NRFqTEejSXsL07/sXBEhJSKJRsSuQKDTv4NLLIFsOF9BABYIDfBrhI+EY5AqEGFGKM+lB8tMQjjhLxtxm6GzRvtMeQdh9zYT1jQH2jV8QCoMFIKG827y+34sbVrQoLV62hKyKMO+SOeNejLxV2iu8yD0SujA=="
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAuVVbC6YgqqUWubCQbtZ+zxlFdobBRt9wt+NRFqTEejSXsL07/sXBEhJSKJRsSuQKDTv4NLLIFsOF9BABYIDfBrhI+EY5AqEGFGKM+lB8tMQjjhLxtxm6GzRvtMeQdh9zYT1jQH2jV8QCoMFIKG827y+34sbVrQoLV62hKyKMO+SOeNejLxV2iu8yD0SujA=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421541,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
      "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421541,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
      "balance": 69999999999998
    },
    {
      "account": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421540,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421540,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAuVVbC6YgqqUWubCQbtZ+zxlFdobBRt9wt+NRFqTEejSXsL07/sXBEhJSKJRsSuQKDTv4NLLIFsOF9BABYIDfBrhI+EY5AqEGFGKM+lB8tMQjjhLxtxm6GzRvtMeQdh9zYT1jQH2jV8QCoMFIKG827y+34sbVrQoLV62hKyKMO+SOeNejLxV2iu8yD0SujA==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCFYQZwC4TkePXj95x9iIc+N8rWNQqfXCZ6Z6Z1WeoY44vKCgEAhj+qJSJf/rDvQAGgIWkMmQL20NbNDS+4AoAYbniyxc/OU80prXb/Khbul2mLygoBAIYkYTnKgAIi+Mxl"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421539,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
      "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421539,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
      "balance": 40000000000002
    },
    {
      "account": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
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
    "from": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
    "to": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "error": {
    "code": 3,
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
        "from": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
        "to": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
      }
    }
  },
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
    "to": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "error": {
    "code": 3,
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
        "to": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
      }
    }
  },
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
    "from": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "error": {
    "code": 3,
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
        "from": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
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
    "from": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
    "to": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhRijPpQfLTEI44S8bcZuhs0b7THkHYfc2E9Y0B9o1fEA6AT9Wn8Tkdnuaoodpc6BeTDuhcr5AomtfE8oNF/mMTRU2OQ/UE=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
          "op": "OffChainTransfer",
          "to": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
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
  "id": -576460752303421538,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQYUYoz6UHy0xCOOEvG3GbobNG+0x5B2H3NhPWNAfaNXxAOgE/Vp/E5HZ7mqKHaXOgXkw7oXK+QKJrXxPKDRf5jE0VPOxHd2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421538,
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQYUYoz6UHy0xCOOEvG3GbobNG+0x5B2H3NhPWNAfaNXxAOgE/Vp/E5HZ7mqKHaXOgXkw7oXK+QKJrXxPKDRf5jE0VPOxHd2",
      "updates": [
        {
          "amount": 1,
          "from": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
          "op": "OffChainTransfer",
          "to": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
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
  "id": -576460752303421537,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAtAWJYqFjkDEX6LYPxlWj4RdaoUH/pS42+Amad1Gs7/L0gB8EDo/jtM0j7eZOt6ISOlIQ3U6/Ak1uJWAHGGrPBrhI+EY5AqEGFGKM+lB8tMQjjhLxtxm6GzRvtMeQdh9zYT1jQH2jV8QDoBP1afxOR2e5qih2lzoF5MO6FyvkCia18Tyg0X+YxNFTtZtP1Q=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421537,
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAtAWJYqFjkDEX6LYPxlWj4RdaoUH/pS42+Amad1Gs7/L0gB8EDo/jtM0j7eZOt6ISOlIQ3U6/Ak1uJWAHGGrPBrhI+EY5AqEGFGKM+lB8tMQjjhLxtxm6GzRvtMeQdh9zYT1jQH2jV8QDoBP1afxOR2e5qih2lzoF5MO6FyvkCia18Tyg0X+YxNFTtZtP1Q=="
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAtAWJYqFjkDEX6LYPxlWj4RdaoUH/pS42+Amad1Gs7/L0gB8EDo/jtM0j7eZOt6ISOlIQ3U6/Ak1uJWAHGGrPBrhI+EY5AqEGFGKM+lB8tMQjjhLxtxm6GzRvtMeQdh9zYT1jQH2jV8QDoBP1afxOR2e5qih2lzoF5MO6FyvkCia18Tyg0X+YxNFTtZtP1Q=="
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
      "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
      "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421536,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
      "balance": 40000000000001
    },
    {
      "account": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421535,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421535,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAtAWJYqFjkDEX6LYPxlWj4RdaoUH/pS42+Amad1Gs7/L0gB8EDo/jtM0j7eZOt6ISOlIQ3U6/Ak1uJWAHGGrPBrhI+EY5AqEGFGKM+lB8tMQjjhLxtxm6GzRvtMeQdh9zYT1jQH2jV8QDoBP1afxOR2e5qih2lzoF5MO6FyvkCia18Tyg0X+YxNFTtZtP1Q==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCFYQZwC4TkePXj95x9iIc+N8rWNQqfXCZ6Z6Z1WeoY44vKCgEAhj+qJSJf/7DvQAGgIWkMmQL20NbNDS+4AoAYbniyxc/OU80prXb/Khbul2mLygoBAIYkYTnKgAEYbZ7/"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421534,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
      "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421534,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
      "balance": 40000000000001
    },
    {
      "account": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
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
    "from": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
    "to": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "error": {
    "code": 3,
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
        "from": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
        "to": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
      }
    }
  },
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
    "to": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "error": {
    "code": 3,
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
        "to": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
      }
    }
  },
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
    "from": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "error": {
    "code": 3,
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
        "from": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
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
    "from": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
    "to": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhRijPpQfLTEI44S8bcZuhs0b7THkHYfc2E9Y0B9o1fEBKCGTspsLOSVRdxEadthlqBFsif6ugnTF45ftph52dPDYv5Y92Q=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
          "op": "OffChainTransfer",
          "to": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
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
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQYUYoz6UHy0xCOOEvG3GbobNG+0x5B2H3NhPWNAfaNXxASghk7KbCzklUXcRGnbYZagRbIn+roJ0xeOX7aYednTw2KwueJT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421533,
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQYUYoz6UHy0xCOOEvG3GbobNG+0x5B2H3NhPWNAfaNXxASghk7KbCzklUXcRGnbYZagRbIn+roJ0xeOX7aYednTw2KwueJT",
      "updates": [
        {
          "amount": 1,
          "from": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
          "op": "OffChainTransfer",
          "to": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
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
  "id": -576460752303421532,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAcIAvpU3CHSf9pERw3t8IIRyfI0b/yNFZ1AoXOin6d+Vb/d+ttlmDM7B99vWPLGTCkXZzJoOb66wJ0etvIaX3AbhI+EY5AqEGFGKM+lB8tMQjjhLxtxm6GzRvtMeQdh9zYT1jQH2jV8QEoIZOymws5JVF3ERp22GWoEWyJ/q6CdMXjl+2mHnZ08NigAONow=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421532,
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAcIAvpU3CHSf9pERw3t8IIRyfI0b/yNFZ1AoXOin6d+Vb/d+ttlmDM7B99vWPLGTCkXZzJoOb66wJ0etvIaX3AbhI+EY5AqEGFGKM+lB8tMQjjhLxtxm6GzRvtMeQdh9zYT1jQH2jV8QEoIZOymws5JVF3ERp22GWoEWyJ/q6CdMXjl+2mHnZ08NigAONow=="
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAcIAvpU3CHSf9pERw3t8IIRyfI0b/yNFZ1AoXOin6d+Vb/d+ttlmDM7B99vWPLGTCkXZzJoOb66wJ0etvIaX3AbhI+EY5AqEGFGKM+lB8tMQjjhLxtxm6GzRvtMeQdh9zYT1jQH2jV8QEoIZOymws5JVF3ERp22GWoEWyJ/q6CdMXjl+2mHnZ08NigAONow=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421531,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
      "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421531,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
      "balance": 40000000000000
    },
    {
      "account": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421530,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421530,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAcIAvpU3CHSf9pERw3t8IIRyfI0b/yNFZ1AoXOin6d+Vb/d+ttlmDM7B99vWPLGTCkXZzJoOb66wJ0etvIaX3AbhI+EY5AqEGFGKM+lB8tMQjjhLxtxm6GzRvtMeQdh9zYT1jQH2jV8QEoIZOymws5JVF3ERp22GWoEWyJ/q6CdMXjl+2mHnZ08NigAONow==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCFYQZwC4TkePXj95x9iIc+N8rWNQqfXCZ6Z6Z1WeoY44vKCgEAhj+qJSJgALDvQAGgIWkMmQL20NbNDS+4AoAYbniyxc/OU80prXb/Khbul2mLygoBAIYkYTnKgABam9vf"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421529,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
      "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421529,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
      "balance": 70000000000000
    },
    {
      "account": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
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
    "from": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
    "to": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "error": {
    "code": 3,
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
        "from": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
        "to": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k"
      }
    }
  },
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
    "to": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "error": {
    "code": 3,
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
        "to": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k"
      }
    }
  },
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
    "from": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "error": {
    "code": 3,
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
        "from": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
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
    "from": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
    "to": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhRijPpQfLTEI44S8bcZuhs0b7THkHYfc2E9Y0B9o1fEBaAT9Wn8Tkdnuaoodpc6BeTDuhcr5AomtfE8oNF/mMTRU1orOvw=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
          "op": "OffChainTransfer",
          "to": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k"
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
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDyngJxtEcppiXXdrZHC6l4BWXatPJ0etcSKNNl830FeShBFH7IC4qFarVtvvOTvHsVTWYABrxjhjI58+9/V8sHuEj4RjkCoQYUYoz6UHy0xCOOEvG3GbobNG+0x5B2H3NhPWNAfaNXxAWgE/Vp/E5HZ7mqKHaXOgXkw7oXK+QKJrXxPKDRf5jE0VNYuyi7"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421528,
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDyngJxtEcppiXXdrZHC6l4BWXatPJ0etcSKNNl830FeShBFH7IC4qFarVtvvOTvHsVTWYABrxjhjI58+9/V8sHuEj4RjkCoQYUYoz6UHy0xCOOEvG3GbobNG+0x5B2H3NhPWNAfaNXxAWgE/Vp/E5HZ7mqKHaXOgXkw7oXK+QKJrXxPKDRf5jE0VNYuyi7",
      "updates": [
        {
          "amount": 1,
          "from": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
          "op": "OffChainTransfer",
          "to": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k"
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
  "id": -576460752303421527,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA8p4CcbRHKaYl13a2RwupeAVl2rTydHrXEijTZfN9BXkoQRR+yAuKhWq1bb7zk7x7FU1mAAa8Y4YyOfPvf1fLB7hI+EY5AqEGFGKM+lB8tMQjjhLxtxm6GzRvtMeQdh9zYT1jQH2jV8QFoBP1afxOR2e5qih2lzoF5MO6FyvkCia18Tyg0X+YxNFTTY1CCA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421527,
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA8p4CcbRHKaYl13a2RwupeAVl2rTydHrXEijTZfN9BXkoQRR+yAuKhWq1bb7zk7x7FU1mAAa8Y4YyOfPvf1fLB7hI+EY5AqEGFGKM+lB8tMQjjhLxtxm6GzRvtMeQdh9zYT1jQH2jV8QFoBP1afxOR2e5qih2lzoF5MO6FyvkCia18Tyg0X+YxNFTTY1CCA=="
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA8p4CcbRHKaYl13a2RwupeAVl2rTydHrXEijTZfN9BXkoQRR+yAuKhWq1bb7zk7x7FU1mAAa8Y4YyOfPvf1fLB7hI+EY5AqEGFGKM+lB8tMQjjhLxtxm6GzRvtMeQdh9zYT1jQH2jV8QFoBP1afxOR2e5qih2lzoF5MO6FyvkCia18Tyg0X+YxNFTTY1CCA=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421526,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
      "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421526,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
      "balance": 69999999999999
    },
    {
      "account": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421525,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421525,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhA8p4CcbRHKaYl13a2RwupeAVl2rTydHrXEijTZfN9BXkoQRR+yAuKhWq1bb7zk7x7FU1mAAa8Y4YyOfPvf1fLB7hI+EY5AqEGFGKM+lB8tMQjjhLxtxm6GzRvtMeQdh9zYT1jQH2jV8QFoBP1afxOR2e5qih2lzoF5MO6FyvkCia18Tyg0X+YxNFTTY1CCA==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCFYQZwC4TkePXj95x9iIc+N8rWNQqfXCZ6Z6Z1WeoY44vKCgEAhj+qJSJf/7DvQAGgIWkMmQL20NbNDS+4AoAYbniyxc/OU80prXb/Khbul2mLygoBAIYkYTnKgAEYbZ7/"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421524,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
      "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421524,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
      "balance": 40000000000001
    },
    {
      "account": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
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
    "from": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
    "to": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "error": {
    "code": 3,
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
        "from": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
        "to": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
      }
    }
  },
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
    "to": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "error": {
    "code": 3,
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
        "to": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
      }
    }
  },
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
    "from": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "error": {
    "code": 3,
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
        "from": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
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
    "from": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
    "to": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBhRijPpQfLTEI44S8bcZuhs0b7THkHYfc2E9Y0B9o1fEBqCGTspsLOSVRdxEadthlqBFsif6ugnTF45ftph52dPDYlW6dJ0=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
          "op": "OffChainTransfer",
          "to": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
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
  "id": -576460752303421523,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQYUYoz6UHy0xCOOEvG3GbobNG+0x5B2H3NhPWNAfaNXxAaghk7KbCzklUXcRGnbYZagRbIn+roJ0xeOX7aYednTw2IpvIY4"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQYUYoz6UHy0xCOOEvG3GbobNG+0x5B2H3NhPWNAfaNXxAaghk7KbCzklUXcRGnbYZagRbIn+roJ0xeOX7aYednTw2IpvIY4",
      "updates": [
        {
          "amount": 1,
          "from": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
          "op": "OffChainTransfer",
          "to": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
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
  "id": -576460752303421522,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAOuqPOrY478aLW64JZDGCqK/N5KAD+4KBzMz9eaBSzaZK/qAI9xMlSm2lsqD+ikwWXWIgIbICafmCxmebdiKCCLhI+EY5AqEGFGKM+lB8tMQjjhLxtxm6GzRvtMeQdh9zYT1jQH2jV8QGoIZOymws5JVF3ERp22GWoEWyJ/q6CdMXjl+2mHnZ08NiARSvlw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421522,
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAOuqPOrY478aLW64JZDGCqK/N5KAD+4KBzMz9eaBSzaZK/qAI9xMlSm2lsqD+ikwWXWIgIbICafmCxmebdiKCCLhI+EY5AqEGFGKM+lB8tMQjjhLxtxm6GzRvtMeQdh9zYT1jQH2jV8QGoIZOymws5JVF3ERp22GWoEWyJ/q6CdMXjl+2mHnZ08NiARSvlw=="
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
    "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAOuqPOrY478aLW64JZDGCqK/N5KAD+4KBzMz9eaBSzaZK/qAI9xMlSm2lsqD+ikwWXWIgIbICafmCxmebdiKCCLhI+EY5AqEGFGKM+lB8tMQjjhLxtxm6GzRvtMeQdh9zYT1jQH2jV8QGoIZOymws5JVF3ERp22GWoEWyJ/q6CdMXjl+2mHnZ08NiARSvlw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421521,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
      "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421521,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_FiRWKr2vkjXWNeqSPVMR5yvep8NcqM2XVx2WcoELmcGAAHy7k",
      "balance": 40000000000000
    },
    {
      "account": "ak_21jzHUXCDKj9arhRw4p7Xq7tedYMrRnvCazBdozR3v6dW8i81t",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421520,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_9yhynqPMcbMszgbzSMAJjajVsUkmAnq2mcQiQxG1Jdm8RcufW",
  "id": -576460752303421520,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhASFpDJkC9tDWzQ0vuAKAGG54ssXPzlPNKa12/yoW7pdpiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAOuqPOrY478aLW64JZDGCqK/N5KAD+4KBzMz9eaBSzaZK/qAI9xMlSm2lsqD+ikwWXWIgIbICafmCxmebdiKCCLhI+EY5AqEGFGKM+lB8tMQjjhLxtxm6GzRvtMeQdh9zYT1jQH2jV8QGoIZOymws5JVF3ERp22GWoEWyJ/q6CdMXjl+2mHnZ08NiARSvlw==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCFYQZwC4TkePXj95x9iIc+N8rWNQqfXCZ6Z6Z1WeoY44vKCgEAhj+qJSJgALDvQAGgIWkMmQL20NbNDS+4AoAYbniyxc/OU80prXb/Khbul2mLygoBAIYkYTnKgABam9vf"
  },
  "version": 1
}
```
