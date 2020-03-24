
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
      "fsm_id": "ba_z+mGXN+T4mWkIJC5SO5dl2TOn6/d8xJkx8JMsLsL1VV/RexO"
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
      "fsm_id": "ba_kD1L3AZT+tg40rgdW7gfm75rxyE8cGiIbd3V2Z11wW6HXOj3"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBmbBQmos=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422267,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEAIoeeSE8o/O0TjxSOMQb37oKPp64Zpv23gocv9AwdDwF2db+ZxL5JNNSYEPKH4guSsnTcZZP9DV+MfQbYNeh8FuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgZmYwkWN"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422267,
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
    "data": {
      "fsm_id": "ba_kD1L3AZT+tg40rgdW7gfm75rxyE8cGiIbd3V2Z11wW6HXOj3",
      "signed_tx": "tx_+MwLAfhCuEAIoeeSE8o/O0TjxSOMQb37oKPp64Zpv23gocv9AwdDwF2db+ZxL5JNNSYEPKH4guSsnTcZZP9DV+MfQbYNeh8FuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgZmYwkWN",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422266,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhACKHnkhPKPztE48UjjEG9+6Cj6euGab9t4KHL/QMHQ8BdnW/mcS+STTUmBDyh+ILkrJ03GWT/Q1fjH0G2DXofBbhAeI+o+avnLw3xdv3efL2Tlm9jobt1yGz0vHRNp9YKCSCb5ZR4gz4PpdBsCWtXuZ34+mZJP9wLCodC8gUDkzjzB7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GZO2dZKg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
  "id": -576460752303422266,
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhACKHnkhPKPztE48UjjEG9+6Cj6euGab9t4KHL/QMHQ8BdnW/mcS+STTUmBDyh+ILkrJ03GWT/Q1fjH0G2DXofBbhAeI+o+avnLw3xdv3efL2Tlm9jobt1yGz0vHRNp9YKCSCb5ZR4gz4PpdBsCWtXuZ34+mZJP9wLCodC8gUDkzjzB7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GZO2dZKg==",
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_z+mGXN+T4mWkIJC5SO5dl2TOn6/d8xJkx8JMsLsL1VV/RexO"
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhACKHnkhPKPztE48UjjEG9+6Cj6euGab9t4KHL/QMHQ8BdnW/mcS+STTUmBDyh+ILkrJ03GWT/Q1fjH0G2DXofBbhAeI+o+avnLw3xdv3efL2Tlm9jobt1yGz0vHRNp9YKCSCb5ZR4gz4PpdBsCWtXuZ34+mZJP9wLCodC8gUDkzjzB7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GZO2dZKg==",
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhACKHnkhPKPztE48UjjEG9+6Cj6euGab9t4KHL/QMHQ8BdnW/mcS+STTUmBDyh+ILkrJ03GWT/Q1fjH0G2DXofBbhAeI+o+avnLw3xdv3efL2Tlm9jobt1yGz0vHRNp9YKCSCb5ZR4gz4PpdBsCWtXuZ34+mZJP9wLCodC8gUDkzjzB7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GZO2dZKg==",
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhACKHnkhPKPztE48UjjEG9+6Cj6euGab9t4KHL/QMHQ8BdnW/mcS+STTUmBDyh+ILkrJ03GWT/Q1fjH0G2DXofBbhAeI+o+avnLw3xdv3efL2Tlm9jobt1yGz0vHRNp9YKCSCb5ZR4gz4PpdBsCWtXuZ34+mZJP9wLCodC8gUDkzjzB7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GZO2dZKg==",
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
    "data": {
      "message": {
        "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
    "data": {
      "message": {
        "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
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
  "id": -576460752303422265,
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
  "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
  "id": -576460752303422265,
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
    "data": {
      "state": "tx_+QEOCwH4hLhACKHnkhPKPztE48UjjEG9+6Cj6euGab9t4KHL/QMHQ8BdnW/mcS+STTUmBDyh+ILkrJ03GWT/Q1fjH0G2DXofBbhAeI+o+avnLw3xdv3efL2Tlm9jobt1yGz0vHRNp9YKCSCb5ZR4gz4PpdBsCWtXuZ34+mZJP9wLCodC8gUDkzjzB7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GZO2dZKg=="
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
    "data": {
      "state": "tx_+QEOCwH4hLhACKHnkhPKPztE48UjjEG9+6Cj6euGab9t4KHL/QMHQ8BdnW/mcS+STTUmBDyh+ILkrJ03GWT/Q1fjH0G2DXofBbhAeI+o+avnLw3xdv3efL2Tlm9jobt1yGz0vHRNp9YKCSCb5ZR4gz4PpdBsCWtXuZ34+mZJP9wLCodC8gUDkzjzB7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GZO2dZKg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2,
    "nonce": 1234567
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
    "data": {
      "signed_tx": "tx_+HwLAcC4d/h1MwGhBl1oTdML4DFS9udUR3Gw+wRVlCpBFwYcTjvvOSWGV7oZoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gIAhg/OmLnoAKAJfKOkRYFmCfu9WWBbxU0n1wqMcA3FNf3vEd2/gK5qlQKDEtaHFGXqMw==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainDeposit"
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
  "method": "channels.deposit_tx",
  "params": {
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
    "data": {
      "event": "aborted_update"
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBl1oTdML4DFS9udUR3Gw+wRVlCpBFwYcTjvvOSWGV7oZoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+GXW5/+GHK96fwgBAIYPY36W8ACBmiiKt2Q=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422264,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuECNuIpN8fkegMUMKqImFvzV54AfN2p+j/krm2jjUPniiTUbfR29UJrW25dvsqE8EzYfGE7/SJ1OIGe9AnDOvGUAuGD4XjUBoQZdaE3TC+AxUvbnVEdxsPsEVZQqQRcGHE477zklhle6GaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgZqiRxfn"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
  "id": -576460752303422264,
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
    "data": {
      "signed_tx": "tx_+KgLAfhCuECNuIpN8fkegMUMKqImFvzV54AfN2p+j/krm2jjUPniiTUbfR29UJrW25dvsqE8EzYfGE7/SJ1OIGe9AnDOvGUAuGD4XjUBoQZdaE3TC+AxUvbnVEdxsPsEVZQqQRcGHE477zklhle6GaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgZqiRxfn",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422263,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuECNuIpN8fkegMUMKqImFvzV54AfN2p+j/krm2jjUPniiTUbfR29UJrW25dvsqE8EzYfGE7/SJ1OIGe9AnDOvGUAuED06CeHF1N9MoIAEGP/8RCaseiaaRuJZqkyh+6WWsVaA8nvi93Kh4xZ+V4AxlsZOGoGqG3N+iHACO7LTCRYLtkIuGD4XjUBoQZdaE3TC+AxUvbnVEdxsPsEVZQqQRcGHE477zklhle6GaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgZoDAPjr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
  "id": -576460752303422263,
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuECNuIpN8fkegMUMKqImFvzV54AfN2p+j/krm2jjUPniiTUbfR29UJrW25dvsqE8EzYfGE7/SJ1OIGe9AnDOvGUAuED06CeHF1N9MoIAEGP/8RCaseiaaRuJZqkyh+6WWsVaA8nvi93Kh4xZ+V4AxlsZOGoGqG3N+iHACO7LTCRYLtkIuGD4XjUBoQZdaE3TC+AxUvbnVEdxsPsEVZQqQRcGHE477zklhle6GaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgZoDAPjr",
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuECNuIpN8fkegMUMKqImFvzV54AfN2p+j/krm2jjUPniiTUbfR29UJrW25dvsqE8EzYfGE7/SJ1OIGe9AnDOvGUAuED06CeHF1N9MoIAEGP/8RCaseiaaRuJZqkyh+6WWsVaA8nvi93Kh4xZ+V4AxlsZOGoGqG3N+iHACO7LTCRYLtkIuGD4XjUBoQZdaE3TC+AxUvbnVEdxsPsEVZQqQRcGHE477zklhle6GaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgZoDAPjr",
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuECNuIpN8fkegMUMKqImFvzV54AfN2p+j/krm2jjUPniiTUbfR29UJrW25dvsqE8EzYfGE7/SJ1OIGe9AnDOvGUAuED06CeHF1N9MoIAEGP/8RCaseiaaRuJZqkyh+6WWsVaA8nvi93Kh4xZ+V4AxlsZOGoGqG3N+iHACO7LTCRYLtkIuGD4XjUBoQZdaE3TC+AxUvbnVEdxsPsEVZQqQRcGHE477zklhle6GaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgZoDAPjr",
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuECNuIpN8fkegMUMKqImFvzV54AfN2p+j/krm2jjUPniiTUbfR29UJrW25dvsqE8EzYfGE7/SJ1OIGe9AnDOvGUAuED06CeHF1N9MoIAEGP/8RCaseiaaRuJZqkyh+6WWsVaA8nvi93Kh4xZ+V4AxlsZOGoGqG3N+iHACO7LTCRYLtkIuGD4XjUBoQZdaE3TC+AxUvbnVEdxsPsEVZQqQRcGHE477zklhle6GaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgZoDAPjr",
      "type": "channel_close_mutual_tx"
    }
  },
  "version": 1
}
```

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
      "fsm_id": "ba_wAcThvalAMlNaEDkljdWlOThF4uuUmhJp5USTMOZoZgdRMtL"
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
      "fsm_id": "ba_1OQFojCgqLcRFKDkr0ylIZBsJQjJX4hgnERJaHYc6qmV8jKz"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBm3bzRBY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422262,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEATpTLFs305xVO5kC+I3NZbiOzwTOe9blf4h2SEtjFqy7E4H5CIqqLjWVuqVU5f/oZR/w9C4SSglaEbGSdSxl8MuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgZvwV9bv"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422262,
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
    "data": {
      "fsm_id": "ba_1OQFojCgqLcRFKDkr0ylIZBsJQjJX4hgnERJaHYc6qmV8jKz",
      "signed_tx": "tx_+MwLAfhCuEATpTLFs305xVO5kC+I3NZbiOzwTOe9blf4h2SEtjFqy7E4H5CIqqLjWVuqVU5f/oZR/w9C4SSglaEbGSdSxl8MuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgZvwV9bv",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422261,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAE6UyxbN9OcVTuZAviNzWW4js8EznvW5X+IdkhLYxasuxOB+QiKqi41lbqlVOX/6GUf8PQuEkoJWhGxknUsZfDLhAoLeyYKg5zrIjVv0DuN/Wn1OFx/WGcAZ7sN2OjzIUWw42c9I+M7DVjbRKOM5zIrm4xewLz8nd6MlK560mgLZXD7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GbLlfSMQ=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
  "id": -576460752303422261,
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAE6UyxbN9OcVTuZAviNzWW4js8EznvW5X+IdkhLYxasuxOB+QiKqi41lbqlVOX/6GUf8PQuEkoJWhGxknUsZfDLhAoLeyYKg5zrIjVv0DuN/Wn1OFx/WGcAZ7sN2OjzIUWw42c9I+M7DVjbRKOM5zIrm4xewLz8nd6MlK560mgLZXD7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GbLlfSMQ==",
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_wAcThvalAMlNaEDkljdWlOThF4uuUmhJp5USTMOZoZgdRMtL"
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAE6UyxbN9OcVTuZAviNzWW4js8EznvW5X+IdkhLYxasuxOB+QiKqi41lbqlVOX/6GUf8PQuEkoJWhGxknUsZfDLhAoLeyYKg5zrIjVv0DuN/Wn1OFx/WGcAZ7sN2OjzIUWw42c9I+M7DVjbRKOM5zIrm4xewLz8nd6MlK560mgLZXD7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GbLlfSMQ==",
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAE6UyxbN9OcVTuZAviNzWW4js8EznvW5X+IdkhLYxasuxOB+QiKqi41lbqlVOX/6GUf8PQuEkoJWhGxknUsZfDLhAoLeyYKg5zrIjVv0DuN/Wn1OFx/WGcAZ7sN2OjzIUWw42c9I+M7DVjbRKOM5zIrm4xewLz8nd6MlK560mgLZXD7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GbLlfSMQ==",
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAE6UyxbN9OcVTuZAviNzWW4js8EznvW5X+IdkhLYxasuxOB+QiKqi41lbqlVOX/6GUf8PQuEkoJWhGxknUsZfDLhAoLeyYKg5zrIjVv0DuN/Wn1OFx/WGcAZ7sN2OjzIUWw42c9I+M7DVjbRKOM5zIrm4xewLz8nd6MlK560mgLZXD7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GbLlfSMQ==",
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
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
    "channel_id": "ch_i8y86G3SZASWntggqxbBx5KUuWgWmitP1U6Z6u68UnDhcg6fh",
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
    "data": {
      "message": {
        "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
    "data": {
      "message": {
        "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
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
  "id": -576460752303422260,
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
  "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
  "id": -576460752303422260,
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
    "data": {
      "state": "tx_+QEOCwH4hLhAE6UyxbN9OcVTuZAviNzWW4js8EznvW5X+IdkhLYxasuxOB+QiKqi41lbqlVOX/6GUf8PQuEkoJWhGxknUsZfDLhAoLeyYKg5zrIjVv0DuN/Wn1OFx/WGcAZ7sN2OjzIUWw42c9I+M7DVjbRKOM5zIrm4xewLz8nd6MlK560mgLZXD7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GbLlfSMQ=="
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
    "data": {
      "state": "tx_+QEOCwH4hLhAE6UyxbN9OcVTuZAviNzWW4js8EznvW5X+IdkhLYxasuxOB+QiKqi41lbqlVOX/6GUf8PQuEkoJWhGxknUsZfDLhAoLeyYKg5zrIjVv0DuN/Wn1OFx/WGcAZ7sN2OjzIUWw42c9I+M7DVjbRKOM5zIrm4xewLz8nd6MlK560mgLZXD7iE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GbLlfSMQ=="
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2,
    "nonce": 1234567
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
    "data": {
      "signed_tx": "tx_+HwLAcC4d/h1MwGhBgBfyaUG0rWx8jBOpuY3WbfRTkJ0S8Cm9vq94fZFMlQ8oQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AIAhg/OmLnoAKDqgdNkuhddveVDE/es1N/fevZuJ9NTBtOGxk/KimI/YwKDEtaHOapEHQ==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainDeposit"
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
  "method": "channels.deposit_tx",
  "params": {
    "error": 42
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
    "data": {
      "event": "aborted_update"
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBgBfyaUG0rWx8jBOpuY3WbfRTkJ0S8Cm9vq94fZFMlQ8oQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+GXW5/+GHK96fwgBAIYPY36W8ACBnEoUyNI=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422259,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuEAw8Czwx3rWw3QiQITHoAAuh4jN+oJeBJp4A+hXGbJ+K1RMgzRitcBFC/anHn8Ei8HBPAL86cD4ULccur6eHZoJuGD4XjUBoQYAX8mlBtK1sfIwTqbmN1m30U5CdEvApvb6veH2RTJUPKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgZzjADMA"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
  "id": -576460752303422259,
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
    "data": {
      "signed_tx": "tx_+KgLAfhCuEAw8Czwx3rWw3QiQITHoAAuh4jN+oJeBJp4A+hXGbJ+K1RMgzRitcBFC/anHn8Ei8HBPAL86cD4ULccur6eHZoJuGD4XjUBoQYAX8mlBtK1sfIwTqbmN1m30U5CdEvApvb6veH2RTJUPKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgZzjADMA",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422258,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuEAw8Czwx3rWw3QiQITHoAAuh4jN+oJeBJp4A+hXGbJ+K1RMgzRitcBFC/anHn8Ei8HBPAL86cD4ULccur6eHZoJuEB/+lceoQk/4JQHWJz+7uP0eHVgxBY8QFTClFiFVvoSpAtCEItFWqh4RkMwRLGghp07tR7q//eq2dyeAuuzfVwBuGD4XjUBoQYAX8mlBtK1sfIwTqbmN1m30U5CdEvApvb6veH2RTJUPKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgZzEDnXa"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
  "id": -576460752303422258,
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEAw8Czwx3rWw3QiQITHoAAuh4jN+oJeBJp4A+hXGbJ+K1RMgzRitcBFC/anHn8Ei8HBPAL86cD4ULccur6eHZoJuEB/+lceoQk/4JQHWJz+7uP0eHVgxBY8QFTClFiFVvoSpAtCEItFWqh4RkMwRLGghp07tR7q//eq2dyeAuuzfVwBuGD4XjUBoQYAX8mlBtK1sfIwTqbmN1m30U5CdEvApvb6veH2RTJUPKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgZzEDnXa",
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEAw8Czwx3rWw3QiQITHoAAuh4jN+oJeBJp4A+hXGbJ+K1RMgzRitcBFC/anHn8Ei8HBPAL86cD4ULccur6eHZoJuEB/+lceoQk/4JQHWJz+7uP0eHVgxBY8QFTClFiFVvoSpAtCEItFWqh4RkMwRLGghp07tR7q//eq2dyeAuuzfVwBuGD4XjUBoQYAX8mlBtK1sfIwTqbmN1m30U5CdEvApvb6veH2RTJUPKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgZzEDnXa",
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEAw8Czwx3rWw3QiQITHoAAuh4jN+oJeBJp4A+hXGbJ+K1RMgzRitcBFC/anHn8Ei8HBPAL86cD4ULccur6eHZoJuEB/+lceoQk/4JQHWJz+7uP0eHVgxBY8QFTClFiFVvoSpAtCEItFWqh4RkMwRLGghp07tR7q//eq2dyeAuuzfVwBuGD4XjUBoQYAX8mlBtK1sfIwTqbmN1m30U5CdEvApvb6veH2RTJUPKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgZzEDnXa",
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEAw8Czwx3rWw3QiQITHoAAuh4jN+oJeBJp4A+hXGbJ+K1RMgzRitcBFC/anHn8Ei8HBPAL86cD4ULccur6eHZoJuEB/+lceoQk/4JQHWJz+7uP0eHVgxBY8QFTClFiFVvoSpAtCEItFWqh4RkMwRLGghp07tR7q//eq2dyeAuuzfVwBuGD4XjUBoQYAX8mlBtK1sfIwTqbmN1m30U5CdEvApvb6veH2RTJUPKEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1uf/hhyven8IAQCGD2N+lvAAgZzEDnXa",
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
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
    "channel_id": "ch_1AZM4CqFEQ9N16YE8kygZevorUYJP5Diyijr5ojTq6gwJtwq3",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
