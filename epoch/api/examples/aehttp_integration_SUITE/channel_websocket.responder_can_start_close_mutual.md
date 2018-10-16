
#### initiator init (2018-10-16 17:13:58.155)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb&role=initiator
```

#### responder init (2018-10-16 17:13:58.161)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb&role=responder
```

#### responder <--- (2018-10-16 17:13:59.162)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 17:13:59.165)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 17:13:59.175)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpALGJSrzwTy6oub8Qv4su7RMx2hck9JNUEgjtyU6qrUG48oB7x4ucqxPokv4rA4P5zaAWfi6eCujMzNBvMMu3xP8p9Svn5xM77VDy3ntvSFDRTNLxquqDLKr53dA7VoLQyju8FB1sKcPCeRhzzU2bUngSwArdVLi"
  }
}
```

#### initiator ---> (2018-10-16 17:13:59.205)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4Ho7pJ8M6yXm8HZW2tvNtxBDq2J4NuvTZ897cD6kWh92oJUAqQU2sBhLdrB6aPT4fkCkh5t3zV1SiSje7DCgUBjweiueZNGBn8qTLMzR48CBHxpN413ES7sUyB5RjBMGspGVZAnmkuSPygD7wwqY3TqGu7SvN2RrM9gz1X7vb6s29ocL7SoDtZapnEo2ommsYZZbqUkofGvFUUk5UURz58SAQCHEqdotnSgbU31SMeDa7UKu2gWJEscLrdsDeHjikk"
  }
}
```

#### responder <--- (2018-10-16 17:13:59.206)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 17:13:59.207)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpALGJSrzwTy6oub8Qv4su7RMx2hck9JNUEgjtyU6qrUG48oB7x4ucqxPokv4rA4P5zaAWfi6eCujMzNBvMMu3xP8p9Svn5xM77VDy3ntvSFDRTNLxquqDLKr53dA7VoLQyju8FB1sKcPCeRhzzU2bUngSwArdVLi"
  }
}
```

#### responder ---> (2018-10-16 17:13:59.207)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4Hmd87BrQL4FfjymGZi3isXHcDQuuNLgdV8AVJ1TK6K7X3hjazor6yG3NL4EZcpsywKyUMDsH2wCgdSP9Vco4QjgVhsk43Vqz3AtTkbpvXGkd32F4vqrfWGj32xFjTC1AsgRQjm6kwUHWe4f6QFqCvFe2FnnXVmE7eaEKBttMko3NwhaVyuTn27RZjs65pmtzrtdNM7xhfwzXpDMXLSoCv7CuritUZ9QHcfwNSScCVydhk2Qem9ZLWBzG7bcxQ1kLp"
  }
}
```

#### initiator <--- (2018-10-16 17:13:59.209)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 17:13:59.209)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmQzp3a5n89cYuH8XoVnMe1oVzJXWo9hkq8iqq74jUGrt44Zn8aN56DUnmMrVKC5LTickh6dQh6XZy3aXBHuRYvtSN1tpC98RT7YUg9CbzibTHcRwJKbyk4rVRJtvH3BomAoPnMYmy9E3M6vjokDKfQApACUYxPxKeZ4LTMJ6E6o368zW8EfuUc17MNw34bb14N5xDjESLd3kYL62HKhL979UwjGjYSSKZ2atFDoTkK2ixywYNcSfic2sJT7qCwmyzrsZ3KeEUUVAtRXRg4sHb3TBbCJzf756cpxvi9Ghn7g5VaRArdcxTVPThLuwJD3gQmSEUDM7bGxgB4fp6DSwUde2Y2q"
  }
}
```

#### initiator <--- (2018-10-16 17:13:59.210)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmQzp3a5n89cYuH8XoVnMe1oVzJXWo9hkq8iqq74jUGrt44Zn8aN56DUnmMrVKC5LTickh6dQh6XZy3aXBHuRYvtSN1tpC98RT7YUg9CbzibTHcRwJKbyk4rVRJtvH3BomAoPnMYmy9E3M6vjokDKfQApACUYxPxKeZ4LTMJ6E6o368zW8EfuUc17MNw34bb14N5xDjESLd3kYL62HKhL979UwjGjYSSKZ2atFDoTkK2ixywYNcSfic2sJT7qCwmyzrsZ3KeEUUVAtRXRg4sHb3TBbCJzf756cpxvi9Ghn7g5VaRArdcxTVPThLuwJD3gQmSEUDM7bGxgB4fp6DSwUde2Y2q"
  }
}
```

#### initiator <--- (2018-10-16 17:14:01.297)
```javascript
{
  "id": -576460752303423463,
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

#### initiator <--- (2018-10-16 17:14:02.876)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### responder <--- (2018-10-16 17:14:02.876)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### responder <--- (2018-10-16 17:14:02.877)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### initiator <--- (2018-10-16 17:14:02.879)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### responder <--- (2018-10-16 17:14:02.881)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### initiator <--- (2018-10-16 17:14:02.881)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### responder <--- (2018-10-16 17:14:02.882)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmQzp3a5n89cYuH8XoVnMe1oVzJXWo9hkq8iqq74jUGrt44Zn8aN56DUnmMrVKC5LTickh6dQh6XZy3aXBHuRYvtSN1tpC98RT7YUg9CbzibTHcRwJKbyk4rVRJtvH3BomAoPnMYmy9E3M6vjokDKfQApACUYxPxKeZ4LTMJ6E6o368zW8EfuUc17MNw34bb14N5xDjESLd3kYL62HKhL979UwjGjYSSKZ2atFDoTkK2ixywYNcSfic2sJT7qCwmyzrsZ3KeEUUVAtRXRg4sHb3TBbCJzf756cpxvi9Ghn7g5VaRArdcxTVPThLuwJD3gQmSEUDM7bGxgB4fp6DSwUde2Y2q",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### initiator <--- (2018-10-16 17:14:02.883)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmQzp3a5n89cYuH8XoVnMe1oVzJXWo9hkq8iqq74jUGrt44Zn8aN56DUnmMrVKC5LTickh6dQh6XZy3aXBHuRYvtSN1tpC98RT7YUg9CbzibTHcRwJKbyk4rVRJtvH3BomAoPnMYmy9E3M6vjokDKfQApACUYxPxKeZ4LTMJ6E6o368zW8EfuUc17MNw34bb14N5xDjESLd3kYL62HKhL979UwjGjYSSKZ2atFDoTkK2ixywYNcSfic2sJT7qCwmyzrsZ3KeEUUVAtRXRg4sHb3TBbCJzf756cpxvi9Ghn7g5VaRArdcxTVPThLuwJD3gQmSEUDM7bGxgB4fp6DSwUde2Y2q",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

##### initiator: (2018-10-16 17:14:03.693)
> Funding has been confirmed locally on-chain

##### responder: (2018-10-16 17:14:03.693)
> Funding has been confirmed locally on-chain

##### initiator: (2018-10-16 17:14:03.693)
> Funding has been confirmed on-chain by other party

##### responder: (2018-10-16 17:14:03.693)
> Funding has been confirmed on-chain by other party

##### initiator: (2018-10-16 17:14:03.693)
> Channel is `open` and ready to use

##### responder: (2018-10-16 17:14:03.693)
> Channel is `open` and ready to use

#### initiator <--- (2018-10-16 17:14:03.726)
```javascript
{
  "id": -576460752303423462,
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

#### initiator ---> (2018-10-16 17:14:03.727)
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

#### initiator <--- (2018-10-16 17:14:03.733)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQQfh2i4oT7wQdbCSPnJyjAkcPjZ7Zit4mrweTA2pTCH78LrxMd62JswP7XwW4GtJk8bTYo4NC2FA8JywfxGhbywGGcWRJBLh2qmwS2opZeXnNLYYVhSV4sWGaV27vmrng93hBo7CFe1wWCd863mfUGyxZtykaGndmahHCDSZU4KB8is6QCdUpu5EWo9mcNssJY8KE4C7Wfc5Z"
  }
}
```

#### initiator ---> (2018-10-16 17:14:03.735)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak52QyXiXBMhi5tSdKFTheivbXKV4DEVJSUSZBRNiysZUMrwndfsarFUD9xXytd76dNdzLZ9SmyRXioW3Eggquma7c86fBeFj4f2YMyH2fZjEF1S5cYC1oDdhZUxu9zjSdfc9wdjkeV3d6uecAtcysBS7dFzvHwB2HFzBVDexALBZ558cGDdXNpP9g1NJGPbYKN9PzSE8oHQwP2WDwvQek4cgVjBo2LD8Wki4MHKpueMB7uU3xq2SCEmQGduewgwSxg7ztQnwTcpKVQLuqYRjmztucRGBJyyrgVVPFnE83NmEnqK9"
  }
}
```

#### responder <--- (2018-10-16 17:14:03.745)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### responder <--- (2018-10-16 17:14:03.745)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQQfh2i4oT7wQdbCSPnJyjAkcPjZ7Zit4mrweTA2pTCH78LrxMd62JswP7XwW4GtJk8bTYo4NC2FA8JywfxGhbywGGcWRJBLh2qmwS2opZeXnNLYYVhSV4sWGaV27vmrng93hBo7CFe1wWCd863mfUGyxZtykaGndmahHCDSZU4KB8is6QCdUpu5EWo9mcNssJY8KE4C7Wfc5Z"
  }
}
```

#### responder ---> (2018-10-16 17:14:03.747)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4wKtz8F5wvkjKe7Hgb4onSPdSHae621uBKsu4copz24vrvLQPEcmHDVRmiqPqadmoJkpp7WkDiPx12XHFmq3xspdCghoUaNfbcfaTM995zA2yecph4Kr5enUdVy78Eo6JQTMTvEst4QHKCEcW6Ynvrh2oU6rRhZomEFiUb1TkEfSAvkxTTd5KQECAZHTCAz7XmhWxQBWiRXcMYdnfiBH87yKcWkcKE5BUwvoNEZ982uggBL2q7Sdar8m48wDyaWfPeYN1bReF9X9WDt3GTTqyRdXcH3WiJ3G98VCpNKbPd6fyD5"
  }
}
```

#### responder <--- (2018-10-16 17:14:03.752)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkdxZAx7BzzqYMHdZPLrjfZdhJzjwf84iDQnVEQ7gw9mvfP12DezhGfNDAsaVMJsYjxkgGNAfYHeD4C88BXp8SVU4y24N4dPzUBX7c3JQ3SoejVShWmZSgzPczXhdMHVyFDagzwb6uYRDCss7qQNSczV4gZE2GJD697xkEE8Uhnoed3DZMg4D7Jp7jdTTP8V1R2jcPkR7njWpmdeekpNXKwnfJwfwtSAmBK6Cy9E2gexXqmtbbhKWrrbK5wSwNx6xDLyG4FFkucRC8yLjSd4Y1u16rXWZKPzkuEWjTUrvbGPA9kh8s3NWQp17NRjKJkPKBTccePmC8HjzeBw6BAe4SjYoLCopFxVnZCDMur6GThYxKdkFnEeSVU8tyX7v4JBmMibPjWUKf",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### initiator <--- (2018-10-16 17:14:03.754)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkdxZAx7BzzqYMHdZPLrjfZdhJzjwf84iDQnVEQ7gw9mvfP12DezhGfNDAsaVMJsYjxkgGNAfYHeD4C88BXp8SVU4y24N4dPzUBX7c3JQ3SoejVShWmZSgzPczXhdMHVyFDagzwb6uYRDCss7qQNSczV4gZE2GJD697xkEE8Uhnoed3DZMg4D7Jp7jdTTP8V1R2jcPkR7njWpmdeekpNXKwnfJwfwtSAmBK6Cy9E2gexXqmtbbhKWrrbK5wSwNx6xDLyG4FFkucRC8yLjSd4Y1u16rXWZKPzkuEWjTUrvbGPA9kh8s3NWQp17NRjKJkPKBTccePmC8HjzeBw6BAe4SjYoLCopFxVnZCDMur6GThYxKdkFnEeSVU8tyX7v4JBmMibPjWUKf",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### initiator <--- (2018-10-16 17:14:03.759)
```javascript
{
  "id": -576460752303423461,
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

#### initiator <--- (2018-10-16 17:14:03.760)
```javascript
{
  "id": -576460752303423460,
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

#### responder ---> (2018-10-16 17:14:03.760)
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

#### responder <--- (2018-10-16 17:14:03.764)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQQfh2i4oT7wQdbCSPnJyjAkcPjZ7Zit4mrweTA2pTCH78LxNsUdZn5H73Hw3BB1z5aeUKtWi2HYojorxh3ryWqTztjCMsJTgLcv8yMfPFzgQKTPtqQgvinaS6erdbcGbYf9x7ur6N7Z86wCgrT8nDi5nwWvh5dmg5XGyDjtS4xdkBGQtHRHwj21rYJW4zfR3Sz33FGEE9qqb4"
  }
}
```

#### responder ---> (2018-10-16 17:14:03.764)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4wZsVKZQ11ytTfHdsxFfgVwmBWfdj9t6XcQ6RUxDtckVx3NuWrRz1y2PyrM26X1BbD5fRkhKPr6hMMEKKuuN7Qibii9VarXGZwZgiCDUe55SNydo8yktvto2uTbnnqYXWMBRGsFySyCJGiZwxatceRPUp79DTBNdu1Y8cv8YCTBGfweCRWDL9NsEM6rHg9c4TBMJLJJp274Dvg4nPnW5NGSiPsGvr5fgJsZGyfN1wvHWEmg7UUHvPsPX1DKAsLKsWwBoxL6HXYe1HMH8xVRXiWHAUjzU8sthF58kX7Rv6TYg1tk"
  }
}
```

#### initiator <--- (2018-10-16 17:14:03.768)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### initiator <--- (2018-10-16 17:14:03.769)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQQfh2i4oT7wQdbCSPnJyjAkcPjZ7Zit4mrweTA2pTCH78LxNsUdZn5H73Hw3BB1z5aeUKtWi2HYojorxh3ryWqTztjCMsJTgLcv8yMfPFzgQKTPtqQgvinaS6erdbcGbYf9x7ur6N7Z86wCgrT8nDi5nwWvh5dmg5XGyDjtS4xdkBGQtHRHwj21rYJW4zfR3Sz33FGEE9qqb4"
  }
}
```

#### initiator ---> (2018-10-16 17:14:03.769)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4pgKSPGsK5Jfqxqngujz7FXJdgnHb7WE8sd7K3aA1WPKGNxJ1T2ynkCvqwMyehokgoJi2dw2ZtfFfkaeh1kfD2429DyvZRH3kcW29AgQg1N4FMHabv5GaX4uBF9i4Jzxt94RpkUqFv289qDLDTo7rKLSW31jhG9m3zPc8SQtFRABmKDXrrEVp3gopHZQcn3HcgZe34hMWUAtp7xy4GwKBdjrjS2QQSDstiiQ67P4hNYBf9dD2h4uz5tcwWyEn59FsDFTEDjUCG49t8BsaxhyYbr3yZf5z1ce9KjAy4K9XM2aZPc"
  }
}
```

#### initiator <--- (2018-10-16 17:14:03.774)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkSXgUoMdiTjyBqrdN8ePs5pDY66aU5qQvWsDwjpUUrgLgWFF6uP1oPxv7NZaYVjjGb2uwo9eLygkYbdpETbb4HYVswLCAyY8YK8SpcX4Ez1qisZeBjLD62brDwv3yvSZuBRXYP57UkH5UUpqfbkQCC3xnCZi8YXcXQDCeKkpeggQGXgbPpPjdbZhkP8TJ22M8h5hExKBNetmqhHqDgvUTuhEGZRCmacW6pRakdKEyTAQEt1qWDZj5U5PS1VhaagPLSQkifxHspcrPzya2zfRgPx3sWziiHcrM3Dz9gQh4Z9bh5gtMg6n1jVKpArVMhy7Fnkpd69zv7AwGjDr6Ldd9V7qiRsHPtXsUjVT3mJZwVKgLagsYBMQ2BqiPD6jY62TqhxkcnFQ8",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### responder <--- (2018-10-16 17:14:03.774)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkSXgUoMdiTjyBqrdN8ePs5pDY66aU5qQvWsDwjpUUrgLgWFF6uP1oPxv7NZaYVjjGb2uwo9eLygkYbdpETbb4HYVswLCAyY8YK8SpcX4Ez1qisZeBjLD62brDwv3yvSZuBRXYP57UkH5UUpqfbkQCC3xnCZi8YXcXQDCeKkpeggQGXgbPpPjdbZhkP8TJ22M8h5hExKBNetmqhHqDgvUTuhEGZRCmacW6pRakdKEyTAQEt1qWDZj5U5PS1VhaagPLSQkifxHspcrPzya2zfRgPx3sWziiHcrM3Dz9gQh4Z9bh5gtMg6n1jVKpArVMhy7Fnkpd69zv7AwGjDr6Ldd9V7qiRsHPtXsUjVT3mJZwVKgLagsYBMQ2BqiPD6jY62TqhxkcnFQ8",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### initiator <--- (2018-10-16 17:14:03.779)
```javascript
{
  "id": -576460752303423459,
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

#### initiator <--- (2018-10-16 17:14:03.780)
```javascript
{
  "id": -576460752303423458,
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

#### responder ---> (2018-10-16 17:14:03.780)
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

#### responder <--- (2018-10-16 17:14:03.783)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQQfh2i4oT7wQdbCSPnJyjAkcPjZ7Zit4mrweTA2pTCH78M3oPLB7FGcpy3vaJ58q5Mx14SxH6GEhsDurJyLjCaDbvDTmyyK3bGrt8T763jTVR92rTukF9fq42wHDJKXUCbA5S8nxHh7qWcaB6qVjeCg4BpbEvLWxQJfjZP6tiWawBiNtrfr53Mt6SYFkcTeAhRGYA1AL273y8"
  }
}
```

#### responder ---> (2018-10-16 17:14:03.784)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak5CAX4eEyYWCbfJgz3PGpQ6iZ5TBC4THxbi73AbTA2EqsVLM7kR8p8YcRxgXN9uyGYCnQGumsnXNfkRgMm1RKQuxAyjt7SY8M9cAxxde8DqBpoAHwfdQEUncY4sTd9p9tZzFD2MFCVcJ3hmyehec94ainXQAi7KUpvnXR84HjEqjJFFgyktNS6estzCCsEBL7htc6M1QzhU2EynA1UjLkjC2wyReM9U79af8cE6q2txRhHmNySviwx86CTwMfUsgsFRyNJpPAEaBcRfWoLcVvQXjXQATufQQtXzvwch5Bpcv3esm"
  }
}
```

#### initiator <--- (2018-10-16 17:14:03.788)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### initiator <--- (2018-10-16 17:14:03.788)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQQfh2i4oT7wQdbCSPnJyjAkcPjZ7Zit4mrweTA2pTCH78M3oPLB7FGcpy3vaJ58q5Mx14SxH6GEhsDurJyLjCaDbvDTmyyK3bGrt8T763jTVR92rTukF9fq42wHDJKXUCbA5S8nxHh7qWcaB6qVjeCg4BpbEvLWxQJfjZP6tiWawBiNtrfr53Mt6SYFkcTeAhRGYA1AL273y8"
  }
}
```

#### initiator ---> (2018-10-16 17:14:03.789)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4pUnJTe5SpW98pbZMRwhdNmyeWg1zH59d4uSMzekK3pGHujNZFgrQL3h6z69ba237k5ZdXka1nxSCM5bPUaJWssQZTTSmgVsMmF9AepvQg5aXu8HyXvzau1TJEj7k7emLWH5Yvtzw2FnaLDbQWAofgMVw42jRVo7WtHsTJZpKKBLX2LjENVzEZpEoRQAMLKxQc5QJteM2yZVT9MeenRTZ4zK3cxQJsjRYuQA15pF8u4LC21xNEZC2vCjSQETmrhJaeYeFAEyHmPP166mv58ok789KA2gMwQsjg38xFaFhmthA1L"
  }
}
```

#### initiator <--- (2018-10-16 17:14:03.794)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkSBr82LLQ1uR4hi32UpUx7zsvQ5v7wsbbiSfxwyRxLFALfs97R9AmLEVNcfe6AVNdbTSBePBWiX8G3ZKc3YTXkac3ZdmzU6sPavw6DGNneGvjmssZz6ej34q1Yh7C8bPmpixG43mmLnTibr9xwv5uE9Cu9JSEgBqceTa4soKzrrSWhj4C1EpV5zU2prMGthGZrFkUnSH4diK86HGZvnNf7ry2Mh5B2Ys7k8d22xZmRABkrTPPqLkM1sf3FXWZpxnmvmSc3tvqaytEJsUvBJg2efgLQjGBUgjJU6QfyicEiW7e8Jf5dNdHHmTguKSoL8Frxharm1TPjPf4BqXc1VkM58pAUiNFJrsnVCcb7jHK9SgCAACAkK85Y8sgti2vzUBA15aKcPRv",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### responder <--- (2018-10-16 17:14:03.795)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkSBr82LLQ1uR4hi32UpUx7zsvQ5v7wsbbiSfxwyRxLFALfs97R9AmLEVNcfe6AVNdbTSBePBWiX8G3ZKc3YTXkac3ZdmzU6sPavw6DGNneGvjmssZz6ej34q1Yh7C8bPmpixG43mmLnTibr9xwv5uE9Cu9JSEgBqceTa4soKzrrSWhj4C1EpV5zU2prMGthGZrFkUnSH4diK86HGZvnNf7ry2Mh5B2Ys7k8d22xZmRABkrTPPqLkM1sf3FXWZpxnmvmSc3tvqaytEJsUvBJg2efgLQjGBUgjJU6QfyicEiW7e8Jf5dNdHHmTguKSoL8Frxharm1TPjPf4BqXc1VkM58pAUiNFJrsnVCcb7jHK9SgCAACAkK85Y8sgti2vzUBA15aKcPRv",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### initiator <--- (2018-10-16 17:14:03.799)
```javascript
{
  "id": -576460752303423457,
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

#### initiator <--- (2018-10-16 17:14:03.801)
```javascript
{
  "id": -576460752303423456,
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

#### initiator ---> (2018-10-16 17:14:03.801)
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

#### initiator <--- (2018-10-16 17:14:03.805)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQQfh2i4oT7wQdbCSPnJyjAkcPjZ7Zit4mrweTA2pTCH78M9DuBieiTxYtov7QyEqjUW3kUP5PxJrWZ8cXihxfCC5M5JfeBtnnocAuK8vvrs3fPTRPCcSMXG8PLHs2udQdw458Twn2Ni5jEjaqCrXjkkkJoyNA3xW31RUJ8P29kfPMNMqyZm2AFEffMaGzyDcpdPua64wpy6Hz"
  }
}
```

#### initiator ---> (2018-10-16 17:14:03.806)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4jb7mqbDCdNJSY6NzrLMfuciDQC1GV4n63GxhZUV3SMVYRCiXsf721n5P4M8kRPbK3d4YVn16EKkZp7X9fL5GTHamHXMSWxCBDWELiQ19ZR2RuyyTJgrtyw6xTviisP2gRgnRAZDyAh13b3zZuVTJ2voh2LkcDMGDw4BgKPzj8UdwN26cKd6yKRLJrNjD5vREi2wPJXKHkeAGHC5F55YDBmAyFkUTXzCHhBG5bKM4R7yG6ncK7jkAsvmXhixYw2wmkox3iFyN7Zno4zE8VcJvLkimXe76YQZZKuhRQEPaxw63Gm"
  }
}
```

#### responder <--- (2018-10-16 17:14:03.844)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### responder <--- (2018-10-16 17:14:03.846)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQQfh2i4oT7wQdbCSPnJyjAkcPjZ7Zit4mrweTA2pTCH78M9DuBieiTxYtov7QyEqjUW3kUP5PxJrWZ8cXihxfCC5M5JfeBtnnocAuK8vvrs3fPTRPCcSMXG8PLHs2udQdw458Twn2Ni5jEjaqCrXjkkkJoyNA3xW31RUJ8P29kfPMNMqyZm2AFEffMaGzyDcpdPua64wpy6Hz"
  }
}
```

#### responder ---> (2018-10-16 17:14:03.849)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak57Yrh6bgwP962rBybDAjnRbKAuLSVkzFrhPPyx7dMAAKSxvgXTwD51kYGLaft1t5zWt2cNRrAXnwc8zYjz9UEx8PVrUjnGubA1prNTKHu6MELBDuNsLjmtKYww3Z77eBoERVdENcdo3mMvacxrv1oV9u8gPX9xFhHioTXCDLtb7Dcda5hW1xgGvRqJdhEQiukb33LLeQmRDKjtwxqThBCFSgGo296EoUm6M31Mbcd6j5v2nLptSAg2MHefgjzaukSS7wbkGBUFjf1NguzLG4bnMMvZfoMyXGgULbD3gMTWZSEVi"
  }
}
```

#### responder <--- (2018-10-16 17:14:03.863)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkHnBTsp1BxBNACjTzapVp9bX6Y3qtrurbU7pANtt75QpE2aHLeKFyt6LLLS6onLYWDivjvuKggscLgk8sknjNx4DGcPhgEq7aMvXqrotzvWp5h8m4zVyd8HtKgMziZvhaZggunWY6iXCEo5yhZwqqhzvz3XhmzrQM37F8egfJmT2ocsMqHni55T2SdAujpuh582C5FcuBuhn6gAZ45E4VD8h39rR2yfpLyHTsuCYxBcJ6wnjBtYYFqzN3Yq21SZMADEjZLvavT1ouAagBsumdwFmjyF9EXPjvMAxekQUBMT7MTte84avitBN8PcmepdKFWnpDsKxVLdVoEmMMLknrLEoqxTnyADPvFVMetrauK6rMauxVt4W1TDs7mJYJVdCDqThyjjhq",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### initiator <--- (2018-10-16 17:14:03.864)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkHnBTsp1BxBNACjTzapVp9bX6Y3qtrurbU7pANtt75QpE2aHLeKFyt6LLLS6onLYWDivjvuKggscLgk8sknjNx4DGcPhgEq7aMvXqrotzvWp5h8m4zVyd8HtKgMziZvhaZggunWY6iXCEo5yhZwqqhzvz3XhmzrQM37F8egfJmT2ocsMqHni55T2SdAujpuh582C5FcuBuhn6gAZ45E4VD8h39rR2yfpLyHTsuCYxBcJ6wnjBtYYFqzN3Yq21SZMADEjZLvavT1ouAagBsumdwFmjyF9EXPjvMAxekQUBMT7MTte84avitBN8PcmepdKFWnpDsKxVLdVoEmMMLknrLEoqxTnyADPvFVMetrauK6rMauxVt4W1TDs7mJYJVdCDqThyjjhq",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### initiator <--- (2018-10-16 17:14:03.871)
```javascript
{
  "id": -576460752303423455,
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

#### initiator <--- (2018-10-16 17:14:03.873)
```javascript
{
  "id": -576460752303423454,
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

#### responder ---> (2018-10-16 17:14:03.874)
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

#### responder <--- (2018-10-16 17:14:03.878)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQQfh2i4oT7wQdbCSPnJyjAkcPjZ7Zit4mrweTA2pTCH78MEeR3GCBfJGpZueXsNX4vZ4XZqREDcW841dYpJEa3ioyBzcDK1n6akNSdzVdD1fcWJmiurt1SLHuW8Nhk3DWTAL4agg8rFGKyK9bcDeVBragRvK8zwiAbjqiiZojdJSvYhDNKJVaCkXrLfgbQ4qHEKY6NqFnmokf"
  }
}
```

#### responder ---> (2018-10-16 17:14:03.879)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak51ffLTA2WoFzezGXd6VT5oknhXtu6bhKc6EzrgRSR5vVEMtXsRMYqZNFwQh4u8x51uieHwqD4o8uADwsm9xBz8PTRtgcC5RSD1dqR2KbUm76Admv6g2V1ucmmNeq4XLk29ByBgubRiqvAxFrvwtyqyWQ7BsbAYweVMsELuy4b7iphcPET9g2b5cGhJrk1pAnCz93nh4W4CQJ3UR3MA4yGyTxsVRzyC1oVw3scxU8DwYqyq5dhFcvPXERAHeM4VkNFwUtcbWRevbpfUHroUJLhnKaeeF4uqDZLrPawdvdUyZSgnQ"
  }
}
```

#### initiator <--- (2018-10-16 17:14:03.904)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### initiator <--- (2018-10-16 17:14:03.905)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQQfh2i4oT7wQdbCSPnJyjAkcPjZ7Zit4mrweTA2pTCH78MEeR3GCBfJGpZueXsNX4vZ4XZqREDcW841dYpJEa3ioyBzcDK1n6akNSdzVdD1fcWJmiurt1SLHuW8Nhk3DWTAL4agg8rFGKyK9bcDeVBragRvK8zwiAbjqiiZojdJSvYhDNKJVaCkXrLfgbQ4qHEKY6NqFnmokf"
  }
}
```

#### initiator ---> (2018-10-16 17:14:03.908)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4pD3o9JFdQT43iuXqao29SWCTzLs4EcQC1TkP9wbyGbH8anpntz1wMLq6v7UwMDKmg2KiJh9j8awJJLRieKyuAbf6mviFtH6oqnY5KQAaiv6pGzUQzpfHmWGLnx9bgHYKsNUHowFp9tMunXza9DupVWP6FMzR6CJz4pJ3gARFjX1LoLg4svnkAo4HzVa8CombXiHsd7rPbtoQcqztpdoepBd3aXkgouEaCpNdD497AnAbtPFVUDJinzXms6QrQsNzE8Hd3EdizE9UCuqg9kFBXzi1NE41nBg97vzeKN9c48xwmh"
  }
}
```

#### initiator <--- (2018-10-16 17:14:03.917)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkRioNX6nzdS2jTRxLSozzEMMPBdBkQXESPvYZt5JSsoN9pDmec56NRqovS7JitV3NonauuuuCGUzjUmUPM3L8XF4Fv6Vty4qfen9zxFiqEPgJm3ACsCzhwoPAqhF74LMQqJtabYpX8GhuRQAdCXovZCbdfyVDs7rdK7Ky9TeXrCriGLUiBvUk6Yc77S1ueGViAwjcpdwxJ17VjA3dkuiqVVz13xanGsjAcT2wx5jCktTZg9FW25sWH6ycTQbXr3ncM5VNMC3Ks1SAcWSGyvABU6JaRG1EzSp16MUgD4Vij7ABfbC6uHzTse6N1NuufoYViPYQfieeSososyXDVuUBGrknhrBVk9wiusb8xkYmV9bsJC6prWVZwfed1mrySK4zVWWUqhxe",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### responder <--- (2018-10-16 17:14:03.917)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkRioNX6nzdS2jTRxLSozzEMMPBdBkQXESPvYZt5JSsoN9pDmec56NRqovS7JitV3NonauuuuCGUzjUmUPM3L8XF4Fv6Vty4qfen9zxFiqEPgJm3ACsCzhwoPAqhF74LMQqJtabYpX8GhuRQAdCXovZCbdfyVDs7rdK7Ky9TeXrCriGLUiBvUk6Yc77S1ueGViAwjcpdwxJ17VjA3dkuiqVVz13xanGsjAcT2wx5jCktTZg9FW25sWH6ycTQbXr3ncM5VNMC3Ks1SAcWSGyvABU6JaRG1EzSp16MUgD4Vij7ABfbC6uHzTse6N1NuufoYViPYQfieeSososyXDVuUBGrknhrBVk9wiusb8xkYmV9bsJC6prWVZwfed1mrySK4zVWWUqhxe",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### initiator <--- (2018-10-16 17:14:03.923)
```javascript
{
  "id": -576460752303423453,
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

#### responder ---> (2018-10-16 17:14:04.13)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### responder <--- (2018-10-16 17:14:04.18)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "tx": "tx_2M9ipLgcZFrz2ugD3FAsttcZTsY6gzQA7caXNM7ksbi1xGhVw85Q3ouoayTDNwnn5YcSTrUhGA7cvqWniiB2ATvyLegzrDYdasMT9SrUKqYbBU43ppFah"
  }
}
```

#### responder ---> (2018-10-16 17:14:04.19)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "tx": "tx_2iJcVi27J8ZyyhirZQ1mCWVLSov3JiYMLTDcZPo1XSkgSnXDRkPbR4PGVfufhmykkBEPEMCgaW7koH9YALYaJaRdeqDajoY6mD7BTT2mG9N5hJ3RFwnVgmwx2VNDLusq3A9g2L8ZzhtghKcgrpmMyTJLqhokzAYkEP1Hw3VbP6KFwj2RGxUpHRh8A7ZaPGmiGyhfqN6V6zPwqjmNhz2eu9NC8w"
  }
}
```

#### initiator <--- (2018-10-16 17:14:04.20)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "tx": "tx_2M9ipLgcZFrz2ugD3FAsttcZTsY6gzQA7caXNM7ksbi1xGhVw85Q3ouoayTDNwnn5YcSTrUhGA7cvqWniiB2ATvyLegzrDYdasMT9SrUKqYbBU43ppFah"
  }
}
```

#### initiator ---> (2018-10-16 17:14:04.21)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "tx": "tx_2iJcVi27J8Zz2xMqMsKBduvGofx12JYNPx64JRkZv3xGZSmwxbFmwFtosCFz7urAhXjEFzThYajM8RbxUCDeCJgew3E1oFB5avvLViE2364TooxsMLWH7nbaAHXy8cbVnkepUR5hnipNjV4XEKnRQjq59nXto3WoXvA3FJNyix7pL1ZxxBtUkxqn7jWymkVoQ7q4bbeoseVYsXfLqkYdwipbas"
  }
}
```

#### initiator <--- (2018-10-16 17:14:04.23)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3wu1WL1txa1YELSbsxzi8cB68rAxZbRy19bH2gh2i3FZVvgYYfmJwWiM5BBygExHZcsEkCqzEzMhbCuQhaCNYFDALNRZRHSBqEwAbH977mbvgkswGnC8iSxc7ax2DP4eie3yGjLo8U54uUqs3C7eXTQ746bD93Cbswjn4o4jDSzr6zWEDdPisGcqVFqaLQHcktZjHNPn3798oAooH4e1EunDCWgeZWHga6xa7juy7hfwAbeV2aSkRFgWJAb4AtTunej5gT3hVegMoEVtzy9WpBfw2gtxjikCqyH1yGvviJWpEgayi8So",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### initiator <--- (2018-10-16 17:14:04.23)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "close_mutual",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### initiator <--- (2018-10-16 17:14:04.24)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### responder <--- (2018-10-16 17:14:04.30)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3wu1WL1txa1YELSbsxzi8cB68rAxZbRy19bH2gh2i3FZVvgYYfmJwWiM5BBygExHZcsEkCqzEzMhbCuQhaCNYFDALNRZRHSBqEwAbH977mbvgkswGnC8iSxc7ax2DP4eie3yGjLo8U54uUqs3C7eXTQ746bD93Cbswjn4o4jDSzr6zWEDdPisGcqVFqaLQHcktZjHNPn3798oAooH4e1EunDCWgeZWHga6xa7juy7hfwAbeV2aSkRFgWJAb4AtTunej5gT3hVegMoEVtzy9WpBfw2gtxjikCqyH1yGvviJWpEgayi8So",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### responder <--- (2018-10-16 17:14:04.30)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "close_mutual",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```

#### responder <--- (2018-10-16 17:14:04.31)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_wJf1iMx7kACDkGNYm3C8F8Wpt88MSgPPrnC8aPAH91imtRjQW"
  }
}
```
