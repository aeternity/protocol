
#### initiator opens a WebSocket connection (2019-03-13 11:13:39.136)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9&role=initiator
```

#### responder opens a WebSocket connection (2019-03-13 11:13:39.179)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9&role=responder
```

#### responder <--- node (2019-03-13 11:13:40.139)
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

#### initiator <--- node (2019-03-13 11:13:40.143)
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

#### initiator <--- node (2019-03-13 11:13:40.155)
```javascript
{
  "action": "sign",
  "channel_id": null,
  "payload": {
    "tx": "tx_+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgVpx9tT"
  },
  "tag": "initiator_sign",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:40.295)
```javascript
{
  "action": "initiator_sign",
  "payload": {
    "tx": "tx_+MsLAfhCuEDCIbU/0zAuREH0mZPYCeaMZ0EGEPKo42YhDfWatYJQWYbAhYlJz6diETTj14/WC/7g3MXfi/ivDDjwqu45gKUKuIP4gTIBoQEMHR+jKB9TfmalcAw4HlPfLlTP4fGLC6AeHxDL+MjeeoY/qiUiYAChAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrhiRhOcqAAAIKAIYSMJzlQADAoBVQItrXeXi1NNVLrFNRky7mqhur6CrV3Ihp6ANYAJVSBQKv/d8="
  }
}
```

#### responder <--- node (2019-03-13 11:13:40.331)
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

#### responder <--- node (2019-03-13 11:13:40.333)
```javascript
{
  "action": "sign",
  "channel_id": null,
  "payload": {
    "tx": "tx_+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgVpx9tT"
  },
  "tag": "responder_sign",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:13:40.334)
```javascript
{
  "action": "responder_sign",
  "payload": {
    "tx": "tx_+MsLAfhCuEAV7Ph6AMCbNSFWpyqilXVxAb9emkK8nCQixoshktAaKTIuqWBd9UvNAhVqCvBrU+yqpk5GBBAtWah1W6W/d78AuIP4gTIBoQEMHR+jKB9TfmalcAw4HlPfLlTP4fGLC6AeHxDL+MjeeoY/qiUiYAChAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrhiRhOcqAAAIKAIYSMJzlQADAoBVQItrXeXi1NNVLrFNRky7mqhur6CrV3Ihp6ANYAJVSBZTnopg="
  }
}
```

#### responder <--- node (2019-03-13 11:13:40.362)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": null,
  "payload": {
    "tx": "tx_+QENCwH4hLhAFez4egDAmzUhVqcqopV1cQG/XppCvJwkIsaLIZLQGikyLqlgXfVLzQIVagrwa1PsqqZORgQQLVmodVulv3e/ALhAwiG1P9MwLkRB9JmT2AnmjGdBBhDyqONmIQ31mrWCUFmGwIWJSc+nYhE049eP1gv+4NzF34v4rww48KruOYClCriD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgUqpb61"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:40.379)
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

#### initiator <--- node (2019-03-13 11:13:40.383)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": null,
  "payload": {
    "tx": "tx_+QENCwH4hLhAFez4egDAmzUhVqcqopV1cQG/XppCvJwkIsaLIZLQGikyLqlgXfVLzQIVagrwa1PsqqZORgQQLVmodVulv3e/ALhAwiG1P9MwLkRB9JmT2AnmjGdBBhDyqONmIQ31mrWCUFmGwIWJSc+nYhE049eP1gv+4NzF34v4rww48KruOYClCriD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgUqpb61"
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:41.391)
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

#### initiator <--- node (2019-03-13 11:13:41.403)
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

#### responder <--- node (2019-03-13 11:13:42.156)
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

#### initiator <--- node (2019-03-13 11:13:42.165)
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

#### initiator <--- node (2019-03-13 11:13:42.167)
```javascript
{
  "action": "info",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "event": "funding_locked"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:42.168)
```javascript
{
  "action": "info",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "event": "funding_locked"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:42.183)
```javascript
{
  "action": "info",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "event": "open"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:42.184)
```javascript
{
  "action": "update",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "state": "tx_+QENCwH4hLhAFez4egDAmzUhVqcqopV1cQG/XppCvJwkIsaLIZLQGikyLqlgXfVLzQIVagrwa1PsqqZORgQQLVmodVulv3e/ALhAwiG1P9MwLkRB9JmT2AnmjGdBBhDyqONmIQ31mrWCUFmGwIWJSc+nYhE049eP1gv+4NzF34v4rww48KruOYClCriD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgUqpb61"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:42.187)
```javascript
{
  "action": "info",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "event": "open"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:42.188)
```javascript
{
  "action": "update",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "state": "tx_+QENCwH4hLhAFez4egDAmzUhVqcqopV1cQG/XppCvJwkIsaLIZLQGikyLqlgXfVLzQIVagrwa1PsqqZORgQQLVmodVulv3e/ALhAwiG1P9MwLkRB9JmT2AnmjGdBBhDyqONmIQ31mrWCUFmGwIWJSc+nYhE049eP1gv+4NzF34v4rww48KruOYClCriD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgUqpb61"
  },
  "version": 1
}
```

#### initiator: (2019-03-13 11:13:42.614)
> Funding has been confirmed locally on-chain

#### responder: (2019-03-13 11:13:42.614)
> Funding has been confirmed locally on-chain

#### initiator: (2019-03-13 11:13:42.614)
> Funding has been confirmed on-chain by other party

#### responder: (2019-03-13 11:13:42.614)
> Funding has been confirmed on-chain by other party

#### initiator: (2019-03-13 11:13:42.614)
> Channel is `open` and ready to use

#### responder: (2019-03-13 11:13:42.615)
> Channel is `open` and ready to use

#### initiator ---> node (2019-03-13 11:13:42.615)
```javascript
{
  "action": "leave"
}
```

#### responder <--- node (2019-03-13 11:13:42.626)
```javascript
{
  "action": "leave",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "state": "tx_+QENCwH4hLhAFez4egDAmzUhVqcqopV1cQG/XppCvJwkIsaLIZLQGikyLqlgXfVLzQIVagrwa1PsqqZORgQQLVmodVulv3e/ALhAwiG1P9MwLkRB9JmT2AnmjGdBBhDyqONmIQ31mrWCUFmGwIWJSc+nYhE049eP1gv+4NzF34v4rww48KruOYClCriD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgUqpb61"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:42.628)
```javascript
{
  "action": "info",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "event": "died"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:42.635)
```javascript
{
  "action": "leave",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "state": "tx_+QENCwH4hLhAFez4egDAmzUhVqcqopV1cQG/XppCvJwkIsaLIZLQGikyLqlgXfVLzQIVagrwa1PsqqZORgQQLVmodVulv3e/ALhAwiG1P9MwLkRB9JmT2AnmjGdBBhDyqONmIQ31mrWCUFmGwIWJSc+nYhE049eP1gv+4NzF34v4rww48KruOYClCriD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgUqpb61"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:42.636)
```javascript
{
  "action": "info",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "event": "died"
  },
  "version": 1
}
```

#### responder opens a WebSocket connection (2019-03-13 11:13:42.691)
```
ws://localhost:3014/channel?channel_reserve=2&existing_channel_id=ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83&initiator_amount=70000000000000&initiator_id=ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn&lock_period=10&offchain_tx=tx_%2BQENCwH4hLhAFez4egDAmzUhVqcqopV1cQG%2FXppCvJwkIsaLIZLQGikyLqlgXfVLzQIVagrwa1PsqqZORgQQLVmodVulv3e%2FALhAwiG1P9MwLkRB9JmT2AnmjGdBBhDyqONmIQ31mrWCUFmGwIWJSc%2BnYhE049eP1gv%2B4NzF34v4rww48KruOYClCriD%2BIEyAaEBDB0foygfU35mpXAMOB5T3y5Uz%2BHxiwugHh8Qy%2FjI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8%2FEZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq%2Bgq1dyIaegDWACVUgUqpb61&port=12341&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9&role=responder
```

#### initiator opens a WebSocket connection (2019-03-13 11:13:42.713)
```
ws://localhost:3014/channel?channel_reserve=2&existing_channel_id=ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83&host=localhost&initiator_amount=70000000000000&initiator_id=ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn&lock_period=10&offchain_tx=tx_%2BQENCwH4hLhAFez4egDAmzUhVqcqopV1cQG%2FXppCvJwkIsaLIZLQGikyLqlgXfVLzQIVagrwa1PsqqZORgQQLVmodVulv3e%2FALhAwiG1P9MwLkRB9JmT2AnmjGdBBhDyqONmIQ31mrWCUFmGwIWJSc%2BnYhE049eP1gv%2B4NzF34v4rww48KruOYClCriD%2BIEyAaEBDB0foygfU35mpXAMOB5T3y5Uz%2BHxiwugHh8Qy%2FjI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8%2FEZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq%2Bgq1dyIaegDWACVUgUqpb61&port=12341&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9&role=initiator
```

#### responder <--- node (2019-03-13 11:13:42.722)
```javascript
{
  "action": "info",
  "channel_id": null,
  "payload": {
    "event": "channel_reestablished"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:42.725)
```javascript
{
  "action": "info",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "event": "open"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:42.727)
```javascript
{
  "action": "update",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "state": "tx_+QENCwH4hLhAFez4egDAmzUhVqcqopV1cQG/XppCvJwkIsaLIZLQGikyLqlgXfVLzQIVagrwa1PsqqZORgQQLVmodVulv3e/ALhAwiG1P9MwLkRB9JmT2AnmjGdBBhDyqONmIQ31mrWCUFmGwIWJSc+nYhE049eP1gv+4NzF34v4rww48KruOYClCriD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgUqpb61"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:42.730)
```javascript
{
  "action": "info",
  "channel_id": null,
  "payload": {
    "event": "channel_reestablished"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:42.735)
```javascript
{
  "action": "info",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "event": "open"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:42.736)
```javascript
{
  "action": "update",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "state": "tx_+QENCwH4hLhAFez4egDAmzUhVqcqopV1cQG/XppCvJwkIsaLIZLQGikyLqlgXfVLzQIVagrwa1PsqqZORgQQLVmodVulv3e/ALhAwiG1P9MwLkRB9JmT2AnmjGdBBhDyqONmIQ31mrWCUFmGwIWJSc+nYhE049eP1gv+4NzF34v4rww48KruOYClCriD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgUqpb61"
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:42.739)
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

#### initiator <--- node (2019-03-13 11:13:42.744)
```javascript
{
  "action": "get",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
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

#### initiator ---> node (2019-03-13 11:13:42.745)
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

#### initiator <--- node (2019-03-13 11:13:42.761)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "tx": "tx_+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwC+E24S/hJggI6AaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAaA7pv4mg8xv+FCuz/dffsQJfmMd+RvIpdZVGhCPqJtqsv+H9g0="
  },
  "tag": "update",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:42.762)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuECqRrQg4gs9PgZChZK/1ZSWyG8G7C3Y1bqJHxBPfnBWCyO53WA/2qx0t5fj8Ztu/5S8Xwk0U5K0MvxwoJUG+WsGuJf4lTkBoQa0YDC4PfkyUYI5JPn61MD7d7ZNVoHCaR1QPE4N1VjAjAL4TbhL+EmCAjoBoQEMHR+jKB9TfmalcAw4HlPfLlTP4fGLC6AeHxDL+MjeeqEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFysBoDum/iaDzG/4UK7P919+xAl+Yx35G8il1lUaEI+om2qy3aHw2w=="
  }
}
```

#### responder <--- node (2019-03-13 11:13:42.815)
```javascript
{
  "action": "info",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "event": "update"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:42.816)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "tx": "tx_+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwC+E24S/hJggI6AaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAaA7pv4mg8xv+FCuz/dffsQJfmMd+RvIpdZVGhCPqJtqsv+H9g0="
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:13:42.817)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+N8LAfhCuEAWhhmUHYpNZeXZS2qzL824scUwfU17kcyxesYRGXKJUe+7BxwEL9gCWvObJ9KpHGtPfDqFTDKs1/6pZ25s0FIDuJf4lTkBoQa0YDC4PfkyUYI5JPn61MD7d7ZNVoHCaR1QPE4N1VjAjAL4TbhL+EmCAjoBoQEMHR+jKB9TfmalcAw4HlPfLlTP4fGLC6AeHxDL+MjeeqEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFysBoDum/iaDzG/4UK7P919+xAl+Yx35G8il1lUaEI+om2qysoWVVQ=="
  }
}
```

#### responder <--- node (2019-03-13 11:13:42.884)
```javascript
{
  "action": "update",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "state": "tx_+QEhCwH4hLhAFoYZlB2KTWXl2Utqsy/NuLHFMH1Ne5HMsXrGERlyiVHvuwccBC/YAlrzmyfSqRxrT3w6hUwyrNf+qWdubNBSA7hAqka0IOILPT4GQoWSv9WUlshvBuwt2NW6iR8QT35wVgsjud1gP9qsdLeX4/Gbbv+UvF8JNFOStDL8cKCVBvlrBriX+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwC+E24S/hJggI6AaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAaA7pv4mg8xv+FCuz/dffsQJfmMd+RvIpdZVGhCPqJtqsqszMUU="
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:42.906)
```javascript
{
  "action": "update",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "state": "tx_+QEhCwH4hLhAFoYZlB2KTWXl2Utqsy/NuLHFMH1Ne5HMsXrGERlyiVHvuwccBC/YAlrzmyfSqRxrT3w6hUwyrNf+qWdubNBSA7hAqka0IOILPT4GQoWSv9WUlshvBuwt2NW6iR8QT35wVgsjud1gP9qsdLeX4/Gbbv+UvF8JNFOStDL8cKCVBvlrBriX+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwC+E24S/hJggI6AaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAaA7pv4mg8xv+FCuz/dffsQJfmMd+RvIpdZVGhCPqJtqsqszMUU="
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:42.920)
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

#### initiator <--- node (2019-03-13 11:13:42.925)
```javascript
{
  "action": "get",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
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

#### initiator ---> node (2019-03-13 11:13:42.926)
```javascript
{
  "action": "get",
  "payload": {
    "a": "a"
  },
  "tag": "offchain_state"
}
```

#### initiator <--- node (2019-03-13 11:13:42.932)
```javascript
{
  "action": "get",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAFoYZlB2KTWXl2Utqsy/NuLHFMH1Ne5HMsXrGERlyiVHvuwccBC/YAlrzmyfSqRxrT3w6hUwyrNf+qWdubNBSA7hAqka0IOILPT4GQoWSv9WUlshvBuwt2NW6iR8QT35wVgsjud1gP9qsdLeX4/Gbbv+UvF8JNFOStDL8cKCVBvlrBriX+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwC+E24S/hJggI6AaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAaA7pv4mg8xv+FCuz/dffsQJfmMd+RvIpdZVGhCPqJtqsqszMUU=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaClZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4vKCgEAhiRhOcqAArDvQAGgDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqLygoBAIY/qiUiX/69jYLo"
  },
  "tag": "offchain_state",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:42.940)
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

#### initiator <--- node (2019-03-13 11:13:42.950)
```javascript
{
  "action": "get",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
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

#### responder ---> node (2019-03-13 11:13:42.951)
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

#### responder <--- node (2019-03-13 11:13:42.964)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "tx": "tx_+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwD+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUuN+hUo="
  },
  "tag": "update",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:13:42.965)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEC/ea6KaynX6WHVRq7nDHYkgK37LrKiuTcxBdtAEWQoKJFS50ggoXgmXvscnlth8gPGubyGQOuJXa1X2BxW8iQBuJf4lTkBoQa0YDC4PfkyUYI5JPn61MD7d7ZNVoHCaR1QPE4N1VjAjAP4TbhL+EmCAjoBoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK6EBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noBoBVQItrXeXi1NNVLrFNRky7mqhur6CrV3Ihp6ANYAJVSD6BB7Q=="
  }
}
```

#### initiator <--- node (2019-03-13 11:13:43.4)
```javascript
{
  "action": "info",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "event": "update"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:43.5)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "tx": "tx_+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwD+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUuN+hUo="
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:43.7)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+N8LAfhCuEA0DcZ1SZBk/FM0EBrnMmsAR3kAsYX83k1NwyQwa3tzjJ8oYc/xncJLEVqV2i4keT+iHnsa6IU6upTeGNwq16YKuJf4lTkBoQa0YDC4PfkyUYI5JPn61MD7d7ZNVoHCaR1QPE4N1VjAjAP4TbhL+EmCAjoBoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK6EBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noBoBVQItrXeXi1NNVLrFNRky7mqhur6CrV3Ihp6ANYAJVSy8RuxQ=="
  }
}
```

#### initiator <--- node (2019-03-13 11:13:43.35)
```javascript
{
  "action": "update",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "state": "tx_+QEhCwH4hLhANA3GdUmQZPxTNBAa5zJrAEd5ALGF/N5NTcMkMGt7c4yfKGHP8Z3CSxFaldouJHk/oh57GuiFOrqU3hjcKtemCrhAv3muimsp1+lh1Uau5wx2JICt+y6york3MQXbQBFkKCiRUudIIKF4Jl77HJ5bYfIDxrm8hkDriV2tV9gcVvIkAbiX+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwD+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUleYZpU="
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:43.70)
```javascript
{
  "action": "update",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "state": "tx_+QEhCwH4hLhANA3GdUmQZPxTNBAa5zJrAEd5ALGF/N5NTcMkMGt7c4yfKGHP8Z3CSxFaldouJHk/oh57GuiFOrqU3hjcKtemCrhAv3muimsp1+lh1Uau5wx2JICt+y6york3MQXbQBFkKCiRUudIIKF4Jl77HJ5bYfIDxrm8hkDriV2tV9gcVvIkAbiX+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwD+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUleYZpU="
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:43.89)
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

#### initiator <--- node (2019-03-13 11:13:43.96)
```javascript
{
  "action": "get",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
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

#### initiator ---> node (2019-03-13 11:13:43.98)
```javascript
{
  "action": "get",
  "payload": {
    "a": "a"
  },
  "tag": "offchain_state"
}
```

#### initiator <--- node (2019-03-13 11:13:43.120)
```javascript
{
  "action": "get",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhANA3GdUmQZPxTNBAa5zJrAEd5ALGF/N5NTcMkMGt7c4yfKGHP8Z3CSxFaldouJHk/oh57GuiFOrqU3hjcKtemCrhAv3muimsp1+lh1Uau5wx2JICt+y6york3MQXbQBFkKCiRUudIIKF4Jl77HJ5bYfIDxrm8hkDriV2tV9gcVvIkAbiX+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwD+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUleYZpU=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaClZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4vKCgEAhiRhOcqAAbDvQAGgDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqLygoBAIY/qiUiX/8ymMs+"
  },
  "tag": "offchain_state",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:43.128)
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

#### initiator <--- node (2019-03-13 11:13:43.133)
```javascript
{
  "action": "get",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
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

#### responder ---> node (2019-03-13 11:13:43.134)
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

#### responder <--- node (2019-03-13 11:13:43.157)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "tx": "tx_+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwE+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaDwZQ8gtvUEyGfm3kGX5jplOBh1f3MifkAHG85vI5x8ECp2WXY="
  },
  "tag": "update",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:13:43.158)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEDNnqbtdkcEiyXxbbdBfKwA0AR2ZNMyuTu0Q6fswW0B2oR0YG8kejuNScu8ZDZqDu1EFDxmRI3hCL3ZbC2zMNcBuJf4lTkBoQa0YDC4PfkyUYI5JPn61MD7d7ZNVoHCaR1QPE4N1VjAjAT4TbhL+EmCAjoBoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK6EBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noBoPBlDyC29QTIZ+beQZfmOmU4GHV/cyJ+QAcbzm8jnHwQSlUKKA=="
  }
}
```

#### initiator <--- node (2019-03-13 11:13:43.200)
```javascript
{
  "action": "info",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "event": "update"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:43.201)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "tx": "tx_+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwE+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaDwZQ8gtvUEyGfm3kGX5jplOBh1f3MifkAHG85vI5x8ECp2WXY="
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:43.202)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+N8LAfhCuECvgodRKJcfThy6zRKDjjHFW1fPPlIIZpnZ2/NdtCVrK9ntkhomQi03jmHA+HpsU88Ks3BtWOLmcsENq85zCAAKuJf4lTkBoQa0YDC4PfkyUYI5JPn61MD7d7ZNVoHCaR1QPE4N1VjAjAT4TbhL+EmCAjoBoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK6EBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noBoPBlDyC29QTIZ+beQZfmOmU4GHV/cyJ+QAcbzm8jnHwQ6M0JhA=="
  }
}
```

#### initiator <--- node (2019-03-13 11:13:43.267)
```javascript
{
  "action": "update",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "state": "tx_+QEhCwH4hLhAr4KHUSiXH04cus0Sg44xxVtXzz5SCGaZ2dvzXbQlayvZ7ZIaJkItN45hwPh6bFPPCrNwbVji5nLBDavOcwgACrhAzZ6m7XZHBIsl8W23QXysANAEdmTTMrk7tEOn7MFtAdqEdGBvJHo7jUnLvGQ2ag7tRBQ8ZkSN4Qi92WwtszDXAbiX+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwE+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaDwZQ8gtvUEyGfm3kGX5jplOBh1f3MifkAHG85vI5x8EEbGLNg="
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:43.286)
```javascript
{
  "action": "update",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "state": "tx_+QEhCwH4hLhAr4KHUSiXH04cus0Sg44xxVtXzz5SCGaZ2dvzXbQlayvZ7ZIaJkItN45hwPh6bFPPCrNwbVji5nLBDavOcwgACrhAzZ6m7XZHBIsl8W23QXysANAEdmTTMrk7tEOn7MFtAdqEdGBvJHo7jUnLvGQ2ag7tRBQ8ZkSN4Qi92WwtszDXAbiX+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwE+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaDwZQ8gtvUEyGfm3kGX5jplOBh1f3MifkAHG85vI5x8EEbGLNg="
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:43.307)
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

#### initiator <--- node (2019-03-13 11:13:43.315)
```javascript
{
  "action": "get",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
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

#### initiator ---> node (2019-03-13 11:13:43.316)
```javascript
{
  "action": "get",
  "payload": {
    "a": "a"
  },
  "tag": "offchain_state"
}
```

#### initiator <--- node (2019-03-13 11:13:43.321)
```javascript
{
  "action": "get",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAr4KHUSiXH04cus0Sg44xxVtXzz5SCGaZ2dvzXbQlayvZ7ZIaJkItN45hwPh6bFPPCrNwbVji5nLBDavOcwgACrhAzZ6m7XZHBIsl8W23QXysANAEdmTTMrk7tEOn7MFtAdqEdGBvJHo7jUnLvGQ2ag7tRBQ8ZkSN4Qi92WwtszDXAbiX+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwE+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaDwZQ8gtvUEyGfm3kGX5jplOBh1f3MifkAHG85vI5x8EEbGLNg=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaClZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4vKCgEAhiRhOcqAALDvQAGgDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqLygoBAIY/qiUiYAAoH7hl"
  },
  "tag": "offchain_state",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:43.332)
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

#### initiator <--- node (2019-03-13 11:13:43.336)
```javascript
{
  "action": "get",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
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

#### initiator ---> node (2019-03-13 11:13:43.338)
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

#### initiator <--- node (2019-03-13 11:13:43.357)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "tx": "tx_+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwF+E24S/hJggI6AaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAaAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUos/UH0="
  },
  "tag": "update",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:43.358)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEAqEEV8uohQ/jvNMcZUmAutS3+VhS7aotWYPogJxLtUPvb8+v4+hiCCdIJB5ha9lnfF4XcwZQZ4hMrS5U0U/WAIuJf4lTkBoQa0YDC4PfkyUYI5JPn61MD7d7ZNVoHCaR1QPE4N1VjAjAX4TbhL+EmCAjoBoQEMHR+jKB9TfmalcAw4HlPfLlTP4fGLC6AeHxDL+MjeeqEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFysBoBVQItrXeXi1NNVLrFNRky7mqhur6CrV3Ihp6ANYAJVSRbeCZA=="
  }
}
```

#### responder <--- node (2019-03-13 11:13:43.405)
```javascript
{
  "action": "info",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "event": "update"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:43.406)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "tx": "tx_+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwF+E24S/hJggI6AaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAaAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUos/UH0="
  },
  "tag": "update_ack",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:13:43.424)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+N8LAfhCuEAX9cIr4yztrG2/BPzPVn40TbR8Lx2rckmUYD/R0SNa3uH35xVDeB+qmfqMNbC16K/n/joTIeUp5/rvWEb/tMAEuJf4lTkBoQa0YDC4PfkyUYI5JPn61MD7d7ZNVoHCaR1QPE4N1VjAjAX4TbhL+EmCAjoBoQEMHR+jKB9TfmalcAw4HlPfLlTP4fGLC6AeHxDL+MjeeqEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFysBoBVQItrXeXi1NNVLrFNRky7mqhur6CrV3Ihp6ANYAJVStqV2dQ=="
  }
}
```

#### responder <--- node (2019-03-13 11:13:43.477)
```javascript
{
  "action": "update",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "state": "tx_+QEhCwH4hLhAF/XCK+Ms7axtvwT8z1Z+NE20fC8dq3JJlGA/0dEjWt7h9+cVQ3gfqpn6jDWwteiv5/46EyHlKef671hG/7TABLhAKhBFfLqIUP47zTHGVJgLrUt/lYUu2qLVmD6ICcS7VD72/Pr+PoYggnSCQeYWvZZ3xeF3MGUGeITK0uVNFP1gCLiX+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwF+E24S/hJggI6AaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAaAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUhwInog="
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:43.503)
```javascript
{
  "action": "update",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "state": "tx_+QEhCwH4hLhAF/XCK+Ms7axtvwT8z1Z+NE20fC8dq3JJlGA/0dEjWt7h9+cVQ3gfqpn6jDWwteiv5/46EyHlKef671hG/7TABLhAKhBFfLqIUP47zTHGVJgLrUt/lYUu2qLVmD6ICcS7VD72/Pr+PoYggnSCQeYWvZZ3xeF3MGUGeITK0uVNFP1gCLiX+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwF+E24S/hJggI6AaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAaAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUhwInog="
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:43.516)
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

#### initiator <--- node (2019-03-13 11:13:43.520)
```javascript
{
  "action": "get",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
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

#### initiator ---> node (2019-03-13 11:13:43.521)
```javascript
{
  "action": "get",
  "payload": {
    "a": "a"
  },
  "tag": "offchain_state"
}
```

#### initiator <--- node (2019-03-13 11:13:43.528)
```javascript
{
  "action": "get",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAF/XCK+Ms7axtvwT8z1Z+NE20fC8dq3JJlGA/0dEjWt7h9+cVQ3gfqpn6jDWwteiv5/46EyHlKef671hG/7TABLhAKhBFfLqIUP47zTHGVJgLrUt/lYUu2qLVmD6ICcS7VD72/Pr+PoYggnSCQeYWvZZ3xeF3MGUGeITK0uVNFP1gCLiX+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwF+E24S/hJggI6AaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAaAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUhwInog=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaClZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4vKCgEAhiRhOcqAAbDvQAGgDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqLygoBAIY/qiUiX/8ymMs+"
  },
  "tag": "offchain_state",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:43.536)
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

#### initiator <--- node (2019-03-13 11:13:43.548)
```javascript
{
  "action": "get",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
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

#### responder ---> node (2019-03-13 11:13:43.549)
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

#### responder <--- node (2019-03-13 11:13:43.562)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "tx": "tx_+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwG+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaDwZQ8gtvUEyGfm3kGX5jplOBh1f3MifkAHG85vI5x8ED+xDoQ="
  },
  "tag": "update",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:13:43.564)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEAC8Cb+8bVLTu18lPRiReJy7H/yEGg+DmcfiPxKlER6dqKd01GV+aEElXnECAtoMoo6PFGrk6X1LQClJxX8yVoDuJf4lTkBoQa0YDC4PfkyUYI5JPn61MD7d7ZNVoHCaR1QPE4N1VjAjAb4TbhL+EmCAjoBoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK6EBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noBoPBlDyC29QTIZ+beQZfmOmU4GHV/cyJ+QAcbzm8jnHwQwkZ4uA=="
  }
}
```

#### initiator <--- node (2019-03-13 11:13:43.601)
```javascript
{
  "action": "info",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "event": "update"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:43.602)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "tx": "tx_+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwG+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaDwZQ8gtvUEyGfm3kGX5jplOBh1f3MifkAHG85vI5x8ED+xDoQ="
  },
  "tag": "update_ack",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:43.603)
```javascript
{
  "action": "update_ack",
  "payload": {
    "tx": "tx_+N8LAfhCuEAMvLYOJjSVdLEpWcchLuRy0gEByJus+DG3CJTHxkL6Zm83ove3E56qyoCdxgFcXN5O4JL/+aUpS3w0u8ejKEoDuJf4lTkBoQa0YDC4PfkyUYI5JPn61MD7d7ZNVoHCaR1QPE4N1VjAjAb4TbhL+EmCAjoBoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK6EBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noBoPBlDyC29QTIZ+beQZfmOmU4GHV/cyJ+QAcbzm8jnHwQwr+l2w=="
  }
}
```

#### initiator <--- node (2019-03-13 11:13:43.631)
```javascript
{
  "action": "update",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "state": "tx_+QEhCwH4hLhAAvAm/vG1S07tfJT0YkXicux/8hBoPg5nH4j8SpREenaindNRlfmhBJV5xAgLaDKKOjxRq5Ol9S0ApScV/MlaA7hADLy2DiY0lXSxKVnHIS7kctIBAcibrPgxtwiUx8ZC+mZvN6L3txOeqsqAncYBXFzeTuCS//mlKUt8NLvHoyhKA7iX+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwG+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaDwZQ8gtvUEyGfm3kGX5jplOBh1f3MifkAHG85vI5x8EF6JI2Y="
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:43.647)
```javascript
{
  "action": "update",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "state": "tx_+QEhCwH4hLhAAvAm/vG1S07tfJT0YkXicux/8hBoPg5nH4j8SpREenaindNRlfmhBJV5xAgLaDKKOjxRq5Ol9S0ApScV/MlaA7hADLy2DiY0lXSxKVnHIS7kctIBAcibrPgxtwiUx8ZC+mZvN6L3txOeqsqAncYBXFzeTuCS//mlKUt8NLvHoyhKA7iX+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwG+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaDwZQ8gtvUEyGfm3kGX5jplOBh1f3MifkAHG85vI5x8EF6JI2Y="
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:43.668)
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

#### initiator <--- node (2019-03-13 11:13:43.675)
```javascript
{
  "action": "get",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
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

#### initiator ---> node (2019-03-13 11:13:43.676)
```javascript
{
  "action": "get",
  "payload": {
    "a": "a"
  },
  "tag": "offchain_state"
}
```

#### initiator <--- node (2019-03-13 11:13:43.682)
```javascript
{
  "action": "get",
  "channel_id": "ch_2NSTTuoeVsME5xqVWWUf2zn5oW1ep2Rc8xP8PvJcnnPWKHWi83",
  "payload": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhAAvAm/vG1S07tfJT0YkXicux/8hBoPg5nH4j8SpREenaindNRlfmhBJV5xAgLaDKKOjxRq5Ol9S0ApScV/MlaA7hADLy2DiY0lXSxKVnHIS7kctIBAcibrPgxtwiUx8ZC+mZvN6L3txOeqsqAncYBXFzeTuCS//mlKUt8NLvHoyhKA7iX+JU5AaEGtGAwuD35MlGCOST5+tTA+3e2TVaBwmkdUDxODdVYwIwG+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaDwZQ8gtvUEyGfm3kGX5jplOBh1f3MifkAHG85vI5x8EF6JI2Y=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaClZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4vKCgEAhiRhOcqAALDvQAGgDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqLygoBAIY/qiUiYAAoH7hl"
  },
  "tag": "offchain_state",
  "version": 1
}
```
