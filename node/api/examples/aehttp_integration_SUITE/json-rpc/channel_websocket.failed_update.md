
#### initiator init (2018-10-24 12:53:15.365)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ&role=initiator
```

#### responder init (2018-10-24 12:53:15.369)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ&role=responder
```

#### responder <--- (2018-10-24 12:53:16.371)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "undefined",
    "data": {
      "event": "channel_open"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:53:16.372)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "undefined",
    "data": {
      "event": "channel_accept"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:53:16.374)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": "undefined",
    "data": {
      "tx": "tx_3d11KjpALBGjNkDnd6KHWu5iTiKtNxx7QB3F4FAQKEUoRqgew2XUdpGzQSHzCU45vuAQtu9BwjdbpJixR7So3AVsan7KuCjyjhr7NDiNTQ75Reiaog9FiphxWu6wrqdFhLcvtZC2BQ516zK233PhbT2oNjp4QhvN2rgr57"
    }
  }
}
```

#### initiator ---> (2018-10-24 12:53:16.392)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HkzZRv6Xd4VPZ9Nbr4ZEdAcBrRieTZJ2m4xPcbuiMHHaEed47T3YUyh1uNUCwUzVd6pP57wD1VvvWUp7pJx8o8ZKdEGMYPanzHzyMFqAqrxuiSnFkZYxUAdyCmNbw59z3RxupkZRgzQF75xNucYyko6YfhpUhK71mffe3ADXJtuk8Dw6wPP3KcqUDhZbqLFPc2WmW9TeP8bvSDYLNUm9GiwG2uERYaz3GbPveiBSMQvvuXR3UqAyJuaQgMYbMkWRM"
  }
}
```

#### responder <--- (2018-10-24 12:53:16.393)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "undefined",
    "data": {
      "event": "funding_created"
    }
  }
}
```

#### responder <--- (2018-10-24 12:53:16.394)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": "undefined",
    "data": {
      "tx": "tx_3d11KjpALBGjNkDnd6KHWu5iTiKtNxx7QB3F4FAQKEUoRqgew2XUdpGzQSHzCU45vuAQtu9BwjdbpJixR7So3AVsan7KuCjyjhr7NDiNTQ75Reiaog9FiphxWu6wrqdFhLcvtZC2BQ516zK233PhbT2oNjp4QhvN2rgr57"
    }
  }
}
```

#### responder ---> (2018-10-24 12:53:16.394)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4Hm2gzDsiws24Y8jaYqTjqZh1WBoQy6BcGBakZe9GbeYvNN4osgvni52GcMZikzy1f7t5edvEUEkyVQJyfVjE48RnWpHuup3YVV5DAexpjzpXSNm6Zjz324Cckq8f1E1PMcWBD2UXupTgrTqNJeTYPdRgoMMWPZBYwfN8WeKJ3Njpbu8wTDeCBDnakkkWwNCVC4fn9smKM5LUjC7LYpuaZAzD2eRTDhjv5TemhpeJsBYG79zoPbYD22QHA7mc4XV4m"
  }
}
```

#### initiator <--- (2018-10-24 12:53:16.396)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "undefined",
    "data": {
      "event": "funding_signed"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:53:16.397)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "undefined",
    "data": {
      "tx": "tx_6jPYBUFTkcmPuxFB1VCyYUVqYM9QhzDYGjpWzFz5haJFycsputz2PyfKEA6tKCf1qM9vgfwepgUEqAxR2TTKPbmJ1UXbJc12DdbfvkZBebQjniynQTuduTbrQZgd9w871nPdHn6Pav3JMzyLke6st6apr1g3qkDLMvp9K3fKGuPYC2JqVLiztGPtnttVPGSzkbVRZXZL8krsn5HmQL7QRXkq2Zq88NH12pw8WZ5GZMeS5QLkSWeA2DzAVBs2VGUfdCoULgmsbZ4uu8sN6pjfmN9QzNXo2rErHTT4ijNUeoSQcKt6mLm1R2Aia2BHu2b2nS9smP5oEKaYeMEW1RArx17tRnZ4gtqRy8JEP"
    }
  }
}
```

#### responder <--- (2018-10-24 12:53:16.397)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "undefined",
    "data": {
      "tx": "tx_6jPYBUFTkcmPuxFB1VCyYUVqYM9QhzDYGjpWzFz5haJFycsputz2PyfKEA6tKCf1qM9vgfwepgUEqAxR2TTKPbmJ1UXbJc12DdbfvkZBebQjniynQTuduTbrQZgd9w871nPdHn6Pav3JMzyLke6st6apr1g3qkDLMvp9K3fKGuPYC2JqVLiztGPtnttVPGSzkbVRZXZL8krsn5HmQL7QRXkq2Zq88NH12pw8WZ5GZMeS5QLkSWeA2DzAVBs2VGUfdCoULgmsbZ4uu8sN6pjfmN9QzNXo2rErHTT4ijNUeoSQcKt6mLm1R2Aia2BHu2b2nS9smP5oEKaYeMEW1RArx17tRnZ4gtqRy8JEP"
    }
  }
}
```

#### initiator ---> (2018-10-24 12:53:17.509)
```javascript
{
  "id": -576460752303423477,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
      "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ"
    ]
  }
}
```

#### initiator <--- (2018-10-24 12:53:17.510)
```javascript
{
  "id": -576460752303423477,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
      "balance": 699
    },
    {
      "account": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
      "balance": 401
    }
  ]
}
```

#### initiator <--- (2018-10-24 12:53:20.835)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2t8GLdAJaB1JMy5p6p4BbBvzkFXXjsULWRKQ3JQoTRVM2QLB67",
    "data": {
      "event": "own_funding_locked"
    }
  }
}
```

#### responder <--- (2018-10-24 12:53:20.835)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2t8GLdAJaB1JMy5p6p4BbBvzkFXXjsULWRKQ3JQoTRVM2QLB67",
    "data": {
      "event": "own_funding_locked"
    }
  }
}
```

#### responder <--- (2018-10-24 12:53:20.836)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2t8GLdAJaB1JMy5p6p4BbBvzkFXXjsULWRKQ3JQoTRVM2QLB67",
    "data": {
      "event": "funding_locked"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:53:20.836)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2t8GLdAJaB1JMy5p6p4BbBvzkFXXjsULWRKQ3JQoTRVM2QLB67",
    "data": {
      "event": "funding_locked"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:53:20.838)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2t8GLdAJaB1JMy5p6p4BbBvzkFXXjsULWRKQ3JQoTRVM2QLB67",
    "data": {
      "event": "open"
    }
  }
}
```

#### responder <--- (2018-10-24 12:53:20.839)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2t8GLdAJaB1JMy5p6p4BbBvzkFXXjsULWRKQ3JQoTRVM2QLB67",
    "data": {
      "event": "open"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:53:20.840)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2t8GLdAJaB1JMy5p6p4BbBvzkFXXjsULWRKQ3JQoTRVM2QLB67",
    "data": {
      "state": "tx_6jPYBUFTkcmPuxFB1VCyYUVqYM9QhzDYGjpWzFz5haJFycsputz2PyfKEA6tKCf1qM9vgfwepgUEqAxR2TTKPbmJ1UXbJc12DdbfvkZBebQjniynQTuduTbrQZgd9w871nPdHn6Pav3JMzyLke6st6apr1g3qkDLMvp9K3fKGuPYC2JqVLiztGPtnttVPGSzkbVRZXZL8krsn5HmQL7QRXkq2Zq88NH12pw8WZ5GZMeS5QLkSWeA2DzAVBs2VGUfdCoULgmsbZ4uu8sN6pjfmN9QzNXo2rErHTT4ijNUeoSQcKt6mLm1R2Aia2BHu2b2nS9smP5oEKaYeMEW1RArx17tRnZ4gtqRy8JEP"
    }
  }
}
```

#### responder <--- (2018-10-24 12:53:20.840)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2t8GLdAJaB1JMy5p6p4BbBvzkFXXjsULWRKQ3JQoTRVM2QLB67",
    "data": {
      "state": "tx_6jPYBUFTkcmPuxFB1VCyYUVqYM9QhzDYGjpWzFz5haJFycsputz2PyfKEA6tKCf1qM9vgfwepgUEqAxR2TTKPbmJ1UXbJc12DdbfvkZBebQjniynQTuduTbrQZgd9w871nPdHn6Pav3JMzyLke6st6apr1g3qkDLMvp9K3fKGuPYC2JqVLiztGPtnttVPGSzkbVRZXZL8krsn5HmQL7QRXkq2Zq88NH12pw8WZ5GZMeS5QLkSWeA2DzAVBs2VGUfdCoULgmsbZ4uu8sN6pjfmN9QzNXo2rErHTT4ijNUeoSQcKt6mLm1R2Aia2BHu2b2nS9smP5oEKaYeMEW1RArx17tRnZ4gtqRy8JEP"
    }
  }
}
```

#### initiator: (2018-10-24 12:53:21.338)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-24 12:53:21.338)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-24 12:53:21.338)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-24 12:53:21.338)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-24 12:53:21.338)
> Channel is `open` and ready to use

#### responder: (2018-10-24 12:53:21.338)
> Channel is `open` and ready to use

#### initiator: (2018-10-24 12:53:21.374)
> Failing update, insufficient balance

#### initiator ---> (2018-10-24 12:53:21.374)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 10000,
    "from": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
    "to": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ"
  }
}
```

#### initiator <--- (2018-10-24 12:53:21.386)
```javascript
{
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1001,
        "message": "Insufficient balance"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 10000,
        "from": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
        "to": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0"
}
```

#### initiator: (2018-10-24 12:53:21.387)
> Failing update, negative amount

#### initiator ---> (2018-10-24 12:53:21.387)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": -1,
    "from": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
    "to": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ"
  }
}
```

#### initiator <--- (2018-10-24 12:53:21.389)
```javascript
{
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1002,
        "message": "Negative amount"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": -1,
        "from": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
        "to": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0"
}
```

#### initiator: (2018-10-24 12:53:21.389)
> Failing update, invalid pubkeys

#### initiator ---> (2018-10-24 12:53:21.389)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_11111111111111111111111111111115rHyByZ",
    "to": "ak_11111111111111111111111111111115sBJATr"
  }
}
```

#### initiator <--- (2018-10-24 12:53:21.391)
```javascript
{
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1003,
        "message": "Invalid pubkeys"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_11111111111111111111111111111115rHyByZ",
        "to": "ak_11111111111111111111111111111115sBJATr"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0"
}
```

#### responder: (2018-10-24 12:53:21.391)
> Failing update, insufficient balance

#### responder ---> (2018-10-24 12:53:21.392)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 10000,
    "from": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
    "to": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY"
  }
}
```

#### responder <--- (2018-10-24 12:53:21.398)
```javascript
{
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1001,
        "message": "Insufficient balance"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 10000,
        "from": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
        "to": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0"
}
```

#### responder: (2018-10-24 12:53:21.398)
> Failing update, negative amount

#### responder ---> (2018-10-24 12:53:21.398)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": -1,
    "from": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
    "to": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY"
  }
}
```

#### responder <--- (2018-10-24 12:53:21.399)
```javascript
{
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1002,
        "message": "Negative amount"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": -1,
        "from": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
        "to": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0"
}
```

#### responder: (2018-10-24 12:53:21.399)
> Failing update, invalid pubkeys

#### responder ---> (2018-10-24 12:53:21.399)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_11111111111111111111111111111115sBJATr",
    "to": "ak_11111111111111111111111111111115rHyByZ"
  }
}
```

#### responder <--- (2018-10-24 12:53:21.401)
```javascript
{
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1003,
        "message": "Invalid pubkeys"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_11111111111111111111111111111115sBJATr",
        "to": "ak_11111111111111111111111111111115rHyByZ"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0"
}
```
