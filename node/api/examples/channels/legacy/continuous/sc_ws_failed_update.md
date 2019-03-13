
#### initiator: (2019-03-18 14:15:56.438)
> Failing update, insufficient balance

#### initiator ---> node (2019-03-18 14:15:56.438)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 10000000000000000,
    "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
  },
  "tag": "new"
}
```

#### initiator <--- node (2019-03-18 14:15:56.452)
```javascript
{
  "action": "error",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "reason": "insufficient_balance",
    "request": {
      "method": "channels.update.new",
      "params": {
        "amount": 10000000000000000,
        "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
      }
    }
  },
  "version": 1
}
```

#### initiator: (2019-03-18 14:15:56.453)
> Failing update, negative amount

#### initiator ---> node (2019-03-18 14:15:56.453)
```javascript
{
  "action": "update",
  "payload": {
    "amount": -1,
    "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
  },
  "tag": "new"
}
```

#### initiator <--- node (2019-03-18 14:15:56.455)
```javascript
{
  "action": "error",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "reason": "negative_amount",
    "request": {
      "method": "channels.update.new",
      "params": {
        "amount": -1,
        "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
      }
    }
  },
  "version": 1
}
```

#### initiator: (2019-03-18 14:15:56.455)
> Failing update, invalid pubkeys

#### initiator ---> node (2019-03-18 14:15:56.456)
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

#### initiator <--- node (2019-03-18 14:15:56.461)
```javascript
{
  "action": "error",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
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

#### responder: (2019-03-18 14:15:56.462)
> Failing update, insufficient balance

#### responder ---> node (2019-03-18 14:15:56.462)
```javascript
{
  "action": "update",
  "payload": {
    "amount": 10000000000000000,
    "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
  },
  "tag": "new"
}
```

#### responder <--- node (2019-03-18 14:15:56.487)
```javascript
{
  "action": "error",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "reason": "insufficient_balance",
    "request": {
      "method": "channels.update.new",
      "params": {
        "amount": 10000000000000000,
        "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
      }
    }
  },
  "version": 1
}
```

#### responder: (2019-03-18 14:15:56.488)
> Failing update, negative amount

#### responder ---> node (2019-03-18 14:15:56.488)
```javascript
{
  "action": "update",
  "payload": {
    "amount": -1,
    "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
    "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
  },
  "tag": "new"
}
```

#### responder <--- node (2019-03-18 14:15:56.493)
```javascript
{
  "action": "error",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
  "payload": {
    "reason": "negative_amount",
    "request": {
      "method": "channels.update.new",
      "params": {
        "amount": -1,
        "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
      }
    }
  },
  "version": 1
}
```

#### responder: (2019-03-18 14:15:56.494)
> Failing update, invalid pubkeys

#### responder ---> node (2019-03-18 14:15:56.495)
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

#### responder <--- node (2019-03-18 14:15:56.502)
```javascript
{
  "action": "error",
  "channel_id": "ch_2WDx2uyKSNAMSEb11eczNNtSMyRLNfhFAUwwP73xDk4cngy9u9",
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
