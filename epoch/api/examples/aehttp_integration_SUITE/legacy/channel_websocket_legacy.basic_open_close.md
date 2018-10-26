
#### initiator init (2018-10-24 12:59:14.623)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=8&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=4&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=initiator&timeout_accept=100
```

#### initiator <--- (2018-10-24 12:59:14.723)
```javascript
{
  "action": "info",
  "payload": {
    "event": "died"
  }
}
```

#### initiator init (2018-10-24 12:59:14.827)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=initiator
```

#### responder init (2018-10-24 12:59:14.831)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=responder
```

#### responder <--- (2018-10-24 12:59:15.871)
```javascript
{
  "action": "info",
  "payload": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-24 12:59:15.872)
```javascript
{
  "action": "info",
  "payload": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-24 12:59:15.882)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_3d11KjpALm3t32sAMLL9Y5p9SUg9j82o5Er3hc4WTAmdXk3cXjxDydY4eoq6STXDutDQ59tM59bMr9CogemLkb4tUXrrZYvPc4DkdzkXhqGZjnzLVRAYpjMHXUeVmmqr9Fk96GrERRgHqJTaNp7wfhyEnqvb1nHj6UGduM"
  },
  "tag": "initiator_sign"
}
```

#### initiator ---> (2018-10-24 12:59:15.893)
```javascript
{
  "action": "initiator_sign",
  "payload": {
    "tx": "tx_4L9GSozvM4HoaHcduwzF5eBrA7F7iHRTvVtvYfqtf5B8fosNNPMe7aZmEXRLrT3aA1BgYS3stXFWZuqmVpsARhNFTEDMWPjCYSw4AdwUA6LUF9ciwkAadV4SCLDaaNSYgpvJ9iBpNKqnb3V7ZfuTXmJbDCFCvtpaKvFaZUMPaXYtjjcszaPw7d9KE6gMyYHAhB7SyZKuso6pGFKR2Qk1FKpa1oC9S1kpLUrjVJyqadxJ9yjWykn2fF2zgKA1hrMbGurPpYKdnsP"
  }
}
```

#### responder <--- (2018-10-24 12:59:15.894)
```javascript
{
  "action": "info",
  "payload": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-24 12:59:15.894)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_3d11KjpALm3t32sAMLL9Y5p9SUg9j82o5Er3hc4WTAmdXk3cXjxDydY4eoq6STXDutDQ59tM59bMr9CogemLkb4tUXrrZYvPc4DkdzkXhqGZjnzLVRAYpjMHXUeVmmqr9Fk96GrERRgHqJTaNp7wfhyEnqvb1nHj6UGduM"
  },
  "tag": "responder_sign"
}
```

#### responder ---> (2018-10-24 12:59:15.895)
```javascript
{
  "action": "responder_sign",
  "payload": {
    "tx": "tx_4L9GSozvM4Hoq5GShFU5Em5AGGkwPz8uNd9RyphTSHBWWXYPyameJXty3ovm8jb1GW9GvfPeFPHkYSWif5SUxDjqP8CtFiybJngSmBFMH6oKiymSXh88uwuhBds5X9Z7MUedj2BBTESV6sqb4xXAGV21b815CDrYu4HmxKgkvkHPeWfLjkW9JXHeKTBYd1gstLwyo421rhjkk3uLS8SVKidqErvQPB3RgEbUBvn6xHcGaeR1wUHZi4ZyMQFPnVM13wyXvgiNmB1"
  }
}
```

#### initiator <--- (2018-10-24 12:59:15.896)
```javascript
{
  "action": "info",
  "payload": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-24 12:59:15.897)
```javascript
{
  "action": "on_chain_tx",
  "payload": {
    "tx": "tx_6jPYBUFTkcmUMMpLCzyZa22jHGDkboUP4yFK91YvmLRa4vEjTxzFBRXo2RkrgZzf5g9r4DWkkg7jFgDjXynyjCqjYNJuNe8sHcwer7m5eXDdAgTXUnS9A9Qg4XN8MRKrUo9zMr7dUh3KxmHTk7MYyfo3Jy3stX3ekYLpa4D9hfkHm1DoLiCHLBzeQ74N7cGwX2adtiw1KV6Wi3zyxFPKZBPqVuqBXc1T2PQYP7qp45MP98fwdtGnxw5vDqkbTYN7a5c8PcHR1kr6mhHEEPPVNikMVTugcKfuYJYYb4p29YkUVVJcpBfouZ4F3YSJjekNEeWpPqNvk9MH8SnwdzjrBjznpbpygTU4fhttQ"
  }
}
```

#### initiator <--- (2018-10-24 12:59:15.897)
```javascript
{
  "action": "on_chain_tx",
  "payload": {
    "tx": "tx_6jPYBUFTkcmUMMpLCzyZa22jHGDkboUP4yFK91YvmLRa4vEjTxzFBRXo2RkrgZzf5g9r4DWkkg7jFgDjXynyjCqjYNJuNe8sHcwer7m5eXDdAgTXUnS9A9Qg4XN8MRKrUo9zMr7dUh3KxmHTk7MYyfo3Jy3stX3ekYLpa4D9hfkHm1DoLiCHLBzeQ74N7cGwX2adtiw1KV6Wi3zyxFPKZBPqVuqBXc1T2PQYP7qp45MP98fwdtGnxw5vDqkbTYN7a5c8PcHR1kr6mhHEEPPVNikMVTugcKfuYJYYb4p29YkUVVJcpBfouZ4F3YSJjekNEeWpPqNvk9MH8SnwdzjrBjznpbpygTU4fhttQ"
  }
}
```

#### initiator ---> (2018-10-24 12:59:18.374)
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

#### initiator <--- (2018-10-24 12:59:18.375)
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

#### responder <--- (2018-10-24 12:59:20.566)
```javascript
{
  "action": "info",
  "channel_id": "ch_n1U3NKFhr2bgukf9vQcgwt6CewrPNCtorogfg2ExPtnWZCtdf",
  "payload": {
    "event": "own_funding_locked"
  }
}
```

#### initiator <--- (2018-10-24 12:59:20.567)
```javascript
{
  "action": "info",
  "channel_id": "ch_n1U3NKFhr2bgukf9vQcgwt6CewrPNCtorogfg2ExPtnWZCtdf",
  "payload": {
    "event": "own_funding_locked"
  }
}
```

#### initiator <--- (2018-10-24 12:59:20.567)
```javascript
{
  "action": "info",
  "channel_id": "ch_n1U3NKFhr2bgukf9vQcgwt6CewrPNCtorogfg2ExPtnWZCtdf",
  "payload": {
    "event": "funding_locked"
  }
}
```

#### responder <--- (2018-10-24 12:59:20.568)
```javascript
{
  "action": "info",
  "channel_id": "ch_n1U3NKFhr2bgukf9vQcgwt6CewrPNCtorogfg2ExPtnWZCtdf",
  "payload": {
    "event": "funding_locked"
  }
}
```

#### initiator <--- (2018-10-24 12:59:20.570)
```javascript
{
  "action": "info",
  "channel_id": "ch_n1U3NKFhr2bgukf9vQcgwt6CewrPNCtorogfg2ExPtnWZCtdf",
  "payload": {
    "event": "open"
  }
}
```

#### responder <--- (2018-10-24 12:59:20.570)
```javascript
{
  "action": "info",
  "channel_id": "ch_n1U3NKFhr2bgukf9vQcgwt6CewrPNCtorogfg2ExPtnWZCtdf",
  "payload": {
    "event": "open"
  }
}
```

#### initiator <--- (2018-10-24 12:59:20.571)
```javascript
{
  "action": "update",
  "channel_id": "ch_n1U3NKFhr2bgukf9vQcgwt6CewrPNCtorogfg2ExPtnWZCtdf",
  "payload": {
    "state": "tx_6jPYBUFTkcmUMMpLCzyZa22jHGDkboUP4yFK91YvmLRa4vEjTxzFBRXo2RkrgZzf5g9r4DWkkg7jFgDjXynyjCqjYNJuNe8sHcwer7m5eXDdAgTXUnS9A9Qg4XN8MRKrUo9zMr7dUh3KxmHTk7MYyfo3Jy3stX3ekYLpa4D9hfkHm1DoLiCHLBzeQ74N7cGwX2adtiw1KV6Wi3zyxFPKZBPqVuqBXc1T2PQYP7qp45MP98fwdtGnxw5vDqkbTYN7a5c8PcHR1kr6mhHEEPPVNikMVTugcKfuYJYYb4p29YkUVVJcpBfouZ4F3YSJjekNEeWpPqNvk9MH8SnwdzjrBjznpbpygTU4fhttQ"
  }
}
```

#### responder <--- (2018-10-24 12:59:20.571)
```javascript
{
  "action": "update",
  "channel_id": "ch_n1U3NKFhr2bgukf9vQcgwt6CewrPNCtorogfg2ExPtnWZCtdf",
  "payload": {
    "state": "tx_6jPYBUFTkcmUMMpLCzyZa22jHGDkboUP4yFK91YvmLRa4vEjTxzFBRXo2RkrgZzf5g9r4DWkkg7jFgDjXynyjCqjYNJuNe8sHcwer7m5eXDdAgTXUnS9A9Qg4XN8MRKrUo9zMr7dUh3KxmHTk7MYyfo3Jy3stX3ekYLpa4D9hfkHm1DoLiCHLBzeQ74N7cGwX2adtiw1KV6Wi3zyxFPKZBPqVuqBXc1T2PQYP7qp45MP98fwdtGnxw5vDqkbTYN7a5c8PcHR1kr6mhHEEPPVNikMVTugcKfuYJYYb4p29YkUVVJcpBfouZ4F3YSJjekNEeWpPqNvk9MH8SnwdzjrBjznpbpygTU4fhttQ"
  }
}
```

#### initiator: (2018-10-24 12:59:22.326)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-24 12:59:22.326)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-24 12:59:22.327)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-24 12:59:22.327)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-24 12:59:22.327)
> Channel is `open` and ready to use

#### responder: (2018-10-24 12:59:22.327)
> Channel is `open` and ready to use

#### initiator ---> (2018-10-24 12:59:22.362)
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

#### initiator <--- (2018-10-24 12:59:22.365)
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

#### initiator ---> (2018-10-24 12:59:22.366)
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

#### initiator <--- (2018-10-24 12:59:22.390)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQQ5grMVKphCFm5B5QSSkrjwSgyJAa7Mn1E9H1hoR5GQ5iiooK6ScD45VPkU75VC9ph7HRhJ7oZZHdPcnT3RcafKzyUL6naHW7FTGSiNoPpJU8x8afcR6THD6nCgfFATcGdr5LMdPK4Wg5XGJpwGJKQ9wWorQ1GeaK6jM2wfc2iq8C9ikJJTdYLsyV3gdedUTBRaaApvxhqMcn"
  },
  "tag": "update"
}
```

#### initiator ---> (2018-10-24 12:59:22.399)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4nuxxviWF3vDnPc9Jsjh2kbmRw1NyjbZAU99BdwdAFHpTiEawYUP9hCSu151D29RXbKCym1zxYxTMNprWCNnR6kTctX2VHkJ9eDTpm4h2vtb6iT3anjAhqChJFDmcCdK6getjLgttPrpvHZ5TCZZtEMkoc2MHgPJL6ZPpvGHZixPz3xFc3f2BFmPqUux5nnPyrV4rSa8vc9JAvoybgWfoK93ejPHcyzfQUUMq9NZo3xSQSaFXYy7WKB2gs1gNcQJEUQAAA3smRuhq6eGa2nS42EoEW1WG6iYHJmcuVjKrDvkBaR"
  }
}
```

#### responder <--- (2018-10-24 12:59:22.404)
```javascript
{
  "action": "info",
  "channel_id": "ch_n1U3NKFhr2bgukf9vQcgwt6CewrPNCtorogfg2ExPtnWZCtdf",
  "payload": {
    "event": "update"
  }
}
```

#### responder <--- (2018-10-24 12:59:22.405)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQQ5grMVKphCFm5B5QSSkrjwSgyJAa7Mn1E9H1hoR5GQ5iiooK6ScD45VPkU75VC9ph7HRhJ7oZZHdPcnT3RcafKzyUL6naHW7FTGSiNoPpJU8x8afcR6THD6nCgfFATcGdr5LMdPK4Wg5XGJpwGJKQ9wWorQ1GeaK6jM2wfc2iq8C9ikJJTdYLsyV3gdedUTBRaaApvxhqMcn"
  },
  "tag": "update_ack"
}
```

#### responder ---> (2018-10-24 12:59:22.406)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak4zRAc1g39Dmn1vad6dcmj3goyeJWTi3NjAXjkJGeCkxqTa319SrAD7aAqE4iJCGKZqXj2uceoPsWJLXkAzbhQpDqht7G9TTnM9Pvb6S3VcLg7oty3EoJf2zD3FdLoQ8jVyMApEV8HraUhHChhyXqEPekRqZAiJBs5CwvMLG3sfXaVpyFPEtFeEihsDtervcxucUq5HxiNZGtb8mf4EkgSWEY9qwun2uYvHrCaYYLdvLVU6asYu9m4J26GdAz2FqXRgC9KeY7LN4DW5ehvLoeK7593yiXD8c67AdWEbV2bDHTw5n"
  }
}
```

#### responder <--- (2018-10-24 12:59:22.411)
```javascript
{
  "action": "update",
  "channel_id": "ch_n1U3NKFhr2bgukf9vQcgwt6CewrPNCtorogfg2ExPtnWZCtdf",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkPVigiqqp57b71rBm7t8sZVMX6FQ4837FT3k3oGqu9gdFdQi21uxgVEi2NLHM5xfQsijztw5gCRZSeyEDVoDLbHgUVPqfZACndYB2GH1jy3dsRoKNESHdkkuPwiRqcp266DwhUKesZThLgvLX4r7qH7ayPKP8G3YsQSZxBxmSB7RRBF29aJSeggPCZdJ3yHMWcQTZHKcQE34oB5EczHCctqc5wSsXyiUwumTa8nuoJy3qksM5hVAhMnivsmqEKXn2u79JNSwiEHa9cTomtvNohCBoxGfjvsEAUdDTa2Xp6bqRbKAHFFykghhyF9bWqXwMQeTdKDzfAjBpy7RvUBrcqpihEbCfgV6khK2xu754F7ynDMnSktEUisAriQffdGpEP7Kc1Yhx"
  }
}
```

#### initiator <--- (2018-10-24 12:59:22.412)
```javascript
{
  "action": "update",
  "channel_id": "ch_n1U3NKFhr2bgukf9vQcgwt6CewrPNCtorogfg2ExPtnWZCtdf",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkPVigiqqp57b71rBm7t8sZVMX6FQ4837FT3k3oGqu9gdFdQi21uxgVEi2NLHM5xfQsijztw5gCRZSeyEDVoDLbHgUVPqfZACndYB2GH1jy3dsRoKNESHdkkuPwiRqcp266DwhUKesZThLgvLX4r7qH7ayPKP8G3YsQSZxBxmSB7RRBF29aJSeggPCZdJ3yHMWcQTZHKcQE34oB5EczHCctqc5wSsXyiUwumTa8nuoJy3qksM5hVAhMnivsmqEKXn2u79JNSwiEHa9cTomtvNohCBoxGfjvsEAUdDTa2Xp6bqRbKAHFFykghhyF9bWqXwMQeTdKDzfAjBpy7RvUBrcqpihEbCfgV6khK2xu754F7ynDMnSktEUisAriQffdGpEP7Kc1Yhx"
  }
}
```

#### initiator ---> (2018-10-24 12:59:22.414)
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

#### initiator <--- (2018-10-24 12:59:22.415)
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

#### initiator ---> (2018-10-24 12:59:22.416)
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

#### initiator <--- (2018-10-24 12:59:22.417)
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

#### responder ---> (2018-10-24 12:59:22.417)
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

#### responder <--- (2018-10-24 12:59:22.420)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQQ5grMVKphCFm5B5QSSkrjwSgyJAa7Mn1E9H1hoR5GQ5iiuDpwz9gFRDKWTeCPKEJjUSQPjfAkvoyPxE7aE1piRrNt7v4oTEzsWVgfEFsPxYPv9sqVo6BXhjYJsoJDE2sqQSBGfjMJEHmrfdN2jQVCxaHX7z4f1nEptzi8tQ49iCXBAJwfcRnsWS1QL4A3uTfkBHYw11FB26E"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 12:59:22.421)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak5BkTyjCHZd7vWsgtbykqnNmWoxh24zYTuPS2eTzGafrEiZbQcFbR9FP6BDrGujN26zPbywexSH2Mc1RjMkFVNVtmTs7yNq1HmRGdiMvQ9XV5Bgrjiek3wMJHenzo5bbFDK78HGef7VefZouxctBX17PZHk1NRXz1yqxJBcdCocoDpbSWMti2STxUpVWcsicVtoADEw7jo4Xahf5zMVDH4WWPacheECArPX8ussaWMWw8JN9eaGYs1DWPQLC2KyYw2ZL8gjswhXrWkhHJChkkPRBjeesfjdYBikLuyKo3K8vLyZC"
  }
}
```

#### initiator <--- (2018-10-24 12:59:22.454)
```javascript
{
  "action": "info",
  "channel_id": "ch_n1U3NKFhr2bgukf9vQcgwt6CewrPNCtorogfg2ExPtnWZCtdf",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 12:59:22.455)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQQ5grMVKphCFm5B5QSSkrjwSgyJAa7Mn1E9H1hoR5GQ5iiuDpwz9gFRDKWTeCPKEJjUSQPjfAkvoyPxE7aE1piRrNt7v4oTEzsWVgfEFsPxYPv9sqVo6BXhjYJsoJDE2sqQSBGfjMJEHmrfdN2jQVCxaHX7z4f1nEptzi8tQ49iCXBAJwfcRnsWS1QL4A3uTfkBHYw11FB26E"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 12:59:22.456)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak527RmFA2pTtuXBkhSoyjTPpxxxL2S2vLab7JWB7WViJ9XqoQvKpkH1wux4SJ9hpCjDHWf5c81LSEAN4sNV9f5yDg1yGVsUREHTXvskRdqd534vzdMe2jJqsBWeEmqkyc8xH6ZVwSVfnS7kq8kFxJK8BDToWkZz2xdvjWGHKCfwDoRZzJor1A3P9Xh3MJiXppQ893qr7uXUgyoASLBYTnnHsGpoycj1ebuzL8pFpe5X9pH83ZqjzC78rS3WyRC8JK18ygH7SxYpsQw1UPja7Dk71tv6a9nXrWTVAMmG5uy3EXBxN"
  }
}
```

#### initiator <--- (2018-10-24 12:59:22.460)
```javascript
{
  "action": "update",
  "channel_id": "ch_n1U3NKFhr2bgukf9vQcgwt6CewrPNCtorogfg2ExPtnWZCtdf",
  "payload": {
    "state": "tx_3XPhV5wAjiGDknBgEeGBHC3knFkwUtNYcQVtCoY8rfXgwT7QMtUkUfwdAkyFsqFJCh3AUs1MahJErjWYKVy9mfzMchPxSbwkaRtrrG7ZmaXDwiC2zwBqUitD2v1xByL4G4E3ZJkua2FBdD44bbrYbmg6zjsoz6CTkGfRbWM6Ag4btugzX2ek7xfy36UfAihHvCYYQrxzNBgWnfYiP6tkBooPG7pyPUQCMyMqD5mz3zH2WpyC9z8MNZpuNMCMfF1MTTkVqcWHsnmN62gXbjFYtTGLMscKTKmguttjjpjxNTCEGS7DajjXKTGVhuySKPrmctYyyK76jWEopd3cVFkiNpaqqN8S5Vo2uFFuH87gfVBUKa9CGyzyFpzzSzMgcvmtJDtcHYVMHxXUkd6xxtMMY"
  }
}
```

#### responder <--- (2018-10-24 12:59:22.460)
```javascript
{
  "action": "update",
  "channel_id": "ch_n1U3NKFhr2bgukf9vQcgwt6CewrPNCtorogfg2ExPtnWZCtdf",
  "payload": {
    "state": "tx_3XPhV5wAjiGDknBgEeGBHC3knFkwUtNYcQVtCoY8rfXgwT7QMtUkUfwdAkyFsqFJCh3AUs1MahJErjWYKVy9mfzMchPxSbwkaRtrrG7ZmaXDwiC2zwBqUitD2v1xByL4G4E3ZJkua2FBdD44bbrYbmg6zjsoz6CTkGfRbWM6Ag4btugzX2ek7xfy36UfAihHvCYYQrxzNBgWnfYiP6tkBooPG7pyPUQCMyMqD5mz3zH2WpyC9z8MNZpuNMCMfF1MTTkVqcWHsnmN62gXbjFYtTGLMscKTKmguttjjpjxNTCEGS7DajjXKTGVhuySKPrmctYyyK76jWEopd3cVFkiNpaqqN8S5Vo2uFFuH87gfVBUKa9CGyzyFpzzSzMgcvmtJDtcHYVMHxXUkd6xxtMMY"
  }
}
```

#### initiator ---> (2018-10-24 12:59:22.462)
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

#### initiator <--- (2018-10-24 12:59:22.463)
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

#### initiator ---> (2018-10-24 12:59:22.464)
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

#### initiator <--- (2018-10-24 12:59:22.465)
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

#### responder ---> (2018-10-24 12:59:22.465)
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

#### responder <--- (2018-10-24 12:59:22.468)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQQ5grMVKphCFm5B5QSSkrjwSgyJAa7Mn1E9H1hoR5GQ5iizeLoXh9SkwFGTBKHS5JWmy8xBEEjci6p17jVhmWTBTQNPLBUJcFXTEqkfxf8jdVbnqTzrQcQxMUbJNzvUuXmQZVVcbGso1BY37cR6MuhYqXpnY97breGcdku7VBSUm6dCSFH34NPXs5BcJL3dEjg8oLZpuQ8yvb"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 12:59:22.469)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak51APgwp2bEMG5eehZBkwKRzigZhTuxiRwvXkAJ5boVCG73GLAgyDEDnhK3he5EqoK1wE2L1Wvrg3BmxrJKgkSx3C8gVZMZducYeDHCQGVmqJHzNCR9euyxLh9imgMQYG6uicfXG9XqPJ8xejCYRpsp9YLaGAm4RLkFRzgG4yqRn19d74nt2AcaBjve2EYQmLd1fNnKYePvxdAKzdmxjRfz5NaHQ3MLQtPiqNazYapSfG91s75D3cCkyVQRdxvzVYcTHLrczkUKBiedxzjPBQmey4hrExgLTkCNAmecN2z6Gtjse"
  }
}
```

#### initiator <--- (2018-10-24 12:59:22.472)
```javascript
{
  "action": "info",
  "channel_id": "ch_n1U3NKFhr2bgukf9vQcgwt6CewrPNCtorogfg2ExPtnWZCtdf",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 12:59:22.473)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQQ5grMVKphCFm5B5QSSkrjwSgyJAa7Mn1E9H1hoR5GQ5iizeLoXh9SkwFGTBKHS5JWmy8xBEEjci6p17jVhmWTBTQNPLBUJcFXTEqkfxf8jdVbnqTzrQcQxMUbJNzvUuXmQZVVcbGso1BY37cR6MuhYqXpnY97breGcdku7VBSUm6dCSFH34NPXs5BcJL3dEjg8oLZpuQ8yvb"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 12:59:22.474)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak4oauGq5ohj8kXJoEVRnRhzg6VZx644mMUeKWaubgMnAPQFNoFFUm5A3wvYfwoYJDMhSL6kJeDYeDfkWkz9LJmFg91pFNgLXmS5Yf8Re28CkYtiLiuNrksGWtFPprX5d2dStqqcwLicgDsG31o4dtUUn61BXPbWjkXFZMiKzDFGuQy8JWDaimv1s7guGFDdDJWUzcGqj7z1DgSL3NtvbcgrdfM2HP91JXL5JDrG9UM8Uz1oDSq6YxsJaVgLac3XycaorECEeBeYi1GQ9WKywY1fKW8kJsW5TrEpxkqcpr3Ee6ZTd"
  }
}
```

#### initiator <--- (2018-10-24 12:59:22.477)
```javascript
{
  "action": "update",
  "channel_id": "ch_n1U3NKFhr2bgukf9vQcgwt6CewrPNCtorogfg2ExPtnWZCtdf",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkQef6bwkYyG39PHsk5a2bLpNyqjCZh9x7nM9EsriTbp7EyKkZu1P2F8orWPzWtJm1QkAAFUHckSNmJmb85ExCJUp31en53jKzvH6DKdTVgQydDBuMFE1M5xc1fXid8zDWJT28Bky1WBMb6KJJGddPyrBYhRtwkrt77uHC6Xah8MEEgvLpSk5JEwgq9vU7pfVx1dyxc6v1xFAbKrUVpzApsZWRH3xCbsoQDeVouBzX5Xge1cVE4q1Yf9NkyxRGYSAdmT4ahTpcgrvg2UWzLEti3uzFuoDXiS4ys1zPvnWk9pStAukhBsvj7gtDh3ZzYXJqMmNou2oH2BGt3HTUYBFVR6P13XhVxYTp57QWN6hkj9vjG8MGivPaWC6U719dq9BsUspoZXm2"
  }
}
```

#### responder <--- (2018-10-24 12:59:22.478)
```javascript
{
  "action": "update",
  "channel_id": "ch_n1U3NKFhr2bgukf9vQcgwt6CewrPNCtorogfg2ExPtnWZCtdf",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkQef6bwkYyG39PHsk5a2bLpNyqjCZh9x7nM9EsriTbp7EyKkZu1P2F8orWPzWtJm1QkAAFUHckSNmJmb85ExCJUp31en53jKzvH6DKdTVgQydDBuMFE1M5xc1fXid8zDWJT28Bky1WBMb6KJJGddPyrBYhRtwkrt77uHC6Xah8MEEgvLpSk5JEwgq9vU7pfVx1dyxc6v1xFAbKrUVpzApsZWRH3xCbsoQDeVouBzX5Xge1cVE4q1Yf9NkyxRGYSAdmT4ahTpcgrvg2UWzLEti3uzFuoDXiS4ys1zPvnWk9pStAukhBsvj7gtDh3ZzYXJqMmNou2oH2BGt3HTUYBFVR6P13XhVxYTp57QWN6hkj9vjG8MGivPaWC6U719dq9BsUspoZXm2"
  }
}
```

#### initiator ---> (2018-10-24 12:59:22.480)
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

#### initiator <--- (2018-10-24 12:59:22.481)
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

#### initiator ---> (2018-10-24 12:59:22.482)
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

#### initiator <--- (2018-10-24 12:59:22.483)
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

#### initiator ---> (2018-10-24 12:59:22.483)
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

#### initiator <--- (2018-10-24 12:59:22.486)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQQ5grMVKphCFm5B5QSSkrjwSgyJAa7Mn1E9H1hoR5GQ5ij64rf5Ece6fB2SiSBYgp31sdNcq1Vcz1dmTJorsdsap3w8M8aqbsDHVuzhum2djS13TZ7b3jvxxb3xQMJEEERrTH2Ty5oCpJZNma6MAasvjFir1GMjxiWbiq8uMK7H3iUjTpSHqgLnVJEdmRipL4jgjUU2njFzo6"
  },
  "tag": "update"
}
```

#### initiator ---> (2018-10-24 12:59:22.486)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4oFw6dSdKqgRFp5BwyHhcVVDLJLedET3xfUtB7C7Ar7mLyRt1pTTETuaw1uSt9tEJkbCfKngAcefRvyxmxQPZA2TgaHtjfJ2eBQPj76K8mxFfjCWFsAo53pU3eawNMHrarm7W5VqzXgUSpvcE7ZDe6pZMc4pYcQxaLdkxd5zXcN2iKrftA3k4kXZ4D7v5dg6Jg5eTfktQbcu68UL8rEqyXYHTnR7fPb76NYWeat4Bk1TKxR2fhmF7ziPeSkJWCx5R1mM6xYXh4wr6ryHkjbiuvgNU853MHNxjwWNRQGBNhoqwRH"
  }
}
```

#### responder <--- (2018-10-24 12:59:22.524)
```javascript
{
  "action": "info",
  "channel_id": "ch_n1U3NKFhr2bgukf9vQcgwt6CewrPNCtorogfg2ExPtnWZCtdf",
  "payload": {
    "event": "update"
  }
}
```

#### responder <--- (2018-10-24 12:59:22.526)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQQ5grMVKphCFm5B5QSSkrjwSgyJAa7Mn1E9H1hoR5GQ5ij64rf5Ece6fB2SiSBYgp31sdNcq1Vcz1dmTJorsdsap3w8M8aqbsDHVuzhum2djS13TZ7b3jvxxb3xQMJEEERrTH2Ty5oCpJZNma6MAasvjFir1GMjxiWbiq8uMK7H3iUjTpSHqgLnVJEdmRipL4jgjUU2njFzo6"
  },
  "tag": "update_ack"
}
```

#### responder ---> (2018-10-24 12:59:22.529)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak4u6HpSdhEdjrHFVmwByvwXS69aW3oGsvwu3tcsYGdHvMeiMAApihrU4ApbbiwU434cvSegygT1GeEFTiydqDJTavKaa4ztNryR5X3TLjQDg6UNQDx8R569NQmP9Dt7py51gSBdiLitDncAo5CRQMW7XHBXKWyvEQe6sV2Z8GARzqhsjB3ghMLs8oC7FWnPounjcYUNFwMB3URDZjeFKmUbwVzuTUZKKbHkyJEZZ6Zc2VX5ufaz7UYbtCdDTGPPWoiPHan9cAcdZWAGNbmUrbPSWQ3jGTSAmmkh6RC1cBehxs5XK"
  }
}
```

#### responder <--- (2018-10-24 12:59:22.542)
```javascript
{
  "action": "update",
  "channel_id": "ch_n1U3NKFhr2bgukf9vQcgwt6CewrPNCtorogfg2ExPtnWZCtdf",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkQ63i9yCP3KJY1rjwqU6CukqM76hDxo7Udy7NvFMMQ2VfgLA2EY1yBqCu8KdGLXWwLLmWbvyVcHtt2iGtp53fGWTCZmYdTbepVqjsADVF1NXEPMLuJUkpDVQ9bQiWtL4vfnSFwJyh8cQBTw4PMpvXhdWFKdVRQyrgMn3CfAz6rN6kfxE1nrDGNryjHpxsFVVVtE4z2t7ZtogHQEWTZyaj5idbUqqWi4DdHpKF2SnMvowPVbD98kZXJgm4P3ZMdvKCYg6F4KgnYw9iAA9e9cyxBrRzhip6cVgwrqRxFfAkc5h5TUjvVuYempfAnXjUshECUX9tmBYdqX5zYToN8pfej8CKuxqmAmszxpRPEjo6383V3Sk9sPmb7CdrG6WUn7s4NB2Tp14S"
  }
}
```

#### initiator <--- (2018-10-24 12:59:22.543)
```javascript
{
  "action": "update",
  "channel_id": "ch_n1U3NKFhr2bgukf9vQcgwt6CewrPNCtorogfg2ExPtnWZCtdf",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkQ63i9yCP3KJY1rjwqU6CukqM76hDxo7Udy7NvFMMQ2VfgLA2EY1yBqCu8KdGLXWwLLmWbvyVcHtt2iGtp53fGWTCZmYdTbepVqjsADVF1NXEPMLuJUkpDVQ9bQiWtL4vfnSFwJyh8cQBTw4PMpvXhdWFKdVRQyrgMn3CfAz6rN6kfxE1nrDGNryjHpxsFVVVtE4z2t7ZtogHQEWTZyaj5idbUqqWi4DdHpKF2SnMvowPVbD98kZXJgm4P3ZMdvKCYg6F4KgnYw9iAA9e9cyxBrRzhip6cVgwrqRxFfAkc5h5TUjvVuYempfAnXjUshECUX9tmBYdqX5zYToN8pfej8CKuxqmAmszxpRPEjo6383V3Sk9sPmb7CdrG6WUn7s4NB2Tp14S"
  }
}
```

#### initiator ---> (2018-10-24 12:59:22.549)
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

#### initiator <--- (2018-10-24 12:59:22.551)
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

#### initiator ---> (2018-10-24 12:59:22.552)
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

#### initiator <--- (2018-10-24 12:59:22.554)
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

#### responder ---> (2018-10-24 12:59:22.555)
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

#### responder <--- (2018-10-24 12:59:22.561)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQQ5grMVKphCFm5B5QSSkrjwSgyJAa7Mn1E9H1hoR5GQ5ijBVNWcn5qSP6nSFZ5fmJ5P2c54NNgzWMe6tyLfGsvgfTLvAQp1LkqLj9wZNEcHogy4kizy3UBTbMA9YQLzeqdQp7wWK82vRztn67BpGkgjN2S7cMn2cQZgjvEaQCZCGqTWkkvVUuEQJUz2EJz3uKVBoGwVofVvX6"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 12:59:22.562)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4mAHHzAMZfHbc4gWgN6XhK3NFKLRHnfk2a77uLx3MyfZyidLpBUqM4SKntqcp5pknxkTSNYeLbPWV7Tr2QiVhGCELddTtLwd1F3WkNQxmpkf8uPySGw2xCFiz1h5piVeMoQFnvnoCDcM7VxxJZbV1hnBjyM4ZpSnEPCe7vqtYHEWVvAJ6xdwnYD4FRzBpKik1pi9JvK7Myi2aoavueqReG2aQacGgQqkfbJqVzmgv8VHBXUndGzaKg4uE5NYVBmUKxvFitvAmnjRYKoDmvfPEyMK33b2qdzdtvcPBAsD4QquCiP"
  }
}
```

#### initiator <--- (2018-10-24 12:59:22.580)
```javascript
{
  "action": "info",
  "channel_id": "ch_n1U3NKFhr2bgukf9vQcgwt6CewrPNCtorogfg2ExPtnWZCtdf",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 12:59:22.581)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQQ5grMVKphCFm5B5QSSkrjwSgyJAa7Mn1E9H1hoR5GQ5ijBVNWcn5qSP6nSFZ5fmJ5P2c54NNgzWMe6tyLfGsvgfTLvAQp1LkqLj9wZNEcHogy4kizy3UBTbMA9YQLzeqdQp7wWK82vRztn67BpGkgjN2S7cMn2cQZgjvEaQCZCGqTWkkvVUuEQJUz2EJz3uKVBoGwVofVvX6"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 12:59:22.584)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak4uKpm9FdPrJrLri9ksceVgeiPxW2jW2nCuLK3TFn1yREoui1G3FdYGMPnBsJBF7MULfQoN4eeKdQcQrXvn96UwqfqKEkS299n7vcR1EPQ3TwH6TCPawie6Dq3ZXn89h7GjAHuSkqCDCMJ41Nq1sA29nmU6jVoCUm9igwenRCnKkzUomewwhXw58eHibFGNTyKz3ediHj8P3MY3hC3HJwxP7m1RApEY2JCayWkYzPUfZpGjsTYaZ7KN8hBBvQi9UNXEqYi4oZszcPCELgcUSpaJa3NXc6195H2nk7WJjUnqfTbZZ"
  }
}
```

#### initiator <--- (2018-10-24 12:59:22.595)
```javascript
{
  "action": "update",
  "channel_id": "ch_n1U3NKFhr2bgukf9vQcgwt6CewrPNCtorogfg2ExPtnWZCtdf",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkLUubfKVrynSP3LbxDKJffDab3GDHx23Q5eD2jt9vAPW4asJqvmNeV6AVLzUVRRafHtgB1LGkozLXKsMfKN7YQA2TcBiuRiWJyjRBi4U2tE5s1iV1Dnxwq7B8GVjLSUWKeqzjQPb9ZcjsW3sxY7w5B6ZRiyYh4cHDPbU1kCm6QXG6NUneENteaqHcxKoUbA9ViFDs3XeAjjcrto7qshjed3v7z691AehupnMVGRz6PdaVPVZ6YCcSKseXwYexBvwRmbkYJJU89At9vKpCV6xgn6PsGGs8n1JqQzvcqAFDEgKAj1FV63DgUqvVuFYSAJnhgJ99DrWUAX59rBbeukLHyozfzU5XCtSiQBNe7PeLEM47u2prqyX11ekBe7CjMXyHoaSii48s"
  }
}
```

#### responder <--- (2018-10-24 12:59:22.597)
```javascript
{
  "action": "update",
  "channel_id": "ch_n1U3NKFhr2bgukf9vQcgwt6CewrPNCtorogfg2ExPtnWZCtdf",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkLUubfKVrynSP3LbxDKJffDab3GDHx23Q5eD2jt9vAPW4asJqvmNeV6AVLzUVRRafHtgB1LGkozLXKsMfKN7YQA2TcBiuRiWJyjRBi4U2tE5s1iV1Dnxwq7B8GVjLSUWKeqzjQPb9ZcjsW3sxY7w5B6ZRiyYh4cHDPbU1kCm6QXG6NUneENteaqHcxKoUbA9ViFDs3XeAjjcrto7qshjed3v7z691AehupnMVGRz6PdaVPVZ6YCcSKseXwYexBvwRmbkYJJU89At9vKpCV6xgn6PsGGs8n1JqQzvcqAFDEgKAj1FV63DgUqvVuFYSAJnhgJ99DrWUAX59rBbeukLHyozfzU5XCtSiQBNe7PeLEM47u2prqyX11ekBe7CjMXyHoaSii48s"
  }
}
```

#### initiator ---> (2018-10-24 12:59:22.602)
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

#### initiator <--- (2018-10-24 12:59:22.603)
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
