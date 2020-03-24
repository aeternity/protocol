
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
      "fsm_id": "ba_e6LjoQNIYYCTlOS2mtICz437hNn83QSWzMZzrzODsi22h+6o"
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
      "fsm_id": "ba_GsgDag6reNzELngM1GJuesZKJEPiTgktMvCK4a9Zk37ButAR"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtsIDjNHw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422481,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDLCpvSIOdmd7kZQpCNrsqgsHCNChW8ybH6ZUGBsFEiBV7kxfYUEVaRZRo40yIXaEGQYGWu9r7mScKvGiTQ9aIEuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LbP0FxtI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422481,
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "fsm_id": "ba_GsgDag6reNzELngM1GJuesZKJEPiTgktMvCK4a9Zk37ButAR",
      "signed_tx": "tx_+MsLAfhCuEDLCpvSIOdmd7kZQpCNrsqgsHCNChW8ybH6ZUGBsFEiBV7kxfYUEVaRZRo40yIXaEGQYGWu9r7mScKvGiTQ9aIEuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LbP0FxtI=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422480,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAJzOJgulumdbX5evawTtWL7zGR+JR/38yy6yjiPiuUgkxIWZp3aLJrYNxKyU2AF5oeEAjg5kgD/M/cM3DtctvB7hAywqb0iDnZne5GUKQja7KoLBwjQoVvMmx+mVBgbBRIgVe5MX2FBFWkWUaONMiF2hBkGBlrva+5knCrxok0PWiBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2wmA2Dh"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
  "id": -576460752303422480,
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAJzOJgulumdbX5evawTtWL7zGR+JR/38yy6yjiPiuUgkxIWZp3aLJrYNxKyU2AF5oeEAjg5kgD/M/cM3DtctvB7hAywqb0iDnZne5GUKQja7KoLBwjQoVvMmx+mVBgbBRIgVe5MX2FBFWkWUaONMiF2hBkGBlrva+5knCrxok0PWiBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2wmA2Dh",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_e6LjoQNIYYCTlOS2mtICz437hNn83QSWzMZzrzODsi22h+6o"
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAJzOJgulumdbX5evawTtWL7zGR+JR/38yy6yjiPiuUgkxIWZp3aLJrYNxKyU2AF5oeEAjg5kgD/M/cM3DtctvB7hAywqb0iDnZne5GUKQja7KoLBwjQoVvMmx+mVBgbBRIgVe5MX2FBFWkWUaONMiF2hBkGBlrva+5knCrxok0PWiBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2wmA2Dh",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAJzOJgulumdbX5evawTtWL7zGR+JR/38yy6yjiPiuUgkxIWZp3aLJrYNxKyU2AF5oeEAjg5kgD/M/cM3DtctvB7hAywqb0iDnZne5GUKQja7KoLBwjQoVvMmx+mVBgbBRIgVe5MX2FBFWkWUaONMiF2hBkGBlrva+5knCrxok0PWiBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2wmA2Dh",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAJzOJgulumdbX5evawTtWL7zGR+JR/38yy6yjiPiuUgkxIWZp3aLJrYNxKyU2AF5oeEAjg5kgD/M/cM3DtctvB7hAywqb0iDnZne5GUKQja7KoLBwjQoVvMmx+mVBgbBRIgVe5MX2FBFWkWUaONMiF2hBkGBlrva+5knCrxok0PWiBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2wmA2Dh",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "message": {
        "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "message": {
        "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
  "id": -576460752303422479,
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
  "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
  "id": -576460752303422479,
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "state": "tx_+QENCwH4hLhAJzOJgulumdbX5evawTtWL7zGR+JR/38yy6yjiPiuUgkxIWZp3aLJrYNxKyU2AF5oeEAjg5kgD/M/cM3DtctvB7hAywqb0iDnZne5GUKQja7KoLBwjQoVvMmx+mVBgbBRIgVe5MX2FBFWkWUaONMiF2hBkGBlrva+5knCrxok0PWiBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2wmA2Dh"
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "state": "tx_+QENCwH4hLhAJzOJgulumdbX5evawTtWL7zGR+JR/38yy6yjiPiuUgkxIWZp3aLJrYNxKyU2AF5oeEAjg5kgD/M/cM3DtctvB7hAywqb0iDnZne5GUKQja7KoLBwjQoVvMmx+mVBgbBRIgVe5MX2FBFWkWUaONMiF2hBkGBlrva+5knCrxok0PWiBLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2wmA2Dh"
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "message": {
        "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "message": {
        "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
  "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "message": {
        "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "message": {
        "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBgNici0ncxOuzluHfUAua65hYUZa0j/czalFM5S4Fn/6oQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gIAhuCRDDYefqD6aIyRp0q4njYpKUN7EoE8dGS1wKGxithIYn6oqM3YIgJtYO7ppg==",
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
  "id": -576460752303422478,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuECytfYUmBGo0WagcH0BQqAreNd9PQVZr00S3lWSO+OLcQLFP6jZsLq/R21eElKVYIG4nzYwkasi4rlQMPH8ir4DuHT4cjQBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIbgkQw2Hn6g+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICbRHkmGY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
  "id": -576460752303422478,
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "signed_tx": "tx_+LwLAfhCuECytfYUmBGo0WagcH0BQqAreNd9PQVZr00S3lWSO+OLcQLFP6jZsLq/R21eElKVYIG4nzYwkasi4rlQMPH8ir4DuHT4cjQBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIbgkQw2Hn6g+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICbRHkmGY=",
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
  "id": -576460752303422477,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuECtzFt0mFMn1JqBPBGb6JDTBzoXgnxZSbdQKI4J7+e39P5eOpGhINo42G93JIULJ7+c6V7Wb9zCYzFV+xnflNsFuECytfYUmBGo0WagcH0BQqAreNd9PQVZr00S3lWSO+OLcQLFP6jZsLq/R21eElKVYIG4nzYwkasi4rlQMPH8ir4DuHT4cjQBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIbgkQw2Hn6g+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICbQ6YoUs="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
  "id": -576460752303422477,
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuECtzFt0mFMn1JqBPBGb6JDTBzoXgnxZSbdQKI4J7+e39P5eOpGhINo42G93JIULJ7+c6V7Wb9zCYzFV+xnflNsFuECytfYUmBGo0WagcH0BQqAreNd9PQVZr00S3lWSO+OLcQLFP6jZsLq/R21eElKVYIG4nzYwkasi4rlQMPH8ir4DuHT4cjQBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIbgkQw2Hn6g+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICbQ6YoUs=",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuECtzFt0mFMn1JqBPBGb6JDTBzoXgnxZSbdQKI4J7+e39P5eOpGhINo42G93JIULJ7+c6V7Wb9zCYzFV+xnflNsFuECytfYUmBGo0WagcH0BQqAreNd9PQVZr00S3lWSO+OLcQLFP6jZsLq/R21eElKVYIG4nzYwkasi4rlQMPH8ir4DuHT4cjQBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIbgkQw2Hn6g+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICbQ6YoUs=",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "message": {
        "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "message": {
        "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECtzFt0mFMn1JqBPBGb6JDTBzoXgnxZSbdQKI4J7+e39P5eOpGhINo42G93JIULJ7+c6V7Wb9zCYzFV+xnflNsFuECytfYUmBGo0WagcH0BQqAreNd9PQVZr00S3lWSO+OLcQLFP6jZsLq/R21eElKVYIG4nzYwkasi4rlQMPH8ir4DuHT4cjQBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIbgkQw2Hn6g+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICbQ6YoUs=",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECtzFt0mFMn1JqBPBGb6JDTBzoXgnxZSbdQKI4J7+e39P5eOpGhINo42G93JIULJ7+c6V7Wb9zCYzFV+xnflNsFuECytfYUmBGo0WagcH0BQqAreNd9PQVZr00S3lWSO+OLcQLFP6jZsLq/R21eElKVYIG4nzYwkasi4rlQMPH8ir4DuHT4cjQBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIbgkQw2Hn6g+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICbQ6YoUs=",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "state": "tx_+P4LAfiEuECtzFt0mFMn1JqBPBGb6JDTBzoXgnxZSbdQKI4J7+e39P5eOpGhINo42G93JIULJ7+c6V7Wb9zCYzFV+xnflNsFuECytfYUmBGo0WagcH0BQqAreNd9PQVZr00S3lWSO+OLcQLFP6jZsLq/R21eElKVYIG4nzYwkasi4rlQMPH8ir4DuHT4cjQBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIbgkQw2Hn6g+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICbQ6YoUs="
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "state": "tx_+P4LAfiEuECtzFt0mFMn1JqBPBGb6JDTBzoXgnxZSbdQKI4J7+e39P5eOpGhINo42G93JIULJ7+c6V7Wb9zCYzFV+xnflNsFuECytfYUmBGo0WagcH0BQqAreNd9PQVZr00S3lWSO+OLcQLFP6jZsLq/R21eElKVYIG4nzYwkasi4rlQMPH8ir4DuHT4cjQBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIbgkQw2Hn6g+miMkadKuJ42KSlDexKBPHRktcChsYrYSGJ+qKjN2CICbQ6YoUs="
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "message": {
        "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "message": {
        "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
  "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "message": {
        "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "message": {
        "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "fee": 246913579753086,
    "gas_price": 1000000000
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBgNici0ncxOuzluHfUAua65hYUZa0j/czalFM5S4Fn/6oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AIAhuCRDDYefqBIWkDp9eRQQRyHm8U+8URorUUQQNdonwOQZqEaw6yolgMsOkKWQA==",
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
  "id": -576460752303422476,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEBfLHeA9CkoLXvCOCnCFr3aI4OTZAl/xD1jC8R4lIa2I52Pwt/+nIZPta5WR5EseH2tgtZGVnkqfK7Wxko+Tt4OuHT4cjQBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIbgkQw2Hn6gSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDLPgzmUM="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
  "id": -576460752303422476,
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEBfLHeA9CkoLXvCOCnCFr3aI4OTZAl/xD1jC8R4lIa2I52Pwt/+nIZPta5WR5EseH2tgtZGVnkqfK7Wxko+Tt4OuHT4cjQBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIbgkQw2Hn6gSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDLPgzmUM=",
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
  "id": -576460752303422475,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBfLHeA9CkoLXvCOCnCFr3aI4OTZAl/xD1jC8R4lIa2I52Pwt/+nIZPta5WR5EseH2tgtZGVnkqfK7Wxko+Tt4OuECTekO3g8FUXxDJ0mUzCRe/l29pK7gu+X+L8xpKEhR0b1gvJRSQ0FridYKlmA9NytE7uTEYdjm+d6y8J6TY0cYIuHT4cjQBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIbgkQw2Hn6gSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDLKWz3gk="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
  "id": -576460752303422475,
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEBfLHeA9CkoLXvCOCnCFr3aI4OTZAl/xD1jC8R4lIa2I52Pwt/+nIZPta5WR5EseH2tgtZGVnkqfK7Wxko+Tt4OuECTekO3g8FUXxDJ0mUzCRe/l29pK7gu+X+L8xpKEhR0b1gvJRSQ0FridYKlmA9NytE7uTEYdjm+d6y8J6TY0cYIuHT4cjQBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIbgkQw2Hn6gSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDLKWz3gk=",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEBfLHeA9CkoLXvCOCnCFr3aI4OTZAl/xD1jC8R4lIa2I52Pwt/+nIZPta5WR5EseH2tgtZGVnkqfK7Wxko+Tt4OuECTekO3g8FUXxDJ0mUzCRe/l29pK7gu+X+L8xpKEhR0b1gvJRSQ0FridYKlmA9NytE7uTEYdjm+d6y8J6TY0cYIuHT4cjQBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIbgkQw2Hn6gSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDLKWz3gk=",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "message": {
        "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "message": {
        "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBfLHeA9CkoLXvCOCnCFr3aI4OTZAl/xD1jC8R4lIa2I52Pwt/+nIZPta5WR5EseH2tgtZGVnkqfK7Wxko+Tt4OuECTekO3g8FUXxDJ0mUzCRe/l29pK7gu+X+L8xpKEhR0b1gvJRSQ0FridYKlmA9NytE7uTEYdjm+d6y8J6TY0cYIuHT4cjQBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIbgkQw2Hn6gSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDLKWz3gk=",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBfLHeA9CkoLXvCOCnCFr3aI4OTZAl/xD1jC8R4lIa2I52Pwt/+nIZPta5WR5EseH2tgtZGVnkqfK7Wxko+Tt4OuECTekO3g8FUXxDJ0mUzCRe/l29pK7gu+X+L8xpKEhR0b1gvJRSQ0FridYKlmA9NytE7uTEYdjm+d6y8J6TY0cYIuHT4cjQBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIbgkQw2Hn6gSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDLKWz3gk=",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "state": "tx_+P4LAfiEuEBfLHeA9CkoLXvCOCnCFr3aI4OTZAl/xD1jC8R4lIa2I52Pwt/+nIZPta5WR5EseH2tgtZGVnkqfK7Wxko+Tt4OuECTekO3g8FUXxDJ0mUzCRe/l29pK7gu+X+L8xpKEhR0b1gvJRSQ0FridYKlmA9NytE7uTEYdjm+d6y8J6TY0cYIuHT4cjQBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIbgkQw2Hn6gSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDLKWz3gk="
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "state": "tx_+P4LAfiEuEBfLHeA9CkoLXvCOCnCFr3aI4OTZAl/xD1jC8R4lIa2I52Pwt/+nIZPta5WR5EseH2tgtZGVnkqfK7Wxko+Tt4OuECTekO3g8FUXxDJ0mUzCRe/l29pK7gu+X+L8xpKEhR0b1gvJRSQ0FridYKlmA9NytE7uTEYdjm+d6y8J6TY0cYIuHT4cjQBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIbgkQw2Hn6gSFpA6fXkUEEch5vFPvFEaK1FEEDXaJ8DkGahGsOsqJYDLKWz3gk="
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBgNici0ncxOuzluHfUAua65hYUZa0j/czalFM5S4Fn/6oQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+rniy/2GHLHOiuv/AIYPXtZ/KABuSSKmyA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422474,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuECz6q5NTXDdZC8Geomrc/fNspuwuL8PfjI6oWRw8/aQltDfNqHGtlFwUvJYnQX/EkmmyZiSQWAXUfe6PxMVh40OuF/4XTUBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv9hhyxzorr/wCGD17WfygAbixsm24="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
  "id": -576460752303422474,
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "signed_tx": "tx_+KcLAfhCuECz6q5NTXDdZC8Geomrc/fNspuwuL8PfjI6oWRw8/aQltDfNqHGtlFwUvJYnQX/EkmmyZiSQWAXUfe6PxMVh40OuF/4XTUBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv9hhyxzorr/wCGD17WfygAbixsm24=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422473,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEB/hJ9EhYNraHxocQyOqehDvCaF+E6JFf0lVAu8TlvCv3NFfeev7ETmpcqxyQ23qlsbG+U18CjPNqsP0Qw+OwQJuECz6q5NTXDdZC8Geomrc/fNspuwuL8PfjI6oWRw8/aQltDfNqHGtlFwUvJYnQX/EkmmyZiSQWAXUfe6PxMVh40OuF/4XTUBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv9hhyxzorr/wCGD17WfygAbuueJME="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
  "id": -576460752303422473,
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEB/hJ9EhYNraHxocQyOqehDvCaF+E6JFf0lVAu8TlvCv3NFfeev7ETmpcqxyQ23qlsbG+U18CjPNqsP0Qw+OwQJuECz6q5NTXDdZC8Geomrc/fNspuwuL8PfjI6oWRw8/aQltDfNqHGtlFwUvJYnQX/EkmmyZiSQWAXUfe6PxMVh40OuF/4XTUBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv9hhyxzorr/wCGD17WfygAbuueJME=",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEB/hJ9EhYNraHxocQyOqehDvCaF+E6JFf0lVAu8TlvCv3NFfeev7ETmpcqxyQ23qlsbG+U18CjPNqsP0Qw+OwQJuECz6q5NTXDdZC8Geomrc/fNspuwuL8PfjI6oWRw8/aQltDfNqHGtlFwUvJYnQX/EkmmyZiSQWAXUfe6PxMVh40OuF/4XTUBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv9hhyxzorr/wCGD17WfygAbuueJME=",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEB/hJ9EhYNraHxocQyOqehDvCaF+E6JFf0lVAu8TlvCv3NFfeev7ETmpcqxyQ23qlsbG+U18CjPNqsP0Qw+OwQJuECz6q5NTXDdZC8Geomrc/fNspuwuL8PfjI6oWRw8/aQltDfNqHGtlFwUvJYnQX/EkmmyZiSQWAXUfe6PxMVh40OuF/4XTUBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv9hhyxzorr/wCGD17WfygAbuueJME=",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEB/hJ9EhYNraHxocQyOqehDvCaF+E6JFf0lVAu8TlvCv3NFfeev7ETmpcqxyQ23qlsbG+U18CjPNqsP0Qw+OwQJuECz6q5NTXDdZC8Geomrc/fNspuwuL8PfjI6oWRw8/aQltDfNqHGtlFwUvJYnQX/EkmmyZiSQWAXUfe6PxMVh40OuF/4XTUBoQYDYnItJ3MTrs5bh31ALmuuYWFGWtI/3M2pRTOUuBZ/+qEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv9hhyxzorr/wCGD17WfygAbuueJME=",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
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
    "channel_id": "ch_2VTKwikit3TvZqpVYrgNipea9AR9Z1LbagPbJvMTFme9Bevwj",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
