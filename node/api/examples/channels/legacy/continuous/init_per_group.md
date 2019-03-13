
#### initiator opens a WebSocket connection (2019-03-13 11:13:43.996)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9&role=initiator
```

#### responder opens a WebSocket connection (2019-03-13 11:13:44.20)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9&role=responder
```

#### responder <--- node (2019-03-13 11:13:44.992)
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

#### initiator <--- node (2019-03-13 11:13:44.995)
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

#### initiator <--- node (2019-03-13 11:13:45.19)
```javascript
{
  "action": "sign",
  "channel_id": null,
  "payload": {
    "tx": "tx_+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgaHrC6q"
  },
  "tag": "initiator_sign",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:45.113)
```javascript
{
  "action": "initiator_sign",
  "payload": {
    "tx": "tx_+MsLAfhCuECgj5+9d+uEniSNLP6WCKPgJL0A28eawOu9uQl44MYDo8cI3Geiuz9Wi1RhRl4u4zYXyZ1IEFsUVMFKMr/JlCMGuIP4gTIBoQEMHR+jKB9TfmalcAw4HlPfLlTP4fGLC6AeHxDL+MjeeoY/qiUiYAChAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrhiRhOcqAAAIKAIYSMJzlQADAoBVQItrXeXi1NNVLrFNRky7mqhur6CrV3Ihp6ANYAJVSBpieiwo="
  }
}
```

#### responder <--- node (2019-03-13 11:13:45.132)
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

#### responder <--- node (2019-03-13 11:13:45.133)
```javascript
{
  "action": "sign",
  "channel_id": null,
  "payload": {
    "tx": "tx_+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgaHrC6q"
  },
  "tag": "responder_sign",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:13:45.134)
```javascript
{
  "action": "responder_sign",
  "payload": {
    "tx": "tx_+MsLAfhCuECZlttV/j81+aFVucsRTPE/XNv+b+vWYewHNBEgHkq7Zsaspvujoy8ByNfo8pKt23iGxyIvofTEWcNGnlXdwksBuIP4gTIBoQEMHR+jKB9TfmalcAw4HlPfLlTP4fGLC6AeHxDL+MjeeoY/qiUiYAChAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrhiRhOcqAAAIKAIYSMJzlQADAoBVQItrXeXi1NNVLrFNRky7mqhur6CrV3Ihp6ANYAJVSBqmGIU4="
  }
}
```

#### responder <--- node (2019-03-13 11:13:45.148)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": null,
  "payload": {
    "tx": "tx_+QENCwH4hLhAmZbbVf4/NfmhVbnLEUzxP1zb/m/r1mHsBzQRIB5Ku2bGrKb7o6MvAcjX6PKSrdt4hsciL6H0xFnDRp5V3cJLAbhAoI+fvXfrhJ4kjSz+lgij4CS9ANvHmsDrvbkJeODGA6PHCNxnors/VotUYUZeLuM2F8mdSBBbFFTBSjK/yZQjBriD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUga6kKf1"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:45.150)
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

#### initiator <--- node (2019-03-13 11:13:45.153)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": null,
  "payload": {
    "tx": "tx_+QENCwH4hLhAmZbbVf4/NfmhVbnLEUzxP1zb/m/r1mHsBzQRIB5Ku2bGrKb7o6MvAcjX6PKSrdt4hsciL6H0xFnDRp5V3cJLAbhAoI+fvXfrhJ4kjSz+lgij4CS9ANvHmsDrvbkJeODGA6PHCNxnors/VotUYUZeLuM2F8mdSBBbFFTBSjK/yZQjBriD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUga6kKf1"
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:46.954)
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

#### initiator <--- node (2019-03-13 11:13:46.964)
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

#### responder <--- node (2019-03-13 11:13:48.476)
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

#### initiator <--- node (2019-03-13 11:13:48.480)
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

#### initiator <--- node (2019-03-13 11:13:48.480)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "funding_locked"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:48.486)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "funding_locked"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:48.501)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "open"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:48.503)
```javascript
{
  "action": "update",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "state": "tx_+QENCwH4hLhAmZbbVf4/NfmhVbnLEUzxP1zb/m/r1mHsBzQRIB5Ku2bGrKb7o6MvAcjX6PKSrdt4hsciL6H0xFnDRp5V3cJLAbhAoI+fvXfrhJ4kjSz+lgij4CS9ANvHmsDrvbkJeODGA6PHCNxnors/VotUYUZeLuM2F8mdSBBbFFTBSjK/yZQjBriD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUga6kKf1"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:48.507)
```javascript
{
  "action": "info",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "event": "open"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:48.511)
```javascript
{
  "action": "update",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "state": "tx_+QENCwH4hLhAmZbbVf4/NfmhVbnLEUzxP1zb/m/r1mHsBzQRIB5Ku2bGrKb7o6MvAcjX6PKSrdt4hsciL6H0xFnDRp5V3cJLAbhAoI+fvXfrhJ4kjSz+lgij4CS9ANvHmsDrvbkJeODGA6PHCNxnors/VotUYUZeLuM2F8mdSBBbFFTBSjK/yZQjBriD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUga6kKf1"
  },
  "version": 1
}
```

#### responder: (2019-03-13 11:13:48.972)
> Funding has been confirmed locally on-chain

#### initiator: (2019-03-13 11:13:48.972)
> Funding has been confirmed locally on-chain

#### responder: (2019-03-13 11:13:48.972)
> Funding has been confirmed on-chain by other party

#### initiator: (2019-03-13 11:13:48.972)
> Funding has been confirmed on-chain by other party

#### responder: (2019-03-13 11:13:48.972)
> Channel is `open` and ready to use

#### initiator: (2019-03-13 11:13:48.972)
> Channel is `open` and ready to use
