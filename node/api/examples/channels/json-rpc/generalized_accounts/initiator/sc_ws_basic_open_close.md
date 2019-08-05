
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2&lock_period=10&port=13454&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz&role=initiator
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2&lock_period=10&port=13454&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz&role=responder
```

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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yhj+qJSJgAKEBf3pGHzTC+loeGcbKEZaqtMp3G8SKG5kBCxANx0biSPuGJGE5yoAAAgoAhhAGeddIAMCgOAxQZ9e6FL82Wq63q0CGorzKnuQzxyO8v3980KZgN3oAFfVVjQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422486,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+QFuCwHAuQFo+QFlUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiK+IgLAcC4g/iBMgGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yhj+qJSJgAKEBf3pGHzTC+loeGcbKEZaqtMp3G8SKG5kBCxANx0biSPuGJGE5yoAAAgoAhhAGeddIAMCgOAxQZ9e6FL82Wq63q0CGorzKnuQzxyO8v3980KZgN3oA2fBLeQ=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422486,
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
      "signed_tx": "tx_+QFuCwHAuQFo+QFlUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiK+IgLAcC4g/iBMgGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yhj+qJSJgAKEBf3pGHzTC+loeGcbKEZaqtMp3G8SKG5kBCxANx0biSPuGJGE5yoAAAgoAhhAGeddIAMCgOAxQZ9e6FL82Wq63q0CGorzKnuQzxyO8v3980KZgN3oA2fBLeQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422485,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QGxCwHAuQGr+QGoUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEBf4pA3PaOtOWSt7A9/KpQU16wJaOTCsQwql/t1PivVbJTerv5HtPv0b+vL/PZNob7oe543arChz3pWuzkExVcCuIP4gTIBoQGAF1qSXoRJjoDKfGqHSgLe888eTGt1o4u8TwOC+u4+coY/qiUiYAChAX96Rh80wvpaHhnGyhGWqrTKdxvEihuZAQsQDcdG4kj7hiRhOcqAAAIKAIYQBnnXSADAoDgMUGfXuhS/Nlqut6tAhqK8yp7kM8cjvL9/fNCmYDd6AABKa0s="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422485,
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
    "channel_id": null,
    "data": {
      "info": "funding_created",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEBf4pA3PaOtOWSt7A9/KpQU16wJaOTCsQwql/t1PivVbJTerv5HtPv0b+vL/PZNob7oe543arChz3pWuzkExVcCuIP4gTIBoQGAF1qSXoRJjoDKfGqHSgLe888eTGt1o4u8TwOC+u4+coY/qiUiYAChAX96Rh80wvpaHhnGyhGWqrTKdxvEihuZAQsQDcdG4kj7hiRhOcqAAAIKAIYQBnnXSADAoDgMUGfXuhS/Nlqut6tAhqK8yp7kM8cjvL9/fNCmYDd6AABKa0s=",
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
    "channel_id": null,
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEBf4pA3PaOtOWSt7A9/KpQU16wJaOTCsQwql/t1PivVbJTerv5HtPv0b+vL/PZNob7oe543arChz3pWuzkExVcCuIP4gTIBoQGAF1qSXoRJjoDKfGqHSgLe888eTGt1o4u8TwOC+u4+coY/qiUiYAChAX96Rh80wvpaHhnGyhGWqrTKdxvEihuZAQsQDcdG4kj7hiRhOcqAAAIKAIYQBnnXSADAoDgMUGfXuhS/Nlqut6tAhqK8yp7kM8cjvL9/fNCmYDd6AABKa0s=",
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
    "channel_id": null,
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEBf4pA3PaOtOWSt7A9/KpQU16wJaOTCsQwql/t1PivVbJTerv5HtPv0b+vL/PZNob7oe543arChz3pWuzkExVcCuIP4gTIBoQGAF1qSXoRJjoDKfGqHSgLe888eTGt1o4u8TwOC+u4+coY/qiUiYAChAX96Rh80wvpaHhnGyhGWqrTKdxvEihuZAQsQDcdG4kj7hiRhOcqAAAIKAIYQBnnXSADAoDgMUGfXuhS/Nlqut6tAhqK8yp7kM8cjvL9/fNCmYDd6AABKa0s=",
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
    "channel_id": null,
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QGxCwHAuQGr+QGoUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEBf4pA3PaOtOWSt7A9/KpQU16wJaOTCsQwql/t1PivVbJTerv5HtPv0b+vL/PZNob7oe543arChz3pWuzkExVcCuIP4gTIBoQGAF1qSXoRJjoDKfGqHSgLe888eTGt1o4u8TwOC+u4+coY/qiUiYAChAX96Rh80wvpaHhnGyhGWqrTKdxvEihuZAQsQDcdG4kj7hiRhOcqAAAIKAIYQBnnXSADAoDgMUGfXuhS/Nlqut6tAhqK8yp7kM8cjvL9/fNCmYDd6AABKa0s=",
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
    "to": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "message": {
        "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
        "from": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
        "info": "Hello",
        "to": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz"
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
    "to": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "message": {
        "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
        "from": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
        "info": "Hello back",
        "to": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422484,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
      "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422484,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
      "balance": 69999999999999
    },
    {
      "account": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "event": "own_funding_locked"
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### responder info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "event": "funding_locked"
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "state": "tx_+QGxCwHAuQGr+QGoUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEBf4pA3PaOtOWSt7A9/KpQU16wJaOTCsQwql/t1PivVbJTerv5HtPv0b+vL/PZNob7oe543arChz3pWuzkExVcCuIP4gTIBoQGAF1qSXoRJjoDKfGqHSgLe888eTGt1o4u8TwOC+u4+coY/qiUiYAChAX96Rh80wvpaHhnGyhGWqrTKdxvEihuZAQsQDcdG4kj7hiRhOcqAAAIKAIYQBnnXSADAoDgMUGfXuhS/Nlqut6tAhqK8yp7kM8cjvL9/fNCmYDd6AABKa0s="
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "state": "tx_+QGxCwHAuQGr+QGoUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALjN+MsLAfhCuEBf4pA3PaOtOWSt7A9/KpQU16wJaOTCsQwql/t1PivVbJTerv5HtPv0b+vL/PZNob7oe543arChz3pWuzkExVcCuIP4gTIBoQGAF1qSXoRJjoDKfGqHSgLe888eTGt1o4u8TwOC+u4+coY/qiUiYAChAX96Rh80wvpaHhnGyhGWqrTKdxvEihuZAQsQDcdG4kj7hiRhOcqAAAIKAIYQBnnXSADAoDgMUGfXuhS/Nlqut6tAhqK8yp7kM8cjvL9/fNCmYDd6AABKa0s="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422483,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
      "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422483,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
      "balance": 69999999999999
    },
    {
      "account": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
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
    "from": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
    "to": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
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
        "from": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
        "to": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz"
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
    "to": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
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
        "to": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz"
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
    "from": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
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
        "from": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
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
    "from": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
    "to": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuo88KcZ72nou8s0F5sQDWv/z2FhNUUdTfEmbl/e/VwcAqCkGVuAx+vzGuMq8BDNBk8cUW4zQbwbwOxM5ONI4ViLO8zvH0M=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
          "op": "OffChainTransfer",
          "to": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz"
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
  "id": -576460752303422482,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBuo88KcZ72nou8s0F5sQDWv/z2FhNUUdTfEmbl/e/VwcAqCkGVuAx+vzGuMq8BDNBk8cUW4zQbwbwOxM5ONI4ViLO8uX7vA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422482,
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBuo88KcZ72nou8s0F5sQDWv/z2FhNUUdTfEmbl/e/VwcAqCkGVuAx+vzGuMq8BDNBk8cUW4zQbwbwOxM5ONI4ViLO8uX7vA=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
          "op": "OffChainTransfer",
          "to": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz"
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
  "id": -576460752303422481,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAHGVxp+2v8kUQTljMck2OFaMC0BXfG2XdpJHeBj88k1LKVi/HWXNguqrOcLizO0xhLbeMfJ9cqGEK1p0LFfHYHuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHAKgpBlbgMfr8xrjKvAQzQZPHFFuM0G8G8DsTOTjSOFYizukYKZC"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422481,
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAHGVxp+2v8kUQTljMck2OFaMC0BXfG2XdpJHeBj88k1LKVi/HWXNguqrOcLizO0xhLbeMfJ9cqGEK1p0LFfHYHuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHAKgpBlbgMfr8xrjKvAQzQZPHFFuM0G8G8DsTOTjSOFYizukYKZC"
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAHGVxp+2v8kUQTljMck2OFaMC0BXfG2XdpJHeBj88k1LKVi/HWXNguqrOcLizO0xhLbeMfJ9cqGEK1p0LFfHYHuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHAKgpBlbgMfr8xrjKvAQzQZPHFFuM0G8G8DsTOTjSOFYizukYKZC"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422480,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
      "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422480,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
      "balance": 69999999999998
    },
    {
      "account": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422479,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422479,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAHGVxp+2v8kUQTljMck2OFaMC0BXfG2XdpJHeBj88k1LKVi/HWXNguqrOcLizO0xhLbeMfJ9cqGEK1p0LFfHYHuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHAKgpBlbgMfr8xrjKvAQzQZPHFFuM0G8G8DsTOTjSOFYizukYKZC",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCAF1qSXoRJjoDKfGqHSgLe888eTGt1o4u8TwOC+u4+covKCgEAhj+qJSJf/rDvQAGgf3pGHzTC+loeGcbKEZaqtMp3G8SKG5kBCxANx0biSPuLygoBAIYkYTnKgAI9a2RG"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422478,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
      "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422478,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
      "balance": 40000000000002
    },
    {
      "account": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
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
    "from": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
    "to": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
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
        "from": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
        "to": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
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
    "to": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
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
        "to": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
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
    "from": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
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
        "from": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
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
    "from": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
    "to": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuo88KcZ72nou8s0F5sQDWv/z2FhNUUdTfEmbl/e/VwcA6A4DFBn17oUvzZarrerQIaivMqe5DPHI7y/f3zQpmA3ehJqz2E=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
          "op": "OffChainTransfer",
          "to": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
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
  "id": -576460752303422477,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAD0PX0sxmG4MmRnZiBADlcue/C03/sJ3bujEn6O+N+3oHccskBAbjhp2xcfT/OCDy1FhAQX0ow9lWo9TZ+iyEFuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHAOgOAxQZ9e6FL82Wq63q0CGorzKnuQzxyO8v3980KZgN3oCus3x"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422477,
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAD0PX0sxmG4MmRnZiBADlcue/C03/sJ3bujEn6O+N+3oHccskBAbjhp2xcfT/OCDy1FhAQX0ow9lWo9TZ+iyEFuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHAOgOAxQZ9e6FL82Wq63q0CGorzKnuQzxyO8v3980KZgN3oCus3x",
      "updates": [
        {
          "amount": 1,
          "from": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
          "op": "OffChainTransfer",
          "to": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
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
  "id": -576460752303422476,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAD0PX0sxmG4MmRnZiBADlcue/C03/sJ3bujEn6O+N+3oHccskBAbjhp2xcfT/OCDy1FhAQX0ow9lWo9TZ+iyEFuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHAOgOAxQZ9e6FL82Wq63q0CGorzKnuQzxyO8v3980KZgN3rmozuy"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422476,
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAD0PX0sxmG4MmRnZiBADlcue/C03/sJ3bujEn6O+N+3oHccskBAbjhp2xcfT/OCDy1FhAQX0ow9lWo9TZ+iyEFuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHAOgOAxQZ9e6FL82Wq63q0CGorzKnuQzxyO8v3980KZgN3rmozuy"
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAD0PX0sxmG4MmRnZiBADlcue/C03/sJ3bujEn6O+N+3oHccskBAbjhp2xcfT/OCDy1FhAQX0ow9lWo9TZ+iyEFuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHAOgOAxQZ9e6FL82Wq63q0CGorzKnuQzxyO8v3980KZgN3rmozuy"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422475,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
      "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422475,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
      "balance": 40000000000001
    },
    {
      "account": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422474,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422474,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEAD0PX0sxmG4MmRnZiBADlcue/C03/sJ3bujEn6O+N+3oHccskBAbjhp2xcfT/OCDy1FhAQX0ow9lWo9TZ+iyEFuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHAOgOAxQZ9e6FL82Wq63q0CGorzKnuQzxyO8v3980KZgN3rmozuy",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCAF1qSXoRJjoDKfGqHSgLe888eTGt1o4u8TwOC+u4+covKCgEAhj+qJSJf/7DvQAGgf3pGHzTC+loeGcbKEZaqtMp3G8SKG5kBCxANx0biSPuLygoBAIYkYTnKgAHQdGYc"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422473,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
      "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422473,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
      "balance": 40000000000001
    },
    {
      "account": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
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
    "from": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
    "to": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
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
        "from": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
        "to": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
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
    "to": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
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
        "to": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
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
    "from": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
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
        "from": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
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
    "from": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
    "to": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuo88KcZ72nou8s0F5sQDWv/z2FhNUUdTfEmbl/e/VwcBKBGmxviEOFj3mlAF8cgau4mUbaZh4Lx4g+5FqNGaLL39dBXta8=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
          "op": "OffChainTransfer",
          "to": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
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
  "id": -576460752303422472,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB8/nMzfGjVgVSjIBRTvWfuefABZ7vICnvHXgtSiRA4oS6aMpabJxiJ48gbudmlYs1Tow3eU3nIZdsIKKo79WgKuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHASgRpsb4hDhY95pQBfHIGruJlG2mYeC8eIPuRajRmiy9/W6GbY8"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422472,
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB8/nMzfGjVgVSjIBRTvWfuefABZ7vICnvHXgtSiRA4oS6aMpabJxiJ48gbudmlYs1Tow3eU3nIZdsIKKo79WgKuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHASgRpsb4hDhY95pQBfHIGruJlG2mYeC8eIPuRajRmiy9/W6GbY8",
      "updates": [
        {
          "amount": 1,
          "from": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
          "op": "OffChainTransfer",
          "to": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
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
  "id": -576460752303422471,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEB8/nMzfGjVgVSjIBRTvWfuefABZ7vICnvHXgtSiRA4oS6aMpabJxiJ48gbudmlYs1Tow3eU3nIZdsIKKo79WgKuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHASgRpsb4hDhY95pQBfHIGruJlG2mYeC8eIPuRajRmiy9/VG4JcD"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422471,
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEB8/nMzfGjVgVSjIBRTvWfuefABZ7vICnvHXgtSiRA4oS6aMpabJxiJ48gbudmlYs1Tow3eU3nIZdsIKKo79WgKuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHASgRpsb4hDhY95pQBfHIGruJlG2mYeC8eIPuRajRmiy9/VG4JcD"
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEB8/nMzfGjVgVSjIBRTvWfuefABZ7vICnvHXgtSiRA4oS6aMpabJxiJ48gbudmlYs1Tow3eU3nIZdsIKKo79WgKuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHASgRpsb4hDhY95pQBfHIGruJlG2mYeC8eIPuRajRmiy9/VG4JcD"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422470,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
      "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422470,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
      "balance": 40000000000000
    },
    {
      "account": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422469,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422469,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEB8/nMzfGjVgVSjIBRTvWfuefABZ7vICnvHXgtSiRA4oS6aMpabJxiJ48gbudmlYs1Tow3eU3nIZdsIKKo79WgKuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHASgRpsb4hDhY95pQBfHIGruJlG2mYeC8eIPuRajRmiy9/VG4JcD",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCAF1qSXoRJjoDKfGqHSgLe888eTGt1o4u8TwOC+u4+covKCgEAhj+qJSJgALDvQAGgf3pGHzTC+loeGcbKEZaqtMp3G8SKG5kBCxANx0biSPuLygoBAIYkYTnKgACZ0dTB"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422468,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
      "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422468,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
      "balance": 70000000000000
    },
    {
      "account": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
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
    "from": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
    "to": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
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
        "from": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
        "to": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz"
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
    "to": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
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
        "to": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz"
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
    "from": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
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
        "from": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
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
    "from": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
    "to": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuo88KcZ72nou8s0F5sQDWv/z2FhNUUdTfEmbl/e/VwcBaA4DFBn17oUvzZarrerQIaivMqe5DPHI7y/f3zQpmA3euxA2ZU=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
          "op": "OffChainTransfer",
          "to": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz"
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
  "id": -576460752303422467,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBuo88KcZ72nou8s0F5sQDWv/z2FhNUUdTfEmbl/e/VwcBaA4DFBn17oUvzZarrerQIaivMqe5DPHI7y/f3zQpmA3el0hUTA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422467,
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "signed_tx": "tx_+QEzCwHAuQEt+QEqUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALhP+E0LAcC4SPhGOQKhBuo88KcZ72nou8s0F5sQDWv/z2FhNUUdTfEmbl/e/VwcBaA4DFBn17oUvzZarrerQIaivMqe5DPHI7y/f3zQpmA3el0hUTA=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
          "op": "OffChainTransfer",
          "to": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz"
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
  "id": -576460752303422466,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEBr4pHdfT91sKxiaN0pOMNMGcb1M07D323bx20fjd38sj7b5FyJ8G36PGphSQXwz3n0wjJXy4icVliu/HC0AScGuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHAWgOAxQZ9e6FL82Wq63q0CGorzKnuQzxyO8v3980KZgN3qPPpCE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422466,
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEBr4pHdfT91sKxiaN0pOMNMGcb1M07D323bx20fjd38sj7b5FyJ8G36PGphSQXwz3n0wjJXy4icVliu/HC0AScGuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHAWgOAxQZ9e6FL82Wq63q0CGorzKnuQzxyO8v3980KZgN3qPPpCE"
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEBr4pHdfT91sKxiaN0pOMNMGcb1M07D323bx20fjd38sj7b5FyJ8G36PGphSQXwz3n0wjJXy4icVliu/HC0AScGuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHAWgOAxQZ9e6FL82Wq63q0CGorzKnuQzxyO8v3980KZgN3qPPpCE"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422465,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
      "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422465,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
      "balance": 69999999999999
    },
    {
      "account": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422464,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422464,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEBr4pHdfT91sKxiaN0pOMNMGcb1M07D323bx20fjd38sj7b5FyJ8G36PGphSQXwz3n0wjJXy4icVliu/HC0AScGuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHAWgOAxQZ9e6FL82Wq63q0CGorzKnuQzxyO8v3980KZgN3qPPpCE",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCAF1qSXoRJjoDKfGqHSgLe888eTGt1o4u8TwOC+u4+covKCgEAhj+qJSJf/7DvQAGgf3pGHzTC+loeGcbKEZaqtMp3G8SKG5kBCxANx0biSPuLygoBAIYkYTnKgAHQdGYc"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422463,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
      "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422463,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
      "balance": 40000000000001
    },
    {
      "account": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
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
    "from": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
    "to": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
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
        "from": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
        "to": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
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
    "to": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
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
        "to": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
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
    "from": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
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
        "from": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
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
    "from": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
    "to": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBuo88KcZ72nou8s0F5sQDWv/z2FhNUUdTfEmbl/e/VwcBqBGmxviEOFj3mlAF8cgau4mUbaZh4Lx4g+5FqNGaLL39RshXb4=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
          "op": "OffChainTransfer",
          "to": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
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
  "id": -576460752303422462,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDlCIErnXGETJ2W0XnR9uaPqTSQVHPFY6SVwGO3ybU1OoIu6+ZuudAxy1WYcZVvqv9I6AY9OhxXCrBZ9KF4YcUHuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHAagRpsb4hDhY95pQBfHIGruJlG2mYeC8eIPuRajRmiy9/XikoIq"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422462,
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDlCIErnXGETJ2W0XnR9uaPqTSQVHPFY6SVwGO3ybU1OoIu6+ZuudAxy1WYcZVvqv9I6AY9OhxXCrBZ9KF4YcUHuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHAagRpsb4hDhY95pQBfHIGruJlG2mYeC8eIPuRajRmiy9/XikoIq",
      "updates": [
        {
          "amount": 1,
          "from": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
          "op": "OffChainTransfer",
          "to": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
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
  "id": -576460752303422461,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDlCIErnXGETJ2W0XnR9uaPqTSQVHPFY6SVwGO3ybU1OoIu6+ZuudAxy1WYcZVvqv9I6AY9OhxXCrBZ9KF4YcUHuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHAagRpsb4hDhY95pQBfHIGruJlG2mYeC8eIPuRajRmiy9/UU6qbU"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422461,
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDlCIErnXGETJ2W0XnR9uaPqTSQVHPFY6SVwGO3ybU1OoIu6+ZuudAxy1WYcZVvqv9I6AY9OhxXCrBZ9KF4YcUHuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHAagRpsb4hDhY95pQBfHIGruJlG2mYeC8eIPuRajRmiy9/UU6qbU"
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
    "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
    "data": {
      "state": "tx_+QF2CwHAuQFw+QFtUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDlCIErnXGETJ2W0XnR9uaPqTSQVHPFY6SVwGO3ybU1OoIu6+ZuudAxy1WYcZVvqv9I6AY9OhxXCrBZ9KF4YcUHuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHAagRpsb4hDhY95pQBfHIGruJlG2mYeC8eIPuRajRmiy9/UU6qbU"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422460,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
      "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422460,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_y9FDH14q5Mtjd3AYoStrdV6Z9DkXKZAvSAujK5gMfsvcEjjgz",
      "balance": 40000000000000
    },
    {
      "account": "ak_yQvGekawHYcR3kBxGsGfZM9TrN2Ktj7zKnCJE5tdA2A2SgzS2",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422459,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2nAJCXtYtJxNcP8aM3ZgNR6vSGWEnaHfxwHVgEUjou3o7VY3xz",
  "id": -576460752303422459,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QF2CwHAuQFw+QFtUQGhAYAXWpJehEmOgMp8aodKAt7zzx5Ma3Wji7xPA4L67j5yuKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIOlPA4RhnKrkGsO393LKP5do+0tIaKWDPh28sc1y9it/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAYcDjX6kxoAAgk4ghejUpRAAALiS+JALAfhCuEDlCIErnXGETJ2W0XnR9uaPqTSQVHPFY6SVwGO3ybU1OoIu6+ZuudAxy1WYcZVvqv9I6AY9OhxXCrBZ9KF4YcUHuEj4RjkCoQbqPPCnGe9p6LvLNBebEA1r/89hYTVFHU3xJm5f3v1cHAagRpsb4hDhY95pQBfHIGruJlG2mYeC8eIPuRajRmiy9/UU6qbU",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCAF1qSXoRJjoDKfGqHSgLe888eTGt1o4u8TwOC+u4+covKCgEAhj+qJSJgALDvQAGgf3pGHzTC+loeGcbKEZaqtMp3G8SKG5kBCxANx0biSPuLygoBAIYkYTnKgACZ0dTB"
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP&lock_period=10&port=12890&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF&role=initiator
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP&lock_period=10&port=12890&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF&role=responder
```

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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+hj+qJSJgAKEBF0ouZW0JiF0HMMU8R2zQ14W4kEExkAu1y8LRPKIRoJWGJGE5yoAAAgoAhhAGeddIAMCg0vKgyNzsW83DCJkdWpLvgtO9MoJQHSy69mswIBEt01IAVbt6wA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421575,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+NQLAcC4z/jNUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQHrs/OJZvLQmRTTK4X/A3473wFFi8OKB1TKo4GyaWElPoY/qiUiYAChARdKLmVtCYhdBzDFPEds0NeFuJBBMZALtcvC0TyiEaCVhiRhOcqAAAIKAIYQBnnXSADAoNLyoMjc7FvNwwiZHVqS74LTvTKCUB0suvZrMCARLdNSAP7Ssyo="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421575,
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
      "signed_tx": "tx_+NQLAcC4z/jNUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4iviICwHAuIP4gTIBoQHrs/OJZvLQmRTTK4X/A3473wFFi8OKB1TKo4GyaWElPoY/qiUiYAChARdKLmVtCYhdBzDFPEds0NeFuJBBMZALtcvC0TyiEaCVhiRhOcqAAAIKAIYQBnnXSADAoNLyoMjc7FvNwwiZHVqS74LTvTKCUB0suvZrMCARLdNSAP7Ssyo=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421574,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEZCwHAuQET+QEQUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAVAvHJkCUG5RaKQgfXyS7ftT1/mZqstWRv/a16b/+dQGL5DpWVlKQJoM0wOOyVbU6BSEELYb8bJHHywT53rX0DbiD+IEyAaEB67PziWby0JkU0yuF/wN+O98BRYvDigdUyqOBsmlhJT6GP6olImAAoQEXSi5lbQmIXQcwxTxHbNDXhbiQQTGQC7XLwtE8ohGglYYkYTnKgAACCgCGEAZ510gAwKDS8qDI3OxbzcMImR1aku+C070yglAdLLr2azAgES3TUgAeZ4tN"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421574,
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
    "channel_id": null,
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAVAvHJkCUG5RaKQgfXyS7ftT1/mZqstWRv/a16b/+dQGL5DpWVlKQJoM0wOOyVbU6BSEELYb8bJHHywT53rX0DbiD+IEyAaEB67PziWby0JkU0yuF/wN+O98BRYvDigdUyqOBsmlhJT6GP6olImAAoQEXSi5lbQmIXQcwxTxHbNDXhbiQQTGQC7XLwtE8ohGglYYkYTnKgAACCgCGEAZ510gAwKDS8qDI3OxbzcMImR1aku+C070yglAdLLr2azAgES3TUgAeZ4tN",
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
    "channel_id": null,
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAVAvHJkCUG5RaKQgfXyS7ftT1/mZqstWRv/a16b/+dQGL5DpWVlKQJoM0wOOyVbU6BSEELYb8bJHHywT53rX0DbiD+IEyAaEB67PziWby0JkU0yuF/wN+O98BRYvDigdUyqOBsmlhJT6GP6olImAAoQEXSi5lbQmIXQcwxTxHbNDXhbiQQTGQC7XLwtE8ohGglYYkYTnKgAACCgCGEAZ510gAwKDS8qDI3OxbzcMImR1aku+C070yglAdLLr2azAgES3TUgAeZ4tN",
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
    "channel_id": null,
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAVAvHJkCUG5RaKQgfXyS7ftT1/mZqstWRv/a16b/+dQGL5DpWVlKQJoM0wOOyVbU6BSEELYb8bJHHywT53rX0DbiD+IEyAaEB67PziWby0JkU0yuF/wN+O98BRYvDigdUyqOBsmlhJT6GP6olImAAoQEXSi5lbQmIXQcwxTxHbNDXhbiQQTGQC7XLwtE8ohGglYYkYTnKgAACCgCGEAZ510gAwKDS8qDI3OxbzcMImR1aku+C070yglAdLLr2azAgES3TUgAeZ4tN",
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
    "channel_id": null,
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEZCwHAuQET+QEQUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAVAvHJkCUG5RaKQgfXyS7ftT1/mZqstWRv/a16b/+dQGL5DpWVlKQJoM0wOOyVbU6BSEELYb8bJHHywT53rX0DbiD+IEyAaEB67PziWby0JkU0yuF/wN+O98BRYvDigdUyqOBsmlhJT6GP6olImAAoQEXSi5lbQmIXQcwxTxHbNDXhbiQQTGQC7XLwtE8ohGglYYkYTnKgAACCgCGEAZ510gAwKDS8qDI3OxbzcMImR1aku+C070yglAdLLr2azAgES3TUgAeZ4tN",
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
    "to": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "message": {
        "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
        "from": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
        "info": "Hello",
        "to": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF"
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
    "to": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "message": {
        "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
        "from": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
        "info": "Hello back",
        "to": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421573,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
      "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421573,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
      "balance": 69999999999999
    },
    {
      "account": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "state": "tx_+QEZCwHAuQET+QEQUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAVAvHJkCUG5RaKQgfXyS7ftT1/mZqstWRv/a16b/+dQGL5DpWVlKQJoM0wOOyVbU6BSEELYb8bJHHywT53rX0DbiD+IEyAaEB67PziWby0JkU0yuF/wN+O98BRYvDigdUyqOBsmlhJT6GP6olImAAoQEXSi5lbQmIXQcwxTxHbNDXhbiQQTGQC7XLwtE8ohGglYYkYTnKgAACCgCGEAZ510gAwKDS8qDI3OxbzcMImR1aku+C070yglAdLLr2azAgES3TUgAeZ4tN"
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "state": "tx_+QEZCwHAuQET+QEQUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4zfjLCwH4QrhAVAvHJkCUG5RaKQgfXyS7ftT1/mZqstWRv/a16b/+dQGL5DpWVlKQJoM0wOOyVbU6BSEELYb8bJHHywT53rX0DbiD+IEyAaEB67PziWby0JkU0yuF/wN+O98BRYvDigdUyqOBsmlhJT6GP6olImAAoQEXSi5lbQmIXQcwxTxHbNDXhbiQQTGQC7XLwtE8ohGglYYkYTnKgAACCgCGEAZ510gAwKDS8qDI3OxbzcMImR1aku+C070yglAdLLr2azAgES3TUgAeZ4tN"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421572,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
      "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421572,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
      "balance": 69999999999999
    },
    {
      "account": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
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
    "from": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
    "to": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
        "from": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
        "to": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF"
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
    "to": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
        "to": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF"
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
    "from": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
        "from": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
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
    "from": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
    "to": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiVixIOErNItkdhQPoejQcX5mO/XqiHtzPDjBiRbavLkAqA4QCzLMmkGTrgUqj4Tx29dQp6N3GNYemdqLsb86Ed0VLE1Kho=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
          "op": "OffChainTransfer",
          "to": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF"
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
  "id": -576460752303421571,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQYlYsSDhKzSLZHYUD6Ho0HF+Zjv16oh7czw4wYkW2ry5AKgOEAsyzJpBk64FKo+E8dvXUKejdxjWHpnai7G/OhHdFTAPufM"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421571,
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQYlYsSDhKzSLZHYUD6Ho0HF+Zjv16oh7czw4wYkW2ry5AKgOEAsyzJpBk64FKo+E8dvXUKejdxjWHpnai7G/OhHdFTAPufM",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
          "op": "OffChainTransfer",
          "to": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF"
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
  "id": -576460752303421570,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAHBweGQ2P5jAqVjrhD3j2VpYSBsQNMjtgclJtLuukIQEPPcRGySeIz2kDVm2SP8jRCX8nFufCJthVONE6eGfiDLhI+EY5AqEGJWLEg4Ss0i2R2FA+h6NBxfmY79eqIe3M8OMGJFtq8uQCoDhALMsyaQZOuBSqPhPHb11Cno3cY1h6Z2ouxvzoR3RUnahaMg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421570,
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAHBweGQ2P5jAqVjrhD3j2VpYSBsQNMjtgclJtLuukIQEPPcRGySeIz2kDVm2SP8jRCX8nFufCJthVONE6eGfiDLhI+EY5AqEGJWLEg4Ss0i2R2FA+h6NBxfmY79eqIe3M8OMGJFtq8uQCoDhALMsyaQZOuBSqPhPHb11Cno3cY1h6Z2ouxvzoR3RUnahaMg=="
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAHBweGQ2P5jAqVjrhD3j2VpYSBsQNMjtgclJtLuukIQEPPcRGySeIz2kDVm2SP8jRCX8nFufCJthVONE6eGfiDLhI+EY5AqEGJWLEg4Ss0i2R2FA+h6NBxfmY79eqIe3M8OMGJFtq8uQCoDhALMsyaQZOuBSqPhPHb11Cno3cY1h6Z2ouxvzoR3RUnahaMg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421569,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
      "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421569,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
      "balance": 69999999999998
    },
    {
      "account": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421568,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421568,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAHBweGQ2P5jAqVjrhD3j2VpYSBsQNMjtgclJtLuukIQEPPcRGySeIz2kDVm2SP8jRCX8nFufCJthVONE6eGfiDLhI+EY5AqEGJWLEg4Ss0i2R2FA+h6NBxfmY79eqIe3M8OMGJFtq8uQCoDhALMsyaQZOuBSqPhPHb11Cno3cY1h6Z2ouxvzoR3RUnahaMg==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDrs/OJZvLQmRTTK4X/A3473wFFi8OKB1TKo4GyaWElPovKCgEAhj+qJSJf/rDvQAGgF0ouZW0JiF0HMMU8R2zQ14W4kEExkAu1y8LRPKIRoJWLygoBAIYkYTnKgAJ+eAWT"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421567,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
      "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421567,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
      "balance": 40000000000002
    },
    {
      "account": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
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
    "from": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
    "to": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
        "from": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
        "to": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
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
    "to": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
        "to": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
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
    "from": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
        "from": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
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
    "from": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
    "to": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiVixIOErNItkdhQPoejQcX5mO/XqiHtzPDjBiRbavLkA6DS8qDI3OxbzcMImR1aku+C070yglAdLLr2azAgES3TUlrLynM=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
          "op": "OffChainTransfer",
          "to": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
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
  "id": -576460752303421566,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECaF34KPQalp9wuu224yZmozrj2nt55Z/xxNyI3l9T+0Lj6CUoVXc0RsjHjrnsSgnzhzV/Kyuzf5DQhAq87u70IuEj4RjkCoQYlYsSDhKzSLZHYUD6Ho0HF+Zjv16oh7czw4wYkW2ry5AOg0vKgyNzsW83DCJkdWpLvgtO9MoJQHSy69mswIBEt01JgS0LL"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421566,
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "signed_tx": "tx_+JALAfhCuECaF34KPQalp9wuu224yZmozrj2nt55Z/xxNyI3l9T+0Lj6CUoVXc0RsjHjrnsSgnzhzV/Kyuzf5DQhAq87u70IuEj4RjkCoQYlYsSDhKzSLZHYUD6Ho0HF+Zjv16oh7czw4wYkW2ry5AOg0vKgyNzsW83DCJkdWpLvgtO9MoJQHSy69mswIBEt01JgS0LL",
      "updates": [
        {
          "amount": 1,
          "from": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
          "op": "OffChainTransfer",
          "to": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
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
  "id": -576460752303421565,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAmhd+Cj0GpafcLrttuMmZqM649p7eeWf8cTciN5fU/tC4+glKFV3NEbIx4657EoJ84c1fysrs3+Q0IQKvO7u9CLhI+EY5AqEGJWLEg4Ss0i2R2FA+h6NBxfmY79eqIe3M8OMGJFtq8uQDoNLyoMjc7FvNwwiZHVqS74LTvTKCUB0suvZrMCARLdNS4gAGIA=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421565,
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAmhd+Cj0GpafcLrttuMmZqM649p7eeWf8cTciN5fU/tC4+glKFV3NEbIx4657EoJ84c1fysrs3+Q0IQKvO7u9CLhI+EY5AqEGJWLEg4Ss0i2R2FA+h6NBxfmY79eqIe3M8OMGJFtq8uQDoNLyoMjc7FvNwwiZHVqS74LTvTKCUB0suvZrMCARLdNS4gAGIA=="
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAmhd+Cj0GpafcLrttuMmZqM649p7eeWf8cTciN5fU/tC4+glKFV3NEbIx4657EoJ84c1fysrs3+Q0IQKvO7u9CLhI+EY5AqEGJWLEg4Ss0i2R2FA+h6NBxfmY79eqIe3M8OMGJFtq8uQDoNLyoMjc7FvNwwiZHVqS74LTvTKCUB0suvZrMCARLdNS4gAGIA=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421564,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
      "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421564,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
      "balance": 40000000000001
    },
    {
      "account": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421563,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421563,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAmhd+Cj0GpafcLrttuMmZqM649p7eeWf8cTciN5fU/tC4+glKFV3NEbIx4657EoJ84c1fysrs3+Q0IQKvO7u9CLhI+EY5AqEGJWLEg4Ss0i2R2FA+h6NBxfmY79eqIe3M8OMGJFtq8uQDoNLyoMjc7FvNwwiZHVqS74LTvTKCUB0suvZrMCARLdNS4gAGIA==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDrs/OJZvLQmRTTK4X/A3473wFFi8OKB1TKo4GyaWElPovKCgEAhj+qJSJf/7DvQAGgF0ouZW0JiF0HMMU8R2zQ14W4kEExkAu1y8LRPKIRoJWLygoBAIYkYTnKgAE7rb7K"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421562,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
      "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421562,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
      "balance": 40000000000001
    },
    {
      "account": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
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
    "from": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
    "to": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
        "from": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
        "to": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
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
    "to": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
        "to": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
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
    "from": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
        "from": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
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
    "from": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
    "to": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiVixIOErNItkdhQPoejQcX5mO/XqiHtzPDjBiRbavLkBKBD96iqYQ6aaeVGz249nXm5cwaKo2P8v7Gf+oJRPf/a5wiUDH8=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
          "op": "OffChainTransfer",
          "to": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
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
  "id": -576460752303421561,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB9aNMyHzvqapbhRS06lQvsiqHuJg/N3Y72p7gaMMU0kn0V8qZEi1KpCRbTsdENisXfXrexgTcVNfLVBnXdEeAIuEj4RjkCoQYlYsSDhKzSLZHYUD6Ho0HF+Zjv16oh7czw4wYkW2ry5ASgQ/eoqmEOmmnlRs9uPZ15uXMGiqNj/L+xn/qCUT3/2udOrK95"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421561,
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB9aNMyHzvqapbhRS06lQvsiqHuJg/N3Y72p7gaMMU0kn0V8qZEi1KpCRbTsdENisXfXrexgTcVNfLVBnXdEeAIuEj4RjkCoQYlYsSDhKzSLZHYUD6Ho0HF+Zjv16oh7czw4wYkW2ry5ASgQ/eoqmEOmmnlRs9uPZ15uXMGiqNj/L+xn/qCUT3/2udOrK95",
      "updates": [
        {
          "amount": 1,
          "from": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
          "op": "OffChainTransfer",
          "to": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
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
  "id": -576460752303421560,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAfWjTMh876mqW4UUtOpUL7Iqh7iYPzd2O9qe4GjDFNJJ9FfKmRItSqQkW07HRDYrF3163sYE3FTXy1QZ13RHgCLhI+EY5AqEGJWLEg4Ss0i2R2FA+h6NBxfmY79eqIe3M8OMGJFtq8uQEoEP3qKphDppp5UbPbj2deblzBoqjY/y/sZ/6glE9/9rnPyWsyw=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421560,
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAfWjTMh876mqW4UUtOpUL7Iqh7iYPzd2O9qe4GjDFNJJ9FfKmRItSqQkW07HRDYrF3163sYE3FTXy1QZ13RHgCLhI+EY5AqEGJWLEg4Ss0i2R2FA+h6NBxfmY79eqIe3M8OMGJFtq8uQEoEP3qKphDppp5UbPbj2deblzBoqjY/y/sZ/6glE9/9rnPyWsyw=="
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAfWjTMh876mqW4UUtOpUL7Iqh7iYPzd2O9qe4GjDFNJJ9FfKmRItSqQkW07HRDYrF3163sYE3FTXy1QZ13RHgCLhI+EY5AqEGJWLEg4Ss0i2R2FA+h6NBxfmY79eqIe3M8OMGJFtq8uQEoEP3qKphDppp5UbPbj2deblzBoqjY/y/sZ/6glE9/9rnPyWsyw=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421559,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
      "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421559,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
      "balance": 40000000000000
    },
    {
      "account": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421558,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421558,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAfWjTMh876mqW4UUtOpUL7Iqh7iYPzd2O9qe4GjDFNJJ9FfKmRItSqQkW07HRDYrF3163sYE3FTXy1QZ13RHgCLhI+EY5AqEGJWLEg4Ss0i2R2FA+h6NBxfmY79eqIe3M8OMGJFtq8uQEoEP3qKphDppp5UbPbj2deblzBoqjY/y/sZ/6glE9/9rnPyWsyw==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDrs/OJZvLQmRTTK4X/A3473wFFi8OKB1TKo4GyaWElPovKCgEAhj+qJSJgALDvQAGgF0ouZW0JiF0HMMU8R2zQ14W4kEExkAu1y8LRPKIRoJWLygoBAIYkYTnKgAA7eL1x"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421557,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
      "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421557,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
      "balance": 70000000000000
    },
    {
      "account": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
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
    "from": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
    "to": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
        "from": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
        "to": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF"
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
    "to": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
        "to": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF"
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
    "from": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
        "from": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
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
    "from": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
    "to": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiVixIOErNItkdhQPoejQcX5mO/XqiHtzPDjBiRbavLkBaDS8qDI3OxbzcMImR1aku+C070yglAdLLr2azAgES3TUgMSxlw=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
          "op": "OffChainTransfer",
          "to": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF"
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
  "id": -576460752303421556,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JkLAcC4lPiSUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQYlYsSDhKzSLZHYUD6Ho0HF+Zjv16oh7czw4wYkW2ry5AWg0vKgyNzsW83DCJkdWpLvgtO9MoJQHSy69mswIBEt01KVn2b7"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421556,
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "signed_tx": "tx_+JkLAcC4lPiSUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4T/hNCwHAuEj4RjkCoQYlYsSDhKzSLZHYUD6Ho0HF+Zjv16oh7czw4wYkW2ry5AWg0vKgyNzsW83DCJkdWpLvgtO9MoJQHSy69mswIBEt01KVn2b7",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
          "op": "OffChainTransfer",
          "to": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF"
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
  "id": -576460752303421555,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhALll07SZcEjb4VeSwHKWWv0t25c33SkrL1hNATtsTNzDmrmeg3kX7/ul9y9IiXsA5wVLAQwCHBn9c6TUP2E12BbhI+EY5AqEGJWLEg4Ss0i2R2FA+h6NBxfmY79eqIe3M8OMGJFtq8uQFoNLyoMjc7FvNwwiZHVqS74LTvTKCUB0suvZrMCARLdNSeqxr3w=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421555,
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhALll07SZcEjb4VeSwHKWWv0t25c33SkrL1hNATtsTNzDmrmeg3kX7/ul9y9IiXsA5wVLAQwCHBn9c6TUP2E12BbhI+EY5AqEGJWLEg4Ss0i2R2FA+h6NBxfmY79eqIe3M8OMGJFtq8uQFoNLyoMjc7FvNwwiZHVqS74LTvTKCUB0suvZrMCARLdNSeqxr3w=="
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhALll07SZcEjb4VeSwHKWWv0t25c33SkrL1hNATtsTNzDmrmeg3kX7/ul9y9IiXsA5wVLAQwCHBn9c6TUP2E12BbhI+EY5AqEGJWLEg4Ss0i2R2FA+h6NBxfmY79eqIe3M8OMGJFtq8uQFoNLyoMjc7FvNwwiZHVqS74LTvTKCUB0suvZrMCARLdNSeqxr3w=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421554,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
      "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421554,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
      "balance": 69999999999999
    },
    {
      "account": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421553,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421553,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhALll07SZcEjb4VeSwHKWWv0t25c33SkrL1hNATtsTNzDmrmeg3kX7/ul9y9IiXsA5wVLAQwCHBn9c6TUP2E12BbhI+EY5AqEGJWLEg4Ss0i2R2FA+h6NBxfmY79eqIe3M8OMGJFtq8uQFoNLyoMjc7FvNwwiZHVqS74LTvTKCUB0suvZrMCARLdNSeqxr3w==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDrs/OJZvLQmRTTK4X/A3473wFFi8OKB1TKo4GyaWElPovKCgEAhj+qJSJf/7DvQAGgF0ouZW0JiF0HMMU8R2zQ14W4kEExkAu1y8LRPKIRoJWLygoBAIYkYTnKgAE7rb7K"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421552,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
      "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421552,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
      "balance": 40000000000001
    },
    {
      "account": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
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
    "from": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
    "to": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
        "from": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
        "to": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
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
    "to": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
        "to": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
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
    "from": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
        "from": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
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
    "from": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
    "to": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBiVixIOErNItkdhQPoejQcX5mO/XqiHtzPDjBiRbavLkBqBD96iqYQ6aaeVGz249nXm5cwaKo2P8v7Gf+oJRPf/a5+b3pZw=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
          "op": "OffChainTransfer",
          "to": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
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
  "id": -576460752303421551,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB3DbX848akCDqsuFCBeNA0NfzAsDiEXqiPy4fKxSTXwaUB8he0zYnbm0+120RR/i5GP2lf6psLQ1pMmw8HGwoAuEj4RjkCoQYlYsSDhKzSLZHYUD6Ho0HF+Zjv16oh7czw4wYkW2ry5AagQ/eoqmEOmmnlRs9uPZ15uXMGiqNj/L+xn/qCUT3/2ucG43QP"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421551,
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB3DbX848akCDqsuFCBeNA0NfzAsDiEXqiPy4fKxSTXwaUB8he0zYnbm0+120RR/i5GP2lf6psLQ1pMmw8HGwoAuEj4RjkCoQYlYsSDhKzSLZHYUD6Ho0HF+Zjv16oh7czw4wYkW2ry5AagQ/eoqmEOmmnlRs9uPZ15uXMGiqNj/L+xn/qCUT3/2ucG43QP",
      "updates": [
        {
          "amount": 1,
          "from": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
          "op": "OffChainTransfer",
          "to": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
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
  "id": -576460752303421550,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NwLAcC41/jVUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAdw21/OPGpAg6rLhQgXjQNDX8wLA4hF6oj8uHysUk18GlAfIXtM2J25tPtdtEUf4uRj9pX+qbC0NaTJsPBxsKALhI+EY5AqEGJWLEg4Ss0i2R2FA+h6NBxfmY79eqIe3M8OMGJFtq8uQGoEP3qKphDppp5UbPbj2deblzBoqjY/y/sZ/6glE9/9rnEoLPog=="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421550,
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAdw21/OPGpAg6rLhQgXjQNDX8wLA4hF6oj8uHysUk18GlAfIXtM2J25tPtdtEUf4uRj9pX+qbC0NaTJsPBxsKALhI+EY5AqEGJWLEg4Ss0i2R2FA+h6NBxfmY79eqIe3M8OMGJFtq8uQGoEP3qKphDppp5UbPbj2deblzBoqjY/y/sZ/6glE9/9rnEoLPog=="
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
    "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
    "data": {
      "state": "tx_+NwLAcC41/jVUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAdw21/OPGpAg6rLhQgXjQNDX8wLA4hF6oj8uHysUk18GlAfIXtM2J25tPtdtEUf4uRj9pX+qbC0NaTJsPBxsKALhI+EY5AqEGJWLEg4Ss0i2R2FA+h6NBxfmY79eqIe3M8OMGJFtq8uQGoEP3qKphDppp5UbPbj2deblzBoqjY/y/sZ/6glE9/9rnEoLPog=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421549,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
      "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421549,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_BFuYYR9XZ4SStWnsN3UFYvhGDEKdcv9s8nJDVXMc4JHqRQQfF",
      "balance": 40000000000000
    },
    {
      "account": "ak_2noiUg9DJRdbH126aDgnoCSemUKSaLvFGVonEkQYPz9PWHUgXP",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421548,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_HTyHK9hRCcTK5vb3SqiqcxarSikjfJJP2nZzAPSr3fsDxzJRz",
  "id": -576460752303421548,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NwLAcC41/jVUQGhAeuz84lm8tCZFNMrhf8DfjvfAUWLw4oHVMqjgbJpYSU+iSsRbPJXCytUAgOHA41+pMaAAIJOIIXo1KUQAAC4kviQCwH4QrhAdw21/OPGpAg6rLhQgXjQNDX8wLA4hF6oj8uHysUk18GlAfIXtM2J25tPtdtEUf4uRj9pX+qbC0NaTJsPBxsKALhI+EY5AqEGJWLEg4Ss0i2R2FA+h6NBxfmY79eqIe3M8OMGJFtq8uQGoEP3qKphDppp5UbPbj2deblzBoqjY/y/sZ/6glE9/9rnEoLPog==",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDrs/OJZvLQmRTTK4X/A3473wFFi8OKB1TKo4GyaWElPovKCgEAhj+qJSJgALDvQAGgF0ouZW0JiF0HMMU8R2zQ14W4kEExkAu1y8LRPKIRoJWLygoBAIYkYTnKgAA7eL1x"
  },
  "version": 1
}
```
