
#### initiator init (2018-10-24 12:53:21.546)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ&role=initiator
```

#### responder init (2018-10-24 12:53:21.550)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ&role=responder
```

#### responder <--- (2018-10-24 12:53:22.551)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "undefined",
    "data": {
      "event": "channel_open"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:53:22.551)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "undefined",
    "data": {
      "event": "channel_accept"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:53:22.554)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": "undefined",
    "data": {
      "tx": "tx_3d11KjpALBGjNkDnd6KHWu5iTiKtNxx7QB3F4FAQKEUoRqgew2XUdpGzQSHzCU45vuAQtu9BwjdbpJixR7So3AVsan7KuCjyjhr7NDiNTQ75Reiaog9FiphxWu6wrqdFhLcvtZC2BQ516zK233PhbT2oNjp4QhvN9hE6G4"
    }
  }
}
```

#### initiator ---> (2018-10-24 12:53:22.572)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HjwRVNiMoGx3HhVbGZpS9279iDrvPLmrKKUNFAMXt6NmSCMzLizouMRdmU8XtnqJHY1L9gUHpiX8LyLbjFPMf7cCyGv9tYtdn3z2iHbhGNJvp8y3k14Lp7KsxKwa24Caq9pp1sGzNYPTftZZRwg9fFRZLXDpprLjZXKuPygRmaVwAhejpuftus1r75WKPkLzmi5xwuuYbzxamZ4kASod8gcKSqxsiFRtGtqxetfQvWwjAKHo1To8wpZN6aQ9BghRq"
  }
}
```

#### responder <--- (2018-10-24 12:53:22.573)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "undefined",
    "data": {
      "event": "funding_created"
    }
  }
}
```

#### responder <--- (2018-10-24 12:53:22.574)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": "undefined",
    "data": {
      "tx": "tx_3d11KjpALBGjNkDnd6KHWu5iTiKtNxx7QB3F4FAQKEUoRqgew2XUdpGzQSHzCU45vuAQtu9BwjdbpJixR7So3AVsan7KuCjyjhr7NDiNTQ75Reiaog9FiphxWu6wrqdFhLcvtZC2BQ516zK233PhbT2oNjp4QhvN9hE6G4"
    }
  }
}
```

#### responder ---> (2018-10-24 12:53:22.574)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4Hm2CftGGRteXYRyHg22vovrViGEC1TXxRvJmEjo7G3fSBzacMRGKVJq4QNNSzS9amViWAsZpnYQAZcnRnBAjMQtM2qqxs5vobTbxeQ81MPVtxbaeHCajTxGwu9NteCFVS4rrhW655GTGeBgd631At3pVVhuwVPZjVhHBH3FrnTcqZ9xy91Eg2kbXSqvJ9c9TUs6eARXgJ1aobsmFXJT4FqttewegbdYZ4r9Eg9yNJV5UDKYcKeibjq755mfsAqxHW"
  }
}
```

#### initiator <--- (2018-10-24 12:53:22.576)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "undefined",
    "data": {
      "event": "funding_signed"
    }
  }
}
```

#### responder <--- (2018-10-24 12:53:22.577)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "undefined",
    "data": {
      "tx": "tx_6jPYBUFTkcmN6rBJJRzrN12P3NooWuAupZPA8GKVJDGW3cnzqeNgBYUK1tnanjAqg5VcEw4tr3ctsmkp4QS2gTXk1LkvDKRnd5tdHcNj2r6aSzQ7JA8VT1tKJDUbnoSaHxdhbtbhym6DGUdNXimwwbuCzoWebvncdQYifMAYawCsBH5bJjzEyfSvL1rbbtyZzotBcNFrStsK7CqEVLbPwHY24fFouQghjZborafwoLTAsUSSRCjC1JowHCkJtNPACLoYPJnbL99K4ZopTZW88SzqZaQBx4wK8CbZJkVnQb4oNTmC8826V1fhZo77Hvpw3iLFt4jsyRPeySAod2bzNCGQtAcUnYybkDmj7"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:53:22.578)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "undefined",
    "data": {
      "tx": "tx_6jPYBUFTkcmN6rBJJRzrN12P3NooWuAupZPA8GKVJDGW3cnzqeNgBYUK1tnanjAqg5VcEw4tr3ctsmkp4QS2gTXk1LkvDKRnd5tdHcNj2r6aSzQ7JA8VT1tKJDUbnoSaHxdhbtbhym6DGUdNXimwwbuCzoWebvncdQYifMAYawCsBH5bJjzEyfSvL1rbbtyZzotBcNFrStsK7CqEVLbPwHY24fFouQghjZborafwoLTAsUSSRCjC1JowHCkJtNPACLoYPJnbL99K4ZopTZW88SzqZaQBx4wK8CbZJkVnQb4oNTmC8826V1fhZo77Hvpw3iLFt4jsyRPeySAod2bzNCGQtAcUnYybkDmj7"
    }
  }
}
```

#### initiator ---> (2018-10-24 12:53:23.911)
```javascript
{
  "id": -576460752303423476,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
      "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ"
    ]
  }
}
```

#### initiator <--- (2018-10-24 12:53:23.913)
```javascript
{
  "id": -576460752303423476,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
      "balance": 699
    },
    {
      "account": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
      "balance": 401
    }
  ]
}
```

#### responder <--- (2018-10-24 12:53:28.159)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_61i9fQVjHt7XBs2Nbp9qzdaUMd97zMd1Cwi2NBrNZVDYydk13",
    "data": {
      "event": "own_funding_locked"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:53:28.159)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_61i9fQVjHt7XBs2Nbp9qzdaUMd97zMd1Cwi2NBrNZVDYydk13",
    "data": {
      "event": "own_funding_locked"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:53:28.160)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_61i9fQVjHt7XBs2Nbp9qzdaUMd97zMd1Cwi2NBrNZVDYydk13",
    "data": {
      "event": "funding_locked"
    }
  }
}
```

#### responder <--- (2018-10-24 12:53:28.160)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_61i9fQVjHt7XBs2Nbp9qzdaUMd97zMd1Cwi2NBrNZVDYydk13",
    "data": {
      "event": "funding_locked"
    }
  }
}
```

#### responder <--- (2018-10-24 12:53:28.163)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_61i9fQVjHt7XBs2Nbp9qzdaUMd97zMd1Cwi2NBrNZVDYydk13",
    "data": {
      "event": "open"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:53:28.163)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_61i9fQVjHt7XBs2Nbp9qzdaUMd97zMd1Cwi2NBrNZVDYydk13",
    "data": {
      "event": "open"
    }
  }
}
```

#### responder <--- (2018-10-24 12:53:28.164)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_61i9fQVjHt7XBs2Nbp9qzdaUMd97zMd1Cwi2NBrNZVDYydk13",
    "data": {
      "state": "tx_6jPYBUFTkcmN6rBJJRzrN12P3NooWuAupZPA8GKVJDGW3cnzqeNgBYUK1tnanjAqg5VcEw4tr3ctsmkp4QS2gTXk1LkvDKRnd5tdHcNj2r6aSzQ7JA8VT1tKJDUbnoSaHxdhbtbhym6DGUdNXimwwbuCzoWebvncdQYifMAYawCsBH5bJjzEyfSvL1rbbtyZzotBcNFrStsK7CqEVLbPwHY24fFouQghjZborafwoLTAsUSSRCjC1JowHCkJtNPACLoYPJnbL99K4ZopTZW88SzqZaQBx4wK8CbZJkVnQb4oNTmC8826V1fhZo77Hvpw3iLFt4jsyRPeySAod2bzNCGQtAcUnYybkDmj7"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:53:28.164)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_61i9fQVjHt7XBs2Nbp9qzdaUMd97zMd1Cwi2NBrNZVDYydk13",
    "data": {
      "state": "tx_6jPYBUFTkcmN6rBJJRzrN12P3NooWuAupZPA8GKVJDGW3cnzqeNgBYUK1tnanjAqg5VcEw4tr3ctsmkp4QS2gTXk1LkvDKRnd5tdHcNj2r6aSzQ7JA8VT1tKJDUbnoSaHxdhbtbhym6DGUdNXimwwbuCzoWebvncdQYifMAYawCsBH5bJjzEyfSvL1rbbtyZzotBcNFrStsK7CqEVLbPwHY24fFouQghjZborafwoLTAsUSSRCjC1JowHCkJtNPACLoYPJnbL99K4ZopTZW88SzqZaQBx4wK8CbZJkVnQb4oNTmC8826V1fhZo77Hvpw3iLFt4jsyRPeySAod2bzNCGQtAcUnYybkDmj7"
    }
  }
}
```

#### initiator: (2018-10-24 12:53:28.426)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-24 12:53:28.426)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-24 12:53:28.426)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-24 12:53:28.426)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-24 12:53:28.426)
> Channel is `open` and ready to use

#### responder: (2018-10-24 12:53:28.426)
> Channel is `open` and ready to use

#### initiator ---> (2018-10-24 12:53:28.462)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "hejsan",
    "to": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ"
  }
}
```

#### responder <--- (2018-10-24 12:53:28.466)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_61i9fQVjHt7XBs2Nbp9qzdaUMd97zMd1Cwi2NBrNZVDYydk13",
    "data": {
      "message": {
        "channel_id": "ch_61i9fQVjHt7XBs2Nbp9qzdaUMd97zMd1Cwi2NBrNZVDYydk13",
        "from": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
        "info": "hejsan",
        "to": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ"
      }
    }
  }
}
```

#### responder ---> (2018-10-24 12:53:28.467)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "svejsan",
    "to": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY"
  }
}
```

#### initiator <--- (2018-10-24 12:53:28.472)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_61i9fQVjHt7XBs2Nbp9qzdaUMd97zMd1Cwi2NBrNZVDYydk13",
    "data": {
      "message": {
        "channel_id": "ch_61i9fQVjHt7XBs2Nbp9qzdaUMd97zMd1Cwi2NBrNZVDYydk13",
        "from": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
        "info": "svejsan",
        "to": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY"
      }
    }
  }
}
```

#### initiator ---> (2018-10-24 12:53:28.473)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "first message in a row",
    "to": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ"
  }
}
```

#### responder <--- (2018-10-24 12:53:28.477)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_61i9fQVjHt7XBs2Nbp9qzdaUMd97zMd1Cwi2NBrNZVDYydk13",
    "data": {
      "message": {
        "channel_id": "ch_61i9fQVjHt7XBs2Nbp9qzdaUMd97zMd1Cwi2NBrNZVDYydk13",
        "from": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
        "info": "first message in a row",
        "to": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ"
      }
    }
  }
}
```

#### initiator ---> (2018-10-24 12:53:28.478)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "second message in a row",
    "to": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ"
  }
}
```

#### responder <--- (2018-10-24 12:53:28.521)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_61i9fQVjHt7XBs2Nbp9qzdaUMd97zMd1Cwi2NBrNZVDYydk13",
    "data": {
      "message": {
        "channel_id": "ch_61i9fQVjHt7XBs2Nbp9qzdaUMd97zMd1Cwi2NBrNZVDYydk13",
        "from": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
        "info": "second message in a row",
        "to": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ"
      }
    }
  }
}
```

#### responder ---> (2018-10-24 12:53:28.522)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "some message",
    "to": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY"
  }
}
```

#### initiator <--- (2018-10-24 12:53:28.528)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_61i9fQVjHt7XBs2Nbp9qzdaUMd97zMd1Cwi2NBrNZVDYydk13",
    "data": {
      "message": {
        "channel_id": "ch_61i9fQVjHt7XBs2Nbp9qzdaUMd97zMd1Cwi2NBrNZVDYydk13",
        "from": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
        "info": "some message",
        "to": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY"
      }
    }
  }
}
```

#### responder ---> (2018-10-24 12:53:28.528)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "other message",
    "to": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY"
  }
}
```

#### initiator <--- (2018-10-24 12:53:28.569)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_61i9fQVjHt7XBs2Nbp9qzdaUMd97zMd1Cwi2NBrNZVDYydk13",
    "data": {
      "message": {
        "channel_id": "ch_61i9fQVjHt7XBs2Nbp9qzdaUMd97zMd1Cwi2NBrNZVDYydk13",
        "from": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
        "info": "other message",
        "to": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY"
      }
    }
  }
}
```
