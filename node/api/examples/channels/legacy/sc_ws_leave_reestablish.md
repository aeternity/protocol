
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
    "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwXZ7XjY"
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
    "tx": "tx_+MsLAfhCuED1SbadCPtiUzHdkLlRCB8X0OD8WU9NDlKTNJ0DMQvT93D1C5cpBek8foPRPYJkLGKoa8monKQCpah8VZjxydoIuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/BfUgSuI="
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
    "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwXZ7XjY"
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
    "tx": "tx_+MsLAfhCuEAEz3s7Ehg+3PY5zgp/bQAwoDcaCexAy2ikzaDxqnXsHWZn24UcH0uUz6tA911KeFghSPjQlCr60QmJWzskRR0LuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/BYtcG0k="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "on_chain_tx",
  "channel_id": null,
  "payload": {
    "tx": "tx_+QENCwH4hLhABM97OxIYPtz2Oc4Kf20AMKA3GgnsQMtopM2g8ap17B1mZ9uFHB9LlM+rQPddSnhYIUj40JQq+tEJiVs7JEUdC7hA9Um2nQj7YlMx3ZC5UQgfF9Dg/FlPTQ5SkzSdAzEL0/dw9QuXKQXpPH6D0T2CZCxiqGvJqJykAqWofFWY8cnaCLiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwUG+R1a"
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
    "tx": "tx_+QENCwH4hLhABM97OxIYPtz2Oc4Kf20AMKA3GgnsQMtopM2g8ap17B1mZ9uFHB9LlM+rQPddSnhYIUj40JQq+tEJiVs7JEUdC7hA9Um2nQj7YlMx3ZC5UQgfF9Dg/FlPTQ5SkzSdAzEL0/dw9QuXKQXpPH6D0T2CZCxiqGvJqJykAqWofFWY8cnaCLiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwUG+R1a"
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "state": "tx_+QENCwH4hLhABM97OxIYPtz2Oc4Kf20AMKA3GgnsQMtopM2g8ap17B1mZ9uFHB9LlM+rQPddSnhYIUj40JQq+tEJiVs7JEUdC7hA9Um2nQj7YlMx3ZC5UQgfF9Dg/FlPTQ5SkzSdAzEL0/dw9QuXKQXpPH6D0T2CZCxiqGvJqJykAqWofFWY8cnaCLiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwUG+R1a"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "state": "tx_+QENCwH4hLhABM97OxIYPtz2Oc4Kf20AMKA3GgnsQMtopM2g8ap17B1mZ9uFHB9LlM+rQPddSnhYIUj40JQq+tEJiVs7JEUdC7hA9Um2nQj7YlMx3ZC5UQgfF9Dg/FlPTQ5SkzSdAzEL0/dw9QuXKQXpPH6D0T2CZCxiqGvJqJykAqWofFWY8cnaCLiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwUG+R1a"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "action": "leave"
}
```

#### responder <--- node
```javascript
{
  "action": "leave",
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "state": "tx_+QENCwH4hLhABM97OxIYPtz2Oc4Kf20AMKA3GgnsQMtopM2g8ap17B1mZ9uFHB9LlM+rQPddSnhYIUj40JQq+tEJiVs7JEUdC7hA9Um2nQj7YlMx3ZC5UQgfF9Dg/FlPTQ5SkzSdAzEL0/dw9QuXKQXpPH6D0T2CZCxiqGvJqJykAqWofFWY8cnaCLiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwUG+R1a"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "event": "died"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "leave",
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "state": "tx_+QENCwH4hLhABM97OxIYPtz2Oc4Kf20AMKA3GgnsQMtopM2g8ap17B1mZ9uFHB9LlM+rQPddSnhYIUj40JQq+tEJiVs7JEUdC7hA9Um2nQj7YlMx3ZC5UQgfF9Dg/FlPTQ5SkzSdAzEL0/dw9QuXKQXpPH6D0T2CZCxiqGvJqJykAqWofFWY8cnaCLiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwUG+R1a"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "event": "died"
  },
  "version": 1
}
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&existing_channel_id=ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t&initiator_amount=70000000000000&initiator_id=ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm&lock_period=10&offchain_tx=tx_%2BQENCwH4hLhABM97OxIYPtz2Oc4Kf20AMKA3GgnsQMtopM2g8ap17B1mZ9uFHB9LlM%2BrQPddSnhYIUj40JQq%2BtEJiVs7JEUdC7hA9Um2nQj7YlMx3ZC5UQgfF9Dg%2FFlPTQ5SkzSdAzEL0%2Fdw9QuXKQXpPH6D0T2CZCxiqGvJqJykAqWofFWY8cnaCLiD%2BIEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe%2BrdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D%2F5sB8yCR8WumWh0WxWvwUG%2BR1a&port=12341&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC&role=responder
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&existing_channel_id=ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm&lock_period=10&offchain_tx=tx_%2BQENCwH4hLhABM97OxIYPtz2Oc4Kf20AMKA3GgnsQMtopM2g8ap17B1mZ9uFHB9LlM%2BrQPddSnhYIUj40JQq%2BtEJiVs7JEUdC7hA9Um2nQj7YlMx3ZC5UQgfF9Dg%2FFlPTQ5SkzSdAzEL0%2Fdw9QuXKQXpPH6D0T2CZCxiqGvJqJykAqWofFWY8cnaCLiD%2BIEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe%2BrdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D%2F5sB8yCR8WumWh0WxWvwUG%2BR1a&port=12341&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC&role=initiator
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": null,
  "payload": {
    "event": "channel_reestablished"
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "state": "tx_+QENCwH4hLhABM97OxIYPtz2Oc4Kf20AMKA3GgnsQMtopM2g8ap17B1mZ9uFHB9LlM+rQPddSnhYIUj40JQq+tEJiVs7JEUdC7hA9Um2nQj7YlMx3ZC5UQgfF9Dg/FlPTQ5SkzSdAzEL0/dw9QuXKQXpPH6D0T2CZCxiqGvJqJykAqWofFWY8cnaCLiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwUG+R1a"
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
    "event": "channel_reestablished"
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "state": "tx_+QENCwH4hLhABM97OxIYPtz2Oc4Kf20AMKA3GgnsQMtopM2g8ap17B1mZ9uFHB9LlM+rQPddSnhYIUj40JQq+tEJiVs7JEUdC7hA9Um2nQj7YlMx3ZC5UQgfF9Dg/FlPTQ5SkzSdAzEL0/dw9QuXKQXpPH6D0T2CZCxiqGvJqJykAqWofFWY8cnaCLiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwUG+R1a"
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "tx": "tx_+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4RgGEv0="
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
    "tx": "tx_+N8LAfhCuEAJucXkQXN/tCSLeXjp9g5Em8OrdzF1kjm1UNLjyozxCdlzsizi0RLWYkjSmj3P7inUPM6Nvde4ZLJluwd3b7AOuJf4lTkBoQbY/TE9PmMeWVRJAbe/imvTDDLJq5Tm6nwlHYQdGnB9GgL4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoNUqd4GTOFacRsLar0VqTNSHraQXvmyQrL/MBqX090LhzxWeeQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "tx": "tx_+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4RgGEv0="
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
    "tx": "tx_+N8LAfhCuED01ftyCc1MJl77Q9rkyqrVhfP/AAJG1+iXGW0OLSWB2g9ZJoV8X1j+b5wB/xpCYMdavI1AnIalKIqguQ+uQ9MMuJf4lTkBoQbY/TE9PmMeWVRJAbe/imvTDDLJq5Tm6nwlHYQdGnB9GgL4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoNUqd4GTOFacRsLar0VqTNSHraQXvmyQrL/MBqX090LhJL4cvw=="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "state": "tx_+QEhCwH4hLhACbnF5EFzf7Qki3l46fYORJvDq3cxdZI5tVDS48qM8QnZc7Is4tES1mJI0po9z+4p1DzOjb3XuGSyZbsHd2+wDrhA9NX7cgnNTCZe+0Pa5Mqq1YXz/wACRtfolxltDi0lgdoPWSaFfF9Y/m+cAf8aQmDHWryNQJyGpSiKoLkPrkPTDLiX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4cw1EJo="
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "state": "tx_+QEhCwH4hLhACbnF5EFzf7Qki3l46fYORJvDq3cxdZI5tVDS48qM8QnZc7Is4tES1mJI0po9z+4p1DzOjb3XuGSyZbsHd2+wDrhA9NX7cgnNTCZe+0Pa5Mqq1YXz/wACRtfolxltDi0lgdoPWSaFfF9Y/m+cAf8aQmDHWryNQJyGpSiKoLkPrkPTDLiX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4cw1EJo="
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhACbnF5EFzf7Qki3l46fYORJvDq3cxdZI5tVDS48qM8QnZc7Is4tES1mJI0po9z+4p1DzOjb3XuGSyZbsHd2+wDrhA9NX7cgnNTCZe+0Pa5Mqq1YXz/wACRtfolxltDi0lgdoPWSaFfF9Y/m+cAf8aQmDHWryNQJyGpSiKoLkPrkPTDLiX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4cw1EJo=",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "tx": "tx_+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoD+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv1RUFNY="
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
    "tx": "tx_+N8LAfhCuEB/zTwYY1gQHhWhs49a3cq4y3EXB0bmPoJ1Qdzksu/nS4zKvKkCEKqSvndbTm4NI59NncRvtzZKD/mPDkulOMUDuJf4lTkBoQbY/TE9PmMeWVRJAbe/imvTDDLJq5Tm6nwlHYQdGnB9GgP4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/eQQZsA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "tx": "tx_+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoD+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv1RUFNY="
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
    "tx": "tx_+N8LAfhCuEAjLFqpCxhRPWCdBm5x23jxPH2KjePE066ING9XTjigj4gXSAl/jVcfwJYkj5A6ogilBVYQXsmp2F9d/du2OO4OuJf4lTkBoQbY/TE9PmMeWVRJAbe/imvTDDLJq5Tm6nwlHYQdGnB9GgP4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/1hLXXA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "state": "tx_+QEhCwH4hLhAIyxaqQsYUT1gnQZucdt48Tx9io3jxNOuiDRvV044oI+IF0gJf41XH8CWJI+QOqIIpQVWEF7JqdhfXf3btjjuDrhAf808GGNYEB4VobOPWt3KuMtxFwdG5j6CdUHc5LLv50uMyrypAhCqkr53W05uDSOfTZ3Eb7c2Sg/5jw5LpTjFA7iX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoD+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwftUvg="
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "state": "tx_+QEhCwH4hLhAIyxaqQsYUT1gnQZucdt48Tx9io3jxNOuiDRvV044oI+IF0gJf41XH8CWJI+QOqIIpQVWEF7JqdhfXf3btjjuDrhAf808GGNYEB4VobOPWt3KuMtxFwdG5j6CdUHc5LLv50uMyrypAhCqkr53W05uDSOfTZ3Eb7c2Sg/5jw5LpTjFA7iX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoD+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwftUvg="
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAIyxaqQsYUT1gnQZucdt48Tx9io3jxNOuiDRvV044oI+IF0gJf41XH8CWJI+QOqIIpQVWEF7JqdhfXf3btjjuDrhAf808GGNYEB4VobOPWt3KuMtxFwdG5j6CdUHc5LLv50uMyrypAhCqkr53W05uDSOfTZ3Eb7c2Sg/5jw5LpTjFA7iX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoD+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwftUvg=",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "tx": "tx_+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsTebCVE="
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
    "tx": "tx_+N8LAfhCuEAMj0w2TaI8goBRtWTY1ewHXWMEEDZ3g73h6yod3ATDzmz0qjHF0S/1HEacuy8/mjkYkfuaUL1woDe2fhfkrbUDuJf4lTkBoQbY/TE9PmMeWVRJAbe/imvTDDLJq5Tm6nwlHYQdGnB9GgT4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROx11WAsA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "tx": "tx_+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsTebCVE="
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
    "tx": "tx_+N8LAfhCuEBFD/CHtgTPMH3RW+IAJgmBUNEB2+neXfvN2GjLpQuzWtY3+yuJWX2Dsx1Fc7CnRVtUrTByN2b74cOsTx7j3GkNuJf4lTkBoQbY/TE9PmMeWVRJAbe/imvTDDLJq5Tm6nwlHYQdGnB9GgT4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROx62E20g=="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "state": "tx_+QEhCwH4hLhADI9MNk2iPIKAUbVk2NXsB11jBBA2d4O94esqHdwEw85s9KoxxdEv9RxGnLsvP5o5GJH7mlC9cKA3tn4X5K21A7hARQ/wh7YEzzB90VviACYJgVDRAdvp3l37zdhoy6ULs1rWN/sriVl9g7MdRXOwp0VbVK0wcjdm++HDrE8e49xpDbiX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsfwX0hs="
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "state": "tx_+QEhCwH4hLhADI9MNk2iPIKAUbVk2NXsB11jBBA2d4O94esqHdwEw85s9KoxxdEv9RxGnLsvP5o5GJH7mlC9cKA3tn4X5K21A7hARQ/wh7YEzzB90VviACYJgVDRAdvp3l37zdhoy6ULs1rWN/sriVl9g7MdRXOwp0VbVK0wcjdm++HDrE8e49xpDbiX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsfwX0hs="
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhADI9MNk2iPIKAUbVk2NXsB11jBBA2d4O94esqHdwEw85s9KoxxdEv9RxGnLsvP5o5GJH7mlC9cKA3tn4X5K21A7hARQ/wh7YEzzB90VviACYJgVDRAdvp3l37zdhoy6ULs1rWN/sriVl9g7MdRXOwp0VbVK0wcjdm++HDrE8e49xpDbiX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsfwX0hs=",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "tx": "tx_+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv9/9VMM="
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
    "tx": "tx_+N8LAfhCuEC7TvlAWelk0OX3mchzbHvmHadDZSV0KRipJTL3zdbGT/gRKpKSXFFJjC4Hr3cznHdejfAOcWKdl+v5hvJKvvAEuJf4lTkBoQbY/TE9PmMeWVRJAbe/imvTDDLJq5Tm6nwlHYQdGnB9GgX4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/wG12Ow=="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "tx": "tx_+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv9/9VMM="
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
    "tx": "tx_+N8LAfhCuEBxwijinBGG5VWagSoSy9ddRKq7ttqwKWG5xLSCxC7dw9Nc8x+jOThxc4kl6AKTqpqmHEdduMUNMrzny1csQWgMuJf4lTkBoQbY/TE9PmMeWVRJAbe/imvTDDLJq5Tm6nwlHYQdGnB9GgX4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/cTLNYA=="
  }
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "state": "tx_+QEhCwH4hLhAccIo4pwRhuVVmoEqEsvXXUSqu7basClhucS0gsQu3cPTXPMfozk4cXOJJegCk6qaphxHXbjFDTK858tXLEFoDLhAu075QFnpZNDl95nIc2x75h2nQ2UldCkYqSUy983Wxk/4ESqSklxRSYwuB693M5x3Xo3wDnFinZfr+YbySr7wBLiX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv8j3HnQ="
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "state": "tx_+QEhCwH4hLhAccIo4pwRhuVVmoEqEsvXXUSqu7basClhucS0gsQu3cPTXPMfozk4cXOJJegCk6qaphxHXbjFDTK858tXLEFoDLhAu075QFnpZNDl95nIc2x75h2nQ2UldCkYqSUy983Wxk/4ESqSklxRSYwuB693M5x3Xo3wDnFinZfr+YbySr7wBLiX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv8j3HnQ="
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAccIo4pwRhuVVmoEqEsvXXUSqu7basClhucS0gsQu3cPTXPMfozk4cXOJJegCk6qaphxHXbjFDTK858tXLEFoDLhAu075QFnpZNDl95nIc2x75h2nQ2UldCkYqSUy983Wxk/4ESqSklxRSYwuB693M5x3Xo3wDnFinZfr+YbySr7wBLiX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv8j3HnQ=",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "tx": "tx_+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TscPCptE="
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
    "tx": "tx_+N8LAfhCuEBXfI/zrbOyQ5WZX1y9pFBQwEs+iXF2zR3sIlRJ1m1BBJU5+Q0gi75MGDmNd/O09JMsBE0ezAdil22DFsat8ckGuJf4lTkBoQbY/TE9PmMeWVRJAbe/imvTDDLJq5Tm6nwlHYQdGnB9Ggb4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROx4FONvg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "info",
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "tx": "tx_+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TscPCptE="
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
    "tx": "tx_+N8LAfhCuEAteJX0AAeHc2AMPRYxLc63G35oxZdaBKOQLNSMWiCYwK5DcNbjtEMpQDD0jcj0eM/AY6Ofhe37LLwynRMbVZ0MuJf4lTkBoQbY/TE9PmMeWVRJAbe/imvTDDLJq5Tm6nwlHYQdGnB9Ggb4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROx8Po4WA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "state": "tx_+QEhCwH4hLhALXiV9AAHh3NgDD0WMS3Otxt+aMWXWgSjkCzUjFogmMCuQ3DW47RDKUAw9I3I9HjPwGOjn4Xt+yy8Mp0TG1WdDLhAV3yP862zskOVmV9cvaRQUMBLPolxds0d7CJUSdZtQQSVOfkNIIu+TBg5jXfztPSTLARNHswHYpdtgxbGrfHJBriX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TseQeWHE="
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "action": "update",
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "state": "tx_+QEhCwH4hLhALXiV9AAHh3NgDD0WMS3Otxt+aMWXWgSjkCzUjFogmMCuQ3DW47RDKUAw9I3I9HjPwGOjn4Xt+yy8Mp0TG1WdDLhAV3yP862zskOVmV9cvaRQUMBLPolxds0d7CJUSdZtQQSVOfkNIIu+TBg5jXfztPSTLARNHswHYpdtgxbGrfHJBriX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TseQeWHE="
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
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
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhALXiV9AAHh3NgDD0WMS3Otxt+aMWXWgSjkCzUjFogmMCuQ3DW47RDKUAw9I3I9HjPwGOjn4Xt+yy8Mp0TG1WdDLhAV3yP862zskOVmV9cvaRQUMBLPolxds0d7CJUSdZtQQSVOfkNIIu+TBg5jXfztPSTLARNHswHYpdtgxbGrfHJBriX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TseQeWHE=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJgALDvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAA6duKo"
  },
  "tag": "offchain_state",
  "version": 1
}
```
