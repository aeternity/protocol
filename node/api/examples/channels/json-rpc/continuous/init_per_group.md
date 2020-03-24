
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
      "fsm_id": "ba_SjGYqfCM+VEOK9xYRv9OpTuFGyINxuvNavQ2mTNEMEUW1pRo"
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
      "fsm_id": "ba_hjPwGwryAT4H7h4FGjHc1t47+i1p+fT8yv5O0N+550ZYZhu9"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsxf3aWiQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422844,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAqchowZqZvXuwBUmvzKZa8+tomd9XmBkWnU1ejQo4sZZVVQt98UL1ouevm1QkdpsIt1mSatCHrXSwID7/7nIsCuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LMbBsFAA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422844,
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "fsm_id": "ba_hjPwGwryAT4H7h4FGjHc1t47+i1p+fT8yv5O0N+550ZYZhu9",
      "signed_tx": "tx_+MsLAfhCuEAqchowZqZvXuwBUmvzKZa8+tomd9XmBkWnU1ejQo4sZZVVQt98UL1ouevm1QkdpsIt1mSatCHrXSwID7/7nIsCuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LMbBsFAA=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422843,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAKnIaMGamb17sAVJr8ymWvPraJnfV5gZFp1NXo0KOLGWVVULffFC9aLnr5tUJHabCLdZkmrQh610sCA+/+5yLArhAh+Z7Iq3/VHjnQBQRjv1eoNBaYr65bYkTWe8fBK1mpqieJl89n4+NghrtxYTCnTtWtRFOs31nvbTTnGsR7CESDbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzGg9rdU"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
  "id": -576460752303422843,
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAKnIaMGamb17sAVJr8ymWvPraJnfV5gZFp1NXo0KOLGWVVULffFC9aLnr5tUJHabCLdZkmrQh610sCA+/+5yLArhAh+Z7Iq3/VHjnQBQRjv1eoNBaYr65bYkTWe8fBK1mpqieJl89n4+NghrtxYTCnTtWtRFOs31nvbTTnGsR7CESDbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzGg9rdU",
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_SjGYqfCM+VEOK9xYRv9OpTuFGyINxuvNavQ2mTNEMEUW1pRo"
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAKnIaMGamb17sAVJr8ymWvPraJnfV5gZFp1NXo0KOLGWVVULffFC9aLnr5tUJHabCLdZkmrQh610sCA+/+5yLArhAh+Z7Iq3/VHjnQBQRjv1eoNBaYr65bYkTWe8fBK1mpqieJl89n4+NghrtxYTCnTtWtRFOs31nvbTTnGsR7CESDbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzGg9rdU",
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAKnIaMGamb17sAVJr8ymWvPraJnfV5gZFp1NXo0KOLGWVVULffFC9aLnr5tUJHabCLdZkmrQh610sCA+/+5yLArhAh+Z7Iq3/VHjnQBQRjv1eoNBaYr65bYkTWe8fBK1mpqieJl89n4+NghrtxYTCnTtWtRFOs31nvbTTnGsR7CESDbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzGg9rdU",
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAKnIaMGamb17sAVJr8ymWvPraJnfV5gZFp1NXo0KOLGWVVULffFC9aLnr5tUJHabCLdZkmrQh610sCA+/+5yLArhAh+Z7Iq3/VHjnQBQRjv1eoNBaYr65bYkTWe8fBK1mpqieJl89n4+NghrtxYTCnTtWtRFOs31nvbTTnGsR7CESDbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzGg9rdU",
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "message": {
        "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "message": {
        "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
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
  "id": -576460752303422842,
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
  "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
  "id": -576460752303422842,
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "state": "tx_+QENCwH4hLhAKnIaMGamb17sAVJr8ymWvPraJnfV5gZFp1NXo0KOLGWVVULffFC9aLnr5tUJHabCLdZkmrQh610sCA+/+5yLArhAh+Z7Iq3/VHjnQBQRjv1eoNBaYr65bYkTWe8fBK1mpqieJl89n4+NghrtxYTCnTtWtRFOs31nvbTTnGsR7CESDbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzGg9rdU"
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "state": "tx_+QENCwH4hLhAKnIaMGamb17sAVJr8ymWvPraJnfV5gZFp1NXo0KOLGWVVULffFC9aLnr5tUJHabCLdZkmrQh610sCA+/+5yLArhAh+Z7Iq3/VHjnQBQRjv1eoNBaYr65bYkTWe8fBK1mpqieJl89n4+NghrtxYTCnTtWtRFOs31nvbTTnGsR7CESDbiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCzGg9rdU"
    }
  },
  "version": 1
}
```
