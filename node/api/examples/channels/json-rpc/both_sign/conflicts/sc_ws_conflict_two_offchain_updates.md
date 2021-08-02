
#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
    "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
    "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmWNK6aBbShPk6CRMTltOGiGAOZ3qfuG99dqNXQHI+TnAqCmYmrUI8WuLhPHqyM94yQpUk/m5NeucZIHeasu3QdCyuTU8Vw=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainTransfer",
          "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
        }
      ]
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmWNK6aBbShPk6CRMTltOGiGAOZ3qfuG99dqNXQHI+TnAqCyPuq+gQA2a6qmnwMyrfvY3kyHmlBoHoJrMzYXSPbNfOBz3I8=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C",
          "op": "OffChainTransfer",
          "to": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt"
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
    "signed_tx": "tx_+JALAfhCuEA+9uNvs6ZkeviIYVWvbEpdNzapaI/A8c/5p0XueZZXQSns0zsIWnWeXeqt+plEsm0Q1yU/HB40myD6NJ8tq0QCuEj4RjkCoQZljSumgW0oT5OgkTE5bThohgDmd6n7hvfXajV0ByPk5wKgpmJq1CPFri4Tx6sjPeMkKVJP5uTXrnGSB3mrLt0HQspqQ1Vx"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAxuAhwq5s44/ym96QALIdYGERoITUJTaZL4r5hZKfe32zzeKsBQAo22x+TiE29oA09xoqvITv+hdpezk9VMa8CuEj4RjkCoQZljSumgW0oT5OgkTE5bThohgDmd6n7hvfXajV0ByPk5wKgsj7qvoEANmuqpp8DMq372N5Mh5pQaB6CazM2F0j2zXzD8+qW"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 1
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 1
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
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
    "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
    "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmWNK6aBbShPk6CRMTltOGiGAOZ3qfuG99dqNXQHI+TnAqDWrhhINTEoJLw82j9f9Bk+vNmSkxyPrGNp3wYPetMKfGuqKV4=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
          "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
        }
      ]
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmWNK6aBbShPk6CRMTltOGiGAOZ3qfuG99dqNXQHI+TnAqDdqOzEXWz8Y2itvyrEosD88v7VNFxfGdbGSLDDea6BYHEx+vk=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26jAbCjYM16ppbhFG6PCQhv6HkwRAri7QNJfoEtb1R8amLscpt",
          "op": "OffChainTransfer",
          "to": "ak_mLjWgLbapr5CiVD2Q248aS2TQj9itXnoPv5tteXvZaJ8tdD2C"
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
    "signed_tx": "tx_+JALAfhCuECqsf282JdN7cNSRkIt4kxJ57SnjtOabkVphE8Yv86W6IWchajde3yUgSb7T4QOZ8vw2QirCpa51XdfYQRUX40JuEj4RjkCoQZljSumgW0oT5OgkTE5bThohgDmd6n7hvfXajV0ByPk5wKg3ajsxF1s/GNorb8qxKLA/PL+1TRcXxnWxkiww3mugWBrjpVw"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEALY5WoWnCoRqxZr7aE04XjMu9+7kQCVsQK3GePnzW/uWuP6Fru3WlLfBie/I7h7rU4cWH6EBAjWTkSgbp8SpMFuEj4RjkCoQZljSumgW0oT5OgkTE5bThohgDmd6n7hvfXajV0ByPk5wKg1q4YSDUxKCS8PNo/X/QZPrzZkpMcj6xjad8GD3rTCny2HOSg"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 1
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
    "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
    "data": {
      "channel_id": "ch_mizjcLi5wLPdFhGgSGgCVYZQZSsj8anpLN2tj46nDMZkHa5sv",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 1
    }
  },
  "version": 1
}
```
