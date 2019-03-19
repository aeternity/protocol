
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
    "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwIjpDEM"
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
    "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwIjpDEM"
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
  "action": "shutdown"
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "tx": "tx_+F01AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XihAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmhjaR1q+//4YbSOtX4AEAhhIwnOVAAANe4ar8"
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
    "tx": "tx_+KcLAfhCuEBjFLnPgoPp15I2oYzgPjrQJQyqvg1O1EimmGosw9jrNw2jTfaZXzSleSqPJ7F5T/dqLUSmqN5Py7ZlWQFKn4IFuF/4XTUBoQY/KKbrcmIHVGiACvxWdOMPb8t4vp8YuHJJaGqCvt7teKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGNpHWr7//hhtI61fgAQCGEjCc5UAAA9iOZm4="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "tx": "tx_+F01AaEGPyim63JiB1RogAr8VnTjD2/LeL6fGLhySWhqgr7e7XihAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmhjaR1q+//4YbSOtX4AEAhhIwnOVAAANe4ar8"
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
    "tx": "tx_+KcLAfhCuECzm2E8CsyzKvbO6zx8QHMnqX2lorQfH/t+FE7SQsf7tAL32BbqyFMox0su5RN9nriuXW1zdSCBkNvtKGDyVukCuF/4XTUBoQY/KKbrcmIHVGiACvxWdOMPb8t4vp8YuHJJaGqCvt7teKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGNpHWr7//hhtI61fgAQCGEjCc5UAAA3BBwE8="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "tx": "tx_+OkLAfiEuEBjFLnPgoPp15I2oYzgPjrQJQyqvg1O1EimmGosw9jrNw2jTfaZXzSleSqPJ7F5T/dqLUSmqN5Py7ZlWQFKn4IFuECzm2E8CsyzKvbO6zx8QHMnqX2lorQfH/t+FE7SQsf7tAL32BbqyFMox0su5RN9nriuXW1zdSCBkNvtKGDyVukCuF/4XTUBoQY/KKbrcmIHVGiACvxWdOMPb8t4vp8YuHJJaGqCvt7teKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGNpHWr7//hhtI61fgAQCGEjCc5UAAA3KhgIw="
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
    "event": "close_mutual"
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
    "event": "died"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_UpJnk4rp1qMqze3PxDKNAPUtKR18MNkCoAx3wX8gkQy8JfsjM",
  "payload": {
    "tx": "tx_+OkLAfiEuEBjFLnPgoPp15I2oYzgPjrQJQyqvg1O1EimmGosw9jrNw2jTfaZXzSleSqPJ7F5T/dqLUSmqN5Py7ZlWQFKn4IFuECzm2E8CsyzKvbO6zx8QHMnqX2lorQfH/t+FE7SQsf7tAL32BbqyFMox0su5RN9nriuXW1zdSCBkNvtKGDyVukCuF/4XTUBoQY/KKbrcmIHVGiACvxWdOMPb8t4vp8YuHJJaGqCvt7teKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGNpHWr7//hhtI61fgAQCGEjCc5UAAA3KhgIw="
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
    "event": "close_mutual"
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
    "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwRqQ7eQ"
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
    "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwRqQ7eQ"
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
  "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
  "payload": {
    "tx": "tx_+F01AaEGXfP3k2aiLfV2X4HR75EK/1UzKSNqQqHHe0CN8/jQc6GhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhjaR1q+//4YbSOtX4AEAhhIwnOVAAAFP7TAc"
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
    "tx": "tx_+KcLAfhCuEDPyVlPLD3thSWyeg0TM7r5acXU4tlKm/FSEtI/aYrLr0WZa+CwO97rUW2qhUlEbM7aEiKEnh48kEu+gmzqv9IBuF/4XTUBoQZd8/eTZqIt9XZfgdHvkQr/VTMpI2pCocd7QI3z+NBzoaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSGNpHWr7//hhtI61fgAQCGEjCc5UAAAfd8B/U="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "sign",
  "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
  "payload": {
    "tx": "tx_+F01AaEGXfP3k2aiLfV2X4HR75EK/1UzKSNqQqHHe0CN8/jQc6GhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhjaR1q+//4YbSOtX4AEAhhIwnOVAAAFP7TAc"
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
    "tx": "tx_+KcLAfhCuECAQz0Bw8f/K1Q8poLbhIseTwMJO63Nll9DUAgcE7msAVN5eZATZroQfIPfDQvMnntMTV/MUuLNDtzwLqK/gfAKuF/4XTUBoQZd8/eTZqIt9XZfgdHvkQr/VTMpI2pCocd7QI3z+NBzoaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSGNpHWr7//hhtI61fgAQCGEjCc5UAAAeaLIq8="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
  "payload": {
    "tx": "tx_+OkLAfiEuECAQz0Bw8f/K1Q8poLbhIseTwMJO63Nll9DUAgcE7msAVN5eZATZroQfIPfDQvMnntMTV/MUuLNDtzwLqK/gfAKuEDPyVlPLD3thSWyeg0TM7r5acXU4tlKm/FSEtI/aYrLr0WZa+CwO97rUW2qhUlEbM7aEiKEnh48kEu+gmzqv9IBuF/4XTUBoQZd8/eTZqIt9XZfgdHvkQr/VTMpI2pCocd7QI3z+NBzoaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSGNpHWr7//hhtI61fgAQCGEjCc5UAAAd5UzfI="
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

#### responder <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
  "payload": {
    "tx": "tx_+OkLAfiEuECAQz0Bw8f/K1Q8poLbhIseTwMJO63Nll9DUAgcE7msAVN5eZATZroQfIPfDQvMnntMTV/MUuLNDtzwLqK/gfAKuEDPyVlPLD3thSWyeg0TM7r5acXU4tlKm/FSEtI/aYrLr0WZa+CwO97rUW2qhUlEbM7aEiKEnh48kEu+gmzqv9IBuF/4XTUBoQZd8/eTZqIt9XZfgdHvkQr/VTMpI2pCocd7QI3z+NBzoaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSGNpHWr7//hhtI61fgAQCGEjCc5UAAAd5UzfI="
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
