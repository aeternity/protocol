
#### initiator init (2018-10-24 13:00:56.838)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=initiator
```

#### responder init (2018-10-24 13:00:56.842)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=responder
```

#### responder <--- (2018-10-24 13:00:57.843)
```javascript
{
  "action": "info",
  "payload": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-24 13:00:57.846)
```javascript
{
  "action": "info",
  "payload": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-24 13:00:57.856)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_3d11KjpALm3t32sAMLL9Y5p9SUg9j82o5Er3hc4WTAmdXk3cXjxDydY4eoq6STXDutDQ59tM59bMr9CogemLkb4tUXrrZYvPc4DkdzkXhqGZjnzLVRAYpjMHXUeVmmqr9Fk96GrERRgHqJTaNp7wfhyEnqvb1nHkSXRK27"
  },
  "tag": "initiator_sign"
}
```

#### initiator ---> (2018-10-24 13:00:57.886)
```javascript
{
  "action": "initiator_sign",
  "payload": {
    "tx": "tx_4L9GSozvM4HjysGu9Dh4yXuhPx5WLgn1jpRSpZUkjTuNoLpjF5UKWGK958K5RaqhWiJXf2EGjMzpoKRS6c3JZGQscQShYf3dG5yDfjkghD4QXZsUZt3YikMmcxDEtqk6puc2MEyMt2okqfgtRGaWoALcoWXerJTCZwwBBcKHAmKaLRBe1dYajdoMehgNdNzsLgcTczpfKszWQj2EoqDLHHg5hrQh5CZ9uRsXVH6dis4K8jFzQVPGULADhgZ4n64B6GcEYrEHbjY"
  }
}
```

#### responder <--- (2018-10-24 13:00:57.887)
```javascript
{
  "action": "info",
  "payload": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-24 13:00:57.888)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_3d11KjpALm3t32sAMLL9Y5p9SUg9j82o5Er3hc4WTAmdXk3cXjxDydY4eoq6STXDutDQ59tM59bMr9CogemLkb4tUXrrZYvPc4DkdzkXhqGZjnzLVRAYpjMHXUeVmmqr9Fk96GrERRgHqJTaNp7wfhyEnqvb1nHkSXRK27"
  },
  "tag": "responder_sign"
}
```

#### responder ---> (2018-10-24 13:00:57.889)
```javascript
{
  "action": "responder_sign",
  "payload": {
    "tx": "tx_4L9GSozvM4HkQ2gRSFXMjUjfQbzK8Tcy2pidunQ7bPuNmhYoEBZErfy6uUZiiJsYV4vswvAjvStERqa47EWnijGcn3r38d5bWXfxwVXqZy48ptUitGQXaV561tB1ETqKiJDNQjqxyLKwqCSNXou8XsJ9hubgeKenJypGPX99bpwr9ha9NdokPbp1Gi2u4VbUPRc4YHAhiqc6pZbEieYwtgDqUDXGDWRm8LTpsSXqGAuxTzwW7gyCbQg7nPqF8zdSmwx8y1kZvu5"
  }
}
```

#### initiator <--- (2018-10-24 13:00:57.890)
```javascript
{
  "action": "info",
  "payload": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-24 13:00:57.891)
```javascript
{
  "action": "on_chain_tx",
  "payload": {
    "tx": "tx_6jPYBUFTkcmNB3vvEH6uvYBvGCeYaobhvNp55H6wv4ALmAhVzvgRDvdqQARuFx79zrFqaF55RnxJhbiRSmYomkpRBikncNB9T3xCKveoxs9Eijz7brRHXxa561eVrxnn8uzcyYmyPgW2dNh8sHM42FVfKZqJuYcBdcyb9YT5aTAZvGBzEwKAU36FNNvfro8xQsTMz1LtySh9FZ12ShUwUx4oct3q7LjzDA9bRWZQPr9eHeWdCAiQRVj37ZQxtvwgHYBS3xWgNH7NDPLm8k4zHEhw6deVHHPYDYKsb9SDTEjLWoxtGBMfKYd38nFdWAS2JKYc2HQMgzRSpjnUPyRGskYnd4qySYuKkTMeA"
  }
}
```

#### initiator <--- (2018-10-24 13:00:57.892)
```javascript
{
  "action": "on_chain_tx",
  "payload": {
    "tx": "tx_6jPYBUFTkcmNB3vvEH6uvYBvGCeYaobhvNp55H6wv4ALmAhVzvgRDvdqQARuFx79zrFqaF55RnxJhbiRSmYomkpRBikncNB9T3xCKveoxs9Eijz7brRHXxa561eVrxnn8uzcyYmyPgW2dNh8sHM42FVfKZqJuYcBdcyb9YT5aTAZvGBzEwKAU36FNNvfro8xQsTMz1LtySh9FZ12ShUwUx4oct3q7LjzDA9bRWZQPr9eHeWdCAiQRVj37ZQxtvwgHYBS3xWgNH7NDPLm8k4zHEhw6deVHHPYDYKsb9SDTEjLWoxtGBMfKYd38nFdWAS2JKYc2HQMgzRSpjnUPyRGskYnd4qySYuKkTMeA"
  }
}
```

#### initiator ---> (2018-10-24 13:00:59.224)
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

#### initiator <--- (2018-10-24 13:00:59.230)
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

#### initiator <--- (2018-10-24 13:01:06.968)
```javascript
{
  "action": "info",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "event": "own_funding_locked"
  }
}
```

#### responder <--- (2018-10-24 13:01:06.972)
```javascript
{
  "action": "info",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "event": "own_funding_locked"
  }
}
```

#### initiator <--- (2018-10-24 13:01:06.973)
```javascript
{
  "action": "info",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "event": "funding_locked"
  }
}
```

#### responder <--- (2018-10-24 13:01:06.973)
```javascript
{
  "action": "info",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "event": "funding_locked"
  }
}
```

#### responder <--- (2018-10-24 13:01:06.976)
```javascript
{
  "action": "info",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "event": "open"
  }
}
```

#### responder <--- (2018-10-24 13:01:06.978)
```javascript
{
  "action": "update",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "state": "tx_6jPYBUFTkcmNB3vvEH6uvYBvGCeYaobhvNp55H6wv4ALmAhVzvgRDvdqQARuFx79zrFqaF55RnxJhbiRSmYomkpRBikncNB9T3xCKveoxs9Eijz7brRHXxa561eVrxnn8uzcyYmyPgW2dNh8sHM42FVfKZqJuYcBdcyb9YT5aTAZvGBzEwKAU36FNNvfro8xQsTMz1LtySh9FZ12ShUwUx4oct3q7LjzDA9bRWZQPr9eHeWdCAiQRVj37ZQxtvwgHYBS3xWgNH7NDPLm8k4zHEhw6deVHHPYDYKsb9SDTEjLWoxtGBMfKYd38nFdWAS2JKYc2HQMgzRSpjnUPyRGskYnd4qySYuKkTMeA"
  }
}
```

#### initiator <--- (2018-10-24 13:01:06.978)
```javascript
{
  "action": "info",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "event": "open"
  }
}
```

#### initiator <--- (2018-10-24 13:01:06.980)
```javascript
{
  "action": "update",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "state": "tx_6jPYBUFTkcmNB3vvEH6uvYBvGCeYaobhvNp55H6wv4ALmAhVzvgRDvdqQARuFx79zrFqaF55RnxJhbiRSmYomkpRBikncNB9T3xCKveoxs9Eijz7brRHXxa561eVrxnn8uzcyYmyPgW2dNh8sHM42FVfKZqJuYcBdcyb9YT5aTAZvGBzEwKAU36FNNvfro8xQsTMz1LtySh9FZ12ShUwUx4oct3q7LjzDA9bRWZQPr9eHeWdCAiQRVj37ZQxtvwgHYBS3xWgNH7NDPLm8k4zHEhw6deVHHPYDYKsb9SDTEjLWoxtGBMfKYd38nFdWAS2JKYc2HQMgzRSpjnUPyRGskYnd4qySYuKkTMeA"
  }
}
```

#### initiator: (2018-10-24 13:01:08.370)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-24 13:01:08.370)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-24 13:01:08.370)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-24 13:01:08.370)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-24 13:01:08.370)
> Channel is `open` and ready to use

#### responder: (2018-10-24 13:01:08.370)
> Channel is `open` and ready to use

#### initiator ---> (2018-10-24 13:01:08.413)
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

#### initiator <--- (2018-10-24 13:01:08.416)
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

#### initiator ---> (2018-10-24 13:01:08.417)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 1,
    "from": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
    "to": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt"
  },
  "tag": "new"
}
```

#### initiator <--- (2018-10-24 13:01:08.428)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQMbHPb4aEKzhq4eHPNn8UykZs6cqYYgm7pTrBWnqcBPCEUuEQNcTau8UFf9xpX5siPNRzQdzmNZHP4Fx5fYrgKUz4uoH5Bq8oJbDksSNoi58bDAR6SLG37a42Ls5Yd17kjwjQM8UGemic4NZyGJqdUyREd3ruBaToVKKxUr5Bo7eTxsARhBi252rSphF1YaHVdtNAKePXqMJV"
  },
  "tag": "update"
}
```

#### initiator ---> (2018-10-24 13:01:08.431)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4o5kTjo1cJbunAatVD8XJQ2TJAHRY6EGq7bY7M5Go33MFuNewVEGJJLNU2xCwm5X8AXxX8zBnVb4D2jU5J7v561LtXwXAMH2YTb5GZEgf8ayspEfC9dDyNBCbYptyDNugTnmn1iR1rouXbBczbA6PManAUijqfxVGF37U1brkUB6UTBiefSdE74frdocchsDcyJKbXM6t1MTE3vWArhThCcfnyejRWysgtCC5c3SCxk9un8oUd5AQSJsVUZHf1Q2CdphSAUi2pbGQ3rScoTPYs5SRRcttxDfVHUhyk23b5PJ8Ts"
  }
}
```

#### responder <--- (2018-10-24 13:01:08.443)
```javascript
{
  "action": "info",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "event": "update"
  }
}
```

#### responder <--- (2018-10-24 13:01:08.445)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQMbHPb4aEKzhq4eHPNn8UykZs6cqYYgm7pTrBWnqcBPCEUuEQNcTau8UFf9xpX5siPNRzQdzmNZHP4Fx5fYrgKUz4uoH5Bq8oJbDksSNoi58bDAR6SLG37a42Ls5Yd17kjwjQM8UGemic4NZyGJqdUyREd3ruBaToVKKxUr5Bo7eTxsARhBi252rSphF1YaHVdtNAKePXqMJV"
  },
  "tag": "update_ack"
}
```

#### responder ---> (2018-10-24 13:01:08.447)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak4y6C8dEdwoG1Joo6nDWg3b7GaRuiCK4RGcZYhxVCcbs228Pmf9TEVfseX79xcAUQb6tGzGMFWDLUdYNR1xAwo1PBBawtWrboLdMc5vKJyS1ZxsziKV9H6PAqn2ea7ySHYiF1xdx8zdQsEiPKLGcJkNHbjpVygQHFpaKXFfq3NgMixZngoSPSanJXzposVDHhKH1oVHhUDHE82A8CeusMNCj1Yh1S4GgMHmM3nzLz2XCyg3FTHNZS5hwEFavdzsgZU7hTGhr4BNeB8vDxJZBRTYPVJmqtE4VjH7pMm5pZhbooMTc"
  }
}
```

#### responder <--- (2018-10-24 13:01:08.456)
```javascript
{
  "action": "update",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkPnYJouEuJjACJDX6ppcqkv5cLH9XQEbBL6aQSbmBye6PR7NYrr1AuYZAu3jE72ZdBi2vT7QTRReF4wuPA73QaVJXCEWmKvA8DN9D7b99FkGQZbQQZjZiZHLAwapmwyJJui2JLXMZw5smMZWhkyotwVJf9KvXDUg3PTPJpUVdV5SKbS8887su5fRhPZMhJJFBksAKbQWEWBVa77jqeLu2NYouYtBabSGqgNL5TPcF3etxNY3KzDoj6cNusWVWvmyXYvXX7ecdyK7EgjaasrqxVUkpZzz4YDFqrq22rd7QvMyFubRqEK6nRtso8A7LqmgcDqBHbTf3uBE8EuBLjnKhCjsWErma5ijSZv2Uj6DQz5j8kCJFhbHJiFehpbxbK9GK9FrifQWb"
  }
}
```

#### initiator <--- (2018-10-24 13:01:08.457)
```javascript
{
  "action": "update",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkPnYJouEuJjACJDX6ppcqkv5cLH9XQEbBL6aQSbmBye6PR7NYrr1AuYZAu3jE72ZdBi2vT7QTRReF4wuPA73QaVJXCEWmKvA8DN9D7b99FkGQZbQQZjZiZHLAwapmwyJJui2JLXMZw5smMZWhkyotwVJf9KvXDUg3PTPJpUVdV5SKbS8887su5fRhPZMhJJFBksAKbQWEWBVa77jqeLu2NYouYtBabSGqgNL5TPcF3etxNY3KzDoj6cNusWVWvmyXYvXX7ecdyK7EgjaasrqxVUkpZzz4YDFqrq22rd7QvMyFubRqEK6nRtso8A7LqmgcDqBHbTf3uBE8EuBLjnKhCjsWErma5ijSZv2Uj6DQz5j8kCJFhbHJiFehpbxbK9GK9FrifQWb"
  }
}
```

#### initiator ---> (2018-10-24 13:01:08.461)
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

#### initiator <--- (2018-10-24 13:01:08.463)
```javascript
{
  "action": "get",
  "payload": [
    {
      "account": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
      "balance": 698
    },
    {
      "account": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "balance": 402
    }
  ],
  "tag": "balances"
}
```

#### initiator ---> (2018-10-24 13:01:08.463)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- (2018-10-24 13:01:08.465)
```javascript
{
  "action": "get",
  "payload": [
    {
      "account": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "balance": 402
    },
    {
      "account": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
      "balance": 698
    }
  ],
  "tag": "balances"
}
```

#### responder ---> (2018-10-24 13:01:08.465)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 1,
    "from": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
    "to": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
  },
  "tag": "new"
}
```

#### responder <--- (2018-10-24 13:01:08.469)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQMbHPb4aEKzhq4eHPNn8UykZs6cqYYgm7pTrBWnqcBPCEUzevEA146UCBR9VwRCxCRjay75Y8Zvoj4bPkCMFvNaqUKb6MQzsgveSzpHqHHjCrBBiGKiFmN4gnT4DbfmYMwW6FGApJtVLJPmtWMmwoHn41LKSxZwfjDUydg4sDDzinzJj54LWGbfJyBLfWy1HyxV5YRiSZ3UNZ"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 13:01:08.470)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4ka7ZRsBDo4kwyfmtZZrLN1tkeFrpfRz5XfrmUk3G2MwEDZx4Y2w9aj1K8ev9wvh2x2hHjpFjAHVvkacXodP8rvwsVqGtMGhotM6BDLXRcQXPS61dJ6mRpqwJcjmXBYChFw27Th2RdryrbMFnJsH6CdmC3FHf2VwsVu9kfUKnnikfLePj8FnackKqqBuLDUr1Ku12N1wdYYK1oVsAAsWzvJfficXoKqLE6UQvauequhv3dSwNFxKsG3wxYiZh66TbffR7zkk1Wkt8s8LpjB7DujVtyhWCbbNXXamAouMeipxbys"
  }
}
```

#### initiator <--- (2018-10-24 13:01:08.474)
```javascript
{
  "action": "info",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 13:01:08.474)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQMbHPb4aEKzhq4eHPNn8UykZs6cqYYgm7pTrBWnqcBPCEUzevEA146UCBR9VwRCxCRjay75Y8Zvoj4bPkCMFvNaqUKb6MQzsgveSzpHqHHjCrBBiGKiFmN4gnT4DbfmYMwW6FGApJtVLJPmtWMmwoHn41LKSxZwfjDUydg4sDDzinzJj54LWGbfJyBLfWy1HyxV5YRiSZ3UNZ"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 13:01:08.475)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak4pYcvrQ3YwQszGmNM23am7EPXDjBcVq2C5vyPW67aVLeuepsdRTSe5EVgw9xjaFDATCWxXE1MhHNr7MyMxLrLk8GYdt1VaqxH9VGg8jWyFFinbUt2oS3nDyvjTHJvKZ7Pg92ZVMckMyKiCGdXjZXAfyKZsKJDzE2HeDv1Vs755ELD1sY55UqxooHrSzBnjdnXr7664Nnygt9yEm4fLauLmzzQnef4HnL4ZjTBCCftGWXEiD3xKsJ2qU3izeY4gWitBNdfj2ptQvsv986PNmg3TUjHXcC9qRUGHHsZpSHb66PFVr"
  }
}
```

#### initiator <--- (2018-10-24 13:01:08.478)
```javascript
{
  "action": "update",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkKUAfYhiEL12XS3QxskexNB9gVjSZ5SuL73GNqDT9D9G63UNVqhDmoYWbb1S2VgAg35B17twgLxVcuPnquWWVAyopPv7nCZAUoCTgbCkyD2GJbQKUfjafD6MvbUas85gBz46naHQSiVqYQsX3c6YVqnq31fT6PAfkPtbTbWr5wgN7PMg3zsphCPKLAidKiD8xzP2e5kSXCYu4PGpRz8RjLACzFc1KmnRP6F52ybEamMyX34oqBt9qKgH5JLhPiRkGkHRhbVjWa16sYJ2hw4euDfeQrMkvTFfJHAhkvMzfvEpJfHm6hPEpZiiQh9vryKQiet1wMpLpaxSiwLBcZc3JgMRLVvAqjNXD2vgzaxxccX3gnM6RNVzZLJPCyBjqVpmg6WXmGYMx"
  }
}
```

#### responder <--- (2018-10-24 13:01:08.479)
```javascript
{
  "action": "update",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkKUAfYhiEL12XS3QxskexNB9gVjSZ5SuL73GNqDT9D9G63UNVqhDmoYWbb1S2VgAg35B17twgLxVcuPnquWWVAyopPv7nCZAUoCTgbCkyD2GJbQKUfjafD6MvbUas85gBz46naHQSiVqYQsX3c6YVqnq31fT6PAfkPtbTbWr5wgN7PMg3zsphCPKLAidKiD8xzP2e5kSXCYu4PGpRz8RjLACzFc1KmnRP6F52ybEamMyX34oqBt9qKgH5JLhPiRkGkHRhbVjWa16sYJ2hw4euDfeQrMkvTFfJHAhkvMzfvEpJfHm6hPEpZiiQh9vryKQiet1wMpLpaxSiwLBcZc3JgMRLVvAqjNXD2vgzaxxccX3gnM6RNVzZLJPCyBjqVpmg6WXmGYMx"
  }
}
```

#### initiator ---> (2018-10-24 13:01:08.482)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- (2018-10-24 13:01:08.483)
```javascript
{
  "action": "get",
  "payload": [
    {
      "account": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "balance": 401
    },
    {
      "account": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
      "balance": 699
    }
  ],
  "tag": "balances"
}
```

#### initiator ---> (2018-10-24 13:01:08.483)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- (2018-10-24 13:01:08.484)
```javascript
{
  "action": "get",
  "payload": [
    {
      "account": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "balance": 401
    },
    {
      "account": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
      "balance": 699
    }
  ],
  "tag": "balances"
}
```

#### responder ---> (2018-10-24 13:01:08.484)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 1,
    "from": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
    "to": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
  },
  "tag": "new"
}
```

#### responder <--- (2018-10-24 13:01:08.487)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQMbHPb4aEKzhq4eHPNn8UykZs6cqYYgm7pTrBWnqcBPCEV65S5hYXHov7B934KKoCD37hfX7CYchrUeHN7q1c7LSVorWU5rEwabC9ujY52WHwrpftpmaCFKJijUoJP2R1sWDZV7gEU43i59Nkk8uDnNKFdz132Xk8fCcgSHxLWmHNSLrNfm8r7gk2xcugxj53tSbL4YGWMm6e"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 13:01:08.487)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4rojovZ6ZKpTahrCPmV9DyQ5PmEGLXy6RJxLUVfZ4RWG61LXnVKWRF7DNQap86ap3vzAxWmaArwrTSx29TBikTs81eRRToqagwTCqfF9939f36eEMxAzJUwhS8JZ5t7G8CAcMyJBs7Hxjmj1ad8D1c2h6RYdJEZWb3k38QaBe6hLvAdY1Fh7hWrbKxw71htQFELgA2qrRavvmB7xW6EWfbz6yZPEZTBWjLCr3CRSH8dZyuBM5dwYiie4yN7whocqx2spbdBBhfABQ8osFG3zXYF6t2Divo8tQoox8WTPdNBSanC"
  }
}
```

#### initiator <--- (2018-10-24 13:01:08.490)
```javascript
{
  "action": "info",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 13:01:08.491)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQMbHPb4aEKzhq4eHPNn8UykZs6cqYYgm7pTrBWnqcBPCEV65S5hYXHov7B934KKoCD37hfX7CYchrUeHN7q1c7LSVorWU5rEwabC9ujY52WHwrpftpmaCFKJijUoJP2R1sWDZV7gEU43i59Nkk8uDnNKFdz132Xk8fCcgSHxLWmHNSLrNfm8r7gk2xcugxj53tSbL4YGWMm6e"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 13:01:08.492)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak4wq3ChoVGnNMtCm1aRd6CqyQx9VeKc3yGVtVDUyATES6GBphjNU3b4Q2fgHZFMsKm71BvGbauuxvGGGn1EbCk2uFM1aKBN77rJKvTuv7xa32KGrTuyUoo7hzmzBbfkTKfTv4zjuB7Edsv2cRh2TLAgZdQXiVea5Vdt9TQs7nP86x8VzZnMfxFAQJit7uz9juDswBE8AV72Npksrw5dQ7kSLPWAL3BE9NpKjWbJy7uo481KojvfsaSEYtNuKJ4Rsw8SF2RgPWmKMd8aqFMnetVvAg3hbhHFNjwsXTSi8sJWDxKmD"
  }
}
```

#### initiator <--- (2018-10-24 13:01:08.495)
```javascript
{
  "action": "update",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkWBrvSpGzQkQghYkw22nz3qkNYY8vyWmZ3Cyf2oYK7U8HS2oXjkSmXzBrbn3f7iTTkCrZj4Lxkt5DyRYM9oJg1KbunUrYdL9zuBpL6rwS84fwgM9oKUJdzX4HRFgK5J1MPGderqNQna6qJrx273Pdzw92bbWzoydfca7hQbSqo1a4SoUkRAkyGbHpuDREytP2ViC5Fo8iE4cbZ5wX2Vgz1Uqg1viakXSppFBiSn3syEAk5f6L3Cu2rLDLgYpmkZz1bGgNe4Hr6zTrdDdyJYTJF9tbjhHjsPatJtC9SnM7gL7qt9vsQWf6caBST3qiZbZxgXNGd7FVdEGNPM2MYSrwVdydTB4yriwNXFV1gnb7ot65sKBsgAc6GU2bK3UsvRRAhXbJWAwW"
  }
}
```

#### responder <--- (2018-10-24 13:01:08.497)
```javascript
{
  "action": "update",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkWBrvSpGzQkQghYkw22nz3qkNYY8vyWmZ3Cyf2oYK7U8HS2oXjkSmXzBrbn3f7iTTkCrZj4Lxkt5DyRYM9oJg1KbunUrYdL9zuBpL6rwS84fwgM9oKUJdzX4HRFgK5J1MPGderqNQna6qJrx273Pdzw92bbWzoydfca7hQbSqo1a4SoUkRAkyGbHpuDREytP2ViC5Fo8iE4cbZ5wX2Vgz1Uqg1viakXSppFBiSn3syEAk5f6L3Cu2rLDLgYpmkZz1bGgNe4Hr6zTrdDdyJYTJF9tbjhHjsPatJtC9SnM7gL7qt9vsQWf6caBST3qiZbZxgXNGd7FVdEGNPM2MYSrwVdydTB4yriwNXFV1gnb7ot65sKBsgAc6GU2bK3UsvRRAhXbJWAwW"
  }
}
```

#### initiator ---> (2018-10-24 13:01:08.499)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- (2018-10-24 13:01:08.500)
```javascript
{
  "action": "get",
  "payload": [
    {
      "account": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "balance": 400
    },
    {
      "account": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
      "balance": 700
    }
  ],
  "tag": "balances"
}
```

#### initiator ---> (2018-10-24 13:01:08.500)
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

#### initiator <--- (2018-10-24 13:01:08.501)
```javascript
{
  "action": "get",
  "payload": [
    {
      "account": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
      "balance": 700
    },
    {
      "account": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "balance": 400
    }
  ],
  "tag": "balances"
}
```

#### initiator ---> (2018-10-24 13:01:08.501)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 1,
    "from": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
    "to": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt"
  },
  "tag": "new"
}
```

#### initiator <--- (2018-10-24 13:01:08.504)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQMbHPb4aEKzhq4eHPNn8UykZs6cqYYgm7pTrBWnqcBPCEVBVwwF5zV9e2w8aBDSQhjH2C5xhyJcymJQcwRz7jXjo9NbXRCPEZGRTE9mVAvQPtG5HywWDKmKuqC8pekmjiXx7M1y43PTrq6V2iRPhtxkCyY3UAGfrCuBhkg5pUBZZzHsswq1vA4wNG1eNndvANwzXTxkJ8AfJH"
  },
  "tag": "update"
}
```

#### initiator ---> (2018-10-24 13:01:08.505)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4ttQAycsLoof9uy9b6VVQ8yWMAN5M2tvhdtAPR3v3Zc32Nfr5gpsZutkt3oAJr3PyYB4XToJKSAPv2j2txfTt9WkA4kRZ4r8GBYdRwVr6D2nXqsGz13xUCUqAeoQM6y1FPE8nvRq2xi2cn6W6PkB8LAtpTy8YhRbc1PPhzuXc8AHXsX14UM999kLyTYnk1yy8wMAi1jZw1UJ75Mt1oSQECXNxQKmMSrEL6rw2Ld5LKgYzwzUZvcJkJzkXQXVUdPJNrEp8kru5rZRiW7wCR2LsbZpuCVugv81Wkg7KXwonqbVgfy"
  }
}
```

#### responder <--- (2018-10-24 13:01:08.547)
```javascript
{
  "action": "info",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "event": "update"
  }
}
```

#### responder <--- (2018-10-24 13:01:08.549)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQMbHPb4aEKzhq4eHPNn8UykZs6cqYYgm7pTrBWnqcBPCEVBVwwF5zV9e2w8aBDSQhjH2C5xhyJcymJQcwRz7jXjo9NbXRCPEZGRTE9mVAvQPtG5HywWDKmKuqC8pekmjiXx7M1y43PTrq6V2iRPhtxkCyY3UAGfrCuBhkg5pUBZZzHsswq1vA4wNG1eNndvANwzXTxkJ8AfJH"
  },
  "tag": "update_ack"
}
```

#### responder ---> (2018-10-24 13:01:08.552)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak4ynAKQvqGWbtww5zArLJtftBTj7bsEtXy18kbhuvFoQ9Dk9FKCZ8fiJWsHM9gzvrMVCBBMsX8BpPjwnBNy5nanvwVcwcmTxCihdqx5oFAYyq2sXYcATXhhYGofVaBoscTkNmwwL4dJsJKwmHuAGHxtPY3n2pTVnn6FrehrTRryAA7KxVTsysPBHPCydtGW7tU33DAJDGtXBLxLYXfia8BocPK8jqxVxYj7x3VLG1iT7Y3jCSnvFY8Xnn32r4tSanrD4F1hKGXnC4wZ7ALe3GEwrbMLVXjuAnWxKQsQmxNjemsEz"
  }
}
```

#### responder <--- (2018-10-24 13:01:08.562)
```javascript
{
  "action": "update",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkZmJHNr3nE2U4hgwMUwfH5b9C6aJhNmTfR8W2aAqdLs1KDQn7JhnScU92b9d8axKpz337szyDrCFwaRLoYSZ6YmrGsMMg598EvKZEC5MZH6oSSnhGjz1PEyswY8353A23jf4YXzJi7uFbVLmGiLBSProBxC7sr8jjrzXHPeARVfeK8ahDckkQD5XxDm7qZedAQtYAmkaczGFxmCzwa9qCu7QKS2X1XUemjWeGvYETgX2SMu589y9fxiaCfXn4KSmbN1RBhi83QAFG3j4NmbDcnzXVxdgfJQ1gzahtFLj3kkiLUK1ZeQ4ZokcTYzrmzBHvZJfpHVVw6UHikyEUucQsxzQ4oDJf56Pzm2a4tbMjUf1bWDrcvwAZHf2yX8sC1CDGxC6RDfPc"
  }
}
```

#### initiator <--- (2018-10-24 13:01:08.563)
```javascript
{
  "action": "update",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkZmJHNr3nE2U4hgwMUwfH5b9C6aJhNmTfR8W2aAqdLs1KDQn7JhnScU92b9d8axKpz337szyDrCFwaRLoYSZ6YmrGsMMg598EvKZEC5MZH6oSSnhGjz1PEyswY8353A23jf4YXzJi7uFbVLmGiLBSProBxC7sr8jjrzXHPeARVfeK8ahDckkQD5XxDm7qZedAQtYAmkaczGFxmCzwa9qCu7QKS2X1XUemjWeGvYETgX2SMu589y9fxiaCfXn4KSmbN1RBhi83QAFG3j4NmbDcnzXVxdgfJQ1gzahtFLj3kkiLUK1ZeQ4ZokcTYzrmzBHvZJfpHVVw6UHikyEUucQsxzQ4oDJf56Pzm2a4tbMjUf1bWDrcvwAZHf2yX8sC1CDGxC6RDfPc"
  }
}
```

#### initiator ---> (2018-10-24 13:01:08.566)
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

#### initiator <--- (2018-10-24 13:01:08.568)
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

#### initiator ---> (2018-10-24 13:01:08.568)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- (2018-10-24 13:01:08.569)
```javascript
{
  "action": "get",
  "payload": [
    {
      "account": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "balance": 401
    },
    {
      "account": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
      "balance": 699
    }
  ],
  "tag": "balances"
}
```

#### responder ---> (2018-10-24 13:01:08.569)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 1,
    "from": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
    "to": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
  },
  "tag": "new"
}
```

#### responder <--- (2018-10-24 13:01:08.573)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQMbHPb4aEKzhq4eHPNn8UykZs6cqYYgm7pTrBWnqcBPCEVGvTnndTgVMxh87J7ZVBmeBAnQFLVzW7Jk4bxnWyaqeYnPLhRYyStUgU6cweW4U9E6b9ptD41pYbJKxhoYAKjWUBw1Q5dBUXRtMFWrp4mYqkFK5FgxVtxGiqmksMdUo7GfAtKDZNxZBSm2qfu9jdhVbGSDAwRGb3"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 13:01:08.574)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak59nCkf4bAyhmQnknNNBGKAu5ABVM6QdhoAhTq4U8AfL1zxH2Gc4h2nqUxq7fFefRvRCcGvyyNmK9cpmm2W1XVCcVMQjai7Sqhsqvbhv6oQqzoJBqsQs1XK2ucVoHj9K58Hpq8U87ph8H4wEn1nxGq9No2R7r2aDVas2Hc2TxbjqMQ6kDg8YAqWXFeTuWdZDA3VEeWTZxoqM9kq9dCqjocgb95gNvtiLvrPWP34MYmTCT6HbbpgFPCCooiNABnRavbixZuVr7HujJE5UTbUo5fka3tekaPJh5XpXvEK1vVAtgjYG"
  }
}
```

#### initiator <--- (2018-10-24 13:01:08.602)
```javascript
{
  "action": "info",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 13:01:08.603)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQMbHPb4aEKzhq4eHPNn8UykZs6cqYYgm7pTrBWnqcBPCEVGvTnndTgVMxh87J7ZVBmeBAnQFLVzW7Jk4bxnWyaqeYnPLhRYyStUgU6cweW4U9E6b9ptD41pYbJKxhoYAKjWUBw1Q5dBUXRtMFWrp4mYqkFK5FgxVtxGiqmksMdUo7GfAtKDZNxZBSm2qfu9jdhVbGSDAwRGb3"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 13:01:08.605)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak58T4caurmrtZr7yxidGtK1dsyqFh1jckZuAeQj4Lp24cijrh6VZRo3iJHvGD9zd6MdAwXgvhuJh5KMjXW5axiMcZ48JLqcQbgYwghPW3JAKHTq6xUU2q8Uv8jsc75P9Y7XrF7qCDAxPK6aWTpoUuCNLvZNr7XMZvTg4pomV6GCnppyHeruBXuNbikszWfZL1ZEtngFsaLYUYQcFN8ymtKDTcif6fmg3rgAnYhHSoWMmBPN123ZSRgjyWEGsX3pAsBUYveDkXh4A65FGmtmW6q7WtwG8C3HeeZohXqbBoKxjvT3H"
  }
}
```

#### initiator <--- (2018-10-24 13:01:08.617)
```javascript
{
  "action": "update",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "state": "tx_3XPhV5wAjiGDky5ho8duMQ616ui6o5QLPzLuB6RWuG9hpwWiB83voSMQipjoU7eqByJywv5mvwioud1EaaoABmSDh6NsmsjC5DNhUwiVT8i51eomWRVHJvTkUgaFk1EYXbDozvmT4P5MLgJC7YUZ6CCgDmYkt11WJPXmsH5KiHYTjsp9vibm94kmUGXdtzTshC2zxY2T4GfbyvSDw46zGms53hGnme7KsYHt5XYmeCi4jpTm6DRH5wZM64Zip4m6431gbonvP6c6SbyLwcDtxRgSW2ETZRQZ9C1AsxTfWSnph9tBSeduBukkc3jbwVniyQPRdzrXeqEh2rZVYeoaoqQgadqwsnwHuxv2o6r3vQHvpJ7bzSrhCrMAmRorAcBBYDjgoaD39mKy8bP6BrNh7"
  }
}
```

#### responder <--- (2018-10-24 13:01:08.617)
```javascript
{
  "action": "update",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "state": "tx_3XPhV5wAjiGDky5ho8duMQ616ui6o5QLPzLuB6RWuG9hpwWiB83voSMQipjoU7eqByJywv5mvwioud1EaaoABmSDh6NsmsjC5DNhUwiVT8i51eomWRVHJvTkUgaFk1EYXbDozvmT4P5MLgJC7YUZ6CCgDmYkt11WJPXmsH5KiHYTjsp9vibm94kmUGXdtzTshC2zxY2T4GfbyvSDw46zGms53hGnme7KsYHt5XYmeCi4jpTm6DRH5wZM64Zip4m6431gbonvP6c6SbyLwcDtxRgSW2ETZRQZ9C1AsxTfWSnph9tBSeduBukkc3jbwVniyQPRdzrXeqEh2rZVYeoaoqQgadqwsnwHuxv2o6r3vQHvpJ7bzSrhCrMAmRorAcBBYDjgoaD39mKy8bP6BrNh7"
  }
}
```

#### initiator ---> (2018-10-24 13:01:08.621)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- (2018-10-24 13:01:08.622)
```javascript
{
  "action": "get",
  "payload": [
    {
      "account": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "balance": 400
    },
    {
      "account": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
      "balance": 700
    }
  ],
  "tag": "balances"
}
```

#### initiator ---> (2018-10-24 13:01:08.675)
```javascript
{
  "action": "withdraw",
  "payload": {
    "amount": 2
  }
}
```

#### initiator <--- (2018-10-24 13:01:08.681)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_2C9estKT2SHZ8tyKtG9kZncuB5LnPSiD1PzRuvfzfv8wSSiiUYf5HFjdE8osqHdLjyMpA2mxP59a9ZHLqZpRrFsGdLfE92jiEZL48d1kiJwv7XQqjoZ2jbkjUZWygzHFcfDPCcxC5WL5Z1E7HEfKhHVeepbGNt"
  },
  "tag": "withdraw_tx"
}
```

#### initiator ---> (2018-10-24 13:01:08.684)
```javascript
{
  "action": "withdraw_tx",
  "payload": {
    "tx": "tx_2WsEQsiC5XsneNEVxd7Ax7RPrV6sikqN7Hh9ABvfTiMK5g667tWeJGpDFGS8ayx9Ccv827XcABR9nmQPAA9HovZd9hLg2ZECvLtUH1JcfhgxfaqTFpgJbGadHydVzw5H9crsB7SUJX6hUfGgZT5vrw3vskEn4xFCoMedBpmhLuxW8Jg2jAWaiuPcpJoan2yM3J6kDRJX51xbuRnD9zRqEPqGv7zDLwWRGorKkMKQpRKYoMDDLCVTtW7H6SMyVJ2Uz7N"
  }
}
```

#### responder <--- (2018-10-24 13:01:08.685)
```javascript
{
  "action": "info",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "event": "withdraw_created"
  }
}
```

#### responder <--- (2018-10-24 13:01:08.685)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_2C9estKT2SHZ8tyKtG9kZncuB5LnPSiD1PzRuvfzfv8wSSiiUYf5HFjdE8osqHdLjyMpA2mxP59a9ZHLqZpRrFsGdLfE92jiEZL48d1kiJwv7XQqjoZ2jbkjUZWygzHFcfDPCcxC5WL5Z1E7HEfKhHVeepbGNt"
  },
  "tag": "withdraw_ack"
}
```

#### responder ---> (2018-10-24 13:01:08.686)
```javascript
{
  "action": "withdraw_ack",
  "payload": {
    "tx": "tx_2WsEQsiC5XsneDD5QbsTt9L9EVaqVrFvzWgh9T9SgjnEe3MdsfRU6iYXESQqiZtDY8rzZjFT8YcFhLrrKz263oRaUZCA57fPL3mgEwPbRDy5nWpU212zs9jvkjNMBNJJJjvkk12LJdpEP5m5quQDnuumAuXYDj7f6x6Wnq2jfcnM6JuCFczoCAxdSXjFZxvQ3DDrJi7to6vA5L3T1YJgDAQvceaPz1taPpijymGF1Dty4MbCj11eE2WbWw54mokuMcL"
  }
}
```

#### responder <--- (2018-10-24 13:01:08.688)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "tx": "tx_3cDMp6242sBzqZ34oA34QiGsjKPTS6uDgz7fR49xhXnFAkcCKS2a2ydSdi2TEsbCerAmKTQCDXHLKipJGVnvgxmLA3eyg9RGwuTyQe4PrVSEMFLgh9MjJAiSZwzKvdLwe9QVTz4x1k2yihebVCanm7DH4ZdW1aycrf5CtksbvFimG9PonBfJiYRaVzEnYt15ope6FHtnRapR9uGrj1YvmDwBYJUENnLDcJQ14C4K1kVj182RYVKjP85bA7DqvyPG69kttdkta992TENgBioRC8uM9hQBsBn2jbvx2qvATCTeWnq3WjCEP4x9ZLeJxLPKKTmqsWAXw3fsUq4y6LM254EyUr6fq"
  }
}
```

#### initiator <--- (2018-10-24 13:01:08.688)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "tx": "tx_3cDMp6242sBzqZ34oA34QiGsjKPTS6uDgz7fR49xhXnFAkcCKS2a2ydSdi2TEsbCerAmKTQCDXHLKipJGVnvgxmLA3eyg9RGwuTyQe4PrVSEMFLgh9MjJAiSZwzKvdLwe9QVTz4x1k2yihebVCanm7DH4ZdW1aycrf5CtksbvFimG9PonBfJiYRaVzEnYt15ope6FHtnRapR9uGrj1YvmDwBYJUENnLDcJQ14C4K1kVj182RYVKjP85bA7DqvyPG69kttdkta992TENgBioRC8uM9hQBsBn2jbvx2qvATCTeWnq3WjCEP4x9ZLeJxLPKKTmqsWAXw3fsUq4y6LM254EyUr6fq"
  }
}
```

#### responder <--- (2018-10-24 13:01:14.160)
```javascript
{
  "action": "info",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "event": "own_withdraw_locked"
  }
}
```

#### initiator <--- (2018-10-24 13:01:14.160)
```javascript
{
  "action": "info",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "event": "own_withdraw_locked"
  }
}
```

#### initiator <--- (2018-10-24 13:01:14.161)
```javascript
{
  "action": "info",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "event": "withdraw_locked"
  }
}
```

#### responder <--- (2018-10-24 13:01:14.161)
```javascript
{
  "action": "info",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "event": "withdraw_locked"
  }
}
```

#### responder <--- (2018-10-24 13:01:14.163)
```javascript
{
  "action": "update",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "state": "tx_3cDMp6242sBzqZ34oA34QiGsjKPTS6uDgz7fR49xhXnFAkcCKS2a2ydSdi2TEsbCerAmKTQCDXHLKipJGVnvgxmLA3eyg9RGwuTyQe4PrVSEMFLgh9MjJAiSZwzKvdLwe9QVTz4x1k2yihebVCanm7DH4ZdW1aycrf5CtksbvFimG9PonBfJiYRaVzEnYt15ope6FHtnRapR9uGrj1YvmDwBYJUENnLDcJQ14C4K1kVj182RYVKjP85bA7DqvyPG69kttdkta992TENgBioRC8uM9hQBsBn2jbvx2qvATCTeWnq3WjCEP4x9ZLeJxLPKKTmqsWAXw3fsUq4y6LM254EyUr6fq"
  }
}
```

#### initiator <--- (2018-10-24 13:01:14.164)
```javascript
{
  "action": "update",
  "channel_id": "ch_6XdmZgtrmJN182QhQ2XW7UAkeXdfv6vi75MchcEC8Datid7uR",
  "payload": {
    "state": "tx_3cDMp6242sBzqZ34oA34QiGsjKPTS6uDgz7fR49xhXnFAkcCKS2a2ydSdi2TEsbCerAmKTQCDXHLKipJGVnvgxmLA3eyg9RGwuTyQe4PrVSEMFLgh9MjJAiSZwzKvdLwe9QVTz4x1k2yihebVCanm7DH4ZdW1aycrf5CtksbvFimG9PonBfJiYRaVzEnYt15ope6FHtnRapR9uGrj1YvmDwBYJUENnLDcJQ14C4K1kVj182RYVKjP85bA7DqvyPG69kttdkta992TENgBioRC8uM9hQBsBn2jbvx2qvATCTeWnq3WjCEP4x9ZLeJxLPKKTmqsWAXw3fsUq4y6LM254EyUr6fq"
  }
}
```
