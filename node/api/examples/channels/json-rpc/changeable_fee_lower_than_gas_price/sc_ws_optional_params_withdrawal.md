
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator
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
      "fsm_id": "ba_2cxr8xxKvuF792gKdEaNEfWiFfPFT93k6AJe6tYF2jtC2U+3"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder
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
      "fsm_id": "ba_w/Ej58JZVfS3ylmDvyGwP2NZRh2A14d9VlURjJusfkp875Hz"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBhCDfw44=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422389,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEDcW7sEIbo3FdVKb9bHR4akqOs+5k69cQfK1MBcXTA3eXHpUB46+afDIIZAfd+JlOxNZVI3oIvxalp4Om3fu8wJuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgYQfzQXF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422389,
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "fsm_id": "ba_w/Ej58JZVfS3ylmDvyGwP2NZRh2A14d9VlURjJusfkp875Hz",
      "signed_tx": "tx_+MwLAfhCuEDcW7sEIbo3FdVKb9bHR4akqOs+5k69cQfK1MBcXTA3eXHpUB46+afDIIZAfd+JlOxNZVI3oIvxalp4Om3fu8wJuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgYQfzQXF",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422388,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhA3Fu7BCG6NxXVSm/Wx0eGpKjrPuZOvXEHytTAXF0wN3lx6VAeOvmnwyCGQH3fiZTsTWVSN6CL8WpaeDpt37vMCbhA5BUNmjQmcuTobaWxT5efOyQekLzs+2cP/D6QdBw8uesANJ0EdyCz7B3zGi4EltMU7UurhG7IU0Ps/yWDG5pQCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GEuhp+OA=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
  "id": -576460752303422388,
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhA3Fu7BCG6NxXVSm/Wx0eGpKjrPuZOvXEHytTAXF0wN3lx6VAeOvmnwyCGQH3fiZTsTWVSN6CL8WpaeDpt37vMCbhA5BUNmjQmcuTobaWxT5efOyQekLzs+2cP/D6QdBw8uesANJ0EdyCz7B3zGi4EltMU7UurhG7IU0Ps/yWDG5pQCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GEuhp+OA==",
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_2cxr8xxKvuF792gKdEaNEfWiFfPFT93k6AJe6tYF2jtC2U+3"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhA3Fu7BCG6NxXVSm/Wx0eGpKjrPuZOvXEHytTAXF0wN3lx6VAeOvmnwyCGQH3fiZTsTWVSN6CL8WpaeDpt37vMCbhA5BUNmjQmcuTobaWxT5efOyQekLzs+2cP/D6QdBw8uesANJ0EdyCz7B3zGi4EltMU7UurhG7IU0Ps/yWDG5pQCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GEuhp+OA==",
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhA3Fu7BCG6NxXVSm/Wx0eGpKjrPuZOvXEHytTAXF0wN3lx6VAeOvmnwyCGQH3fiZTsTWVSN6CL8WpaeDpt37vMCbhA5BUNmjQmcuTobaWxT5efOyQekLzs+2cP/D6QdBw8uesANJ0EdyCz7B3zGi4EltMU7UurhG7IU0Ps/yWDG5pQCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GEuhp+OA==",
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhA3Fu7BCG6NxXVSm/Wx0eGpKjrPuZOvXEHytTAXF0wN3lx6VAeOvmnwyCGQH3fiZTsTWVSN6CL8WpaeDpt37vMCbhA5BUNmjQmcuTobaWxT5efOyQekLzs+2cP/D6QdBw8uesANJ0EdyCz7B3zGi4EltMU7UurhG7IU0Ps/yWDG5pQCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GEuhp+OA==",
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "message": {
        "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "message": {
        "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello back",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422387,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
  "id": -576460752303422387,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999999
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "state": "tx_+QEOCwH4hLhA3Fu7BCG6NxXVSm/Wx0eGpKjrPuZOvXEHytTAXF0wN3lx6VAeOvmnwyCGQH3fiZTsTWVSN6CL8WpaeDpt37vMCbhA5BUNmjQmcuTobaWxT5efOyQekLzs+2cP/D6QdBw8uesANJ0EdyCz7B3zGi4EltMU7UurhG7IU0Ps/yWDG5pQCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GEuhp+OA=="
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "state": "tx_+QEOCwH4hLhA3Fu7BCG6NxXVSm/Wx0eGpKjrPuZOvXEHytTAXF0wN3lx6VAeOvmnwyCGQH3fiZTsTWVSN6CL8WpaeDpt37vMCbhA5BUNmjQmcuTobaWxT5efOyQekLzs+2cP/D6QdBw8uesANJ0EdyCz7B3zGi4EltMU7UurhG7IU0Ps/yWDG5pQCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GEuhp+OA=="
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "message": {
        "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "message": {
        "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello back",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
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
      "method": "channels.withdraw",
      "params": {
        "amount": "2"
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
  "method": "channels.message",
  "params": {
    "info": "Hello",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "message": {
        "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "message": {
        "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello back",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 2,
    "fee": 1,
    "gas_price": 1000001234
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzNAGhBi1VMh/MOubBy1i4dRPKbfFmaN/LuOQts4M6HK6/I4QJoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gIAhg/FSdDYOKD6aIyRp0q4njYpKUN7EoE8dGS1wKGxithIYn6oqM3YIgKBhfF9tio=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "id": -576460752303422386,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+L0LAfhCuEA069Qg/Z+rdsF4Ixqm78MTNextG8y0EdtvYCB4EumG9e+6QHGacncDgk4eCHLwsNbs6vVt6x/hJ3+depJxYDsEuHX4czQBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUnQ2Dig+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICgYUDGjdC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
  "id": -576460752303422386,
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "signed_tx": "tx_+L0LAfhCuEA069Qg/Z+rdsF4Ixqm78MTNextG8y0EdtvYCB4EumG9e+6QHGacncDgk4eCHLwsNbs6vVt6x/hJ3+depJxYDsEuHX4czQBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUnQ2Dig+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICgYUDGjdC",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "id": -576460752303422385,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P8LAfiEuEA069Qg/Z+rdsF4Ixqm78MTNextG8y0EdtvYCB4EumG9e+6QHGacncDgk4eCHLwsNbs6vVt6x/hJ3+depJxYDsEuEDJN8Q7rmkuK354pqKZjgViZKD4r7uKMGdX6ISwJ4I1iGZQxtWj3xj1TUuL2LNXqWZ2+eu/o4kcembZ1p8HnysMuHX4czQBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUnQ2Dig+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICgYVAMMoP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
  "id": -576460752303422385,
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P8LAfiEuEA069Qg/Z+rdsF4Ixqm78MTNextG8y0EdtvYCB4EumG9e+6QHGacncDgk4eCHLwsNbs6vVt6x/hJ3+depJxYDsEuEDJN8Q7rmkuK354pqKZjgViZKD4r7uKMGdX6ISwJ4I1iGZQxtWj3xj1TUuL2LNXqWZ2+eu/o4kcembZ1p8HnysMuHX4czQBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUnQ2Dig+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICgYVAMMoP",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P8LAfiEuEA069Qg/Z+rdsF4Ixqm78MTNextG8y0EdtvYCB4EumG9e+6QHGacncDgk4eCHLwsNbs6vVt6x/hJ3+depJxYDsEuEDJN8Q7rmkuK354pqKZjgViZKD4r7uKMGdX6ISwJ4I1iGZQxtWj3xj1TUuL2LNXqWZ2+eu/o4kcembZ1p8HnysMuHX4czQBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUnQ2Dig+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICgYVAMMoP",
      "type": "channel_withdraw_tx"
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "message": {
        "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "message": {
        "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello back",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P8LAfiEuEA069Qg/Z+rdsF4Ixqm78MTNextG8y0EdtvYCB4EumG9e+6QHGacncDgk4eCHLwsNbs6vVt6x/hJ3+depJxYDsEuEDJN8Q7rmkuK354pqKZjgViZKD4r7uKMGdX6ISwJ4I1iGZQxtWj3xj1TUuL2LNXqWZ2+eu/o4kcembZ1p8HnysMuHX4czQBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUnQ2Dig+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICgYVAMMoP",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P8LAfiEuEA069Qg/Z+rdsF4Ixqm78MTNextG8y0EdtvYCB4EumG9e+6QHGacncDgk4eCHLwsNbs6vVt6x/hJ3+depJxYDsEuEDJN8Q7rmkuK354pqKZjgViZKD4r7uKMGdX6ISwJ4I1iGZQxtWj3xj1TUuL2LNXqWZ2+eu/o4kcembZ1p8HnysMuHX4czQBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUnQ2Dig+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICgYVAMMoP",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "state": "tx_+P8LAfiEuEA069Qg/Z+rdsF4Ixqm78MTNextG8y0EdtvYCB4EumG9e+6QHGacncDgk4eCHLwsNbs6vVt6x/hJ3+depJxYDsEuEDJN8Q7rmkuK354pqKZjgViZKD4r7uKMGdX6ISwJ4I1iGZQxtWj3xj1TUuL2LNXqWZ2+eu/o4kcembZ1p8HnysMuHX4czQBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUnQ2Dig+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICgYVAMMoP"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "state": "tx_+P8LAfiEuEA069Qg/Z+rdsF4Ixqm78MTNextG8y0EdtvYCB4EumG9e+6QHGacncDgk4eCHLwsNbs6vVt6x/hJ3+depJxYDsEuEDJN8Q7rmkuK354pqKZjgViZKD4r7uKMGdX6ISwJ4I1iGZQxtWj3xj1TUuL2LNXqWZ2+eu/o4kcembZ1p8HnysMuHX4czQBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUnQ2Dig+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICgYVAMMoP"
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
    "info": "Hello",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "message": {
        "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
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
    "info": "Hello back",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "message": {
        "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello back",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "method": "channels.withdraw",
  "params": {
    "amount": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
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
      "method": "channels.withdraw",
      "params": {
        "amount": "2"
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
  "method": "channels.message",
  "params": {
    "info": "Hello",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "message": {
        "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
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
    "info": "Hello back",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "message": {
        "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello back",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "method": "channels.withdraw",
  "params": {
    "amount": 2,
    "fee": 1,
    "gas_price": 1000001234
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBi1VMh/MOubBy1i4dRPKbfFmaN/LuOQts4M6HK6/I4QJoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AIAhg/Aobiv0KBIWkDp9eRQQRyHm8U+8URorUUQQNdonwOQZqEaw6yolgM25OmGbQ==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "id": -576460752303422384,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuECq1RWjwW1rTouiPpiuP5yjrNJ7O6lnxq9XViVBxly6HdONVkqKg+DDMMjo+XzicWA/ez3VLA9acpk6Z175IOIJuHT4cjQBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDNhr/2ec="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
  "id": -576460752303422384,
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "signed_tx": "tx_+LwLAfhCuECq1RWjwW1rTouiPpiuP5yjrNJ7O6lnxq9XViVBxly6HdONVkqKg+DDMMjo+XzicWA/ez3VLA9acpk6Z175IOIJuHT4cjQBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDNhr/2ec=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "id": -576460752303422383,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEALjSJcaEqLw+IGItd4iKz++zg0o7oWasQ5JI+FX5La85PfVilSpCLB0lXUVCVeYlu5YJZDrjkTtPNFLrk81M8JuECq1RWjwW1rTouiPpiuP5yjrNJ7O6lnxq9XViVBxly6HdONVkqKg+DDMMjo+XzicWA/ez3VLA9acpk6Z175IOIJuHT4cjQBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDNjSky8A="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
  "id": -576460752303422383,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEALjSJcaEqLw+IGItd4iKz++zg0o7oWasQ5JI+FX5La85PfVilSpCLB0lXUVCVeYlu5YJZDrjkTtPNFLrk81M8JuECq1RWjwW1rTouiPpiuP5yjrNJ7O6lnxq9XViVBxly6HdONVkqKg+DDMMjo+XzicWA/ez3VLA9acpk6Z175IOIJuHT4cjQBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDNjSky8A=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEALjSJcaEqLw+IGItd4iKz++zg0o7oWasQ5JI+FX5La85PfVilSpCLB0lXUVCVeYlu5YJZDrjkTtPNFLrk81M8JuECq1RWjwW1rTouiPpiuP5yjrNJ7O6lnxq9XViVBxly6HdONVkqKg+DDMMjo+XzicWA/ez3VLA9acpk6Z175IOIJuHT4cjQBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDNjSky8A=",
      "type": "channel_withdraw_tx"
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
    "info": "Hello",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "message": {
        "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
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
    "info": "Hello back",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "message": {
        "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello back",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
      }
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEALjSJcaEqLw+IGItd4iKz++zg0o7oWasQ5JI+FX5La85PfVilSpCLB0lXUVCVeYlu5YJZDrjkTtPNFLrk81M8JuECq1RWjwW1rTouiPpiuP5yjrNJ7O6lnxq9XViVBxly6HdONVkqKg+DDMMjo+XzicWA/ez3VLA9acpk6Z175IOIJuHT4cjQBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDNjSky8A=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEALjSJcaEqLw+IGItd4iKz++zg0o7oWasQ5JI+FX5La85PfVilSpCLB0lXUVCVeYlu5YJZDrjkTtPNFLrk81M8JuECq1RWjwW1rTouiPpiuP5yjrNJ7O6lnxq9XViVBxly6HdONVkqKg+DDMMjo+XzicWA/ez3VLA9acpk6Z175IOIJuHT4cjQBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDNjSky8A=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "state": "tx_+P4LAfiEuEALjSJcaEqLw+IGItd4iKz++zg0o7oWasQ5JI+FX5La85PfVilSpCLB0lXUVCVeYlu5YJZDrjkTtPNFLrk81M8JuECq1RWjwW1rTouiPpiuP5yjrNJ7O6lnxq9XViVBxly6HdONVkqKg+DDMMjo+XzicWA/ez3VLA9acpk6Z175IOIJuHT4cjQBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDNjSky8A="
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "state": "tx_+P4LAfiEuEALjSJcaEqLw+IGItd4iKz++zg0o7oWasQ5JI+FX5La85PfVilSpCLB0lXUVCVeYlu5YJZDrjkTtPNFLrk81M8JuECq1RWjwW1rTouiPpiuP5yjrNJ7O6lnxq9XViVBxly6HdONVkqKg+DDMMjo+XzicWA/ez3VLA9acpk6Z175IOIJuHT4cjQBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDNjSky8A="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBi1VMh/MOubBy1i4dRPKbfFmaN/LuOQts4M6HK6/I4QJoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+GXW5/2GHK96fwf/AIYPY36W8ACBhsYhL4k=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422382,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuEC+UwoHRv635fGhvEpgn2S7OQbU0ZvHTZqMovmrGNqdSKIgLbiAvENtr82FRJbXGnjmuSmTtJGYVQma6wyJzBULuGD4XjUBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf9hhyven8H/wCGD2N+lvAAgYbAMGeM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
  "id": -576460752303422382,
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "event": "shutdown"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "signed_tx": "tx_+KgLAfhCuEC+UwoHRv635fGhvEpgn2S7OQbU0ZvHTZqMovmrGNqdSKIgLbiAvENtr82FRJbXGnjmuSmTtJGYVQma6wyJzBULuGD4XjUBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf9hhyven8H/wCGD2N+lvAAgYbAMGeM",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422381,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuEC+UwoHRv635fGhvEpgn2S7OQbU0ZvHTZqMovmrGNqdSKIgLbiAvENtr82FRJbXGnjmuSmTtJGYVQma6wyJzBULuEDENd1K9/xT7ZwyvZ6YQZmMS2F1jGwKcw4hWVzgOdvhGfszvpHlD8oeXOb7sloUH+WjRB34sPG16Dg8YErPACcEuGD4XjUBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf9hhyven8H/wCGD2N+lvAAgYZ27Pbt"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
  "id": -576460752303422381,
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEC+UwoHRv635fGhvEpgn2S7OQbU0ZvHTZqMovmrGNqdSKIgLbiAvENtr82FRJbXGnjmuSmTtJGYVQma6wyJzBULuEDENd1K9/xT7ZwyvZ6YQZmMS2F1jGwKcw4hWVzgOdvhGfszvpHlD8oeXOb7sloUH+WjRB34sPG16Dg8YErPACcEuGD4XjUBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf9hhyven8H/wCGD2N+lvAAgYZ27Pbt",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "event": "closing"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEC+UwoHRv635fGhvEpgn2S7OQbU0ZvHTZqMovmrGNqdSKIgLbiAvENtr82FRJbXGnjmuSmTtJGYVQma6wyJzBULuEDENd1K9/xT7ZwyvZ6YQZmMS2F1jGwKcw4hWVzgOdvhGfszvpHlD8oeXOb7sloUH+WjRB34sPG16Dg8YErPACcEuGD4XjUBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf9hhyven8H/wCGD2N+lvAAgYZ27Pbt",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "event": "closing"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEC+UwoHRv635fGhvEpgn2S7OQbU0ZvHTZqMovmrGNqdSKIgLbiAvENtr82FRJbXGnjmuSmTtJGYVQma6wyJzBULuEDENd1K9/xT7ZwyvZ6YQZmMS2F1jGwKcw4hWVzgOdvhGfszvpHlD8oeXOb7sloUH+WjRB34sPG16Dg8YErPACcEuGD4XjUBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf9hhyven8H/wCGD2N+lvAAgYZ27Pbt",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEC+UwoHRv635fGhvEpgn2S7OQbU0ZvHTZqMovmrGNqdSKIgLbiAvENtr82FRJbXGnjmuSmTtJGYVQma6wyJzBULuEDENd1K9/xT7ZwyvZ6YQZmMS2F1jGwKcw4hWVzgOdvhGfszvpHlD8oeXOb7sloUH+WjRB34sPG16Dg8YErPACcEuGD4XjUBoQYtVTIfzDrmwctYuHUTym3xZmjfy7jkLbODOhyuvyOECaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf9hhyven8H/wCGD2N+lvAAgYZ27Pbt",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "event": "closed_confirmed"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
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
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "event": "closed_confirmed"
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
    "channel_id": "ch_LxxziYybf9cRQDPrKp6KAtSrqkqJTW6mgXMntC7r9WryLRqu3",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
