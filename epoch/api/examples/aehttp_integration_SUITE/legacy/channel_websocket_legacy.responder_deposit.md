
#### initiator init (2018-10-24 13:00:34.379)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=initiator
```

#### responder init (2018-10-24 13:00:34.383)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=responder
```

#### responder <--- (2018-10-24 13:00:35.385)
```javascript
{
  "action": "info",
  "payload": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-24 13:00:35.387)
```javascript
{
  "action": "info",
  "payload": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-24 13:00:35.391)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_3d11KjpALm3t32sAMLL9Y5p9SUg9j82o5Er3hc4WTAmdXk3cXjxDydY4eoq6STXDutDQ59tM59bMr9CogemLkb4tUXrrZYvPc4DkdzkXhqGZjnzLVRAYpjMHXUeVmmqr9Fk96GrERRgHqJTaNp7wfhyEnqvb1nHkNdWrq5"
  },
  "tag": "initiator_sign"
}
```

#### initiator ---> (2018-10-24 13:00:35.406)
```javascript
{
  "action": "initiator_sign",
  "payload": {
    "tx": "tx_4L9GSozvM4HnUC9nugWtUjN47ogtfvY71Q5es5Mr29B4B51NGz5TwTDmjmd8PkYoB5GVEf5u4FnNqrrRiFwVVXAi2KAwMk5hCYzvkTPEU3ukrm8NPA3CnAnxm3iHxFTe2XfYmsw3AwAX6fcU194uJUPXfyV1wqdTdYnNBUr46dnMZeCFFVkNcKDc5Jw97PaCFzsVU9Auy9GM5cPT8zPPdaMnPQTVkRXpNpUe7oN1cW4eQWpRoaWFXuzVGds9gcNYE1wcGXpX971"
  }
}
```

#### responder <--- (2018-10-24 13:00:35.407)
```javascript
{
  "action": "info",
  "payload": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-24 13:00:35.407)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_3d11KjpALm3t32sAMLL9Y5p9SUg9j82o5Er3hc4WTAmdXk3cXjxDydY4eoq6STXDutDQ59tM59bMr9CogemLkb4tUXrrZYvPc4DkdzkXhqGZjnzLVRAYpjMHXUeVmmqr9Fk96GrERRgHqJTaNp7wfhyEnqvb1nHkNdWrq5"
  },
  "tag": "responder_sign"
}
```

#### responder ---> (2018-10-24 13:00:35.407)
```javascript
{
  "action": "responder_sign",
  "payload": {
    "tx": "tx_4L9GSozvM4Hm23CVYZRfvcHbSm8a8Gi1andPRGwvQR8GqhfF5NgKrsf2JRwM8pdTmJwQRLNvr6K798iBU3JvVzivucqvvW6rpgoJ4L4xeQPgtvgCk1BkKe94B1aTe3gJUwNc9MAfzoHjYVJ6AHxVnqSw4mRRSke5Ea7pmScTkJhcByxf2w3AiLRaiiGc8ErPdUt7wSPiNCeRisEQEfPQZrLPZ7qYHJPqepUZSmjv74Gmf9zLBRAUaWDtzWoT73Mn3aXaWBGf9cu"
  }
}
```

#### initiator <--- (2018-10-24 13:00:35.408)
```javascript
{
  "action": "info",
  "payload": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-24 13:00:35.409)
```javascript
{
  "action": "on_chain_tx",
  "payload": {
    "tx": "tx_6jPYBUFTkcmPxVhJhGQsydPEsyApwNn7L5gFSG1hzf3pdBT3yLyPxn7RLcQgMFB9pZwK7jHEe7Bb2pNHGA9L1sQNkmjobXTmszLfwuwNctBQ11E82bS1AUKYSTZsS5afQ4fAg2UReLRm65SkTjYuGR9jpPrjGFehgEV8i59eMtaDCz8MznBKC3uCEyvp2y16vd6Ehy13zrB6RsgbTpzffi7X9KtouxpiyH5LPK6847VSEf4xdw9YDkFV4jLnTGmMxuYsogKdPWZHkUi14Mucub7NEyWp3dv5FeZJ4AA6be8rra7vmbAs2mkC8S5z7emSQvBA6uQh8KSxQdGazxWkDbPU5xe53NSaTvjHP"
  }
}
```

#### initiator <--- (2018-10-24 13:00:35.409)
```javascript
{
  "action": "on_chain_tx",
  "payload": {
    "tx": "tx_6jPYBUFTkcmPxVhJhGQsydPEsyApwNn7L5gFSG1hzf3pdBT3yLyPxn7RLcQgMFB9pZwK7jHEe7Bb2pNHGA9L1sQNkmjobXTmszLfwuwNctBQ11E82bS1AUKYSTZsS5afQ4fAg2UReLRm65SkTjYuGR9jpPrjGFehgEV8i59eMtaDCz8MznBKC3uCEyvp2y16vd6Ehy13zrB6RsgbTpzffi7X9KtouxpiyH5LPK6847VSEf4xdw9YDkFV4jLnTGmMxuYsogKdPWZHkUi14Mucub7NEyWp3dv5FeZJ4AA6be8rra7vmbAs2mkC8S5z7emSQvBA6uQh8KSxQdGazxWkDbPU5xe53NSaTvjHP"
  }
}
```

#### initiator ---> (2018-10-24 13:00:37.800)
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

#### initiator <--- (2018-10-24 13:00:37.803)
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

#### initiator <--- (2018-10-24 13:00:41.158)
```javascript
{
  "action": "info",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "event": "own_funding_locked"
  }
}
```

#### responder <--- (2018-10-24 13:00:41.158)
```javascript
{
  "action": "info",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "event": "own_funding_locked"
  }
}
```

#### responder <--- (2018-10-24 13:00:41.159)
```javascript
{
  "action": "info",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "event": "funding_locked"
  }
}
```

#### initiator <--- (2018-10-24 13:00:41.159)
```javascript
{
  "action": "info",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "event": "funding_locked"
  }
}
```

#### initiator <--- (2018-10-24 13:00:41.162)
```javascript
{
  "action": "info",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "event": "open"
  }
}
```

#### initiator <--- (2018-10-24 13:00:41.163)
```javascript
{
  "action": "update",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "state": "tx_6jPYBUFTkcmPxVhJhGQsydPEsyApwNn7L5gFSG1hzf3pdBT3yLyPxn7RLcQgMFB9pZwK7jHEe7Bb2pNHGA9L1sQNkmjobXTmszLfwuwNctBQ11E82bS1AUKYSTZsS5afQ4fAg2UReLRm65SkTjYuGR9jpPrjGFehgEV8i59eMtaDCz8MznBKC3uCEyvp2y16vd6Ehy13zrB6RsgbTpzffi7X9KtouxpiyH5LPK6847VSEf4xdw9YDkFV4jLnTGmMxuYsogKdPWZHkUi14Mucub7NEyWp3dv5FeZJ4AA6be8rra7vmbAs2mkC8S5z7emSQvBA6uQh8KSxQdGazxWkDbPU5xe53NSaTvjHP"
  }
}
```

#### responder <--- (2018-10-24 13:00:41.163)
```javascript
{
  "action": "info",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "event": "open"
  }
}
```

#### responder <--- (2018-10-24 13:00:41.164)
```javascript
{
  "action": "update",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "state": "tx_6jPYBUFTkcmPxVhJhGQsydPEsyApwNn7L5gFSG1hzf3pdBT3yLyPxn7RLcQgMFB9pZwK7jHEe7Bb2pNHGA9L1sQNkmjobXTmszLfwuwNctBQ11E82bS1AUKYSTZsS5afQ4fAg2UReLRm65SkTjYuGR9jpPrjGFehgEV8i59eMtaDCz8MznBKC3uCEyvp2y16vd6Ehy13zrB6RsgbTpzffi7X9KtouxpiyH5LPK6847VSEf4xdw9YDkFV4jLnTGmMxuYsogKdPWZHkUi14Mucub7NEyWp3dv5FeZJ4AA6be8rra7vmbAs2mkC8S5z7emSQvBA6uQh8KSxQdGazxWkDbPU5xe53NSaTvjHP"
  }
}
```

#### initiator: (2018-10-24 13:00:43.260)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-24 13:00:43.260)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-24 13:00:43.261)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-24 13:00:43.261)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-24 13:00:43.261)
> Channel is `open` and ready to use

#### responder: (2018-10-24 13:00:43.261)
> Channel is `open` and ready to use

#### initiator ---> (2018-10-24 13:00:43.302)
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

#### initiator <--- (2018-10-24 13:00:43.305)
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

#### initiator ---> (2018-10-24 13:00:43.306)
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

#### initiator <--- (2018-10-24 13:00:43.315)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQPT3Tq1947vh34qUzEcpAqRYbfNoT5CqfALMRFwi8cfZxzuVgLVXGYBbTKxPwhfD11enDSGbT6H5gYz84iTMwCR4T4M4ZqRPtzkSDHThkyRJLwhxxNNJRMsS3UmnkHafWJ8ygtb7qTyJMZbDFDvAYvnUbFV3iVQZrS11QAKz4yDqQz7udEcrt393RYBx5CB3N4GjBZvr2jAhm"
  },
  "tag": "update"
}
```

#### initiator ---> (2018-10-24 13:00:43.318)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4p5fRAEgQoG5CzUC2tJAPd83HphQ4W9vDy87L7JKG9fvw9xnjP1mEPg8H1Jd42yztRTVkfbsWn5aXhg7riAczkwj3HFxRXaHHRgEjJFj3E8GH27fMUceG2rKhnu7vjGt17PKSkbk9CLh1ZdoY6eprhuFsb5qKDFwaACdkK4mEybdwNH3ePiaxmmtJwYUmc4dv4SVoayCPQR9qobpWbwLtszqS9CZW4qmSZUtuWjm3o8NhpV2w8oBtQ5PEinkWGu8gkUDnm648twsX3N9NauTVvsqvj2wCK9eHdpZnTE5KzDDrLd"
  }
}
```

#### responder <--- (2018-10-24 13:00:43.329)
```javascript
{
  "action": "info",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "event": "update"
  }
}
```

#### responder <--- (2018-10-24 13:00:43.330)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQPT3Tq1947vh34qUzEcpAqRYbfNoT5CqfALMRFwi8cfZxzuVgLVXGYBbTKxPwhfD11enDSGbT6H5gYz84iTMwCR4T4M4ZqRPtzkSDHThkyRJLwhxxNNJRMsS3UmnkHafWJ8ygtb7qTyJMZbDFDvAYvnUbFV3iVQZrS11QAKz4yDqQz7udEcrt393RYBx5CB3N4GjBZvr2jAhm"
  },
  "tag": "update_ack"
}
```

#### responder ---> (2018-10-24 13:00:43.332)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak4pUC3QpeirFv5iHzkMu43HC6KmNoWB1ErM6utzHMfdbiTqEX9BEDKeA3iy7B2pmKvdrgYzQ7MEeY2vQYhnJ15RnEvkBeDaEEJqCco1jMh9WmvByvjBk1T5cRejEKFgF43nkYWwjtme2CEnLtoMjzuntnq8UzFGEzpRCPpvcXpnF49V4Y2YedfpmCwn8gbTCVEVp9QKqprYDiCtBoBoqNNH996HrJvkMMpvDt2VwRDDuv2tecYRy6P5nTh4MeDiL6i8RhNqcRvuec1o4Yt64fHHsGKC2sJ6qTCgfbxYhe66kVa8h"
  }
}
```

#### responder <--- (2018-10-24 13:00:43.339)
```javascript
{
  "action": "update",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkRW6v6tQC9Ym5SA7crpjiJcPm3xbhXnzRnvxMowCiCsyj5B1F9Q9tmcRGYkFkDRNvo8z35NEBavKMAsCvTMzQciJ9PJ83UoybqSCQg2V2YALPvdSFzjXTz1xRy1Vk13qtv4HjuCBYVR7uWTds137HxwNNdDhi381JvwAJNpZDhQgfza5seKQ7h6hybSpcHA2U16LqtcWcSf9HnSDj9GinBF6ZHfxDK3peag8dhYr9k7jzkPdKXRrXatGF7WAcJXtkQFeBNaKMh5aDM9pojrM9M6sP8cWZtPHzQx3KbsVrVuwiART7CCu3MAit6niJ91U94sETWAFNRgmp5kGEN9t9y7bMKE2JrLbyjHY1Qo492FG7xFEhSRrXPvH7H8kDbQxcUAH1yWAM"
  }
}
```

#### initiator <--- (2018-10-24 13:00:43.340)
```javascript
{
  "action": "update",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkRW6v6tQC9Ym5SA7crpjiJcPm3xbhXnzRnvxMowCiCsyj5B1F9Q9tmcRGYkFkDRNvo8z35NEBavKMAsCvTMzQciJ9PJ83UoybqSCQg2V2YALPvdSFzjXTz1xRy1Vk13qtv4HjuCBYVR7uWTds137HxwNNdDhi381JvwAJNpZDhQgfza5seKQ7h6hybSpcHA2U16LqtcWcSf9HnSDj9GinBF6ZHfxDK3peag8dhYr9k7jzkPdKXRrXatGF7WAcJXtkQFeBNaKMh5aDM9pojrM9M6sP8cWZtPHzQx3KbsVrVuwiART7CCu3MAit6niJ91U94sETWAFNRgmp5kGEN9t9y7bMKE2JrLbyjHY1Qo492FG7xFEhSRrXPvH7H8kDbQxcUAH1yWAM"
  }
}
```

#### initiator ---> (2018-10-24 13:00:43.344)
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

#### initiator <--- (2018-10-24 13:00:43.345)
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

#### initiator ---> (2018-10-24 13:00:43.346)
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

#### initiator <--- (2018-10-24 13:00:43.347)
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

#### responder ---> (2018-10-24 13:00:43.347)
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

#### responder <--- (2018-10-24 13:00:43.351)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQPT3Tq1947vh34qUzEcpAqRYbfNoT5CqfALMRFwi8cfZxzzvCC34jjXKP5ww4bnHV41wC8i8pHec2ZKZjFFmBFWurU8sr4b8ncofTEKAEZ5NbujG8FkJ9cN4oaxvoLM67VhLXodTshgv3tzXnKPGijb7MxkdmsmmnAAf5MYn6Q6uk1ZUGbmf8ZmVwtqNacc3rNsSZfzqHEANW"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 13:00:43.352)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak5C6JqiCfNSDPFpzKXL4yqFfh8TrpTMpikaM9hvBPM7aM3ahEj3EboqEpK6jw3CmaFtF3DnLCoXn5tFEAuvEwQCA4AJKkqPqs5h8NW8PsysNKbFrHN358Zt442Mq6Snb4DzEnpMcVPt4asZoPVwk9znAKbbp9R2QLCx8mYRnzNt57mEfnZ897v3ktScLUjFvUcfo6aaNogeE8rhGg3opoqgYL6GZxub1CX8DVEmsTNqbryDeU7TXPWiGWNWZtopr8v2rMyPVKFTmAj11Kh4TdsQjJBEr1D4QGrMfNsZBaLE9ex4u"
  }
}
```

#### initiator <--- (2018-10-24 13:00:43.355)
```javascript
{
  "action": "info",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 13:00:43.356)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQPT3Tq1947vh34qUzEcpAqRYbfNoT5CqfALMRFwi8cfZxzzvCC34jjXKP5ww4bnHV41wC8i8pHec2ZKZjFFmBFWurU8sr4b8ncofTEKAEZ5NbujG8FkJ9cN4oaxvoLM67VhLXodTshgv3tzXnKPGijb7MxkdmsmmnAAf5MYn6Q6uk1ZUGbmf8ZmVwtqNacc3rNsSZfzqHEANW"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 13:00:43.356)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak4p1uK4joZuWjLd7a7ffBHm5xzheX58UhZxnNtdi5VTL7DECE6kTwhJbQ4XA2ZShTfTHWYf5EWccQpQAYsjnXHGbQErh95P8Cu9PwaNnLCUqixqSuCG6gdq2YQotgArZdJGwa4W8Zx7zXHJsbNxu1ezbw68ZxgxgH2C1jiBdkpe7WmAZpqAdMsD7kGqXwHfzzXu4ALrDGkx62fSLUH3t4fjmvVvbopUkrCjWNcENZZd2hooPvA8cvJ4FTinpCUoDebcntJc5nEUefBLeivVjUg6xPgGsM3hgNEwHviS6k5UGxowU"
  }
}
```

#### initiator <--- (2018-10-24 13:00:43.360)
```javascript
{
  "action": "update",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkRPdxTxUwWA5qcju7zT7TM1wJVdTXWGfhttrgFibWHvVRQ1msyameU7yds3NKWajrpp7n1jFXw2T5MCRpF9Lbue1wCi84tBeu2FrZ2raQwCW67BzzDgqEC3zacDvei8xMHA4DqFQ3yhAMmo2QDjZ118pSKLwMusCprf6Ecva78SyiqN935ayzeHR9Dui59XZtY39cAefnb3asXvPqWpGE57CDoUqpuz4HCaiaTJfD7vpDhDfyySqDVZzrhyJgquXBSRDvsPwdxJVA5tPoWyP3rJkTQmpMipfV1Uwhw2DWvEcJyyFmpoKuhooBzoFX4PNhRFPmytYchCF4CmzLU7m8J5H6tDynwE4taQENZvJFb35yM1GYxWLN97tAJHapUCJnUsfQiNBt"
  }
}
```

#### responder <--- (2018-10-24 13:00:43.360)
```javascript
{
  "action": "update",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkRPdxTxUwWA5qcju7zT7TM1wJVdTXWGfhttrgFibWHvVRQ1msyameU7yds3NKWajrpp7n1jFXw2T5MCRpF9Lbue1wCi84tBeu2FrZ2raQwCW67BzzDgqEC3zacDvei8xMHA4DqFQ3yhAMmo2QDjZ118pSKLwMusCprf6Ecva78SyiqN935ayzeHR9Dui59XZtY39cAefnb3asXvPqWpGE57CDoUqpuz4HCaiaTJfD7vpDhDfyySqDVZzrhyJgquXBSRDvsPwdxJVA5tPoWyP3rJkTQmpMipfV1Uwhw2DWvEcJyyFmpoKuhooBzoFX4PNhRFPmytYchCF4CmzLU7m8J5H6tDynwE4taQENZvJFb35yM1GYxWLN97tAJHapUCJnUsfQiNBt"
  }
}
```

#### initiator ---> (2018-10-24 13:00:43.362)
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

#### initiator <--- (2018-10-24 13:00:43.363)
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

#### initiator ---> (2018-10-24 13:00:43.364)
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

#### initiator <--- (2018-10-24 13:00:43.364)
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

#### responder ---> (2018-10-24 13:00:43.365)
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

#### responder <--- (2018-10-24 13:00:43.367)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQPT3Tq1947vh34qUzEcpAqRYbfNoT5CqfALMRFwi8cfZy16Li3acCvs3JqwUBVu8UqKTvh9htGLW9yNTMAjWrzGWsxQHxjSW3GkQcKks2HrThbNDkkocaVcgjsPWW3bxmRhTr2aKoHFdTaN22hkE9EBNcGRBrLMrBbtJ87msDgsUKTbbaDCHi5nw1g7ckcKpvJpxMJphXjsu3"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 13:00:43.368)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak5AhGmcT5sfVq8NZzJtVXxsLQEhBtB9vYgWeH9hKosdBHGYfSHzjS9hynB3KXU7JsPHTNVaqqubQrg2AbALxj5zbz9jDASGzGyxcFzig8YDMPhvs85QvNiGhPYhmidDGcQwWnyMMDA82HRhG2AUqkwmV6rfLLRPjcRmG6RTVbGj4tVUxrpn7DE4tTcoim8dpSyZket2TtecN7QHPQbidv71zkuAF9hRuvLDC8xY65ct1EKXz6w3fVN2Vn4HGi1mcb3TGr3EtWtuMREMCDQzQ8oXTTgsp1b26giHouArsDoijphke"
  }
}
```

#### initiator <--- (2018-10-24 13:00:43.371)
```javascript
{
  "action": "info",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 13:00:43.371)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQPT3Tq1947vh34qUzEcpAqRYbfNoT5CqfALMRFwi8cfZy16Li3acCvs3JqwUBVu8UqKTvh9htGLW9yNTMAjWrzGWsxQHxjSW3GkQcKks2HrThbNDkkocaVcgjsPWW3bxmRhTr2aKoHFdTaN22hkE9EBNcGRBrLMrBbtJ87msDgsUKTbbaDCHi5nw1g7ckcKpvJpxMJphXjsu3"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 13:00:43.372)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak4vWLzr1GTqahRg5eYprH3VEbvjzpz8wufPfyN13ej9foXM4Zt9HXMEdN5ifsQWZ4m4DQfYmnyH8JpTrhAF9ZdL2VHFK7ALkreNZNs3xTNuzwK6nJ2Tzd4NYxNMnBWACNxvv1WNqs8hn57updBgyo52whaJLJ9pgY3drjoeSvSu5vnYmygtCxNYwJ6xvdtNRaoVghMsFKggVyPLwbF7zMcDo4uqw6M9ZssBicxPWLo6CVrtggFBNfBmqH9Pq79ojN3veQYeePAF45d97BKjMkKk6zFNanhQ7mYMfp71oncj6Qocr"
  }
}
```

#### initiator <--- (2018-10-24 13:00:43.376)
```javascript
{
  "action": "update",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkcYojDYYimagdd4kpigNWFxazVbLoSkqRmeZZaN88H5yCqRyyKmDE88PNYypQMrWErvbuBn4bZmLh4kank2C6Pf5GTT5DPmFJNByxBt9xnMuEzskWe9mRuJfNVyzw38A7N117xAxZm1YxgFQf4hNwX6aiLfVgvi5hpdKChqdP79PQk68bpqAUegcoTjdVPUuDTVCpaG2oiuAgYeJBn4NayiouTTDTWodu7Gwz7F9vkaUNZ4WwUUVXrZj6mRxf73WUEyKSXcJg1GqBvjqqfmSXwdyQbbyZ1jtLFkiNj81bgM498rBKcZuKmyWqSqzgeZ1S1WgVwphRDosdht864pCvg5FmHgi2dxy2kTjsVJzZ7VKVjrQjf7nqeF7rpUgcyQaeNojTSPaF"
  }
}
```

#### responder <--- (2018-10-24 13:00:43.376)
```javascript
{
  "action": "update",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkcYojDYYimagdd4kpigNWFxazVbLoSkqRmeZZaN88H5yCqRyyKmDE88PNYypQMrWErvbuBn4bZmLh4kank2C6Pf5GTT5DPmFJNByxBt9xnMuEzskWe9mRuJfNVyzw38A7N117xAxZm1YxgFQf4hNwX6aiLfVgvi5hpdKChqdP79PQk68bpqAUegcoTjdVPUuDTVCpaG2oiuAgYeJBn4NayiouTTDTWodu7Gwz7F9vkaUNZ4WwUUVXrZj6mRxf73WUEyKSXcJg1GqBvjqqfmSXwdyQbbyZ1jtLFkiNj81bgM498rBKcZuKmyWqSqzgeZ1S1WgVwphRDosdht864pCvg5FmHgi2dxy2kTjsVJzZ7VKVjrQjf7nqeF7rpUgcyQaeNojTSPaF"
  }
}
```

#### initiator ---> (2018-10-24 13:00:43.378)
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

#### initiator <--- (2018-10-24 13:00:43.379)
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

#### initiator ---> (2018-10-24 13:00:43.380)
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

#### initiator <--- (2018-10-24 13:00:43.380)
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

#### initiator ---> (2018-10-24 13:00:43.381)
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

#### initiator <--- (2018-10-24 13:00:43.383)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQPT3Tq1947vh34qUzEcpAqRYbfNoT5CqfALMRFwi8cfZy1BmDu89g8CmEbw1JQ1jzMZNR7bJf2Ln4o8nvUtczQfsXX9JuqyVexafgZnp8BkZdzcqqsYFi1dHrL3XrRMHU69MdZRhcCfSabhfzP12pQZGLAUeyaVxFqsPCMZjMMfkwK8d9NT5233ZEj95rHWvFNNtVD2fsjF4y"
  },
  "tag": "update"
}
```

#### initiator ---> (2018-10-24 13:00:43.384)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4pGWU9iYJ1rWyam2Um76rDoNP1AbyxHV9eW1RWmoALiEQWwsdyTGdcA2NjzHaY7sjAiL6pp3rxFsN8uTJ99U9nfbhXQ83AL5nxEmuqQrnj2S5Dy9N2tXoFWQv7h5bULsGoBeWrahG6SGi7XtH56Em4W6yyU97q36FNYdDnVdbrarcf8BSmg1c2c38g2Y7a61H1n4ujMDUEENe9XeeZFWxo4uJMf6Zgm81DVXxQv3ngpbCycunFysfW3RqKRtP7nSs7zgkjdRCWwfHcDqECi2cQEycyjSmWpY9sFvVYf225drgbD"
  }
}
```

#### responder <--- (2018-10-24 13:00:43.418)
```javascript
{
  "action": "info",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "event": "update"
  }
}
```

#### responder <--- (2018-10-24 13:00:43.419)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQPT3Tq1947vh34qUzEcpAqRYbfNoT5CqfALMRFwi8cfZy1BmDu89g8CmEbw1JQ1jzMZNR7bJf2Ln4o8nvUtczQfsXX9JuqyVexafgZnp8BkZdzcqqsYFi1dHrL3XrRMHU69MdZRhcCfSabhfzP12pQZGLAUeyaVxFqsPCMZjMMfkwK8d9NT5233ZEj95rHWvFNNtVD2fsjF4y"
  },
  "tag": "update_ack"
}
```

#### responder ---> (2018-10-24 13:00:43.420)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak4nZAgmLN4H25Gd3dEJkdmtQwFZP8kPDppi1cZ1Fkw7yTVQHbdVDuDBfWGjSLrovcDbYXHF2BJ3XaUveKArvMGTeeFSVe35nXKb1ZkqW3JAM1F4uhbZmjQNDCV6dmYXRwQzeV89diZMjC579UDYkHjPDoRgTpHgaVZWm6ucHEkEMv6Y1FsoCJKVkikdvCGHR1YNpMfeW4Mvy8qgD5o4pXCsoaCGAv9ZTj6HdsVBAroQBwgFGby1GXqR8ux7KoUmEm4MLVBfh2wBxsTbLtnieCCYcP5R2DFy8tH5EUdnKPY1zbdnN"
  }
}
```

#### responder <--- (2018-10-24 13:00:43.423)
```javascript
{
  "action": "update",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkNsxtaiiYis8MxquPQKyySmVSZjvsYJJbmYnVd3ebQAebNWbkkmx5PkA7AzmQjXJsGbTyMAYTLyEfSfMCdo7PGvosADRe9BMHyefLDoaWBWbDUGU2a3yeL43JaqhyXdWhDy8zFAC9KXtxtMBGmbWMC8XF3HaG7CsWN123YnFyoBnNZkVqJ9kir4G89EfjNSxRVf2aWwAomAhYD6ZSK9doujZYhXtjt55neqoWU1YoqTn29cGfZrJWhkp4TcpoURrVJSWYUZrRTvUxVCzmxJQL39ic728pMbR1ap6A5CbNmKPWMtWozeTkDeJ399f7wydwcoKz12bau7NRByJJ1DkFVsNfPJrEF2Q5uXeDTvS7X9VHgtSzmjJ5E9bGhBh4vrDTaT6ZjWYw"
  }
}
```

#### initiator <--- (2018-10-24 13:00:43.424)
```javascript
{
  "action": "update",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkNsxtaiiYis8MxquPQKyySmVSZjvsYJJbmYnVd3ebQAebNWbkkmx5PkA7AzmQjXJsGbTyMAYTLyEfSfMCdo7PGvosADRe9BMHyefLDoaWBWbDUGU2a3yeL43JaqhyXdWhDy8zFAC9KXtxtMBGmbWMC8XF3HaG7CsWN123YnFyoBnNZkVqJ9kir4G89EfjNSxRVf2aWwAomAhYD6ZSK9doujZYhXtjt55neqoWU1YoqTn29cGfZrJWhkp4TcpoURrVJSWYUZrRTvUxVCzmxJQL39ic728pMbR1ap6A5CbNmKPWMtWozeTkDeJ399f7wydwcoKz12bau7NRByJJ1DkFVsNfPJrEF2Q5uXeDTvS7X9VHgtSzmjJ5E9bGhBh4vrDTaT6ZjWYw"
  }
}
```

#### initiator ---> (2018-10-24 13:00:43.426)
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

#### initiator <--- (2018-10-24 13:00:43.427)
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

#### initiator ---> (2018-10-24 13:00:43.428)
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

#### initiator <--- (2018-10-24 13:00:43.429)
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

#### responder ---> (2018-10-24 13:00:43.429)
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

#### responder <--- (2018-10-24 13:00:43.432)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQPT3Tq1947vh34qUzEcpAqRYbfNoT5CqfALMRFwi8cfZy1HBjkfh9KYVAMvYRJ8pUPvXPp2r2DiJQoUEb1h2ETmivvw8C59EYadtvWeGbmQdtxe91kvFSG7vcSEfuU7i5HhiUUU3eSP4Gw6zXUU8zDMu6skG4znbwtxQHTEnEoaz4Huv5reiEvfNRUXYjYkVW7sxHgVfpgTno"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 13:00:43.432)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak5AxN3DvqBZ6mqJmrJXeTkrxVqdsooidL28tMgu2n25nqYv8x8mAA2pPpokVN2sHhXiCWZCjY7oSVHUkVHNE8ua9tTMnckApK4jrid6vBeubCztsHgY78zZd6QgahjLw87dTYcDfazr9vvVrQJADWQDFLM8GfuqCUSfjmNTpfZLDfgxSCvmJ5MEjg9svve58CaJ1ApnWJkXjWwQigWMEQ4gPLC4Vb7J3AkjQ6RhVbyDwMxYGpXzxy4w86mHEk5zVzsa8QcTREK9sJm28gBMX8bDcveGGZoH7nXZ7VP6btn3dTWXz"
  }
}
```

#### initiator <--- (2018-10-24 13:00:43.472)
```javascript
{
  "action": "info",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 13:00:43.474)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQPT3Tq1947vh34qUzEcpAqRYbfNoT5CqfALMRFwi8cfZy1HBjkfh9KYVAMvYRJ8pUPvXPp2r2DiJQoUEb1h2ETmivvw8C59EYadtvWeGbmQdtxe91kvFSG7vcSEfuU7i5HhiUUU3eSP4Gw6zXUU8zDMu6skG4znbwtxQHTEnEoaz4Huv5reiEvfNRUXYjYkVW7sxHgVfpgTno"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 13:00:43.476)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak4ywC5WrF4awv3ASNiaah529aiExbvUbrWmtnLqxEjPnRr3B7A8ZiihfPc6qGQ328NweEHHR9pT8qLZthCyx5E9fRkxAjBQtrdVQ6rRA4hxbScvNGFrMXRzGt3gr4Lg7bCcHn9rFL3iAn26GTdyRz6amMwYYZ7HuNW9BxMxhy7k8SRwEVf9NbJj7iVS3VBpPdsnHquStSG65iJ6DYiLgwMUzZqZPrcwab7B3RSwzzcH9BLGhYjuCRzpLzxEZqpGeeJCrKjoviEbTAMp2GhxC2yALcjQ9Ki1NEefKBVTpCo35yKb7"
  }
}
```

#### initiator <--- (2018-10-24 13:00:43.489)
```javascript
{
  "action": "update",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkiSf2iGb68y6KL5oajspN6qYyA3uJ9jSaghLFBo8J7MoBz6t24ZBGaEQcqFdv8FWQmLfWCvLmVo2NyxrhwsABdmyubT8zxNYDDb7nSBZMCGbjLxZ59h5gPbg5Pri1FXBGp1cwsq6f8EdcMuAfd8R1mRDba7sdVCy5vkNbEGFzotCHuUsRZX8PLHMy9zg2xmRTfbA971RT37ns4DwtKSXzRUu22qpbPuYXddpYpeQbx1LTPm5NXNkjXCyZUQxsZAqTNU7xZ8BQaYZphQmkud7ARNn1DSmnws4dnjoiXuMcRVDg1qxCUY2Tt25t8rHfNdBeCohovqE5qmJa6XbU5s8ywqsq4K9LCDwT3wRATnt2p7NbF31JY79cVFMnvvJepfqA6Vw2Dru4"
  }
}
```

#### responder <--- (2018-10-24 13:00:43.490)
```javascript
{
  "action": "update",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkiSf2iGb68y6KL5oajspN6qYyA3uJ9jSaghLFBo8J7MoBz6t24ZBGaEQcqFdv8FWQmLfWCvLmVo2NyxrhwsABdmyubT8zxNYDDb7nSBZMCGbjLxZ59h5gPbg5Pri1FXBGp1cwsq6f8EdcMuAfd8R1mRDba7sdVCy5vkNbEGFzotCHuUsRZX8PLHMy9zg2xmRTfbA971RT37ns4DwtKSXzRUu22qpbPuYXddpYpeQbx1LTPm5NXNkjXCyZUQxsZAqTNU7xZ8BQaYZphQmkud7ARNn1DSmnws4dnjoiXuMcRVDg1qxCUY2Tt25t8rHfNdBeCohovqE5qmJa6XbU5s8ywqsq4K9LCDwT3wRATnt2p7NbF31JY79cVFMnvvJepfqA6Vw2Dru4"
  }
}
```

#### initiator ---> (2018-10-24 13:00:43.496)
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

#### initiator <--- (2018-10-24 13:00:43.498)
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

#### responder ---> (2018-10-24 13:00:43.552)
```javascript
{
  "action": "deposit",
  "payload": {
    "amount": 2
  }
}
```

#### responder <--- (2018-10-24 13:00:43.557)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_2C9es4FjHtC9cjEgpshT7NBD6NWVEdqnTwTRwSisF3UKYCtsEoR48Sow8pUrWxLZhePFaMWfukho1UZ8zC1koAZHmD6CfzkLMe5QPUbuEcURcU3wnWz26SzoW89s13qsfuG88Vv5oSsp3shcPUy3LncVTXdfPf"
  },
  "tag": "deposit_tx"
}
```

#### responder ---> (2018-10-24 13:00:43.558)
```javascript
{
  "action": "deposit_tx",
  "payload": {
    "tx": "tx_2WsEQsiC5Xsn9eWE8ruRoEKMpUW36eJn76jE8JwSHD2cvbxkXza87vuAawP2mUtkAQwdtspgqGaA5ZHt4jmYfzFDiZEMAdeEtJX86F4ndXpUwGJiVHc495K8Rk9YmjvuoVRwsmJZvE4HBNx3xCvUirtpTdgtmJo2XsCW5AUdWqVSgGm1uzwTZeAptfm9DtQgAqKFtnHfMYb8js3LGLRCLYbGCr2tSnb8DAaiSYsRE3gCSBR6uJkh8UoFur5DUpZSF32"
  }
}
```

#### initiator <--- (2018-10-24 13:00:43.559)
```javascript
{
  "action": "info",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "event": "deposit_created"
  }
}
```

#### initiator <--- (2018-10-24 13:00:43.559)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_2C9es4FjHtC9cjEgpshT7NBD6NWVEdqnTwTRwSisF3UKYCtsEoR48Sow8pUrWxLZhePFaMWfukho1UZ8zC1koAZHmD6CfzkLMe5QPUbuEcURcU3wnWz26SzoW89s13qsfuG88Vv5oSsp3shcPUy3LncVTXdfPf"
  },
  "tag": "deposit_ack"
}
```

#### initiator ---> (2018-10-24 13:00:43.560)
```javascript
{
  "action": "deposit_ack",
  "payload": {
    "tx": "tx_2WsEQsiC5XsnZewbhQ8vfn2BY6VBHHWQG1PGrGNEsg5YxdyJ9fLKiVRUmsHG77tkvkAZpp3hHKE7Ru7Buyo4phFr8unYSAMfAwP9G7ArNeGGiYzEnmedCRQL3W3TUzu5jCMFo2Pys8sTMxtT4XgBR27uqwDv8Z2dgai948uuYT9psgbhhixxrNybEMDoQSBHhVyiPDYraSJrXnDUnd2f15g72odFD94shKTkCRitq77w8H8Qe2PwwmqeQgYjFzHxbN7"
  }
}
```

#### initiator <--- (2018-10-24 13:00:43.562)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "tx": "tx_3cDMp6242sByzStCfnEoLGsJiksQ296i2CVy3Vm3F6yLUfd6xLNYVrQhzWi84TdpB7DTAgkcEEBxQR9LWY5VzeJjHyoF3EDFurcXmuUuUiz6oLjLjbgQscDPPq5ZqkjvXjX8tXX9uDm7aSd77SKiRQur1e1YQXgrsZicUoQtebuSUfQr7qjnJ1bDWqkHvVbnGTQRu2vgJkvzKMQMgNy42BMxKMkEuKRbBAGp2nQe5whEJpsX5P8La5uVdcUmTosQRe1teUZLoUTwxL5wZUp7CAvb297KXwGvB1RA3UxVLpvBusibBsmi73aC1BanxKTzMsaJm8ySyLLkiAKX9XUnW6QhTiKbb"
  }
}
```

#### responder <--- (2018-10-24 13:00:43.562)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "tx": "tx_3cDMp6242sByzStCfnEoLGsJiksQ296i2CVy3Vm3F6yLUfd6xLNYVrQhzWi84TdpB7DTAgkcEEBxQR9LWY5VzeJjHyoF3EDFurcXmuUuUiz6oLjLjbgQscDPPq5ZqkjvXjX8tXX9uDm7aSd77SKiRQur1e1YQXgrsZicUoQtebuSUfQr7qjnJ1bDWqkHvVbnGTQRu2vgJkvzKMQMgNy42BMxKMkEuKRbBAGp2nQe5whEJpsX5P8La5uVdcUmTosQRe1teUZLoUTwxL5wZUp7CAvb297KXwGvB1RA3UxVLpvBusibBsmi73aC1BanxKTzMsaJm8ySyLLkiAKX9XUnW6QhTiKbb"
  }
}
```

#### initiator <--- (2018-10-24 13:00:54.899)
```javascript
{
  "action": "info",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "event": "own_deposit_locked"
  }
}
```

#### initiator <--- (2018-10-24 13:00:54.900)
```javascript
{
  "action": "info",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "event": "deposit_locked"
  }
}
```

#### responder <--- (2018-10-24 13:00:54.900)
```javascript
{
  "action": "info",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "event": "own_deposit_locked"
  }
}
```

#### responder <--- (2018-10-24 13:00:54.900)
```javascript
{
  "action": "info",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "event": "deposit_locked"
  }
}
```

#### initiator <--- (2018-10-24 13:00:54.903)
```javascript
{
  "action": "update",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "state": "tx_3cDMp6242sByzStCfnEoLGsJiksQ296i2CVy3Vm3F6yLUfd6xLNYVrQhzWi84TdpB7DTAgkcEEBxQR9LWY5VzeJjHyoF3EDFurcXmuUuUiz6oLjLjbgQscDPPq5ZqkjvXjX8tXX9uDm7aSd77SKiRQur1e1YQXgrsZicUoQtebuSUfQr7qjnJ1bDWqkHvVbnGTQRu2vgJkvzKMQMgNy42BMxKMkEuKRbBAGp2nQe5whEJpsX5P8La5uVdcUmTosQRe1teUZLoUTwxL5wZUp7CAvb297KXwGvB1RA3UxVLpvBusibBsmi73aC1BanxKTzMsaJm8ySyLLkiAKX9XUnW6QhTiKbb"
  }
}
```

#### responder <--- (2018-10-24 13:00:54.903)
```javascript
{
  "action": "update",
  "channel_id": "ch_bzPcPxFAoEa3vU7kjQ9gWHAP94xe9JE7YW8aWJ4raUFNBaKCL",
  "payload": {
    "state": "tx_3cDMp6242sByzStCfnEoLGsJiksQ296i2CVy3Vm3F6yLUfd6xLNYVrQhzWi84TdpB7DTAgkcEEBxQR9LWY5VzeJjHyoF3EDFurcXmuUuUiz6oLjLjbgQscDPPq5ZqkjvXjX8tXX9uDm7aSd77SKiRQur1e1YQXgrsZicUoQtebuSUfQr7qjnJ1bDWqkHvVbnGTQRu2vgJkvzKMQMgNy42BMxKMkEuKRbBAGp2nQe5whEJpsX5P8La5uVdcUmTosQRe1teUZLoUTwxL5wZUp7CAvb297KXwGvB1RA3UxVLpvBusibBsmi73aC1BanxKTzMsaJm8ySyLLkiAKX9XUnW6QhTiKbb"
  }
}
```
