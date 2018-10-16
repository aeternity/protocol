
#### initiator init (2018-10-16 20:26:15.512)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A&role=initiator
```

#### responder init (2018-10-16 20:26:15.517)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A&role=responder
```

#### responder <--- (2018-10-16 20:26:16.518)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 20:26:16.521)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 20:26:16.530)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpALFUXGGsdug6Jrs56usDVK43SheHuLKP3h48aDzajQnhSXBUWq2rVDufMiousdvbextEcPQPuUq7817TtZyDq2vCt4rqTh3SqYy9jCHBN6SuCufA4j65Xrud4Spcwoi5gsMaowEXQETWMtFFZcbw7DeBpLA7gUF"
  }
}
```

#### initiator ---> (2018-10-16 20:26:16.564)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4Hp1nihLED1nmrXUKQZRgMYk6nTJewxe4MkLZ27L7ZGw8gCpwH3Hry4X3C1QnYckcg4HMroYtXFzxPvVsDetMQVMJtSrvbZnXkr8V5Zq8S7GhmDNmqKrwZRR99a6XzgTgCfk5mTEoa9C5AwYa5x8Ap7KoYWvC5xpiy79awrhLHutBGeJqrMWcCk8fCKeHTLUwn97sQyctxvAF9HoQGmLXARkzNEKEytXRAfgux2zf8oE1wZPVxFuCRSz23UzWbKYAx"
  }
}
```

#### responder <--- (2018-10-16 20:26:16.566)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 20:26:16.566)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpALFUXGGsdug6Jrs56usDVK43SheHuLKP3h48aDzajQnhSXBUWq2rVDufMiousdvbextEcPQPuUq7817TtZyDq2vCt4rqTh3SqYy9jCHBN6SuCufA4j65Xrud4Spcwoi5gsMaowEXQETWMtFFZcbw7DeBpLA7gUF"
  }
}
```

#### responder ---> (2018-10-16 20:26:16.567)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HkEA24ot7aaYES1SG3Uw9dzE4oYTWWvQd9ket6G1aMqR5dAD9RTnvfVeWo5c8aVavm44v8pVKXGAYrZahJwurk4r1gJqLWD16eMRdB5WwWYahn2XM6gan1bhzDcKhcAvtYGV2yS4hTfciPKhG5APHPasctAkaTq9kt8RuC7yQwtwcGu9R1rM87gFSdooPm4ETLc3xCQT3SfcDZS87Deyb4uqbPPvmqFGUUgNJBCSiRCWDznbMUG71ZaGDjxVZ9kE3"
  }
}
```

#### initiator <--- (2018-10-16 20:26:16.568)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 20:26:16.569)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmNbcgSvq2MHesbzFEPfv1LEmwSTJjfzmN9JAQxcJvCcJYgM2uWjwfT821FiWdEgz2dVtsZsgCk4eegkVPT4nRFvZnMMMJ3bKGFJZr5h4NfNgjUXjJGVdeNb8k1Ua97JZvgs67pj51rWJx2Lz1vi3xNWF6EUcxsHdiNB2dsYXwByb9oTcFefB6XqtYe78NhuSHAwEnkjMASQRVtiwArKdrZgQFpDeFL635cWD1yFZ9LNkdbBXmXfxUDQwSEUhBYPti22LgT2jxLQKzEXaam78xdHhPQTm8T7ECFr17jHnbp3VMruNv7wv6LFcXtsLn1mKcgyzjJt9ARa9Q5bQrg6HwqmTq3q"
  }
}
```

#### initiator <--- (2018-10-16 20:26:16.570)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmNbcgSvq2MHesbzFEPfv1LEmwSTJjfzmN9JAQxcJvCcJYgM2uWjwfT821FiWdEgz2dVtsZsgCk4eegkVPT4nRFvZnMMMJ3bKGFJZr5h4NfNgjUXjJGVdeNb8k1Ua97JZvgs67pj51rWJx2Lz1vi3xNWF6EUcxsHdiNB2dsYXwByb9oTcFefB6XqtYe78NhuSHAwEnkjMASQRVtiwArKdrZgQFpDeFL635cWD1yFZ9LNkdbBXmXfxUDQwSEUhBYPti22LgT2jxLQKzEXaam78xdHhPQTm8T7ECFr17jHnbp3VMruNv7wv6LFcXtsLn1mKcgyzjJt9ARa9Q5bQrg6HwqmTq3q"
  }
}
```

#### initiator <--- (2018-10-16 20:26:17.28)
```javascript
{
  "id": -576460752303423408,
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

#### initiator <--- (2018-10-16 20:26:18.832)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### responder <--- (2018-10-16 20:26:18.833)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### initiator <--- (2018-10-16 20:26:18.834)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### responder <--- (2018-10-16 20:26:18.836)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### responder <--- (2018-10-16 20:26:18.839)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### responder <--- (2018-10-16 20:26:18.841)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmNbcgSvq2MHesbzFEPfv1LEmwSTJjfzmN9JAQxcJvCcJYgM2uWjwfT821FiWdEgz2dVtsZsgCk4eegkVPT4nRFvZnMMMJ3bKGFJZr5h4NfNgjUXjJGVdeNb8k1Ua97JZvgs67pj51rWJx2Lz1vi3xNWF6EUcxsHdiNB2dsYXwByb9oTcFefB6XqtYe78NhuSHAwEnkjMASQRVtiwArKdrZgQFpDeFL635cWD1yFZ9LNkdbBXmXfxUDQwSEUhBYPti22LgT2jxLQKzEXaam78xdHhPQTm8T7ECFr17jHnbp3VMruNv7wv6LFcXtsLn1mKcgyzjJt9ARa9Q5bQrg6HwqmTq3q",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### initiator <--- (2018-10-16 20:26:18.841)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### initiator <--- (2018-10-16 20:26:18.842)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmNbcgSvq2MHesbzFEPfv1LEmwSTJjfzmN9JAQxcJvCcJYgM2uWjwfT821FiWdEgz2dVtsZsgCk4eegkVPT4nRFvZnMMMJ3bKGFJZr5h4NfNgjUXjJGVdeNb8k1Ua97JZvgs67pj51rWJx2Lz1vi3xNWF6EUcxsHdiNB2dsYXwByb9oTcFefB6XqtYe78NhuSHAwEnkjMASQRVtiwArKdrZgQFpDeFL635cWD1yFZ9LNkdbBXmXfxUDQwSEUhBYPti22LgT2jxLQKzEXaam78xdHhPQTm8T7ECFr17jHnbp3VMruNv7wv6LFcXtsLn1mKcgyzjJt9ARa9Q5bQrg6HwqmTq3q",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### initiator: (2018-10-16 20:26:18.943)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-16 20:26:18.943)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-16 20:26:18.943)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-16 20:26:18.943)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-16 20:26:18.943)
> Channel is `open` and ready to use

#### responder: (2018-10-16 20:26:18.943)
> Channel is `open` and ready to use

#### initiator <--- (2018-10-16 20:26:18.993)
```javascript
{
  "id": -576460752303423407,
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

#### initiator ---> (2018-10-16 20:26:18.993)
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

#### initiator <--- (2018-10-16 20:26:18.998)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQQDLTkJmPFFvD35BB2etbFQ4nUcYEGKA2oM6PD6XkLqc42F76vx9jChofVev8efJP86LoCrgVNda4KsL3AGkuwzBCCV7ibnFguszCTTaJLcJrq3tC2mRWGSGRyetUJkxZU2uPnB59w6QC6prytgfvYgRspuZvQREmQYEZ9LaWnX2i1oYPgNoWo3qJt1ncbBn29anF39dBPpkB"
  }
}
```

#### initiator ---> (2018-10-16 20:26:19.0)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4pVbLhJ8axgAyLabF2d8KojTA9tDJjtvpe2TFiVgZ9gW52Br3nB7g45P3FSeE4ao9F7wBuZ7M3pvaNU3ZzbWjPr2BBi4iLeBkUwGNnaVHb2QP8myyxWYxyA3VCxNwTDDY4tAZhNCsQnCthdSbosZiaQ8B35pB1UgrzVxz6UUMtww6sJhe8N9n8BEBdBY2TGucLKU1LtNuw9Sdmh6HKRqEe49D3DZBy4niPDYkHArnZ2ERLUwqHA4skkbkepjPBWHCR7zsx7isXThZYGQzHPtXgHSFko5Chdki7bXyCUGf5J3xYf"
  }
}
```

#### responder <--- (2018-10-16 20:26:19.4)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### responder <--- (2018-10-16 20:26:19.5)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQQDLTkJmPFFvD35BB2etbFQ4nUcYEGKA2oM6PD6XkLqc42F76vx9jChofVev8efJP86LoCrgVNda4KsL3AGkuwzBCCV7ibnFguszCTTaJLcJrq3tC2mRWGSGRyetUJkxZU2uPnB59w6QC6prytgfvYgRspuZvQREmQYEZ9LaWnX2i1oYPgNoWo3qJt1ncbBn29anF39dBPpkB"
  }
}
```

#### responder ---> (2018-10-16 20:26:19.6)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4z2zWbkAtXFprsJPrtx4cz7NFsYZuGjhXh89uyXnQfZfmtn1kS3mnn5ogecrD7BxrFPpnCVxuFQ7dKTB3ZeoboDSBGUwEzsApFZWBTL2fz26aDZExkwZ3Ev57zwGwzHqiFFaitmeHeotYN6DvfR7F3ZrxvUXPf6PBaqUJzUA8nMtaCc3pzuMSMQaZtrjVu5Bk7HYritbAXU5e1SzX6nSuyErSHWLYosa6cNHkF7yhDjz28pJ6LSN863Exmg6NDZuu5YikFRiv2DREMWRXe6RitUFmo8ohub42wCQK5s5mMx5Z7e"
  }
}
```

#### responder <--- (2018-10-16 20:26:19.11)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkSDEzKRwjbDMLfG3bCpnjdHyctvYWCX1bFEsCFMhis85Ay9zZupa5WZKqRHihQdQKwj41KYFnoTvbVhuSdxUDfwphjzBXdDLyqJyUk5gzbexaGwzKg7PKzscQq38JmarRtqVuPjho5gL9mTM9Guq7jackeoCoKZw4Pz95ebUx3djusrNcN5PNJL67aj2NqqB8EEPcrRiiVDZHwZ62ErWoCh27k7G8tZmXKm5kcnuT1Z9TLo6o7GJ3tYQinDysA8Gk7Uu2Trm2TP266JbEegpZug6cEJ9pKvU4xtz2UmPG8kFo7tVLDfYZCEgum8pNnP9wAssLV9hG15Huup52DrryVpXbSHEQ27shJtqgq6CvwjZckKPhE1fKsaFttPu2QpaFi41PzPDn",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### initiator <--- (2018-10-16 20:26:19.12)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkSDEzKRwjbDMLfG3bCpnjdHyctvYWCX1bFEsCFMhis85Ay9zZupa5WZKqRHihQdQKwj41KYFnoTvbVhuSdxUDfwphjzBXdDLyqJyUk5gzbexaGwzKg7PKzscQq38JmarRtqVuPjho5gL9mTM9Guq7jackeoCoKZw4Pz95ebUx3djusrNcN5PNJL67aj2NqqB8EEPcrRiiVDZHwZ62ErWoCh27k7G8tZmXKm5kcnuT1Z9TLo6o7GJ3tYQinDysA8Gk7Uu2Trm2TP266JbEegpZug6cEJ9pKvU4xtz2UmPG8kFo7tVLDfYZCEgum8pNnP9wAssLV9hG15Huup52DrryVpXbSHEQ27shJtqgq6CvwjZckKPhE1fKsaFttPu2QpaFi41PzPDn",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### initiator <--- (2018-10-16 20:26:19.16)
```javascript
{
  "id": -576460752303423406,
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

#### initiator <--- (2018-10-16 20:26:19.18)
```javascript
{
  "id": -576460752303423405,
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

#### responder ---> (2018-10-16 20:26:19.18)
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

#### responder <--- (2018-10-16 20:26:19.22)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQQDLTkJmPFFvD35BB2etbFQ4nUcYEGKA2oM6PD6XkLqc42LXcnVhCQ3XbFeTFYnFvFcSRozZiQJEFS5FKGNW1F9Zjayg1mGpHe551Atk5o4FnUDeH6w98yARi14GnDm4ShrdMijtYzrBPm5nzUyLWsvF6DXsZAdi8fMZE3TtcTr2tbPcgt6xAvc6YK62nUMfykBdyxdSrQf8C"
  }
}
```

#### responder ---> (2018-10-16 20:26:19.23)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak51U7gNRxWLQBguFM7QvrFmVwNjjeAffbPLLRKpHAvXn6dsPaYZocTEy8uuXJEg7zCxAFF6qAa5BoCCVRSVpMkNz9TwjvG3iDp2YquWZRkaviC2akpCNzwJaLmnFhpoR8bN2CYJFEFXBRBhiJoxuh2oNwwZX8qXibdbnQdp9y8A4imyudYrxA6v6EQxcBcKjDLtqdSHKaCR9QcWGp9DnGtVGhvxL73Lqu7nXmpMW38KW3XhaDERnVMwa7q7WtzzPgNgbiVf8jrutgpi9gyNWVT51ySnqX8zGnCwpj3Npi5prGRv7"
  }
}
```

#### initiator <--- (2018-10-16 20:26:19.51)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### initiator <--- (2018-10-16 20:26:19.52)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQQDLTkJmPFFvD35BB2etbFQ4nUcYEGKA2oM6PD6XkLqc42LXcnVhCQ3XbFeTFYnFvFcSRozZiQJEFS5FKGNW1F9Zjayg1mGpHe551Atk5o4FnUDeH6w98yARi14GnDm4ShrdMijtYzrBPm5nzUyLWsvF6DXsZAdi8fMZE3TtcTr2tbPcgt6xAvc6YK62nUMfykBdyxdSrQf8C"
  }
}
```

#### initiator ---> (2018-10-16 20:26:19.53)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4xgn45vzHY276RsxMeu5SNA6Fht5aS87gpwCKfJebwy3Dvh7Ww9oNCsiXCGsi775LQdbEw8b6uqPFecc6b5w8bcNuHXa6fywWS6iAchi5LpkMtcjdMwcnyCtCyf9PzMjAK8EhpMW6gt9Uexxe4oQR5LSwBJNvrnbEgFjq5XsCmVPzq3geo3BCooT14Ep38Wvf8nmeRVMU4BeR3qwGfdNdffdAApPP1MjDzLvFXkxh5Xpjnwh9sZEY1G1LQgFQN89bj8LzkmkupCx7emsqq2RhuFy1Q4SkvUzc9peaBMCCbCSr7u"
  }
}
```

#### initiator <--- (2018-10-16 20:26:19.57)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkgJAUxVaRqLBxvwNnUMYVpNg4PK2dwjDqonCHcvigyhWwYF1i8zNiSKoUMZ9zSbqPF8nAPVhLsHtiqN79wVmk3J6ssy6suB2C3Q6A3wSMrCyuER72mg5pdn9xN92m3hZq1Vj4AzMBWUXd6UTLepzcEHkCibWdiXuhHABGCDdWNaGrSRAHPuSusYEbn1ZpNSEs9tkgKfyWctA9FzCwjhmtt1UzbGcgRhGDYbBgkjxePK3VD3NU1wttrYeyvZsddtiANkizseq4MGNNWnSQwPYUgMJAESR9xuaHtUazE2eLkknzvZq6gxo7N6nzedfXXyK5mB5CkwcYiEffS8kMfxqikaGv8hB4pmor2UATVMVFvLud299oBR51GLkFm5vs96wGTJfPXBAC",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### responder <--- (2018-10-16 20:26:19.58)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkgJAUxVaRqLBxvwNnUMYVpNg4PK2dwjDqonCHcvigyhWwYF1i8zNiSKoUMZ9zSbqPF8nAPVhLsHtiqN79wVmk3J6ssy6suB2C3Q6A3wSMrCyuER72mg5pdn9xN92m3hZq1Vj4AzMBWUXd6UTLepzcEHkCibWdiXuhHABGCDdWNaGrSRAHPuSusYEbn1ZpNSEs9tkgKfyWctA9FzCwjhmtt1UzbGcgRhGDYbBgkjxePK3VD3NU1wttrYeyvZsddtiANkizseq4MGNNWnSQwPYUgMJAESR9xuaHtUazE2eLkknzvZq6gxo7N6nzedfXXyK5mB5CkwcYiEffS8kMfxqikaGv8hB4pmor2UATVMVFvLud299oBR51GLkFm5vs96wGTJfPXBAC",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### initiator <--- (2018-10-16 20:26:19.63)
```javascript
{
  "id": -576460752303423404,
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

#### initiator <--- (2018-10-16 20:26:19.64)
```javascript
{
  "id": -576460752303423403,
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

#### responder ---> (2018-10-16 20:26:19.64)
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

#### responder <--- (2018-10-16 20:26:19.68)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQQDLTkJmPFFvD35BB2etbFQ4nUcYEGKA2oM6PD6XkLqc42Rx8e3EfbPFX1dzNSu6v2uyANS8nNz8Nr88wBrFgyuAm5F68S8BYJ1pAGLSsXqLt9rbubzTZrR3eHUrUw1w6drkfwgkUaQtoSTHEsLHwNWWLXCS3wujWUfzqgSfh3Zn7aQ2yMosyZMhaDmw311NeuTUap1JtPhyv"
  }
}
```

#### responder ---> (2018-10-16 20:26:19.69)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4uiFZermtpiQUTTNp1TMqgXpr92uAt7gK5mzdFxHorbgDupvJZ4fn1HzC5CUBQuXSTrMi3JnUaJ2xBn8w4zar9WYgT528E56JxzH11nMNupnEw5XEiHPULSqrf4kaQVEB6CANGGPoAmEvAZfbwK3gjLkNUZsBSzj1bx1WLWc28WHH8Xmb2ZnSzfksettPBaG3GN51YykBcve4MwSn1aQrJbFbqMnBXGyhKx1g51WqUG1vdR7XM8azBAXF5MUV3eQKuhPi7DCvzMFi3vgu3XDHa5LPvonWhrxgWj6JyRs65TPEw2"
  }
}
```

#### initiator <--- (2018-10-16 20:26:19.72)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### initiator <--- (2018-10-16 20:26:19.73)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQQDLTkJmPFFvD35BB2etbFQ4nUcYEGKA2oM6PD6XkLqc42Rx8e3EfbPFX1dzNSu6v2uyANS8nNz8Nr88wBrFgyuAm5F68S8BYJ1pAGLSsXqLt9rbubzTZrR3eHUrUw1w6drkfwgkUaQtoSTHEsLHwNWWLXCS3wujWUfzqgSfh3Zn7aQ2yMosyZMhaDmw311NeuTUap1JtPhyv"
  }
}
```

#### initiator ---> (2018-10-16 20:26:19.74)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4vCcFh6Rp9S8ubQLkUCGzYtBfArmedVTaVnxQBrm1ppeJqcwMPeEHmkmf4Ft9KZD8dd37ZQAaBHrGDA8KZ1XnGryC1GLzQ5p6qkEfRHNvPQsMBxFytLHdK3cDoTbmqbn4owKUkwEUVJA9Htr6pCWt1ohSz1MeV6Yg8k6c9RskrtYSB7tKYzzBWGbTs12pYNwQpNQjh1fVjUkZB5TiUyasHzSfckq2ddNvryq4qXTk5g2bSmZTgekFbMxQxqv52VzhqSfweMFrCbuPwKvB8YwfzfCcqmaVu96UjWeZJJnAtgAyh1"
  }
}
```

#### initiator <--- (2018-10-16 20:26:19.79)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkbBZeS6WLXvbdyPYSqaVK6StWqHnDpz5nNcA9x5wdkaeJisK5rVPVdUMYGT2G3Car7Zc3eNCMaYgQC9Xzp7tBRuegu59xJBAqqMzAfdWgGpuNi11EZTTmjvnuat8dpxFMeuhUA8XY3RXP3ohNiRqh3Vm2S231P9uf9GHt2R2fQB4ENzwAvXZ3ivtELraaLsnp1etQ1BtWEBPtkZwQLt7qxvUYnzpayURiqP7BYrGChTjT5es8ixUKQ94SCrJLR2AKKckiLCf81ZERCoL7pmsME7sbRvknp43WtbER8QWsqagwnTh91uMUCk7r3s72kDaaUDHBptcR2mKozz7NwLDaN1MegQBBuAPFkLe9ky33LMXRKUzCr3ngFJJ2Qq3trCSy5udR2cNU",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### responder <--- (2018-10-16 20:26:19.80)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkbBZeS6WLXvbdyPYSqaVK6StWqHnDpz5nNcA9x5wdkaeJisK5rVPVdUMYGT2G3Car7Zc3eNCMaYgQC9Xzp7tBRuegu59xJBAqqMzAfdWgGpuNi11EZTTmjvnuat8dpxFMeuhUA8XY3RXP3ohNiRqh3Vm2S231P9uf9GHt2R2fQB4ENzwAvXZ3ivtELraaLsnp1etQ1BtWEBPtkZwQLt7qxvUYnzpayURiqP7BYrGChTjT5es8ixUKQ94SCrJLR2AKKckiLCf81ZERCoL7pmsME7sbRvknp43WtbER8QWsqagwnTh91uMUCk7r3s72kDaaUDHBptcR2mKozz7NwLDaN1MegQBBuAPFkLe9ky33LMXRKUzCr3ngFJJ2Qq3trCSy5udR2cNU",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### initiator <--- (2018-10-16 20:26:19.84)
```javascript
{
  "id": -576460752303423402,
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

#### initiator <--- (2018-10-16 20:26:19.85)
```javascript
{
  "id": -576460752303423401,
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

#### initiator ---> (2018-10-16 20:26:19.86)
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

#### initiator <--- (2018-10-16 20:26:19.89)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQQDLTkJmPFFvD35BB2etbFQ4nUcYEGKA2oM6PD6XkLqc42XNeVan8niySmdXVM1qNTzvztBPhJhGSa1ztvi1yAEzGfHN4cLMSsiDfjngfYwa9sxm5XwNnvC8EpvdaSXaXG3HLT1evfnYR8wKj3mYC2TDcjuAzGPo2Ejd4ufDsTginmzJownYRgjMGa76e3azLKvnc2mmNxVwQ"
  }
}
```

#### initiator ---> (2018-10-16 20:26:19.90)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4tcstkSQ3K9qMT3Jr7iiScXU5dLoW4ydHp4zfLifbXFgjf7PZ9TE9pwfMgGNCPRm2xXWFvLEQGcLzfK8VbkGKQCZwqcb5Z8upDmFkDvN5YSvmapGGV9iHJ8YwC1oy3JLfTk8VXt6L26N34bVLM54upPVFt3GgyFyg9dXv3esQiFncKJ3hLttAgLic88RqAg1iYHuakoF8Sh9gMpHCMDisc8t7NTgwK7y6fYai2WbMYsvwq67619DDGMMrA8ASXfdjBoBTH89DXGzGJPoLKgiQzsWnK7A81YFZs4LRRNoxeDPh5M"
  }
}
```

#### responder <--- (2018-10-16 20:26:19.119)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### responder <--- (2018-10-16 20:26:19.120)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQQDLTkJmPFFvD35BB2etbFQ4nUcYEGKA2oM6PD6XkLqc42XNeVan8niySmdXVM1qNTzvztBPhJhGSa1ztvi1yAEzGfHN4cLMSsiDfjngfYwa9sxm5XwNnvC8EpvdaSXaXG3HLT1evfnYR8wKj3mYC2TDcjuAzGPo2Ejd4ufDsTginmzJownYRgjMGa76e3azLKvnc2mmNxVwQ"
  }
}
```

#### responder ---> (2018-10-16 20:26:19.121)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4vbQugruv3j7QuxFoA75h21BMkRGngLomgEbN9BxMRsWxSFEAo3HmeiPbXFi5oRTtQVV6hg625P4fBG7NJaLwkDtkrQVfS32dSfgAw2v6B1QywG3eq4RRderCAxsgT8u9J6srHYWTVahkNh6n7FGzQeVdD53SYsUH7UqtNF5cth67csgc8p2cKBQxJFY5xdvgcwJJKoWhPs5sP4NswemF7Wn3rp8hWciKLv21VncsJPAgo4caihTtJjnNsCSit1nChc8SoRa16MFsdEQLNpeRXsrELjhVL7qDDJPXsaJ4tMGgZg"
  }
}
```

#### responder <--- (2018-10-16 20:26:19.125)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkZJcYv7DCaZvsYBPEkv2sLLLTpMgwzZ2YEFjU29z46Zd4a575TjMRXh5fgp1YTAUZEXWCpo9pWS1H6Aaq2gp12xrvXQcf57pPwQAV8rL8fznms5rvEW8Hh4KjZwkjW75uCknsbz721uCifF5fAF71vvogvNX68xd1Gh7j1f9zRr3wXEERh1iAqsipsjk7DeoCWXLgf1xKZrFY8sibxw6a87h3VPFHafc5BznVjThBkEFDr2BN7eoRn1WHcn6F9UMU7TTnDrGkZbtwNrGDJhNVr6KTujuTi2QjbsH8jpxV5PgX2W2tF9a1pGDEvBCPwuGzPa9s8Hvu7RTyqVTDRpi5cXc7PHqnWENBdz7mSCz6Tad5HQ4eY3XJ8JU4a3RbUTed8nde8K42",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### initiator <--- (2018-10-16 20:26:19.126)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkZJcYv7DCaZvsYBPEkv2sLLLTpMgwzZ2YEFjU29z46Zd4a575TjMRXh5fgp1YTAUZEXWCpo9pWS1H6Aaq2gp12xrvXQcf57pPwQAV8rL8fznms5rvEW8Hh4KjZwkjW75uCknsbz721uCifF5fAF71vvogvNX68xd1Gh7j1f9zRr3wXEERh1iAqsipsjk7DeoCWXLgf1xKZrFY8sibxw6a87h3VPFHafc5BznVjThBkEFDr2BN7eoRn1WHcn6F9UMU7TTnDrGkZbtwNrGDJhNVr6KTujuTi2QjbsH8jpxV5PgX2W2tF9a1pGDEvBCPwuGzPa9s8Hvu7RTyqVTDRpi5cXc7PHqnWENBdz7mSCz6Tad5HQ4eY3XJ8JU4a3RbUTed8nde8K42",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### initiator <--- (2018-10-16 20:26:19.131)
```javascript
{
  "id": -576460752303423400,
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

#### initiator <--- (2018-10-16 20:26:19.132)
```javascript
{
  "id": -576460752303423399,
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

#### responder ---> (2018-10-16 20:26:19.132)
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

#### responder <--- (2018-10-16 20:26:19.136)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQQDLTkJmPFFvD35BB2etbFQ4nUcYEGKA2oM6PD6XkLqc42coAM8Kbz4hNXd4cF8nubX2dVKGvLMvdgDvB2om4TQNp3mvMmpv3buJUTDrT1PX5X8XAc76RcvHWrL1tMXgQVs1JPaUKjYKcoCFje4CnMh2q8XWGcLVGmk711uaiAHHrQiMV1GJWQE8z2Bs1wS3EiWUXBgBMoPCR"
  }
}
```

#### responder ---> (2018-10-16 20:26:19.137)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak566bFRytVNmHwoBYVjkREXFoGKZCf9uNpsbNhpcgMziwYMde1EDauqT2HY7WPkePuNcXKY4ZNGuoLH3C7L2dwT7byogGT5JDFapqNwvFNmpfHzL8j6hVUGDPpW8VaPVvMJ3gZNoQtJ2cHYVis43ZY3rMGxAYyjdicL8F3Cc6jdDqrCd93ZR1FvUUBeRmMGmf6GtH9R9Zm6LqJVtAsLhonBfMd2xbcuPqUHebEUdqQQmJ86AsWRXfF6Y6sKmELvB8AhMRq1z9g3VkrVC9BTGT1eTRDmXmPbYnc7S9vNQPnrHN9iB"
  }
}
```

#### initiator <--- (2018-10-16 20:26:19.168)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### initiator <--- (2018-10-16 20:26:19.168)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQQDLTkJmPFFvD35BB2etbFQ4nUcYEGKA2oM6PD6XkLqc42coAM8Kbz4hNXd4cF8nubX2dVKGvLMvdgDvB2om4TQNp3mvMmpv3buJUTDrT1PX5X8XAc76RcvHWrL1tMXgQVs1JPaUKjYKcoCFje4CnMh2q8XWGcLVGmk711uaiAHHrQiMV1GJWQE8z2Bs1wS3EiWUXBgBMoPCR"
  }
}
```

#### initiator ---> (2018-10-16 20:26:19.170)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak52u1G1L8PpPhcqhwe1mrLGoDh25x8yzYhyqaoXm27AyKZMQbQWAMfg4xcdbX4KKs4Nhz1Ex3VrTchQkcGP7VEeWVDAbCB5ybtwfNybXouRyiDBsZoGcz2Qr9ZSkHLYayh5DxggaLXcVKkTgbrX1HY3LSmM7ZcqNsjjYNu5odWdXb1BUpJRyhz2T7cCZ1Z7327JYvrfnqdEyMdhKUfhkBSunH5Zx5ErgU6GaCYxkfELgo1rR52RrVJWhWScaLwTkgbXBrK5Y5L4MZH4CRXzVC5ek2m662uTHfnG9LPAqatgCfsEn"
  }
}
```

#### initiator <--- (2018-10-16 20:26:19.176)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkoY2rDCmZg6yLKJgT1akESaxY4M2UKhNuNpNmT432hNg3jpFX9fKuuFGxp42Ythbyt1hZdWnQbCTtZGgP7uMSLC6yh8geJXPKSgL1HViDokqrqGkdszemARektxFZFzS2yajWdYmEF2CJC8iKToagLXgVmpEfLdkaUhRTERnUZz39ixavMHj8iyKbjKa5FMNWQGaYppZRabhVj29V23WXk2XvrWHpFdvWLyPu5Lm9Zv7f6K754gtZH9tmVxxoUn8CpfJzpMY5AWbcCBQGtooAr8jiQP343uBSPHqVi8t7nRRqTebdAoY1m3wKKdzmEnKQQfsqKMfQ9FL5s1yJNtzs6VLcVgxqVzAJUsqhWigx1UefoPQNGPhYW6fcbHSz8i42XU6KbTVy",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### responder <--- (2018-10-16 20:26:19.177)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkoY2rDCmZg6yLKJgT1akESaxY4M2UKhNuNpNmT432hNg3jpFX9fKuuFGxp42Ythbyt1hZdWnQbCTtZGgP7uMSLC6yh8geJXPKSgL1HViDokqrqGkdszemARektxFZFzS2yajWdYmEF2CJC8iKToagLXgVmpEfLdkaUhRTERnUZz39ixavMHj8iyKbjKa5FMNWQGaYppZRabhVj29V23WXk2XvrWHpFdvWLyPu5Lm9Zv7f6K754gtZH9tmVxxoUn8CpfJzpMY5AWbcCBQGtooAr8jiQP343uBSPHqVi8t7nRRqTebdAoY1m3wKKdzmEnKQQfsqKMfQ9FL5s1yJNtzs6VLcVgxqVzAJUsqhWigx1UefoPQNGPhYW6fcbHSz8i42XU6KbTVy",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### initiator <--- (2018-10-16 20:26:19.182)
```javascript
{
  "id": -576460752303423398,
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

#### responder ---> (2018-10-16 20:26:19.251)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### responder <--- (2018-10-16 20:26:19.257)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "tx": "tx_2C9estKT2eEsu7dU3VbURFGJaNPgaEmtRABr64Uf8RsJjxHCyZtRQ5G5mPKgfRi1uHXhtEYqbHvX4pDDhFYeZDPvs13akSSbSEb7nqVrx7sqZd7JEC6aPAVEPJ3S1FZmaNXJoBqTpmpgYksXjcddxZffEX9NbX"
  }
}
```

#### responder ---> (2018-10-16 20:26:19.258)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "tx": "tx_2WsEQsiC5Xsn4NZ8PQcKbE2sWH4dcCNEB5Bw1ftJ98R6iWVy1aoE1Nw3s5STb1TxR85eypSxHyscF31reCKKVoBRLgZoSrQ1CHB2UjYurmxyMcZttaishdsCkmMgo63XmjHQ6BRD9kJbvXjdxBhmQMnEHbnwAgjiz6qqRKx1L9sauvyJbUHkd9tznqydxXRk7crwepETtCmvbtwEmBqvR7dWyNSfVikHq6X1LAqqjaBstpNuDfsEBNEJy1dXhEM4gPZ"
  }
}
```

#### initiator <--- (2018-10-16 20:26:19.259)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "withdraw_created",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### initiator <--- (2018-10-16 20:26:19.260)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "tx": "tx_2C9estKT2eEsu7dU3VbURFGJaNPgaEmtRABr64Uf8RsJjxHCyZtRQ5G5mPKgfRi1uHXhtEYqbHvX4pDDhFYeZDPvs13akSSbSEb7nqVrx7sqZd7JEC6aPAVEPJ3S1FZmaNXJoBqTpmpgYksXjcddxZffEX9NbX"
  }
}
```

#### initiator ---> (2018-10-16 20:26:19.260)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "tx": "tx_2WsEQsiC5XsnMq1ipJLHwCxyunbuYQf5zxAif8CH8oyNNHo8TNiiJTQjSHrbWRXRJWUxZaT7VinEWggmCErEUAc3J3UeFTKGnVEx4kFcz3zeCcaKAYWNZze4fE8TmYmk6taHyhjPq1oDMyrU5kJQrbdWA3c51BJcCJM8r5pNkSRNpm46nqmXcnyANGeTVVezovn7775x3kgekocYeWoxz1W7xvcjpo4B2m5wWtKMpXUjACTW47xjrXGivdnfjm7y3en"
  }
}
```

#### initiator <--- (2018-10-16 20:26:19.263)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3cDMp6242sByqNuQ1HkMNe59oU5gnDgrHwr1WP6kMZ1urVCoLof6LFT2SvGGbwsLS7Pe5LURZYzSgzeGcePCHLrdz27Ev1o5xoh3aauxXRiH1j9Q5FSSWNLxydVqSzLDvdnqUgiyzrkckwv8TYV4t4PabHGXNAtkSiT5aYuJ7MhN43bCASNPpjcpwHYiB7iYiYetzcqXiXqF7VS49j8LYAQyLKLDHnDJ3XYn1Kw4nh8Ldn59oodaKdjkB3YW1gszzrggLBdwHDPX6LjgC9Tko1VZqEyBroo9zPd4Zt8rocYptmPH8FVSeU2ufwHZK6zAn2pLtNM6eV2MgbepryHKx37ybtCfH",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### responder <--- (2018-10-16 20:26:19.263)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3cDMp6242sByqNuQ1HkMNe59oU5gnDgrHwr1WP6kMZ1urVCoLof6LFT2SvGGbwsLS7Pe5LURZYzSgzeGcePCHLrdz27Ev1o5xoh3aauxXRiH1j9Q5FSSWNLxydVqSzLDvdnqUgiyzrkckwv8TYV4t4PabHGXNAtkSiT5aYuJ7MhN43bCASNPpjcpwHYiB7iYiYetzcqXiXqF7VS49j8LYAQyLKLDHnDJ3XYn1Kw4nh8Ldn59oodaKdjkB3YW1gszzrggLBdwHDPX6LjgC9Tko1VZqEyBroo9zPd4Zt8rocYptmPH8FVSeU2ufwHZK6zAn2pLtNM6eV2MgbepryHKx37ybtCfH",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### initiator <--- (2018-10-16 20:26:21.136)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_withdraw_locked",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### responder <--- (2018-10-16 20:26:21.136)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_withdraw_locked",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### initiator <--- (2018-10-16 20:26:21.136)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "withdraw_locked",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### responder <--- (2018-10-16 20:26:21.137)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "withdraw_locked",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### responder <--- (2018-10-16 20:26:21.140)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3cDMp6242sByqNuQ1HkMNe59oU5gnDgrHwr1WP6kMZ1urVCoLof6LFT2SvGGbwsLS7Pe5LURZYzSgzeGcePCHLrdz27Ev1o5xoh3aauxXRiH1j9Q5FSSWNLxydVqSzLDvdnqUgiyzrkckwv8TYV4t4PabHGXNAtkSiT5aYuJ7MhN43bCASNPpjcpwHYiB7iYiYetzcqXiXqF7VS49j8LYAQyLKLDHnDJ3XYn1Kw4nh8Ldn59oodaKdjkB3YW1gszzrggLBdwHDPX6LjgC9Tko1VZqEyBroo9zPd4Zt8rocYptmPH8FVSeU2ufwHZK6zAn2pLtNM6eV2MgbepryHKx37ybtCfH",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```

#### initiator <--- (2018-10-16 20:26:21.140)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3cDMp6242sByqNuQ1HkMNe59oU5gnDgrHwr1WP6kMZ1urVCoLof6LFT2SvGGbwsLS7Pe5LURZYzSgzeGcePCHLrdz27Ev1o5xoh3aauxXRiH1j9Q5FSSWNLxydVqSzLDvdnqUgiyzrkckwv8TYV4t4PabHGXNAtkSiT5aYuJ7MhN43bCASNPpjcpwHYiB7iYiYetzcqXiXqF7VS49j8LYAQyLKLDHnDJ3XYn1Kw4nh8Ldn59oodaKdjkB3YW1gszzrggLBdwHDPX6LjgC9Tko1VZqEyBroo9zPd4Zt8rocYptmPH8FVSeU2ufwHZK6zAn2pLtNM6eV2MgbepryHKx37ybtCfH",
    "channel_id": "ch_p6kQ97Sziebk8y13ko6AUbsdZ9nkbbyUWy6Ub87GZGVc5ZADD"
  }
}
```
