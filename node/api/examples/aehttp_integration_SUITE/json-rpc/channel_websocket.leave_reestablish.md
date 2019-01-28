
#### initiator init (2018-10-24 12:53:56.462)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ&role=initiator
```

#### responder init (2018-10-24 12:53:56.466)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ&role=responder
```

#### responder <--- (2018-10-24 12:53:57.470)
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

#### initiator <--- (2018-10-24 12:53:57.471)
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

#### initiator <--- (2018-10-24 12:53:57.474)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": "undefined",
    "data": {
      "tx": "tx_3d11KjpALBGjNkDnd6KHWu5iTiKtNxx7QB3F4FAQKEUoRqgew2XUdpGzQSHzCU45vuAQtu9BwjdbpJixR7So3AVsan7KuCjyjhr7NDiNTQ75Reiaog9FiphxWu6wrqdFhLcvtZC2BQ516zK233PhbT2oNjp4QhvNiV4qDS"
    }
  }
}
```

#### initiator ---> (2018-10-24 12:53:57.493)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HoVhjLBE6Hr7wcCRwuMxfHq4NCVxPXNi66NT4DqH2g4JSwYZtrbBcz7Pbi3mJhonvM3iWU5ewv6tQBvQRDNAJFAurxMwLGJHPXaLe6z3bav9CXAmw1YGH59RE1Qa9CvvYJG3XGzb2ZL3roJJW3gqbET88u4p9z1MdtAfM8jJDiZBTbjqrWhy25CBiXknHpJA7b9yxQbUSyS7W9Su4ktbY4SFefEtRimpEpUEJKv1TZhDvLwXLKnZxNk5m5V36MkkV"
  }
}
```

#### responder <--- (2018-10-24 12:53:57.494)
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

#### responder <--- (2018-10-24 12:53:57.495)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": "undefined",
    "data": {
      "tx": "tx_3d11KjpALBGjNkDnd6KHWu5iTiKtNxx7QB3F4FAQKEUoRqgew2XUdpGzQSHzCU45vuAQtu9BwjdbpJixR7So3AVsan7KuCjyjhr7NDiNTQ75Reiaog9FiphxWu6wrqdFhLcvtZC2BQ516zK233PhbT2oNjp4QhvNiV4qDS"
    }
  }
}
```

#### responder ---> (2018-10-24 12:53:57.496)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HkmwmM1LvApNNM4KEkxBrPboaH63vRvqorfVZ8EHXRdwKLpqx3STsNi6sQNVnhg4zD5RnyXygNw9ptLjyzLYpxzEv3T8itX92eE2hiWgxuHFwgFQxVZtLh4XUwKKMkzehbxsDNUbCZwzGfTxnBSrUz8btbSh44bqoWczcX74vVRh9vbVFwdpZzFWg2RiTmCo6VNnuTLswKUuAxNEw4mf1UdshYmQuos9kvqXy4wRSX7sYozdFJU1fY4iEwTGiGKQM"
  }
}
```

#### initiator <--- (2018-10-24 12:53:57.497)
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

#### responder <--- (2018-10-24 12:53:57.498)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "undefined",
    "data": {
      "tx": "tx_6jPYBUFTkcmPYGPaqQy3Dv5xMtqA5jySwnY9meqiN21RHTaFpETJAWoP4wfoWdP4XSLRs231yA7UerxqWjpTMJ1uKtMBdgcWyb4dmb2hPvZ73fgDkrTV3bYCSpADDauAWAKnFbpZ4KBYK1H2drJE8QHVFJwQFA5XX6vmTHjqywagqXTbaQedMbH64sS7RzrwQrRKgXApsAhtaN8kxDDUedrTb376GTDghrpCDnFsaHTKQkZoDCfLkaec5zxogfJJiLPLfzVQ9B4LPWk2cEepnqoDzE7CgSa4xyxkddLwnYJB3BSzqPXzKa9wZLCdBCSpo58f5xudZixXBJVJ7wiv25NH6kMMsJ41LUEGg"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:53:57.498)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "undefined",
    "data": {
      "tx": "tx_6jPYBUFTkcmPYGPaqQy3Dv5xMtqA5jySwnY9meqiN21RHTaFpETJAWoP4wfoWdP4XSLRs231yA7UerxqWjpTMJ1uKtMBdgcWyb4dmb2hPvZ73fgDkrTV3bYCSpADDauAWAKnFbpZ4KBYK1H2drJE8QHVFJwQFA5XX6vmTHjqywagqXTbaQedMbH64sS7RzrwQrRKgXApsAhtaN8kxDDUedrTb376GTDghrpCDnFsaHTKQkZoDCfLkaec5zxogfJJiLPLfzVQ9B4LPWk2cEepnqoDzE7CgSa4xyxkddLwnYJB3BSzqPXzKa9wZLCdBCSpo58f5xudZixXBJVJ7wiv25NH6kMMsJ41LUEGg"
    }
  }
}
```

#### initiator ---> (2018-10-24 12:53:58.318)
```javascript
{
  "id": -576460752303423452,
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

#### initiator <--- (2018-10-24 12:53:58.320)
```javascript
{
  "id": -576460752303423452,
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

#### initiator <--- (2018-10-24 12:54:06.475)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "event": "own_funding_locked"
    }
  }
}
```

#### responder <--- (2018-10-24 12:54:06.476)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "event": "own_funding_locked"
    }
  }
}
```

#### responder <--- (2018-10-24 12:54:06.476)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "event": "funding_locked"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.477)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "event": "funding_locked"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.479)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "event": "open"
    }
  }
}
```

#### responder <--- (2018-10-24 12:54:06.479)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "event": "open"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.480)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "state": "tx_6jPYBUFTkcmPYGPaqQy3Dv5xMtqA5jySwnY9meqiN21RHTaFpETJAWoP4wfoWdP4XSLRs231yA7UerxqWjpTMJ1uKtMBdgcWyb4dmb2hPvZ73fgDkrTV3bYCSpADDauAWAKnFbpZ4KBYK1H2drJE8QHVFJwQFA5XX6vmTHjqywagqXTbaQedMbH64sS7RzrwQrRKgXApsAhtaN8kxDDUedrTb376GTDghrpCDnFsaHTKQkZoDCfLkaec5zxogfJJiLPLfzVQ9B4LPWk2cEepnqoDzE7CgSa4xyxkddLwnYJB3BSzqPXzKa9wZLCdBCSpo58f5xudZixXBJVJ7wiv25NH6kMMsJ41LUEGg"
    }
  }
}
```

#### responder <--- (2018-10-24 12:54:06.481)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "state": "tx_6jPYBUFTkcmPYGPaqQy3Dv5xMtqA5jySwnY9meqiN21RHTaFpETJAWoP4wfoWdP4XSLRs231yA7UerxqWjpTMJ1uKtMBdgcWyb4dmb2hPvZ73fgDkrTV3bYCSpADDauAWAKnFbpZ4KBYK1H2drJE8QHVFJwQFA5XX6vmTHjqywagqXTbaQedMbH64sS7RzrwQrRKgXApsAhtaN8kxDDUedrTb376GTDghrpCDnFsaHTKQkZoDCfLkaec5zxogfJJiLPLfzVQ9B4LPWk2cEepnqoDzE7CgSa4xyxkddLwnYJB3BSzqPXzKa9wZLCdBCSpo58f5xudZixXBJVJ7wiv25NH6kMMsJ41LUEGg"
    }
  }
}
```

#### initiator: (2018-10-24 12:54:06.552)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-24 12:54:06.552)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-24 12:54:06.553)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-24 12:54:06.553)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-24 12:54:06.553)
> Channel is `open` and ready to use

#### responder: (2018-10-24 12:54:06.553)
> Channel is `open` and ready to use

#### initiator ---> (2018-10-24 12:54:06.592)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {}
}
```

#### initiator <--- (2018-10-24 12:54:06.601)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "state": "tx_6jPYBUFTkcmPYGPaqQy3Dv5xMtqA5jySwnY9meqiN21RHTaFpETJAWoP4wfoWdP4XSLRs231yA7UerxqWjpTMJ1uKtMBdgcWyb4dmb2hPvZ73fgDkrTV3bYCSpADDauAWAKnFbpZ4KBYK1H2drJE8QHVFJwQFA5XX6vmTHjqywagqXTbaQedMbH64sS7RzrwQrRKgXApsAhtaN8kxDDUedrTb376GTDghrpCDnFsaHTKQkZoDCfLkaec5zxogfJJiLPLfzVQ9B4LPWk2cEepnqoDzE7CgSa4xyxkddLwnYJB3BSzqPXzKa9wZLCdBCSpo58f5xudZixXBJVJ7wiv25NH6kMMsJ41LUEGg"
    }
  }
}
```

#### responder <--- (2018-10-24 12:54:06.602)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "state": "tx_6jPYBUFTkcmPYGPaqQy3Dv5xMtqA5jySwnY9meqiN21RHTaFpETJAWoP4wfoWdP4XSLRs231yA7UerxqWjpTMJ1uKtMBdgcWyb4dmb2hPvZ73fgDkrTV3bYCSpADDauAWAKnFbpZ4KBYK1H2drJE8QHVFJwQFA5XX6vmTHjqywagqXTbaQedMbH64sS7RzrwQrRKgXApsAhtaN8kxDDUedrTb376GTDghrpCDnFsaHTKQkZoDCfLkaec5zxogfJJiLPLfzVQ9B4LPWk2cEepnqoDzE7CgSa4xyxkddLwnYJB3BSzqPXzKa9wZLCdBCSpo58f5xudZixXBJVJ7wiv25NH6kMMsJ41LUEGg"
    }
  }
}
```

#### responder <--- (2018-10-24 12:54:06.604)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "event": "died"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.604)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "event": "died"
    }
  }
}
```

#### responder init (2018-10-24 12:54:06.648)
```
ws://localhost:3014/channel?channel_reserve=2&existing_channel_id=ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm&initiator_amount=700&initiator_id=ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY&lock_period=10&offchain_tx=tx_6jPYBUFTkcmPYGPaqQy3Dv5xMtqA5jySwnY9meqiN21RHTaFpETJAWoP4wfoWdP4XSLRs231yA7UerxqWjpTMJ1uKtMBdgcWyb4dmb2hPvZ73fgDkrTV3bYCSpADDauAWAKnFbpZ4KBYK1H2drJE8QHVFJwQFA5XX6vmTHjqywagqXTbaQedMbH64sS7RzrwQrRKgXApsAhtaN8kxDDUedrTb376GTDghrpCDnFsaHTKQkZoDCfLkaec5zxogfJJiLPLfzVQ9B4LPWk2cEepnqoDzE7CgSa4xyxkddLwnYJB3BSzqPXzKa9wZLCdBCSpo58f5xudZixXBJVJ7wiv25NH6kMMsJ41LUEGg&port=12341&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ&role=responder
```

#### initiator init (2018-10-24 12:54:06.656)
```
ws://localhost:3014/channel?channel_reserve=2&existing_channel_id=ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm&host=localhost&initiator_amount=700&initiator_id=ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY&lock_period=10&offchain_tx=tx_6jPYBUFTkcmPYGPaqQy3Dv5xMtqA5jySwnY9meqiN21RHTaFpETJAWoP4wfoWdP4XSLRs231yA7UerxqWjpTMJ1uKtMBdgcWyb4dmb2hPvZ73fgDkrTV3bYCSpADDauAWAKnFbpZ4KBYK1H2drJE8QHVFJwQFA5XX6vmTHjqywagqXTbaQedMbH64sS7RzrwQrRKgXApsAhtaN8kxDDUedrTb376GTDghrpCDnFsaHTKQkZoDCfLkaec5zxogfJJiLPLfzVQ9B4LPWk2cEepnqoDzE7CgSa4xyxkddLwnYJB3BSzqPXzKa9wZLCdBCSpo58f5xudZixXBJVJ7wiv25NH6kMMsJ41LUEGg&port=12341&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ&role=initiator
```

#### responder <--- (2018-10-24 12:54:06.663)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "event": "channel_reestablished"
    }
  }
}
```

#### responder <--- (2018-10-24 12:54:06.663)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "event": "open"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.665)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "event": "channel_reestablished"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.665)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "event": "open"
    }
  }
}
```

#### responder <--- (2018-10-24 12:54:06.666)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "state": "tx_6jPYBUFTkcmPYGPaqQy3Dv5xMtqA5jySwnY9meqiN21RHTaFpETJAWoP4wfoWdP4XSLRs231yA7UerxqWjpTMJ1uKtMBdgcWyb4dmb2hPvZ73fgDkrTV3bYCSpADDauAWAKnFbpZ4KBYK1H2drJE8QHVFJwQFA5XX6vmTHjqywagqXTbaQedMbH64sS7RzrwQrRKgXApsAhtaN8kxDDUedrTb376GTDghrpCDnFsaHTKQkZoDCfLkaec5zxogfJJiLPLfzVQ9B4LPWk2cEepnqoDzE7CgSa4xyxkddLwnYJB3BSzqPXzKa9wZLCdBCSpo58f5xudZixXBJVJ7wiv25NH6kMMsJ41LUEGg"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.667)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "state": "tx_6jPYBUFTkcmPYGPaqQy3Dv5xMtqA5jySwnY9meqiN21RHTaFpETJAWoP4wfoWdP4XSLRs231yA7UerxqWjpTMJ1uKtMBdgcWyb4dmb2hPvZ73fgDkrTV3bYCSpADDauAWAKnFbpZ4KBYK1H2drJE8QHVFJwQFA5XX6vmTHjqywagqXTbaQedMbH64sS7RzrwQrRKgXApsAhtaN8kxDDUedrTb376GTDghrpCDnFsaHTKQkZoDCfLkaec5zxogfJJiLPLfzVQ9B4LPWk2cEepnqoDzE7CgSa4xyxkddLwnYJB3BSzqPXzKa9wZLCdBCSpo58f5xudZixXBJVJ7wiv25NH6kMMsJ41LUEGg"
    }
  }
}
```

#### initiator ---> (2018-10-24 12:54:06.716)
```javascript
{
  "id": -576460752303423451,
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

#### initiator <--- (2018-10-24 12:54:06.718)
```javascript
{
  "id": -576460752303423451,
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

#### initiator ---> (2018-10-24 12:54:06.719)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
    "to": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ"
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.725)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "tx": "tx_GB8bJXCQR918gbjgUqaGfGDPGZ8Z3GQeSBXNeB5rQZweAc7knLTRYKD2zA9uLCGGL4KnY3RCFsPr4SfioYCNoB8MSTbf4H7gkZcwBPm42BksrZXdejFMPCdx7gdzJ2op3xt49ZiTR76en6WHwxWc3mYDuszQRxaSsFGCiyJ1gNB9oLAjtaiRzQmYDoKcEz67orSZa9TPkJG4TfmFKQjZ"
    }
  }
}
```

#### initiator ---> (2018-10-24 12:54:06.727)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4rpY1ao6NmHit5vDyi87f39ef4QS4tuv4TRinzX6UGVd815XWStsmjXzmZroRdKANKjJpt1eBCgELbvStskpKDtWfWD96bSnRfarjakBt7CRuehUDAbeA44XoyhP4zEnsBLQzbt7gZjE7PVJEy2JSy9XGGm6kqXY5nXNB3EcrnrjdvjM7Q9C1AqWSLkg8YBgvvTp9vrFkLMFYMWFQrfCuWbSiSXP8qyW1Ye95t9KUBytCNyy95k8fe2JAjTmnQx7qRVZ1cgWDnCbKQsiqDpqNhf18WmyhcBBLnFAVzYYRmmD2CM"
  }
}
```

#### responder <--- (2018-10-24 12:54:06.733)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "event": "update"
    }
  }
}
```

#### responder <--- (2018-10-24 12:54:06.734)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "tx": "tx_GB8bJXCQR918gbjgUqaGfGDPGZ8Z3GQeSBXNeB5rQZweAc7knLTRYKD2zA9uLCGGL4KnY3RCFsPr4SfioYCNoB8MSTbf4H7gkZcwBPm42BksrZXdejFMPCdx7gdzJ2op3xt49ZiTR76en6WHwxWc3mYDuszQRxaSsFGCiyJ1gNB9oLAjtaiRzQmYDoKcEz67orSZa9TPkJG4TfmFKQjZ"
    }
  }
}
```

#### responder ---> (2018-10-24 12:54:06.736)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4oFJrFgezYmQs9A4wNtgougdDti3GXtFmq2E8ZKfqdqPAb2ytXGgH8rvzJeXjdorqDPqVh58ux92pgkYvbchPP213uKszUK55bv1xxrhMfwQmF6xBWgRLatUFnWFBmBqJJnS16KNTUd8dvYPNpaCvL3dSZ1kQrq2PMKxLkvcyj9PdpY767eH7P9kpWrVVTBWC7xpemPyqqTQyDxFFRRZP5Kus6RXtpqjYb4dpZqHBJgmGTH7cLAvxxaHj31KuPRweHcpDgWAsCYwxJcarEXtinvScDxBhTjtZjh5opUedneLpp2"
  }
}
```

#### responder <--- (2018-10-24 12:54:06.743)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "state": "tx_3XPhV5wAjiGDkQ4yPpVUvCutB987K5GbyAMUadWa2ja7o9vFzZ9LAyw7jXPNAttiRZNNFutG13rjNJngGa4DkceQnfTjYfbx1CUGUzwu8hT2xrrekzQTZJWpitGVWmnw4m6631iswJP7sD89iL7mMzksNaR83MFvykGn4WeeTbozQK31g4Y5y4vc1Bzo11kivFGAQyvzrhpRtNWaJy3ua72rVJdD7FCqhE2kaUr4oSUXo2hVXV5DMzW3RmUbHwQLR3jAw3pc1b6HZE2G3W8uopUrnSCZ6q6UijyD9Anf9QCtPoNdqQU6jupenGDCYA9mEVsvspUDHWXRwyYynhNp4AWYnQxFuNLTqRgC8vM5HmrTvLTKtsWbjtu9A3zun5F6QCGrwoxCBBLPnhCAjNKuc"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.744)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "state": "tx_3XPhV5wAjiGDkQ4yPpVUvCutB987K5GbyAMUadWa2ja7o9vFzZ9LAyw7jXPNAttiRZNNFutG13rjNJngGa4DkceQnfTjYfbx1CUGUzwu8hT2xrrekzQTZJWpitGVWmnw4m6631iswJP7sD89iL7mMzksNaR83MFvykGn4WeeTbozQK31g4Y5y4vc1Bzo11kivFGAQyvzrhpRtNWaJy3ua72rVJdD7FCqhE2kaUr4oSUXo2hVXV5DMzW3RmUbHwQLR3jAw3pc1b6HZE2G3W8uopUrnSCZ6q6UijyD9Anf9QCtPoNdqQU6jupenGDCYA9mEVsvspUDHWXRwyYynhNp4AWYnQxFuNLTqRgC8vM5HmrTvLTKtsWbjtu9A3zun5F6QCGrwoxCBBLPnhCAjNKuc"
    }
  }
}
```

#### initiator ---> (2018-10-24 12:54:06.749)
```javascript
{
  "id": -576460752303423450,
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

#### initiator <--- (2018-10-24 12:54:06.751)
```javascript
{
  "id": -576460752303423450,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
      "balance": 698
    },
    {
      "account": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
      "balance": 402
    }
  ]
}
```

#### initiator ---> (2018-10-24 12:54:06.751)
```javascript
{
  "id": -576460752303423449,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
      "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY"
    ]
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.753)
```javascript
{
  "id": -576460752303423449,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
      "balance": 402
    },
    {
      "account": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
      "balance": 698
    }
  ]
}
```

#### responder ---> (2018-10-24 12:54:06.754)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
    "to": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY"
  }
}
```

#### responder <--- (2018-10-24 12:54:06.759)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "tx": "tx_GB8bJXCQR918gbjgUqaGfGDPGZ8Z3GQeSBXNeB5rQZweAc7knLTRYQdYqhhNXXzC63ruSArxNhMXwpGTwcHFjF4mchUUzKKv198VckE9E4PKhonG9U1qozuVdxGgLtQRtcw26fPP4VbrWMt5Wr8pCp7HwxQSDJr1SGyGySKpdifv6KNZh37psAe4LwhC9xXox1Fag3UoauXcmJsggxDG"
    }
  }
}
```

#### responder ---> (2018-10-24 12:54:06.760)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4tMdotS2FdPTtH82bvJxNktzXMu9QX5rhthksGGzs7ac25LrLTqPBGWoVS5RLDukmJu7axYgGYTx5QiE6pEYd4yDkoL9TPpN5NPW5XTJq7zH1USHXKre9ewtV2x3Ukm4opULJpVbV7pJUsoKBqHdut7VWRn3Ec9Q63YyfuSiYRwWwEvZC8L2UTMpCn7AtSevmsgf2wTqfj2uFV3rnzSKPXEAXvGgMu5YTJ7guMNjJGU5G55nZ2f4m2SXrqHhZUWafAk4eSUmBdevZsineAN3Nw2ATeCgLkLFjESQnXv7AEpbJ6h"
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.767)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "event": "update"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.768)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "tx": "tx_GB8bJXCQR918gbjgUqaGfGDPGZ8Z3GQeSBXNeB5rQZweAc7knLTRYQdYqhhNXXzC63ruSArxNhMXwpGTwcHFjF4mchUUzKKv198VckE9E4PKhonG9U1qozuVdxGgLtQRtcw26fPP4VbrWMt5Wr8pCp7HwxQSDJr1SGyGySKpdifv6KNZh37psAe4LwhC9xXox1Fag3UoauXcmJsggxDG"
    }
  }
}
```

#### initiator ---> (2018-10-24 12:54:06.770)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4pNGdicBc8UwZxrQbZrYnPpQzBiABubWjuh82zmJYRgQ3J6R9iMBLqXM1NBV1NShsKuGAV7CEsUrvaNW6JYGXGzTPybLgf3EBCF4qevENfiVvUy7HNVSZrihB7os4PFscmfb5qfvQRNsp6GtvstjyfLL8ysyVY6d2jjyFrbGDRAGcX3NAFMgmX8VpQJUqXQphX6TN2kw1Vwdi2NQPf1Zhrvxs3APNTZ5AMfPmPMBJGwi5zQsaqmY5E12X4MGPEHYxLJ9t4ciNtGVyXqPkegqorr3jeFTMEBpLmTdwxmcTiTWV9a"
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.777)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "state": "tx_3XPhV5wAjiGDkRzer6TXnbeV4cFiyoHD4wV6uPhYgTQhN8FMdVrm5PfkUERKVGjYkTmSp9VmtpDKoFWd8ioi8wwvwjabuC1Ypf16mEnXqFj1vBFixwjdjUqxNbrYWg7KwMek6TCP3YFQSp7rZ4FTmRXYavkfZXaYU6PAJ2Vw7WLT67srAwi8WmyvaXRanKqDZBQycr9QxyFGWYcSL7Gtj6iAbxznfQTrQxDAAHUW4krmppNEaNWMXow93PHzxA8DtFo7D46YUnAvDnJVXJ6rBqKSWp6Een3WTo6Es39AQPKvFDweD5fRBXHfJA5zp3X3FfDVdBAXB9JTk7M1VmV2G6ATwXasyJ13NuZxYgDRMhMqnnwwTyc3x9fgnnHZhJ2QNiw5VmqxCjRHPM3uLXu5P"
    }
  }
}
```

#### responder <--- (2018-10-24 12:54:06.778)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "state": "tx_3XPhV5wAjiGDkRzer6TXnbeV4cFiyoHD4wV6uPhYgTQhN8FMdVrm5PfkUERKVGjYkTmSp9VmtpDKoFWd8ioi8wwvwjabuC1Ypf16mEnXqFj1vBFixwjdjUqxNbrYWg7KwMek6TCP3YFQSp7rZ4FTmRXYavkfZXaYU6PAJ2Vw7WLT67srAwi8WmyvaXRanKqDZBQycr9QxyFGWYcSL7Gtj6iAbxznfQTrQxDAAHUW4krmppNEaNWMXow93PHzxA8DtFo7D46YUnAvDnJVXJ6rBqKSWp6Een3WTo6Es39AQPKvFDweD5fRBXHfJA5zp3X3FfDVdBAXB9JTk7M1VmV2G6ATwXasyJ13NuZxYgDRMhMqnnwwTyc3x9fgnnHZhJ2QNiw5VmqxCjRHPM3uLXu5P"
    }
  }
}
```

#### initiator ---> (2018-10-24 12:54:06.782)
```javascript
{
  "id": -576460752303423448,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
      "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY"
    ]
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.784)
```javascript
{
  "id": -576460752303423448,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
      "balance": 401
    },
    {
      "account": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
      "balance": 699
    }
  ]
}
```

#### initiator ---> (2018-10-24 12:54:06.784)
```javascript
{
  "id": -576460752303423447,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
      "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY"
    ]
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.786)
```javascript
{
  "id": -576460752303423447,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
      "balance": 401
    },
    {
      "account": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
      "balance": 699
    }
  ]
}
```

#### responder ---> (2018-10-24 12:54:06.786)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
    "to": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY"
  }
}
```

#### responder <--- (2018-10-24 12:54:06.791)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "tx": "tx_GB8bJXCQR918gbjgUqaGfGDPGZ8Z3GQeSBXNeB5rQZweAc7knLTRYW44hFEqisi7r3Q2LHhx9ztGWFqXvJBP9HxPYBEAj4vwVQYcHbbPt18UoFV3tF6wVds891b7E92NB3WiovG2zVjAjJk16QrDtBbYLKMrhu7FjwXmqqh4d1J2WGAB9tCsFEtLWY6Tbqb8YHVcyR4egThdHjZZWnkQ"
    }
  }
}
```

#### responder ---> (2018-10-24 12:54:06.792)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4xXxtomN7Qrntndv2ryGHrw2vuRrvQ6DZ9w4cpkYX241LvFkmMNEyL4xjm3vB8og2xYkVTzJXnEP6QSxhQVYU2QGmfBehwdcBTMmGvPSXrzCL8CoYVNKoxkoyvBfEayQWHGg4YtWKBfk8RJhUz1HKrYP6Zi3we2S3kbnBSpQ2qX7KTKMDsqELme8R6gKaiF4XncmCGYKy7nYdEcWiUWscto2jCz2b4jRxBnRHTj6EXByLqEKUvT97tNdHeAfCQqtFkVZjy6tmY2QjVsUo6ssJy1uQjoy3qvTox53EiKLM6nCWkE"
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.797)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "event": "update"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.797)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "tx": "tx_GB8bJXCQR918gbjgUqaGfGDPGZ8Z3GQeSBXNeB5rQZweAc7knLTRYW44hFEqisi7r3Q2LHhx9ztGWFqXvJBP9HxPYBEAj4vwVQYcHbbPt18UoFV3tF6wVds891b7E92NB3WiovG2zVjAjJk16QrDtBbYLKMrhu7FjwXmqqh4d1J2WGAB9tCsFEtLWY6Tbqb8YHVcyR4egThdHjZZWnkQ"
    }
  }
}
```

#### initiator ---> (2018-10-24 12:54:06.798)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4mAtvUqMiwXRJJtcREiimv5YwnquK4pKKPMHFLZ6An4LmFeUrV8hHoKutiyRvEtzPcimD9J45igtSewo5WdBCWhoW48KTfc9WURapEAnKkMEiYbGaTj8yY2o37h6fahZFbMa43v9uAADucapv3CVbwENBGrWzByNSgcYK77BFim2zJ6BR3KR2aLqxg3cC85CYBsXtdKjaxqyUBEf1FuzH5wQEsqR2D5PrQAtZsXJd8RB3vwv2QxvLQVF1MnZ1EGz3d2Tq9PAqrbidAEY6eQDftvAFHKmsqtL5Ww7wyCNH8jJZSz"
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.803)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "state": "tx_3XPhV5wAjiGDkLVxrK4YdUry7Sdsehpu3cb1uuwcRqFDTpKeeB9E1HRejPi6xgZjJBcVkYxRWRR8r2GQtiYJbXAFGidxhSHBFpuu3usna5fvEJAakHA4VQcdqm2zF96SpnQGwWavSW2NFoQkZYbTVM6Qnpmfg3XJA9n3MteGLHnKcffVDYvg7QZ8ZcP2iQai8aPB4rc9QrDwkGiKzoBvBriNjNzj7CwAf1fD2qibbDvpd7saVVThiMDV79aSjhx9QAJPJokmRL5c3G5jLr7ayepcTM1hSTVCb6eWj7iAWg6AFj747Exux4fNjmUPUPinZdqyMhYeTCm5ovnTRFCMPh1UqUDczPnn2rrqa72Ai3kkukKvq6gtP9LKy6QVUAajPRDq8NbW35u4zPyiQUzPr"
    }
  }
}
```

#### responder <--- (2018-10-24 12:54:06.804)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "state": "tx_3XPhV5wAjiGDkLVxrK4YdUry7Sdsehpu3cb1uuwcRqFDTpKeeB9E1HRejPi6xgZjJBcVkYxRWRR8r2GQtiYJbXAFGidxhSHBFpuu3usna5fvEJAakHA4VQcdqm2zF96SpnQGwWavSW2NFoQkZYbTVM6Qnpmfg3XJA9n3MteGLHnKcffVDYvg7QZ8ZcP2iQai8aPB4rc9QrDwkGiKzoBvBriNjNzj7CwAf1fD2qibbDvpd7saVVThiMDV79aSjhx9QAJPJokmRL5c3G5jLr7ayepcTM1hSTVCb6eWj7iAWg6AFj747Exux4fNjmUPUPinZdqyMhYeTCm5ovnTRFCMPh1UqUDczPnn2rrqa72Ai3kkukKvq6gtP9LKy6QVUAajPRDq8NbW35u4zPyiQUzPr"
    }
  }
}
```

#### initiator ---> (2018-10-24 12:54:06.807)
```javascript
{
  "id": -576460752303423446,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
      "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY"
    ]
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.808)
```javascript
{
  "id": -576460752303423446,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
      "balance": 400
    },
    {
      "account": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
      "balance": 700
    }
  ]
}
```

#### initiator ---> (2018-10-24 12:54:06.808)
```javascript
{
  "id": -576460752303423445,
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

#### initiator <--- (2018-10-24 12:54:06.809)
```javascript
{
  "id": -576460752303423445,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
      "balance": 700
    },
    {
      "account": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
      "balance": 400
    }
  ]
}
```

#### initiator ---> (2018-10-24 12:54:06.810)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
    "to": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ"
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.813)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "tx": "tx_GB8bJXCQR918gbjgUqaGfGDPGZ8Z3GQeSBXNeB5rQZweAc7knLTRYbUaYnnJvDS3c2w9EPxBbmz3jmNvjbtm3KoDCtriGXvmDMsHBwroz1zM8tdzs4WeS7WqcrbGwnfcuEdAHLLRD7UbSw64geeq5szy4xrfujNBnEsJ8bErk9WVYwQC1PbAuHMHU6F5YubH87FfSExCUyFdgyf8Qqjm"
    }
  }
}
```

#### initiator ---> (2018-10-24 12:54:06.814)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4sd77AmeTKG3FZVTZB4jZN2e1LM936vQcef4LbPVmWZ2cyCEPqXaSvsbFKPjhcBVLs2w4Lz4JZhCfFvfLnp37XYeGKmNxPEPq9y6R2AKcLBnjTF5goRqPGi4xNGSAthfZgWMEnErXc1uUMvPWmGsXSdXJRVfmbBqDcBsDUgy5c31zHkS5Bb5hsRoKZeYfaBQhtak3tjcLwqUN6XomKUGT8VxdmRy5xx41irfMMBTrKCSx5FPNYjui78hVXEbvoeGbjzXafhx8qYtzWsykGv3qvNUvug8AAaneLKQh77Nhp7nNG5"
  }
}
```

#### responder <--- (2018-10-24 12:54:06.852)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "event": "update"
    }
  }
}
```

#### responder <--- (2018-10-24 12:54:06.854)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "tx": "tx_GB8bJXCQR918gbjgUqaGfGDPGZ8Z3GQeSBXNeB5rQZweAc7knLTRYbUaYnnJvDS3c2w9EPxBbmz3jmNvjbtm3KoDCtriGXvmDMsHBwroz1zM8tdzs4WeS7WqcrbGwnfcuEdAHLLRD7UbSw64geeq5szy4xrfujNBnEsJ8bErk9WVYwQC1PbAuHMHU6F5YubH87FfSExCUyFdgyf8Qqjm"
    }
  }
}
```

#### responder ---> (2018-10-24 12:54:06.857)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak54HJeNa1xRGQMf31EEQFFrY5DhYDJRHG3mSGrfcr2LmEH7NTfdW24WHf47Ws34qzcFAqzoVSFX6hTe6jj2sqm6szxmdUdZNWVRrfBrNefxoLxrVL3g4c2oMDySyRED6W17T66WQsgA3DX8sNRg58D4MWokjxWc45WuFtCQ1izSRRLFyxwNcVVyPuqXrMgBm4nYKm75sofx7d873M5HagDy7VMAbG24FPmXUkppZGFcGRALGisGLmg4vzp1kdXjWvbhYHB918XMmVbZP6Ruxn8bNuMt8fGD1Jr2Q3TutYzW7RmZx"
  }
}
```

#### responder <--- (2018-10-24 12:54:06.870)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "state": "tx_3XPhV5wAjiGDkXbHzEdEnCe2kHYwfWGzGE5bX4DLUAeExJyKRZEcxHWqGaAN6xfjA3GPwA3FYLUvJkmp6GAhAqx3aCBrs3CWfK6is6C4GXuAZWrxsaYf3ePph2V2E31BeKHuc4vyq8ojUwydCQrBVozHKB2jEpQcmxi5cbjvTpCrr74vnXu3i9qWow32Gdxed5hggJ6fcEeYcTUbBHxvSNmM8EbUSKhNzskRARrn6Mo3vzxS3GUpV6dFjvx6CDZ3pyTp7q86yW9u1UKuHsZrQB8nkHMogDzgUDHzcAV3iFp53qy8QUdAWHBC7zSJei4W6swscQdk41FM4Z4wA8FCJSuVh3ds3iBbsLGskxz5mexKSqz67SoSLWzuVjLBPco4vFb4pq76vAbHsZiC3nqUQ"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.871)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "state": "tx_3XPhV5wAjiGDkXbHzEdEnCe2kHYwfWGzGE5bX4DLUAeExJyKRZEcxHWqGaAN6xfjA3GPwA3FYLUvJkmp6GAhAqx3aCBrs3CWfK6is6C4GXuAZWrxsaYf3ePph2V2E31BeKHuc4vyq8ojUwydCQrBVozHKB2jEpQcmxi5cbjvTpCrr74vnXu3i9qWow32Gdxed5hggJ6fcEeYcTUbBHxvSNmM8EbUSKhNzskRARrn6Mo3vzxS3GUpV6dFjvx6CDZ3pyTp7q86yW9u1UKuHsZrQB8nkHMogDzgUDHzcAV3iFp53qy8QUdAWHBC7zSJei4W6swscQdk41FM4Z4wA8FCJSuVh3ds3iBbsLGskxz5mexKSqz67SoSLWzuVjLBPco4vFb4pq76vAbHsZiC3nqUQ"
    }
  }
}
```

#### initiator ---> (2018-10-24 12:54:06.878)
```javascript
{
  "id": -576460752303423444,
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

#### initiator <--- (2018-10-24 12:54:06.881)
```javascript
{
  "id": -576460752303423444,
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

#### initiator ---> (2018-10-24 12:54:06.881)
```javascript
{
  "id": -576460752303423443,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
      "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY"
    ]
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.883)
```javascript
{
  "id": -576460752303423443,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
      "balance": 401
    },
    {
      "account": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
      "balance": 699
    }
  ]
}
```

#### responder ---> (2018-10-24 12:54:06.883)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
    "to": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY"
  }
}
```

#### responder <--- (2018-10-24 12:54:06.888)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "tx": "tx_GB8bJXCQR918gbjgUqaGfGDPGZ8Z3GQeSBXNeB5rQZweAc7knLTRYgu6QLKn7Z9yN2UG8XPwibwjd8yfsfydyPjdP8jYCa8zTwNqdJKuBtcnz8tdMoH8runP98DxzeGEjtg8ES1LrVyoBCTrFYH3Eva373Ghh5dkMGbzWGSpv5QBqj5CGbic5ZCr9zWzSi2YLhRbuqjEVWhZfQSq3m3a"
    }
  }
}
```

#### responder ---> (2018-10-24 12:54:06.889)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4ksXxbDWQuQ3rkpoUv6AW8Sw8qXpRtHBQ3p5vAhAEbq5BBtCSZTEF6Pjyp88r5knX9VgGWKJNhHoZgaPiHA69dsWwzuq7auiD98ZjjJtdjpiaLZsjEHUXbr2u6S7tN4ZQermpNFEHn82fwqEAyMWgSapE2F4rnCAtUXGNNXMSCGJkzvLPdnE6ELZiXvqd69HGGfRaYm3mNmasVwwZfXHfAigNBfJjG5VaRUSDwFo2mfXpYs1g4QNV7ZReM3M9DjUaBq9bGA2WzokJEdnb4VuXaEtSiNnjFQWk7NeHw4uSXHT8uZ"
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.903)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "event": "update"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.903)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "tx": "tx_GB8bJXCQR918gbjgUqaGfGDPGZ8Z3GQeSBXNeB5rQZweAc7knLTRYgu6QLKn7Z9yN2UG8XPwibwjd8yfsfydyPjdP8jYCa8zTwNqdJKuBtcnz8tdMoH8runP98DxzeGEjtg8ES1LrVyoBCTrFYH3Eva373Ghh5dkMGbzWGSpv5QBqj5CGbic5ZCr9zWzSi2YLhRbuqjEVWhZfQSq3m3a"
    }
  }
}
```

#### initiator ---> (2018-10-24 12:54:06.904)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak58z56CNWwLD7MLysSmgf1CvcMNBDxunEzqUybZ5d6h6EMqmNg8QfMjqpQMpbv7WGtGypVQ3xVbC9sgbNGScCVYsKT1GVAY8UFxFZjVoHLWCdFkoRffipSzZHLVWWmaDWgd3HYEvBZ2BjMR5cX1ahVy7huYywZGqSn9pBM873ivnBzKEdSzxEFW4BF8BLTiL3GapE9LT8RVtCnfXQkzzCHg54QMHShekcFtLKmYyrBsJohgUeNRcG1JH7Wi2Lr1F362i16oJQ3L39qk5qKigQmBdaY1SsgWXoUQ9Q3jnMrTomm62"
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.909)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "state": "tx_3XPhV5wAjiGDkKz7iDivG4Z42Z5P25cmLPbJMyCT8yuktt5z3poJBrkRkbgnT6tMqZoP2mbXB3sNgKrJU4pmhK7QQqXgUkjqmS51hqeCsQJbisoyU3gacXfjxdFbnmLb3FVYuZ6FsMJqBybKnTCR7yWyUeDCterhLzHXRgTsejiRXNjz9osm5jmY5BFFhRHwmFATxKR1Zvetc4j3qLATpX2QhnQWSQiNrurqEnVUHGj6gue3CmPMqKEsn2yMv26JkcfaEYUZE4Rgh2QGBTwRfddFqDyivTNhpFrCH46r9ped5EsrRma7PnhzDDNzy5XNXaBPpz8Achq5QDZUK1FuLxGRqZZ2HxuuWVwGi12rVzAap3CBicsPK969SP1P2NiWUPPRP5iLFyELJdrBdujca"
    }
  }
}
```

#### responder <--- (2018-10-24 12:54:06.910)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "state": "tx_3XPhV5wAjiGDkKz7iDivG4Z42Z5P25cmLPbJMyCT8yuktt5z3poJBrkRkbgnT6tMqZoP2mbXB3sNgKrJU4pmhK7QQqXgUkjqmS51hqeCsQJbisoyU3gacXfjxdFbnmLb3FVYuZ6FsMJqBybKnTCR7yWyUeDCterhLzHXRgTsejiRXNjz9osm5jmY5BFFhRHwmFATxKR1Zvetc4j3qLATpX2QhnQWSQiNrurqEnVUHGj6gue3CmPMqKEsn2yMv26JkcfaEYUZE4Rgh2QGBTwRfddFqDyivTNhpFrCH46r9ped5EsrRma7PnhzDDNzy5XNXaBPpz8Achq5QDZUK1FuLxGRqZZ2HxuuWVwGi12rVzAap3CBicsPK969SP1P2NiWUPPRP5iLFyELJdrBdujca"
    }
  }
}
```

#### initiator ---> (2018-10-24 12:54:06.913)
```javascript
{
  "id": -576460752303423442,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
      "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY"
    ]
  }
}
```

#### initiator <--- (2018-10-24 12:54:06.914)
```javascript
{
  "id": -576460752303423442,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
      "balance": 400
    },
    {
      "account": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
      "balance": 700
    }
  ]
}
```

#### initiator ---> (2018-10-24 12:54:06.999)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### initiator <--- (2018-10-24 12:54:07.3)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "tx": "tx_2M9ipLgcZJHoEYxWkxkZWbnBQv3hZfn6sAawrEcL1sghwDEsaAy8FkXWebZGDQ7xTFcYFAJSS2qkVLB52iVXhcvX6Qr8aDDgkhxjmYwCFnRAJ3h6gz9WQ"
    }
  }
}
```

#### initiator ---> (2018-10-24 12:54:07.4)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "tx": "tx_2iJcVi27J8a12S5YZB9UAnYSHkQupNwrriB63E63jee9AHAE4LPQwr9JN8NuW1oGHHqQRD2UpYUHnqPKBj13eKx6YQznpjCzLLKJF787cbXH1vDXtbfY5Zd4BovgKFNo6Y7nSnk8R4F3GXWA1KDqMJiPtb7kXFBDm3pUkf35CYpUGLRg6eNd6KLHzbCjRakoXkX9fxNLeM75PezTjTVA8JPzEx"
  }
}
```

#### responder <--- (2018-10-24 12:54:07.6)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "tx": "tx_2M9ipLgcZJHoEYxWkxkZWbnBQv3hZfn6sAawrEcL1sghwDEsaAy8FkXWebZGDQ7xTFcYFAJSS2qkVLB52iVXhcvX6Qr8aDDgkhxjmYwCFnRAJ3h6gz9WQ"
    }
  }
}
```

#### responder ---> (2018-10-24 12:54:07.7)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "tx": "tx_2iJcVi27J8ZzYhjcCtoWwJiKgc7Nb9oC1PNxCsQHMj7JaHGAcaBYu3XNnGeVarSYzGF1eHcnb9KgXam7FiTWjQaypGB5Ea8252h1SCK6WnGbbLAFa7eHwyNgpYmTBEGr5MuGmNsXCKVCXG4dWHjBybc2oCDuzGQ6vxUU1vL3Nr7DHXbaSQu3L1KUFsRKpPvmHACFecrT6rb4es6HVc1se6ieHT"
  }
}
```

#### responder <--- (2018-10-24 12:54:07.9)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "tx": "tx_3wu1WL1txa1ZD4xAJexv9VJrAQB9pPx83q3tNv8eybUXrNFwAZoVBX48YtRVXGcjMnAcrUgNxxxLXuAoFu1oCKvDGFPVuaBTCiyHXg5zGSFCvSEUizk7V3GnJMeosVQHwJRiP41hs7Wvzvy3qR9wfTo9V9neP45Apa39YkEcQcpkAomQPt2DyHtG8yZwwmXV3TDDRaADUxf7eCkfZ7A3fDLrnZTGoM1CsGk6zjCkHj1fZau8CQgTGdVfA57mijXPVM6qVnmkgfJL6nvRg3NJPMCqk81zaXQwxQuZasHZx9CCLXSgoj2C"
    }
  }
}
```

#### responder <--- (2018-10-24 12:54:07.10)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "event": "close_mutual"
    }
  }
}
```

#### responder <--- (2018-10-24 12:54:07.10)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "event": "died"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:54:07.17)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "tx": "tx_3wu1WL1txa1ZD4xAJexv9VJrAQB9pPx83q3tNv8eybUXrNFwAZoVBX48YtRVXGcjMnAcrUgNxxxLXuAoFu1oCKvDGFPVuaBTCiyHXg5zGSFCvSEUizk7V3GnJMeosVQHwJRiP41hs7Wvzvy3qR9wfTo9V9neP45Apa39YkEcQcpkAomQPt2DyHtG8yZwwmXV3TDDRaADUxf7eCkfZ7A3fDLrnZTGoM1CsGk6zjCkHj1fZau8CQgTGdVfA57mijXPVM6qVnmkgfJL6nvRg3NJPMCqk81zaXQwxQuZasHZx9CCLXSgoj2C"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:54:07.17)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "event": "close_mutual"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:54:07.17)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_24mkF7qyEGfQmX8Wa9ocme6XtotAcPTBtv5xMycnxgP6KnN8Nm",
    "data": {
      "event": "died"
    }
  }
}
```
