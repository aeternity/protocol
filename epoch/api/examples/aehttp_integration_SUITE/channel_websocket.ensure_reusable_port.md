
#### initiator init (2018-10-16 20:05:46.424)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW&role=initiator
```

#### responder init (2018-10-16 20:05:46.428)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW&role=responder
```

#### responder <--- (2018-10-16 20:05:47.430)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 20:05:47.442)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 20:05:47.443)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpAKyYf94hoccj3VfMcLCNKgGhdgxiiPcV8DEwHrhHxH4cTaJe4u8Enx3nQbRKu1nQBP2Suk9ejZcQcsUT5XGWuA1qSSdqjYyyNURtiFgqthSZdPEQiKa5f4FaZaVszregXvP3kxQmMW9rzj59PkMnTZJ1JiCsJhz"
  }
}
```

#### initiator ---> (2018-10-16 20:05:47.469)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HmQtDcgCT9cPexhCcGcVvr5GNGSdv7SQUqFJqwS5r2a9WjCHET99RarZ5HqxPNgXPukKm4B5DAUMkDi2mV4xEp1nN9gDeGFDmZxahpf11G3LK5DzZcgBYRSgL583Dmp6Kbk6gWRwtHAKNTRHGx8F7JgD9EKgYJrXrnNddaSjkNHqFeEMq2stuP8HfidzF8UjeyBxdXArbPz2fpCaXKG8jyuzsBMKZcLmc9Jf7FA3nZ4jRXy7PuPQcmN4oSkrDCgTK"
  }
}
```

#### responder <--- (2018-10-16 20:05:47.470)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 20:05:47.470)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpAKyYf94hoccj3VfMcLCNKgGhdgxiiPcV8DEwHrhHxH4cTaJe4u8Enx3nQbRKu1nQBP2Suk9ejZcQcsUT5XGWuA1qSSdqjYyyNURtiFgqthSZdPEQiKa5f4FaZaVszregXvP3kxQmMW9rzj59PkMnTZJ1JiCsJhz"
  }
}
```

#### responder ---> (2018-10-16 20:05:47.471)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HjxgMsCctBCsZri6m2FwRRB5PSPCfZnmnEY2TsqyjA5VTeJvBL2wMV19erFM5Xp3pk1udPiBM8Mp7Etqwx11JtfzDo75iNecY2mVN16HfRanHhNxSnkZC5PFCFSXu3QeeK9aTLSNsUzjUdGfEU8QCckHVUUN3jHirALKSo7D8rNA1gmKV38yTMxMA3VKHsRCaXBK11AWKkRnyiZNnW4gTcH5BvdbMEuvRjK5SV3spZk9nKNwqMcyDrSRRjG7VdDrV"
  }
}
```

#### initiator <--- (2018-10-16 20:05:47.473)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 20:05:47.474)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmN91TM5UDPaHoc68WgH7wZbUkz6i7x3qPBmfo7B226JHMPDLiiRa4uBAkSqqWaRrLm8XfwerzApcJvFdFuc8SMVHWZmS8jKrYWS12GskwrzbN5K1f4MssGgBrYqdSUZu7DZMjmMwcFpwpt6wYDe1kYzfvV28dS2wAWGYstSipBM1QSgDWtArjh6hmKyomnU5Vq7ax9Y2BL9fvGwQCMRXXp5MkzpZD9qicAtJBuPHZ6rF1NCxK7yEzV4po7MUHAub35X4Mcs4NJKPXTHQvSjobnLsRPd4J7TombFmuM4nnhcgCRQDYBxRMbd9xWUtTM6ppyHRfAjoHRRkEuptTzzVhQMroEB"
  }
}
```

#### initiator <--- (2018-10-16 20:05:47.475)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmN91TM5UDPaHoc68WgH7wZbUkz6i7x3qPBmfo7B226JHMPDLiiRa4uBAkSqqWaRrLm8XfwerzApcJvFdFuc8SMVHWZmS8jKrYWS12GskwrzbN5K1f4MssGgBrYqdSUZu7DZMjmMwcFpwpt6wYDe1kYzfvV28dS2wAWGYstSipBM1QSgDWtArjh6hmKyomnU5Vq7ax9Y2BL9fvGwQCMRXXp5MkzpZD9qicAtJBuPHZ6rF1NCxK7yEzV4po7MUHAub35X4Mcs4NJKPXTHQvSjobnLsRPd4J7TombFmuM4nnhcgCRQDYBxRMbd9xWUtTM6ppyHRfAjoHRRkEuptTzzVhQMroEB"
  }
}
```

#### initiator <--- (2018-10-16 20:05:49.100)
```javascript
{
  "id": -576460752303423477,
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

#### responder <--- (2018-10-16 20:05:50.770)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_nRX78ywBaCGWRBDppLVSyAXf97iHu6gpX38yiZbBvK28EhV2c"
  }
}
```

#### initiator <--- (2018-10-16 20:05:50.770)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_nRX78ywBaCGWRBDppLVSyAXf97iHu6gpX38yiZbBvK28EhV2c"
  }
}
```

#### initiator <--- (2018-10-16 20:05:50.771)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_nRX78ywBaCGWRBDppLVSyAXf97iHu6gpX38yiZbBvK28EhV2c"
  }
}
```

#### responder <--- (2018-10-16 20:05:50.771)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_nRX78ywBaCGWRBDppLVSyAXf97iHu6gpX38yiZbBvK28EhV2c"
  }
}
```

#### responder <--- (2018-10-16 20:05:50.775)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_nRX78ywBaCGWRBDppLVSyAXf97iHu6gpX38yiZbBvK28EhV2c"
  }
}
```

#### initiator <--- (2018-10-16 20:05:50.776)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_nRX78ywBaCGWRBDppLVSyAXf97iHu6gpX38yiZbBvK28EhV2c"
  }
}
```

#### responder <--- (2018-10-16 20:05:50.776)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmN91TM5UDPaHoc68WgH7wZbUkz6i7x3qPBmfo7B226JHMPDLiiRa4uBAkSqqWaRrLm8XfwerzApcJvFdFuc8SMVHWZmS8jKrYWS12GskwrzbN5K1f4MssGgBrYqdSUZu7DZMjmMwcFpwpt6wYDe1kYzfvV28dS2wAWGYstSipBM1QSgDWtArjh6hmKyomnU5Vq7ax9Y2BL9fvGwQCMRXXp5MkzpZD9qicAtJBuPHZ6rF1NCxK7yEzV4po7MUHAub35X4Mcs4NJKPXTHQvSjobnLsRPd4J7TombFmuM4nnhcgCRQDYBxRMbd9xWUtTM6ppyHRfAjoHRRkEuptTzzVhQMroEB",
    "channel_id": "ch_nRX78ywBaCGWRBDppLVSyAXf97iHu6gpX38yiZbBvK28EhV2c"
  }
}
```

#### initiator <--- (2018-10-16 20:05:50.777)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmN91TM5UDPaHoc68WgH7wZbUkz6i7x3qPBmfo7B226JHMPDLiiRa4uBAkSqqWaRrLm8XfwerzApcJvFdFuc8SMVHWZmS8jKrYWS12GskwrzbN5K1f4MssGgBrYqdSUZu7DZMjmMwcFpwpt6wYDe1kYzfvV28dS2wAWGYstSipBM1QSgDWtArjh6hmKyomnU5Vq7ax9Y2BL9fvGwQCMRXXp5MkzpZD9qicAtJBuPHZ6rF1NCxK7yEzV4po7MUHAub35X4Mcs4NJKPXTHQvSjobnLsRPd4J7TombFmuM4nnhcgCRQDYBxRMbd9xWUtTM6ppyHRfAjoHRRkEuptTzzVhQMroEB",
    "channel_id": "ch_nRX78ywBaCGWRBDppLVSyAXf97iHu6gpX38yiZbBvK28EhV2c"
  }
}
```

##### initiator: (2018-10-16 20:05:50.857)
> Funding has been confirmed locally on-chain

##### responder: (2018-10-16 20:05:50.857)
> Funding has been confirmed locally on-chain

##### initiator: (2018-10-16 20:05:50.857)
> Funding has been confirmed on-chain by other party

##### responder: (2018-10-16 20:05:50.857)
> Funding has been confirmed on-chain by other party

##### initiator: (2018-10-16 20:05:50.857)
> Channel is `open` and ready to use

##### responder: (2018-10-16 20:05:50.857)
> Channel is `open` and ready to use

##### initiator: (2018-10-16 20:05:50.888)
> Failing update, insufficient balance

#### initiator ---> (2018-10-16 20:05:50.888)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 10000,
    "from": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
    "to": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW"
  }
}
```

#### initiator <--- (2018-10-16 20:05:50.892)
```javascript
{
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1001,
        "message": "Insufficient balance"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 10000,
        "from": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
        "to": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0"
}
```

##### initiator: (2018-10-16 20:05:50.892)
> Failing update, negative amount

#### initiator ---> (2018-10-16 20:05:50.892)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": -1,
    "from": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
    "to": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW"
  }
}
```

#### initiator <--- (2018-10-16 20:05:50.893)
```javascript
{
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1002,
        "message": "Negative amount"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": -1,
        "from": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
        "to": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0"
}
```

##### initiator: (2018-10-16 20:05:50.893)
> Failing update, invalid pubkeys

#### initiator ---> (2018-10-16 20:05:50.893)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_11111111111111111111111111111115rHyByZ",
    "to": "ak_11111111111111111111111111111115sBJATr"
  }
}
```

#### initiator <--- (2018-10-16 20:05:50.895)
```javascript
{
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1003,
        "message": "Invalid pubkeys"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_11111111111111111111111111111115rHyByZ",
        "to": "ak_11111111111111111111111111111115sBJATr"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0"
}
```

##### responder: (2018-10-16 20:05:50.895)
> Failing update, insufficient balance

#### responder ---> (2018-10-16 20:05:50.895)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 10000,
    "from": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
    "to": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz"
  }
}
```

#### responder <--- (2018-10-16 20:05:50.899)
```javascript
{
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1001,
        "message": "Insufficient balance"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 10000,
        "from": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
        "to": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0"
}
```

##### responder: (2018-10-16 20:05:50.900)
> Failing update, negative amount

#### responder ---> (2018-10-16 20:05:50.900)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": -1,
    "from": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
    "to": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz"
  }
}
```

#### responder <--- (2018-10-16 20:05:50.900)
```javascript
{
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1002,
        "message": "Negative amount"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": -1,
        "from": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
        "to": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0"
}
```

##### responder: (2018-10-16 20:05:50.901)
> Failing update, invalid pubkeys

#### responder ---> (2018-10-16 20:05:50.901)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_11111111111111111111111111111115sBJATr",
    "to": "ak_11111111111111111111111111111115rHyByZ"
  }
}
```

#### responder <--- (2018-10-16 20:05:50.902)
```javascript
{
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1003,
        "message": "Invalid pubkeys"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_11111111111111111111111111111115sBJATr",
        "to": "ak_11111111111111111111111111111115rHyByZ"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0"
}
```

#### initiator init (2018-10-16 20:05:50.982)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW&role=initiator
```

#### responder init (2018-10-16 20:05:50.986)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW&role=responder
```

#### responder <--- (2018-10-16 20:05:51.988)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 20:05:51.991)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 20:05:51.995)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpAKyYf94hoccj3VfMcLCNKgGhdgxiiPcV8DEwHrhHxH4cTaJe4u8Enx3nQbRKu1nQBP2Suk9ejZcQcsUT5XGWuA1qSSdqjYyyNURtiFgqthSZdPEQiKa5f4FaZaVszregXvP3kxQmMW9rzj59PkMnTZJ1JpimM36"
  }
}
```

#### initiator ---> (2018-10-16 20:05:52.13)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HngNysLY6FgoECvfusqd2BhxrhVQRUu3JcG7arLP1PiCGzSzLDy7CFZd5qSvok7egTaP36jcgPLFS3srxV8Kxm9YhrLTA4vKcKqmzj2yWSBgkPDj5XBUqgNk1cvreUeYjeM16ts3joBiUH9DQGyh5ypkXu2xMbErUeEDj5QpLRiQvmHj3urKeTwCV79FdD315oVJS7xNQQX3FUQQSvcXpBUnd7nXS9gmTBW7sUmqCpXAowHdGkXdZ5MQCZxXgPFYx"
  }
}
```

#### responder <--- (2018-10-16 20:05:52.14)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 20:05:52.14)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpAKyYf94hoccj3VfMcLCNKgGhdgxiiPcV8DEwHrhHxH4cTaJe4u8Enx3nQbRKu1nQBP2Suk9ejZcQcsUT5XGWuA1qSSdqjYyyNURtiFgqthSZdPEQiKa5f4FaZaVszregXvP3kxQmMW9rzj59PkMnTZJ1JpimM36"
  }
}
```

#### responder ---> (2018-10-16 20:05:52.15)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HnWYBDH9Bst7oyXv4zWFhKEwuNvp5ueBYmbxo8b43SCamYCDDxyyxdfGt6Gyz9Py1VDXsvFBYqPvdboTFmoMkZvZizeVozVMNzCZh8hm8HiwmKyyGrGJ5YGVYpTWpDWZHHYxvrsH99FgKcYXjinQyKDBVrwB8K5uqK1tg9c5nw94KXWgw8J88niFW4LLvt8tsrxHp7MeyjSXxswgaJAzkHcPZUkKRZvXzS2jgBNRazKLdqr5RCHein1wbpNoBieMn"
  }
}
```

#### initiator <--- (2018-10-16 20:05:52.16)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 20:05:52.17)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmSXCitdfKW3fkae4HggX7WFLMWPKsi673TeEpjq33waPqtGRdMDzPUfCLpj9ed2bab7dEgXPg2A9VycNAoTzNuKcxTQ1nWn5ca5brPyiGiRoXnAWG4G3nU3iWAKMWye6cqiLUbYGLScvWoCUKyrQdWL8jRYyC7UsXYubQuHtjHAUGC5FXKW1wD7ofyUjyBBay2Frf5opwouQircx74VQkFDxinqgpYQQirD9iqCZJrmuAk7EDkzTGDELfh8CKT6Z1vsJUBQobZhRxWC9SfbkSxT9Ktu165W8eGFkHQKy6cFBK1AC9g6vxyfp1i9ejzn7DKUy1qFnTKZkWV9jmJqvVMFwHSp"
  }
}
```

#### initiator <--- (2018-10-16 20:05:52.18)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmSXCitdfKW3fkae4HggX7WFLMWPKsi673TeEpjq33waPqtGRdMDzPUfCLpj9ed2bab7dEgXPg2A9VycNAoTzNuKcxTQ1nWn5ca5brPyiGiRoXnAWG4G3nU3iWAKMWye6cqiLUbYGLScvWoCUKyrQdWL8jRYyC7UsXYubQuHtjHAUGC5FXKW1wD7ofyUjyBBay2Frf5opwouQircx74VQkFDxinqgpYQQirD9iqCZJrmuAk7EDkzTGDELfh8CKT6Z1vsJUBQobZhRxWC9SfbkSxT9Ktu165W8eGFkHQKy6cFBK1AC9g6vxyfp1i9ejzn7DKUy1qFnTKZkWV9jmJqvVMFwHSp"
  }
}
```

#### initiator <--- (2018-10-16 20:05:52.263)
```javascript
{
  "id": -576460752303423476,
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

#### initiator <--- (2018-10-16 20:05:52.842)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_pyCgsKBQzsZHaMQe8P3nVvCwukynukbRREGBYW5DsbCLeJWLb"
  }
}
```

#### responder <--- (2018-10-16 20:05:52.843)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_pyCgsKBQzsZHaMQe8P3nVvCwukynukbRREGBYW5DsbCLeJWLb"
  }
}
```

#### initiator <--- (2018-10-16 20:05:52.843)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_pyCgsKBQzsZHaMQe8P3nVvCwukynukbRREGBYW5DsbCLeJWLb"
  }
}
```

#### responder <--- (2018-10-16 20:05:52.843)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_pyCgsKBQzsZHaMQe8P3nVvCwukynukbRREGBYW5DsbCLeJWLb"
  }
}
```

#### responder <--- (2018-10-16 20:05:52.845)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_pyCgsKBQzsZHaMQe8P3nVvCwukynukbRREGBYW5DsbCLeJWLb"
  }
}
```

#### initiator <--- (2018-10-16 20:05:52.846)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_pyCgsKBQzsZHaMQe8P3nVvCwukynukbRREGBYW5DsbCLeJWLb"
  }
}
```

#### responder <--- (2018-10-16 20:05:52.847)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmSXCitdfKW3fkae4HggX7WFLMWPKsi673TeEpjq33waPqtGRdMDzPUfCLpj9ed2bab7dEgXPg2A9VycNAoTzNuKcxTQ1nWn5ca5brPyiGiRoXnAWG4G3nU3iWAKMWye6cqiLUbYGLScvWoCUKyrQdWL8jRYyC7UsXYubQuHtjHAUGC5FXKW1wD7ofyUjyBBay2Frf5opwouQircx74VQkFDxinqgpYQQirD9iqCZJrmuAk7EDkzTGDELfh8CKT6Z1vsJUBQobZhRxWC9SfbkSxT9Ktu165W8eGFkHQKy6cFBK1AC9g6vxyfp1i9ejzn7DKUy1qFnTKZkWV9jmJqvVMFwHSp",
    "channel_id": "ch_pyCgsKBQzsZHaMQe8P3nVvCwukynukbRREGBYW5DsbCLeJWLb"
  }
}
```

#### initiator <--- (2018-10-16 20:05:52.847)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmSXCitdfKW3fkae4HggX7WFLMWPKsi673TeEpjq33waPqtGRdMDzPUfCLpj9ed2bab7dEgXPg2A9VycNAoTzNuKcxTQ1nWn5ca5brPyiGiRoXnAWG4G3nU3iWAKMWye6cqiLUbYGLScvWoCUKyrQdWL8jRYyC7UsXYubQuHtjHAUGC5FXKW1wD7ofyUjyBBay2Frf5opwouQircx74VQkFDxinqgpYQQirD9iqCZJrmuAk7EDkzTGDELfh8CKT6Z1vsJUBQobZhRxWC9SfbkSxT9Ktu165W8eGFkHQKy6cFBK1AC9g6vxyfp1i9ejzn7DKUy1qFnTKZkWV9jmJqvVMFwHSp",
    "channel_id": "ch_pyCgsKBQzsZHaMQe8P3nVvCwukynukbRREGBYW5DsbCLeJWLb"
  }
}
```

##### initiator: (2018-10-16 20:05:52.918)
> Funding has been confirmed locally on-chain

##### responder: (2018-10-16 20:05:52.918)
> Funding has been confirmed locally on-chain

##### initiator: (2018-10-16 20:05:52.918)
> Funding has been confirmed on-chain by other party

##### responder: (2018-10-16 20:05:52.918)
> Funding has been confirmed on-chain by other party

##### initiator: (2018-10-16 20:05:52.918)
> Channel is `open` and ready to use

##### responder: (2018-10-16 20:05:52.918)
> Channel is `open` and ready to use

#### initiator ---> (2018-10-16 20:05:52.950)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "hejsan",
    "to": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW"
  }
}
```

#### responder <--- (2018-10-16 20:05:52.952)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "message": {
      "channel_id": "ch_pyCgsKBQzsZHaMQe8P3nVvCwukynukbRREGBYW5DsbCLeJWLb",
      "from": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "info": "hejsan",
      "to": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW"
    },
    "channel_id": "ch_pyCgsKBQzsZHaMQe8P3nVvCwukynukbRREGBYW5DsbCLeJWLb"
  }
}
```

#### responder ---> (2018-10-16 20:05:52.952)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "svejsan",
    "to": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz"
  }
}
```

#### initiator <--- (2018-10-16 20:05:52.954)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "message": {
      "channel_id": "ch_pyCgsKBQzsZHaMQe8P3nVvCwukynukbRREGBYW5DsbCLeJWLb",
      "from": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "info": "svejsan",
      "to": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz"
    },
    "channel_id": "ch_pyCgsKBQzsZHaMQe8P3nVvCwukynukbRREGBYW5DsbCLeJWLb"
  }
}
```

#### initiator ---> (2018-10-16 20:05:52.955)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "first message in a row",
    "to": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW"
  }
}
```

#### responder <--- (2018-10-16 20:05:52.958)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "message": {
      "channel_id": "ch_pyCgsKBQzsZHaMQe8P3nVvCwukynukbRREGBYW5DsbCLeJWLb",
      "from": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "info": "first message in a row",
      "to": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW"
    },
    "channel_id": "ch_pyCgsKBQzsZHaMQe8P3nVvCwukynukbRREGBYW5DsbCLeJWLb"
  }
}
```

#### initiator ---> (2018-10-16 20:05:52.958)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "second message in a row",
    "to": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW"
  }
}
```

#### responder <--- (2018-10-16 20:05:53.4)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "message": {
      "channel_id": "ch_pyCgsKBQzsZHaMQe8P3nVvCwukynukbRREGBYW5DsbCLeJWLb",
      "from": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
      "info": "second message in a row",
      "to": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW"
    },
    "channel_id": "ch_pyCgsKBQzsZHaMQe8P3nVvCwukynukbRREGBYW5DsbCLeJWLb"
  }
}
```

#### responder ---> (2018-10-16 20:05:53.6)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "some message",
    "to": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz"
  }
}
```

#### initiator <--- (2018-10-16 20:05:53.11)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "message": {
      "channel_id": "ch_pyCgsKBQzsZHaMQe8P3nVvCwukynukbRREGBYW5DsbCLeJWLb",
      "from": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "info": "some message",
      "to": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz"
    },
    "channel_id": "ch_pyCgsKBQzsZHaMQe8P3nVvCwukynukbRREGBYW5DsbCLeJWLb"
  }
}
```

#### responder ---> (2018-10-16 20:05:53.12)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "other message",
    "to": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz"
  }
}
```

#### initiator <--- (2018-10-16 20:05:53.53)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "message": {
      "channel_id": "ch_pyCgsKBQzsZHaMQe8P3nVvCwukynukbRREGBYW5DsbCLeJWLb",
      "from": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
      "info": "other message",
      "to": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz"
    },
    "channel_id": "ch_pyCgsKBQzsZHaMQe8P3nVvCwukynukbRREGBYW5DsbCLeJWLb"
  }
}
```

#### initiator init (2018-10-16 20:05:53.160)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW&role=initiator
```

#### responder init (2018-10-16 20:05:53.165)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW&role=responder
```

#### responder <--- (2018-10-16 20:05:54.166)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 20:05:54.169)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 20:05:54.174)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpAKyYf94hoccj3VfMcLCNKgGhdgxiiPcV8DEwHrhHxH4cTaJe4u8Enx3nQbRKu1nQBP2Suk9ejZcQcsUT5XGWuA1qSSdqjYyyNURtiFgqthSZdPEQiKa5f4FaZaVszregXvP3kxQmMW9rzj59PkMnTZJ1JrgZWkP"
  }
}
```

#### initiator ---> (2018-10-16 20:05:54.193)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HojdFfdCRiga4CrxoBhgtqi271dqHt769BgGSDVsS9ggNDTtwT2cRiJHG1CRTqevKx17eMyh3XxQVPbY4zeKT8J86uFjFy19mbCPNRMsGyT2sQwLMQPX2LRFrGgwSMZsmQSHtuuzSvxxckRCCHfPmex2NF48R2s4aGGP3tBoH2SCGHswK2mpg1DAqKRXcjG6i5MVWZkUxBzFYWkfvzuYvFaAEKeJUJAY9LdfRGPh9D9YqSkjokuzdaMGed9JYTDRN"
  }
}
```

#### responder <--- (2018-10-16 20:05:54.194)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 20:05:54.195)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpAKyYf94hoccj3VfMcLCNKgGhdgxiiPcV8DEwHrhHxH4cTaJe4u8Enx3nQbRKu1nQBP2Suk9ejZcQcsUT5XGWuA1qSSdqjYyyNURtiFgqthSZdPEQiKa5f4FaZaVszregXvP3kxQmMW9rzj59PkMnTZJ1JrgZWkP"
  }
}
```

#### responder ---> (2018-10-16 20:05:54.195)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4Hk59p11zTRoKJnWVzScpgguPLYL4Zz9n3MDGafG4ypo29A9uxfHj2TKEJpaGHjxSnxCRLSuMMvQVvZpPbMH6sPasRJGQMH3twdeVDLxnDgqUPmcWteet1JEhcL5veYTR6orW6mtxAyi72V5Yc9ZDD5fGBLgba5cCHvr9HMhApeUiZMXb7ZjYu8fjPCDhxTiqQT13E9mAPPEqhz4V8DDyVsNmQRYek5CyMorsAb1bLYbh9fTeqf6Fq44RdusN6wB3L"
  }
}
```

#### initiator <--- (2018-10-16 20:05:54.197)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 20:05:54.198)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmNL8vBJu17ZHye2Yqs4M1couC9uxPCCmkKH1raeLqFBFP26FL87tMBe4UyV1EFv9iNQttnt1RvDk6nZvSrxbNVaVEjvm4iu4xw9szKKpsqbaLL7rixfPb9JDL9Mkt2Ntw147mLSgYTGuMTaW9SfdT93RdNUSk7ae1UFhTwoTGqBcancfeKBnBnibQg28J5bFJZpxXZqsDruDnrGWJSu1H39pMxaL9WdQ2NReJFmnBpHFcUZV7KjvCA5tkZ16xVWxMq8BRge4tKnvabGjoecXtPkv1WqoBaCzEovx5wRocxXNmbGGhjdxygFwdcLm3rxmRaEhrDFGmK5rjiSeDiApMyqLmTJ"
  }
}
```

#### initiator <--- (2018-10-16 20:05:54.198)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmNL8vBJu17ZHye2Yqs4M1couC9uxPCCmkKH1raeLqFBFP26FL87tMBe4UyV1EFv9iNQttnt1RvDk6nZvSrxbNVaVEjvm4iu4xw9szKKpsqbaLL7rixfPb9JDL9Mkt2Ntw147mLSgYTGuMTaW9SfdT93RdNUSk7ae1UFhTwoTGqBcancfeKBnBnibQg28J5bFJZpxXZqsDruDnrGWJSu1H39pMxaL9WdQ2NReJFmnBpHFcUZV7KjvCA5tkZ16xVWxMq8BRge4tKnvabGjoecXtPkv1WqoBaCzEovx5wRocxXNmbGGhjdxygFwdcLm3rxmRaEhrDFGmK5rjiSeDiApMyqLmTJ"
  }
}
```

#### initiator <--- (2018-10-16 20:05:54.940)
```javascript
{
  "id": -576460752303423475,
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

#### initiator <--- (2018-10-16 20:05:55.696)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_29w6DawuzPcVbFAFt8QF11upvn6hcoiLM6g5dMd3KZsa3KMNoh"
  }
}
```

#### responder <--- (2018-10-16 20:05:55.696)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_29w6DawuzPcVbFAFt8QF11upvn6hcoiLM6g5dMd3KZsa3KMNoh"
  }
}
```

#### responder <--- (2018-10-16 20:05:55.697)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_29w6DawuzPcVbFAFt8QF11upvn6hcoiLM6g5dMd3KZsa3KMNoh"
  }
}
```

#### initiator <--- (2018-10-16 20:05:55.698)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_29w6DawuzPcVbFAFt8QF11upvn6hcoiLM6g5dMd3KZsa3KMNoh"
  }
}
```

#### responder <--- (2018-10-16 20:05:55.702)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_29w6DawuzPcVbFAFt8QF11upvn6hcoiLM6g5dMd3KZsa3KMNoh"
  }
}
```

#### initiator <--- (2018-10-16 20:05:55.703)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_29w6DawuzPcVbFAFt8QF11upvn6hcoiLM6g5dMd3KZsa3KMNoh"
  }
}
```

#### responder <--- (2018-10-16 20:05:55.703)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmNL8vBJu17ZHye2Yqs4M1couC9uxPCCmkKH1raeLqFBFP26FL87tMBe4UyV1EFv9iNQttnt1RvDk6nZvSrxbNVaVEjvm4iu4xw9szKKpsqbaLL7rixfPb9JDL9Mkt2Ntw147mLSgYTGuMTaW9SfdT93RdNUSk7ae1UFhTwoTGqBcancfeKBnBnibQg28J5bFJZpxXZqsDruDnrGWJSu1H39pMxaL9WdQ2NReJFmnBpHFcUZV7KjvCA5tkZ16xVWxMq8BRge4tKnvabGjoecXtPkv1WqoBaCzEovx5wRocxXNmbGGhjdxygFwdcLm3rxmRaEhrDFGmK5rjiSeDiApMyqLmTJ",
    "channel_id": "ch_29w6DawuzPcVbFAFt8QF11upvn6hcoiLM6g5dMd3KZsa3KMNoh"
  }
}
```

#### initiator <--- (2018-10-16 20:05:55.704)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmNL8vBJu17ZHye2Yqs4M1couC9uxPCCmkKH1raeLqFBFP26FL87tMBe4UyV1EFv9iNQttnt1RvDk6nZvSrxbNVaVEjvm4iu4xw9szKKpsqbaLL7rixfPb9JDL9Mkt2Ntw147mLSgYTGuMTaW9SfdT93RdNUSk7ae1UFhTwoTGqBcancfeKBnBnibQg28J5bFJZpxXZqsDruDnrGWJSu1H39pMxaL9WdQ2NReJFmnBpHFcUZV7KjvCA5tkZ16xVWxMq8BRge4tKnvabGjoecXtPkv1WqoBaCzEovx5wRocxXNmbGGhjdxygFwdcLm3rxmRaEhrDFGmK5rjiSeDiApMyqLmTJ",
    "channel_id": "ch_29w6DawuzPcVbFAFt8QF11upvn6hcoiLM6g5dMd3KZsa3KMNoh"
  }
}
```

##### initiator: (2018-10-16 20:05:56.157)
> Funding has been confirmed locally on-chain

##### responder: (2018-10-16 20:05:56.157)
> Funding has been confirmed locally on-chain

##### initiator: (2018-10-16 20:05:56.157)
> Funding has been confirmed on-chain by other party

##### responder: (2018-10-16 20:05:56.157)
> Funding has been confirmed on-chain by other party

##### initiator: (2018-10-16 20:05:56.158)
> Channel is `open` and ready to use

##### responder: (2018-10-16 20:05:56.158)
> Channel is `open` and ready to use

#### initiator ---> (2018-10-16 20:05:56.189)
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

#### responder ---> (2018-10-16 20:05:56.189)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 2,
    "from": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz",
    "to": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW"
  }
}
```

#### initiator <--- (2018-10-16 20:05:56.193)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQRTt38jCE8smFs5sKkqRbQqVwPhWyhV8Bx2fPj7KMPquibTJrJunANiSSKdyWqcjzGs7GUuQ7pvZd5JzC9THjAZU15aZCTGE5necMAWDeQQv3mXmbsHTxUrEKrGvgFyiQCd4ESdbdvT56DnMpazCMosVE6gfPpDGeFQxug3urNxqvQqTEE5UBP2GXEeffwPQ2DstiSe66Vdns"
  }
}
```

#### responder <--- (2018-10-16 20:05:56.194)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQRTt38jCE8smFs5sKkqRbQqVwPhWyhV8Bx2fPj7KMPquibTJrJunANiSSKdyWqcjzGs7GUuQ7pvZd5JzC9THjAZU15aZCTGE5necMAWDeQQv3mXmbsHTxUrEKrGvgFyiQCd4ESdbdvT56DnMpazCMosVE6qFyHsJ6w48KjU3EuYK6m3iqrvwin351x9322nozdc9CB1vvtJ8u"
  }
}
```

#### initiator ---> (2018-10-16 20:05:56.195)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak519VfCzo8oJwRG4aN5KMucXRZSnpTHnhHSdqsLqvNBpKAuAHjm9krDabzQG9vJUPKUVxgBXfkkJq1HsquCLYVwQSXYS6LnWvKyLrEvCLecN6odszPvGsE7fWxqWoC3ghzRS5qSRi8CunM9ChVAq1fHGShW4tc4NkJVo7mpUnbJUUyNCsKySkFJDqmW2yZy8EYo6Fot5MwhKyVezLshN1EoxCf5EHu2ekGTpRc3cv1TMcNSxFmHFrU1J6H6RaJxTyQ6P6APj7vLkvvrF3EM9yuxzQMZUk8cAFUXhRzPDUYEvPGrz"
  }
}
```

#### responder ---> (2018-10-16 20:05:56.195)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4nuFr7n1D4NUYoGSBbxady17d37gYhSuCtS8Ndm1ZNdLyjY9UDddLeTKw7gfZRVcDPYSp8nk8izdGdpq2XjR43UZh7zLk4xmXmoj4P32DYHYF2tzUAUNB8WCNW6cpmAFethPg4sQjmvYJ8SfyNykHPooxSQKyCXvbMdtwddJFsQsQbPxBjkrTseCvCEPMUXREmcWahEj6QNfiq4kzrcZJBgMd8zMJCwbXfvs4RMok6ZLCK4WiDR7dDkX9ByQv3n8znk1atzUuCPEp4jctYH4nWyUtBSePxuba5vdBmspzLV9kJk"
  }
}
```

#### responder <--- (2018-10-16 20:05:56.197)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_29w6DawuzPcVbFAFt8QF11upvn6hcoiLM6g5dMd3KZsa3KMNoh",
    "round": 1
  }
}
```

#### initiator <--- (2018-10-16 20:05:56.197)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_29w6DawuzPcVbFAFt8QF11upvn6hcoiLM6g5dMd3KZsa3KMNoh",
    "round": 1
  }
}
```

#### responder ---> (2018-10-16 20:05:56.197)
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

#### initiator ---> (2018-10-16 20:05:56.198)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 2,
    "from": "ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW",
    "to": "ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz"
  }
}
```

#### responder <--- (2018-10-16 20:05:56.203)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQRTt38jCE8smFs5sKkqRbQqVwPhWyhV8Bx2fPj7KMPquibTJrJunANiSSKdyWqdDhTJwmjSCtZQ1zrXR4Y22NBoZ5zuwjrptUNfZBC6bdQbNpgQCnhh8iah7pDLxnSxdDygGnB53HCuYc7bwT3WRghCeJ1TZ7RwxXJaiKHGQGi7VeRjSiCxyixeCbUvNgiZuoX4NYXGLMM4NG"
  }
}
```

#### initiator <--- (2018-10-16 20:05:56.203)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQRTt38jCE8smFs5sKkqRbQqVwPhWyhV8Bx2fPj7KMPquibTJrJunANiSSKdyWqdDhTJwmjSCtZQ1zrXR4Y22NBoZ5zuwjrptUNfZBC6bdQbNpgQCnhh8iah7pDLxnSxdDygGnB53HCuYc7bwT3WRghCeJ1c7USHDAzBTbMPKZgMyAM7ATVByEqscKosAjpTzKxQf5mXeBv8H3"
  }
}
```

#### responder ---> (2018-10-16 20:05:56.204)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak59mvgjZjWorB6w7o57hHAoUFLHkxBXGqPmwhE96DgccfuCvoGHvFoa7BkjwNxqpQomeaqEYs5fAqL5CH5qZJKQ3mjtLC2cNfCPP966v67JBbZ8S2o4ViEHbouGcDForhi7EENReueaTbze6iWH2CPBrEqrXaZC49ZofMueUjyc7AMN8DKgfmWFSsu5yzjn74DV1x9mExHBEYfHv37hpYD48bdQKjz1xMa921BNNsAA9DktLtaP3RpsGk5UZsv2suDPmSsxuGBrRFRBgfvgpByDRkFRNkMKDuKWXLXSS6mGzYwp1"
  }
}
```

#### initiator ---> (2018-10-16 20:05:56.205)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4zg2L3nU7SnvULzPxv1yWRKyMz2cwecAC3BvLcGaWsro29LdruHMCBWEWeNKTSkhtUQydib1Y2qEXPnzNAfRhmhm4MMuXh1qsZRZxDkw5TbaEM2MeoxfGYtbNv3qQKffopWLB9QbHVUsdJ4oB2nUr3ngqpaWZ5S9zaLDj3Q3ye1hFiNJS6LVME2YYZA7yoMzjzDHy1XrdZsgC78XeeqGNGDUywyNFZdXyLpNacmdGoyDgV9UhmWqRUVD1uYSznDWbMSY15q16FmkbeCqPRn8GEb7FKfMsV4GUhdMNcX6tBsCNTx"
  }
}
```

#### initiator <--- (2018-10-16 20:05:56.206)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_29w6DawuzPcVbFAFt8QF11upvn6hcoiLM6g5dMd3KZsa3KMNoh",
    "round": 1
  }
}
```

#### responder <--- (2018-10-16 20:05:56.207)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_29w6DawuzPcVbFAFt8QF11upvn6hcoiLM6g5dMd3KZsa3KMNoh",
    "round": 1
  }
}
```
