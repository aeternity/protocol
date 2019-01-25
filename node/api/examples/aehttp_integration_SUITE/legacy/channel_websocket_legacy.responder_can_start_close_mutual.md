
#### initiator init (2018-10-24 12:59:55.4)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=initiator
```

#### responder init (2018-10-24 12:59:55.8)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=responder
```

#### responder <--- (2018-10-24 12:59:56.11)
```javascript
{
  "action": "info",
  "payload": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-24 12:59:56.12)
```javascript
{
  "action": "info",
  "payload": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-24 12:59:56.16)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_3d11KjpALm3t32sAMLL9Y5p9SUg9j82o5Er3hc4WTAmdXk3cXjxDydY4eoq6STXDutDQ59tM59bMr9CogemLkb4tUXrrZYvPc4DkdzkXhqGZjnzLVRAYpjMHXUeVmmqr9Fk96GrERRgHqJTaNp7wfhyEnqvb1nHjpsjHZL"
  },
  "tag": "initiator_sign"
}
```

#### initiator ---> (2018-10-24 12:59:56.37)
```javascript
{
  "action": "initiator_sign",
  "payload": {
    "tx": "tx_4L9GSozvM4HnX1wYoKyoTLxFZ8YA4UiTj2smv4bkoXFf4hytuSWDQQK1ADTQXaR9Ba8tDr2EZaEVYXCg6tAWL8MQtirm3eaYXV9MFwcnNVH5KAejukZu9XqpkbTtgpu9cRcKY8nb1yTX5riuhzgqVGCM4uSPUsXkogwa14KRwcFcvSzXvNwH7nh4Mf9AznKXYus7CcePuJ7jUGzBwuaZaN92obpDw61jdiLWqf3bbzsgfTDnyygGde2QZckUvvSVLdeuPQ6x8ta"
  }
}
```

#### responder <--- (2018-10-24 12:59:56.38)
```javascript
{
  "action": "info",
  "payload": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-24 12:59:56.38)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_3d11KjpALm3t32sAMLL9Y5p9SUg9j82o5Er3hc4WTAmdXk3cXjxDydY4eoq6STXDutDQ59tM59bMr9CogemLkb4tUXrrZYvPc4DkdzkXhqGZjnzLVRAYpjMHXUeVmmqr9Fk96GrERRgHqJTaNp7wfhyEnqvb1nHjpsjHZL"
  },
  "tag": "responder_sign"
}
```

#### responder ---> (2018-10-24 12:59:56.39)
```javascript
{
  "action": "responder_sign",
  "payload": {
    "tx": "tx_4L9GSozvM4Hn8TEPtzBwAeXSb8WcQSjgrmDUxzMmGWPaookxUAQACmgHHRzn64tgRGzntTp1J9XsrqQ3VdMPGWsw6N3k3Fnqr5W4BRmuy6cwid9AzUJSDDG5ReaFui8qRjBBYUR9BvtN4fm26Ue4Yg3saEMySUHi7b2yPAvya6qnVTw2HEVSuw93KBFCekquBFxFREsQGcGZVNDDTY8oPt74cxMsuExi8P2HYatc9tAWun1djwifNs6fhhU7iNDzziUKD2oq8GR"
  }
}
```

#### initiator <--- (2018-10-24 12:59:56.40)
```javascript
{
  "action": "info",
  "payload": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-24 12:59:56.41)
```javascript
{
  "action": "on_chain_tx",
  "payload": {
    "tx": "tx_6jPYBUFTkcmRsEZdMjuFoiPcX3oE6azo8PHaaojxXa9hgNNAGwX782c5xTPDot1fBcBBsr2qHjmTpxJ41iLHVE8WMYQJG7GZNbiTSBcd51udtxUnv5NJWQccJxW2gSNcvfAX8US6TnZxyHz335TuRiX8beP7qz5nQMYhMooJUBykhLeFUeqthQFLjgDPp7jUVxWFMXJcLKK8e871UTfLLn1ofYsyZmBFMWKaZPtQWnK2rhPXVM6Phyt3chG5np88wuEZjSgzfsjf3QaKWjGZUM3WqNR5AwZkgtCA7ReePpbMZPTBwvNopRgtEUWrq7riS6W1ZMmryiztQLSZWksLSczTUrfUfUjfT6ob4"
  }
}
```

#### initiator <--- (2018-10-24 12:59:56.42)
```javascript
{
  "action": "on_chain_tx",
  "payload": {
    "tx": "tx_6jPYBUFTkcmRsEZdMjuFoiPcX3oE6azo8PHaaojxXa9hgNNAGwX782c5xTPDot1fBcBBsr2qHjmTpxJ41iLHVE8WMYQJG7GZNbiTSBcd51udtxUnv5NJWQccJxW2gSNcvfAX8US6TnZxyHz335TuRiX8beP7qz5nQMYhMooJUBykhLeFUeqthQFLjgDPp7jUVxWFMXJcLKK8e871UTfLLn1ofYsyZmBFMWKaZPtQWnK2rhPXVM6Phyt3chG5np88wuEZjSgzfsjf3QaKWjGZUM3WqNR5AwZkgtCA7ReePpbMZPTBwvNopRgtEUWrq7riS6W1ZMmryiztQLSZWksLSczTUrfUfUjfT6ob4"
  }
}
```

#### initiator ---> (2018-10-24 12:59:59.315)
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

#### initiator <--- (2018-10-24 12:59:59.318)
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

#### responder <--- (2018-10-24 13:00:04.767)
```javascript
{
  "action": "info",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "event": "own_funding_locked"
  }
}
```

#### initiator <--- (2018-10-24 13:00:04.768)
```javascript
{
  "action": "info",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "event": "own_funding_locked"
  }
}
```

#### initiator <--- (2018-10-24 13:00:04.768)
```javascript
{
  "action": "info",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "event": "funding_locked"
  }
}
```

#### responder <--- (2018-10-24 13:00:04.769)
```javascript
{
  "action": "info",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "event": "funding_locked"
  }
}
```

#### initiator <--- (2018-10-24 13:00:04.772)
```javascript
{
  "action": "info",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "event": "open"
  }
}
```

#### responder <--- (2018-10-24 13:00:04.773)
```javascript
{
  "action": "info",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "event": "open"
  }
}
```

#### initiator <--- (2018-10-24 13:00:04.774)
```javascript
{
  "action": "update",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "state": "tx_6jPYBUFTkcmRsEZdMjuFoiPcX3oE6azo8PHaaojxXa9hgNNAGwX782c5xTPDot1fBcBBsr2qHjmTpxJ41iLHVE8WMYQJG7GZNbiTSBcd51udtxUnv5NJWQccJxW2gSNcvfAX8US6TnZxyHz335TuRiX8beP7qz5nQMYhMooJUBykhLeFUeqthQFLjgDPp7jUVxWFMXJcLKK8e871UTfLLn1ofYsyZmBFMWKaZPtQWnK2rhPXVM6Phyt3chG5np88wuEZjSgzfsjf3QaKWjGZUM3WqNR5AwZkgtCA7ReePpbMZPTBwvNopRgtEUWrq7riS6W1ZMmryiztQLSZWksLSczTUrfUfUjfT6ob4"
  }
}
```

#### responder <--- (2018-10-24 13:00:04.774)
```javascript
{
  "action": "update",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "state": "tx_6jPYBUFTkcmRsEZdMjuFoiPcX3oE6azo8PHaaojxXa9hgNNAGwX782c5xTPDot1fBcBBsr2qHjmTpxJ41iLHVE8WMYQJG7GZNbiTSBcd51udtxUnv5NJWQccJxW2gSNcvfAX8US6TnZxyHz335TuRiX8beP7qz5nQMYhMooJUBykhLeFUeqthQFLjgDPp7jUVxWFMXJcLKK8e871UTfLLn1ofYsyZmBFMWKaZPtQWnK2rhPXVM6Phyt3chG5np88wuEZjSgzfsjf3QaKWjGZUM3WqNR5AwZkgtCA7ReePpbMZPTBwvNopRgtEUWrq7riS6W1ZMmryiztQLSZWksLSczTUrfUfUjfT6ob4"
  }
}
```

#### initiator: (2018-10-24 13:00:05.482)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-24 13:00:05.482)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-24 13:00:05.482)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-24 13:00:05.482)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-24 13:00:05.482)
> Channel is `open` and ready to use

#### responder: (2018-10-24 13:00:05.482)
> Channel is `open` and ready to use

#### initiator ---> (2018-10-24 13:00:05.529)
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

#### initiator <--- (2018-10-24 13:00:05.533)
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

#### initiator ---> (2018-10-24 13:00:05.535)
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

#### initiator <--- (2018-10-24 13:00:05.545)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQT2xKHAbEbspK1rggJxrFTGsRx7WMKDKX3iVnieu3P1Gydo3Y4TdewG3Zwgus5MPhoKQ2YxZsJwn9Ptg2z3GDJ9L2AzWiwEGcsPotig7Q6N91EYX7mj7dfyioMybrARQZvDRaAaMArZ3C7SMY9VwYyn9EKY3NJcsb2u5cmvUfsuuesWJFQ6Shm32mR42EjEQuqWmtB6JL394J"
  },
  "tag": "update"
}
```

#### initiator ---> (2018-10-24 13:00:05.547)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4q2o5BwAXpnYuLnp5JEMcgeHrke1CVuNnaC5dKEEMzVWNu415gk1r4uQy7rEXTddumov1q2bnAKY7gbNjax7v1kA7hDuXjqaVbirkZnvuH1CiudtfxJf9uozpuDSeV6xct8Tfu7qbwxpQCEVfJxWYPLjAdCbD9kT41wrBquhToHffkv2Fcsbxbz6dSB2kwUZxBcKx4Qy4Hmp9A9uJzoAr3EyniyLYcq77MZHg3njM4prmd3BAmEibWZViUXvarH71agehnFLJoCtYcZ1Apt228RTbFYARL8BaWPwTRHAbvcDJGd"
  }
}
```

#### responder <--- (2018-10-24 13:00:05.552)
```javascript
{
  "action": "info",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "event": "update"
  }
}
```

#### responder <--- (2018-10-24 13:00:05.553)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQT2xKHAbEbspK1rggJxrFTGsRx7WMKDKX3iVnieu3P1Gydo3Y4TdewG3Zwgus5MPhoKQ2YxZsJwn9Ptg2z3GDJ9L2AzWiwEGcsPotig7Q6N91EYX7mj7dfyioMybrARQZvDRaAaMArZ3C7SMY9VwYyn9EKY3NJcsb2u5cmvUfsuuesWJFQ6Shm32mR42EjEQuqWmtB6JL394J"
  },
  "tag": "update_ack"
}
```

#### responder ---> (2018-10-24 13:00:05.554)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak55bmgpyWgofkkPQZhxbUPNM1ccVutwSxvwMzgma2sLMAFq5pxdGonsSzj7YFgChdT5FpSADkEJvtDrDvdMSVWSWPJRvXdJqXUo2tcNq782Udt1ZYo9xWtbsWJqM9o9StM43Q6CnaiopgtGdheherPhXknFbZxmNNFwS3ATQhMEw2UCUwYDpBmRGNuT5R62iQhPRNrb5XDjZLEezavdj4SX9d4PBuGh5zzxjETwP98e2tSVncrmmCwjXryq9SsPvSQVdSuTkqt2RbKhpcTB6mVApF98bS9bwQvYYkoouds7JRC7t"
  }
}
```

#### responder <--- (2018-10-24 13:00:05.559)
```javascript
{
  "action": "update",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkT8tDuU5QdvDoJ66CrH4NumT5r7QAmmcPRgm6SF1GxioaKix4ZZakv1J9djL7JN1sf3MZaMCz7UA2j6Z5JC3Nosd2reK6r77qWatRXE5HJMgZc61eK51ctVNicngMWdUarXLVvbYDm4PmLw4pG3HsB79mmzDCdQbEYy72gU9ZCApgHhNXNonfyXLBMVGEJjwyP5f42MB6BYHCXqW11ABrYR3UUDMLCkFy3r1P8i671VdK161JWh4prMMEfLNCqcZgKd1Ya7g2ZAibiYwUFWYajAbFMDjLkdXiXMSoMHYJBEPA2M1WwQQGpZaz7xYGdNyw54EBazBnKZg3zwSXCRm13Ffw3hAS7J81ccSdohp7Fw4LbqZVxscEzELTZD2VadyMF6DeA9Dt"
  }
}
```

#### initiator <--- (2018-10-24 13:00:05.560)
```javascript
{
  "action": "update",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkT8tDuU5QdvDoJ66CrH4NumT5r7QAmmcPRgm6SF1GxioaKix4ZZakv1J9djL7JN1sf3MZaMCz7UA2j6Z5JC3Nosd2reK6r77qWatRXE5HJMgZc61eK51ctVNicngMWdUarXLVvbYDm4PmLw4pG3HsB79mmzDCdQbEYy72gU9ZCApgHhNXNonfyXLBMVGEJjwyP5f42MB6BYHCXqW11ABrYR3UUDMLCkFy3r1P8i671VdK161JWh4prMMEfLNCqcZgKd1Ya7g2ZAibiYwUFWYajAbFMDjLkdXiXMSoMHYJBEPA2M1WwQQGpZaz7xYGdNyw54EBazBnKZg3zwSXCRm13Ffw3hAS7J81ccSdohp7Fw4LbqZVxscEzELTZD2VadyMF6DeA9Dt"
  }
}
```

#### initiator ---> (2018-10-24 13:00:05.563)
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

#### initiator <--- (2018-10-24 13:00:05.564)
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

#### initiator ---> (2018-10-24 13:00:05.564)
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

#### initiator <--- (2018-10-24 13:00:05.565)
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

#### responder ---> (2018-10-24 13:00:05.565)
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

#### responder <--- (2018-10-24 13:00:05.568)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQT2xKHAbEbspK1rggJxrFTGsRx7WMKDKX3iVnieu3P1GydtU3v1B88bmVhgSyyUUBqgZ1FQ7EWKJVQE7hWqfTMFBRanL1AQ1WVT38fXZsg2DGCZpHf77MvUMZUAjuDBqB7mnR5chD6GetSqg5Ey3inan12odRgz5Wm4jHy9GhJnyytwrtmFExHfVHmhSk9fRQA7VGHAD9JyME"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 13:00:05.569)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4pVaW6tHQsGaeqzrFNFh7fTp7xc5P7ShYAxthAnitRCBhqb9WHgJMUTBkqNJ2QTgU3ou5Wiqt2RFw8GWumg2uQejKsTXqLfF12LNeLxm75uPbTdNvFrhF2v1NF7f7UcDnJJYruVZknfFDwmLKcmMkiLNT6Tm5WQ5QXpF39hdu45pcoW2p7cuD3sYPe5ehWjaqXWVBZgy8Fs8RFCpFirAmy4ofsJNwM5byCKkE99Hd9vazk1GbAqtQoiwnPTNpWLNZippwWqh4eEdm3wZyAjaaFkubL5sHkdeCSWnEqST6GTDdBD"
  }
}
```

#### initiator <--- (2018-10-24 13:00:05.608)
```javascript
{
  "action": "info",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 13:00:05.610)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQT2xKHAbEbspK1rggJxrFTGsRx7WMKDKX3iVnieu3P1GydtU3v1B88bmVhgSyyUUBqgZ1FQ7EWKJVQE7hWqfTMFBRanL1AQ1WVT38fXZsg2DGCZpHf77MvUMZUAjuDBqB7mnR5chD6GetSqg5Ey3inan12odRgz5Wm4jHy9GhJnyytwrtmFExHfVHmhSk9fRQA7VGHAD9JyME"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 13:00:05.612)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak5CDc9NvdxCbsXbTbustMm4fas3SEWkPgazoqRo2q5xn93GRTzDXn14KX3tySk9SqkHSWm7eCv81yYCYjzzDp6HiVxh3JfyUPN2gW66HpmiqMr9LyoJ83iYynPGzkXQMfhaigbeTqCpA7N4vYhQWmUEFnjui2wFhtEdEAXd419d6VyoUbTzcDEnnBKwhAeDBRu4zeSeJMLb3oCBLWfoC7nRcEwcyNFUBY6vZDagVNVC9o7ZmLXDMA9WmMpx6FAshPRU1wvfNBEPaYDQ7m2EWHUvb3EgzXWbRNJJ7qbfDeSdb5WPm"
  }
}
```

#### initiator <--- (2018-10-24 13:00:05.625)
```javascript
{
  "action": "update",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkSDDYn7Gd46FyLR59aPbJgACy3jeeVhVUpkoo6yyhycFHcCZKLUhqPL7DB65Sr2RLwUxApcgmf6b8fC6KnPE69yUimhQT7zVV6Rx7Xj5L4NzixcdnA1eKJZYhuy78cUCcysEJWYDwj6jNV4Hx2N3dpjuQwUZGShkSnmTJTobJLERQBCNqd9Y8Wyt333yTMyJb4vCjtd7XEwptiknvMiyV5us7iX8sjRirCTJqwLa5ggBrmw53QjTehCpEafHbVDFx1kwptrhVPWiKYXuyyxZ9DGcDRU6gp8p6tiTByeRtr8RDL2XA1WXgfBNMrPNfesDgMqhtVbeoWZXPGqbMY8mPBEA5pg8yQpXmAaSYHcFtSyg1bh1oU6TfTSV1naauQYcJktQP2Cw9"
  }
}
```

#### responder <--- (2018-10-24 13:00:05.627)
```javascript
{
  "action": "update",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkSDDYn7Gd46FyLR59aPbJgACy3jeeVhVUpkoo6yyhycFHcCZKLUhqPL7DB65Sr2RLwUxApcgmf6b8fC6KnPE69yUimhQT7zVV6Rx7Xj5L4NzixcdnA1eKJZYhuy78cUCcysEJWYDwj6jNV4Hx2N3dpjuQwUZGShkSnmTJTobJLERQBCNqd9Y8Wyt333yTMyJb4vCjtd7XEwptiknvMiyV5us7iX8sjRirCTJqwLa5ggBrmw53QjTehCpEafHbVDFx1kwptrhVPWiKYXuyyxZ9DGcDRU6gp8p6tiTByeRtr8RDL2XA1WXgfBNMrPNfesDgMqhtVbeoWZXPGqbMY8mPBEA5pg8yQpXmAaSYHcFtSyg1bh1oU6TfTSV1naauQYcJktQP2Cw9"
  }
}
```

#### initiator ---> (2018-10-24 13:00:05.633)
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

#### initiator <--- (2018-10-24 13:00:05.635)
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

#### initiator ---> (2018-10-24 13:00:05.636)
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

#### initiator <--- (2018-10-24 13:00:05.637)
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

#### responder ---> (2018-10-24 13:00:05.637)
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

#### responder <--- (2018-10-24 13:00:05.642)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQT2xKHAbEbspK1rggJxrFTGsRx7WMKDKX3iVnieu3P1GydytZmYibKwVRTfz6sbKBcz5joqgJV1CcpH1KSKR95znT53k7qFNm9PnHkyGfQoJMtCmvAARnoiyVkbKbvShq3mujJZZ8fqNJ8DAKdL19HB3FLUBW9a9vCnNLjNMpbZYZLyzCNfsXogvMYygv9PCU6513uzAayNMJ"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 13:00:05.643)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak5C4SyCw2dU6ePmLsoXai8YRH5tfJPyRxBKVPi25i2AtJZtZxvTBpfwXGKPGjpzcft7xwJFRmHnKzkomtpAokFXQK1VWK6vZt55rgsmojK2sKeCagvEjRiE6AR5KD3TD6o82Hjp2jYUTeRLuooD7RY9rGPXWTrPbEBqMdzZ3NeCbyDwqL32YtDp8LfTiCseM8JgyexLujbCaqydSdasAtDBsp4F2Muaufiex3scX8QpN9rTFWswcXXVat9CMmaPdiWtSViAiLKBXmNtinSxPGWcXs4r3FDqQyUdSKv9v2h4bWvBF"
  }
}
```

#### initiator <--- (2018-10-24 13:00:05.647)
```javascript
{
  "action": "info",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 13:00:05.648)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQT2xKHAbEbspK1rggJxrFTGsRx7WMKDKX3iVnieu3P1GydytZmYibKwVRTfz6sbKBcz5joqgJV1CcpH1KSKR95znT53k7qFNm9PnHkyGfQoJMtCmvAARnoiyVkbKbvShq3mujJZZ8fqNJ8DAKdL19HB3FLUBW9a9vCnNLjNMpbZYZLyzCNfsXogvMYygv9PCU6513uzAayNMJ"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 13:00:05.649)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak4oG9PQ9zYyWyCxyTQokb64GeexZEcunQrsz2z1cJpiLdy25pHLZ8yGCSbe76EH64DUBPaoqxCgQ9d3PvTgT6UQp8tHJCBhrruk93M4ekAVKNwQGruZvUxU7eMEaEwZY9UugnSaGh9kwcP2mxfq3pWR18yxtWZjyrTTSRYbyKd96GpBipsAEWG8oXMSNa6jfEAPdEgz1KJ9g5G8QpEMp9eZJJEmpx5ZjsQPQTUUKPvTAKaCd6Jc8Bq2JYYzpMJwmmsqsoPPXrUXczAaGc1Ko3u5XxMF6eQu728hVckQzEGzLfp4T"
  }
}
```

#### initiator <--- (2018-10-24 13:00:05.654)
```javascript
{
  "action": "update",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkQ6QqXbY1EHRLp9dbYKhiWUGpUfxLBb3TiGfr3aAxPd6stkBQJ95c2XedKejE1qtQQZxYQ4xZwnzS9PDpZ5ZTwYC1qyVGKrp9hpH3daiHcjE7sEKZnkZhiV6uPhQjkGdyfX2772jo6Uu8CeGVTjNs9Yhtt6JCNgP7PtuavF6YUTRoYEeF7LUygNTKbxCd1cwXNHD9rKvrVGXbiAY3zoC82SrxdeL9QRVuUQt6zVARP3qVPjYJ8PK6oCmYdTkWuoBi1aAG2b9Rrca471Kb3HcsoqJNbHhpPiaP7EBtKnS9VbEca5Lu83ch3Xb2PsrHkgc24RoBzpVXUcgj4MzZtQY5cMM6vpPiCE3iXkThWvecX4Yxw4ctmNTd3Cq56GPAAwVefM3tu4CC"
  }
}
```

#### responder <--- (2018-10-24 13:00:05.654)
```javascript
{
  "action": "update",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkQ6QqXbY1EHRLp9dbYKhiWUGpUfxLBb3TiGfr3aAxPd6stkBQJ95c2XedKejE1qtQQZxYQ4xZwnzS9PDpZ5ZTwYC1qyVGKrp9hpH3daiHcjE7sEKZnkZhiV6uPhQjkGdyfX2772jo6Uu8CeGVTjNs9Yhtt6JCNgP7PtuavF6YUTRoYEeF7LUygNTKbxCd1cwXNHD9rKvrVGXbiAY3zoC82SrxdeL9QRVuUQt6zVARP3qVPjYJ8PK6oCmYdTkWuoBi1aAG2b9Rrca471Kb3HcsoqJNbHhpPiaP7EBtKnS9VbEca5Lu83ch3Xb2PsrHkgc24RoBzpVXUcgj4MzZtQY5cMM6vpPiCE3iXkThWvecX4Yxw4ctmNTd3Cq56GPAAwVefM3tu4CC"
  }
}
```

#### initiator ---> (2018-10-24 13:00:05.657)
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

#### initiator <--- (2018-10-24 13:00:05.657)
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

#### initiator ---> (2018-10-24 13:00:05.658)
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

#### initiator <--- (2018-10-24 13:00:05.659)
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

#### initiator ---> (2018-10-24 13:00:05.659)
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

#### initiator <--- (2018-10-24 13:00:05.662)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQT2xKHAbEbspK1rggJxrFTGsRx7WMKDKX3iVnieu3P1Gye5K5d6G4XHDMDfXDmhvh9DzEEHH5F1UXe3LtkUXGWQ96dnm4wnNNqE3N11DmJhQJHTQ1Gu4vKjacDFLxJC2XiDoWqQvwbFBR9YpHJaopTYvyEXedPiFzSmTQyADxGMqBCX1mXveqkwYac1A1paHo9cwBpC2NQbKV"
  },
  "tag": "update"
}
```

#### initiator ---> (2018-10-24 13:00:05.662)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak52H5Dz86UW8njW9EK2im1cN8gpPmMkaybWVpVjNMkFzpMdWwuPNo3VukZ3Znyb44TttatMVZmokisiLqqmyo5J1wKJ1Gah8MMtmrEbauKEzPjxBR85fozicbHC62NE3qAJx1HbqfjsrgRAgDaNPWE5KtAoCTuBHx27sJcjvzD8sUqcPtaa2KvUdgAZD8CNLx3a1qkpFXEAYnFR4pizL1GUifoX26s95w5VTrjfYQSQBUxrZC6edEikSKy7Asqy2orHFDqZEnddVt81dfJrVNmx3wjRxMDg4o5vEUTEKYmpEfB7d"
  }
}
```

#### responder <--- (2018-10-24 13:00:05.700)
```javascript
{
  "action": "info",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "event": "update"
  }
}
```

#### responder <--- (2018-10-24 13:00:05.701)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQT2xKHAbEbspK1rggJxrFTGsRx7WMKDKX3iVnieu3P1Gye5K5d6G4XHDMDfXDmhvh9DzEEHH5F1UXe3LtkUXGWQ96dnm4wnNNqE3N11DmJhQJHTQ1Gu4vKjacDFLxJC2XiDoWqQvwbFBR9YpHJaopTYvyEXedPiFzSmTQyADxGMqBCX1mXveqkwYac1A1paHo9cwBpC2NQbKV"
  },
  "tag": "update_ack"
}
```

#### responder ---> (2018-10-24 13:00:05.704)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak54RAga6wzTcFfCYX1KEKi35Mcs1Z8qSQUAVuQykxR2Yh5RjBbbYBzLwnn19ut7BKpG71fN4UDJ87ytDx1ZaaSR2uUQgXcGAahFkoBDsB6rdPVaGNvrLv4dmvPMKaEDtfEV8QMfSgkQnKpoKQar98LeyiiAidFRbSMTUZKiNc2iNSmJVzAiBbjzCVRoEQEoYo5v4kqjA4HKAtv8QYcc7hD9PDY4U2ZsSsh4Aq9XKmkKEgcnY5PuNnwLfpsqbEnYxjDo1C4YYKRQkCdLv9nU2vqT3u4dg5KvYVEBxv8PA7xJS8Wrm"
  }
}
```

#### responder <--- (2018-10-24 13:00:05.717)
```javascript
{
  "action": "update",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "state": "tx_3XPhV5wAjiGDknUG3UapBEXHCvDdDom6r4fnCD8Lf1gTJKqh7RJiXHaR4fsYQt6y1Lt9fmcHppGzjQVb5YM5guHhb3UekFmSGBhc6Aqpmmaq54aQhUGGHvKbJkL98VZcYxmLE3UiZyxsPNvRbGsfoT7aQgjyZiqVaxdDKe2Wnh9DTKrRMbm2gp3Qe8cRTJjZ172iohsrfDe1LifBSbdCSTsESNsFsy1BAbLh1G96yH7RNPmjvjdXrVfWBgUBRyJ8YeMSkDNL79C7AzKYYMYJdy9r1bpCTym798AaL4vAiQnSRNufBBNha34WE3ebWPFzLkeiTaHDV5JNN5XvyFCEintd56QBGnVVEWavFhdBj8vuHHSGxQXrh1fs48GsSfn4AiAqEcvXk9d6vdohDnodB"
  }
}
```

#### initiator <--- (2018-10-24 13:00:05.719)
```javascript
{
  "action": "update",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "state": "tx_3XPhV5wAjiGDknUG3UapBEXHCvDdDom6r4fnCD8Lf1gTJKqh7RJiXHaR4fsYQt6y1Lt9fmcHppGzjQVb5YM5guHhb3UekFmSGBhc6Aqpmmaq54aQhUGGHvKbJkL98VZcYxmLE3UiZyxsPNvRbGsfoT7aQgjyZiqVaxdDKe2Wnh9DTKrRMbm2gp3Qe8cRTJjZ172iohsrfDe1LifBSbdCSTsESNsFsy1BAbLh1G96yH7RNPmjvjdXrVfWBgUBRyJ8YeMSkDNL79C7AzKYYMYJdy9r1bpCTym798AaL4vAiQnSRNufBBNha34WE3ebWPFzLkeiTaHDV5JNN5XvyFCEintd56QBGnVVEWavFhdBj8vuHHSGxQXrh1fs48GsSfn4AiAqEcvXk9d6vdohDnodB"
  }
}
```

#### initiator ---> (2018-10-24 13:00:05.724)
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

#### initiator <--- (2018-10-24 13:00:05.725)
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

#### initiator ---> (2018-10-24 13:00:05.726)
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

#### initiator <--- (2018-10-24 13:00:05.727)
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

#### responder ---> (2018-10-24 13:00:05.728)
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

#### responder <--- (2018-10-24 13:00:05.732)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQT2xKHAbEbspK1rggJxrFTGsRx7WMKDKX3iVnieu3P1GyeAjbUdoXicwGyf4Lfq1BBb9CvipSSNzseNnZHGvWZVzW3aaMAx7GTHGbwrgEtMUZFUhBAH4eaEDNKSV1LxT8unAMkTGypxo7Ux8pQ3uzGMZjwoFiozugVrUW4qGqiH4JBJJi28J4eZMmMPcu5os3u7zzHezB2NGi"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 13:00:05.733)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4q8hYfhmd8Ava7euUiW8TkLm5HrnVNhae1WkvhjLd3x3guocVLRXpLyUQE36jgqDuSm1Ed6RvyZiJKCP9KqoiXQDFWGKBpEUKazqt95KEJPy3DbvqU9NityLykjbyzPodtazGqAzBynn18BQnmdV6LS5V2WeowSUp2g3uSyXksuW8HJfM96o8UMV2EpCEpVKDQF6NH545shs5eEng6bQ2UdjYpKirBfrNEfkmm9VXBjXtjBKoaXBPCBMNdRKQe6haPFRBkRe89KAASNeYTb7y68i3nFnmuytdSNnLdUJ1XPKku4"
  }
}
```

#### initiator <--- (2018-10-24 13:00:05.757)
```javascript
{
  "action": "info",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 13:00:05.759)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQT2xKHAbEbspK1rggJxrFTGsRx7WMKDKX3iVnieu3P1GyeAjbUdoXicwGyf4Lfq1BBb9CvipSSNzseNnZHGvWZVzW3aaMAx7GTHGbwrgEtMUZFUhBAH4eaEDNKSV1LxT8unAMkTGypxo7Ux8pQ3uzGMZjwoFiozugVrUW4qGqiH4JBJJi28J4eZMmMPcu5os3u7zzHezB2NGi"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 13:00:05.761)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak4kd5NkUURjTWxQxosusVSnPZsfk3kEkRhqUcWSKbCgwDTBbhVzvKcGqTRhxM12TgVLgTXphAfj42rC5NDspm3FR6F15yTT2Fx7ze5rNGHRUK2Qq91Z7QUfFcjThFQETmggLx8GNWuKGCMC6UQAwCGtnp8XzesyPLdKTi3jcJdbqHocEoe3jyw8yoHNknw6MksepjGegkRJ23ZiUjBYr9L2UnDfw3HBW3LxvnQ5pKJJ2431aAmevb95mnyfuAXuJczpwCtKkdV5PNFiRMeH5n2ijZ92xrXVqZHGTyw5Uep8UACPJ"
  }
}
```

#### initiator <--- (2018-10-24 13:00:05.770)
```javascript
{
  "action": "update",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkKZG3cA4HCjFSK8Snd3dzddNzmgvVPRzG6hKbGhH5YEjG99tiJ7JRi6jhBG661Qc652FNtQPtt9o9JfsuyHErg7Wz8xGTKd9FiAiLPCqEMZ9F8HYtK3p2W7LC5xeRWLkLGFUX2uF1ZKtAcTwqVABespW2CrkjkTupEANQ6MkrhRFdsK8VYZxd5D4uC6hN5DsT4d7hMqbNXwDFtUGDFXgmk1vtsVFKgouoR7H1ioXPaJoxyi7WjJZ1UQv6M9HrNCGuBGsu2JKg6uAefm42NkAwxzm29SjdDmM3Hb3hdY4FFyV1Kok6zsjQSZJXYoLJWnZLo2aREKZQdrJ3DZzK9aa7XCShQEufemKqY5rAYA3hyFdxjdkR6cn77jaz1LBcmd8HefpoL8G7"
  }
}
```

#### responder <--- (2018-10-24 13:00:05.773)
```javascript
{
  "action": "update",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkKZG3cA4HCjFSK8Snd3dzddNzmgvVPRzG6hKbGhH5YEjG99tiJ7JRi6jhBG661Qc652FNtQPtt9o9JfsuyHErg7Wz8xGTKd9FiAiLPCqEMZ9F8HYtK3p2W7LC5xeRWLkLGFUX2uF1ZKtAcTwqVABespW2CrkjkTupEANQ6MkrhRFdsK8VYZxd5D4uC6hN5DsT4d7hMqbNXwDFtUGDFXgmk1vtsVFKgouoR7H1ioXPaJoxyi7WjJZ1UQv6M9HrNCGuBGsu2JKg6uAefm42NkAwxzm29SjdDmM3Hb3hdY4FFyV1Kok6zsjQSZJXYoLJWnZLo2aREKZQdrJ3DZzK9aa7XCShQEufemKqY5rAYA3hyFdxjdkR6cn77jaz1LBcmd8HefpoL8G7"
  }
}
```

#### initiator ---> (2018-10-24 13:00:05.776)
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

#### initiator <--- (2018-10-24 13:00:05.777)
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

#### responder ---> (2018-10-24 13:00:05.852)
```javascript
{
  "action": "shutdown"
}
```

#### responder <--- (2018-10-24 13:00:05.855)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_2M9ipLgcZU4gErR937LNboLNi9dRD5urUB19uaWn9DH3yVJus39nNBX6znrkZhY2g8RyASXEUSXS5AwH7G35UMf8YMurnxW4CPCkA4FEQzAoj6kR8W47i"
  },
  "tag": "shutdown_sign"
}
```

#### responder ---> (2018-10-24 13:00:05.855)
```javascript
{
  "action": "shutdown_sign",
  "payload": {
    "tx": "tx_2iJcVi27J8ZyUZjw5iPikAqTTM9a3Z8nyktnH14gJGMmj5dbMDrCMs4wVrnVVcg9gZpa7zWbthu8h1HypwDN5bH6Sh2rHF6kfdzFqg95zspSo8czetMtJzrwePMYZJ8tJURJWX3Ts5A385E33YU9W5r7Pt5Azd5kWFS4CaDMvAddi7yR8DcUJFAWJSDbKrAfL7GsCea3eKkLuHSwJmzUgB7E6V"
  }
}
```

#### initiator <--- (2018-10-24 13:00:05.856)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_2M9ipLgcZU4gErR937LNboLNi9dRD5urUB19uaWn9DH3yVJus39nNBX6znrkZhY2g8RyASXEUSXS5AwH7G35UMf8YMurnxW4CPCkA4FEQzAoj6kR8W47i"
  },
  "tag": "shutdown_sign_ack"
}
```

#### initiator ---> (2018-10-24 13:00:05.857)
```javascript
{
  "action": "shutdown_sign_ack",
  "payload": {
    "tx": "tx_2iJcVi27J8ZzZCUdmGPaKuWe8XmKJ5rWGW29SAm616cBpu1ehEtxUEQ7GCFhrGBeZw34Moguh5fz3txGohapQWQVcuPxTzvLNXL8U8NgDGdU6P6s6Hdy8Es2m9xUXBYoMSqNRrqbKB8AUV1ZtPx9og7VS8pA1RLZHMhS8xQSZf7VyiWEnaXmWoo1arwBbNbJrm9KgF9ZeDRVJjSomUc9MW6HZm"
  }
}
```

#### initiator <--- (2018-10-24 13:00:05.858)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "tx": "tx_3wu1WL1txa1XNF5csL7KeNa6b49exwjubatcNKPRVhtsZgNp7aPLTCKx2ivm3jEPMzDAsvSzyx1AXRfwQBZAnMsvoR1TYqp9FTZLqB9MUKdknwUdaVNtxXf1Vy3geT6a29ZMmJ486NWaQNje7mLEYVp8tnsDcVdqgrYXAYreRndquALoHjjJH51RWUmVTLNRs87pCPBf4TitvefEW8grEBk6uBF7PY8gwnbNf2bJJXFrXtuNAbSxEeHZrnpvFfSGpY6og3mXFFJuJeVA4mcVPeJP2LfdWX4qnKZkYvkdMwQHvwQww9Tz"
  }
}
```

#### initiator <--- (2018-10-24 13:00:05.859)
```javascript
{
  "action": "info",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "event": "close_mutual"
  }
}
```

#### initiator <--- (2018-10-24 13:00:05.859)
```javascript
{
  "action": "info",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "event": "died"
  }
}
```

#### responder <--- (2018-10-24 13:00:05.863)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "tx": "tx_3wu1WL1txa1XNF5csL7KeNa6b49exwjubatcNKPRVhtsZgNp7aPLTCKx2ivm3jEPMzDAsvSzyx1AXRfwQBZAnMsvoR1TYqp9FTZLqB9MUKdknwUdaVNtxXf1Vy3geT6a29ZMmJ486NWaQNje7mLEYVp8tnsDcVdqgrYXAYreRndquALoHjjJH51RWUmVTLNRs87pCPBf4TitvefEW8grEBk6uBF7PY8gwnbNf2bJJXFrXtuNAbSxEeHZrnpvFfSGpY6og3mXFFJuJeVA4mcVPeJP2LfdWX4qnKZkYvkdMwQHvwQww9Tz"
  }
}
```

#### responder <--- (2018-10-24 13:00:05.864)
```javascript
{
  "action": "info",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "event": "close_mutual"
  }
}
```

#### responder <--- (2018-10-24 13:00:05.864)
```javascript
{
  "action": "info",
  "channel_id": "ch_2aqFfuQEgSu7Q3QqD3Snqyrwzz97nT8GJuNdikSWZhQhH2Kq1q",
  "payload": {
    "event": "died"
  }
}
```
