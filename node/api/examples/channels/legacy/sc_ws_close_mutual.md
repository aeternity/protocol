
#### initiator opens a WebSocket connection (2019-03-13 11:13:24.416)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9&role=initiator
```

#### responder opens a WebSocket connection (2019-03-13 11:13:24.438)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9&role=responder
```

#### responder <--- node (2019-03-13 11:13:25.406)
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

#### initiator <--- node (2019-03-13 11:13:25.409)
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

#### initiator <--- node (2019-03-13 11:13:25.435)
```javascript
{
  "action": "sign",
  "channel_id": null,
  "payload": {
    "tx": "tx_+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgKow6pd"
  },
  "tag": "initiator_sign",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:25.529)
```javascript
{
  "action": "initiator_sign",
  "payload": {
    "tx": "tx_+MsLAfhCuEB/CIezz/ej/VJy9Cwezggn6xbh3H28tmQ1C3+qszn1WWJ/8xPGBunYdTYRcADw7FjKplDp8BMq7mU5cJfP7bALuIP4gTIBoQEMHR+jKB9TfmalcAw4HlPfLlTP4fGLC6AeHxDL+MjeeoY/qiUiYAChAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrhiRhOcqAAAIKAIYSMJzlQADAoBVQItrXeXi1NNVLrFNRky7mqhur6CrV3Ihp6ANYAJVSAgvowho="
  }
}
```

#### responder <--- node (2019-03-13 11:13:25.549)
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

#### responder <--- node (2019-03-13 11:13:25.551)
```javascript
{
  "action": "sign",
  "channel_id": null,
  "payload": {
    "tx": "tx_+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgKow6pd"
  },
  "tag": "responder_sign",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:13:25.552)
```javascript
{
  "action": "responder_sign",
  "payload": {
    "tx": "tx_+MsLAfhCuEBYeGQyDYO9NDlf5s9eEXzhcU/tpHUpJpi3mOmmTDGJ4VRgiiHXBTL2LleCKsj8ySdgiiOpuXRL92vT+F+08cgDuIP4gTIBoQEMHR+jKB9TfmalcAw4HlPfLlTP4fGLC6AeHxDL+MjeeoY/qiUiYAChAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrhiRhOcqAAAIKAIYSMJzlQADAoBVQItrXeXi1NNVLrFNRky7mqhur6CrV3Ihp6ANYAJVSAo54uBw="
  }
}
```

#### responder <--- node (2019-03-13 11:13:25.566)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": null,
  "payload": {
    "tx": "tx_+QENCwH4hLhAWHhkMg2DvTQ5X+bPXhF84XFP7aR1KSaYt5jppkwxieFUYIoh1wUy9i5XgirI/MknYIojqbl0S/dr0/hftPHIA7hAfwiHs8/3o/1ScvQsHs4IJ+sW4dx9vLZkNQt/qrM59Vlif/MTxgbp2HU2EXAA8OxYyqZQ6fATKu5lOXCXz+2wC7iD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgLsPDYI"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:25.569)
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

#### initiator <--- node (2019-03-13 11:13:25.570)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": null,
  "payload": {
    "tx": "tx_+QENCwH4hLhAWHhkMg2DvTQ5X+bPXhF84XFP7aR1KSaYt5jppkwxieFUYIoh1wUy9i5XgirI/MknYIojqbl0S/dr0/hftPHIA7hAfwiHs8/3o/1ScvQsHs4IJ+sW4dx9vLZkNQt/qrM59Vlif/MTxgbp2HU2EXAA8OxYyqZQ6fATKu5lOXCXz+2wC7iD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgLsPDYI"
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:27.891)
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

#### initiator <--- node (2019-03-13 11:13:27.898)
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

#### responder <--- node (2019-03-13 11:13:28.293)
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

#### initiator <--- node (2019-03-13 11:13:28.300)
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

#### initiator <--- node (2019-03-13 11:13:28.303)
```javascript
{
  "action": "info",
  "channel_id": "ch_mNHe8bMgHe1DWdty22UdEnUQnVPzHKcXNzcwRBAUh98wY1mQr",
  "payload": {
    "event": "funding_locked"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:28.306)
```javascript
{
  "action": "info",
  "channel_id": "ch_mNHe8bMgHe1DWdty22UdEnUQnVPzHKcXNzcwRBAUh98wY1mQr",
  "payload": {
    "event": "funding_locked"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:28.319)
```javascript
{
  "action": "info",
  "channel_id": "ch_mNHe8bMgHe1DWdty22UdEnUQnVPzHKcXNzcwRBAUh98wY1mQr",
  "payload": {
    "event": "open"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:28.325)
```javascript
{
  "action": "update",
  "channel_id": "ch_mNHe8bMgHe1DWdty22UdEnUQnVPzHKcXNzcwRBAUh98wY1mQr",
  "payload": {
    "state": "tx_+QENCwH4hLhAWHhkMg2DvTQ5X+bPXhF84XFP7aR1KSaYt5jppkwxieFUYIoh1wUy9i5XgirI/MknYIojqbl0S/dr0/hftPHIA7hAfwiHs8/3o/1ScvQsHs4IJ+sW4dx9vLZkNQt/qrM59Vlif/MTxgbp2HU2EXAA8OxYyqZQ6fATKu5lOXCXz+2wC7iD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgLsPDYI"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:28.342)
```javascript
{
  "action": "info",
  "channel_id": "ch_mNHe8bMgHe1DWdty22UdEnUQnVPzHKcXNzcwRBAUh98wY1mQr",
  "payload": {
    "event": "open"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:28.342)
```javascript
{
  "action": "update",
  "channel_id": "ch_mNHe8bMgHe1DWdty22UdEnUQnVPzHKcXNzcwRBAUh98wY1mQr",
  "payload": {
    "state": "tx_+QENCwH4hLhAWHhkMg2DvTQ5X+bPXhF84XFP7aR1KSaYt5jppkwxieFUYIoh1wUy9i5XgirI/MknYIojqbl0S/dr0/hftPHIA7hAfwiHs8/3o/1ScvQsHs4IJ+sW4dx9vLZkNQt/qrM59Vlif/MTxgbp2HU2EXAA8OxYyqZQ6fATKu5lOXCXz+2wC7iD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgLsPDYI"
  },
  "version": 1
}
```

#### initiator: (2019-03-13 11:13:28.422)
> Funding has been confirmed locally on-chain

#### responder: (2019-03-13 11:13:28.422)
> Funding has been confirmed locally on-chain

#### initiator: (2019-03-13 11:13:28.422)
> Funding has been confirmed on-chain by other party

#### responder: (2019-03-13 11:13:28.422)
> Funding has been confirmed on-chain by other party

#### initiator: (2019-03-13 11:13:28.423)
> Channel is `open` and ready to use

#### responder: (2019-03-13 11:13:28.423)
> Channel is `open` and ready to use

#### initiator ---> node (2019-03-13 11:13:28.524)
```javascript
{
  "action": "shutdown"
}
```

#### initiator <--- node (2019-03-13 11:13:28.551)
```javascript
{
  "action": "sign",
  "channel_id": "ch_mNHe8bMgHe1DWdty22UdEnUQnVPzHKcXNzcwRBAUh98wY1mQr",
  "payload": {
    "tx": "tx_+F01AaEGZL2g5H7LgJT5WnluQbTZ02ZoqRBJn02UghDnGigHr3ahAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56hjaR1q+//4YbSOtX4AEAhhIwnOVAAANF0Zy7"
  },
  "tag": "shutdown_sign",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:28.552)
```javascript
{
  "action": "shutdown_sign",
  "payload": {
    "tx": "tx_+KcLAfhCuEA9LJQR1nLWUxBW9jVVtZRl+Mk4JYJdYFUL/lN9vzZGstpphslJ4MoAWsVhyPHxZKJRZtrV/h/8KDE7UGPm4tUOuF/4XTUBoQZkvaDkfsuAlPlaeW5BtNnTZmipEEmfTZSCEOcaKAevdqEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGNpHWr7//hhtI61fgAQCGEjCc5UAAA6UcarU="
  }
}
```

#### responder <--- node (2019-03-13 11:13:28.613)
```javascript
{
  "action": "sign",
  "channel_id": "ch_mNHe8bMgHe1DWdty22UdEnUQnVPzHKcXNzcwRBAUh98wY1mQr",
  "payload": {
    "tx": "tx_+F01AaEGZL2g5H7LgJT5WnluQbTZ02ZoqRBJn02UghDnGigHr3ahAQwdH6MoH1N+ZqVwDDgeU98uVM/h8YsLoB4fEMv4yN56hjaR1q+//4YbSOtX4AEAhhIwnOVAAANF0Zy7"
  },
  "tag": "shutdown_sign_ack",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:13:28.614)
```javascript
{
  "action": "shutdown_sign_ack",
  "payload": {
    "tx": "tx_+KcLAfhCuEB5chq8Ii6kM8ieKXUoXiobHupZy6ATseOhdbe6+EE1xPpwTf4r4R4EtHPPkoO/LozWa84T4B1RvIRO1YKVTjIFuF/4XTUBoQZkvaDkfsuAlPlaeW5BtNnTZmipEEmfTZSCEOcaKAevdqEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGNpHWr7//hhtI61fgAQCGEjCc5UAAA9IzgAE="
  }
}
```

#### responder <--- node (2019-03-13 11:13:28.631)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_mNHe8bMgHe1DWdty22UdEnUQnVPzHKcXNzcwRBAUh98wY1mQr",
  "payload": {
    "tx": "tx_+OkLAfiEuEA9LJQR1nLWUxBW9jVVtZRl+Mk4JYJdYFUL/lN9vzZGstpphslJ4MoAWsVhyPHxZKJRZtrV/h/8KDE7UGPm4tUOuEB5chq8Ii6kM8ieKXUoXiobHupZy6ATseOhdbe6+EE1xPpwTf4r4R4EtHPPkoO/LozWa84T4B1RvIRO1YKVTjIFuF/4XTUBoQZkvaDkfsuAlPlaeW5BtNnTZmipEEmfTZSCEOcaKAevdqEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGNpHWr7//hhtI61fgAQCGEjCc5UAAA+pd34w="
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:28.633)
```javascript
{
  "action": "info",
  "channel_id": "ch_mNHe8bMgHe1DWdty22UdEnUQnVPzHKcXNzcwRBAUh98wY1mQr",
  "payload": {
    "event": "close_mutual"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:28.635)
```javascript
{
  "action": "info",
  "channel_id": "ch_mNHe8bMgHe1DWdty22UdEnUQnVPzHKcXNzcwRBAUh98wY1mQr",
  "payload": {
    "event": "died"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:28.670)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_mNHe8bMgHe1DWdty22UdEnUQnVPzHKcXNzcwRBAUh98wY1mQr",
  "payload": {
    "tx": "tx_+OkLAfiEuEA9LJQR1nLWUxBW9jVVtZRl+Mk4JYJdYFUL/lN9vzZGstpphslJ4MoAWsVhyPHxZKJRZtrV/h/8KDE7UGPm4tUOuEB5chq8Ii6kM8ieKXUoXiobHupZy6ATseOhdbe6+EE1xPpwTf4r4R4EtHPPkoO/LozWa84T4B1RvIRO1YKVTjIFuF/4XTUBoQZkvaDkfsuAlPlaeW5BtNnTZmipEEmfTZSCEOcaKAevdqEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGNpHWr7//hhtI61fgAQCGEjCc5UAAA+pd34w="
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:28.675)
```javascript
{
  "action": "info",
  "channel_id": "ch_mNHe8bMgHe1DWdty22UdEnUQnVPzHKcXNzcwRBAUh98wY1mQr",
  "payload": {
    "event": "close_mutual"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:28.678)
```javascript
{
  "action": "info",
  "channel_id": "ch_mNHe8bMgHe1DWdty22UdEnUQnVPzHKcXNzcwRBAUh98wY1mQr",
  "payload": {
    "event": "died"
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection (2019-03-13 11:13:29.563)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9&role=initiator
```

#### responder opens a WebSocket connection (2019-03-13 11:13:29.587)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_6LRvzWhqyZL2c4Z2Vzocr5SsfcaR3T515Wm34m62u2xsaGMqn&lock_period=10&port=12340&protocol=legacy&push_amount=1&responder_amount=40000000000000&responder_id=ak_2FqziTRw9osxE289AHiNo4s2GN2c8i52RpLaiwTjqCbY5YREq9&role=responder
```

#### responder <--- node (2019-03-13 11:13:30.559)
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

#### initiator <--- node (2019-03-13 11:13:30.562)
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

#### initiator <--- node (2019-03-13 11:13:30.593)
```javascript
{
  "action": "sign",
  "channel_id": null,
  "payload": {
    "tx": "tx_+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgQfJ9FZ"
  },
  "tag": "initiator_sign",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:30.712)
```javascript
{
  "action": "initiator_sign",
  "payload": {
    "tx": "tx_+MsLAfhCuECTDhNVlnaEkuc4qYjl2bFKXCFB6BHjfveygGgV/AhvCrFAQ/P6uKIjFYOcyzyAk+lv+BMFOU7RlO4M3gxK5rIGuIP4gTIBoQEMHR+jKB9TfmalcAw4HlPfLlTP4fGLC6AeHxDL+MjeeoY/qiUiYAChAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrhiRhOcqAAAIKAIYSMJzlQADAoBVQItrXeXi1NNVLrFNRky7mqhur6CrV3Ihp6ANYAJVSBKc/HUw="
  }
}
```

#### responder <--- node (2019-03-13 11:13:30.739)
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

#### responder <--- node (2019-03-13 11:13:30.742)
```javascript
{
  "action": "sign",
  "channel_id": null,
  "payload": {
    "tx": "tx_+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgQfJ9FZ"
  },
  "tag": "responder_sign",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:13:30.744)
```javascript
{
  "action": "responder_sign",
  "payload": {
    "tx": "tx_+MsLAfhCuEBJ8cJt2E1g2G+1yxwVIqPi7CMVuX1pjPtESMyn0KmPppnuNNYo6XWz8mfWxjZrqH+T31TXeItq3EvrL2v0wc8OuIP4gTIBoQEMHR+jKB9TfmalcAw4HlPfLlTP4fGLC6AeHxDL+MjeeoY/qiUiYAChAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrhiRhOcqAAAIKAIYSMJzlQADAoBVQItrXeXi1NNVLrFNRky7mqhur6CrV3Ihp6ANYAJVSBMT2isA="
  }
}
```

#### responder <--- node (2019-03-13 11:13:30.781)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": null,
  "payload": {
    "tx": "tx_+QENCwH4hLhASfHCbdhNYNhvtcscFSKj4uwjFbl9aYz7REjMp9Cpj6aZ7jTWKOl1s/Jn1sY2a6h/k99U13iLatxL6y9r9MHPDrhAkw4TVZZ2hJLnOKmI5dmxSlwhQegR4373soBoFfwIbwqxQEPz+riiIxWDnMs8gJPpb/gTBTlO0ZTuDN4MSuayBriD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgSigFmg"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:30.783)
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

#### initiator <--- node (2019-03-13 11:13:30.784)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": null,
  "payload": {
    "tx": "tx_+QENCwH4hLhASfHCbdhNYNhvtcscFSKj4uwjFbl9aYz7REjMp9Cpj6aZ7jTWKOl1s/Jn1sY2a6h/k99U13iLatxL6y9r9MHPDrhAkw4TVZZ2hJLnOKmI5dmxSlwhQegR4373soBoFfwIbwqxQEPz+riiIxWDnMs8gJPpb/gTBTlO0ZTuDN4MSuayBriD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgSigFmg"
  },
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:31.855)
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

#### initiator <--- node (2019-03-13 11:13:31.863)
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

#### initiator <--- node (2019-03-13 11:13:35.666)
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

#### responder <--- node (2019-03-13 11:13:35.668)
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

#### responder <--- node (2019-03-13 11:13:35.672)
```javascript
{
  "action": "info",
  "channel_id": "ch_2JSs8UBgx7npzGuxNdyzTjciijUafrbUrU8SEi2zxLPP49uw8",
  "payload": {
    "event": "funding_locked"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:35.678)
```javascript
{
  "action": "info",
  "channel_id": "ch_2JSs8UBgx7npzGuxNdyzTjciijUafrbUrU8SEi2zxLPP49uw8",
  "payload": {
    "event": "funding_locked"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:35.700)
```javascript
{
  "action": "info",
  "channel_id": "ch_2JSs8UBgx7npzGuxNdyzTjciijUafrbUrU8SEi2zxLPP49uw8",
  "payload": {
    "event": "open"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:35.708)
```javascript
{
  "action": "info",
  "channel_id": "ch_2JSs8UBgx7npzGuxNdyzTjciijUafrbUrU8SEi2zxLPP49uw8",
  "payload": {
    "event": "open"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:35.709)
```javascript
{
  "action": "update",
  "channel_id": "ch_2JSs8UBgx7npzGuxNdyzTjciijUafrbUrU8SEi2zxLPP49uw8",
  "payload": {
    "state": "tx_+QENCwH4hLhASfHCbdhNYNhvtcscFSKj4uwjFbl9aYz7REjMp9Cpj6aZ7jTWKOl1s/Jn1sY2a6h/k99U13iLatxL6y9r9MHPDrhAkw4TVZZ2hJLnOKmI5dmxSlwhQegR4373soBoFfwIbwqxQEPz+riiIxWDnMs8gJPpb/gTBTlO0ZTuDN4MSuayBriD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgSigFmg"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:35.710)
```javascript
{
  "action": "update",
  "channel_id": "ch_2JSs8UBgx7npzGuxNdyzTjciijUafrbUrU8SEi2zxLPP49uw8",
  "payload": {
    "state": "tx_+QENCwH4hLhASfHCbdhNYNhvtcscFSKj4uwjFbl9aYz7REjMp9Cpj6aZ7jTWKOl1s/Jn1sY2a6h/k99U13iLatxL6y9r9MHPDrhAkw4TVZZ2hJLnOKmI5dmxSlwhQegR4373soBoFfwIbwqxQEPz+riiIxWDnMs8gJPpb/gTBTlO0ZTuDN4MSuayBriD+IEyAaEBDB0foygfU35mpXAMOB5T3y5Uz+HxiwugHh8Qy/jI3nqGP6olImAAoQGlZyRxc6JXyoCZ1k5JANokwX6uj8/EZxGEGyc8x2MXK4YkYTnKgAACCgCGEjCc5UAAwKAVUCLa13l4tTTVS6xTUZMu5qobq+gq1dyIaegDWACVUgSigFmg"
  },
  "version": 1
}
```

#### initiator: (2019-03-13 11:13:36.440)
> Funding has been confirmed locally on-chain

#### responder: (2019-03-13 11:13:36.440)
> Funding has been confirmed locally on-chain

#### initiator: (2019-03-13 11:13:36.440)
> Funding has been confirmed on-chain by other party

#### responder: (2019-03-13 11:13:36.440)
> Funding has been confirmed on-chain by other party

#### initiator: (2019-03-13 11:13:36.440)
> Channel is `open` and ready to use

#### responder: (2019-03-13 11:13:36.440)
> Channel is `open` and ready to use

#### responder ---> node (2019-03-13 11:13:36.541)
```javascript
{
  "action": "shutdown"
}
```

#### responder <--- node (2019-03-13 11:13:36.555)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2JSs8UBgx7npzGuxNdyzTjciijUafrbUrU8SEi2zxLPP49uw8",
  "payload": {
    "tx": "tx_+F01AaEGAvQfnMTUtwoV9/wqI+mNjhkpizkFXJmHot9R7kmO8dShAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrhjaR1q+//4YbSOtX4AEAhhIwnOVAAAFEQl2g"
  },
  "tag": "shutdown_sign",
  "version": 1
}
```

#### responder ---> node (2019-03-13 11:13:36.556)
```javascript
{
  "action": "shutdown_sign",
  "payload": {
    "tx": "tx_+KcLAfhCuECR2oyFsd7AbG2NPlKuijrRKQnR65U8j131k17Z2vcohp1Mtz1/a59A1aiW8xr16zRvEbaWw0tY+8PfqiNhj/8FuF/4XTUBoQYC9B+cxNS3ChX3/Coj6Y2OGSmLOQVcmYei31HuSY7x1KEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuGNpHWr7//hhtI61fgAQCGEjCc5UAAASiK33E="
  }
}
```

#### initiator <--- node (2019-03-13 11:13:36.601)
```javascript
{
  "action": "sign",
  "channel_id": "ch_2JSs8UBgx7npzGuxNdyzTjciijUafrbUrU8SEi2zxLPP49uw8",
  "payload": {
    "tx": "tx_+F01AaEGAvQfnMTUtwoV9/wqI+mNjhkpizkFXJmHot9R7kmO8dShAaVnJHFzolfKgJnWTkkA2iTBfq6Pz8RnEYQbJzzHYxcrhjaR1q+//4YbSOtX4AEAhhIwnOVAAAFEQl2g"
  },
  "tag": "shutdown_sign_ack",
  "version": 1
}
```

#### initiator ---> node (2019-03-13 11:13:36.602)
```javascript
{
  "action": "shutdown_sign_ack",
  "payload": {
    "tx": "tx_+KcLAfhCuECZ62Isy9PCsG0RD2V2rPS1oy7787NMqiD6nGxETqlspVzS6/zsXFoxYTn11tK34W7DQfMqS85N5S3OnxvnGdYNuF/4XTUBoQYC9B+cxNS3ChX3/Coj6Y2OGSmLOQVcmYei31HuSY7x1KEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuGNpHWr7//hhtI61fgAQCGEjCc5UAAARwgfkw="
  }
}
```

#### initiator <--- node (2019-03-13 11:13:36.619)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_2JSs8UBgx7npzGuxNdyzTjciijUafrbUrU8SEi2zxLPP49uw8",
  "payload": {
    "tx": "tx_+OkLAfiEuECR2oyFsd7AbG2NPlKuijrRKQnR65U8j131k17Z2vcohp1Mtz1/a59A1aiW8xr16zRvEbaWw0tY+8PfqiNhj/8FuECZ62Isy9PCsG0RD2V2rPS1oy7787NMqiD6nGxETqlspVzS6/zsXFoxYTn11tK34W7DQfMqS85N5S3OnxvnGdYNuF/4XTUBoQYC9B+cxNS3ChX3/Coj6Y2OGSmLOQVcmYei31HuSY7x1KEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuGNpHWr7//hhtI61fgAQCGEjCc5UAAAe9bZGc="
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:36.625)
```javascript
{
  "action": "info",
  "channel_id": "ch_2JSs8UBgx7npzGuxNdyzTjciijUafrbUrU8SEi2zxLPP49uw8",
  "payload": {
    "event": "close_mutual"
  },
  "version": 1
}
```

#### initiator <--- node (2019-03-13 11:13:36.629)
```javascript
{
  "action": "info",
  "channel_id": "ch_2JSs8UBgx7npzGuxNdyzTjciijUafrbUrU8SEi2zxLPP49uw8",
  "payload": {
    "event": "died"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:36.670)
```javascript
{
  "action": "on_chain_tx",
  "channel_id": "ch_2JSs8UBgx7npzGuxNdyzTjciijUafrbUrU8SEi2zxLPP49uw8",
  "payload": {
    "tx": "tx_+OkLAfiEuECR2oyFsd7AbG2NPlKuijrRKQnR65U8j131k17Z2vcohp1Mtz1/a59A1aiW8xr16zRvEbaWw0tY+8PfqiNhj/8FuECZ62Isy9PCsG0RD2V2rPS1oy7787NMqiD6nGxETqlspVzS6/zsXFoxYTn11tK34W7DQfMqS85N5S3OnxvnGdYNuF/4XTUBoQYC9B+cxNS3ChX3/Coj6Y2OGSmLOQVcmYei31HuSY7x1KEBpWckcXOiV8qAmdZOSQDaJMF+ro/PxGcRhBsnPMdjFyuGNpHWr7//hhtI61fgAQCGEjCc5UAAAe9bZGc="
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:36.674)
```javascript
{
  "action": "info",
  "channel_id": "ch_2JSs8UBgx7npzGuxNdyzTjciijUafrbUrU8SEi2zxLPP49uw8",
  "payload": {
    "event": "close_mutual"
  },
  "version": 1
}
```

#### responder <--- node (2019-03-13 11:13:36.675)
```javascript
{
  "action": "info",
  "channel_id": "ch_2JSs8UBgx7npzGuxNdyzTjciijUafrbUrU8SEi2zxLPP49uw8",
  "payload": {
    "event": "died"
  },
  "version": 1
}
```
