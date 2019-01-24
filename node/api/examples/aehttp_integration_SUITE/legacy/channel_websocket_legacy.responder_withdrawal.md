
#### initiator init (2018-10-24 13:01:15.678)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=initiator
```

#### responder init (2018-10-24 13:01:15.682)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=responder
```

#### responder <--- (2018-10-24 13:01:16.685)
```javascript
{
  "action": "info",
  "payload": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-24 13:01:16.686)
```javascript
{
  "action": "info",
  "payload": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-24 13:01:16.689)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_3d11KjpALm3t32sAMLL9Y5p9SUg9j82o5Er3hc4WTAmdXk3cXjxDydY4eoq6STXDutDQ59tM59bMr9CogemLkb4tUXrrZYvPc4DkdzkXhqGZjnzLVRAYpjMHXUeVmmqr9Fk96GrERRgHqJTaNp7wfhyEnqvb1nHkhAnLGJ"
  },
  "tag": "initiator_sign"
}
```

#### initiator ---> (2018-10-24 13:01:16.710)
```javascript
{
  "action": "initiator_sign",
  "payload": {
    "tx": "tx_4L9GSozvM4Hmgi4fVPDVPMDPoqS3vf3tD5vpSTdQHJKj1B5iWKgEUSi3Dz8KbNdX5tdFL6v7eoKQmQB4UfaXyr1AXrkzzsqtZqyZpyjEQqKn73x6vPrBSymPqK6Sm17Amsx94TsNkGt3qcNkqD7qg8A7vbad25MiK55REcHvuJJkaXkGmWHycZpPiHhxsSPaRS7cFjdktiziPDb9naMCzYvzziW6cUi46r9mHPFsTmcmUtuqHfEq27EKKHBesuYiBRZ7mcc2sPD"
  }
}
```

#### responder <--- (2018-10-24 13:01:16.711)
```javascript
{
  "action": "info",
  "payload": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-24 13:01:16.711)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_3d11KjpALm3t32sAMLL9Y5p9SUg9j82o5Er3hc4WTAmdXk3cXjxDydY4eoq6STXDutDQ59tM59bMr9CogemLkb4tUXrrZYvPc4DkdzkXhqGZjnzLVRAYpjMHXUeVmmqr9Fk96GrERRgHqJTaNp7wfhyEnqvb1nHkhAnLGJ"
  },
  "tag": "responder_sign"
}
```

#### responder ---> (2018-10-24 13:01:16.712)
```javascript
{
  "action": "responder_sign",
  "payload": {
    "tx": "tx_4L9GSozvM4Hp6FEQQu8PvGg862gz8VrMDFX8vZvLw3isEkpk5rjZKdP6zZE4mFSLd3KdpVUhwYhhtdaBMJrm412C6JY8rzwyTFikSrs522RKEzHvaAxpSYGbBhNnbWE8Tcr3VunZAeJeL7ic3rCP7TFFgbSeYXa7oxpsujrWAKUpPQBp3xHUQSmqHeSKidAx8htqBANwwTRhj5pkoo5e5WyAGDacumxJTQCHUPueZxG1L7a59w6SoKFZMsqbKJhUjUbSj5iJRhe"
  }
}
```

#### initiator <--- (2018-10-24 13:01:16.714)
```javascript
{
  "action": "info",
  "payload": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-24 13:01:16.714)
```javascript
{
  "action": "on_chain_tx",
  "payload": {
    "tx": "tx_6jPYBUFTkcmR6yZGrv3GFuQhY8wCTswy47HaF2G6bamojrhkBoKiDWQuKKfn7odcx5PU1QSio7meuCdv8f33VgVQf9sxZg3SivrkzBGC64DFPJqYD33iDba4em1BD98ikEnqSRWCqXrbTuha11rRFjys6DdoW3jXYVpUxMmBQzXRum5ATQLqBpdo1x1KqP3LXssPyASVun49B8H4JTkG13Tu3LyLprzdED8agjqgtZ8siciRbhpNQvNsYy8UYKTRtYtB6RfuMRU3XuxnaBsVscd1yvakAdkcui8pkts97mjYCq24VphSFTghrHDjdK7s8RG1byu3AkY8mzG1H7h5PHLwiRU1JWmNxZNkn"
  }
}
```

#### initiator <--- (2018-10-24 13:01:16.715)
```javascript
{
  "action": "on_chain_tx",
  "payload": {
    "tx": "tx_6jPYBUFTkcmR6yZGrv3GFuQhY8wCTswy47HaF2G6bamojrhkBoKiDWQuKKfn7odcx5PU1QSio7meuCdv8f33VgVQf9sxZg3SivrkzBGC64DFPJqYD33iDba4em1BD98ikEnqSRWCqXrbTuha11rRFjys6DdoW3jXYVpUxMmBQzXRum5ATQLqBpdo1x1KqP3LXssPyASVun49B8H4JTkG13Tu3LyLprzdED8agjqgtZ8siciRbhpNQvNsYy8UYKTRtYtB6RfuMRU3XuxnaBsVscd1yvakAdkcui8pkts97mjYCq24VphSFTghrHDjdK7s8RG1byu3AkY8mzG1H7h5PHLwiRU1JWmNxZNkn"
  }
}
```

#### initiator ---> (2018-10-24 13:01:17.841)
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

#### initiator <--- (2018-10-24 13:01:17.842)
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

#### responder <--- (2018-10-24 13:01:20.522)
```javascript
{
  "action": "info",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "event": "own_funding_locked"
  }
}
```

#### initiator <--- (2018-10-24 13:01:20.523)
```javascript
{
  "action": "info",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "event": "own_funding_locked"
  }
}
```

#### initiator <--- (2018-10-24 13:01:20.523)
```javascript
{
  "action": "info",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "event": "funding_locked"
  }
}
```

#### responder <--- (2018-10-24 13:01:20.524)
```javascript
{
  "action": "info",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "event": "funding_locked"
  }
}
```

#### initiator <--- (2018-10-24 13:01:20.527)
```javascript
{
  "action": "info",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "event": "open"
  }
}
```

#### responder <--- (2018-10-24 13:01:20.527)
```javascript
{
  "action": "info",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "event": "open"
  }
}
```

#### responder <--- (2018-10-24 13:01:20.528)
```javascript
{
  "action": "update",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "state": "tx_6jPYBUFTkcmR6yZGrv3GFuQhY8wCTswy47HaF2G6bamojrhkBoKiDWQuKKfn7odcx5PU1QSio7meuCdv8f33VgVQf9sxZg3SivrkzBGC64DFPJqYD33iDba4em1BD98ikEnqSRWCqXrbTuha11rRFjys6DdoW3jXYVpUxMmBQzXRum5ATQLqBpdo1x1KqP3LXssPyASVun49B8H4JTkG13Tu3LyLprzdED8agjqgtZ8siciRbhpNQvNsYy8UYKTRtYtB6RfuMRU3XuxnaBsVscd1yvakAdkcui8pkts97mjYCq24VphSFTghrHDjdK7s8RG1byu3AkY8mzG1H7h5PHLwiRU1JWmNxZNkn"
  }
}
```

#### initiator <--- (2018-10-24 13:01:20.529)
```javascript
{
  "action": "update",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "state": "tx_6jPYBUFTkcmR6yZGrv3GFuQhY8wCTswy47HaF2G6bamojrhkBoKiDWQuKKfn7odcx5PU1QSio7meuCdv8f33VgVQf9sxZg3SivrkzBGC64DFPJqYD33iDba4em1BD98ikEnqSRWCqXrbTuha11rRFjys6DdoW3jXYVpUxMmBQzXRum5ATQLqBpdo1x1KqP3LXssPyASVun49B8H4JTkG13Tu3LyLprzdED8agjqgtZ8siciRbhpNQvNsYy8UYKTRtYtB6RfuMRU3XuxnaBsVscd1yvakAdkcui8pkts97mjYCq24VphSFTghrHDjdK7s8RG1byu3AkY8mzG1H7h5PHLwiRU1JWmNxZNkn"
  }
}
```

#### initiator: (2018-10-24 13:01:20.721)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-24 13:01:20.721)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-24 13:01:20.721)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-24 13:01:20.721)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-24 13:01:20.721)
> Channel is `open` and ready to use

#### responder: (2018-10-24 13:01:20.721)
> Channel is `open` and ready to use

#### initiator ---> (2018-10-24 13:01:20.764)
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

#### initiator <--- (2018-10-24 13:01:20.767)
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

#### initiator ---> (2018-10-24 13:01:20.768)
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

#### initiator <--- (2018-10-24 13:01:20.776)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQSBToaZb28om38fRZ4wUbJHF3HTZTw3LVi2PbWNdUeKigEy1yD4WumP2K1P3F5yFqpYcRG6ojzbkfXkfgwdNy57ARxgrbRX69q3UxKifm3DAzVTWcFR379ih6iEwvQ3yKJtpA46bWuLxo1K5DRmC8SBGmuESWDbsVbMKAq5MR6WoXZrcsxkFbgvn2qSDgWF9uJpF4wMNzTk6A"
  },
  "tag": "update"
}
```

#### initiator ---> (2018-10-24 13:01:20.778)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak5AxZ8S2hJ6YnprsmpePmSM4YKjwCjCwAMkWcQaUq4uYUrhJgAhpp2cDarYRp5ax6RkmehoqgqpqwoiSZnpVYMvAu7VuJnoEKEC5HCvFDvEhdeUFP4eTXCLStZtGdk7s9Ep4axeu4gfKCeyKrQWruCpWp1XLPJZwV6pxKMvWC2nWZUbpov6NQArsuC1wtFcWoZkV3rrWurSntowTmY8ZosJDLXqHk2QWfMxM45Qd2EbuRzyJ8EQBzsMB3auqnJwAawmTm2myqkBMehf9CX3BkmqcGycnP18GRdKqw5beTMMRAx1Z"
  }
}
```

#### responder <--- (2018-10-24 13:01:20.784)
```javascript
{
  "action": "info",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "event": "update"
  }
}
```

#### responder <--- (2018-10-24 13:01:20.785)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQSBToaZb28om38fRZ4wUbJHF3HTZTw3LVi2PbWNdUeKigEy1yD4WumP2K1P3F5yFqpYcRG6ojzbkfXkfgwdNy57ARxgrbRX69q3UxKifm3DAzVTWcFR379ih6iEwvQ3yKJtpA46bWuLxo1K5DRmC8SBGmuESWDbsVbMKAq5MR6WoXZrcsxkFbgvn2qSDgWF9uJpF4wMNzTk6A"
  },
  "tag": "update_ack"
}
```

#### responder ---> (2018-10-24 13:01:20.786)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak59KouNqikJzxdexKDgvZbB7S5R3SMZRfhQaQsZtpjGdYGpgQWypjpLLfVEefdZbER8MBHpw4RY9hi8fmYNX6dzS7Emj8fjwBdSaLQXYH8kQoggyPvQtcvhQFnB8ZjaqXQcGx6GrxouXRUt8XheYQUDkWGUkzqP9neFvnWemdXipStXLDKSdqpsZM1pcG5K2hLF2XLBDrSotGBN4w3trdJ2RxszcJgmA9a6eb7wqCbn3TukxYpf7ZaE3czYoHFcq1CyQzBLnkKwXcyuJdDX9F3C7Ae3JjPRDjVUVCkNyuXT3oQFR"
  }
}
```

#### responder <--- (2018-10-24 13:01:20.792)
```javascript
{
  "action": "update",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkzawoeHSYUvF9eY28xEXdZDRydpYgKJDBfsz92P6A73KxzP66wK8gXYbNfAdiXmi8T5mSkB8ayaLee9YNng5i8PZMCRLp9bLcijfZewQNnh8epNT5UUiAHcVsNhae7gUAUTbb75WuQ8UYqmikNrQe3o3yDoFtYBFmmWxkJKLXG2WX1qDnyareL2tBChNM2cxWaxqPGAietL5q6xm9PcUanWQc8vjrk1bvNFYioVLh8Nokq7NBPjX7EBabdWXVMYqWD27UdYuSQ14f9jXXUgwpxJN9h7kvpg2FWMM2Sx2NwXhqt6dUSqDvJmSJ9XCPpW5Ws6S63EJSSXeoNJJy8sYefBPLHD4Vp8UU3mgJDCQFxXs3GHWAy2K6gwwXznkC6fHBk7FitGrc"
  }
}
```

#### initiator <--- (2018-10-24 13:01:20.792)
```javascript
{
  "action": "update",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkzawoeHSYUvF9eY28xEXdZDRydpYgKJDBfsz92P6A73KxzP66wK8gXYbNfAdiXmi8T5mSkB8ayaLee9YNng5i8PZMCRLp9bLcijfZewQNnh8epNT5UUiAHcVsNhae7gUAUTbb75WuQ8UYqmikNrQe3o3yDoFtYBFmmWxkJKLXG2WX1qDnyareL2tBChNM2cxWaxqPGAietL5q6xm9PcUanWQc8vjrk1bvNFYioVLh8Nokq7NBPjX7EBabdWXVMYqWD27UdYuSQ14f9jXXUgwpxJN9h7kvpg2FWMM2Sx2NwXhqt6dUSqDvJmSJ9XCPpW5Ws6S63EJSSXeoNJJy8sYefBPLHD4Vp8UU3mgJDCQFxXs3GHWAy2K6gwwXznkC6fHBk7FitGrc"
  }
}
```

#### initiator ---> (2018-10-24 13:01:20.795)
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

#### initiator <--- (2018-10-24 13:01:20.796)
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

#### initiator ---> (2018-10-24 13:01:20.797)
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

#### initiator <--- (2018-10-24 13:01:20.798)
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

#### responder ---> (2018-10-24 13:01:20.798)
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

#### responder <--- (2018-10-24 13:01:20.801)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQSBToaZb28om38fRZ4wUbJHF3HTZTw3LVi2PbWNdUeKigF4SV4c4NxikEmNaMz6LKrumPxYM7ByH1Y67MURnD8D1qNUfsegq3T6iCGa8EcsFFTUon8o2qQDKrpS5ySpPvWTAzy8wZ94aVLiPkXEJJEyuYcW2Zby5RKWxr2J9SXPsrbJBXKu3rDZEZC5eBvgAPdQxT3RQvoEsG"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 13:01:20.802)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak56auPY9hyk2A8VAchLhcT97F6wMTaV9nFMgwJSf3pTDMdLVSwNWszSXyM17yMJSL9zxGaRo9vX3jxFSrGJ2LFAWAXhdrC1Vsyr3mHfGUPwWbJmRM2pnvHzBLz2cgrmcPVMrrKy9KEHWJmr2YUM5zAazhBGWqVSDiK8sQKzr2d8GZ4NZRZ5koBqtvbgjqjD7BKNUXXYge7iXQ6u8DYKumn3G2fXcKUGm6uCumat7BnBFMGVs6A2bTJo83MmTrSkckWDr3nGrNZsNtF29kTgBXDpjPjdWQAuDhhE5wFp8oY7kiZHZ"
  }
}
```

#### initiator <--- (2018-10-24 13:01:20.837)
```javascript
{
  "action": "info",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 13:01:20.838)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQSBToaZb28om38fRZ4wUbJHF3HTZTw3LVi2PbWNdUeKigF4SV4c4NxikEmNaMz6LKrumPxYM7ByH1Y67MURnD8D1qNUfsegq3T6iCGa8EcsFFTUon8o2qQDKrpS5ySpPvWTAzy8wZ94aVLiPkXEJJEyuYcW2Zby5RKWxr2J9SXPsrbJBXKu3rDZEZC5eBvgAPdQxT3RQvoEsG"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 13:01:20.840)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak54mhKbY2B6dmkNdDntcfP5ut9QDRKoieKwZXFaZdbxanNr9LwmBif52GZ7Kt1Uif3enN9g6Pjc7tjDYK678VV9mMofBrqbCPD215VR1Ef36AswrecjJ7NnzgFhW7vm5LiRqWbkcvwzeq2MKgfgwcT4xDKDnvzjGeD9hMH4kY3fjfYPyBk3zKFCBjXamZpQDFYxPhneypvLS9zDnirKaZjFbqojEhXVp5LUv5Z24kRAkjHET467STaKak7ebGTxEhAjsDsNoWj3C45nKBFW4nj5W7VhTPtD55h5EWQaL9U9GDScq"
  }
}
```

#### initiator <--- (2018-10-24 13:01:20.853)
```javascript
{
  "action": "update",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkrktbB736Trpqe1cR34ptWAqxft7nrzC4LmPBpYCRZvnKB7YxSCs7knE5V7jTGXzbg9xhov59k3Vrn12KQeLL3SD7kVEXfSFuXbs9EQZV9b6HZpNGoMWrBst6kjrByLkVQWx9uWRgN8bzogc7XSU3UnAAsmMZMq9WcYWmxP9ivfL5EzfEwCYb3HZMJeM6seFXifCMzmVPwsGRmFG55kb7vD7szRAq2J7wrsXetsJmxJnQ6w1PiikpoeAhvVDDDcRHsYixrTSWHZuKAVaY1vY3ASgzmNZRuL3tpfLWU7Y6tJcJa9DN6P3WrSJRf2kN61dHh2SE2ZacrLrctTvkxtHB1EWNMbb2sJZySJdGa6P9wnLz2nird7TxhGvRXmXyaCPrDZciNxzD"
  }
}
```

#### responder <--- (2018-10-24 13:01:20.855)
```javascript
{
  "action": "update",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkrktbB736Trpqe1cR34ptWAqxft7nrzC4LmPBpYCRZvnKB7YxSCs7knE5V7jTGXzbg9xhov59k3Vrn12KQeLL3SD7kVEXfSFuXbs9EQZV9b6HZpNGoMWrBst6kjrByLkVQWx9uWRgN8bzogc7XSU3UnAAsmMZMq9WcYWmxP9ivfL5EzfEwCYb3HZMJeM6seFXifCMzmVPwsGRmFG55kb7vD7szRAq2J7wrsXetsJmxJnQ6w1PiikpoeAhvVDDDcRHsYixrTSWHZuKAVaY1vY3ASgzmNZRuL3tpfLWU7Y6tJcJa9DN6P3WrSJRf2kN61dHh2SE2ZacrLrctTvkxtHB1EWNMbb2sJZySJdGa6P9wnLz2nird7TxhGvRXmXyaCPrDZciNxzD"
  }
}
```

#### initiator ---> (2018-10-24 13:01:20.859)
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

#### initiator <--- (2018-10-24 13:01:20.860)
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

#### initiator ---> (2018-10-24 13:01:20.861)
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

#### initiator <--- (2018-10-24 13:01:20.862)
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

#### responder ---> (2018-10-24 13:01:20.862)
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

#### responder <--- (2018-10-24 13:01:20.866)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQSBToaZb28om38fRZ4wUbJHF3HTZTw3LVi2PbWNdUeKigF9rzv9brA4UAXN7UtDBKeDJ8WyvBAfB8x8zyPuXtrxcrrk5zKYCJ73TMN1q2MeLM97mQdrMGHTwo6rfgA5GaSTJKC5oUidHu25szubFijaAnvAae4Z9pmEbtnXEZpASS3LJpwKgRjafcyMtMvPwTZNUEgFJuqPHq"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 13:01:20.867)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4nqdikjPbawAWDuE7yb7JttD1ykkacP6oaiCFvK7nLa43gPf229Aatz3eDD66TVEFaAf9f4dYpc3W5PS1G1dgR2ZyPGqGcHHs8t5b39mbwZzQASUV7ju8GcUMvphTkL82HQJgE9SmcUgR8sLaGSXNXwfi82oHgxfcPwQaqnMPTzGDZwokhUzRqfvSGhwrbCrCMcLWyNN7HxF74brdvJT2j9mPkx19dLErkdK1ms8G78qQkE8gKZVQZoVAeBatnXNDQT5Xbp7NQG8L6ymrYxvidqHnEfUT1nyqzG22xhnExPbj5H"
  }
}
```

#### initiator <--- (2018-10-24 13:01:20.871)
```javascript
{
  "action": "info",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 13:01:20.871)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQSBToaZb28om38fRZ4wUbJHF3HTZTw3LVi2PbWNdUeKigF9rzv9brA4UAXN7UtDBKeDJ8WyvBAfB8x8zyPuXtrxcrrk5zKYCJ73TMN1q2MeLM97mQdrMGHTwo6rfgA5GaSTJKC5oUidHu25szubFijaAnvAae4Z9pmEbtnXEZpASS3LJpwKgRjafcyMtMvPwTZNUEgFJuqPHq"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 13:01:20.872)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak52BobdutX6nKWYgx6tVgn7P7h1PcEV7kJwXEizCtttKeon2XP5pnkWQf7raCupmMJLYkXj8vQEVW36QbK17AvtNGqti1zYKLGNFFndKPBNdAKrxD7j488Stx4QeZ9bxBv6s9YfEypXjdegZznSueectzAGZieiNJ5tbY9SwcP6GXPg4DTmrcuNW1tDYQY3DEJad163ji39n4TimYx6PmwoydpLjWocKCQM11ZTUE3zjwxHjafm9iS4K1pwEGB2HFiCLGMSb4ssMk7fALXe9Tu12xtKLcQ9RxJrr998rcpkEy1zv"
  }
}
```

#### initiator <--- (2018-10-24 13:01:20.877)
```javascript
{
  "action": "update",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkPNGkiEtt1W8na5wDA4i7DSwkWa65dSuxzweEh9tPMALBjKDGeAMEzPTYsr6DKHvrutRrAwhBM2hEYFyMqz5wwkz3ymvhbH4QqrWDh1MKFdffuNbaPBbNX8JdN3RaTuArjTd6rzuC6p6eZ9bTUfJ3eVoy6e2uEuaVNM4ZPiegsryF4Wn5phTc3LRs1MdGpb2YRibs34C4SndcmqGxSeM75UivfLsgBqgdr7KZasyQZdinbJB4y92k5ru2AWY2sxGA4XEpGWVRXMwuGaGDfzMzbS5qL1he4zrekHVFJE7WeEQRZNwmeghrNtVizaiEw8dnfXGrtpRp6Ys4UARBE1GxtERuoPgPsU42UGkGPhyfCdjpowTv8eiELie2C2D9LxriZfJSnjuK"
  }
}
```

#### responder <--- (2018-10-24 13:01:20.877)
```javascript
{
  "action": "update",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkPNGkiEtt1W8na5wDA4i7DSwkWa65dSuxzweEh9tPMALBjKDGeAMEzPTYsr6DKHvrutRrAwhBM2hEYFyMqz5wwkz3ymvhbH4QqrWDh1MKFdffuNbaPBbNX8JdN3RaTuArjTd6rzuC6p6eZ9bTUfJ3eVoy6e2uEuaVNM4ZPiegsryF4Wn5phTc3LRs1MdGpb2YRibs34C4SndcmqGxSeM75UivfLsgBqgdr7KZasyQZdinbJB4y92k5ru2AWY2sxGA4XEpGWVRXMwuGaGDfzMzbS5qL1he4zrekHVFJE7WeEQRZNwmeghrNtVizaiEw8dnfXGrtpRp6Ys4UARBE1GxtERuoPgPsU42UGkGPhyfCdjpowTv8eiELie2C2D9LxriZfJSnjuK"
  }
}
```

#### initiator ---> (2018-10-24 13:01:20.880)
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

#### initiator <--- (2018-10-24 13:01:20.881)
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

#### initiator ---> (2018-10-24 13:01:20.882)
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

#### initiator <--- (2018-10-24 13:01:20.882)
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

#### initiator ---> (2018-10-24 13:01:20.883)
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

#### initiator <--- (2018-10-24 13:01:20.886)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQSBToaZb28om38fRZ4wUbJHF3HTZTw3LVi2PbWNdUeKigFFHWmh9KMQC6HMebnKnqATCcwRWwvfT3muLYi4e2HMyWRV6wS5BunsiRc3n8FYSHYNPVkazPoUYuZWh2XpbH6uC6iwBHe3723RXxar4Pux4WpE3mJhFu1Dgy2K6hUxj3tsLQ6aTjgqHr2PMTbb2ncvQNaTHg1P24"
  },
  "tag": "update"
}
```

#### initiator ---> (2018-10-24 13:01:20.886)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4oTL7Ze5Kz8ihdtCe6RqNcozFkMHQZdwHgJNfZ3F6yrrEtxWm25uYpAccyJV1JhLDwYTcfFxaTrzXVpG1uUeLYEDAVvaxwhDdifW2giDThkiD7UjuWiqyQDSXGWAKYKtx2AVax4cWbYPVUSTHZcyEMb6SJLr97z3dnUXRCEF3GZcm5WtzxsGEQZHCYnQS46cz6P12dtkqZCRYFZWrU57L76Tp6hCdEt2F5LKJZGDpU1LZewz5apfHdb2WMTUgtcHNTKidRKJP14VpLZLe9M9cvBVmxZp8WjPw5cgkvcXpghXYaR"
  }
}
```

#### responder <--- (2018-10-24 13:01:20.922)
```javascript
{
  "action": "info",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "event": "update"
  }
}
```

#### responder <--- (2018-10-24 13:01:20.923)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQSBToaZb28om38fRZ4wUbJHF3HTZTw3LVi2PbWNdUeKigFFHWmh9KMQC6HMebnKnqATCcwRWwvfT3muLYi4e2HMyWRV6wS5BunsiRc3n8FYSHYNPVkazPoUYuZWh2XpbH6uC6iwBHe3723RXxar4Pux4WpE3mJhFu1Dgy2K6hUxj3tsLQ6aTjgqHr2PMTbb2ncvQNaTHg1P24"
  },
  "tag": "update_ack"
}
```

#### responder ---> (2018-10-24 13:01:20.925)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak53qznRMA5Z142DXVqxxACWYiriS7poNGv8NNLqhRZbmBm3too8GgFF2ptaQNsGmPZ7JVjRGyNGt8Fw5xeypGzum3bYuVRc7ZnkgFmBve2mVbFqsQ5Y3hALv6cQYLRyupYdQ8cNMDENkz8KT6vmXFPdAXCn8a8ARxBovBDC7n2zx2eaCr534CTw9KD2gB5kctSRx9ZR5NQgHkvZc8btEQPppSCdKGc7wuPbCSZ7qfXhDNxfPB9isQr8wewZSszioGfkHSudSpSL8fwxtZvu9Nu145WDeb36hEr1R9kdJG4k2kykf"
  }
}
```

#### responder <--- (2018-10-24 13:01:20.934)
```javascript
{
  "action": "update",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkQRe7DjQ1qpEP7caXkitrcUyk8DvLhSSZs5hkgjX3f6o2i2dH7FXnDD9aarK6w4kzWcVEYqfKR77eCDdmUQMW7dF7rRETXBsYoKFytF3DUwp5hHQwzzEyzL5GQD3m3wwUwEoG5oUyR4hXKZ78hWMeKALZcCEgyV7ddd4aYGxW8RmmPWnhRVSK6ewbMkg6vus66pAP2GzgiDHE8bnzKzt5Fzv14C3bA2rC4GVQasEJuLMMRapK59sWetwrF1rfTDGMuFmpv2LNKChAHZY6ThwcLMMPLj8CTvHhsz56iTbZqwhQrwv5fazVPWTkUqkR5ZkR29pFVnJMSqN4jMTUBq1S3xnPpywyCqA3iWLhDZAyx7WRZSarEVgR1RtqxZno2SeVboF6XbCc"
  }
}
```

#### initiator <--- (2018-10-24 13:01:20.935)
```javascript
{
  "action": "update",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkQRe7DjQ1qpEP7caXkitrcUyk8DvLhSSZs5hkgjX3f6o2i2dH7FXnDD9aarK6w4kzWcVEYqfKR77eCDdmUQMW7dF7rRETXBsYoKFytF3DUwp5hHQwzzEyzL5GQD3m3wwUwEoG5oUyR4hXKZ78hWMeKALZcCEgyV7ddd4aYGxW8RmmPWnhRVSK6ewbMkg6vus66pAP2GzgiDHE8bnzKzt5Fzv14C3bA2rC4GVQasEJuLMMRapK59sWetwrF1rfTDGMuFmpv2LNKChAHZY6ThwcLMMPLj8CTvHhsz56iTbZqwhQrwv5fazVPWTkUqkR5ZkR29pFVnJMSqN4jMTUBq1S3xnPpywyCqA3iWLhDZAyx7WRZSarEVgR1RtqxZno2SeVboF6XbCc"
  }
}
```

#### initiator ---> (2018-10-24 13:01:20.942)
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

#### initiator <--- (2018-10-24 13:01:20.943)
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

#### initiator ---> (2018-10-24 13:01:20.944)
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

#### initiator <--- (2018-10-24 13:01:20.946)
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

#### responder ---> (2018-10-24 13:01:20.946)
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

#### responder <--- (2018-10-24 13:01:20.951)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQSBToaZb28om38fRZ4wUbJHF3HTZTw3LVi2PbWNdUeKigFLi2dEgnYjv23MBigSsKCpMbds4K82yPnEnDEs3GLTpuqGvDfEvoQvwfYuEbqCWYWPgfdxz83yBffhq5ab1tJTYwdyXKskiiNprVgKAZikhHXVeriyub4Ji47z9avsxAsedLan6xaT72mmpLrpc3NRUB3vCoAzft"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 13:01:20.953)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4qXBzgK2psHFhZHBHuCNJXzwNMPydsJbBbFR6HPixjoy5RyLUaMKXuBjfN7jRow1nGpdYrk3KXDENSo7pejFo6c7PnSiL5gPuwicBhLZPMT4gMykgYocviHtckbkejM46DVHcoaRXDaw3qt1Mzmm4dNtxn4S2nzPBYGR3S9hmpsw1b3dDWs7GbcRoSmPWYPJADLAhSERENE7PbvD74pX8Q3moygebda1aDWvZziCpm8Yfv1mwb6LdTbz6FcifaNQBLSfxRbDSk2UDWGa8xqRnuTDvDi64nJRAJdth3hMoiXonDd"
  }
}
```

#### initiator <--- (2018-10-24 13:01:20.972)
```javascript
{
  "action": "info",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 13:01:20.973)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQSBToaZb28om38fRZ4wUbJHF3HTZTw3LVi2PbWNdUeKigFLi2dEgnYjv23MBigSsKCpMbds4K82yPnEnDEs3GLTpuqGvDfEvoQvwfYuEbqCWYWPgfdxz83yBffhq5ab1tJTYwdyXKskiiNprVgKAZikhHXVeriyub4Ji47z9avsxAsedLan6xaT72mmpLrpc3NRUB3vCoAzft"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 13:01:20.975)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak4rJEGM69v5SoBGuSSkehDSAgSPj53azsovJD1GMHtEkc1ozJKGCE6HtwsHFunnhkyddNekfKRGj3rDuBTfK5RH8WHL42SRR27QAYLQM1e3aJN6dy8EvjhHZqkA5f62farQfACxa4xzVj5khWpVZByJyngNkBfdxur4tachLnsQ4W3NKYBdRPscWJNWtmHVdUsFcwc17zxjesxmWJbaw5f6g3xyD9LrcVz9DRVXJpvUpntpqfy7b5YAeJwgUorvdVxsyu7Wwddh4U1HYcALp6WsaaSFjmT75mMTKZLJXX8U36tYH"
  }
}
```

#### initiator <--- (2018-10-24 13:01:20.981)
```javascript
{
  "action": "update",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkTyhZP7qqfrwKzKRVC8w57kuVWm2gAoxgLCBUKwCrrFt9qhmfFZw7LQ4mmd1gnjjFkppqirPxaR1Jc2M7bXD7P6oykmfkfDsiu4gvETNBFTiKpSmFf4AUDej7N1PBzEz1oL9Nc3f8zPzmupQgSupxofZr4qNdfVS8yMjyAUSEXTzQqeVvkTikcyCWmBeMadSX9Rey1BH9fYsboHESirqnrW5ZnSFHtNi6o5cmYhXECkVnkbCcrVRVjnSqdK1ARsCvj8NXWWBQ77mVsUD3zzq7Xbyq6S6asxoe36cow6pw1XEgUjSApPhJHCeDEw3QhCnti1Sjc9BN1xeZ5ppayzAiEu2Co28BRxS9NvQ7Hf2uQ3UvproFdpLfEjwYqYeWiLxHo1YwJpnY"
  }
}
```

#### responder <--- (2018-10-24 13:01:20.983)
```javascript
{
  "action": "update",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkTyhZP7qqfrwKzKRVC8w57kuVWm2gAoxgLCBUKwCrrFt9qhmfFZw7LQ4mmd1gnjjFkppqirPxaR1Jc2M7bXD7P6oykmfkfDsiu4gvETNBFTiKpSmFf4AUDej7N1PBzEz1oL9Nc3f8zPzmupQgSupxofZr4qNdfVS8yMjyAUSEXTzQqeVvkTikcyCWmBeMadSX9Rey1BH9fYsboHESirqnrW5ZnSFHtNi6o5cmYhXECkVnkbCcrVRVjnSqdK1ARsCvj8NXWWBQ77mVsUD3zzq7Xbyq6S6asxoe36cow6pw1XEgUjSApPhJHCeDEw3QhCnti1Sjc9BN1xeZ5ppayzAiEu2Co28BRxS9NvQ7Hf2uQ3UvproFdpLfEjwYqYeWiLxHo1YwJpnY"
  }
}
```

#### initiator ---> (2018-10-24 13:01:20.989)
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

#### initiator <--- (2018-10-24 13:01:20.990)
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

#### responder ---> (2018-10-24 13:01:21.75)
```javascript
{
  "action": "withdraw",
  "payload": {
    "amount": 2
  }
}
```

#### responder <--- (2018-10-24 13:01:21.82)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_2C9estKT2oDGShEYYZ6QN8dddGtj396nqzmvWSXVaovxePB7934s42rVqeaYqRTJWoCcH8Za7a4BPUpxE6ojttWMKf2WQWwpn7Eonb3hcWG1zttFGYJHFj4ho11Dkb5GsX9aBgpnytsZFbRNq3xTQ8KsEMUVnd"
  },
  "tag": "withdraw_tx"
}
```

#### responder ---> (2018-10-24 13:01:21.83)
```javascript
{
  "action": "withdraw_tx",
  "payload": {
    "tx": "tx_2WsEQsiC5Xsn5AxEsY6WyVfLd43NArbgYKa9oJugQPSSLLqxXAHFsPcfgky29y6fAp4Fn5kwG4eKFRL6EdeFkDZSHNYZLCuCsEC9ZjZGPE6CW4oAqEf3HScYtnNCS73NPLZ6My85vf2m6x7JgjpyMLbmDZiZDmTcfBWA4uq5ihVtY7qLiM6J1Mo5zUMKFjy2gba1UU5zmabcWEE2BoQbnymJkEyxb4CNRgzp5ekWfqJ3oG1Wu4AiCyB4ciY9AiGGr74"
  }
}
```

#### initiator <--- (2018-10-24 13:01:21.84)
```javascript
{
  "action": "info",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "event": "withdraw_created"
  }
}
```

#### initiator <--- (2018-10-24 13:01:21.85)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_2C9estKT2oDGShEYYZ6QN8dddGtj396nqzmvWSXVaovxePB7934s42rVqeaYqRTJWoCcH8Za7a4BPUpxE6ojttWMKf2WQWwpn7Eonb3hcWG1zttFGYJHFj4ho11Dkb5GsX9aBgpnytsZFbRNq3xTQ8KsEMUVnd"
  },
  "tag": "withdraw_ack"
}
```

#### initiator ---> (2018-10-24 13:01:21.86)
```javascript
{
  "action": "withdraw_ack",
  "payload": {
    "tx": "tx_2WsEQsiC5XsoF98LGVcCoVfmAD8Vd1H4xSsonnhBhd2dmhoDCtLH7WNkr8FkaGihuNoueJk4o5ggQ4PzjdP82BjH5rp279HUngaYyKknwg8aqvNNJcGvAQfCv5AdZVSvPS7yyNciHSYbDP7GnuSLP8Yu8hu5ZwCuViYqrK7TH6ygvyLwYsfCLkmGo5WyEEQFwZBa9Fd24dcBMqgG9wMuGwH3juZLxLnjciFfjikdZkzgSCdkMGtWv3dkxGDnu8APh7c"
  }
}
```

#### initiator <--- (2018-10-24 13:01:21.88)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "tx": "tx_3cDMp6242sByrkfsSTwpGGu1hrDvaY5TAecjJijx6dBwi6UgTdPcCmdGh33xqUgCeteGmB2wtQkb75rhRcvguq1gVA3PedUyRcjRAS4xbQb6z6XCv8TKjVWYCSG8PsqAdyJ3R9mbukGcAmEfJdFdqaR8kNKtsUnxLGS7ZdKAHVU7JZbFMkiM9PEGtdV9zTkwqCXqNL9HdCMcPvxZyZqV1LjRyUzJFMS7DiiwpuPWA1rakvvJzbg8f6rgJ2T7Sp9HQcaK3XFhFZsyaA6Dqjm2XEqDnEqL6AEB2W3Pd2sp5X6TTUTNVwTCASrECKpmTsBZi14L9ye7Ej7uxNxqqdQgpf7VAvHAc"
  }
}
```

#### responder <--- (2018-10-24 13:01:21.88)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "tx": "tx_3cDMp6242sByrkfsSTwpGGu1hrDvaY5TAecjJijx6dBwi6UgTdPcCmdGh33xqUgCeteGmB2wtQkb75rhRcvguq1gVA3PedUyRcjRAS4xbQb6z6XCv8TKjVWYCSG8PsqAdyJ3R9mbukGcAmEfJdFdqaR8kNKtsUnxLGS7ZdKAHVU7JZbFMkiM9PEGtdV9zTkwqCXqNL9HdCMcPvxZyZqV1LjRyUzJFMS7DiiwpuPWA1rakvvJzbg8f6rgJ2T7Sp9HQcaK3XFhFZsyaA6Dqjm2XEqDnEqL6AEB2W3Pd2sp5X6TTUTNVwTCASrECKpmTsBZi14L9ye7Ej7uxNxqqdQgpf7VAvHAc"
  }
}
```

#### responder <--- (2018-10-24 13:01:22.896)
```javascript
{
  "action": "info",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "event": "own_withdraw_locked"
  }
}
```

#### initiator <--- (2018-10-24 13:01:22.898)
```javascript
{
  "action": "info",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "event": "own_withdraw_locked"
  }
}
```

#### initiator <--- (2018-10-24 13:01:22.898)
```javascript
{
  "action": "info",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "event": "withdraw_locked"
  }
}
```

#### responder <--- (2018-10-24 13:01:22.898)
```javascript
{
  "action": "info",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "event": "withdraw_locked"
  }
}
```

#### initiator <--- (2018-10-24 13:01:22.901)
```javascript
{
  "action": "update",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "state": "tx_3cDMp6242sByrkfsSTwpGGu1hrDvaY5TAecjJijx6dBwi6UgTdPcCmdGh33xqUgCeteGmB2wtQkb75rhRcvguq1gVA3PedUyRcjRAS4xbQb6z6XCv8TKjVWYCSG8PsqAdyJ3R9mbukGcAmEfJdFdqaR8kNKtsUnxLGS7ZdKAHVU7JZbFMkiM9PEGtdV9zTkwqCXqNL9HdCMcPvxZyZqV1LjRyUzJFMS7DiiwpuPWA1rakvvJzbg8f6rgJ2T7Sp9HQcaK3XFhFZsyaA6Dqjm2XEqDnEqL6AEB2W3Pd2sp5X6TTUTNVwTCASrECKpmTsBZi14L9ye7Ej7uxNxqqdQgpf7VAvHAc"
  }
}
```

#### responder <--- (2018-10-24 13:01:22.901)
```javascript
{
  "action": "update",
  "channel_id": "ch_2MJTmCtrnRQSAvjRXTGEL7mZNFioWrBPmBekFVZfepnWBC9hD7",
  "payload": {
    "state": "tx_3cDMp6242sByrkfsSTwpGGu1hrDvaY5TAecjJijx6dBwi6UgTdPcCmdGh33xqUgCeteGmB2wtQkb75rhRcvguq1gVA3PedUyRcjRAS4xbQb6z6XCv8TKjVWYCSG8PsqAdyJ3R9mbukGcAmEfJdFdqaR8kNKtsUnxLGS7ZdKAHVU7JZbFMkiM9PEGtdV9zTkwqCXqNL9HdCMcPvxZyZqV1LjRyUzJFMS7DiiwpuPWA1rakvvJzbg8f6rgJ2T7Sp9HQcaK3XFhFZsyaA6Dqjm2XEqDnEqL6AEB2W3Pd2sp5X6TTUTNVwTCASrECKpmTsBZi14L9ye7Ej7uxNxqqdQgpf7VAvHAc"
  }
}
```
