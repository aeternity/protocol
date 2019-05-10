
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm&lock_period=10&minimum_depth=4&port=12340&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC&role=initiator
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm&lock_period=10&minimum_depth=4&port=12340&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC&role=responder
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": null,
  "payload": {
    "event": "channel_open"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": null,
  "payload": {
    "event": "channel_accept"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": null,
  "payload": {
    "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwIjpDEM",
    "updates": []
  },
  "tag": "initiator_sign",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "initiator_sign",
  "payload": {
    "tx": "tx_+MsLAfhCuEBBhXnR9cHZ+y9mHju9v6zO9r6+oKgmO057kytIvdeN0fLlvLmwmafeFNK/LMHBS6bhdfGiI4d+BjLR5PwcGToEuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/AgzxyIM="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": null,
  "payload": {
    "event": "funding_created"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": null,
  "payload": {
    "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwIjpDEM",
    "updates": []
  },
  "tag": "responder_sign",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "responder_sign",
  "payload": {
    "tx": "tx_+MsLAfhCuEBZlcQttiqL236aG7gtGcPAw+h7Cpz4FcNFI7xgqa2MTgvq5Dp53DeVM2gbl1ME8f/n5JVsv57pFnQVzpWEQagLuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/AtWmo4E="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": null,
  "payload": {
    "tx": "tx_+QENCwH4hLhAQYV50fXB2fsvZh47vb+szva+vqCoJjtOe5MrSL3XjdHy5by5sJmn3hTSvyzBwUum4XXxoiOHfgYy0eT8HBk6BLhAWZXELbYqi9t+mhu4LRnDwMPoewqc+BXDRSO8YKmtjE4L6uQ6edw3lTNoG5dTBPH/5+SVbL+e6RZ0Fc6VhEGoC7iD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwKi7c1T"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": null,
  "payload": {
    "event": "funding_signed"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": null,
  "payload": {
    "tx": "tx_+QENCwH4hLhAQYV50fXB2fsvZh47vb+szva+vqCoJjtOe5MrSL3XjdHy5by5sJmn3hTSvyzBwUum4XXxoiOHfgYy0eT8HBk6BLhAWZXELbYqi9t+mhu4LRnDwMPoewqc+BXDRSO8YKmtjE4L6uQ6edw3lTNoG5dTBPH/5+SVbL+e6RZ0Fc6VhEGoC7iD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwKi7c1T"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": null,
  "payload": [
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 69999999999999
    },
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000001
    }
  ],
  "tag": "balances",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": null,
  "payload": {
    "event": "own_funding_locked"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": null,
  "payload": {
    "event": "own_funding_locked"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "event": "funding_locked"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "event": "funding_locked"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "event": "open"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "event": "open"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "state": "tx_+QENCwH4hLhAQYV50fXB2fsvZh47vb+szva+vqCoJjtOe5MrSL3XjdHy5by5sJmn3hTSvyzBwUum4XXxoiOHfgYy0eT8HBk6BLhAWZXELbYqi9t+mhu4LRnDwMPoewqc+BXDRSO8YKmtjE4L6uQ6edw3lTNoG5dTBPH/5+SVbL+e6RZ0Fc6VhEGoC7iD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwKi7c1T"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "state": "tx_+QENCwH4hLhAQYV50fXB2fsvZh47vb+szva+vqCoJjtOe5MrSL3XjdHy5by5sJmn3hTSvyzBwUum4XXxoiOHfgYy0eT8HBk6BLhAWZXELbYqi9t+mhu4LRnDwMPoewqc+BXDRSO8YKmtjE4L6uQ6edw3lTNoG5dTBPH/5+SVbL+e6RZ0Fc6VhEGoC7iD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwKi7c1T"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": [
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 69999999999999
    },
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000001
    }
  ],
  "tag": "balances",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "amount": "1",
    "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
  },
  "tag": "new"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "reason": "not_a_number",
    "request": {
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "amount": 1,
    "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
  },
  "tag": "new"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "tx": "tx_+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4T7EieA=",
    "updates": [
      {
        "amount": 1,
        "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "op": "OffChainTransfer",
        "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
      }
    ]
  },
  "tag": "update",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEBf8F9gCvEzEQEjiq4T9UCwXucslE7mZY3ZL2n1KKL5NmkFulQRNpmmFopKJQpdig1dsDwEDck+q89S19PZrXUDuJf4lTkBoQY/KKbrcmIHVGiACvxWdOMPb8t4vp8YuHJJaGqCvt7teAL4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoNUqd4GTOFacRsLar0VqTNSHraQXvmyQrL/MBqX090LhdL3QBw=="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "event": "update"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "tx": "tx_+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4T7EieA=",
    "updates": [
      {
        "amount": 1,
        "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "op": "OffChainTransfer",
        "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+N8LAfhCuEAfdKJm4kij9EnghEolSbYMlA4uS7Umrtgei9/C2MRj2726kkHJNxqpOGo8GE39gtszUeSzkxYCdhxFYWPEDbALuJf4lTkBoQY/KKbrcmIHVGiACvxWdOMPb8t4vp8YuHJJaGqCvt7teAL4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoNUqd4GTOFacRsLar0VqTNSHraQXvmyQrL/MBqX090LhJRKkZQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "state": "tx_+QEhCwH4hLhAH3SiZuJIo/RJ4IRKJUm2DJQOLku1Jq7YHovfwtjEY9u9upJByTcaqThqPBhN/YLbM1Hks5MWAnYcRWFjxA2wC7hAX/BfYArxMxEBI4quE/VAsF7nLJRO5mWN2S9p9Sii+TZpBbpUETaZphaKSiUKXYoNXbA8BA3JPqvPUtfT2a11A7iX+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4VvHlKw="
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "state": "tx_+QEhCwH4hLhAH3SiZuJIo/RJ4IRKJUm2DJQOLku1Jq7YHovfwtjEY9u9upJByTcaqThqPBhN/YLbM1Hks5MWAnYcRWFjxA2wC7hAX/BfYArxMxEBI4quE/VAsF7nLJRO5mWN2S9p9Sii+TZpBbpUETaZphaKSiUKXYoNXbA8BA3JPqvPUtfT2a11A7iX+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4VvHlKw="
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": [
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 69999999999998
    },
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000002
    }
  ],
  "tag": "balances",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "a": "a"
  },
  "tag": "offchain_state"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAH3SiZuJIo/RJ4IRKJUm2DJQOLku1Jq7YHovfwtjEY9u9upJByTcaqThqPBhN/YLbM1Hks5MWAnYcRWFjxA2wC7hAX/BfYArxMxEBI4quE/VAsF7nLJRO5mWN2S9p9Sii+TZpBbpUETaZphaKSiUKXYoNXbA8BA3JPqvPUtfT2a11A7iX+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4VvHlKw=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJf/rDvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAJXk16b"
  },
  "tag": "offchain_state",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": [
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000002
    },
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 69999999999998
    }
  ],
  "tag": "balances",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "amount": "1",
    "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
  },
  "tag": "new"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "reason": "not_a_number",
    "request": {
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "amount": 1,
    "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
  },
  "tag": "new"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "tx": "tx_+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgD+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv3g28go=",
    "updates": [
      {
        "amount": 1,
        "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "op": "OffChainTransfer",
        "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
      }
    ]
  },
  "tag": "update",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuECWwq5DdvBwqnKONjwmCzkbVZCSfKEmtAFqOgF5lF33Wj1/+yow3ESPQ5h8PIivhukfqSlgzfGQXcwfksxRuREOuJf4lTkBoQY/KKbrcmIHVGiACvxWdOMPb8t4vp8YuHJJaGqCvt7teAP4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/hfp2PA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "event": "update"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "tx": "tx_+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgD+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv3g28go=",
    "updates": [
      {
        "amount": 1,
        "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "op": "OffChainTransfer",
        "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+N8LAfhCuEAdWJnIMovl43U5ITN62EyNCscJUSd+8NVHJ7AzxZxWpZmQG6/acVZNJj0YRYJ8CBlbaUnQ8jK70TldlqvKj6kEuJf4lTkBoQY/KKbrcmIHVGiACvxWdOMPb8t4vp8YuHJJaGqCvt7teAP4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/+1qDrw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "state": "tx_+QEhCwH4hLhAHViZyDKL5eN1OSEzethMjQrHCVEnfvDVRyewM8WcVqWZkBuv2nFWTSY9GEWCfAgZW2lJ0PIyu9E5XZaryo+pBLhAlsKuQ3bwcKpyjjY8Jgs5G1WQknyhJrQBajoBeZRd91o9f/sqMNxEj0OYfDyIr4bpH6kpYM3xkF3MH5LMUbkRDriX+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgD+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv9MXO9k="
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "state": "tx_+QEhCwH4hLhAHViZyDKL5eN1OSEzethMjQrHCVEnfvDVRyewM8WcVqWZkBuv2nFWTSY9GEWCfAgZW2lJ0PIyu9E5XZaryo+pBLhAlsKuQ3bwcKpyjjY8Jgs5G1WQknyhJrQBajoBeZRd91o9f/sqMNxEj0OYfDyIr4bpH6kpYM3xkF3MH5LMUbkRDriX+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgD+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv9MXO9k="
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": [
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000001
    },
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 69999999999999
    }
  ],
  "tag": "balances",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "a": "a"
  },
  "tag": "offchain_state"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAHViZyDKL5eN1OSEzethMjQrHCVEnfvDVRyewM8WcVqWZkBuv2nFWTSY9GEWCfAgZW2lJ0PIyu9E5XZaryo+pBLhAlsKuQ3bwcKpyjjY8Jgs5G1WQknyhJrQBajoBeZRd91o9f/sqMNxEj0OYfDyIr4bpH6kpYM3xkF3MH5LMUbkRDriX+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgD+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv9MXO9k=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJf/7DvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAFkGvNa"
  },
  "tag": "offchain_state",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": [
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000001
    },
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 69999999999999
    }
  ],
  "tag": "balances",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "amount": "1",
    "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
  },
  "tag": "new"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "reason": "not_a_number",
    "request": {
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "amount": 1,
    "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
  },
  "tag": "new"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "tx": "tx_+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsRndBEA=",
    "updates": [
      {
        "amount": 1,
        "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "op": "OffChainTransfer",
        "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
      }
    ]
  },
  "tag": "update",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEBsbyplVr/tR84IbVbueHRbbmdqC78xPbBQ9Ril3Z8am36sFKg3p1343e3UkJKhhQz1vzjhJaqKs6NzxYaF5nsCuJf4lTkBoQY/KKbrcmIHVGiACvxWdOMPb8t4vp8YuHJJaGqCvt7teAT4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROxvn8FWQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "event": "update"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "tx": "tx_+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsRndBEA=",
    "updates": [
      {
        "amount": 1,
        "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "op": "OffChainTransfer",
        "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+N8LAfhCuEAb3L3cA4IBGfWadJvPCf780caQ+FQKdhYszzGUO/GgsPQhXUOBstWu2a66LCHjY2JnXYeEGiQWIsflsHFeM0QNuJf4lTkBoQY/KKbrcmIHVGiACvxWdOMPb8t4vp8YuHJJaGqCvt7teAT4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROxCArh2g=="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "state": "tx_+QEhCwH4hLhAG9y93AOCARn1mnSbzwn+/NHGkPhUCnYWLM8xlDvxoLD0IV1DgbLVrtmuuiwh42NiZ12HhBokFiLH5bBxXjNEDbhAbG8qZVa/7UfOCG1W7nh0W25nagu/MT2wUPUYpd2fGpt+rBSoN6dd+N3t1JCSoYUM9b844SWqirOjc8WGheZ7AriX+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90Tsc6YD24="
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "state": "tx_+QEhCwH4hLhAG9y93AOCARn1mnSbzwn+/NHGkPhUCnYWLM8xlDvxoLD0IV1DgbLVrtmuuiwh42NiZ12HhBokFiLH5bBxXjNEDbhAbG8qZVa/7UfOCG1W7nh0W25nagu/MT2wUPUYpd2fGpt+rBSoN6dd+N3t1JCSoYUM9b844SWqirOjc8WGheZ7AriX+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90Tsc6YD24="
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": [
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000000
    },
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 70000000000000
    }
  ],
  "tag": "balances",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "a": "a"
  },
  "tag": "offchain_state"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAG9y93AOCARn1mnSbzwn+/NHGkPhUCnYWLM8xlDvxoLD0IV1DgbLVrtmuuiwh42NiZ12HhBokFiLH5bBxXjNEDbhAbG8qZVa/7UfOCG1W7nh0W25nagu/MT2wUPUYpd2fGpt+rBSoN6dd+N3t1JCSoYUM9b844SWqirOjc8WGheZ7AriX+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90Tsc6YD24=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJgALDvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAA6duKo"
  },
  "tag": "offchain_state",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": [
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 70000000000000
    },
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000000
    }
  ],
  "tag": "balances",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "amount": "1",
    "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
  },
  "tag": "new"
}
```

#### initiator <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "reason": "not_a_number",
    "request": {
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "amount": 1,
    "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
  },
  "tag": "new"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "tx": "tx_+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvyIut1E=",
    "updates": [
      {
        "amount": 1,
        "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "op": "OffChainTransfer",
        "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
      }
    ]
  },
  "tag": "update",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEAmeulPPrHTLSyoKQW85KPLD/IzxylB4CdZ+RjnPATwH4r0P+6kUuXUNZmijhRCu+dGUoS3El4nivtbFAfaCBsHuJf4lTkBoQY/KKbrcmIHVGiACvxWdOMPb8t4vp8YuHJJaGqCvt7teAX4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/NGA1jg=="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "event": "update"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "tx": "tx_+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvyIut1E=",
    "updates": [
      {
        "amount": 1,
        "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "op": "OffChainTransfer",
        "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+N8LAfhCuEA3Yc1H5kaRs4OkP20GT03LGhSvpcPUwpH4NcDIt2QHXXVsPBK4wUJdfByw1WMY0w0hhoia0lwQ0p0GXur79TQLuJf4lTkBoQY/KKbrcmIHVGiACvxWdOMPb8t4vp8YuHJJaGqCvt7teAX4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/tfIsig=="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "state": "tx_+QEhCwH4hLhAJnrpTz6x0y0sqCkFvOSjyw/yM8cpQeAnWfkY5zwE8B+K9D/upFLl1DWZoo4UQrvnRlKEtxJeJ4r7WxQH2ggbB7hAN2HNR+ZGkbODpD9tBk9NyxoUr6XD1MKR+DXAyLdkB111bDwSuMFCXXwcsNVjGNMNIYaImtJcENKdBl7q+/U0C7iX+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv+MnKP8="
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "state": "tx_+QEhCwH4hLhAJnrpTz6x0y0sqCkFvOSjyw/yM8cpQeAnWfkY5zwE8B+K9D/upFLl1DWZoo4UQrvnRlKEtxJeJ4r7WxQH2ggbB7hAN2HNR+ZGkbODpD9tBk9NyxoUr6XD1MKR+DXAyLdkB111bDwSuMFCXXwcsNVjGNMNIYaImtJcENKdBl7q+/U0C7iX+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv+MnKP8="
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": [
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 69999999999999
    },
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000001
    }
  ],
  "tag": "balances",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "a": "a"
  },
  "tag": "offchain_state"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAJnrpTz6x0y0sqCkFvOSjyw/yM8cpQeAnWfkY5zwE8B+K9D/upFLl1DWZoo4UQrvnRlKEtxJeJ4r7WxQH2ggbB7hAN2HNR+ZGkbODpD9tBk9NyxoUr6XD1MKR+DXAyLdkB111bDwSuMFCXXwcsNVjGNMNIYaImtJcENKdBl7q+/U0C7iX+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv+MnKP8=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJf/7DvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAFkGvNa"
  },
  "tag": "offchain_state",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": [
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000001
    },
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 69999999999999
    }
  ],
  "tag": "balances",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "amount": "1",
    "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
  },
  "tag": "new"
}
```

#### responder <--- node
```javascript
{
  "action": "error",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "reason": "not_a_number",
    "request": {
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "amount": 1,
    "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
  },
  "tag": "new"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "tx": "tx_+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsVAwDkI=",
    "updates": [
      {
        "amount": 1,
        "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "op": "OffChainTransfer",
        "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
      }
    ]
  },
  "tag": "update",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuECDkydoqlBaTWkMnZi+s/fSpOCpbBhAZvCHhnAUalGGUusOs4bqRcs9B82AmZa3FRFVt/UdToolIMbtdqWIzk4KuJf4lTkBoQY/KKbrcmIHVGiACvxWdOMPb8t4vp8YuHJJaGqCvt7teAb4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROx2Px/cQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "event": "update"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "tx": "tx_+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsVAwDkI=",
    "updates": [
      {
        "amount": 1,
        "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "op": "OffChainTransfer",
        "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
      }
    ]
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+N8LAfhCuEDl6n/8QlXskouu5mWDPGgcnuZQlRBmZHPwtDTOV1iAwkvUuebYgX6OzwpgDej0sl4ANKzLgO3h+Hqv+gbKM+MJuJf4lTkBoQY/KKbrcmIHVGiACvxWdOMPb8t4vp8YuHJJaGqCvt7teAb4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROx5QCKGg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "state": "tx_+QEhCwH4hLhAg5MnaKpQWk1pDJ2YvrP30qTgqWwYQGbwh4ZwFGpRhlLrDrOG6kXLPQfNgJmWtxURVbf1HU6KJSDG7XaliM5OCrhA5ep//EJV7JKLruZlgzxoHJ7mUJUQZmRz8LQ0zldYgMJL1Lnm2IF+js8KYA3o9LJeADSsy4Dt4fh6r/oGyjPjCbiX+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90Tsbm+UPQ="
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "state": "tx_+QEhCwH4hLhAg5MnaKpQWk1pDJ2YvrP30qTgqWwYQGbwh4ZwFGpRhlLrDrOG6kXLPQfNgJmWtxURVbf1HU6KJSDG7XaliM5OCrhA5ep//EJV7JKLruZlgzxoHJ7mUJUQZmRz8LQ0zldYgMJL1Lnm2IF+js8KYA3o9LJeADSsy4Dt4fh6r/oGyjPjCbiX+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90Tsbm+UPQ="
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": [
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000000
    },
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 70000000000000
    }
  ],
  "tag": "balances",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "get",
  "payload": {
    "a": "a"
  },
  "tag": "offchain_state"
}
```

#### initiator <--- node
```javascript
{
  "action": "get",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAg5MnaKpQWk1pDJ2YvrP30qTgqWwYQGbwh4ZwFGpRhlLrDrOG6kXLPQfNgJmWtxURVbf1HU6KJSDG7XaliM5OCrhA5ep//EJV7JKLruZlgzxoHJ7mUJUQZmRz8LQ0zldYgMJL1Lnm2IF+js8KYA3o9LJeADSsy4Dt4fh6r/oGyjPjCbiX+JU5AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XgG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90Tsbm+UPQ=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJgALDvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAA6duKo"
  },
  "tag": "offchain_state",
  "version": 1
}
```
