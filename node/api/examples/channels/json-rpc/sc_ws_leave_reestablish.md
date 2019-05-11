
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

#### responder info
> Received an WebSocket opening request

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
      "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvweINQi8",
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
    "tx": "tx_+MsLAfhCuEBipY2tbygMBouPQkJR5bQ1802Gzh0oMmge64J1aGdfivzTZzlkAUpXsRX+YeKFVfOAvJpFoj9JXDYpL7PjvVsCuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/B8kjmVM="
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
      "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvweINQi8",
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
    "tx": "tx_+MsLAfhCuEA/4SI+lcU7zQx2oafDoaRoBik4cK9w/8oEolnkgiJxgEi0D2z3nNkD5FfUM02F6iuVtlgody03dnK8qewVrscOuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/B1yXdmA="
  }
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
      "tx": "tx_+QENCwH4hLhAP+EiPpXFO80MdqGnw6GkaAYpOHCvcP/KBKJZ5IIicYBItA9s95zZA+RX1DNNheorlbZYKHctN3ZyvKnsFa7HDrhAYqWNrW8oDAaLj0JCUeW0NfNNhs4dKDJoHuuCdWhnX4r802c5ZAFKV7EV/mHihVXzgLyaRaI/SVw2KS+z471bAriD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwdz6zEk"
    }
  },
  "version": 1
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
      "tx": "tx_+QENCwH4hLhAP+EiPpXFO80MdqGnw6GkaAYpOHCvcP/KBKJZ5IIicYBItA9s95zZA+RX1DNNheorlbZYKHctN3ZyvKnsFa7HDrhAYqWNrW8oDAaLj0JCUeW0NfNNhs4dKDJoHuuCdWhnX4r802c5ZAFKV7EV/mHihVXzgLyaRaI/SVw2KS+z471bAriD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwdz6zEk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
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

#### initiator <--- node
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
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
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
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder info
> Channel is `open` and ready to use

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "state": "tx_+QENCwH4hLhAP+EiPpXFO80MdqGnw6GkaAYpOHCvcP/KBKJZ5IIicYBItA9s95zZA+RX1DNNheorlbZYKHctN3ZyvKnsFa7HDrhAYqWNrW8oDAaLj0JCUeW0NfNNhs4dKDJoHuuCdWhnX4r802c5ZAFKV7EV/mHihVXzgLyaRaI/SVw2KS+z471bAriD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwdz6zEk"
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
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "state": "tx_+QENCwH4hLhAP+EiPpXFO80MdqGnw6GkaAYpOHCvcP/KBKJZ5IIicYBItA9s95zZA+RX1DNNheorlbZYKHctN3ZyvKnsFa7HDrhAYqWNrW8oDAaLj0JCUeW0NfNNhs4dKDJoHuuCdWhnX4r802c5ZAFKV7EV/mHihVXzgLyaRaI/SVw2KS+z471bAriD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwdz6zEk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "state": "tx_+QENCwH4hLhAP+EiPpXFO80MdqGnw6GkaAYpOHCvcP/KBKJZ5IIicYBItA9s95zZA+RX1DNNheorlbZYKHctN3ZyvKnsFa7HDrhAYqWNrW8oDAaLj0JCUeW0NfNNhs4dKDJoHuuCdWhnX4r802c5ZAFKV7EV/mHihVXzgLyaRaI/SVw2KS+z471bAriD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwdz6zEk"
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
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "state": "tx_+QENCwH4hLhAP+EiPpXFO80MdqGnw6GkaAYpOHCvcP/KBKJZ5IIicYBItA9s95zZA+RX1DNNheorlbZYKHctN3ZyvKnsFa7HDrhAYqWNrW8oDAaLj0JCUeW0NfNNhs4dKDJoHuuCdWhnX4r802c5ZAFKV7EV/mHihVXzgLyaRaI/SVw2KS+z471bAriD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwdz6zEk"
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
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR&offchain_tx=tx_%2BQENCwH4hLhAP%2BEiPpXFO80MdqGnw6GkaAYpOHCvcP%2FKBKJZ5IIicYBItA9s95zZA%2BRX1DNNheorlbZYKHctN3ZyvKnsFa7HDrhAYqWNrW8oDAaLj0JCUeW0NfNNhs4dKDJoHuuCdWhnX4r802c5ZAFKV7EV%2FmHihVXzgLyaRaI%2FSVw2KS%2Bz471bAriD%2BIEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe%2BrdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D%2F5sB8yCR8WumWh0WxWvwdz6zEk&port=12341&protocol=json-rpc&role=responder
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR&host=localhost&offchain_tx=tx_%2BQENCwH4hLhAP%2BEiPpXFO80MdqGnw6GkaAYpOHCvcP%2FKBKJZ5IIicYBItA9s95zZA%2BRX1DNNheorlbZYKHctN3ZyvKnsFa7HDrhAYqWNrW8oDAaLj0JCUeW0NfNNhs4dKDJoHuuCdWhnX4r802c5ZAFKV7EV%2FmHihVXzgLyaRaI%2FSVw2KS%2Bz471bAriD%2BIEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe%2BrdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D%2F5sB8yCR8WumWh0WxWvwdz6zEk&port=12341&protocol=json-rpc&role=initiator
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_reestablished"
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
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "state": "tx_+QENCwH4hLhAP+EiPpXFO80MdqGnw6GkaAYpOHCvcP/KBKJZ5IIicYBItA9s95zZA+RX1DNNheorlbZYKHctN3ZyvKnsFa7HDrhAYqWNrW8oDAaLj0JCUeW0NfNNhs4dKDJoHuuCdWhnX4r802c5ZAFKV7EV/mHihVXzgLyaRaI/SVw2KS+z471bAriD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwdz6zEk"
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
      "event": "channel_reestablished"
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
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Channel is `open` and ready to use

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "state": "tx_+QENCwH4hLhAP+EiPpXFO80MdqGnw6GkaAYpOHCvcP/KBKJZ5IIicYBItA9s95zZA+RX1DNNheorlbZYKHctN3ZyvKnsFa7HDrhAYqWNrW8oDAaLj0JCUeW0NfNNhs4dKDJoHuuCdWhnX4r802c5ZAFKV7EV/mHihVXzgLyaRaI/SVw2KS+z471bAriD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwdz6zEk"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423453,
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
  "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
  "id": -576460752303423453,
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
  "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
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
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "tx": "tx_+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4YToyHU=",
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
    "tx": "tx_+N8LAfhCuEBZrh+BcqJSCHpLVIBGyHjEPV0GygAWoCvMPlmqQU4R+7DGS6Q2ouwoKjABJ2LSeWZ0k3SXDotsrTVVw36ImmwFuJf4lTkBoQZx0m3B8AcLUeUEcEtDtZiNRsP/KZGjsHB0GqdPQT6DBQL4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoNUqd4GTOFacRsLar0VqTNSHraQXvmyQrL/MBqX090LhGiUmdQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
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
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "tx": "tx_+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4YToyHU=",
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
    "tx": "tx_+N8LAfhCuEDbF0d5bfQkV0iMm4WLG61n6x3zDr4r56B3EExTTB21cfUutun2etraPZYbbf7ow2BQHOmcIij3PaUCzx/hfN8NuJf4lTkBoQZx0m3B8AcLUeUEcEtDtZiNRsP/KZGjsHB0GqdPQT6DBQL4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoNUqd4GTOFacRsLar0VqTNSHraQXvmyQrL/MBqX090LhfMDR5w=="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "state": "tx_+QEhCwH4hLhAWa4fgXKiUgh6S1SARsh4xD1dBsoAFqArzD5ZqkFOEfuwxkukNqLsKCowASdi0nlmdJN0lw6LbK01VcN+iJpsBbhA2xdHeW30JFdIjJuFixutZ+sd8w6+K+egdxBMU0wdtXH1Lrbp9nra2j2WG23+6MNgUBzpnCIo9z2lAs8f4XzfDbiX+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4Sdxwa0="
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
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "state": "tx_+QEhCwH4hLhAWa4fgXKiUgh6S1SARsh4xD1dBsoAFqArzD5ZqkFOEfuwxkukNqLsKCowASdi0nlmdJN0lw6LbK01VcN+iJpsBbhA2xdHeW30JFdIjJuFixutZ+sd8w6+K+egdxBMU0wdtXH1Lrbp9nra2j2WG23+6MNgUBzpnCIo9z2lAs8f4XzfDbiX+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4Sdxwa0="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423452,
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
  "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
  "id": -576460752303423452,
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
  "id": -576460752303423451,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
  "id": -576460752303423451,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAWa4fgXKiUgh6S1SARsh4xD1dBsoAFqArzD5ZqkFOEfuwxkukNqLsKCowASdi0nlmdJN0lw6LbK01VcN+iJpsBbhA2xdHeW30JFdIjJuFixutZ+sd8w6+K+egdxBMU0wdtXH1Lrbp9nra2j2WG23+6MNgUBzpnCIo9z2lAs8f4XzfDbiX+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4Sdxwa0=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJf/rDvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAJXk16b"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423450,
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
  "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
  "id": -576460752303423450,
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
  "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
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
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "tx": "tx_+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUD+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv1AAv/s=",
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
    "tx": "tx_+N8LAfhCuEAErjSw6DlYziM0GZyJNq8O8BVfjkp3bAxRWrzwDN6Dt0YEVF0ME/FTDUg/Dd4BKy5pl+aTLPl+HQjZcgesnr0HuJf4lTkBoQZx0m3B8AcLUeUEcEtDtZiNRsP/KZGjsHB0GqdPQT6DBQP4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/27t9ag=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
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
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "tx": "tx_+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUD+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv1AAv/s=",
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
    "tx": "tx_+N8LAfhCuECpwvy7JoNBXn9lD4O3xNTGoLsys8TaVBexY/f4JCfF2y2j/Jcd2bVx71r1Fut5YUaYpnPOshwon6Hsx/m+t+YNuJf4lTkBoQZx0m3B8AcLUeUEcEtDtZiNRsP/KZGjsHB0GqdPQT6DBQP4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/ZpiN8Q=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "state": "tx_+QEhCwH4hLhABK40sOg5WM4jNBmciTavDvAVX45Kd2wMUVq88Azeg7dGBFRdDBPxUw1IPw3eASsuaZfmkyz5fh0I2XIHrJ69B7hAqcL8uyaDQV5/ZQ+Dt8TUxqC7MrPE2lQXsWP3+CQnxdsto/yXHdm1ce9a9RbreWFGmKZzzrIcKJ+h7Mf5vrfmDbiX+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUD+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv3/wh68="
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
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "state": "tx_+QEhCwH4hLhABK40sOg5WM4jNBmciTavDvAVX45Kd2wMUVq88Azeg7dGBFRdDBPxUw1IPw3eASsuaZfmkyz5fh0I2XIHrJ69B7hAqcL8uyaDQV5/ZQ+Dt8TUxqC7MrPE2lQXsWP3+CQnxdsto/yXHdm1ce9a9RbreWFGmKZzzrIcKJ+h7Mf5vrfmDbiX+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUD+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv3/wh68="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423449,
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
  "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
  "id": -576460752303423449,
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
  "id": -576460752303423448,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
  "id": -576460752303423448,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhABK40sOg5WM4jNBmciTavDvAVX45Kd2wMUVq88Azeg7dGBFRdDBPxUw1IPw3eASsuaZfmkyz5fh0I2XIHrJ69B7hAqcL8uyaDQV5/ZQ+Dt8TUxqC7MrPE2lQXsWP3+CQnxdsto/yXHdm1ce9a9RbreWFGmKZzzrIcKJ+h7Mf5vrfmDbiX+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUD+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv3/wh68=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJf/7DvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAFkGvNa"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423447,
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
  "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
  "id": -576460752303423447,
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
  "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
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
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "tx": "tx_+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsflKXeU=",
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
    "tx": "tx_+N8LAfhCuEAat1GZ/MibT8asyJQ96pWP5MXxXoXrVyT7AjiiNqKatlW+jZjIrl63tUeGW4Cls1XtDVxv3LDjCY71VHHqL5EDuJf4lTkBoQZx0m3B8AcLUeUEcEtDtZiNRsP/KZGjsHB0GqdPQT6DBQT4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROxkRB4cg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
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
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "tx": "tx_+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsflKXeU=",
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
    "tx": "tx_+N8LAfhCuEBLCDgxZ5Dnty2fSPB8IXrcYPioMUPwOvBjQgrjARVtZbVVH4bID1dMm3+LjTidUO63AbZdDCFnF2MvkfPnq6YKuJf4lTkBoQZx0m3B8AcLUeUEcEtDtZiNRsP/KZGjsHB0GqdPQT6DBQT4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROxW/d1EQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "state": "tx_+QEhCwH4hLhAGrdRmfzIm0/GrMiUPeqVj+TF8V6F61ck+wI4ojaimrZVvo2YyK5et7VHhluApbNV7Q1cb9yw4wmO9VRx6i+RA7hASwg4MWeQ57ctn0jwfCF63GD4qDFD8DrwY0IK4wEVbWW1VR+GyA9XTJt/i404nVDutwG2XQwhZxdjL5Hz56umCriX+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsUw51bA="
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
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "state": "tx_+QEhCwH4hLhAGrdRmfzIm0/GrMiUPeqVj+TF8V6F61ck+wI4ojaimrZVvo2YyK5et7VHhluApbNV7Q1cb9yw4wmO9VRx6i+RA7hASwg4MWeQ57ctn0jwfCF63GD4qDFD8DrwY0IK4wEVbWW1VR+GyA9XTJt/i404nVDutwG2XQwhZxdjL5Hz56umCriX+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsUw51bA="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423446,
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
  "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
  "id": -576460752303423446,
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
  "id": -576460752303423445,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
  "id": -576460752303423445,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAGrdRmfzIm0/GrMiUPeqVj+TF8V6F61ck+wI4ojaimrZVvo2YyK5et7VHhluApbNV7Q1cb9yw4wmO9VRx6i+RA7hASwg4MWeQ57ctn0jwfCF63GD4qDFD8DrwY0IK4wEVbWW1VR+GyA9XTJt/i404nVDutwG2XQwhZxdjL5Hz56umCriX+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsUw51bA=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJgALDvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAA6duKo"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423444,
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
  "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
  "id": -576460752303423444,
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
  "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
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
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "tx": "tx_+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwG7lcs=",
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
    "tx": "tx_+N8LAfhCuEA6D+STqHA+oFyVHNFDB+j7518uptcGZSCuftcC8AZVwqQydGhgkTgyGXhMIujNNILs6E9ZHyyfuxyWKEZgQVADuJf4lTkBoQZx0m3B8AcLUeUEcEtDtZiNRsP/KZGjsHB0GqdPQT6DBQX4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/v4JRjQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
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
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "tx": "tx_+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwG7lcs=",
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
    "tx": "tx_+N8LAfhCuEAwF9meXlLbDHjLYjIkaOqnatM+wTa9hgxxbbe//FYOWvNJ5vR5frJ/LZP9wCHyquOixw+b3Pl9jgBKn/urbcsKuJf4lTkBoQZx0m3B8AcLUeUEcEtDtZiNRsP/KZGjsHB0GqdPQT6DBQX4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/1PM8Xg=="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "state": "tx_+QEhCwH4hLhAMBfZnl5S2wx4y2IyJGjqp2rTPsE2vYYMcW23v/xWDlrzSeb0eX6yfy2T/cAh8qrjoscPm9z5fY4ASp/7q23LCrhAOg/kk6hwPqBclRzRQwfo++dfLqbXBmUgrn7XAvAGVcKkMnRoYJE4Mhl4TCLozTSC7OhPWR8sn7sclihGYEFQA7iX+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv6kynaA="
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
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "state": "tx_+QEhCwH4hLhAMBfZnl5S2wx4y2IyJGjqp2rTPsE2vYYMcW23v/xWDlrzSeb0eX6yfy2T/cAh8qrjoscPm9z5fY4ASp/7q23LCrhAOg/kk6hwPqBclRzRQwfo++dfLqbXBmUgrn7XAvAGVcKkMnRoYJE4Mhl4TCLozTSC7OhPWR8sn7sclihGYEFQA7iX+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv6kynaA="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423443,
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
  "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
  "id": -576460752303423443,
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
  "id": -576460752303423442,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
  "id": -576460752303423442,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAMBfZnl5S2wx4y2IyJGjqp2rTPsE2vYYMcW23v/xWDlrzSeb0eX6yfy2T/cAh8qrjoscPm9z5fY4ASp/7q23LCrhAOg/kk6hwPqBclRzRQwfo++dfLqbXBmUgrn7XAvAGVcKkMnRoYJE4Mhl4TCLozTSC7OhPWR8sn7sclihGYEFQA7iX+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv6kynaA=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJf/7DvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAFkGvNa"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423441,
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
  "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
  "id": -576460752303423441,
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
  "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
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
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "tx": "tx_+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsSI8kkc=",
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
    "tx": "tx_+N8LAfhCuECCAOzmN/+ahfyRqgeVdb39f34Aj+PXHp5xJB/6r9DPzfTkU6WUqHbp4h13cF+5Pr3NkkYkTS2DWNaFTwaCMW0LuJf4lTkBoQZx0m3B8AcLUeUEcEtDtZiNRsP/KZGjsHB0GqdPQT6DBQb4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROx70wM4Q=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
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
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "tx": "tx_+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsSI8kkc=",
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
    "tx": "tx_+N8LAfhCuEDSRTqs0mPI0qwQ9PdqzsLzFnZemfvdqkrv0n+4XrwqSPRH2bI982FUUP37w15xbHbyEE60nnrW4g1N4K2uWqcEuJf4lTkBoQZx0m3B8AcLUeUEcEtDtZiNRsP/KZGjsHB0GqdPQT6DBQb4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROxGB10nA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "state": "tx_+QEhCwH4hLhAggDs5jf/moX8kaoHlXW9/X9+AI/j1x6ecSQf+q/Qz8305FOllKh26eIdd3BfuT69zZJGJE0tg1jWhU8GgjFtC7hA0kU6rNJjyNKsEPT3as7C8xZ2Xpn73apK79J/uF68Kkj0R9myPfNhVFD9+8NecWx28hBOtJ561uINTeCtrlqnBLiX+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsdwJN4Y="
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
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "state": "tx_+QEhCwH4hLhAggDs5jf/moX8kaoHlXW9/X9+AI/j1x6ecSQf+q/Qz8305FOllKh26eIdd3BfuT69zZJGJE0tg1jWhU8GgjFtC7hA0kU6rNJjyNKsEPT3as7C8xZ2Xpn73apK79J/uF68Kkj0R9myPfNhVFD9+8NecWx28hBOtJ561uINTeCtrlqnBLiX+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsdwJN4Y="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423440,
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
  "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
  "id": -576460752303423440,
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
  "id": -576460752303423439,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
  "id": -576460752303423439,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAggDs5jf/moX8kaoHlXW9/X9+AI/j1x6ecSQf+q/Qz8305FOllKh26eIdd3BfuT69zZJGJE0tg1jWhU8GgjFtC7hA0kU6rNJjyNKsEPT3as7C8xZ2Xpn73apK79J/uF68Kkj0R9myPfNhVFD9+8NecWx28hBOtJ561uINTeCtrlqnBLiX+JU5AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwUG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsdwJN4Y=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJgALDvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAA6duKo"
  },
  "version": 1
}
```
