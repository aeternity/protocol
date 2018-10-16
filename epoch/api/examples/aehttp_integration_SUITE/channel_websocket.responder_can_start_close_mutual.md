
#### initiator init (2018-10-16 20:25:46.124)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A&role=initiator
```

#### responder init (2018-10-16 20:25:46.130)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A&role=responder
```

#### responder <--- (2018-10-16 20:25:47.130)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 20:25:47.134)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 20:25:47.144)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpALFUXGGsdug6Jrs56usDVK43SheHuLKP3h48aDzajQnhSXBUWq2rVDufMiousdvbextEcPQPuUq7817TtZyDq2vCt4rqTh3SqYy9jCHBN6SuCufA4j65Xrud4Spcwoi5gsMaowEXQETWMtFFZcbw7DeBoV2oj38"
  }
}
```

#### initiator ---> (2018-10-16 20:25:47.203)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HjrehqztczhFqXi8eMGB3JbPdBQ7N9PxUTXXenecFpJGcTDrAeaLxkdzfgHCut7xehDiam2jAdoSXfoieHu8c2N2eVSAU6yEka5k2S2kf8MCnxdq3Gf2Pytq2FWNUghoino7vQssRwGF5XcLG5j6tAZagfWNKPKYKN4UaHuohqBo2KbVAgUB3GkaPtfU7NFwAU1m79E2vKeYRtghJmWxESRMPt4mfNe8d8D2F1svySckaGWykFU9qsvGBVvgDkVyK"
  }
}
```

#### responder <--- (2018-10-16 20:25:47.204)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 20:25:47.205)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpALFUXGGsdug6Jrs56usDVK43SheHuLKP3h48aDzajQnhSXBUWq2rVDufMiousdvbextEcPQPuUq7817TtZyDq2vCt4rqTh3SqYy9jCHBN6SuCufA4j65Xrud4Spcwoi5gsMaowEXQETWMtFFZcbw7DeBoV2oj38"
  }
}
```

#### responder ---> (2018-10-16 20:25:47.206)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HoowS5GNueERzSN8dHTeUVtiHLS5pgH54rx28BHbqkme5R8Vi8zU742fRAAfx9ovDVtSTB7mZGccRcaVEvfVRDYTJnhJZJD4ZBG7VA9xhw8W6vkaGYmpb8ifGDbwUTjUpEsxJzLPpKQFtG68HgMSTr8xRMCtnyZb3rRiAPsb751pQHeo8MZA38a4J7BBucNFScAQpvo9z3WPmoXRoE2tWpka8R9acKAVrZUpDh3gfL3DfmjhXEu9Y6HyJgu1VNLXi"
  }
}
```

#### initiator <--- (2018-10-16 20:25:47.208)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 20:25:47.209)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmMxeLaycr8FQ5ZFWNZ8b3vHmurJsBitant9Kk3e3EYkC3q99VE3Sxb8H9d2qj85o6sUzX2PNz8V4ZTRfHQAADRAJyAJUPsNWsg55S7tJwmzoFiUf2ZsPVo9Lyyt1ZRG3nsiocKNJRdJfKmGxNHA76vb9Dd1UcUByLxPwk3cJkDUkUVaaNwXRqepDnrgRLGyNrvLXsZxhWfLdZsMfWUgmUXYqDjrnMUMxjdPdm9EAFCZVCnK4mXGBSzj3ueY4NEx4UG3boCcJrfexAxTZyESShKMGtLy5VokRVxtGZwnkX4vQgjjKK46R3pUjt9jiTiKse2Dh9QbgoU3zqnVTDHyDMe5AKyh"
  }
}
```

#### initiator <--- (2018-10-16 20:25:47.210)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmMxeLaycr8FQ5ZFWNZ8b3vHmurJsBitant9Kk3e3EYkC3q99VE3Sxb8H9d2qj85o6sUzX2PNz8V4ZTRfHQAADRAJyAJUPsNWsg55S7tJwmzoFiUf2ZsPVo9Lyyt1ZRG3nsiocKNJRdJfKmGxNHA76vb9Dd1UcUByLxPwk3cJkDUkUVaaNwXRqepDnrgRLGyNrvLXsZxhWfLdZsMfWUgmUXYqDjrnMUMxjdPdm9EAFCZVCnK4mXGBSzj3ueY4NEx4UG3boCcJrfexAxTZyESShKMGtLy5VokRVxtGZwnkX4vQgjjKK46R3pUjt9jiTiKse2Dh9QbgoU3zqnVTDHyDMe5AKyh"
  }
}
```

#### initiator <--- (2018-10-16 20:25:47.894)
```javascript
{
  "id": -576460752303423463,
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

#### initiator <--- (2018-10-16 20:25:48.830)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### responder <--- (2018-10-16 20:25:48.832)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### responder <--- (2018-10-16 20:25:48.833)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### initiator <--- (2018-10-16 20:25:48.833)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### responder <--- (2018-10-16 20:25:48.836)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### initiator <--- (2018-10-16 20:25:48.836)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### responder <--- (2018-10-16 20:25:48.837)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmMxeLaycr8FQ5ZFWNZ8b3vHmurJsBitant9Kk3e3EYkC3q99VE3Sxb8H9d2qj85o6sUzX2PNz8V4ZTRfHQAADRAJyAJUPsNWsg55S7tJwmzoFiUf2ZsPVo9Lyyt1ZRG3nsiocKNJRdJfKmGxNHA76vb9Dd1UcUByLxPwk3cJkDUkUVaaNwXRqepDnrgRLGyNrvLXsZxhWfLdZsMfWUgmUXYqDjrnMUMxjdPdm9EAFCZVCnK4mXGBSzj3ueY4NEx4UG3boCcJrfexAxTZyESShKMGtLy5VokRVxtGZwnkX4vQgjjKK46R3pUjt9jiTiKse2Dh9QbgoU3zqnVTDHyDMe5AKyh",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### initiator <--- (2018-10-16 20:25:48.838)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmMxeLaycr8FQ5ZFWNZ8b3vHmurJsBitant9Kk3e3EYkC3q99VE3Sxb8H9d2qj85o6sUzX2PNz8V4ZTRfHQAADRAJyAJUPsNWsg55S7tJwmzoFiUf2ZsPVo9Lyyt1ZRG3nsiocKNJRdJfKmGxNHA76vb9Dd1UcUByLxPwk3cJkDUkUVaaNwXRqepDnrgRLGyNrvLXsZxhWfLdZsMfWUgmUXYqDjrnMUMxjdPdm9EAFCZVCnK4mXGBSzj3ueY4NEx4UG3boCcJrfexAxTZyESShKMGtLy5VokRVxtGZwnkX4vQgjjKK46R3pUjt9jiTiKse2Dh9QbgoU3zqnVTDHyDMe5AKyh",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### initiator: (2018-10-16 20:25:49.321)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-16 20:25:49.321)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-16 20:25:49.321)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-16 20:25:49.321)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-16 20:25:49.321)
> Channel is `open` and ready to use

#### responder: (2018-10-16 20:25:49.321)
> Channel is `open` and ready to use

#### initiator <--- (2018-10-16 20:25:49.353)
```javascript
{
  "id": -576460752303423462,
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

#### initiator ---> (2018-10-16 20:25:49.353)
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

#### initiator <--- (2018-10-16 20:25:49.358)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTsY6buDedLd9oVUjzmMq4jyrYUQvQVmLRJsmoqVs5TZSjUteebvFFidZMRMWL5E9H9HoGWyWAYU18a59PKVcUNkxnBwtQrDrfUoeykWTE3UCgVGaqqqM42BEKKJqSEhcYgNoUpcATE31d8FQQD4S3fLHs7USL9cxnwqGbFkipaSFWBrTdaZ4GTMaxCRFPzkH2Nvnco6RpZVG"
  }
}
```

#### initiator ---> (2018-10-16 20:25:49.359)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak57KndS6w9b6DZD1jEc5qkcRfGPnwRgifHq9QoPg9m8ubuLKXaGZapQDQGLwAgTX2cqFpdtEEjKH8F2Vh2bw4xeQSV5LeDL4g9FR4MWoczMgUcpx4YKePPcbYYS6PtacFDSykZmp9uS95tf521NP76P5PbrJkTPWqzNpN7DoDea9KF8sjJWhZjw4jUpB4jTjV7E7NA3GG2MB8PtVX1VPUdm8gDcoAJrf3MRP6h3TDyYtCUwDgJtNH7stwRv2ii1yLMefFLBCqx4yFRcSsBm4QfhXk7idv6mYaBQNrJtDA995VoN4"
  }
}
```

#### responder <--- (2018-10-16 20:25:49.364)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### responder <--- (2018-10-16 20:25:49.365)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTsY6buDedLd9oVUjzmMq4jyrYUQvQVmLRJsmoqVs5TZSjUteebvFFidZMRMWL5E9H9HoGWyWAYU18a59PKVcUNkxnBwtQrDrfUoeykWTE3UCgVGaqqqM42BEKKJqSEhcYgNoUpcATE31d8FQQD4S3fLHs7USL9cxnwqGbFkipaSFWBrTdaZ4GTMaxCRFPzkH2Nvnco6RpZVG"
  }
}
```

#### responder ---> (2018-10-16 20:25:49.366)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak5CJBUcTJAR2X61GRCuEmZVBTs38PsdmAiucd47ipawxM7KqqmXHALpBhDhsvPsUDkwp6onLXjQY4DLwknerSBEqYZwPvN7A7qiUFbZLZMpkyqTjDJw67yzF8Sq5wrf8azdRsBxAJ7jiMiJVCEMhrtN8HJg55ZNaxesHdgHGeJsDVeWrkkfYW2VcQotBmr9hU9HhGNMC3zXvkmkTDjbjHNP6w1S47Dywjuff7HwQsiCKy3wy7KMsaD2S8fe6UZbYgt7RWvF7A1Rd9XgzwNnJKVt7bZZgQALx3rL2STbn3wsxNmbW"
  }
}
```

#### responder <--- (2018-10-16 20:25:49.371)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkw9V3xDXUdqd1cmLzCBdbyrgf6UpSbMkTWSbaVvQ5FGnLMFcRwG6mHtAKJ6p2eCH4WWdwHKYydVebBmqtB2Hv3EvwjsbGbdySM2G8Ww8cSBnYU8kM2m3u6gU6QeaDNrunPyQkjbKf1f8PGK24tqTQ1YppMeonzrWwhD3q6K5vjnJUxWua1JLUYv2mBVSShFuX1qTFgjWJhxQBEoJbYo8VLqTvF18hQjpYb5ziV7FWHSv2YiryKr75iU2dv2q4vdx6WpGRwEBkEiQEibWEYFjJnSmiiXc6BjFsVvEb9jiw7Zixb5PojXmiqTPnrSjjgpdYLPsX5em5PmDpw82v4KpiG4RoFJd17HEmysQQ3tYDDUxkWE5GJtktNv74LRrm1DL1rwsWVtVD",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### initiator <--- (2018-10-16 20:25:49.371)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkw9V3xDXUdqd1cmLzCBdbyrgf6UpSbMkTWSbaVvQ5FGnLMFcRwG6mHtAKJ6p2eCH4WWdwHKYydVebBmqtB2Hv3EvwjsbGbdySM2G8Ww8cSBnYU8kM2m3u6gU6QeaDNrunPyQkjbKf1f8PGK24tqTQ1YppMeonzrWwhD3q6K5vjnJUxWua1JLUYv2mBVSShFuX1qTFgjWJhxQBEoJbYo8VLqTvF18hQjpYb5ziV7FWHSv2YiryKr75iU2dv2q4vdx6WpGRwEBkEiQEibWEYFjJnSmiiXc6BjFsVvEb9jiw7Zixb5PojXmiqTPnrSjjgpdYLPsX5em5PmDpw82v4KpiG4RoFJd17HEmysQQ3tYDDUxkWE5GJtktNv74LRrm1DL1rwsWVtVD",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### initiator <--- (2018-10-16 20:25:49.376)
```javascript
{
  "id": -576460752303423461,
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

#### initiator <--- (2018-10-16 20:25:49.378)
```javascript
{
  "id": -576460752303423460,
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

#### responder ---> (2018-10-16 20:25:49.378)
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

#### responder <--- (2018-10-16 20:25:49.382)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTsY6buDedLd9oVUjzmMq4jyrYUQvQVmLRJsmoqVs5TZSjaKAW9TiT4MV7QtdECBgQfPRserjCD8CEmzRVREhmY9WAgWBaLnTPftThBgEgVR8Kf2fv1YykkLWLih9MEoVnW6mRPRZWypDHPBQzVj2Nu9WFjn56N6L3m9wVP4pVuSS5mvkqJhiQ1cpPGfRHAeEcynXYH4MBhot"
  }
}
```

#### responder ---> (2018-10-16 20:25:49.383)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak59DmAZysD9EAKED6TVpC3wo1n61khUU5fYXPKDqLXCreTMtaNjKcJfXmC2CvwjHVwuyNdXxZFdv4iHFC5WCh1P4EnwUWQnNMJ5CzyjjpaaG6mBb8FY3n9Cjt3oPvWGwnPDJyAXbHcYgi2s752a8ciAEmcXzSqaiz3ny6eTEazmp7RGKsCUpw1x2JhRkDbHbXfJLHPnr2niU4jLw9pxKn3g5x79mJ6w2pF6E6yhTsxGrnLgw4QfxUR13BWMHJtR4AYQgsjHKiFA8xsdBCEDBDw5HT6vPHihxVdvDiPibT9eitBb8"
  }
}
```

#### initiator <--- (2018-10-16 20:25:49.387)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### initiator <--- (2018-10-16 20:25:49.388)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTsY6buDedLd9oVUjzmMq4jyrYUQvQVmLRJsmoqVs5TZSjaKAW9TiT4MV7QtdECBgQfPRserjCD8CEmzRVREhmY9WAgWBaLnTPftThBgEgVR8Kf2fv1YykkLWLih9MEoVnW6mRPRZWypDHPBQzVj2Nu9WFjn56N6L3m9wVP4pVuSS5mvkqJhiQ1cpPGfRHAeEcynXYH4MBhot"
  }
}
```

#### initiator ---> (2018-10-16 20:25:49.389)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak5A7qzHZX6yuBEtX1WRXZBUXWQVr1EcbsdgWB1ANbYibGemWtrrPLSLbhciKsj6bX87TnDbvsvmwRqB3FLaBpLwQuR3pMThKfFrf5N6rUVJR5rbvEgrb6EoFA2egH5PTKLZd9UWRdgeTfXtpuoLeg2jqqUS63su8ouBVYzd7oFajMzudzKE2ehUWGbq2r1cpdsFwL937BdxXe898gxfQQDvNUs4UqBALuQH6zd9SGDcXoEwHJZwcgXbDk573SZ3CMBaY7CEs6StMuJChHFn8v2GGiDrUBdeawv8ihfKhkpsnaYQ4"
  }
}
```

#### initiator <--- (2018-10-16 20:25:49.393)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkzQYpwZcM3kQReR5Zy8FgJRh7DhcrwdGS5WtnQzEVPxbzr5uc2UyvK6RweMMzhLPnGqSMDf8JDNUXqdRUvuw7xaEmDVfzGKJudJVn4pZwwm3HmdAvPwUUJA6U9i3fBLtD6DVZtiGg66oavQRUqoUxWRuuD8ZFfLRUSA22u7Lhhb7m2qESBhukBTz6DBmxkCuNudEJhxeGo6wxi5HzSwYfjmwvHv3xRL6gSRuwULRBwqTjZKrSduTu77AgHXCnHqVg5cotzTjE11rSf7VA1Hvmj69ZiDXmRJv9bSquirMtVBp4mfzdynBTuv3U4U9XmKx9B7dxFgBaYJVMzJhiWwwmoZvUKzgkaKPaPTqdyaj4PcZHACeYdqwkUxgFRDJusA6TWnayqwga",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### responder <--- (2018-10-16 20:25:49.394)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkzQYpwZcM3kQReR5Zy8FgJRh7DhcrwdGS5WtnQzEVPxbzr5uc2UyvK6RweMMzhLPnGqSMDf8JDNUXqdRUvuw7xaEmDVfzGKJudJVn4pZwwm3HmdAvPwUUJA6U9i3fBLtD6DVZtiGg66oavQRUqoUxWRuuD8ZFfLRUSA22u7Lhhb7m2qESBhukBTz6DBmxkCuNudEJhxeGo6wxi5HzSwYfjmwvHv3xRL6gSRuwULRBwqTjZKrSduTu77AgHXCnHqVg5cotzTjE11rSf7VA1Hvmj69ZiDXmRJv9bSquirMtVBp4mfzdynBTuv3U4U9XmKx9B7dxFgBaYJVMzJhiWwwmoZvUKzgkaKPaPTqdyaj4PcZHACeYdqwkUxgFRDJusA6TWnayqwga",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### initiator <--- (2018-10-16 20:25:49.399)
```javascript
{
  "id": -576460752303423459,
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

#### initiator <--- (2018-10-16 20:25:49.400)
```javascript
{
  "id": -576460752303423458,
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

#### responder ---> (2018-10-16 20:25:49.400)
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

#### responder <--- (2018-10-16 20:25:49.404)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTsY6buDedLd9oVUjzmMq4jyrYUQvQVmLRJsmoqVs5TZSjfjgMh1BeQ5QsQRk8K2gBxvAS6RoAu2Kept3QtzPWHkXewvJFC9i3cdcndP2RGWE1HzJR4sQdzxSd9Gr4Vg9iWE5eLHV6YXcxkffNrgSsVQkZQLZse7hs5bZ8Mqu5dBf4nM3K1dX2mDrHxZfopLunFd8Pen1LUpR"
  }
}
```

#### responder ---> (2018-10-16 20:25:49.405)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4ognBRfcQ1VSppw4ZE5f6shDo3wDC3g35FeHdcDpAWU1GupPmG6cuSkesnD4qkSbgTq8d8VpNpkn8rnwRF98NoZZLsXERtSWXspsoW6ERjeP3UF75Njtaee7fJzatqHKHW4cuYJQMhAx4YYQT9rj7LK2SH8DWPxVFDn3zu4MCwMzsGrQjab9uxZxAnrV9DRmTSs895uzeKELfq1XuzgNvAiWDpXGabuP5SoPsGJ61ujXr6H1Ao84vdtiyJFLr3W9T8zCDqunhoWUoetP54e8TfT1gLLbds8kfCjwxZnvtWQ6N6p"
  }
}
```

#### initiator <--- (2018-10-16 20:25:49.409)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### initiator <--- (2018-10-16 20:25:49.409)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTsY6buDedLd9oVUjzmMq4jyrYUQvQVmLRJsmoqVs5TZSjfjgMh1BeQ5QsQRk8K2gBxvAS6RoAu2Kept3QtzPWHkXewvJFC9i3cdcndP2RGWE1HzJR4sQdzxSd9Gr4Vg9iWE5eLHV6YXcxkffNrgSsVQkZQLZse7hs5bZ8Mqu5dBf4nM3K1dX2mDrHxZfopLunFd8Pen1LUpR"
  }
}
```

#### initiator ---> (2018-10-16 20:25:49.410)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4p7ta6BnLVNh68tqYnPmmh8Rby1VZDmictzfptxQZyAWVgT1knuzAqHh4QCsRxWBdmEoi2RNnBAx5nYXYxmdb6XduuX3tAsSvRTsXWbmnZbsAkMYnmduZCtPHgYgNWyiMECRC6v56sUaTYDAVpeJrQG1aQv8dVkJQRkZ3HpQTpYdknCZj8XFPRCkLihJmsx8RUHZcYoVxdtiTauppbh9sMVzWfgzgJbDXWDiaFjRgY7MPaG5z1NmDFEky1xyvfR4dGSVjwrVLid1pqEDdrVPSzzE18SvujhVJCVHCv9iJyMxHci"
  }
}
```

#### initiator <--- (2018-10-16 20:25:49.415)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkQpmB1sQuvcit75GTbCJNjPhu5ZTo96v9jDQYzeapZZaLEPMBFMuFJqLKR8LSnWCrCgkofic79kLNf1NqzWE3qCE7wmrwyG2WnPAPfzMGCrra4AnLbGPYhYQvsDV5EMjwGT5suqLMsG2R4vfMC6AAkppECrrLKanXbfCBC4HpGAbAs3A4BfQmQrM73EJikEGPxXMTCf43eErQBStBfhp6VGD8csQfbCwKhJGhexDhjyeqYqCV8EQ3hn33UYzAwPN1VRtStuJU4vovP8GpB3dzWSqWUbZwG4WCm11eS4kHKqTG5XPwEa5dqVx89N6pQfefr9TVzpXFJb4pXMr2nYefZDW3Si15hTKhsVZEaJ5o4Pi5aQqCYpMnp5VEX6dTUmez6BQQsxz1",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### responder <--- (2018-10-16 20:25:49.415)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkQpmB1sQuvcit75GTbCJNjPhu5ZTo96v9jDQYzeapZZaLEPMBFMuFJqLKR8LSnWCrCgkofic79kLNf1NqzWE3qCE7wmrwyG2WnPAPfzMGCrra4AnLbGPYhYQvsDV5EMjwGT5suqLMsG2R4vfMC6AAkppECrrLKanXbfCBC4HpGAbAs3A4BfQmQrM73EJikEGPxXMTCf43eErQBStBfhp6VGD8csQfbCwKhJGhexDhjyeqYqCV8EQ3hn33UYzAwPN1VRtStuJU4vovP8GpB3dzWSqWUbZwG4WCm11eS4kHKqTG5XPwEa5dqVx89N6pQfefr9TVzpXFJb4pXMr2nYefZDW3Si15hTKhsVZEaJ5o4Pi5aQqCYpMnp5VEX6dTUmez6BQQsxz1",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### initiator <--- (2018-10-16 20:25:49.420)
```javascript
{
  "id": -576460752303423457,
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

#### initiator <--- (2018-10-16 20:25:49.421)
```javascript
{
  "id": -576460752303423456,
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

#### initiator ---> (2018-10-16 20:25:49.422)
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

#### initiator <--- (2018-10-16 20:25:49.425)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTsY6buDedLd9oVUjzmMq4jyrYUQvQVmLRJsmoqVs5TZSjmACDEYeqjoLdPxs2Rm8d3szwqgi6cAPNik19kkfgda3EzCERQKcdK38G5cpSNjVjQ9UM1ndhn33Ab3wa1KaLgkk9fBwBvBEfEi9ZHvhXS82n75WC8BDd9DnMaQ5Vk8LGNcstzHyA8sYeHjGrPxbCiw9cRHwN9Sm"
  }
}
```

#### initiator ---> (2018-10-16 20:25:49.426)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4sh7cqDcWHBXi72WJbGtRoKkp3X2FST8Jtjs8LzpeYbqd9AftLX4jiVJHHJCvHv8utEfDbXe3Z6cG4kPevXEqyWnYfR86VbQr1xKDVbQH6hYbtESyzxiQbgyxdDuJgqwLdd31pbFNDFtmydvi1PoZXywQU7tnTY1diTZKoF1oznHd67ia3r5qQE9sRBTfuDoDKbk87pX2HaUvP8XKanqTp2iNbY8TQtawLvM7wEQL7yuhx9LS6LodjV9xFEJjALoEJRJ83j5zenWG5cyvyLnKgfvYCmgdawAiweZ1VGeGNiNMNb"
  }
}
```

#### responder <--- (2018-10-16 20:25:49.455)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### responder <--- (2018-10-16 20:25:49.456)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTsY6buDedLd9oVUjzmMq4jyrYUQvQVmLRJsmoqVs5TZSjmACDEYeqjoLdPxs2Rm8d3szwqgi6cAPNik19kkfgda3EzCERQKcdK38G5cpSNjVjQ9UM1ndhn33Ab3wa1KaLgkk9fBwBvBEfEi9ZHvhXS82n75WC8BDd9DnMaQ5Vk8LGNcstzHyA8sYeHjGrPxbCiw9cRHwN9Sm"
  }
}
```

#### responder ---> (2018-10-16 20:25:49.457)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4uhpf1dRK1SZvwGSSN8yAji7x5eFHJGpZiv9Cnw6ev3ydnKCBubywqn7Uy5xnDjUPhqErwv2taMTNuVRETZcrT8YbZ7Shyt1daRuvF3R1BS42p37Z8HPrCP7EJBdwws2MdMjSeXihqvoxHXBEEqyCNVzMrwUno5RinV7t7b45EHXU9kw7zK3mbixQRfSBGXkXv6untk9L1ULaAuxAKAv8hPqN2BXNhgfKUQidiUHG6zXWpfEgdaAwUkhRjiAzhKbhtD1eE6Pb1Urw157y5dHMV5V7rBqgcu5tMdr2tAnDZtX9BM"
  }
}
```

#### responder <--- (2018-10-16 20:25:49.461)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkXiBiMW5iHnUuSND865EYcAfXRUG4dohF2VReDUQRvBiwf6Lbfu46fNQbBwyxLmrgnmastHNcyZpLiXTwm2xzx3pAkLpYfh63qFZ3QLfyAreMaxYCrMNfgfVyiPETXtnsgVHLxes5qUe6izkyxtD3SPAYk5VzKTkXvt3kckeuXuShagVgk1Y6jtc1K12n4eQaEJby73j77nx1U5BChVPzCjSbcJR8H2bsJV9qQsR3MCH5RMHdK69PG2XLeuPiHxH2Q4tE1zN2MTkP2AhgtwyYBXM3GoG9iFd55v4nu8yQnqfCNV4nvtk7coYRXtafYu9xrFDKiNffwXdfYZU4BSRMnw5oACZXUk65hMnJLzrhPCpeGtT4ZAWgBZsCb36cgnainU8zvSc3",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### initiator <--- (2018-10-16 20:25:49.462)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkXiBiMW5iHnUuSND865EYcAfXRUG4dohF2VReDUQRvBiwf6Lbfu46fNQbBwyxLmrgnmastHNcyZpLiXTwm2xzx3pAkLpYfh63qFZ3QLfyAreMaxYCrMNfgfVyiPETXtnsgVHLxes5qUe6izkyxtD3SPAYk5VzKTkXvt3kckeuXuShagVgk1Y6jtc1K12n4eQaEJby73j77nx1U5BChVPzCjSbcJR8H2bsJV9qQsR3MCH5RMHdK69PG2XLeuPiHxH2Q4tE1zN2MTkP2AhgtwyYBXM3GoG9iFd55v4nu8yQnqfCNV4nvtk7coYRXtafYu9xrFDKiNffwXdfYZU4BSRMnw5oACZXUk65hMnJLzrhPCpeGtT4ZAWgBZsCb36cgnainU8zvSc3",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### initiator <--- (2018-10-16 20:25:49.466)
```javascript
{
  "id": -576460752303423455,
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

#### initiator <--- (2018-10-16 20:25:49.468)
```javascript
{
  "id": -576460752303423454,
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

#### responder ---> (2018-10-16 20:25:49.468)
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

#### responder <--- (2018-10-16 20:25:49.472)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTsY6buDedLd9oVUjzmMq4jyrYUQvQVmLRJsmoqVs5TZSjrai4n6835XGPPVyvYifkZydYyZw8GpaUvfHFrVkynxadUkXattDMW7vyWnbtpgRNZuZRBWGQWCKBzSFV1RTaWUi6E1LFfxSKVeA9abHrfwFAjQnY4sUA9hiTpkvCLhPu6fYxU43sdfG6NVekF1VbJd4mKm8KExQ"
  }
}
```

#### responder ---> (2018-10-16 20:25:49.473)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak5AJjjH6az3LNw6yhMDUUuf3RqY6CbeENeejZvtuqJbVb1fMAFtEkfU6hQ7AcEfMXtjxgtrFhDDHJGGruvZ2LhNQyaWZLgCsLEVeTmyEugZNb86stA32DBHtfAgoFLPNJr9hoPfDkFYzQe4oc1n3ANFwdCFXFren4fFtT4JqSKs39jtoT5LyFepgAqEoBogAATAhftYZv1ncHyV1PhobYfAEw4REhRLhkfSBcjMfLTkFLKKoYaKf9AyzHNnuTR3Uo2jf8NKmtN4P1tc2RrFvnKowjhmW2hVFma6AxhWrgDm66tZt"
  }
}
```

#### initiator <--- (2018-10-16 20:25:49.506)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### initiator <--- (2018-10-16 20:25:49.507)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTsY6buDedLd9oVUjzmMq4jyrYUQvQVmLRJsmoqVs5TZSjrai4n6835XGPPVyvYifkZydYyZw8GpaUvfHFrVkynxadUkXattDMW7vyWnbtpgRNZuZRBWGQWCKBzSFV1RTaWUi6E1LFfxSKVeA9abHrfwFAjQnY4sUA9hiTpkvCLhPu6fYxU43sdfG6NVekF1VbJd4mKm8KExQ"
  }
}
```

#### initiator ---> (2018-10-16 20:25:49.509)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4pcvkR3cs5jwhKqt8vaqWmiJAJ5ZCqVi6hsE41Nam7XJwHfwejWiMZ79qQ8G8w1ZWRr5iWKVuNZJiBEYhHDxYVYh1SP19EECm4qBNFVDPDgKA3dnYDY1dg4TnukmjaRvBNb7YUQV1mrQ7jgwn1x7k9pt9AakzZcPCNsmYreBeqcXTQVdtwCCebMxx8TXmtFLbqmFsnnh51HomNjCtDnQCBsPr6LRQKJd5wL1WRkRGzBB5AEH78DBM2FHSY5y1KVTCVvB7t19NNR3qXzzd92VyJEXy94hGLH9t4qjrU6ZCK3nndD"
  }
}
```

#### initiator <--- (2018-10-16 20:25:49.518)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkSRrLauH5bfmokkFEgYbHXfQhjfai56T8rVG6r6r1YuttrivpqQriNPshunXjGWegrrZWFvryiY5fTu9wrwMo3MNiXCn6v7ETEZQpD9TfyoTGTg36PdDJyuA9c9W2kToieWkSTP8vn4facL6DFmQYwNepVxkDinaEqmrnajdbYhXp2RR9VcsXvjKiHknYCiikzt64WcoidjPL2FcSa28zJTiTjzvD4RTd59Y8EEy5PMaEpwT5cMFEREAXwuCmFjnYoqUtM5mnVLbBgSez9prPEG4uWdGBBQAFkvamqVbemSimZhUR2PMXBgd2LiwEVuTkmvovD6HDi7V52HpXNFrDLT4yuutPGrtzEnxNCCWH3P6HTWb98nuedjkwLFaD5d1yeVtCqsBW",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### responder <--- (2018-10-16 20:25:49.520)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkSRrLauH5bfmokkFEgYbHXfQhjfai56T8rVG6r6r1YuttrivpqQriNPshunXjGWegrrZWFvryiY5fTu9wrwMo3MNiXCn6v7ETEZQpD9TfyoTGTg36PdDJyuA9c9W2kToieWkSTP8vn4facL6DFmQYwNepVxkDinaEqmrnajdbYhXp2RR9VcsXvjKiHknYCiikzt64WcoidjPL2FcSa28zJTiTjzvD4RTd59Y8EEy5PMaEpwT5cMFEREAXwuCmFjnYoqUtM5mnVLbBgSez9prPEG4uWdGBBQAFkvamqVbemSimZhUR2PMXBgd2LiwEVuTkmvovD6HDi7V52HpXNFrDLT4yuutPGrtzEnxNCCWH3P6HTWb98nuedjkwLFaD5d1yeVtCqsBW",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### initiator <--- (2018-10-16 20:25:49.529)
```javascript
{
  "id": -576460752303423453,
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

#### responder ---> (2018-10-16 20:25:49.589)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### responder <--- (2018-10-16 20:25:49.593)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "tx": "tx_2M9ipLgcZYP9wwMpiVyjmq4YWYk9CWojnWLLRmz6DsWmrutRB48VBn1yuTtS4ZCNPYgj8N4e1sxaaRh8r2GHuKmmMkvVqteW6GgYqTxdBeeNXMWafotPA"
  }
}
```

#### responder ---> (2018-10-16 20:25:49.593)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "tx": "tx_2iJcVi27J8Zz1HJQ5mHdGj4s5N1DreMarHACDUG6KmHRMeeWcCJSbGrBmFz1LAf1uxQjrNXumfSPtBmtW9VTeBoN46Pp4JhdQPxmGAt2QZHPgvbeCdPcwbyDpZtw2SQf1etx9pWhSGPu37ZkExvdKMghxCLNK9W8vn3k8M99Va5mxheogCL8TjAfxQ41zAeCcBhgfavf4dCh4NyPwCnbvToANm"
  }
}
```

#### initiator <--- (2018-10-16 20:25:49.595)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "tx": "tx_2M9ipLgcZYP9wwMpiVyjmq4YWYk9CWojnWLLRmz6DsWmrutRB48VBn1yuTtS4ZCNPYgj8N4e1sxaaRh8r2GHuKmmMkvVqteW6GgYqTxdBeeNXMWafotPA"
  }
}
```

#### initiator ---> (2018-10-16 20:25:49.595)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "tx": "tx_2iJcVi27J8Zz4pjon8qMc6d73m1uptqqNLMwh3zVmn5oPVCqDQXn79tG6UMaxaETANjUZzfw4vMcBVT5VpQHa8kZiZCUukNDk4sVFBX9M8JLNM8KbthSRjMf5yEemZz5NLHPQi8PR19J2XuuD95dhgPwxSiGRpnPCYUya2UnKecNcgoY1EADhMAyhZXM1Gb4KsSgKcfgifU3mWcrzavCNjdCiA"
  }
}
```

#### initiator <--- (2018-10-16 20:25:49.597)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3wu1WL1txa1YH3t37PrHbpy9h4CztPLtHCktCE7d7dSboqPSYAab3aMTZeJ552Ru7v5yKnrMaxzLJTp1VjmEhXw2o1Tbphwtfm77XsQ1AWbGHHyJEG3rULPvbsV7RSsi2QbcVvQTMvtKh12Py9qd5bK6uFpjfhQapdYWc6qumRMTbJhGB7d5EH9r4nbZW8dDoJtWy4WCLfcAuaeGaEzLK7kSud559bLshcMhMwyvNXk2bnVYKY4DwoXrhb4ZhqGuHC79uKJNPKXWbTs35mtBU8CcP4V9YkVaxF8GSXqvxnKdgred6JBG",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### initiator <--- (2018-10-16 20:25:49.597)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "close_mutual",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### initiator <--- (2018-10-16 20:25:49.598)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### responder <--- (2018-10-16 20:25:49.604)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3wu1WL1txa1YH3t37PrHbpy9h4CztPLtHCktCE7d7dSboqPSYAab3aMTZeJ552Ru7v5yKnrMaxzLJTp1VjmEhXw2o1Tbphwtfm77XsQ1AWbGHHyJEG3rULPvbsV7RSsi2QbcVvQTMvtKh12Py9qd5bK6uFpjfhQapdYWc6qumRMTbJhGB7d5EH9r4nbZW8dDoJtWy4WCLfcAuaeGaEzLK7kSud559bLshcMhMwyvNXk2bnVYKY4DwoXrhb4ZhqGuHC79uKJNPKXWbTs35mtBU8CcP4V9YkVaxF8GSXqvxnKdgred6JBG",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### responder <--- (2018-10-16 20:25:49.604)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "close_mutual",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```

#### responder <--- (2018-10-16 20:25:49.604)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_2p7dRhupq25RKp4DNJAY6mDL4Xjh3pnvh6cS7ToJsPQQChoxXY"
  }
}
```
