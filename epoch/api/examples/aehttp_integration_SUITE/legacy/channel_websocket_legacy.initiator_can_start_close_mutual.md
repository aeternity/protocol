
#### initiator init (2018-10-24 12:59:45.261)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=initiator
```

#### responder init (2018-10-24 12:59:45.265)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=responder
```

#### responder <--- (2018-10-24 12:59:46.267)
```javascript
{
  "action": "info",
  "payload": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-24 12:59:46.268)
```javascript
{
  "action": "info",
  "payload": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-24 12:59:46.271)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_3d11KjpALm3t32sAMLL9Y5p9SUg9j82o5Er3hc4WTAmdXk3cXjxDydY4eoq6STXDutDQ59tM59bMr9CogemLkb4tUXrrZYvPc4DkdzkXhqGZjnzLVRAYpjMHXUeVmmqr9Fk96GrERRgHqJTaNp7wfhyEnqvb1nHjbQbN7i"
  },
  "tag": "initiator_sign"
}
```

#### initiator ---> (2018-10-24 12:59:46.292)
```javascript
{
  "action": "initiator_sign",
  "payload": {
    "tx": "tx_4L9GSozvM4HkLDW8YMkuiKqZXkZeBE5fd4gfVts3AtmCMKyE26t6dv16tGhsb5HqrNvtzL3cSboFsSo9qZVtY5FE6RdBktPVncNx1o3f7jtfANF5a3GDfXY5zVM6TxRaJJbu3yf1fSjKThPemExgjd4GfrJADo2AMjqprhYFS5epz3h69kFJGgi2hjNVdfpMY4DRz1knYPdGa6Z4KgtMNCrhVnqPgRHgTKTohCy9UqvBx1bjGUeUmsynNNNAbiPfrpSwBL4Jhpg"
  }
}
```

#### responder <--- (2018-10-24 12:59:46.293)
```javascript
{
  "action": "info",
  "payload": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-24 12:59:46.294)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_3d11KjpALm3t32sAMLL9Y5p9SUg9j82o5Er3hc4WTAmdXk3cXjxDydY4eoq6STXDutDQ59tM59bMr9CogemLkb4tUXrrZYvPc4DkdzkXhqGZjnzLVRAYpjMHXUeVmmqr9Fk96GrERRgHqJTaNp7wfhyEnqvb1nHjbQbN7i"
  },
  "tag": "responder_sign"
}
```

#### responder ---> (2018-10-24 12:59:46.295)
```javascript
{
  "action": "responder_sign",
  "payload": {
    "tx": "tx_4L9GSozvM4HnJDsNehZSGEQKw8fpu84RAnbvXzwVfkGTsGZscsVj75DZsuksg7AjVhdXrb6p4TBMBXWCoVUwxp2e8kDtsaj3ecJAcD6TK5iUboLuRJS83pBhjnMGchvUDbob1i3jKJoWxV6pEgR3nfnXw5VQuwA4Yabaphdc3ka7zHAMo9nWTBxtsQZhq3QW9cx2cE7RFwcsQWrqbtfWBRdWaLwFLXAXoC8e8WMvbrwKrNyShmRKpXHBFa6Ew472RW8s2ED4QPm"
  }
}
```

#### initiator <--- (2018-10-24 12:59:46.296)
```javascript
{
  "action": "info",
  "payload": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-24 12:59:46.297)
```javascript
{
  "action": "on_chain_tx",
  "payload": {
    "tx": "tx_6jPYBUFTkcmNn2wWpj3gRL4gU9Kj77ka8XG2CTDRS367Wu92S7tx7dP9pZKknHeMqJuLj9yhX8bCgYS18sC3cQDboD9DtZqbJYbnza46oqJcivh6WaHUZMMzsyWqoUq2puvomgrC3MxCfbkLTBZcWt5HoeDvqo3HQF2oxSCXDrsXYwGaPY3kQCZo1fVCbwLnJAiHUDbDyZuXnY7XTAqyeuyiWQMLFgEi3EsRysEws7k8SY9GobwpfFs1Ly8CEYhHz8DxDQePLtR3KJA3vSutKCV7Hb2L2bzXWDP82ZpAaWVV4DGmkNdr8oqGv4jzvvVL5TqYMquEvA1YBLGPr9B3YnTL5gUFPDqV5u22C"
  }
}
```

#### initiator <--- (2018-10-24 12:59:46.297)
```javascript
{
  "action": "on_chain_tx",
  "payload": {
    "tx": "tx_6jPYBUFTkcmNn2wWpj3gRL4gU9Kj77ka8XG2CTDRS367Wu92S7tx7dP9pZKknHeMqJuLj9yhX8bCgYS18sC3cQDboD9DtZqbJYbnza46oqJcivh6WaHUZMMzsyWqoUq2puvomgrC3MxCfbkLTBZcWt5HoeDvqo3HQF2oxSCXDrsXYwGaPY3kQCZo1fVCbwLnJAiHUDbDyZuXnY7XTAqyeuyiWQMLFgEi3EsRysEws7k8SY9GobwpfFs1Ly8CEYhHz8DxDQePLtR3KJA3vSutKCV7Hb2L2bzXWDP82ZpAaWVV4DGmkNdr8oqGv4jzvvVL5TqYMquEvA1YBLGPr9B3YnTL5gUFPDqV5u22C"
  }
}
```

#### initiator ---> (2018-10-24 12:59:50.487)
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

#### initiator <--- (2018-10-24 12:59:50.489)
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

#### initiator <--- (2018-10-24 12:59:52.715)
```javascript
{
  "action": "info",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "event": "own_funding_locked"
  }
}
```

#### responder <--- (2018-10-24 12:59:52.715)
```javascript
{
  "action": "info",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "event": "own_funding_locked"
  }
}
```

#### responder <--- (2018-10-24 12:59:52.715)
```javascript
{
  "action": "info",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "event": "funding_locked"
  }
}
```

#### initiator <--- (2018-10-24 12:59:52.716)
```javascript
{
  "action": "info",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "event": "funding_locked"
  }
}
```

#### initiator <--- (2018-10-24 12:59:52.719)
```javascript
{
  "action": "info",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "event": "open"
  }
}
```

#### responder <--- (2018-10-24 12:59:52.719)
```javascript
{
  "action": "info",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "event": "open"
  }
}
```

#### responder <--- (2018-10-24 12:59:52.720)
```javascript
{
  "action": "update",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "state": "tx_6jPYBUFTkcmNn2wWpj3gRL4gU9Kj77ka8XG2CTDRS367Wu92S7tx7dP9pZKknHeMqJuLj9yhX8bCgYS18sC3cQDboD9DtZqbJYbnza46oqJcivh6WaHUZMMzsyWqoUq2puvomgrC3MxCfbkLTBZcWt5HoeDvqo3HQF2oxSCXDrsXYwGaPY3kQCZo1fVCbwLnJAiHUDbDyZuXnY7XTAqyeuyiWQMLFgEi3EsRysEws7k8SY9GobwpfFs1Ly8CEYhHz8DxDQePLtR3KJA3vSutKCV7Hb2L2bzXWDP82ZpAaWVV4DGmkNdr8oqGv4jzvvVL5TqYMquEvA1YBLGPr9B3YnTL5gUFPDqV5u22C"
  }
}
```

#### initiator <--- (2018-10-24 12:59:52.720)
```javascript
{
  "action": "update",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "state": "tx_6jPYBUFTkcmNn2wWpj3gRL4gU9Kj77ka8XG2CTDRS367Wu92S7tx7dP9pZKknHeMqJuLj9yhX8bCgYS18sC3cQDboD9DtZqbJYbnza46oqJcivh6WaHUZMMzsyWqoUq2puvomgrC3MxCfbkLTBZcWt5HoeDvqo3HQF2oxSCXDrsXYwGaPY3kQCZo1fVCbwLnJAiHUDbDyZuXnY7XTAqyeuyiWQMLFgEi3EsRysEws7k8SY9GobwpfFs1Ly8CEYhHz8DxDQePLtR3KJA3vSutKCV7Hb2L2bzXWDP82ZpAaWVV4DGmkNdr8oqGv4jzvvVL5TqYMquEvA1YBLGPr9B3YnTL5gUFPDqV5u22C"
  }
}
```

#### initiator: (2018-10-24 12:59:53.947)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-24 12:59:53.947)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-24 12:59:53.947)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-24 12:59:53.947)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-24 12:59:53.947)
> Channel is `open` and ready to use

#### initiator: (2018-10-24 12:59:53.947)
> Channel is `open` and ready to use

#### initiator ---> (2018-10-24 12:59:53.986)
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

#### initiator <--- (2018-10-24 12:59:53.989)
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

#### initiator ---> (2018-10-24 12:59:53.990)
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

#### initiator <--- (2018-10-24 12:59:53.999)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQPaZ85eXvv7UVo678PDw9icXgoyqXGLrreubQZdHA18uK22JBudpBzk8CSmcaVG7jUQio6WPbfLJPfWUKsqbGNxn29cqWy8mSMgoQgCi474qDsrfqmFVfdpv5peUbwi7SMJTnwgysRymjYwWYe8PBDwUxD4rj89ER4gwArqveC3b81fWqj3Uf3ZUuBfus5VCP81JVEQ959q7W"
  },
  "tag": "update"
}
```

#### initiator ---> (2018-10-24 12:59:54.1)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4pc3UUJ5ocpKKCggEn7DGdcuTbGZoW56ugL1F67rFX5YLFGvZNjQvD52uKgxFtx5mqGw56zSBEfjHi8L12cxjEype3cpYdfGxzios3JWQz1ALmPa9xpQPYg5Mhm3jNWaFT6JjLwB22GTL9khVnYVDnUEHWdBiYydtQQTMZTRMeVjUXQY5JjPL8v6PPQnAdt3L5HfnPvN6JV2qfL6LkjnZy7Xh4w8pYWUAguvd8CxZvdJ1VLKZBkGTYmUqbYAiLv9Y4GNekCKAWda2BV2p1MwoY99DsUCW4ihNBxQ4B6uBDLVCRv"
  }
}
```

#### responder <--- (2018-10-24 12:59:54.9)
```javascript
{
  "action": "info",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "event": "update"
  }
}
```

#### responder <--- (2018-10-24 12:59:54.11)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQPaZ85eXvv7UVo678PDw9icXgoyqXGLrreubQZdHA18uK22JBudpBzk8CSmcaVG7jUQio6WPbfLJPfWUKsqbGNxn29cqWy8mSMgoQgCi474qDsrfqmFVfdpv5peUbwi7SMJTnwgysRymjYwWYe8PBDwUxD4rj89ER4gwArqveC3b81fWqj3Uf3ZUuBfus5VCP81JVEQ959q7W"
  },
  "tag": "update_ack"
}
```

#### responder ---> (2018-10-24 12:59:54.12)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak58DbdYvkf8wXjiGtURX3bwMaPacfR7qej6L3AFygvbd2xUvb3m55Ej9J5N96Yp7CmMGn1QDsUJSnRKQxaBUnk9Mz4BvnoPt6PY1n3afjebeYStf82DFYbFjqecdgNZbhhe17Fmj9PQKcobcwA4SnUwDppvvXi4Qkr7ssp1ibSwqyjW1eKB9rdjhAoenNi9bsXnJiBiC5SRcbtLriw2HC84kd8VKcbe77ZzhyqysjxvZ6jRAjfdDtcdTEzvqzJfNKKPKepqvUrGoBgMhDonE59rhmY9GLpURGDPKjPsR5Xz28bhE"
  }
}
```

#### responder <--- (2018-10-24 12:59:54.19)
```javascript
{
  "action": "update",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkSQLBsnGxfGJkJZfwUDUYZPTZYCzZjQUCyYjz6rtMSh1wN2iRtVqCnfHkbN26LJctMDUnKGmMZz3aasAAQYDmSZTSyakLe5Fovt7mvhWoAmNGigdqXinmd67ToH8exwShgF5hfooaMuPAT7BxhFdABtos3wzErwpGfWQSfW1sb93ZTfnSMt4eeESXYUuuhcuHqqBkCNnpk3xvQZoFv1enSVEXdwTH7jSWzYAmqESfBK2Jrtx3pFwQGNe9JSRxBDz6hGQm82jyaN4hqkX3c7f1TkQ61CvVZ8dreTmQLU9khpNb76AqTy7QUP1Q2cjbS4rfMVhByFti3QduZPwZozv3XdDr3wNcuM4GjKBthxmbmcrJqmrnYkYxSV5dGZRj3D9mAiAK68ci"
  }
}
```

#### initiator <--- (2018-10-24 12:59:54.21)
```javascript
{
  "action": "update",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkSQLBsnGxfGJkJZfwUDUYZPTZYCzZjQUCyYjz6rtMSh1wN2iRtVqCnfHkbN26LJctMDUnKGmMZz3aasAAQYDmSZTSyakLe5Fovt7mvhWoAmNGigdqXinmd67ToH8exwShgF5hfooaMuPAT7BxhFdABtos3wzErwpGfWQSfW1sb93ZTfnSMt4eeESXYUuuhcuHqqBkCNnpk3xvQZoFv1enSVEXdwTH7jSWzYAmqESfBK2Jrtx3pFwQGNe9JSRxBDz6hGQm82jyaN4hqkX3c7f1TkQ61CvVZ8dreTmQLU9khpNb76AqTy7QUP1Q2cjbS4rfMVhByFti3QduZPwZozv3XdDr3wNcuM4GjKBthxmbmcrJqmrnYkYxSV5dGZRj3D9mAiAK68ci"
  }
}
```

#### initiator ---> (2018-10-24 12:59:54.24)
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

#### initiator <--- (2018-10-24 12:59:54.25)
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

#### initiator ---> (2018-10-24 12:59:54.26)
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

#### initiator <--- (2018-10-24 12:59:54.27)
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

#### responder ---> (2018-10-24 12:59:54.27)
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

#### responder <--- (2018-10-24 12:59:54.30)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQPaZ85eXvv7UVo678PDw9icXgoyqXGLrreubQZdHA18uK27ihmBMfC5r8Cm9hPPCDWmsmnwvxrhpjfquzQdzWS4dRZQeoCJWKyk2ed4AXgiuUqsy1edVPtKYqvqcezUY3YrpdrjKufhPRtLq5jbVM2k7ivLSnWWSLnrar44ifcvfT375V6CGuaBwRYKLNVvCsSc1sLU5K2FFA"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 12:59:54.31)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4pF2jeo28cmJq15WaXmR3aR2JMGA5MZKrt8dof7dyz5tSqvJLoNMxaDAHq7MHoqbjHd2jQE5rJSui2ZgqEafgnrXzsd9KgnHLahr3CwbGGBFRqqRNyaJTdyTzaUBbRUHprG3MLhqjScC9XUP6ZC6nWuoE6ZjukLxVqWGmNLDpZeAPYHosteYrJ7vgthZkUn5mLLRU26GL6NxrKEsENdkiRrfKioEHKqTxjCHLWLxWGwJwD2nzU8GsjCzfUiV4eEPXD7EjX3r6iURbbuJnceNiYWBBsX49KZD3CRvNak8XVSriip"
  }
}
```

#### initiator <--- (2018-10-24 12:59:54.34)
```javascript
{
  "action": "info",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 12:59:54.34)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQPaZ85eXvv7UVo678PDw9icXgoyqXGLrreubQZdHA18uK27ihmBMfC5r8Cm9hPPCDWmsmnwvxrhpjfquzQdzWS4dRZQeoCJWKyk2ed4AXgiuUqsy1edVPtKYqvqcezUY3YrpdrjKufhPRtLq5jbVM2k7ivLSnWWSLnrar44ifcvfT375V6CGuaBwRYKLNVvCsSc1sLU5K2FFA"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 12:59:54.35)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak4nc6Ssu1qSgiS6kTAAGK4P8c7RrSxNw6CxWVpqEFxQXdfwYywPNLUs6FRUAniiXpAcvAiXUF7WLJWnkfSyCW9jhSDAfegLq1zxRQPxQMDDk45XETdXUBdbrWrZ7SXqXxRNHGaq6ijTeGh4tCTwh4Cy72kcfk1PQz8qTty2ABmpLzXkXqDoFqNiRBhJdmvCGhtvJF5cenAaeHkDE9fFcDa2SYGL4mts3an7oTyMv3mMB6NLY3kWgPnfjuWEpsQewWKvWB9RStnzD5GyG2AioSDK5BPPnCuoFwQhz5mERLxkxzhFF"
  }
}
```

#### initiator <--- (2018-10-24 12:59:54.39)
```javascript
{
  "action": "update",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkNxzjhmZbm8K5Cfvn7pycu2URUTSYddAh2cZcuqUsQxD3MjEfMeYgMCtcpzCW5jwYsbm53dqt2GQCAqCmVZAFMYLhuZYx9XAR7P93hPNwCeN5tnFFfQrDVMB9w8Xk2xCyLxfabbFEBytGvUX5LUzKWtiWxQH6bhV1oVKLZkSLpxBsVS2uc4165nxVo7XFBbHL1Hw4Vmf2fB6rhWG9v9Vgj1w43A8vsst7Pq1aZRpUWHd5iAZnNAs747djCXdcE4S7bVxQZv5jYx8AHyjRYGj6hrcgZnE9FKJkW4aSoZKtswTVBmLaMSvEHm5wrzxVJ3wazScpXhRxrg1gpr9arwhERUHMWbaVhSwXQBLERtx1dUvBorgKJmuMfaq5t1zMbdJyKVgPstwt"
  }
}
```

#### responder <--- (2018-10-24 12:59:54.39)
```javascript
{
  "action": "update",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkNxzjhmZbm8K5Cfvn7pycu2URUTSYddAh2cZcuqUsQxD3MjEfMeYgMCtcpzCW5jwYsbm53dqt2GQCAqCmVZAFMYLhuZYx9XAR7P93hPNwCeN5tnFFfQrDVMB9w8Xk2xCyLxfabbFEBytGvUX5LUzKWtiWxQH6bhV1oVKLZkSLpxBsVS2uc4165nxVo7XFBbHL1Hw4Vmf2fB6rhWG9v9Vgj1w43A8vsst7Pq1aZRpUWHd5iAZnNAs747djCXdcE4S7bVxQZv5jYx8AHyjRYGj6hrcgZnE9FKJkW4aSoZKtswTVBmLaMSvEHm5wrzxVJ3wazScpXhRxrg1gpr9arwhERUHMWbaVhSwXQBLERtx1dUvBorgKJmuMfaq5t1zMbdJyKVgPstwt"
  }
}
```

#### initiator ---> (2018-10-24 12:59:54.42)
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

#### initiator <--- (2018-10-24 12:59:54.43)
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

#### initiator ---> (2018-10-24 12:59:54.43)
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

#### initiator <--- (2018-10-24 12:59:54.44)
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

#### responder ---> (2018-10-24 12:59:54.44)
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

#### responder <--- (2018-10-24 12:59:54.47)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQPaZ85eXvv7UVo678PDw9icXgoyqXGLrreubQZdHA18uK2D9Dciu8PRa3xkgpHW3DJ5QWMPW2qPis5tocL7kCApET3g4us9sadgmoiVsKRVzaXWve9gopmaAnDGCMhjQhUrwx5gBqFG6qZiKL7xSmXLNyDzzry6WkEaDtpHonuhE2V9CnhcuV6DNVKbaYVdywNZXeyJ2BSHkR"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 12:59:54.47)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4qHMCWkGRFiDbzw894AncAVHUNvyCrSqWEsVRv8d5VmGBQmC7zKXLUyLZTmJzwyqhpY4bdnzXcR3uTc77UYwiatHnUxvfzJYbhQ93PPNMPYnDFenkFb6QYQMPe3h6gJGG5HmW9o3AWo26zC1tL9z6PyHbjuEJ4hTqw6HA4QUG1W3gWMdFJyRs13HMLFo6eHuaHTMSESqjGTf6axfUqcdJVjkvvUt8CyZJUhjzmio6BazPpaT4yJDgxwY3jstyor9cp2LxRg4ENumDVh2f9YEE97bYADWRZouhHtMBR1T72tjcpF"
  }
}
```

#### initiator <--- (2018-10-24 12:59:54.50)
```javascript
{
  "action": "info",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 12:59:54.51)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQPaZ85eXvv7UVo678PDw9icXgoyqXGLrreubQZdHA18uK2D9Dciu8PRa3xkgpHW3DJ5QWMPW2qPis5tocL7kCApET3g4us9sadgmoiVsKRVzaXWve9gopmaAnDGCMhjQhUrwx5gBqFG6qZiKL7xSmXLNyDzzry6WkEaDtpHonuhE2V9CnhcuV6DNVKbaYVdywNZXeyJ2BSHkR"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 12:59:54.52)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak4rPHEnpo6ERFvGwLehJ5Px39w9ykQoCvbPSRKJhYXTkYc2RRPVgfDqA1byZwKqXdfGvNUuJEeeGCq2HJThXNDYG3s24hQvqQBKt2JMhJLypvbRGS4F9e1b3wrQ6uy6nXgFbWZMEd7ojH3aabx3uA7UEJ2mG78MNrGroNyJP5dvuoC8g4pmEeQf5GuyWViAeMfbbKZFxCfZtn6CBMhTYTj8UpeqMAYZsXm3F3Evy2nKfHfYAEL2FCN8dWCZguX2qHBM8KTZducsoYEnn9BJeKG5GTjMngYprx7rPfg1by2fzYdNR"
  }
}
```

#### responder <--- (2018-10-24 12:59:54.56)
```javascript
{
  "action": "update",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkTZuRCkz9FMpQbUNnCEwrvDwkyBCubdvJVbSPvbn9GGMPuHRMYW6UNGhbxcK9aVhBENB6Amk33c87kq5rCKAegXUqznroaF1bMWAsxL3CPoQFNXuQrr8BxwRscCwVmFjXzqk7BcPwFr31HsBwjxBeMfsqDVA61FPnMLnuB2dTsk1Pve56GbRWHQZYyHPK9MZ9LzQD6euAnTDevpHrfcdqLkDe7rKVmmpCn1tAVjiwxiq2DL376ThcnUDseS5D72ZcrYMcdhCssXFDbu5J7AwZiurF2pCyXrxPMkHqi5jcxpJZN5sD1vA5xGLbnA5GfjQFBLiM6hEcJvtk7GMLZxVqKi2HvHyXEuh1ZcadGs6fg7RTa9qDHWf1VuNtQxmnD6tRDTdtDGxZ"
  }
}
```

#### initiator <--- (2018-10-24 12:59:54.56)
```javascript
{
  "action": "update",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkTZuRCkz9FMpQbUNnCEwrvDwkyBCubdvJVbSPvbn9GGMPuHRMYW6UNGhbxcK9aVhBENB6Amk33c87kq5rCKAegXUqznroaF1bMWAsxL3CPoQFNXuQrr8BxwRscCwVmFjXzqk7BcPwFr31HsBwjxBeMfsqDVA61FPnMLnuB2dTsk1Pve56GbRWHQZYyHPK9MZ9LzQD6euAnTDevpHrfcdqLkDe7rKVmmpCn1tAVjiwxiq2DL376ThcnUDseS5D72ZcrYMcdhCssXFDbu5J7AwZiurF2pCyXrxPMkHqi5jcxpJZN5sD1vA5xGLbnA5GfjQFBLiM6hEcJvtk7GMLZxVqKi2HvHyXEuh1ZcadGs6fg7RTa9qDHWf1VuNtQxmnD6tRDTdtDGxZ"
  }
}
```

#### initiator ---> (2018-10-24 12:59:54.59)
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

#### initiator <--- (2018-10-24 12:59:54.60)
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

#### initiator ---> (2018-10-24 12:59:54.61)
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

#### initiator <--- (2018-10-24 12:59:54.62)
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

#### initiator ---> (2018-10-24 12:59:54.62)
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

#### initiator <--- (2018-10-24 12:59:54.65)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQPaZ85eXvv7UVo678PDw9icXgoyqXGLrreubQZdHA18uK2JZjUGSbamHyikDwBceipKJzmq6obPzmuf9BeGrKbDb6cR5rygsCKX2sxXpRKQ6WvmYjGRSxHamtfvDi5UjQ9JqjcXZeAfuxb3yHoDFShiGh84TzDEcpUZJy45fvaVWeLgEMrsgo3TziNd3eAq5GS7TnsVzuKecF"
  },
  "tag": "update"
}
```

#### initiator ---> (2018-10-24 12:59:54.66)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak59uJygQK36KLGq6zU8viCUhU1sDU2HaHzSwj1bJYGTpYMpzbfesTvbSF4rPNAH1WLwTL9mwkq5uEbcrU2bGXvuS8Aid8eyFM6hehgBYPnbdNzRQ36JkRgo1uY4Ai7Dd1Ma3FPPXrCthZ7t7nvkfcTYDmiJE5GZDvytHHBifDj9xkRk1JQ6FdSgRW3wmbVd3CY74gr5eH9XhZkijwaWzCfGPsSSg1yx4V1Shr9KPCaJfWNZcQq9n96e4Rny7nZJZbuKcCR6KucXD1bNYG18oH6piqFiGakyxbUXjQSyuBuBFWN2Y"
  }
}
```

#### responder <--- (2018-10-24 12:59:54.99)
```javascript
{
  "action": "info",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "event": "update"
  }
}
```

#### responder <--- (2018-10-24 12:59:54.100)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQPaZ85eXvv7UVo678PDw9icXgoyqXGLrreubQZdHA18uK2JZjUGSbamHyikDwBceipKJzmq6obPzmuf9BeGrKbDb6cR5rygsCKX2sxXpRKQ6WvmYjGRSxHamtfvDi5UjQ9JqjcXZeAfuxb3yHoDFShiGh84TzDEcpUZJy45fvaVWeLgEMrsgo3TziNd3eAq5GS7TnsVzuKecF"
  },
  "tag": "update_ack"
}
```

#### responder ---> (2018-10-24 12:59:54.101)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak5Bteb38K51kA3zdCLR7VXYGJBYwEujH1mtLE3mGSX3auB5CWVzZgenoGukpp1bj9kYFZTTaYjqubEuK28mjwbG1nnAVbyXGkRicbHkJmA288HFUeEt3KZytH8Xb2aLZAzmcDbgH2ocH1DuUfVU7WnD9eJ4npDfaqphdohRJg6CfqaMjJ1BsHAsvQEkfDZqUHn1h61FvRL6FLofJuagX6qL2REmFCfDK3vQXwqzRNfQ2E8WgpsvK4qqrvEwPgQyH72tb2sX74kbEEhfFN3pJD1ERBUpDVFGFZUd95yiFNkYKv33L"
  }
}
```

#### responder <--- (2018-10-24 12:59:54.107)
```javascript
{
  "action": "update",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "state": "tx_3XPhV5wAjiGDm1aYGwrZraL611MHdWSqEQeeDXTee8chCz3GFtsr2VjKwhwvruZj5hUcCnGh8F29VNr7vtT4ePp1aeiMNn6jkwU6BvgDPgU5sTHZNX85EKdHh8a9USYWsWZTtB4vbnWYnK9EpA4PCqWaLqf67L1oyghe1iXd1od8SHKUdEV5KWjtF75GVZXpgvZsCW9Gpc68wUMKwSWhP2Du7US1svU7hARvSLDsjXoDNxq4s8mzHPpYca5imAbpoWPEskB9QbzsaZ1wafi76KA4gf4h3vQYUqT9YNZddgYU3ac2xyN5dgAqt5mpdwDWchmZoB3zNY3X5EZMDuMnsTVC7V7wqizSYv3neNvQ5zpAghYQtRsGUYP3qnATHS9oF8sDrhCddyETDm8unMjQS"
  }
}
```

#### initiator <--- (2018-10-24 12:59:54.109)
```javascript
{
  "action": "update",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "state": "tx_3XPhV5wAjiGDm1aYGwrZraL611MHdWSqEQeeDXTee8chCz3GFtsr2VjKwhwvruZj5hUcCnGh8F29VNr7vtT4ePp1aeiMNn6jkwU6BvgDPgU5sTHZNX85EKdHh8a9USYWsWZTtB4vbnWYnK9EpA4PCqWaLqf67L1oyghe1iXd1od8SHKUdEV5KWjtF75GVZXpgvZsCW9Gpc68wUMKwSWhP2Du7US1svU7hARvSLDsjXoDNxq4s8mzHPpYca5imAbpoWPEskB9QbzsaZ1wafi76KA4gf4h3vQYUqT9YNZddgYU3ac2xyN5dgAqt5mpdwDWchmZoB3zNY3X5EZMDuMnsTVC7V7wqizSYv3neNvQ5zpAghYQtRsGUYP3qnATHS9oF8sDrhCddyETDm8unMjQS"
  }
}
```

#### initiator ---> (2018-10-24 12:59:54.112)
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

#### initiator <--- (2018-10-24 12:59:54.113)
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

#### initiator ---> (2018-10-24 12:59:54.113)
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

#### initiator <--- (2018-10-24 12:59:54.114)
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

#### responder ---> (2018-10-24 12:59:54.115)
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

#### responder <--- (2018-10-24 12:59:54.118)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQPaZ85eXvv7UVo678PDw9icXgoyqXGLrreubQZdHA18uK2PzFKoz4n71uUjm45jjCrgTyUGeAnmX7uzarB5FZeKSW2Cu9Crc5waG7uPGtu4Amtnqu9oSgY5Qen7Mm8FA1LsCaXZugQPXevTHptgMcWWuTqL55dXGWXeL49kip2QjmKTXJM5L1w5ou81WXS4eXBcXbLxwHnUwZ"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 12:59:54.119)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak54HT3aG8BoBxBkGzASbbWtXTzCLsqs8QrW7ZbVGjb8CqufFsYZqHJ6f558xMpxmpw4jxa2Bup2Zb42bfvC7k8NC3Qohq1RX7m8PgjyRXBpd6W6zaZP3KAdh2Zj7BPjr5zkkLHajeQ27j5td7avAXowrNKfK6a8fgKJafxfCmvhmbJSugd4Y3fvWRSutuDyDmBsP6uRibUTxrEqjzGaW2gbaPMKP6tyJDe7YFjXvFnkuMcn78gyGmE3ZpadPHyx1bRyKH6U14BR8XJXV5HwVqdKsUNpsuF4C9aGMXBtvufhyj475"
  }
}
```

#### initiator <--- (2018-10-24 12:59:54.146)
```javascript
{
  "action": "info",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 12:59:54.147)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQPaZ85eXvv7UVo678PDw9icXgoyqXGLrreubQZdHA18uK2PzFKoz4n71uUjm45jjCrgTyUGeAnmX7uzarB5FZeKSW2Cu9Crc5waG7uPGtu4Amtnqu9oSgY5Qen7Mm8FA1LsCaXZugQPXevTHptgMcWWuTqL55dXGWXeL49kip2QjmKTXJM5L1w5ou81WXS4eXBcXbLxwHnUwZ"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 12:59:54.148)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak54jHQgkvd2QBjPd5diDhFKMZqCbRDGkBreUFuA6p8DFw9esH2TGWmnh9kS5GLJQJg89gbeGPo2TZ7NzXrtStSueTCggVrsBiNYQ6uFRkgKj2wYvmpkvyovuDgaWujNTrpUrnM4MVKJVeCdjwheJ3wHGLQojQz8T9cMZsnMt3rR3Sstu1tBPRtAUsYzeSmGMqj46uR423CqegGR9RRgGMbGyJYi9qKfo4418nZeCxMj3pM4sbYQR4YzwyZYASuV2tpe5YGmNW2Ys5YwBdR3w1w5AGBbdvExPKXxKJCvf3BpKy52z"
  }
}
```

#### initiator <--- (2018-10-24 12:59:54.152)
```javascript
{
  "action": "update",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkqvL7odRAE6AEFM7mhHFqrZG8WRsh7AYAptRJQWGG1SytzH66QwjFmetNAkMxjcAYiTBCbLdKEQBrUif93ybmYTiXRQ1ia8LiZWiuuAeR4v2FDt9BiFWo2yXpUEiARwX2jpBrSbyv8R79iryWfq7Ty9EZG6uFi2Cjfy6HcDqh8JAErtjCfY2aAiaxwbuVHnRDP8GFxfQomonNE9H6bq2cVBiL2oMpLiP7AK3kikSkvDWgjERwssQRwYQfcboo7nZiFYGSCFXL6etneFt9DhNwvPLFrJF4bxFsv8rziwPmArTQzDfmFc2cYoCgLFn7LiJZiqprRwg7RiZxKw32sparENyoekargEZE512ye8Na6gqMq37FfqqVcuU2kghA8LKyY4oD2s9G"
  }
}
```

#### responder <--- (2018-10-24 12:59:54.153)
```javascript
{
  "action": "update",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkqvL7odRAE6AEFM7mhHFqrZG8WRsh7AYAptRJQWGG1SytzH66QwjFmetNAkMxjcAYiTBCbLdKEQBrUif93ybmYTiXRQ1ia8LiZWiuuAeR4v2FDt9BiFWo2yXpUEiARwX2jpBrSbyv8R79iryWfq7Ty9EZG6uFi2Cjfy6HcDqh8JAErtjCfY2aAiaxwbuVHnRDP8GFxfQomonNE9H6bq2cVBiL2oMpLiP7AK3kikSkvDWgjERwssQRwYQfcboo7nZiFYGSCFXL6etneFt9DhNwvPLFrJF4bxFsv8rziwPmArTQzDfmFc2cYoCgLFn7LiJZiqprRwg7RiZxKw32sparENyoekargEZE512ye8Na6gqMq37FfqqVcuU2kghA8LKyY4oD2s9G"
  }
}
```

#### initiator ---> (2018-10-24 12:59:54.156)
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

#### initiator <--- (2018-10-24 12:59:54.157)
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

#### initiator ---> (2018-10-24 12:59:54.236)
```javascript
{
  "action": "shutdown"
}
```

#### initiator <--- (2018-10-24 12:59:54.242)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_2M9ipLgcZAFUF5DNbU7n1xHjMunt3dwmrMH4WaSbCd3CdoJ9oeRKdsExsEs4wj7XynqXgfRNzpK1drhBCFKRTKM4msqHQBjQDUDPPSTZMdrH57qpNiFLy"
  },
  "tag": "shutdown_sign"
}
```

#### initiator ---> (2018-10-24 12:59:54.244)
```javascript
{
  "action": "shutdown_sign",
  "payload": {
    "tx": "tx_2iJcVi27J8ZzEnycVMRD7tkd5YxXjgo53Cq4Q3xcCzsoxjYQexeg1qti4xLLzbNWSBWZ59DjzDqdvEursCAsnn328dNAV8EKExdgZoZzY5SsmUht2Q5PucYzHy2JFYn15Yi4n6CDrxXRV2ttSqH9EbSpbz3XWLqEdEvrQRAcTVAS2r2CDspLHawZx49kxb67719L5JkSnUbfXvwt5CngM1gxth"
  }
}
```

#### responder <--- (2018-10-24 12:59:54.245)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_2M9ipLgcZAFUF5DNbU7n1xHjMunt3dwmrMH4WaSbCd3CdoJ9oeRKdsExsEs4wj7XynqXgfRNzpK1drhBCFKRTKM4msqHQBjQDUDPPSTZMdrH57qpNiFLy"
  },
  "tag": "shutdown_sign_ack"
}
```

#### responder ---> (2018-10-24 12:59:54.246)
```javascript
{
  "action": "shutdown_sign_ack",
  "payload": {
    "tx": "tx_2iJcVi27J8ZyfbRJNsvzNEKPuWFnBvjyMqLCFRVPzGiDwm5UUm3Nx9fHBoNV3nFncWwH4K8QrwjkVQsu5y6F7ao9HssKBkGQFNNuHReaSk3RLrh3DHfhWoCPThcBfJotRR1JHeSX4YCKsttWpswogjh68aoNYSv1JnzcakhCbhTjiegNYuQgiu45eSVoygPbEZvLEda66LW4vz3DjMU82C4yeJ"
  }
}
```

#### responder <--- (2018-10-24 12:59:54.247)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "tx": "tx_3wu1WL1txa1XhCo6eZTksFsqB94xuPBU5CfRD5nnYJqBUuDHrUhtrz5hiAAVBQDNV65ao2CbUxMTxB34notHMknMz61ndoe33p54MhnaXPgd5Xi2phpZDfrccvfEDVcEBPm1NymXuiZxanLxG9LDZtg5vh69dQLpEw1XwjCGiAJuXEmGbC5fiq7ptKQGgXnCdH4mN86vJvQq8R4k1UUxRC1mmu5Du5RyohMPLHGenVWttY7aMZdNbMhsnCvVDkKFZByPxfJZDSAUBns8Ah7uaQJh4rZRPVu7dqzMr8cmEbiKrQPCN6JT"
  }
}
```

#### responder <--- (2018-10-24 12:59:54.248)
```javascript
{
  "action": "info",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "event": "close_mutual"
  }
}
```

#### responder <--- (2018-10-24 12:59:54.248)
```javascript
{
  "action": "info",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "event": "died"
  }
}
```

#### initiator <--- (2018-10-24 12:59:54.252)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "tx": "tx_3wu1WL1txa1XhCo6eZTksFsqB94xuPBU5CfRD5nnYJqBUuDHrUhtrz5hiAAVBQDNV65ao2CbUxMTxB34notHMknMz61ndoe33p54MhnaXPgd5Xi2phpZDfrccvfEDVcEBPm1NymXuiZxanLxG9LDZtg5vh69dQLpEw1XwjCGiAJuXEmGbC5fiq7ptKQGgXnCdH4mN86vJvQq8R4k1UUxRC1mmu5Du5RyohMPLHGenVWttY7aMZdNbMhsnCvVDkKFZByPxfJZDSAUBns8Ah7uaQJh4rZRPVu7dqzMr8cmEbiKrQPCN6JT"
  }
}
```

#### initiator <--- (2018-10-24 12:59:54.253)
```javascript
{
  "action": "info",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "event": "close_mutual"
  }
}
```

#### initiator <--- (2018-10-24 12:59:54.253)
```javascript
{
  "action": "info",
  "channel_id": "ch_e3Vtpq5YJB49YEUFu6jBcChpJFgbNQXF26Qko1xesmTVroFMn",
  "payload": {
    "event": "died"
  }
}
```
