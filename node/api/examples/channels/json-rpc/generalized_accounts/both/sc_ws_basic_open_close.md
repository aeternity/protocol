
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf&keep_running=false&lock_period=10&port=13088&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu&role=initiator
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_XfNd/E0KIEq49tCtiIV+HZC5yl+0gKY0C10k5vSnOhonN4y8"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf&keep_running=false&lock_period=10&port=13088&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu&role=responder
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_dHp5Be2RGaTk82i8Z1jvQYwEwohG4yigJTUiffZ1dN3cO/cp"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

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

#### responder info
> Received an WebSocket opening request

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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAfvOLnmWDSh90jnvPgmG70f3d2IZLW+I2uGwrrP+dtsvhj+qJSJgAKEBJAUlgdTozkXKO+qtgPLxFNqPCVpX7IRf6/OaAZnj0myGJGE5yoAAAgoAhhAGeddIAMCgwmhrYorf3z33MRoRrjaBEnW3GkcFod8ygLF4HHXl3TwAykuc+w==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422125,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+QFuCwHAuQFo+QFlUQGhAfvOLnmWDSh90jnvPgmG70f3d2IZLW+I2uGwrrP+dtsvuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiK+IgLAcC4g/iBMgGhAfvOLnmWDSh90jnvPgmG70f3d2IZLW+I2uGwrrP+dtsvhj+qJSJgAKEBJAUlgdTozkXKO+qtgPLxFNqPCVpX7IRf6/OaAZnj0myGJGE5yoAAAgoAhhAGeddIAMCgwmhrYorf3z33MRoRrjaBEnW3GkcFod8ygLF4HHXl3TwACfYukA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422125,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
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
      "signed_tx": "tx_+QFuCwHAuQFo+QFlUQGhAfvOLnmWDSh90jnvPgmG70f3d2IZLW+I2uGwrrP+dtsvuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiK+IgLAcC4g/iBMgGhAfvOLnmWDSh90jnvPgmG70f3d2IZLW+I2uGwrrP+dtsvhj+qJSJgAKEBJAUlgdTozkXKO+qtgPLxFNqPCVpX7IRf6/OaAZnj0myGJGE5yoAAAgoAhhAGeddIAMCgwmhrYorf3z33MRoRrjaBEnW3GkcFod8ygLF4HHXl3TwACfYukA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422124,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QJWCwHAuQJQ+QJNUQGhASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JsuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBcfkBbgsBwLkBaPkBZVEBoQH7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL7igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQH7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL4Y/qiUiYAChASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JshiRhOcqAAAIKAIYQBnnXSADAoMJoa2KK39899zEaEa42gRJ1txpHBaHfMoCxeBx15d08APP6c8U="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422124,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QJWCwHAuQJQ+QJNUQGhASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JsuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBcfkBbgsBwLkBaPkBZVEBoQH7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL7igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQH7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL4Y/qiUiYAChASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JshiRhOcqAAAIKAIYQBnnXSADAoMJoa2KK39899zEaEa42gRJ1txpHBaHfMoCxeBx15d08APP6c8U=",
      "type": "channel_create_tx"
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
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QJWCwHAuQJQ+QJNUQGhASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JsuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBcfkBbgsBwLkBaPkBZVEBoQH7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL7igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQH7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL4Y/qiUiYAChASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JshiRhOcqAAAIKAIYQBnnXSADAoMJoa2KK39899zEaEa42gRJ1txpHBaHfMoCxeBx15d08APP6c8U=",
      "type": "channel_create_tx"
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
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QJWCwHAuQJQ+QJNUQGhASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JsuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBcfkBbgsBwLkBaPkBZVEBoQH7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL7igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQH7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL4Y/qiUiYAChASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JshiRhOcqAAAIKAIYQBnnXSADAoMJoa2KK39899zEaEa42gRJ1txpHBaHfMoCxeBx15d08APP6c8U=",
      "type": "channel_create_tx"
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
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QJWCwHAuQJQ+QJNUQGhASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JsuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBcfkBbgsBwLkBaPkBZVEBoQH7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL7igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQH7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL4Y/qiUiYAChASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JshiRhOcqAAAIKAIYQBnnXSADAoMJoa2KK39899zEaEa42gRJ1txpHBaHfMoCxeBx15d08APP6c8U=",
      "type": "channel_create_tx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello",
    "to": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "message": {
        "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
        "from": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
        "info": "Hello",
        "to": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
    "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "message": {
        "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
        "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
        "info": "Hello back",
        "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422123,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
      "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422123,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
      "balance": 69999999999999
    },
    {
      "account": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
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
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
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
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
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
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "state": "tx_+QJWCwHAuQJQ+QJNUQGhASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JsuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBcfkBbgsBwLkBaPkBZVEBoQH7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL7igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQH7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL4Y/qiUiYAChASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JshiRhOcqAAAIKAIYQBnnXSADAoMJoa2KK39899zEaEa42gRJ1txpHBaHfMoCxeBx15d08APP6c8U="
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
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "state": "tx_+QJWCwHAuQJQ+QJNUQGhASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JsuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBcfkBbgsBwLkBaPkBZVEBoQH7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL7igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQH7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL4Y/qiUiYAChASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JshiRhOcqAAAIKAIYQBnnXSADAoMJoa2KK39899zEaEa42gRJ1txpHBaHfMoCxeBx15d08APP6c8U="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422122,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
      "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422122,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
      "balance": 69999999999999
    },
    {
      "account": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
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
    "from": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
    "to": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
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
        "from": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
        "to": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
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
    "from": "ABCDEF",
    "to": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
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
    "from": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
        "to": "ABCDEF"
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
    "from": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
    "meta": 17,
    "to": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
        "meta": 17,
        "to": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
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
    "from": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
    "to": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlF6JIH+70ASGh61S7CbqyhryGyPp6Cj9IohGsc0vBIVAqBuAA8FpGZMSvee99UNbeEW1kIqtjxnhx9L791Cc/s3eECLBoY=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
          "op": "OffChainTransfer",
          "to": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
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
  "id": -576460752303422121,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAfvOLnmWDSh90jnvPgmG70f3d2IZLW+I2uGwrrP+dtsvuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBlF6JIH+70ASGh61S7CbqyhryGyPp6Cj9IohGsc0vBIVAqBuAA8FpGZMSvee99UNbeEW1kIqtjxnhx9L791Cc/s3eLPY+bQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422121,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
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
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAfvOLnmWDSh90jnvPgmG70f3d2IZLW+I2uGwrrP+dtsvuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBlF6JIH+70ASGh61S7CbqyhryGyPp6Cj9IohGsc0vBIVAqBuAA8FpGZMSvee99UNbeEW1kIqtjxnhx9L791Cc/s3eLPY+bQ=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
          "op": "OffChainTransfer",
          "to": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
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
  "id": -576460752303422120,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JsuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQH7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL7igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZReiSB/u9AEhoetUuwm6soa8hsj6ego/SKIRrHNLwSFQKgbgAPBaRmTEr3nvfVDW3hFtZCKrY8Z4cfS+/dQnP7N3gpnUdR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422120,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JsuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQH7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL7igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZReiSB/u9AEhoetUuwm6soa8hsj6ego/SKIRrHNLwSFQKgbgAPBaRmTEr3nvfVDW3hFtZCKrY8Z4cfS+/dQnP7N3gpnUdR"
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
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JsuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQH7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL7igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZReiSB/u9AEhoetUuwm6soa8hsj6ego/SKIRrHNLwSFQKgbgAPBaRmTEr3nvfVDW3hFtZCKrY8Z4cfS+/dQnP7N3gpnUdR"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422119,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
      "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422119,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
      "balance": 69999999999998
    },
    {
      "account": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422118,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422118,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JsuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQH7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL7igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZReiSB/u9AEhoetUuwm6soa8hsj6ego/SKIRrHNLwSFQKgbgAPBaRmTEr3nvfVDW3hFtZCKrY8Z4cfS+/dQnP7N3gpnUdR",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL4vKCgEAhj+qJSJf/rDvQAGgJAUlgdTozkXKO+qtgPLxFNqPCVpX7IRf6/OaAZnj0myLygoBAIYkYTnKgAJ9b0wc"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422117,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
      "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422117,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
      "balance": 40000000000002
    },
    {
      "account": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
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
    "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
    "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
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
        "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
        "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
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
    "from": "ABCDEF",
    "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
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
    "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
        "to": "ABCDEF"
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
    "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
    "meta": 17,
    "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
        "meta": 17,
        "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
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
    "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
    "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlF6JIH+70ASGh61S7CbqyhryGyPp6Cj9IohGsc0vBIVA6DCaGtiit/fPfcxGhGuNoESdbcaRwWh3zKAsXgcdeXdPKmnieU=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
          "op": "OffChainTransfer",
          "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
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
  "id": -576460752303422116,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JsuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBlF6JIH+70ASGh61S7CbqyhryGyPp6Cj9IohGsc0vBIVA6DCaGtiit/fPfcxGhGuNoESdbcaRwWh3zKAsXgcdeXdPMU+tsw="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422116,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
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
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JsuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBlF6JIH+70ASGh61S7CbqyhryGyPp6Cj9IohGsc0vBIVA6DCaGtiit/fPfcxGhGuNoESdbcaRwWh3zKAsXgcdeXdPMU+tsw=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
          "op": "OffChainTransfer",
          "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
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
  "id": -576460752303422115,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhAfvOLnmWDSh90jnvPgmG70f3d2IZLW+I2uGwrrP+dtsvuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEkBSWB1OjORco76q2A8vEU2o8JWlfshF/r85oBmePSbLigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZReiSB/u9AEhoetUuwm6soa8hsj6ego/SKIRrHNLwSFQOgwmhrYorf3z33MRoRrjaBEnW3GkcFod8ygLF4HHXl3TyEQnaG"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422115,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhAfvOLnmWDSh90jnvPgmG70f3d2IZLW+I2uGwrrP+dtsvuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEkBSWB1OjORco76q2A8vEU2o8JWlfshF/r85oBmePSbLigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZReiSB/u9AEhoetUuwm6soa8hsj6ego/SKIRrHNLwSFQOgwmhrYorf3z33MRoRrjaBEnW3GkcFod8ygLF4HHXl3TyEQnaG"
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
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhAfvOLnmWDSh90jnvPgmG70f3d2IZLW+I2uGwrrP+dtsvuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEkBSWB1OjORco76q2A8vEU2o8JWlfshF/r85oBmePSbLigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZReiSB/u9AEhoetUuwm6soa8hsj6ego/SKIRrHNLwSFQOgwmhrYorf3z33MRoRrjaBEnW3GkcFod8ygLF4HHXl3TyEQnaG"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422114,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
      "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422114,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
      "balance": 40000000000001
    },
    {
      "account": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422113,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422113,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhAfvOLnmWDSh90jnvPgmG70f3d2IZLW+I2uGwrrP+dtsvuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEkBSWB1OjORco76q2A8vEU2o8JWlfshF/r85oBmePSbLigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZReiSB/u9AEhoetUuwm6soa8hsj6ego/SKIRrHNLwSFQOgwmhrYorf3z33MRoRrjaBEnW3GkcFod8ygLF4HHXl3TyEQnaG",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL4vKCgEAhj+qJSJf/7DvQAGgJAUlgdTozkXKO+qtgPLxFNqPCVpX7IRf6/OaAZnj0myLygoBAIYkYTnKgAGRWhB0"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422112,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
      "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422112,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
      "balance": 40000000000001
    },
    {
      "account": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
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
    "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
    "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
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
        "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
        "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
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
    "from": "ABCDEF",
    "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
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
    "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
        "to": "ABCDEF"
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
    "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
    "meta": 17,
    "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
        "meta": 17,
        "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
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
    "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
    "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlF6JIH+70ASGh61S7CbqyhryGyPp6Cj9IohGsc0vBIVBKAp3/6zfdBnqelAJuRcI1iovWkMB3iIIiJkDA+HdFLCXfgYQgY=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
          "op": "OffChainTransfer",
          "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
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
  "id": -576460752303422111,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JsuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBlF6JIH+70ASGh61S7CbqyhryGyPp6Cj9IohGsc0vBIVBKAp3/6zfdBnqelAJuRcI1iovWkMB3iIIiJkDA+HdFLCXe7g7YY="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422111,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
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
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JsuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBlF6JIH+70ASGh61S7CbqyhryGyPp6Cj9IohGsc0vBIVBKAp3/6zfdBnqelAJuRcI1iovWkMB3iIIiJkDA+HdFLCXe7g7YY=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
          "op": "OffChainTransfer",
          "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
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
  "id": -576460752303422110,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhAfvOLnmWDSh90jnvPgmG70f3d2IZLW+I2uGwrrP+dtsvuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEkBSWB1OjORco76q2A8vEU2o8JWlfshF/r85oBmePSbLigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZReiSB/u9AEhoetUuwm6soa8hsj6ego/SKIRrHNLwSFQSgKd/+s33QZ6npQCbkXCNYqL1pDAd4iCIiZAwPh3RSwl3vBsw1"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422110,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhAfvOLnmWDSh90jnvPgmG70f3d2IZLW+I2uGwrrP+dtsvuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEkBSWB1OjORco76q2A8vEU2o8JWlfshF/r85oBmePSbLigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZReiSB/u9AEhoetUuwm6soa8hsj6ego/SKIRrHNLwSFQSgKd/+s33QZ6npQCbkXCNYqL1pDAd4iCIiZAwPh3RSwl3vBsw1"
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
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhAfvOLnmWDSh90jnvPgmG70f3d2IZLW+I2uGwrrP+dtsvuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEkBSWB1OjORco76q2A8vEU2o8JWlfshF/r85oBmePSbLigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZReiSB/u9AEhoetUuwm6soa8hsj6ego/SKIRrHNLwSFQSgKd/+s33QZ6npQCbkXCNYqL1pDAd4iCIiZAwPh3RSwl3vBsw1"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422109,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
      "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422109,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
      "balance": 40000000000000
    },
    {
      "account": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422108,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422108,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhAfvOLnmWDSh90jnvPgmG70f3d2IZLW+I2uGwrrP+dtsvuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEkBSWB1OjORco76q2A8vEU2o8JWlfshF/r85oBmePSbLigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZReiSB/u9AEhoetUuwm6soa8hsj6ego/SKIRrHNLwSFQSgKd/+s33QZ6npQCbkXCNYqL1pDAd4iCIiZAwPh3RSwl3vBsw1",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL4vKCgEAhj+qJSJgALDvQAGgJAUlgdTozkXKO+qtgPLxFNqPCVpX7IRf6/OaAZnj0myLygoBAIYkYTnKgABfYOiQ"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422107,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
      "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422107,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
      "balance": 70000000000000
    },
    {
      "account": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
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
    "from": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
    "to": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
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
        "from": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
        "to": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
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
    "from": "ABCDEF",
    "to": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
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
    "from": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
        "to": "ABCDEF"
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
    "from": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
    "meta": 17,
    "to": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
        "meta": 17,
        "to": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
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
    "from": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
    "to": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlF6JIH+70ASGh61S7CbqyhryGyPp6Cj9IohGsc0vBIVBaDCaGtiit/fPfcxGhGuNoESdbcaRwWh3zKAsXgcdeXdPLfZ8SE=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
          "op": "OffChainTransfer",
          "to": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
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
  "id": -576460752303422106,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAfvOLnmWDSh90jnvPgmG70f3d2IZLW+I2uGwrrP+dtsvuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBlF6JIH+70ASGh61S7CbqyhryGyPp6Cj9IohGsc0vBIVBaDCaGtiit/fPfcxGhGuNoESdbcaRwWh3zKAsXgcdeXdPGVb85w="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422106,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
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
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAfvOLnmWDSh90jnvPgmG70f3d2IZLW+I2uGwrrP+dtsvuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBlF6JIH+70ASGh61S7CbqyhryGyPp6Cj9IohGsc0vBIVBaDCaGtiit/fPfcxGhGuNoESdbcaRwWh3zKAsXgcdeXdPGVb85w=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
          "op": "OffChainTransfer",
          "to": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
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
  "id": -576460752303422105,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JsuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQH7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL7igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZReiSB/u9AEhoetUuwm6soa8hsj6ego/SKIRrHNLwSFQWgwmhrYorf3z33MRoRrjaBEnW3GkcFod8ygLF4HHXl3TxOVdzO"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422105,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JsuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQH7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL7igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZReiSB/u9AEhoetUuwm6soa8hsj6ego/SKIRrHNLwSFQWgwmhrYorf3z33MRoRrjaBEnW3GkcFod8ygLF4HHXl3TxOVdzO"
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
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JsuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQH7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL7igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZReiSB/u9AEhoetUuwm6soa8hsj6ego/SKIRrHNLwSFQWgwmhrYorf3z33MRoRrjaBEnW3GkcFod8ygLF4HHXl3TxOVdzO"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422104,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
      "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422104,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
      "balance": 69999999999999
    },
    {
      "account": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422103,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422103,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JsuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQH7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL7igAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZReiSB/u9AEhoetUuwm6soa8hsj6ego/SKIRrHNLwSFQWgwmhrYorf3z33MRoRrjaBEnW3GkcFod8ygLF4HHXl3TxOVdzO",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL4vKCgEAhj+qJSJf/7DvQAGgJAUlgdTozkXKO+qtgPLxFNqPCVpX7IRf6/OaAZnj0myLygoBAIYkYTnKgAGRWhB0"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422102,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
      "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422102,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
      "balance": 40000000000001
    },
    {
      "account": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
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
    "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
    "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
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
        "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
        "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
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
    "from": "ABCDEF",
    "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
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
    "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
        "to": "ABCDEF"
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
    "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
    "meta": 17,
    "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
        "meta": 17,
        "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
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
    "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
    "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBlF6JIH+70ASGh61S7CbqyhryGyPp6Cj9IohGsc0vBIVBqAp3/6zfdBnqelAJuRcI1iovWkMB3iIIiJkDA+HdFLCXfxhGg8=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
          "op": "OffChainTransfer",
          "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
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
  "id": -576460752303422101,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JsuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBlF6JIH+70ASGh61S7CbqyhryGyPp6Cj9IohGsc0vBIVBqAp3/6zfdBnqelAJuRcI1iovWkMB3iIIiJkDA+HdFLCXQYoBWc="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422101,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
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
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhASQFJYHU6M5FyjvqrYDy8RTajwlaV+yEX+vzmgGZ49JsuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBlF6JIH+70ASGh61S7CbqyhryGyPp6Cj9IohGsc0vBIVBqAp3/6zfdBnqelAJuRcI1iovWkMB3iIIiJkDA+HdFLCXQYoBWc=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
          "op": "OffChainTransfer",
          "to": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
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
  "id": -576460752303422100,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhAfvOLnmWDSh90jnvPgmG70f3d2IZLW+I2uGwrrP+dtsvuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEkBSWB1OjORco76q2A8vEU2o8JWlfshF/r85oBmePSbLigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZReiSB/u9AEhoetUuwm6soa8hsj6ego/SKIRrHNLwSFQagKd/+s33QZ6npQCbkXCNYqL1pDAd4iCIiZAwPh3RSwl1bMzoK"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422100,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhAfvOLnmWDSh90jnvPgmG70f3d2IZLW+I2uGwrrP+dtsvuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEkBSWB1OjORco76q2A8vEU2o8JWlfshF/r85oBmePSbLigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZReiSB/u9AEhoetUuwm6soa8hsj6ego/SKIRrHNLwSFQagKd/+s33QZ6npQCbkXCNYqL1pDAd4iCIiZAwPh3RSwl1bMzoK"
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
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "state": "tx_+QIbCwHAuQIV+QISUQGhAfvOLnmWDSh90jnvPgmG70f3d2IZLW+I2uGwrrP+dtsvuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEkBSWB1OjORco76q2A8vEU2o8JWlfshF/r85oBmePSbLigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZReiSB/u9AEhoetUuwm6soa8hsj6ego/SKIRrHNLwSFQagKd/+s33QZ6npQCbkXCNYqL1pDAd4iCIiZAwPh3RSwl1bMzoK"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422099,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
      "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422099,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_Gs5wcpoeRMeajCA54UhsFVkJur2YvWG2r8wjrAVLkz4ti8KMu",
      "balance": 40000000000000
    },
    {
      "account": "ak_2uu2nwjyroZxcGmFme71uJG1YmANE1rV6G2LqBKHsTrZXA9YTf",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422098,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422098,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QIbCwHAuQIV+QISUQGhAfvOLnmWDSh90jnvPgmG70f3d2IZLW+I2uGwrrP+dtsvuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALkBNvkBMwsBwLkBLfkBKlEBoQEkBSWB1OjORco76q2A8vEU2o8JWlfshF/r85oBmePSbLigAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDpTwOEYZyq5BrDt/dyyj+XaPtLSGilgz4dvLHNcvYrfwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACoAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQGHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZReiSB/u9AEhoetUuwm6soa8hsj6ego/SKIRrHNLwSFQagKd/+s33QZ6npQCbkXCNYqL1pDAd4iCIiZAwPh3RSwl1bMzoK",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaD7zi55lg0ofdI57z4Jhu9H93diGS1viNrhsK6z/nbbL4vKCgEAhj+qJSJgALDvQAGgJAUlgdTozkXKO+qtgPLxFNqPCVpX7IRf6/OaAZnj0myLygoBAIYkYTnKgABfYOiQ"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422097,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
  "id": -576460752303422097,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_ctDyQorH9RYkXmVm6WaMoR9tn9DnLHHRimuKn41RsKd6PRW4C",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422096,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU&keep_running=false&lock_period=10&port=12524&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU&role=initiator
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_bfxnwYVz6rdv5vLwa0KSZTgaku39a/UW1pOBYxcJDggdBom7"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU&keep_running=false&lock_period=10&port=12524&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU&role=responder
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_naUIzz3fEpqDJwQahSZ6IHqZSuwjTdBvZifWbFdD8AYGaaS6"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

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

#### responder info
> Received an WebSocket opening request

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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbBNsa7l6b2Yjm8NEvu1TlYmaeKQOjoAa7OUKhE6AUOAhj+qJSJgAKEBnq/tAoBd/OZ16eykptvP35nanOk2z3vYyrC0qtDf77GGJGE5yoAAAgoAhhAGeddIAMCgimGXThHamcBcrdPUEvHPj9Slt2maroILDJ5qDCiNauMA8wUPzw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421478,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+NQLAcC4z/jNUQGhAbBNsa7l6b2Yjm8NEvu1TlYmaeKQOjoAa7OUKhE6AUOAiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQGwTbGu5em9mI5vDRL7tU5WJmnikDo6AGuzlCoROgFDgIY/qiUiYAChAZ6v7QKAXfzmdenspKbbz9+Z2pzpNs972MqwtKrQ3++xhiRhOcqAAAIKAIYQBnnXSADAoIphl04R2pnAXK3T1BLxz4/Upbdpmq6CCwyeagwojWrjADri//w="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421478,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
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
      "signed_tx": "tx_+NQLAcC4z/jNUQGhAbBNsa7l6b2Yjm8NEvu1TlYmaeKQOjoAa7OUKhE6AUOAiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQGwTbGu5em9mI5vDRL7tU5WJmnikDo6AGuzlCoROgFDgIY/qiUiYAChAZ6v7QKAXfzmdenspKbbz9+Z2pzpNs972MqwtKrQ3++xhiRhOcqAAAIKAIYQBnnXSADAoIphl04R2pnAXK3T1BLxz4/Upbdpmq6CCwyeagwojWrjADri//w=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421477,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEiCwHAuQEc+QEZUQGhAZ6v7QKAXfzmdenspKbbz9+Z2pzpNs972MqwtKrQ3++xiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQGwTbGu5em9mI5vDRL7tU5WJmnikDo6AGuzlCoROgFDgIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBsE2xruXpvZiObw0S+7VOViZp4pA6OgBrs5QqEToBQ4CGP6olImAAoQGer+0CgF385nXp7KSm28/fmdqc6TbPe9jKsLSq0N/vsYYkYTnKgAACCgCGEAZ510gAwKCKYZdOEdqZwFyt09QS8c+P1KW3aZquggsMnmoMKI1q4wDJpJ7b"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421477,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEiCwHAuQEc+QEZUQGhAZ6v7QKAXfzmdenspKbbz9+Z2pzpNs972MqwtKrQ3++xiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQGwTbGu5em9mI5vDRL7tU5WJmnikDo6AGuzlCoROgFDgIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBsE2xruXpvZiObw0S+7VOViZp4pA6OgBrs5QqEToBQ4CGP6olImAAoQGer+0CgF385nXp7KSm28/fmdqc6TbPe9jKsLSq0N/vsYYkYTnKgAACCgCGEAZ510gAwKCKYZdOEdqZwFyt09QS8c+P1KW3aZquggsMnmoMKI1q4wDJpJ7b",
      "type": "channel_create_tx"
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
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEiCwHAuQEc+QEZUQGhAZ6v7QKAXfzmdenspKbbz9+Z2pzpNs972MqwtKrQ3++xiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQGwTbGu5em9mI5vDRL7tU5WJmnikDo6AGuzlCoROgFDgIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBsE2xruXpvZiObw0S+7VOViZp4pA6OgBrs5QqEToBQ4CGP6olImAAoQGer+0CgF385nXp7KSm28/fmdqc6TbPe9jKsLSq0N/vsYYkYTnKgAACCgCGEAZ510gAwKCKYZdOEdqZwFyt09QS8c+P1KW3aZquggsMnmoMKI1q4wDJpJ7b",
      "type": "channel_create_tx"
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
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEiCwHAuQEc+QEZUQGhAZ6v7QKAXfzmdenspKbbz9+Z2pzpNs972MqwtKrQ3++xiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQGwTbGu5em9mI5vDRL7tU5WJmnikDo6AGuzlCoROgFDgIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBsE2xruXpvZiObw0S+7VOViZp4pA6OgBrs5QqEToBQ4CGP6olImAAoQGer+0CgF385nXp7KSm28/fmdqc6TbPe9jKsLSq0N/vsYYkYTnKgAACCgCGEAZ510gAwKCKYZdOEdqZwFyt09QS8c+P1KW3aZquggsMnmoMKI1q4wDJpJ7b",
      "type": "channel_create_tx"
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
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEiCwHAuQEc+QEZUQGhAZ6v7QKAXfzmdenspKbbz9+Z2pzpNs972MqwtKrQ3++xiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQGwTbGu5em9mI5vDRL7tU5WJmnikDo6AGuzlCoROgFDgIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBsE2xruXpvZiObw0S+7VOViZp4pA6OgBrs5QqEToBQ4CGP6olImAAoQGer+0CgF385nXp7KSm28/fmdqc6TbPe9jKsLSq0N/vsYYkYTnKgAACCgCGEAZ510gAwKCKYZdOEdqZwFyt09QS8c+P1KW3aZquggsMnmoMKI1q4wDJpJ7b",
      "type": "channel_create_tx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello",
    "to": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "message": {
        "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
        "from": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
        "info": "Hello",
        "to": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
      }
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
    "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "message": {
        "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
        "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
        "info": "Hello back",
        "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421476,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
      "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421476,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
      "balance": 69999999999999
    },
    {
      "account": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
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
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
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
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
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
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "state": "tx_+QEiCwHAuQEc+QEZUQGhAZ6v7QKAXfzmdenspKbbz9+Z2pzpNs972MqwtKrQ3++xiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQGwTbGu5em9mI5vDRL7tU5WJmnikDo6AGuzlCoROgFDgIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBsE2xruXpvZiObw0S+7VOViZp4pA6OgBrs5QqEToBQ4CGP6olImAAoQGer+0CgF385nXp7KSm28/fmdqc6TbPe9jKsLSq0N/vsYYkYTnKgAACCgCGEAZ510gAwKCKYZdOEdqZwFyt09QS8c+P1KW3aZquggsMnmoMKI1q4wDJpJ7b"
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
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
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
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "state": "tx_+QEiCwHAuQEc+QEZUQGhAZ6v7QKAXfzmdenspKbbz9+Z2pzpNs972MqwtKrQ3++xiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC41vjUCwHAuM/4zVEBoQGwTbGu5em9mI5vDRL7tU5WJmnikDo6AGuzlCoROgFDgIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuIr4iAsBwLiD+IEyAaEBsE2xruXpvZiObw0S+7VOViZp4pA6OgBrs5QqEToBQ4CGP6olImAAoQGer+0CgF385nXp7KSm28/fmdqc6TbPe9jKsLSq0N/vsYYkYTnKgAACCgCGEAZ510gAwKCKYZdOEdqZwFyt09QS8c+P1KW3aZquggsMnmoMKI1q4wDJpJ7b"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421475,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
      "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421475,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
      "balance": 69999999999999
    },
    {
      "account": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
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
    "from": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
    "to": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
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
        "from": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
        "to": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
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
    "from": "ABCDEF",
    "to": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
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
    "from": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
        "to": "ABCDEF"
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
    "from": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
    "meta": 17,
    "to": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
        "meta": 17,
        "to": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
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
    "from": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
    "to": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmBjfARGYP8DMlAzxhx14yYSKLEMPDwYLwrqaXuA0eBPAqAdnWGRj25z4IWdCaEDgFAHwXme8Afw8lhJlFxvImXDTDZeL44=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
          "op": "OffChainTransfer",
          "to": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
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
  "id": -576460752303421474,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAbBNsa7l6b2Yjm8NEvu1TlYmaeKQOjoAa7OUKhE6AUOAiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZgY3wERmD/AzJQM8YcdeMmEiixDDw8GC8K6ml7gNHgTwKgHZ1hkY9uc+CFnQmhA4BQB8F5nvAH8PJYSZRcbyJlw0xI92/+"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421474,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
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
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAbBNsa7l6b2Yjm8NEvu1TlYmaeKQOjoAa7OUKhE6AUOAiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZgY3wERmD/AzJQM8YcdeMmEiixDDw8GC8K6ml7gNHgTwKgHZ1hkY9uc+CFnQmhA4BQB8F5nvAH8PJYSZRcbyJlw0xI92/+",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
          "op": "OffChainTransfer",
          "to": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
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
  "id": -576460752303421473,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhAZ6v7QKAXfzmdenspKbbz9+Z2pzpNs972MqwtKrQ3++xiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGwTbGu5em9mI5vDRL7tU5WJmnikDo6AGuzlCoROgFDgIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGYGN8BEZg/wMyUDPGHHXjJhIosQw8PBgvCuppe4DR4E8CoB2dYZGPbnPghZ0JoQOAUAfBeZ7wB/DyWEmUXG8iZcNMwYuiwQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421473,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAZ6v7QKAXfzmdenspKbbz9+Z2pzpNs972MqwtKrQ3++xiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGwTbGu5em9mI5vDRL7tU5WJmnikDo6AGuzlCoROgFDgIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGYGN8BEZg/wMyUDPGHHXjJhIosQw8PBgvCuppe4DR4E8CoB2dYZGPbnPghZ0JoQOAUAfBeZ7wB/DyWEmUXG8iZcNMwYuiwQ=="
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
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAZ6v7QKAXfzmdenspKbbz9+Z2pzpNs972MqwtKrQ3++xiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGwTbGu5em9mI5vDRL7tU5WJmnikDo6AGuzlCoROgFDgIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGYGN8BEZg/wMyUDPGHHXjJhIosQw8PBgvCuppe4DR4E8CoB2dYZGPbnPghZ0JoQOAUAfBeZ7wB/DyWEmUXG8iZcNMwYuiwQ=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421472,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
      "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421472,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
      "balance": 69999999999998
    },
    {
      "account": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421471,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421471,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhAZ6v7QKAXfzmdenspKbbz9+Z2pzpNs972MqwtKrQ3++xiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGwTbGu5em9mI5vDRL7tU5WJmnikDo6AGuzlCoROgFDgIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGYGN8BEZg/wMyUDPGHHXjJhIosQw8PBgvCuppe4DR4E8CoB2dYZGPbnPghZ0JoQOAUAfBeZ7wB/DyWEmUXG8iZcNMwYuiwQ==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCwTbGu5em9mI5vDRL7tU5WJmnikDo6AGuzlCoROgFDgIvKCgEAhj+qJSJf/rDvQAGgnq/tAoBd/OZ16eykptvP35nanOk2z3vYyrC0qtDf77GLygoBAIYkYTnKgAIIyL9d"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421470,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
      "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421470,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
      "balance": 40000000000002
    },
    {
      "account": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
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
    "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
    "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
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
        "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
        "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
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
    "from": "ABCDEF",
    "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
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
    "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
        "to": "ABCDEF"
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
    "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
    "meta": 17,
    "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
        "meta": 17,
        "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
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
    "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
    "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmBjfARGYP8DMlAzxhx14yYSKLEMPDwYLwrqaXuA0eBPA6CKYZdOEdqZwFyt09QS8c+P1KW3aZquggsMnmoMKI1q49ryDWQ=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
          "op": "OffChainTransfer",
          "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
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
  "id": -576460752303421469,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAZ6v7QKAXfzmdenspKbbz9+Z2pzpNs972MqwtKrQ3++xiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZgY3wERmD/AzJQM8YcdeMmEiixDDw8GC8K6ml7gNHgTwOgimGXThHamcBcrdPUEvHPj9Slt2maroILDJ5qDCiNauNQfIFb"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421469,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
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
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAZ6v7QKAXfzmdenspKbbz9+Z2pzpNs972MqwtKrQ3++xiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZgY3wERmD/AzJQM8YcdeMmEiixDDw8GC8K6ml7gNHgTwOgimGXThHamcBcrdPUEvHPj9Slt2maroILDJ5qDCiNauNQfIFb",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
          "op": "OffChainTransfer",
          "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
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
  "id": -576460752303421468,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhAbBNsa7l6b2Yjm8NEvu1TlYmaeKQOjoAa7OUKhE6AUOAiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGer+0CgF385nXp7KSm28/fmdqc6TbPe9jKsLSq0N/vsYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGYGN8BEZg/wMyUDPGHHXjJhIosQw8PBgvCuppe4DR4E8DoIphl04R2pnAXK3T1BLxz4/Upbdpmq6CCwyeagwojWrjEIumCg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421468,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAbBNsa7l6b2Yjm8NEvu1TlYmaeKQOjoAa7OUKhE6AUOAiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGer+0CgF385nXp7KSm28/fmdqc6TbPe9jKsLSq0N/vsYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGYGN8BEZg/wMyUDPGHHXjJhIosQw8PBgvCuppe4DR4E8DoIphl04R2pnAXK3T1BLxz4/Upbdpmq6CCwyeagwojWrjEIumCg=="
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
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAbBNsa7l6b2Yjm8NEvu1TlYmaeKQOjoAa7OUKhE6AUOAiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGer+0CgF385nXp7KSm28/fmdqc6TbPe9jKsLSq0N/vsYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGYGN8BEZg/wMyUDPGHHXjJhIosQw8PBgvCuppe4DR4E8DoIphl04R2pnAXK3T1BLxz4/Upbdpmq6CCwyeagwojWrjEIumCg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421467,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
      "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421467,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
      "balance": 40000000000001
    },
    {
      "account": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421466,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421466,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhAbBNsa7l6b2Yjm8NEvu1TlYmaeKQOjoAa7OUKhE6AUOAiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGer+0CgF385nXp7KSm28/fmdqc6TbPe9jKsLSq0N/vsYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGYGN8BEZg/wMyUDPGHHXjJhIosQw8PBgvCuppe4DR4E8DoIphl04R2pnAXK3T1BLxz4/Upbdpmq6CCwyeagwojWrjEIumCg==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCwTbGu5em9mI5vDRL7tU5WJmnikDo6AGuzlCoROgFDgIvKCgEAhj+qJSJf/7DvQAGgnq/tAoBd/OZ16eykptvP35nanOk2z3vYyrC0qtDf77GLygoBAIYkYTnKgAFkQGTz"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421465,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
      "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421465,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
      "balance": 40000000000001
    },
    {
      "account": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
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
    "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
    "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
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
        "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
        "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
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
    "from": "ABCDEF",
    "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
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
    "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
        "to": "ABCDEF"
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
    "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
    "meta": 17,
    "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
        "meta": 17,
        "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
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
    "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
    "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmBjfARGYP8DMlAzxhx14yYSKLEMPDwYLwrqaXuA0eBPBKD0f8KLUwRFNa1jU0pFM7jLTD/YIsi+RKrAAmDYFLHUWfMC29c=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
          "op": "OffChainTransfer",
          "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
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
  "id": -576460752303421464,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAZ6v7QKAXfzmdenspKbbz9+Z2pzpNs972MqwtKrQ3++xiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZgY3wERmD/AzJQM8YcdeMmEiixDDw8GC8K6ml7gNHgTwSg9H/Ci1MERTWtY1NKRTO4y0w/2CLIvkSqwAJg2BSx1FkOqpku"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421464,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
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
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAZ6v7QKAXfzmdenspKbbz9+Z2pzpNs972MqwtKrQ3++xiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZgY3wERmD/AzJQM8YcdeMmEiixDDw8GC8K6ml7gNHgTwSg9H/Ci1MERTWtY1NKRTO4y0w/2CLIvkSqwAJg2BSx1FkOqpku",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
          "op": "OffChainTransfer",
          "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
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
  "id": -576460752303421463,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhAbBNsa7l6b2Yjm8NEvu1TlYmaeKQOjoAa7OUKhE6AUOAiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGer+0CgF385nXp7KSm28/fmdqc6TbPe9jKsLSq0N/vsYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGYGN8BEZg/wMyUDPGHHXjJhIosQw8PBgvCuppe4DR4E8EoPR/wotTBEU1rWNTSkUzuMtMP9giyL5EqsACYNgUsdRZFtez7w=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421463,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAbBNsa7l6b2Yjm8NEvu1TlYmaeKQOjoAa7OUKhE6AUOAiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGer+0CgF385nXp7KSm28/fmdqc6TbPe9jKsLSq0N/vsYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGYGN8BEZg/wMyUDPGHHXjJhIosQw8PBgvCuppe4DR4E8EoPR/wotTBEU1rWNTSkUzuMtMP9giyL5EqsACYNgUsdRZFtez7w=="
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
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAbBNsa7l6b2Yjm8NEvu1TlYmaeKQOjoAa7OUKhE6AUOAiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGer+0CgF385nXp7KSm28/fmdqc6TbPe9jKsLSq0N/vsYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGYGN8BEZg/wMyUDPGHHXjJhIosQw8PBgvCuppe4DR4E8EoPR/wotTBEU1rWNTSkUzuMtMP9giyL5EqsACYNgUsdRZFtez7w=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421462,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
      "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421462,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
      "balance": 40000000000000
    },
    {
      "account": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421461,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421461,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhAbBNsa7l6b2Yjm8NEvu1TlYmaeKQOjoAa7OUKhE6AUOAiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGer+0CgF385nXp7KSm28/fmdqc6TbPe9jKsLSq0N/vsYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGYGN8BEZg/wMyUDPGHHXjJhIosQw8PBgvCuppe4DR4E8EoPR/wotTBEU1rWNTSkUzuMtMP9giyL5EqsACYNgUsdRZFtez7w==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCwTbGu5em9mI5vDRL7tU5WJmnikDo6AGuzlCoROgFDgIvKCgEAhj+qJSJgALDvQAGgnq/tAoBd/OZ16eykptvP35nanOk2z3vYyrC0qtDf77GLygoBAIYkYTnKgAALe0NI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421460,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
      "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421460,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
      "balance": 70000000000000
    },
    {
      "account": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
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
    "from": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
    "to": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
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
        "from": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
        "to": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
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
    "from": "ABCDEF",
    "to": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
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
    "from": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
        "to": "ABCDEF"
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
    "from": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
    "meta": 17,
    "to": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
        "meta": 17,
        "to": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
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
    "from": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
    "to": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmBjfARGYP8DMlAzxhx14yYSKLEMPDwYLwrqaXuA0eBPBaCKYZdOEdqZwFyt09QS8c+P1KW3aZquggsMnmoMKI1q4+I8dos=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
          "op": "OffChainTransfer",
          "to": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
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
  "id": -576460752303421459,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAbBNsa7l6b2Yjm8NEvu1TlYmaeKQOjoAa7OUKhE6AUOAiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZgY3wERmD/AzJQM8YcdeMmEiixDDw8GC8K6ml7gNHgTwWgimGXThHamcBcrdPUEvHPj9Slt2maroILDJ5qDCiNauOB3jvl"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421459,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
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
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAbBNsa7l6b2Yjm8NEvu1TlYmaeKQOjoAa7OUKhE6AUOAiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZgY3wERmD/AzJQM8YcdeMmEiixDDw8GC8K6ml7gNHgTwWgimGXThHamcBcrdPUEvHPj9Slt2maroILDJ5qDCiNauOB3jvl",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
          "op": "OffChainTransfer",
          "to": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
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
  "id": -576460752303421458,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhAZ6v7QKAXfzmdenspKbbz9+Z2pzpNs972MqwtKrQ3++xiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGwTbGu5em9mI5vDRL7tU5WJmnikDo6AGuzlCoROgFDgIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGYGN8BEZg/wMyUDPGHHXjJhIosQw8PBgvCuppe4DR4E8FoIphl04R2pnAXK3T1BLxz4/Upbdpmq6CCwyeagwojWrjazkDLw=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421458,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAZ6v7QKAXfzmdenspKbbz9+Z2pzpNs972MqwtKrQ3++xiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGwTbGu5em9mI5vDRL7tU5WJmnikDo6AGuzlCoROgFDgIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGYGN8BEZg/wMyUDPGHHXjJhIosQw8PBgvCuppe4DR4E8FoIphl04R2pnAXK3T1BLxz4/Upbdpmq6CCwyeagwojWrjazkDLw=="
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
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAZ6v7QKAXfzmdenspKbbz9+Z2pzpNs972MqwtKrQ3++xiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGwTbGu5em9mI5vDRL7tU5WJmnikDo6AGuzlCoROgFDgIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGYGN8BEZg/wMyUDPGHHXjJhIosQw8PBgvCuppe4DR4E8FoIphl04R2pnAXK3T1BLxz4/Upbdpmq6CCwyeagwojWrjazkDLw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421457,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
      "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421457,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
      "balance": 69999999999999
    },
    {
      "account": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421456,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421456,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhAZ6v7QKAXfzmdenspKbbz9+Z2pzpNs972MqwtKrQ3++xiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGwTbGu5em9mI5vDRL7tU5WJmnikDo6AGuzlCoROgFDgIkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGYGN8BEZg/wMyUDPGHHXjJhIosQw8PBgvCuppe4DR4E8FoIphl04R2pnAXK3T1BLxz4/Upbdpmq6CCwyeagwojWrjazkDLw==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCwTbGu5em9mI5vDRL7tU5WJmnikDo6AGuzlCoROgFDgIvKCgEAhj+qJSJf/7DvQAGgnq/tAoBd/OZ16eykptvP35nanOk2z3vYyrC0qtDf77GLygoBAIYkYTnKgAFkQGTz"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421455,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
      "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421455,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
      "balance": 40000000000001
    },
    {
      "account": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
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
    "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
    "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
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
        "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
        "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
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
    "from": "ABCDEF",
    "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
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
    "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
        "to": "ABCDEF"
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
    "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
    "meta": 17,
    "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
        "meta": 17,
        "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
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
    "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
    "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmBjfARGYP8DMlAzxhx14yYSKLEMPDwYLwrqaXuA0eBPBqD0f8KLUwRFNa1jU0pFM7jLTD/YIsi+RKrAAmDYFLHUWbLIw0M=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
          "op": "OffChainTransfer",
          "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
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
  "id": -576460752303421454,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAZ6v7QKAXfzmdenspKbbz9+Z2pzpNs972MqwtKrQ3++xiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZgY3wERmD/AzJQM8YcdeMmEiixDDw8GC8K6ml7gNHgTwag9H/Ci1MERTWtY1NKRTO4y0w/2CLIvkSqwAJg2BSx1Fnr83IT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421454,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
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
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAZ6v7QKAXfzmdenspKbbz9+Z2pzpNs972MqwtKrQ3++xiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQZgY3wERmD/AzJQM8YcdeMmEiixDDw8GC8K6ml7gNHgTwag9H/Ci1MERTWtY1NKRTO4y0w/2CLIvkSqwAJg2BSx1Fnr83IT",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
          "op": "OffChainTransfer",
          "to": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
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
  "id": -576460752303421453,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+OULAcC44PjeUQGhAbBNsa7l6b2Yjm8NEvu1TlYmaeKQOjoAa7OUKhE6AUOAiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGer+0CgF385nXp7KSm28/fmdqc6TbPe9jKsLSq0N/vsYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGYGN8BEZg/wMyUDPGHHXjJhIosQw8PBgvCuppe4DR4E8GoPR/wotTBEU1rWNTSkUzuMtMP9giyL5EqsACYNgUsdRZCLz2MA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421453,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAbBNsa7l6b2Yjm8NEvu1TlYmaeKQOjoAa7OUKhE6AUOAiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGer+0CgF385nXp7KSm28/fmdqc6TbPe9jKsLSq0N/vsYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGYGN8BEZg/wMyUDPGHHXjJhIosQw8PBgvCuppe4DR4E8GoPR/wotTBEU1rWNTSkUzuMtMP9giyL5EqsACYNgUsdRZCLz2MA=="
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
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "state": "tx_+OULAcC44PjeUQGhAbBNsa7l6b2Yjm8NEvu1TlYmaeKQOjoAa7OUKhE6AUOAiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGer+0CgF385nXp7KSm28/fmdqc6TbPe9jKsLSq0N/vsYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGYGN8BEZg/wMyUDPGHHXjJhIosQw8PBgvCuppe4DR4E8GoPR/wotTBEU1rWNTSkUzuMtMP9giyL5EqsACYNgUsdRZCLz2MA=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421452,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
      "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421452,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2CtTCsW9M2VMJVpkF5JkE8kxzsr3uZqYRaBaEvvu2wyt2EwzvU",
      "balance": 40000000000000
    },
    {
      "account": "ak_2LeSJ1cB345bAQiVxDNDdzpnzgGnWvwNp6pZSAxURDFh6RXVGU",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421451,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421451,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+OULAcC44PjeUQGhAbBNsa7l6b2Yjm8NEvu1TlYmaeKQOjoAa7OUKhE6AUOAiSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4m/iZCwHAuJT4klEBoQGer+0CgF385nXp7KSm28/fmdqc6TbPe9jKsLSq0N/vsYkrEWzyVwsrVAIDhwONfqTGgACCTiCF6NSlEAAAuE/4TQsBwLhI+EY5AqEGYGN8BEZg/wMyUDPGHHXjJhIosQw8PBgvCuppe4DR4E8GoPR/wotTBEU1rWNTSkUzuMtMP9giyL5EqsACYNgUsdRZCLz2MA==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCwTbGu5em9mI5vDRL7tU5WJmnikDo6AGuzlCoROgFDgIvKCgEAhj+qJSJgALDvQAGgnq/tAoBd/OZ16eykptvP35nanOk2z3vYyrC0qtDf77GLygoBAIYkYTnKgAALe0NI"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421450,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421450,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421449,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
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
  "channel_id": "ch_jT7pxJxKQPAfcnAPmNF2GrQyrZP5DsQF7MapPsm2ZezdBUfJU",
  "id": -576460752303421449,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
