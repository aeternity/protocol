
#### initiator opens a WebSocket connection (2019-03-13 11:13:18.575)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9&role=initiator
```

#### responder opens a WebSocket connection (2019-03-13 11:13:18.599)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9&role=responder
```

#### responder <--- node (2019-03-13 11:13:19.683)
```javascript
{
  "action": "info",
  "channel_id": null,
  "payload": {
    "event": "channel_open"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:19.686)
```javascript
{
  "action": "info",
  "channel_id": null,
  "payload": {
    "event": "channel_accept"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:19.732)
```javascript
{
  "action": "sign",
  "channel_id": null,
  "payload": {
    "tx": "tx_+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgFlP/27"
  },
  "tag": "initiator_sign",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:19.811)
```javascript
{
  "action": "initiator_sign",
  "payload": {
    "tx": "tx_+MsLAfhCuEAZPgdWv8+wl3Cg3etoy4hQDP/rgbzAt/gBf/XQcgTxrB3X0J015OGkxW8sD1fWXfGSzNTsZ8c53o2TZPRRqaYAuIP4gTIBoQEMHR+jKB9TfmalcAw4HlPfLlTP4fGLC6AeHxDL+MjeeoY/qiUiYAChAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrhiRhOcqAAAIKAIYSMJzlQADAoBVQItrXeXi1NNVLrFNRky7mqhur6CrV3Ihp6ANYAJVSAXebcgc="
  }
}
```

#### responder <--- node (2019-03-13 11:13:19.847)
```javascript
{
  "action": "info",
  "channel_id": null,
  "payload": {
    "event": "funding_created"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:19.848)
```javascript
{
  "action": "sign",
  "channel_id": null,
  "payload": {
    "tx": "tx_+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgFlP/27"
  },
  "tag": "responder_sign",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:13:19.849)
```javascript
{
  "action": "responder_sign",
  "payload": {
    "tx": "tx_+MsLAfhCuEDpacoKU21wE0LkI7Bs8/iwAXuY1NKx/KRrACvlxJ7IR14rxk7Mx7IFgL4c64jFWy94TTFpLfXgZn/vZAusYgoPuIP4gTIBoQEMHR+jKB9TfmalcAw4HlPfLlTP4fGLC6AeHxDL+MjeeoY/qiUiYAChAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrhiRhOcqAAAIKAIYSMJzlQADAoBVQItrXeXi1NNVLrFNRky7mqhur6CrV3Ihp6ANYAJVSAZHEUaY="
  }
}
```

#### responder <--- node (2019-03-13 11:13:19.861)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": null,
  "payload": {
    "tx": "tx_+QENCwH4hLhAGT4HVr/PsJdwoN3raMuIUAz/64G8wLf4AX/10HIE8awd19CdNeThpMVvLA9X1l3xkszU7GfHOd6Nk2T0UammALhA6WnKClNtcBNC5COwbPP4sAF7mNTSsfykawAr5cSeyEdeK8ZOzMeyBYC+HOuIxVsveE0xaS314GZ/72QLrGIKD7iD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgGhFaYU"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:19.862)
```javascript
{
  "action": "info",
  "channel_id": null,
  "payload": {
    "event": "funding_signed"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:19.865)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": null,
  "payload": {
    "tx": "tx_+QENCwH4hLhAGT4HVr/PsJdwoN3raMuIUAz/64G8wLf4AX/10HIE8awd19CdNeThpMVvLA9X1l3xkszU7GfHOd6Nk2T0UammALhA6WnKClNtcBNC5COwbPP4sAF7mNTSsfykawAr5cSeyEdeK8ZOzMeyBYC+HOuIxVsveE0xaS314GZ/72QLrGIKD7iD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgGhFaYU"
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:21.451)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn",
      "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- node (2019-03-13 11:13:21.457)
```javascript
{
  "action": "get",
  "channel_id": null,
  "payload": [
    {
      "account": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn",
      "balance": 69999999999999
    },
    {
      "account": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
      "balance": 40000000000001
    }
  ],
  "tag": "balances",
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:23.29)
```javascript
{
  "action": "info",
  "channel_id": null,
  "payload": {
    "event": "own_funding_locked"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:23.30)
```javascript
{
  "action": "info",
  "channel_id": null,
  "payload": {
    "event": "own_funding_locked"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:23.33)
```javascript
{
  "action": "info",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "event": "funding_locked"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:23.38)
```javascript
{
  "action": "info",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "event": "funding_locked"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:23.54)
```javascript
{
  "action": "info",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "event": "open"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:23.67)
```javascript
{
  "action": "update",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "state": "tx_+QENCwH4hLhAGT4HVr/PsJdwoN3raMuIUAz/64G8wLf4AX/10HIE8awd19CdNeThpMVvLA9X1l3xkszU7GfHOd6Nk2T0UammALhA6WnKClNtcBNC5COwbPP4sAF7mNTSsfykawAr5cSeyEdeK8ZOzMeyBYC+HOuIxVsveE0xaS314GZ/72QLrGIKD7iD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgGhFaYU"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:23.68)
```javascript
{
  "action": "info",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "event": "open"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:23.76)
```javascript
{
  "action": "update",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "state": "tx_+QENCwH4hLhAGT4HVr/PsJdwoN3raMuIUAz/64G8wLf4AX/10HIE8awd19CdNeThpMVvLA9X1l3xkszU7GfHOd6Nk2T0UammALhA6WnKClNtcBNC5COwbPP4sAF7mNTSsfykawAr5cSeyEdeK8ZOzMeyBYC+HOuIxVsveE0xaS314GZ/72QLrGIKD7iD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgGhFaYU"
  },
  "version": 1
}
```

#### initiator: (2019-03-13 11:13:23.161)
> Funding has been confirmed locally on-chain

#### responder: (2019-03-13 11:13:23.161)
> Funding has been confirmed locally on-chain

#### initiator: (2019-03-13 11:13:23.161)
> Funding has been confirmed on-chain by other party

#### responder: (2019-03-13 11:13:23.161)
> Funding has been confirmed on-chain by other party

#### initiator: (2019-03-13 11:13:23.161)
> Channel is `open` and ready to use

#### responder: (2019-03-13 11:13:23.162)
> Channel is `open` and ready to use

#### initiator ---> node (2019-03-13 11:13:23.162)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn",
      "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- node (2019-03-13 11:13:23.170)
```javascript
{
  "action": "get",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": [
    {
      "account": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn",
      "balance": 69999999999999
    },
    {
      "account": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
      "balance": 40000000000001
    }
  ],
  "tag": "balances",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:23.171)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 1,
    "from": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn",
    "to": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9"
  },
  "tag": "new"
}
```

#### initiator <--- node (2019-03-13 11:13:23.220)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "tx": "tx_+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQC+E24S/hJggI6AaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAaA7pv4mg8xv+FCuz/dffsQJfmMd+RvIpdZVGhCPqJtqsgciGJg="
  },
  "tag": "update",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:23.221)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEAtwaprWsNPCN6eaGpepnJY4C+N5/Baj341mwtG+Om/PFD1Qfn+vFdf5m3vYbdy6fnkW+Sdk7lp79lYD22ijzIAuJf4lTkBoQad06vsKcGdNdgD7xA+KpuVMsQpGpIGboLmtvpN50ZCtAL4TbhL+EmCAjoBoQEMHR+jKB9TfmalcAw4HlPfLlTP4fGLC6AeHxDL+MjeeqEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFysBoDum/iaDzG/4UK7P919+xAl+Yx35G8il1lUaEI+om2qyl8wNeg=="
  }
}
```

#### responder <--- node (2019-03-13 11:13:23.280)
```javascript
{
  "action": "info",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "event": "update"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:23.281)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "tx": "tx_+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQC+E24S/hJggI6AaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAaA7pv4mg8xv+FCuz/dffsQJfmMd+RvIpdZVGhCPqJtqsgciGJg="
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:13:23.282)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+N8LAfhCuEA8scj3IKY/EzPOk1EkOQG0EUAQvw+JRl0wpdOueuOMCRcmXfgRh7k6rWreIfKdttOmJ30Jf5+CaEq54Srs+x4CuJf4lTkBoQad06vsKcGdNdgD7xA+KpuVMsQpGpIGboLmtvpN50ZCtAL4TbhL+EmCAjoBoQEMHR+jKB9TfmalcAw4HlPfLlTP4fGLC6AeHxDL+MjeeqEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFysBoDum/iaDzG/4UK7P919+xAl+Yx35G8il1lUaEI+om2qyiGse2g=="
  }
}
```

#### responder <--- node (2019-03-13 11:13:23.320)
```javascript
{
  "action": "update",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "state": "tx_+QEhCwH4hLhALcGqa1rDTwjenmhqXqZyWOAvjefwWo9+NZsLRvjpvzxQ9UH5/rxXX+Zt72G3cun55FvknZO5ae/ZWA9too8yALhAPLHI9yCmPxMzzpNRJDkBtBFAEL8PiUZdMKXTrnrjjAkXJl34EYe5Oq1q3iHynbbTpid9CX+fgmhKueEq7PseAriX+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQC+E24S/hJggI6AaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAaA7pv4mg8xv+FCuz/dffsQJfmMd+RvIpdZVGhCPqJtqspFy8s8="
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:23.344)
```javascript
{
  "action": "update",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "state": "tx_+QEhCwH4hLhALcGqa1rDTwjenmhqXqZyWOAvjefwWo9+NZsLRvjpvzxQ9UH5/rxXX+Zt72G3cun55FvknZO5ae/ZWA9too8yALhAPLHI9yCmPxMzzpNRJDkBtBFAEL8PiUZdMKXTrnrjjAkXJl34EYe5Oq1q3iHynbbTpid9CX+fgmhKueEq7PseAriX+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQC+E24S/hJggI6AaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAaA7pv4mg8xv+FCuz/dffsQJfmMd+RvIpdZVGhCPqJtqspFy8s8="
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:23.355)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn",
      "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- node (2019-03-13 11:13:23.359)
```javascript
{
  "action": "get",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": [
    {
      "account": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn",
      "balance": 69999999999998
    },
    {
      "account": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
      "balance": 40000000000002
    }
  ],
  "tag": "balances",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:23.360)
```javascript
{
  "action": "get",
  "payload": {
    "a": "a"
  },
  "tag": "offchain_state"
}
```

#### initiator <--- node (2019-03-13 11:13:23.365)
```javascript
{
  "action": "get",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhALcGqa1rDTwjenmhqXqZyWOAvjefwWo9+NZsLRvjpvzxQ9UH5/rxXX+Zt72G3cun55FvknZO5ae/ZWA9too8yALhAPLHI9yCmPxMzzpNRJDkBtBFAEL8PiUZdMKXTrnrjjAkXJl34EYe5Oq1q3iHynbbTpid9CX+fgmhKueEq7PseAriX+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQC+E24S/hJggI6AaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAaA7pv4mg8xv+FCuz/dffsQJfmMd+RvIpdZVGhCPqJtqspFy8s8=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaClZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4vKCgEAhiRhOcqAArDvQAGgDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqLygoBAIY/qiUiX/69jYLo"
  },
  "tag": "offchain_state",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:23.376)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
      "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- node (2019-03-13 11:13:23.389)
```javascript
{
  "action": "get",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": [
    {
      "account": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
      "balance": 40000000000002
    },
    {
      "account": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn",
      "balance": 69999999999998
    }
  ],
  "tag": "balances",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:13:23.391)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 1,
    "from": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
    "to": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn"
  },
  "tag": "new"
}
```

#### responder <--- node (2019-03-13 11:13:23.404)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "tx": "tx_+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQD+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUopHXho="
  },
  "tag": "update",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:13:23.406)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEBqu92xsWPoYoU02ES0cP/0CD6J6+2BRiaDi+fLjfdG3pYODd2Mk6ntEjIdQwqI4yYul7NXANVVrE654UvXL/gOuJf4lTkBoQad06vsKcGdNdgD7xA+KpuVMsQpGpIGboLmtvpN50ZCtAP4TbhL+EmCAjoBoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK6EBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noBoBVQItrXeXi1NNVLrFNRky7mqhur6CrV3Ihp6ANYAJVSOeYVNA=="
  }
}
```

#### initiator <--- node (2019-03-13 11:13:23.462)
```javascript
{
  "action": "info",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "event": "update"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:23.465)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "tx": "tx_+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQD+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUopHXho="
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:23.467)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+N8LAfhCuECtKYmf0KJgCW19hvqdUCR3VpuAmDIeHho7MDjcRQ7aKpXG9bF//ouejWGNOvH7UuEFMbISGoQ0c959Ikmk1dwFuJf4lTkBoQad06vsKcGdNdgD7xA+KpuVMsQpGpIGboLmtvpN50ZCtAP4TbhL+EmCAjoBoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK6EBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noBoBVQItrXeXi1NNVLrFNRky7mqhur6CrV3Ihp6ANYAJVSzDcH6g=="
  }
}
```

#### initiator <--- node (2019-03-13 11:13:23.505)
```javascript
{
  "action": "update",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "state": "tx_+QEhCwH4hLhAarvdsbFj6GKFNNhEtHD/9Ag+ievtgUYmg4vny433Rt6WDg3djJOp7RIyHUMKiOMmLpezVwDVVaxOueFL1y/4DrhArSmJn9CiYAltfYb6nVAkd1abgJgyHh4aOzA43EUO2iqVxvWxf/6Lno1hjTrx+1LhBTGyEhqENHPefSJJpNXcBbiX+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQD+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUmRYMY0="
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:23.519)
```javascript
{
  "action": "update",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "state": "tx_+QEhCwH4hLhAarvdsbFj6GKFNNhEtHD/9Ag+ievtgUYmg4vny433Rt6WDg3djJOp7RIyHUMKiOMmLpezVwDVVaxOueFL1y/4DrhArSmJn9CiYAltfYb6nVAkd1abgJgyHh4aOzA43EUO2iqVxvWxf/6Lno1hjTrx+1LhBTGyEhqENHPefSJJpNXcBbiX+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQD+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUmRYMY0="
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:23.532)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
      "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- node (2019-03-13 11:13:23.537)
```javascript
{
  "action": "get",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": [
    {
      "account": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
      "balance": 40000000000001
    },
    {
      "account": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn",
      "balance": 69999999999999
    }
  ],
  "tag": "balances",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:23.538)
```javascript
{
  "action": "get",
  "payload": {
    "a": "a"
  },
  "tag": "offchain_state"
}
```

#### initiator <--- node (2019-03-13 11:13:23.546)
```javascript
{
  "action": "get",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAarvdsbFj6GKFNNhEtHD/9Ag+ievtgUYmg4vny433Rt6WDg3djJOp7RIyHUMKiOMmLpezVwDVVaxOueFL1y/4DrhArSmJn9CiYAltfYb6nVAkd1abgJgyHh4aOzA43EUO2iqVxvWxf/6Lno1hjTrx+1LhBTGyEhqENHPefSJJpNXcBbiX+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQD+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUmRYMY0=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaClZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4vKCgEAhiRhOcqAAbDvQAGgDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqLygoBAIY/qiUiX/8ymMs+"
  },
  "tag": "offchain_state",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:23.553)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
      "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- node (2019-03-13 11:13:23.559)
```javascript
{
  "action": "get",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": [
    {
      "account": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
      "balance": 40000000000001
    },
    {
      "account": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn",
      "balance": 69999999999999
    }
  ],
  "tag": "balances",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:13:23.561)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 1,
    "from": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
    "to": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn"
  },
  "tag": "new"
}
```

#### responder <--- node (2019-03-13 11:13:23.575)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "tx": "tx_+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQE+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaDwZQ8gtvUEyGfm3kGX5jplOBh1f3MifkAHG85vI5x8EFV4/J4="
  },
  "tag": "update",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:13:23.576)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEAiag8h3yBOotJZnry2hU0Glg1QF5TdF0PGZPafBg8ssodiRouid90y1eqWJ5bSfEw9jmBWxViMPFCupwa9lzsMuJf4lTkBoQad06vsKcGdNdgD7xA+KpuVMsQpGpIGboLmtvpN50ZCtAT4TbhL+EmCAjoBoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK6EBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noBoPBlDyC29QTIZ+beQZfmOmU4GHV/cyJ+QAcbzm8jnHwQkShRcA=="
  }
}
```

#### initiator <--- node (2019-03-13 11:13:23.621)
```javascript
{
  "action": "info",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "event": "update"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:23.624)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "tx": "tx_+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQE+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaDwZQ8gtvUEyGfm3kGX5jplOBh1f3MifkAHG85vI5x8EFV4/J4="
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:23.625)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+N8LAfhCuEATBwMdWomJasoXcPLD34Lk+ltJE4JUQHc+5RrYzbyBnfmhc8nxkmLuN3FyjF5IU04CqJIv7i8AjAwj/0RHxj4GuJf4lTkBoQad06vsKcGdNdgD7xA+KpuVMsQpGpIGboLmtvpN50ZCtAT4TbhL+EmCAjoBoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK6EBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noBoPBlDyC29QTIZ+beQZfmOmU4GHV/cyJ+QAcbzm8jnHwQzW8nKQ=="
  }
}
```

#### initiator <--- node (2019-03-13 11:13:23.654)
```javascript
{
  "action": "update",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "state": "tx_+QEhCwH4hLhAEwcDHVqJiWrKF3Dyw9+C5PpbSROCVEB3PuUa2M28gZ35oXPJ8ZJi7jdxcoxeSFNOAqiSL+4vAIwMI/9ER8Y+BrhAImoPId8gTqLSWZ68toVNBpYNUBeU3RdDxmT2nwYPLLKHYkaLonfdMtXqlieW0nxMPY5gVsVYjDxQrqcGvZc7DLiX+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQE+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaDwZQ8gtvUEyGfm3kGX5jplOBh1f3MifkAHG85vI5x8EDUUMq8="
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:23.670)
```javascript
{
  "action": "update",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "state": "tx_+QEhCwH4hLhAEwcDHVqJiWrKF3Dyw9+C5PpbSROCVEB3PuUa2M28gZ35oXPJ8ZJi7jdxcoxeSFNOAqiSL+4vAIwMI/9ER8Y+BrhAImoPId8gTqLSWZ68toVNBpYNUBeU3RdDxmT2nwYPLLKHYkaLonfdMtXqlieW0nxMPY5gVsVYjDxQrqcGvZc7DLiX+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQE+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaDwZQ8gtvUEyGfm3kGX5jplOBh1f3MifkAHG85vI5x8EDUUMq8="
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:23.691)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
      "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- node (2019-03-13 11:13:23.698)
```javascript
{
  "action": "get",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": [
    {
      "account": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
      "balance": 40000000000000
    },
    {
      "account": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn",
      "balance": 70000000000000
    }
  ],
  "tag": "balances",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:23.700)
```javascript
{
  "action": "get",
  "payload": {
    "a": "a"
  },
  "tag": "offchain_state"
}
```

#### initiator <--- node (2019-03-13 11:13:23.716)
```javascript
{
  "action": "get",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAEwcDHVqJiWrKF3Dyw9+C5PpbSROCVEB3PuUa2M28gZ35oXPJ8ZJi7jdxcoxeSFNOAqiSL+4vAIwMI/9ER8Y+BrhAImoPId8gTqLSWZ68toVNBpYNUBeU3RdDxmT2nwYPLLKHYkaLonfdMtXqlieW0nxMPY5gVsVYjDxQrqcGvZc7DLiX+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQE+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaDwZQ8gtvUEyGfm3kGX5jplOBh1f3MifkAHG85vI5x8EDUUMq8=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaClZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4vKCgEAhiRhOcqAALDvQAGgDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqLygoBAIY/qiUiYAAoH7hl"
  },
  "tag": "offchain_state",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:23.724)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn",
      "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- node (2019-03-13 11:13:23.731)
```javascript
{
  "action": "get",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": [
    {
      "account": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn",
      "balance": 70000000000000
    },
    {
      "account": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
      "balance": 40000000000000
    }
  ],
  "tag": "balances",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:23.733)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 1,
    "from": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn",
    "to": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9"
  },
  "tag": "new"
}
```

#### initiator <--- node (2019-03-13 11:13:23.769)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "tx": "tx_+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQF+E24S/hJggI6AaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAaAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUub5CjU="
  },
  "tag": "update",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:23.771)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEDuMfparwX42n0pZXTxUIuax5pHnEN+ESyV95Pq5/TqNIy9BCPCx2iD0zIPr3SvAfjCzqeDo2E9ffvj0bScet4EuJf4lTkBoQad06vsKcGdNdgD7xA+KpuVMsQpGpIGboLmtvpN50ZCtAX4TbhL+EmCAjoBoQEMHR+jKB9TfmalcAw4HlPfLlTP4fGLC6AeHxDL+MjeeqEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFysBoBVQItrXeXi1NNVLrFNRky7mqhur6CrV3Ihp6ANYAJVS9Y6eyQ=="
  }
}
```

#### responder <--- node (2019-03-13 11:13:23.821)
```javascript
{
  "action": "info",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "event": "update"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:23.822)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "tx": "tx_+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQF+E24S/hJggI6AaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAaAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUub5CjU="
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:13:23.823)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+N8LAfhCuEDU9/I1/3BDSj+2N5zkBhcDDqLiJFGTtJH5r7eeYS1xeNHKvrp8M5v26xYJJXRNaKy71mwGH7N7vuQrS9eOsn8CuJf4lTkBoQad06vsKcGdNdgD7xA+KpuVMsQpGpIGboLmtvpN50ZCtAX4TbhL+EmCAjoBoQEMHR+jKB9TfmalcAw4HlPfLlTP4fGLC6AeHxDL+MjeeqEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFysBoBVQItrXeXi1NNVLrFNRky7mqhur6CrV3Ihp6ANYAJVSO3syTg=="
  }
}
```

#### responder <--- node (2019-03-13 11:13:23.859)
```javascript
{
  "action": "update",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "state": "tx_+QEhCwH4hLhA1PfyNf9wQ0o/tjec5AYXAw6i4iRRk7SR+a+3nmEtcXjRyr66fDOb9usWCSV0TWisu9ZsBh+ze77kK0vXjrJ/ArhA7jH6Wq8F+Np9KWV08VCLmseaR5xDfhEslfeT6uf06jSMvQQjwsdog9MyD690rwH4ws6ng6NhPX3749G0nHreBLiX+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQF+E24S/hJggI6AaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAaAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUoZ6rXw="
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:23.877)
```javascript
{
  "action": "update",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "state": "tx_+QEhCwH4hLhA1PfyNf9wQ0o/tjec5AYXAw6i4iRRk7SR+a+3nmEtcXjRyr66fDOb9usWCSV0TWisu9ZsBh+ze77kK0vXjrJ/ArhA7jH6Wq8F+Np9KWV08VCLmseaR5xDfhEslfeT6uf06jSMvQQjwsdog9MyD690rwH4ws6ng6NhPX3749G0nHreBLiX+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQF+E24S/hJggI6AaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAaAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUoZ6rXw="
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:23.894)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn",
      "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- node (2019-03-13 11:13:23.903)
```javascript
{
  "action": "get",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": [
    {
      "account": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn",
      "balance": 69999999999999
    },
    {
      "account": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
      "balance": 40000000000001
    }
  ],
  "tag": "balances",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:23.904)
```javascript
{
  "action": "get",
  "payload": {
    "a": "a"
  },
  "tag": "offchain_state"
}
```

#### initiator <--- node (2019-03-13 11:13:23.911)
```javascript
{
  "action": "get",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhA1PfyNf9wQ0o/tjec5AYXAw6i4iRRk7SR+a+3nmEtcXjRyr66fDOb9usWCSV0TWisu9ZsBh+ze77kK0vXjrJ/ArhA7jH6Wq8F+Np9KWV08VCLmseaR5xDfhEslfeT6uf06jSMvQQjwsdog9MyD690rwH4ws6ng6NhPX3749G0nHreBLiX+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQF+E24S/hJggI6AaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAaAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUoZ6rXw=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaClZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4vKCgEAhiRhOcqAAbDvQAGgDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqLygoBAIY/qiUiX/8ymMs+"
  },
  "tag": "offchain_state",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:23.922)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
      "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- node (2019-03-13 11:13:23.931)
```javascript
{
  "action": "get",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": [
    {
      "account": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
      "balance": 40000000000001
    },
    {
      "account": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn",
      "balance": 69999999999999
    }
  ],
  "tag": "balances",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:13:23.932)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 1,
    "from": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
    "to": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn"
  },
  "tag": "new"
}
```

#### responder <--- node (2019-03-13 11:13:23.949)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "tx": "tx_+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQG+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaDwZQ8gtvUEyGfm3kGX5jplOBh1f3MifkAHG85vI5x8EGwBjrU="
  },
  "tag": "update",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:13:23.950)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEDyI9gVXD5pam4kgCJ0RMKC//5Q1mDlnSysqTcs9+qR9r8n2Vo/peIGWQqRVxhjCZiiRDSP7YZ0ccR5LuQD3xYGuJf4lTkBoQad06vsKcGdNdgD7xA+KpuVMsQpGpIGboLmtvpN50ZCtAb4TbhL+EmCAjoBoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK6EBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noBoPBlDyC29QTIZ+beQZfmOmU4GHV/cyJ+QAcbzm8jnHwQgs50vA=="
  }
}
```

#### initiator <--- node (2019-03-13 11:13:23.995)
```javascript
{
  "action": "info",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "event": "update"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:23.998)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "tx": "tx_+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQG+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaDwZQ8gtvUEyGfm3kGX5jplOBh1f3MifkAHG85vI5x8EGwBjrU="
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:23.999)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+N8LAfhCuED41Bi95t8eOCP8J22p5wSLKeqPBsHiebQfHrdRF7EVX600BRU1s2Wuz9OrD8L4k1zZE3Sb3vHwgEuyXPoNmB8HuJf4lTkBoQad06vsKcGdNdgD7xA+KpuVMsQpGpIGboLmtvpN50ZCtAb4TbhL+EmCAjoBoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK6EBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noBoPBlDyC29QTIZ+beQZfmOmU4GHV/cyJ+QAcbzm8jnHwQbPtAlA=="
  }
}
```

#### initiator <--- node (2019-03-13 11:13:24.37)
```javascript
{
  "action": "update",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "state": "tx_+QEhCwH4hLhA8iPYFVw+aWpuJIAidETCgv/+UNZg5Z0srKk3LPfqkfa/J9laP6XiBlkKkVcYYwmYokQ0j+2GdHHEeS7kA98WBrhA+NQYvebfHjgj/CdtqecEiynqjwbB4nm0Hx63URexFV+tNAUVNbNlrs/Tqw/C+JNc2RN0m97x8IBLslz6DZgfB7iX+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQG+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaDwZQ8gtvUEyGfm3kGX5jplOBh1f3MifkAHG85vI5x8ENOwKjw="
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:24.54)
```javascript
{
  "action": "update",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "state": "tx_+QEhCwH4hLhA8iPYFVw+aWpuJIAidETCgv/+UNZg5Z0srKk3LPfqkfa/J9laP6XiBlkKkVcYYwmYokQ0j+2GdHHEeS7kA98WBrhA+NQYvebfHjgj/CdtqecEiynqjwbB4nm0Hx63URexFV+tNAUVNbNlrs/Tqw/C+JNc2RN0m97x8IBLslz6DZgfB7iX+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQG+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaDwZQ8gtvUEyGfm3kGX5jplOBh1f3MifkAHG85vI5x8ENOwKjw="
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:24.81)
```javascript
{
  "action": "get",
  "payload": {
    "accounts": [
      "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
      "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn"
    ]
  },
  "tag": "balances"
}
```

#### initiator <--- node (2019-03-13 11:13:24.85)
```javascript
{
  "action": "get",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": [
    {
      "account": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
      "balance": 40000000000000
    },
    {
      "account": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn",
      "balance": 70000000000000
    }
  ],
  "tag": "balances",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:24.86)
```javascript
{
  "action": "get",
  "payload": {
    "a": "a"
  },
  "tag": "offchain_state"
}
```

#### initiator <--- node (2019-03-13 11:13:24.94)
```javascript
{
  "action": "get",
  "channel_id": "ch_2CWUYQtUhajgWSePn4eSjhanKPbh688S7xUdcq3cLW2RjHNb5C",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhA8iPYFVw+aWpuJIAidETCgv/+UNZg5Z0srKk3LPfqkfa/J9laP6XiBlkKkVcYYwmYokQ0j+2GdHHEeS7kA98WBrhA+NQYvebfHjgj/CdtqecEiynqjwbB4nm0Hx63URexFV+tNAUVNbNlrs/Tqw/C+JNc2RN0m97x8IBLslz6DZgfB7iX+JU5AaEGndOr7CnBnTXYA+8QPiqblTLEKRqSBm6C5rb6TedGQrQG+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaDwZQ8gtvUEyGfm3kGX5jplOBh1f3MifkAHG85vI5x8ENOwKjw=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaClZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4vKCgEAhiRhOcqAALDvQAGgDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqLygoBAIY/qiUiYAAoH7hl"
  },
  "tag": "offchain_state",
  "version": 1
}
```
