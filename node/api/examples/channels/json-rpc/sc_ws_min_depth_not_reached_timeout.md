
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&minimum_depth=1&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_min_depth_not_reached_timeout_%2F2870&timeout_funding_lock=3000
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
      "fsm_id": "ba_zEmfXq9ExD7pK1IWthqTaA2OxqFpb7QEkmV/vhLgwuxqnTf8"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&minimum_depth=1&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_min_depth_not_reached_timeout_%2F2870&timeout_funding_lock=3000
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
      "fsm_id": "ba_f/qKpHtYNc05hsqliKaJtyFFLX9U5qgd6dU1q8NYjTDi+zQ6"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsBYcY30g==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423488,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAujVfMNxn4WtR/xiGHOT1TaG4jIz4YWumjdEUBm9EJMURyngUsZm+FcfudmCDcTGe0iYxOmksiohthEH+3wBAHuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAYBq42o="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423488,
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
    "channel_id": "ch_21w1yRK33VJ38qEZTvfgTog7dP8nCtFt9q7sX7eG2gSRVbVyLg",
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
    "channel_id": "ch_21w1yRK33VJ38qEZTvfgTog7dP8nCtFt9q7sX7eG2gSRVbVyLg",
    "data": {
      "fsm_id": "ba_f/qKpHtYNc05hsqliKaJtyFFLX9U5qgd6dU1q8NYjTDi+zQ6",
      "signed_tx": "tx_+MsLAfhCuEAujVfMNxn4WtR/xiGHOT1TaG4jIz4YWumjdEUBm9EJMURyngUsZm+FcfudmCDcTGe0iYxOmksiohthEH+3wBAHuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LAYBq42o=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423487,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAEJ28xQAsbQTpG+05994pyouvvg/h1/sCByS9wfxrfTR61CS5kC5ZHL+Esi9Wr9+qlWhSh+P2jelq/sMt6J/6AbhALo1XzDcZ+FrUf8Yhhzk9U2huIyM+GFrpo3RFAZvRCTFEcp4FLGZvhXH7nZgg3ExntImMTppLIqIbYRB/t8AQB7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwHTJRqL"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_21w1yRK33VJ38qEZTvfgTog7dP8nCtFt9q7sX7eG2gSRVbVyLg",
  "id": -576460752303423487,
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
    "channel_id": "ch_21w1yRK33VJ38qEZTvfgTog7dP8nCtFt9q7sX7eG2gSRVbVyLg",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAEJ28xQAsbQTpG+05994pyouvvg/h1/sCByS9wfxrfTR61CS5kC5ZHL+Esi9Wr9+qlWhSh+P2jelq/sMt6J/6AbhALo1XzDcZ+FrUf8Yhhzk9U2huIyM+GFrpo3RFAZvRCTFEcp4FLGZvhXH7nZgg3ExntImMTppLIqIbYRB/t8AQB7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwHTJRqL",
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
    "channel_id": "ch_21w1yRK33VJ38qEZTvfgTog7dP8nCtFt9q7sX7eG2gSRVbVyLg",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_zEmfXq9ExD7pK1IWthqTaA2OxqFpb7QEkmV/vhLgwuxqnTf8"
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
    "channel_id": "ch_21w1yRK33VJ38qEZTvfgTog7dP8nCtFt9q7sX7eG2gSRVbVyLg",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAEJ28xQAsbQTpG+05994pyouvvg/h1/sCByS9wfxrfTR61CS5kC5ZHL+Esi9Wr9+qlWhSh+P2jelq/sMt6J/6AbhALo1XzDcZ+FrUf8Yhhzk9U2huIyM+GFrpo3RFAZvRCTFEcp4FLGZvhXH7nZgg3ExntImMTppLIqIbYRB/t8AQB7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwHTJRqL",
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
    "channel_id": "ch_21w1yRK33VJ38qEZTvfgTog7dP8nCtFt9q7sX7eG2gSRVbVyLg",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAEJ28xQAsbQTpG+05994pyouvvg/h1/sCByS9wfxrfTR61CS5kC5ZHL+Esi9Wr9+qlWhSh+P2jelq/sMt6J/6AbhALo1XzDcZ+FrUf8Yhhzk9U2huIyM+GFrpo3RFAZvRCTFEcp4FLGZvhXH7nZgg3ExntImMTppLIqIbYRB/t8AQB7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwHTJRqL",
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
    "channel_id": "ch_21w1yRK33VJ38qEZTvfgTog7dP8nCtFt9q7sX7eG2gSRVbVyLg",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAEJ28xQAsbQTpG+05994pyouvvg/h1/sCByS9wfxrfTR61CS5kC5ZHL+Esi9Wr9+qlWhSh+P2jelq/sMt6J/6AbhALo1XzDcZ+FrUf8Yhhzk9U2huIyM+GFrpo3RFAZvRCTFEcp4FLGZvhXH7nZgg3ExntImMTppLIqIbYRB/t8AQB7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwHTJRqL",
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
    "channel_id": "ch_21w1yRK33VJ38qEZTvfgTog7dP8nCtFt9q7sX7eG2gSRVbVyLg",
    "data": {
      "event": "timeout"
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
    "channel_id": "ch_21w1yRK33VJ38qEZTvfgTog7dP8nCtFt9q7sX7eG2gSRVbVyLg",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_21w1yRK33VJ38qEZTvfgTog7dP8nCtFt9q7sX7eG2gSRVbVyLg",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection
