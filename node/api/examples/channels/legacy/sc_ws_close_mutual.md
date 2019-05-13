
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC&role=initiator
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC&role=responder
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
    "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwRqQ7eQ",
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
    "tx": "tx_+MsLAfhCuEBkSxMnuNp3kGHEftADtPhwBSKzJoO3P28Fq2bT3XF+cW3shQDS4EI7I7THoa/gMD3bCiLa9uHqqZS1r/+/NW8CuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/BLQng84="
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
    "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwRqQ7eQ",
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
    "tx": "tx_+MsLAfhCuEClco2MB7PPPOHTcAOmmPUuZXVkrKIvosKJiG1nZZ6c/OcqPsJVrPcdGNMEg9nNC7MXrwlurbNpmXI7I+1D6OIOuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/BKMoIDo="
  }
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
    "tx": "tx_+QENCwH4hLhAZEsTJ7jad5BhxH7QA7T4cAUisyaDtz9vBatm091xfnFt7IUA0uBCOyO0x6Gv4DA92woi2vbh6qmUta//vzVvArhApXKNjAezzzzh03ADppj1LmV1ZKyiL6LCiYhtZ2WenPznKj7CVaz3HRjTBIPZzQuzF68Jbq2zaZlyOyPtQ+jiDriD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwQGYsFm"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": null,
  "payload": {
    "tx": "tx_+QENCwH4hLhAZEsTJ7jad5BhxH7QA7T4cAUisyaDtz9vBatm091xfnFt7IUA0uBCOyO0x6Gv4DA92woi2vbh6qmUta//vzVvArhApXKNjAezzzzh03ADppj1LmV1ZKyiL6LCiYhtZ2WenPznKj7CVaz3HRjTBIPZzQuzF68Jbq2zaZlyOyPtQ+jiDriD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwQGYsFm"
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
  "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
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
  "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
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
  "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
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
  "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
  "payload": {
    "event": "open"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
  "payload": {
    "state": "tx_+QENCwH4hLhAZEsTJ7jad5BhxH7QA7T4cAUisyaDtz9vBatm091xfnFt7IUA0uBCOyO0x6Gv4DA92woi2vbh6qmUta//vzVvArhApXKNjAezzzzh03ADppj1LmV1ZKyiL6LCiYhtZ2WenPznKj7CVaz3HRjTBIPZzQuzF68Jbq2zaZlyOyPtQ+jiDriD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwQGYsFm"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
  "payload": {
    "state": "tx_+QENCwH4hLhAZEsTJ7jad5BhxH7QA7T4cAUisyaDtz9vBatm091xfnFt7IUA0uBCOyO0x6Gv4DA92woi2vbh6qmUta//vzVvArhApXKNjAezzzzh03ADppj1LmV1ZKyiL6LCiYhtZ2WenPznKj7CVaz3HRjTBIPZzQuzF68Jbq2zaZlyOyPtQ+jiDriD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwQGYsFm"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "shutdown"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
  "payload": {
    "tx": "tx_+F01AaEGXfP3k2aiLfV2X4HR75EK/1UzKSNqQqHHe0CN8/jQc6GhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmhjaR1q+//4YbSOtX4AEAhhIwnOVAAAWwHvpF",
    "updates": []
  },
  "tag": "shutdown_sign",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "shutdown_sign",
  "payload": {
    "tx": "tx_+KcLAfhCuEC1uzCpbr9f7MYnkb5u/iL9okyhJTcRMGlTIqgMsari9Kdomn+Z+P3FmcAw1ma4GENBPYF/hl/X9EJi1fktkKAOuF/4XTUBoQZd8/eTZqIt9XZfgdHvkQr/VTMpI2pCocd7QI3z+NBzoaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGNpHWr7//hhtI61fgAQCGEjCc5UAABc176hQ="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
  "payload": {
    "tx": "tx_+F01AaEGXfP3k2aiLfV2X4HR75EK/1UzKSNqQqHHe0CN8/jQc6GhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmhjaR1q+//4YbSOtX4AEAhhIwnOVAAAWwHvpF",
    "updates": []
  },
  "tag": "shutdown_sign_ack",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "shutdown_sign_ack",
  "payload": {
    "tx": "tx_+KcLAfhCuEA2hK6nlhTF+hVjLYYoh09xVn5M4BrSwB3dXyjteMotYj8/+WpdbJwvO1KBUsg2p2zedlZnnVfR5g7O4m1q9OkOuF/4XTUBoQZd8/eTZqIt9XZfgdHvkQr/VTMpI2pCocd7QI3z+NBzoaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGNpHWr7//hhtI61fgAQCGEjCc5UAABY9XDr0="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
  "payload": {
    "tx": "tx_+OkLAfiEuEA2hK6nlhTF+hVjLYYoh09xVn5M4BrSwB3dXyjteMotYj8/+WpdbJwvO1KBUsg2p2zedlZnnVfR5g7O4m1q9OkOuEC1uzCpbr9f7MYnkb5u/iL9okyhJTcRMGlTIqgMsari9Kdomn+Z+P3FmcAw1ma4GENBPYF/hl/X9EJi1fktkKAOuF/4XTUBoQZd8/eTZqIt9XZfgdHvkQr/VTMpI2pCocd7QI3z+NBzoaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGNpHWr7//hhtI61fgAQCGEjCc5UAABVYF49s="
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
  "payload": {
    "event": "close_mutual"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
  "payload": {
    "event": "died"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
  "payload": {
    "tx": "tx_+OkLAfiEuEA2hK6nlhTF+hVjLYYoh09xVn5M4BrSwB3dXyjteMotYj8/+WpdbJwvO1KBUsg2p2zedlZnnVfR5g7O4m1q9OkOuEC1uzCpbr9f7MYnkb5u/iL9okyhJTcRMGlTIqgMsari9Kdomn+Z+P3FmcAw1ma4GENBPYF/hl/X9EJi1fktkKAOuF/4XTUBoQZd8/eTZqIt9XZfgdHvkQr/VTMpI2pCocd7QI3z+NBzoaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGNpHWr7//hhtI61fgAQCGEjCc5UAABVYF49s="
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
  "payload": {
    "event": "close_mutual"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
  "payload": {
    "event": "died"
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC&role=initiator
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC&role=responder
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
    "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwacFM/z",
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
    "tx": "tx_+MsLAfhCuECaHxrOXQB62F7zLVyRAEpR/LxVwFqcn6XlWVmkxeD/IRO0N7AiA5MI5pJAlpcgoDWS6jMszatmzDyWm698OUcBuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/BuQuHu8="
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
    "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwacFM/z",
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
    "tx": "tx_+MsLAfhCuED03nq3Nu91Votu/GBda41x1yC826uIeN6rF4svrQgomkBhwUPtAXGuo9dwetzW7ku9Co6JQ0seGtzt4nzA/wsDuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/BsMX/1Q="
  }
}
```

#### responder <--- node
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
    "tx": "tx_+QENCwH4hLhAmh8azl0Aethe8y1ckQBKUfy8VcBanJ+l5VlZpMXg/yETtDewIgOTCOaSQJaXIKA1kuozLM2rZsw8lpuvfDlHAbhA9N56tzbvdVaLbvxgXWuNcdcgvNuriHjeqxeLL60IKJpAYcFD7QFxrqPXcHrc1u5LvQqOiUNLHhrc7eJ8wP8LA7iD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwZdPEBJ"
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
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
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
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
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
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "event": "open"
  },
  "version": 1
}
```

#### responder <--- node
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

#### initiator <--- node
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

#### initiator <--- node
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

#### responder ---> node
```javascript
{
  "action": "shutdown"
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "tx": "tx_+F01AaEGxg0THRn6EnayrKAiA7XHtC8jht9LlO75Omp4uAd28NWhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhjaR1q+//4YbSOtX4AEAhhIwnOVAAAFXc+xr",
    "updates": []
  },
  "tag": "shutdown_sign",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "action": "shutdown_sign",
  "payload": {
    "tx": "tx_+KcLAfhCuEDucfjqyAJud1hbiHbDhgwAudJyHFY6TYmqPFe4xYD5XHv1XZMBlrqbQoUL2IThfYOah6WWXXPKNmTM/waBBSYCuF/4XTUBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSGNpHWr7//hhtI61fgAQCGEjCc5UAAATaHDXc="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "tx": "tx_+F01AaEGxg0THRn6EnayrKAiA7XHtC8jht9LlO75Omp4uAd28NWhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhjaR1q+//4YbSOtX4AEAhhIwnOVAAAFXc+xr",
    "updates": []
  },
  "tag": "shutdown_sign_ack",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "shutdown_sign_ack",
  "payload": {
    "tx": "tx_+KcLAfhCuEBoq5PkpWljAviMhg29b6KRZHOQskyU8Xp1iqyFHxA+iir/zXdY0x0jfXOCJmn03qpksyuvHyEwEZxsQeryXboLuF/4XTUBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSGNpHWr7//hhtI61fgAQCGEjCc5UAAAWMppJI="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "tx": "tx_+OkLAfiEuEBoq5PkpWljAviMhg29b6KRZHOQskyU8Xp1iqyFHxA+iir/zXdY0x0jfXOCJmn03qpksyuvHyEwEZxsQeryXboLuEDucfjqyAJud1hbiHbDhgwAudJyHFY6TYmqPFe4xYD5XHv1XZMBlrqbQoUL2IThfYOah6WWXXPKNmTM/waBBSYCuF/4XTUBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSGNpHWr7//hhtI61fgAQCGEjCc5UAAATAbgLE="
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "event": "close_mutual"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "event": "died"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "tx": "tx_+OkLAfiEuEBoq5PkpWljAviMhg29b6KRZHOQskyU8Xp1iqyFHxA+iir/zXdY0x0jfXOCJmn03qpksyuvHyEwEZxsQeryXboLuEDucfjqyAJud1hbiHbDhgwAudJyHFY6TYmqPFe4xYD5XHv1XZMBlrqbQoUL2IThfYOah6WWXXPKNmTM/waBBSYCuF/4XTUBoQbGDRMdGfoSdrKsoCIDtce0LyOG30uU7vk6ani4B3bw1aEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSGNpHWr7//hhtI61fgAQCGEjCc5UAAATAbgLE="
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "event": "close_mutual"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "event": "died"
  },
  "version": 1
}
```
