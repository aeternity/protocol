
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&minimum_depth=0&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_reconnect_early%2F2916
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
      "fsm_id": "ba_k7qxTjK6Yp94pwoikersG6cc9g0y8v3SwDgbUFG0qgQhm6nu"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&minimum_depth=0&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_reconnect_early%2F2916
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
      "fsm_id": "ba_46ykTneCyCNptNi9xNChbQeQwt5GOUs6sD0o1mhjPtyC6UuQ"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsZR+tP5A==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423157,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEA+ApFlaxkDPjv28Ij5vsVPEMkmHe71nqwyJdcI+zc0zISdKgJePXt0bVTRgbicyU8GuTX0Plv8wHnw5/5W7CkMuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LGf78ncI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423157,
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
    "data": {
      "fsm_id": "ba_46ykTneCyCNptNi9xNChbQeQwt5GOUs6sD0o1mhjPtyC6UuQ",
      "signed_tx": "tx_+MsLAfhCuEA+ApFlaxkDPjv28Ij5vsVPEMkmHe71nqwyJdcI+zc0zISdKgJePXt0bVTRgbicyU8GuTX0Plv8wHnw5/5W7CkMuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LGf78ncI=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423156,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAPgKRZWsZAz479vCI+b7FTxDJJh3u9Z6sMiXXCPs3NMyEnSoCXj17dG1U0YG4nMlPBrk19D5b/MB58Of+VuwpDLhAxUNIxSARkcu7cYURvIL51hUx/IZjoBVGK+CodV1SvH3qQwcT/TVoHjKkTJuncKA1JJ+h7fQu39ht1ZChlc9KALiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxmtWAu7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
  "id": -576460752303423156,
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAPgKRZWsZAz479vCI+b7FTxDJJh3u9Z6sMiXXCPs3NMyEnSoCXj17dG1U0YG4nMlPBrk19D5b/MB58Of+VuwpDLhAxUNIxSARkcu7cYURvIL51hUx/IZjoBVGK+CodV1SvH3qQwcT/TVoHjKkTJuncKA1JJ+h7fQu39ht1ZChlc9KALiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxmtWAu7",
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_k7qxTjK6Yp94pwoikersG6cc9g0y8v3SwDgbUFG0qgQhm6nu"
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAPgKRZWsZAz479vCI+b7FTxDJJh3u9Z6sMiXXCPs3NMyEnSoCXj17dG1U0YG4nMlPBrk19D5b/MB58Of+VuwpDLhAxUNIxSARkcu7cYURvIL51hUx/IZjoBVGK+CodV1SvH3qQwcT/TVoHjKkTJuncKA1JJ+h7fQu39ht1ZChlc9KALiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxmtWAu7",
      "type": "channel_create_tx"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?existing_channel_id=ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d&existing_fsm_id=ba_k7qxTjK6Yp94pwoikersG6cc9g0y8v3SwDgbUFG0qgQhm6nu&host=localhost&port=13179&protocol=json-rpc&role=initiator
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_k7qxTjK6Yp94pwoikersG6cc9g0y8v3SwDgbUFG0qgQhm6nu"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAPgKRZWsZAz479vCI+b7FTxDJJh3u9Z6sMiXXCPs3NMyEnSoCXj17dG1U0YG4nMlPBrk19D5b/MB58Of+VuwpDLhAxUNIxSARkcu7cYURvIL51hUx/IZjoBVGK+CodV1SvH3qQwcT/TVoHjKkTJuncKA1JJ+h7fQu39ht1ZChlc9KALiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxmtWAu7",
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAPgKRZWsZAz479vCI+b7FTxDJJh3u9Z6sMiXXCPs3NMyEnSoCXj17dG1U0YG4nMlPBrk19D5b/MB58Of+VuwpDLhAxUNIxSARkcu7cYURvIL51hUx/IZjoBVGK+CodV1SvH3qQwcT/TVoHjKkTJuncKA1JJ+h7fQu39ht1ZChlc9KALiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxmtWAu7",
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
    "data": {
      "state": "tx_+QENCwH4hLhAPgKRZWsZAz479vCI+b7FTxDJJh3u9Z6sMiXXCPs3NMyEnSoCXj17dG1U0YG4nMlPBrk19D5b/MB58Of+VuwpDLhAxUNIxSARkcu7cYURvIL51hUx/IZjoBVGK+CodV1SvH3qQwcT/TVoHjKkTJuncKA1JJ+h7fQu39ht1ZChlc9KALiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxmtWAu7"
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
    "data": {
      "state": "tx_+QENCwH4hLhAPgKRZWsZAz479vCI+b7FTxDJJh3u9Z6sMiXXCPs3NMyEnSoCXj17dG1U0YG4nMlPBrk19D5b/MB58Of+VuwpDLhAxUNIxSARkcu7cYURvIL51hUx/IZjoBVGK+CodV1SvH3qQwcT/TVoHjKkTJuncKA1JJ+h7fQu39ht1ZChlc9KALiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCxmtWAu7"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
    "data": {
      "message": {
        "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
    "data": {
      "message": {
        "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
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
  "id": -576460752303423155,
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
  "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
  "id": -576460752303423155,
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBtRCOSJn9NV0UYK47zchEmvhZR+Oss1NvciWyEJuhCDHoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY3+rniy/+GHLHOiuwBAIYPXtZ/KAAaYWWzOQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423154,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEBHwtz0KoioWL/4/qhvN3WD2NhSQ9PSEd+hufKGFrqLlF4aJr+QB3lAQtsYRE+uTUHMRShCpBcs7DWysn8nndsHuF/4XTUBoQbUQjkiZ/TVdFGCuO83IRJr4WUfjrLNTb3IlshCboQgx6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAGlZ7xT8="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
  "id": -576460752303423154,
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEBHwtz0KoioWL/4/qhvN3WD2NhSQ9PSEd+hufKGFrqLlF4aJr+QB3lAQtsYRE+uTUHMRShCpBcs7DWysn8nndsHuF/4XTUBoQbUQjkiZ/TVdFGCuO83IRJr4WUfjrLNTb3IlshCboQgx6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAGlZ7xT8=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423153,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEAiSjkH1bOfG5kN4nolNcS4cJgEE5VUuO6dR7o1FkQJ0aRamiXpXZp9B+Fa8ASO/ex372H4MXcb9eZpNbENAEMLuEBHwtz0KoioWL/4/qhvN3WD2NhSQ9PSEd+hufKGFrqLlF4aJr+QB3lAQtsYRE+uTUHMRShCpBcs7DWysn8nndsHuF/4XTUBoQbUQjkiZ/TVdFGCuO83IRJr4WUfjrLNTb3IlshCboQgx6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAGp36DC8="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
  "id": -576460752303423153,
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAiSjkH1bOfG5kN4nolNcS4cJgEE5VUuO6dR7o1FkQJ0aRamiXpXZp9B+Fa8ASO/ex372H4MXcb9eZpNbENAEMLuEBHwtz0KoioWL/4/qhvN3WD2NhSQ9PSEd+hufKGFrqLlF4aJr+QB3lAQtsYRE+uTUHMRShCpBcs7DWysn8nndsHuF/4XTUBoQbUQjkiZ/TVdFGCuO83IRJr4WUfjrLNTb3IlshCboQgx6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAGp36DC8=",
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAiSjkH1bOfG5kN4nolNcS4cJgEE5VUuO6dR7o1FkQJ0aRamiXpXZp9B+Fa8ASO/ex372H4MXcb9eZpNbENAEMLuEBHwtz0KoioWL/4/qhvN3WD2NhSQ9PSEd+hufKGFrqLlF4aJr+QB3lAQtsYRE+uTUHMRShCpBcs7DWysn8nndsHuF/4XTUBoQbUQjkiZ/TVdFGCuO83IRJr4WUfjrLNTb3IlshCboQgx6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAGp36DC8=",
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAiSjkH1bOfG5kN4nolNcS4cJgEE5VUuO6dR7o1FkQJ0aRamiXpXZp9B+Fa8ASO/ex372H4MXcb9eZpNbENAEMLuEBHwtz0KoioWL/4/qhvN3WD2NhSQ9PSEd+hufKGFrqLlF4aJr+QB3lAQtsYRE+uTUHMRShCpBcs7DWysn8nndsHuF/4XTUBoQbUQjkiZ/TVdFGCuO83IRJr4WUfjrLNTb3IlshCboQgx6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAGp36DC8=",
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuEAiSjkH1bOfG5kN4nolNcS4cJgEE5VUuO6dR7o1FkQJ0aRamiXpXZp9B+Fa8ASO/ex372H4MXcb9eZpNbENAEMLuEBHwtz0KoioWL/4/qhvN3WD2NhSQ9PSEd+hufKGFrqLlF4aJr+QB3lAQtsYRE+uTUHMRShCpBcs7DWysn8nndsHuF/4XTUBoQbUQjkiZ/TVdFGCuO83IRJr4WUfjrLNTb3IlshCboQgx6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGN/q54sv/hhyxzorsAQCGD17WfygAGp36DC8=",
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
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
    "channel_id": "ch_2cUs4qUVpCk2eUKjdtemZ8hs9Z5ZWFy9JDStLCkBZR7rMQcc3d",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
