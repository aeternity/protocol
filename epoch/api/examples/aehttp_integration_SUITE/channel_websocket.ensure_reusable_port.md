
#### initiator init (2018-10-16 20:25:32.718)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A&role=initiator
```

#### responder init (2018-10-16 20:25:32.723)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A&role=responder
```

#### responder <--- (2018-10-16 20:25:33.723)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 20:25:33.725)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 20:25:33.733)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpALFUXGGsdug6Jrs56usDVK43SheHuLKP3h48aDzajQnhSXBUWq2rVDufMiousdvbextEcPQPuUq7817TtZyDq2vCt4rqTh3SqYy9jCHBN6SuCufA4j65Xrud4Spcwoi5gsMaowEXQETWMtFFZcbw7DeBnukD5NY"
  }
}
```

#### initiator ---> (2018-10-16 20:25:33.775)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4Ho6ac9M4kWRCnfXJGKWyqpoL6ecbRVbP6GMfMSV84RdpRv1p8dLvnuVrhSCdxudUJtVCWVvgzTzjm8jm5XGatjaWYTprt8fXBYXD3tBAZz8J7a9iqAWrBwHUrEzZaytWsivkK5mWDHE3ChdSgSE7UddjCy67vADMRfdzf93BHFDAM9qV7GnRTdZNWgFZosZk6qXfSdVNEwpK6AFE6Sp4GNkfDSgaMJ3rfubn5WhqZKMsRrnaZc1Er9mFE8o4KGRsS"
  }
}
```

#### responder <--- (2018-10-16 20:25:33.776)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 20:25:33.777)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpALFUXGGsdug6Jrs56usDVK43SheHuLKP3h48aDzajQnhSXBUWq2rVDufMiousdvbextEcPQPuUq7817TtZyDq2vCt4rqTh3SqYy9jCHBN6SuCufA4j65Xrud4Spcwoi5gsMaowEXQETWMtFFZcbw7DeBnukD5NY"
  }
}
```

#### responder ---> (2018-10-16 20:25:33.778)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4Hmns6DCDSdMUhXYfhgjk9MYU1FM82QyFiB4q1jPKXv6QVS15TbgqPJzyqgCoTii3eY7qYpLJwqsGUFxkwAsS3QKeXt5k81n1zVbdY2h3hgVAQna4D4p6Zbh8SmLf8L2tLMp8DSBv2Fw8hVXDWV21bd7CA95h4WqvqyScaLHQCqdMqqMzjARiFd2Hjk86EhmtGhRVi9efAqKdBZfrzmFnY5UQDUNz3iMLtp2gL4UHmSFxAEK5BiN55o2NUeRYaAZVX"
  }
}
```

#### initiator <--- (2018-10-16 20:25:33.779)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 20:25:33.780)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmRHZM2K3E3JWqYS4mCjCk7GhYWLfhsvGZcj8ywGmYfgtY5syzyThDPETujFHmYUiXnfNyoWCsKs7CXjpnDDeYiRDWQ5ZUTRaLVKRUdrXgSSZqUqtC5yA1McVkacGScsJZLE9kdZoLeu9XP5qmWottWwqCSxaw5bodxKtFGA9bUmsF1i3YPH1FcfKs1LnYv4Q9GTPhtqinThBG5Hwiyd3ipU3Bcc5fLUfdum9bT4kySzGLZCqZrmni7RSYm91ufAKBNBPzKfeEm9Y7TWDwRLhqsTfm16cSKm4pVHrMxaRxjF4oJgbifhutiy8oiCeW5DG76DkT8vZia3WwpcEwe7mG8rCaGg"
  }
}
```

#### initiator <--- (2018-10-16 20:25:33.780)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmRHZM2K3E3JWqYS4mCjCk7GhYWLfhsvGZcj8ywGmYfgtY5syzyThDPETujFHmYUiXnfNyoWCsKs7CXjpnDDeYiRDWQ5ZUTRaLVKRUdrXgSSZqUqtC5yA1McVkacGScsJZLE9kdZoLeu9XP5qmWottWwqCSxaw5bodxKtFGA9bUmsF1i3YPH1FcfKs1LnYv4Q9GTPhtqinThBG5Hwiyd3ipU3Bcc5fLUfdum9bT4kySzGLZCqZrmni7RSYm91ufAKBNBPzKfeEm9Y7TWDwRLhqsTfm16cSKm4pVHrMxaRxjF4oJgbifhutiy8oiCeW5DG76DkT8vZia3WwpcEwe7mG8rCaGg"
  }
}
```

#### initiator <--- (2018-10-16 20:25:34.583)
```javascript
{
  "id": -576460752303423477,
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

#### initiator <--- (2018-10-16 20:25:35.439)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_8MnkVkwQMs7xB4zyZJbbcagbm6EMCNdfx3rK2TjNDwS87Y7Gi"
  }
}
```

#### responder <--- (2018-10-16 20:25:35.439)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_8MnkVkwQMs7xB4zyZJbbcagbm6EMCNdfx3rK2TjNDwS87Y7Gi"
  }
}
```

#### initiator <--- (2018-10-16 20:25:35.439)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_8MnkVkwQMs7xB4zyZJbbcagbm6EMCNdfx3rK2TjNDwS87Y7Gi"
  }
}
```

#### responder <--- (2018-10-16 20:25:35.440)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_8MnkVkwQMs7xB4zyZJbbcagbm6EMCNdfx3rK2TjNDwS87Y7Gi"
  }
}
```

#### responder <--- (2018-10-16 20:25:35.443)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_8MnkVkwQMs7xB4zyZJbbcagbm6EMCNdfx3rK2TjNDwS87Y7Gi"
  }
}
```

#### initiator <--- (2018-10-16 20:25:35.444)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_8MnkVkwQMs7xB4zyZJbbcagbm6EMCNdfx3rK2TjNDwS87Y7Gi"
  }
}
```

#### responder <--- (2018-10-16 20:25:35.445)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmRHZM2K3E3JWqYS4mCjCk7GhYWLfhsvGZcj8ywGmYfgtY5syzyThDPETujFHmYUiXnfNyoWCsKs7CXjpnDDeYiRDWQ5ZUTRaLVKRUdrXgSSZqUqtC5yA1McVkacGScsJZLE9kdZoLeu9XP5qmWottWwqCSxaw5bodxKtFGA9bUmsF1i3YPH1FcfKs1LnYv4Q9GTPhtqinThBG5Hwiyd3ipU3Bcc5fLUfdum9bT4kySzGLZCqZrmni7RSYm91ufAKBNBPzKfeEm9Y7TWDwRLhqsTfm16cSKm4pVHrMxaRxjF4oJgbifhutiy8oiCeW5DG76DkT8vZia3WwpcEwe7mG8rCaGg",
    "channel_id": "ch_8MnkVkwQMs7xB4zyZJbbcagbm6EMCNdfx3rK2TjNDwS87Y7Gi"
  }
}
```

#### initiator <--- (2018-10-16 20:25:35.445)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmRHZM2K3E3JWqYS4mCjCk7GhYWLfhsvGZcj8ywGmYfgtY5syzyThDPETujFHmYUiXnfNyoWCsKs7CXjpnDDeYiRDWQ5ZUTRaLVKRUdrXgSSZqUqtC5yA1McVkacGScsJZLE9kdZoLeu9XP5qmWottWwqCSxaw5bodxKtFGA9bUmsF1i3YPH1FcfKs1LnYv4Q9GTPhtqinThBG5Hwiyd3ipU3Bcc5fLUfdum9bT4kySzGLZCqZrmni7RSYm91ufAKBNBPzKfeEm9Y7TWDwRLhqsTfm16cSKm4pVHrMxaRxjF4oJgbifhutiy8oiCeW5DG76DkT8vZia3WwpcEwe7mG8rCaGg",
    "channel_id": "ch_8MnkVkwQMs7xB4zyZJbbcagbm6EMCNdfx3rK2TjNDwS87Y7Gi"
  }
}
```

#### initiator: (2018-10-16 20:25:35.721)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-16 20:25:35.722)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-16 20:25:35.722)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-16 20:25:35.722)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-16 20:25:35.722)
> Channel is `open` and ready to use

#### responder: (2018-10-16 20:25:35.722)
> Channel is `open` and ready to use

#### initiator: (2018-10-16 20:25:35.753)
> Failing update, insufficient balance

#### initiator ---> (2018-10-16 20:25:35.753)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 10000,
    "from": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
    "to": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A"
  }
}
```

#### initiator <--- (2018-10-16 20:25:35.760)
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
        "from": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
        "to": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0"
}
```

#### initiator: (2018-10-16 20:25:35.761)
> Failing update, negative amount

#### initiator ---> (2018-10-16 20:25:35.761)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": -1,
    "from": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
    "to": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A"
  }
}
```

#### initiator <--- (2018-10-16 20:25:35.762)
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
        "from": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
        "to": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0"
}
```

#### initiator: (2018-10-16 20:25:35.762)
> Failing update, invalid pubkeys

#### initiator ---> (2018-10-16 20:25:35.762)
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

#### initiator <--- (2018-10-16 20:25:35.764)
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

#### responder: (2018-10-16 20:25:35.765)
> Failing update, insufficient balance

#### responder ---> (2018-10-16 20:25:35.765)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 10000,
    "from": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
    "to": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh"
  }
}
```

#### responder <--- (2018-10-16 20:25:35.770)
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
        "from": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
        "to": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0"
}
```

#### responder: (2018-10-16 20:25:35.770)
> Failing update, negative amount

#### responder ---> (2018-10-16 20:25:35.771)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": -1,
    "from": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
    "to": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh"
  }
}
```

#### responder <--- (2018-10-16 20:25:35.771)
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
        "from": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
        "to": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0"
}
```

#### responder: (2018-10-16 20:25:35.772)
> Failing update, invalid pubkeys

#### responder ---> (2018-10-16 20:25:35.772)
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

#### responder <--- (2018-10-16 20:25:35.773)
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

#### initiator init (2018-10-16 20:25:35.861)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A&role=initiator
```

#### responder init (2018-10-16 20:25:35.867)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A&role=responder
```

#### responder <--- (2018-10-16 20:25:36.869)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 20:25:36.872)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 20:25:36.879)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpALFUXGGsdug6Jrs56usDVK43SheHuLKP3h48aDzajQnhSXBUWq2rVDufMiousdvbextEcPQPuUq7817TtZyDq2vCt4rqTh3SqYy9jCHBN6SuCufA4j65Xrud4Spcwoi5gsMaowEXQETWMtFFZcbw7DeBo3y5B67"
  }
}
```

#### initiator ---> (2018-10-16 20:25:36.915)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4Hnzn41thHRZu6S62Pfpmc5KqXXcqUrvLnZfTVwwTemU82QyeakszBtkooKCn2bsNCMKtnvGxvTMkYq683wRnDNzmhgEYoQGvGnfo2Ff3SYVbnJi6YvAdoWundBJetcZAJvrCaA6VKxEoz9QjiVqMaZ64UXEJiUhXSjfLii9TJ8Vkiipy63hz2KuVmVjESnqVQKPf3XaG3hQLe7TCfZHQLV7HU3qnGtn25gUGzVXkKfsyodbpYQZPcTgXTdXpKkQpD"
  }
}
```

#### responder <--- (2018-10-16 20:25:36.917)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 20:25:36.917)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpALFUXGGsdug6Jrs56usDVK43SheHuLKP3h48aDzajQnhSXBUWq2rVDufMiousdvbextEcPQPuUq7817TtZyDq2vCt4rqTh3SqYy9jCHBN6SuCufA4j65Xrud4Spcwoi5gsMaowEXQETWMtFFZcbw7DeBo3y5B67"
  }
}
```

#### responder ---> (2018-10-16 20:25:36.918)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HmL6C2dhFXW7c4gVQEPizbj28ygASS2x2SAtNq59y9P1K7BtQ2uPJ7eTpa6gYY7gLNgZxuBYuohQwVez9mdgLsANyWQByJLaUHZi99Ay2SpUVsATZe64mw55YuhMqYCDEd9Uddo9XVxQmt2yRmEMNM4ushJfMbyoduKU8eJjrkPjfENVNZV9XUSHeU85SCdpTzpF3bsGXQ1cUJt3efJTQ6Cj6CibL2wGb6FKodoxS1LYGPrNj3akCQDRjRCzrqukG"
  }
}
```

#### initiator <--- (2018-10-16 20:25:36.920)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 20:25:36.921)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmQVXehPoD8VWHMPWzYXtMJDkXQH1xNJB8XhvB3uuK36kXFKLUuPbFiGki7gMWqC2WVANEhVVuupNHRSBfXGM1m7GhhTn7mA6gWU7Xyp7XATZV65XvzamqJSJXpvptu93xuYxXXFm7yciFJ1rE8WdMDWTh4C3Pd3oqnHJzEN1WcxZ7zUe7QoXmycUUbPwXwT7rUXr667kzM3hymMEGCugXfhLi3snphHmJPgmG5umrU1AoVAfVUBEk4YWvLycCmJSLwnixQt9BDCU9gr9vPMqcAbDoqsK54a8cSxZHWneNnzXm7DHWmfvBC5hZ8jF2X63UesGxyWeUvckG5CwMQ3f24TZCHD"
  }
}
```

#### initiator <--- (2018-10-16 20:25:36.922)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmQVXehPoD8VWHMPWzYXtMJDkXQH1xNJB8XhvB3uuK36kXFKLUuPbFiGki7gMWqC2WVANEhVVuupNHRSBfXGM1m7GhhTn7mA6gWU7Xyp7XATZV65XvzamqJSJXpvptu93xuYxXXFm7yciFJ1rE8WdMDWTh4C3Pd3oqnHJzEN1WcxZ7zUe7QoXmycUUbPwXwT7rUXr667kzM3hymMEGCugXfhLi3snphHmJPgmG5umrU1AoVAfVUBEk4YWvLycCmJSLwnixQt9BDCU9gr9vPMqcAbDoqsK54a8cSxZHWneNnzXm7DHWmfvBC5hZ8jF2X63UesGxyWeUvckG5CwMQ3f24TZCHD"
  }
}
```

#### initiator <--- (2018-10-16 20:25:37.824)
```javascript
{
  "id": -576460752303423476,
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

#### responder <--- (2018-10-16 20:25:38.375)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_t3FUbji1Pmo2H9K5RYJuwdGfb9gTK4AHwQ2pgmJQEJFdaXHeg"
  }
}
```

#### initiator <--- (2018-10-16 20:25:38.376)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_t3FUbji1Pmo2H9K5RYJuwdGfb9gTK4AHwQ2pgmJQEJFdaXHeg"
  }
}
```

#### initiator <--- (2018-10-16 20:25:38.377)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_t3FUbji1Pmo2H9K5RYJuwdGfb9gTK4AHwQ2pgmJQEJFdaXHeg"
  }
}
```

#### responder <--- (2018-10-16 20:25:38.378)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_t3FUbji1Pmo2H9K5RYJuwdGfb9gTK4AHwQ2pgmJQEJFdaXHeg"
  }
}
```

#### initiator <--- (2018-10-16 20:25:38.382)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_t3FUbji1Pmo2H9K5RYJuwdGfb9gTK4AHwQ2pgmJQEJFdaXHeg"
  }
}
```

#### responder <--- (2018-10-16 20:25:38.382)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_t3FUbji1Pmo2H9K5RYJuwdGfb9gTK4AHwQ2pgmJQEJFdaXHeg"
  }
}
```

#### initiator <--- (2018-10-16 20:25:38.384)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmQVXehPoD8VWHMPWzYXtMJDkXQH1xNJB8XhvB3uuK36kXFKLUuPbFiGki7gMWqC2WVANEhVVuupNHRSBfXGM1m7GhhTn7mA6gWU7Xyp7XATZV65XvzamqJSJXpvptu93xuYxXXFm7yciFJ1rE8WdMDWTh4C3Pd3oqnHJzEN1WcxZ7zUe7QoXmycUUbPwXwT7rUXr667kzM3hymMEGCugXfhLi3snphHmJPgmG5umrU1AoVAfVUBEk4YWvLycCmJSLwnixQt9BDCU9gr9vPMqcAbDoqsK54a8cSxZHWneNnzXm7DHWmfvBC5hZ8jF2X63UesGxyWeUvckG5CwMQ3f24TZCHD",
    "channel_id": "ch_t3FUbji1Pmo2H9K5RYJuwdGfb9gTK4AHwQ2pgmJQEJFdaXHeg"
  }
}
```

#### responder <--- (2018-10-16 20:25:38.384)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmQVXehPoD8VWHMPWzYXtMJDkXQH1xNJB8XhvB3uuK36kXFKLUuPbFiGki7gMWqC2WVANEhVVuupNHRSBfXGM1m7GhhTn7mA6gWU7Xyp7XATZV65XvzamqJSJXpvptu93xuYxXXFm7yciFJ1rE8WdMDWTh4C3Pd3oqnHJzEN1WcxZ7zUe7QoXmycUUbPwXwT7rUXr667kzM3hymMEGCugXfhLi3snphHmJPgmG5umrU1AoVAfVUBEk4YWvLycCmJSLwnixQt9BDCU9gr9vPMqcAbDoqsK54a8cSxZHWneNnzXm7DHWmfvBC5hZ8jF2X63UesGxyWeUvckG5CwMQ3f24TZCHD",
    "channel_id": "ch_t3FUbji1Pmo2H9K5RYJuwdGfb9gTK4AHwQ2pgmJQEJFdaXHeg"
  }
}
```

#### initiator: (2018-10-16 20:25:39.500)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-16 20:25:39.500)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-16 20:25:39.500)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-16 20:25:39.500)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-16 20:25:39.500)
> Channel is `open` and ready to use

#### responder: (2018-10-16 20:25:39.500)
> Channel is `open` and ready to use

#### initiator ---> (2018-10-16 20:25:39.534)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "hejsan",
    "to": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A"
  }
}
```

#### responder <--- (2018-10-16 20:25:39.536)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "message": {
      "channel_id": "ch_t3FUbji1Pmo2H9K5RYJuwdGfb9gTK4AHwQ2pgmJQEJFdaXHeg",
      "from": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "info": "hejsan",
      "to": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A"
    },
    "channel_id": "ch_t3FUbji1Pmo2H9K5RYJuwdGfb9gTK4AHwQ2pgmJQEJFdaXHeg"
  }
}
```

#### responder ---> (2018-10-16 20:25:39.536)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "svejsan",
    "to": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh"
  }
}
```

#### initiator <--- (2018-10-16 20:25:39.539)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "message": {
      "channel_id": "ch_t3FUbji1Pmo2H9K5RYJuwdGfb9gTK4AHwQ2pgmJQEJFdaXHeg",
      "from": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "info": "svejsan",
      "to": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh"
    },
    "channel_id": "ch_t3FUbji1Pmo2H9K5RYJuwdGfb9gTK4AHwQ2pgmJQEJFdaXHeg"
  }
}
```

#### initiator ---> (2018-10-16 20:25:39.539)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "first message in a row",
    "to": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A"
  }
}
```

#### responder <--- (2018-10-16 20:25:39.542)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "message": {
      "channel_id": "ch_t3FUbji1Pmo2H9K5RYJuwdGfb9gTK4AHwQ2pgmJQEJFdaXHeg",
      "from": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "info": "first message in a row",
      "to": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A"
    },
    "channel_id": "ch_t3FUbji1Pmo2H9K5RYJuwdGfb9gTK4AHwQ2pgmJQEJFdaXHeg"
  }
}
```

#### initiator ---> (2018-10-16 20:25:39.543)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "second message in a row",
    "to": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A"
  }
}
```

#### responder <--- (2018-10-16 20:25:39.588)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "message": {
      "channel_id": "ch_t3FUbji1Pmo2H9K5RYJuwdGfb9gTK4AHwQ2pgmJQEJFdaXHeg",
      "from": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
      "info": "second message in a row",
      "to": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A"
    },
    "channel_id": "ch_t3FUbji1Pmo2H9K5RYJuwdGfb9gTK4AHwQ2pgmJQEJFdaXHeg"
  }
}
```

#### responder ---> (2018-10-16 20:25:39.590)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "some message",
    "to": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh"
  }
}
```

#### initiator <--- (2018-10-16 20:25:39.594)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "message": {
      "channel_id": "ch_t3FUbji1Pmo2H9K5RYJuwdGfb9gTK4AHwQ2pgmJQEJFdaXHeg",
      "from": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "info": "some message",
      "to": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh"
    },
    "channel_id": "ch_t3FUbji1Pmo2H9K5RYJuwdGfb9gTK4AHwQ2pgmJQEJFdaXHeg"
  }
}
```

#### responder ---> (2018-10-16 20:25:39.596)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "other message",
    "to": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh"
  }
}
```

#### initiator <--- (2018-10-16 20:25:39.638)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "message": {
      "channel_id": "ch_t3FUbji1Pmo2H9K5RYJuwdGfb9gTK4AHwQ2pgmJQEJFdaXHeg",
      "from": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
      "info": "other message",
      "to": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh"
    },
    "channel_id": "ch_t3FUbji1Pmo2H9K5RYJuwdGfb9gTK4AHwQ2pgmJQEJFdaXHeg"
  }
}
```

#### initiator init (2018-10-16 20:25:39.754)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A&role=initiator
```

#### responder init (2018-10-16 20:25:39.758)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A&role=responder
```

#### responder <--- (2018-10-16 20:25:40.761)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 20:25:40.763)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 20:25:40.772)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpALFUXGGsdug6Jrs56usDVK43SheHuLKP3h48aDzajQnhSXBUWq2rVDufMiousdvbextEcPQPuUq7817TtZyDq2vCt4rqTh3SqYy9jCHBN6SuCufA4j65Xrud4Spcwoi5gsMaowEXQETWMtFFZcbw7DeBo8GagkN"
  }
}
```

#### initiator ---> (2018-10-16 20:25:40.821)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HmpEo1x7qoPjxaiSfJETCxKYq2ubyN8AAZpeWZgKfenHDsEV11ppQdFBLMFt61FmtBmbrRbiNLeGsUvZpLrm7nAwBLp1wUYAAZnvLGjwPJGftAVTaihSHd2b63qWX7Myp4Js9yKQYpJuGA1EUpqwtuL3ZeWFDu75xUHaeqXhcH1rstCUpTNyQFSXpn3caLoudzXzvNQVxcMLeBhPcfqU8WuFa3fHaxvNinahL6Vv277QZkAXJ62JvhoyLLiLVN9Gp"
  }
}
```

#### responder <--- (2018-10-16 20:25:40.823)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 20:25:40.823)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpALFUXGGsdug6Jrs56usDVK43SheHuLKP3h48aDzajQnhSXBUWq2rVDufMiousdvbextEcPQPuUq7817TtZyDq2vCt4rqTh3SqYy9jCHBN6SuCufA4j65Xrud4Spcwoi5gsMaowEXQETWMtFFZcbw7DeBo8GagkN"
  }
}
```

#### responder ---> (2018-10-16 20:25:40.824)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4Ho5thN8WYmNyUKYSqFuv2tP8ztUUekmq6hhfmYgKMRZqU8xtVZzq3ArpYjzpD7Laf29RAT7qWRz6yrUhM8VKnQV38g1egrTqNUUzpVk4zFfpXKp7cQHEuEUcQ8CgqLnSKGh7vfhCgj61o6zZ5bDR15KcV1KQFoQPXMAo5qFEPEEJ8Lh5JgKDS83UicaJFWoS3htQJfAJKasJzNYwwNzdqUJ3u7kUuDkujjcSff6rv7Qm256pLz53wyy3bVBXQAE16"
  }
}
```

#### initiator <--- (2018-10-16 20:25:40.826)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 20:25:40.827)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmRKvNQLy181XMiXUTmpxdrxC3VV2WwZQthy5jL59rJ9GKm6tB2RdG5fXKt94Wi6SEQgUBZxLryycwxvfmgCiiXHtcbiHqfQzYmnG2Bqo4GqDyTsZhG1S49zXDUt8sxm3F13KXWCq6Fvj835jCmgAFydLHtUH6rxNkCvJhgfNijw28xozrMVz6x8po5FwpQAEY1YLaSoCeG9FDPCfQiXfjBjNnxcnfzJsAsEw21EWbr1iaa7J9UJdvKJyUcRMH49XpoBGx1d9RJxR1494GokcDGqFEyCwaTDGiFvWsfKBvmZrW35pBodTT4nBViPsjuMmFnuG5qzTFMz1F23sPYcrNgqyKuo"
  }
}
```

#### initiator <--- (2018-10-16 20:25:40.828)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmRKvNQLy181XMiXUTmpxdrxC3VV2WwZQthy5jL59rJ9GKm6tB2RdG5fXKt94Wi6SEQgUBZxLryycwxvfmgCiiXHtcbiHqfQzYmnG2Bqo4GqDyTsZhG1S49zXDUt8sxm3F13KXWCq6Fvj835jCmgAFydLHtUH6rxNkCvJhgfNijw28xozrMVz6x8po5FwpQAEY1YLaSoCeG9FDPCfQiXfjBjNnxcnfzJsAsEw21EWbr1iaa7J9UJdvKJyUcRMH49XpoBGx1d9RJxR1494GokcDGqFEyCwaTDGiFvWsfKBvmZrW35pBodTT4nBViPsjuMmFnuG5qzTFMz1F23sPYcrNgqyKuo"
  }
}
```

#### initiator <--- (2018-10-16 20:25:41.405)
```javascript
{
  "id": -576460752303423475,
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

#### initiator <--- (2018-10-16 20:25:42.38)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_2CE4SWPR9WvgidTcU2Hx7SR7KVZvVV1L3L2xqXLfYsdsFJ4zou"
  }
}
```

#### responder <--- (2018-10-16 20:25:42.39)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_2CE4SWPR9WvgidTcU2Hx7SR7KVZvVV1L3L2xqXLfYsdsFJ4zou"
  }
}
```

#### responder <--- (2018-10-16 20:25:42.39)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_2CE4SWPR9WvgidTcU2Hx7SR7KVZvVV1L3L2xqXLfYsdsFJ4zou"
  }
}
```

#### initiator <--- (2018-10-16 20:25:42.39)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_2CE4SWPR9WvgidTcU2Hx7SR7KVZvVV1L3L2xqXLfYsdsFJ4zou"
  }
}
```

#### initiator <--- (2018-10-16 20:25:42.43)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2CE4SWPR9WvgidTcU2Hx7SR7KVZvVV1L3L2xqXLfYsdsFJ4zou"
  }
}
```

#### responder <--- (2018-10-16 20:25:42.44)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2CE4SWPR9WvgidTcU2Hx7SR7KVZvVV1L3L2xqXLfYsdsFJ4zou"
  }
}
```

#### initiator <--- (2018-10-16 20:25:42.44)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmRKvNQLy181XMiXUTmpxdrxC3VV2WwZQthy5jL59rJ9GKm6tB2RdG5fXKt94Wi6SEQgUBZxLryycwxvfmgCiiXHtcbiHqfQzYmnG2Bqo4GqDyTsZhG1S49zXDUt8sxm3F13KXWCq6Fvj835jCmgAFydLHtUH6rxNkCvJhgfNijw28xozrMVz6x8po5FwpQAEY1YLaSoCeG9FDPCfQiXfjBjNnxcnfzJsAsEw21EWbr1iaa7J9UJdvKJyUcRMH49XpoBGx1d9RJxR1494GokcDGqFEyCwaTDGiFvWsfKBvmZrW35pBodTT4nBViPsjuMmFnuG5qzTFMz1F23sPYcrNgqyKuo",
    "channel_id": "ch_2CE4SWPR9WvgidTcU2Hx7SR7KVZvVV1L3L2xqXLfYsdsFJ4zou"
  }
}
```

#### responder <--- (2018-10-16 20:25:42.45)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmRKvNQLy181XMiXUTmpxdrxC3VV2WwZQthy5jL59rJ9GKm6tB2RdG5fXKt94Wi6SEQgUBZxLryycwxvfmgCiiXHtcbiHqfQzYmnG2Bqo4GqDyTsZhG1S49zXDUt8sxm3F13KXWCq6Fvj835jCmgAFydLHtUH6rxNkCvJhgfNijw28xozrMVz6x8po5FwpQAEY1YLaSoCeG9FDPCfQiXfjBjNnxcnfzJsAsEw21EWbr1iaa7J9UJdvKJyUcRMH49XpoBGx1d9RJxR1494GokcDGqFEyCwaTDGiFvWsfKBvmZrW35pBodTT4nBViPsjuMmFnuG5qzTFMz1F23sPYcrNgqyKuo",
    "channel_id": "ch_2CE4SWPR9WvgidTcU2Hx7SR7KVZvVV1L3L2xqXLfYsdsFJ4zou"
  }
}
```

#### initiator: (2018-10-16 20:25:42.74)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-16 20:25:42.74)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-16 20:25:42.74)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-16 20:25:42.74)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-16 20:25:42.74)
> Channel is `open` and ready to use

#### responder: (2018-10-16 20:25:42.74)
> Channel is `open` and ready to use

#### initiator ---> (2018-10-16 20:25:42.105)
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

#### responder ---> (2018-10-16 20:25:42.106)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 2,
    "from": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh",
    "to": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A"
  }
}
```

#### responder <--- (2018-10-16 20:25:42.112)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQRcGPwE9oBBjNticpehPM5WSqzfueGjHgH2bWQtujT1RPDeqFEb7zGrS2BZNf2nPGnvqRubzYo6RZATjGsWivQPkLkp1vZDn4575HyFJzPw91BnZsi9mX7NCcgwaDAmFtp62Pv4SXEYksJcTaHozBv6E52K4JMehEDYjvRh5d5XrrgswwdyJjtmUu12EgHp8BMHNf8RU2RUzg"
  }
}
```

#### initiator <--- (2018-10-16 20:25:42.113)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQRcGPwE9oBBjNticpehPM5WSqzfueGjHgH2bWQtujT1RPDeqFEb7zGrS2BZNf2nPGnvqRubzYo6RZATjGsWivQPkLkp1vZDn4575HyFJzPw91BnZsi9mX7NCcgwaDAmFtp62Pv4SXEYksJcTaHozBv6E52AUpkJ7W2NoVboMWihm7Xf9QH5FpPUkuLzQZPX1dAv5HMv34JK8D"
  }
}
```

#### initiator ---> (2018-10-16 20:25:42.115)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4kD3GX1VRjZBdsCe44zu4KboiMvevPWmMm6Au3rME5AmmdPBqUGEg3XZH1FfwURs5XVNJ9gJETFhMbNj8chGiJTjRLFnbtmJRqhAx4KQubymKrmBoVfUAaP9t4iYT9DQJeQ3ZCY8BSavr6TjqFm4cdLFRphF1tAzScsyfJWLfgcBV6tE78wiqrtTXVdjXquBqJu2TC5MBRY5Pc8zV3VwokoGM1ErDQC1MU75rTvPhfV7kJKgE2VMVdwLFCa7Ygz7tMRwtP7pbhpZ5zn9H6XiXa6TukDRZzAFiDqWD9HP1ADAUQQ"
  }
}
```

#### responder ---> (2018-10-16 20:25:42.116)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak53drptNx9VNHpHkGppwW4NLXKK94zac7WYyV4KqcSaRBTG8ytkoJyv4KGmSStemL292wV7o7g3zMsYcgqGwz2NyhFZn9kfrLFYdsiWpSuQVHhtLjWiHcXmRwtuXzDmvLmaMQ9Q5NUT5wDt9QE71kPWfNMBZWxN3GzBYt9iHXQMgAiKyNyYVWtGMJ18ds75anrAVwp3hE3cQi8ZdtDSqUVnymsCDzrXycuQmr3fP7emnAmubiVUGdnGo5CDy6x75fW25vw2oXZ1KJzSaJVcpFExxLNe2xQuWE4nsNw7zusW9VGzF"
  }
}
```

#### responder <--- (2018-10-16 20:25:42.117)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2CE4SWPR9WvgidTcU2Hx7SR7KVZvVV1L3L2xqXLfYsdsFJ4zou",
    "round": 1
  }
}
```

#### initiator <--- (2018-10-16 20:25:42.118)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2CE4SWPR9WvgidTcU2Hx7SR7KVZvVV1L3L2xqXLfYsdsFJ4zou",
    "round": 1
  }
}
```

#### responder ---> (2018-10-16 20:25:42.118)
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

#### initiator ---> (2018-10-16 20:25:42.118)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 2,
    "from": "ak_db5pAwz4yETLDDQ7TLzoiHFGjL53hBgEtFGLKkUABaKYLPR4A",
    "to": "ak_SG9Rf4Gp52s77489zvpig6aCQUCNA422H2iAGqijbHjcsCCPh"
  }
}
```

#### initiator <--- (2018-10-16 20:25:42.124)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQRcGPwE9oBBjNticpehPM5WSqzfueGjHgH2bWQtujT1RPDeqFEb7zGrS2BZNf2nVp99QKxJJhr5Bcrckw48iKxoXrf3A73ryQ9MQwbEmz7bzq9KNLHGAivqjxRvNpNWV87ud3dgPzijpfHVuLVjhMkjn37GqwK8qig1BvFjpAKevBh7uxeTLTZCu3PJj4pPguN3jY9XZvXJVu"
  }
}
```

#### responder <--- (2018-10-16 20:25:42.124)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQRcGPwE9oBBjNticpehPM5WSqzfueGjHgH2bWQtujT1RPDeqFEb7zGrS2BZNf2nVp99QKxJJhr5Bcrckw48iKxoXrf3A73ryQ9MQwbEmz7bzq9KNLHGAivqjxRvNpNWV87ud3dgPzijpfHVuLVjhMkjn378GjdMrUoSTcoSXfs2znFwKUK3ukJvBktLczruwg7jmgm6pZFa2v"
  }
}
```

#### responder ---> (2018-10-16 20:25:42.126)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4oyngbPYeUBbLXt1rDGmicfQj8b8YGZWYQSGVfoiJQ1CfJvtVtqexQ9s62ejK4SmqcJd1M1u1iwLSkqETPiCc6yWcNa1Z7PaoXXnxMJcBboQcK9B29M3DMTS8zgh8tZLdZnAg2gp65tZzDuvTs3NZGSUAFRLCY2YQm8bPu2zo8UHfaFPsVijiFGUq7hD4vQUy8asiorTkJRWuMJNw6mYNrkTLCZ6KFnMXqVyBkia9vDW2Pif4UzeXVdFPV44iQwPivjzjodqzzC3TGfY2Zvw1cG6fn6TtCFd4oeSarp3P4iWv4C"
  }
}
```

#### initiator ---> (2018-10-16 20:25:42.126)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak5ALy1HFXvRVNLztFMZ2mnKZS1Ns2FvAgkS3BLYjECkuRPqZmX43Cs5cJpVBbxGTzFcJusM4vJ8QcSPSTwLjGuHq6VgeBdkxwPVuakcvcFiMWK1WmQwQ3QotTQ5a2CnLm9LqT3JoeiX9W5GNCPWQnhqfMMHa9msa9oDxMaPAr5KaGowRpHM7WZjEBknGizQ7x7UtqWYBw6Te8gryHWCXEXrtGDSwmKz4wTBCVR2h6fnBcLvszFDqZeCr3ARecm1BecGffPDbRe5TWakCHBVcs9CNLqPEsuquoEB4D7zzcP6k9vkK"
  }
}
```

#### initiator <--- (2018-10-16 20:25:42.128)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2CE4SWPR9WvgidTcU2Hx7SR7KVZvVV1L3L2xqXLfYsdsFJ4zou",
    "round": 1
  }
}
```

#### responder <--- (2018-10-16 20:25:42.128)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2CE4SWPR9WvgidTcU2Hx7SR7KVZvVV1L3L2xqXLfYsdsFJ4zou",
    "round": 1
  }
}
```
