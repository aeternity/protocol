
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish_responder_stays%2F3750
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
      "fsm_id": "ba_Rn8ne9TjtLpv3fyuqsowrHgEO8zH7oCCQUrG+NF25T3o5S0z"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=true&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_leave_reestablish_responder_stays%2F3750
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
      "fsm_id": "ba_KYuYvb45DRmjnMkkyX2DFDs0eoLxlL1z4Ht/Xcm2y8rmqaop"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsX9GRubw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423217,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDYwKIDVDShPvx2sc0lGW6pLfFJ0bTpMK0qmpNQxh1jHjVK8jTLO0oZlMJPHWIcg3AuunO4gr56EC2lFTU17XkLuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LFw/AR/Q="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423217,
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "fsm_id": "ba_KYuYvb45DRmjnMkkyX2DFDs0eoLxlL1z4Ht/Xcm2y8rmqaop",
      "signed_tx": "tx_+MsLAfhCuEDYwKIDVDShPvx2sc0lGW6pLfFJ0bTpMK0qmpNQxh1jHjVK8jTLO0oZlMJPHWIcg3AuunO4gr56EC2lFTU17XkLuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LFw/AR/Q=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423216,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhA2MCiA1Q0oT78drHNJRluqS3xSdG06TCtKpqTUMYdYx41SvI0yztKGZTCTx1iHINwLrpzuIK+ehAtpRU1Ne15C7hA+TKM/8t4Yx77fpM8vOrDvDQ8evuGKZ2DTOECFeQENhiknw5PhbkWN8ewAzdjvuRHoTh5wpQowULCuHFRht2+BLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxdqiPxr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423216,
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhA2MCiA1Q0oT78drHNJRluqS3xSdG06TCtKpqTUMYdYx41SvI0yztKGZTCTx1iHINwLrpzuIK+ehAtpRU1Ne15C7hA+TKM/8t4Yx77fpM8vOrDvDQ8evuGKZ2DTOECFeQENhiknw5PhbkWN8ewAzdjvuRHoTh5wpQowULCuHFRht2+BLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxdqiPxr",
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_Rn8ne9TjtLpv3fyuqsowrHgEO8zH7oCCQUrG+NF25T3o5S0z"
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhA2MCiA1Q0oT78drHNJRluqS3xSdG06TCtKpqTUMYdYx41SvI0yztKGZTCTx1iHINwLrpzuIK+ehAtpRU1Ne15C7hA+TKM/8t4Yx77fpM8vOrDvDQ8evuGKZ2DTOECFeQENhiknw5PhbkWN8ewAzdjvuRHoTh5wpQowULCuHFRht2+BLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxdqiPxr",
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhA2MCiA1Q0oT78drHNJRluqS3xSdG06TCtKpqTUMYdYx41SvI0yztKGZTCTx1iHINwLrpzuIK+ehAtpRU1Ne15C7hA+TKM/8t4Yx77fpM8vOrDvDQ8evuGKZ2DTOECFeQENhiknw5PhbkWN8ewAzdjvuRHoTh5wpQowULCuHFRht2+BLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxdqiPxr",
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhA2MCiA1Q0oT78drHNJRluqS3xSdG06TCtKpqTUMYdYx41SvI0yztKGZTCTx1iHINwLrpzuIK+ehAtpRU1Ne15C7hA+TKM/8t4Yx77fpM8vOrDvDQ8evuGKZ2DTOECFeQENhiknw5PhbkWN8ewAzdjvuRHoTh5wpQowULCuHFRht2+BLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxdqiPxr",
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "message": {
        "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "message": {
        "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
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
  "id": -576460752303423215,
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
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423215,
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "state": "tx_+QENCwH4hLhA2MCiA1Q0oT78drHNJRluqS3xSdG06TCtKpqTUMYdYx41SvI0yztKGZTCTx1iHINwLrpzuIK+ehAtpRU1Ne15C7hA+TKM/8t4Yx77fpM8vOrDvDQ8evuGKZ2DTOECFeQENhiknw5PhbkWN8ewAzdjvuRHoTh5wpQowULCuHFRht2+BLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxdqiPxr"
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "state": "tx_+QENCwH4hLhA2MCiA1Q0oT78drHNJRluqS3xSdG06TCtKpqTUMYdYx41SvI0yztKGZTCTx1iHINwLrpzuIK+ehAtpRU1Ne15C7hA+TKM/8t4Yx77fpM8vOrDvDQ8evuGKZ2DTOECFeQENhiknw5PhbkWN8ewAzdjvuRHoTh5wpQowULCuHFRht2+BLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxdqiPxr"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "state": "tx_+QENCwH4hLhA2MCiA1Q0oT78drHNJRluqS3xSdG06TCtKpqTUMYdYx41SvI0yztKGZTCTx1iHINwLrpzuIK+ehAtpRU1Ne15C7hA+TKM/8t4Yx77fpM8vOrDvDQ8evuGKZ2DTOECFeQENhiknw5PhbkWN8ewAzdjvuRHoTh5wpQowULCuHFRht2+BLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxdqiPxr"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "state": "tx_+QENCwH4hLhA2MCiA1Q0oT78drHNJRluqS3xSdG06TCtKpqTUMYdYx41SvI0yztKGZTCTx1iHINwLrpzuIK+ehAtpRU1Ne15C7hA+TKM/8t4Yx77fpM8vOrDvDQ8evuGKZ2DTOECFeQENhiknw5PhbkWN8ewAzdjvuRHoTh5wpQowULCuHFRht2+BLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxdqiPxr"
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "event": "peer_disconnected"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P&existing_fsm_id=ba_Rn8ne9TjtLpv3fyuqsowrHgEO8zH7oCCQUrG%2BNF25T3o5S0z&host=localhost&offchain_tx=tx_%2BQENCwH4hLhA2MCiA1Q0oT78drHNJRluqS3xSdG06TCtKpqTUMYdYx41SvI0yztKGZTCTx1iHINwLrpzuIK%2BehAtpRU1Ne15C7hA%2BTKM%2F8t4Yx77fpM8vOrDvDQ8evuGKZ2DTOECFeQENhiknw5PhbkWN8ewAzdjvuRHoTh5wpQowULCuHFRht2%2BBLiD%2BIEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh%2FFEwKX%2BPC9G6hZsWaEiKDybvHpsfS9YsGPmLT%2FC8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxdqiPxr&port=13179&protocol=json-rpc&role=initiator
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
      "fsm_id": "ba_K+8oTTSo8Tuc+bE5/C3uOt0mJ2iaVVJ284DitGr7CEhZmUJo"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "event": "channel_reestablished"
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "event": "channel_reestablished"
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "state": "tx_+QENCwH4hLhA2MCiA1Q0oT78drHNJRluqS3xSdG06TCtKpqTUMYdYx41SvI0yztKGZTCTx1iHINwLrpzuIK+ehAtpRU1Ne15C7hA+TKM/8t4Yx77fpM8vOrDvDQ8evuGKZ2DTOECFeQENhiknw5PhbkWN8ewAzdjvuRHoTh5wpQowULCuHFRht2+BLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxdqiPxr"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423214,
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
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423214,
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

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "meta": 17,
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "meta": 17,
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBm2GN3/xrboFnxkOHYAQXIh+mWIOs6fxYDPwhe7E3bL1AqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAnUhmSQ=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
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
  "id": -576460752303423213,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEA5itglPZUKQGpY4sMG55tbFI7Wu+UKX98QJcn+KcsZupiVNQZtrlOqMXwrJ7R6i0uNkTRzzHuRS1ZokYef3XAIuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKSkwU9"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423213,
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "signed_tx": "tx_+JALAfhCuEA5itglPZUKQGpY4sMG55tbFI7Wu+UKX98QJcn+KcsZupiVNQZtrlOqMXwrJ7R6i0uNkTRzzHuRS1ZokYef3XAIuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKSkwU9",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
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
  "id": -576460752303423212,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA5itglPZUKQGpY4sMG55tbFI7Wu+UKX98QJcn+KcsZupiVNQZtrlOqMXwrJ7R6i0uNkTRzzHuRS1ZokYef3XAIuEB6go9ZSTN2snKlZ5Bl/jtWCck0KiuAJAxY8Mw+52ld5o3YgGezbMal81iHlA7p722/PkU6Bn+YheuIiCvzImoKuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIJ/ZOj"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423212,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "state": "tx_+NILAfiEuEA5itglPZUKQGpY4sMG55tbFI7Wu+UKX98QJcn+KcsZupiVNQZtrlOqMXwrJ7R6i0uNkTRzzHuRS1ZokYef3XAIuEB6go9ZSTN2snKlZ5Bl/jtWCck0KiuAJAxY8Mw+52ld5o3YgGezbMal81iHlA7p722/PkU6Bn+YheuIiCvzImoKuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIJ/ZOj"
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "state": "tx_+NILAfiEuEA5itglPZUKQGpY4sMG55tbFI7Wu+UKX98QJcn+KcsZupiVNQZtrlOqMXwrJ7R6i0uNkTRzzHuRS1ZokYef3XAIuEB6go9ZSTN2snKlZ5Bl/jtWCck0KiuAJAxY8Mw+52ld5o3YgGezbMal81iHlA7p722/PkU6Bn+YheuIiCvzImoKuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIJ/ZOj"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423211,
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
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423211,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999998
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423210,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423210,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA5itglPZUKQGpY4sMG55tbFI7Wu+UKX98QJcn+KcsZupiVNQZtrlOqMXwrJ7R6i0uNkTRzzHuRS1ZokYef3XAIuEB6go9ZSTN2snKlZ5Bl/jtWCck0KiuAJAxY8Mw+52ld5o3YgGezbMal81iHlA7p722/PkU6Bn+YheuIiCvzImoKuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIJ/ZOj",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423209,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423209,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000002
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999998
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "meta": 17,
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "meta": 17,
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBm2GN3/xrboFnxkOHYAQXIh+mWIOs6fxYDPwhe7E3bL1A6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC/98yoA=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
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
  "id": -576460752303423208,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBaBUTpvOIThxOl+Aa8Xvd4vg1S7+jfZUHOdm21rLJsIJTbwrsBdJYEHRyYcjRgBU/LusUjgKF30Ls53XMQy9IKuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgses0NR"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423208,
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBaBUTpvOIThxOl+Aa8Xvd4vg1S7+jfZUHOdm21rLJsIJTbwrsBdJYEHRyYcjRgBU/LusUjgKF30Ls53XMQy9IKuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgses0NR",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
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
  "id": -576460752303423207,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAjoK90zJ20XiSRD2wIix8xagQO5B+X8MLZhdMEEC4Xu65AGG/unQ7MWj4hvVM/gziYYE8zROsbSOj3Sg3uKF4AuEBaBUTpvOIThxOl+Aa8Xvd4vg1S7+jfZUHOdm21rLJsIJTbwrsBdJYEHRyYcjRgBU/LusUjgKF30Ls53XMQy9IKuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvkKby2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423207,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "state": "tx_+NILAfiEuEAjoK90zJ20XiSRD2wIix8xagQO5B+X8MLZhdMEEC4Xu65AGG/unQ7MWj4hvVM/gziYYE8zROsbSOj3Sg3uKF4AuEBaBUTpvOIThxOl+Aa8Xvd4vg1S7+jfZUHOdm21rLJsIJTbwrsBdJYEHRyYcjRgBU/LusUjgKF30Ls53XMQy9IKuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvkKby2"
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "state": "tx_+NILAfiEuEAjoK90zJ20XiSRD2wIix8xagQO5B+X8MLZhdMEEC4Xu65AGG/unQ7MWj4hvVM/gziYYE8zROsbSOj3Sg3uKF4AuEBaBUTpvOIThxOl+Aa8Xvd4vg1S7+jfZUHOdm21rLJsIJTbwrsBdJYEHRyYcjRgBU/LusUjgKF30Ls53XMQy9IKuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvkKby2"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423206,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423206,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000001
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423205,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423205,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAjoK90zJ20XiSRD2wIix8xagQO5B+X8MLZhdMEEC4Xu65AGG/unQ7MWj4hvVM/gziYYE8zROsbSOj3Sg3uKF4AuEBaBUTpvOIThxOl+Aa8Xvd4vg1S7+jfZUHOdm21rLJsIJTbwrsBdJYEHRyYcjRgBU/LusUjgKF30Ls53XMQy9IKuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvkKby2",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423204,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423204,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000001
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "meta": 17,
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "meta": 17,
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBm2GN3/xrboFnxkOHYAQXIh+mWIOs6fxYDPwhe7E3bL1BKCPVbQrAfYXrWTP0iwmtWIe9nj7Tuv+WHg7LyUfwRTSMdXDphs=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
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
  "id": -576460752303423203,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDh800IU/h2CjTxfc2Sc2HiA0Sx5/j7ce30l2UlUE38c5cw29IibYPUgIRmJxgT7ihazZL97tMOlIkQdJZCi8AAuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jE5T6ck"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423203,
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDh800IU/h2CjTxfc2Sc2HiA0Sx5/j7ce30l2UlUE38c5cw29IibYPUgIRmJxgT7ihazZL97tMOlIkQdJZCi8AAuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jE5T6ck",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
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
  "id": -576460752303423202,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAmRZtpNS2y+noz9C+AFHDvzPE5S/ztR0k0sYBRKNsOa5bkUcrU65zhlLmQRRNeGU5xHNs+RUFEAch4Y23l2IoMuEDh800IU/h2CjTxfc2Sc2HiA0Sx5/j7ce30l2UlUE38c5cw29IibYPUgIRmJxgT7ihazZL97tMOlIkQdJZCi8AAuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGRsz4R"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423202,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "state": "tx_+NILAfiEuEAmRZtpNS2y+noz9C+AFHDvzPE5S/ztR0k0sYBRKNsOa5bkUcrU65zhlLmQRRNeGU5xHNs+RUFEAch4Y23l2IoMuEDh800IU/h2CjTxfc2Sc2HiA0Sx5/j7ce30l2UlUE38c5cw29IibYPUgIRmJxgT7ihazZL97tMOlIkQdJZCi8AAuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGRsz4R"
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "state": "tx_+NILAfiEuEAmRZtpNS2y+noz9C+AFHDvzPE5S/ztR0k0sYBRKNsOa5bkUcrU65zhlLmQRRNeGU5xHNs+RUFEAch4Y23l2IoMuEDh800IU/h2CjTxfc2Sc2HiA0Sx5/j7ce30l2UlUE38c5cw29IibYPUgIRmJxgT7ihazZL97tMOlIkQdJZCi8AAuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGRsz4R"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423201,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423201,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000000
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423200,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423200,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAmRZtpNS2y+noz9C+AFHDvzPE5S/ztR0k0sYBRKNsOa5bkUcrU65zhlLmQRRNeGU5xHNs+RUFEAch4Y23l2IoMuEDh800IU/h2CjTxfc2Sc2HiA0Sx5/j7ce30l2UlUE38c5cw29IibYPUgIRmJxgT7ihazZL97tMOlIkQdJZCi8AAuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGRsz4R",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJgALDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgACNzKhd"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423199,
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
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423199,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 70000000000000
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "meta": 17,
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "meta": 17,
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBm2GN3/xrboFnxkOHYAQXIh+mWIOs6fxYDPwhe7E3bL1BaAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC6q4T1k=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
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
  "id": -576460752303423198,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAciODMNc3KNV3PjlodyHYp0Z9X599yV2tKlDIr3OXDjHqmk6/fMg0Kpe9XZzzHACZ51PUWoadxGQXL3dEu0BcDuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsQEcK0"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423198,
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAciODMNc3KNV3PjlodyHYp0Z9X599yV2tKlDIr3OXDjHqmk6/fMg0Kpe9XZzzHACZ51PUWoadxGQXL3dEu0BcDuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsQEcK0",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
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
  "id": -576460752303423197,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAciODMNc3KNV3PjlodyHYp0Z9X599yV2tKlDIr3OXDjHqmk6/fMg0Kpe9XZzzHACZ51PUWoadxGQXL3dEu0BcDuECy1Y4YMvmLqRbOoK7qqzABipejAbHI4/qr/py0OOxlcB6ljtfEdyUvv6MSuQj+FQm2BdQdzFcAPbb3DotS1f8GuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvMkPsw"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423197,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "state": "tx_+NILAfiEuEAciODMNc3KNV3PjlodyHYp0Z9X599yV2tKlDIr3OXDjHqmk6/fMg0Kpe9XZzzHACZ51PUWoadxGQXL3dEu0BcDuECy1Y4YMvmLqRbOoK7qqzABipejAbHI4/qr/py0OOxlcB6ljtfEdyUvv6MSuQj+FQm2BdQdzFcAPbb3DotS1f8GuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvMkPsw"
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "state": "tx_+NILAfiEuEAciODMNc3KNV3PjlodyHYp0Z9X599yV2tKlDIr3OXDjHqmk6/fMg0Kpe9XZzzHACZ51PUWoadxGQXL3dEu0BcDuECy1Y4YMvmLqRbOoK7qqzABipejAbHI4/qr/py0OOxlcB6ljtfEdyUvv6MSuQj+FQm2BdQdzFcAPbb3DotS1f8GuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvMkPsw"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423196,
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
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423196,
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

#### initiator ---> node
```javascript
{
  "id": -576460752303423195,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423195,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAciODMNc3KNV3PjlodyHYp0Z9X599yV2tKlDIr3OXDjHqmk6/fMg0Kpe9XZzzHACZ51PUWoadxGQXL3dEu0BcDuECy1Y4YMvmLqRbOoK7qqzABipejAbHI4/qr/py0OOxlcB6ljtfEdyUvv6MSuQj+FQm2BdQdzFcAPbb3DotS1f8GuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9QWgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgvMkPsw",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423194,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423194,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000001
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": "1",
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "meta": 17,
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "meta": 17,
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBm2GN3/xrboFnxkOHYAQXIh+mWIOs6fxYDPwhe7E3bL1BqCPVbQrAfYXrWTP0iwmtWIe9nj7Tuv+WHg7LyUfwRTSMdKBbDk=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
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
  "id": -576460752303423193,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDkxF4nKY85fOnOXVWxOVu6K069MijJZGgyzzaDJcT63v9u2FWD8s3DxiKA7NPmRw/0EIOYEM5rnvyJQ6dWTosAuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9Qagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGk6ZIu"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423193,
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDkxF4nKY85fOnOXVWxOVu6K069MijJZGgyzzaDJcT63v9u2FWD8s3DxiKA7NPmRw/0EIOYEM5rnvyJQ6dWTosAuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9Qagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jGk6ZIu",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
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
  "id": -576460752303423192,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECvDouWLKDQLyQZeWnLq7bNCerB86aGFAjHqlu/6GjJdFUhqHFlXWRR9FIHk9MbvbEiHwyC73UsbPM6iFYwmIAHuEDkxF4nKY85fOnOXVWxOVu6K069MijJZGgyzzaDJcT63v9u2FWD8s3DxiKA7NPmRw/0EIOYEM5rnvyJQ6dWTosAuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9Qagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jFldA2T"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423192,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "state": "tx_+NILAfiEuECvDouWLKDQLyQZeWnLq7bNCerB86aGFAjHqlu/6GjJdFUhqHFlXWRR9FIHk9MbvbEiHwyC73UsbPM6iFYwmIAHuEDkxF4nKY85fOnOXVWxOVu6K069MijJZGgyzzaDJcT63v9u2FWD8s3DxiKA7NPmRw/0EIOYEM5rnvyJQ6dWTosAuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9Qagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jFldA2T"
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
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "state": "tx_+NILAfiEuECvDouWLKDQLyQZeWnLq7bNCerB86aGFAjHqlu/6GjJdFUhqHFlXWRR9FIHk9MbvbEiHwyC73UsbPM6iFYwmIAHuEDkxF4nKY85fOnOXVWxOVu6K069MijJZGgyzzaDJcT63v9u2FWD8s3DxiKA7NPmRw/0EIOYEM5rnvyJQ6dWTosAuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9Qagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jFldA2T"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423191,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423191,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000000
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423190,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423190,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECvDouWLKDQLyQZeWnLq7bNCerB86aGFAjHqlu/6GjJdFUhqHFlXWRR9FIHk9MbvbEiHwyC73UsbPM6iFYwmIAHuEDkxF4nKY85fOnOXVWxOVu6K069MijJZGgyzzaDJcT63v9u2FWD8s3DxiKA7NPmRw/0EIOYEM5rnvyJQ6dWTosAuEj4RjkCoQZthjd/8a26BZ8ZDh2AEFyIfpliDrOn8WAz8IXuxN2y9Qagj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jFldA2T",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJgALDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgACNzKhd"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423189,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423189,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423188,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_qEekT2VzhiStYHcnQV1KCh6UPtj3fwrD4NCDL8MXvXsJpAf9P",
  "id": -576460752303423188,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
