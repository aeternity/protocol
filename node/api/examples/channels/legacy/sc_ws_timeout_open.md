
#### initiator opens a WebSocket connection (2019-03-18 14:15:05.804)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=8&initiator_id=ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=4&responder_id=ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC&role=initiator&timeout_accept=100
```

#### initiator <--- node (2019-03-18 14:15:05.923)
```javascript
{
  "action": "info",
  "channel_id": null,
  "payload": {
    "event": "died"
  },
  "version": 1
}
```
