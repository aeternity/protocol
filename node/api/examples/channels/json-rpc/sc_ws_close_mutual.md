
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=246913579753086&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=246913579753086&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator
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
      "fsm_id": "ba_ZAJPTCpy3LEcOhkhvyA+gjF0dgsyLhwIbmF3+lZkQ7ttHOjG"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=246913579753086&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=246913579753086&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder
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
      "fsm_id": "ba_vO1wHLvFxP0LChnkD6DudD9IHMoskFtiIn963QSU5gzJ8fAt"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WhuCRDDYefqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCG4JEMNh5+AgoAhhAGeddIAMCgcFcOf6OvG9uiXtIrVttI5HFdo7YdR4gxLrkgK1vBDKwJYWccJw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423311,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDfu0fJLpnXw1Bku5nJaZdSV0d85f3JqWCHREZIZQCR/f7P70tEQ2YKoCt/3ln2wQe/DWRMRoSB/WF53LT9blwDuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1obgkQw2Hn6hAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhuCRDDYefgIKAIYQBnnXSADAoHBXDn+jrxvbol7SK1bbSORxXaO2HUeIMS65ICtbwQysCRTwvno="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423311,
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
    "data": {
      "fsm_id": "ba_vO1wHLvFxP0LChnkD6DudD9IHMoskFtiIn963QSU5gzJ8fAt",
      "signed_tx": "tx_+MsLAfhCuEDfu0fJLpnXw1Bku5nJaZdSV0d85f3JqWCHREZIZQCR/f7P70tEQ2YKoCt/3ln2wQe/DWRMRoSB/WF53LT9blwDuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1obgkQw2Hn6hAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhuCRDDYefgIKAIYQBnnXSADAoHBXDn+jrxvbol7SK1bbSORxXaO2HUeIMS65ICtbwQysCRTwvno=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423310,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAnexNnKGbGin6/z64vJ47Kiq7UntwEgIJSz8fwkREl9wHIDjtgDjO6tCFc2PuShKpulQjrCTclLU+0jBvXf1JBbhA37tHyS6Z18NQZLuZyWmXUldHfOX9yalgh0RGSGUAkf3+z+9LRENmCqArf95Z9sEHvw1kTEaEgf1hedy0/W5cA7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aG4JEMNh5+oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IbgkQw2Hn4CCgCGEAZ510gAwKBwVw5/o68b26Je0itW20jkcV2jth1HiDEuuSArW8EMrAmITPkr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
  "id": -576460752303423310,
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAnexNnKGbGin6/z64vJ47Kiq7UntwEgIJSz8fwkREl9wHIDjtgDjO6tCFc2PuShKpulQjrCTclLU+0jBvXf1JBbhA37tHyS6Z18NQZLuZyWmXUldHfOX9yalgh0RGSGUAkf3+z+9LRENmCqArf95Z9sEHvw1kTEaEgf1hedy0/W5cA7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aG4JEMNh5+oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IbgkQw2Hn4CCgCGEAZ510gAwKBwVw5/o68b26Je0itW20jkcV2jth1HiDEuuSArW8EMrAmITPkr",
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_ZAJPTCpy3LEcOhkhvyA+gjF0dgsyLhwIbmF3+lZkQ7ttHOjG"
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAnexNnKGbGin6/z64vJ47Kiq7UntwEgIJSz8fwkREl9wHIDjtgDjO6tCFc2PuShKpulQjrCTclLU+0jBvXf1JBbhA37tHyS6Z18NQZLuZyWmXUldHfOX9yalgh0RGSGUAkf3+z+9LRENmCqArf95Z9sEHvw1kTEaEgf1hedy0/W5cA7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aG4JEMNh5+oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IbgkQw2Hn4CCgCGEAZ510gAwKBwVw5/o68b26Je0itW20jkcV2jth1HiDEuuSArW8EMrAmITPkr",
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAnexNnKGbGin6/z64vJ47Kiq7UntwEgIJSz8fwkREl9wHIDjtgDjO6tCFc2PuShKpulQjrCTclLU+0jBvXf1JBbhA37tHyS6Z18NQZLuZyWmXUldHfOX9yalgh0RGSGUAkf3+z+9LRENmCqArf95Z9sEHvw1kTEaEgf1hedy0/W5cA7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aG4JEMNh5+oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IbgkQw2Hn4CCgCGEAZ510gAwKBwVw5/o68b26Je0itW20jkcV2jth1HiDEuuSArW8EMrAmITPkr",
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAnexNnKGbGin6/z64vJ47Kiq7UntwEgIJSz8fwkREl9wHIDjtgDjO6tCFc2PuShKpulQjrCTclLU+0jBvXf1JBbhA37tHyS6Z18NQZLuZyWmXUldHfOX9yalgh0RGSGUAkf3+z+9LRENmCqArf95Z9sEHvw1kTEaEgf1hedy0/W5cA7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aG4JEMNh5+oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IbgkQw2Hn4CCgCGEAZ510gAwKBwVw5/o68b26Je0itW20jkcV2jth1HiDEuuSArW8EMrAmITPkr",
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
    "data": {
      "message": {
        "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
    "data": {
      "message": {
        "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
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
  "id": -576460752303423309,
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
  "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
  "id": -576460752303423309,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 246913579753085
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 246913579753087
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
    "data": {
      "state": "tx_+QENCwH4hLhAnexNnKGbGin6/z64vJ47Kiq7UntwEgIJSz8fwkREl9wHIDjtgDjO6tCFc2PuShKpulQjrCTclLU+0jBvXf1JBbhA37tHyS6Z18NQZLuZyWmXUldHfOX9yalgh0RGSGUAkf3+z+9LRENmCqArf95Z9sEHvw1kTEaEgf1hedy0/W5cA7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aG4JEMNh5+oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IbgkQw2Hn4CCgCGEAZ510gAwKBwVw5/o68b26Je0itW20jkcV2jth1HiDEuuSArW8EMrAmITPkr"
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
    "data": {
      "state": "tx_+QENCwH4hLhAnexNnKGbGin6/z64vJ47Kiq7UntwEgIJSz8fwkREl9wHIDjtgDjO6tCFc2PuShKpulQjrCTclLU+0jBvXf1JBbhA37tHyS6Z18NQZLuZyWmXUldHfOX9yalgh0RGSGUAkf3+z+9LRENmCqArf95Z9sEHvw1kTEaEgf1hedy0/W5cA7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aG4JEMNh5+oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IbgkQw2Hn4CCgCGEAZ510gAwKBwVw5/o68b26Je0itW20jkcV2jth1HiDEuuSArW8EMrAmITPkr"
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBnqrkLQTcTKLfVcv4Y/EUDwqOAk8lIcfnoNqPP860nTAoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1obY4aD2in2G2OGg9op/AIYPXtZ/KAAKTsH6ow==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423308,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEDE4uvb/DRZg5eXJJxi/SR+r5mZd+tCOWV8fGfG/C1FI6KTn2BnD8lG5p126bfmKAKBexXgzEJgIWglF/26JL0GuF/4XTUBoQZ6q5C0E3Eyi31XL+GPxFA8KjgJPJSHH56Dajz/OtJ0wKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aG2OGg9op9htjhoPaKfwCGD17WfygACvjOkPA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
  "id": -576460752303423308,
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEDE4uvb/DRZg5eXJJxi/SR+r5mZd+tCOWV8fGfG/C1FI6KTn2BnD8lG5p126bfmKAKBexXgzEJgIWglF/26JL0GuF/4XTUBoQZ6q5C0E3Eyi31XL+GPxFA8KjgJPJSHH56Dajz/OtJ0wKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aG2OGg9op9htjhoPaKfwCGD17WfygACvjOkPA=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423307,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuECrsZTm/YOomwdrTbTEYOtngfD7Flj4z3chz4MqKq2IlIspHXyiCVQVCGldETAsbIp/5Pv2mDTm3V7vwegV3lIIuEDE4uvb/DRZg5eXJJxi/SR+r5mZd+tCOWV8fGfG/C1FI6KTn2BnD8lG5p126bfmKAKBexXgzEJgIWglF/26JL0GuF/4XTUBoQZ6q5C0E3Eyi31XL+GPxFA8KjgJPJSHH56Dajz/OtJ0wKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aG2OGg9op9htjhoPaKfwCGD17WfygACgErOtg="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
  "id": -576460752303423307,
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuECrsZTm/YOomwdrTbTEYOtngfD7Flj4z3chz4MqKq2IlIspHXyiCVQVCGldETAsbIp/5Pv2mDTm3V7vwegV3lIIuEDE4uvb/DRZg5eXJJxi/SR+r5mZd+tCOWV8fGfG/C1FI6KTn2BnD8lG5p126bfmKAKBexXgzEJgIWglF/26JL0GuF/4XTUBoQZ6q5C0E3Eyi31XL+GPxFA8KjgJPJSHH56Dajz/OtJ0wKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aG2OGg9op9htjhoPaKfwCGD17WfygACgErOtg=",
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuECrsZTm/YOomwdrTbTEYOtngfD7Flj4z3chz4MqKq2IlIspHXyiCVQVCGldETAsbIp/5Pv2mDTm3V7vwegV3lIIuEDE4uvb/DRZg5eXJJxi/SR+r5mZd+tCOWV8fGfG/C1FI6KTn2BnD8lG5p126bfmKAKBexXgzEJgIWglF/26JL0GuF/4XTUBoQZ6q5C0E3Eyi31XL+GPxFA8KjgJPJSHH56Dajz/OtJ0wKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aG2OGg9op9htjhoPaKfwCGD17WfygACgErOtg=",
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuECrsZTm/YOomwdrTbTEYOtngfD7Flj4z3chz4MqKq2IlIspHXyiCVQVCGldETAsbIp/5Pv2mDTm3V7vwegV3lIIuEDE4uvb/DRZg5eXJJxi/SR+r5mZd+tCOWV8fGfG/C1FI6KTn2BnD8lG5p126bfmKAKBexXgzEJgIWglF/26JL0GuF/4XTUBoQZ6q5C0E3Eyi31XL+GPxFA8KjgJPJSHH56Dajz/OtJ0wKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aG2OGg9op9htjhoPaKfwCGD17WfygACgErOtg=",
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuECrsZTm/YOomwdrTbTEYOtngfD7Flj4z3chz4MqKq2IlIspHXyiCVQVCGldETAsbIp/5Pv2mDTm3V7vwegV3lIIuEDE4uvb/DRZg5eXJJxi/SR+r5mZd+tCOWV8fGfG/C1FI6KTn2BnD8lG5p126bfmKAKBexXgzEJgIWglF/26JL0GuF/4XTUBoQZ6q5C0E3Eyi31XL+GPxFA8KjgJPJSHH56Dajz/OtJ0wKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aG2OGg9op9htjhoPaKfwCGD17WfygACgErOtg=",
      "type": "channel_close_mutual_tx"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=246913579753086&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=246913579753086&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator
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
      "fsm_id": "ba_wNIkC7dMy6UEl0rWE/swBIMe+S/FtUQ9Vnr6Xwvz3wCrzZ/K"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=246913579753086&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=246913579753086&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder
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
      "fsm_id": "ba_v2/mAFOApGCrjqqJgZtvvWuGIlELOKNFW5E8LiOndJGHTZ6S"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/WhuCRDDYefqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCG4JEMNh5+AgoAhhAGeddIAMCgcFcOf6OvG9uiXtIrVttI5HFdo7YdR4gxLrkgK1vBDKwL8CEYxw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423306,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECgQfJyr7wxRiBHPcHM3PYbyl8lgnl4ZDhwvx8X5/mVTA44+tk8qgzePFdb58041FaceQ7sChbaB0llX5gzlFwKuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1obgkQw2Hn6hAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhuCRDDYefgIKAIYQBnnXSADAoHBXDn+jrxvbol7SK1bbSORxXaO2HUeIMS65ICtbwQysCwz3kP0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423306,
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
    "data": {
      "fsm_id": "ba_v2/mAFOApGCrjqqJgZtvvWuGIlELOKNFW5E8LiOndJGHTZ6S",
      "signed_tx": "tx_+MsLAfhCuECgQfJyr7wxRiBHPcHM3PYbyl8lgnl4ZDhwvx8X5/mVTA44+tk8qgzePFdb58041FaceQ7sChbaB0llX5gzlFwKuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1obgkQw2Hn6hAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhuCRDDYefgIKAIYQBnnXSADAoHBXDn+jrxvbol7SK1bbSORxXaO2HUeIMS65ICtbwQysCwz3kP0=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423305,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAfPuv/r2rS6SMyOxTckFvlorRq0ffCxCoO8Dz6luINSZIQFzGJXu23m2UoOWsANuZ+pHH/bY9il3SNx/LJttGBLhAoEHycq+8MUYgRz3BzNz2G8pfJYJ5eGQ4cL8fF+f5lUwOOPrZPKoM3jxXW+fNONRWnHkO7AoW2gdJZV+YM5RcCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aG4JEMNh5+oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IbgkQw2Hn4CCgCGEAZ510gAwKBwVw5/o68b26Je0itW20jkcV2jth1HiDEuuSArW8EMrAvIz8/9"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
  "id": -576460752303423305,
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAfPuv/r2rS6SMyOxTckFvlorRq0ffCxCoO8Dz6luINSZIQFzGJXu23m2UoOWsANuZ+pHH/bY9il3SNx/LJttGBLhAoEHycq+8MUYgRz3BzNz2G8pfJYJ5eGQ4cL8fF+f5lUwOOPrZPKoM3jxXW+fNONRWnHkO7AoW2gdJZV+YM5RcCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aG4JEMNh5+oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IbgkQw2Hn4CCgCGEAZ510gAwKBwVw5/o68b26Je0itW20jkcV2jth1HiDEuuSArW8EMrAvIz8/9",
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_wNIkC7dMy6UEl0rWE/swBIMe+S/FtUQ9Vnr6Xwvz3wCrzZ/K"
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAfPuv/r2rS6SMyOxTckFvlorRq0ffCxCoO8Dz6luINSZIQFzGJXu23m2UoOWsANuZ+pHH/bY9il3SNx/LJttGBLhAoEHycq+8MUYgRz3BzNz2G8pfJYJ5eGQ4cL8fF+f5lUwOOPrZPKoM3jxXW+fNONRWnHkO7AoW2gdJZV+YM5RcCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aG4JEMNh5+oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IbgkQw2Hn4CCgCGEAZ510gAwKBwVw5/o68b26Je0itW20jkcV2jth1HiDEuuSArW8EMrAvIz8/9",
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAfPuv/r2rS6SMyOxTckFvlorRq0ffCxCoO8Dz6luINSZIQFzGJXu23m2UoOWsANuZ+pHH/bY9il3SNx/LJttGBLhAoEHycq+8MUYgRz3BzNz2G8pfJYJ5eGQ4cL8fF+f5lUwOOPrZPKoM3jxXW+fNONRWnHkO7AoW2gdJZV+YM5RcCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aG4JEMNh5+oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IbgkQw2Hn4CCgCGEAZ510gAwKBwVw5/o68b26Je0itW20jkcV2jth1HiDEuuSArW8EMrAvIz8/9",
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAfPuv/r2rS6SMyOxTckFvlorRq0ffCxCoO8Dz6luINSZIQFzGJXu23m2UoOWsANuZ+pHH/bY9il3SNx/LJttGBLhAoEHycq+8MUYgRz3BzNz2G8pfJYJ5eGQ4cL8fF+f5lUwOOPrZPKoM3jxXW+fNONRWnHkO7AoW2gdJZV+YM5RcCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aG4JEMNh5+oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IbgkQw2Hn4CCgCGEAZ510gAwKBwVw5/o68b26Je0itW20jkcV2jth1HiDEuuSArW8EMrAvIz8/9",
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

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
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
    "channel_id": "ch_w2Sp4aHgMw5RgKpb5KLLN2muftv54hWF1QVZGEwQHFv4omtAu",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
    "data": {
      "message": {
        "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
    "data": {
      "message": {
        "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
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
  "id": -576460752303423304,
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
  "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
  "id": -576460752303423304,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 246913579753085
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 246913579753087
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
    "data": {
      "event": "funding_locked"
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### initiator info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
    "data": {
      "state": "tx_+QENCwH4hLhAfPuv/r2rS6SMyOxTckFvlorRq0ffCxCoO8Dz6luINSZIQFzGJXu23m2UoOWsANuZ+pHH/bY9il3SNx/LJttGBLhAoEHycq+8MUYgRz3BzNz2G8pfJYJ5eGQ4cL8fF+f5lUwOOPrZPKoM3jxXW+fNONRWnHkO7AoW2gdJZV+YM5RcCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aG4JEMNh5+oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IbgkQw2Hn4CCgCGEAZ510gAwKBwVw5/o68b26Je0itW20jkcV2jth1HiDEuuSArW8EMrAvIz8/9"
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
    "data": {
      "state": "tx_+QENCwH4hLhAfPuv/r2rS6SMyOxTckFvlorRq0ffCxCoO8Dz6luINSZIQFzGJXu23m2UoOWsANuZ+pHH/bY9il3SNx/LJttGBLhAoEHycq+8MUYgRz3BzNz2G8pfJYJ5eGQ4cL8fF+f5lUwOOPrZPKoM3jxXW+fNONRWnHkO7AoW2gdJZV+YM5RcCriD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aG4JEMNh5+oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IbgkQw2Hn4CCgCGEAZ510gAwKBwVw5/o68b26Je0itW20jkcV2jth1HiDEuuSArW8EMrAvIz8/9"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBnUsdS1gIuYwj6AuuXl++cyj/T62oP0bmJmEAd+/c65CoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IbY4aD2in2G2OGg9op/AIYPXtZ/KAAD324Pjg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423303,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEDdFI4GWrTazwnAWIU2cjJ+yI8TPlZavCBfxYXbXrmwxXnfzIHdtO/waC/NGLZwCO48VC5/NDX2DGoUkdpdBawHuF/4XTUBoQZ1LHUtYCLmMI+gLrl5fvnMo/0+tqD9G5iZhAHfv3OuQqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCG2OGg9op9htjhoPaKfwCGD17WfygAA+h1TX8="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
  "id": -576460752303423303,
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
    "data": {
      "event": "shutdown"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEDdFI4GWrTazwnAWIU2cjJ+yI8TPlZavCBfxYXbXrmwxXnfzIHdtO/waC/NGLZwCO48VC5/NDX2DGoUkdpdBawHuF/4XTUBoQZ1LHUtYCLmMI+gLrl5fvnMo/0+tqD9G5iZhAHfv3OuQqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCG2OGg9op9htjhoPaKfwCGD17WfygAA+h1TX8=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423302,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEBghfLceZG2RbEvdU5w2nGBk+pimx9PSoB6ia9b7DUX9PHfpVHIJ7dKs/zt2S8j2jSzrm77bV/Jf73PDmwZPK4HuEDdFI4GWrTazwnAWIU2cjJ+yI8TPlZavCBfxYXbXrmwxXnfzIHdtO/waC/NGLZwCO48VC5/NDX2DGoUkdpdBawHuF/4XTUBoQZ1LHUtYCLmMI+gLrl5fvnMo/0+tqD9G5iZhAHfv3OuQqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCG2OGg9op9htjhoPaKfwCGD17WfygAAykIEu0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
  "id": -576460752303423302,
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBghfLceZG2RbEvdU5w2nGBk+pimx9PSoB6ia9b7DUX9PHfpVHIJ7dKs/zt2S8j2jSzrm77bV/Jf73PDmwZPK4HuEDdFI4GWrTazwnAWIU2cjJ+yI8TPlZavCBfxYXbXrmwxXnfzIHdtO/waC/NGLZwCO48VC5/NDX2DGoUkdpdBawHuF/4XTUBoQZ1LHUtYCLmMI+gLrl5fvnMo/0+tqD9G5iZhAHfv3OuQqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCG2OGg9op9htjhoPaKfwCGD17WfygAAykIEu0=",
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
    "data": {
      "event": "closing"
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEBghfLceZG2RbEvdU5w2nGBk+pimx9PSoB6ia9b7DUX9PHfpVHIJ7dKs/zt2S8j2jSzrm77bV/Jf73PDmwZPK4HuEDdFI4GWrTazwnAWIU2cjJ+yI8TPlZavCBfxYXbXrmwxXnfzIHdtO/waC/NGLZwCO48VC5/NDX2DGoUkdpdBawHuF/4XTUBoQZ1LHUtYCLmMI+gLrl5fvnMo/0+tqD9G5iZhAHfv3OuQqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCG2OGg9op9htjhoPaKfwCGD17WfygAAykIEu0=",
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBghfLceZG2RbEvdU5w2nGBk+pimx9PSoB6ia9b7DUX9PHfpVHIJ7dKs/zt2S8j2jSzrm77bV/Jf73PDmwZPK4HuEDdFI4GWrTazwnAWIU2cjJ+yI8TPlZavCBfxYXbXrmwxXnfzIHdtO/waC/NGLZwCO48VC5/NDX2DGoUkdpdBawHuF/4XTUBoQZ1LHUtYCLmMI+gLrl5fvnMo/0+tqD9G5iZhAHfv3OuQqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCG2OGg9op9htjhoPaKfwCGD17WfygAAykIEu0=",
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEBghfLceZG2RbEvdU5w2nGBk+pimx9PSoB6ia9b7DUX9PHfpVHIJ7dKs/zt2S8j2jSzrm77bV/Jf73PDmwZPK4HuEDdFI4GWrTazwnAWIU2cjJ+yI8TPlZavCBfxYXbXrmwxXnfzIHdtO/waC/NGLZwCO48VC5/NDX2DGoUkdpdBawHuF/4XTUBoQZ1LHUtYCLmMI+gLrl5fvnMo/0+tqD9G5iZhAHfv3OuQqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCG2OGg9op9htjhoPaKfwCGD17WfygAAykIEu0=",
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
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
    "channel_id": "ch_tc3YsabERmqVXmQJvsVbJ1huDYj5mqJiWt6sFT8FQkCBfb1yD",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
