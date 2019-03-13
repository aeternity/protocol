
#### initiator opens a WebSocket connection (2019-03-18 14:15:06.219)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC&role=initiator
```

#### responder opens a WebSocket connection (2019-03-18 14:15:06.239)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC&role=responder
```

#### responder <--- node (2019-03-18 14:15:07.296)
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

#### initiator <--- node (2019-03-18 14:15:07.299)
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

#### initiator <--- node (2019-03-18 14:15:07.342)
```javascript
{
  "action": "sign",
  "channel_id": null,
  "payload": {
    "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwEWWmi2"
  },
  "tag": "initiator_sign",
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:15:07.432)
```javascript
{
  "action": "initiator_sign",
  "payload": {
    "tx": "tx_+MsLAfhCuEA8qOUSomEv4vYDrI78VvYo5/hgXIXzHFftvIWVKP1P6N823VPgptGj6+8JgctKZNIHrRp/3dApg/3LEVleoOQOuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/Ac8BpMU="
  }
}
```

#### responder <--- node (2019-03-18 14:15:07.471)
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

#### responder <--- node (2019-03-18 14:15:07.473)
```javascript
{
  "action": "sign",
  "channel_id": null,
  "payload": {
    "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwEWWmi2"
  },
  "tag": "responder_sign",
  "version": 1
}
```

#### responder ---> node (2019-03-18 14:15:07.475)
```javascript
{
  "action": "responder_sign",
  "payload": {
    "tx": "tx_+MsLAfhCuEAHZz43YSe53ifjLFyM38v7YR/svIA8AIDZkNyybX65RrwZ+CkJmGiLAHOLTmwIxIiwBb9zClE19gSo9fJPRf4OuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/Ac2Lv6w="
  }
}
```

#### responder <--- node (2019-03-18 14:15:07.496)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": null,
  "payload": {
    "tx": "tx_+QENCwH4hLhAB2c+N2Enud4n4yxcjN/L+2Ef7LyAPACA2ZDcsm1+uUa8GfgpCZhoiwBzi05sCMSIsAW/cwpRNfYEqPXyT0X+DrhAPKjlEqJhL+L2A6yO/Fb2KOf4YFyF8xxX7byFlSj9T+jfNt1T4KbRo+vvCYHLSmTSB60af93QKYP9yxFZXqDkDriD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwHTqe+I"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:15:07.497)
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

#### initiator <--- node (2019-03-18 14:15:07.498)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": null,
  "payload": {
    "tx": "tx_+QENCwH4hLhAB2c+N2Enud4n4yxcjN/L+2Ef7LyAPACA2ZDcsm1+uUa8GfgpCZhoiwBzi05sCMSIsAW/cwpRNfYEqPXyT0X+DrhAPKjlEqJhL+L2A6yO/Fb2KOf4YFyF8xxX7byFlSj9T+jfNt1T4KbRo+vvCYHLSmTSB60af93QKYP9yxFZXqDkDriD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwHTqe+I"
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:15:08.203)
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

#### initiator <--- node (2019-03-18 14:15:08.217)
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

#### responder <--- node (2019-03-18 14:15:09.31)
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

#### initiator <--- node (2019-03-18 14:15:09.37)
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

#### responder <--- node (2019-03-18 14:15:09.37)
```javascript
{
  "action": "info",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "event": "funding_locked"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:15:09.39)
```javascript
{
  "action": "info",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "event": "funding_locked"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:15:09.54)
```javascript
{
  "action": "info",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "event": "open"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:15:09.57)
```javascript
{
  "action": "info",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "event": "open"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:15:09.57)
```javascript
{
  "action": "update",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "state": "tx_+QENCwH4hLhAB2c+N2Enud4n4yxcjN/L+2Ef7LyAPACA2ZDcsm1+uUa8GfgpCZhoiwBzi05sCMSIsAW/cwpRNfYEqPXyT0X+DrhAPKjlEqJhL+L2A6yO/Fb2KOf4YFyF8xxX7byFlSj9T+jfNt1T4KbRo+vvCYHLSmTSB60af93QKYP9yxFZXqDkDriD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwHTqe+I"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:15:09.59)
```javascript
{
  "action": "update",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "state": "tx_+QENCwH4hLhAB2c+N2Enud4n4yxcjN/L+2Ef7LyAPACA2ZDcsm1+uUa8GfgpCZhoiwBzi05sCMSIsAW/cwpRNfYEqPXyT0X+DrhAPKjlEqJhL+L2A6yO/Fb2KOf4YFyF8xxX7byFlSj9T+jfNt1T4KbRo+vvCYHLSmTSB60af93QKYP9yxFZXqDkDriD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwHTqe+I"
  },
  "version": 1
}
```

#### initiator: (2019-03-18 14:15:09.285)
> Funding has been confirmed locally on-chain

#### responder: (2019-03-18 14:15:09.285)
> Funding has been confirmed locally on-chain

#### responder: (2019-03-18 14:15:09.285)
> Funding has been confirmed on-chain by other party

#### initiator: (2019-03-18 14:15:09.285)
> Funding has been confirmed on-chain by other party

#### responder: (2019-03-18 14:15:09.285)
> Channel is `open` and ready to use

#### initiator: (2019-03-18 14:15:09.285)
> Channel is `open` and ready to use

#### initiator ---> node (2019-03-18 14:15:09.285)
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

#### initiator <--- node (2019-03-18 14:15:09.291)
```javascript
{
  "action": "get",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
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

#### initiator ---> node (2019-03-18 14:15:09.292)
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

#### initiator <--- node (2019-03-18 14:15:09.335)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "tx": "tx_+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0C+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4YUGXZs="
  },
  "tag": "update",
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:15:09.336)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEDXknLeKt1fP/3GE1Zyxs0BkYqHrNi0DVDiMbwd3tJYRLM8IoYjaZwPUJFGjVVT/rC0mfiDaliN2jV+7jrjHawIuJf4lTkBoQa/mYDOYVZNuFBtkiWU8EpQy9V5iSxb3zNPPQIhKgY+XQL4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoNUqd4GTOFacRsLar0VqTNSHraQXvmyQrL/MBqX090Lh3szM2A=="
  }
}
```

#### responder <--- node (2019-03-18 14:15:09.375)
```javascript
{
  "action": "info",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "event": "update"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:15:09.376)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "tx": "tx_+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0C+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4YUGXZs="
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node (2019-03-18 14:15:09.377)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+N8LAfhCuEAVfA1pJarvlNkHoyqNdvbft6DUdcDC1EmMdlJjFFgEC+++4scRmIYuIInWutCk91R/WJ7PzIzAGje5+f7NAJcDuJf4lTkBoQa/mYDOYVZNuFBtkiWU8EpQy9V5iSxb3zNPPQIhKgY+XQL4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoNUqd4GTOFacRsLar0VqTNSHraQXvmyQrL/MBqX090LhaDx9GQ=="
  }
}
```

#### responder <--- node (2019-03-18 14:15:09.401)
```javascript
{
  "action": "update",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "state": "tx_+QEhCwH4hLhAFXwNaSWq75TZB6MqjXb237eg1HXAwtRJjHZSYxRYBAvvvuLHEZiGLiCJ1rrQpPdUf1iez8yMwBo3ufn+zQCXA7hA15Jy3irdXz/9xhNWcsbNAZGKh6zYtA1Q4jG8Hd7SWESzPCKGI2mcD1CRRo1VU/6wtJn4g2pYjdo1fu464x2sCLiX+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0C+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4a8Rvaw="
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:15:09.420)
```javascript
{
  "action": "update",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "state": "tx_+QEhCwH4hLhAFXwNaSWq75TZB6MqjXb237eg1HXAwtRJjHZSYxRYBAvvvuLHEZiGLiCJ1rrQpPdUf1iez8yMwBo3ufn+zQCXA7hA15Jy3irdXz/9xhNWcsbNAZGKh6zYtA1Q4jG8Hd7SWESzPCKGI2mcD1CRRo1VU/6wtJn4g2pYjdo1fu464x2sCLiX+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0C+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4a8Rvaw="
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:15:09.431)
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

#### initiator <--- node (2019-03-18 14:15:09.436)
```javascript
{
  "action": "get",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
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

#### initiator ---> node (2019-03-18 14:15:09.437)
```javascript
{
  "action": "get",
  "payload": {
    "a": "a"
  },
  "tag": "offchain_state"
}
```

#### initiator <--- node (2019-03-18 14:15:09.441)
```javascript
{
  "action": "get",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAFXwNaSWq75TZB6MqjXb237eg1HXAwtRJjHZSYxRYBAvvvuLHEZiGLiCJ1rrQpPdUf1iez8yMwBo3ufn+zQCXA7hA15Jy3irdXz/9xhNWcsbNAZGKh6zYtA1Q4jG8Hd7SWESzPCKGI2mcD1CRRo1VU/6wtJn4g2pYjdo1fu464x2sCLiX+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0C+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4a8Rvaw=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJf/rDvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAJXk16b"
  },
  "tag": "offchain_state",
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:15:09.449)
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

#### initiator <--- node (2019-03-18 14:15:09.464)
```javascript
{
  "action": "get",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
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

#### responder ---> node (2019-03-18 14:15:09.465)
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

#### responder <--- node (2019-03-18 14:15:09.478)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "tx": "tx_+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0D+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv+PypBg="
  },
  "tag": "update",
  "version": 1
}
```

#### responder ---> node (2019-03-18 14:15:09.479)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEA/qqa78UGB58yjrLsXOCOhrI776/Jt9oui4iTNFkBsYXn87Bck3+vg5/jURgo93EmSpV6iHLjRSI3fOF64hEgGuJf4lTkBoQa/mYDOYVZNuFBtkiWU8EpQy9V5iSxb3zNPPQIhKgY+XQP4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/teJdNw=="
  }
}
```

#### initiator <--- node (2019-03-18 14:15:09.519)
```javascript
{
  "action": "info",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "event": "update"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:15:09.520)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "tx": "tx_+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0D+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv+PypBg="
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:15:09.522)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+N8LAfhCuEBg4LWvkze6zbzTnHHHFEscSlpEh6GVlJq95AJKZ8yHqVsI+YXhy3+bC4EOQw78XkGveKF2JbCwRG54NI51itkBuJf4lTkBoQa/mYDOYVZNuFBtkiWU8EpQy9V5iSxb3zNPPQIhKgY+XQP4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/PTf9qA=="
  }
}
```

#### initiator <--- node (2019-03-18 14:15:09.548)
```javascript
{
  "action": "update",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "state": "tx_+QEhCwH4hLhAP6qmu/FBgefMo6y7FzgjoayO++vybfaLouIkzRZAbGF5/OwXJN/r4Of41EYKPdxJkqVeohy40UiN3zheuIRIBrhAYOC1r5M3us2805xxxxRLHEpaRIehlZSaveQCSmfMh6lbCPmF4ct/mwuBDkMO/F5Br3ihdiWwsERueDSOdYrZAbiX+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0D+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv9GhDcI="
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:15:09.562)
```javascript
{
  "action": "update",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "state": "tx_+QEhCwH4hLhAP6qmu/FBgefMo6y7FzgjoayO++vybfaLouIkzRZAbGF5/OwXJN/r4Of41EYKPdxJkqVeohy40UiN3zheuIRIBrhAYOC1r5M3us2805xxxxRLHEpaRIehlZSaveQCSmfMh6lbCPmF4ct/mwuBDkMO/F5Br3ihdiWwsERueDSOdYrZAbiX+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0D+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv9GhDcI="
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:15:09.574)
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

#### initiator <--- node (2019-03-18 14:15:09.580)
```javascript
{
  "action": "get",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
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

#### initiator ---> node (2019-03-18 14:15:09.580)
```javascript
{
  "action": "get",
  "payload": {
    "a": "a"
  },
  "tag": "offchain_state"
}
```

#### initiator <--- node (2019-03-18 14:15:09.595)
```javascript
{
  "action": "get",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAP6qmu/FBgefMo6y7FzgjoayO++vybfaLouIkzRZAbGF5/OwXJN/r4Of41EYKPdxJkqVeohy40UiN3zheuIRIBrhAYOC1r5M3us2805xxxxRLHEpaRIehlZSaveQCSmfMh6lbCPmF4ct/mwuBDkMO/F5Br3ihdiWwsERueDSOdYrZAbiX+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0D+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv9GhDcI=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJf/7DvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAFkGvNa"
  },
  "tag": "offchain_state",
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:15:09.605)
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

#### initiator <--- node (2019-03-18 14:15:09.613)
```javascript
{
  "action": "get",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
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

#### responder ---> node (2019-03-18 14:15:09.614)
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

#### responder <--- node (2019-03-18 14:15:09.628)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "tx": "tx_+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0E+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsaauNCM="
  },
  "tag": "update",
  "version": 1
}
```

#### responder ---> node (2019-03-18 14:15:09.630)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuECpK+AUbIKquLpTwlmSl3a1zhBIu1q1W28nzU/TUF0qW8dsfa25GucHS5hZkB4x5yJgGRO/w5yiZeyYQvixYrkKuJf4lTkBoQa/mYDOYVZNuFBtkiWU8EpQy9V5iSxb3zNPPQIhKgY+XQT4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROx/JJAJA=="
  }
}
```

#### initiator <--- node (2019-03-18 14:15:09.671)
```javascript
{
  "action": "info",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "event": "update"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:15:09.672)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "tx": "tx_+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0E+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsaauNCM="
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:15:09.673)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+N8LAfhCuEC7hBarfSqTcbMp36bAGz5M6Cm7Arti9Uh7TFReZj25zjiWwxZyCMAgUZojguyHBhS/Uq8wssS08m49lhrtQmMGuJf4lTkBoQa/mYDOYVZNuFBtkiWU8EpQy9V5iSxb3zNPPQIhKgY+XQT4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROxh9xFtQ=="
  }
}
```

#### initiator <--- node (2019-03-18 14:15:09.703)
```javascript
{
  "action": "update",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "state": "tx_+QEhCwH4hLhAqSvgFGyCqri6U8JZkpd2tc4QSLtatVtvJ81P01BdKlvHbH2tuRrnB0uYWZAeMeciYBkTv8OcomXsmEL4sWK5CrhAu4QWq30qk3GzKd+mwBs+TOgpuwK7YvVIe0xUXmY9uc44lsMWcgjAIFGaI4LshwYUv1KvMLLEtPJuPZYa7UJjBriX+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0E+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsZaqwzg="
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:15:09.718)
```javascript
{
  "action": "update",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "state": "tx_+QEhCwH4hLhAqSvgFGyCqri6U8JZkpd2tc4QSLtatVtvJ81P01BdKlvHbH2tuRrnB0uYWZAeMeciYBkTv8OcomXsmEL4sWK5CrhAu4QWq30qk3GzKd+mwBs+TOgpuwK7YvVIe0xUXmY9uc44lsMWcgjAIFGaI4LshwYUv1KvMLLEtPJuPZYa7UJjBriX+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0E+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsZaqwzg="
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:15:09.736)
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

#### initiator <--- node (2019-03-18 14:15:09.741)
```javascript
{
  "action": "get",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
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

#### initiator ---> node (2019-03-18 14:15:09.742)
```javascript
{
  "action": "get",
  "payload": {
    "a": "a"
  },
  "tag": "offchain_state"
}
```

#### initiator <--- node (2019-03-18 14:15:09.748)
```javascript
{
  "action": "get",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAqSvgFGyCqri6U8JZkpd2tc4QSLtatVtvJ81P01BdKlvHbH2tuRrnB0uYWZAeMeciYBkTv8OcomXsmEL4sWK5CrhAu4QWq30qk3GzKd+mwBs+TOgpuwK7YvVIe0xUXmY9uc44lsMWcgjAIFGaI4LshwYUv1KvMLLEtPJuPZYa7UJjBriX+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0E+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsZaqwzg=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJgALDvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAA6duKo"
  },
  "tag": "offchain_state",
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:15:09.758)
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

#### initiator <--- node (2019-03-18 14:15:09.764)
```javascript
{
  "action": "get",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
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

#### initiator ---> node (2019-03-18 14:15:09.765)
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

#### initiator <--- node (2019-03-18 14:15:09.781)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "tx": "tx_+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0F+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv461qBE="
  },
  "tag": "update",
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:15:09.782)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEDW9zApyY+2QR+u99eaMAlk0rJlhC69nYbiaPEd5ZA1Lk+HjfioE2V4kvwxGh3G85ELxLkCoRrzjp1ZdFFVoVwDuJf4lTkBoQa/mYDOYVZNuFBtkiWU8EpQy9V5iSxb3zNPPQIhKgY+XQX4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/Qlw+Gg=="
  }
}
```

#### responder <--- node (2019-03-18 14:15:09.842)
```javascript
{
  "action": "info",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "event": "update"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:15:09.843)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "tx": "tx_+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0F+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv461qBE="
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node (2019-03-18 14:15:09.844)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+N8LAfhCuED9SpzbueEN8/11jDijpNb48l4ZaCLmeKpkBqzuzQVK5QZXuK8pZ4fFLYC+S5voxtucHz85FHF7bCiOZBDWsfAEuJf4lTkBoQa/mYDOYVZNuFBtkiWU8EpQy9V5iSxb3zNPPQIhKgY+XQX4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/4Lx3dA=="
  }
}
```

#### responder <--- node (2019-03-18 14:15:09.869)
```javascript
{
  "action": "update",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "state": "tx_+QEhCwH4hLhA1vcwKcmPtkEfrvfXmjAJZNKyZYQuvZ2G4mjxHeWQNS5Ph434qBNleJL8MRodxvORC8S5AqEa846dWXRRVaFcA7hA/Uqc27nhDfP9dYw4o6TW+PJeGWgi5niqZAas7s0FSuUGV7ivKWeHxS2Avkub6MbbnB8/ORRxe2wojmQQ1rHwBLiX+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0F+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv8eISQY="
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:15:09.884)
```javascript
{
  "action": "update",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "state": "tx_+QEhCwH4hLhA1vcwKcmPtkEfrvfXmjAJZNKyZYQuvZ2G4mjxHeWQNS5Ph434qBNleJL8MRodxvORC8S5AqEa846dWXRRVaFcA7hA/Uqc27nhDfP9dYw4o6TW+PJeGWgi5niqZAas7s0FSuUGV7ivKWeHxS2Avkub6MbbnB8/ORRxe2wojmQQ1rHwBLiX+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0F+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv8eISQY="
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:15:09.894)
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

#### initiator <--- node (2019-03-18 14:15:09.900)
```javascript
{
  "action": "get",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
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

#### initiator ---> node (2019-03-18 14:15:09.901)
```javascript
{
  "action": "get",
  "payload": {
    "a": "a"
  },
  "tag": "offchain_state"
}
```

#### initiator <--- node (2019-03-18 14:15:09.907)
```javascript
{
  "action": "get",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhA1vcwKcmPtkEfrvfXmjAJZNKyZYQuvZ2G4mjxHeWQNS5Ph434qBNleJL8MRodxvORC8S5AqEa846dWXRRVaFcA7hA/Uqc27nhDfP9dYw4o6TW+PJeGWgi5niqZAas7s0FSuUGV7ivKWeHxS2Avkub6MbbnB8/ORRxe2wojmQQ1rHwBLiX+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0F+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv8eISQY=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJf/7DvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAFkGvNa"
  },
  "tag": "offchain_state",
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:15:09.915)
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

#### initiator <--- node (2019-03-18 14:15:09.928)
```javascript
{
  "action": "get",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
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

#### responder ---> node (2019-03-18 14:15:09.930)
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

#### responder <--- node (2019-03-18 14:15:09.944)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "tx": "tx_+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0G+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsRSIQr8="
  },
  "tag": "update",
  "version": 1
}
```

#### responder ---> node (2019-03-18 14:15:09.945)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuECzHrb6PRn7SJ3vImJh36y5L+YzXv43ggVMWXeJHgLVODoFQTG7A7Y7nUIiLDMw+y32a2pwyRtL/EbOBv6kPecJuJf4lTkBoQa/mYDOYVZNuFBtkiWU8EpQy9V5iSxb3zNPPQIhKgY+XQb4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROxdelsqQ=="
  }
}
```

#### initiator <--- node (2019-03-18 14:15:09.986)
```javascript
{
  "action": "info",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "event": "update"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:15:09.987)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "tx": "tx_+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0G+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsRSIQr8="
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:15:09.989)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+N8LAfhCuEBgWYwpwHtaRQUcWPj3Y8ndomVXAukwHCCebTU9i1z2APmMRpalxtK4vEtA4VFI66S2JVory0eszMaq+qfMWIIAuJf4lTkBoQa/mYDOYVZNuFBtkiWU8EpQy9V5iSxb3zNPPQIhKgY+XQb4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROxU8YSJQ=="
  }
}
```

#### initiator <--- node (2019-03-18 14:15:10.28)
```javascript
{
  "action": "update",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "state": "tx_+QEhCwH4hLhAYFmMKcB7WkUFHFj492PJ3aJlVwLpMBwgnm01PYtc9gD5jEaWpcbSuLxLQOFRSOuktiVaK8tHrMzGqvqnzFiCALhAsx62+j0Z+0id7yJiYd+suS/mM17+N4IFTFl3iR4C1Tg6BUExuwO2O51CIiwzMPst9mtqcMkbS/xGzgb+pD3nCbiX+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0G+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsV/17jE="
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:15:10.47)
```javascript
{
  "action": "update",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "state": "tx_+QEhCwH4hLhAYFmMKcB7WkUFHFj492PJ3aJlVwLpMBwgnm01PYtc9gD5jEaWpcbSuLxLQOFRSOuktiVaK8tHrMzGqvqnzFiCALhAsx62+j0Z+0id7yJiYd+suS/mM17+N4IFTFl3iR4C1Tg6BUExuwO2O51CIiwzMPst9mtqcMkbS/xGzgb+pD3nCbiX+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0G+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsV/17jE="
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:15:10.65)
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

#### initiator <--- node (2019-03-18 14:15:10.71)
```javascript
{
  "action": "get",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
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

#### initiator ---> node (2019-03-18 14:15:10.71)
```javascript
{
  "action": "get",
  "payload": {
    "a": "a"
  },
  "tag": "offchain_state"
}
```

#### initiator <--- node (2019-03-18 14:15:10.77)
```javascript
{
  "action": "get",
  "channel_id": "ch_2TPA12qYnQUE6359Vmg55SD5wMvKUQxZA9wWChWSsRkFvvYAUd",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAYFmMKcB7WkUFHFj492PJ3aJlVwLpMBwgnm01PYtc9gD5jEaWpcbSuLxLQOFRSOuktiVaK8tHrMzGqvqnzFiCALhAsx62+j0Z+0id7yJiYd+suS/mM17+N4IFTFl3iR4C1Tg6BUExuwO2O51CIiwzMPst9mtqcMkbS/xGzgb+pD3nCbiX+JU5AaEGv5mAzmFWTbhQbZIllPBKUMvVeYksW98zTz0CISoGPl0G+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsV/17jE=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJgALDvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAA6duKo"
  },
  "tag": "offchain_state",
  "version": 1
}
```
