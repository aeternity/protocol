
#### initiator init (2018-10-24 12:59:22.816)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=initiator
```

#### responder init (2018-10-24 12:59:22.819)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=responder
```

#### responder <--- (2018-10-24 12:59:23.823)
```javascript
{
  "action": "info",
  "payload": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-24 12:59:23.824)
```javascript
{
  "action": "info",
  "payload": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-24 12:59:23.827)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_3d11KjpALm3t32sAMLL9Y5p9SUg9j82o5Er3hc4WTAmdXk3cXjxDydY4eoq6STXDutDQ59tM59bMr9CogemLkb4tUXrrZYvPc4DkdzkXhqGZjnzLVRAYpjMHXUeVmmqr9Fk96GrERRgHqJTaNp7wfhyEnqvb1nHjFV6BnC"
  },
  "tag": "initiator_sign"
}
```

#### initiator ---> (2018-10-24 12:59:23.846)
```javascript
{
  "action": "initiator_sign",
  "payload": {
    "tx": "tx_4L9GSozvM4HnCFe3NPYo9JkefUQaQyW1aenSg1C5iJTXfYMdem1pHHvnv5X9L3wfSErJBEnweuJBRBhyKnh9kfb4G7fQETNYx76W9q2gTkySkQhMg6vDvmcD4m1qDMSN2TuzY2Tkgt3x6ESjNMvjzmpL9cEWtNVpAcHJs4VJmXyTHXCRjyjh5rkzLfXGSHf3TsPpR5qFiEtsTuwdzvUCcz4HGhmTLdCwy2RtwhdXJ52EqMo5p9Qa3aUynkqrnKmgYbGFRB3bH8Q"
  }
}
```

#### responder <--- (2018-10-24 12:59:23.847)
```javascript
{
  "action": "info",
  "payload": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-24 12:59:23.848)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_3d11KjpALm3t32sAMLL9Y5p9SUg9j82o5Er3hc4WTAmdXk3cXjxDydY4eoq6STXDutDQ59tM59bMr9CogemLkb4tUXrrZYvPc4DkdzkXhqGZjnzLVRAYpjMHXUeVmmqr9Fk96GrERRgHqJTaNp7wfhyEnqvb1nHjFV6BnC"
  },
  "tag": "responder_sign"
}
```

#### responder ---> (2018-10-24 12:59:23.848)
```javascript
{
  "action": "responder_sign",
  "payload": {
    "tx": "tx_4L9GSozvM4HmVMaEUujbtMtm9hayb2Mn1gXukaanfA7tAAm4K92fA4XZKuyRzPY59zU6TSY1YDRMUSKFNTJKFPPN1uxUCW9TrDHdK8h2n96cLpjiT3qfpqrefdq9pXhWhjWpxuQhXSx5GLsjasf6MGzrke8puTxdqwMuRRTBKqnAjEq7Tc4hGchM3kzhCmeV7Vs1UsCRj1cN4isgxYQLXGG9RMkjFJWTq9J9Vkg8ep5GdJ11zQxWHQDFxjv3UfLu8TmA2r64JRu"
  }
}
```

#### initiator <--- (2018-10-24 12:59:23.850)
```javascript
{
  "action": "info",
  "payload": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-24 12:59:23.851)
```javascript
{
  "action": "on_chain_tx",
  "payload": {
    "tx": "tx_6jPYBUFTkcmQmTW5CDNwGZLmxRTASKGWKc84FH8zsrDnR2Cwe8Gy5zsJzWbTZFhYqazZxEJ5Mp9hNBufXSssj4D96NFHW978mT4sCYwKGmbALmw2Bq8oqFgwo4RuQynSHy7WSpDypMSiXzURm3HH8XKE9Eej2bznCQ5AG34niyNMaQXVkgDDKA7ELfsc7R8zgSv9NP57FztnTteckjmCXVBHF2ZJYQvefF3B5jj3GvcUbVcqTACawd9PAKakcFWtYYUxqa8dCBRM332um7HdgKnQgS2mXJtaspUAgTAyGeHSHUXsQYC6RgygP22JBzcV2AyMrHeVCkN6WSkGKQHBZDbEjRskEq9e5jQ9V"
  }
}
```

#### initiator <--- (2018-10-24 12:59:23.851)
```javascript
{
  "action": "on_chain_tx",
  "payload": {
    "tx": "tx_6jPYBUFTkcmQmTW5CDNwGZLmxRTASKGWKc84FH8zsrDnR2Cwe8Gy5zsJzWbTZFhYqazZxEJ5Mp9hNBufXSssj4D96NFHW978mT4sCYwKGmbALmw2Bq8oqFgwo4RuQynSHy7WSpDypMSiXzURm3HH8XKE9Eej2bznCQ5AG34niyNMaQXVkgDDKA7ELfsc7R8zgSv9NP57FztnTteckjmCXVBHF2ZJYQvefF3B5jj3GvcUbVcqTACawd9PAKakcFWtYYUxqa8dCBRM332um7HdgKnQgS2mXJtaspUAgTAyGeHSHUXsQYC6RgygP22JBzcV2AyMrHeVCkN6WSkGKQHBZDbEjRskEq9e5jQ9V"
  }
}
```

#### initiator ---> (2018-10-24 12:59:24.811)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
      "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- (2018-10-24 12:59:24.812)
```javascript
{
  "action": "get",
  "payload": [
    {
      "account": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
      "balance": 699
    },
    {
      "account": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "balance": 401
    }
  ],
  "tag": "balances"
}
```

#### initiator <--- (2018-10-24 12:59:26.634)
```javascript
{
  "action": "info",
  "channel_id": "ch_gntuZ9odunoiWwyypvtkjBofJFrH75bmDcCpfZXiEuuLJEvdU",
  "payload": {
    "event": "own_funding_locked"
  }
}
```

#### responder <--- (2018-10-24 12:59:26.634)
```javascript
{
  "action": "info",
  "channel_id": "ch_gntuZ9odunoiWwyypvtkjBofJFrH75bmDcCpfZXiEuuLJEvdU",
  "payload": {
    "event": "own_funding_locked"
  }
}
```

#### responder <--- (2018-10-24 12:59:26.635)
```javascript
{
  "action": "info",
  "channel_id": "ch_gntuZ9odunoiWwyypvtkjBofJFrH75bmDcCpfZXiEuuLJEvdU",
  "payload": {
    "event": "funding_locked"
  }
}
```

#### initiator <--- (2018-10-24 12:59:26.635)
```javascript
{
  "action": "info",
  "channel_id": "ch_gntuZ9odunoiWwyypvtkjBofJFrH75bmDcCpfZXiEuuLJEvdU",
  "payload": {
    "event": "funding_locked"
  }
}
```

#### responder <--- (2018-10-24 12:59:26.637)
```javascript
{
  "action": "info",
  "channel_id": "ch_gntuZ9odunoiWwyypvtkjBofJFrH75bmDcCpfZXiEuuLJEvdU",
  "payload": {
    "event": "open"
  }
}
```

#### initiator <--- (2018-10-24 12:59:26.638)
```javascript
{
  "action": "info",
  "channel_id": "ch_gntuZ9odunoiWwyypvtkjBofJFrH75bmDcCpfZXiEuuLJEvdU",
  "payload": {
    "event": "open"
  }
}
```

#### responder <--- (2018-10-24 12:59:26.638)
```javascript
{
  "action": "update",
  "channel_id": "ch_gntuZ9odunoiWwyypvtkjBofJFrH75bmDcCpfZXiEuuLJEvdU",
  "payload": {
    "state": "tx_6jPYBUFTkcmQmTW5CDNwGZLmxRTASKGWKc84FH8zsrDnR2Cwe8Gy5zsJzWbTZFhYqazZxEJ5Mp9hNBufXSssj4D96NFHW978mT4sCYwKGmbALmw2Bq8oqFgwo4RuQynSHy7WSpDypMSiXzURm3HH8XKE9Eej2bznCQ5AG34niyNMaQXVkgDDKA7ELfsc7R8zgSv9NP57FztnTteckjmCXVBHF2ZJYQvefF3B5jj3GvcUbVcqTACawd9PAKakcFWtYYUxqa8dCBRM332um7HdgKnQgS2mXJtaspUAgTAyGeHSHUXsQYC6RgygP22JBzcV2AyMrHeVCkN6WSkGKQHBZDbEjRskEq9e5jQ9V"
  }
}
```

#### initiator <--- (2018-10-24 12:59:26.639)
```javascript
{
  "action": "update",
  "channel_id": "ch_gntuZ9odunoiWwyypvtkjBofJFrH75bmDcCpfZXiEuuLJEvdU",
  "payload": {
    "state": "tx_6jPYBUFTkcmQmTW5CDNwGZLmxRTASKGWKc84FH8zsrDnR2Cwe8Gy5zsJzWbTZFhYqazZxEJ5Mp9hNBufXSssj4D96NFHW978mT4sCYwKGmbALmw2Bq8oqFgwo4RuQynSHy7WSpDypMSiXzURm3HH8XKE9Eej2bznCQ5AG34niyNMaQXVkgDDKA7ELfsc7R8zgSv9NP57FztnTteckjmCXVBHF2ZJYQvefF3B5jj3GvcUbVcqTACawd9PAKakcFWtYYUxqa8dCBRM332um7HdgKnQgS2mXJtaspUAgTAyGeHSHUXsQYC6RgygP22JBzcV2AyMrHeVCkN6WSkGKQHBZDbEjRskEq9e5jQ9V"
  }
}
```

#### initiator: (2018-10-24 12:59:26.940)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-24 12:59:26.940)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-24 12:59:26.940)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-24 12:59:26.940)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-24 12:59:26.940)
> Channel is `open` and ready to use

#### responder: (2018-10-24 12:59:26.941)
> Channel is `open` and ready to use

#### initiator: (2018-10-24 12:59:26.977)
> Failing update, insufficient balance

#### initiator ---> (2018-10-24 12:59:26.977)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 10000,
    "from": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
    "to": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt"
  },
  "tag": "new"
}
```

#### initiator <--- (2018-10-24 12:59:26.985)
```javascript
{
  "action": "error",
  "payload": {
    "reason": "insufficient_balance",
    "request": {
      "action": "update",
      "method": "channels.update.new",
      "payload": {
        "amount": 10000,
        "from": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
        "to": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt"
      },
      "tag": "new"
    }
  }
}
```

#### initiator: (2018-10-24 12:59:26.986)
> Failing update, negative amount

#### initiator ---> (2018-10-24 12:59:26.987)
```javascript
{
  "action": "update",
  "payload": {
    "amount": -1,
    "from": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
    "to": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt"
  },
  "tag": "new"
}
```

#### initiator <--- (2018-10-24 12:59:26.988)
```javascript
{
  "action": "error",
  "payload": {
    "reason": "negative_amount",
    "request": {
      "action": "update",
      "method": "channels.update.new",
      "payload": {
        "amount": -1,
        "from": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
        "to": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt"
      },
      "tag": "new"
    }
  }
}
```

#### initiator: (2018-10-24 12:59:26.989)
> Failing update, invalid pubkeys

#### initiator ---> (2018-10-24 12:59:26.989)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 1,
    "from": "ak_11111111111111111111111111111115rHyByZ",
    "to": "ak_11111111111111111111111111111115sBJATr"
  },
  "tag": "new"
}
```

#### initiator <--- (2018-10-24 12:59:26.992)
```javascript
{
  "action": "error",
  "payload": {
    "reason": "invalid_pubkeys",
    "request": {
      "action": "update",
      "method": "channels.update.new",
      "payload": {
        "amount": 1,
        "from": "ak_11111111111111111111111111111115rHyByZ",
        "to": "ak_11111111111111111111111111111115sBJATr"
      },
      "tag": "new"
    }
  }
}
```

#### responder: (2018-10-24 12:59:26.993)
> Failing update, insufficient balance

#### responder ---> (2018-10-24 12:59:26.993)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 10000,
    "from": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
    "to": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
  },
  "tag": "new"
}
```

#### responder <--- (2018-10-24 12:59:27.2)
```javascript
{
  "action": "error",
  "payload": {
    "reason": "insufficient_balance",
    "request": {
      "action": "update",
      "method": "channels.update.new",
      "payload": {
        "amount": 10000,
        "from": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
        "to": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
      },
      "tag": "new"
    }
  }
}
```

#### responder: (2018-10-24 12:59:27.3)
> Failing update, negative amount

#### responder ---> (2018-10-24 12:59:27.3)
```javascript
{
  "action": "update",
  "payload": {
    "amount": -1,
    "from": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
    "to": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
  },
  "tag": "new"
}
```

#### responder <--- (2018-10-24 12:59:27.5)
```javascript
{
  "action": "error",
  "payload": {
    "reason": "negative_amount",
    "request": {
      "action": "update",
      "method": "channels.update.new",
      "payload": {
        "amount": -1,
        "from": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
        "to": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
      },
      "tag": "new"
    }
  }
}
```

#### responder: (2018-10-24 12:59:27.5)
> Failing update, invalid pubkeys

#### responder ---> (2018-10-24 12:59:27.6)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 1,
    "from": "ak_11111111111111111111111111111115sBJATr",
    "to": "ak_11111111111111111111111111111115rHyByZ"
  },
  "tag": "new"
}
```

#### responder <--- (2018-10-24 12:59:27.8)
```javascript
{
  "action": "error",
  "payload": {
    "reason": "invalid_pubkeys",
    "request": {
      "action": "update",
      "method": "channels.update.new",
      "payload": {
        "amount": 1,
        "from": "ak_11111111111111111111111111111115sBJATr",
        "to": "ak_11111111111111111111111111111115rHyByZ"
      },
      "tag": "new"
    }
  }
}
```
