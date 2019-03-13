
#### initiator ---> node (2019-03-13 11:05:13.740)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- node (2019-03-13 11:05:13.769)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "tx": "tx_+HIzAaEGvlKRORFMQ6yZVoRRHcALKMj/ey09I/8FJv6O9Cm+7QahASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAgCGEjCc5UAAoH008j6uxeUVTwp5LGyk9WNSD5Oh7r9RTf0ZLi2pfEolAgeFWSXQ"
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:13.781)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "tx": "tx_+LwLAfhCuEDmV8M+oo3OiOFgJs7iF16iL39QeHcXVIc2JmTPC3xxdApmooXZaLmHktuZgw+5pWlTpO/xE5sdRM33Y6i7GjYDuHT4cjMBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cCAIYSMJzlQACgfTTyPq7F5RVPCnksbKT1Y1IPk6Huv1FN/RkuLal8SiUCB267oBU="
  }
}
```

#### responder <--- node (2019-03-13 11:05:13.807)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:13.812)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "tx": "tx_+HIzAaEGvlKRORFMQ6yZVoRRHcALKMj/ey09I/8FJv6O9Cm+7QahASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAgCGEjCc5UAAoH008j6uxeUVTwp5LGyk9WNSD5Oh7r9RTf0ZLi2pfEolAgeFWSXQ"
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:05:13.813)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "tx": "tx_+LwLAfhCuEAkM7fIOPJx7zvGvTV0Qr8YGjUnWPWLdWPescK503s3+AyBbE0LCqL3edXeV5eFg3Y6g5jNaR8Cv5UNeT0KBfUGuHT4cjMBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cCAIYSMJzlQACgfTTyPq7F5RVPCnksbKT1Y1IPk6Huv1FN/RkuLal8SiUCB8tJPCE="
  }
}
```

#### responder <--- node (2019-03-13 11:05:13.842)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "tx": "tx_+P4LAfiEuEAkM7fIOPJx7zvGvTV0Qr8YGjUnWPWLdWPescK503s3+AyBbE0LCqL3edXeV5eFg3Y6g5jNaR8Cv5UNeT0KBfUGuEDmV8M+oo3OiOFgJs7iF16iL39QeHcXVIc2JmTPC3xxdApmooXZaLmHktuZgw+5pWlTpO/xE5sdRM33Y6i7GjYDuHT4cjMBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cCAIYSMJzlQACgfTTyPq7F5RVPCnksbKT1Y1IPk6Huv1FN/RkuLal8SiUCBzKO4fU="
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:13.888)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "tx": "tx_+P4LAfiEuEAkM7fIOPJx7zvGvTV0Qr8YGjUnWPWLdWPescK503s3+AyBbE0LCqL3edXeV5eFg3Y6g5jNaR8Cv5UNeT0KBfUGuEDmV8M+oo3OiOFgJs7iF16iL39QeHcXVIc2JmTPC3xxdApmooXZaLmHktuZgw+5pWlTpO/xE5sdRM33Y6i7GjYDuHT4cjMBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cCAIYSMJzlQACgfTTyPq7F5RVPCnksbKT1Y1IPk6Huv1FN/RkuLal8SiUCBzKO4fU="
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:16.684)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "own_deposit_locked"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:16.685)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "own_deposit_locked"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:16.686)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "deposit_locked"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:16.686)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "deposit_locked"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:16.700)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "state": "tx_+P4LAfiEuEAkM7fIOPJx7zvGvTV0Qr8YGjUnWPWLdWPescK503s3+AyBbE0LCqL3edXeV5eFg3Y6g5jNaR8Cv5UNeT0KBfUGuEDmV8M+oo3OiOFgJs7iF16iL39QeHcXVIc2JmTPC3xxdApmooXZaLmHktuZgw+5pWlTpO/xE5sdRM33Y6i7GjYDuHT4cjMBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cCAIYSMJzlQACgfTTyPq7F5RVPCnksbKT1Y1IPk6Huv1FN/RkuLal8SiUCBzKO4fU="
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:16.701)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "state": "tx_+P4LAfiEuEAkM7fIOPJx7zvGvTV0Qr8YGjUnWPWLdWPescK503s3+AyBbE0LCqL3edXeV5eFg3Y6g5jNaR8Cv5UNeT0KBfUGuEDmV8M+oo3OiOFgJs7iF16iL39QeHcXVIc2JmTPC3xxdApmooXZaLmHktuZgw+5pWlTpO/xE5sdRM33Y6i7GjYDuHT4cjMBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cCAIYSMJzlQACgfTTyPq7F5RVPCnksbKT1Y1IPk6Huv1FN/RkuLal8SiUCBzKO4fU="
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:05:20.282)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

#### responder <--- node (2019-03-13 11:05:20.309)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "tx": "tx_+HIzAaEGvlKRORFMQ6yZVoRRHcALKMj/ey09I/8FJv6O9Cm+7QahAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAgCGEjCc5UAAoPcACEIhEkXaY4e2KaT80TqJjt0iu553OajAJggpbTqrAwKgxjyK"
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:05:20.310)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "tx": "tx_+LwLAfhCuEAKW+GaYeXcKLZ09Y5Ye72wMx8W+nBIhSUPHGC5KhnQZVHbPhZu/ba0oO/YPi2hOyB5X3onNArJDCFTZRDiuz4MuHT4cjMBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA208CAIYSMJzlQACg9wAIQiESRdpjh7YppPzROomO3SK7nnc5qMAmCCltOqsDAuNp/Ac="
  }
}
```

#### initiator <--- node (2019-03-13 11:05:20.340)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:20.343)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "tx": "tx_+HIzAaEGvlKRORFMQ6yZVoRRHcALKMj/ey09I/8FJv6O9Cm+7QahAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAgCGEjCc5UAAoPcACEIhEkXaY4e2KaT80TqJjt0iu553OajAJggpbTqrAwKgxjyK"
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:20.344)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "tx": "tx_+LwLAfhCuEDbWO6/cGva94ny2r5qBHySARv7zB6lnw/L8jFwKsI+WNfpsrmYlxCH9IUcudigV0Ah+5Fpz3VnztiaJsVXAPgAuHT4cjMBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA208CAIYSMJzlQACg9wAIQiESRdpjh7YppPzROomO3SK7nnc5qMAmCCltOqsDAhs3dgs="
  }
}
```

#### initiator <--- node (2019-03-13 11:05:20.369)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "tx": "tx_+P4LAfiEuEAKW+GaYeXcKLZ09Y5Ye72wMx8W+nBIhSUPHGC5KhnQZVHbPhZu/ba0oO/YPi2hOyB5X3onNArJDCFTZRDiuz4MuEDbWO6/cGva94ny2r5qBHySARv7zB6lnw/L8jFwKsI+WNfpsrmYlxCH9IUcudigV0Ah+5Fpz3VnztiaJsVXAPgAuHT4cjMBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA208CAIYSMJzlQACg9wAIQiESRdpjh7YppPzROomO3SK7nnc5qMAmCCltOqsDAqbkZuY="
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:20.382)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "tx": "tx_+P4LAfiEuEAKW+GaYeXcKLZ09Y5Ye72wMx8W+nBIhSUPHGC5KhnQZVHbPhZu/ba0oO/YPi2hOyB5X3onNArJDCFTZRDiuz4MuEDbWO6/cGva94ny2r5qBHySARv7zB6lnw/L8jFwKsI+WNfpsrmYlxCH9IUcudigV0Ah+5Fpz3VnztiaJsVXAPgAuHT4cjMBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA208CAIYSMJzlQACg9wAIQiESRdpjh7YppPzROomO3SK7nnc5qMAmCCltOqsDAqbkZuY="
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:23.203)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "own_deposit_locked"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:23.203)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "own_deposit_locked"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:23.204)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "deposit_locked"
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:23.204)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "event": "deposit_locked"
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:23.217)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "state": "tx_+P4LAfiEuEAKW+GaYeXcKLZ09Y5Ye72wMx8W+nBIhSUPHGC5KhnQZVHbPhZu/ba0oO/YPi2hOyB5X3onNArJDCFTZRDiuz4MuEDbWO6/cGva94ny2r5qBHySARv7zB6lnw/L8jFwKsI+WNfpsrmYlxCH9IUcudigV0Ah+5Fpz3VnztiaJsVXAPgAuHT4cjMBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA208CAIYSMJzlQACg9wAIQiESRdpjh7YppPzROomO3SK7nnc5qMAmCCltOqsDAqbkZuY="
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:23.218)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "state": "tx_+P4LAfiEuEAKW+GaYeXcKLZ09Y5Ye72wMx8W+nBIhSUPHGC5KhnQZVHbPhZu/ba0oO/YPi2hOyB5X3onNArJDCFTZRDiuz4MuEDbWO6/cGva94ny2r5qBHySARv7zB6lnw/L8jFwKsI+WNfpsrmYlxCH9IUcudigV0Ah+5Fpz3VnztiaJsVXAPgAuHT4cjMBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBqEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA208CAIYSMJzlQACg9wAIQiESRdpjh7YppPzROomO3SK7nnc5qMAmCCltOqsDAqbkZuY="
    }
  },
  "version": 1
}
```
