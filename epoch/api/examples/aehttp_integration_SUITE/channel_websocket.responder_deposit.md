
#### initiator init (2018-10-16 20:26:03.610)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A&role=initiator
```

#### responder init (2018-10-16 20:26:03.614)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A&role=responder
```

#### responder <--- (2018-10-16 20:26:04.614)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 20:26:04.617)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 20:26:04.625)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpALFUXGGsdug6Jrs56usDVK43SheHuLKP3h48aDzajQnhSXBUWq2rVDufMiousdvbextEcPQPuUq7817TtZyDq2vCt4rqTh3SqYy9jCHBN6SuCufA4j65Xrud4Spcwoi5gsMaowEXQETWMtFFZcbw7DeBp5X6ajr"
  }
}
```

#### initiator ---> (2018-10-16 20:26:04.663)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HmrkYXmky7MMCSUevgDZfHgtscpcFHZYYQEZyVKm1kZ2hb68AzfLvemqu8tXnyaat8Pnm6hLX1VjvMvhyWt3NaRRje5HgyW3Et3HoFdSNo4LGvkH4pkctdggcXCjrfD1C4Uvq8BeMiZxcqLUN9DFWy3DrVRiXBDiYxFuwZTJcBwaRnbP2wvmC8zgmsRdswSGncVsCNFgGCkiXFJMpsSQV8dystycAigaWAyvtQf6Ufd2mi9Z5JJSTjQDDskTjBSZo"
  }
}
```

#### responder <--- (2018-10-16 20:26:04.664)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 20:26:04.665)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpALFUXGGsdug6Jrs56usDVK43SheHuLKP3h48aDzajQnhSXBUWq2rVDufMiousdvbextEcPQPuUq7817TtZyDq2vCt4rqTh3SqYy9jCHBN6SuCufA4j65Xrud4Spcwoi5gsMaowEXQETWMtFFZcbw7DeBp5X6ajr"
  }
}
```

#### responder ---> (2018-10-16 20:26:04.666)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4Hk9PSiUWdnKNSUz26SG1UHRperwatAaZidyNwfyfFFrSfHVdkP7SeebYhJa2PzTEA3k3uxbMbRK1aXaLBQe2j2ftitb3bSaz7g2VrJwW6YemhVPF8Hpp6s24nB7ggFikgRp3G2mWncVxvDsWD5WpYgyA3KpL2mMqMfkrETn1iuYFP3LMuNJjri4JmZCddUK7Pym8kBCHwsiFH6DbMY8GgbsdhTVsacFdfxwV51t6RCD6ZRaF9HNMH6qBQ1xEBKEeC"
  }
}
```

#### initiator <--- (2018-10-16 20:26:04.668)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 20:26:04.668)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmNTRCfzVYr3HR58jh6r9abTxiiem2kgvWZGhQHxowJ8opMaBLoexEcgVFXGXio27bwyAJ6Hrsdsg1vXs6sV577wF236XotkNvWaWkgr7ZzKRK2ePCtEZYZmHtSiZ1T6KeuwYVW7WoEZPvEE29QUYPyRSjU57Hxtq9QaV8DjQzvfLPk1uoJTm9RtBxMDrAyjzv9FZVFQQETvHhhXKhzGfM4Roqmc8hQF3HbDrsiuCdUknoe7mWmzGAUsHdEnWCQFdYKwk7Jzq3FYMmbyWbnaTxv5hMCjqUATHAfegF2A42LXxZ4YYwmW6XyJwhjJ886fFG21RNsWFe8B5wxsZBXtdW8RYfRy"
  }
}
```

#### initiator <--- (2018-10-16 20:26:04.669)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmNTRCfzVYr3HR58jh6r9abTxiiem2kgvWZGhQHxowJ8opMaBLoexEcgVFXGXio27bwyAJ6Hrsdsg1vXs6sV577wF236XotkNvWaWkgr7ZzKRK2ePCtEZYZmHtSiZ1T6KeuwYVW7WoEZPvEE29QUYPyRSjU57Hxtq9QaV8DjQzvfLPk1uoJTm9RtBxMDrAyjzv9FZVFQQETvHhhXKhzGfM4Roqmc8hQF3HbDrsiuCdUknoe7mWmzGAUsHdEnWCQFdYKwk7Jzq3FYMmbyWbnaTxv5hMCjqUATHAfegF2A42LXxZ4YYwmW6XyJwhjJ886fFG21RNsWFe8B5wxsZBXtdW8RYfRy"
  }
}
```

#### initiator <--- (2018-10-16 20:26:04.996)
```javascript
{
  "id": -576460752303423430,
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

#### initiator <--- (2018-10-16 20:26:05.662)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### responder <--- (2018-10-16 20:26:05.662)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### initiator <--- (2018-10-16 20:26:05.664)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### responder <--- (2018-10-16 20:26:05.664)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### responder <--- (2018-10-16 20:26:05.667)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### initiator <--- (2018-10-16 20:26:05.668)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### responder <--- (2018-10-16 20:26:05.669)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmNTRCfzVYr3HR58jh6r9abTxiiem2kgvWZGhQHxowJ8opMaBLoexEcgVFXGXio27bwyAJ6Hrsdsg1vXs6sV577wF236XotkNvWaWkgr7ZzKRK2ePCtEZYZmHtSiZ1T6KeuwYVW7WoEZPvEE29QUYPyRSjU57Hxtq9QaV8DjQzvfLPk1uoJTm9RtBxMDrAyjzv9FZVFQQETvHhhXKhzGfM4Roqmc8hQF3HbDrsiuCdUknoe7mWmzGAUsHdEnWCQFdYKwk7Jzq3FYMmbyWbnaTxv5hMCjqUATHAfegF2A42LXxZ4YYwmW6XyJwhjJ886fFG21RNsWFe8B5wxsZBXtdW8RYfRy",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### initiator <--- (2018-10-16 20:26:05.669)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmNTRCfzVYr3HR58jh6r9abTxiiem2kgvWZGhQHxowJ8opMaBLoexEcgVFXGXio27bwyAJ6Hrsdsg1vXs6sV577wF236XotkNvWaWkgr7ZzKRK2ePCtEZYZmHtSiZ1T6KeuwYVW7WoEZPvEE29QUYPyRSjU57Hxtq9QaV8DjQzvfLPk1uoJTm9RtBxMDrAyjzv9FZVFQQETvHhhXKhzGfM4Roqmc8hQF3HbDrsiuCdUknoe7mWmzGAUsHdEnWCQFdYKwk7Jzq3FYMmbyWbnaTxv5hMCjqUATHAfegF2A42LXxZ4YYwmW6XyJwhjJ886fFG21RNsWFe8B5wxsZBXtdW8RYfRy",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### initiator: (2018-10-16 20:26:05.801)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-16 20:26:05.801)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-16 20:26:05.801)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-16 20:26:05.801)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-16 20:26:05.801)
> Channel is `open` and ready to use

#### responder: (2018-10-16 20:26:05.801)
> Channel is `open` and ready to use

#### initiator <--- (2018-10-16 20:26:05.832)
```javascript
{
  "id": -576460752303423429,
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

#### initiator ---> (2018-10-16 20:26:05.833)
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

#### initiator <--- (2018-10-16 20:26:05.839)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQNuc5m2hkM1JhuZ3tq2PQHgok4aXmv3fn5juCtmGszeBnPAfUfpfPBEYT6C6vWrkQAq18h2dVRDp4Kr6yBJLT5yYvomeqUG1zjytuuKVdfwyrcWgAjnXJgocHd1tNAHgKnQZ4pqCk1QwnriT1m4YRvEF4LmCuJHyRQFCUdQfvS88ycbHTsPXXpQfDCM7oHJYSYGdeXrp6wEj2"
  }
}
```

#### initiator ---> (2018-10-16 20:26:05.840)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak566AmcfAUNSfNp2jBpD5QAvyeKUri9xXEyphBMHWb52Z4KqRDEeGQHGRjDY52BfCCuzjhVno9i42mXqdQyssHfzNfPYPVfihC9GG2bKDEgVFVD1bF7kjGwExeQrLkq1z2v9VMJpp1h2WcCfpZc9BbfMfhvLjTK6oM2rZHRbtYb8qZq5RuCEprmiDyeNHBNZ5dYvucHhc4Lo7jp8FcoWTNFRFuFiSoTo2Vzg13nUfK325XFeWYgDzdHJ4YgvfEDBvuXp3MC5zqF54WhKjXbGuRnWMwwgxToiywfvRiy2kxSJJinP"
  }
}
```

#### responder <--- (2018-10-16 20:26:05.847)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### responder <--- (2018-10-16 20:26:05.847)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQNuc5m2hkM1JhuZ3tq2PQHgok4aXmv3fn5juCtmGszeBnPAfUfpfPBEYT6C6vWrkQAq18h2dVRDp4Kr6yBJLT5yYvomeqUG1zjytuuKVdfwyrcWgAjnXJgocHd1tNAHgKnQZ4pqCk1QwnriT1m4YRvEF4LmCuJHyRQFCUdQfvS88ycbHTsPXXpQfDCM7oHJYSYGdeXrp6wEj2"
  }
}
```

#### responder ---> (2018-10-16 20:26:05.849)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4wQnzXQmjXxUSS7H6AznbZ1BJmJHdefa4KjLwKLzTEtzPab7ayFjE4hJDSg1mAZQa7fEoExVDyeqTVD5UxtVmrCTi6iuCgY1iZ3wQ564gAe171iRzRYcJ4WQWR74sQe5VYTGrcfRUSQLM1m7VAagCZkW5fqxbAp8quh5X1TqD5ohwm9QVYr89cXAULV7yveJTSn8CCYAxLohT2gqHcKM3pwdosiWgFWwuCn52s3eWYXdpirX5b8MQRkqxqU393LFh8gc19ynN2GYBd2dQxaof5gS5eV3UhNPe9gVgoLeuu5gcqQ"
  }
}
```

#### responder <--- (2018-10-16 20:26:05.855)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDke6yRmg2K4vmNcdhT6TepgxeBDmgGeT73fMe85cvM4xpvqDkGSL3jZVVwP4Q8DqjjTq2XVUMS8VsTBEAAJR8NPsa9hdaKh6abfiiuwmhbdgL485gD1Sg6pNKAKMY7DLd3MVDsCKDzmk88KSur5JMrViVqSBqB9MUm5F1eb4NKo5iFC73jNgQBaSEYB59smBq7diGSkmfSDzVVCNedUW7ZLyUPzJ5ZRgRULHMe4RuDtZqDxjKkYehpqLnWPbZkkjpfpWfJfnRBdL6BTPBnKp9FVHTfpPK66AjBWn6ASz3h7dTXfs1VvFwWzBUrwLQYSPyxEv2Sjmz3E5d5rM4xGt5PXs7HEDCNVbBhzrYDm7ZVhhJ8PT6FUNJ5He9nEyfCy7CcTEH6UqN7",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### initiator <--- (2018-10-16 20:26:05.856)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDke6yRmg2K4vmNcdhT6TepgxeBDmgGeT73fMe85cvM4xpvqDkGSL3jZVVwP4Q8DqjjTq2XVUMS8VsTBEAAJR8NPsa9hdaKh6abfiiuwmhbdgL485gD1Sg6pNKAKMY7DLd3MVDsCKDzmk88KSur5JMrViVqSBqB9MUm5F1eb4NKo5iFC73jNgQBaSEYB59smBq7diGSkmfSDzVVCNedUW7ZLyUPzJ5ZRgRULHMe4RuDtZqDxjKkYehpqLnWPbZkkjpfpWfJfnRBdL6BTPBnKp9FVHTfpPK66AjBWn6ASz3h7dTXfs1VvFwWzBUrwLQYSPyxEv2Sjmz3E5d5rM4xGt5PXs7HEDCNVbBhzrYDm7ZVhhJ8PT6FUNJ5He9nEyfCy7CcTEH6UqN7",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### initiator <--- (2018-10-16 20:26:05.861)
```javascript
{
  "id": -576460752303423428,
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

#### initiator <--- (2018-10-16 20:26:05.862)
```javascript
{
  "id": -576460752303423427,
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

#### responder ---> (2018-10-16 20:26:05.862)
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

#### responder <--- (2018-10-16 20:26:05.866)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQNuc5m2hkM1JhuZ3tq2PQHgok4aXmv3fn5juCtmGszeBnPG5zXNCrNaGNrBe3QyhwJM6mJAWiStUFS42FHQ5YP8wUCGD8dkabUAyickfR8PvnFgSFoxEwPXmZeRGg5HnD2EH2mQ295AizWyP2MMD2FU4GjPWY4WSnf4X9XXz27T9ACBMm57gBwxvSdRMyAUSQ8sVPTLp4phKQ"
  }
}
```

#### responder ---> (2018-10-16 20:26:05.867)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak57CMQCd6m4RGX3NYVK3FE6La8ED4nnaEoU39csUFvVZEumJd1TTdHdiDcipRiQsPrpiFm6kvfzdaaS5Tu17wK7Uzbowi3tpgV5FARMbdsRHYWj8guwwta7fWM75WesotbYkahPaYc5kiZhdjjAunRswMbo47joU4pgxFPiKgLqGeHWEzmBxJj8XmouMNC6rjRvDaR1voq8zCNarGDnA9uBfeisXX67AG8dSU8d2NhqArT5VEnVhe2n4XcsXZdFE5GDf7VKW3tyF19JrsFR9RG775HQH7JguCnpZSDDo2A2GZhZe"
  }
}
```

#### initiator <--- (2018-10-16 20:26:05.871)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### initiator <--- (2018-10-16 20:26:05.871)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQNuc5m2hkM1JhuZ3tq2PQHgok4aXmv3fn5juCtmGszeBnPG5zXNCrNaGNrBe3QyhwJM6mJAWiStUFS42FHQ5YP8wUCGD8dkabUAyickfR8PvnFgSFoxEwPXmZeRGg5HnD2EH2mQ295AizWyP2MMD2FU4GjPWY4WSnf4X9XXz27T9ACBMm57gBwxvSdRMyAUSQ8sVPTLp4phKQ"
  }
}
```

#### initiator ---> (2018-10-16 20:26:05.872)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4zPMednLf5sK6kVXkyhcKnTBDrhpRQNSCyTGMMcAAZYBFRd1iQUPBzsp4PkT7A8De6xWFG4ugfk3g4qCK4qf9wHAQqmepGoh8rrkbgURs4PxQEdZjXSy2uJckXtgu7TKaWqhvA2mUfrLwdvrs8PA1HcKujCJWxQkJr4MRNBEEc8EkxV9ayLiUyb7DTS8L3BxnqLdH3BUXHPsQ9VaWJ8aPrBVLBqbmeyZX1wKP1uXR8bQsDu8aL5Uh2LRbciQHuE254YbMvuXx5gjipWgB5CJM6yceZpyQBgvqC48hnVWpiBR7y8"
  }
}
```

#### initiator <--- (2018-10-16 20:26:05.877)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkjDdzMbnKT7yVoK6Yi1WpVdamVAvf63ajrh63wNSwvcVjRqiGLF14WWqQRgorxcBooX6vGhprzmWh8xcT9JfGAG4wf7adz4RJ347SR4Vv2u68kp1RRVKaz1FyLoYzxhfiyBoTb3JHrocGNWYYwLXZSWz3tF4xafJiWv6ihwjbNxWRNbeDyU8X2oCAXXGDxdBLLh7P8uTihBi3zep88MMXyiu5JPYD9K7hawbMPvZT4AEhvs3AixurSSJSgGSzoe1J2G79FFjbVvkmhjAokN6krdfnyRj3Jn5a6HLCuR8QNutJ9cuAV9LjPGqt4GW6tisgGZ74DNd2yBVcm1vSh7PiXnzEcePpQQHUg3sMYFCGtgPnNh8aeNbYGG8YZdETpobkkvHd1QKh",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### responder <--- (2018-10-16 20:26:05.878)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkjDdzMbnKT7yVoK6Yi1WpVdamVAvf63ajrh63wNSwvcVjRqiGLF14WWqQRgorxcBooX6vGhprzmWh8xcT9JfGAG4wf7adz4RJ347SR4Vv2u68kp1RRVKaz1FyLoYzxhfiyBoTb3JHrocGNWYYwLXZSWz3tF4xafJiWv6ihwjbNxWRNbeDyU8X2oCAXXGDxdBLLh7P8uTihBi3zep88MMXyiu5JPYD9K7hawbMPvZT4AEhvs3AixurSSJSgGSzoe1J2G79FFjbVvkmhjAokN6krdfnyRj3Jn5a6HLCuR8QNutJ9cuAV9LjPGqt4GW6tisgGZ74DNd2yBVcm1vSh7PiXnzEcePpQQHUg3sMYFCGtgPnNh8aeNbYGG8YZdETpobkkvHd1QKh",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### initiator <--- (2018-10-16 20:26:05.881)
```javascript
{
  "id": -576460752303423426,
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

#### initiator <--- (2018-10-16 20:26:05.883)
```javascript
{
  "id": -576460752303423425,
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

#### responder ---> (2018-10-16 20:26:05.883)
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

#### responder <--- (2018-10-16 20:26:05.886)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQNuc5m2hkM1JhuZ3tq2PQHgok4aXmv3fn5juCtmGszeBnPMWWNukKZuzJcBBAK6Yw5edVrc5nRaNNr6usCsqE7tYVgXdFJbwr87isiCNCsB1swKPtK1ZNGnPVvqrNnYerxEQLzLt4ejSQCLsGjiASk4KX3452qnUAUNxmAWm6hAtPBBn3YpbzaiXUY7GDh895J9KzJiWxotV5"
  }
}
```

#### responder ---> (2018-10-16 20:26:05.887)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak591W4eFZEWev1qech5qn9mygMQ9U5E3EfMXvbzxWQWdjVjz47DbnZj1vjkXy8BWTKHjQt3tiXcgmfQqaDH18Uk4SrVFJoe8YhvLTYp8xBenxu8Ck7AnJ8haYbGEfTUoF6zdH49XokVWQtXC4Xowfr6DA3BmM49AbcbT2EvmivYMdRq9c96Amo4BnADdyWBppTNsWEEt31ELSRzvyd9o2sWWecmjxEkxnrJW6AQcnFUM5vD1ViASLzy8G9GZDsVXLT4mCNcKAKqxw8hc2BhHoSs8mRMFNAUGc2cXek4sKnxS197j"
  }
}
```

#### initiator <--- (2018-10-16 20:26:05.892)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### initiator <--- (2018-10-16 20:26:05.892)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQNuc5m2hkM1JhuZ3tq2PQHgok4aXmv3fn5juCtmGszeBnPMWWNukKZuzJcBBAK6Yw5edVrc5nRaNNr6usCsqE7tYVgXdFJbwr87isiCNCsB1swKPtK1ZNGnPVvqrNnYerxEQLzLt4ejSQCLsGjiASk4KX3452qnUAUNxmAWm6hAtPBBn3YpbzaiXUY7GDh895J9KzJiWxotV5"
  }
}
```

#### initiator ---> (2018-10-16 20:26:05.893)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak54VYxaDvXrpH5ubPQMto2rNWUuPFUHi9gyVs7kJH4jRpaT9uiJ18D7divV1sUgwt6AFDj7bzMZm2rbkAo2NGutwB4jhbLCL94ecr2n7F7ARnMYsMYAeXbwwirLCBoksshVEN1x5CeVRaaMpM9CQvY3xNavuk8ky6wohvtaKZZn3Ha7WsiYn6CgMzEozUMSs7xa8dQGKmXVkbhu666kdfPM1zDLSmGDfRnJGyfgsXrumfFmPUQsJ2geq6onuqTzrcNyYSf8ASwpK9jhtSjHQTpZHz63MgcbhKozCb7fgXLXTU1ee"
  }
}
```

#### initiator <--- (2018-10-16 20:26:05.898)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkrH8pr6ysUGs3su3ZdVoXHArYCBsANLcBUMcy8gssHsMjQPxtf5LLHL9GACwwwH7WUbbHzTzH7zhjiGLrBowcq26ZYA5cGwpXaqysiJuWHsBWKkn6rjDP52R8TvWJJjtmcsr13RsZnL4B9YhNuExME8monGtKAZpgZuD2WUrTPRLehAanEM93cnfRLuU3QRdUNLtFh1za29L7rGtTLiAwT7iJVsPKZeuLCsybEU4U8xxRok8AEviDQmNeR8uRrYEn8yBjkgMQUYdubwkkGsyYfLhtBXHeAFrntyr4hkqfhdgQa9qLyHfr7igNgGek8txhWvjTLVLEVqhrJd7stRuiWxzmYGxxz6g3Hm4ySWzM5S8WVvyxgtQCSmGemhVw1LdV2nKoT4ee",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### responder <--- (2018-10-16 20:26:05.898)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkrH8pr6ysUGs3su3ZdVoXHArYCBsANLcBUMcy8gssHsMjQPxtf5LLHL9GACwwwH7WUbbHzTzH7zhjiGLrBowcq26ZYA5cGwpXaqysiJuWHsBWKkn6rjDP52R8TvWJJjtmcsr13RsZnL4B9YhNuExME8monGtKAZpgZuD2WUrTPRLehAanEM93cnfRLuU3QRdUNLtFh1za29L7rGtTLiAwT7iJVsPKZeuLCsybEU4U8xxRok8AEviDQmNeR8uRrYEn8yBjkgMQUYdubwkkGsyYfLhtBXHeAFrntyr4hkqfhdgQa9qLyHfr7igNgGek8txhWvjTLVLEVqhrJd7stRuiWxzmYGxxz6g3Hm4ySWzM5S8WVvyxgtQCSmGemhVw1LdV2nKoT4ee",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### initiator <--- (2018-10-16 20:26:05.902)
```javascript
{
  "id": -576460752303423424,
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

#### initiator <--- (2018-10-16 20:26:05.904)
```javascript
{
  "id": -576460752303423423,
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

#### initiator ---> (2018-10-16 20:26:05.904)
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

#### initiator <--- (2018-10-16 20:26:05.908)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQNuc5m2hkM1JhuZ3tq2PQHgok4aXmv3fn5juCtmGszeBnPSw2ETHnmFiENAiHDDHPWjbLNMLhMHWSZzmpwjbWJEN1GZuBUp7khp8PBebztHF9fRZ4ExUbLZU6UHdUJ4JHaQw1VfnWk761tpukv9QhQ12oFkoyAGXgESazPjKH7Hq4Nn3t8oGSi6BAtSRpjhkkice1XUyRwKVi"
  }
}
```

#### initiator ---> (2018-10-16 20:26:05.909)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak55v8zVU6Lpv1f9yXvLdTh74WuAcc58zigA1NZcgYE7hcv7BXhsrs3P9tbDvVDs9wZQRXPkaJApTYwcepp2wBDyLD6MU5xJ3B11vkfLaJu4N69vtsQNexb7N6Jub5vtccbwEwyjedp1FM8Q2hn6zNbkBq9k1v7zW6u8UuzQmAHxHaby44S78xDvftWpS9VqL2azHP83TBJ8N5uZm5zkc63p3QZibXjauovPAzD6MY4DBuRuoMgQR3QXRsax6qXdPFDgpdpKh8koRWMt4ko7Xd5Z87goebH8w5hMm8BuEKffw87ec"
  }
}
```

#### responder <--- (2018-10-16 20:26:05.939)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### responder <--- (2018-10-16 20:26:05.940)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQNuc5m2hkM1JhuZ3tq2PQHgok4aXmv3fn5juCtmGszeBnPSw2ETHnmFiENAiHDDHPWjbLNMLhMHWSZzmpwjbWJEN1GZuBUp7khp8PBebztHF9fRZ4ExUbLZU6UHdUJ4JHaQw1VfnWk761tpukv9QhQ12oFkoyAGXgESazPjKH7Hq4Nn3t8oGSi6BAtSRpjhkkice1XUyRwKVi"
  }
}
```

#### responder ---> (2018-10-16 20:26:05.941)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4yjCAySyB7DMhesrwne673zw6bdXzDXLUGGBeg4MSaue6hbfcmkMqVecpcksU896uj6SGvn1rBtRtiwCNV7mWGGFqskwoQ7zjudWGLEQxiZxdoBbBFuRmNs87GS5pD9i8sxn1vGSkgMEm29iLgCbFRhg2Q97Zw6AHB6KBjVqYnkD3qqL5xgtY5er484yZxi4sBX5Mi2GRxjSQVopPWkVxcEszMzY5hweCBSY341BDSPnbG3XdMiMfDp6vRNRZwDVnawBpWW4CSih6RfDNW2Z9sCmHvZovBmdQgZ32y8iSAEXhit"
  }
}
```

#### responder <--- (2018-10-16 20:26:05.946)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDki62ej99qcizHiPa1rVsXDLZA5aFWJySohKv3kpgazuLUprYZDXKwajYf7LxNBMTZ5Gg6G1fLXLBYVErDNbMwqtRePSXGHtRuBJu16TUEyCdJkBfLGTJjJPCpBZBhmQQKaPPwdC75T27gVn36BQpuYhJqSBtzfyHQEGeKcje8bhciUEqbYJRJ4LF4eEnTP1UCvFmHAceoaw1rC8NDa7dyw41aFuR41ANere7k9LKJJSHuVPyYJ8yeikqoXMasPvYx98AmFVuJTjVyCZP54cJrm4EKk64C4XbAytzF7tfcdbScWWDcEdx6N4NXhBxQdbetbdudFotmWKsjVdt4VMHXnBMwayXZo5RBFcs9xfqwhj2z7x7uax6k6TSukMrMDD1k2tQQswFN",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### initiator <--- (2018-10-16 20:26:05.946)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDki62ej99qcizHiPa1rVsXDLZA5aFWJySohKv3kpgazuLUprYZDXKwajYf7LxNBMTZ5Gg6G1fLXLBYVErDNbMwqtRePSXGHtRuBJu16TUEyCdJkBfLGTJjJPCpBZBhmQQKaPPwdC75T27gVn36BQpuYhJqSBtzfyHQEGeKcje8bhciUEqbYJRJ4LF4eEnTP1UCvFmHAceoaw1rC8NDa7dyw41aFuR41ANere7k9LKJJSHuVPyYJ8yeikqoXMasPvYx98AmFVuJTjVyCZP54cJrm4EKk64C4XbAytzF7tfcdbScWWDcEdx6N4NXhBxQdbetbdudFotmWKsjVdt4VMHXnBMwayXZo5RBFcs9xfqwhj2z7x7uax6k6TSukMrMDD1k2tQQswFN",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### initiator <--- (2018-10-16 20:26:05.950)
```javascript
{
  "id": -576460752303423422,
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

#### initiator <--- (2018-10-16 20:26:05.952)
```javascript
{
  "id": -576460752303423421,
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

#### responder ---> (2018-10-16 20:26:05.952)
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

#### responder <--- (2018-10-16 20:26:05.955)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQNuc5m2hkM1JhuZ3tq2PQHgok4aXmv3fn5juCtmGszeBnPYMY5zqFxbSA8AFQ7LEveFgxyVDvNxAdgCh73qLbbPkYf4TUeJgMS1DBu5mnLjC5JbK9K8CE3HdNVh1nD4QApEeySEbuorsDZ5qmWS5HjEr1eP9FWDDvmT4vVyg7otQ81W6ZCH2XRaxtLXCCdYof7CKvgPRuTQ36"
  }
}
```

#### responder ---> (2018-10-16 20:26:05.956)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4pHtAS4Mdo4pX6Q8ton2SJjvcakn5mvNRirNVorE2q4n3WwPmK24Un3q3zYkNLQ9y4vD3P2DY3a672srVyd5GvF8Pfvk4xmpMP3wftCoR2bJkhKHaW6sVTVptPD2bfx44Jae5CtcZ6J1u95Pzak7VqZiBCMBF73HX3UhdHv3wdpyw3aUrjUkYhNB7abudNPS6yJ1QaHLA7kBjEg37qHxn7FkceboXwwgjAkvnTTYsjjDDY8uLbsBejJLzRGjRnBBAxDQCLc8hpvU83F7fVDG5zjnGVfRuWEnXXNkUVaLBeL9ubF"
  }
}
```

#### initiator <--- (2018-10-16 20:26:05.995)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### initiator <--- (2018-10-16 20:26:05.997)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQNuc5m2hkM1JhuZ3tq2PQHgok4aXmv3fn5juCtmGszeBnPYMY5zqFxbSA8AFQ7LEveFgxyVDvNxAdgCh73qLbbPkYf4TUeJgMS1DBu5mnLjC5JbK9K8CE3HdNVh1nD4QApEeySEbuorsDZ5qmWS5HjEr1eP9FWDDvmT4vVyg7otQ81W6ZCH2XRaxtLXCCdYof7CKvgPRuTQ36"
  }
}
```

#### initiator ---> (2018-10-16 20:26:05.999)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4jiyY9bC1XUbHip5KyYd2fY625JJGFWgCkBVXZaz8E36gTNMFTeUwbtB2775kt1EctP9bzDhzvmVqdRfidkuB31DeyTY1V1QF3QpyLCLAEkvZA48v3wDfaKa7Xs8TKHdv5Rej85Ud4eTh3FSPgtgA1TBxbfz7B5Ghek76w2653ofeVpzPdeL4F75opyKqqFBn1w8DAN3RUxQyrux5YqjRdQZNdjaMafzq31ET1ydMYuz6pYSjku1atUU4QFBU7AZmkMwp82WNVscNGqTxbPDP4YByryLRiq9HdyxbTpQSggTCNJ"
  }
}
```

#### initiator <--- (2018-10-16 20:26:06.16)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkJ1gztpbtuQJduA7b1NVcBchkz5xrPCu4trPKuuFAY8gQZNVc2aL7U26i7nis7hkkCp5wGiih5N9GUHQ5rGY1haQ9HYAV3C4AJS8XPooqVFEL5QmdxqAtrC4S5zVrZzGWKGzfyiyffXGAFbZhLiSWRuy4K9GqPcxzE9pg24wBhQZBpnrWtko9VyUSCkL3aYAWLjcqPpvMKUPhDTad9SsbFVqVdiYZGULveSQhfAwhyhUc4un7R7R1hSn5Q7dtmKyrCTV8HC7Hx24PU5KztDRqNCPEF7ijEvZc3dJ1EcCuQzamvn8DRFFnyGhstnk4y5eBd3KsZzGhgv6t9WKK6S4gKrbxaDAanmhc5Fa2RZbgLURjqTPej14WUBP6d5ztrw2HpGNv98Ey",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### responder <--- (2018-10-16 20:26:06.19)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkJ1gztpbtuQJduA7b1NVcBchkz5xrPCu4trPKuuFAY8gQZNVc2aL7U26i7nis7hkkCp5wGiih5N9GUHQ5rGY1haQ9HYAV3C4AJS8XPooqVFEL5QmdxqAtrC4S5zVrZzGWKGzfyiyffXGAFbZhLiSWRuy4K9GqPcxzE9pg24wBhQZBpnrWtko9VyUSCkL3aYAWLjcqPpvMKUPhDTad9SsbFVqVdiYZGULveSQhfAwhyhUc4un7R7R1hSn5Q7dtmKyrCTV8HC7Hx24PU5KztDRqNCPEF7ijEvZc3dJ1EcCuQzamvn8DRFFnyGhstnk4y5eBd3KsZzGhgv6t9WKK6S4gKrbxaDAanmhc5Fa2RZbgLURjqTPej14WUBP6d5ztrw2HpGNv98Ey",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### initiator <--- (2018-10-16 20:26:06.29)
```javascript
{
  "id": -576460752303423420,
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

#### responder ---> (2018-10-16 20:26:06.121)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

#### responder <--- (2018-10-16 20:26:06.129)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "tx": "tx_2C9es4FjHqioTVcBWiaXnP7vv2DfQycNC8ZCscUWVLmf5EnYCagBUotHmNTa35RquJfz9yJ7wuGrSsEpawYTxBZc6dz4FXDX4MNM7rbGTbHPyciu16wSocDNbvJZRutHqfVEVAYTPCj7HmgNruz4ifmkjXsFLv"
  }
}
```

#### responder ---> (2018-10-16 20:26:06.131)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "tx": "tx_2WsEQsiC5Xsnt1fJgkG4aCwQwyAtX3UsXEtBgLBHJzoksT6Jdb1c44PDRJxcdjrHfhNaD5CSGzYKKgjLzSgjjpafDyC2zKrY7cVQSkDTJvgVQmhccvXqhsrdjpX4gsHM8e8fA1vMKcZMpUTzPVz6uZVKf7nQ48MqHLsPr4JHEgU8HvsqM5TdbShxtN1itcoeFsZcxJaS92eVqcg91vBQBQD2deWeKczdxm9kVaHoUUz52p7MkKGh91XQbYvwbsKFQxM"
  }
}
```

#### initiator <--- (2018-10-16 20:26:06.133)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "deposit_created",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### initiator <--- (2018-10-16 20:26:06.133)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "tx": "tx_2C9es4FjHqioTVcBWiaXnP7vv2DfQycNC8ZCscUWVLmf5EnYCagBUotHmNTa35RquJfz9yJ7wuGrSsEpawYTxBZc6dz4FXDX4MNM7rbGTbHPyciu16wSocDNbvJZRutHqfVEVAYTPCj7HmgNruz4ifmkjXsFLv"
  }
}
```

#### initiator ---> (2018-10-16 20:26:06.135)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "tx": "tx_2WsEQsiC5XsmfGUsvaXqtdudz2SKG2LseY3sitjxadTig95BcLXAEzrTHj7x9dgiuUtst8FAYxM5S3sgHK7ZrddvYhKp3EY3K2xtGStmft2MZBEzoW9aTJi1dJE9HxRX6yWw6MP2NhZ6SK6mdRGqTJU55dLYW5GjCL85yhF83F9FqMexiAmy4quQjmEJN6B8Fm1EVxNvpaQgQSrkLQp5ybxyVGwnXHusrW6tfW1kWdHBk5A7bqL4swx3A8iXFzX7wRE"
  }
}
```

#### initiator <--- (2018-10-16 20:26:06.137)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3cDMp6242sBy9f6N4na9pGxWMHzM8ZpTEhjMSG5935tTzXAaZ6qE86QJ1VgimTppVr9mHiLnwimsgUyBPnB5AQxaks3pDcMySoTuDcdE2jK87izUgqW4cf9k4w7RtRbKBGd8MeXPMcZMxce575PKuacG4TDx41jymWCw5oHWnvopS9RMwnfDrm4iXyEy1EZYWKVdMFTBgrCXmC1tfv23ocKHJYwuM4Xd8UpRBmJbErot1cnMgyEw57UnvBtin2sESrpe8fwdTH6dq92RBZf3rk523Wskm4rxvEdTNv2CJgXptDRFdtAW6nwXZD5KNVLftUMMu3DRYdXRJxSEQaXHq2J36bpiN",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### responder <--- (2018-10-16 20:26:06.138)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3cDMp6242sBy9f6N4na9pGxWMHzM8ZpTEhjMSG5935tTzXAaZ6qE86QJ1VgimTppVr9mHiLnwimsgUyBPnB5AQxaks3pDcMySoTuDcdE2jK87izUgqW4cf9k4w7RtRbKBGd8MeXPMcZMxce575PKuacG4TDx41jymWCw5oHWnvopS9RMwnfDrm4iXyEy1EZYWKVdMFTBgrCXmC1tfv23ocKHJYwuM4Xd8UpRBmJbErot1cnMgyEw57UnvBtin2sESrpe8fwdTH6dq92RBZf3rk523Wskm4rxvEdTNv2CJgXptDRFdtAW6nwXZD5KNVLftUMMu3DRYdXRJxSEQaXHq2J36bpiN",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### initiator <--- (2018-10-16 20:26:08.24)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_deposit_locked",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### responder <--- (2018-10-16 20:26:08.25)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_deposit_locked",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### responder <--- (2018-10-16 20:26:08.25)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "deposit_locked",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### initiator <--- (2018-10-16 20:26:08.26)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "deposit_locked",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### responder <--- (2018-10-16 20:26:08.30)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3cDMp6242sBy9f6N4na9pGxWMHzM8ZpTEhjMSG5935tTzXAaZ6qE86QJ1VgimTppVr9mHiLnwimsgUyBPnB5AQxaks3pDcMySoTuDcdE2jK87izUgqW4cf9k4w7RtRbKBGd8MeXPMcZMxce575PKuacG4TDx41jymWCw5oHWnvopS9RMwnfDrm4iXyEy1EZYWKVdMFTBgrCXmC1tfv23ocKHJYwuM4Xd8UpRBmJbErot1cnMgyEw57UnvBtin2sESrpe8fwdTH6dq92RBZf3rk523Wskm4rxvEdTNv2CJgXptDRFdtAW6nwXZD5KNVLftUMMu3DRYdXRJxSEQaXHq2J36bpiN",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```

#### initiator <--- (2018-10-16 20:26:08.30)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3cDMp6242sBy9f6N4na9pGxWMHzM8ZpTEhjMSG5935tTzXAaZ6qE86QJ1VgimTppVr9mHiLnwimsgUyBPnB5AQxaks3pDcMySoTuDcdE2jK87izUgqW4cf9k4w7RtRbKBGd8MeXPMcZMxce575PKuacG4TDx41jymWCw5oHWnvopS9RMwnfDrm4iXyEy1EZYWKVdMFTBgrCXmC1tfv23ocKHJYwuM4Xd8UpRBmJbErot1cnMgyEw57UnvBtin2sESrpe8fwdTH6dq92RBZf3rk523Wskm4rxvEdTNv2CJgXptDRFdtAW6nwXZD5KNVLftUMMu3DRYdXRJxSEQaXHq2J36bpiN",
    "channel_id": "ch_TPt96dM914RTze8orjMHrUDMmewECfBoozggzgsUohNbWhs3m"
  }
}
```
