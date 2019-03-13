
#### initiator opens a WebSocket connection (2019-03-13 11:04:45.887)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3&role=initiator
```

#### responder opens a WebSocket connection (2019-03-13 11:04:45.904)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3&role=responder
```

#### responder <--- node (2019-03-13 11:04:47.10)
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

#### initiator <--- node (2019-03-13 11:04:47.16)
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

#### initiator <--- node (2019-03-13 11:04:47.51)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAH/TE+d"
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:47.172)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_+MsLAfhCuEAr1K5pVAPaoBaWrwi4zRMvymc6G/YCTI44S4sv3XwAXZBKWUba638S+Q1OuAeCK33M6997zRw9VED1AXjDNuwHuIP4gTIBoQEmB6t0j6CEj0TF7aBkfLKhLNj0/vfE3UYgZ2CLIgbnp4Y/qiUiYAChAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPhiRhOcqAAAIKAIYSMJzlQADAoODtFIhe84yV0+uaXXnfGCrRRApvdISmjmGVfhKf0nkoAUdW/8k="
  }
}
```

#### responder <--- node (2019-03-13 11:04:47.201)
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

#### responder <--- node (2019-03-13 11:04:47.202)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAH/TE+d"
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:04:47.203)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_+MsLAfhCuEBP5q9goCJvb49K3uHE3xzc2HnWhMZ5Yt9UoA2ZHjnbUkBhbyASYgsSqKQfLT9axBNghojKZDK9Yi1r3iBKKV0BuIP4gTIBoQEmB6t0j6CEj0TF7aBkfLKhLNj0/vfE3UYgZ2CLIgbnp4Y/qiUiYAChAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPhiRhOcqAAAIKAIYSMJzlQADAoODtFIhe84yV0+uaXXnfGCrRRApvdISmjmGVfhKf0nkoASNpZb0="
  }
}
```

#### responder <--- node (2019-03-13 11:04:47.214)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+QENCwH4hLhAK9SuaVQD2qAWlq8IuM0TL8pnOhv2AkyOOEuLL918AF2QSllG2ut/EvkNTrgHgit9zOvfe80cPVRA9QF4wzbsB7hAT+avYKAib2+PSt7hxN8c3Nh51oTGeWLfVKANmR4521JAYW8gEmILEqikHy0/WsQTYIaIymQyvWIta94gSildAbiD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAF6rCV2"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:04:47.216)
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

#### initiator <--- node (2019-03-13 11:04:47.218)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": null,
    "data": {
      "tx": "tx_+QENCwH4hLhAK9SuaVQD2qAWlq8IuM0TL8pnOhv2AkyOOEuLL918AF2QSllG2ut/EvkNTrgHgit9zOvfe80cPVRA9QF4wzbsB7hAT+avYKAib2+PSt7hxN8c3Nh51oTGeWLfVKANmR4521JAYW8gEmILEqikHy0/WsQTYIaIymQyvWIta94gSildAbiD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAF6rCV2"
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:48.458)
```javascript
{
  "id": -576460752303423488,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
    ]
  }
}
```

#### initiator <--- node (2019-03-13 11:04:48.464)
```javascript
{
  "channel_id": null,
  "id": -576460752303423488,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "balance": 69999999999999
    },
    {
      "account": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:04:49.174)
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

#### initiator <--- node (2019-03-13 11:04:49.178)
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

#### initiator <--- node (2019-03-13 11:04:49.182)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:04:49.183)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:04:49.195)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:04:49.196)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "state": "tx_+QENCwH4hLhAK9SuaVQD2qAWlq8IuM0TL8pnOhv2AkyOOEuLL918AF2QSllG2ut/EvkNTrgHgit9zOvfe80cPVRA9QF4wzbsB7hAT+avYKAib2+PSt7hxN8c3Nh51oTGeWLfVKANmR4521JAYW8gEmILEqikHy0/WsQTYIaIymQyvWIta94gSildAbiD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAF6rCV2"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:04:49.201)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:04:49.205)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "state": "tx_+QENCwH4hLhAK9SuaVQD2qAWlq8IuM0TL8pnOhv2AkyOOEuLL918AF2QSllG2ut/EvkNTrgHgit9zOvfe80cPVRA9QF4wzbsB7hAT+avYKAib2+PSt7hxN8c3Nh51oTGeWLfVKANmR4521JAYW8gEmILEqikHy0/WsQTYIaIymQyvWIta94gSildAbiD+IEyAaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eGP6olImAAoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4YkYTnKgAACCgCGEjCc5UAAwKDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KAF6rCV2"
    }
  },
  "version": 1
}
```

#### initiator: (2019-03-13 11:04:49.736)
> Funding has been confirmed locally on-chain

#### responder: (2019-03-13 11:04:49.736)
> Funding has been confirmed locally on-chain

#### initiator: (2019-03-13 11:04:49.736)
> Funding has been confirmed on-chain by other party

#### responder: (2019-03-13 11:04:49.736)
> Funding has been confirmed on-chain by other party

#### initiator: (2019-03-13 11:04:49.736)
> Channel is `open` and ready to use

#### responder: (2019-03-13 11:04:49.736)
> Channel is `open` and ready to use

#### initiator ---> node (2019-03-13 11:04:49.737)
```javascript
{
  "id": -576460752303423487,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
    ]
  }
}
```

#### initiator <--- node (2019-03-13 11:04:49.743)
```javascript
{
  "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
  "id": -576460752303423487,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "balance": 69999999999999
    },
    {
      "account": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:49.744)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
    "to": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
  }
}
```

#### initiator <--- node (2019-03-13 11:04:49.828)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "tx": "tx_+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUC+E24S/hJggI6AaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56ehAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAaDbfGCXUMfw4lZS/r1ddw6JYAjcG83JwCYsD8jmhgKs0tyms+4="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:49.847)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuECdrVclC0t0mJl1FZrNtfRkcoOzjveaRobHVVAtsZrZvyph21i0k3/lHe+PlHNkL2Q43uZBqZu6cmpXyl+BJZ8CuJf4lTkBoQYxAE8hV7bye4oQbSMABEyD/Nox1qSr8388sQ2FRP9AhQL4TbhL+EmCAjoBoQEmB6t0j6CEj0TF7aBkfLKhLNj0/vfE3UYgZ2CLIgbnp6EBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA208BoNt8YJdQx/DiVlL+vV13DolgCNwbzcnAJiwPyOaGAqzSsJsSYQ=="
  }
}
```

#### responder <--- node (2019-03-13 11:04:49.886)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:04:49.887)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "tx": "tx_+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUC+E24S/hJggI6AaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56ehAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAaDbfGCXUMfw4lZS/r1ddw6JYAjcG83JwCYsD8jmhgKs0tyms+4="
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:04:49.889)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+N8LAfhCuEAvlfQjPzUXYxxifV1aZBEf72GqL4QskKjC5PrL7cKw4KDdpL42yXps3pP+6iKGYYCdI+PkIqEWcEkWzm1PlLgLuJf4lTkBoQYxAE8hV7bye4oQbSMABEyD/Nox1qSr8388sQ2FRP9AhQL4TbhL+EmCAjoBoQEmB6t0j6CEj0TF7aBkfLKhLNj0/vfE3UYgZ2CLIgbnp6EBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA208BoNt8YJdQx/DiVlL+vV13DolgCNwbzcnAJiwPyOaGAqzSb1drPw=="
  }
}
```

#### responder <--- node (2019-03-13 11:04:49.914)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "state": "tx_+QEhCwH4hLhAL5X0Iz81F2McYn1dWmQRH+9hqi+ELJCowuT6y+3CsOCg3aS+Nsl6bN6T/uoihmGAnSPj5CKhFnBJFs5tT5S4C7hAna1XJQtLdJiZdRWazbX0ZHKDs473mkaGx1VQLbGa2b8qYdtYtJN/5R3vj5RzZC9kON7mQambunJqV8pfgSWfAriX+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUC+E24S/hJggI6AaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56ehAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAaDbfGCXUMfw4lZS/r1ddw6JYAjcG83JwCYsD8jmhgKs0tQcUFY="
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:04:49.928)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "state": "tx_+QEhCwH4hLhAL5X0Iz81F2McYn1dWmQRH+9hqi+ELJCowuT6y+3CsOCg3aS+Nsl6bN6T/uoihmGAnSPj5CKhFnBJFs5tT5S4C7hAna1XJQtLdJiZdRWazbX0ZHKDs473mkaGx1VQLbGa2b8qYdtYtJN/5R3vj5RzZC9kON7mQambunJqV8pfgSWfAriX+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUC+E24S/hJggI6AaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56ehAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAaDbfGCXUMfw4lZS/r1ddw6JYAjcG83JwCYsD8jmhgKs0tQcUFY="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:49.940)
```javascript
{
  "id": -576460752303423486,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
    ]
  }
}
```

#### initiator <--- node (2019-03-13 11:04:49.944)
```javascript
{
  "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
  "id": -576460752303423486,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "balance": 69999999999998
    },
    {
      "account": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:49.945)
```javascript
{
  "id": -576460752303423485,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node (2019-03-13 11:04:49.955)
```javascript
{
  "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
  "id": -576460752303423485,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAL5X0Iz81F2McYn1dWmQRH+9hqi+ELJCowuT6y+3CsOCg3aS+Nsl6bN6T/uoihmGAnSPj5CKhFnBJFs5tT5S4C7hAna1XJQtLdJiZdRWazbX0ZHKDs473mkaGx1VQLbGa2b8qYdtYtJN/5R3vj5RzZC9kON7mQambunJqV8pfgSWfAriX+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUC+E24S/hJggI6AaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56ehAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAaDbfGCXUMfw4lZS/r1ddw6JYAjcG83JwCYsD8jmhgKs0tQcUFY=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4vKCgEAhiRhOcqAArDvQAGgJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eLygoBAIY/qiUiX/5NyGDh"
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:50.124)
```javascript
{
  "id": -576460752303423484,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
    ]
  }
}
```

#### initiator <--- node (2019-03-13 11:04:50.128)
```javascript
{
  "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
  "id": -576460752303423484,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "balance": 40000000000002
    },
    {
      "account": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "balance": 69999999999998
    }
  ],
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:04:50.129)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
    "to": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
  }
}
```

#### responder <--- node (2019-03-13 11:04:50.152)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "tx": "tx_+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUD+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KHLD41E="
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:04:50.153)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuECkqgrCcjX+BsyVV3yP4uekHzjjV5CKgaSkcNeCZPssdmgWtaihzt0YvDS1HMOMrCnaVJjqBazGDKdU8JWOuIYCuJf4lTkBoQYxAE8hV7bye4oQbSMABEyD/Nox1qSr8388sQ2FRP9AhQP4TbhL+EmCAjoBoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT6EBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cBoODtFIhe84yV0+uaXXnfGCrRRApvdISmjmGVfhKf0nkoML5ZiA=="
  }
}
```

#### initiator <--- node (2019-03-13 11:04:50.192)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:04:50.193)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "tx": "tx_+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUD+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KHLD41E="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:50.194)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+N8LAfhCuECPAAsxB6/moyoj1/1+BAobDswLM8iMt/+zbxvh8bVEpklGRiTO0Bb1CbWwN24zvV2429oAb5J1wooGSzeVjtgAuJf4lTkBoQYxAE8hV7bye4oQbSMABEyD/Nox1qSr8388sQ2FRP9AhQP4TbhL+EmCAjoBoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT6EBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cBoODtFIhe84yV0+uaXXnfGCrRRApvdISmjmGVfhKf0nkopOc6ng=="
  }
}
```

#### initiator <--- node (2019-03-13 11:04:50.218)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "state": "tx_+QEhCwH4hLhAjwALMQev5qMqI9f9fgQKGw7MCzPIjLf/s28b4fG1RKZJRkYkztAW9Qm1sDduM71duNvaAG+SdcKKBks3lY7YALhApKoKwnI1/gbMlVd8j+LnpB8441eQioGkpHDXgmT7LHZoFrWooc7dGLw0tRzDjKwp2lSY6gWsxgynVPCVjriGAriX+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUD+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KCnUTvQ="
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:04:50.231)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "state": "tx_+QEhCwH4hLhAjwALMQev5qMqI9f9fgQKGw7MCzPIjLf/s28b4fG1RKZJRkYkztAW9Qm1sDduM71duNvaAG+SdcKKBks3lY7YALhApKoKwnI1/gbMlVd8j+LnpB8441eQioGkpHDXgmT7LHZoFrWooc7dGLw0tRzDjKwp2lSY6gWsxgynVPCVjriGAriX+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUD+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KCnUTvQ="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:50.251)
```javascript
{
  "id": -576460752303423483,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
    ]
  }
}
```

#### initiator <--- node (2019-03-13 11:04:50.255)
```javascript
{
  "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
  "id": -576460752303423483,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "balance": 40000000000001
    },
    {
      "account": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:50.256)
```javascript
{
  "id": -576460752303423482,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node (2019-03-13 11:04:50.260)
```javascript
{
  "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
  "id": -576460752303423482,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAjwALMQev5qMqI9f9fgQKGw7MCzPIjLf/s28b4fG1RKZJRkYkztAW9Qm1sDduM71duNvaAG+SdcKKBks3lY7YALhApKoKwnI1/gbMlVd8j+LnpB8441eQioGkpHDXgmT7LHZoFrWooc7dGLw0tRzDjKwp2lSY6gWsxgynVPCVjriGAriX+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUD+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KCnUTvQ=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4vKCgEAhiRhOcqAAbDvQAGgJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eLygoBAIY/qiUiX//8omNo"
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:50.267)
```javascript
{
  "id": -576460752303423481,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
    ]
  }
}
```

#### initiator <--- node (2019-03-13 11:04:50.271)
```javascript
{
  "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
  "id": -576460752303423481,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "balance": 40000000000001
    },
    {
      "account": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:04:50.272)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
    "to": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
  }
}
```

#### responder <--- node (2019-03-13 11:04:50.284)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "tx": "tx_+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUE+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaBtJeqayYNAxAR8VEb/US6Hb7IetZ7x8ND25z+UAJu3MyZK5L4="
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:04:50.285)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuEAnM6919+mCdxBCdIjKPU0Gs8lyfHVb6v243CX2GwqIz01VEfzbadDo73bhW79sTctX/wSaBZCC9jmQw8MUh0kOuJf4lTkBoQYxAE8hV7bye4oQbSMABEyD/Nox1qSr8388sQ2FRP9AhQT4TbhL+EmCAjoBoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT6EBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cBoG0l6prJg0DEBHxURv9RLodvsh61nvHw0PbnP5QAm7czoqvk+g=="
  }
}
```

#### initiator <--- node (2019-03-13 11:04:50.325)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:04:50.326)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "tx": "tx_+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUE+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaBtJeqayYNAxAR8VEb/US6Hb7IetZ7x8ND25z+UAJu3MyZK5L4="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:50.327)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+N8LAfhCuEBocSjeC2t32MmF4AhSojHrUIFTcp7si/XOI4yLIKReVLHDV4uo0wvrK1UHQ7bRe44XQReqrN7amTTd8hs8njEIuJf4lTkBoQYxAE8hV7bye4oQbSMABEyD/Nox1qSr8388sQ2FRP9AhQT4TbhL+EmCAjoBoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT6EBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cBoG0l6prJg0DEBHxURv9RLodvsh61nvHw0PbnP5QAm7czNG93BA=="
  }
}
```

#### initiator <--- node (2019-03-13 11:04:50.350)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "state": "tx_+QEhCwH4hLhAJzOvdffpgncQQnSIyj1NBrPJcnx1W+r9uNwl9hsKiM9NVRH822nQ6O924Vu/bE3LV/8EmgWQgvY5kMPDFIdJDrhAaHEo3gtrd9jJheAIUqIx61CBU3Ke7Iv1ziOMiyCkXlSxw1eLqNML6ytVB0O20XuOF0EXqqze2pk03fIbPJ4xCLiX+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUE+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaBtJeqayYNAxAR8VEb/US6Hb7IetZ7x8ND25z+UAJu3M+Xb8e8="
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:04:50.364)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "state": "tx_+QEhCwH4hLhAJzOvdffpgncQQnSIyj1NBrPJcnx1W+r9uNwl9hsKiM9NVRH822nQ6O924Vu/bE3LV/8EmgWQgvY5kMPDFIdJDrhAaHEo3gtrd9jJheAIUqIx61CBU3Ke7Iv1ziOMiyCkXlSxw1eLqNML6ytVB0O20XuOF0EXqqze2pk03fIbPJ4xCLiX+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUE+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaBtJeqayYNAxAR8VEb/US6Hb7IetZ7x8ND25z+UAJu3M+Xb8e8="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:50.375)
```javascript
{
  "id": -576460752303423480,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
    ]
  }
}
```

#### initiator <--- node (2019-03-13 11:04:50.380)
```javascript
{
  "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
  "id": -576460752303423480,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "balance": 40000000000000
    },
    {
      "account": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:50.381)
```javascript
{
  "id": -576460752303423479,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node (2019-03-13 11:04:50.386)
```javascript
{
  "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
  "id": -576460752303423479,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAJzOvdffpgncQQnSIyj1NBrPJcnx1W+r9uNwl9hsKiM9NVRH822nQ6O924Vu/bE3LV/8EmgWQgvY5kMPDFIdJDrhAaHEo3gtrd9jJheAIUqIx61CBU3Ke7Iv1ziOMiyCkXlSxw1eLqNML6ytVB0O20XuOF0EXqqze2pk03fIbPJ4xCLiX+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUE+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaBtJeqayYNAxAR8VEb/US6Hb7IetZ7x8ND25z+UAJu3M+Xb8e8=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4vKCgEAhiRhOcqAALDvQAGgJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eLygoBAIY/qiUiYADbIKsP"
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:50.393)
```javascript
{
  "id": -576460752303423478,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
    ]
  }
}
```

#### initiator <--- node (2019-03-13 11:04:50.398)
```javascript
{
  "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
  "id": -576460752303423478,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "balance": 70000000000000
    },
    {
      "account": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "balance": 40000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:50.399)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
    "to": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
  }
}
```

#### initiator <--- node (2019-03-13 11:04:50.412)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "tx": "tx_+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUF+E24S/hJggI6AaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56ehAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAaDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KLQbd3Q="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:50.413)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuEA5ZQDrN200bhwkOTc8hoRm9cX0UcJi/NFL1Ys69VCp9si4yfvpJbNJTVXljK0eHza37WeFtdOezGyeGUHJT/AIuJf4lTkBoQYxAE8hV7bye4oQbSMABEyD/Nox1qSr8388sQ2FRP9AhQX4TbhL+EmCAjoBoQEmB6t0j6CEj0TF7aBkfLKhLNj0/vfE3UYgZ2CLIgbnp6EBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA208BoODtFIhe84yV0+uaXXnfGCrRRApvdISmjmGVfhKf0nko+OV+6g=="
  }
}
```

#### responder <--- node (2019-03-13 11:04:50.468)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:04:50.471)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "tx": "tx_+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUF+E24S/hJggI6AaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56ehAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAaDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KLQbd3Q="
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:04:50.472)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+N8LAfhCuEA7LR7ylQPM3NHAIMfEpaHDPDuoaHn1ibDXIL6b4DevqR9yi5LQK1K6IxuF/GdKAbRvg6/F3SdAgmvzNIbiDhQFuJf4lTkBoQYxAE8hV7bye4oQbSMABEyD/Nox1qSr8388sQ2FRP9AhQX4TbhL+EmCAjoBoQEmB6t0j6CEj0TF7aBkfLKhLNj0/vfE3UYgZ2CLIgbnp6EBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA208BoODtFIhe84yV0+uaXXnfGCrRRApvdISmjmGVfhKf0nkojUaCpg=="
  }
}
```

#### responder <--- node (2019-03-13 11:04:50.496)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "state": "tx_+QEhCwH4hLhAOWUA6zdtNG4cJDk3PIaEZvXF9FHCYvzRS9WLOvVQqfbIuMn76SWzSU1V5YytHh82t+1nhbXTnsxsnhlByU/wCLhAOy0e8pUDzNzRwCDHxKWhwzw7qGh59Ymw1yC+m+A3r6kfcouS0CtSuiMbhfxnSgG0b4Ovxd0nQIJr8zSG4g4UBbiX+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUF+E24S/hJggI6AaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56ehAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAaDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KKdXJgM="
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:04:50.509)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "state": "tx_+QEhCwH4hLhAOWUA6zdtNG4cJDk3PIaEZvXF9FHCYvzRS9WLOvVQqfbIuMn76SWzSU1V5YytHh82t+1nhbXTnsxsnhlByU/wCLhAOy0e8pUDzNzRwCDHxKWhwzw7qGh59Ymw1yC+m+A3r6kfcouS0CtSuiMbhfxnSgG0b4Ovxd0nQIJr8zSG4g4UBbiX+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUF+E24S/hJggI6AaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56ehAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAaDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KKdXJgM="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:50.521)
```javascript
{
  "id": -576460752303423477,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
    ]
  }
}
```

#### initiator <--- node (2019-03-13 11:04:50.525)
```javascript
{
  "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
  "id": -576460752303423477,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "balance": 69999999999999
    },
    {
      "account": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:50.526)
```javascript
{
  "id": -576460752303423476,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node (2019-03-13 11:04:50.532)
```javascript
{
  "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
  "id": -576460752303423476,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAOWUA6zdtNG4cJDk3PIaEZvXF9FHCYvzRS9WLOvVQqfbIuMn76SWzSU1V5YytHh82t+1nhbXTnsxsnhlByU/wCLhAOy0e8pUDzNzRwCDHxKWhwzw7qGh59Ymw1yC+m+A3r6kfcouS0CtSuiMbhfxnSgG0b4Ovxd0nQIJr8zSG4g4UBbiX+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUF+E24S/hJggI6AaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56ehAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAaDg7RSIXvOMldPrml153xgq0UQKb3SEpo5hlX4Sn9J5KKdXJgM=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4vKCgEAhiRhOcqAAbDvQAGgJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eLygoBAIY/qiUiX//8omNo"
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:50.539)
```javascript
{
  "id": -576460752303423475,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
    ]
  }
}
```

#### initiator <--- node (2019-03-13 11:04:50.543)
```javascript
{
  "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
  "id": -576460752303423475,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "balance": 40000000000001
    },
    {
      "account": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:04:50.544)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
    "to": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
  }
}
```

#### responder <--- node (2019-03-13 11:04:50.557)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "tx": "tx_+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUG+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaBtJeqayYNAxAR8VEb/US6Hb7IetZ7x8ND25z+UAJu3M7YS81M="
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:04:50.558)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuEDk1t31utfKNY7UwU/YrFz26EOglqPpy0ACBuIWzkn6TBZiDnU+J+Fh1MrzOTdFs06HexGeNRYvHGIiCS7/2kkFuJf4lTkBoQYxAE8hV7bye4oQbSMABEyD/Nox1qSr8388sQ2FRP9AhQb4TbhL+EmCAjoBoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT6EBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cBoG0l6prJg0DEBHxURv9RLodvsh61nvHw0PbnP5QAm7cznBOxOQ=="
  }
}
```

#### initiator <--- node (2019-03-13 11:04:50.610)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:04:50.611)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "tx": "tx_+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUG+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaBtJeqayYNAxAR8VEb/US6Hb7IetZ7x8ND25z+UAJu3M7YS81M="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:50.612)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+N8LAfhCuEDTxT0Mw/+1TACA7cKWAKos7HyNmiGMgqk4yvS+GiXndXkG1W+ogaK9y/AREso8MyBVvwGNlAAEgmIUvcAbiVUMuJf4lTkBoQYxAE8hV7bye4oQbSMABEyD/Nox1qSr8388sQ2FRP9AhQb4TbhL+EmCAjoBoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT6EBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cBoG0l6prJg0DEBHxURv9RLodvsh61nvHw0PbnP5QAm7czmw2kGw=="
  }
}
```

#### initiator <--- node (2019-03-13 11:04:50.636)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "state": "tx_+QEhCwH4hLhA08U9DMP/tUwAgO3ClgCqLOx8jZohjIKpOMr0vhol53V5BtVvqIGivcvwERLKPDMgVb8BjZQABIJiFL3AG4lVDLhA5Nbd9brXyjWO1MFP2Kxc9uhDoJaj6ctAAgbiFs5J+kwWYg51PifhYdTK8zk3RbNOh3sRnjUWLxxiIgku/9pJBbiX+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUG+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaBtJeqayYNAxAR8VEb/US6Hb7IetZ7x8ND25z+UAJu3M1kXGPU="
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:04:50.652)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
    "data": {
      "state": "tx_+QEhCwH4hLhA08U9DMP/tUwAgO3ClgCqLOx8jZohjIKpOMr0vhol53V5BtVvqIGivcvwERLKPDMgVb8BjZQABIJiFL3AG4lVDLhA5Nbd9brXyjWO1MFP2Kxc9uhDoJaj6ctAAgbiFs5J+kwWYg51PifhYdTK8zk3RbNOh3sRnjUWLxxiIgku/9pJBbiX+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUG+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaBtJeqayYNAxAR8VEb/US6Hb7IetZ7x8ND25z+UAJu3M1kXGPU="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:50.662)
```javascript
{
  "id": -576460752303423474,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
    ]
  }
}
```

#### initiator <--- node (2019-03-13 11:04:50.666)
```javascript
{
  "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
  "id": -576460752303423474,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
      "balance": 40000000000000
    },
    {
      "account": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:04:50.667)
```javascript
{
  "id": -576460752303423473,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node (2019-03-13 11:04:50.672)
```javascript
{
  "channel_id": "ch_Nafs97iFXM7wJxhiL8Qy6oWPgmJtkBQkuqcB7TzNiNHUmAmKi",
  "id": -576460752303423473,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhA08U9DMP/tUwAgO3ClgCqLOx8jZohjIKpOMr0vhol53V5BtVvqIGivcvwERLKPDMgVb8BjZQABIJiFL3AG4lVDLhA5Nbd9brXyjWO1MFP2Kxc9uhDoJaj6ctAAgbiFs5J+kwWYg51PifhYdTK8zk3RbNOh3sRnjUWLxxiIgku/9pJBbiX+JU5AaEGMQBPIVe28nuKEG0jAARMg/zaMdakq/N/PLENhUT/QIUG+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaBtJeqayYNAxAR8VEb/US6Hb7IetZ7x8ND25z+UAJu3M1kXGPU=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT4vKCgEAhiRhOcqAALDvQAGgJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56eLygoBAIY/qiUiYADbIKsP"
  },
  "version": 1
}
```
