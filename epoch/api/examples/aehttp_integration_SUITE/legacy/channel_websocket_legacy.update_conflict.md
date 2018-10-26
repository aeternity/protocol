
#### initiator init (2018-10-24 12:59:39.414)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=initiator
```

#### responder init (2018-10-24 12:59:39.417)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=responder
```

#### responder <--- (2018-10-24 12:59:40.422)
```javascript
{
  "action": "info",
  "payload": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-24 12:59:40.424)
```javascript
{
  "action": "info",
  "payload": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-24 12:59:40.429)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_3d11KjpALm3t32sAMLL9Y5p9SUg9j82o5Er3hc4WTAmdXk3cXjxDydY4eoq6STXDutDQ59tM59bMr9CogemLkb4tUXrrZYvPc4DkdzkXhqGZjnzLVRAYpjMHXUeVmmqr9Fk96GrERRgHqJTaNp7wfhyEnqvb1nHjTwbGis"
  },
  "tag": "initiator_sign"
}
```

#### initiator ---> (2018-10-24 12:59:40.452)
```javascript
{
  "action": "initiator_sign",
  "payload": {
    "tx": "tx_4L9GSozvM4Hmvwb56638RWJ4V3hDwh1A2hiNAYkFUJtA39uL6AKcfgcPo6ZKkRUtFupsRFUbAaGxU3uEf5ZSpxkrrr9WarF3a17Uao6YxCazBV3Sqa5WctSCUoAK9zF9CQGi4mfUBcaLidVcbuj459wy9GKYBc7A1XmTLWU9rdxMKn7iTSQ1WnnNsJYTFrY4TkJaxzyKEPjWDDfHxrFcKYphhdoxVBPM3P51RbZhFTCQJJwAW3rCDfNc8dHxNLVRSbVowT4wT3w"
  }
}
```

#### responder <--- (2018-10-24 12:59:40.453)
```javascript
{
  "action": "info",
  "payload": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-24 12:59:40.453)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_3d11KjpALm3t32sAMLL9Y5p9SUg9j82o5Er3hc4WTAmdXk3cXjxDydY4eoq6STXDutDQ59tM59bMr9CogemLkb4tUXrrZYvPc4DkdzkXhqGZjnzLVRAYpjMHXUeVmmqr9Fk96GrERRgHqJTaNp7wfhyEnqvb1nHjTwbGis"
  },
  "tag": "responder_sign"
}
```

#### responder ---> (2018-10-24 12:59:40.454)
```javascript
{
  "action": "responder_sign",
  "payload": {
    "tx": "tx_4L9GSozvM4Hkb3Jv5Bz6jiyTsfazUJgDjmR3s3yunuTzueBJaXGa89Bz6VtBLYcmifwg2kQpFhih36KrUtGJuE3ef4BjvqB4WinkhPpeAkARQjz29TJi7bUEhh2rc8kmEZZ7qQd3eB4NXCY6kmWxe5wChH6SWHufndJTuMyWLuKFbPg9RodWmhfMxTg94gzNcKi1KSqdMGxGcHCAaJhBTWftzRFw7wnDCTbHkbHiRwGFnjY8VbDiArQ6D7HAdToPKrm6LRgP2C3"
  }
}
```

#### initiator <--- (2018-10-24 12:59:40.455)
```javascript
{
  "action": "info",
  "payload": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-24 12:59:40.456)
```javascript
{
  "action": "on_chain_tx",
  "payload": {
    "tx": "tx_6jPYBUFTkcmPDX6L26hvU7pCpJiiHB8hma1MKQbXUXZ7riqiTNyBrPxeQf9BubS2UhafR2Yzvk4heM15G4b8YrvEX4V5oX1QhZe9b48CGDrMrEYQGwQusot6WkE6bjSwtmSBHrbvgJUtNvdV6CcdVVVWwTgUrTfs6x9Px7bAnhJMx7PNUyAsLcnYHzpQWFPpARwNvi6VPm9KE13SFPgeRTW4q99sejq7fG714FnY1tY8cxcevSJi4NM1xknD97zX9N4KDL1HhS4zrX2GT9C4FUEwqP4vxsxPmK35Sg1zd1TjZBggJZxaPrFFVdQBLYY2DtCLEzYdZYk8SJsqnT7GPrzqcVpVLa3rea7dM"
  }
}
```

#### initiator <--- (2018-10-24 12:59:40.457)
```javascript
{
  "action": "on_chain_tx",
  "payload": {
    "tx": "tx_6jPYBUFTkcmPDX6L26hvU7pCpJiiHB8hma1MKQbXUXZ7riqiTNyBrPxeQf9BubS2UhafR2Yzvk4heM15G4b8YrvEX4V5oX1QhZe9b48CGDrMrEYQGwQusot6WkE6bjSwtmSBHrbvgJUtNvdV6CcdVVVWwTgUrTfs6x9Px7bAnhJMx7PNUyAsLcnYHzpQWFPpARwNvi6VPm9KE13SFPgeRTW4q99sejq7fG714FnY1tY8cxcevSJi4NM1xknD97zX9N4KDL1HhS4zrX2GT9C4FUEwqP4vxsxPmK35Sg1zd1TjZBggJZxaPrFFVdQBLYY2DtCLEzYdZYk8SJsqnT7GPrzqcVpVLa3rea7dM"
  }
}
```

#### initiator ---> (2018-10-24 12:59:42.855)
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

#### initiator <--- (2018-10-24 12:59:42.857)
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

#### initiator <--- (2018-10-24 12:59:44.839)
```javascript
{
  "action": "info",
  "channel_id": "ch_vmfxDKeX8d2MZdhDtJ8rA9QPCneDmGNENrsCzezskmNadvZbu",
  "payload": {
    "event": "own_funding_locked"
  }
}
```

#### responder <--- (2018-10-24 12:59:44.839)
```javascript
{
  "action": "info",
  "channel_id": "ch_vmfxDKeX8d2MZdhDtJ8rA9QPCneDmGNENrsCzezskmNadvZbu",
  "payload": {
    "event": "own_funding_locked"
  }
}
```

#### responder <--- (2018-10-24 12:59:44.839)
```javascript
{
  "action": "info",
  "channel_id": "ch_vmfxDKeX8d2MZdhDtJ8rA9QPCneDmGNENrsCzezskmNadvZbu",
  "payload": {
    "event": "funding_locked"
  }
}
```

#### initiator <--- (2018-10-24 12:59:44.839)
```javascript
{
  "action": "info",
  "channel_id": "ch_vmfxDKeX8d2MZdhDtJ8rA9QPCneDmGNENrsCzezskmNadvZbu",
  "payload": {
    "event": "funding_locked"
  }
}
```

#### initiator <--- (2018-10-24 12:59:44.842)
```javascript
{
  "action": "info",
  "channel_id": "ch_vmfxDKeX8d2MZdhDtJ8rA9QPCneDmGNENrsCzezskmNadvZbu",
  "payload": {
    "event": "open"
  }
}
```

#### responder <--- (2018-10-24 12:59:44.842)
```javascript
{
  "action": "info",
  "channel_id": "ch_vmfxDKeX8d2MZdhDtJ8rA9QPCneDmGNENrsCzezskmNadvZbu",
  "payload": {
    "event": "open"
  }
}
```

#### initiator <--- (2018-10-24 12:59:44.843)
```javascript
{
  "action": "update",
  "channel_id": "ch_vmfxDKeX8d2MZdhDtJ8rA9QPCneDmGNENrsCzezskmNadvZbu",
  "payload": {
    "state": "tx_6jPYBUFTkcmPDX6L26hvU7pCpJiiHB8hma1MKQbXUXZ7riqiTNyBrPxeQf9BubS2UhafR2Yzvk4heM15G4b8YrvEX4V5oX1QhZe9b48CGDrMrEYQGwQusot6WkE6bjSwtmSBHrbvgJUtNvdV6CcdVVVWwTgUrTfs6x9Px7bAnhJMx7PNUyAsLcnYHzpQWFPpARwNvi6VPm9KE13SFPgeRTW4q99sejq7fG714FnY1tY8cxcevSJi4NM1xknD97zX9N4KDL1HhS4zrX2GT9C4FUEwqP4vxsxPmK35Sg1zd1TjZBggJZxaPrFFVdQBLYY2DtCLEzYdZYk8SJsqnT7GPrzqcVpVLa3rea7dM"
  }
}
```

#### responder <--- (2018-10-24 12:59:44.843)
```javascript
{
  "action": "update",
  "channel_id": "ch_vmfxDKeX8d2MZdhDtJ8rA9QPCneDmGNENrsCzezskmNadvZbu",
  "payload": {
    "state": "tx_6jPYBUFTkcmPDX6L26hvU7pCpJiiHB8hma1MKQbXUXZ7riqiTNyBrPxeQf9BubS2UhafR2Yzvk4heM15G4b8YrvEX4V5oX1QhZe9b48CGDrMrEYQGwQusot6WkE6bjSwtmSBHrbvgJUtNvdV6CcdVVVWwTgUrTfs6x9Px7bAnhJMx7PNUyAsLcnYHzpQWFPpARwNvi6VPm9KE13SFPgeRTW4q99sejq7fG714FnY1tY8cxcevSJi4NM1xknD97zX9N4KDL1HhS4zrX2GT9C4FUEwqP4vxsxPmK35Sg1zd1TjZBggJZxaPrFFVdQBLYY2DtCLEzYdZYk8SJsqnT7GPrzqcVpVLa3rea7dM"
  }
}
```

#### initiator: (2018-10-24 12:59:45.36)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-24 12:59:45.36)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-24 12:59:45.37)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-24 12:59:45.37)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-24 12:59:45.37)
> Channel is `open` and ready to use

#### responder: (2018-10-24 12:59:45.37)
> Channel is `open` and ready to use

#### initiator ---> (2018-10-24 12:59:45.75)
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

#### responder ---> (2018-10-24 12:59:45.75)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 2,
    "from": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
    "to": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt"
  },
  "tag": "new"
}
```

#### responder <--- (2018-10-24 12:59:45.86)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQQdjheTuKnUfzG54TbMzUVCr4edujGN19i8ikqzCbwCMTEUv8GBqoz7AnMTvT8rCHoG637pV5aKC3FjJXNqKqweHb4H1hcg17sAWYPb5jN4CBnjiQkys3UfiRbWUrNFZFisbgMv9eLbhcxN7DTEU5bPiMfo1Y1UYeq9fz1PMFvxEEv6gX6toafNbuFP8M5fCR7RAadwssJQnw"
  },
  "tag": "update"
}
```

#### initiator <--- (2018-10-24 12:59:45.86)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQQdjheTuKnUfzG54TbMzUVCr4edujGN19i8ikqzCbwCMTEUv8GBqoz7AnMTvT8rCHoG637pV5aKC3FjJXNqKqweHb4H1hcg17sAWYPb5jN4CBnjiQkys3UfiRbWUrNFZFisbgMv9eLbhcxN7DTEU5bPiMfeQZmqAy5Qorg78QwnqRwHkG8871H6gERamLN9LyFN1Af3o79LrR"
  },
  "tag": "update"
}
```

#### initiator ---> (2018-10-24 12:59:45.89)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4qCHcRS4prMqqrP8uNEZHYwAkBwJLWakCSHs65F5nMuruV4CaNyzvECDKsr2cA2byWrUWCz8bJB7nXNXz6ntx81MteEGvBBfA6u7dCXmEeCDBrzvEdwrJMbNEjmyep1UWPbJ92fXDYWp8T6qEx6y8MGQ7rBs2U3Xgb4cPkzGf252StwEJ2huLhqU1KGfXACUDw8E5WQSeVoLDS2Fe2Xs28KisnoYhck6ndCyE5fU5SqpLuquvR6mzi11femnYCX1PHjFHbMTGjXbvvTaU1NwDvaUsGFXZuDiPNzQc8YCsH8D8z2"
  }
}
```

#### responder ---> (2018-10-24 12:59:45.89)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4rZFMHQZfHhfoCwG1SoQU3pgWVqTx5D9oQXzU9GsPQ1KSscYNkp6PXrLauWf4Y6dTLdKBXxQnfuAkq8zAe22hoYm8iDcZPDnxySK3oNcSKuTdmJTZZtuEuDYa1sfkTr5nyVxtEM6r1CzD73MJ5aPAER6HKJHWm4EMvRXVYKwjY9o9dVRH78nzvyGP72tGux9U6m5dCWtvzkUDD7gCdqny7MZX2yoYKFvGdf2E9CVtFFAntPMGMU5e5U47HsXHQppJndc3Hd1ji6Z57UQAqS8zGxugCsxJMPP2r5b2Un6AjCVxPi"
  }
}
```

#### initiator <--- (2018-10-24 12:59:45.92)
```javascript
{
  "action": "conflict",
  "channel_id": "ch_vmfxDKeX8d2MZdhDtJ8rA9QPCneDmGNENrsCzezskmNadvZbu",
  "payload": {
    "channel_id": "ch_vmfxDKeX8d2MZdhDtJ8rA9QPCneDmGNENrsCzezskmNadvZbu",
    "round": 1
  }
}
```

#### responder <--- (2018-10-24 12:59:45.92)
```javascript
{
  "action": "conflict",
  "channel_id": "ch_vmfxDKeX8d2MZdhDtJ8rA9QPCneDmGNENrsCzezskmNadvZbu",
  "payload": {
    "channel_id": "ch_vmfxDKeX8d2MZdhDtJ8rA9QPCneDmGNENrsCzezskmNadvZbu",
    "round": 1
  }
}
```

#### responder ---> (2018-10-24 12:59:45.92)
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

#### initiator ---> (2018-10-24 12:59:45.92)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 2,
    "from": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
    "to": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
  },
  "tag": "new"
}
```

#### initiator <--- (2018-10-24 12:59:45.97)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQQdjheTuKnUfzG54TbMzUVCr4edujGN19i8ikqzCbwCMTEUv8GBqoz7AnMTvT8rRn4KiHFpTNnzpFr1rZz9yQFzXxyoQsAzNkqGzdEzqRCwBM583x9JYLqujFRH3Chm7CzRqD41dkzkbucPwWALcpuc5t5Q3qsotYqaKsQvMfMhsZNtT4FWEEepLAzNLXD71WrRVz1xuxaunZ"
  },
  "tag": "update"
}
```

#### responder <--- (2018-10-24 12:59:45.97)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQQdjheTuKnUfzG54TbMzUVCr4edujGN19i8ikqzCbwCMTEUv8GBqoz7AnMTvT8rRn4KiHFpTNnzpFr1rZz9yQFzXxyoQsAzNkqGzdEzqRCwBM583x9JYLqujFRH3Chm7CzRqD41dkzkbucPwWALcpuc5t5FUUxMhXxDzRJ66YYixbaT7hTF7JUt8Qm6W2qsTwgsEQ2Gn3bvq9"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 12:59:45.99)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak54Duk2WpUP8EvjEr74FDrS65u7tXCcctBJLADDxBvt7eN6kCmHFPBAQKVby9VUj2tjaL8pkdvauSjMbefYihpbowzd7hxYj1wAHRs6ofBX3FmbfCoSKWQ9op5znNukv7Gpemw2HedPMHAURNEHtxJcgLMYHA1g3UhkuJux2KVxi3C58GoPnvZkYz2pFnkzpZVanBL1ZepZBT6kWaV96sMoYYHPargnXLfdBrRvokVvXbqy5yHNHDXPLgGbyy4RtAsEz21NnQWjgYN5E7ZUV54Q1tCYX3t7nJVhZC4XgZwGGhiYs"
  }
}
```

#### initiator ---> (2018-10-24 12:59:45.99)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4pixcqykdGzzWuHAhaLnf5zquH6vkoLHWf5QV1MBpsLRkJPWeBZ73G1t4uvarQkVCVmfxFDHC2uuPb98kDhfzUooKSAY8MCZLZvqWLQMNgWJvKEMPfooQs8xbbgUukNhpnWofbATP6RQWcK8HLiJDvR2Y7w3BnQQWpcFwRCWY1QBNwSrAQB7G2pNWdd5D5ttwjAc3s8Fo3E2HsRSDvABMEMUgYp66UD2asZRcXHNR4ihJFHNu2rnmP2WoHiU1XNyPqvfVYciPqwaM45nCtHypsCTW6jrUyvodiqHFTRNVkhuV8y"
  }
}
```

#### initiator <--- (2018-10-24 12:59:45.100)
```javascript
{
  "action": "conflict",
  "channel_id": "ch_vmfxDKeX8d2MZdhDtJ8rA9QPCneDmGNENrsCzezskmNadvZbu",
  "payload": {
    "channel_id": "ch_vmfxDKeX8d2MZdhDtJ8rA9QPCneDmGNENrsCzezskmNadvZbu",
    "round": 1
  }
}
```

#### responder <--- (2018-10-24 12:59:45.100)
```javascript
{
  "action": "conflict",
  "channel_id": "ch_vmfxDKeX8d2MZdhDtJ8rA9QPCneDmGNENrsCzezskmNadvZbu",
  "payload": {
    "channel_id": "ch_vmfxDKeX8d2MZdhDtJ8rA9QPCneDmGNENrsCzezskmNadvZbu",
    "round": 1
  }
}
```
