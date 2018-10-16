
#### initiator init (2018-10-16 20:06:14.141)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW&role=initiator
```

#### responder init (2018-10-16 20:06:14.145)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_14PiMMZmdiQotKBkRmJF8jtLQ8pM4Ntjmf1H22eavngdXnHBz&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_q3dW7XXSkwvDQo4VwWFt5fFuVMhVsjUtFHbmseca5B7oukByW&role=responder
```

#### responder <--- (2018-10-16 20:06:15.146)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 20:06:15.148)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 20:06:15.157)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpAKyYf94hoccj3VfMcLCNKgGhdgxiiPcV8DEwHrhHxH4cTaJe4u8Enx3nQbRKu1nQBP2Suk9ejZcQcsUT5XGWuA1qSSdqjYyyNURtiFgqthSZdPEQiKa5f4FaZaVszregXvP3kxQmMW9rzj59PkMnTZJ1KqPAzKj"
  }
}
```

#### initiator ---> (2018-10-16 20:06:15.193)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HnYNs9FvVpnLjnjc4pBAFwoXZ6mWPDVuLK9Z8NJdLKQdKPnRfkmQp9bzpAAiJhwiYVn6y76Du8PBVC42bJjKyb1GuWzRHuuwFRNZd88ULjXx45zrP9DUTNnnBKY26PCxsEgzys9eZBEWDhdQ16rfDcHJoABx5y1FPV4dhQYs7kRQ3Sb9CxoTXQaBHP9fELzWYKrvipEDWgKQqESbL3axG5oEqwMUDxNkxLPtnC2fb4SAhRD4gncEx9zWuXrmCqVqo"
  }
}
```

#### responder <--- (2018-10-16 20:06:15.194)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 20:06:15.195)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpAKyYf94hoccj3VfMcLCNKgGhdgxiiPcV8DEwHrhHxH4cTaJe4u8Enx3nQbRKu1nQBP2Suk9ejZcQcsUT5XGWuA1qSSdqjYyyNURtiFgqthSZdPEQiKa5f4FaZaVszregXvP3kxQmMW9rzj59PkMnTZJ1KqPAzKj"
  }
}
```

#### responder ---> (2018-10-16 20:06:15.196)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HkHj6pi9tXJ99mNncGnbE3Zcctxm4ieVt7ntbdJNH4GygtWbEbKY5cSkgi3JCcqWzo8QPnXJdzVUSZrp8Bu3YyLB6mJLvbb831iq5tyC6EBic25p5uYaWTbk7tSA1sXpQHByL8dJWdo1XHudnnonkGhp87ufnVSmBAr4FAcn2k6nvjojYf3BTWpeR2iimKmei5GywudcxQgs18hQauESoqWVbdukFsCDhyot59Vxy6piFzpqkbD9uHXo8amE5oeEX"
  }
}
```

#### initiator <--- (2018-10-16 20:06:15.198)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 20:06:15.198)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmNhkgxNKdUzBwwT746XSrVYrNsASd2hjM6i327ZVkkMDe5tSPoBdSuCB5HSBp42bwjzNDC3g3AQGfFrxGTneTuPBFUxXgJHpLTErQPyXqwhiUmrunjArvhZMj6BeYqCj97rXf4FDkWcW6eEV67rcM2LcpngE47jw5QKiV3p9k9Qqoz5uRKNMJc3czKHnKL46bpCAfJuqwPAEG3RehbrU3kvkn1nZgyJStCoVHsk5eWPS2VJSCAeZryfZgZEPk6FQf7rWceEKafm26qR7bubUAQeZGEEP2LnCkCtra24SUSjcDxvq3w3GZCakdVgkQD7YzabJp8YSd5f47fdQF4tqUAVn17D"
  }
}
```

#### initiator <--- (2018-10-16 20:06:15.199)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmNhkgxNKdUzBwwT746XSrVYrNsASd2hjM6i327ZVkkMDe5tSPoBdSuCB5HSBp42bwjzNDC3g3AQGfFrxGTneTuPBFUxXgJHpLTErQPyXqwhiUmrunjArvhZMj6BeYqCj97rXf4FDkWcW6eEV67rcM2LcpngE47jw5QKiV3p9k9Qqoz5uRKNMJc3czKHnKL46bpCAfJuqwPAEG3RehbrU3kvkn1nZgyJStCoVHsk5eWPS2VJSCAeZryfZgZEPk6FQf7rWceEKafm26qR7bubUAQeZGEEP2LnCkCtra24SUSjcDxvq3w3GZCakdVgkQD7YzabJp8YSd5f47fdQF4tqUAVn17D"
  }
}
```

#### initiator <--- (2018-10-16 20:06:15.679)
```javascript
{
  "id": -576460752303423430,
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

#### initiator <--- (2018-10-16 20:06:16.213)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### responder <--- (2018-10-16 20:06:16.214)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### initiator <--- (2018-10-16 20:06:16.214)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### responder <--- (2018-10-16 20:06:16.215)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### initiator <--- (2018-10-16 20:06:16.218)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### responder <--- (2018-10-16 20:06:16.219)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### initiator <--- (2018-10-16 20:06:16.220)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmNhkgxNKdUzBwwT746XSrVYrNsASd2hjM6i327ZVkkMDe5tSPoBdSuCB5HSBp42bwjzNDC3g3AQGfFrxGTneTuPBFUxXgJHpLTErQPyXqwhiUmrunjArvhZMj6BeYqCj97rXf4FDkWcW6eEV67rcM2LcpngE47jw5QKiV3p9k9Qqoz5uRKNMJc3czKHnKL46bpCAfJuqwPAEG3RehbrU3kvkn1nZgyJStCoVHsk5eWPS2VJSCAeZryfZgZEPk6FQf7rWceEKafm26qR7bubUAQeZGEEP2LnCkCtra24SUSjcDxvq3w3GZCakdVgkQD7YzabJp8YSd5f47fdQF4tqUAVn17D",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### responder <--- (2018-10-16 20:06:16.221)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmNhkgxNKdUzBwwT746XSrVYrNsASd2hjM6i327ZVkkMDe5tSPoBdSuCB5HSBp42bwjzNDC3g3AQGfFrxGTneTuPBFUxXgJHpLTErQPyXqwhiUmrunjArvhZMj6BeYqCj97rXf4FDkWcW6eEV67rcM2LcpngE47jw5QKiV3p9k9Qqoz5uRKNMJc3czKHnKL46bpCAfJuqwPAEG3RehbrU3kvkn1nZgyJStCoVHsk5eWPS2VJSCAeZryfZgZEPk6FQf7rWceEKafm26qR7bubUAQeZGEEP2LnCkCtra24SUSjcDxvq3w3GZCakdVgkQD7YzabJp8YSd5f47fdQF4tqUAVn17D",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

##### initiator: (2018-10-16 20:06:16.671)
> Funding has been confirmed locally on-chain

##### responder: (2018-10-16 20:06:16.671)
> Funding has been confirmed locally on-chain

##### initiator: (2018-10-16 20:06:16.671)
> Funding has been confirmed on-chain by other party

##### responder: (2018-10-16 20:06:16.671)
> Funding has been confirmed on-chain by other party

##### initiator: (2018-10-16 20:06:16.671)
> Channel is `open` and ready to use

##### responder: (2018-10-16 20:06:16.671)
> Channel is `open` and ready to use

#### initiator <--- (2018-10-16 20:06:16.703)
```javascript
{
  "id": -576460752303423429,
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

#### initiator ---> (2018-10-16 20:06:16.704)
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

#### initiator <--- (2018-10-16 20:06:16.708)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQQ8ZuaHrdfiMEUo4xVV4dWKfZvWaKHBu8L3QL4XhvexDoBHs4ZKt6gjBqwFjD27rh7in7NSqGHcLMzeN3w3Fah2ijmWjh2xPWiVavrYs8kPMJ1ZtTrtuiGASqXcyBLcGX7KcTNSz4WzAEV1ei5qwovkDJ2npnUScv5NDeRtdwyfU7NyZqigEmHqLX5ZerbtUedBixnTspQY5C"
  }
}
```

#### initiator ---> (2018-10-16 20:06:16.709)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4vpgKhpMrAhZcM2fGSmvqY8Yuujjq4LshrWDnfWYZsvkePpX2C84i17gjn7ahBhsovutNm5fWXsQW4XS7bZm3N5VSb9uf12KTeiUdgjaK4LU29Dy8dLrichzGhSKo2ndm7rCLb7Bek4MFnAK4hnaPJFMAQcnS59ydaCt3q5DQ4LeM8rmzqyjLUMZyxbSsWL3jAe43PJXaqZEjL5oKRffSoqew2FDCaYk9yAbyqdmaqgE9vvWPvxdCPgJ32GgvojbhQkxX8eExrfvrYPKaGxvKbgzC7R397iafcvekXHJPPCUTRx"
  }
}
```

#### responder <--- (2018-10-16 20:06:16.714)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### responder <--- (2018-10-16 20:06:16.714)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQQ8ZuaHrdfiMEUo4xVV4dWKfZvWaKHBu8L3QL4XhvexDoBHs4ZKt6gjBqwFjD27rh7in7NSqGHcLMzeN3w3Fah2ijmWjh2xPWiVavrYs8kPMJ1ZtTrtuiGASqXcyBLcGX7KcTNSz4WzAEV1ei5qwovkDJ2npnUScv5NDeRtdwyfU7NyZqigEmHqLX5ZerbtUedBixnTspQY5C"
  }
}
```

#### responder ---> (2018-10-16 20:06:16.715)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4ovg17Yp8Mjk2dBhweRCqzYFZx85HFBunDvbKbmXdzYkM13KLgBZW36yQXpMbN1HxBv2VVR6nLs6z8AjvxWHLMsGazMsMpmK56YW9P7FCHaRV6QRdvWZkkD5P1cu7kbW595m2mBmaKZhrXobU3VEN45J7WjBzXRFki6BpuCZUKe5dagzCdz5fKDh5N977GhRWLrSNrSfZ2nYR8XCZJSNDhNRgCEJrfk5Y8KwXfzoCR2VWPJ5stYiTXkhjQyYn3F3cg2KNFyC8zaxCb3X7zhYod7n2VBwukD9483XdeH9sHRRcR8"
  }
}
```

#### responder <--- (2018-10-16 20:06:16.720)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkREeWwuTB637L7kyi2f9pAkmizWpr79DMb94zQvPWRRUhG5GPZiASG5XSmq7N6wNw2XVz3SW8NtLKDVWvrvaU2SH9bxxUqzQLhwW3hKj2QvpsY7mq38CcyfoYogBSASB1oVrovq2UDNPeywiW365b4RbnX9xNbvxEvUtZbsSMNHWQsvXQA5nsj59nWcExSPd7dEnE7gpdYwDFafZo47uAGT3v3TCj3qk4NibdjuEps6xzFTuc8H4SSm5CWnAXx7iTPxzp6GraWAoFtgKEgPgoNXCZuVrdvFHxwsSsH7vbPCSaRaQr8yG16axbnL4wTxbPeRh4xP6ReEFtkzXZTqKBGwRBvhXkuyFtLVo7b6UXeySd4TPKGwSfJopNeUPbjAyWrjBEAtCa",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### initiator <--- (2018-10-16 20:06:16.721)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkREeWwuTB637L7kyi2f9pAkmizWpr79DMb94zQvPWRRUhG5GPZiASG5XSmq7N6wNw2XVz3SW8NtLKDVWvrvaU2SH9bxxUqzQLhwW3hKj2QvpsY7mq38CcyfoYogBSASB1oVrovq2UDNPeywiW365b4RbnX9xNbvxEvUtZbsSMNHWQsvXQA5nsj59nWcExSPd7dEnE7gpdYwDFafZo47uAGT3v3TCj3qk4NibdjuEps6xzFTuc8H4SSm5CWnAXx7iTPxzp6GraWAoFtgKEgPgoNXCZuVrdvFHxwsSsH7vbPCSaRaQr8yG16axbnL4wTxbPeRh4xP6ReEFtkzXZTqKBGwRBvhXkuyFtLVo7b6UXeySd4TPKGwSfJopNeUPbjAyWrjBEAtCa",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### initiator <--- (2018-10-16 20:06:16.726)
```javascript
{
  "id": -576460752303423428,
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

#### initiator <--- (2018-10-16 20:06:16.728)
```javascript
{
  "id": -576460752303423427,
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

#### responder ---> (2018-10-16 20:06:16.728)
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

#### responder <--- (2018-10-16 20:06:16.732)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQQ8ZuaHrdfiMEUo4xVV4dWKfZvWaKHBu8L3QL4XhvexDoBPHaQsRZt4umhFGKvFBQ5U9MBRD6zmgsBugYF5juT2QrB7YM7NR9xTGuyawuVLuAc5HHCMtuFFxGB7azEr3zpNxKKqHdP1MA4Ciavj8ZJfdcFEDuKAwHHVHwCSAvvSZtihYLvWwjt5kUrhPhG8fHxCQo6qgM19ra"
  }
}
```

#### responder ---> (2018-10-16 20:06:16.733)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak538BBFzaV5gA1LB9NzAnBCyPEp64sKYYtoA7u4psEwcbt2fkGpk2gMeh4JSMD1wfnfKqDoEhiaoJZ1CcV2LVWfDhaRwjaq8YqZsNzsJBsYF1jHanZuG4PjJ3ecYHDj1mywx3tfZBgDu7RZ1iWqibsH5oToqvg49UfJj5g8Y44vw4vALNWA8LgXjaumrvS3spBiSWohPw5j65uos2cGMb7nCyZzQoigesWmPHZxyk1o7JiTJsvx9kVKLehbb1iwkzruMegqX87namgqALFudbZopMUFTJ4jUttgBY5akSwDCXtFy"
  }
}
```

#### initiator <--- (2018-10-16 20:06:16.737)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### initiator <--- (2018-10-16 20:06:16.737)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQQ8ZuaHrdfiMEUo4xVV4dWKfZvWaKHBu8L3QL4XhvexDoBPHaQsRZt4umhFGKvFBQ5U9MBRD6zmgsBugYF5juT2QrB7YM7NR9xTGuyawuVLuAc5HHCMtuFFxGB7azEr3zpNxKKqHdP1MA4Ciavj8ZJfdcFEDuKAwHHVHwCSAvvSZtihYLvWwjt5kUrhPhG8fHxCQo6qgM19ra"
  }
}
```

#### initiator ---> (2018-10-16 20:06:16.738)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4t5Ffw7fy5YeAv9m9Tcr5Xnyj3BDMdgw9CR6wzTCDJC1CKcvH1tcE6XmVJYLnFQv3YYzBUecUfoFuSmztX6x7YtWYYPdcnG2Jqe32598cKGLMwtAriEoz4tPSRzpUXT6Hrx4ZPdQZmY3Rta8MjatV3P139Cfkd5hEz7eFocvmqebXAnEZiHSYBAe9t3FWL5pMvkudx8J22LwzG2XswYAvqiwXeV1xKDF9Um2QaSimpamRN94Y9ghoG7XCeCeNtrm7c5sLcv35TGqNRDEJEYMHbSHrXaNMDrbJ4VJ2HjTJr2wkhQ"
  }
}
```

#### initiator <--- (2018-10-16 20:06:16.743)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkYNFDZHLg5MVZgSEkidJ8Q9Cf75i1kP4e9Ze4kR82FoFXB4ESBwHMX6ueKPPCMkFXoJiWQ1Y1ZJbYAJHGDcTb7iM5wFsmXpwnSdUsCqFjiw8N2kyin3DRG1Uj8zF8xfPwzqZX3jinioxQFhTxYqdiPMM6UTCWYiKv8uDra6Zijx82u1Aa8iYUkD7mCFbfcDWwVJ8K5UuYohCbaHxbF9JseRBvRoBDE764VKLW5NvVCsZufKbMGRySHoAUsEcE7ozKtuZcrLVJLVeHLYWvYR33WabELVf3GzLwhMhYVPRS4QexcuHuWzpEHCyUoD8y7UjSG5pVJKtnckpivnkKsxPXnQfvSYjZkWVaWEQSiabU1jfhu9dByvhoDZBVDjzc7TkTvoXMh6w1",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### responder <--- (2018-10-16 20:06:16.744)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkYNFDZHLg5MVZgSEkidJ8Q9Cf75i1kP4e9Ze4kR82FoFXB4ESBwHMX6ueKPPCMkFXoJiWQ1Y1ZJbYAJHGDcTb7iM5wFsmXpwnSdUsCqFjiw8N2kyin3DRG1Uj8zF8xfPwzqZX3jinioxQFhTxYqdiPMM6UTCWYiKv8uDra6Zijx82u1Aa8iYUkD7mCFbfcDWwVJ8K5UuYohCbaHxbF9JseRBvRoBDE764VKLW5NvVCsZufKbMGRySHoAUsEcE7ozKtuZcrLVJLVeHLYWvYR33WabELVf3GzLwhMhYVPRS4QexcuHuWzpEHCyUoD8y7UjSG5pVJKtnckpivnkKsxPXnQfvSYjZkWVaWEQSiabU1jfhu9dByvhoDZBVDjzc7TkTvoXMh6w1",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### initiator <--- (2018-10-16 20:06:16.748)
```javascript
{
  "id": -576460752303423426,
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

#### initiator <--- (2018-10-16 20:06:16.750)
```javascript
{
  "id": -576460752303423425,
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

#### responder ---> (2018-10-16 20:06:16.750)
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

#### responder <--- (2018-10-16 20:06:16.753)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQQ8ZuaHrdfiMEUo4xVV4dWKfZvWaKHBu8L3QL4XhvexDoBUi6GQy35QdhTEoSpN2Prmg5jrnAyTazbxaAAZVbBn1sfNxTnDnQcQ2552ehE7zGHiEuhRDL8WaCTYAgx6vekP5dYn9Yxa4ZjaCqK65yoFtrYtnikc4ZRc5DNa3PRXdaEBsqM2AqiKi18FHrKVf1jRCjEm2SoXNe"
  }
}
```

#### responder ---> (2018-10-16 20:06:16.754)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak51pJ2eoapqhT9MzjJLsKK6VMsSuAMcBNVSJEJGMG87ZvjLVyxZxWzD79jkYk98HwQPrDnn7dQqcV2a1UdyDNtP1CXG6uBdBeUuqpWeJRLi2Kgss1okdfpS6e9HaXeSrGAoDYvMZoajQEKCvm4byjvP75pJAqYzxBy4d6wUzHwLo2teEp6A2pgzQm8LfdD33ENCjrErSyaEZCdKMfbW5d3KHyTJCmeQBZp9423NCy6WjmQoKeCqJVamGpWNfNW75DRPFtBZwBzF4DjmTSDqGCj7ZfdeEjXR9FGdFrxfojRQT1aiK"
  }
}
```

#### initiator <--- (2018-10-16 20:06:16.758)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### initiator <--- (2018-10-16 20:06:16.758)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQQ8ZuaHrdfiMEUo4xVV4dWKfZvWaKHBu8L3QL4XhvexDoBUi6GQy35QdhTEoSpN2Prmg5jrnAyTazbxaAAZVbBn1sfNxTnDnQcQ2552ehE7zGHiEuhRDL8WaCTYAgx6vekP5dYn9Yxa4ZjaCqK65yoFtrYtnikc4ZRc5DNa3PRXdaEBsqM2AqiKi18FHrKVf1jRCjEm2SoXNe"
  }
}
```

#### initiator ---> (2018-10-16 20:06:16.759)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak54zRenr55fgC6EPDDoTWJ2WaTcRWDhv2T1dWvG3XWaBKKXmjGKTwAg6F4MebcETzvaBp4JfuRR98SNJDDjpWo4ZNLFPQMsP4zEHqGpBeQeRNtVQ4Vsy7Ghrk1ebvR7ZGCswmxVbdZazMtTGSzKfio7wAVFPSQALHEZnBHgkURBH115o2o7a6rFyUxgmynVALB6BPzRrQDtM8k2XvBDXJ6aFqWcrSrjYNjkS8ha3oBLR86yCrWEpq7V6tzomJbbqwjjUEt9pkTy9X1Ro2bLw4kBuRVq1SmtrLLjT4UDgn8A7kAV7"
  }
}
```

#### initiator <--- (2018-10-16 20:06:16.764)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkmgDqfWUhBGzAtdASTwLnFU5RX4Dk3zabFPvahzMtuv1TftK3LvzboxaK6DeUnogwWXtRwmfNBTEzi1MVomFfyEGYQVc9ekgGxtTACk8ywEMV16Xsf2LFwAmqGVB2F69frLBdbadWZZJi42d18umFxBRhc229VKid1zhkXAEpbYYTeTf5XAkFB6oXfLgzTkeNny715nDhZR12E2T1hFiCivPQsmMay7wrw46YgsZf6XTrd2gacQ9Xo9ZF8j16GLLsbSV8ajtgEbU6FR1JiyPYovoUPyGKNYHHYCFkM7W9SSVFNXeXC2LavT1UJGBxgM6jYY7f2vkX3FrvQXLaNQWgHz7fC3pX2nRCtenMLePG17He2hemHqohfvLAMLNBrNLPdVKWu7AR",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### responder <--- (2018-10-16 20:06:16.764)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkmgDqfWUhBGzAtdASTwLnFU5RX4Dk3zabFPvahzMtuv1TftK3LvzboxaK6DeUnogwWXtRwmfNBTEzi1MVomFfyEGYQVc9ekgGxtTACk8ywEMV16Xsf2LFwAmqGVB2F69frLBdbadWZZJi42d18umFxBRhc229VKid1zhkXAEpbYYTeTf5XAkFB6oXfLgzTkeNny715nDhZR12E2T1hFiCivPQsmMay7wrw46YgsZf6XTrd2gacQ9Xo9ZF8j16GLLsbSV8ajtgEbU6FR1JiyPYovoUPyGKNYHHYCFkM7W9SSVFNXeXC2LavT1UJGBxgM6jYY7f2vkX3FrvQXLaNQWgHz7fC3pX2nRCtenMLePG17He2hemHqohfvLAMLNBrNLPdVKWu7AR",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### initiator <--- (2018-10-16 20:06:16.769)
```javascript
{
  "id": -576460752303423424,
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

#### initiator <--- (2018-10-16 20:06:16.770)
```javascript
{
  "id": -576460752303423423,
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

#### initiator ---> (2018-10-16 20:06:16.770)
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

#### initiator <--- (2018-10-16 20:06:16.773)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQQ8ZuaHrdfiMEUo4xVV4dWKfZvWaKHBu8L3QL4XhvexDoBa8c7xWWGkMdDELZiUPgTdNK3mYUDg2kEo2uhUWduHXpEJz33WVGgKpQ8syVxicb4UmMN4rzuvJeNtiHUNtUuKzQ3HZqFgJTX87TEvp5QX12wnRxMVj38KXc5qiqM2RhE2MzNwVUfVHSANVmmYYWJr5EmBfH3j6w"
  }
}
```

#### initiator ---> (2018-10-16 20:06:16.774)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4kbJZVtD6iXLSX2kuz37Hp27sQxrcpbZAhmnBE5Prxs9NZ9HzF7dgQDNccA9nn3hj4o4HKPrqEWxgGT76sYreZ37F9TaZpqaJGvzAJx8uvrPc4Ep5wsmsmLMcgJPhobY7Cj8MeAbZ48N16qQHh94GfuxQQS46MVHR1BhZEge9LhaHadJBkAYiUW18JLpK2hD23FWNE158a3C56fe3qk374mmTXFKtFjKtTAGGkcHDMXHCj5jPSFmb7f8f3eu9QJFZNi62fB9gW5FToLPgJmJ9eV2VvwqaHXEUCGduUZpBHTmhHj"
  }
}
```

#### responder <--- (2018-10-16 20:06:16.807)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### responder <--- (2018-10-16 20:06:16.808)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQQ8ZuaHrdfiMEUo4xVV4dWKfZvWaKHBu8L3QL4XhvexDoBa8c7xWWGkMdDELZiUPgTdNK3mYUDg2kEo2uhUWduHXpEJz33WVGgKpQ8syVxicb4UmMN4rzuvJeNtiHUNtUuKzQ3HZqFgJTX87TEvp5QX12wnRxMVj38KXc5qiqM2RhE2MzNwVUfVHSANVmmYYWJr5EmBfH3j6w"
  }
}
```

#### responder ---> (2018-10-16 20:06:16.809)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak54BRUAnwbi9anKv3NYsTFHNdosrM7iWBiDcbzcZdEpLS8Hcnd5BLvM1xKEq4MkUChhfUGac8cgSMYUZT5FqHih3EF5WQEgkbrfkUJ16dJeQMD5Gio6hnP5TTwTU8JmbPukuBgi341yRQMPnGF3YPPB6shW61sgxjWbgicqarwMUkvpajspW83W5K7D2criidXWj1Wg77LPHrUiEWoyVixQ8o8d8XFRjgL58MwKSoXNfeXiXPBuc2WXncb4qYGvYDCrLmLKy7CyquX6mntPZocQV4T1HerdxuNQTncwBc2w3WiAW"
  }
}
```

#### responder <--- (2018-10-16 20:06:16.813)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkKWDHmyy3nLQkSvEBF3Hc7Np5vPqLeqb7DjPAZCp371pY99sTMDxD3MNDAyw8K3fETgejBSZyZzivf6f3AWhgSofLKvFcYkBDWSRqnfMXvpanDe5miFEKwDFKPUSbQtGeG89FEYzUiyJy5dkdt8k42s3VXVqSNfLNfEnfY5hLYkPvrPxcZWmdJLcWEt94GwBrEHnyig6jJzFoaEpPrVTpRwoHFS8447D69YNz7CVEhDgAk2k2ZPTBWqJG63NYhNKPMgu3FC6y7qDgfdmshe99xKcasR5WbBS2r2fRCiRqEUGbJou1HhzgXLTj5rpvnYiY1J63CGJK3emitCw2Kc7YvEHWpoDj5mWcpEWLNqxx6ZL7RNvXXmXUqdC9Sa6uq6tcHWWnm2wB",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### initiator <--- (2018-10-16 20:06:16.814)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkKWDHmyy3nLQkSvEBF3Hc7Np5vPqLeqb7DjPAZCp371pY99sTMDxD3MNDAyw8K3fETgejBSZyZzivf6f3AWhgSofLKvFcYkBDWSRqnfMXvpanDe5miFEKwDFKPUSbQtGeG89FEYzUiyJy5dkdt8k42s3VXVqSNfLNfEnfY5hLYkPvrPxcZWmdJLcWEt94GwBrEHnyig6jJzFoaEpPrVTpRwoHFS8447D69YNz7CVEhDgAk2k2ZPTBWqJG63NYhNKPMgu3FC6y7qDgfdmshe99xKcasR5WbBS2r2fRCiRqEUGbJou1HhzgXLTj5rpvnYiY1J63CGJK3emitCw2Kc7YvEHWpoDj5mWcpEWLNqxx6ZL7RNvXXmXUqdC9Sa6uq6tcHWWnm2wB",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### initiator <--- (2018-10-16 20:06:16.818)
```javascript
{
  "id": -576460752303423422,
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

#### initiator <--- (2018-10-16 20:06:16.819)
```javascript
{
  "id": -576460752303423421,
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

#### responder ---> (2018-10-16 20:06:16.819)
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

#### responder <--- (2018-10-16 20:06:16.823)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQQ8ZuaHrdfiMEUo4xVV4dWKfZvWaKHBu8L3QL4XhvexDoBfZ7yW3yU65YyDsgcbiPRNjYrjvJvqPFS4MQ1WzxfHDvdunh7vWuvHWPFv4GhgATezAAhXrBu1p52PL6NcfxcPLFzfsQ7hVP6KBL5ozpnSRMADrwR2pKigBNi2xQYF9K4WCLzUbNZC9QvfDqFvKbYUCfcRxNVLSP"
  }
}
```

#### responder ---> (2018-10-16 20:06:16.823)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak54fA2Y4W2S3q7MXZhiuYy3hdBDaYLV3ZmC9fdvBBaq8sEpQh7dA6wYzBEzb9aYycuSYGzAV8MTHWisCGutFkrUMaeWzFHnyk2VHHCY6c6zSz82ofgDgnxpLgKjcvS1Z2RaPvFybqMoiECrcgX76ngsFZ6yx8pHHSPFwNXSE8yxn8CX4WcJcc1PGJub6pvwq1rCKxdVodXUeh5VVwzbm9j54XpKo3cLTiq56qiw5DbChJ3km39ZXuWMXYsGV4bzgeBu94G5ACXeUYVD1nxttNA5BqM2WnRJt9qZMJnUNHG7xUJ9k"
  }
}
```

#### initiator <--- (2018-10-16 20:06:16.863)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### initiator <--- (2018-10-16 20:06:16.865)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQQ8ZuaHrdfiMEUo4xVV4dWKfZvWaKHBu8L3QL4XhvexDoBfZ7yW3yU65YyDsgcbiPRNjYrjvJvqPFS4MQ1WzxfHDvdunh7vWuvHWPFv4GhgATezAAhXrBu1p52PL6NcfxcPLFzfsQ7hVP6KBL5ozpnSRMADrwR2pKigBNi2xQYF9K4WCLzUbNZC9QvfDqFvKbYUCfcRxNVLSP"
  }
}
```

#### initiator ---> (2018-10-16 20:06:16.868)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak58z2xHmaoES1PtQDKfyLwt7pQsuY15Yhrre95ReFs3ZEeZ6nAThZYcSKVzcfewcrkkEPMThoFGe2VaymunmETQkqtdZfW8rCc9mqnhXjYvVjXftDqxpC2eEpNLQrYmGshZzMsLUKtHMDFejHqqaBq8snerorsJyJ3BYi1RY1Ys1REzHJcVpuebgLpp2fbB2B4BYH3gBbtRRhRZrKoQEnCzoPV63mhEmhnmYvWN5sBHrenoQh7tCB5iBgmBnELGRxHWXyVGGGqNUnAAo7SKx6sesmYH5ENdRpVSQrgHYaW1zyCwy"
  }
}
```

#### initiator <--- (2018-10-16 20:06:16.881)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkrZeX6cyU2qR5z93vm5AwXe9NgoirtYfoL3GtZSEK9J6q7vQcmDuPX49Zw9WNamPKFGR42wHQUqAgvHrFNRvYVcLopxXGCPt676y2A58wCZcGxNNL3rW19tBfpB413zmyqgbP833ciPi7SSPYqZH1gL1zTpmTxpZdRTthyq1FrSJy3oZ2TKWaPCtoVqDNF4Zdd6S25AjARkKksXvoMq7S58DrmSQ6DoLJh3pXCch5zKXurPbYXbKzvcArRMR2GsVszGe7u77Gz43qYgbUt6JDypNxH8hXAek2TgEdYoAayfvSAL5RiEcsyonQWB6xwxbth816QVWLdRGsE53S2VQEnTgjzdVTS7h2UJBMQ7krTRwt9j9vNjYyacZQCm1R5wUxHduKSGo8",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### responder <--- (2018-10-16 20:06:16.882)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkrZeX6cyU2qR5z93vm5AwXe9NgoirtYfoL3GtZSEK9J6q7vQcmDuPX49Zw9WNamPKFGR42wHQUqAgvHrFNRvYVcLopxXGCPt676y2A58wCZcGxNNL3rW19tBfpB413zmyqgbP833ciPi7SSPYqZH1gL1zTpmTxpZdRTthyq1FrSJy3oZ2TKWaPCtoVqDNF4Zdd6S25AjARkKksXvoMq7S58DrmSQ6DoLJh3pXCch5zKXurPbYXbKzvcArRMR2GsVszGe7u77Gz43qYgbUt6JDypNxH8hXAek2TgEdYoAayfvSAL5RiEcsyonQWB6xwxbth816QVWLdRGsE53S2VQEnTgjzdVTS7h2UJBMQ7krTRwt9j9vNjYyacZQCm1R5wUxHduKSGo8",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### initiator <--- (2018-10-16 20:06:16.889)
```javascript
{
  "id": -576460752303423420,
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

#### responder ---> (2018-10-16 20:06:16.943)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

#### responder <--- (2018-10-16 20:06:16.948)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "tx": "tx_2C9es4FjHwJNb45vHZyEYktZJF51a6x7bN1evutWu12VJ67PiQjmTU6jqSGN8H8ZmrkGTThSkkuNJTV3crqfPbEs6fzP6PoCtd3QnXfsMUmb4FM3eDhTMsCVTZiJ8PbqyuQ5JeLP2rUjhGbzv5r51XWexYvF2G"
  }
}
```

#### responder ---> (2018-10-16 20:06:16.949)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "tx": "tx_2WsEQsiC5XsngMhzhH7ofwh2FJ63VR428cSgKH1BygweAZTY1NbfHj9oYdbVGCahT6D5fKVxsoBSvH9mpcgDmD5eR9ccARD1sJ4gtojJu1q8wNYmFHoVFPMw3kBXJRGgshVq2ddn1kZjnQotQf7L1if9KHgjWRJa4FhrytXYMrEu11LBK6XtNXLvoawMYbN5pRi4We7QnWvZwARqhmNtzvSJWS3ceoMw8u26KYCheoMr9Vwp7r4NymHhLuMpB8t6ERB"
  }
}
```

#### initiator <--- (2018-10-16 20:06:16.950)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "deposit_created",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### initiator <--- (2018-10-16 20:06:16.951)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "tx": "tx_2C9es4FjHwJNb45vHZyEYktZJF51a6x7bN1evutWu12VJ67PiQjmTU6jqSGN8H8ZmrkGTThSkkuNJTV3crqfPbEs6fzP6PoCtd3QnXfsMUmb4FM3eDhTMsCVTZiJ8PbqyuQ5JeLP2rUjhGbzv5r51XWexYvF2G"
  }
}
```

#### initiator ---> (2018-10-16 20:06:16.951)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "tx": "tx_2WsEQsiC5XsmmNUB5RejcDjLtrjMdxP6r8ZyFruw1cgyxtUHfdnERe8afnDz7bYQXL5v2ok2dqS6NyNkfVH8z2x5dhoejepZjz2KQGJRknT2QWFm67X7xp188zy79YmD1ZcGfvMSD8rWJYTjdLorE8QftUuWXuYpnEzsRNvFYci99JqEDNiT6wHym6PSXp2GDVTpZVZreWXsbmCRFV5e5En2gGrTjLzBSpTaVefyDdUmaebSwpEAws8dhWHGtGSisXK"
  }
}
```

#### initiator <--- (2018-10-16 20:06:16.953)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3cDMp6242sByL9f7EYWHWkkYD1tEpKL5ycgaDUQvmmGHy5YMx7JyzymH3bvD4GqirQyBWsUDwFD9HtnsVsEZw1xj5VGN6FoFXvVHs83um5JHqfNds3LcE6oqQRAsxQuAM7xaWiLut4mToN7eNUjY3z8HyZ44AxD3mgKYo3JaqnQnqPtaQ1PnkdLydMqnUMwLNHpCY1LcwccgzXYbTm4ULzx8kvMHLM4ubnNn6U2oJqnGwafVtgsNwj885Wzt3Ev5oLS5duoQEubHNqgQBeYgPJBQEHdRPwjCdJTcWNVz7BFG7AH9wA7F9DFaPhptc1ouUoPajKGNmi7fGEMbqXJfruYXooPH7",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### responder <--- (2018-10-16 20:06:16.954)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3cDMp6242sByL9f7EYWHWkkYD1tEpKL5ycgaDUQvmmGHy5YMx7JyzymH3bvD4GqirQyBWsUDwFD9HtnsVsEZw1xj5VGN6FoFXvVHs83um5JHqfNds3LcE6oqQRAsxQuAM7xaWiLut4mToN7eNUjY3z8HyZ44AxD3mgKYo3JaqnQnqPtaQ1PnkdLydMqnUMwLNHpCY1LcwccgzXYbTm4ULzx8kvMHLM4ubnNn6U2oJqnGwafVtgsNwj885Wzt3Ev5oLS5duoQEubHNqgQBeYgPJBQEHdRPwjCdJTcWNVz7BFG7AH9wA7F9DFaPhptc1ouUoPajKGNmi7fGEMbqXJfruYXooPH7",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### responder <--- (2018-10-16 20:06:18.914)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_deposit_locked",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### initiator <--- (2018-10-16 20:06:18.914)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_deposit_locked",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### initiator <--- (2018-10-16 20:06:18.915)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "deposit_locked",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### responder <--- (2018-10-16 20:06:18.915)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "deposit_locked",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### initiator <--- (2018-10-16 20:06:18.918)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3cDMp6242sByL9f7EYWHWkkYD1tEpKL5ycgaDUQvmmGHy5YMx7JyzymH3bvD4GqirQyBWsUDwFD9HtnsVsEZw1xj5VGN6FoFXvVHs83um5JHqfNds3LcE6oqQRAsxQuAM7xaWiLut4mToN7eNUjY3z8HyZ44AxD3mgKYo3JaqnQnqPtaQ1PnkdLydMqnUMwLNHpCY1LcwccgzXYbTm4ULzx8kvMHLM4ubnNn6U2oJqnGwafVtgsNwj885Wzt3Ev5oLS5duoQEubHNqgQBeYgPJBQEHdRPwjCdJTcWNVz7BFG7AH9wA7F9DFaPhptc1ouUoPajKGNmi7fGEMbqXJfruYXooPH7",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```

#### responder <--- (2018-10-16 20:06:18.919)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3cDMp6242sByL9f7EYWHWkkYD1tEpKL5ycgaDUQvmmGHy5YMx7JyzymH3bvD4GqirQyBWsUDwFD9HtnsVsEZw1xj5VGN6FoFXvVHs83um5JHqfNds3LcE6oqQRAsxQuAM7xaWiLut4mToN7eNUjY3z8HyZ44AxD3mgKYo3JaqnQnqPtaQ1PnkdLydMqnUMwLNHpCY1LcwccgzXYbTm4ULzx8kvMHLM4ubnNn6U2oJqnGwafVtgsNwj885Wzt3Ev5oLS5duoQEubHNqgQBeYgPJBQEHdRPwjCdJTcWNVz7BFG7AH9wA7F9DFaPhptc1ouUoPajKGNmi7fGEMbqXJfruYXooPH7",
    "channel_id": "ch_no941exbPegTJx1pPNaCJhkWT9KvszngLmaoTkFJEDnrRxYnp"
  }
}
```
