
#### initiator init (2018-10-24 13:00:06.366)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=initiator
```

#### responder init (2018-10-24 13:00:06.369)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=responder
```

#### responder <--- (2018-10-24 13:00:07.373)
```javascript
{
  "action": "info",
  "payload": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-24 13:00:07.375)
```javascript
{
  "action": "info",
  "payload": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-24 13:00:07.380)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_3d11KjpALm3t32sAMLL9Y5p9SUg9j82o5Er3hc4WTAmdXk3cXjxDydY4eoq6STXDutDQ59tM59bMr9CogemLkb4tUXrrZYvPc4DkdzkXhqGZjnzLVRAYpjMHXUeVmmqr9Fk96GrERRgHqJTaNp7wfhyEnqvb1nHjvLVwNk"
  },
  "tag": "initiator_sign"
}
```

#### initiator ---> (2018-10-24 13:00:07.399)
```javascript
{
  "action": "initiator_sign",
  "payload": {
    "tx": "tx_4L9GSozvM4HoFV8ZVrdmdr4b99SFrBrqQAGwnwGMUBx4Dy54Dex5pJRmv8mpTdzm4Wywj17XMsscVEHPQfdJzXXkzfLs1CwESwmLMknQ2B4f4DHChvLZrhYwkfSgWfT7KsJoyXw85EUHrXc6nev68tqrQ4nj7vdnUGSBKWHkk1qxVoK88JWdBoYD3pJPpY6Q5NTpMmk3st7F9wQ8jJVpUXhQoBaQar6HuMtiD5qRU5CLrJPfogYKxM5cNoUYs1uW5AsFruzV6Qd"
  }
}
```

#### responder <--- (2018-10-24 13:00:07.400)
```javascript
{
  "action": "info",
  "payload": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-24 13:00:07.400)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_3d11KjpALm3t32sAMLL9Y5p9SUg9j82o5Er3hc4WTAmdXk3cXjxDydY4eoq6STXDutDQ59tM59bMr9CogemLkb4tUXrrZYvPc4DkdzkXhqGZjnzLVRAYpjMHXUeVmmqr9Fk96GrERRgHqJTaNp7wfhyEnqvb1nHjvLVwNk"
  },
  "tag": "responder_sign"
}
```

#### responder ---> (2018-10-24 13:00:07.401)
```javascript
{
  "action": "responder_sign",
  "payload": {
    "tx": "tx_4L9GSozvM4Hn9huuQkAkdg54UeSH4c4KfuuCxEgTe2k5w7jvkBJXTio8yAzhegjz6QgrUBjYb4CfWAoeZyjuvsDkiiy5PYeb4SD9B6XUkEcU7ou7cYT96A3Cbp2Qg7ww5VmfiHD3p9RdxMBdcUEZyaQH31JR5KUc7xf8t5SnqGp5tV3YfaXUbL2x1gtZK8REUySNV8HdFRxRtuEpjAJY5Nr4TB99RtVoF6JLGfVSCogLEVqRfPepyvfRE42yf5qcbDxEpKzsoPR"
  }
}
```

#### initiator <--- (2018-10-24 13:00:07.402)
```javascript
{
  "action": "info",
  "payload": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-24 13:00:07.403)
```javascript
{
  "action": "on_chain_tx",
  "payload": {
    "tx": "tx_6jPYBUFTkcmRuPWo4yf162derY4aDB2JmLDxkCw5wURvbGkvW9nvVNVKfTn8P9ujiWYkEHd5CcZ7dSbptrfWWJtXU6rXjhPP5vp7278Mx5oPH1YrGcGxCmdxfH9ToMBG69nNMbF3G4x3DeEbiagAG4KYAtTBWohidaE5Zm2H8ZUXszHP41ST61XXibeo6oK3BizHXmwUKm81LMnSgPyJXJ5D4wy9A9a8jg1r5qp8uJv55Vr1MZ6UwaNvmXytHMi4KfdA2EJ5k5ysNRYnHViQU5Wok5tnPRmb3GuicpTRXruG5rDhqeGopqbMDT3GJg4MGLXVszzz97j1FiT3fPZL2ycDjBE9sfZ51mFgm"
  }
}
```

#### initiator <--- (2018-10-24 13:00:07.404)
```javascript
{
  "action": "on_chain_tx",
  "payload": {
    "tx": "tx_6jPYBUFTkcmRuPWo4yf162derY4aDB2JmLDxkCw5wURvbGkvW9nvVNVKfTn8P9ujiWYkEHd5CcZ7dSbptrfWWJtXU6rXjhPP5vp7278Mx5oPH1YrGcGxCmdxfH9ToMBG69nNMbF3G4x3DeEbiagAG4KYAtTBWohidaE5Zm2H8ZUXszHP41ST61XXibeo6oK3BizHXmwUKm81LMnSgPyJXJ5D4wy9A9a8jg1r5qp8uJv55Vr1MZ6UwaNvmXytHMi4KfdA2EJ5k5ysNRYnHViQU5Wok5tnPRmb3GuicpTRXruG5rDhqeGopqbMDT3GJg4MGLXVszzz97j1FiT3fPZL2ycDjBE9sfZ51mFgm"
  }
}
```

#### initiator ---> (2018-10-24 13:00:09.900)
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

#### initiator <--- (2018-10-24 13:00:09.902)
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

#### responder <--- (2018-10-24 13:00:16.729)
```javascript
{
  "action": "info",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "event": "own_funding_locked"
  }
}
```

#### initiator <--- (2018-10-24 13:00:16.730)
```javascript
{
  "action": "info",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "event": "own_funding_locked"
  }
}
```

#### initiator <--- (2018-10-24 13:00:16.730)
```javascript
{
  "action": "info",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "event": "funding_locked"
  }
}
```

#### responder <--- (2018-10-24 13:00:16.731)
```javascript
{
  "action": "info",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "event": "funding_locked"
  }
}
```

#### responder <--- (2018-10-24 13:00:16.734)
```javascript
{
  "action": "info",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "event": "open"
  }
}
```

#### initiator <--- (2018-10-24 13:00:16.734)
```javascript
{
  "action": "info",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "event": "open"
  }
}
```

#### responder <--- (2018-10-24 13:00:16.735)
```javascript
{
  "action": "update",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "state": "tx_6jPYBUFTkcmRuPWo4yf162derY4aDB2JmLDxkCw5wURvbGkvW9nvVNVKfTn8P9ujiWYkEHd5CcZ7dSbptrfWWJtXU6rXjhPP5vp7278Mx5oPH1YrGcGxCmdxfH9ToMBG69nNMbF3G4x3DeEbiagAG4KYAtTBWohidaE5Zm2H8ZUXszHP41ST61XXibeo6oK3BizHXmwUKm81LMnSgPyJXJ5D4wy9A9a8jg1r5qp8uJv55Vr1MZ6UwaNvmXytHMi4KfdA2EJ5k5ysNRYnHViQU5Wok5tnPRmb3GuicpTRXruG5rDhqeGopqbMDT3GJg4MGLXVszzz97j1FiT3fPZL2ycDjBE9sfZ51mFgm"
  }
}
```

#### initiator <--- (2018-10-24 13:00:16.736)
```javascript
{
  "action": "update",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "state": "tx_6jPYBUFTkcmRuPWo4yf162derY4aDB2JmLDxkCw5wURvbGkvW9nvVNVKfTn8P9ujiWYkEHd5CcZ7dSbptrfWWJtXU6rXjhPP5vp7278Mx5oPH1YrGcGxCmdxfH9ToMBG69nNMbF3G4x3DeEbiagAG4KYAtTBWohidaE5Zm2H8ZUXszHP41ST61XXibeo6oK3BizHXmwUKm81LMnSgPyJXJ5D4wy9A9a8jg1r5qp8uJv55Vr1MZ6UwaNvmXytHMi4KfdA2EJ5k5ysNRYnHViQU5Wok5tnPRmb3GuicpTRXruG5rDhqeGopqbMDT3GJg4MGLXVszzz97j1FiT3fPZL2ycDjBE9sfZ51mFgm"
  }
}
```

#### initiator: (2018-10-24 13:00:17.402)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-24 13:00:17.402)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-24 13:00:17.402)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-24 13:00:17.402)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-24 13:00:17.403)
> Channel is `open` and ready to use

#### responder: (2018-10-24 13:00:17.403)
> Channel is `open` and ready to use

#### initiator ---> (2018-10-24 13:00:17.442)
```javascript
{
  "action": "leave"
}
```

#### responder <--- (2018-10-24 13:00:17.450)
```javascript
{
  "action": "leave",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "state": "tx_6jPYBUFTkcmRuPWo4yf162derY4aDB2JmLDxkCw5wURvbGkvW9nvVNVKfTn8P9ujiWYkEHd5CcZ7dSbptrfWWJtXU6rXjhPP5vp7278Mx5oPH1YrGcGxCmdxfH9ToMBG69nNMbF3G4x3DeEbiagAG4KYAtTBWohidaE5Zm2H8ZUXszHP41ST61XXibeo6oK3BizHXmwUKm81LMnSgPyJXJ5D4wy9A9a8jg1r5qp8uJv55Vr1MZ6UwaNvmXytHMi4KfdA2EJ5k5ysNRYnHViQU5Wok5tnPRmb3GuicpTRXruG5rDhqeGopqbMDT3GJg4MGLXVszzz97j1FiT3fPZL2ycDjBE9sfZ51mFgm"
  }
}
```

#### responder <--- (2018-10-24 13:00:17.451)
```javascript
{
  "action": "info",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "event": "died"
  }
}
```

#### initiator <--- (2018-10-24 13:00:17.452)
```javascript
{
  "action": "leave",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "state": "tx_6jPYBUFTkcmRuPWo4yf162derY4aDB2JmLDxkCw5wURvbGkvW9nvVNVKfTn8P9ujiWYkEHd5CcZ7dSbptrfWWJtXU6rXjhPP5vp7278Mx5oPH1YrGcGxCmdxfH9ToMBG69nNMbF3G4x3DeEbiagAG4KYAtTBWohidaE5Zm2H8ZUXszHP41ST61XXibeo6oK3BizHXmwUKm81LMnSgPyJXJ5D4wy9A9a8jg1r5qp8uJv55Vr1MZ6UwaNvmXytHMi4KfdA2EJ5k5ysNRYnHViQU5Wok5tnPRmb3GuicpTRXruG5rDhqeGopqbMDT3GJg4MGLXVszzz97j1FiT3fPZL2ycDjBE9sfZ51mFgm"
  }
}
```

#### initiator <--- (2018-10-24 13:00:17.453)
```javascript
{
  "action": "info",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "event": "died"
  }
}
```

#### responder init (2018-10-24 13:00:17.509)
```
ws://localhost:3014/channel?channel_reserve=2&existing_channel_id=ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&offchain_tx=tx_6jPYBUFTkcmRuPWo4yf162derY4aDB2JmLDxkCw5wURvbGkvW9nvVNVKfTn8P9ujiWYkEHd5CcZ7dSbptrfWWJtXU6rXjhPP5vp7278Mx5oPH1YrGcGxCmdxfH9ToMBG69nNMbF3G4x3DeEbiagAG4KYAtTBWohidaE5Zm2H8ZUXszHP41ST61XXibeo6oK3BizHXmwUKm81LMnSgPyJXJ5D4wy9A9a8jg1r5qp8uJv55Vr1MZ6UwaNvmXytHMi4KfdA2EJ5k5ysNRYnHViQU5Wok5tnPRmb3GuicpTRXruG5rDhqeGopqbMDT3GJg4MGLXVszzz97j1FiT3fPZL2ycDjBE9sfZ51mFgm&port=12341&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=responder
```

#### initiator init (2018-10-24 13:00:17.516)
```
ws://localhost:3014/channel?channel_reserve=2&existing_channel_id=ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf&host=localhost&initiator_amount=700&initiator_id=ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL&lock_period=10&offchain_tx=tx_6jPYBUFTkcmRuPWo4yf162derY4aDB2JmLDxkCw5wURvbGkvW9nvVNVKfTn8P9ujiWYkEHd5CcZ7dSbptrfWWJtXU6rXjhPP5vp7278Mx5oPH1YrGcGxCmdxfH9ToMBG69nNMbF3G4x3DeEbiagAG4KYAtTBWohidaE5Zm2H8ZUXszHP41ST61XXibeo6oK3BizHXmwUKm81LMnSgPyJXJ5D4wy9A9a8jg1r5qp8uJv55Vr1MZ6UwaNvmXytHMi4KfdA2EJ5k5ysNRYnHViQU5Wok5tnPRmb3GuicpTRXruG5rDhqeGopqbMDT3GJg4MGLXVszzz97j1FiT3fPZL2ycDjBE9sfZ51mFgm&port=12341&protocol=legacy&push_amount=1&responder_amount=400&responder_id=ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt&role=initiator
```

#### responder <--- (2018-10-24 13:00:17.520)
```javascript
{
  "action": "info",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "event": "channel_reestablished"
  }
}
```

#### responder <--- (2018-10-24 13:00:17.521)
```javascript
{
  "action": "info",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "event": "open"
  }
}
```

#### initiator <--- (2018-10-24 13:00:17.522)
```javascript
{
  "action": "info",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "event": "channel_reestablished"
  }
}
```

#### initiator <--- (2018-10-24 13:00:17.522)
```javascript
{
  "action": "info",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "event": "open"
  }
}
```

#### responder <--- (2018-10-24 13:00:17.522)
```javascript
{
  "action": "update",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "state": "tx_6jPYBUFTkcmRuPWo4yf162derY4aDB2JmLDxkCw5wURvbGkvW9nvVNVKfTn8P9ujiWYkEHd5CcZ7dSbptrfWWJtXU6rXjhPP5vp7278Mx5oPH1YrGcGxCmdxfH9ToMBG69nNMbF3G4x3DeEbiagAG4KYAtTBWohidaE5Zm2H8ZUXszHP41ST61XXibeo6oK3BizHXmwUKm81LMnSgPyJXJ5D4wy9A9a8jg1r5qp8uJv55Vr1MZ6UwaNvmXytHMi4KfdA2EJ5k5ysNRYnHViQU5Wok5tnPRmb3GuicpTRXruG5rDhqeGopqbMDT3GJg4MGLXVszzz97j1FiT3fPZL2ycDjBE9sfZ51mFgm"
  }
}
```

#### initiator <--- (2018-10-24 13:00:17.523)
```javascript
{
  "action": "update",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "state": "tx_6jPYBUFTkcmRuPWo4yf162derY4aDB2JmLDxkCw5wURvbGkvW9nvVNVKfTn8P9ujiWYkEHd5CcZ7dSbptrfWWJtXU6rXjhPP5vp7278Mx5oPH1YrGcGxCmdxfH9ToMBG69nNMbF3G4x3DeEbiagAG4KYAtTBWohidaE5Zm2H8ZUXszHP41ST61XXibeo6oK3BizHXmwUKm81LMnSgPyJXJ5D4wy9A9a8jg1r5qp8uJv55Vr1MZ6UwaNvmXytHMi4KfdA2EJ5k5ysNRYnHViQU5Wok5tnPRmb3GuicpTRXruG5rDhqeGopqbMDT3GJg4MGLXVszzz97j1FiT3fPZL2ycDjBE9sfZ51mFgm"
  }
}
```

#### initiator ---> (2018-10-24 13:00:17.564)
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

#### initiator <--- (2018-10-24 13:00:17.567)
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

#### initiator ---> (2018-10-24 13:00:17.568)
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

#### initiator <--- (2018-10-24 13:00:17.579)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQMzFQwpi7ENiuTxdkZdKFAnqnLkBSMZdcLq5bJgJMFhMs8srsUzLhqWaggt9BbGeKKhu9dMdPALdsVL5mwbF1KNjYUNhhYnYHSLA8rG3Q2UQeoWMWZ8eMiSoEVPT8R4GwZSeyowF1DDBhtu2XD4UBqDeVKWhQ9cioetGdXhEmq5wiyPcjVTNsnFX6TGsd3Ajd1Qbm8fKZnkYz"
  },
  "tag": "update"
}
```

#### initiator ---> (2018-10-24 13:00:17.581)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4oVxZ8dWtyZ7zh9mP4eXEaEavnHeYU9r7yu574jegDsDPThVd636kMuy1EWQCB6jjq5SZB2MNJRMWuQhCk5Sd1d8dyvAqXSbWGJdJQcK8GA7Vvtxi6LW9PtMRLpgy57kheM2dpFDPsxh6n3f8kKYg2pDc4V5VESMEfcFE7TqG1ST3tbdcUL2SNug3HmHdG37vbHPzPp8UXMJzfNYHcZiJCyNrhm2gB1TKmZ8YiN54JArqZD4AUehzhCCo3am1Z8MMA92eze5MYUq2ewobJLKLb66UAuWpMY8pQK1sHDzxgtJK9u"
  }
}
```

#### responder <--- (2018-10-24 13:00:17.588)
```javascript
{
  "action": "info",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "event": "update"
  }
}
```

#### responder <--- (2018-10-24 13:00:17.589)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQMzFQwpi7ENiuTxdkZdKFAnqnLkBSMZdcLq5bJgJMFhMs8srsUzLhqWaggt9BbGeKKhu9dMdPALdsVL5mwbF1KNjYUNhhYnYHSLA8rG3Q2UQeoWMWZ8eMiSoEVPT8R4GwZSeyowF1DDBhtu2XD4UBqDeVKWhQ9cioetGdXhEmq5wiyPcjVTNsnFX6TGsd3Ajd1Qbm8fKZnkYz"
  },
  "tag": "update_ack"
}
```

#### responder ---> (2018-10-24 13:00:17.590)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak4sYThmvzbP3EeectjQvf15ANCSjih4nvawuPXp7MoNzsL52BJnsCN9YyrhUKuVKNhYGrMzPTL52oDBWYmpG2UHz3bCaf5kuTZiMSB2BaoEzE8PdjrDhtCf7RpxdqcLUkc9aMnWKDAuszZqtYf9XRyAGApVxYDxGLUy8Mva2oqZChmA4GuqJdnw5Z2963MSuNcAz5ntRR2V7g4RJKUZYKytXm18A5uefo9ZwDMFQRcmP5cREfLTJi46K9gJ8KGNTKa5b5puTwECPCu7TJpTpNxhArUtEp9CBdMuo1X9qoUPs74EM"
  }
}
```

#### responder <--- (2018-10-24 13:00:17.595)
```javascript
{
  "action": "update",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkQWABMvCCcUy43rsXK1RmeQNJDta8jRxcJSkzdUHV9uhckUZHuZVfnfFZgyAa5BG2MbB98eZydpXZogiboAun7mCorgug9Hwz86EBT7cF6UJH9K53GVRNctQFvfJx1yv23Fq5Y3dma76pGdGN3HPDvWHXjfvtgGyfNV5kRNUoCnzUwAQ7XNHiNLQhXENqASsoCmLqs3aWFyRqHETjrMF4Ap3T5kMkRr6JDZu3fnV6FwY5wKYx6Yx2b4SvTk4i4Rh4pmfFWYGNqBGvQszfQLKH61DhnWBS8UsYadM26kd6cCwVN6S9ZbwKxCn3MZrjm41xzaujgtzQNQ174KFzrU5p2zhQstMUHjRUrriZLHzTfJEvPXZUKK48PdTPXjHJrpHHXcfV7Lkx"
  }
}
```

#### initiator <--- (2018-10-24 13:00:17.597)
```javascript
{
  "action": "update",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkQWABMvCCcUy43rsXK1RmeQNJDta8jRxcJSkzdUHV9uhckUZHuZVfnfFZgyAa5BG2MbB98eZydpXZogiboAun7mCorgug9Hwz86EBT7cF6UJH9K53GVRNctQFvfJx1yv23Fq5Y3dma76pGdGN3HPDvWHXjfvtgGyfNV5kRNUoCnzUwAQ7XNHiNLQhXENqASsoCmLqs3aWFyRqHETjrMF4Ap3T5kMkRr6JDZu3fnV6FwY5wKYx6Yx2b4SvTk4i4Rh4pmfFWYGNqBGvQszfQLKH61DhnWBS8UsYadM26kd6cCwVN6S9ZbwKxCn3MZrjm41xzaujgtzQNQ174KFzrU5p2zhQstMUHjRUrriZLHzTfJEvPXZUKK48PdTPXjHJrpHHXcfV7Lkx"
  }
}
```

#### initiator ---> (2018-10-24 13:00:17.601)
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

#### initiator <--- (2018-10-24 13:00:17.602)
```javascript
{
  "action": "get",
  "payload": [
    {
      "account": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
      "balance": 698
    },
    {
      "account": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "balance": 402
    }
  ],
  "tag": "balances"
}
```

#### initiator ---> (2018-10-24 13:00:17.602)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- (2018-10-24 13:00:17.603)
```javascript
{
  "action": "get",
  "payload": [
    {
      "account": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "balance": 402
    },
    {
      "account": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
      "balance": 698
    }
  ],
  "tag": "balances"
}
```

#### responder ---> (2018-10-24 13:00:17.604)
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

#### responder <--- (2018-10-24 13:00:17.607)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQMzFQwpi7ENiuTxdkZdKFAnqnLkBSMZdcLq5bJgJMFhMs8yHPLXtB2rJcSsgJVPioN548KoAkMiADVfXSUPeFNUawtAWymxHB4PPNo7Vsc8UumXegSWe5xwRzbabBTphYm11piyb3SvoQEJM4JXaMe2HG2nHTXyvjP3vJiv2oFy23zqBNrcB8JsycovJ8Tbk7L1K9EjH7N2Zh"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 13:00:17.608)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak4mMpJgfCkoiGnriqAknjwsMUQHiq8UvALxAsnRawKNxUiBRdTw6t5ip2SwCwgkWAGfPgmDcqqggp7Z4KyJRnVgnPQgb1QXV9bRzFCTgeDyDAB7idEzFwgEWCw69GTG7WZ5jYc2Sis3DHJ59igxbj5bZCpaATqaGs3KsDU4mKkXS22k6zhSYsQuZ2TwdfMfHFAG4HYrjTr87PNUDtmBYx2Hdo8F2cQCYEnPmTgWPBxGzYNHsCTwuobwY4UWKahCZcLV4yYgZXWoNGdCCa6Pnga9rMKp4DMoGnnWJ7DQuZojitXC2"
  }
}
```

#### initiator <--- (2018-10-24 13:00:17.612)
```javascript
{
  "action": "info",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 13:00:17.612)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQMzFQwpi7ENiuTxdkZdKFAnqnLkBSMZdcLq5bJgJMFhMs8yHPLXtB2rJcSsgJVPioN548KoAkMiADVfXSUPeFNUawtAWymxHB4PPNo7Vsc8UumXegSWe5xwRzbabBTphYm11piyb3SvoQEJM4JXaMe2HG2nHTXyvjP3vJiv2oFy23zqBNrcB8JsycovJ8Tbk7L1K9EjH7N2Zh"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 13:00:17.613)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak4sBmtkrbQ4Ha99cJTEtJYbTfEeijLp8et9shr8rUBp6H2vNQXq6EqusuB8eprsWngVqFkhkGtX4PdVY4GHDZLfiXyhDQTLHJ1pZPLtyaWWszMGoWpZjntZVhkMEJcDWopmX6knhb1ZXVRcjJGsyJbLJ1aARenUbp9WCu1jjTXhrRATyJjjwf3s7FmwXQTU6w94gjLpaYQwyw3r86rWKt9GbkFLGpAoMmG8dDJGJYTKTGzJ1UWnnMQUjbU6DCmFwASQJqQgFJhXLeCSVPrL1Dt8JtSJ8HR281MdEiALPVYmQN1nU"
  }
}
```

#### initiator <--- (2018-10-24 13:00:17.617)
```javascript
{
  "action": "update",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkLpjk1mvZZhZEdxwx45wFcZPFa6vQhc7VPgdmoB7m4BpcBZsB4feP1sGRksodSn1ifFuf7VEq3CvPTdTEMW4wyQRGXn7n9imY5K1ppoQHt6Xr5xZBdD8kkL6GNRJPn6WSxBPtNmR8RNkED9TFgvMZaKt1ahTM81Q8TLNDCUq5qJooiCMvrTs2qeYZkVz8fmznFFzWmoMPBeRDNGJV5TmtSf2hXZv78Mw33DnhisjbinEsa2qndF7AoXhn7w1eo2zgytEJ1qFeA6LxoGVT579zpMwUzkJnL7gu5LEqQPzC7yHUibtH3BqRngbYi15pWoQV3XMVPTSi32dFMrgJWZXCjoyhWFDpvK9PceieHn9nTDGgu2yXxgtduXPsiNs2aph3eMVGehHm"
  }
}
```

#### responder <--- (2018-10-24 13:00:17.617)
```javascript
{
  "action": "update",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkLpjk1mvZZhZEdxwx45wFcZPFa6vQhc7VPgdmoB7m4BpcBZsB4feP1sGRksodSn1ifFuf7VEq3CvPTdTEMW4wyQRGXn7n9imY5K1ppoQHt6Xr5xZBdD8kkL6GNRJPn6WSxBPtNmR8RNkED9TFgvMZaKt1ahTM81Q8TLNDCUq5qJooiCMvrTs2qeYZkVz8fmznFFzWmoMPBeRDNGJV5TmtSf2hXZv78Mw33DnhisjbinEsa2qndF7AoXhn7w1eo2zgytEJ1qFeA6LxoGVT579zpMwUzkJnL7gu5LEqQPzC7yHUibtH3BqRngbYi15pWoQV3XMVPTSi32dFMrgJWZXCjoyhWFDpvK9PceieHn9nTDGgu2yXxgtduXPsiNs2aph3eMVGehHm"
  }
}
```

#### initiator ---> (2018-10-24 13:00:17.620)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- (2018-10-24 13:00:17.620)
```javascript
{
  "action": "get",
  "payload": [
    {
      "account": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "balance": 401
    },
    {
      "account": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
      "balance": 699
    }
  ],
  "tag": "balances"
}
```

#### initiator ---> (2018-10-24 13:00:17.621)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- (2018-10-24 13:00:17.622)
```javascript
{
  "action": "get",
  "payload": [
    {
      "account": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "balance": 401
    },
    {
      "account": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
      "balance": 699
    }
  ],
  "tag": "balances"
}
```

#### responder ---> (2018-10-24 13:00:17.622)
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

#### responder <--- (2018-10-24 13:00:17.625)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQMzFQwpi7ENiuTxdkZdKFAnqnLkBSMZdcLq5bJgJMFhMs94huC5ReEC2YCsDRPWZo9NartEjpLQ4LuiR4PsPw7EByNRw6SoeRiL8XtZCfLua1TAcJwZxWrC3vt1AtB5aCh198wvSy2VWoufqJgtXn8cYWLSqXza18pmZMV97vYjadSsJgU2ohpuQgbCYJTKXBFxpvsZ9dm8zK"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 13:00:17.626)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak5AarMv2uaLCSJFsEzhp3jS6uJ37SQ4apynyrZCyWH587T7QJTkw424m4B8uAzcU5ChVY7aHMHLxfwbA88GRQeDNthAopYTYmdLPBWhXSodBjUJ5d1zanjzTMz3j1kiLGAQ6sSJquhPd9KGBZFDu5iVnhzSB3fCzjEFpXZZvaJj2fudF9RzG4HpgeYLw9DzB3kuRHg9iUaqPDPgyyGCm95MAAGLJ4WqWA8Dh7xx1rkdGsr8zP34YPGB9hb8vjKnjz8DZsgBiS2Ervp5yzCJrCbMXgp3DTku3Hu2BXg2yL6HH4Zik"
  }
}
```

#### initiator <--- (2018-10-24 13:00:17.630)
```javascript
{
  "action": "info",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 13:00:17.630)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQMzFQwpi7ENiuTxdkZdKFAnqnLkBSMZdcLq5bJgJMFhMs94huC5ReEC2YCsDRPWZo9NartEjpLQ4LuiR4PsPw7EByNRw6SoeRiL8XtZCfLua1TAcJwZxWrC3vt1AtB5aCh198wvSy2VWoufqJgtXn8cYWLSqXza18pmZMV97vYjadSsJgU2ohpuQgbCYJTKXBFxpvsZ9dm8zK"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 13:00:17.631)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak4tFPoWmkAPKHf7ATj7DX2kTJcv8JWTQ96Cqz1rZY2GJs7T6VwtcwbfnHNisZnf38Lqqkt1bLUVgnzQxTnwoxkNCpCpSy1iVH5EaxFNpDHJLsitYX53WGobQZaGXVpUfXk2hAcJVNewPMXbUwmUptG85NUe5NUu8jcZhqHg8eL6cJQs7GT7VmETdf52AidRNa43rx1ByevCkYjPtYCsBePZZKGfoFpv4VRGnZPj5gzfU8p9iKCWRrFwGmqvFx2ZTkgDeJniQRT3c3NGLeHJKzGUK3SZE2KKJhgyUYk181mVGacJV"
  }
}
```

#### initiator <--- (2018-10-24 13:00:17.634)
```javascript
{
  "action": "update",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkYfgK6DZMuAat1PYDBeyUGYBMPXGPxTE7WZsHbM5cZnK5sHvQ8EQAfQp68TovRLwPXnMZYyfZUdDrWZukusKq3omqjeaup35oi9PnxEFCootQw1sYadNwEiAPmaDsTGUZZgpDnMcRcJXyocZpFMYkjLNKBFA1M3sD84edW7TDapfHES5oocuBFKNZQzVB5ZhkVAsxoRrh9T9tGvHjCirT9vH3PSgM4sbk6HcBAVvRqoiN3YdPVUXaV7qM9nkUCJZyPU4vSgwLQY5HToxRBmenRzBx3iJwtTXYNPUMQ55UJiEdupFLuLrdappiJ1rEGr7L49k2QUSWvTyHe9gPJTpNGWe1pUPvDCWde6HhUgNJvqdzQqXvrJ5VyKZfVDF6jo8LhBN9LYMH"
  }
}
```

#### responder <--- (2018-10-24 13:00:17.635)
```javascript
{
  "action": "update",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkYfgK6DZMuAat1PYDBeyUGYBMPXGPxTE7WZsHbM5cZnK5sHvQ8EQAfQp68TovRLwPXnMZYyfZUdDrWZukusKq3omqjeaup35oi9PnxEFCootQw1sYadNwEiAPmaDsTGUZZgpDnMcRcJXyocZpFMYkjLNKBFA1M3sD84edW7TDapfHES5oocuBFKNZQzVB5ZhkVAsxoRrh9T9tGvHjCirT9vH3PSgM4sbk6HcBAVvRqoiN3YdPVUXaV7qM9nkUCJZyPU4vSgwLQY5HToxRBmenRzBx3iJwtTXYNPUMQ55UJiEdupFLuLrdappiJ1rEGr7L49k2QUSWvTyHe9gPJTpNGWe1pUPvDCWde6HhUgNJvqdzQqXvrJ5VyKZfVDF6jo8LhBN9LYMH"
  }
}
```

#### initiator ---> (2018-10-24 13:00:17.637)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- (2018-10-24 13:00:17.638)
```javascript
{
  "action": "get",
  "payload": [
    {
      "account": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "balance": 400
    },
    {
      "account": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
      "balance": 700
    }
  ],
  "tag": "balances"
}
```

#### initiator ---> (2018-10-24 13:00:17.638)
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

#### initiator <--- (2018-10-24 13:00:17.639)
```javascript
{
  "action": "get",
  "payload": [
    {
      "account": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
      "balance": 700
    },
    {
      "account": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "balance": 400
    }
  ],
  "tag": "balances"
}
```

#### initiator ---> (2018-10-24 13:00:17.640)
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

#### initiator <--- (2018-10-24 13:00:17.642)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQMzFQwpi7ENiuTxdkZdKFAnqnLkBSMZdcLq5bJgJMFhMs9A8R3cy7RXkTxrkYHdBJfcVMJgLb6QLFjUkdi2W4XdYcwAx3ZLe3QAPc8b9mEofwrREQ4JbeNCf3LfCEYptuMT2vUmpmwuKvw1VGN9LTJzSEEWJfEi7D4keRivz4DXsFJQLFdHb1nA2ueE1Q8WcWKWm4mm6TjFmR"
  },
  "tag": "update"
}
```

#### initiator ---> (2018-10-24 13:00:17.643)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak51v3AFS1zuXcyRTR6b9KDHD2EY2xszPHkyPJa7T4p7DPyxnMpTHcDvdoySipALqCVFEQD2Tkua6VkaWhRLrP3h9EduwuDwvJYh46YQ18vLKNrDqMpAiT8zJ1T1i9XsXtZJiNifJ9h1Q5MPtmVKFn5sBJZKy5ka99wFezr45cbvxXLvKuqBF8skjCUhGoTJmC9mmriMPXmgDEmSkR4UbbAxfmCWcypivmqp4yrttZsvWnp17a5nY9bZEG2rsqr2nd7sptDVuQkAgMNzM9STCg3vV14wnVJafQMvE1MYPnixxk8vK"
  }
}
```

#### responder <--- (2018-10-24 13:00:17.679)
```javascript
{
  "action": "info",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "event": "update"
  }
}
```

#### responder <--- (2018-10-24 13:00:17.679)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQMzFQwpi7ENiuTxdkZdKFAnqnLkBSMZdcLq5bJgJMFhMs9A8R3cy7RXkTxrkYHdBJfcVMJgLb6QLFjUkdi2W4XdYcwAx3ZLe3QAPc8b9mEofwrREQ4JbeNCf3LfCEYptuMT2vUmpmwuKvw1VGN9LTJzSEEWJfEi7D4keRivz4DXsFJQLFdHb1nA2ueE1Q8WcWKWm4mm6TjFmR"
  },
  "tag": "update_ack"
}
```

#### responder ---> (2018-10-24 13:00:17.680)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak561UTif6z3KZFZrDnGLyqY5fx9ovgSEzHFiqFU98k44494439NFojLGmXX5mMLV84NJmgiW4aZS6Q71eXFBZusa9pCZ5s9p6dw14LMmBZHK9M59VNHkySTr8f9yxTV7g3mJwNR263rLHNiZxtLFeuwgo4TavvAioAGjsQ45LZEvuBke29HHSX4orvPUURCacnrFJNakANCX6VAz7JWHxxLLXwLrSRW9ognSVDFzW6UvGJs5LtsZiBXp6CMXiUC5F3yDcGQU6moa6JKsXPfkeUM3TCuWeCU2wwnJajFvd17Vxzvn"
  }
}
```

#### responder <--- (2018-10-24 13:00:17.686)
```javascript
{
  "action": "update",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkmr6YjX2rv6VU6WCTpFagihvwDJQWdCRV557sNSexktvmxSZu1jBXWogQshdTLdBd8sAtWZgUQSqZZACoRfg2tr8cMaKqgYHP6Fj2FJo7Zt5YyH7b3xTLA2ZAxNEqDgcnUdt3ZRoU5T9edsM2Y9KCktRAdJEFQZVYVddw4jdFpFKaZ4cRv6JprtSYWUazmrifJ3EqzvyQZYZgEuSshZ6jeAG4vP1w5oFPBQJyKsbPvB83buNgoyrJxDUxWFujAjwkW3s4c7MUxqAZpFHDFoEsKKQC2iLVMyL3dYnvB3t7k8rztUzJyHZtZzzYbkSSEkPLtcQRGr3VNVEitf9PuAiG25UdC2Zw4GUN1cDyumGVQpY5x1e6MxbixVn1gr7h3Qbxmrc1TxSu"
  }
}
```

#### initiator <--- (2018-10-24 13:00:17.686)
```javascript
{
  "action": "update",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkmr6YjX2rv6VU6WCTpFagihvwDJQWdCRV557sNSexktvmxSZu1jBXWogQshdTLdBd8sAtWZgUQSqZZACoRfg2tr8cMaKqgYHP6Fj2FJo7Zt5YyH7b3xTLA2ZAxNEqDgcnUdt3ZRoU5T9edsM2Y9KCktRAdJEFQZVYVddw4jdFpFKaZ4cRv6JprtSYWUazmrifJ3EqzvyQZYZgEuSshZ6jeAG4vP1w5oFPBQJyKsbPvB83buNgoyrJxDUxWFujAjwkW3s4c7MUxqAZpFHDFoEsKKQC2iLVMyL3dYnvB3t7k8rztUzJyHZtZzzYbkSSEkPLtcQRGr3VNVEitf9PuAiG25UdC2Zw4GUN1cDyumGVQpY5x1e6MxbixVn1gr7h3Qbxmrc1TxSu"
  }
}
```

#### initiator ---> (2018-10-24 13:00:17.690)
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

#### initiator <--- (2018-10-24 13:00:17.691)
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

#### initiator ---> (2018-10-24 13:00:17.691)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- (2018-10-24 13:00:17.692)
```javascript
{
  "action": "get",
  "payload": [
    {
      "account": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "balance": 401
    },
    {
      "account": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
      "balance": 699
    }
  ],
  "tag": "balances"
}
```

#### responder ---> (2018-10-24 13:00:17.693)
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

#### responder <--- (2018-10-24 13:00:17.697)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQMzFQwpi7ENiuTxdkZdKFAnqnLkBSMZdcLq5bJgJMFhMs9FYvuAWacsUPirHfBkFnhyeL17sxHmrbjpCJEpuJajQ2LxmKnWNw2Dcr5ScEpTkCpSXZwgbNchHoSrLHbbKWZ1PmPpApBcwdGQooTcSd7o4zwmukezku7qfWpc2wfT6NHBdC7VEEfmr6PcUHPkBm51psFE9dq9zC"
  },
  "tag": "update"
}
```

#### responder ---> (2018-10-24 13:00:17.698)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_LHMmG11Rak55KESMm8R9z9FMYEE9siUyCxL6DW2nRs9kGT83K3tM4b1BDtkkyA5A26WizD7npsGDkxXVEJCyXK5AW3tGEs3HhZuxe5C7toiMbsvJBKQWzAxaCypFmv14f7XYXRbr7ArtKHk4MRh4Cq7gNcz9XnqT97ET7vCnXinwmefueNh7dkW4KaJar94Ti1sVJwuS4AKzVwJMwP51wrRhVBPNBUBqyn2iS9DxfCnUgGg1puUqxhTheGnxqfn72bc1C5fHHWPE1nhQUoA3JfwGJsYpxswxKUHTJAxLiujQeGHNJfroYUGxz"
  }
}
```

#### initiator <--- (2018-10-24 13:00:17.727)
```javascript
{
  "action": "info",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "event": "update"
  }
}
```

#### initiator <--- (2018-10-24 13:00:17.728)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_GB8bJXCQMzFQwpi7ENiuTxdkZdKFAnqnLkBSMZdcLq5bJgJMFhMs9FYvuAWacsUPirHfBkFnhyeL17sxHmrbjpCJEpuJajQ2LxmKnWNw2Dcr5ScEpTkCpSXZwgbNchHoSrLHbbKWZ1PmPpApBcwdGQooTcSd7o4zwmukezku7qfWpc2wfT6NHBdC7VEEfmr6PcUHPkBm51psFE9dq9zC"
  },
  "tag": "update_ack"
}
```

#### initiator ---> (2018-10-24 13:00:17.729)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_LHMmG11Rak4yYyL41oxM8JoVq46AgHm9T7nBKyU5yXnukoj3FS2NBcK3YgcwL19t26ZNRBeKSBN5nzThsWRv2cedCkqE9zpzBSPkyEYHjevV3fUbR5fzR7FnXVWM1UEgLFWwUQ2fQSqoEA8Bb2LoAAV36RJLTSkqxw4GMQZ1J7sYAMfGdauawEyo3GrUyh6ao4tXrF8zqJDPxKMucvXw21NPrp87KH2gkwbaGSSNK5Ed3hYPj3C3BtpcoSL4fv1wTWhw1vnQRFFcBwGnyYLjbGqCR9yDpVBuKah8oQM9vCLuhWXbP7L9C8Zfq"
  }
}
```

#### initiator <--- (2018-10-24 13:00:17.734)
```javascript
{
  "action": "update",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkhnTTGuFUBhXkyZ29m7v6aqEsvhuzVM8QHVVLZbYDGeA5bwKxEyjQPaPwErveRrxe9x23mms5cE9E1ZhgPtPuEMsneQV3RLhDcjXAfX6hndyxRUSuL6MbboWLeXmUaGcJccSomNAqe5bpCD46dcuuRZTuMyEWFj8d16R2TtZCZdZswdKyvzVztscGrkdTsAS8LVdnNYJqjvfNTHkmnhBPfchs8yAuXhLaLNsmNEdoKhnYBjAmaQ7DfJTyesR35sY5wuhKaRFhaqMbqqkHrkw3cgb8QS3jzp2kJcAzomAHq62aXNq38qJwAZE2xrhq2FYszhJeDtytRCyqWV7ZT1mqMDiJZhtS6bb8Ydtud4h79P7qbDYyyitoMTzRTNJgupqJ1CXny66s"
  }
}
```

#### responder <--- (2018-10-24 13:00:17.734)
```javascript
{
  "action": "update",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "state": "tx_3XPhV5wAjiGDkhnTTGuFUBhXkyZ29m7v6aqEsvhuzVM8QHVVLZbYDGeA5bwKxEyjQPaPwErveRrxe9x23mms5cE9E1ZhgPtPuEMsneQV3RLhDcjXAfX6hndyxRUSuL6MbboWLeXmUaGcJccSomNAqe5bpCD46dcuuRZTuMyEWFj8d16R2TtZCZdZswdKyvzVztscGrkdTsAS8LVdnNYJqjvfNTHkmnhBPfchs8yAuXhLaLNsmNEdoKhnYBjAmaQ7DfJTyesR35sY5wuhKaRFhaqMbqqkHrkw3cgb8QS3jzp2kJcAzomAHq62aXNq38qJwAZE2xrhq2FYszhJeDtytRCyqWV7ZT1mqMDiJZhtS6bb8Ydtud4h79P7qbDYyyitoMTzRTNJgupqJ1CXny66s"
  }
}
```

#### initiator ---> (2018-10-24 13:00:17.738)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- (2018-10-24 13:00:17.739)
```javascript
{
  "action": "get",
  "payload": [
    {
      "account": "ak_2eQtrZPEwNDSwM11SidcwEMnj6FUhd9tYdaRC4CrPTupjhaCkt",
      "balance": 400
    },
    {
      "account": "ak_2F4DR4wbwEekWumqZjFpQyDRha7ttoMYw9TvYHmdKaE8BLaiVL",
      "balance": 700
    }
  ],
  "tag": "balances"
}
```

#### initiator ---> (2018-10-24 13:00:17.834)
```javascript
{
  "action": "shutdown"
}
```

#### initiator <--- (2018-10-24 13:00:17.841)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_2M9ipLgcZ23ZzBqDKRTav3PSchGZCY4EQCkHF7RFtaVJQLNLwo6uqs36sQFrhcrUiZvMbwYS5XVtDb3mzEEMhv8WKYnt7HG8idWU9bfEEFmAFNK1RtftX"
  },
  "tag": "shutdown_sign"
}
```

#### initiator ---> (2018-10-24 13:00:17.842)
```javascript
{
  "action": "shutdown_sign",
  "payload": {
    "tx": "tx_2iJcVi27J8ZzdH5oDs9XR6AQyYHuVLnFzC9oFcougm6GtmMRvCeLcFX3QFewm7t6j1AZTQAztsFDEoXdq7PBwQBAAK3XnYDmrzEUnwAdCaV6cSHTecMNT2qP8FaTkXxBmfzuccZPrnByZy3G71aZxfBxq9uix8dTar6xKWsGgF3GYhj9vtx4CZmRxpb1aPt4f1sBs9PE5CWRqcs72JCVdmiw9t"
  }
}
```

#### responder <--- (2018-10-24 13:00:17.845)
```javascript
{
  "action": "sign",
  "payload": {
    "tx": "tx_2M9ipLgcZ23ZzBqDKRTav3PSchGZCY4EQCkHF7RFtaVJQLNLwo6uqs36sQFrhcrUiZvMbwYS5XVtDb3mzEEMhv8WKYnt7HG8idWU9bfEEFmAFNK1RtftX"
  },
  "tag": "shutdown_sign_ack"
}
```

#### responder ---> (2018-10-24 13:00:17.846)
```javascript
{
  "action": "shutdown_sign_ack",
  "payload": {
    "tx": "tx_2iJcVi27J8ZzPBEhqkiENXyhbfJFJGdPVTXbuA8r4GeVLaVAa8FUDqCW4A1DMnVPHos1YrCw1niMscKwiVmiexZLBdDZ1gxQbEhmfLyZJ91AfwyX3M4o2m2r5YrAcPSyrBYNKyhJTyvcuNDPh9d2zY7RLpUbMSghs6joonuLdUzSrD8D8JApY5gHWER94reonRWU8B9hqTX89LcXB1EjQrUR9a"
  }
}
```

#### responder <--- (2018-10-24 13:00:17.851)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "tx": "tx_3wu1WL1txa1Yvh7bNNW6bCRpneRvToUdqy9KU81d2usQc7LcxHG6AgQcAjVNB15F41R4UKGjyefiwAfdu8TqWuAwAmQASTFKtudVbk1AeXPRd7x3ihJDxDrUtwg6FmNjVA7k8G1xZTtEXp7LU8uXDtTGSzqpCN91bZ3Wf5YjrXMnnkvZDB7pKmpX44meCN1LqLiPCbXVvKBLgqpfeZJ2n6GhuXy4x7fxyLLBciowYKd6ASTbrHLiiDL2giCWMsDSiiV4CVVXquubFc61CWaBMMaawEjTr76PJa7YMtLtzDuRJdHLdeUH"
  }
}
```

#### responder <--- (2018-10-24 13:00:17.851)
```javascript
{
  "action": "info",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "event": "close_mutual"
  }
}
```

#### responder <--- (2018-10-24 13:00:17.852)
```javascript
{
  "action": "info",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "event": "died"
  }
}
```

#### initiator <--- (2018-10-24 13:00:17.863)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "tx": "tx_3wu1WL1txa1Yvh7bNNW6bCRpneRvToUdqy9KU81d2usQc7LcxHG6AgQcAjVNB15F41R4UKGjyefiwAfdu8TqWuAwAmQASTFKtudVbk1AeXPRd7x3ihJDxDrUtwg6FmNjVA7k8G1xZTtEXp7LU8uXDtTGSzqpCN91bZ3Wf5YjrXMnnkvZDB7pKmpX44meCN1LqLiPCbXVvKBLgqpfeZJ2n6GhuXy4x7fxyLLBciowYKd6ASTbrHLiiDL2giCWMsDSiiV4CVVXquubFc61CWaBMMaawEjTr76PJa7YMtLtzDuRJdHLdeUH"
  }
}
```

#### initiator <--- (2018-10-24 13:00:17.864)
```javascript
{
  "action": "info",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "event": "close_mutual"
  }
}
```

#### initiator <--- (2018-10-24 13:00:17.864)
```javascript
{
  "action": "info",
  "channel_id": "ch_CookqWXm9FRCdh2qxRwj9xC19sBx5MUPrxCJSmxk4Hwi5MDtf",
  "payload": {
    "event": "died"
  }
}
```
