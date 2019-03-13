
#### initiator opens a WebSocket connection (2019-03-18 14:06:33.601)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC&role=initiator
```

#### responder opens a WebSocket connection (2019-03-18 14:06:33.628)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC&role=responder
```

#### responder <--- node (2019-03-18 14:06:34.590)
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

#### initiator <--- node (2019-03-18 14:06:34.609)
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

#### initiator <--- node (2019-03-18 14:06:34.609)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwacFM/z"
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:06:34.746)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_+MsLAfhCuECaHxrOXQB62F7zLVyRAEpR/LxVwFqcn6XlWVmkxeD/IRO0N7AiA5MI5pJAlpcgoDWS6jMszatmzDyWm698OUcBuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/BuQuHu8="
  }
}
```

#### responder <--- node (2019-03-18 14:06:34.765)
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

#### responder <--- node (2019-03-18 14:06:34.773)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwacFM/z"
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-18 14:06:34.780)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_+MsLAfhCuED03nq3Nu91Votu/GBda41x1yC826uIeN6rF4svrQgomkBhwUPtAXGuo9dwetzW7ku9Co6JQ0seGtzt4nzA/wsDuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/BsMX/1Q="
  }
}
```

#### initiator <--- node (2019-03-18 14:06:34.800)
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

#### responder <--- node (2019-03-18 14:06:34.800)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+QENCwH4hLhAmh8azl0Aethe8y1ckQBKUfy8VcBanJ+l5VlZpMXg/yETtDewIgOTCOaSQJaXIKA1kuozLM2rZsw8lpuvfDlHAbhA9N56tzbvdVaLbvxgXWuNcdcgvNuriHjeqxeLL60IKJpAYcFD7QFxrqPXcHrc1u5LvQqOiUNLHhrc7eJ8wP8LA7iD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwZdPEBJ"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:06:34.801)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+QENCwH4hLhAmh8azl0Aethe8y1ckQBKUfy8VcBanJ+l5VlZpMXg/yETtDewIgOTCOaSQJaXIKA1kuozLM2rZsw8lpuvfDlHAbhA9N56tzbvdVaLbvxgXWuNcdcgvNuriHjeqxeLL60IKJpAYcFD7QFxrqPXcHrc1u5LvQqOiUNLHhrc7eJ8wP8LA7iD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwZdPEBJ"
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:06:35.424)
```javascript
{
  "id": -576460752303423454,
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

#### initiator <--- node (2019-03-18 14:06:35.436)
```javascript
{
  "channel_id": null,
  "id": -576460752303423454,
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

#### responder <--- node (2019-03-18 14:06:36.631)
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

#### initiator <--- node (2019-03-18 14:06:36.632)
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

#### initiator <--- node (2019-03-18 14:06:36.636)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:06:36.638)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:06:36.660)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:06:36.662)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
    "data": {
      "state": "tx_+QENCwH4hLhAmh8azl0Aethe8y1ckQBKUfy8VcBanJ+l5VlZpMXg/yETtDewIgOTCOaSQJaXIKA1kuozLM2rZsw8lpuvfDlHAbhA9N56tzbvdVaLbvxgXWuNcdcgvNuriHjeqxeLL60IKJpAYcFD7QFxrqPXcHrc1u5LvQqOiUNLHhrc7eJ8wP8LA7iD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwZdPEBJ"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:06:36.664)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:06:36.665)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
    "data": {
      "state": "tx_+QENCwH4hLhAmh8azl0Aethe8y1ckQBKUfy8VcBanJ+l5VlZpMXg/yETtDewIgOTCOaSQJaXIKA1kuozLM2rZsw8lpuvfDlHAbhA9N56tzbvdVaLbvxgXWuNcdcgvNuriHjeqxeLL60IKJpAYcFD7QFxrqPXcHrc1u5LvQqOiUNLHhrc7eJ8wP8LA7iD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwZdPEBJ"
    }
  },
  "version": 1
}
```

#### responder: (2019-03-18 14:06:36.818)
> Funding has been confirmed locally on-chain

#### responder: (2019-03-18 14:06:36.818)
> Funding has been confirmed on-chain by other party

#### responder: (2019-03-18 14:06:36.818)
> Channel is `open` and ready to use

#### initiator: (2019-03-18 14:06:36.818)
> Funding has been confirmed locally on-chain

#### initiator: (2019-03-18 14:06:36.819)
> Funding has been confirmed on-chain by other party

#### initiator: (2019-03-18 14:06:36.819)
> Channel is `open` and ready to use
