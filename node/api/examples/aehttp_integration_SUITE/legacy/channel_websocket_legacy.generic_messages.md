
#### initiator init (2018-10-24 12:59:27.166)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=initiator
```

#### responder init (2018-10-24 12:59:27.170)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=responder
```

#### responder <--- (2018-10-24 12:59:28.175)
```javascript
{
  "action": "info",
  "payload": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-24 12:59:28.177)
```javascript
{
  "action": "info",
  "payload": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-24 12:59:28.181)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_3d11KjpALm3t32sAMLL9Y5p9SUg9j82o5Er3hc4WTAmdXk3cXjxDydY4eoq6STXDutDQ59tM59bMr9CogemLkb4tUXrrZYvPc4DkdzkXhqGZjnzLVRAYpjMHXUeVmmqr9Fk96GrERRgHqJTaNp7wfhyEnqvb1nHjPyqCUr"
  },
  "tag": "initiator_sign"
}
```

#### initiator ---> (2018-10-24 12:59:28.203)
```javascript
{
  "action": "initiator_sign",
  "payload": {
    "tx": "tx_4L9GSozvM4Hnsco2wV3rJ23VBvhjdW7rXQSRjMtavXVbj27t1PhMCnZvLKSby2MHAUPDbJnpj9BynntKmMKnQGcFCgr6AWupL8Foj2pqC3raypXgSQk5CbFK9W8evi3t9V72UQpDS88Pup4PC1WqatRY13aQVbLhanD1oH48XAaXQ8966bhzbLT2mcBQkfaukjmgesiTRrW8RqfVFYjhHYwUfkgKtXyVSkLyzFV7XDRT5tZQxWE7gkzCqJtQKgvjG48bb14RuDQ"
  }
}
```

#### responder <--- (2018-10-24 12:59:28.204)
```javascript
{
  "action": "info",
  "payload": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-24 12:59:28.205)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_3d11KjpALm3t32sAMLL9Y5p9SUg9j82o5Er3hc4WTAmdXk3cXjxDydY4eoq6STXDutDQ59tM59bMr9CogemLkb4tUXrrZYvPc4DkdzkXhqGZjnzLVRAYpjMHXUeVmmqr9Fk96GrERRgHqJTaNp7wfhyEnqvb1nHjPyqCUr"
  },
  "tag": "responder_sign"
}
```

#### responder ---> (2018-10-24 12:59:28.205)
```javascript
{
  "action": "responder_sign",
  "payload": {
    "tx": "tx_4L9GSozvM4HkhxMhbwsWrDb1NDp4Cr64yGx7pUa2mS9bL8yaBjsbAonoFztfS25GvDqpa5LhBDasFGKErp1Bo1eb5NSKKSubiS21oGrG9DkahiV8Ly26uebm4X5k3QH6AgCEc8q34Ap1ddTn7mugfJPJTuwrcCPPQbbJi8yana4o5UAcJVDFR3YSYL3juYNHVoGfsskx1BesnFdBf3PH8Fc5gz589ys8Acg8p3ixNstFnqnpWXaq9FoAzGw1ErwiTpa6LFM1QaZ"
  }
}
```

#### initiator <--- (2018-10-24 12:59:28.207)
```javascript
{
  "action": "info",
  "payload": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-24 12:59:28.207)
```javascript
{
  "action": "on_chain_tx",
  "payload": {
    "tx": "tx_6jPYBUFTkcmPRQZXJfh3zTScdrj6ySMdsD1uYmPFRc8ir9TPLYeZWLqD3iD5hyYzmEPvaGqWQ8GQvQcAnAKk7HFMmFmQUA4QKSLjYXVUY81NrBhAARv7jY6gffw5bDoiPvqvha9mK5D8yZTUeCZ5RDCwKZACLQ8uf4NHgezGPsuZ9KhBZKaBYeRAK9TqKrXdZdhxkg81xH1u7uNcVPNfpyNEWhG1XE9YVD4ew6gK1rLb1T2QbeRdeDtpTDacanA6ti1d55q1msEeBQj6msEFTxuGbEqcy73cGG6uWDMcPgF4hLyuQ6nDfTGzoMybaMbZr9TuuvrLm5QzY8Gt7CdKiGbovGazmVEEaMtno"
  }
}
```

#### initiator <--- (2018-10-24 12:59:28.208)
```javascript
{
  "action": "on_chain_tx",
  "payload": {
    "tx": "tx_6jPYBUFTkcmPRQZXJfh3zTScdrj6ySMdsD1uYmPFRc8ir9TPLYeZWLqD3iD5hyYzmEPvaGqWQ8GQvQcAnAKk7HFMmFmQUA4QKSLjYXVUY81NrBhAARv7jY6gffw5bDoiPvqvha9mK5D8yZTUeCZ5RDCwKZACLQ8uf4NHgezGPsuZ9KhBZKaBYeRAK9TqKrXdZdhxkg81xH1u7uNcVPNfpyNEWhG1XE9YVD4ew6gK1rLb1T2QbeRdeDtpTDacanA6ti1d55q1msEeBQj6msEFTxuGbEqcy73cGG6uWDMcPgF4hLyuQ6nDfTGzoMybaMbZr9TuuvrLm5QzY8Gt7CdKiGbovGazmVEEaMtno"
  }
}
```

#### initiator ---> (2018-10-24 12:59:31.995)
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

#### initiator <--- (2018-10-24 12:59:31.996)
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

#### initiator <--- (2018-10-24 12:59:38.45)
```javascript
{
  "action": "info",
  "channel_id": "ch_2fKxbDWoB7zCV5Mh5EZoo9SVJTL74Q5Qu9TbtVRP2bANqnmCuC",
  "payload": {
    "event": "own_funding_locked"
  }
}
```

#### responder <--- (2018-10-24 12:59:38.45)
```javascript
{
  "action": "info",
  "channel_id": "ch_2fKxbDWoB7zCV5Mh5EZoo9SVJTL74Q5Qu9TbtVRP2bANqnmCuC",
  "payload": {
    "event": "own_funding_locked"
  }
}
```

#### responder <--- (2018-10-24 12:59:38.46)
```javascript
{
  "action": "info",
  "channel_id": "ch_2fKxbDWoB7zCV5Mh5EZoo9SVJTL74Q5Qu9TbtVRP2bANqnmCuC",
  "payload": {
    "event": "funding_locked"
  }
}
```

#### initiator <--- (2018-10-24 12:59:38.46)
```javascript
{
  "action": "info",
  "channel_id": "ch_2fKxbDWoB7zCV5Mh5EZoo9SVJTL74Q5Qu9TbtVRP2bANqnmCuC",
  "payload": {
    "event": "funding_locked"
  }
}
```

#### responder <--- (2018-10-24 12:59:38.49)
```javascript
{
  "action": "info",
  "channel_id": "ch_2fKxbDWoB7zCV5Mh5EZoo9SVJTL74Q5Qu9TbtVRP2bANqnmCuC",
  "payload": {
    "event": "open"
  }
}
```

#### initiator <--- (2018-10-24 12:59:38.50)
```javascript
{
  "action": "info",
  "channel_id": "ch_2fKxbDWoB7zCV5Mh5EZoo9SVJTL74Q5Qu9TbtVRP2bANqnmCuC",
  "payload": {
    "event": "open"
  }
}
```

#### responder <--- (2018-10-24 12:59:38.50)
```javascript
{
  "action": "update",
  "channel_id": "ch_2fKxbDWoB7zCV5Mh5EZoo9SVJTL74Q5Qu9TbtVRP2bANqnmCuC",
  "payload": {
    "state": "tx_6jPYBUFTkcmPRQZXJfh3zTScdrj6ySMdsD1uYmPFRc8ir9TPLYeZWLqD3iD5hyYzmEPvaGqWQ8GQvQcAnAKk7HFMmFmQUA4QKSLjYXVUY81NrBhAARv7jY6gffw5bDoiPvqvha9mK5D8yZTUeCZ5RDCwKZACLQ8uf4NHgezGPsuZ9KhBZKaBYeRAK9TqKrXdZdhxkg81xH1u7uNcVPNfpyNEWhG1XE9YVD4ew6gK1rLb1T2QbeRdeDtpTDacanA6ti1d55q1msEeBQj6msEFTxuGbEqcy73cGG6uWDMcPgF4hLyuQ6nDfTGzoMybaMbZr9TuuvrLm5QzY8Gt7CdKiGbovGazmVEEaMtno"
  }
}
```

#### initiator <--- (2018-10-24 12:59:38.51)
```javascript
{
  "action": "update",
  "channel_id": "ch_2fKxbDWoB7zCV5Mh5EZoo9SVJTL74Q5Qu9TbtVRP2bANqnmCuC",
  "payload": {
    "state": "tx_6jPYBUFTkcmPRQZXJfh3zTScdrj6ySMdsD1uYmPFRc8ir9TPLYeZWLqD3iD5hyYzmEPvaGqWQ8GQvQcAnAKk7HFMmFmQUA4QKSLjYXVUY81NrBhAARv7jY6gffw5bDoiPvqvha9mK5D8yZTUeCZ5RDCwKZACLQ8uf4NHgezGPsuZ9KhBZKaBYeRAK9TqKrXdZdhxkg81xH1u7uNcVPNfpyNEWhG1XE9YVD4ew6gK1rLb1T2QbeRdeDtpTDacanA6ti1d55q1msEeBQj6msEFTxuGbEqcy73cGG6uWDMcPgF4hLyuQ6nDfTGzoMybaMbZr9TuuvrLm5QzY8Gt7CdKiGbovGazmVEEaMtno"
  }
}
```

#### initiator: (2018-10-24 12:59:39.121)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-24 12:59:39.121)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-24 12:59:39.121)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-24 12:59:39.121)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-24 12:59:39.121)
> Channel is `open` and ready to use

#### responder: (2018-10-24 12:59:39.121)
> Channel is `open` and ready to use

#### initiator ---> (2018-10-24 12:59:39.150)
```javascript
{
  "action": "message",
  "payload": {
    "info": "hejsan",
    "to": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt"
  }
}
```

#### responder <--- (2018-10-24 12:59:39.151)
```javascript
{
  "action": "message",
  "channel_id": "ch_2fKxbDWoB7zCV5Mh5EZoo9SVJTL74Q5Qu9TbtVRP2bANqnmCuC",
  "payload": {
    "message": {
      "channel_id": "ch_2fKxbDWoB7zCV5Mh5EZoo9SVJTL74Q5Qu9TbtVRP2bANqnmCuC",
      "from": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
      "info": "hejsan",
      "to": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt"
    }
  }
}
```

#### responder ---> (2018-10-24 12:59:39.152)
```javascript
{
  "action": "message",
  "payload": {
    "info": "svejsan",
    "to": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
  }
}
```

#### initiator <--- (2018-10-24 12:59:39.153)
```javascript
{
  "action": "message",
  "channel_id": "ch_2fKxbDWoB7zCV5Mh5EZoo9SVJTL74Q5Qu9TbtVRP2bANqnmCuC",
  "payload": {
    "message": {
      "channel_id": "ch_2fKxbDWoB7zCV5Mh5EZoo9SVJTL74Q5Qu9TbtVRP2bANqnmCuC",
      "from": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "info": "svejsan",
      "to": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
    }
  }
}
```

#### initiator ---> (2018-10-24 12:59:39.154)
```javascript
{
  "action": "message",
  "payload": {
    "info": "first message in a row",
    "to": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt"
  }
}
```

#### responder <--- (2018-10-24 12:59:39.155)
```javascript
{
  "action": "message",
  "channel_id": "ch_2fKxbDWoB7zCV5Mh5EZoo9SVJTL74Q5Qu9TbtVRP2bANqnmCuC",
  "payload": {
    "message": {
      "channel_id": "ch_2fKxbDWoB7zCV5Mh5EZoo9SVJTL74Q5Qu9TbtVRP2bANqnmCuC",
      "from": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
      "info": "first message in a row",
      "to": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt"
    }
  }
}
```

#### initiator ---> (2018-10-24 12:59:39.156)
```javascript
{
  "action": "message",
  "payload": {
    "info": "second message in a row",
    "to": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt"
  }
}
```

#### responder <--- (2018-10-24 12:59:39.199)
```javascript
{
  "action": "message",
  "channel_id": "ch_2fKxbDWoB7zCV5Mh5EZoo9SVJTL74Q5Qu9TbtVRP2bANqnmCuC",
  "payload": {
    "message": {
      "channel_id": "ch_2fKxbDWoB7zCV5Mh5EZoo9SVJTL74Q5Qu9TbtVRP2bANqnmCuC",
      "from": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
      "info": "second message in a row",
      "to": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt"
    }
  }
}
```

#### responder ---> (2018-10-24 12:59:39.201)
```javascript
{
  "action": "message",
  "payload": {
    "info": "some message",
    "to": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
  }
}
```

#### initiator <--- (2018-10-24 12:59:39.206)
```javascript
{
  "action": "message",
  "channel_id": "ch_2fKxbDWoB7zCV5Mh5EZoo9SVJTL74Q5Qu9TbtVRP2bANqnmCuC",
  "payload": {
    "message": {
      "channel_id": "ch_2fKxbDWoB7zCV5Mh5EZoo9SVJTL74Q5Qu9TbtVRP2bANqnmCuC",
      "from": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "info": "some message",
      "to": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
    }
  }
}
```

#### responder ---> (2018-10-24 12:59:39.207)
```javascript
{
  "action": "message",
  "payload": {
    "info": "other message",
    "to": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
  }
}
```

#### initiator <--- (2018-10-24 12:59:39.249)
```javascript
{
  "action": "message",
  "channel_id": "ch_2fKxbDWoB7zCV5Mh5EZoo9SVJTL74Q5Qu9TbtVRP2bANqnmCuC",
  "payload": {
    "message": {
      "channel_id": "ch_2fKxbDWoB7zCV5Mh5EZoo9SVJTL74Q5Qu9TbtVRP2bANqnmCuC",
      "from": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "info": "other message",
      "to": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
    }
  }
}
```
