
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=8&initiator_id=ak_11111111111111111111111111111115rHyByZ&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=4&responder_id=ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1011,
        "message": "Participant not found"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=8&initiator_id=ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=4&responder_id=ak_11111111111111111111111111111115rHyByZ&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1011,
        "message": "Participant not found"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=-1&initiator_id=ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=4&responder_id=ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 105,
        "message": "Value too low"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=8&initiator_id=ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=-1&responder_id=ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 105,
        "message": "Value too low"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=-1&initiator_id=ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=-1&responder_id=ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 105,
        "message": "Value too low"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=-1&host=localhost&initiator_amount=8&initiator_id=ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=4&responder_id=ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 105,
        "message": "Value too low"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=8&initiator_id=ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR&lock_period=10&port=13179&protocol=json-rpc&push_amount=-1&responder_amount=4&responder_id=ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 105,
        "message": "Value too low"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=8&initiator_id=ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR&lock_period=-1&port=13179&protocol=json-rpc&push_amount=1&responder_amount=4&responder_id=ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT&role=initiator
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "error": {
    "code": 3,
    "data": [
      {
        "code": 105,
        "message": "Value too low"
      }
    ],
    "message": "Rejected",
    "request": {}
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```
