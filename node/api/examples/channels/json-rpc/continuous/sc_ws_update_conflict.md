
#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
    "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 2,
    "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
    "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgaV+DmvL9j9vfVuI46KW8utRGzWgdP/ANr7y0NXKTUQBqCBc5ctffDDQWJo7ZPQH/k0bRE7GJreEajctppMowEzBPBr57Y=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
          "op": "OffChainTransfer",
          "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgaV+DmvL9j9vfVuI46KW8utRGzWgdP/ANr7y0NXKTUQBqBBCOFlzgxrCKtRrQPx23phpiUnifrgJMUhpNa+5DFOwvXpzV8=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
          "op": "OffChainTransfer",
          "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
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
    "signed_tx": "tx_+JALAfhCuEBxVndTWo8ODwDdIatkD6R5f89SvYT9Psyi30jrldtZyDJ3hg7IcI2ERoPMxU/e2YmZAWAGlKJWoUaQ+9yZotMBuEj4RjkCoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EAagQQjhZc4MawirUa0D8dt6YaYlJ4n64CTFIaTWvuQxTsJ6MD3t"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBs813NWMdq31HAToWUGsa2BZ/HdA97qsSFCA0qCMZqCGca6wedeF7l9G8ns9RMoeFhG4eraUXsmXPn3UF0deEPuEj4RjkCoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EAaggXOXLX3ww0FiaO2T0B/5NG0ROxia3hGo3LaaTKMBMwQuqUlL"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
      "round": 5
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
      "round": 5
    }
  },
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
    "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
    "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 2,
    "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
    "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
      "round": 5
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
      "round": 5
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgaV+DmvL9j9vfVuI46KW8utRGzWgdP/ANr7y0NXKTUQBqBD48upGMSQmUHkvAbXk8OLPb+iXSg8kxqzNfUkPoVMWdNe63g=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
          "op": "OffChainTransfer",
          "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
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
    "signed_tx": "tx_+JALAfhCuEClKE7369vgNhjDjOx6ejaQaXl74QYaQrG1lSV2N6MeAfNiJeNrX/J4GhF12Mo1AOlBzQnIhElaOBmsviYVtg4OuEj4RjkCoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EAagQ+PLqRjEkJlB5LwG15PDiz2/ol0oPJMaszX1JD6FTFlfEP1J"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgaV+DmvL9j9vfVuI46KW8utRGzWgdP/ANr7y0NXKTUQBqAOdMOxOLPDgqKMNYb6h/lVdi5+4MJQDAlPDfAWGz2bqLJyKLQ=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
          "op": "OffChainTransfer",
          "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
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
    "signed_tx": "tx_+JALAfhCuEBrRRqcJ19D+mp0qv58G+ewgwRBpbs6DVdt5K7ET9d1WYczwmKqQ9Sn44KyiT3Uymbsgqye+o7NostUNhEyvXQPuEj4RjkCoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EAagDnTDsTizw4KijDWG+of5VXYufuDCUAwJTw3wFhs9m6gla8sk"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
      "round": 5
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
      "round": 5
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
      "round": 5
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
      "round": 5
    }
  },
  "version": 1
}
```
