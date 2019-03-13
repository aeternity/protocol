
#### initiator opens a WebSocket connection (2019-03-18 14:15:31.247)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC&role=initiator
```

#### responder opens a WebSocket connection (2019-03-18 14:15:31.267)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC&role=responder
```

#### responder <--- node (2019-03-18 14:15:32.243)
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

#### initiator <--- node (2019-03-18 14:15:32.246)
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

#### initiator <--- node (2019-03-18 14:15:32.257)
```javascript
{
  "action": "sign",
  "channel_id": null,
  "payload": {
    "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwacFM/z"
  },
  "tag": "initiator_sign",
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:15:32.352)
```javascript
{
  "action": "initiator_sign",
  "payload": {
    "tx": "tx_+MsLAfhCuECaHxrOXQB62F7zLVyRAEpR/LxVwFqcn6XlWVmkxeD/IRO0N7AiA5MI5pJAlpcgoDWS6jMszatmzDyWm698OUcBuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/BuQuHu8="
  }
}
```

#### responder <--- node (2019-03-18 14:15:32.377)
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

#### responder <--- node (2019-03-18 14:15:32.378)
```javascript
{
  "action": "sign",
  "channel_id": null,
  "payload": {
    "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwacFM/z"
  },
  "tag": "responder_sign",
  "version": 1
}
```

#### responder ---> node (2019-03-18 14:15:32.380)
```javascript
{
  "action": "responder_sign",
  "payload": {
    "tx": "tx_+MsLAfhCuED03nq3Nu91Votu/GBda41x1yC826uIeN6rF4svrQgomkBhwUPtAXGuo9dwetzW7ku9Co6JQ0seGtzt4nzA/wsDuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/BsMX/1Q="
  }
}
```

#### responder <--- node (2019-03-18 14:15:32.401)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": null,
  "payload": {
    "tx": "tx_+QENCwH4hLhAmh8azl0Aethe8y1ckQBKUfy8VcBanJ+l5VlZpMXg/yETtDewIgOTCOaSQJaXIKA1kuozLM2rZsw8lpuvfDlHAbhA9N56tzbvdVaLbvxgXWuNcdcgvNuriHjeqxeLL60IKJpAYcFD7QFxrqPXcHrc1u5LvQqOiUNLHhrc7eJ8wP8LA7iD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwZdPEBJ"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:15:32.409)
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

#### initiator <--- node (2019-03-18 14:15:32.409)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": null,
  "payload": {
    "tx": "tx_+QENCwH4hLhAmh8azl0Aethe8y1ckQBKUfy8VcBanJ+l5VlZpMXg/yETtDewIgOTCOaSQJaXIKA1kuozLM2rZsw8lpuvfDlHAbhA9N56tzbvdVaLbvxgXWuNcdcgvNuriHjeqxeLL60IKJpAYcFD7QFxrqPXcHrc1u5LvQqOiUNLHhrc7eJ8wP8LA7iD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwZdPEBJ"
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:15:33.249)
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

#### initiator <--- node (2019-03-18 14:15:33.255)
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

#### responder <--- node (2019-03-18 14:15:36.245)
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

#### initiator <--- node (2019-03-18 14:15:36.261)
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

#### initiator <--- node (2019-03-18 14:15:36.263)
```javascript
{
  "action": "info",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "event": "funding_locked"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:15:36.264)
```javascript
{
  "action": "info",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "event": "funding_locked"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:15:36.276)
```javascript
{
  "action": "info",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "event": "open"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:15:36.279)
```javascript
{
  "action": "update",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "state": "tx_+QENCwH4hLhAmh8azl0Aethe8y1ckQBKUfy8VcBanJ+l5VlZpMXg/yETtDewIgOTCOaSQJaXIKA1kuozLM2rZsw8lpuvfDlHAbhA9N56tzbvdVaLbvxgXWuNcdcgvNuriHjeqxeLL60IKJpAYcFD7QFxrqPXcHrc1u5LvQqOiUNLHhrc7eJ8wP8LA7iD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwZdPEBJ"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:15:36.281)
```javascript
{
  "action": "info",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "event": "open"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:15:36.283)
```javascript
{
  "action": "update",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "state": "tx_+QENCwH4hLhAmh8azl0Aethe8y1ckQBKUfy8VcBanJ+l5VlZpMXg/yETtDewIgOTCOaSQJaXIKA1kuozLM2rZsw8lpuvfDlHAbhA9N56tzbvdVaLbvxgXWuNcdcgvNuriHjeqxeLL60IKJpAYcFD7QFxrqPXcHrc1u5LvQqOiUNLHhrc7eJ8wP8LA7iD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwZdPEBJ"
  },
  "version": 1
}
```

#### initiator: (2019-03-18 14:15:36.576)
> Funding has been confirmed locally on-chain

#### responder: (2019-03-18 14:15:36.576)
> Funding has been confirmed locally on-chain

#### initiator: (2019-03-18 14:15:36.576)
> Funding has been confirmed on-chain by other party

#### responder: (2019-03-18 14:15:36.576)
> Funding has been confirmed on-chain by other party

#### initiator: (2019-03-18 14:15:36.576)
> Channel is `open` and ready to use

#### responder: (2019-03-18 14:15:36.577)
> Channel is `open` and ready to use
