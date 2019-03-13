
#### initiator opens a WebSocket connection (2019-03-18 14:06:27.681)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC&role=initiator
```

#### responder opens a WebSocket connection (2019-03-18 14:06:27.704)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC&role=responder
```

#### responder <--- node (2019-03-18 14:06:28.677)
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

#### initiator <--- node (2019-03-18 14:06:28.683)
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

#### initiator <--- node (2019-03-18 14:06:28.689)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwXZ7XjY"
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:06:28.792)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_+MsLAfhCuED1SbadCPtiUzHdkLlRCB8X0OD8WU9NDlKTNJ0DMQvT93D1C5cpBek8foPRPYJkLGKoa8monKQCpah8VZjxydoIuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/BfUgSuI="
  }
}
```

#### responder <--- node (2019-03-18 14:06:28.816)
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

#### responder <--- node (2019-03-18 14:06:28.817)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwXZ7XjY"
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-18 14:06:28.818)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_+MsLAfhCuEAEz3s7Ehg+3PY5zgp/bQAwoDcaCexAy2ikzaDxqnXsHWZn24UcH0uUz6tA911KeFghSPjQlCr60QmJWzskRR0LuIP4gTIBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoY/qiUiYAChAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EhiRhOcqAAAIKAIYSMJzlQADAoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/BYtcG0k="
  }
}
```

#### initiator <--- node (2019-03-18 14:06:28.844)
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

#### responder <--- node (2019-03-18 14:06:28.844)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+QENCwH4hLhABM97OxIYPtz2Oc4Kf20AMKA3GgnsQMtopM2g8ap17B1mZ9uFHB9LlM+rQPddSnhYIUj40JQq+tEJiVs7JEUdC7hA9Um2nQj7YlMx3ZC5UQgfF9Dg/FlPTQ5SkzSdAzEL0/dw9QuXKQXpPH6D0T2CZCxiqGvJqJykAqWofFWY8cnaCLiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwUG+R1a"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:06:28.845)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+QENCwH4hLhABM97OxIYPtz2Oc4Kf20AMKA3GgnsQMtopM2g8ap17B1mZ9uFHB9LlM+rQPddSnhYIUj40JQq+tEJiVs7JEUdC7hA9Um2nQj7YlMx3ZC5UQgfF9Dg/FlPTQ5SkzSdAzEL0/dw9QuXKQXpPH6D0T2CZCxiqGvJqJykAqWofFWY8cnaCLiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwUG+R1a"
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:06:29.744)
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

#### initiator <--- node (2019-03-18 14:06:29.762)
```javascript
{
  "channel_id": null,
  "id": -576460752303423470,
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

#### initiator <--- node (2019-03-18 14:06:30.850)
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

#### responder <--- node (2019-03-18 14:06:30.854)
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

#### responder <--- node (2019-03-18 14:06:30.858)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:06:30.859)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:06:30.876)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:06:30.877)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "state": "tx_+QENCwH4hLhABM97OxIYPtz2Oc4Kf20AMKA3GgnsQMtopM2g8ap17B1mZ9uFHB9LlM+rQPddSnhYIUj40JQq+tEJiVs7JEUdC7hA9Um2nQj7YlMx3ZC5UQgfF9Dg/FlPTQ5SkzSdAzEL0/dw9QuXKQXpPH6D0T2CZCxiqGvJqJykAqWofFWY8cnaCLiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwUG+R1a"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:06:30.886)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:06:30.896)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "state": "tx_+QENCwH4hLhABM97OxIYPtz2Oc4Kf20AMKA3GgnsQMtopM2g8ap17B1mZ9uFHB9LlM+rQPddSnhYIUj40JQq+tEJiVs7JEUdC7hA9Um2nQj7YlMx3ZC5UQgfF9Dg/FlPTQ5SkzSdAzEL0/dw9QuXKQXpPH6D0T2CZCxiqGvJqJykAqWofFWY8cnaCLiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwUG+R1a"
    }
  },
  "version": 1
}
```

#### initiator: (2019-03-18 14:06:32.200)
> Funding has been confirmed locally on-chain

#### responder: (2019-03-18 14:06:32.200)
> Funding has been confirmed locally on-chain

#### initiator: (2019-03-18 14:06:32.200)
> Funding has been confirmed on-chain by other party

#### responder: (2019-03-18 14:06:32.200)
> Funding has been confirmed on-chain by other party

#### initiator: (2019-03-18 14:06:32.200)
> Channel is `open` and ready to use

#### responder: (2019-03-18 14:06:32.200)
> Channel is `open` and ready to use

#### initiator ---> node (2019-03-18 14:06:32.201)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {}
}
```

#### responder <--- node (2019-03-18 14:06:32.241)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "state": "tx_+QENCwH4hLhABM97OxIYPtz2Oc4Kf20AMKA3GgnsQMtopM2g8ap17B1mZ9uFHB9LlM+rQPddSnhYIUj40JQq+tEJiVs7JEUdC7hA9Um2nQj7YlMx3ZC5UQgfF9Dg/FlPTQ5SkzSdAzEL0/dw9QuXKQXpPH6D0T2CZCxiqGvJqJykAqWofFWY8cnaCLiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwUG+R1a"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:06:32.242)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:06:32.255)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "state": "tx_+QENCwH4hLhABM97OxIYPtz2Oc4Kf20AMKA3GgnsQMtopM2g8ap17B1mZ9uFHB9LlM+rQPddSnhYIUj40JQq+tEJiVs7JEUdC7hA9Um2nQj7YlMx3ZC5UQgfF9Dg/FlPTQ5SkzSdAzEL0/dw9QuXKQXpPH6D0T2CZCxiqGvJqJykAqWofFWY8cnaCLiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwUG+R1a"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:06:32.256)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder opens a WebSocket connection (2019-03-18 14:06:32.304)
```
ws://localhost:3014/channel?channel_reserve=2&existing_channel_id=ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t&initiator_amount=70000000000000&initiator_id=ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm&lock_period=10&offchain_tx=tx_%2BQENCwH4hLhABM97OxIYPtz2Oc4Kf20AMKA3GgnsQMtopM2g8ap17B1mZ9uFHB9LlM%2BrQPddSnhYIUj40JQq%2BtEJiVs7JEUdC7hA9Um2nQj7YlMx3ZC5UQgfF9Dg%2FFlPTQ5SkzSdAzEL0%2Fdw9QuXKQXpPH6D0T2CZCxiqGvJqJykAqWofFWY8cnaCLiD%2BIEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe%2BrdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D%2F5sB8yCR8WumWh0WxWvwUG%2BR1a&port=12341&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC&role=responder
```

#### initiator opens a WebSocket connection (2019-03-18 14:06:32.325)
```
ws://localhost:3014/channel?channel_reserve=2&existing_channel_id=ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm&lock_period=10&offchain_tx=tx_%2BQENCwH4hLhABM97OxIYPtz2Oc4Kf20AMKA3GgnsQMtopM2g8ap17B1mZ9uFHB9LlM%2BrQPddSnhYIUj40JQq%2BtEJiVs7JEUdC7hA9Um2nQj7YlMx3ZC5UQgfF9Dg%2FFlPTQ5SkzSdAzEL0%2Fdw9QuXKQXpPH6D0T2CZCxiqGvJqJykAqWofFWY8cnaCLiD%2BIEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe%2BrdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D%2F5sB8yCR8WumWh0WxWvwUG%2BR1a&port=12341&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC&role=initiator
```

#### responder <--- node (2019-03-18 14:06:32.345)
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

#### responder <--- node (2019-03-18 14:06:32.347)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:06:32.349)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "state": "tx_+QENCwH4hLhABM97OxIYPtz2Oc4Kf20AMKA3GgnsQMtopM2g8ap17B1mZ9uFHB9LlM+rQPddSnhYIUj40JQq+tEJiVs7JEUdC7hA9Um2nQj7YlMx3ZC5UQgfF9Dg/FlPTQ5SkzSdAzEL0/dw9QuXKQXpPH6D0T2CZCxiqGvJqJykAqWofFWY8cnaCLiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwUG+R1a"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:06:32.351)
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

#### initiator <--- node (2019-03-18 14:06:32.353)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:06:32.354)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "state": "tx_+QENCwH4hLhABM97OxIYPtz2Oc4Kf20AMKA3GgnsQMtopM2g8ap17B1mZ9uFHB9LlM+rQPddSnhYIUj40JQq+tEJiVs7JEUdC7hA9Um2nQj7YlMx3ZC5UQgfF9Dg/FlPTQ5SkzSdAzEL0/dw9QuXKQXpPH6D0T2CZCxiqGvJqJykAqWofFWY8cnaCLiD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwUG+R1a"
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:06:32.355)
```javascript
{
  "id": -576460752303423469,
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

#### initiator <--- node (2019-03-18 14:06:32.360)
```javascript
{
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "id": -576460752303423469,
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

#### initiator ---> node (2019-03-18 14:06:32.361)
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

#### initiator <--- node (2019-03-18 14:06:32.376)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "tx": "tx_+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4RgGEv0="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:06:32.377)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuEAJucXkQXN/tCSLeXjp9g5Em8OrdzF1kjm1UNLjyozxCdlzsizi0RLWYkjSmj3P7inUPM6Nvde4ZLJluwd3b7AOuJf4lTkBoQbY/TE9PmMeWVRJAbe/imvTDDLJq5Tm6nwlHYQdGnB9GgL4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoNUqd4GTOFacRsLar0VqTNSHraQXvmyQrL/MBqX090LhzxWeeQ=="
  }
}
```

#### responder <--- node (2019-03-18 14:06:32.430)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:06:32.433)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "tx": "tx_+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4RgGEv0="
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-18 14:06:32.434)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+N8LAfhCuED01ftyCc1MJl77Q9rkyqrVhfP/AAJG1+iXGW0OLSWB2g9ZJoV8X1j+b5wB/xpCYMdavI1AnIalKIqguQ+uQ9MMuJf4lTkBoQbY/TE9PmMeWVRJAbe/imvTDDLJq5Tm6nwlHYQdGnB9GgL4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoNUqd4GTOFacRsLar0VqTNSHraQXvmyQrL/MBqX090LhJL4cvw=="
  }
}
```

#### responder <--- node (2019-03-18 14:06:32.465)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "state": "tx_+QEhCwH4hLhACbnF5EFzf7Qki3l46fYORJvDq3cxdZI5tVDS48qM8QnZc7Is4tES1mJI0po9z+4p1DzOjb3XuGSyZbsHd2+wDrhA9NX7cgnNTCZe+0Pa5Mqq1YXz/wACRtfolxltDi0lgdoPWSaFfF9Y/m+cAf8aQmDHWryNQJyGpSiKoLkPrkPTDLiX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4cw1EJo="
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:06:32.490)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "state": "tx_+QEhCwH4hLhACbnF5EFzf7Qki3l46fYORJvDq3cxdZI5tVDS48qM8QnZc7Is4tES1mJI0po9z+4p1DzOjb3XuGSyZbsHd2+wDrhA9NX7cgnNTCZe+0Pa5Mqq1YXz/wACRtfolxltDi0lgdoPWSaFfF9Y/m+cAf8aQmDHWryNQJyGpSiKoLkPrkPTDLiX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4cw1EJo="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:06:32.506)
```javascript
{
  "id": -576460752303423468,
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

#### initiator <--- node (2019-03-18 14:06:32.512)
```javascript
{
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "id": -576460752303423468,
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

#### initiator ---> node (2019-03-18 14:06:32.513)
```javascript
{
  "id": -576460752303423467,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node (2019-03-18 14:06:32.518)
```javascript
{
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "id": -576460752303423467,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhACbnF5EFzf7Qki3l46fYORJvDq3cxdZI5tVDS48qM8QnZc7Is4tES1mJI0po9z+4p1DzOjb3XuGSyZbsHd2+wDrhA9NX7cgnNTCZe+0Pa5Mqq1YXz/wACRtfolxltDi0lgdoPWSaFfF9Y/m+cAf8aQmDHWryNQJyGpSiKoLkPrkPTDLiX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4cw1EJo=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJf/rDvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAJXk16b"
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:06:32.526)
```javascript
{
  "id": -576460752303423466,
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

#### initiator <--- node (2019-03-18 14:06:32.531)
```javascript
{
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "id": -576460752303423466,
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

#### responder ---> node (2019-03-18 14:06:32.532)
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

#### responder <--- node (2019-03-18 14:06:32.547)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "tx": "tx_+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoD+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv1RUFNY="
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-18 14:06:32.548)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuEB/zTwYY1gQHhWhs49a3cq4y3EXB0bmPoJ1Qdzksu/nS4zKvKkCEKqSvndbTm4NI59NncRvtzZKD/mPDkulOMUDuJf4lTkBoQbY/TE9PmMeWVRJAbe/imvTDDLJq5Tm6nwlHYQdGnB9GgP4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/eQQZsA=="
  }
}
```

#### initiator <--- node (2019-03-18 14:06:32.601)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:06:32.602)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "tx": "tx_+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoD+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv1RUFNY="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:06:32.604)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+N8LAfhCuEAjLFqpCxhRPWCdBm5x23jxPH2KjePE066ING9XTjigj4gXSAl/jVcfwJYkj5A6ogilBVYQXsmp2F9d/du2OO4OuJf4lTkBoQbY/TE9PmMeWVRJAbe/imvTDDLJq5Tm6nwlHYQdGnB9GgP4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/1hLXXA=="
  }
}
```

#### initiator <--- node (2019-03-18 14:06:32.656)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "state": "tx_+QEhCwH4hLhAIyxaqQsYUT1gnQZucdt48Tx9io3jxNOuiDRvV044oI+IF0gJf41XH8CWJI+QOqIIpQVWEF7JqdhfXf3btjjuDrhAf808GGNYEB4VobOPWt3KuMtxFwdG5j6CdUHc5LLv50uMyrypAhCqkr53W05uDSOfTZ3Eb7c2Sg/5jw5LpTjFA7iX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoD+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwftUvg="
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:06:32.669)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "state": "tx_+QEhCwH4hLhAIyxaqQsYUT1gnQZucdt48Tx9io3jxNOuiDRvV044oI+IF0gJf41XH8CWJI+QOqIIpQVWEF7JqdhfXf3btjjuDrhAf808GGNYEB4VobOPWt3KuMtxFwdG5j6CdUHc5LLv50uMyrypAhCqkr53W05uDSOfTZ3Eb7c2Sg/5jw5LpTjFA7iX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoD+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwftUvg="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:06:32.684)
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

#### initiator <--- node (2019-03-18 14:06:32.689)
```javascript
{
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
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

#### initiator ---> node (2019-03-18 14:06:32.690)
```javascript
{
  "id": -576460752303423464,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node (2019-03-18 14:06:32.698)
```javascript
{
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "id": -576460752303423464,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAIyxaqQsYUT1gnQZucdt48Tx9io3jxNOuiDRvV044oI+IF0gJf41XH8CWJI+QOqIIpQVWEF7JqdhfXf3btjjuDrhAf808GGNYEB4VobOPWt3KuMtxFwdG5j6CdUHc5LLv50uMyrypAhCqkr53W05uDSOfTZ3Eb7c2Sg/5jw5LpTjFA7iX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoD+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwftUvg=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJf/7DvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAFkGvNa"
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:06:32.704)
```javascript
{
  "id": -576460752303423463,
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

#### initiator <--- node (2019-03-18 14:06:32.710)
```javascript
{
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "id": -576460752303423463,
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

#### responder ---> node (2019-03-18 14:06:32.710)
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

#### responder <--- node (2019-03-18 14:06:32.725)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "tx": "tx_+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsTebCVE="
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-18 14:06:32.726)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuEAMj0w2TaI8goBRtWTY1ewHXWMEEDZ3g73h6yod3ATDzmz0qjHF0S/1HEacuy8/mjkYkfuaUL1woDe2fhfkrbUDuJf4lTkBoQbY/TE9PmMeWVRJAbe/imvTDDLJq5Tm6nwlHYQdGnB9GgT4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROx11WAsA=="
  }
}
```

#### initiator <--- node (2019-03-18 14:06:32.777)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:06:32.778)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "tx": "tx_+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsTebCVE="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:06:32.779)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+N8LAfhCuEBFD/CHtgTPMH3RW+IAJgmBUNEB2+neXfvN2GjLpQuzWtY3+yuJWX2Dsx1Fc7CnRVtUrTByN2b74cOsTx7j3GkNuJf4lTkBoQbY/TE9PmMeWVRJAbe/imvTDDLJq5Tm6nwlHYQdGnB9GgT4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROx62E20g=="
  }
}
```

#### initiator <--- node (2019-03-18 14:06:32.808)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "state": "tx_+QEhCwH4hLhADI9MNk2iPIKAUbVk2NXsB11jBBA2d4O94esqHdwEw85s9KoxxdEv9RxGnLsvP5o5GJH7mlC9cKA3tn4X5K21A7hARQ/wh7YEzzB90VviACYJgVDRAdvp3l37zdhoy6ULs1rWN/sriVl9g7MdRXOwp0VbVK0wcjdm++HDrE8e49xpDbiX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsfwX0hs="
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:06:32.827)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "state": "tx_+QEhCwH4hLhADI9MNk2iPIKAUbVk2NXsB11jBBA2d4O94esqHdwEw85s9KoxxdEv9RxGnLsvP5o5GJH7mlC9cKA3tn4X5K21A7hARQ/wh7YEzzB90VviACYJgVDRAdvp3l37zdhoy6ULs1rWN/sriVl9g7MdRXOwp0VbVK0wcjdm++HDrE8e49xpDbiX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsfwX0hs="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:06:32.841)
```javascript
{
  "id": -576460752303423462,
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

#### initiator <--- node (2019-03-18 14:06:32.847)
```javascript
{
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "id": -576460752303423462,
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

#### initiator ---> node (2019-03-18 14:06:32.848)
```javascript
{
  "id": -576460752303423461,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node (2019-03-18 14:06:32.854)
```javascript
{
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "id": -576460752303423461,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhADI9MNk2iPIKAUbVk2NXsB11jBBA2d4O94esqHdwEw85s9KoxxdEv9RxGnLsvP5o5GJH7mlC9cKA3tn4X5K21A7hARQ/wh7YEzzB90VviACYJgVDRAdvp3l37zdhoy6ULs1rWN/sriVl9g7MdRXOwp0VbVK0wcjdm++HDrE8e49xpDbiX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoE+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TsfwX0hs=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJgALDvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAA6duKo"
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:06:32.860)
```javascript
{
  "id": -576460752303423460,
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

#### initiator <--- node (2019-03-18 14:06:32.865)
```javascript
{
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "id": -576460752303423460,
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

#### initiator ---> node (2019-03-18 14:06:32.866)
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

#### initiator <--- node (2019-03-18 14:06:32.881)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "tx": "tx_+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv9/9VMM="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:06:32.882)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuEC7TvlAWelk0OX3mchzbHvmHadDZSV0KRipJTL3zdbGT/gRKpKSXFFJjC4Hr3cznHdejfAOcWKdl+v5hvJKvvAEuJf4lTkBoQbY/TE9PmMeWVRJAbe/imvTDDLJq5Tm6nwlHYQdGnB9GgX4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/wG12Ow=="
  }
}
```

#### responder <--- node (2019-03-18 14:06:32.926)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:06:32.928)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "tx": "tx_+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv9/9VMM="
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-18 14:06:32.929)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+N8LAfhCuEBxwijinBGG5VWagSoSy9ddRKq7ttqwKWG5xLSCxC7dw9Nc8x+jOThxc4kl6AKTqpqmHEdduMUNMrzny1csQWgMuJf4lTkBoQbY/TE9PmMeWVRJAbe/imvTDDLJq5Tm6nwlHYQdGnB9GgX4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoKM+TsJdaNIdM7xXZj1ZNp3oP/mwHzIJHxa6ZaHRbFa/cTLNYA=="
  }
}
```

#### responder <--- node (2019-03-18 14:06:32.962)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "state": "tx_+QEhCwH4hLhAccIo4pwRhuVVmoEqEsvXXUSqu7basClhucS0gsQu3cPTXPMfozk4cXOJJegCk6qaphxHXbjFDTK858tXLEFoDLhAu075QFnpZNDl95nIc2x75h2nQ2UldCkYqSUy983Wxk/4ESqSklxRSYwuB693M5x3Xo3wDnFinZfr+YbySr7wBLiX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv8j3HnQ="
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:06:32.977)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "state": "tx_+QEhCwH4hLhAccIo4pwRhuVVmoEqEsvXXUSqu7basClhucS0gsQu3cPTXPMfozk4cXOJJegCk6qaphxHXbjFDTK858tXLEFoDLhAu075QFnpZNDl95nIc2x75h2nQ2UldCkYqSUy983Wxk/4ESqSklxRSYwuB693M5x3Xo3wDnFinZfr+YbySr7wBLiX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv8j3HnQ="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:06:33.1)
```javascript
{
  "id": -576460752303423459,
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

#### initiator <--- node (2019-03-18 14:06:33.6)
```javascript
{
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "id": -576460752303423459,
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

#### initiator ---> node (2019-03-18 14:06:33.7)
```javascript
{
  "id": -576460752303423458,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node (2019-03-18 14:06:33.12)
```javascript
{
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "id": -576460752303423458,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAccIo4pwRhuVVmoEqEsvXXUSqu7basClhucS0gsQu3cPTXPMfozk4cXOJJegCk6qaphxHXbjFDTK858tXLEFoDLhAu075QFnpZNDl95nIc2x75h2nQ2UldCkYqSUy983Wxk/4ESqSklxRSYwuB693M5x3Xo3wDnFinZfr+YbySr7wBLiX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoF+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWv8j3HnQ=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJf/7DvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAFkGvNa"
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:06:33.19)
```javascript
{
  "id": -576460752303423457,
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

#### initiator <--- node (2019-03-18 14:06:33.30)
```javascript
{
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "id": -576460752303423457,
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

#### responder ---> node (2019-03-18 14:06:33.31)
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

#### responder <--- node (2019-03-18 14:06:33.54)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "tx": "tx_+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TscPCptE="
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-18 14:06:33.56)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuEBXfI/zrbOyQ5WZX1y9pFBQwEs+iXF2zR3sIlRJ1m1BBJU5+Q0gi75MGDmNd/O09JMsBE0ezAdil22DFsat8ckGuJf4lTkBoQbY/TE9PmMeWVRJAbe/imvTDDLJq5Tm6nwlHYQdGnB9Ggb4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROx4FONvg=="
  }
}
```

#### initiator <--- node (2019-03-18 14:06:33.117)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-18 14:06:33.118)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "tx": "tx_+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TscPCptE="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:06:33.119)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+N8LAfhCuEAteJX0AAeHc2AMPRYxLc63G35oxZdaBKOQLNSMWiCYwK5DcNbjtEMpQDD0jcj0eM/AY6Ofhe37LLwynRMbVZ0MuJf4lTkBoQbY/TE9PmMeWVRJAbe/imvTDDLJq5Tm6nwlHYQdGnB9Ggb4TbhL+EmCAjoBoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhKEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YBoNhOjuIpbimiTVaVvCHPhiIL2gAhGK56FQ6MLyET3ROx8Po4WA=="
  }
}
```

#### initiator <--- node (2019-03-18 14:06:33.159)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "state": "tx_+QEhCwH4hLhALXiV9AAHh3NgDD0WMS3Otxt+aMWXWgSjkCzUjFogmMCuQ3DW47RDKUAw9I3I9HjPwGOjn4Xt+yy8Mp0TG1WdDLhAV3yP862zskOVmV9cvaRQUMBLPolxds0d7CJUSdZtQQSVOfkNIIu+TBg5jXfztPSTLARNHswHYpdtgxbGrfHJBriX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TseQeWHE="
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-18 14:06:33.183)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
    "data": {
      "state": "tx_+QEhCwH4hLhALXiV9AAHh3NgDD0WMS3Otxt+aMWXWgSjkCzUjFogmMCuQ3DW47RDKUAw9I3I9HjPwGOjn4Xt+yy8Mp0TG1WdDLhAV3yP862zskOVmV9cvaRQUMBLPolxds0d7CJUSdZtQQSVOfkNIIu+TBg5jXfztPSTLARNHswHYpdtgxbGrfHJBriX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TseQeWHE="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-18 14:06:33.205)
```javascript
{
  "id": -576460752303423456,
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

#### initiator <--- node (2019-03-18 14:06:33.212)
```javascript
{
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "id": -576460752303423456,
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

#### initiator ---> node (2019-03-18 14:06:33.212)
```javascript
{
  "id": -576460752303423455,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node (2019-03-18 14:06:33.218)
```javascript
{
  "channel_id": "ch_2eZhEJ676pykdcHHcTZuSF346bq1ru3qnAiT2KowopwrPKwy7t",
  "id": -576460752303423455,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhALXiV9AAHh3NgDD0WMS3Otxt+aMWXWgSjkCzUjFogmMCuQ3DW47RDKUAw9I3I9HjPwGOjn4Xt+yy8Mp0TG1WdDLhAV3yP862zskOVmV9cvaRQUMBLPolxds0d7CJUSdZtQQSVOfkNIIu+TBg5jXfztPSTLARNHswHYpdtgxbGrfHJBriX+JU5AaEG2P0xPT5jHllUSQG3v4pr0wwyyauU5up8JR2EHRpwfRoG+E24S/hJggI6AaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oShAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAaDYTo7iKW4pok1Wlbwhz4YiC9oAIRiuehUOjC8hE90TseQeWHE=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJgALDvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAA6duKo"
  },
  "version": 1
}
```
