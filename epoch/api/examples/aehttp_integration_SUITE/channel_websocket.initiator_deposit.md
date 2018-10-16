
#### initiator init (2018-10-16 20:25:54.825)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A&role=initiator
```

#### responder init (2018-10-16 20:25:54.830)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A&role=responder
```

#### responder <--- (2018-10-16 20:25:55.833)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 20:25:55.836)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 20:25:55.845)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpALFUXGGsdug6Jrs56usDVK43SheHuLKP3h48aDzajQnhSXBUWq2rVDufMiousdvbextEcPQPuUq7817TtZyDq2vCt4rqTh3SqYy9jCHBN6SuCufA4j65Xrud4Spcwoi5gsMaowEXQETWMtFFZcbw7DeBonvFBkz"
  }
}
```

#### initiator ---> (2018-10-16 20:25:55.885)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HnBBJEgJZ4a9qNeywpEmGcNdvw2NxEWwnjCxUP9YyiExxuPzYHnDTgkY3paxG6sLn3xfGaNeXnq3Q5wpXMoQGJRsvVph3DGR8f9tx61mjyJ6ExsSUk41Ws25zp3zV4EeALwiz15K2gWBgELCBJWnF9pgE2y31jA8SeW9dKwtGG5Bicss6SBfB51FRS8FRzBoiTxhE6ZjrYok5JVHKBQSntwhme9hbjrdXbeFEmVhTkRAMKU3t7Z4BWUaYwiBu7B7s"
  }
}
```

#### responder <--- (2018-10-16 20:25:55.886)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 20:25:55.887)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpALFUXGGsdug6Jrs56usDVK43SheHuLKP3h48aDzajQnhSXBUWq2rVDufMiousdvbextEcPQPuUq7817TtZyDq2vCt4rqTh3SqYy9jCHBN6SuCufA4j65Xrud4Spcwoi5gsMaowEXQETWMtFFZcbw7DeBonvFBkz"
  }
}
```

#### responder ---> (2018-10-16 20:25:55.888)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HoF7Wh4U1qJLZfsKGSJrA2NDsteWjKYE3DqbqVjbv2zLRFGUBLibp89PUWRL3kpmiAywBphC3SiD5hdnx3AkD1CGBKa2VECJvCFfdsJYiWtFsVDNzEZjMLHMMGqKRHLcR5aRcLtGdbsY8WPuhEXRgSZ2yihLAo5amgBiXnc64LVooGAVgatUefsYeg5TMWKosKrRZMtmWevN4wcTdYMvTpAcERSScsv2nXGpjPfYu9mnPuvUJyTuGvSvWabZTJSfC"
  }
}
```

#### initiator <--- (2018-10-16 20:25:55.891)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 20:25:55.892)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmRwvJgicR3AtGxv5mesf4Aej7DLTDGaHbJRtUN3FT82UfuPa1fcnEb4Tdg9dDAxrggLAS4WyX3siBHLUbPpfJnxBAkirhvaFw1sGsFrHut9v6tEDX3WadqcqDbgsd1cnHazXV9NExbDHW8j6LFmL6fg7wSjSaU6jga2JEunFQuDQv6mBv8VuUj9i2TW5K1wgH2qFetGH4QYhKM58bSHMphXBFeDJeqGqn1Mi7s9S3JfhrjnfpEUvy1Et2aXmxAxRWYB3Ej6Y2HmZZ8riJ2ggUhABihdmbYvdQUC5KsX2dpEzCWqbyHeh7e9pQ6hdLtpJcDs2pipkZwMuXDShG4gDWKP5QN8"
  }
}
```

#### initiator <--- (2018-10-16 20:25:55.893)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmRwvJgicR3AtGxv5mesf4Aej7DLTDGaHbJRtUN3FT82UfuPa1fcnEb4Tdg9dDAxrggLAS4WyX3siBHLUbPpfJnxBAkirhvaFw1sGsFrHut9v6tEDX3WadqcqDbgsd1cnHazXV9NExbDHW8j6LFmL6fg7wSjSaU6jga2JEunFQuDQv6mBv8VuUj9i2TW5K1wgH2qFetGH4QYhKM58bSHMphXBFeDJeqGqn1Mi7s9S3JfhrjnfpEUvy1Et2aXmxAxRWYB3Ej6Y2HmZZ8riJ2ggUhABihdmbYvdQUC5KsX2dpEzCWqbyHeh7e9pQ6hdLtpJcDs2pipkZwMuXDShG4gDWKP5QN8"
  }
}
```

#### initiator <--- (2018-10-16 20:25:56.756)
```javascript
{
  "id": -576460752303423441,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "balance": 699
    },
    {
      "account": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "balance": 401
    }
  ]
}
```

#### responder <--- (2018-10-16 20:25:57.765)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### initiator <--- (2018-10-16 20:25:57.766)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### initiator <--- (2018-10-16 20:25:57.766)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### responder <--- (2018-10-16 20:25:57.766)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### initiator <--- (2018-10-16 20:25:57.771)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### responder <--- (2018-10-16 20:25:57.771)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### initiator <--- (2018-10-16 20:25:57.772)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmRwvJgicR3AtGxv5mesf4Aej7DLTDGaHbJRtUN3FT82UfuPa1fcnEb4Tdg9dDAxrggLAS4WyX3siBHLUbPpfJnxBAkirhvaFw1sGsFrHut9v6tEDX3WadqcqDbgsd1cnHazXV9NExbDHW8j6LFmL6fg7wSjSaU6jga2JEunFQuDQv6mBv8VuUj9i2TW5K1wgH2qFetGH4QYhKM58bSHMphXBFeDJeqGqn1Mi7s9S3JfhrjnfpEUvy1Et2aXmxAxRWYB3Ej6Y2HmZZ8riJ2ggUhABihdmbYvdQUC5KsX2dpEzCWqbyHeh7e9pQ6hdLtpJcDs2pipkZwMuXDShG4gDWKP5QN8",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### responder <--- (2018-10-16 20:25:57.773)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmRwvJgicR3AtGxv5mesf4Aej7DLTDGaHbJRtUN3FT82UfuPa1fcnEb4Tdg9dDAxrggLAS4WyX3siBHLUbPpfJnxBAkirhvaFw1sGsFrHut9v6tEDX3WadqcqDbgsd1cnHazXV9NExbDHW8j6LFmL6fg7wSjSaU6jga2JEunFQuDQv6mBv8VuUj9i2TW5K1wgH2qFetGH4QYhKM58bSHMphXBFeDJeqGqn1Mi7s9S3JfhrjnfpEUvy1Et2aXmxAxRWYB3Ej6Y2HmZZ8riJ2ggUhABihdmbYvdQUC5KsX2dpEzCWqbyHeh7e9pQ6hdLtpJcDs2pipkZwMuXDShG4gDWKP5QN8",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### initiator: (2018-10-16 20:25:57.920)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-16 20:25:57.920)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-16 20:25:57.920)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-16 20:25:57.920)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-16 20:25:57.920)
> Channel is `open` and ready to use

#### responder: (2018-10-16 20:25:57.920)
> Channel is `open` and ready to use

#### initiator <--- (2018-10-16 20:25:57.956)
```javascript
{
  "id": -576460752303423440,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "balance": 699
    },
    {
      "account": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "balance": 401
    }
  ]
}
```

#### initiator ---> (2018-10-16 20:25:57.956)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
    "to": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A"
  }
}
```

#### initiator <--- (2018-10-16 20:25:57.964)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTiKBfWYDbYaLuN9aWEsEwRA9cKUgJbrpZZeqFf9ETwfAcVBWAhxbXG2coTgogb2qzcsHm8jYXWoB5uPKby53YW2iDhdqBR4SQuAMyTRnzKpk6V7bqnf6W9TK2tKkwHtregUTRoGnsBFYWiRwMQJLyu3gma7aEhjkGgUyAkDE3mWU5t3niLhVnT1ZqDKnkAr44fdfKgfPKQek"
  }
}
```

#### initiator ---> (2018-10-16 20:25:57.966)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4u7ok7YzAH7MUvuUFndz9fxjti5mg7JsL81mVjpxUSxPiPAogvC41MhDDmjr34C5cVWzzrvVBJGB6RzQwhEvUQEV6pX4JpJtkPuFax3c1ywQK7peom5b832msrshDxZbXJ9wF1V6yVeptTqUfy5Po8P15QhZrD3qnNh9XDpLce68eE8J3JViZRkQsRaT3NnJAmn5Zgiz8ZLe738rY43gmMYci7KYHWXvnj3yxwehGo6eYJBCXQpuZ2fDvxDVhWgFMUtk7xX1D6F7BbGXYeQbM11cfpkFeMDLM4uDxkTXUJeodVf"
  }
}
```

#### responder <--- (2018-10-16 20:25:57.972)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### responder <--- (2018-10-16 20:25:57.973)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTiKBfWYDbYaLuN9aWEsEwRA9cKUgJbrpZZeqFf9ETwfAcVBWAhxbXG2coTgogb2qzcsHm8jYXWoB5uPKby53YW2iDhdqBR4SQuAMyTRnzKpk6V7bqnf6W9TK2tKkwHtregUTRoGnsBFYWiRwMQJLyu3gma7aEhjkGgUyAkDE3mWU5t3niLhVnT1ZqDKnkAr44fdfKgfPKQek"
  }
}
```

#### responder ---> (2018-10-16 20:25:57.974)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4osEWfvuC3EnRL5pN3qGXJYcNatzLisD1c7hPR8H2GGPuh1ynf5e6mgmUtk8wFoRvJX8mPMd3C7KGJo2XTyVBUzxku6iJrKpjTeGEXB96NCBgf44TcymqPUvZnBGmWUPiCaYcG8J2T9UiUb38Av9uPdDkdBZgSCqBujUsvCqsstDmHuciWzYeZEywZBmc68NjKNgB1BdwAagHTfhk8czq9VAtJ2zN9hNaaj4WvNUqSdqG1LUgoMW5GAqssmcAFDbBzA4zcWxyYrpRVYYq4uGCzFz3zJjgXtXGXx21FA17yHAeuV"
  }
}
```

#### responder <--- (2018-10-16 20:25:57.981)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkR8jZR4S32Fd7nhjdwiTg312jrYwy7tyMCfquaZq6cjrqyHVwx5PTa2BnHHhWWFYzcEJNLTYaK23KDREtVbFQe52Xj71UByxiFrx87ED7gdgsTq8tRGfC1cGNc2kQvhV9SeyqBbqU6ZybaoJt12dAEwAK7LHqWReYZaMGjddAwwj4XH3YFUCdqBNp2MBxeYmAtM8LjEXFWdrebXZxCoSAAquqBBXHjLcqjanXZK2pd3vRNdWZrrzVUX8rNikDYjjKS5DwMbEiNvVGftCUdHv1sXvDWycorkADPwzPyShqhwZPp8RW1X2CiDf7H8VZEKeeV8CjuEyk28f2QqH7UoAMRpxxDUhbnQwPQDcSpZAUfLmbJ1Hj7SD5jcY7ehCwUnwmXENyrDLQ",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### initiator <--- (2018-10-16 20:25:57.982)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkR8jZR4S32Fd7nhjdwiTg312jrYwy7tyMCfquaZq6cjrqyHVwx5PTa2BnHHhWWFYzcEJNLTYaK23KDREtVbFQe52Xj71UByxiFrx87ED7gdgsTq8tRGfC1cGNc2kQvhV9SeyqBbqU6ZybaoJt12dAEwAK7LHqWReYZaMGjddAwwj4XH3YFUCdqBNp2MBxeYmAtM8LjEXFWdrebXZxCoSAAquqBBXHjLcqjanXZK2pd3vRNdWZrrzVUX8rNikDYjjKS5DwMbEiNvVGftCUdHv1sXvDWycorkADPwzPyShqhwZPp8RW1X2CiDf7H8VZEKeeV8CjuEyk28f2QqH7UoAMRpxxDUhbnQwPQDcSpZAUfLmbJ1Hj7SD5jcY7ehCwUnwmXENyrDLQ",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### initiator <--- (2018-10-16 20:25:57.988)
```javascript
{
  "id": -576460752303423439,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "balance": 698
    },
    {
      "account": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "balance": 402
    }
  ]
}
```

#### initiator <--- (2018-10-16 20:25:57.991)
```javascript
{
  "id": -576460752303423438,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "balance": 402
    },
    {
      "account": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "balance": 698
    }
  ]
}
```

#### responder ---> (2018-10-16 20:25:57.991)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
    "to": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh"
  }
}
```

#### responder <--- (2018-10-16 20:25:57.996)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTiKBfWYDbYaLuN9aWEsEwRA9cKUgJbrpZZeqFf9ETwfAcac22FW4ibkYZTDvahzP88xvNGcmZBTNC7Jbi4p8qfRFcCC8Lud396FAgtbaSmmfjesguxNjCscb4Hi4rHzjtWCRNN6Bvw2kAyMwwgxwK8ruACRCzvD7XVoe4sXKj6WefU85v4r9v1GoGHZxdLk1fGVQFAbQMGN2"
  }
}
```

#### responder ---> (2018-10-16 20:25:57.997)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak5BbDeiiDr9P1EXBgXjpvXT4E4exaiw3K6pGUsfhmdYpcBp78hcdbRhaqqiXmBTNa8CKx4CHkaGbFa2b9SfitqBBJMmfc1Re8WJ9gtQmLcmvcwg4X1hAjQVrhVc72NLSc3EPCpaJCg4HyC1yEvaR16jud7vgvbbgwgS2VzqtLtZE7fTmYQ62S8vKgWCEe1jNAHjrahEFv4mRorV1XfbyWQ6qJmcq8qkhwhim34FN7oQ2es31naa8SYff3D8h8LnnkyiBEvj6hYUchiGvWcnjuVht3iUbtxwLJy5wqHNMe5WE2Y2Z"
  }
}
```

#### initiator <--- (2018-10-16 20:25:58.19)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### initiator <--- (2018-10-16 20:25:58.19)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTiKBfWYDbYaLuN9aWEsEwRA9cKUgJbrpZZeqFf9ETwfAcac22FW4ibkYZTDvahzP88xvNGcmZBTNC7Jbi4p8qfRFcCC8Lud396FAgtbaSmmfjesguxNjCscb4Hi4rHzjtWCRNN6Bvw2kAyMwwgxwK8ruACRCzvD7XVoe4sXKj6WefU85v4r9v1GoGHZxdLk1fGVQFAbQMGN2"
  }
}
```

#### initiator ---> (2018-10-16 20:25:58.20)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4jh4iyuuFREXnQsSkE8SQaywnc3GAC2n5SeEvjsjYzcC99KMJTsgwjKbtJ4XwfHSyZEjEACER9nB7e4Qo3E5nihqYEPH1kGxuAAPzmrffmLHCVXHdSAWvTU3ugAzNeMD91kH1udBM46EFHXPsdrrphGxesjFjTNrcJmouy58d9fo5yynH7UpfNyrQotwrKADaeCo7hVJdrhkV4kmJNS6aFPGCDTz1p1d2NPMAnUqzdnh8VXHbU8C4NLpu2LVVr3iu1QY2gqe2ko2ALQmq4NEohhW32UdVaG1Aa2jVE4wi2LZSJ4"
  }
}
```

#### initiator <--- (2018-10-16 20:25:58.25)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkHxQVWrA1wWdaftpBwRPHWHLnLJbmNetqsJ7x2HPCzCTGhENkkdtMjSsvHpN7AdhRUSLDnm5jpfiJxevh2jhURXcUhmonxYv9dqyEd6xAsaETWw1qzwfSuF8PTdmVQiNJ7CwTZ9mMFs6c9KLaSHZtT8RtS6jTA6gx3Phwz6FiLHQhwEjstmnfchqWETECUgUzUk3Dkt9QPHzemcWBr3RTcu6g8CEoUJYH3zgBoZjBKhDWwK5ba7J6mRvkubwcJEyHAtw4RJNW16somX8Sc5aZtSEBC85DWAysnP4A7ZBN2VVpyyYVsX2mp45cGPetfN1qk5via8Lw8TvMSh85gCmrYxB3TY5nU5bHvHvvKpiiT8oHyzfptcHcnZ2fFA74eHHet8ffa6tm",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### responder <--- (2018-10-16 20:25:58.26)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkHxQVWrA1wWdaftpBwRPHWHLnLJbmNetqsJ7x2HPCzCTGhENkkdtMjSsvHpN7AdhRUSLDnm5jpfiJxevh2jhURXcUhmonxYv9dqyEd6xAsaETWw1qzwfSuF8PTdmVQiNJ7CwTZ9mMFs6c9KLaSHZtT8RtS6jTA6gx3Phwz6FiLHQhwEjstmnfchqWETECUgUzUk3Dkt9QPHzemcWBr3RTcu6g8CEoUJYH3zgBoZjBKhDWwK5ba7J6mRvkubwcJEyHAtw4RJNW16somX8Sc5aZtSEBC85DWAysnP4A7ZBN2VVpyyYVsX2mp45cGPetfN1qk5via8Lw8TvMSh85gCmrYxB3TY5nU5bHvHvvKpiiT8oHyzfptcHcnZ2fFA74eHHet8ffa6tm",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### initiator <--- (2018-10-16 20:25:58.30)
```javascript
{
  "id": -576460752303423437,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "balance": 401
    },
    {
      "account": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "balance": 699
    }
  ]
}
```

#### initiator <--- (2018-10-16 20:25:58.31)
```javascript
{
  "id": -576460752303423436,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "balance": 401
    },
    {
      "account": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "balance": 699
    }
  ]
}
```

#### responder ---> (2018-10-16 20:25:58.31)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
    "to": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh"
  }
}
```

#### responder <--- (2018-10-16 20:25:58.35)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTiKBfWYDbYaLuN9aWEsEwRA9cKUgJbrpZZeqFf9ETwfAcg2Xso3XuwUUKSm3UpqNuSVeviBqXsMVcACDdYZpaR2H6TcF1kzHo2zKnLJNBYrmRHqKR1hA68EXLiHmZYsPpWKjbJx7WVk9rLrCL3vMoj89TryhnCEVLpFFhrJQJpFseUYNPmmxYksqAyUD9zSgpYL16YLuxJSV"
  }
}
```

#### responder ---> (2018-10-16 20:25:58.36)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak54wh3FxZtHSZYTt1kvUtLkUBvePgLGixjgCMvKWcmWtFfyQQK5e7SugmY591SjG7e4kyk6Va8ydpMoYYR6du8eUpThf5S7AQ3qdAz5rcEvKxCoZAvg4frbw93VBNnmyJ5nVRSixYmkt16zroqzYQV4PsQy1ApVsEgxNru8VTZokhsWCZ7xeALdqqtQy3HgB8275rWMZJZH38VtMdDbbEgoUPFBRkee56LUxiX11mj8unN5YgbCUwgVs14nSvp3RfTuHBUY5jNWyhgrbiHyqoP5LXRV5LmbeeKSULEeT9nJj88BU"
  }
}
```

#### initiator <--- (2018-10-16 20:25:58.40)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### initiator <--- (2018-10-16 20:25:58.41)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTiKBfWYDbYaLuN9aWEsEwRA9cKUgJbrpZZeqFf9ETwfAcg2Xso3XuwUUKSm3UpqNuSVeviBqXsMVcACDdYZpaR2H6TcF1kzHo2zKnLJNBYrmRHqKR1hA68EXLiHmZYsPpWKjbJx7WVk9rLrCL3vMoj89TryhnCEVLpFFhrJQJpFseUYNPmmxYksqAyUD9zSgpYL16YLuxJSV"
  }
}
```

#### initiator ---> (2018-10-16 20:25:58.42)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak52WfncvTu76XhpmpSF8yeK1nbbqCuWov3CyHaFUXU3oxrBxKrYxcYz352hM6VcBNGju6v6J41haE9QLgiPae8trWjRavTHYjnB6dfP6nbnjCmDCB5nAHdFbuQxfXgdteWH1VridWnxBGiNX8gt6WCv2WDtwEcwmrZ2gLpa2qyyT2jTZof6GNskVBc2TJLAaokiajBhdnFwDUujMTpwGKsUwTn615DN1uXD3GtLDK22ys6MSg6xm5GFKLLCjnDoaSsWuUZQkeNukfSVCWwb9sL2uh5XshJ7G1UiJzc5UrC8PMqd4"
  }
}
```

#### initiator <--- (2018-10-16 20:25:58.47)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDknsdiRsMsYsygbzqznpqAdEgdVMy7wMRN9A16XDHSCRzMrztJTA9H6pBU9SuQhBbBWvWBK39iXmWDeVGU8jKHbuer6pYdGpUufCx1RjBonATfthyv1BvUcjrZnNTb37bFKGtLVjroT7XXMunrXus31TgvaDLbsVV3UY2d7M5S6YWsZWQgDyyvixp6YNmW3yZJGCrpbcPbPFrHCy2gGSjNYgk69GMAgRqNXbmnvWWQeGWi1KUJY7Tnono6SB5nQsmZpi3espKCbrEi6vuMfsf3PdULZxjTY2ia2SutcJfaUATi4Qe6q42HoYGMcGYMa88bC2Vox6kqATsXbE9hnfHPgUXEcpYEtWZd6f37CgQZDYVQSQKgdVVCu7mNstYb9mYhn32eQy1R",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### responder <--- (2018-10-16 20:25:58.48)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDknsdiRsMsYsygbzqznpqAdEgdVMy7wMRN9A16XDHSCRzMrztJTA9H6pBU9SuQhBbBWvWBK39iXmWDeVGU8jKHbuer6pYdGpUufCx1RjBonATfthyv1BvUcjrZnNTb37bFKGtLVjroT7XXMunrXus31TgvaDLbsVV3UY2d7M5S6YWsZWQgDyyvixp6YNmW3yZJGCrpbcPbPFrHCy2gGSjNYgk69GMAgRqNXbmnvWWQeGWi1KUJY7Tnono6SB5nQsmZpi3espKCbrEi6vuMfsf3PdULZxjTY2ia2SutcJfaUATi4Qe6q42HoYGMcGYMa88bC2Vox6kqATsXbE9hnfHPgUXEcpYEtWZd6f37CgQZDYVQSQKgdVVCu7mNstYb9mYhn32eQy1R",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### initiator <--- (2018-10-16 20:25:58.52)
```javascript
{
  "id": -576460752303423435,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "balance": 400
    },
    {
      "account": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "balance": 700
    }
  ]
}
```

#### initiator <--- (2018-10-16 20:25:58.53)
```javascript
{
  "id": -576460752303423434,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "balance": 700
    },
    {
      "account": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "balance": 400
    }
  ]
}
```

#### initiator ---> (2018-10-16 20:25:58.53)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
    "to": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A"
  }
}
```

#### initiator <--- (2018-10-16 20:25:58.57)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTiKBfWYDbYaLuN9aWEsEwRA9cKUgJbrpZZeqFf9ETwfAcmT3jLb17HCQ5SJANwZqLXTVSTSkTaVZL44BNQL6kkqngVtBByACNjPqFnYACf639PzVLxcP9uK7tA4s54WpSgrQ6drZbsPmYptgWVAcTfqRgZie6gJ16ssUw4raiwCYr4pCykSQg8XXXJdpCa4NF1e2KJkAhhki"
  }
}
```

#### initiator ---> (2018-10-16 20:25:58.58)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak52SVj2mCWVb7WVusJEomcCmB7FMgYJwbN3xLWPseboMk2AXF3Vu8vRiUPhuVvniZKRGYDqF9qgcewX4jmNYadPcmKNvjBRKu4BedAAB4npAmweXJpHSB5s8Q6JAsuLQg8DFMc7kxXyxSPh2nD4KTgVmJXMKjcRx1kmQVbaWqTHDqTzTBFYuGGbKQaSnCqXGXuvydCKn3RafA5AtC1Q8gdTAytK4baaFmNtkMM3E6Fb1sURHgUaqmUePtRQBy4ykRJz2p19wJJH8YkUzvEAUDNXhPEHky55S2WsDnqxxdhDV5Brk"
  }
}
```

#### responder <--- (2018-10-16 20:25:58.95)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### responder <--- (2018-10-16 20:25:58.97)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTiKBfWYDbYaLuN9aWEsEwRA9cKUgJbrpZZeqFf9ETwfAcmT3jLb17HCQ5SJANwZqLXTVSTSkTaVZL44BNQL6kkqngVtBByACNjPqFnYACf639PzVLxcP9uK7tA4s54WpSgrQ6drZbsPmYptgWVAcTfqRgZie6gJ16ssUw4raiwCYr4pCykSQg8XXXJdpCa4NF1e2KJkAhhki"
  }
}
```

#### responder ---> (2018-10-16 20:25:58.99)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak5AuuVgZKKSLZAzmpUigJm45sAiuoR3C26WnxThUVzCPSd9bPHD9S8dKv3mnTuse7t2RPzAWU4WqjRDzeiVwM3LkjN1PRLqMFp51yijC1yf6SXaXivTJ33XSQLcy6YicNC3R9dCtB41eaPs4UXFEw1hU3qP8vjNXQqLeNjZ3vwLrCWukJwhy7RTK1NaSGLjbx5KzjRDHK3a7N8gbjSfkbkTqAg3o1w56RmxxVUyWbB5gthZHJzChvSRiYq2f7Xok3q4TnwSbwSXj9za7zAkefgd4daDN3nPgATMA1p3hPGRqMiPj"
  }
}
```

#### responder <--- (2018-10-16 20:25:58.112)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDknkTa24XiT1A9RXF8yrJUxTtsGekFnuL71dHwP4QASWrtPe4zWPRGMyoW6R2BK5q4tdtrgKh44s8yuuk8AQ7KyLVpZ9tGpELEP8j1v5SX4FuUPP64RJK7tZgoAeN7T2Tpbr9V7eotoiJtcY4JqqdKmpyJC3DFEnppQgVQ1YkdzCXVh877Je7rT4YZRWZbgsRBgwcKRXytBbZBvW4XpidxZjsQxfRMaCx1VYLGCYhnGzdh3Yy5p93qKgBc6jWsbviJ8J49tYV1vKoNVpLHbWG6XDnUJsGR3kjLuShvExyTxwMzH9Y13ueJbbCAjJDCxqpuGCEhNo5hp59xFfzcTog497YJhd6egbrt6uSnNwD8LWav2GbjgkrkWuddNPDSuAGMjxJQEMR8",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### initiator <--- (2018-10-16 20:25:58.113)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDknkTa24XiT1A9RXF8yrJUxTtsGekFnuL71dHwP4QASWrtPe4zWPRGMyoW6R2BK5q4tdtrgKh44s8yuuk8AQ7KyLVpZ9tGpELEP8j1v5SX4FuUPP64RJK7tZgoAeN7T2Tpbr9V7eotoiJtcY4JqqdKmpyJC3DFEnppQgVQ1YkdzCXVh877Je7rT4YZRWZbgsRBgwcKRXytBbZBvW4XpidxZjsQxfRMaCx1VYLGCYhnGzdh3Yy5p93qKgBc6jWsbviJ8J49tYV1vKoNVpLHbWG6XDnUJsGR3kjLuShvExyTxwMzH9Y13ueJbbCAjJDCxqpuGCEhNo5hp59xFfzcTog497YJhd6egbrt6uSnNwD8LWav2GbjgkrkWuddNPDSuAGMjxJQEMR8",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### initiator <--- (2018-10-16 20:25:58.119)
```javascript
{
  "id": -576460752303423433,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "balance": 699
    },
    {
      "account": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "balance": 401
    }
  ]
}
```

#### initiator <--- (2018-10-16 20:25:58.122)
```javascript
{
  "id": -576460752303423432,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "balance": 401
    },
    {
      "account": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "balance": 699
    }
  ]
}
```

#### responder ---> (2018-10-16 20:25:58.122)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
    "to": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh"
  }
}
```

#### responder <--- (2018-10-16 20:25:58.127)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTiKBfWYDbYaLuN9aWEsEwRA9cKUgJbrpZZeqFf9ETwfAcrsZat8UJcvKqRqHH4XNU3Z83bKyVF9kSFyTUW5C3vEL4zSUMTio6vUdyDhwf72xnZkaR8L1rdUPuZTAz4chgWaN3CfxfdAyD5ph6mqCnuee5C3vSczFdtMR3KDRRXmcUnrt3ECVPdKEyPQC6R7GdbKwUDDwubPQ"
  }
}
```

#### responder ---> (2018-10-16 20:25:58.128)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4rEz1Chui6WH272qChmhAc9d1ygh9euG9hkTV6kT187dGDPR91i8EKyvFYv2L55qq7uYSuL2t4Aroz7eShWaJSfWFHcTcox3KFfvvJroFiAnGksNmYsRRc7u77d5vMZyv4y5oED1hfzPDkbPAn54M1bsFmWFsAfRWw1hnF2NCaRjQ8ZsYBCkUpZahKRUmpmmw19R8L2eVrDcM93SZmJNQYtipY9iBhmdTk7GuUtbG16wq7qFovWeoUJ3VmZbscMueF1CQYCttdQbHzaTEb7Qcuxprn3PyCK2K9B2LtZZPLbJKjL"
  }
}
```

#### initiator <--- (2018-10-16 20:25:58.155)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### initiator <--- (2018-10-16 20:25:58.156)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTiKBfWYDbYaLuN9aWEsEwRA9cKUgJbrpZZeqFf9ETwfAcrsZat8UJcvKqRqHH4XNU3Z83bKyVF9kSFyTUW5C3vEL4zSUMTio6vUdyDhwf72xnZkaR8L1rdUPuZTAz4chgWaN3CfxfdAyD5ph6mqCnuee5C3vSczFdtMR3KDRRXmcUnrt3ECVPdKEyPQC6R7GdbKwUDDwubPQ"
  }
}
```

#### initiator ---> (2018-10-16 20:25:58.159)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak5BCboQRXaorC2tXjyASkdNzWByw3XhzaezP3X9KY8quWX9JTgrMUaDs7W8WXzDDoyoCfnKQPGWxptVKFEDT8nh4CS2zsL6NQnas7vtr28EMQNKYrspBEBL2xtSqDMpZzQerpH29ZBB8UHL9FrJpkDHoTUs7sxpP11JVHKwpx21oieoiJwawtznTseiPrb1rBwVcrn9b1E4qr5iGZvsXBQ7EanKMdMmsotXad9s6mDNEtrTEfPRHCrShHMoaqoS8sEaEJnPqoTDFtGuUrC1QGk6JM6tCKcNqJDqHsgHjdEnBLKSP"
  }
}
```

#### initiator <--- (2018-10-16 20:25:58.174)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkVDYqXxGMHM3cfnXb7Y5wVpbQez9pYpUJQb4hVC1dDizeKFBQ78QUbN9JBGeK16xF6JGvu7Lm7g7G8SV9NixHhchSN2rRp6fmFdok2JnCTdRGhi2thHEnzbJe4MG7W7qWNKikFFKqSTHxdimQGmRqvq6B7pMhqe7vSt8c2ikRW51turhUKsHjXfqDSujaNhANiYDXGcajR8k1EQCzrWfhrPZEf3fzFw5GSHGG9YsDjLbLPsRauVCH1ZGBGMxH2P1RwaEgy9d6khz3xmNbrrRLAK1S9DcFtVn6tsZZEV1kCEm3PsnxqCA75C2YE6yjdtPVqgYvvbW3CAcw1Cigeu5KDVWWp3fRTKtuTyMZySx3Ud4WL1agoZyzJJmQxv6pvrdku7NqJPNw",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### responder <--- (2018-10-16 20:25:58.175)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkVDYqXxGMHM3cfnXb7Y5wVpbQez9pYpUJQb4hVC1dDizeKFBQ78QUbN9JBGeK16xF6JGvu7Lm7g7G8SV9NixHhchSN2rRp6fmFdok2JnCTdRGhi2thHEnzbJe4MG7W7qWNKikFFKqSTHxdimQGmRqvq6B7pMhqe7vSt8c2ikRW51turhUKsHjXfqDSujaNhANiYDXGcajR8k1EQCzrWfhrPZEf3fzFw5GSHGG9YsDjLbLPsRauVCH1ZGBGMxH2P1RwaEgy9d6khz3xmNbrrRLAK1S9DcFtVn6tsZZEV1kCEm3PsnxqCA75C2YE6yjdtPVqgYvvbW3CAcw1Cigeu5KDVWWp3fRTKtuTyMZySx3Ud4WL1agoZyzJJmQxv6pvrdku7NqJPNw",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### initiator <--- (2018-10-16 20:25:58.183)
```javascript
{
  "id": -576460752303423431,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "balance": 400
    },
    {
      "account": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "balance": 700
    }
  ]
}
```

#### initiator ---> (2018-10-16 20:25:58.249)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- (2018-10-16 20:25:58.258)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "tx": "tx_2C9es4FjJDdeHEuktLd1kRXfiz6NMb2FRDDdfcZemWiCmf7pb9r6yatfM1JsoJF6vKAZM9yWkRr7ZNLr7jMPBRamYV4qfY6bLfxGbZt5jbfQeQrHakVsdrsqWxENWDpxNYqxnoYTTQ8f5hERi5y9PPu4LWtwpY"
  }
}
```

#### initiator ---> (2018-10-16 20:25:58.261)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "tx": "tx_2WsEQsiC5XsnuUpTRoUr6EvCQpZr3L56B96uEzvLVWow3UeEWmNKC9xBxDoMqQJzMBiGYTKcRhJsK8dWFmRRJ3mnTJ8npYYSyhp9Zua9LYWBC5eLWU6suZpfcTihpem5qdLiHXwA822nJsKKkQXLr4uCniCjMX64wLYPQCWAqmmmBUiXsGmmjYxDvvLfzUTrJwXSZdcvKiNfqqatbXSsDYeS5cXc3bDsoVtAgEutuTstRDG778h7FkaZo4nx4JtnBQ7"
  }
}
```

#### responder <--- (2018-10-16 20:25:58.263)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "deposit_created",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### responder <--- (2018-10-16 20:25:58.263)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "tx": "tx_2C9es4FjJDdeHEuktLd1kRXfiz6NMb2FRDDdfcZemWiCmf7pb9r6yatfM1JsoJF6vKAZM9yWkRr7ZNLr7jMPBRamYV4qfY6bLfxGbZt5jbfQeQrHakVsdrsqWxENWDpxNYqxnoYTTQ8f5hERi5y9PPu4LWtwpY"
  }
}
```

#### responder ---> (2018-10-16 20:25:58.264)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "tx": "tx_2WsEQsiC5XsmicPWcahgWnftc4kJFkXJwSESSrqZXAznz938a264LPeaLQQZQ6FhXxo6L4tPrMqiHc48fS6PNkPP3vjW8WhYxm6urz6tSxDMKAcgRX93xd4r9rzyRzcA4NZvRuTpBimekz1QcaJgNMwpF97HimRJ5rM5t1dDFfXGnCDejBHG5p2csWu9S4c4xwuWQYE6qvqir8ys9uwRE9i1fNj1s8BWd3BFG69dGdtAT78ji2oYWggc9CFkbsadyJW"
  }
}
```

#### responder <--- (2018-10-16 20:25:58.266)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3cDMp6242sByFQTDLhT5KWdAgqhDrpZr1zJibVycXbz3RFASs4ufw6RzNgmrznPYNyUjB8sGUWtWYrdJqsqJjJB29RPE3t1WhUbk14oscyTG9iRYe9WAT6f3zdn8RDAdi73QffSdsJF5ZVjs2LhASq3pXUksW6JUpHoKaAHdM2jzN5en9Sf52dtci42bVv4mxSyGDCUDvPjVQgG8fXum1u76jgBYPhuh1CJGmTgd9ZzXuHnpsrGmdwWgq7JAKws1KUdbThbWJGfpVgG4NpDanHdjPjSn2YAsPNRiw2BCU6Uxsa69nqzT7LzzcauV7AATMR6uY1un2JdrbkXFgprg42iNLGJna",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### initiator <--- (2018-10-16 20:25:58.266)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3cDMp6242sByFQTDLhT5KWdAgqhDrpZr1zJibVycXbz3RFASs4ufw6RzNgmrznPYNyUjB8sGUWtWYrdJqsqJjJB29RPE3t1WhUbk14oscyTG9iRYe9WAT6f3zdn8RDAdi73QffSdsJF5ZVjs2LhASq3pXUksW6JUpHoKaAHdM2jzN5en9Sf52dtci42bVv4mxSyGDCUDvPjVQgG8fXum1u76jgBYPhuh1CJGmTgd9ZzXuHnpsrGmdwWgq7JAKws1KUdbThbWJGfpVgG4NpDanHdjPjSn2YAsPNRiw2BCU6Uxsa69nqzT7LzzcauV7AATMR6uY1un2JdrbkXFgprg42iNLGJna",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### initiator <--- (2018-10-16 20:26:00.470)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_deposit_locked",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### responder <--- (2018-10-16 20:26:00.471)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_deposit_locked",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### responder <--- (2018-10-16 20:26:00.471)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "deposit_locked",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### initiator <--- (2018-10-16 20:26:00.472)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "deposit_locked",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### responder <--- (2018-10-16 20:26:00.475)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3cDMp6242sByFQTDLhT5KWdAgqhDrpZr1zJibVycXbz3RFASs4ufw6RzNgmrznPYNyUjB8sGUWtWYrdJqsqJjJB29RPE3t1WhUbk14oscyTG9iRYe9WAT6f3zdn8RDAdi73QffSdsJF5ZVjs2LhASq3pXUksW6JUpHoKaAHdM2jzN5en9Sf52dtci42bVv4mxSyGDCUDvPjVQgG8fXum1u76jgBYPhuh1CJGmTgd9ZzXuHnpsrGmdwWgq7JAKws1KUdbThbWJGfpVgG4NpDanHdjPjSn2YAsPNRiw2BCU6Uxsa69nqzT7LzzcauV7AATMR6uY1un2JdrbkXFgprg42iNLGJna",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```

#### initiator <--- (2018-10-16 20:26:00.476)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3cDMp6242sByFQTDLhT5KWdAgqhDrpZr1zJibVycXbz3RFASs4ufw6RzNgmrznPYNyUjB8sGUWtWYrdJqsqJjJB29RPE3t1WhUbk14oscyTG9iRYe9WAT6f3zdn8RDAdi73QffSdsJF5ZVjs2LhASq3pXUksW6JUpHoKaAHdM2jzN5en9Sf52dtci42bVv4mxSyGDCUDvPjVQgG8fXum1u76jgBYPhuh1CJGmTgd9ZzXuHnpsrGmdwWgq7JAKws1KUdbThbWJGfpVgG4NpDanHdjPjSn2YAsPNRiw2BCU6Uxsa69nqzT7LzzcauV7AATMR6uY1un2JdrbkXFgprg42iNLGJna",
    "channel_id": "ch_2mbPH7vuADXYvzH8c4nBhY7nLcseKysB8hfo5MB7FLQoMJV5w4"
  }
}
```
