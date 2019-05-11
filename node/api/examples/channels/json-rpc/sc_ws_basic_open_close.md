
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC&role=initiator
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC&role=responder
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_open"
    }
  },
  "version": 1
}
```

#### responder info
> Received an WebSocket opening request

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_accept"
    }
  },
  "version": 1
}
```

#### initiator info
> Received an WebSocket connection accepted

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwN8SjX6",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_+MsLAfhCuEBKcaEsD44NQBne0ogwN9kp0R2SE7+5gq4YcUebdB08ZJQx4ZyOKNxoi6kd5SvJIR7bQJl7qCjKEO83+gdVfhEBuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/A0hqzio="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "funding_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwN8SjX6",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_+MsLAfhCuEBl75m7gWWmkiboeETwsC06U1GGolZEXN+G1HWFGdEo5OXsq2JJ1wGZFnzpyYlgKfUzXbG86eENUwuHuFV69HUGuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/Aw77dP0="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+QENCwH4hLhASnGhLA+ODUAZ3tKIMDfZKdEdkhO/uYKuGHFHm3QdPGSUMeGcjijcaIupHeUrySEe20CZe6goyhDvN/oHVX4RAbhAZe+Zu4FlppIm6HhE8LAtOlNRhqJWRFzfhtR1hRnRKOTl7KtiSdcBmRZ86cmJYCn1M12xvOnhDVMLh7hVevR1BriD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwML9I89"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "funding_signed"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+QENCwH4hLhASnGhLA+ODUAZ3tKIMDfZKdEdkhO/uYKuGHFHm3QdPGSUMeGcjijcaIupHeUrySEe20CZe6goyhDvN/oHVX4RAbhAZe+Zu4FlppIm6HhE8LAtOlNRhqJWRFzfhtR1hRnRKOTl7KtiSdcBmRZ86cmJYCn1M12xvOnhDVMLh7hVevR1BriD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwML9I89"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423472,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423472,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 69999999999999
    },
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Channel is `open` and ready to use

#### responder info
> Channel is `open` and ready to use

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "state": "tx_+QENCwH4hLhASnGhLA+ODUAZ3tKIMDfZKdEdkhO/uYKuGHFHm3QdPGSUMeGcjijcaIupHeUrySEe20CZe6goyhDvN/oHVX4RAbhAZe+Zu4FlppIm6HhE8LAtOlNRhqJWRFzfhtR1hRnRKOTl7KtiSdcBmRZ86cmJYCn1M12xvOnhDVMLh7hVevR1BriD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwML9I89"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "state": "tx_+QENCwH4hLhASnGhLA+ODUAZ3tKIMDfZKdEdkhO/uYKuGHFHm3QdPGSUMeGcjijcaIupHeUrySEe20CZe6goyhDvN/oHVX4RAbhAZe+Zu4FlppIm6HhE8LAtOlNRhqJWRFzfhtR1hRnRKOTl7KtiSdcBmRZ86cmJYCn1M12xvOnhDVMLh7hVevR1BriD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwML9I89"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423471,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
  "id": -576460752303423471,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 69999999999999
    },
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "tx": "tx_+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4Zxbb8Q=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
          "op": "OffChainTransfer",
          "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuEAFOva8xKyh9tzeIps9Tum89u4xTvbT0yokbLnu78KnIK6wZRZiYlwrBujUEQg0t3Tud9BXDn5oKwnkdJizmA0GuJf4lTkBoQasBNkKrZJu+gk87ymFQsCsenQzLt8Fb1JKm0n7nKzTYgL4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoNUqd4GTOFacRsLar0VqTNSHraQXvmyQrL/MBqX090Lh+pkf9A=="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "tx": "tx_+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4Zxbb8Q=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
          "op": "OffChainTransfer",
          "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+N8LAfhCuEAGx0qykrlj5/DVq6RJ2AsMe6uiCL4TX8Emv1sC3TL2IdDp9S3jrzRQnIe6gWtM/9kR++JRGwVL+gs+O7SjCKYIuJf4lTkBoQasBNkKrZJu+gk87ymFQsCsenQzLt8Fb1JKm0n7nKzTYgL4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoNUqd4GTOFacRsLar0VqTNSHraQXvmyQrL/MBqX090LhNHGU2A=="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "state": "tx_+QEhCwH4hLhABTr2vMSsofbc3iKbPU7pvPbuMU7209MqJGy57u/CpyCusGUWYmJcKwbo1BEINLd07nfQVw5+aCsJ5HSYs5gNBrhABsdKspK5Y+fw1aukSdgLDHurogi+E1/BJr9bAt0y9iHQ6fUt4680UJyHuoFrTP/ZEfviURsFS/oLPju0owimCLiX+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4ffJBsU="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "state": "tx_+QEhCwH4hLhABTr2vMSsofbc3iKbPU7pvPbuMU7209MqJGy57u/CpyCusGUWYmJcKwbo1BEINLd07nfQVw5+aCsJ5HSYs5gNBrhABsdKspK5Y+fw1aukSdgLDHurogi+E1/BJr9bAt0y9iHQ6fUt4680UJyHuoFrTP/ZEfviURsFS/oLPju0owimCLiX+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4ffJBsU="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423470,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
  "id": -576460752303423470,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 69999999999998
    },
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423469,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
  "id": -576460752303423469,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhABTr2vMSsofbc3iKbPU7pvPbuMU7209MqJGy57u/CpyCusGUWYmJcKwbo1BEINLd07nfQVw5+aCsJ5HSYs5gNBrhABsdKspK5Y+fw1aukSdgLDHurogi+E1/BJr9bAt0y9iHQ6fUt4680UJyHuoFrTP/ZEfviURsFS/oLPju0owimCLiX+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4ffJBsU=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJf/rDvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAJXk16b"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423468,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
  "id": -576460752303423468,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000002
    },
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 69999999999998
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "tx": "tx_+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02ID+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvx4JYow=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
          "op": "OffChainTransfer",
          "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuEB8tXLGpWcG1je+iHmCMHGsEn5C/gZ4zmDkPHNnCNqPMIGqB9rpS/O0dappWSybXFecF1dnRBsB9kSwG83sakcGuJf4lTkBoQasBNkKrZJu+gk87ymFQsCsenQzLt8Fb1JKm0n7nKzTYgP4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/EvKVYg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "tx": "tx_+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02ID+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvx4JYow=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
          "op": "OffChainTransfer",
          "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+N8LAfhCuEBc4t4CVhbGwJpSzqBA0mfL7zis8m1VcdLThiVFdeOExMKEgv39yMfUmVwtafcuFZfUIMqTNqo/fV+wWedJaqcFuJf4lTkBoQasBNkKrZJu+gk87ymFQsCsenQzLt8Fb1JKm0n7nKzTYgP4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/sKnS6g=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "state": "tx_+QEhCwH4hLhAXOLeAlYWxsCaUs6gQNJny+84rPJtVXHS04YlRXXjhMTChIL9/cjH1JlcLWn3LhWX1CDKkzaqP31fsFnnSWqnBbhAfLVyxqVnBtY3voh5gjBxrBJ+Qv4GeM5g5DxzZwjajzCBqgfa6UvztHWqaVksm1xXnBdXZ0QbAfZEsBvN7GpHBriX+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02ID+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvyq7Hd4="
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "state": "tx_+QEhCwH4hLhAXOLeAlYWxsCaUs6gQNJny+84rPJtVXHS04YlRXXjhMTChIL9/cjH1JlcLWn3LhWX1CDKkzaqP31fsFnnSWqnBbhAfLVyxqVnBtY3voh5gjBxrBJ+Qv4GeM5g5DxzZwjajzCBqgfa6UvztHWqaVksm1xXnBdXZ0QbAfZEsBvN7GpHBriX+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02ID+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvyq7Hd4="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423467,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
  "id": -576460752303423467,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000001
    },
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423466,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
  "id": -576460752303423466,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAXOLeAlYWxsCaUs6gQNJny+84rPJtVXHS04YlRXXjhMTChIL9/cjH1JlcLWn3LhWX1CDKkzaqP31fsFnnSWqnBbhAfLVyxqVnBtY3voh5gjBxrBJ+Qv4GeM5g5DxzZwjajzCBqgfa6UvztHWqaVksm1xXnBdXZ0QbAfZEsBvN7GpHBriX+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02ID+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvyq7Hd4=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJf/7DvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAFkGvNa"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423465,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
  "id": -576460752303423465,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000001
    },
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "tx": "tx_+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90Tscj79nM=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
          "op": "OffChainTransfer",
          "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuEDebeD2Rt1PQ35GmNt32tGPx9DqYsOUoygp3RxDn/yVZR4iY6Jr96PDdJ7hPuhq+1bD9eiqvykaEzTfbDB63O4FuJf4lTkBoQasBNkKrZJu+gk87ymFQsCsenQzLt8Fb1JKm0n7nKzTYgT4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROxTkD56A=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "tx": "tx_+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90Tscj79nM=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
          "op": "OffChainTransfer",
          "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+N8LAfhCuEAVX4uqHdD4Oc5Cfrn9wVD2SOQ0s25HZgyvXABajFBOhBkXChHHmd/0wolz3Xg+3zOBOqWnT9cs/g0P3ZGmt+8PuJf4lTkBoQasBNkKrZJu+gk87ymFQsCsenQzLt8Fb1JKm0n7nKzTYgT4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROxkzPtYQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "state": "tx_+QEhCwH4hLhAFV+Lqh3Q+DnOQn65/cFQ9kjkNLNuR2YMr1wAWoxQToQZFwoRx5nf9MKJc914Pt8zgTqlp0/XLP4ND92RprfvD7hA3m3g9kbdT0N+Rpjbd9rRj8fQ6mLDlKMoKd0cQ5/8lWUeImOia/ejw3Se4T7oavtWw/Xoqr8pGhM032wwetzuBbiX+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsSCdXkg="
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "state": "tx_+QEhCwH4hLhAFV+Lqh3Q+DnOQn65/cFQ9kjkNLNuR2YMr1wAWoxQToQZFwoRx5nf9MKJc914Pt8zgTqlp0/XLP4ND92RprfvD7hA3m3g9kbdT0N+Rpjbd9rRj8fQ6mLDlKMoKd0cQ5/8lWUeImOia/ejw3Se4T7oavtWw/Xoqr8pGhM032wwetzuBbiX+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsSCdXkg="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423464,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
  "id": -576460752303423464,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000000
    },
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423463,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
  "id": -576460752303423463,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAFV+Lqh3Q+DnOQn65/cFQ9kjkNLNuR2YMr1wAWoxQToQZFwoRx5nf9MKJc914Pt8zgTqlp0/XLP4ND92RprfvD7hA3m3g9kbdT0N+Rpjbd9rRj8fQ6mLDlKMoKd0cQ5/8lWUeImOia/ejw3Se4T7oavtWw/Xoqr8pGhM032wwetzuBbiX+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsSCdXkg=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJgALDvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAA6duKo"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423462,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
  "id": -576460752303423462,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 70000000000000
    },
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "tx": "tx_+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv+EMMrg=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
          "op": "OffChainTransfer",
          "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuEAeQAaqoKsr1Sp57VhzwP8hJ0WlfVnIvBaTtStn84qcYNg88ssjkEXgwWMFXT1vUbf8Uwpp4mQIyRkrhiTehZsOuJf4lTkBoQasBNkKrZJu+gk87ymFQsCsenQzLt8Fb1JKm0n7nKzTYgX4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/H5HdGw=="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "tx": "tx_+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv+EMMrg=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
          "op": "OffChainTransfer",
          "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+N8LAfhCuEAviNVSdnlG/N4TVN9ujCKEOOgKc1qRrTdukcgGZ4qk+bev1vkZSF9xxPbR11RO1gYsfF33nNdtYOgTN8eH21YDuJf4lTkBoQasBNkKrZJu+gk87ymFQsCsenQzLt8Fb1JKm0n7nKzTYgX4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/ZhspZA=="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "state": "tx_+QEhCwH4hLhAHkAGqqCrK9Uqee1Yc8D/ISdFpX1ZyLwWk7UrZ/OKnGDYPPLLI5BF4MFjBV09b1G3/FMKaeJkCMkZK4Yk3oWbDrhAL4jVUnZ5RvzeE1TfbowihDjoCnNaka03bpHIBmeKpPm3r9b5GUhfccT20ddUTtYGLHxd95zXbWDoEzfHh9tWA7iX+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv0e2VI0="
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "state": "tx_+QEhCwH4hLhAHkAGqqCrK9Uqee1Yc8D/ISdFpX1ZyLwWk7UrZ/OKnGDYPPLLI5BF4MFjBV09b1G3/FMKaeJkCMkZK4Yk3oWbDrhAL4jVUnZ5RvzeE1TfbowihDjoCnNaka03bpHIBmeKpPm3r9b5GUhfccT20ddUTtYGLHxd95zXbWDoEzfHh9tWA7iX+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv0e2VI0="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423461,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
  "id": -576460752303423461,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 69999999999999
    },
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423460,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
  "id": -576460752303423460,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAHkAGqqCrK9Uqee1Yc8D/ISdFpX1ZyLwWk7UrZ/OKnGDYPPLLI5BF4MFjBV09b1G3/FMKaeJkCMkZK4Yk3oWbDrhAL4jVUnZ5RvzeE1TfbowihDjoCnNaka03bpHIBmeKpPm3r9b5GUhfccT20ddUTtYGLHxd95zXbWDoEzfHh9tWA7iX+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv0e2VI0=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJf/7DvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAFkGvNa"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423459,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
  "id": -576460752303423459,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000001
    },
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "tx": "tx_+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsQLcImY=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
          "op": "OffChainTransfer",
          "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuED0LiVpmFQpt3ULkIsQs1XnaVQuuG3iRMHSItBINMK++f+YmaXMpIZZkF+ec3UqwSOFRMKXwrcGrcP/Sr8UfA4GuJf4lTkBoQasBNkKrZJu+gk87ymFQsCsenQzLt8Fb1JKm0n7nKzTYgb4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROxIHuwmg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "tx": "tx_+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsQLcImY=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
          "op": "OffChainTransfer",
          "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+N8LAfhCuECwoD0GX10ywWMeorfzZ2pAUmWYGL8QcgIbqOt/fF28K8hcrETNDQ2rEiSw35d6YLdZr6EqYAkLhXLTV1nOgNYJuJf4lTkBoQasBNkKrZJu+gk87ymFQsCsenQzLt8Fb1JKm0n7nKzTYgb4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROxZZzIUQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "state": "tx_+QEhCwH4hLhAsKA9Bl9dMsFjHqK382dqQFJlmBi/EHICG6jrf3xdvCvIXKxEzQ0NqxIksN+XemC3Wa+hKmAJC4Vy01dZzoDWCbhA9C4laZhUKbd1C5CLELNV52lULrht4kTB0iLQSDTCvvn/mJmlzKSGWZBfnnN1KsEjhUTCl8K3Bq3D/0q/FHwOBriX+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsdHp27o="
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "state": "tx_+QEhCwH4hLhAsKA9Bl9dMsFjHqK382dqQFJlmBi/EHICG6jrf3xdvCvIXKxEzQ0NqxIksN+XemC3Wa+hKmAJC4Vy01dZzoDWCbhA9C4laZhUKbd1C5CLELNV52lULrht4kTB0iLQSDTCvvn/mJmlzKSGWZBfnnN1KsEjhUTCl8K3Bq3D/0q/FHwOBriX+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsdHp27o="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423458,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
  "id": -576460752303423458,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
      "balance": 40000000000000
    },
    {
      "account": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423457,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
  "id": -576460752303423457,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAsKA9Bl9dMsFjHqK382dqQFJlmBi/EHICG6jrf3xdvCvIXKxEzQ0NqxIksN+XemC3Wa+hKmAJC4Vy01dZzoDWCbhA9C4laZhUKbd1C5CLELNV52lULrht4kTB0iLQSDTCvvn/mJmlzKSGWZBfnnN1KsEjhUTCl8K3Bq3D/0q/FHwOBriX+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsdHp27o=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJgALDvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAA6duKo"
  },
  "version": 1
}
```
