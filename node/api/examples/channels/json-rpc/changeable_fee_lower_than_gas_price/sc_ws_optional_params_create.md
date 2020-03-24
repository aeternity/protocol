
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&fee=1&gas_price=1000001234&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator
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
      "fsm_id": "ba_5x98bDX/55GG1dFzFzzYnpxOno8M+2LPoOAU2spDRo/rcpul"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&fee=1&gas_price=1000001234&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder
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
      "fsm_id": "ba_QFhS9izQIv1Qz19cRccEd9b2LYOISPcXG9qQXKrsrnckDXhn"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeyMN6MCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgt/IKCe7Q==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422403,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEArt28rDS3k4DBQblPtVB3jIDQWsCMdrmUleFoWJVfdbyWLZ5ykGjXKXrjSaDPRmvbIGyOAYmsCqVWAc0bY7bcMuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnsjDejAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4Lf9Tz6Rg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422403,
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
    "data": {
      "fsm_id": "ba_QFhS9izQIv1Qz19cRccEd9b2LYOISPcXG9qQXKrsrnckDXhn",
      "signed_tx": "tx_+MsLAfhCuEArt28rDS3k4DBQblPtVB3jIDQWsCMdrmUleFoWJVfdbyWLZ5ykGjXKXrjSaDPRmvbIGyOAYmsCqVWAc0bY7bcMuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnsjDejAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4Lf9Tz6Rg=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422402,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAK7dvKw0t5OAwUG5T7VQd4yA0FrAjHa5lJXhaFiVX3W8li2ecpBo1yl640mgz0Zr2yBsjgGJrAqlVgHNG2O23DLhAuxant+YTzl1LfAaU32qY6hahBjobLdra9C0zMajYPU0Ds82GzJnGyVasjmpESO3OZczbJ3GNVHiVPZv9rAsOD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ7Iw3owKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3/tEeud"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
  "id": -576460752303422402,
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAK7dvKw0t5OAwUG5T7VQd4yA0FrAjHa5lJXhaFiVX3W8li2ecpBo1yl640mgz0Zr2yBsjgGJrAqlVgHNG2O23DLhAuxant+YTzl1LfAaU32qY6hahBjobLdra9C0zMajYPU0Ds82GzJnGyVasjmpESO3OZczbJ3GNVHiVPZv9rAsOD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ7Iw3owKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3/tEeud",
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_5x98bDX/55GG1dFzFzzYnpxOno8M+2LPoOAU2spDRo/rcpul"
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAK7dvKw0t5OAwUG5T7VQd4yA0FrAjHa5lJXhaFiVX3W8li2ecpBo1yl640mgz0Zr2yBsjgGJrAqlVgHNG2O23DLhAuxant+YTzl1LfAaU32qY6hahBjobLdra9C0zMajYPU0Ds82GzJnGyVasjmpESO3OZczbJ3GNVHiVPZv9rAsOD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ7Iw3owKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3/tEeud",
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAK7dvKw0t5OAwUG5T7VQd4yA0FrAjHa5lJXhaFiVX3W8li2ecpBo1yl640mgz0Zr2yBsjgGJrAqlVgHNG2O23DLhAuxant+YTzl1LfAaU32qY6hahBjobLdra9C0zMajYPU0Ds82GzJnGyVasjmpESO3OZczbJ3GNVHiVPZv9rAsOD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ7Iw3owKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3/tEeud",
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAK7dvKw0t5OAwUG5T7VQd4yA0FrAjHa5lJXhaFiVX3W8li2ecpBo1yl640mgz0Zr2yBsjgGJrAqlVgHNG2O23DLhAuxant+YTzl1LfAaU32qY6hahBjobLdra9C0zMajYPU0Ds82GzJnGyVasjmpESO3OZczbJ3GNVHiVPZv9rAsOD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ7Iw3owKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3/tEeud",
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
    "data": {
      "message": {
        "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
    "data": {
      "message": {
        "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
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
  "id": -576460752303422401,
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
  "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
  "id": -576460752303422401,
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
    "data": {
      "state": "tx_+QENCwH4hLhAK7dvKw0t5OAwUG5T7VQd4yA0FrAjHa5lJXhaFiVX3W8li2ecpBo1yl640mgz0Zr2yBsjgGJrAqlVgHNG2O23DLhAuxant+YTzl1LfAaU32qY6hahBjobLdra9C0zMajYPU0Ds82GzJnGyVasjmpESO3OZczbJ3GNVHiVPZv9rAsOD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ7Iw3owKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3/tEeud"
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
    "data": {
      "state": "tx_+QENCwH4hLhAK7dvKw0t5OAwUG5T7VQd4yA0FrAjHa5lJXhaFiVX3W8li2ecpBo1yl640mgz0Zr2yBsjgGJrAqlVgHNG2O23DLhAuxant+YTzl1LfAaU32qY6hahBjobLdra9C0zMajYPU0Ds82GzJnGyVasjmpESO3OZczbJ3GNVHiVPZv9rAsOD7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ7Iw3owKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC3/tEeud"
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBv8ru4/8ikIQiqnAZrPZXYt0usKNmQfG0b9yjW3lRsSaoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+GXW5/+GHK96fwgBAIYPY36W8ACBgD1zmiQ=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422400,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuEDXQx7DPvtLtBzwMsC5glsWliumD1dGOBW/goA/Q/ddCr9Ii2jA5NNuf556rAB0hWzUf+XiZDd9YwR97UMMxhANuGD4XjUBoQb/K7uP/IpCEIqpwGaz2V2LdLrCjZkHxtG/co1t5UbEmqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgYBgFZ+6"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
  "id": -576460752303422400,
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
    "data": {
      "signed_tx": "tx_+KgLAfhCuEDXQx7DPvtLtBzwMsC5glsWliumD1dGOBW/goA/Q/ddCr9Ii2jA5NNuf556rAB0hWzUf+XiZDd9YwR97UMMxhANuGD4XjUBoQb/K7uP/IpCEIqpwGaz2V2LdLrCjZkHxtG/co1t5UbEmqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgYBgFZ+6",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422399,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuEDXQx7DPvtLtBzwMsC5glsWliumD1dGOBW/goA/Q/ddCr9Ii2jA5NNuf556rAB0hWzUf+XiZDd9YwR97UMMxhANuEDvldcp/EQimSEV57TdeIKVw/zoq1IA3FiTbuMjJkyO1ZCgNt8jAPMWhlA/vh/AgyARehldVhmX+ZOrtgokN2QNuGD4XjUBoQb/K7uP/IpCEIqpwGaz2V2LdLrCjZkHxtG/co1t5UbEmqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgYCevRFE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
  "id": -576460752303422399,
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEDXQx7DPvtLtBzwMsC5glsWliumD1dGOBW/goA/Q/ddCr9Ii2jA5NNuf556rAB0hWzUf+XiZDd9YwR97UMMxhANuEDvldcp/EQimSEV57TdeIKVw/zoq1IA3FiTbuMjJkyO1ZCgNt8jAPMWhlA/vh/AgyARehldVhmX+ZOrtgokN2QNuGD4XjUBoQb/K7uP/IpCEIqpwGaz2V2LdLrCjZkHxtG/co1t5UbEmqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgYCevRFE",
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEDXQx7DPvtLtBzwMsC5glsWliumD1dGOBW/goA/Q/ddCr9Ii2jA5NNuf556rAB0hWzUf+XiZDd9YwR97UMMxhANuEDvldcp/EQimSEV57TdeIKVw/zoq1IA3FiTbuMjJkyO1ZCgNt8jAPMWhlA/vh/AgyARehldVhmX+ZOrtgokN2QNuGD4XjUBoQb/K7uP/IpCEIqpwGaz2V2LdLrCjZkHxtG/co1t5UbEmqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgYCevRFE",
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEDXQx7DPvtLtBzwMsC5glsWliumD1dGOBW/goA/Q/ddCr9Ii2jA5NNuf556rAB0hWzUf+XiZDd9YwR97UMMxhANuEDvldcp/EQimSEV57TdeIKVw/zoq1IA3FiTbuMjJkyO1ZCgNt8jAPMWhlA/vh/AgyARehldVhmX+ZOrtgokN2QNuGD4XjUBoQb/K7uP/IpCEIqpwGaz2V2LdLrCjZkHxtG/co1t5UbEmqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgYCevRFE",
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEDXQx7DPvtLtBzwMsC5glsWliumD1dGOBW/goA/Q/ddCr9Ii2jA5NNuf556rAB0hWzUf+XiZDd9YwR97UMMxhANuEDvldcp/EQimSEV57TdeIKVw/zoq1IA3FiTbuMjJkyO1ZCgNt8jAPMWhlA/vh/AgyARehldVhmX+ZOrtgokN2QNuGD4XjUBoQb/K7uP/IpCEIqpwGaz2V2LdLrCjZkHxtG/co1t5UbEmqEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgYCevRFE",
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
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
    "channel_id": "ch_2wNznshiwTyDHUSiJMMcGJpiPX9RTGDGKi4epKT3FbNCmfkm9r",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
