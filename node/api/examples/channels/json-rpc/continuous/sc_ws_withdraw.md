
#### initiator ---> node (2019-03-13 11:05:24.337)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- node (2019-03-13 11:05:24.364)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "tx": "tx_+HI0AaEGvlKRORFMQ6yZVoRRHcALKMj/ey09I/8FJv6O9Cm+7QahASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAgCGEjCc5UAAoPeVP4c5REs7Ro3xD/VmeKnktP8HlqXCce2XRZO8itFEBAi4xMtX"
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:24.374)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "tx": "tx_+LwLAfhCuEA3KLKX3ex+xWczP9inVYtuq4ljtGXBJoekld23p/fQOdWb1Y5drOJl8vfVJ3QXS68o1GlYl9X6jK+rmLvqJgsCuHT4cjQBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cCAIYSMJzlQACg95U/hzlESztGjfEP9WZ4qeS0/weWpcJx7ZdFk7yK0UQECMFWzIA="
  }
}
```

#### responder <--- node (2019-03-13 11:05:24.398)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:24.399)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "tx": "tx_+HI0AaEGvlKRORFMQ6yZVoRRHcALKMj/ey09I/8FJv6O9Cm+7QahASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAgCGEjCc5UAAoPeVP4c5REs7Ro3xD/VmeKnktP8HlqXCce2XRZO8itFEBAi4xMtX"
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:05:24.400)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "tx": "tx_+LwLAfhCuEBji8qm7PTQ5KDqrLlWbJF3/ZP8mkb8DrteXe3r+Qzvpcb66lnWBAFAn7af2HY+ioRSE4aKULtOyelPBqWg2lIIuHT4cjQBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cCAIYSMJzlQACg95U/hzlESztGjfEP9WZ4qeS0/weWpcJx7ZdFk7yK0UQECPLgW34="
  }
}
```

#### responder <--- node (2019-03-13 11:05:24.415)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "tx": "tx_+P4LAfiEuEA3KLKX3ex+xWczP9inVYtuq4ljtGXBJoekld23p/fQOdWb1Y5drOJl8vfVJ3QXS68o1GlYl9X6jK+rmLvqJgsCuEBji8qm7PTQ5KDqrLlWbJF3/ZP8mkb8DrteXe3r+Qzvpcb66lnWBAFAn7af2HY+ioRSE4aKULtOyelPBqWg2lIIuHT4cjQBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cCAIYSMJzlQACg95U/hzlESztGjfEP9WZ4qeS0/weWpcJx7ZdFk7yK0UQECNGtmgY="
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:24.428)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "tx": "tx_+P4LAfiEuEA3KLKX3ex+xWczP9inVYtuq4ljtGXBJoekld23p/fQOdWb1Y5drOJl8vfVJ3QXS68o1GlYl9X6jK+rmLvqJgsCuEBji8qm7PTQ5KDqrLlWbJF3/ZP8mkb8DrteXe3r+Qzvpcb66lnWBAFAn7af2HY+ioRSE4aKULtOyelPBqWg2lIIuHT4cjQBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cCAIYSMJzlQACg95U/hzlESztGjfEP9WZ4qeS0/weWpcJx7ZdFk7yK0UQECNGtmgY="
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:31.900)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "own_withdraw_locked"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:31.904)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "own_withdraw_locked"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:31.909)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "withdraw_locked"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:31.912)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "withdraw_locked"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:31.934)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "state": "tx_+P4LAfiEuEA3KLKX3ex+xWczP9inVYtuq4ljtGXBJoekld23p/fQOdWb1Y5drOJl8vfVJ3QXS68o1GlYl9X6jK+rmLvqJgsCuEBji8qm7PTQ5KDqrLlWbJF3/ZP8mkb8DrteXe3r+Qzvpcb66lnWBAFAn7af2HY+ioRSE4aKULtOyelPBqWg2lIIuHT4cjQBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cCAIYSMJzlQACg95U/hzlESztGjfEP9WZ4qeS0/weWpcJx7ZdFk7yK0UQECNGtmgY="
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:31.935)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "state": "tx_+P4LAfiEuEA3KLKX3ex+xWczP9inVYtuq4ljtGXBJoekld23p/fQOdWb1Y5drOJl8vfVJ3QXS68o1GlYl9X6jK+rmLvqJgsCuEBji8qm7PTQ5KDqrLlWbJF3/ZP8mkb8DrteXe3r+Qzvpcb66lnWBAFAn7af2HY+ioRSE4aKULtOyelPBqWg2lIIuHT4cjQBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cCAIYSMJzlQACg95U/hzlESztGjfEP9WZ4qeS0/weWpcJx7ZdFk7yK0UQECNGtmgY="
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:05:32.600)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### responder <--- node (2019-03-13 11:05:32.623)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "tx": "tx_+HI0AaEGvlKRORFMQ6yZVoRRHcALKMj/ey09I/8FJv6O9Cm+7QahAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAgCGEjCc5UAAoODtFIhe84yV0+uaXXnfGCrRRApvdISmjmGVfhKf0nkoBQPoNTrE"
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:05:32.624)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "tx": "tx_+LwLAfhCuECqNKDshuFDFn2yCfKMOC7vUG7uqxWTsoH9oKFY7IFb4Q2MdeFni4MMI1FZaQUtA6tOjqeXr/XGipaidpyhgCEDuHT4cjQBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA208CAIYSMJzlQACg4O0UiF7zjJXT65pded8YKtFECm90hKaOYZV+Ep/SeSgFA+RSVmQ="
  }
}
```

#### initiator <--- node (2019-03-13 11:05:32.652)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:32.666)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "tx": "tx_+HI0AaEGvlKRORFMQ6yZVoRRHcALKMj/ey09I/8FJv6O9Cm+7QahAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAgCGEjCc5UAAoODtFIhe84yV0+uaXXnfGCrRRApvdISmjmGVfhKf0nkoBQPoNTrE"
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:32.668)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "tx": "tx_+LwLAfhCuEDuowr1DibhbU3ia45UGxy2Q4tWDoL5IyaqEjzDo8rXlfqvIAXmYwYMYU4yH1mHUVKhMTVFVuSxhnLI9/e4VuYKuHT4cjQBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA208CAIYSMJzlQACg4O0UiF7zjJXT65pded8YKtFECm90hKaOYZV+Ep/SeSgFA87ibCs="
  }
}
```

#### initiator <--- node (2019-03-13 11:05:32.697)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "tx": "tx_+P4LAfiEuECqNKDshuFDFn2yCfKMOC7vUG7uqxWTsoH9oKFY7IFb4Q2MdeFni4MMI1FZaQUtA6tOjqeXr/XGipaidpyhgCEDuEDuowr1DibhbU3ia45UGxy2Q4tWDoL5IyaqEjzDo8rXlfqvIAXmYwYMYU4yH1mHUVKhMTVFVuSxhnLI9/e4VuYKuHT4cjQBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA208CAIYSMJzlQACg4O0UiF7zjJXT65pded8YKtFECm90hKaOYZV+Ep/SeSgFA8yeIaA="
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:32.709)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "tx": "tx_+P4LAfiEuECqNKDshuFDFn2yCfKMOC7vUG7uqxWTsoH9oKFY7IFb4Q2MdeFni4MMI1FZaQUtA6tOjqeXr/XGipaidpyhgCEDuEDuowr1DibhbU3ia45UGxy2Q4tWDoL5IyaqEjzDo8rXlfqvIAXmYwYMYU4yH1mHUVKhMTVFVuSxhnLI9/e4VuYKuHT4cjQBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA208CAIYSMJzlQACg4O0UiF7zjJXT65pded8YKtFECm90hKaOYZV+Ep/SeSgFA8yeIaA="
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:35.489)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "own_withdraw_locked"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:35.490)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "own_withdraw_locked"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:35.491)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "withdraw_locked"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:35.500)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "withdraw_locked"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:35.512)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "state": "tx_+P4LAfiEuECqNKDshuFDFn2yCfKMOC7vUG7uqxWTsoH9oKFY7IFb4Q2MdeFni4MMI1FZaQUtA6tOjqeXr/XGipaidpyhgCEDuEDuowr1DibhbU3ia45UGxy2Q4tWDoL5IyaqEjzDo8rXlfqvIAXmYwYMYU4yH1mHUVKhMTVFVuSxhnLI9/e4VuYKuHT4cjQBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA208CAIYSMJzlQACg4O0UiF7zjJXT65pded8YKtFECm90hKaOYZV+Ep/SeSgFA8yeIaA="
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:35.513)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "state": "tx_+P4LAfiEuECqNKDshuFDFn2yCfKMOC7vUG7uqxWTsoH9oKFY7IFb4Q2MdeFni4MMI1FZaQUtA6tOjqeXr/XGipaidpyhgCEDuEDuowr1DibhbU3ia45UGxy2Q4tWDoL5IyaqEjzDo8rXlfqvIAXmYwYMYU4yH1mHUVKhMTVFVuSxhnLI9/e4VuYKuHT4cjQBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA208CAIYSMJzlQACg4O0UiF7zjJXT65pded8YKtFECm90hKaOYZV+Ep/SeSgFA8yeIaA="
    }
  },
  "version": 1
}
```
