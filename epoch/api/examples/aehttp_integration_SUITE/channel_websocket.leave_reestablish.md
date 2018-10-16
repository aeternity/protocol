
#### initiator init (2018-10-16 20:25:50.307)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A&role=initiator
```

#### responder init (2018-10-16 20:25:50.311)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A&role=responder
```

#### responder <--- (2018-10-16 20:25:51.310)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 20:25:51.311)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 20:25:51.315)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpALFUXGGsdug6Jrs56usDVK43SheHuLKP3h48aDzajQnhSXBUWq2rVDufMiousdvbextEcPQPuUq7817TtZyDq2vCt4rqTh3SqYy9jCHBN6SuCufA4j65Xrud4Spcwoi5gsMaowEXQETWMtFFZcbw7DeBoYuNJ1f"
  }
}
```

#### initiator ---> (2018-10-16 20:25:51.336)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HnVHUeod6GtdE9VDa8y4ZF5ng6hbVpNz63pP2te8nemxvfTzExZjdRPtAm1TieiieUtW5mp6zPF1BMwST4KACFGPujFviSyNSWjuhSDjV5mrNAi3A2mGm8FcJi36nWrG8qHQoDJPymXhv9QdFj7SmHLoBgiNLdaojnw56osg8Lzg3DgtYJGzKWiqQh96Yz33Tyo6yN9gFxfNP1mQszMmTnmAteyoUVjF1mdGFkhrrbpvBKeW7HGC8R6pJgj5Ppj1H"
  }
}
```

#### responder <--- (2018-10-16 20:25:51.337)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 20:25:51.337)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpALFUXGGsdug6Jrs56usDVK43SheHuLKP3h48aDzajQnhSXBUWq2rVDufMiousdvbextEcPQPuUq7817TtZyDq2vCt4rqTh3SqYy9jCHBN6SuCufA4j65Xrud4Spcwoi5gsMaowEXQETWMtFFZcbw7DeBoYuNJ1f"
  }
}
```

#### responder ---> (2018-10-16 20:25:51.338)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4Hm2zpDXiDYqPWtGpiWHcYgevNXNr644RrQBiLu2bmadhrTAaeUEBW9kntcQzoDtA63oBKWZaD3D5FwpSBQaGAqq8Gt5vDez4L4TGkDmNiKezWtKNiiR6N1AM33mEUTrRnf7MyZb6Ao1ACMWhjJ3y5YzDmYWUeBd4xJHmP5hQM3j1U3EMXmD26VZVkLFrmWAm8B4i7BDoC2ggx9DiVbhPcw4VBGvu4wvR4GmBBaTiAeSwpUx5NwTHThj4bryLWohc5"
  }
}
```

#### initiator <--- (2018-10-16 20:25:51.340)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 20:25:51.340)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmPz9JsEBGXU7KQhr2XwFDq2yNkrzZspQMkA71XUDYyU1yRVDc8dNZ84dGG7uqi9XbByqw323Ti6rBP1KxLEoC2fmb6uYiushUnGFCKZ9nxHSQp6rMYTyQx9bdC3qmTgRVif2Sn69t2hQSw3ZhA6L5QBNWj4Xbg2vZbFKgK7twJm75hz1xyk1MUWmkqYyptcziLV22HzZn4N1wso1mxQVHGpARCWLSb6HwNzXyeyPjwMTGmPJGvRk8MTSEh8rF9NGNVyTp5HwGgmcefmnFzCZL3UxLwA1yDxtjGbahHHXTX1dRTUaKXDK8EWUZyeAFyjthxuBng2VhJF4kVkEjD8TbbAXPfj"
  }
}
```

#### initiator <--- (2018-10-16 20:25:51.341)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmPz9JsEBGXU7KQhr2XwFDq2yNkrzZspQMkA71XUDYyU1yRVDc8dNZ84dGG7uqi9XbByqw323Ti6rBP1KxLEoC2fmb6uYiushUnGFCKZ9nxHSQp6rMYTyQx9bdC3qmTgRVif2Sn69t2hQSw3ZhA6L5QBNWj4Xbg2vZbFKgK7twJm75hz1xyk1MUWmkqYyptcziLV22HzZn4N1wso1mxQVHGpARCWLSb6HwNzXyeyPjwMTGmPJGvRk8MTSEh8rF9NGNVyTp5HwGgmcefmnFzCZL3UxLwA1yDxtjGbahHHXTX1dRTUaKXDK8EWUZyeAFyjthxuBng2VhJF4kVkEjD8TbbAXPfj"
  }
}
```

#### initiator <--- (2018-10-16 20:25:52.39)
```javascript
{
  "id": -576460752303423452,
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

#### initiator <--- (2018-10-16 20:25:52.826)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### responder <--- (2018-10-16 20:25:52.828)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### responder <--- (2018-10-16 20:25:52.829)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### initiator <--- (2018-10-16 20:25:52.829)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### initiator <--- (2018-10-16 20:25:52.834)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### responder <--- (2018-10-16 20:25:52.834)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### initiator <--- (2018-10-16 20:25:52.835)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmPz9JsEBGXU7KQhr2XwFDq2yNkrzZspQMkA71XUDYyU1yRVDc8dNZ84dGG7uqi9XbByqw323Ti6rBP1KxLEoC2fmb6uYiushUnGFCKZ9nxHSQp6rMYTyQx9bdC3qmTgRVif2Sn69t2hQSw3ZhA6L5QBNWj4Xbg2vZbFKgK7twJm75hz1xyk1MUWmkqYyptcziLV22HzZn4N1wso1mxQVHGpARCWLSb6HwNzXyeyPjwMTGmPJGvRk8MTSEh8rF9NGNVyTp5HwGgmcefmnFzCZL3UxLwA1yDxtjGbahHHXTX1dRTUaKXDK8EWUZyeAFyjthxuBng2VhJF4kVkEjD8TbbAXPfj",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### responder <--- (2018-10-16 20:25:52.835)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmPz9JsEBGXU7KQhr2XwFDq2yNkrzZspQMkA71XUDYyU1yRVDc8dNZ84dGG7uqi9XbByqw323Ti6rBP1KxLEoC2fmb6uYiushUnGFCKZ9nxHSQp6rMYTyQx9bdC3qmTgRVif2Sn69t2hQSw3ZhA6L5QBNWj4Xbg2vZbFKgK7twJm75hz1xyk1MUWmkqYyptcziLV22HzZn4N1wso1mxQVHGpARCWLSb6HwNzXyeyPjwMTGmPJGvRk8MTSEh8rF9NGNVyTp5HwGgmcefmnFzCZL3UxLwA1yDxtjGbahHHXTX1dRTUaKXDK8EWUZyeAFyjthxuBng2VhJF4kVkEjD8TbbAXPfj",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### initiator: (2018-10-16 20:25:53.401)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-16 20:25:53.401)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-16 20:25:53.401)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-16 20:25:53.401)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-16 20:25:53.401)
> Channel is `open` and ready to use

#### responder: (2018-10-16 20:25:53.402)
> Channel is `open` and ready to use

#### initiator ---> (2018-10-16 20:25:53.432)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {}
}
```

#### responder <--- (2018-10-16 20:25:53.435)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "state": "tx_6jPYBUFTkcmPz9JsEBGXU7KQhr2XwFDq2yNkrzZspQMkA71XUDYyU1yRVDc8dNZ84dGG7uqi9XbByqw323Ti6rBP1KxLEoC2fmb6uYiushUnGFCKZ9nxHSQp6rMYTyQx9bdC3qmTgRVif2Sn69t2hQSw3ZhA6L5QBNWj4Xbg2vZbFKgK7twJm75hz1xyk1MUWmkqYyptcziLV22HzZn4N1wso1mxQVHGpARCWLSb6HwNzXyeyPjwMTGmPJGvRk8MTSEh8rF9NGNVyTp5HwGgmcefmnFzCZL3UxLwA1yDxtjGbahHHXTX1dRTUaKXDK8EWUZyeAFyjthxuBng2VhJF4kVkEjD8TbbAXPfj",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### responder <--- (2018-10-16 20:25:53.436)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.436)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "state": "tx_6jPYBUFTkcmPz9JsEBGXU7KQhr2XwFDq2yNkrzZspQMkA71XUDYyU1yRVDc8dNZ84dGG7uqi9XbByqw323Ti6rBP1KxLEoC2fmb6uYiushUnGFCKZ9nxHSQp6rMYTyQx9bdC3qmTgRVif2Sn69t2hQSw3ZhA6L5QBNWj4Xbg2vZbFKgK7twJm75hz1xyk1MUWmkqYyptcziLV22HzZn4N1wso1mxQVHGpARCWLSb6HwNzXyeyPjwMTGmPJGvRk8MTSEh8rF9NGNVyTp5HwGgmcefmnFzCZL3UxLwA1yDxtjGbahHHXTX1dRTUaKXDK8EWUZyeAFyjthxuBng2VhJF4kVkEjD8TbbAXPfj",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.436)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### responder init (2018-10-16 20:25:53.477)
```
ws://localhost:3014/channel?channel_reserve=2&existing_channel_id=ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB&initiator_amount=700&initiator_id=ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh&lock_period=10&offchain_tx=tx_6jPYBUFTkcmPz9JsEBGXU7KQhr2XwFDq2yNkrzZspQMkA71XUDYyU1yRVDc8dNZ84dGG7uqi9XbByqw323Ti6rBP1KxLEoC2fmb6uYiushUnGFCKZ9nxHSQp6rMYTyQx9bdC3qmTgRVif2Sn69t2hQSw3ZhA6L5QBNWj4Xbg2vZbFKgK7twJm75hz1xyk1MUWmkqYyptcziLV22HzZn4N1wso1mxQVHGpARCWLSb6HwNzXyeyPjwMTGmPJGvRk8MTSEh8rF9NGNVyTp5HwGgmcefmnFzCZL3UxLwA1yDxtjGbahHHXTX1dRTUaKXDK8EWUZyeAFyjthxuBng2VhJF4kVkEjD8TbbAXPfj&port=12341&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A&role=responder
```

#### initiator init (2018-10-16 20:25:53.483)
```
ws://localhost:3014/channel?channel_reserve=2&existing_channel_id=ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB&host=localhost&initiator_amount=700&initiator_id=ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh&lock_period=10&offchain_tx=tx_6jPYBUFTkcmPz9JsEBGXU7KQhr2XwFDq2yNkrzZspQMkA71XUDYyU1yRVDc8dNZ84dGG7uqi9XbByqw323Ti6rBP1KxLEoC2fmb6uYiushUnGFCKZ9nxHSQp6rMYTyQx9bdC3qmTgRVif2Sn69t2hQSw3ZhA6L5QBNWj4Xbg2vZbFKgK7twJm75hz1xyk1MUWmkqYyptcziLV22HzZn4N1wso1mxQVHGpARCWLSb6HwNzXyeyPjwMTGmPJGvRk8MTSEh8rF9NGNVyTp5HwGgmcefmnFzCZL3UxLwA1yDxtjGbahHHXTX1dRTUaKXDK8EWUZyeAFyjthxuBng2VhJF4kVkEjD8TbbAXPfj&port=12341&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A&role=initiator
```

#### responder <--- (2018-10-16 20:25:53.489)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_reestablished",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### responder <--- (2018-10-16 20:25:53.490)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.491)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_reestablished",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### responder <--- (2018-10-16 20:25:53.492)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmPz9JsEBGXU7KQhr2XwFDq2yNkrzZspQMkA71XUDYyU1yRVDc8dNZ84dGG7uqi9XbByqw323Ti6rBP1KxLEoC2fmb6uYiushUnGFCKZ9nxHSQp6rMYTyQx9bdC3qmTgRVif2Sn69t2hQSw3ZhA6L5QBNWj4Xbg2vZbFKgK7twJm75hz1xyk1MUWmkqYyptcziLV22HzZn4N1wso1mxQVHGpARCWLSb6HwNzXyeyPjwMTGmPJGvRk8MTSEh8rF9NGNVyTp5HwGgmcefmnFzCZL3UxLwA1yDxtjGbahHHXTX1dRTUaKXDK8EWUZyeAFyjthxuBng2VhJF4kVkEjD8TbbAXPfj",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.492)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.493)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmPz9JsEBGXU7KQhr2XwFDq2yNkrzZspQMkA71XUDYyU1yRVDc8dNZ84dGG7uqi9XbByqw323Ti6rBP1KxLEoC2fmb6uYiushUnGFCKZ9nxHSQp6rMYTyQx9bdC3qmTgRVif2Sn69t2hQSw3ZhA6L5QBNWj4Xbg2vZbFKgK7twJm75hz1xyk1MUWmkqYyptcziLV22HzZn4N1wso1mxQVHGpARCWLSb6HwNzXyeyPjwMTGmPJGvRk8MTSEh8rF9NGNVyTp5HwGgmcefmnFzCZL3UxLwA1yDxtjGbahHHXTX1dRTUaKXDK8EWUZyeAFyjthxuBng2VhJF4kVkEjD8TbbAXPfj",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.541)
```javascript
{
  "id": -576460752303423451,
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

#### initiator ---> (2018-10-16 20:25:53.542)
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

#### initiator <--- (2018-10-16 20:25:53.553)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQS7fZiqFW5oMB4jRcv5eedJR1Cpjq2WEs8poXDxoK51iPi7UC61ywZPBxD7MC88CBocKDTGgELTsqjZewkhdcMrG91qzAj3VhQLpJ7bwGzW9xMSD2X8s7nF9DEgFWpyz8Az67ptdPA6Sa429uPGdoKeibG5w5DRq9XDudmUfiwTE4S9ekDsCiqhusdFcukrWbEyQLUJ1F5di3"
  }
}
```

#### initiator ---> (2018-10-16 20:25:53.556)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak59iS8SAV1yW9FwpED4jqyARAUfzAbEUe1TibEU5ujad9Bw1YCon2swM4PyeVYNv6861kaRrAZH338aMXMJvanxkfEgX5vGXirygXMA9RbBW3VH32VWHeavcSYFVWvDoprN5VP1WyQfE1EVSbEaqtx8uSTdiDs7pSpzuiiL4ByWfnHmPNvqgqBv7k7TYug9VV7UR9U3ad985C3AzYCNiDBNQX8Kky7mLcA7zJMnhQuWWuEvLj6Kd7dAmXhpKg8MYFus5c2qzcQKqknnfpkSGpqMsZJaxfx6QsRLMhK3mn1fEiKVm"
  }
}
```

#### responder <--- (2018-10-16 20:25:53.567)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### responder <--- (2018-10-16 20:25:53.568)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQS7fZiqFW5oMB4jRcv5eedJR1Cpjq2WEs8poXDxoK51iPi7UC61ywZPBxD7MC88CBocKDTGgELTsqjZewkhdcMrG91qzAj3VhQLpJ7bwGzW9xMSD2X8s7nF9DEgFWpyz8Az67ptdPA6Sa429uPGdoKeibG5w5DRq9XDudmUfiwTE4S9ekDsCiqhusdFcukrWbEyQLUJ1F5di3"
  }
}
```

#### responder ---> (2018-10-16 20:25:53.570)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4ogZg5yHRgMG8HufTnJ9xs3eMrHnNq8JgMvitEAXQzEG5jihwsq4Y81oK2H2Cg9mpx3ZtmnWqmCuCLTNaZq8RmDDSgcWhHL13tyqdAHxqR31oQSFthdLjCnyp9bdYQQE1FXCN74L3TGiitxUUan6kFFkNDxX5Y4vrdKHSDpd1K8ErihAARFoSgdDM1D6zguQ7Z2kEZGPeMXwqwKujn5AcNKUutFcFMoVS6oRvcfhWwuRUcsg4pKCsH57D9Fe5mdWtCXSyDbSuAuVbHFx3koDpmGPhcAETVZbXQDC6tzL3n2QMWu"
  }
}
```

#### responder <--- (2018-10-16 20:25:53.578)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkQpPg311CTYb2Qf1Q4VzLg5p8L91iPhN2fL1W9aHDNcau72EojboZk2bcB5bN2d3cEjFyQiZt6yL1Yia2ronz2xkKW3XHx4bqiCmXTYKZCqXaAUGJM9oCzqWVFg5JMgwM9gCdDtjDguuyvEU4RnqAhNCsrdp4vQS5igumYbnJ97PsVgfqrZjcZKeEYKsBGK9nv7NpNJmyxFVRGrm8jf4Yrc7qP2iHFxzgwwf41xQT2p9cNXHUHAD5SrALz8VJd8X1Rv9cHfs9APCyhAVK4NXLDLHsChYrHGrZuL77uDwVsaEKjbcKCpY2HCmECotKGDofpmpSQD26FWEHpcpeYZmv73BQn6p41mk176yvzH9bQj3HHec7nop3RCkkdqDysfJExFwPLBzX",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.579)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkQpPg311CTYb2Qf1Q4VzLg5p8L91iPhN2fL1W9aHDNcau72EojboZk2bcB5bN2d3cEjFyQiZt6yL1Yia2ronz2xkKW3XHx4bqiCmXTYKZCqXaAUGJM9oCzqWVFg5JMgwM9gCdDtjDguuyvEU4RnqAhNCsrdp4vQS5igumYbnJ97PsVgfqrZjcZKeEYKsBGK9nv7NpNJmyxFVRGrm8jf4Yrc7qP2iHFxzgwwf41xQT2p9cNXHUHAD5SrALz8VJd8X1Rv9cHfs9APCyhAVK4NXLDLHsChYrHGrZuL77uDwVsaEKjbcKCpY2HCmECotKGDofpmpSQD26FWEHpcpeYZmv73BQn6p41mk176yvzH9bQj3HHec7nop3RCkkdqDysfJExFwPLBzX",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.585)
```javascript
{
  "id": -576460752303423450,
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

#### initiator <--- (2018-10-16 20:25:53.586)
```javascript
{
  "id": -576460752303423449,
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

#### responder ---> (2018-10-16 20:25:53.586)
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

#### responder <--- (2018-10-16 20:25:53.590)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQS7fZiqFW5oMB4jRcv5eedJR1Cpjq2WEs8poXDxoK51iPiCthwZXQkiusy6tK2F9iw8Qr4QZTN8Y2qmaDroNhf1egQLYTtY4J8Xu6q374Sx6szby7bJakUyJVG5dpjz61Qop5mTSnDrDmiH5uyZJPetXoeiEhyeJWn3EJfbypcnEF1jj3RbMNyGB74Ks5e2QYqaG5PmvDqui4"
  }
}
```

#### responder ---> (2018-10-16 20:25:53.591)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4mepPYJaoNne5E8J21smgFF1ReBLR4MC74uFGJViSnztzGsb7hMBh7zpGhKyYA2EhRD9Y8bTsE9cGD4VLvrB74VY2z9U6feAb2dZnZCpdZd5jGwspfoUnQvYLrTxZieHtqTavSg6PUPHrHcR9dLGwNjfP1JDnPdiCMrAa6SFfc6FsEFVPMSe4FUmCukojwYHVN1NZRHwta6sHx75nGJcdKBFpEdoWPJk6PVKrHz6x2YiNXE8JGS7vh5FQ5HtZpWnknTe76LdzQi5wh8Y487D4yiXDDz527EC5XpGb9N7EpJQ7fw"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.595)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.595)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQS7fZiqFW5oMB4jRcv5eedJR1Cpjq2WEs8poXDxoK51iPiCthwZXQkiusy6tK2F9iw8Qr4QZTN8Y2qmaDroNhf1egQLYTtY4J8Xu6q374Sx6szby7bJakUyJVG5dpjz61Qop5mTSnDrDmiH5uyZJPetXoeiEhyeJWn3EJfbypcnEF1jj3RbMNyGB74Ks5e2QYqaG5PmvDqui4"
  }
}
```

#### initiator ---> (2018-10-16 20:25:53.596)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak5853t5WRHykDtTz4PUXPBMvLD9GuD3tqijL1mpRKzZCUJ1pKvxywLpRUmfmcKJitAEkDxeF4wV1EKmAzMNFNiQ92vZvZzgHmQH7JT9vuNM5KuHXS6PmEdKE6FccYCGiThV2Cs1ZcrFPT2DFC5mQGMMUpDPHD49bjYaVAeH5XBu9fz3DtheH9PFY1y5ui7v5tLq3HHMbkTvX14wwWRZwMrAXPwX6iwumDqjuyqFDENEugGPxZ5iwh7UhiXkTSduk3AxqNrQgj3P48am9sZoLBxN8amw29BJud3qvg3WiYayrXbAU"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.600)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkMKxz8okLCQBSEoW74i7Fq3XBrYVkvVSm6N3Es3shHZ6sP89QdTBiumbZx27ZACdFYhJvTnDDsCSfEyFVt99bJVMPmBtLm3VeLxoUu95U37Fmmt7pxcXgkB8dT2omTVCzyqXRGjy6j66aRrTotV9dKSpNdt5APLTLH3cq98iaTnfPYrUGodpk85ihZjY56kvSg7FLdnSzF8tgvGdcQrH1S5YEZ1eGt55biidTHksFzryQ3gDyG5Wa18eaatNUYYNS47aN6rMugLC3htG6gAqgvgb4i4mnEUvT75z5PStfDwxgFB7NJqzgtsv34KdyEj6XmCTD9zaaunmQCoTmddF3TryoJnYfWmQwwjn3N58UTjQj23YLShPbbPmdWzzF31LX1mSdm96E",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### responder <--- (2018-10-16 20:25:53.601)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkMKxz8okLCQBSEoW74i7Fq3XBrYVkvVSm6N3Es3shHZ6sP89QdTBiumbZx27ZACdFYhJvTnDDsCSfEyFVt99bJVMPmBtLm3VeLxoUu95U37Fmmt7pxcXgkB8dT2omTVCzyqXRGjy6j66aRrTotV9dKSpNdt5APLTLH3cq98iaTnfPYrUGodpk85ihZjY56kvSg7FLdnSzF8tgvGdcQrH1S5YEZ1eGt55biidTHksFzryQ3gDyG5Wa18eaatNUYYNS47aN6rMugLC3htG6gAqgvgb4i4mnEUvT75z5PStfDwxgFB7NJqzgtsv34KdyEj6XmCTD9zaaunmQCoTmddF3TryoJnYfWmQwwjn3N58UTjQj23YLShPbbPmdWzzF31LX1mSdm96E",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.605)
```javascript
{
  "id": -576460752303423448,
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

#### initiator <--- (2018-10-16 20:25:53.606)
```javascript
{
  "id": -576460752303423447,
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

#### responder ---> (2018-10-16 20:25:53.606)
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

#### responder <--- (2018-10-16 20:25:53.610)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQS7fZiqFW5oMB4jRcv5eedJR1Cpjq2WEs8poXDxoK51iPiJKDo74sx4doj6RRvMziiRwacr8XLpSAFpTqnH8PPmFhtbxaZPRYnUeFvUorBjBygEvk6MuBNDvRYWDXTExfLowPzQJhoQwBPeaAMvFp9Uo3xNoCkvKtbMfvJakuCVyTzk9KuJHBc1n8y1mLAg7Dzr6gF9g1ytDN"
  }
}
```

#### responder ---> (2018-10-16 20:25:53.611)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4uaqPukvBotJkM1YmqE9tmfRu7icw3K31tSkxBbU5g9gznEmTNkEXpNc1Ryp7isBctDrjUSRS9qE7g7MGdAY6pnTJkKhbbe5LzvRSJ75xhuAdAtH9HTJY82JiCNatgJJVrQuC3Y15sP4Q3Dfj5Vpa27g3CzX7EsFw7VqyWCYGEHBvDte91pfQpZtJnAAqXyaFJMbtWP3kQHNU5EzEQQfiCikYh3UVUMcTGQ5cSjTDXR8af5sDqaZsyLec56ifTnzonzVBSEs71irteBUPpMdihdQDWV9eGLGa5gAZGZbKp5gSW4"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.615)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.616)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQS7fZiqFW5oMB4jRcv5eedJR1Cpjq2WEs8poXDxoK51iPiJKDo74sx4doj6RRvMziiRwacr8XLpSAFpTqnH8PPmFhtbxaZPRYnUeFvUorBjBygEvk6MuBNDvRYWDXTExfLowPzQJhoQwBPeaAMvFp9Uo3xNoCkvKtbMfvJakuCVyTzk9KuJHBc1n8y1mLAg7Dzr6gF9g1ytDN"
  }
}
```

#### initiator ---> (2018-10-16 20:25:53.617)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4yKJRLxzoTWtzSqGzb6uraiXykPgvTNBUiLgX9n2rTrFDDz9bgt9gBagqpZtwjvptQSRw2SWQ11q7sthbf2Crrt93UxAaKtJxHGr6bD3cMyb62KQsCaDEKHa4nAig2wJVt5sTj2vjRNzHMuezsqoe73jAr16vLmFX6eW1mSNxPSMh3CDwTyJVtbNyb9KUieuwCSy5VJE75WXe4jVgXsXxjEbHLC1TQnTZLhqNbprRjTm1gEoj2MTZYpjEr8zMtEehhibMUURvMLgMR7HYD4bjofn2xpVxpeX6ez7qwByKjfXewq"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.623)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkaxp7drx6sBcc8qZjZ4dWjRq6bPc3kACLiGjbx4Lp58BrTbDqLg3TYGyc6V7Ybd7CGndU95huEcg6Ad98xvgfdi1sjQSX4FaQikwEYygbjj6ny5R2Wi9R6R3mx8d2eW4A4nsYX9Y3oUS1zthET2hsUF6vcvrK51VRsFa1GhZcioNZG1sbini32JYa6wXWbrqfqydszzxwv7sEHDXeoj99E8zkZvoRaftcGSMCX4eJtey8utNAvCeCqQ1YyDTAdLpx4YkRwDr3nGCwFedvi1LGEwQStJ9D669NtwtzV4LCH9GSnPiNpEwmWADgvawhAwcrrgDomwX3iwC5gNpd3ZVLNu1BMuD98yud6SD1aGJaGJvHEheeiQdYjN8uxtgAwvwQpVSEJ5Ud",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### responder <--- (2018-10-16 20:25:53.624)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkaxp7drx6sBcc8qZjZ4dWjRq6bPc3kACLiGjbx4Lp58BrTbDqLg3TYGyc6V7Ybd7CGndU95huEcg6Ad98xvgfdi1sjQSX4FaQikwEYygbjj6ny5R2Wi9R6R3mx8d2eW4A4nsYX9Y3oUS1zthET2hsUF6vcvrK51VRsFa1GhZcioNZG1sbini32JYa6wXWbrqfqydszzxwv7sEHDXeoj99E8zkZvoRaftcGSMCX4eJtey8utNAvCeCqQ1YyDTAdLpx4YkRwDr3nGCwFedvi1LGEwQStJ9D669NtwtzV4LCH9GSnPiNpEwmWADgvawhAwcrrgDomwX3iwC5gNpd3ZVLNu1BMuD98yud6SD1aGJaGJvHEheeiQdYjN8uxtgAwvwQpVSEJ5Ud",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.628)
```javascript
{
  "id": -576460752303423446,
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

#### initiator <--- (2018-10-16 20:25:53.629)
```javascript
{
  "id": -576460752303423445,
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

#### initiator ---> (2018-10-16 20:25:53.629)
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

#### initiator <--- (2018-10-16 20:25:53.633)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQS7fZiqFW5oMB4jRcv5eedJR1Cpjq2WEs8poXDxoK51iPiPjjeecM9QMjV5xYpUjB9WuR8bPSGXaDyiKoX8tfa75DUeEWjbbTNB3mPw3eCqRFQM5v2JpQS1125wzcxkc5xzU4VjD9tnao68ceYMW4oRWLB5Y95QPQMRJ9XoK5ccv9CLRAVGwdjPRqKLvwDFiuRKQhTv9rCQ4v"
  }
}
```

#### initiator ---> (2018-10-16 20:25:53.634)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4vF3RApGTqnj7T34uF3F68nQt1fVpW4t9doSrUQgfLjDpqYwZhXH2n4fk1711bh3HGKuwobtTe5JvMB3YbATKdNBH3PQYEvSvcPG1gcSNhaMHwssphcHQYbuduRx5xUsCEYfKd4qbCwvAb7GT5inctUZy6rdcmCpC9qcGy7yc5r9N1L9vkpqE1YBDVefnsVYoZ1uBjcuA8EAc4QqTmUAXyfPQft2PrCjxUjj4DL2HGPbYYcCEJLqJG22Kkq4q7KmPaYQD2VyB2HJ4LwyE72y6ZqnMdx7cVxAyQTrPrRAM49eJJJ"
  }
}
```

#### responder <--- (2018-10-16 20:25:53.671)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### responder <--- (2018-10-16 20:25:53.672)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQS7fZiqFW5oMB4jRcv5eedJR1Cpjq2WEs8poXDxoK51iPiPjjeecM9QMjV5xYpUjB9WuR8bPSGXaDyiKoX8tfa75DUeEWjbbTNB3mPw3eCqRFQM5v2JpQS1125wzcxkc5xzU4VjD9tnao68ceYMW4oRWLB5Y95QPQMRJ9XoK5ccv9CLRAVGwdjPRqKLvwDFiuRKQhTv9rCQ4v"
  }
}
```

#### responder ---> (2018-10-16 20:25:53.675)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4vnYgh5hzD8WJxEdvgahjfktFmXauPXgXEmo1E7JqXKzuCFojaZUMCT3jsgjYhrZH8rWoKbHLvdp9vs5tke89ubAZfbNRW3tuLa2YNJbagzRwuKFezDTaKbK6h8KgfVDdr7NZnrKtHJyMbf7iqDVM9N8mfxNpgm8p1KaewHsbzho8f4wdffpRDcyoVoQypVw4sPGtb5nXarYfL7KWNJUhLQ8UEK2FexeapMDvdYWKTVjUjeDzeYy7h41Sio1meLUqdNb29GLVMURVKkhPyu8mENbKgC74gaYpSPiU7RVsvTQ2Nf"
  }
}
```

#### responder <--- (2018-10-16 20:25:53.690)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkc6Vq1eDmxujSGkSWjG34Qdb8S5dj4fbFcC9dr7RPsBe4ppkXQfdyaxNPqJDy4VnDRpskSh2pHVAUmrvzfUketyw3upkXRxuAQQFyCy7yzL6sq82RgtLdQ9UspBPwBtDy9odZjUyrMqS8D1AFssdkwqacvCJM6r83o6TfUrfVjc84sGMZjr4zS8S23PbJNE2ZjdoMwhfUVxd4nEVooe6JxDSe2fDEHtwu2RJTFMpF29vkZZry8ebJNsuMaYseaLAyJmrtdQ1t3pcoUdZzEFLr1AxAuMDwr9SsWDqqv4o8HMzKPFSdWYwF1BQJtk6PN5iiRB3cvVikR3FQuYAD6feL5yb76qr7CYRLAgnjBfuE5Zmu5saKWAXuNEmYbH6j6UTFWZTNPAeB",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.691)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkc6Vq1eDmxujSGkSWjG34Qdb8S5dj4fbFcC9dr7RPsBe4ppkXQfdyaxNPqJDy4VnDRpskSh2pHVAUmrvzfUketyw3upkXRxuAQQFyCy7yzL6sq82RgtLdQ9UspBPwBtDy9odZjUyrMqS8D1AFssdkwqacvCJM6r83o6TfUrfVjc84sGMZjr4zS8S23PbJNE2ZjdoMwhfUVxd4nEVooe6JxDSe2fDEHtwu2RJTFMpF29vkZZry8ebJNsuMaYseaLAyJmrtdQ1t3pcoUdZzEFLr1AxAuMDwr9SsWDqqv4o8HMzKPFSdWYwF1BQJtk6PN5iiRB3cvVikR3FQuYAD6feL5yb76qr7CYRLAgnjBfuE5Zmu5saKWAXuNEmYbH6j6UTFWZTNPAeB",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.697)
```javascript
{
  "id": -576460752303423444,
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

#### initiator <--- (2018-10-16 20:25:53.699)
```javascript
{
  "id": -576460752303423443,
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

#### responder ---> (2018-10-16 20:25:53.699)
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

#### responder <--- (2018-10-16 20:25:53.703)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQS7fZiqFW5oMB4jRcv5eedJR1Cpjq2WEs8poXDxoK51iPiVAFWC9pLk5fF5VfibgiH313jjGfJCER5vF5dEdksGTks8nou6A46N8a7NDRfHNB3Wr16UY38jAJ7MNvskhyCpC2SJ2YxYMzkPYf8eAf8fKYZhsRRM5etRn5e3fvKDVCq4TqYkhiStDYmRhK76moou6ccpctb2aE"
  }
}
```

#### responder ---> (2018-10-16 20:25:53.704)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4oAKovj5eh8ZgjuLuUMgSLoHHFPRwAy5P7ZMvVuCS4zNGeHQX9KcA919tQ6gnefZysuj83vHbPowzgPHdkzYaT7rkD3CsLwUmhoLTgENM282SAUZSAMM8rCAKth2bfcq7dfJpjx8wsxgSVTYNh7K6K8Lg9DueoCHcmWma3MsBnwGoW1KAUyfPn8NXhwQzjAV43QASV7bfyaXTqvDEHZKE3XP4DBNfoiX55HH7LscD4uQNeb9zqVFh3xWzzJEdLekhjmNniLtvB4k3UwmaqYKFKzuXUcCgWJx2GritJEwtMHekLJ"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.723)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.724)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQS7fZiqFW5oMB4jRcv5eedJR1Cpjq2WEs8poXDxoK51iPiVAFWC9pLk5fF5VfibgiH313jjGfJCER5vF5dEdksGTks8nou6A46N8a7NDRfHNB3Wr16UY38jAJ7MNvskhyCpC2SJ2YxYMzkPYf8eAf8fKYZhsRRM5etRn5e3fvKDVCq4TqYkhiStDYmRhK76moou6ccpctb2aE"
  }
}
```

#### initiator ---> (2018-10-16 20:25:53.724)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4riNa4A87TQuMSwHfVf2yropH9ahFofhqQjr2T6fkaS73dRQtw34GaHwdGjVh3i1C4H5eRtbfad6Kt4dLRsooMhiNtvspYnFGXUqE4BaHYsc9hUEhHwub5gHFXqjt5jzWxbCf3u1hWRdL1PTBgLrfzUdv6REKb39TMNsj4UzcjMSwAE1EnvYgGStcBG1fGUgrkbT62KAq4tUm4U1D4nEp55seG7KAGzrXK9Dd5Gf5cidHbKoxMKX11UvxHBiw6C8kmDzKUp2wb27Q5h639VETwBbu1MbAD9pCeqFHk6HAKMbdJD"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.730)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkPvQV8LLG75byTJWzNA4D7vXdN1Wk6ucGHvrCxEgX3XoXerS3EAZkSSfhPzC1vR813AUiMJHE6qwJ4HrAtRxcW86yk58eBTSAVxJaT4XmQbi92uCUkzb88un5nwTYjnmGfPUU4bea1qNQL1Y8HUTPc6gMn6Gy9GCYhQkennLoezSUn78E9q9u7KTZJtjaAxpttgt5nR3htfYE5ChDxvUcUx2CAf5uxrMp9Q184NfCMYrf5znCxyStYAF724vGTrzqLZv2iREgYhC52TDz9JCf6FGZtnsnDWVxdr71DY3H5M4kw1zTB9DpsLgLm1WKwqxqF9PzqLRvQmQ8vwcMjXFKKUFU7Zo9RZQwzJ1XH1wamRYfCZspmQqEFhfmEcy1mbkmuZY8UuGt",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### responder <--- (2018-10-16 20:25:53.731)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkPvQV8LLG75byTJWzNA4D7vXdN1Wk6ucGHvrCxEgX3XoXerS3EAZkSSfhPzC1vR813AUiMJHE6qwJ4HrAtRxcW86yk58eBTSAVxJaT4XmQbi92uCUkzb88un5nwTYjnmGfPUU4bea1qNQL1Y8HUTPc6gMn6Gy9GCYhQkennLoezSUn78E9q9u7KTZJtjaAxpttgt5nR3htfYE5ChDxvUcUx2CAf5uxrMp9Q184NfCMYrf5znCxyStYAF724vGTrzqLZv2iREgYhC52TDz9JCf6FGZtnsnDWVxdr71DY3H5M4kw1zTB9DpsLgLm1WKwqxqF9PzqLRvQmQ8vwcMjXFKKUFU7Zo9RZQwzJ1XH1wamRYfCZspmQqEFhfmEcy1mbkmuZY8UuGt",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.735)
```javascript
{
  "id": -576460752303423442,
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

#### initiator ---> (2018-10-16 20:25:53.792)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### initiator <--- (2018-10-16 20:25:53.795)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "tx": "tx_2M9ipLgcZPKwB7EThiQrx1zFY65wM5SZWssEu6wtWLwsaTr2sDsixDs3qExYB5ukUEaX6AKgPiaPLYq4q99UDjGtq4fQ2z49n2Mkt4J9h49zccZKTuaXg"
  }
}
```

#### initiator ---> (2018-10-16 20:25:53.796)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "tx": "tx_2iJcVi27J8a1EdsZgeerrUxsgBQNr4jpwThQthf1SywHamjeRzi9KnBXEoHXKiueQyUoq36qaJecX7ehtnxYz5qXJxwzr2SzkgJGVnce9FskdwL1KDYThMX9Ri6ZncGj85Ti3ZbryhbLQGxdgKzcVodroQfq9AY3y1aaBFKqPh6PGJW9pv85cqsRPyPuBYafh54yca4rpRPqKmMa6f7hmVcPUv"
  }
}
```

#### responder <--- (2018-10-16 20:25:53.797)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "tx": "tx_2M9ipLgcZPKwB7EThiQrx1zFY65wM5SZWssEu6wtWLwsaTr2sDsixDs3qExYB5ukUEaX6AKgPiaPLYq4q99UDjGtq4fQ2z49n2Mkt4J9h49zccZKTuaXg"
  }
}
```

#### responder ---> (2018-10-16 20:25:53.798)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "tx": "tx_2iJcVi27J8a1TiU8fzRWBezKp4mpUSEeTt6WrDE6HPs4uQ2NrwC1v3DemMppwzgtLpNtJWkp9Hgty6unfFHyyJYw59pdVYF2SPFEFyqyew7MbSSGcatDrEWdDWEMKxNtiWttNnZFhfwJNW8JQSwvTBr3LjhGgZ9K9hr14AhCL252vAc9DCB6dEjTWTUBaWpxdWLjbG3iPfLzf5ou7aFH1RT6YE"
  }
}
```

#### responder <--- (2018-10-16 20:25:53.800)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3wu1WL1txa1aPinDvVZDTZmonZNZkS79s4oYH8KovJVaJ695VzaMShUwHACkKrd8S6LDp9zSshaRSgoTHAeuUPL3uPZvWb2gSjiUHPTgBLPjd3zP2j1ub6bZYc3hXFApGnsudFVRTCCbz3N3MQApGZtDEVFpcZdrGyQRxATzUhaPsR6gCtTKomMuLqEdbN21b69AEk7zQXR23Sr5Btro3KBJyWFJfS8nBPY3q386nH5urfkMKxV6FvCUj5MZKFcoNXCCdENtax5mroCiXL45NSPK4dwgxDsrreLgXtH68n2vLeZZQ7Bw",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### responder <--- (2018-10-16 20:25:53.800)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "close_mutual",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### responder <--- (2018-10-16 20:25:53.800)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.807)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3wu1WL1txa1aPinDvVZDTZmonZNZkS79s4oYH8KovJVaJ695VzaMShUwHACkKrd8S6LDp9zSshaRSgoTHAeuUPL3uPZvWb2gSjiUHPTgBLPjd3zP2j1ub6bZYc3hXFApGnsudFVRTCCbz3N3MQApGZtDEVFpcZdrGyQRxATzUhaPsR6gCtTKomMuLqEdbN21b69AEk7zQXR23Sr5Btro3KBJyWFJfS8nBPY3q386nH5urfkMKxV6FvCUj5MZKFcoNXCCdENtax5mroCiXL45NSPK4dwgxDsrreLgXtH68n2vLeZZQ7Bw",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.807)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "close_mutual",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```

#### initiator <--- (2018-10-16 20:25:53.807)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_2LGFRGJdcFU9SEGHvutWY29mfUgiXdrNFcAQAgUnto58fjTdtB"
  }
}
```
