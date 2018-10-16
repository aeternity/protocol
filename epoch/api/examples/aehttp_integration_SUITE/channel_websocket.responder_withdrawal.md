
#### initiator init (2018-10-16 17:14:34.9)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb&role=initiator
```

#### responder init (2018-10-16 17:14:34.15)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb&role=responder
```

#### responder <--- (2018-10-16 17:14:35.15)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 17:14:35.18)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 17:14:35.26)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpALGJSrzwTy6oub8Qv4su7RMx2hck9JNUEgjtyU6qrUG48oB7x4ucqxPokv4rA4P5zaAWfi6eCujMzNBvMMu3xP8p9Svn5xM77VDy3ntvSFDRTNLxquqDLKr53dA7VoLQyju8FB1sKcPCeRhzzU2bUngSx5u2w7J"
  }
}
```

#### initiator ---> (2018-10-16 17:14:35.50)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HjijJHU1PgtxbkiZxrwn1aYXVxCwdwyE2uoGNVVGmj8zM9NG6bfqugAoQYxhVgKxPCaCuL76pcQuabGcqzff8sLkzGaYiGVivkztyoSUSN2CrG9GH2XEvwkEvdr7GAsaik1SFjYBTrKm6Ed235WBP1xXQaMjBrzDkWEQDTxTYr8ZXd69JuUPW8b2f7E9og6PEW4q921Enh7789Ng5xngBKkmogNt6QJp3GhfJDLiiVV6sPimJmEGGpQUoPkaTSXuh"
  }
}
```

#### responder <--- (2018-10-16 17:14:35.51)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 17:14:35.51)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpALGJSrzwTy6oub8Qv4su7RMx2hck9JNUEgjtyU6qrUG48oB7x4ucqxPokv4rA4P5zaAWfi6eCujMzNBvMMu3xP8p9Svn5xM77VDy3ntvSFDRTNLxquqDLKr53dA7VoLQyju8FB1sKcPCeRhzzU2bUngSx5u2w7J"
  }
}
```

#### responder ---> (2018-10-16 17:14:35.52)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HmBMpHZ9ZWvZvqfPNjxPgbZvBxXhhVCmoEVh2Beu9AjGnVs1BKwaYREdoCFzQ7cVyLNJbDGsVLTxbT7JfRd8sttxxHKjCTPVxZ1SZg5kLJnjPaUZXkspx3LNhqTNcmwLRduWzPrP72zy7sjm9SmogeZu4fkQd5Uuz9RMSdnStNMGcuuwQwbtM5zEz6kWEqFvHpptkAxsfSWHZ5AQXJwZAuwTUuqf8ewzhMA6ByfDQhJt3PV4UAQ4xwrWLyYEJRnTL"
  }
}
```

#### initiator <--- (2018-10-16 17:14:35.53)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 17:14:35.54)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmMj2YPoghWqBNFCuXYLtpmmTjvWgonZnZDURbLmwELkTMnvwoj71JPPgKyEPgKvFM7FzWu9eppC4eqZPASWh7BVL6ZvR9jCWMHrEBKqRR2SdAGBEuAtyxrqYhHgNWBn9JHsbGfiDvj3KxvKy99otCNaZUFY32L7oW44aKM1GA8TtAoKgUvnZMvETx8B6WWkCZeuKeJi2RzJXJ93LMHVf7ThSFKTSEqLefZgksrdmqvsTDvjdTBid7arLrgtFBA4ZRvxKmH3Y5FYkqkqiSjrbB6PKX1pxtghccjCWjPxERptQw7vCjsqMe8FaTtk5C4NaGeyu59vBUSGHKbFWewS62B7ttzK"
  }
}
```

#### initiator <--- (2018-10-16 17:14:35.54)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmMj2YPoghWqBNFCuXYLtpmmTjvWgonZnZDURbLmwELkTMnvwoj71JPPgKyEPgKvFM7FzWu9eppC4eqZPASWh7BVL6ZvR9jCWMHrEBKqRR2SdAGBEuAtyxrqYhHgNWBn9JHsbGfiDvj3KxvKy99otCNaZUFY32L7oW44aKM1GA8TtAoKgUvnZMvETx8B6WWkCZeuKeJi2RzJXJ93LMHVf7ThSFKTSEqLefZgksrdmqvsTDvjdTBid7arLrgtFBA4ZRvxKmH3Y5FYkqkqiSjrbB6PKX1pxtghccjCWjPxERptQw7vCjsqMe8FaTtk5C4NaGeyu59vBUSGHKbFWewS62B7ttzK"
  }
}
```

#### initiator <--- (2018-10-16 17:14:37.230)
```javascript
{
  "id": -576460752303423408,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 699
    },
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 401
    }
  ]
}
```

#### responder <--- (2018-10-16 17:14:38.147)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### initiator <--- (2018-10-16 17:14:38.150)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### initiator <--- (2018-10-16 17:14:38.150)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### responder <--- (2018-10-16 17:14:38.152)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### initiator <--- (2018-10-16 17:14:38.154)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### responder <--- (2018-10-16 17:14:38.155)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### initiator <--- (2018-10-16 17:14:38.156)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmMj2YPoghWqBNFCuXYLtpmmTjvWgonZnZDURbLmwELkTMnvwoj71JPPgKyEPgKvFM7FzWu9eppC4eqZPASWh7BVL6ZvR9jCWMHrEBKqRR2SdAGBEuAtyxrqYhHgNWBn9JHsbGfiDvj3KxvKy99otCNaZUFY32L7oW44aKM1GA8TtAoKgUvnZMvETx8B6WWkCZeuKeJi2RzJXJ93LMHVf7ThSFKTSEqLefZgksrdmqvsTDvjdTBid7arLrgtFBA4ZRvxKmH3Y5FYkqkqiSjrbB6PKX1pxtghccjCWjPxERptQw7vCjsqMe8FaTtk5C4NaGeyu59vBUSGHKbFWewS62B7ttzK",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### responder <--- (2018-10-16 17:14:38.157)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmMj2YPoghWqBNFCuXYLtpmmTjvWgonZnZDURbLmwELkTMnvwoj71JPPgKyEPgKvFM7FzWu9eppC4eqZPASWh7BVL6ZvR9jCWMHrEBKqRR2SdAGBEuAtyxrqYhHgNWBn9JHsbGfiDvj3KxvKy99otCNaZUFY32L7oW44aKM1GA8TtAoKgUvnZMvETx8B6WWkCZeuKeJi2RzJXJ93LMHVf7ThSFKTSEqLefZgksrdmqvsTDvjdTBid7arLrgtFBA4ZRvxKmH3Y5FYkqkqiSjrbB6PKX1pxtghccjCWjPxERptQw7vCjsqMe8FaTtk5C4NaGeyu59vBUSGHKbFWewS62B7ttzK",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

##### initiator: (2018-10-16 17:14:39.570)
> Funding has been confirmed locally on-chain

##### responder: (2018-10-16 17:14:39.570)
> Funding has been confirmed locally on-chain

##### initiator: (2018-10-16 17:14:39.570)
> Funding has been confirmed on-chain by other party

##### responder: (2018-10-16 17:14:39.570)
> Funding has been confirmed on-chain by other party

##### initiator: (2018-10-16 17:14:39.570)
> Channel is `open` and ready to use

##### responder: (2018-10-16 17:14:39.570)
> Channel is `open` and ready to use

#### initiator <--- (2018-10-16 17:14:39.618)
```javascript
{
  "id": -576460752303423407,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 699
    },
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 401
    }
  ]
}
```

#### initiator ---> (2018-10-16 17:14:39.619)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
    "to": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb"
  }
}
```

#### initiator <--- (2018-10-16 17:14:39.626)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQMHEA1mtKNn37Axft4bdXTb4dHq1Rf9meBhQFV1MZX5FqsFSXemLLvXJyTkT8WejMKU4jMHUKgfVZUyVpktTMiD2XyJE1xNG8BrENRK58u6jv2wboZVYyuZwRVgKLzZRALQcWt4Dxthgx3QCrr9n8guxqTCSrbKnA1AKhiZrzAhRWLi61bxzLNmQZhn5CvF7K9LVKA7VjxAsr"
  }
}
```

#### initiator ---> (2018-10-16 17:14:39.628)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4vaL9Qf25zpnvR5fuKKfHu3agQuHMMtTEgEsNPraPvoADiRg8CRjLwpohcm9zr4xkzPujwVRenkxDxbiX2UJMi8jzJmcWBxNaXhWn6WKvoHXv7gUuWg8YeBohf1BxEiCCWJQtwN5HFMbzsMDSfwKsya6ypCsLqPiN34p19B6hG7kaSnfZgDEci3Tnqu3cEtLtp1Jj8upi5huxP9gP5vHku8Xd7hBy2dSQWU2HFK6tQuXmSJhJhKfMZPNBVFC8DkpRBXq39RRtqhZCRrPKrxEaxYsHGWwgGATmMSaNo8AEH3yZTB"
  }
}
```

#### responder <--- (2018-10-16 17:14:39.633)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### responder <--- (2018-10-16 17:14:39.633)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQMHEA1mtKNn37Axft4bdXTb4dHq1Rf9meBhQFV1MZX5FqsFSXemLLvXJyTkT8WejMKU4jMHUKgfVZUyVpktTMiD2XyJE1xNG8BrENRK58u6jv2wboZVYyuZwRVgKLzZRALQcWt4Dxthgx3QCrr9n8guxqTCSrbKnA1AKhiZrzAhRWLi61bxzLNmQZhn5CvF7K9LVKA7VjxAsr"
  }
}
```

#### responder ---> (2018-10-16 17:14:39.634)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4onxdASvE4FgRDX55d8xgfYm9wzPd39NfN9HhpXFGKiW8ZZHV2ZMsF3JbpLVoSEXpXUkB2dCiS3iWyXQiQm9aSEshLieTfwJwLs2hGYS9jcDMFuLSVVFmWkq6BEoDktA1cgHDdtWaUZdgR8Zsn3YYNo24nhV8nXTdoGGayBQHG9GtYMuUiFcj7TnGnTp7r93CravpxHdx3jpxJ2PRPR5EmfNboTzyeif7SUek4Dcav1PJ1caXRbiHTWPj1iKebHDFLdaNmf5RuMyFCeTrmsD1e88LqAWyusWMNBBoRyczQDeNRJ"
  }
}
```

#### responder <--- (2018-10-16 17:14:39.639)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkR1PQ4j5pVSz1ekdSnwJ3V6siYq4QTQuD29tgifNkueFpFEpTam5VKsJEowcujxxCjvQQJjjRpK7z8D8wkXGgt5pasYr81dPzGuoPVV8vwHSP1FKWs3535UncnmSxMPZaj1oEYScwwSayUYQTSZFBBzzJb6rMGMdMrCTkGew9hCzRVFcidfDUPwpaqpxtLkXJhAdBQCVd6D7XJwwgagcSLjwdtuwh42neDLKGP77gRY6JCMXrhJS9EmsMAu8aqAaxoaoGHAMd5dGGcCoM2bE55CyDZSCXGi9Ce84GCNr7CvPBCN2q6pMH99sw5xJUi5Tm258RAYEcLw4Yg4ANCopT7t7zMMTe2tTejYcrre3ZYwFeXwpEiPMFyBNiBYdH8JwWdwNAKbFq",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### initiator <--- (2018-10-16 17:14:39.639)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkR1PQ4j5pVSz1ekdSnwJ3V6siYq4QTQuD29tgifNkueFpFEpTam5VKsJEowcujxxCjvQQJjjRpK7z8D8wkXGgt5pasYr81dPzGuoPVV8vwHSP1FKWs3535UncnmSxMPZaj1oEYScwwSayUYQTSZFBBzzJb6rMGMdMrCTkGew9hCzRVFcidfDUPwpaqpxtLkXJhAdBQCVd6D7XJwwgagcSLjwdtuwh42neDLKGP77gRY6JCMXrhJS9EmsMAu8aqAaxoaoGHAMd5dGGcCoM2bE55CyDZSCXGi9Ce84GCNr7CvPBCN2q6pMH99sw5xJUi5Tm258RAYEcLw4Yg4ANCopT7t7zMMTe2tTejYcrre3ZYwFeXwpEiPMFyBNiBYdH8JwWdwNAKbFq",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### initiator <--- (2018-10-16 17:14:39.644)
```javascript
{
  "id": -576460752303423406,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 698
    },
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 402
    }
  ]
}
```

#### initiator <--- (2018-10-16 17:14:39.645)
```javascript
{
  "id": -576460752303423405,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 402
    },
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 698
    }
  ]
}
```

#### responder ---> (2018-10-16 17:14:39.645)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
    "to": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7"
  }
}
```

#### responder <--- (2018-10-16 17:14:39.649)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQMHEA1mtKNn37Axft4bdXTb4dHq1Rf9meBhQFV1MZX5FqsLs3WJsp7s2uDjzFQnQgmX5WSjp9wy9AyrWqrUjGZjmA5zAb5VFRxzRukAdqFFMs9nx9Gjzdpe6wfWq1pyE2rWsSzo85NEsYmymdFWtt81oD59PMxJpTwk1jF1jb51zYtFstpdTEVi2bD8NbCnHTbFDLN9exGChx"
  }
}
```

#### responder ---> (2018-10-16 17:14:39.650)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4kPwDJAgYG6s8gyh2rqs2n4HJpoNWDzNnTpF9zR3xtACeWnJ9hD5BwxRRyqxXuykDgnBmThWasYTtha1zhsmmnrg72gayY3wxf29j7cBQ5kzqmmVQ3TA925wmyhEnKsgMuTTyZ1NeRabnriiQAWB9y4mGwqfjAHJWr4Vk3rCLFd4H6LxN21TdChYmTFtN5dZ3EBGQNmf7DkXrcHCnPhtiTQZVuPPJMLLDby5tKvohpeCTst4oRc2VAA1MbK7DyATcskKPcmatzcsxDyojvkGnhGYYPyZVgmXWbFq8i514E6SvGn"
  }
}
```

#### initiator <--- (2018-10-16 17:14:39.681)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### initiator <--- (2018-10-16 17:14:39.682)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQMHEA1mtKNn37Axft4bdXTb4dHq1Rf9meBhQFV1MZX5FqsLs3WJsp7s2uDjzFQnQgmX5WSjp9wy9AyrWqrUjGZjmA5zAb5VFRxzRukAdqFFMs9nx9Gjzdpe6wfWq1pyE2rWsSzo85NEsYmymdFWtt81oD59PMxJpTwk1jF1jb51zYtFstpdTEVi2bD8NbCnHTbFDLN9exGChx"
  }
}
```

#### initiator ---> (2018-10-16 17:14:39.683)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4urCFLseG9pjWHF9KV353oEzt3SNeCaQLgwjc755j1XAWFTnRHJ34FnJfgmQEjMEmCAAE9D9KEy9MRrXwoRC9PEsYzsrVezxc141h3dWmipp1xT2YwMtZYnsnMW1HnUS5znthf5QWCiADLYzjbTVJKa4o1PF4G4sBkyibfaCvJXJNTythV4dXtcEGC2cnrMsjg64JfqsmRad6R6WWqYY4Qc4EpmxStUDLhmexzJqj3mwHd7E49ui2NdYYxMqEpu6w4TXd92sW9kDxPjmBkBhW5HvXFrTTmv7YAQyHFmWKiLcCHP"
  }
}
```

#### initiator <--- (2018-10-16 17:14:39.689)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkKAfm1acckjWT6Dm1WdVqj4xXBnDBTGwckZexwGkQCkEihbsB53NNz9L1wMaDp6Ltro1LS5TwRf6JCBsPcT4VGsFtrSbKp7ihXWHf3TDYKXeCr5sCUFbaYsrqbv7WdkEyoQx5v2Qgrah2MKLCEMtdX4om5tzmUY7NNtq6akWUEvXW9WDxBAn7pMVzTtURvndq8r4HED86boPr39sDTHNa9z3pQ7Nj8X3knUVChFaHLwaofdkZnrEfA4KriW4bTY5ZwSgokjx9JqvzXjR8onJN6XMUVRjFRZ5HueQsbaS53RY66dP68npPezWhhbYpSiTQmUtXofJFkYtQ9A8wB7mTiczsoWai5nCjG9BxsFthUV1kfSjdKVdkpQm6n9e43h8WHRQJ65so",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### responder <--- (2018-10-16 17:14:39.689)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkKAfm1acckjWT6Dm1WdVqj4xXBnDBTGwckZexwGkQCkEihbsB53NNz9L1wMaDp6Ltro1LS5TwRf6JCBsPcT4VGsFtrSbKp7ihXWHf3TDYKXeCr5sCUFbaYsrqbv7WdkEyoQx5v2Qgrah2MKLCEMtdX4om5tzmUY7NNtq6akWUEvXW9WDxBAn7pMVzTtURvndq8r4HED86boPr39sDTHNa9z3pQ7Nj8X3knUVChFaHLwaofdkZnrEfA4KriW4bTY5ZwSgokjx9JqvzXjR8onJN6XMUVRjFRZ5HueQsbaS53RY66dP68npPezWhhbYpSiTQmUtXofJFkYtQ9A8wB7mTiczsoWai5nCjG9BxsFthUV1kfSjdKVdkpQm6n9e43h8WHRQJ65so",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### initiator <--- (2018-10-16 17:14:39.694)
```javascript
{
  "id": -576460752303423404,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 401
    },
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 699
    }
  ]
}
```

#### initiator <--- (2018-10-16 17:14:39.696)
```javascript
{
  "id": -576460752303423403,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 401
    },
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 699
    }
  ]
}
```

#### responder ---> (2018-10-16 17:14:39.696)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
    "to": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7"
  }
}
```

#### responder <--- (2018-10-16 17:14:39.700)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQMHEA1mtKNn37Axft4bdXTb4dHq1Rf9meBhQFV1MZX5FqsSHZMrRHKCkpyjXNJuFgYpcF1BPDvf3JPuQTmxUxJVNBaFahkLcgcwB4qcLcz2SxqRummoK4htiswwQiYE6gnWzmDjyzwoaxTMFsdsrJcc4TNowCf46nj8n4tECEcyBZLDtU5BaYqaGVSt4D11Qi2UiF75mJ3Uqo"
  }
}
```

#### responder ---> (2018-10-16 17:14:39.700)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4yt44qGXVfGBJHVyKCHvamnbw8MGmuQYbeW2gNnFk4DF9XPn2HyCbdLCPpEUu9tGcPhVQS7abxVTUMw6D7yH9yp2E38YGXsG3RFFVyi6FJ3dxLbdNbsNdceNHrU4TDWaymhdEf6GaStJsxZVVQm2DNg5hoxPgF3xrYsEDGeaEumw2uu4XEvhUh6brs5auatr3iPN9JABSA1oUiYvT5gXH3NnsxRXJxFC8xrtEabxYUYWMFB7oJgeQgDCGPmaisDhnwcHvzJMeeUBgdguZS5aqu721Ld9zpUuaotKt4HTf6oXuLh"
  }
}
```

#### initiator <--- (2018-10-16 17:14:39.704)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### initiator <--- (2018-10-16 17:14:39.704)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQMHEA1mtKNn37Axft4bdXTb4dHq1Rf9meBhQFV1MZX5FqsSHZMrRHKCkpyjXNJuFgYpcF1BPDvf3JPuQTmxUxJVNBaFahkLcgcwB4qcLcz2SxqRummoK4htiswwQiYE6gnWzmDjyzwoaxTMFsdsrJcc4TNowCf46nj8n4tECEcyBZLDtU5BaYqaGVSt4D11Qi2UiF75mJ3Uqo"
  }
}
```

#### initiator ---> (2018-10-16 17:14:39.705)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak52crFFuGdJepuAJnEn6UWWDFwLYojNPEkn74pTbAVTf7GAJGrk4eafynezk5X21Yu98dJbGovGzxZQNj6zmUbgEhaLpE1ZqQdfSjo65sUNytF8eFeg3doKo8nFagaCcRYmiRQHfPyMACg6aNeymRrY4qRp6Av1rN9MZu3zR7X3Dv29ZHidHi1adjWfc7d9EAK3quR2ik3ri3DNEg6y3VkyoJqczYftxRii4Y3XTWsdiGYhqNFD8UqQbABiBwDMhempc3vYBSV7UvHuEtcf3opPC3beMSJvnimHYd9XvUFuaS54s"
  }
}
```

#### initiator <--- (2018-10-16 17:14:39.710)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkiMG8185X1AXbZDconreTmgEnW8VZZEkiTZf9bJziCgbhDNEx1ZWAnM1dezmxU3PdH4vWHTFH8JwzRDdY1YMvRs8ujWd2SWHSkmHHHxyJkd64Lk7jSKG5eogLjh498EK6LXmRLK6m2n3BycVuwt4mJHZXxawTHQbk95uqSR9aaT5XWmKrCyhn7cKR96Vw49jaZRknAYnGUuMkzH628o3bTLE5VSAGPMsbDJeSuWFH2FpGtqfJVyYJr4YEMBdeaTKWwYHZ2Eue1czaGk2haronK1A77XaZB5RV2aJTLuceHxSNq1WC4PNFd8BRNwo4e91hjNc7y7rhB9otoH7KANZAtGxZ4EXWcxwcDsyKYMRWkVBdjgVBABukGNrEey5dEcs3uMJCbg4y",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### responder <--- (2018-10-16 17:14:39.710)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkiMG8185X1AXbZDconreTmgEnW8VZZEkiTZf9bJziCgbhDNEx1ZWAnM1dezmxU3PdH4vWHTFH8JwzRDdY1YMvRs8ujWd2SWHSkmHHHxyJkd64Lk7jSKG5eogLjh498EK6LXmRLK6m2n3BycVuwt4mJHZXxawTHQbk95uqSR9aaT5XWmKrCyhn7cKR96Vw49jaZRknAYnGUuMkzH628o3bTLE5VSAGPMsbDJeSuWFH2FpGtqfJVyYJr4YEMBdeaTKWwYHZ2Eue1czaGk2haronK1A77XaZB5RV2aJTLuceHxSNq1WC4PNFd8BRNwo4e91hjNc7y7rhB9otoH7KANZAtGxZ4EXWcxwcDsyKYMRWkVBdjgVBABukGNrEey5dEcs3uMJCbg4y",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### initiator <--- (2018-10-16 17:14:39.714)
```javascript
{
  "id": -576460752303423402,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 400
    },
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 700
    }
  ]
}
```

#### initiator <--- (2018-10-16 17:14:39.716)
```javascript
{
  "id": -576460752303423401,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 700
    },
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 400
    }
  ]
}
```

#### initiator ---> (2018-10-16 17:14:39.717)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
    "to": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb"
  }
}
```

#### initiator <--- (2018-10-16 17:14:39.721)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQMHEA1mtKNn37Axft4bdXTb4dHq1Rf9meBhQFV1MZX5FqsXi5DPxkWYUkjj4VD1GLfNew2cBXcjBwj8AgXKiQvTqcS6UMxvMt9gTqheBW7S1D5rUh4fWGZKoELx4T8L388QzTYtojdPqB5Wfc1EeQAgkaNC4SNVeRRtWodWKfs3dizCqay6XfivqiGCabWarqEc5fBzHwEdHu"
  }
}
```

#### initiator ---> (2018-10-16 17:14:39.722)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4ys7gGdA8b18JYvNszURnF8C8SJSQ1fTPUpAFBPk7TTddKQDFJrvXNBtchPHK2YfXAxyVtmNGZKmyttTECN1tMn3AUE7UfWT9V8qMKxzvFYMQe1X68Hng3KfFfszukk8xneWzoV3oj9NHfqSY3aM92ThYuMR5mJwEFUiRoN2mGiSBymERBKHjCgBZdj6pbEZoznW1L5yzXLGdC9GYNgXN3QbdtTx3mn3gPhXBLijmQzqKGxWRK2eBgd8PWeyYA2BLtNoZBFcxju7TFA7AHot4249unP7n7BPFtXkANosUGXvbdu"
  }
}
```

#### responder <--- (2018-10-16 17:14:39.759)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### responder <--- (2018-10-16 17:14:39.760)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQMHEA1mtKNn37Axft4bdXTb4dHq1Rf9meBhQFV1MZX5FqsXi5DPxkWYUkjj4VD1GLfNew2cBXcjBwj8AgXKiQvTqcS6UMxvMt9gTqheBW7S1D5rUh4fWGZKoELx4T8L388QzTYtojdPqB5Wfc1EeQAgkaNC4SNVeRRtWodWKfs3dizCqay6XfivqiGCabWarqEc5fBzHwEdHu"
  }
}
```

#### responder ---> (2018-10-16 17:14:39.763)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4tRjZYorkNTkuouJUfSC6wAwH6DDZpRGokAi9AZZ5PGB7RBmHE5d4JG9xecwbbuXT43wLrrm4dM1ri725itL8EmBZoqtcKhUwSGuEixt1zC2rFZHnha17ikpzUXvWHf4bE1YFrkuCuf1j4X5n6UfeBJQpGXY1dgQh3U5fhM6ggAa2MMUU9GyuKupdP1ZXKNNzps43NGuNFrnWLy7FHXgCwK6CUspNhsgRkHw6ruhzRKEe4tp3weHDSCsDyvcNAKMBY2MsVWrTzxXwpDcpCpb36H9CXgVvehD3frVM7V5Ko69VCe"
  }
}
```

#### responder <--- (2018-10-16 17:14:39.778)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkYyTQ8DQuCdCWcPFSZYenoF5UG9xMN3k37qgR973554sYZyaiBZGX9MUYwXKkniBBS1McsG2GEGJTANvoKu7Wwau8jSqUBYxnT771PhMn6SwzmQHYHrfcdZYNsRZUAEEWa82TLVMEn9dC88heet4JnA7RqKhSUWV3J1wGg2dVXopBEyQGmCXBk7LnXVpeNbSg2ifeRoY9DLWNPs9xzh5AduMiwxsBgisbCJQs5nCCat4mx9Tp7PTn2PZkAoNECH9A9WLk2N7ZRgjFzze7jeG3Xcwt9jH8gaEJrD5SdvzBk2GX9ANJadtAzVXt5NohwTB3f6QEt4bY3Yy18zRgWCcfoAiKWF12auN3CR8vNQt3fExMhtGL5yDoZH4KVcGqPnR3EwPxqtyz",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### initiator <--- (2018-10-16 17:14:39.779)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkYyTQ8DQuCdCWcPFSZYenoF5UG9xMN3k37qgR973554sYZyaiBZGX9MUYwXKkniBBS1McsG2GEGJTANvoKu7Wwau8jSqUBYxnT771PhMn6SwzmQHYHrfcdZYNsRZUAEEWa82TLVMEn9dC88heet4JnA7RqKhSUWV3J1wGg2dVXopBEyQGmCXBk7LnXVpeNbSg2ifeRoY9DLWNPs9xzh5AduMiwxsBgisbCJQs5nCCat4mx9Tp7PTn2PZkAoNECH9A9WLk2N7ZRgjFzze7jeG3Xcwt9jH8gaEJrD5SdvzBk2GX9ANJadtAzVXt5NohwTB3f6QEt4bY3Yy18zRgWCcfoAiKWF12auN3CR8vNQt3fExMhtGL5yDoZH4KVcGqPnR3EwPxqtyz",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### initiator <--- (2018-10-16 17:14:39.786)
```javascript
{
  "id": -576460752303423400,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 699
    },
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 401
    }
  ]
}
```

#### initiator <--- (2018-10-16 17:14:39.788)
```javascript
{
  "id": -576460752303423399,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 401
    },
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 699
    }
  ]
}
```

#### responder ---> (2018-10-16 17:14:39.788)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
    "to": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7"
  }
}
```

#### responder <--- (2018-10-16 17:14:39.792)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQMHEA1mtKNn37Axft4bdXTb4dHq1Rf9meBhQFV1MZX5Fqsd8b4wWDhtCgVibc78wg7Rfi84XMt2qZE1BhcuzKmzaEYnQw63MBvpfP2VkCTadAChq2muwvUPxkWna7xjqzeXFPfdhr6w1mp6ENQbm9bnawz91RKUrZ2CtEDh7FjghJAYCyie15gShuFHzBwS5HqXiBUkcokbDH"
  }
}
```

#### responder ---> (2018-10-16 17:14:39.793)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak53BfesP8G95ZdhYatbqccA6ZfE5Ra1VTtrsEUrcmRMKpsDTCZbHDDkQZxMMfABy7kbxpn2bTwdYJPSfHjRNX2k7D3s7gbZf5rfYKvHdu1W2pvh9s3tvSxv9osgCAJwfveS8FpjeQDmhN9EQw9TvkM7N1R2Zt9kEzS67nHSqP533NckTvK9MuK6y8Vzq46xmB8bNUboxixvdzumKKG7P7VaUbxW7FdhPNuU5F42Zwvfk1jQndaupA1gmUcJsyM5Gb7JSTGsAhAnk2Hup5gdtBiC46byGi73UcioJ5R6GTS9pVjxn"
  }
}
```

#### initiator <--- (2018-10-16 17:14:39.816)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### initiator <--- (2018-10-16 17:14:39.817)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQMHEA1mtKNn37Axft4bdXTb4dHq1Rf9meBhQFV1MZX5Fqsd8b4wWDhtCgVibc78wg7Rfi84XMt2qZE1BhcuzKmzaEYnQw63MBvpfP2VkCTadAChq2muwvUPxkWna7xjqzeXFPfdhr6w1mp6ENQbm9bnawz91RKUrZ2CtEDh7FjghJAYCyie15gShuFHzBwS5HqXiBUkcokbDH"
  }
}
```

#### initiator ---> (2018-10-16 17:14:39.819)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak5ATKRqmhrXiBvhav2fqPCBbRE5h4G6sni4T4dj4bqnPQhJ3w43WUS9FRnnay6WhEm1Boz17MaD4p61RL2mCxyh3MEze3J6roXYd3XbLbZXZUSoHftwukjJR6Ra9XmVjDZXh4rZ5qbJJU6vLWaqyuuotSwXExvjSJWKZ8N6RgXixVUWdxPes3eUUvtGHCi2nifSYUiMfjQaWbyRFrNuQg63S7ziPg5mWaiuGdQyF1TZYt8UtgH5zSzyg7Lp6RvrQGWyj4y6qh5w2cpxyghuF6iPQ5yCzeXCAJ87LWAp4qtYeQqgz"
  }
}
```

#### initiator <--- (2018-10-16 17:14:39.827)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkp2gF48ZLYydXDH28ytssvzznQRjD5BUfa4mCKn2gC7C73UAyKJKy4PktguyvSG7SRME3dpmTYHGhYRKmZRZPbBXK3wBJBq618x5XQwDekhnZ7D1t59ePmfoPTQmMSfdrfXk5XemKbLFCDrqBjmvRUPRPeaLUyXYuWshnC49F2Rd8jKnjN7qQ6qnMN1K799YJQb1qsvawptFS6BNzpaNDxgGzTcP16hbXa7mwexTSjqDCowJbxbaSv8EaHzfQg7nMBaA97Z8gtxpUf45PsXJaz3t5nUgRQsJiKxRLuykwN7STXrzE1R7wv2NXcW5f8QrWS6vx3cBVdsJBEhPnPzF6aC4d7Z8rvUnQ5iAnW6zwVwMbtCgPHbmkGzKARNX8EicERqAqXkY8",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### responder <--- (2018-10-16 17:14:39.828)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkp2gF48ZLYydXDH28ytssvzznQRjD5BUfa4mCKn2gC7C73UAyKJKy4PktguyvSG7SRME3dpmTYHGhYRKmZRZPbBXK3wBJBq618x5XQwDekhnZ7D1t59ePmfoPTQmMSfdrfXk5XemKbLFCDrqBjmvRUPRPeaLUyXYuWshnC49F2Rd8jKnjN7qQ6qnMN1K799YJQb1qsvawptFS6BNzpaNDxgGzTcP16hbXa7mwexTSjqDCowJbxbaSv8EaHzfQg7nMBaA97Z8gtxpUf45PsXJaz3t5nUgRQsJiKxRLuykwN7STXrzE1R7wv2NXcW5f8QrWS6vx3cBVdsJBEhPnPzF6aC4d7Z8rvUnQ5iAnW6zwVwMbtCgPHbmkGzKARNX8EicERqAqXkY8",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### initiator <--- (2018-10-16 17:14:39.833)
```javascript
{
  "id": -576460752303423398,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 400
    },
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 700
    }
  ]
}
```

#### responder ---> (2018-10-16 17:14:39.904)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### responder <--- (2018-10-16 17:14:39.909)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "tx": "tx_2C9estKT2QsE1d8S9R8GbPZWuPxfDzWpStYffSNxBoDY1qskrbk1MEzHSvbw3VEMksqfCuvhEaH1qk15F2uT8dernWVVVeMS1nBeCNmJjMQxH3FUTASs6VR4u5cYXNddcMJuSoTAdn6pbTbNynoh8HaJ2kGj5b"
  }
}
```

#### responder ---> (2018-10-16 17:14:39.910)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "tx": "tx_2WsEQsiC5XsmYReupKJiM4JcMeDiHPnQRTccNFSQbvQaoZBghnCjiDusgh68GEuwEz5MnD8CkULZcsMzUjvXNin3X8hbCEromxXfzr3Cdh13nrANH5DpFRpUpZwNhCV8H4apQweTReQkzrN51fEzcCDQ9BnhtKRa8eWn99G2Af9EtqRcuSrTayzo9wuhBxmcVxoyrnn4vc8tnRebXFNnoBRk9P3a6zLn8h2oAuR5hwj7ikBPism8UFZLnaDoeYTpoG2"
  }
}
```

#### initiator <--- (2018-10-16 17:14:39.911)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "withdraw_created",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### initiator <--- (2018-10-16 17:14:39.912)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "tx": "tx_2C9estKT2QsE1d8S9R8GbPZWuPxfDzWpStYffSNxBoDY1qskrbk1MEzHSvbw3VEMksqfCuvhEaH1qk15F2uT8dernWVVVeMS1nBeCNmJjMQxH3FUTASs6VR4u5cYXNddcMJuSoTAdn6pbTbNynoh8HaJ2kGj5b"
  }
}
```

#### initiator ---> (2018-10-16 17:14:39.913)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "tx": "tx_2WsEQsiC5XsnCQxuicqrhKLtLoQbZaY3yduPAJdremCUtbh97iPcyNjgywgCmeL6K4hkXpB9NJm3nmnBgtAg3f3arbqeQxtygET6g8HxeTDsGD3YQ11SnqsuKeieGwpXhuteYd2433tDWa5KkMs4r35SSrvDTEZCSnTxosRmsSbGRdZ2GkQV3KCzPWW2QuW6vmt8wucpPrmw95q9T7RuFnrLhJkf7kb8cetGbJpjZLb5Z9qpRauQXjBN6W6nPhcL5UL"
  }
}
```

#### initiator <--- (2018-10-16 17:14:39.914)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3cDMp6242sBxwtt3yHZnTBic73auVRXpsXuSEXfDabpkiWcUN9HZazAoMpAKTH9aecLrHj5QttB1Nzft2NX1e8gkabunWvA3USjKi2cJUjLiGjuHtDea8jMdx5XSWA7PxeQ5WofESG8e5mdTHTTbzHA1VEMPAD1ZvVhPRSSvPcF7NjdjPnufavsnYwhAHnVXQPk1WhaRnuE9ha8Qc57H4b8uwLL7VcAzgPJgMgH9aby6M1sVXRZZNGt7LAcm3Fw2if7jh4pUnpe4sajvWMmhm6Cw2GA1i9sAZoAREyPZA9hCxqydrQujFGcLHTH3RXrKXsmH4t5LhGxvjddST9nDTFhs3Vj1g",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### responder <--- (2018-10-16 17:14:39.915)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3cDMp6242sBxwtt3yHZnTBic73auVRXpsXuSEXfDabpkiWcUN9HZazAoMpAKTH9aecLrHj5QttB1Nzft2NX1e8gkabunWvA3USjKi2cJUjLiGjuHtDea8jMdx5XSWA7PxeQ5WofESG8e5mdTHTTbzHA1VEMPAD1ZvVhPRSSvPcF7NjdjPnufavsnYwhAHnVXQPk1WhaRnuE9ha8Qc57H4b8uwLL7VcAzgPJgMgH9aby6M1sVXRZZNGt7LAcm3Fw2if7jh4pUnpe4sajvWMmhm6Cw2GA1i9sAZoAREyPZA9hCxqydrQujFGcLHTH3RXrKXsmH4t5LhGxvjddST9nDTFhs3Vj1g",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### responder <--- (2018-10-16 17:14:41.153)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_withdraw_locked",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### initiator <--- (2018-10-16 17:14:41.153)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_withdraw_locked",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### initiator <--- (2018-10-16 17:14:41.154)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "withdraw_locked",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### responder <--- (2018-10-16 17:14:41.154)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "withdraw_locked",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### responder <--- (2018-10-16 17:14:41.157)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3cDMp6242sBxwtt3yHZnTBic73auVRXpsXuSEXfDabpkiWcUN9HZazAoMpAKTH9aecLrHj5QttB1Nzft2NX1e8gkabunWvA3USjKi2cJUjLiGjuHtDea8jMdx5XSWA7PxeQ5WofESG8e5mdTHTTbzHA1VEMPAD1ZvVhPRSSvPcF7NjdjPnufavsnYwhAHnVXQPk1WhaRnuE9ha8Qc57H4b8uwLL7VcAzgPJgMgH9aby6M1sVXRZZNGt7LAcm3Fw2if7jh4pUnpe4sajvWMmhm6Cw2GA1i9sAZoAREyPZA9hCxqydrQujFGcLHTH3RXrKXsmH4t5LhGxvjddST9nDTFhs3Vj1g",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```

#### initiator <--- (2018-10-16 17:14:41.158)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3cDMp6242sBxwtt3yHZnTBic73auVRXpsXuSEXfDabpkiWcUN9HZazAoMpAKTH9aecLrHj5QttB1Nzft2NX1e8gkabunWvA3USjKi2cJUjLiGjuHtDea8jMdx5XSWA7PxeQ5WofESG8e5mdTHTTbzHA1VEMPAD1ZvVhPRSSvPcF7NjdjPnufavsnYwhAHnVXQPk1WhaRnuE9ha8Qc57H4b8uwLL7VcAzgPJgMgH9aby6M1sVXRZZNGt7LAcm3Fw2if7jh4pUnpe4sajvWMmhm6Cw2GA1i9sAZoAREyPZA9hCxqydrQujFGcLHTH3RXrKXsmH4t5LhGxvjddST9nDTFhs3Vj1g",
    "channel_id": "ch_bKhwFgj61j5RAf5Ld4uLPMVCQ9DdZJNXuhhfRXbyFUR25Wm7"
  }
}
```
