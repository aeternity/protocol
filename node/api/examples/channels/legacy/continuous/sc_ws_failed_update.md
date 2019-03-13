
#### initiator: (2019-03-13 11:14:08.997)
> Failing update, insufficient balance

#### initiator ---> node (2019-03-13 11:14:08.997)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 10000000000000000,
    "from": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn",
    "to": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9"
  },
  "tag": "new"
}
```

#### initiator <--- node (2019-03-13 11:14:09.9)
```javascript
{
  "action": "error",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "reason": "insufficient_balance",
    "request": {
      "method": "channels.update.new",
      "params": {
        "amount": 10000000000000000,
        "from": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn",
        "to": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9"
      }
    }
  },
  "version": 1
}
```

#### initiator: (2019-03-13 11:14:09.10)
> Failing update, negative amount

#### initiator ---> node (2019-03-13 11:14:09.10)
```javascript
{
  "action": "update",
  "payload": {
    "amount": -1,
    "from": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn",
    "to": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9"
  },
  "tag": "new"
}
```

#### initiator <--- node (2019-03-13 11:14:09.11)
```javascript
{
  "action": "error",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "reason": "negative_amount",
    "request": {
      "method": "channels.update.new",
      "params": {
        "amount": -1,
        "from": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn",
        "to": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9"
      }
    }
  },
  "version": 1
}
```

#### initiator: (2019-03-13 11:14:09.12)
> Failing update, invalid pubkeys

#### initiator ---> node (2019-03-13 11:14:09.12)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 1,
    "from": "ak_11111111111111111111111111111115rHyByZ",
    "to": "ak_11111111111111111111111111111115sBJATr"
  },
  "tag": "new"
}
```

#### initiator <--- node (2019-03-13 11:14:09.17)
```javascript
{
  "action": "error",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "reason": "invalid_pubkeys",
    "request": {
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_11111111111111111111111111111115rHyByZ",
        "to": "ak_11111111111111111111111111111115sBJATr"
      }
    }
  },
  "version": 1
}
```

#### responder: (2019-03-13 11:14:09.17)
> Failing update, insufficient balance

#### responder ---> node (2019-03-13 11:14:09.18)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 10000000000000000,
    "from": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
    "to": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn"
  },
  "tag": "new"
}
```

#### responder <--- node (2019-03-13 11:14:09.33)
```javascript
{
  "action": "error",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "reason": "insufficient_balance",
    "request": {
      "method": "channels.update.new",
      "params": {
        "amount": 10000000000000000,
        "from": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
        "to": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn"
      }
    }
  },
  "version": 1
}
```

#### responder: (2019-03-13 11:14:09.33)
> Failing update, negative amount

#### responder ---> node (2019-03-13 11:14:09.33)
```javascript
{
  "action": "update",
  "payload": {
    "amount": -1,
    "from": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
    "to": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn"
  },
  "tag": "new"
}
```

#### responder <--- node (2019-03-13 11:14:09.34)
```javascript
{
  "action": "error",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "reason": "negative_amount",
    "request": {
      "method": "channels.update.new",
      "params": {
        "amount": -1,
        "from": "ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9",
        "to": "ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn"
      }
    }
  },
  "version": 1
}
```

#### responder: (2019-03-13 11:14:09.35)
> Failing update, invalid pubkeys

#### responder ---> node (2019-03-13 11:14:09.35)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 1,
    "from": "ak_11111111111111111111111111111115sBJATr",
    "to": "ak_11111111111111111111111111111115rHyByZ"
  },
  "tag": "new"
}
```

#### responder <--- node (2019-03-13 11:14:09.40)
```javascript
{
  "action": "error",
  "channel_id": "ch_2gouzi4HtoExEMDucQ96sT4da6wg73cvJuD7Su3Uwqaaq3bFtT",
  "payload": {
    "reason": "invalid_pubkeys",
    "request": {
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_11111111111111111111111111111115sBJATr",
        "to": "ak_11111111111111111111111111111115rHyByZ"
      }
    }
  },
  "version": 1
}
```
