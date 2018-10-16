
#### initiator init (2018-10-16 20:05:59.808)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW&role=initiator
```

#### responder init (2018-10-16 20:05:59.813)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW&role=responder
```

#### responder <--- (2018-10-16 20:06:00.814)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 20:06:00.816)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 20:06:00.825)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpAKyYf94hoccj3VfMcLCNKgGhdgxiiPcV8DEwHrhHxH4cTaJe4u8Enx3nQbRKu1nQBP2Suk9ejZcQcsUT5XGWuA1qSSdqjYyyNURtiFgqthSZdPEQiKa5f4FaZaVszregXvP3kxQmMW9rzj59PkMnTZJ1KBFQs1T"
  }
}
```

#### initiator ---> (2018-10-16 20:06:00.860)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HkMi8fUdxBKh7mpLAiLBXCznnyPx1tzAP5o5ag66DiFEz5boCsU1GYAdZVqjre8pQkq5ABqvqHJ4afbrFk8Y2fsaim9wMH5KcPJ8aApQFQAEETTs5bnfKfDcuCZt6ZPWDZmfi7S8CdaJC3Ua8xzkDYGS4NqAnFKjfZNYTj1XvgPmkrdtZhBPtDVyPtRnGXj9mdouEbEEFx7rEUtQjSXMz2vbg5EBcgCUbK4JWBGnf93bHaeq4nAbttR5pDmtzmnXN"
  }
}
```

#### responder <--- (2018-10-16 20:06:00.862)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 20:06:00.862)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpAKyYf94hoccj3VfMcLCNKgGhdgxiiPcV8DEwHrhHxH4cTaJe4u8Enx3nQbRKu1nQBP2Suk9ejZcQcsUT5XGWuA1qSSdqjYyyNURtiFgqthSZdPEQiKa5f4FaZaVszregXvP3kxQmMW9rzj59PkMnTZJ1KBFQs1T"
  }
}
```

#### responder ---> (2018-10-16 20:06:00.863)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4Hmxnp4LRo5Am6vuwJdpPTGWewh7iZa8jiH2ZbZg2iNnXJpqw57G3ctTMi3zYJcV5u3n2iYsJoL7RBv1m1ATYfEN5oHUEcxgSJRTFs4qHKrPuxxcHBoHW4ezdGAC4PjbyfYZgRKrc2tt5NEZku6iFfUHMucDvaN27MnvNPVU61CiBUP67fRNkDVP6VCtiVEispnRZs5f2bFQ4A3ojcKGGMPREYBqJEKG2HSAK4WCdR6Bc1nTSB1izDqyogqeG536VV"
  }
}
```

#### initiator <--- (2018-10-16 20:06:00.864)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 20:06:00.865)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmNpbsXmyJhEoPPnTEEwEfeNqZuPQJht2ym7D65uHXRUu21mg9vnNaQHzoyH1eFLkqQcK4MJdnJZaqvRnisj27jqmTjJeBP5EjchBptbr65dxVwBbmNaJcRC4wqnsDLD4c413bLC5go6rMMoS6YPTyioSyNPhMhZcB3sR28hxYDvkz1mjv2bkzpFZiE1oyUzpCLjS4cyLeacpVMeedVy163rVbfxJ4mKcrA1STYRMXTkUPo3W8546rTYeNxRo8QsH7kFoDh1yagjRa1mpdjkF3P62sARiL4iSqLQmDfKuutRqV8hTTcCwatqDm9zV3LcggrWX714Ru5Xb8MYRqs8jUTJ6k9b"
  }
}
```

#### initiator <--- (2018-10-16 20:06:00.866)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmNpbsXmyJhEoPPnTEEwEfeNqZuPQJht2ym7D65uHXRUu21mg9vnNaQHzoyH1eFLkqQcK4MJdnJZaqvRnisj27jqmTjJeBP5EjchBptbr65dxVwBbmNaJcRC4wqnsDLD4c413bLC5go6rMMoS6YPTyioSyNPhMhZcB3sR28hxYDvkz1mjv2bkzpFZiE1oyUzpCLjS4cyLeacpVMeedVy163rVbfxJ4mKcrA1STYRMXTkUPo3W8546rTYeNxRo8QsH7kFoDh1yagjRa1mpdjkF3P62sARiL4iSqLQmDfKuutRqV8hTTcCwatqDm9zV3LcggrWX714Ru5Xb8MYRqs8jUTJ6k9b"
  }
}
```

#### initiator <--- (2018-10-16 20:06:01.786)
```javascript
{
  "id": -576460752303423463,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "balance": 699
    },
    {
      "account": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "balance": 401
    }
  ]
}
```

#### initiator <--- (2018-10-16 20:06:02.172)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### responder <--- (2018-10-16 20:06:02.172)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### responder <--- (2018-10-16 20:06:02.173)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.173)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.177)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### responder <--- (2018-10-16 20:06:02.177)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### responder <--- (2018-10-16 20:06:02.178)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmNpbsXmyJhEoPPnTEEwEfeNqZuPQJht2ym7D65uHXRUu21mg9vnNaQHzoyH1eFLkqQcK4MJdnJZaqvRnisj27jqmTjJeBP5EjchBptbr65dxVwBbmNaJcRC4wqnsDLD4c413bLC5go6rMMoS6YPTyioSyNPhMhZcB3sR28hxYDvkz1mjv2bkzpFZiE1oyUzpCLjS4cyLeacpVMeedVy163rVbfxJ4mKcrA1STYRMXTkUPo3W8546rTYeNxRo8QsH7kFoDh1yagjRa1mpdjkF3P62sARiL4iSqLQmDfKuutRqV8hTTcCwatqDm9zV3LcggrWX714Ru5Xb8MYRqs8jUTJ6k9b",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.178)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmNpbsXmyJhEoPPnTEEwEfeNqZuPQJht2ym7D65uHXRUu21mg9vnNaQHzoyH1eFLkqQcK4MJdnJZaqvRnisj27jqmTjJeBP5EjchBptbr65dxVwBbmNaJcRC4wqnsDLD4c413bLC5go6rMMoS6YPTyioSyNPhMhZcB3sR28hxYDvkz1mjv2bkzpFZiE1oyUzpCLjS4cyLeacpVMeedVy163rVbfxJ4mKcrA1STYRMXTkUPo3W8546rTYeNxRo8QsH7kFoDh1yagjRa1mpdjkF3P62sARiL4iSqLQmDfKuutRqV8hTTcCwatqDm9zV3LcggrWX714Ru5Xb8MYRqs8jUTJ6k9b",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

##### initiator: (2018-10-16 20:06:02.520)
> Funding has been confirmed locally on-chain

##### responder: (2018-10-16 20:06:02.520)
> Funding has been confirmed locally on-chain

##### initiator: (2018-10-16 20:06:02.520)
> Funding has been confirmed on-chain by other party

##### responder: (2018-10-16 20:06:02.521)
> Funding has been confirmed on-chain by other party

##### initiator: (2018-10-16 20:06:02.521)
> Channel is `open` and ready to use

##### responder: (2018-10-16 20:06:02.521)
> Channel is `open` and ready to use

#### initiator <--- (2018-10-16 20:06:02.564)
```javascript
{
  "id": -576460752303423462,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "balance": 699
    },
    {
      "account": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "balance": 401
    }
  ]
}
```

#### initiator ---> (2018-10-16 20:06:02.564)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
    "to": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.572)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQRcvU8keeHpFYq1LY1Lop8Gpqi7nPYhAHTcCMAWEwRwzrUDZtYyoEwXN4Z5YqZtRAkkAwJjsfW9uWVfECT7KQtFhBotGqRA1NdJoRiFkLbTCAZyEkuYe3VPNTFHszcbY7mWd9XVcvNSSy24eGrSPtSFDWksTKRsefWdaW6Y3GMmj7Gax27awWbHQrkhsdxwZS5q53PE2YqyS9"
  }
}
```

#### initiator ---> (2018-10-16 20:06:02.574)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak51BN4wT72vhytLQEd3K4nhr8ZZgsP2LsnX7yH5oDWp3FNwsvwv1q9nPJJiUxwdYWBKwJ7TPZD447K1fvZ46anC2wAB65Y2Y9hgL3Kj7wuMBjYtTMEp9Sd9FSALmTrSj9gi5E53AKL14imSbr2c29h5KCwVesU5QzxdNNBqacGUax4L1KLE8VQ349oxooXGr8Zv5ewnYzPufziZMEBdtq6cx31NB5t1WitwAuRLX7FCRQBytrxZa9cLV1EwKFv53Gq6nxe6ZFEskDRgdFovbjXxu3MozSQ1x9b67W2TywNHozeYF"
  }
}
```

#### responder <--- (2018-10-16 20:06:02.579)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### responder <--- (2018-10-16 20:06:02.580)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQRcvU8keeHpFYq1LY1Lop8Gpqi7nPYhAHTcCMAWEwRwzrUDZtYyoEwXN4Z5YqZtRAkkAwJjsfW9uWVfECT7KQtFhBotGqRA1NdJoRiFkLbTCAZyEkuYe3VPNTFHszcbY7mWd9XVcvNSSy24eGrSPtSFDWksTKRsefWdaW6Y3GMmj7Gax27awWbHQrkhsdxwZS5q53PE2YqyS9"
  }
}
```

#### responder ---> (2018-10-16 20:06:02.581)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak53mYqwfTwXVi6PLHGV7WEqV4Xu6rC9sW1DpiwgTrQQUSijbaSpiuAHhGoKJUz7RsicZWe2YTpiTvUGUZ5zqPiJj6XMSgPqYTW25Voy1eAhLQVwaMFbi9iWMrCgptiFmC73mx2rixaiQJZopkWPUy6g5VzmFnQHAGrBgbx5SA4injWrvwjep1tVw1712RDPUtAUHLsWqx3zLdYP6Ks5r4VmiiRGE8giDJGPcX83gNbf7erydswWNUxfSMKrimvdNzKC2n1MPwvVNB2y9hXEmpZN2zcNAikNm7H2uo6e8XJsFL82y"
  }
}
```

#### responder <--- (2018-10-16 20:06:02.586)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkkajT49S7RRbaJAmiDcoe8kXXYroyExNGfMwddNGt8gStzTziHC77TQTsBthGbca4JaNfA3er2BM9CSs8245L4NK234FKhkVLT9UA9416x1o3DHmBce1ZwcCt315jd9herdi49NJRDNSr9poA3WDafX2Lfee8uDHe9i2k657H1PzbP1dnebbCT5tfMMn6C9yc933mBRMvbcfSEUgZnMwDR2cnq13BVDdpsuYpH7sZUmDfSvkvMQoWP31XjqHxzGpqV1d1TDSC5W4VQ2tJSUSfFCbMv2grzwBR3DARC92KzZAwd7WvbSKo9E76AGZBcARrZjAsBYa4NrGSqG4x2GGpKJ4Qa5Be91HJxcopgYj5FTaeSiMBMeHNZqXrVMLfTLgXf2Lezkk6",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.586)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkkajT49S7RRbaJAmiDcoe8kXXYroyExNGfMwddNGt8gStzTziHC77TQTsBthGbca4JaNfA3er2BM9CSs8245L4NK234FKhkVLT9UA9416x1o3DHmBce1ZwcCt315jd9herdi49NJRDNSr9poA3WDafX2Lfee8uDHe9i2k657H1PzbP1dnebbCT5tfMMn6C9yc933mBRMvbcfSEUgZnMwDR2cnq13BVDdpsuYpH7sZUmDfSvkvMQoWP31XjqHxzGpqV1d1TDSC5W4VQ2tJSUSfFCbMv2grzwBR3DARC92KzZAwd7WvbSKo9E76AGZBcARrZjAsBYa4NrGSqG4x2GGpKJ4Qa5Be91HJxcopgYj5FTaeSiMBMeHNZqXrVMLfTLgXf2Lezkk6",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.591)
```javascript
{
  "id": -576460752303423461,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "balance": 698
    },
    {
      "account": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "balance": 402
    }
  ]
}
```

#### initiator <--- (2018-10-16 20:06:02.592)
```javascript
{
  "id": -576460752303423460,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "balance": 402
    },
    {
      "account": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "balance": 698
    }
  ]
}
```

#### responder ---> (2018-10-16 20:06:02.592)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
    "to": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz"
  }
}
```

#### responder <--- (2018-10-16 20:06:02.596)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQRcvU8keeHpFYq1LY1Lop8Gpqi7nPYhAHTcCMAWEwRwzrUJzQQXLi8s5zK55xU1jsiVYB7iFWDKG1gvYgm9ojeFPJDV5VVa31sGVQqHq7LQk3AUdaF1dEUUsstnVoWqKbUZy1UsvVETdtbFi9hKadpAdpyJrSGby2ikens5aFJYptcJvXKReVBXppXqcUdBk5Qqkshbtuqau9"
  }
}
```

#### responder ---> (2018-10-16 20:06:02.597)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4yJXXkeuvXLLJbHgLBtXSdvidGSRJR7hcDkNuQLQSx5yrdJ1hFYuGFf6tNpkXkxJdVQpQ2Pw6VU1nKFiS59ZdyDLLCpgiAAktStWQQHmsauANKKr7S4946waReLorizqPPbL1NtJx4BRkwG1CWB3VG5rwugzZYRNs2mudaviU2CWmAHcqvxCSNNGVJ3hAahfb6yCA8BLbTdcjYGD8jQxXXUe5fvhvFvhztwxX7BqQqFXCb8Q4mysY2SxKWddnJazVDTma7PvFSvUZBtAVjVr3crDQqZ1agyzNuo3wDjBTUGN42o"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.601)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.601)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQRcvU8keeHpFYq1LY1Lop8Gpqi7nPYhAHTcCMAWEwRwzrUJzQQXLi8s5zK55xU1jsiVYB7iFWDKG1gvYgm9ojeFPJDV5VVa31sGVQqHq7LQk3AUdaF1dEUUsstnVoWqKbUZy1UsvVETdtbFi9hKadpAdpyJrSGby2ikens5aFJYptcJvXKReVBXppXqcUdBk5Qqkshbtuqau9"
  }
}
```

#### initiator ---> (2018-10-16 20:06:02.602)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak53Qtn2rvgHMwXVhWUHektMJuvAX5kk9nDwCVoWz9Y5GFD2xReZ8GgetBGsYjmuAfPfnmdxPNMioFjsJa77G3rUcT6sm7KwxCJCxr4mmc43UDCu8yeA7w6VsCv6DvXd12Jb3JXK1vmopMACfQ7h58b1JTjSD4CTFmqEYxBX7eemZxCQ3Jfq4Dcc4GQ2XteAg6bVNvFvBCsx3yPBCPXErkDPmV6oUiREeoeYC6G3fFqEBzy61Z2TVtfCnNeH5NPjmFdzRf2CsFBjBkHxLsq9CbZZ1fN1vBmZ5H8K2n3Eqmvafij4z"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.607)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkhMd8xK9L88v9Xe6qXBe4RJwkteD7SZSddZo1VdtUQkSUkpqTL3xn7yHa2bkTwGABD8soDqN7PcinAVcXFEjoZ4nfUW6zEh6LsGDS9snMVEu6sb9rbf6cQz9FYY3b9EgLkovAi3p6WLM8oMesWYiGcRtP5tUingfXyUztCggUsXGxFAoeTpnEBZu5J83DrP3yxw2SdKrgosRVjDzQZFDDhmonKAfHT3gHDSiJ596dzVYbEfk3a9W6gFTL6Sh8x8237GMJbP3LZYaH4iHUgzVqcpuSYqND4EdD697sokBorfoHaFjFN4tSnLy8xghWm6Mav527pxEG5CDMk9ffGtXuVVmAKaqz8Tas6GcDYtGbTrDVJoNaCd7ATEWp97nQybr8KHe6E5RF",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### responder <--- (2018-10-16 20:06:02.608)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkhMd8xK9L88v9Xe6qXBe4RJwkteD7SZSddZo1VdtUQkSUkpqTL3xn7yHa2bkTwGABD8soDqN7PcinAVcXFEjoZ4nfUW6zEh6LsGDS9snMVEu6sb9rbf6cQz9FYY3b9EgLkovAi3p6WLM8oMesWYiGcRtP5tUingfXyUztCggUsXGxFAoeTpnEBZu5J83DrP3yxw2SdKrgosRVjDzQZFDDhmonKAfHT3gHDSiJ596dzVYbEfk3a9W6gFTL6Sh8x8237GMJbP3LZYaH4iHUgzVqcpuSYqND4EdD697sokBorfoHaFjFN4tSnLy8xghWm6Mav527pxEG5CDMk9ffGtXuVVmAKaqz8Tas6GcDYtGbTrDVJoNaCd7ATEWp97nQybr8KHe6E5RF",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.612)
```javascript
{
  "id": -576460752303423459,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "balance": 401
    },
    {
      "account": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "balance": 699
    }
  ]
}
```

#### initiator <--- (2018-10-16 20:06:02.613)
```javascript
{
  "id": -576460752303423458,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "balance": 401
    },
    {
      "account": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "balance": 699
    }
  ]
}
```

#### responder ---> (2018-10-16 20:06:02.614)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
    "to": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz"
  }
}
```

#### responder <--- (2018-10-16 20:06:02.617)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQRcvU8keeHpFYq1LY1Lop8Gpqi7nPYhAHTcCMAWEwRwzrUQQvG4tBLCov54d5N8asVo4ug9paC1A96ySJgdZRNzzKhkVcARQGXDEZvjXu5Bq8r7bCk4wfMjVpBD5WE6CFQa6KhpnQp2MJGdCQ5gY4Jku5GyRFi36JrsS53DShodta7oG1jvsb1mnLoPWdgYjoC4YoqXCYEmoe"
  }
}
```

#### responder ---> (2018-10-16 20:06:02.618)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4udog5nkoPoLoVdNWfUJ6oS1AU2dUCX6oReFpJ1XUVdgfFFGcQSFbonMXmDzgMY8gPeuHjBpVUZTo1jkXtGaKeskYX3Lk9Xg8hjg2YDnyC3adokhW5yndhoZBVBczXC843r96AeQMNvfH4BK9YriTkc7fHfsoqzVRTiqL893LXuWxBJx7nbdDUWLmzj6h7RHpDBhjyWNHhrdx7jKfpgDTrpJwY2knZ8nn8YCaYiTFhwecrR14NZY14NVhh444RDX4fvq1b7faBXhXanZbeYi2v5cpc2RtRUxoL9mj1FCNBYr7Rx"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.621)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.622)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQRcvU8keeHpFYq1LY1Lop8Gpqi7nPYhAHTcCMAWEwRwzrUQQvG4tBLCov54d5N8asVo4ug9paC1A96ySJgdZRNzzKhkVcARQGXDEZvjXu5Bq8r7bCk4wfMjVpBD5WE6CFQa6KhpnQp2MJGdCQ5gY4Jku5GyRFi36JrsS53DShodta7oG1jvsb1mnLoPWdgYjoC4YoqXCYEmoe"
  }
}
```

#### initiator ---> (2018-10-16 20:06:02.623)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak57hGtp8c8Mf1xJ3UbFMLTMM9JwkGfVQY4xjfchUJXVrn15E3NCzzFFqt3RmysEPhFmUhxFaDQ1SHwcEbwKzHS2dEGXgF14qb6XqJ9v9Snmur8cnPUkzbwJrhSUoYxUVsRDxFih6CmF1RzGkAXsyvgxNntXnWQ2rEAfE218hEoKUppTQBboeV1YkiDdKUNGi2qF8CxQvSBgMN8te5C9AT7wHXYqENnQQjQQtjQ7VtApaDSc7PeVANKZSjrqLspLjhgiyAFmVWPyhrC1fmTmrDL2NzitXRL1o1GmfVuQEVUH9zScB"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.628)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkb3vHrnfPEa7V4aHs14uNatrmizPF3vmgUaVYDcTo4pATgvra79YD34BL13LhTbuF4FRivd4P7w8K9QVAmGutxBafQHZdAETMTHSYEK5bMb982AsLHiZ9L1JZnRjXK1J5emR6TxVaWAvBH12jN9iog4WVLEzUkfQA9Z1ugL9Bsjv6DakXMfjmWDKG7KLHaEJAVNtnxayUXif3uEzy5YznyQLDFapD8juZLGQvYv7aTGms3AwKRQ56HvYqu1vTA2v7Bv4qJA9cgG1bCZHcGTryoMbBQR9cuJKpUd8Y5ThJTT2JNP3v5JPCLZPceUiPjY5DxUKtVgAq6xcHQa8D3GVv2beKVzYR5wM8rvdQTbTpH2M3weEUDLd5ct4BnaFPcbksGeVBZi2k",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### responder <--- (2018-10-16 20:06:02.629)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkb3vHrnfPEa7V4aHs14uNatrmizPF3vmgUaVYDcTo4pATgvra79YD34BL13LhTbuF4FRivd4P7w8K9QVAmGutxBafQHZdAETMTHSYEK5bMb982AsLHiZ9L1JZnRjXK1J5emR6TxVaWAvBH12jN9iog4WVLEzUkfQA9Z1ugL9Bsjv6DakXMfjmWDKG7KLHaEJAVNtnxayUXif3uEzy5YznyQLDFapD8juZLGQvYv7aTGms3AwKRQ56HvYqu1vTA2v7Bv4qJA9cgG1bCZHcGTryoMbBQR9cuJKpUd8Y5ThJTT2JNP3v5JPCLZPceUiPjY5DxUKtVgAq6xcHQa8D3GVv2beKVzYR5wM8rvdQTbTpH2M3weEUDLd5ct4BnaFPcbksGeVBZi2k",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.633)
```javascript
{
  "id": -576460752303423457,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "balance": 400
    },
    {
      "account": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "balance": 700
    }
  ]
}
```

#### initiator <--- (2018-10-16 20:06:02.635)
```javascript
{
  "id": -576460752303423456,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "balance": 700
    },
    {
      "account": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "balance": 400
    }
  ]
}
```

#### initiator ---> (2018-10-16 20:06:02.635)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
    "to": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.638)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQRcvU8keeHpFYq1LY1Lop8Gpqi7nPYhAHTcCMAWEwRwzrUVqS7cReXYXqq4ACGExA6em8z4asSDbtjou4DYaU6WWGGgXBRi78b92tzarhonTTct7eQibL99EG6Zd6kNA5ZX16CLCh78bC4B721XG9v21Ffs4VJvknZatTkV89j8gh7dkAmrCDxwMmqWiZ8bdHmVRKMwnqLJT7"
  }
}
```

#### initiator ---> (2018-10-16 20:06:02.639)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4uRvGNKFEsRsfZ72TmRFbEBPhTew5nwu4yTmjNaXawoWZHwt99aNxhaT9eWAFUMXvoGZzPzmMnV8wH4kXRhSNDe9Af91LsMjs1SmnyvDEeUN2xWoV9y1mpfkueWf7pBTfQCaaYHqA3858i1BGHvyafGMfbZRiDCdAQUSk4j8m1Knp675zJtyVYV5dKnuqki8eMsiEpDeMi6VTP72DzHkjEX4TgYiuiFpVa7VqfUXq9vFduYVhtTaxDCWv2XKCMBjGVUuJ4x3Ri4UD4AxLRn6JPjvceDPQZ59StCY9tTxpTVKqe1"
  }
}
```

#### responder <--- (2018-10-16 20:06:02.671)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### responder <--- (2018-10-16 20:06:02.671)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQRcvU8keeHpFYq1LY1Lop8Gpqi7nPYhAHTcCMAWEwRwzrUVqS7cReXYXqq4ACGExA6em8z4asSDbtjou4DYaU6WWGGgXBRi78b92tzarhonTTct7eQibL99EG6Zd6kNA5ZX16CLCh78bC4B721XG9v21Ffs4VJvknZatTkV89j8gh7dkAmrCDxwMmqWiZ8bdHmVRKMwnqLJT7"
  }
}
```

#### responder ---> (2018-10-16 20:06:02.672)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4tzNrtrMgFfXRNYvugGBaN8nppNZ6iHsnYY1TiFXfaVoAoQBnsXmfSAKi8mFgWGuNT51F2tFyFSJEKRGi5TT4EgLZnJUyyWnGYJHdKzwwRZCtdFFR4szESZD86V5koaogsPogaDXH631UDRajG9x3rujvq3jGm1L16TNhSYbxFoQ6cSomyrC2ky8z2yj1yYfmETAkADqaXgDbk51SZXTgQgozmWuWHtq2F6RGGEPVuegt87phc7tnR6eqHsKpyskkmJnSUzNFKWjpC4R3R8ULx4HM6ZnBd4iH3KdAj1CQrjMMYe"
  }
}
```

#### responder <--- (2018-10-16 20:06:02.677)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkZwaJGGN15MmHCU2mG8YCf5pds2LRwfULnpwNdhZPjkD1qLjKwi1mqivvASw2jcTJCyNx1GNr5XsRiY4X985pb2gkXimjz69ckVQXmc2P7jNjMvem74aSSgJrvLiSPSryh8dj5Vbj3UiJaj1hDaufEtMKku7NUdefbL7kUjZUHwJgyJxeE1e33po4TWLQmJv96sWPyGbaHwRLshSPnJ6pAC7PWQ7mScBCqGZR53vjwD4Ww5CwHqKXLhUMBAJRqyAdURFxuypNAnEp2iGRHKnbK7jcHX6mmhfCCRxBKTcURMxQ6yA2QRTC4wRpdf9awJVBthXjgANZKdAw9L7egLFxwGKvxkjP2NwQwXLXefkUhLanvYbFZ7YXKBrAYRdsJRmxPpj9sykh",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.677)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkZwaJGGN15MmHCU2mG8YCf5pds2LRwfULnpwNdhZPjkD1qLjKwi1mqivvASw2jcTJCyNx1GNr5XsRiY4X985pb2gkXimjz69ckVQXmc2P7jNjMvem74aSSgJrvLiSPSryh8dj5Vbj3UiJaj1hDaufEtMKku7NUdefbL7kUjZUHwJgyJxeE1e33po4TWLQmJv96sWPyGbaHwRLshSPnJ6pAC7PWQ7mScBCqGZR53vjwD4Ww5CwHqKXLhUMBAJRqyAdURFxuypNAnEp2iGRHKnbK7jcHX6mmhfCCRxBKTcURMxQ6yA2QRTC4wRpdf9awJVBthXjgANZKdAw9L7egLFxwGKvxkjP2NwQwXLXefkUhLanvYbFZ7YXKBrAYRdsJRmxPpj9sykh",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.681)
```javascript
{
  "id": -576460752303423455,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "balance": 699
    },
    {
      "account": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "balance": 401
    }
  ]
}
```

#### initiator <--- (2018-10-16 20:06:02.683)
```javascript
{
  "id": -576460752303423454,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "balance": 401
    },
    {
      "account": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "balance": 699
    }
  ]
}
```

#### responder ---> (2018-10-16 20:06:02.683)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
    "to": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz"
  }
}
```

#### responder <--- (2018-10-16 20:06:02.686)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQRcvU8keeHpFYq1LY1Lop8Gpqi7nPYhAHTcCMAWEwRwzrUbFwy9y7itFmb3hKANGs4Q8No2xi9NxPw5DYXb4nrWCNgHKqW88mq6it7cwUYk1LDPWTkBaX8Ejgk4EuebwZGaLx9iWFy9n7dNAtrQSuHwRZtJVUNTr59wYENgMivMQJx7aXPPJ7reDkboSccyQP17YkDC9qM5xt"
  }
}
```

#### responder ---> (2018-10-16 20:06:02.687)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak59ENyvPA1yXrdjtZc3KDUgGqEMiEmJWrnLbBPykjg3cuqkBWnnck1JvAwfY3BycZ7rn8Sgoo4Evm5QFKYxEuu5APS97Dcw1PgX2TuL42eTtSqmYPFYWxu9DZTnPwHsWxdsAftVfFfHpmrv7H2ngK8HVeAaHdYAeqN8wPyTtskLyjEwtrKX6eMugfbZRRzyJLb9ochpmnT6h18iBBBJ8YLv8hKEu4i5Xrty5YmA7Uc2viUP8duUo8vR6rbmaHEfFpdXtkBdceiRd91gorH6obRC69L4eH4kDDVFeBwMPMDKxC5KZ"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.726)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.728)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQRcvU8keeHpFYq1LY1Lop8Gpqi7nPYhAHTcCMAWEwRwzrUbFwy9y7itFmb3hKANGs4Q8No2xi9NxPw5DYXb4nrWCNgHKqW88mq6it7cwUYk1LDPWTkBaX8Ejgk4EuebwZGaLx9iWFy9n7dNAtrQSuHwRZtJVUNTr59wYENgMivMQJx7aXPPJ7reDkboSccyQP17YkDC9qM5xt"
  }
}
```

#### initiator ---> (2018-10-16 20:06:02.731)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak51pw38HmKY3dAcPM5QvsmUpDdyLKohvngUpjVYQWutwJhTq8qpFnjHhzNUsrTxjDWdovFJEcsxWM5ieaH123r4yC94D8KDxoiNoeWXffdBG7ARrfpZzUio1GGotqdovYJ4tysMWcpTFAWoybqdzJW3MyQ7WGUvjjLUR7UqezaMFYt9SR967pMD8H7UMQZi1bVazWJH4Gt1Knxo3MWXRdZUy2Pbg59MPUNZERf24Yz7NmenR8yckmh9E6yRdu5GNPhjA53gM4By7CyQgKn6ESg6nDMcDVDuT98ne9mnF6kU5b1hD"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.746)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkmhKTp9ft6dsPXbmvW5he1bVeQRUU87Fv5wv5f4KLyHKoa2tXkRjz4wASVZhFjRVa4RR4uAbKckXeRJkcRRMcw5nXKGftz2grg9fmaN74foLgbWXj7uXycrgvPFJnQx2LBKA9ibFg5CKpTexmyxi4BJ9Qd2umchWh1C9r4n78uPynyYf3yo67myao8Zsh1P4Yw8MZWSxhY61J7dVTkGm7pcCRo7MogujhHouLg2Y4vbw92LNFJ8ToQ2Gp5maMpzCg1yB5YbrJAyuCnAK1sPymdUXLmi62DiM4GrbjqVb5bZecNAQ6YzE6oPUaSA1uSmg3Frztgs4Ho9qgwvCDMQngVKVPhhLDLS9S7xkocZwX5pagjxrkgdcgVbJW5bShH9RvZKGpz25n",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### responder <--- (2018-10-16 20:06:02.747)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkmhKTp9ft6dsPXbmvW5he1bVeQRUU87Fv5wv5f4KLyHKoa2tXkRjz4wASVZhFjRVa4RR4uAbKckXeRJkcRRMcw5nXKGftz2grg9fmaN74foLgbWXj7uXycrgvPFJnQx2LBKA9ibFg5CKpTexmyxi4BJ9Qd2umchWh1C9r4n78uPynyYf3yo67myao8Zsh1P4Yw8MZWSxhY61J7dVTkGm7pcCRo7MogujhHouLg2Y4vbw92LNFJ8ToQ2Gp5maMpzCg1yB5YbrJAyuCnAK1sPymdUXLmi62DiM4GrbjqVb5bZecNAQ6YzE6oPUaSA1uSmg3Frztgs4Ho9qgwvCDMQngVKVPhhLDLS9S7xkocZwX5pagjxrkgdcgVbJW5bShH9RvZKGpz25n",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.755)
```javascript
{
  "id": -576460752303423453,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "balance": 400
    },
    {
      "account": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "balance": 700
    }
  ]
}
```

#### responder ---> (2018-10-16 20:06:02.858)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### responder <--- (2018-10-16 20:06:02.864)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "tx": "tx_2M9ipLgcZLmk5oDGVTXTBYbyUhc6DUqpGttV2BiLCfbXp5saSYwy9YkrKVNfsUzNvr3b7Kzfy4mvto39omftHmGfPKCUGF2fe5v1WYcDLti1NKMdcNNN7"
  }
}
```

#### responder ---> (2018-10-16 20:06:02.865)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "tx": "tx_2iJcVi27J8ZyhkXgwEyAWcVT8oKPiTGZZWJL9UTpWxwxb7b17GPpzsaKZ4Q4FgJRCNHdJjLWc6W87uzrPAKUPMHb8dZdhp7eKYE6CWg3FubbnNgY6e1z5U4n68oErAsYhxrEqenccL9BrU97Gb84rqUSbRqh1CNDm4wHU9dBnsoGLwxpLdiN2sKv9zSBnnJcDwBQ4hdzsi5snm69LVZMRDwynR"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.866)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "tx": "tx_2M9ipLgcZLmk5oDGVTXTBYbyUhc6DUqpGttV2BiLCfbXp5saSYwy9YkrKVNfsUzNvr3b7Kzfy4mvto39omftHmGfPKCUGF2fe5v1WYcDLti1NKMdcNNN7"
  }
}
```

#### initiator ---> (2018-10-16 20:06:02.867)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "tx": "tx_2iJcVi27J8a1CBU3D7cVDmra4WwoB4DbN7nwQD4JZp9zcujR3FSYCtdXjawzP75RJbrSAvnnmTpnZyVaRHE7JZbW67A8bK4afEKWvgHnQqGFEC8S8pw3X8cmSb9oscrkGXJVWr2ZSombbqApPds9d9TmvJb56dVNiZYt5nCCTEHfjmCxAz5nUU41QPigjTs6EyzoJiic7NKGumNajVWS6gVpiG"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.870)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3wu1WL1txa1Xkut3o7FV7VVnbcRDNjHnborpoDMFmLupkT8NWTdEooTQunEDnFvxz4hnsgAJm7ov9VPRFVJACN11rYwsAxNzYrSp8herXUXDoWDYAEEgXB9QgWrjERC8GTWAE6ZNLSDxZeYVCHr8AhX197HMYnGGXevqByDwJfiyDxZstBzNPzwubMT6kRC5Ang1YbpT7iXXnYMCVoiQ1qzhcLkkFCFfacSskQEBmjW2JQbfojzDDEdAEUpziqpgLG78Jdovs5MFbo3U4qMRZit4UmWSc7idHTVDgi2YSzyhf4SYemMz",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.870)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "close_mutual",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### initiator <--- (2018-10-16 20:06:02.870)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### responder <--- (2018-10-16 20:06:02.876)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3wu1WL1txa1Xkut3o7FV7VVnbcRDNjHnborpoDMFmLupkT8NWTdEooTQunEDnFvxz4hnsgAJm7ov9VPRFVJACN11rYwsAxNzYrSp8herXUXDoWDYAEEgXB9QgWrjERC8GTWAE6ZNLSDxZeYVCHr8AhX197HMYnGGXevqByDwJfiyDxZstBzNPzwubMT6kRC5Ang1YbpT7iXXnYMCVoiQ1qzhcLkkFCFfacSskQEBmjW2JQbfojzDDEdAEUpziqpgLG78Jdovs5MFbo3U4qMRZit4UmWSc7idHTVDgi2YSzyhf4SYemMz",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### responder <--- (2018-10-16 20:06:02.877)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "close_mutual",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```

#### responder <--- (2018-10-16 20:06:02.877)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_2CQUA4sAJXfV12kjCroRZ95Rji2tZoh33UY41TvCKNiUkoUZFk"
  }
}
```
