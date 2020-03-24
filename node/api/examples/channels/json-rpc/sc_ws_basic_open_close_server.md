
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
      "fsm_id": "ba_SrA0cbmpwUGmV5at9mq/La1KThi8v2G0pmTshQlzXbnu6bzf"
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
      "fsm_id": "ba_SYWD1QzLaqvxi9VeP6rY7AxOmCzgev81Aa47fplfk+crcEa/"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsEgZb92g==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423426,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECRHWOZqAUrZwLx8SbqOlA7tIy18PFWpPf8JL9IBjCJ5Sy5P4lALN2wcqcjumhzHJ8mLJTVWIgTgKpilACemeIPuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LBKzs8IY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423426,
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "fsm_id": "ba_SYWD1QzLaqvxi9VeP6rY7AxOmCzgev81Aa47fplfk+crcEa/",
      "signed_tx": "tx_+MsLAfhCuECRHWOZqAUrZwLx8SbqOlA7tIy18PFWpPf8JL9IBjCJ5Sy5P4lALN2wcqcjumhzHJ8mLJTVWIgTgKpilACemeIPuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LBKzs8IY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423425,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAdEk8b1+nem/jcMJGnozUmMkk1QeRiFocFsOlzXaG3RRzii/riec3V/yDO28mPrhntvKTe2loSziM5fGrD887BrhAkR1jmagFK2cC8fEm6jpQO7SMtfDxVqT3/CS/SAYwieUsuT+JQCzdsHKnI7pocxyfJiyU1ViIE4CqYpQAnpniD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwSqs4dd"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423425,
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAdEk8b1+nem/jcMJGnozUmMkk1QeRiFocFsOlzXaG3RRzii/riec3V/yDO28mPrhntvKTe2loSziM5fGrD887BrhAkR1jmagFK2cC8fEm6jpQO7SMtfDxVqT3/CS/SAYwieUsuT+JQCzdsHKnI7pocxyfJiyU1ViIE4CqYpQAnpniD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwSqs4dd",
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_SrA0cbmpwUGmV5at9mq/La1KThi8v2G0pmTshQlzXbnu6bzf"
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAdEk8b1+nem/jcMJGnozUmMkk1QeRiFocFsOlzXaG3RRzii/riec3V/yDO28mPrhntvKTe2loSziM5fGrD887BrhAkR1jmagFK2cC8fEm6jpQO7SMtfDxVqT3/CS/SAYwieUsuT+JQCzdsHKnI7pocxyfJiyU1ViIE4CqYpQAnpniD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwSqs4dd",
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAdEk8b1+nem/jcMJGnozUmMkk1QeRiFocFsOlzXaG3RRzii/riec3V/yDO28mPrhntvKTe2loSziM5fGrD887BrhAkR1jmagFK2cC8fEm6jpQO7SMtfDxVqT3/CS/SAYwieUsuT+JQCzdsHKnI7pocxyfJiyU1ViIE4CqYpQAnpniD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwSqs4dd",
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAdEk8b1+nem/jcMJGnozUmMkk1QeRiFocFsOlzXaG3RRzii/riec3V/yDO28mPrhntvKTe2loSziM5fGrD887BrhAkR1jmagFK2cC8fEm6jpQO7SMtfDxVqT3/CS/SAYwieUsuT+JQCzdsHKnI7pocxyfJiyU1ViIE4CqYpQAnpniD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwSqs4dd",
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "message": {
        "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "message": {
        "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
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
  "id": -576460752303423424,
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
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423424,
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "state": "tx_+QENCwH4hLhAdEk8b1+nem/jcMJGnozUmMkk1QeRiFocFsOlzXaG3RRzii/riec3V/yDO28mPrhntvKTe2loSziM5fGrD887BrhAkR1jmagFK2cC8fEm6jpQO7SMtfDxVqT3/CS/SAYwieUsuT+JQCzdsHKnI7pocxyfJiyU1ViIE4CqYpQAnpniD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwSqs4dd"
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "state": "tx_+QENCwH4hLhAdEk8b1+nem/jcMJGnozUmMkk1QeRiFocFsOlzXaG3RRzii/riec3V/yDO28mPrhntvKTe2loSziM5fGrD887BrhAkR1jmagFK2cC8fEm6jpQO7SMtfDxVqT3/CS/SAYwieUsuT+JQCzdsHKnI7pocxyfJiyU1ViIE4CqYpQAnpniD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwSqs4dd"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423423,
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
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423423,
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
    "amount": "1",
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "error": {
    "code": 3,
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
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
      }
    }
  },
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "error": {
    "code": 3,
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
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
      }
    }
  },
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
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "error": {
    "code": 3,
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
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
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
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "meta": 17,
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
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
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "meta": 17,
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
      }
    }
  },
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpKUfo6qJ6a9Sc/i4v0e7Fh9LzKzCZVCHn7wwJifSeCCAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAlAHnF4=",
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
  "id": -576460752303423422,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEARGwF4fu6yqy1Mu/RGUyLkKdDvZLatlX1Tj67kcjlJjylyXN8xw+jKcNP9cf5dFjlAIEKXF51/MnC+K7FX+ZUHuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgI135nC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423422,
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "signed_tx": "tx_+JALAfhCuEARGwF4fu6yqy1Mu/RGUyLkKdDvZLatlX1Tj67kcjlJjylyXN8xw+jKcNP9cf5dFjlAIEKXF51/MnC+K7FX+ZUHuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgI135nC",
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
  "id": -576460752303423421,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEARGwF4fu6yqy1Mu/RGUyLkKdDvZLatlX1Tj67kcjlJjylyXN8xw+jKcNP9cf5dFjlAIEKXF51/MnC+K7FX+ZUHuEBTWtkeKczQIfjL7eMtPok8qhsK+oZeFuu8k/ibdIrZ/SOWH/+wUw3QcD9BZWtzLRSqJppeEb35z961BrrGAnoMuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIOYCtI"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423421,
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "state": "tx_+NILAfiEuEARGwF4fu6yqy1Mu/RGUyLkKdDvZLatlX1Tj67kcjlJjylyXN8xw+jKcNP9cf5dFjlAIEKXF51/MnC+K7FX+ZUHuEBTWtkeKczQIfjL7eMtPok8qhsK+oZeFuu8k/ibdIrZ/SOWH/+wUw3QcD9BZWtzLRSqJppeEb35z961BrrGAnoMuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIOYCtI"
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "state": "tx_+NILAfiEuEARGwF4fu6yqy1Mu/RGUyLkKdDvZLatlX1Tj67kcjlJjylyXN8xw+jKcNP9cf5dFjlAIEKXF51/MnC+K7FX+ZUHuEBTWtkeKczQIfjL7eMtPok8qhsK+oZeFuu8k/ibdIrZ/SOWH/+wUw3QcD9BZWtzLRSqJppeEb35z961BrrGAnoMuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIOYCtI"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423420,
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
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423420,
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
  "id": -576460752303423419,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423419,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEARGwF4fu6yqy1Mu/RGUyLkKdDvZLatlX1Tj67kcjlJjylyXN8xw+jKcNP9cf5dFjlAIEKXF51/MnC+K7FX+ZUHuEBTWtkeKczQIfjL7eMtPok8qhsK+oZeFuu8k/ibdIrZ/SOWH/+wUw3QcD9BZWtzLRSqJppeEb35z961BrrGAnoMuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIOYCtI",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423418,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423418,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000002
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
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
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "error": {
    "code": 3,
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
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
    }
  },
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "error": {
    "code": 3,
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
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
    }
  },
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
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "error": {
    "code": 3,
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
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
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
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "meta": 17,
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
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
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "meta": 17,
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
    }
  },
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
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpKUfo6qJ6a9Sc/i4v0e7Fh9LzKzCZVCHn7wwJifSeCCA6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC/CunB4=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "id": -576460752303423417,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDW6eABhcfN1YvJzJ0t59WJX8Ey9jCbhbYCR7KdqlQfZwNea/XoT928mrpv6rq+nbS0Imk++H8JwlYhBUMre+gKuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsQuxTN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423417,
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDW6eABhcfN1YvJzJ0t59WJX8Ey9jCbhbYCR7KdqlQfZwNea/XoT928mrpv6rq+nbS0Imk++H8JwlYhBUMre+gKuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsQuxTN",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "id": -576460752303423416,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDW6eABhcfN1YvJzJ0t59WJX8Ey9jCbhbYCR7KdqlQfZwNea/XoT928mrpv6rq+nbS0Imk++H8JwlYhBUMre+gKuED6nEqk73+3Gtcd4vuNSCR/E+IwG/oNvxHMgVWeD6WsyTRjQCJ1gucmUNKXJqkN7DUeaPMWURoyDjldoQbhNKYCuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtcPGZj"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423416,
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "state": "tx_+NILAfiEuEDW6eABhcfN1YvJzJ0t59WJX8Ey9jCbhbYCR7KdqlQfZwNea/XoT928mrpv6rq+nbS0Imk++H8JwlYhBUMre+gKuED6nEqk73+3Gtcd4vuNSCR/E+IwG/oNvxHMgVWeD6WsyTRjQCJ1gucmUNKXJqkN7DUeaPMWURoyDjldoQbhNKYCuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtcPGZj"
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "state": "tx_+NILAfiEuEDW6eABhcfN1YvJzJ0t59WJX8Ey9jCbhbYCR7KdqlQfZwNea/XoT928mrpv6rq+nbS0Imk++H8JwlYhBUMre+gKuED6nEqk73+3Gtcd4vuNSCR/E+IwG/oNvxHMgVWeD6WsyTRjQCJ1gucmUNKXJqkN7DUeaPMWURoyDjldoQbhNKYCuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtcPGZj"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423415,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423415,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000001
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423414,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423414,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDW6eABhcfN1YvJzJ0t59WJX8Ey9jCbhbYCR7KdqlQfZwNea/XoT928mrpv6rq+nbS0Imk++H8JwlYhBUMre+gKuED6nEqk73+3Gtcd4vuNSCR/E+IwG/oNvxHMgVWeD6WsyTRjQCJ1gucmUNKXJqkN7DUeaPMWURoyDjldoQbhNKYCuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtcPGZj",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423413,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423413,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000001
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
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
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "error": {
    "code": 3,
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
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
    }
  },
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "error": {
    "code": 3,
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
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
    }
  },
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
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "error": {
    "code": 3,
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
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
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
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "meta": 17,
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
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
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "meta": 17,
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
    }
  },
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
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpKUfo6qJ6a9Sc/i4v0e7Fh9LzKzCZVCHn7wwJifSeCCBKCPVbQrAfYXrWTP0iwmtWIe9nj7Tuv+WHg7LyUfwRTSMX6rCUs=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "id": -576460752303423412,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED52bocgOOtTjt7O51UnY7uaBpKlJ+qmhzdE//p0z6fMqo4zlbt4ZmzEajhg9ZahcOI/g1b5t/CjJxuXw5NUTILuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jFS8PjI"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423412,
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "signed_tx": "tx_+JALAfhCuED52bocgOOtTjt7O51UnY7uaBpKlJ+qmhzdE//p0z6fMqo4zlbt4ZmzEajhg9ZahcOI/g1b5t/CjJxuXw5NUTILuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jFS8PjI",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "id": -576460752303423411,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDc6WlhgPKyFI3nJaweMRiiXrbbmqtMyqda4H63u7JS+ZQwFLWFJfruxTH/McsF3k/Jkrfy7+GGmy2tKikSIm4KuED52bocgOOtTjt7O51UnY7uaBpKlJ+qmhzdE//p0z6fMqo4zlbt4ZmzEajhg9ZahcOI/g1b5t/CjJxuXw5NUTILuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jE7jjBK"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423411,
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "state": "tx_+NILAfiEuEDc6WlhgPKyFI3nJaweMRiiXrbbmqtMyqda4H63u7JS+ZQwFLWFJfruxTH/McsF3k/Jkrfy7+GGmy2tKikSIm4KuED52bocgOOtTjt7O51UnY7uaBpKlJ+qmhzdE//p0z6fMqo4zlbt4ZmzEajhg9ZahcOI/g1b5t/CjJxuXw5NUTILuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jE7jjBK"
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "state": "tx_+NILAfiEuEDc6WlhgPKyFI3nJaweMRiiXrbbmqtMyqda4H63u7JS+ZQwFLWFJfruxTH/McsF3k/Jkrfy7+GGmy2tKikSIm4KuED52bocgOOtTjt7O51UnY7uaBpKlJ+qmhzdE//p0z6fMqo4zlbt4ZmzEajhg9ZahcOI/g1b5t/CjJxuXw5NUTILuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jE7jjBK"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423410,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423410,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000000
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423409,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423409,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDc6WlhgPKyFI3nJaweMRiiXrbbmqtMyqda4H63u7JS+ZQwFLWFJfruxTH/McsF3k/Jkrfy7+GGmy2tKikSIm4KuED52bocgOOtTjt7O51UnY7uaBpKlJ+qmhzdE//p0z6fMqo4zlbt4ZmzEajhg9ZahcOI/g1b5t/CjJxuXw5NUTILuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jE7jjBK",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJgALDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgACNzKhd"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423408,
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
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423408,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 70000000000000
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
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
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "error": {
    "code": 3,
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
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
      }
    }
  },
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "error": {
    "code": 3,
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
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
      }
    }
  },
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
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "error": {
    "code": 3,
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
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
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
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "meta": 17,
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
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
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "meta": 17,
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
      }
    }
  },
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpKUfo6qJ6a9Sc/i4v0e7Fh9LzKzCZVCHn7wwJifSeCCBaAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC0e0glQ=",
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
  "id": -576460752303423407,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDS0HqIw//59QZrr68gd3fhCPu2g2ktrM7qhNbx7qCFv41Hol2w49lYI890vc7ZV45HnXe6koEy4xc9SJuPwBcPuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvDCmwH"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423407,
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDS0HqIw//59QZrr68gd3fhCPu2g2ktrM7qhNbx7qCFv41Hol2w49lYI890vc7ZV45HnXe6koEy4xc9SJuPwBcPuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvDCmwH",
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
  "id": -576460752303423406,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBSOblA7sY5PFLryjFi23GNCyudeGPgei5mvsY1EFBwSw4+LsCS1/Z1pboDnh1CPYDiWbmtM57PmYtxIAUx4YAHuEDS0HqIw//59QZrr68gd3fhCPu2g2ktrM7qhNbx7qCFv41Hol2w49lYI890vc7ZV45HnXe6koEy4xc9SJuPwBcPuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsn+hpq"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423406,
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "state": "tx_+NILAfiEuEBSOblA7sY5PFLryjFi23GNCyudeGPgei5mvsY1EFBwSw4+LsCS1/Z1pboDnh1CPYDiWbmtM57PmYtxIAUx4YAHuEDS0HqIw//59QZrr68gd3fhCPu2g2ktrM7qhNbx7qCFv41Hol2w49lYI890vc7ZV45HnXe6koEy4xc9SJuPwBcPuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsn+hpq"
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "state": "tx_+NILAfiEuEBSOblA7sY5PFLryjFi23GNCyudeGPgei5mvsY1EFBwSw4+LsCS1/Z1pboDnh1CPYDiWbmtM57PmYtxIAUx4YAHuEDS0HqIw//59QZrr68gd3fhCPu2g2ktrM7qhNbx7qCFv41Hol2w49lYI890vc7ZV45HnXe6koEy4xc9SJuPwBcPuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsn+hpq"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423405,
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
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423405,
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
  "id": -576460752303423404,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423404,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBSOblA7sY5PFLryjFi23GNCyudeGPgei5mvsY1EFBwSw4+LsCS1/Z1pboDnh1CPYDiWbmtM57PmYtxIAUx4YAHuEDS0HqIw//59QZrr68gd3fhCPu2g2ktrM7qhNbx7qCFv41Hol2w49lYI890vc7ZV45HnXe6koEy4xc9SJuPwBcPuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsn+hpq",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423403,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423403,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000001
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
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
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "error": {
    "code": 3,
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
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
    }
  },
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "error": {
    "code": 3,
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
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
    }
  },
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
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "error": {
    "code": 3,
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
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
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
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "meta": 17,
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
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
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "meta": 17,
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
    }
  },
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
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBpKUfo6qJ6a9Sc/i4v0e7Fh9LzKzCZVCHn7wwJifSeCCBqCPVbQrAfYXrWTP0iwmtWIe9nj7Tuv+WHg7LyUfwRTSMYfmhaw=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "id": -576460752303423402,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECS7MFqDwtd1U69qwEdUJ6CtKOEmm8X5ZXz10IBMsM8eTKAW6oYlQK256KoAly4taev9aFXwczMboyiZ/XM150EuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jEXt+P6"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423402,
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "signed_tx": "tx_+JALAfhCuECS7MFqDwtd1U69qwEdUJ6CtKOEmm8X5ZXz10IBMsM8eTKAW6oYlQK256KoAly4taev9aFXwczMboyiZ/XM150EuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jEXt+P6",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "id": -576460752303423401,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBG3eCUVZqmOH8aHnOAk8jenGEf+GF68mF6nKE7FtQA8azEOllDq68mxKxuAJFLqu2dWYhGB45uWdGDMTxE/0gFuECS7MFqDwtd1U69qwEdUJ6CtKOEmm8X5ZXz10IBMsM8eTKAW6oYlQK256KoAly4taev9aFXwczMboyiZ/XM150EuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHwnU6O"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423401,
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "state": "tx_+NILAfiEuEBG3eCUVZqmOH8aHnOAk8jenGEf+GF68mF6nKE7FtQA8azEOllDq68mxKxuAJFLqu2dWYhGB45uWdGDMTxE/0gFuECS7MFqDwtd1U69qwEdUJ6CtKOEmm8X5ZXz10IBMsM8eTKAW6oYlQK256KoAly4taev9aFXwczMboyiZ/XM150EuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHwnU6O"
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
    "data": {
      "state": "tx_+NILAfiEuEBG3eCUVZqmOH8aHnOAk8jenGEf+GF68mF6nKE7FtQA8azEOllDq68mxKxuAJFLqu2dWYhGB45uWdGDMTxE/0gFuECS7MFqDwtd1U69qwEdUJ6CtKOEmm8X5ZXz10IBMsM8eTKAW6oYlQK256KoAly4taev9aFXwczMboyiZ/XM150EuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHwnU6O"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423400,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423400,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000000
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423399,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423399,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBG3eCUVZqmOH8aHnOAk8jenGEf+GF68mF6nKE7FtQA8azEOllDq68mxKxuAJFLqu2dWYhGB45uWdGDMTxE/0gFuECS7MFqDwtd1U69qwEdUJ6CtKOEmm8X5ZXz10IBMsM8eTKAW6oYlQK256KoAly4taev9aFXwczMboyiZ/XM150EuEj4RjkCoQaSlH6OqiemvUnP4uL9HuxYfS8yswmVQh5+8MCYn0ngggagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHwnU6O",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJgALDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgACNzKhd"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423398,
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
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423398,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423397,
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
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
    "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
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
  "channel_id": "ch_27ZC4rnKZoLxJVapGmZK1WJyMYjufGFvzDqEL5cnK1CH2kZHN1",
  "id": -576460752303423397,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
