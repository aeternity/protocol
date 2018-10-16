
#### initiator init (2018-10-16 20:25:42.306)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A&role=initiator
```

#### responder init (2018-10-16 20:25:42.311)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A&role=responder
```

#### responder <--- (2018-10-16 20:25:43.312)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 20:25:43.315)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 20:25:43.326)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpALFUXGGsdug6Jrs56usDVK43SheHuLKP3h48aDzajQnhSXBUWq2rVDufMiousdvbextEcPQPuUq7817TtZyDq2vCt4rqTh3SqYy9jCHBN6SuCufA4j65Xrud4Spcwoi5gsMaowEXQETWMtFFZcbw7DeBoFpcino"
  }
}
```

#### initiator ---> (2018-10-16 20:25:43.356)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HjkKtbJtAjEAgPNWdjnCgqK66NWStrLaSmSeLWib9KDoYmCQ9WcyL5BASmo8nhVCW1hYfCF6phVMtfCkePKsXuQWBHCHArBVWqLoXnr3cW6QueWGcYd9DT7NqoMGi5YoDwg4V81kopJ2CRbeVvvyqS7iftQFsYqZHRakh1PqSQTSCbjdmRDRFjR9vkyurf8Nc3Jm9NmPD6u6ZJ984mEdpQUE7RfWnoVtt4Hu7FFGHrf2tNSwsGBAKkqwxxsPghAjx"
  }
}
```

#### responder <--- (2018-10-16 20:25:43.358)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 20:25:43.358)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpALFUXGGsdug6Jrs56usDVK43SheHuLKP3h48aDzajQnhSXBUWq2rVDufMiousdvbextEcPQPuUq7817TtZyDq2vCt4rqTh3SqYy9jCHBN6SuCufA4j65Xrud4Spcwoi5gsMaowEXQETWMtFFZcbw7DeBoFpcino"
  }
}
```

#### responder ---> (2018-10-16 20:25:43.359)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HnS8DzxkyEz34rwnzY1V56HqiZzPpgmjns7X9RCsQbPGxHjhCWLoYQVY8sNBNGLTPAkEuQUbTKKGHywpmWKKdCom5gRtd7F9xf1oAZSibUs9CR1G1iUTh4AREGz8wX9et2wDXzYZQ9ptbCVo3RP5vjSks8ryB5kUPtAb2HhjgHXyK48SwqnbfdesXKcNXsAbzL5qVtXK4vxta8T7D7TNt4CuJmufDCRgBUzGKrwFsmfPmD44f53eGJ1YQgbWuydDC"
  }
}
```

#### initiator <--- (2018-10-16 20:25:43.360)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 20:25:43.361)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmMmmirWXwgRmsLPRxA3KD8ThQCe1Hcm9TEZH9MYSfr2jzHYK2GLw28JggNL27FMVPhxf9MFAxPt7wYNQrpHyrNCaNHaQEFbHTeVA4UbMwcfQTEKCha5TDVLARWZmN1cEnF9ko9gENY1C9D7L687R2yNzERMywke95AiTtW7k13Sh5s3VY1t4pZL9ZyZh7jHJ98G6dk5PyH3yr8nXrtSyMCEjyMijzDw2LQZKYDYpMT6T7apoRkEJbZQt7puihbbHfmK3Pka57YCrgDqZHFcMeQ1JPZMuoeLxPX2TycK5MXpCfdDCp3FL9gMnihXTRzC5sRtDZjRrWtyDnNG82Q1ooYtn472"
  }
}
```

#### initiator <--- (2018-10-16 20:25:43.362)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmMmmirWXwgRmsLPRxA3KD8ThQCe1Hcm9TEZH9MYSfr2jzHYK2GLw28JggNL27FMVPhxf9MFAxPt7wYNQrpHyrNCaNHaQEFbHTeVA4UbMwcfQTEKCha5TDVLARWZmN1cEnF9ko9gENY1C9D7L687R2yNzERMywke95AiTtW7k13Sh5s3VY1t4pZL9ZyZh7jHJ98G6dk5PyH3yr8nXrtSyMCEjyMijzDw2LQZKYDYpMT6T7apoRkEJbZQt7puihbbHfmK3Pka57YCrgDqZHFcMeQ1JPZMuoeLxPX2TycK5MXpCfdDCp3FL9gMnihXTRzC5sRtDZjRrWtyDnNG82Q1ooYtn472"
  }
}
```

#### initiator <--- (2018-10-16 20:25:43.644)
```javascript
{
  "id": -576460752303423474,
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

#### responder <--- (2018-10-16 20:25:44.443)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### responder <--- (2018-10-16 20:25:44.443)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### initiator <--- (2018-10-16 20:25:44.443)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### initiator <--- (2018-10-16 20:25:44.444)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### responder <--- (2018-10-16 20:25:44.449)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### initiator <--- (2018-10-16 20:25:44.449)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### responder <--- (2018-10-16 20:25:44.450)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmMmmirWXwgRmsLPRxA3KD8ThQCe1Hcm9TEZH9MYSfr2jzHYK2GLw28JggNL27FMVPhxf9MFAxPt7wYNQrpHyrNCaNHaQEFbHTeVA4UbMwcfQTEKCha5TDVLARWZmN1cEnF9ko9gENY1C9D7L687R2yNzERMywke95AiTtW7k13Sh5s3VY1t4pZL9ZyZh7jHJ98G6dk5PyH3yr8nXrtSyMCEjyMijzDw2LQZKYDYpMT6T7apoRkEJbZQt7puihbbHfmK3Pka57YCrgDqZHFcMeQ1JPZMuoeLxPX2TycK5MXpCfdDCp3FL9gMnihXTRzC5sRtDZjRrWtyDnNG82Q1ooYtn472",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### initiator <--- (2018-10-16 20:25:44.451)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmMmmirWXwgRmsLPRxA3KD8ThQCe1Hcm9TEZH9MYSfr2jzHYK2GLw28JggNL27FMVPhxf9MFAxPt7wYNQrpHyrNCaNHaQEFbHTeVA4UbMwcfQTEKCha5TDVLARWZmN1cEnF9ko9gENY1C9D7L687R2yNzERMywke95AiTtW7k13Sh5s3VY1t4pZL9ZyZh7jHJ98G6dk5PyH3yr8nXrtSyMCEjyMijzDw2LQZKYDYpMT6T7apoRkEJbZQt7puihbbHfmK3Pka57YCrgDqZHFcMeQ1JPZMuoeLxPX2TycK5MXpCfdDCp3FL9gMnihXTRzC5sRtDZjRrWtyDnNG82Q1ooYtn472",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### initiator: (2018-10-16 20:25:44.701)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-16 20:25:44.701)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-16 20:25:44.701)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-16 20:25:44.701)
> Channel is `open` and ready to use

#### responder: (2018-10-16 20:25:44.701)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-16 20:25:44.701)
> Channel is `open` and ready to use

#### initiator <--- (2018-10-16 20:25:44.747)
```javascript
{
  "id": -576460752303423473,
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

#### initiator ---> (2018-10-16 20:25:44.748)
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

#### initiator <--- (2018-10-16 20:25:44.760)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTrZN4coVY7aPF31swLGaPUYeCVCssDzgjJwhsxdM2HqadDDPtjzheNLX4DKD6t3y9nCAXeoBXQ4bPxSjFwjgdHY6Ab7kEcg3Qcvomg4bhq52JW8Voq7DKL5GVWHDGPGoNUed3dzpucMwEKvDWV3K4jbz27yU625HwU6DnwhR1eHU9gtqjceE7G9Zw9vG6NY8FvjBMqj6dFMg"
  }
}
```

#### initiator ---> (2018-10-16 20:25:44.763)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4pLrRbTjrwEJhd7pXS27RpnBXHiiAfKancMXTcTTQBudVKetcCHJieexWJJJmAKsBUEQiKqo64CBbZrRapm2A7bLnsyewPCUpMegWMkQyeXwxyZjacz8hUcKwPWWnbjn1kvs9E6GNcYHuWKHdfimKethn8nYmjA28V3K7Wyn5jzcrHgJgiioDx4GnSDyZTXwiCswGbXsqrhHVHcHctB53BFT2v5xSzfQdBkNP4Asn4AghArP6GW1W6LNeRjFnKDVjhzDz27isWnqTM6YLUZDQRzE4C2m6j1JyfAcY6egTo5Bpcn"
  }
}
```

#### responder <--- (2018-10-16 20:25:44.772)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### responder <--- (2018-10-16 20:25:44.773)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTrZN4coVY7aPF31swLGaPUYeCVCssDzgjJwhsxdM2HqadDDPtjzheNLX4DKD6t3y9nCAXeoBXQ4bPxSjFwjgdHY6Ab7kEcg3Qcvomg4bhq52JW8Voq7DKL5GVWHDGPGoNUed3dzpucMwEKvDWV3K4jbz27yU625HwU6DnwhR1eHU9gtqjceE7G9Zw9vG6NY8FvjBMqj6dFMg"
  }
}
```

#### responder ---> (2018-10-16 20:25:44.775)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4tQMqd9jMPvAzPCngdtWdvWDgwderZqmzxDvm1baX8bHRZ5Xyc7csk7kXEVcXsoACVxqvZbTDFDRerd44vdP2Y3xCiY4GHrxKjAG3kqhcvh3MJMMHJkRzNyAQGKqjb9GdP4Dkes2c15je91PRdyArhFG9dKj1aYZq3DLyDoX6xrYBmFrcowZQDUM8N93PbDoGertRG1GrgHRLfj5cNLSMGRWiArH9FE6qmtHKnHzSe5tu4CmFVJXr8DTQRBTw2LTa28PsvRQKptpuPpRaMvj7kEHQnYNo6bCYEazAaukCyeeWVd"
  }
}
```

#### responder <--- (2018-10-16 20:25:44.781)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkRxDWtcL9hXdABspfaiiUgcjZ2vvwkRqSgM9RUxGsFTRkGiqMSpQ2rKSpERnQDdBvxxBaLD8q8S1WXLfPNf4fibZwhjYwdbrWyu3te4V6qi1xjxEcYW29cDexN9ym2xF2wKUJ9XfsfLMnbwJ2vcYixF1AnssnWKWQ5NGZsyxQpUSEfB7syqagS887j2rAbGWiYSW6xbSJ4QpPc372ycpQWjjhjE83TJR8HwquEUnpCX8FEDyiZy7fUvRFMURm89Y63maNXzBaH3hKxoe7onZB8SHQGnpjZJDhYg7aj7yHs2nQLNva4qxBbjKkEKiB1tdNxhjTQCsC5arngrgSxwzdh4g6gaqaWPCTNgNxWo4RJSg1taxpWbNXA7X8CrCkUX9ng1zRvSXv",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### initiator <--- (2018-10-16 20:25:44.782)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkRxDWtcL9hXdABspfaiiUgcjZ2vvwkRqSgM9RUxGsFTRkGiqMSpQ2rKSpERnQDdBvxxBaLD8q8S1WXLfPNf4fibZwhjYwdbrWyu3te4V6qi1xjxEcYW29cDexN9ym2xF2wKUJ9XfsfLMnbwJ2vcYixF1AnssnWKWQ5NGZsyxQpUSEfB7syqagS887j2rAbGWiYSW6xbSJ4QpPc372ycpQWjjhjE83TJR8HwquEUnpCX8FEDyiZy7fUvRFMURm89Y63maNXzBaH3hKxoe7onZB8SHQGnpjZJDhYg7aj7yHs2nQLNva4qxBbjKkEKiB1tdNxhjTQCsC5arngrgSxwzdh4g6gaqaWPCTNgNxWo4RJSg1taxpWbNXA7X8CrCkUX9ng1zRvSXv",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### initiator <--- (2018-10-16 20:25:44.786)
```javascript
{
  "id": -576460752303423472,
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

#### initiator <--- (2018-10-16 20:25:44.787)
```javascript
{
  "id": -576460752303423471,
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

#### responder ---> (2018-10-16 20:25:44.788)
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

#### responder <--- (2018-10-16 20:25:44.791)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTrZN4coVY7aPF31swLGaPUYeCVCssDzgjJwhsxdM2HqadJdukHYAqi4SpCrL111WHJHo8ngQZ4inWAN1N3UmvSvdZ5g3Q7Ee8p1cV7EPAH1wwftaszpr24EYWufXBPNgcJNazCpDyN98tarE6mhuPyRCQkH6rEYfCHQth51WgyHejGy8wLntEpQoNEARyYS5rXavHKaNF1sB"
  }
}
```

#### responder ---> (2018-10-16 20:25:44.792)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4osNvXMVzXvASUXiFkJ6DmbeXpiap6DXoc7KJy58XHbKb9ey6aBMiqmZ6UfgBTHzcejnwKYnfNbkVS3DdVghSLmc3tQ7Ea9FgE5QEGgvSt4EFcwiRcmriAAxraekz8GSNQfVuhdsSkrawJ4ocpxhKYctneSekioWeaSgvTmdVb5g1ZSwMpADD8jDhUnGJCHTw9yM5BBCAjzqFQCZQugdRohQZo2UeYtuUvAWJEGqjUf3TMuSgotcT4CL8RuLtCTbC52Uqfo1ZDu21R4EHQCdTXhn1tsbN5ni1WC9pSeVPRtZftQ"
  }
}
```

#### initiator <--- (2018-10-16 20:25:44.831)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### initiator <--- (2018-10-16 20:25:44.833)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTrZN4coVY7aPF31swLGaPUYeCVCssDzgjJwhsxdM2HqadJdukHYAqi4SpCrL111WHJHo8ngQZ4inWAN1N3UmvSvdZ5g3Q7Ee8p1cV7EPAH1wwftaszpr24EYWufXBPNgcJNazCpDyN98tarE6mhuPyRCQkH6rEYfCHQth51WgyHejGy8wLntEpQoNEARyYS5rXavHKaNF1sB"
  }
}
```

#### initiator ---> (2018-10-16 20:25:44.836)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4kg4DYyHjDdDG9CNdkjYsfsEN6TrBrZ6kgDwuVMovTGHW6nnCwfCPeBy2bsG8cQBAVVmJBkF6kRR8ZSMXGZ8zxeB3dAFLTzQydC6YFD87sKhiCLiTcZANZGBSWo7S7oZVUphJnCXrzttvchAL22zpAfAFKWqqeNRQYPNrzyym2ZWtHUoERF8Kxzeu2bdjZphoDrxVcFLe9yBtxfTc54v4q8vX7Q2LcjUurKohgG9HoQuvufJVb6iPVQDQbMbqqhWmni3ZCPVJfwjYBrfQvPWQLnvqMzfC1fgLuGGoBH95nw7PcN"
  }
}
```

#### initiator <--- (2018-10-16 20:25:44.847)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkKePBvYkjgpDvqFu8RfuSugGhVeRCVnHw8MQQw82mJkSFZL9N2BWSoAn1hyMELifFDvX98nSPx49aDVR6yPAQXMSboBpUrW6DwzY1VFmJHDoQz78m1hLrwuaZJmAAkFARxREVdn6MwJ1AZcv5uy2fL81THHKDBQvgAGTBYzkAYMPdE5WqPrdKtb7iPe315KH3TYvTzEE7TpdXUUPaVjLE96gvtCyD7wJgZTig3ZRoHLCqRZNNY6jSmd4kpeGKip6eHCoKCfAcnFsoNNVhYAChW2edHfttZUgVkzp2mF1rZ7Q4gg7cFscefZiNjyfEfBRpfZf7anmm1VK65xaQvpZ5n5oeidpC726oPQ5qBa1NUhm3s64JnKT2cpDB2xrHPcVn53Lwo9Q4",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### responder <--- (2018-10-16 20:25:44.848)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkKePBvYkjgpDvqFu8RfuSugGhVeRCVnHw8MQQw82mJkSFZL9N2BWSoAn1hyMELifFDvX98nSPx49aDVR6yPAQXMSboBpUrW6DwzY1VFmJHDoQz78m1hLrwuaZJmAAkFARxREVdn6MwJ1AZcv5uy2fL81THHKDBQvgAGTBYzkAYMPdE5WqPrdKtb7iPe315KH3TYvTzEE7TpdXUUPaVjLE96gvtCyD7wJgZTig3ZRoHLCqRZNNY6jSmd4kpeGKip6eHCoKCfAcnFsoNNVhYAChW2edHfttZUgVkzp2mF1rZ7Q4gg7cFscefZiNjyfEfBRpfZf7anmm1VK65xaQvpZ5n5oeidpC726oPQ5qBa1NUhm3s64JnKT2cpDB2xrHPcVn53Lwo9Q4",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### initiator <--- (2018-10-16 20:25:44.855)
```javascript
{
  "id": -576460752303423470,
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

#### initiator <--- (2018-10-16 20:25:44.856)
```javascript
{
  "id": -576460752303423469,
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

#### responder ---> (2018-10-16 20:25:44.856)
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

#### responder <--- (2018-10-16 20:25:44.860)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTrZN4coVY7aPF31swLGaPUYeCVCssDzgjJwhsxdM2HqadQ4Rbq5e33nNaCPSu7rW4bpXhEFUXkcuvDFdHXETfCXf3M6A4xbtnkkmaYwAu473dJrDP49GuJrUoLFDteFLYJVuD9g9YvrYZxLUV8fKtZgSiQqbdWa31brWL3nbGh2siHPRR3igsa1qGv4gWC8m1oRX8hRrMm6p"
  }
}
```

#### responder ---> (2018-10-16 20:25:44.861)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak52nXLosE2xiUAxtd1RhPnYLuCugP88Z9Ld37cg7xxvurkKU2DmXxSxKQhjGqsVNb5n4an8LswnhJoDysPN1i2L1Ac3EXHZDT21cbiDFkSpPM9mV35ozVp9yKWAeVgz9yaJuD6X1iBiZNwwhVyenXFkjX6pRXtecXBVxoTpePd9FnvWKQKUsY8CDxTDJKsrd35KHcj8ps4kEWq2B9MGGnscP5rHikqJ5iYk1Ybpoerrhe4ZFkGe223swshz9VMweWtpVTPNNrQPw2cExN7oAdB5xLDv2JrhsmqL5cnKhrLhLJShH"
  }
}
```

#### initiator <--- (2018-10-16 20:25:44.865)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### initiator <--- (2018-10-16 20:25:44.866)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTrZN4coVY7aPF31swLGaPUYeCVCssDzgjJwhsxdM2HqadQ4Rbq5e33nNaCPSu7rW4bpXhEFUXkcuvDFdHXETfCXf3M6A4xbtnkkmaYwAu473dJrDP49GuJrUoLFDteFLYJVuD9g9YvrYZxLUV8fKtZgSiQqbdWa31brWL3nbGh2siHPRR3igsa1qGv4gWC8m1oRX8hRrMm6p"
  }
}
```

#### initiator ---> (2018-10-16 20:25:44.867)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak5AJSWc5EhJDSvjbUxXrV786udwPsk8BwuqGEWExLdTngT3YKLSDYiteG1gnw1wRvf7DboKot3kq58tzN8HUhdtDA1dhizdurRjpfgMwo9VQ3QtxBKrvKx6PuJDDz6a6knwK3WSKumBLyPNV11M92JFqPrbUuLHwpBYH7d7MVnj45QG8E9DjWqRRLxWpYe8ynbLZqN3e5w69GHkMKiiXBV2Wixdnpy9A5yuZJFP3xJmFoDDv47tCvpAuNb6BUShPkNFKWjzMJv78GNyYTGC1xxLXnx91iq2BshaFjkrqH5Zc8DTS"
  }
}
```

#### initiator <--- (2018-10-16 20:25:44.871)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkoLtarV6zMXveAscxMyiyQzBaHVGQA6vzfLqDz9oYnnzfwXRDEYwEhDnktGSZUyQepeHHvpdpUaRY35jQM3smiuzrACS3QmjxR2hXHQqxUE2ABy9xTcvxe4abNYCXJj6EfoUw9jUBmYTPNZBrdPPRzzPsacH7CnM4nU9WeKNbzgaY9rTsZjP2BYsZeJq7xcUo4LBPmKGr1aHpMsbdQAyKq2SmcXb3QJDysndEUqydLHDNke5qsLkQRVRQv28eCuZ46cuw4cgc4M7H1NuhKgVMefXzd9SRhUcjkQVcgj3JvyqpUD7dzuCvW3fdr4fVid27eAx5zf1t4czL1BGAPKPf7wcSdPS93127WtdH3ip76NmjVjCs3Sx8wRwQTij1MTVM4mYxGajx",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### responder <--- (2018-10-16 20:25:44.872)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkoLtarV6zMXveAscxMyiyQzBaHVGQA6vzfLqDz9oYnnzfwXRDEYwEhDnktGSZUyQepeHHvpdpUaRY35jQM3smiuzrACS3QmjxR2hXHQqxUE2ABy9xTcvxe4abNYCXJj6EfoUw9jUBmYTPNZBrdPPRzzPsacH7CnM4nU9WeKNbzgaY9rTsZjP2BYsZeJq7xcUo4LBPmKGr1aHpMsbdQAyKq2SmcXb3QJDysndEUqydLHDNke5qsLkQRVRQv28eCuZ46cuw4cgc4M7H1NuhKgVMefXzd9SRhUcjkQVcgj3JvyqpUD7dzuCvW3fdr4fVid27eAx5zf1t4czL1BGAPKPf7wcSdPS93127WtdH3ip76NmjVjCs3Sx8wRwQTij1MTVM4mYxGajx",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### initiator <--- (2018-10-16 20:25:44.876)
```javascript
{
  "id": -576460752303423468,
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

#### initiator <--- (2018-10-16 20:25:44.878)
```javascript
{
  "id": -576460752303423467,
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

#### initiator ---> (2018-10-16 20:25:44.878)
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

#### initiator <--- (2018-10-16 20:25:44.882)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTrZN4coVY7aPF31swLGaPUYeCVCssDzgjJwhsxdM2HqadVUwTNd7EPWJLBvZoEaxVgnNCyWPTTkye77b2NzjqYMAdPN6FAmoNTAH41AxvALKMR1PK14Vy5w5Ln2KQ9tmAV2ZiUabeJWAGSNxfZuaYWPiw7aXwzdYmfUjZGLmgoyYusfG12P8zwfXdFEHYmkSSGjYMTqqKewq"
  }
}
```

#### initiator ---> (2018-10-16 20:25:44.883)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4qEZDCzuQXGeoAupdkYMCcvLJdDBDQxjfEjE8nYkhmQp4EpXu4ubd4xkGEn1P31MJpyGUkxLiGobrQPUcg4ABz8oEzQoz2ekmtuN9NY1yJs6suYyWFGbGi7Vt1WwnnjrBpnfxjtMbaJYUSyMxAke7NPQsX741ftyMYAGcgh8BsePLA5xumzF8eBLQ3bzrJgCDLPvw3CUybHNYhahFuPs8fuVKoEShngCSqvJw8yqmgfVh9z4aGjiPEfyWGCFgwPmjiEPnmC97BXX5tZTBzSfY8gD3Xt4zdeP7WYU3RLXcfcfQV7"
  }
}
```

#### responder <--- (2018-10-16 20:25:44.916)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### responder <--- (2018-10-16 20:25:44.916)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTrZN4coVY7aPF31swLGaPUYeCVCssDzgjJwhsxdM2HqadVUwTNd7EPWJLBvZoEaxVgnNCyWPTTkye77b2NzjqYMAdPN6FAmoNTAH41AxvALKMR1PK14Vy5w5Ln2KQ9tmAV2ZiUabeJWAGSNxfZuaYWPiw7aXwzdYmfUjZGLmgoyYusfG12P8zwfXdFEHYmkSSGjYMTqqKewq"
  }
}
```

#### responder ---> (2018-10-16 20:25:44.917)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4x2u4aEDiCcXSzhSPzhG2E28uy5kJwcDcpQsucmaLWmutQKWAq7gBMsrb5U6UFzhALrBmazP5ABY2o88rLkbpr9HaBQXzgJdfVwHYK35JUvqhj7tbzwtkvfbh5KibADGpjKzTLAQc2Z8i3c4q3B39K7eLHf5uXYLbyKXnPuo4wpoMXB6iszttkTEDfqvcDncJfSbNpTfWz6qdhRbSTNJ7mzVrWr6QwrzRimyZWzq7UzBjtWnaNcwmUJibzqbbeJN1iWvvmGXif3pEmu11crzuAx7jaEYAk7q3HAN4jz6BTzRhSM"
  }
}
```

#### responder <--- (2018-10-16 20:25:44.923)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkTV6w6UXKwDBsbEpRo7fV4byCdGtKApcb3rdc2hvyKWZeFaaa3mxhsgcZAZNhTW9ejEbXCEAzzfzj8MDqERXfZjFFkG7MXHyrvQXeYovaFe75CPZyk3Syqj5kWGDfngW5GweFNQspTjkKQZt9QoJ5ryefhntgTQNsnMUX7tq2mQJDuzgGk3ZvDLiiCRqn82A6aaKMn5QPXfgsLGGJDVSarys9FEToczdtoohbJZe94NcedvaejmUq5VMhK8TR7dNido6UwK7XMP9txpqhDRi8eaCUfpw8cZEEQhtL9r5EMipHugXsUZXBAo2SSCY7RWbDJH17QoHfdTqDkqUZHmUjYEjzUkmQvQNtg4Rhk1AHZgtRPvUy2MKsFLywschHAJ8AXjAnX6t3",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### initiator <--- (2018-10-16 20:25:44.923)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkTV6w6UXKwDBsbEpRo7fV4byCdGtKApcb3rdc2hvyKWZeFaaa3mxhsgcZAZNhTW9ejEbXCEAzzfzj8MDqERXfZjFFkG7MXHyrvQXeYovaFe75CPZyk3Syqj5kWGDfngW5GweFNQspTjkKQZt9QoJ5ryefhntgTQNsnMUX7tq2mQJDuzgGk3ZvDLiiCRqn82A6aaKMn5QPXfgsLGGJDVSarys9FEToczdtoohbJZe94NcedvaejmUq5VMhK8TR7dNido6UwK7XMP9txpqhDRi8eaCUfpw8cZEEQhtL9r5EMipHugXsUZXBAo2SSCY7RWbDJH17QoHfdTqDkqUZHmUjYEjzUkmQvQNtg4Rhk1AHZgtRPvUy2MKsFLywschHAJ8AXjAnX6t3",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### initiator <--- (2018-10-16 20:25:44.928)
```javascript
{
  "id": -576460752303423466,
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

#### initiator <--- (2018-10-16 20:25:44.930)
```javascript
{
  "id": -576460752303423465,
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

#### responder ---> (2018-10-16 20:25:44.930)
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

#### responder <--- (2018-10-16 20:25:44.935)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQTrZN4coVY7aPF31swLGaPUYeCVCssDzgjJwhsxdM2HqadauTJvAaRjEE6BTghMYVdCszp7PcV8RAkK2s8Ujq8hji1svPQfLQ6eF5mSLkNcHEzamUPAn8fp6MNBQdK9zeQJkXf3Pzi4HMvhJyFraAskCwKjupHwKoJfxffWhcPQYcYbhw4W9DiSTF5KzfScoLprRTWNLZFFAH"
  }
}
```

#### responder ---> (2018-10-16 20:25:44.936)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4vbaZmpDAUXFLMJo4WtrnZuysLcL2HLgzAyi6pn92kFjxwr5q5NVxK2upRafhnVVPWGaE9CSBrqRpotucQed1F26BmZJMvCSwokQsMbXZodAK3uet42TSb29hL3VeSK7U97TSNZXsHdJZfpKP9eKp429eKWaCQvQHXwb8TnxYMffHVqTVhy8gxXsbDQwBjFxhyvTZhE6sFAxSQZCuuYubwh5CnJaCzVnhjpqFpA44u7zDjotpiG39U8jeCwiywctVKtVKhsXD9QbPZPW1SMaoaVTm3LVnvXMeiAcEvHCyJdabPD"
  }
}
```

#### initiator <--- (2018-10-16 20:25:44.965)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### initiator <--- (2018-10-16 20:25:44.965)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQTrZN4coVY7aPF31swLGaPUYeCVCssDzgjJwhsxdM2HqadauTJvAaRjEE6BTghMYVdCszp7PcV8RAkK2s8Ujq8hji1svPQfLQ6eF5mSLkNcHEzamUPAn8fp6MNBQdK9zeQJkXf3Pzi4HMvhJyFraAskCwKjupHwKoJfxffWhcPQYcYbhw4W9DiSTF5KzfScoLprRTWNLZFFAH"
  }
}
```

#### initiator ---> (2018-10-16 20:25:44.967)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak53p8UZ6BWjvBUgbaq7x6Syd2r8t62g6iqUPnhpEsrwA1DNuCg7QDLTgwDVSspGSDP4Qdad45UbSBK2ZyqXFxxzyViPX3EByE1eRYadTxUSuPyEMu9yEqVHwMMMQSK3z3iVfJM6jeJkDR3Qy2eTprL59pGm5dJB8s6CyKPf9akW4R3PRGFsUrgo31i7TLDWh8uY98nqKn6uxzWpa5uiGr8LGftGVfyCM2GXMyJTdiTDeKdS2zu9JJnLQEBt3K9zQ841mMcKysfSuPZwGBccXRXWoPmdgtuBKrAivfxCoXETParZ4"
  }
}
```

#### initiator <--- (2018-10-16 20:25:44.973)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkchocUuB75s5b1xQanJyNHcKFqKC3h56zAgHe99Vx7bDJCLzxUDmEzT3GtV3gAut1mEEzJ71NmiEvyXt1fnb9uUzmwEUufhfYfnim7Ds1eXAq3j2CVHbzCVwwmWZ8DvMWhfZwSLmEhrUFfBgGrxEwNFgo61Mrj8tApoF8kQ77EiYjk5SEvBdaaQgjwxPJaDxbgTfqRHoEJvU1QiTWZoVeydAemGSFq2trVCt5maYc3J3nyzr6gjUeXUQcZn6cgSESXsuekBxPdyJuCynHw2a2M3uoJEzgNkbLmhvMCyqbDLi9hRDMPTf8Z6QtfYQcRY5Epdz5Y5Gidmy4dq51PuvGoA3Nnw5xEzWyXtryUcUiBPasqRujD2PKwzKiMEax6M8aYVXm4TfW",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### responder <--- (2018-10-16 20:25:44.973)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkchocUuB75s5b1xQanJyNHcKFqKC3h56zAgHe99Vx7bDJCLzxUDmEzT3GtV3gAut1mEEzJ71NmiEvyXt1fnb9uUzmwEUufhfYfnim7Ds1eXAq3j2CVHbzCVwwmWZ8DvMWhfZwSLmEhrUFfBgGrxEwNFgo61Mrj8tApoF8kQ77EiYjk5SEvBdaaQgjwxPJaDxbgTfqRHoEJvU1QiTWZoVeydAemGSFq2trVCt5maYc3J3nyzr6gjUeXUQcZn6cgSESXsuekBxPdyJuCynHw2a2M3uoJEzgNkbLmhvMCyqbDLi9hRDMPTf8Z6QtfYQcRY5Epdz5Y5Gidmy4dq51PuvGoA3Nnw5xEzWyXtryUcUiBPasqRujD2PKwzKiMEax6M8aYVXm4TfW",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### initiator <--- (2018-10-16 20:25:44.979)
```javascript
{
  "id": -576460752303423464,
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

#### initiator ---> (2018-10-16 20:25:45.48)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### initiator <--- (2018-10-16 20:25:45.57)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "tx": "tx_2M9ipLgcZYJ7SpUnQabkk8t4x42kAciNhtNf1E3Fi3geU4YRfhGuk7cHqbSNk2QH9CMSN38WDitbDktvEujMEiySgpcQKvmcXhhyA2MnnQ8BBDyC1FAvA"
  }
}
```

#### initiator ---> (2018-10-16 20:25:45.60)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "tx": "tx_2iJcVi27J8ZyMyYrgiPrP1T9h18TwB5p14ExzLASiqN53hxEKEF1ZNsP5NwVqnsQeh5eEVkieZjkxYbfQFpnDq1mGc6VF5ssrMnRyxY3vGPyfNp3FqqutQnn4tfFPNJxPgXWDYhWR1i9xH9NaWGfq3AcxaaMmEPpmTwgGrPuRqP5k3YVkGR9S13BdiZp7nq5oFqkYohMadfw5wMDR7TLomZaxx"
  }
}
```

#### responder <--- (2018-10-16 20:25:45.62)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "tx": "tx_2M9ipLgcZYJ7SpUnQabkk8t4x42kAciNhtNf1E3Fi3geU4YRfhGuk7cHqbSNk2QH9CMSN38WDitbDktvEujMEiySgpcQKvmcXhhyA2MnnQ8BBDyC1FAvA"
  }
}
```

#### responder ---> (2018-10-16 20:25:45.62)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "tx": "tx_2iJcVi27J8ZyXpZTiwEcm5Lp4W241ukPpCReTvbWnf894q8p9kaSRfKstNLmMHyfiUMTzmhLPwKuDAhrUa16XrvuRyqDZGkrFsRb4UST7g9HwXU5qgqg3fAAau6kU7dGHCnmT7jmibauobs6qMn7n13cyMEJWufMWSTXskewyeZMqQe4B3wZX4Hx9YRqp1czu4gpPmUusJyLL9hdJ6th2GQXwk"
  }
}
```

#### responder <--- (2018-10-16 20:25:45.65)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3wu1WL1txa1XAv2hEA5ar1NQKwkL9X4FFFeyiLbnHpyHicpiBtF9v8fvjzbZjB3zDNB8JTKa2WqQoehvtHDCQJBwAx3QTkNgxxjSkCsFthu5GzrY2AQ7zeYK3qdc4qH46S83baNmAWFnrMrMdFeB2iwYcW7zgnd84U38QmXPRUnB32ptipFvod2onKXwx4Fk6rj4k7r2HLvFaSPwqt3E5R4eihHzBfUYGBeS8pbdWkm827FBqmfMc1EYvYckNs7T1pkpU28deaYQbvPHpUjDhWhSkq6tvAhmE3StYgR1VN8pF2kMeGN8",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### responder <--- (2018-10-16 20:25:45.66)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "close_mutual",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### responder <--- (2018-10-16 20:25:45.66)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### initiator <--- (2018-10-16 20:25:45.71)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3wu1WL1txa1XAv2hEA5ar1NQKwkL9X4FFFeyiLbnHpyHicpiBtF9v8fvjzbZjB3zDNB8JTKa2WqQoehvtHDCQJBwAx3QTkNgxxjSkCsFthu5GzrY2AQ7zeYK3qdc4qH46S83baNmAWFnrMrMdFeB2iwYcW7zgnd84U38QmXPRUnB32ptipFvod2onKXwx4Fk6rj4k7r2HLvFaSPwqt3E5R4eihHzBfUYGBeS8pbdWkm827FBqmfMc1EYvYckNs7T1pkpU28deaYQbvPHpUjDhWhSkq6tvAhmE3StYgR1VN8pF2kMeGN8",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### initiator <--- (2018-10-16 20:25:45.72)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "close_mutual",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```

#### initiator <--- (2018-10-16 20:25:45.72)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_2or7oPuURTUtEUK264yQWYaGUvJw6BwzY5ud99H4KzwjaeLQCM"
  }
}
```
