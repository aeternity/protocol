
#### initiator ---> node (2019-03-13 11:14:09.299)
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

#### responder ---> node (2019-03-13 11:14:09.299)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 2,
    "from": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn",
    "to": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9"
  },
  "tag": "new"
}
```

#### responder <--- node (2019-03-13 11:14:09.314)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "tx": "tx_+JU5AaEG3hZD/8OqLoPpLcMc5cfQwNyjR2sUdl6Nry6JJUyBUsIG+E24S/hJggI6AaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAqAX383H/KgpEQIpg9Po/E8dG/Q6/XH1u+YXLcbI4TXs3rNn01g="
  },
  "tag": "update",
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:14:09.316)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "tx": "tx_+JU5AaEG3hZD/8OqLoPpLcMc5cfQwNyjR2sUdl6Nry6JJUyBUsIG+E24S/hJggI6AaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqhAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrAaA7pv4mg8xv+FCuz/dffsQJfmMd+RvIpdZVGhCPqJtqst4rnyM="
  },
  "tag": "update",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:14:09.317)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEC1TAIBQ7hyRvXbzpceCzatrtXV2Kco8HW6yZecRVIFjlc1aPBXyZi/kyLa6yId0FC47ns00p7l7gYcMtw+WrYDuJf4lTkBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwgb4TbhL+EmCAjoBoQEMHR+jKB9TfmalcAw4HlPfLlTP4fGLC6AeHxDL+MjeeqEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFysBoDum/iaDzG/4UK7P919+xAl+Yx35G8il1lUaEI+om2qypMh40w=="
  }
}
```

#### responder ---> node (2019-03-13 11:14:09.318)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEAKPo25PCZ/WsJoRT42EOG7OJBm/0wIgpzPp7LceQcyXeVAJ0TjLeBfpI5yx/E7SoMGlSUbDh6n+IUoIgVQEzcPuJf4lTkBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwgb4TbhL+EmCAjoBoQEMHR+jKB9TfmalcAw4HlPfLlTP4fGLC6AeHxDL+MjeeqEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFysCoBffzcf8qCkRAimD0+j8Tx0b9Dr9cfW75hctxsjhNezeD7qlzQ=="
  }
}
```

#### responder <--- node (2019-03-13 11:14:09.335)
```javascript
{
  "action": "conflict",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
    "round": 5
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:14:09.336)
```javascript
{
  "action": "conflict",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
    "round": 5
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:14:09.338)
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

#### initiator ---> node (2019-03-13 11:14:09.338)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 2,
    "from": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
    "to": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn"
  },
  "tag": "new"
}
```

#### responder <--- node (2019-03-13 11:14:09.340)
```javascript
{
  "action": "conflict",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
    "round": 5
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:14:09.341)
```javascript
{
  "action": "conflict",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
    "round": 5
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:14:09.353)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "tx": "tx_+JU5AaEG3hZD/8OqLoPpLcMc5cfQwNyjR2sUdl6Nry6JJUyBUsIG+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AaDwZQ8gtvUEyGfm3kGX5jplOBh1f3MifkAHG85vI5x8EMaKyi8="
  },
  "tag": "update",
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:14:09.353)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "tx": "tx_+JU5AaEG3hZD/8OqLoPpLcMc5cfQwNyjR2sUdl6Nry6JJUyBUsIG+E24S/hJggI6AaEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuhAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56AqBXkHpGK2y9UbOg9c15kRlDqsoHzwtR/hc1S4km0id7q7y853k="
  },
  "tag": "update",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:14:09.355)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEDBpDsaIJGWZezylkN2UmRwofWoy0c3N39lU/GU4vvIWo/MKIxiTUal77eAAA51gIseKr7NFaGjMdZKs14XwUYAuJf4lTkBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwgb4TbhL+EmCAjoBoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK6EBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noBoPBlDyC29QTIZ+beQZfmOmU4GHV/cyJ+QAcbzm8jnHwQXnrCZw=="
  }
}
```

#### initiator ---> node (2019-03-13 11:14:09.356)
```javascript
{
  "action": "update",
  "payload": {
    "tx": "tx_+N8LAfhCuEDIax79dMdZ2uKEn7kcPAFrGksBcVtK8LifFH3U7s31iRLheIZz5TZAYlX5ck3r5vlKH3OLCR145jsE6bqOUEECuJf4lTkBoQbeFkP/w6oug+ktwxzlx9DA3KNHaxR2Xo2vLoklTIFSwgb4TbhL+EmCAjoBoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK6EBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3noCoFeQekYrbL1Rs6D1zXmRGUOqygfPC1H+FzVLiSbSJ3urBnUeEw=="
  }
}
```

#### responder <--- node (2019-03-13 11:14:09.374)
```javascript
{
  "action": "conflict",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
    "round": 5
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:14:09.375)
```javascript
{
  "action": "conflict",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
    "round": 5
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:14:09.376)
```javascript
{
  "action": "conflict",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
    "round": 5
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:14:09.376)
```javascript
{
  "action": "conflict",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
    "round": 5
  },
  "version": 1
}
```
