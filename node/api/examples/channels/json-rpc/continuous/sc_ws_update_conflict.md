
#### initiator ---> node (2019-03-13 11:05:36.660)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
    "to": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
  }
}
```

#### responder ---> node (2019-03-13 11:05:36.660)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 2,
    "from": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs",
    "to": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3"
  }
}
```

#### responder <--- node (2019-03-13 11:05:36.676)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "tx": "tx_+JU5AaEGvlKRORFMQ6yZVoRRHcALKMj/ey09I/8FJv6O9Cm+7QYG+E24S/hJggI6AaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56ehAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAqBHngQgVfALm79zVaQ+TOCyJUHJv+sXgfbNa+44nPZXtiM/rJA="
    }
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:05:36.680)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "tx": "tx_+JU5AaEGvlKRORFMQ6yZVoRRHcALKMj/ey09I/8FJv6O9Cm+7QYG+E24S/hJggI6AaEBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56ehAbmB2RdTyQ0rekjmPwIAfoY+c/EJmdijsdf+PoOwANtPAaDbfGCXUMfw4lZS/r1ddw6JYAjcG83JwCYsD8jmhgKs0kCdXFs="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:36.682)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuEB86fYsqBGivi9NNwKwHI1Yt44lVhLXhzX2c/ysXuIPnxg+BMQ/ozFIy8OqSEmep1kOd/EAHXlIwHwXqOlRjYIDuJf4lTkBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBgb4TbhL+EmCAjoBoQEmB6t0j6CEj0TF7aBkfLKhLNj0/vfE3UYgZ2CLIgbnp6EBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA208BoNt8YJdQx/DiVlL+vV13DolgCNwbzcnAJiwPyOaGAqzS3UyTiQ=="
  }
}
```

#### responder ---> node (2019-03-13 11:05:36.683)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuEAcBy/h+PTZzF5LFH9v9NQkOiEGnhkHQiu+pnoqoqrJcp53IuepBB7mIbaNsixmpIQmjnIO6BCiugfwln0nPaQKuJf4lTkBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBgb4TbhL+EmCAjoBoQEmB6t0j6CEj0TF7aBkfLKhLNj0/vfE3UYgZ2CLIgbnp6EBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA208CoEeeBCBV8Aubv3NVpD5M4LIlQcm/6xeB9s1r7jic9le2qsH7ww=="
  }
}
```

#### initiator <--- node (2019-03-13 11:05:36.704)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
      "round": 5
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:36.706)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
      "round": 5
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:36.707)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
      "round": 5
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:05:36.708)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
    "to": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
  }
}
```

#### initiator ---> node (2019-03-13 11:05:36.711)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 2,
    "from": "ak_2QhXumV8mm8Ni9ew5ZFsgcSysB9FtxjpqPWDSehgs7MJvFNoV3",
    "to": "ak_HkRcJAFekttmTHyeZUQkAiqMRvTQ7h9ekQsHWFYMaoNw1JNWs"
  }
}
```

#### initiator <--- node (2019-03-13 11:05:36.715)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
      "round": 5
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:36.721)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "tx": "tx_+JU5AaEGvlKRORFMQ6yZVoRRHcALKMj/ey09I/8FJv6O9Cm+7QYG+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAaBtJeqayYNAxAR8VEb/US6Hb7IetZ7x8ND25z+UAJu3M029aF0="
    }
  },
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:05:36.723)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuED6x5J4yx+XyWiZ/tNfjE+haru1olg+yhYiSBozeeYPL8OtgMZL0Bv/ZaaUG5mQzPo68clvG6aQqxtGi+loFh8NuJf4lTkBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBgb4TbhL+EmCAjoBoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT6EBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cBoG0l6prJg0DEBHxURv9RLodvsh61nvHw0PbnP5QAm7czEdsncQ=="
  }
}
```

#### initiator <--- node (2019-03-13 11:05:36.734)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "tx": "tx_+JU5AaEGvlKRORFMQ6yZVoRRHcALKMj/ey09I/8FJv6O9Cm+7QYG+E24S/hJggI6AaEBuYHZF1PJDSt6SOY/AgB+hj5z8QmZ2KOx1/4+g7AA20+hASYHq3SPoISPRMXtoGR8sqEs2PT+98TdRiBnYIsiBuenAqB/h0mU/M+PR9cCq4jG42oOvFeT9DZ0jHRhxy5288kMxVJlujk="
    }
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:05:36.735)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuEBgkA/S/aT9qXfvzLKBzhWZXGVJhwsQyDdw/z86BEv3O7mTISyhERc0KRKlfDpHj5wmy8fCAtnTK1hnanNmNtkOuJf4lTkBoQa+UpE5EUxDrJlWhFEdwAsoyP97LT0j/wUm/o70Kb7tBgb4TbhL+EmCAjoBoQG5gdkXU8kNK3pI5j8CAH6GPnPxCZnYo7HX/j6DsADbT6EBJgerdI+ghI9Exe2gZHyyoSzY9P73xN1GIGdgiyIG56cCoH+HSZT8z49H1wKriMbjag68V5P0NnSMdGHHLnbzyQzFCql89Q=="
  }
}
```

#### initiator <--- node (2019-03-13 11:05:36.743)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
      "round": 5
    }
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:05:36.744)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
    "data": {
      "channel_id": "ch_2SpXwrmkXpJkimN7CXsvM2x7FZGUEcJZ4oK91V4oVtG4Sui4cE",
      "round": 5
    }
  },
  "version": 1
}
```
