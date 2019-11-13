
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&fee=123456789876543&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=initiator
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
      "fsm_id": "ba_m47khN9gV6tjBDmdPRgtPB/O9Xmi0hLQJjoR/Kj4+xsaLExF"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&fee=123456789876543&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=responder
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
      "fsm_id": "ba_/NN+6hsHeNQQvvREPF8PSGAZq6+/6aHClAAwffuoPnkjHe5I"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhnBIhhsPP8CgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYfnxRuhg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422992,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEB3XESjWz9Wk3yY8AlX7MNnq2t3qjjdo7a5mpDh01yzuZndNc/olR8cz81zrr1AL0lYIeGeIZnGHGt/mv3BIfcPuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIZwSIYbDz/AoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2HzOVUvc="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422992,
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
    "channel_id": null,
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
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+MsLAfhCuEB3XESjWz9Wk3yY8AlX7MNnq2t3qjjdo7a5mpDh01yzuZndNc/olR8cz81zrr1AL0lYIeGeIZnGHGt/mv3BIfcPuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIZwSIYbDz/AoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2HzOVUvc=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422991,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAd1xEo1s/VpN8mPAJV+zDZ6trd6o43aO2uZqQ4dNcs7mZ3TXP6JUfHM/Nc669QC9JWCHhniGZxhxrf5r9wSH3D7hAjJSMLX9+UMountu3D084ZApu3ecz0MskGgFLi0hSt/Ee6TqeyFKm14ce6ozGzJuB86Dqh9iq8BmQedQe3qWoCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGcEiGGw8/wKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdh8g3AUX"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422991,
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAd1xEo1s/VpN8mPAJV+zDZ6trd6o43aO2uZqQ4dNcs7mZ3TXP6JUfHM/Nc669QC9JWCHhniGZxhxrf5r9wSH3D7hAjJSMLX9+UMountu3D084ZApu3ecz0MskGgFLi0hSt/Ee6TqeyFKm14ce6ozGzJuB86Dqh9iq8BmQedQe3qWoCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGcEiGGw8/wKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdh8g3AUX",
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
    "channel_id": null,
    "data": {
      "event": "funding_signed"
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAd1xEo1s/VpN8mPAJV+zDZ6trd6o43aO2uZqQ4dNcs7mZ3TXP6JUfHM/Nc669QC9JWCHhniGZxhxrf5r9wSH3D7hAjJSMLX9+UMountu3D084ZApu3ecz0MskGgFLi0hSt/Ee6TqeyFKm14ce6ozGzJuB86Dqh9iq8BmQedQe3qWoCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGcEiGGw8/wKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdh8g3AUX",
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAd1xEo1s/VpN8mPAJV+zDZ6trd6o43aO2uZqQ4dNcs7mZ3TXP6JUfHM/Nc669QC9JWCHhniGZxhxrf5r9wSH3D7hAjJSMLX9+UMountu3D084ZApu3ecz0MskGgFLi0hSt/Ee6TqeyFKm14ce6ozGzJuB86Dqh9iq8BmQedQe3qWoCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGcEiGGw8/wKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdh8g3AUX",
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAd1xEo1s/VpN8mPAJV+zDZ6trd6o43aO2uZqQ4dNcs7mZ3TXP6JUfHM/Nc669QC9JWCHhniGZxhxrf5r9wSH3D7hAjJSMLX9+UMountu3D084ZApu3ecz0MskGgFLi0hSt/Ee6TqeyFKm14ce6ozGzJuB86Dqh9iq8BmQedQe3qWoCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGcEiGGw8/wKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdh8g3AUX",
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
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
    "data": {
      "message": {
        "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
        "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
        "info": "Hello",
        "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
    "data": {
      "message": {
        "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
        "info": "Hello back",
        "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422990,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
  "id": -576460752303422990,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 69999999999999
    },
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
    "data": {
      "state": "tx_+QENCwH4hLhAd1xEo1s/VpN8mPAJV+zDZ6trd6o43aO2uZqQ4dNcs7mZ3TXP6JUfHM/Nc669QC9JWCHhniGZxhxrf5r9wSH3D7hAjJSMLX9+UMountu3D084ZApu3ecz0MskGgFLi0hSt/Ee6TqeyFKm14ce6ozGzJuB86Dqh9iq8BmQedQe3qWoCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGcEiGGw8/wKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdh8g3AUX"
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
    "data": {
      "state": "tx_+QENCwH4hLhAd1xEo1s/VpN8mPAJV+zDZ6trd6o43aO2uZqQ4dNcs7mZ3TXP6JUfHM/Nc669QC9JWCHhniGZxhxrf5r9wSH3D7hAjJSMLX9+UMountu3D084ZApu3ecz0MskGgFLi0hSt/Ee6TqeyFKm14ce6ozGzJuB86Dqh9iq8BmQedQe3qWoCriD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGcEiGGw8/wKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdh8g3AUX"
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBjobskfxtIUVbHQ6Q1/oLe+pauOUMmzt8mRkZj39EnF5oQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY2kdavv/+GG0jrV+ABAIYSMJzlQAAggpT06A==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422989,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEDtID2RotLdMI3vHVpRU0+I87Jzriw3xXqEG/jW6cqloKHwGUew0NE/AAP3VoeUIaYt1K90vlNaxarGHbrPswUPuF/4XTUBoQY6G7JH8bSFFWx0OkNf6C3vqWrjlDJs7fJkZGY9/RJxeaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7//hhtI61fgAQCGEjCc5UAAIDty1nQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
  "id": -576460752303422989,
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEDtID2RotLdMI3vHVpRU0+I87Jzriw3xXqEG/jW6cqloKHwGUew0NE/AAP3VoeUIaYt1K90vlNaxarGHbrPswUPuF/4XTUBoQY6G7JH8bSFFWx0OkNf6C3vqWrjlDJs7fJkZGY9/RJxeaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7//hhtI61fgAQCGEjCc5UAAIDty1nQ=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422988,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuECwYo9cVPXGFMd1IbjcGNxSKml70Ttf9JUM3e1kko/1a0dkBUafZb1qJ1OSo3jTODPCN+vo45Wl194qBPGWnK4PuEDtID2RotLdMI3vHVpRU0+I87Jzriw3xXqEG/jW6cqloKHwGUew0NE/AAP3VoeUIaYt1K90vlNaxarGHbrPswUPuF/4XTUBoQY6G7JH8bSFFWx0OkNf6C3vqWrjlDJs7fJkZGY9/RJxeaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7//hhtI61fgAQCGEjCc5UAAIPx7pS0="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
  "id": -576460752303422988,
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuECwYo9cVPXGFMd1IbjcGNxSKml70Ttf9JUM3e1kko/1a0dkBUafZb1qJ1OSo3jTODPCN+vo45Wl194qBPGWnK4PuEDtID2RotLdMI3vHVpRU0+I87Jzriw3xXqEG/jW6cqloKHwGUew0NE/AAP3VoeUIaYt1K90vlNaxarGHbrPswUPuF/4XTUBoQY6G7JH8bSFFWx0OkNf6C3vqWrjlDJs7fJkZGY9/RJxeaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7//hhtI61fgAQCGEjCc5UAAIPx7pS0=",
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuECwYo9cVPXGFMd1IbjcGNxSKml70Ttf9JUM3e1kko/1a0dkBUafZb1qJ1OSo3jTODPCN+vo45Wl194qBPGWnK4PuEDtID2RotLdMI3vHVpRU0+I87Jzriw3xXqEG/jW6cqloKHwGUew0NE/AAP3VoeUIaYt1K90vlNaxarGHbrPswUPuF/4XTUBoQY6G7JH8bSFFWx0OkNf6C3vqWrjlDJs7fJkZGY9/RJxeaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7//hhtI61fgAQCGEjCc5UAAIPx7pS0=",
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuECwYo9cVPXGFMd1IbjcGNxSKml70Ttf9JUM3e1kko/1a0dkBUafZb1qJ1OSo3jTODPCN+vo45Wl194qBPGWnK4PuEDtID2RotLdMI3vHVpRU0+I87Jzriw3xXqEG/jW6cqloKHwGUew0NE/AAP3VoeUIaYt1K90vlNaxarGHbrPswUPuF/4XTUBoQY6G7JH8bSFFWx0OkNf6C3vqWrjlDJs7fJkZGY9/RJxeaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7//hhtI61fgAQCGEjCc5UAAIPx7pS0=",
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuECwYo9cVPXGFMd1IbjcGNxSKml70Ttf9JUM3e1kko/1a0dkBUafZb1qJ1OSo3jTODPCN+vo45Wl194qBPGWnK4PuEDtID2RotLdMI3vHVpRU0+I87Jzriw3xXqEG/jW6cqloKHwGUew0NE/AAP3VoeUIaYt1K90vlNaxarGHbrPswUPuF/4XTUBoQY6G7JH8bSFFWx0OkNf6C3vqWrjlDJs7fJkZGY9/RJxeaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7//hhtI61fgAQCGEjCc5UAAIPx7pS0=",
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
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
    "channel_id": "ch_SbJ9jrKpDqoeog4VvfMeydL6S9ryQx6Ncuqx2Lq9NZNEEvFZP",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```

#### responder closes WebSocket connection
```

```
