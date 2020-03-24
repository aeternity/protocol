
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
      "fsm_id": "ba_fJksMnqytl+KvvZuAPREIxGPh0DezvNOLGyQ8FDUwWB9ciVV"
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
      "fsm_id": "ba_w1A1E6mbl1ITxcxC9qSndXkHu1r3w7xldbu1vhT4SqQA5BY7"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBgWYrP9Y=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422398,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEAr4+J5l0ye0QiNnzidyjQScx8KZur8QeSg32bqnsrED5iGY8wb39p1FgunrlDER1jpVIViIUxzO5SMNAsNsNUEuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgYG1hdCB"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422398,
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "fsm_id": "ba_w1A1E6mbl1ITxcxC9qSndXkHu1r3w7xldbu1vhT4SqQA5BY7",
      "signed_tx": "tx_+MwLAfhCuEAr4+J5l0ye0QiNnzidyjQScx8KZur8QeSg32bqnsrED5iGY8wb39p1FgunrlDER1jpVIViIUxzO5SMNAsNsNUEuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgYG1hdCB",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422397,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAK+PieZdMntEIjZ84nco0EnMfCmbq/EHkoN9m6p7KxA+YhmPMG9/adRYLp65QxEdY6VSFYiFMczuUjDQLDbDVBLhAo8nusE5SruvWBSIcgVqLQIWNHICdNWpgXsJkZP4bIs9XC8QdXSSDy992rtrBtZ3/xsVWZLujLtkssjVZDX+CBbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GBssI90g=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
  "id": -576460752303422397,
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAK+PieZdMntEIjZ84nco0EnMfCmbq/EHkoN9m6p7KxA+YhmPMG9/adRYLp65QxEdY6VSFYiFMczuUjDQLDbDVBLhAo8nusE5SruvWBSIcgVqLQIWNHICdNWpgXsJkZP4bIs9XC8QdXSSDy992rtrBtZ3/xsVWZLujLtkssjVZDX+CBbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GBssI90g==",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_fJksMnqytl+KvvZuAPREIxGPh0DezvNOLGyQ8FDUwWB9ciVV"
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAK+PieZdMntEIjZ84nco0EnMfCmbq/EHkoN9m6p7KxA+YhmPMG9/adRYLp65QxEdY6VSFYiFMczuUjDQLDbDVBLhAo8nusE5SruvWBSIcgVqLQIWNHICdNWpgXsJkZP4bIs9XC8QdXSSDy992rtrBtZ3/xsVWZLujLtkssjVZDX+CBbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GBssI90g==",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAK+PieZdMntEIjZ84nco0EnMfCmbq/EHkoN9m6p7KxA+YhmPMG9/adRYLp65QxEdY6VSFYiFMczuUjDQLDbDVBLhAo8nusE5SruvWBSIcgVqLQIWNHICdNWpgXsJkZP4bIs9XC8QdXSSDy992rtrBtZ3/xsVWZLujLtkssjVZDX+CBbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GBssI90g==",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAK+PieZdMntEIjZ84nco0EnMfCmbq/EHkoN9m6p7KxA+YhmPMG9/adRYLp65QxEdY6VSFYiFMczuUjDQLDbDVBLhAo8nusE5SruvWBSIcgVqLQIWNHICdNWpgXsJkZP4bIs9XC8QdXSSDy992rtrBtZ3/xsVWZLujLtkssjVZDX+CBbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GBssI90g==",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "message": {
        "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "message": {
        "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
  "id": -576460752303422396,
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
  "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
  "id": -576460752303422396,
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "event": "funding_locked"
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "state": "tx_+QEOCwH4hLhAK+PieZdMntEIjZ84nco0EnMfCmbq/EHkoN9m6p7KxA+YhmPMG9/adRYLp65QxEdY6VSFYiFMczuUjDQLDbDVBLhAo8nusE5SruvWBSIcgVqLQIWNHICdNWpgXsJkZP4bIs9XC8QdXSSDy992rtrBtZ3/xsVWZLujLtkssjVZDX+CBbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GBssI90g=="
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "state": "tx_+QEOCwH4hLhAK+PieZdMntEIjZ84nco0EnMfCmbq/EHkoN9m6p7KxA+YhmPMG9/adRYLp65QxEdY6VSFYiFMczuUjDQLDbDVBLhAo8nusE5SruvWBSIcgVqLQIWNHICdNWpgXsJkZP4bIs9XC8QdXSSDy992rtrBtZ3/xsVWZLujLtkssjVZDX+CBbiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4GBssI90g=="
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "message": {
        "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "message": {
        "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
  "method": "channels.deposit",
  "params": {
    "amount": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
      "method": "channels.deposit",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "message": {
        "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "message": {
        "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
  "method": "channels.deposit",
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
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "signed_tx": "tx_+HoLAcC4dfhzMwGhBhU1+yIvX6w4Pthx+ShT1C7BpvF09YSEzsEEmygyAMtxoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gIAhg/FSdDYOKAJfKOkRYFmCfu9WWBbxU0n1wqMcA3FNf3vEd2/gK5qlQKBgj+EOqs=",
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
  "id": -576460752303422395,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+L0LAfhCuECFRiN1UbjecKN0UkpN/+UX9nO+lnxiVxZkNV4f2iNmVlmkv9Gdxs7/1glpB6KIjChRf7o+tOKFQvWE4G2lVAgBuHX4czMBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUnQ2DigCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCgYJ9d0tD"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
  "id": -576460752303422395,
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "signed_tx": "tx_+L0LAfhCuECFRiN1UbjecKN0UkpN/+UX9nO+lnxiVxZkNV4f2iNmVlmkv9Gdxs7/1glpB6KIjChRf7o+tOKFQvWE4G2lVAgBuHX4czMBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUnQ2DigCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCgYJ9d0tD",
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

#### responder ---> node
```javascript
{
  "id": -576460752303422394,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P8LAfiEuECFRiN1UbjecKN0UkpN/+UX9nO+lnxiVxZkNV4f2iNmVlmkv9Gdxs7/1glpB6KIjChRf7o+tOKFQvWE4G2lVAgBuECV7Ohzbma3vaD4iHjub5DAmb+T/T4WY6CLJWEHxddlEMW3AQrPTokCEoegN1bhama/pkVYlB2KHXFiUn1b+OkBuHX4czMBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUnQ2DigCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCgYLtcPgg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
  "id": -576460752303422394,
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P8LAfiEuECFRiN1UbjecKN0UkpN/+UX9nO+lnxiVxZkNV4f2iNmVlmkv9Gdxs7/1glpB6KIjChRf7o+tOKFQvWE4G2lVAgBuECV7Ohzbma3vaD4iHjub5DAmb+T/T4WY6CLJWEHxddlEMW3AQrPTokCEoegN1bhama/pkVYlB2KHXFiUn1b+OkBuHX4czMBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUnQ2DigCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCgYLtcPgg",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P8LAfiEuECFRiN1UbjecKN0UkpN/+UX9nO+lnxiVxZkNV4f2iNmVlmkv9Gdxs7/1glpB6KIjChRf7o+tOKFQvWE4G2lVAgBuECV7Ohzbma3vaD4iHjub5DAmb+T/T4WY6CLJWEHxddlEMW3AQrPTokCEoegN1bhama/pkVYlB2KHXFiUn1b+OkBuHX4czMBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUnQ2DigCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCgYLtcPgg",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "message": {
        "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "message": {
        "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P8LAfiEuECFRiN1UbjecKN0UkpN/+UX9nO+lnxiVxZkNV4f2iNmVlmkv9Gdxs7/1glpB6KIjChRf7o+tOKFQvWE4G2lVAgBuECV7Ohzbma3vaD4iHjub5DAmb+T/T4WY6CLJWEHxddlEMW3AQrPTokCEoegN1bhama/pkVYlB2KHXFiUn1b+OkBuHX4czMBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUnQ2DigCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCgYLtcPgg",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P8LAfiEuECFRiN1UbjecKN0UkpN/+UX9nO+lnxiVxZkNV4f2iNmVlmkv9Gdxs7/1glpB6KIjChRf7o+tOKFQvWE4G2lVAgBuECV7Ohzbma3vaD4iHjub5DAmb+T/T4WY6CLJWEHxddlEMW3AQrPTokCEoegN1bhama/pkVYlB2KHXFiUn1b+OkBuHX4czMBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUnQ2DigCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCgYLtcPgg",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "state": "tx_+P8LAfiEuECFRiN1UbjecKN0UkpN/+UX9nO+lnxiVxZkNV4f2iNmVlmkv9Gdxs7/1glpB6KIjChRf7o+tOKFQvWE4G2lVAgBuECV7Ohzbma3vaD4iHjub5DAmb+T/T4WY6CLJWEHxddlEMW3AQrPTokCEoegN1bhama/pkVYlB2KHXFiUn1b+OkBuHX4czMBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUnQ2DigCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCgYLtcPgg"
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "state": "tx_+P8LAfiEuECFRiN1UbjecKN0UkpN/+UX9nO+lnxiVxZkNV4f2iNmVlmkv9Gdxs7/1glpB6KIjChRf7o+tOKFQvWE4G2lVAgBuECV7Ohzbma3vaD4iHjub5DAmb+T/T4WY6CLJWEHxddlEMW3AQrPTokCEoegN1bhama/pkVYlB2KHXFiUn1b+OkBuHX4czMBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPxUnQ2DigCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCgYLtcPgg"
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "message": {
        "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "message": {
        "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
  "method": "channels.deposit",
  "params": {
    "amount": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
      "method": "channels.deposit",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "message": {
        "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "message": {
        "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
  "method": "channels.deposit",
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
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBhU1+yIvX6w4Pthx+ShT1C7BpvF09YSEzsEEmygyAMtxoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AIAhg/Aobiv0KBdYyosJiEVkIv3UfhREtMPbLmXGvLesTSuRCc8B8rvQgM1WZ5eKQ==",
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
  "id": -576460752303422393,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEBKOiAJuH0Xx4J/a+ySj9kWAqA/gl9NbvTqFylWFi/p7zYZVD2wDQAv6cxpq7vu9QMFHlehvsHvKhFS5yFc3CUJuHT4cjMBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDNefPszA="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
  "id": -576460752303422393,
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEBKOiAJuH0Xx4J/a+ySj9kWAqA/gl9NbvTqFylWFi/p7zYZVD2wDQAv6cxpq7vu9QMFHlehvsHvKhFS5yFc3CUJuHT4cjMBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDNefPszA=",
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

#### initiator ---> node
```javascript
{
  "id": -576460752303422392,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBKOiAJuH0Xx4J/a+ySj9kWAqA/gl9NbvTqFylWFi/p7zYZVD2wDQAv6cxpq7vu9QMFHlehvsHvKhFS5yFc3CUJuEB+BCsDT0CMb8Km5bUptgzoN9KBLdzoxS5e/m6NcTWgsgz1zDnpz/1XQm/1Z6BeA3bcj4Pu4mamfFCctjOoS/wGuHT4cjMBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDNZJRJng="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
  "id": -576460752303422392,
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEBKOiAJuH0Xx4J/a+ySj9kWAqA/gl9NbvTqFylWFi/p7zYZVD2wDQAv6cxpq7vu9QMFHlehvsHvKhFS5yFc3CUJuEB+BCsDT0CMb8Km5bUptgzoN9KBLdzoxS5e/m6NcTWgsgz1zDnpz/1XQm/1Z6BeA3bcj4Pu4mamfFCctjOoS/wGuHT4cjMBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDNZJRJng=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEBKOiAJuH0Xx4J/a+ySj9kWAqA/gl9NbvTqFylWFi/p7zYZVD2wDQAv6cxpq7vu9QMFHlehvsHvKhFS5yFc3CUJuEB+BCsDT0CMb8Km5bUptgzoN9KBLdzoxS5e/m6NcTWgsgz1zDnpz/1XQm/1Z6BeA3bcj4Pu4mamfFCctjOoS/wGuHT4cjMBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDNZJRJng=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "message": {
        "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "message": {
        "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBKOiAJuH0Xx4J/a+ySj9kWAqA/gl9NbvTqFylWFi/p7zYZVD2wDQAv6cxpq7vu9QMFHlehvsHvKhFS5yFc3CUJuEB+BCsDT0CMb8Km5bUptgzoN9KBLdzoxS5e/m6NcTWgsgz1zDnpz/1XQm/1Z6BeA3bcj4Pu4mamfFCctjOoS/wGuHT4cjMBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDNZJRJng=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBKOiAJuH0Xx4J/a+ySj9kWAqA/gl9NbvTqFylWFi/p7zYZVD2wDQAv6cxpq7vu9QMFHlehvsHvKhFS5yFc3CUJuEB+BCsDT0CMb8Km5bUptgzoN9KBLdzoxS5e/m6NcTWgsgz1zDnpz/1XQm/1Z6BeA3bcj4Pu4mamfFCctjOoS/wGuHT4cjMBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDNZJRJng=",
      "type": "channel_deposit_tx"
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "event": "deposit_locked"
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "state": "tx_+P4LAfiEuEBKOiAJuH0Xx4J/a+ySj9kWAqA/gl9NbvTqFylWFi/p7zYZVD2wDQAv6cxpq7vu9QMFHlehvsHvKhFS5yFc3CUJuEB+BCsDT0CMb8Km5bUptgzoN9KBLdzoxS5e/m6NcTWgsgz1zDnpz/1XQm/1Z6BeA3bcj4Pu4mamfFCctjOoS/wGuHT4cjMBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDNZJRJng="
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "state": "tx_+P4LAfiEuEBKOiAJuH0Xx4J/a+ySj9kWAqA/gl9NbvTqFylWFi/p7zYZVD2wDQAv6cxpq7vu9QMFHlehvsHvKhFS5yFc3CUJuEB+BCsDT0CMb8Km5bUptgzoN9KBLdzoxS5e/m6NcTWgsgz1zDnpz/1XQm/1Z6BeA3bcj4Pu4mamfFCctjOoS/wGuHT4cjMBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKG4r9CgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDNZJRJng="
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheNQGhBhU1+yIvX6w4Pthx+ShT1C7BpvF09YSEzsEEmygyAMtxoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+GXW6AGGHK96fwgDAIYPY36W8ACBgyoHgXY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422391,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KgLAfhCuEAdxjjZfFns+B04VPAyKjtMUSUEZsKArK2ujBE6Le78t7iCV7ou1QS8N30URU5CPX8SMmwmgrpdG0D618Cw+HUKuGD4XjUBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1ugBhhyven8IAwCGD2N+lvAAgYMFDgyj"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
  "id": -576460752303422391,
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "signed_tx": "tx_+KgLAfhCuEAdxjjZfFns+B04VPAyKjtMUSUEZsKArK2ujBE6Le78t7iCV7ou1QS8N30URU5CPX8SMmwmgrpdG0D618Cw+HUKuGD4XjUBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1ugBhhyven8IAwCGD2N+lvAAgYMFDgyj",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422390,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OoLAfiEuEAdxjjZfFns+B04VPAyKjtMUSUEZsKArK2ujBE6Le78t7iCV7ou1QS8N30URU5CPX8SMmwmgrpdG0D618Cw+HUKuEA1Zhri2yBJ067LqKzh0yPUq9rHY/zQtXfEI1peU3+aAqqzme2Zz6rbKz+NBqb/dwOTacJXzThYpHlbAnpdX18BuGD4XjUBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1ugBhhyven8IAwCGD2N+lvAAgYPZwU/R"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
  "id": -576460752303422390,
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEAdxjjZfFns+B04VPAyKjtMUSUEZsKArK2ujBE6Le78t7iCV7ou1QS8N30URU5CPX8SMmwmgrpdG0D618Cw+HUKuEA1Zhri2yBJ067LqKzh0yPUq9rHY/zQtXfEI1peU3+aAqqzme2Zz6rbKz+NBqb/dwOTacJXzThYpHlbAnpdX18BuGD4XjUBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1ugBhhyven8IAwCGD2N+lvAAgYPZwU/R",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OoLAfiEuEAdxjjZfFns+B04VPAyKjtMUSUEZsKArK2ujBE6Le78t7iCV7ou1QS8N30URU5CPX8SMmwmgrpdG0D618Cw+HUKuEA1Zhri2yBJ067LqKzh0yPUq9rHY/zQtXfEI1peU3+aAqqzme2Zz6rbKz+NBqb/dwOTacJXzThYpHlbAnpdX18BuGD4XjUBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1ugBhhyven8IAwCGD2N+lvAAgYPZwU/R",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEAdxjjZfFns+B04VPAyKjtMUSUEZsKArK2ujBE6Le78t7iCV7ou1QS8N30URU5CPX8SMmwmgrpdG0D618Cw+HUKuEA1Zhri2yBJ067LqKzh0yPUq9rHY/zQtXfEI1peU3+aAqqzme2Zz6rbKz+NBqb/dwOTacJXzThYpHlbAnpdX18BuGD4XjUBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1ugBhhyven8IAwCGD2N+lvAAgYPZwU/R",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OoLAfiEuEAdxjjZfFns+B04VPAyKjtMUSUEZsKArK2ujBE6Le78t7iCV7ou1QS8N30URU5CPX8SMmwmgrpdG0D618Cw+HUKuEA1Zhri2yBJ067LqKzh0yPUq9rHY/zQtXfEI1peU3+aAqqzme2Zz6rbKz+NBqb/dwOTacJXzThYpHlbAnpdX18BuGD4XjUBoQYVNfsiL1+sOD7YcfkoU9QuwabxdPWEhM7BBJsoMgDLcaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/hl1ugBhhyven8IAwCGD2N+lvAAgYPZwU/R",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
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
    "channel_id": "ch_ALoaQVBGEPs3o89vi3bSDy39nA1oZtP6CjPLAZqrgpmTZn26p",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
