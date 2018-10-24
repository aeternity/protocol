
#### initiator init (2018-10-24 13:00:18.368)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=initiator
```

#### responder init (2018-10-24 13:00:18.373)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=responder
```

#### responder <--- (2018-10-24 13:00:19.374)
```javascript
{
  "action": "info",
  "payload": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-24 13:00:19.376)
```javascript
{
  "action": "info",
  "payload": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-24 13:00:19.388)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_3d11KjpALm3t32sAMLL9Y5p9SUg9j82o5Er3hc4WTAmdXk3cXjxDydY4eoq6STXDutDQ59tM59bMr9CogemLkb4tUXrrZYvPc4DkdzkXhqGZjnzLVRAYpjMHXUeVmmqr9Fk96GrERRgHqJTaNp7wfhyEnqvb1nHkCFrzMT"
  },
  "tag": "initiator_sign"
}
```

#### initiator ---> (2018-10-24 13:00:19.426)
```javascript
{
  "action": "initiator_sign",
  "payload": {
    "tx": "tx_4L9GSozvM4HoMiSpx3PBzJLGhb2bSDBvJuBorqq8sHKAUZEjmuRvU3Ut46eEzAQk1qwz1hG7h9yMrtT52kpRznfNDMSfsPJms9XChB7WHDX4vt6ofTH3twkrzryRNwDaLKThMa3aSxwknXfQReZt1e3UYeaTYnqbBxA9FwcB2rfWmwQT8qsAGmKVr2NVN7Zq7YfgqYnsLz38sztsW5uWdaCy9iHPj1fgPmTbixuAFM3KxSLRi4pcZNdmhRKkDYiKVJR2cFLHwcE"
  }
}
```

#### responder <--- (2018-10-24 13:00:19.427)
```javascript
{
  "action": "info",
  "payload": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-24 13:00:19.428)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_3d11KjpALm3t32sAMLL9Y5p9SUg9j82o5Er3hc4WTAmdXk3cXjxDydY4eoq6STXDutDQ59tM59bMr9CogemLkb4tUXrrZYvPc4DkdzkXhqGZjnzLVRAYpjMHXUeVmmqr9Fk96GrERRgHqJTaNp7wfhyEnqvb1nHkCFrzMT"
  },
  "tag": "responder_sign"
}
```

#### responder ---> (2018-10-24 13:00:19.428)
```javascript
{
  "action": "responder_sign",
  "payload": {
    "tx": "tx_4L9GSozvM4HnpjexAUTJHmyY14jKsxa9bxV6dt23AinCAi89j62UjnUShUCah5Wf8sBZkomxTLiQrAcbwam67fDKPc7ttYs6nESsqfiE9An6adb7rjwNcwdWYWFd14YU4Y8cpByRmjRvUsKCjQRjuKKbHHB6fWWE3JtsRNgNzYpyEDoqNekFMaVZvbHh7gmecnmWxXsCWn22WGRYD5caCkNnRzFXaK7hi3gVwD5Csnk3pti9sxDpAQqiy2QTQzToQPLr4bLF5eW"
  }
}
```

#### initiator <--- (2018-10-24 13:00:19.430)
```javascript
{
  "action": "info",
  "payload": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-24 13:00:19.430)
```javascript
{
  "action": "on_chain_tx",
  "payload": {
    "tx": "tx_6jPYBUFTkcmT4VGTnacPuSa5CAzrBXNwa5GWdcZ6ZWucCtszvjop4orxTi7gaQEDx6dxBXgmQb6ES5kh2rH16DWqNSPVCbS7CqNqFruHfTNwtWaxzxhTcW6Pv1GRvndbFGwNpo2yNPZpcimwzNon26QUaFoYFDDE8f6r6gmHNFtyGwcaFcXX77V51PWtPbroEXfkuMP9i1BaXT7JxjhrUBmxuotzawhzs87oKBEveKb2y5B3ygK4fm8wrws4522Ak9rH1YecPRRgd73iLZc3atY4vAPUbTAhCtCfCQk49K5uuE3kMd7NWXfKombSraRZ6z9Q5wGV9y1DWGK3DRsEV7m86TpZQv9RG3iL6"
  }
}
```

#### initiator <--- (2018-10-24 13:00:19.431)
```javascript
{
  "action": "on_chain_tx",
  "payload": {
    "tx": "tx_6jPYBUFTkcmT4VGTnacPuSa5CAzrBXNwa5GWdcZ6ZWucCtszvjop4orxTi7gaQEDx6dxBXgmQb6ES5kh2rH16DWqNSPVCbS7CqNqFruHfTNwtWaxzxhTcW6Pv1GRvndbFGwNpo2yNPZpcimwzNon26QUaFoYFDDE8f6r6gmHNFtyGwcaFcXX77V51PWtPbroEXfkuMP9i1BaXT7JxjhrUBmxuotzawhzs87oKBEveKb2y5B3ygK4fm8wrws4522Ak9rH1YecPRRgd73iLZc3atY4vAPUbTAhCtCfCQk49K5uuE3kMd7NWXfKombSraRZ6z9Q5wGV9y1DWGK3DRsEV7m86TpZQv9RG3iL6"
  }
}
```

#### initiator ---> (2018-10-24 13:00:22.179)
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

#### initiator <--- (2018-10-24 13:00:22.181)
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

#### initiator <--- (2018-10-24 13:00:27.226)
```javascript
{
  "action": "info",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "event": "own_funding_locked"
  }
}
```

#### responder <--- (2018-10-24 13:00:27.227)
```javascript
{
  "action": "info",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "event": "own_funding_locked"
  }
}
```

#### responder <--- (2018-10-24 13:00:27.228)
```javascript
{
  "action": "info",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "event": "funding_locked"
  }
}
```

#### initiator <--- (2018-10-24 13:00:27.230)
```javascript
{
  "action": "info",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "event": "funding_locked"
  }
}
```

#### responder <--- (2018-10-24 13:00:27.233)
```javascript
{
  "action": "info",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "event": "open"
  }
}
```

#### initiator <--- (2018-10-24 13:00:27.233)
```javascript
{
  "action": "info",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "event": "open"
  }
}
```

#### responder <--- (2018-10-24 13:00:27.234)
```javascript
{
  "action": "update",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "state": "tx_6jPYBUFTkcmT4VGTnacPuSa5CAzrBXNwa5GWdcZ6ZWucCtszvjop4orxTi7gaQEDx6dxBXgmQb6ES5kh2rH16DWqNSPVCbS7CqNqFruHfTNwtWaxzxhTcW6Pv1GRvndbFGwNpo2yNPZpcimwzNon26QUaFoYFDDE8f6r6gmHNFtyGwcaFcXX77V51PWtPbroEXfkuMP9i1BaXT7JxjhrUBmxuotzawhzs87oKBEveKb2y5B3ygK4fm8wrws4522Ak9rH1YecPRRgd73iLZc3atY4vAPUbTAhCtCfCQk49K5uuE3kMd7NWXfKombSraRZ6z9Q5wGV9y1DWGK3DRsEV7m86TpZQv9RG3iL6"
  }
}
```

#### initiator <--- (2018-10-24 13:00:27.235)
```javascript
{
  "action": "update",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "state": "tx_6jPYBUFTkcmT4VGTnacPuSa5CAzrBXNwa5GWdcZ6ZWucCtszvjop4orxTi7gaQEDx6dxBXgmQb6ES5kh2rH16DWqNSPVCbS7CqNqFruHfTNwtWaxzxhTcW6Pv1GRvndbFGwNpo2yNPZpcimwzNon26QUaFoYFDDE8f6r6gmHNFtyGwcaFcXX77V51PWtPbroEXfkuMP9i1BaXT7JxjhrUBmxuotzawhzs87oKBEveKb2y5B3ygK4fm8wrws4522Ak9rH1YecPRRgd73iLZc3atY4vAPUbTAhCtCfCQk49K5uuE3kMd7NWXfKombSraRZ6z9Q5wGV9y1DWGK3DRsEV7m86TpZQv9RG3iL6"
  }
}
```

#### initiator: (2018-10-24 13:00:27.863)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-24 13:00:27.863)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-24 13:00:27.863)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-24 13:00:27.864)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-24 13:00:27.864)
> Channel is `open` and ready to use

#### responder: (2018-10-24 13:00:27.864)
> Channel is `open` and ready to use

#### initiator ---> (2018-10-24 13:00:27.907)
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

#### initiator <--- (2018-10-24 13:00:27.910)
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

#### initiator ---> (2018-10-24 13:00:27.910)
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

#### initiator <--- (2018-10-24 13:00:27.917)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQNSNWJkkNXhP3DVD5dpD4oRYNBgEWCDdLJNCdnAW7BndsN9adjRVQc8MF1A5C8mfBB2J9G2ChHbtwgykSMYBTaAC6dz7gy4v2PGgY1vjk52zsUJ1ENsf8S7PX4E4sZfpRkpczhQZqxu8C4oRVirTptQ99pevzf926vN78eBXowTx1vjkV5ZMXdmwjzZpX1wgpv27we1dvdtCJ"
  },
  "tag": "update"
}
```

#### initiator ---> (2018-10-24 13:00:27.919)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak59t18MGdAooYhx3tytvViAeQjsK5sySdwt8v41joDrBeZiHZYfcVV1VFjRb1J8AsMzcBwFh3PFq8WcdcKfZCYqVBeHynA8UmDWp5iUTkzUoZzqG2UYHVH71E1vji57AnLvF9XFiwGabfNsXkXeZ6NzduVdU4WwLEKLGQz5JQBvouP7bzVRJHmqehkZQPdm4rhPSmWP1CvEno1wLR5BA4R16ahCcCm4QJ4cmyicmzwH2SpRmm9CFwEvqfdZuRn8zrYYdTuxCkjbZeR8bNvixfPArt3UceEgAVs68BZxmdTYbViFd"
  }
}
```

#### responder <--- (2018-10-24 13:00:27.926)
```javascript
{
  "action": "info",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "event": "update"
  }
}
```

#### responder <--- (2018-10-24 13:00:27.927)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQNSNWJkkNXhP3DVD5dpD4oRYNBgEWCDdLJNCdnAW7BndsN9adjRVQc8MF1A5C8mfBB2J9G2ChHbtwgykSMYBTaAC6dz7gy4v2PGgY1vjk52zsUJ1ENsf8S7PX4E4sZfpRkpczhQZqxu8C4oRVirTptQ99pevzf926vN78eBXowTx1vjkV5ZMXdmwjzZpX1wgpv27we1dvdtCJ"
  },
  "tag": "update_ack"
}
```

#### responder ---> (2018-10-24 13:00:27.928)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak521nARLMwWbuD6jSoJR3ckCaZomhFWxGDcE4Qvc4AVaVk8QGGDyyMNkyRf8fwyMwmXR8fAzyZZu6iuLFQU9MxaEZXyQKb88CTtnZveB8WBzXdf9bTUirmtYEGRTCNhNPkN5q67Ra5vgKYRkUdMY9KSPs3QSBKggpRLVNNFQS542zmkqrGstKPgR3TRhhFaXdrYgbKDxANsfS2mfoD7p9ncWepXaNMdYWcF889ikfuDWeJ1Q48MZYfPR6ifzVoT8JVmU9txJaTTCqFPfKghZNCuenX7dd3AKAYVzGYKFmEx85e2s"
  }
}
```

#### responder <--- (2018-10-24 13:00:27.935)
```javascript
{
  "action": "update",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkn1y333BQoihahNoWEwfKa8ZvPmjLca9eQrqqkBR9GTgVRctKTaR6phyAaPz7JWWS1Jmox3UBimqMcVi3EX6VKjQa5DLKxBtDAvrNauqUZ9vDCmvzqdRKrUn9iGjZvhAABtMnAQyC17YoyZk1e6K9f42xznhmbjuMKeT4zQtjqMQiWNLTLvCvwBeaYUM1dun4ApXDVpePqRCYwnZwtEeTPkhYFUnc3oBk3jSB21wwE4brtPuVQRRfncP6egDw3Hrgo3uyZg5AzuzwEHHmnP5EGuGGEhnKoY3aXtG8oESEmKgjwLpywcXBSMMZoXxeAdcaTjypTDb7sMFuuqPpppjtR2Meif5TsbgBu9R5h6byNi2mEU8fmY3pwjyFnAK98CMYcj5AtMDr"
  }
}
```

#### initiator <--- (2018-10-24 13:00:27.936)
```javascript
{
  "action": "update",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkn1y333BQoihahNoWEwfKa8ZvPmjLca9eQrqqkBR9GTgVRctKTaR6phyAaPz7JWWS1Jmox3UBimqMcVi3EX6VKjQa5DLKxBtDAvrNauqUZ9vDCmvzqdRKrUn9iGjZvhAABtMnAQyC17YoyZk1e6K9f42xznhmbjuMKeT4zQtjqMQiWNLTLvCvwBeaYUM1dun4ApXDVpePqRCYwnZwtEeTPkhYFUnc3oBk3jSB21wwE4brtPuVQRRfncP6egDw3Hrgo3uyZg5AzuzwEHHmnP5EGuGGEhnKoY3aXtG8oESEmKgjwLpywcXBSMMZoXxeAdcaTjypTDb7sMFuuqPpppjtR2Meif5TsbgBu9R5h6byNi2mEU8fmY3pwjyFnAK98CMYcj5AtMDr"
  }
}
```

#### initiator ---> (2018-10-24 13:00:27.939)
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

#### initiator <--- (2018-10-24 13:00:27.940)
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

#### initiator ---> (2018-10-24 13:00:27.941)
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

#### initiator <--- (2018-10-24 13:00:27.942)
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

#### responder ---> (2018-10-24 13:00:27.942)
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

#### responder <--- (2018-10-24 13:00:27.945)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQNSNWJkkNXhP3DVD5dpD4oRYNBgEWCDdLJNCdnAW7BndsNF19ay2soU5Am9cK2tjfDPT7xTk4UyRHhKC6tLahdG3W3mvyCEev1KumxnCDeh58SKJQGFergc2HARCvcSF2xNyqcSutCcjtQCk2pKZzhCmvXvX43WE2eXkoqQKqNM2LxBK8Si9nAQQGMDF2SNhKEcqKk5gtCny8"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 13:00:27.946)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak54zZyHXnCskvCauz82yZwNufvPKdVBahNU3AUYgTsL3v76eQnoANXSN8wYKhCpg3vZeqcM6X2twGVwJfFPZ4pe9gphNtpUa89K3UsETpeTiHd2gfQAb1h1tHzE8KHTHNAqmE78tSahHv2Pz5W6x8ox6pPUr3BxWPNnpGaHhzzGdKVvGSBSqxg8g8YFhrHoPSnLawt2T1HnAjGgUgrUQ66CprETvaX6Ym2iLVGuU1EHGWGGL1zTECC5eXGKKpMUwqC4xN1KgTzzVSXKbaFrj4m62EbJPUdz15wBEs1K4v9qRWjHy"
  }
}
```

#### initiator <--- (2018-10-24 13:00:27.949)
```javascript
{
  "action": "info",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 13:00:27.950)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQNSNWJkkNXhP3DVD5dpD4oRYNBgEWCDdLJNCdnAW7BndsNF19ay2soU5Am9cK2tjfDPT7xTk4UyRHhKC6tLahdG3W3mvyCEev1KumxnCDeh58SKJQGFergc2HARCvcSF2xNyqcSutCcjtQCk2pKZzhCmvXvX43WE2eXkoqQKqNM2LxBK8Si9nAQQGMDF2SNhKEcqKk5gtCny8"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 13:00:27.951)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak4xC2dhAAx5E9eT4LBLCUNdhdAJ8KVxgjEBmXv9vcQTiW3bvUKo36PuVaTXnGFwBGDwWGD7ezmaBHqLzfiJJbihqF18sMHuJM8DXGQgXxysjndyRURvYWotHtZFsPYmMsLvLxZBSvfscpkzBNZbSkhTdh4u3kRudb4qimzhZ3FwmFVd6zX723i4uZde91hw2YgJ6vbR35PWC1GeVwfcj9hsocGJnoE614N33iouU8H3aexnawAnDMZ6n8QG8yKpGQFhWRKRijbnoX7eZrrhhV37L7mt9CYbLbkNrepWAR66a2Zx5"
  }
}
```

#### initiator <--- (2018-10-24 13:00:27.954)
```javascript
{
  "action": "update",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkfSjuZDo58pTXS3JwBp6TEq1HHZ2qEbGc1TyNPRu1XDTTDQaZy2Atdeg2ifSDUQMCztuuP7tvuhdq16PeR4NWTbxDNkMSs2Sgife9iaXA2gZjKAJdvbg3qUgjngMWnjqpgJ9VvjtszQ6aQTXARTptB9YDTTBEFXj8yb2sqKzAft32yCz1MhNvQuGU3DcSx1dWaLTMReQo5FNDxHLkuhcccA2BmCgT4DEPSbUPSLuNw3wQ3mNpmpnQQSf78RZ7jhSXLjxiXRmu7izPwAbSvsDaGjLyjbw4H1JnwrrweYUSaqVkfiWXJQ4QYNp4HYd8g5GfgT2bf2u49BveHiTRSh5Ge1wqQ2eAwPcNipAUU6DqCWBjs4Gu5xQvHBHkUxpW8xLU4ACmNvHe"
  }
}
```

#### responder <--- (2018-10-24 13:00:27.955)
```javascript
{
  "action": "update",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkfSjuZDo58pTXS3JwBp6TEq1HHZ2qEbGc1TyNPRu1XDTTDQaZy2Atdeg2ifSDUQMCztuuP7tvuhdq16PeR4NWTbxDNkMSs2Sgife9iaXA2gZjKAJdvbg3qUgjngMWnjqpgJ9VvjtszQ6aQTXARTptB9YDTTBEFXj8yb2sqKzAft32yCz1MhNvQuGU3DcSx1dWaLTMReQo5FNDxHLkuhcccA2BmCgT4DEPSbUPSLuNw3wQ3mNpmpnQQSf78RZ7jhSXLjxiXRmu7izPwAbSvsDaGjLyjbw4H1JnwrrweYUSaqVkfiWXJQ4QYNp4HYd8g5GfgT2bf2u49BveHiTRSh5Ge1wqQ2eAwPcNipAUU6DqCWBjs4Gu5xQvHBHkUxpW8xLU4ACmNvHe"
  }
}
```

#### initiator ---> (2018-10-24 13:00:27.958)
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

#### initiator <--- (2018-10-24 13:00:27.959)
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

#### initiator ---> (2018-10-24 13:00:27.959)
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

#### initiator <--- (2018-10-24 13:00:27.960)
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

#### responder ---> (2018-10-24 13:00:27.961)
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

#### responder <--- (2018-10-24 13:00:27.964)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQNSNWJkkNXhP3DVD5dpD4oRYNBgEWCDdLJNCdnAW7BndsNLRfSWaLzoo6X99Rw1aezgyrWuK8TfKR7N5iopLPN1eXY3M5s62AfGew4Du1PUAE7xG2mJyHZreDSqndKh7gtP79qPmonBTJ5aEHCgXRBo3Aqb58W6JS6FPrbdQxf7avQDSS48nMgRqL8VVCS6UPAaM7NuX79vA2"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 13:00:27.965)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4m2gS6X6GitKrgqUtfNaGKrhQqMcHbpnCdjs6WMnmoqvScFjyFSBjpeeMHiue2sCYWmTYAw9cTL5dtG5ymh2yA6ZZC34RpB8NiaAJ5ebRbjrLq1QTScj7gVaVrRtyBEu6hzT3Y9LecWSvQxFyNFvMASUSea4v8JrBwXkspKRc96GJz5dMJDM2RfcAUH5r5zmXitG7HEPpXxqQJAqXrtgzFzjhnyTVk6vpLibGMF3kKux8Ag1DpWSEc9ELfRxbifJZuHaJJ6wjNFSvhdbFPWM3vxpnPdNVgpCeHGi8bzXMrQhsxP"
  }
}
```

#### initiator <--- (2018-10-24 13:00:27.968)
```javascript
{
  "action": "info",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 13:00:27.969)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQNSNWJkkNXhP3DVD5dpD4oRYNBgEWCDdLJNCdnAW7BndsNLRfSWaLzoo6X99Rw1aezgyrWuK8TfKR7N5iopLPN1eXY3M5s62AfGew4Du1PUAE7xG2mJyHZreDSqndKh7gtP79qPmonBTJ5aEHCgXRBo3Aqb58W6JS6FPrbdQxf7avQDSS48nMgRqL8VVCS6UPAaM7NuX79vA2"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 13:00:27.969)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak57nskb6gNwgtD5ayV7mibMJLZdhUbJuoArdMKDTTHNYPo9iYXQ2LKJZQvTtrrLi425dTVaFUFCkPK7C15d6QF9RFxDNAStR7vaaK6hNtrP1ptGQByXE3za7SW9nZZqmfQbjNxQf4aTktfq6hUHWd4b6yaoixzLzxy2ebXjVhLJseR1efnTThRzBt59hJJEbxC9H3PQ7h9EzX4cLZiFVbGLp2gqr7aLbhafYTqFERcLvhPJdKZsjqjQm9tHdg898Uxb5tYQ47hdce9TGe3urmEhPVTq5wRpFEnHmthCeTyy6PTJj"
  }
}
```

#### initiator <--- (2018-10-24 13:00:27.973)
```javascript
{
  "action": "update",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkLFqgj8BMMLcmDneoGnr7ZixbpCxTPGVDTL9YFzH3MHaWanaisxV74duUYdGcZCpMjVHBbw4JKUniEXZTmo3Gg2ZjFRXKgGuWuPfrDtJiYAtTeEo7rPycvSBgj336Dg8NUzCHifkS9njTfXPFKDqoRaapgFQ6hqrdk91j7mCqPCddq8LrDQEMUVTNAemkfkbMPuZq1rkVWMPGvFTtPUW1g1CU7AXxTrjm8HhX1J6vgaJpSdL5gZFtzspgW4hpXZZrq2NRkAx5NryHnCP8DsvSAxvjELMmm5WYSrXUwgKK9D8tdR362HjRK5wVbaFwP3ZqiWRVVapMazvDWHv9b2FRa1M1riHx6bopN8UkJxbVA7emqZTRFsKJWNA5ihgJ2cB5KL6Aa19D"
  }
}
```

#### responder <--- (2018-10-24 13:00:27.974)
```javascript
{
  "action": "update",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkLFqgj8BMMLcmDneoGnr7ZixbpCxTPGVDTL9YFzH3MHaWanaisxV74duUYdGcZCpMjVHBbw4JKUniEXZTmo3Gg2ZjFRXKgGuWuPfrDtJiYAtTeEo7rPycvSBgj336Dg8NUzCHifkS9njTfXPFKDqoRaapgFQ6hqrdk91j7mCqPCddq8LrDQEMUVTNAemkfkbMPuZq1rkVWMPGvFTtPUW1g1CU7AXxTrjm8HhX1J6vgaJpSdL5gZFtzspgW4hpXZZrq2NRkAx5NryHnCP8DsvSAxvjELMmm5WYSrXUwgKK9D8tdR362HjRK5wVbaFwP3ZqiWRVVapMazvDWHv9b2FRa1M1riHx6bopN8UkJxbVA7emqZTRFsKJWNA5ihgJ2cB5KL6Aa19D"
  }
}
```

#### initiator ---> (2018-10-24 13:00:27.976)
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

#### initiator <--- (2018-10-24 13:00:27.977)
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

#### initiator ---> (2018-10-24 13:00:27.978)
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

#### initiator <--- (2018-10-24 13:00:27.979)
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

#### initiator ---> (2018-10-24 13:00:27.979)
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

#### initiator <--- (2018-10-24 13:00:27.982)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQNSNWJkkNXhP3DVD5dpD4oRYNBgEWCDdLJNCdnAW7BndsNRrBJ47pC9X2H8gYq8CAWvtLwLuuDfbKw8RJ7ySWnR1B6nN2yd1nM6v1JFr7HNGAXCt7t3cR5sFKuVoyhSSPYpzwNF9chbGR6utEswL6NAvtjeYFkEQWLEUvqRH6KusYFkU1DPZfdgTZBWxJ7HZiE8HFH7YPMQW9"
  },
  "tag": "update"
}
```

#### initiator ---> (2018-10-24 13:00:27.983)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak58esiqzm9KgHVwqjAC7mytsCmGBqtSVQCJjUoaqgqHG23GZAvJADd9ph6SnJg5GPyLzkMtf6yjjtCVA6twLkEY7285xcE6qkyqCeHrKNFH9PBDhXfddeSwNJp4TnBq1b725jYBg8zbhHTRN7tVtGXyduRfjbdNFUXrMyB9qcEDvqwX4wjuxwoEkjqXMnv9csE7wh1tfZczxQoHoUwZxvmxQu8T34yET7A1oZcpUk5UNUEr2CjYu2VQJiXqZ55SRkV4KBP97wtkCCdAHnCVZVodAjN29m2ov3XbBya1j99Hj34Bz"
  }
}
```

#### responder <--- (2018-10-24 13:00:28.25)
```javascript
{
  "action": "info",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "event": "update"
  }
}
```

#### responder <--- (2018-10-24 13:00:28.27)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQNSNWJkkNXhP3DVD5dpD4oRYNBgEWCDdLJNCdnAW7BndsNRrBJ47pC9X2H8gYq8CAWvtLwLuuDfbKw8RJ7ySWnR1B6nN2yd1nM6v1JFr7HNGAXCt7t3cR5sFKuVoyhSSPYpzwNF9chbGR6utEswL6NAvtjeYFkEQWLEUvqRH6KusYFkU1DPZfdgTZBWxJ7HZiE8HFH7YPMQW9"
  },
  "tag": "update_ack"
}
```

#### responder ---> (2018-10-24 13:00:28.30)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak53fPAh5i3k7vweQn6bCxkNTw1dNcsCNT8gV5QfuVBkmUohd5wHqS6gKC68EQ8FXWXD7KBfKFfo2qxspXUYy6vLgWK1AGuZ24USdRCRTQdDtXDa1tksMzqJcKXCgndBjYH7jfbSH8bTQawKjURuiqxVMeUwwaTS9DAYP5gPWCHz9pgEFfvTXD4mhqymmNgKjQMS5FSBNQHL3BYag68AJwbeDW6gaqRzf3oFa7FHD2o5oZ2PYwVwtU8dyK61UGePcVckodKYFwC38FyMFKh5zurmhwpGGpzhfpVbv4etRPSkBLecU"
  }
}
```

#### responder <--- (2018-10-24 13:00:28.44)
```javascript
{
  "action": "update",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkprKq5yBmtKi11puN6knpwXcUrtd7gmMGHRnKEgiAtLW7fWdAqdaQNXuJp7RDUcFzo87EDecaM6VHkrpwZLaK5ssWwednRTEsweCBkUZeobsvS1fHnBnoxmbZGdfGqzyVfPZAzJGRxd6vNjfG54qVn2V356QQQXsZUvJyT3i42TSXWS1q1SMUukmTS3JEruFKW9y2RRojVptbYjJCvrq21q1KANm98uMw7m8zwrS7Q4AQYxzDPNJw2eSyEuk2nnZGQ8MvcTz46oczY6wMHeNgNbJCA8LwinS9pSQ36P4qRyNAeCeW3QnwpRyQNZoCQQQeQRzcvVUNqYChSLNbzERanWr5FgiWyFZ9PkKE3jtGtSoy3YiGWBbnEn3zqwgDEBovJwhFKigj"
  }
}
```

#### initiator <--- (2018-10-24 13:00:28.46)
```javascript
{
  "action": "update",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkprKq5yBmtKi11puN6knpwXcUrtd7gmMGHRnKEgiAtLW7fWdAqdaQNXuJp7RDUcFzo87EDecaM6VHkrpwZLaK5ssWwednRTEsweCBkUZeobsvS1fHnBnoxmbZGdfGqzyVfPZAzJGRxd6vNjfG54qVn2V356QQQXsZUvJyT3i42TSXWS1q1SMUukmTS3JEruFKW9y2RRojVptbYjJCvrq21q1KANm98uMw7m8zwrS7Q4AQYxzDPNJw2eSyEuk2nnZGQ8MvcTz46oczY6wMHeNgNbJCA8LwinS9pSQ36P4qRyNAeCeW3QnwpRyQNZoCQQQeQRzcvVUNqYChSLNbzERanWr5FgiWyFZ9PkKE3jtGtSoy3YiGWBbnEn3zqwgDEBovJwhFKigj"
  }
}
```

#### initiator ---> (2018-10-24 13:00:28.52)
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

#### initiator <--- (2018-10-24 13:00:28.54)
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

#### initiator ---> (2018-10-24 13:00:28.55)
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

#### initiator <--- (2018-10-24 13:00:28.56)
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

#### responder ---> (2018-10-24 13:00:28.57)
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

#### responder <--- (2018-10-24 13:00:28.61)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQNSNWJkkNXhP3DVD5dpD4oRYNBgEWCDdLJNCdnAW7BndsNXGh9bfHPVEx38DfjFGeZJ3KdnTGR37fwTrxemqkqWraWaBKCnkfyA9FF7Jas2LRVEBHmRc9LMt61gx2kCrzkPMnHHVewJt7SKCmyQSGAyZfSv9MAX4CPKW1w6Kymq6fEXkwhbCtXJGjvuRBNX8xydM3kaUUDByr"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 13:00:28.62)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4srb4RCHBjDxxbq2Q9TdciCsgpyx9j7Hv7w5FfCJsHhpjGL6YK1jFx5hVmJVfnru2txjm2KqcMpkiZuSJuBUh8ZXiRRjoMy6gZZc8Y6xKhLfnbeV7jt5mxUbx2od3sSpyXKmBnm1P1B7H63Zg8EVFBipBPUQGVFmB7U8BXjypXQXfW5jNXVRjVHiAyXZM1yF7iK6gv28YwMFLRq6yJJghz8ZpSjZzu9sqJosL24u593ki5GcKmKo1gL7uzGtYBJRuH7zZsgorq5X7twZwT9gNddT6cyRuM42ts15c3xnhY7tnbu"
  }
}
```

#### initiator <--- (2018-10-24 13:00:28.78)
```javascript
{
  "action": "info",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 13:00:28.79)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQNSNWJkkNXhP3DVD5dpD4oRYNBgEWCDdLJNCdnAW7BndsNXGh9bfHPVEx38DfjFGeZJ3KdnTGR37fwTrxemqkqWraWaBKCnkfyA9FF7Jas2LRVEBHmRc9LMt61gx2kCrzkPMnHHVewJt7SKCmyQSGAyZfSv9MAX4CPKW1w6Kymq6fEXkwhbCtXJGjvuRBNX8xydM3kaUUDByr"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 13:00:28.79)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak535yHCX4BUA1gdXmRU2iCRmQCaAKwXeMbmSsLQN8SxiVFk3dPhcVQPVj3rTSWvfvwdU3yE5wYgDXcY4ZtjwDw7MHksqnsimNUd58P5cWZroLruASaHPqA2RtWp7BpdsZgwAZFbzXGSg1ycwwJ5BuZW3Zv5H27bDPxRMsmSEnHwYaSkr2uNEqGhSVi8qEFWY7sLMHuw837bp6Ffp72j2gZvRNC3FUMfm3v2hVCWRnPa3LCHqjGGnvb2oPS3LrHYWVzvSqKdhoRNwdpVteGLeeGKG41XLf44sK82GRj39JsmHCTyp"
  }
}
```

#### initiator <--- (2018-10-24 13:00:28.83)
```javascript
{
  "action": "update",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkXzUJ5rDyTjK4KTJtdmnNkVeFQQjUKzkdaU6NUUVia3H5vUDdUZQr3aTdbZJNa5Q4c5QQEjcyT3osPucHhK1pBMW6ZpHMaKbEKkQXjaob5zTNX3ZEmJ1ai7sTFK4x9RyifQGXewNYmsK2fKDji75qDjV9fg9UPcpZZxUAGjEX9qDAt7MhYznrzbiSS46WmPuV8R9K5E9aJ8ycBxVeu2ffkSp4JfZDjg6xvRajGax6mVHYQ4fYQ9SxsFzT8p9WMpFNkFaa6NvQnvPRPNiaJ6iZiR8D5HTLDUPmUcjHpG7DiDG2vA5kXDD2rxhoqT8iAbJbfFkqxyhuLajdy1fsCKceRDin5MuqmveG4nP85o6ZJTBjjZ9h83LzKz8mYQJknJhRsm6FVj4R"
  }
}
```

#### responder <--- (2018-10-24 13:00:28.84)
```javascript
{
  "action": "update",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkXzUJ5rDyTjK4KTJtdmnNkVeFQQjUKzkdaU6NUUVia3H5vUDdUZQr3aTdbZJNa5Q4c5QQEjcyT3osPucHhK1pBMW6ZpHMaKbEKkQXjaob5zTNX3ZEmJ1ai7sTFK4x9RyifQGXewNYmsK2fKDji75qDjV9fg9UPcpZZxUAGjEX9qDAt7MhYznrzbiSS46WmPuV8R9K5E9aJ8ycBxVeu2ffkSp4JfZDjg6xvRajGax6mVHYQ4fYQ9SxsFzT8p9WMpFNkFaa6NvQnvPRPNiaJ6iZiR8D5HTLDUPmUcjHpG7DiDG2vA5kXDD2rxhoqT8iAbJbfFkqxyhuLajdy1fsCKceRDin5MuqmveG4nP85o6ZJTBjjZ9h83LzKz8mYQJknJhRsm6FVj4R"
  }
}
```

#### initiator ---> (2018-10-24 13:00:28.87)
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

#### initiator <--- (2018-10-24 13:00:28.88)
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

#### initiator ---> (2018-10-24 13:00:28.161)
```javascript
{
  "action": "deposit",
  "payload": {
    "amount": 2
  }
}
```

#### initiator <--- (2018-10-24 13:00:28.167)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_2C9es4FjHoacyvw9uFsU88HyqWC8kHWVoKsFSgejaTfY71yhCFRbXB1EqpH2uMUQWf2iaDMTPgwGMZtKH8taSPZQ7j94rErvyBJYvvVFZpG1z8buj7sRdytAwVf8JZR9WX3Ntz3chh7jyuC3qjKcb8DYePDskH"
  },
  "tag": "deposit_tx"
}
```

#### initiator ---> (2018-10-24 13:00:28.170)
```javascript
{
  "action": "deposit_tx",
  "payload": {
    "tx": "tx_2WsEQsiC5XsnqpUkxrpXY41jgt5VWzaJ9ufWEPZnA45p4HCPRZNHEhZcNdt29SBbcGmQiptsbyw2XjDEnkRTfU3J9Wz9A9XRWWiYY5wgXXr1QBNrimJH5BsW9Q6NxXWJvPTHz3mfDC2HwdMHteXfAtjcJpeurJU1Eoq9Gb7kXtqPJNyMGywFfYVVgDkhJYKW24Y93wpPwLcnWtu5iQ1MiRAuKDygGPkrtgoDrUdhVyWExhFudmtvFyC3wNogyWtDQwD"
  }
}
```

#### responder <--- (2018-10-24 13:00:28.171)
```javascript
{
  "action": "info",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "event": "deposit_created"
  }
}
```

#### responder <--- (2018-10-24 13:00:28.171)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_2C9es4FjHoacyvw9uFsU88HyqWC8kHWVoKsFSgejaTfY71yhCFRbXB1EqpH2uMUQWf2iaDMTPgwGMZtKH8taSPZQ7j94rErvyBJYvvVFZpG1z8buj7sRdytAwVf8JZR9WX3Ntz3chh7jyuC3qjKcb8DYePDskH"
  },
  "tag": "deposit_ack"
}
```

#### responder ---> (2018-10-24 13:00:28.172)
```javascript
{
  "action": "deposit_ack",
  "payload": {
    "tx": "tx_2WsEQsiC5XsmnephXjWsQuCbhazbyop3mTLWbyYZnhDkDrz8XFF7Zsb1xMuZ5CCeNsc4aVsVqL3PTPii9W6YNES4MA7VpDdPw9XPrLG6Qvv8YennThXbR2FqjK4rAD55p1rCXvTEJdP9yeLnawtcUtGEwBC6J2mzANc1jAYyMVo6PLrsgeh5SS1XXBJsTcooWYUW11Lsfs7tBQfMJUpx21z8b3DLe1yUHvJsqkvfVk1y6e4zKvo81nRXxdWXcaJ4m2j"
  }
}
```

#### responder <--- (2018-10-24 13:00:28.174)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "tx": "tx_3cDMp6242sByNMV4bo7LU9WA8mTFi4tQSzKFpSEy8dEfTAh38kYuzvo6KYV5HoNMo9xpZXzQPKCm9rULkjZyJXXw4ZPubrzeMy2jSTxk8WqALGZZtdxuESvnut2V1LBFaFGeZDBejTtTQtXGrkt4DtDiYy9mX4uEwWUvXKKatCXY5r8mQpevxKuDjudGfbRyHuoZHRePWHXvDiY6hFWFgqkNYc4Jgb8NX8R93ryNjXfmuG6sbfqLiDBLAtyyTZupKbiXurLPW59ms36kA1Mck7u2nL44CDdEUqcn32HnpsLC5u8PNNdHkpihHksuAYE99bV5TbgQV9EoS3b3eN14p1TsDSvw6"
  }
}
```

#### initiator <--- (2018-10-24 13:00:28.174)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "tx": "tx_3cDMp6242sByNMV4bo7LU9WA8mTFi4tQSzKFpSEy8dEfTAh38kYuzvo6KYV5HoNMo9xpZXzQPKCm9rULkjZyJXXw4ZPubrzeMy2jSTxk8WqALGZZtdxuESvnut2V1LBFaFGeZDBejTtTQtXGrkt4DtDiYy9mX4uEwWUvXKKatCXY5r8mQpevxKuDjudGfbRyHuoZHRePWHXvDiY6hFWFgqkNYc4Jgb8NX8R93ryNjXfmuG6sbfqLiDBLAtyyTZupKbiXurLPW59ms36kA1Mck7u2nL44CDdEUqcn32HnpsLC5u8PNNdHkpihHksuAYE99bV5TbgQV9EoS3b3eN14p1TsDSvw6"
  }
}
```

#### initiator <--- (2018-10-24 13:00:33.51)
```javascript
{
  "action": "info",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "event": "own_deposit_locked"
  }
}
```

#### responder <--- (2018-10-24 13:00:33.51)
```javascript
{
  "action": "info",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "event": "own_deposit_locked"
  }
}
```

#### responder <--- (2018-10-24 13:00:33.51)
```javascript
{
  "action": "info",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "event": "deposit_locked"
  }
}
```

#### initiator <--- (2018-10-24 13:00:33.52)
```javascript
{
  "action": "info",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "event": "deposit_locked"
  }
}
```

#### responder <--- (2018-10-24 13:00:33.54)
```javascript
{
  "action": "update",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "state": "tx_3cDMp6242sByNMV4bo7LU9WA8mTFi4tQSzKFpSEy8dEfTAh38kYuzvo6KYV5HoNMo9xpZXzQPKCm9rULkjZyJXXw4ZPubrzeMy2jSTxk8WqALGZZtdxuESvnut2V1LBFaFGeZDBejTtTQtXGrkt4DtDiYy9mX4uEwWUvXKKatCXY5r8mQpevxKuDjudGfbRyHuoZHRePWHXvDiY6hFWFgqkNYc4Jgb8NX8R93ryNjXfmuG6sbfqLiDBLAtyyTZupKbiXurLPW59ms36kA1Mck7u2nL44CDdEUqcn32HnpsLC5u8PNNdHkpihHksuAYE99bV5TbgQV9EoS3b3eN14p1TsDSvw6"
  }
}
```

#### initiator <--- (2018-10-24 13:00:33.55)
```javascript
{
  "action": "update",
  "channel_id": "ch_Kx2gWyZFq8hbdUnBXv7a4TivG9cXowfPznffFqKgzHwqaPC8u",
  "payload": {
    "state": "tx_3cDMp6242sByNMV4bo7LU9WA8mTFi4tQSzKFpSEy8dEfTAh38kYuzvo6KYV5HoNMo9xpZXzQPKCm9rULkjZyJXXw4ZPubrzeMy2jSTxk8WqALGZZtdxuESvnut2V1LBFaFGeZDBejTtTQtXGrkt4DtDiYy9mX4uEwWUvXKKatCXY5r8mQpevxKuDjudGfbRyHuoZHRePWHXvDiY6hFWFgqkNYc4Jgb8NX8R93ryNjXfmuG6sbfqLiDBLAtyyTZupKbiXurLPW59ms36kA1Mck7u2nL44CDdEUqcn32HnpsLC5u8PNNdHkpihHksuAYE99bV5TbgQV9EoS3b3eN14p1TsDSvw6"
  }
}
```
