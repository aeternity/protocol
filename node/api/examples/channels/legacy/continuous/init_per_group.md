
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
    "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwhG8eVK",
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
    "tx": "tx_+MsLAfhCuEB7d6bDLdM6EEb4/g8c7qd4moKutM0AaYMCCfk6esESeiU7Vtum0S2+EY7tiJCGHC/0+sw3rKgmjywimS9eX9cFuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/COnyKTM="
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
    "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwhG8eVK",
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
    "tx": "tx_+MsLAfhCuEDPD8YwUdRZ4hEX8ttKT0oUMJUL9sQtfKeLJbzLAXYuP4RwU/311Ta+YD03La4uYI42cKaSMp+ybSyi0/nTVHQMuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/CIFZNcM="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": null,
  "payload": {
    "tx": "tx_+QENCwH4hLhAe3emwy3TOhBG+P4PHO6neJqCrrTNAGmDAgn5OnrBEnolO1bbptEtvhGO7YiQhhwv9PrMN6yoJo8sIpkvXl/XBbhAzw/GMFHUWeIRF/LbSk9KFDCVC/bELXyniyW8ywF2Lj+EcFP99dU2vmA9Ny2uLmCONnCmkjKfsm0sotP501R0DLiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwiMpqfr"
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
    "tx": "tx_+QENCwH4hLhAe3emwy3TOhBG+P4PHO6neJqCrrTNAGmDAgn5OnrBEnolO1bbptEtvhGO7YiQhhwv9PrMN6yoJo8sIpkvXl/XBbhAzw/GMFHUWeIRF/LbSk9KFDCVC/bELXyniyW8ywF2Lj+EcFP99dU2vmA9Ny2uLmCONnCmkjKfsm0sotP501R0DLiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwiMpqfr"
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
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
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
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
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
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
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
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
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
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QENCwH4hLhAe3emwy3TOhBG+P4PHO6neJqCrrTNAGmDAgn5OnrBEnolO1bbptEtvhGO7YiQhhwv9PrMN6yoJo8sIpkvXl/XBbhAzw/GMFHUWeIRF/LbSk9KFDCVC/bELXyniyW8ywF2Lj+EcFP99dU2vmA9Ny2uLmCONnCmkjKfsm0sotP501R0DLiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwiMpqfr"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "payload": {
    "state": "tx_+QENCwH4hLhAe3emwy3TOhBG+P4PHO6neJqCrrTNAGmDAgn5OnrBEnolO1bbptEtvhGO7YiQhhwv9PrMN6yoJo8sIpkvXl/XBbhAzw/GMFHUWeIRF/LbSk9KFDCVC/bELXyniyW8ywF2Lj+EcFP99dU2vmA9Ny2uLmCONnCmkjKfsm0sotP501R0DLiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwiMpqfr"
  },
  "version": 1
}
```
