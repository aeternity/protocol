
#### initiator init (2018-10-16 17:14:04.913)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb&role=initiator
```

#### responder init (2018-10-16 17:14:04.917)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb&role=responder
```

#### responder <--- (2018-10-16 17:14:05.919)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 17:14:05.922)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 17:14:05.930)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpALGJSrzwTy6oub8Qv4su7RMx2hck9JNUEgjtyU6qrUG48oB7x4ucqxPokv4rA4P5zaAWfi6eCujMzNBvMMu3xP8p9Svn5xM77VDy3ntvSFDRTNLxquqDLKr53dA7VoLQyju8FB1sKcPCeRhzzU2bUngSwEuRt81"
  }
}
```

#### initiator ---> (2018-10-16 17:14:05.966)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HmdoADdRjW9f3KS9Uww4VsigbzGDC2c2TQm3gX8MWDkwvbKyFKZppU1bEo91K8XS9FSz9VEEweiMpP8jVTFzeDMuRprtWWf4tyhYP5ZtRVhDQwReknwhhq2UB4KN1io5PrTBqfnpgbkLgeUweXJqaXmqpzfQoAke6UyR53eyTwxF4mA2rwnDVbJMZpXuBKofrYDPfPLGXRphjRF6xsnsbc6yVwVrCxRNhvdxhksShohHStvUJAp6WiLZFTCZMpuhT"
  }
}
```

#### responder <--- (2018-10-16 17:14:05.968)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 17:14:05.968)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpALGJSrzwTy6oub8Qv4su7RMx2hck9JNUEgjtyU6qrUG48oB7x4ucqxPokv4rA4P5zaAWfi6eCujMzNBvMMu3xP8p9Svn5xM77VDy3ntvSFDRTNLxquqDLKr53dA7VoLQyju8FB1sKcPCeRhzzU2bUngSwEuRt81"
  }
}
```

#### responder ---> (2018-10-16 17:14:05.969)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HkpV8KEdAzRi2kCLQotPhyJ9QgJHkcfD6tD8B1uxqprXRmakogUm6WopBX8z7oQHHWLk9GTd4GUAkm4L3BuogpHEcZNejRWPTX3PkHwmMEjygKApNucaEoHVTQs6wpxCQ5AHDMdLUWFABzkEMvpQvqPv4yuekY9nfK6S7pXGcQ55djvDm2j4Puzh7saCSSCPzsp1aG1FYAeb5E4ew7PDvBWPnobboMJcwH58MjNSbz8QFapqz5PaFajf6M1JmSZX9"
  }
}
```

#### initiator <--- (2018-10-16 17:14:05.970)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 17:14:05.971)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmPcdjG1Yd44b7peqPkv1MvUd9bLjcsMRts8F1c95ExCeymMcQxFssD8ksNVb72hyK6wTxiXrQnwsxM2v2nzEoJ6ZD1yinfAj4UJS9rgNNYUhfBHJrnj2zrde9iyhC6VG1ApMeGQ1dUVCZk9a4LeuN4PiTmzxR4iy9SL3oQV87aF93i9tsW1iTNe6xoVPBzqSsgoo6hdUeuMky4R9gcDqQuqYiNkpwxMaE53pXytqs4CT1yQz5Z7fZpjUXAz2QQAfnMEE6U8asg1nm94b3hZ56EahDpxbLa6BN4xj2hJ1EEHvjByyJ2khBJJhTSmz2HzfKDkTEQAmJRKzTdCggVbCjrtA8Wd"
  }
}
```

#### initiator <--- (2018-10-16 17:14:05.972)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmPcdjG1Yd44b7peqPkv1MvUd9bLjcsMRts8F1c95ExCeymMcQxFssD8ksNVb72hyK6wTxiXrQnwsxM2v2nzEoJ6ZD1yinfAj4UJS9rgNNYUhfBHJrnj2zrde9iyhC6VG1ApMeGQ1dUVCZk9a4LeuN4PiTmzxR4iy9SL3oQV87aF93i9tsW1iTNe6xoVPBzqSsgoo6hdUeuMky4R9gcDqQuqYiNkpwxMaE53pXytqs4CT1yQz5Z7fZpjUXAz2QQAfnMEE6U8asg1nm94b3hZ56EahDpxbLa6BN4xj2hJ1EEHvjByyJ2khBJJhTSmz2HzfKDkTEQAmJRKzTdCggVbCjrtA8Wd"
  }
}
```

#### initiator <--- (2018-10-16 17:14:07.239)
```javascript
{
  "id": -576460752303423452,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 699
    },
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 401
    }
  ]
}
```

#### initiator <--- (2018-10-16 17:14:08.831)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### responder <--- (2018-10-16 17:14:08.832)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### initiator <--- (2018-10-16 17:14:08.832)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### responder <--- (2018-10-16 17:14:08.832)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### initiator <--- (2018-10-16 17:14:08.837)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### responder <--- (2018-10-16 17:14:08.838)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### initiator <--- (2018-10-16 17:14:08.839)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmPcdjG1Yd44b7peqPkv1MvUd9bLjcsMRts8F1c95ExCeymMcQxFssD8ksNVb72hyK6wTxiXrQnwsxM2v2nzEoJ6ZD1yinfAj4UJS9rgNNYUhfBHJrnj2zrde9iyhC6VG1ApMeGQ1dUVCZk9a4LeuN4PiTmzxR4iy9SL3oQV87aF93i9tsW1iTNe6xoVPBzqSsgoo6hdUeuMky4R9gcDqQuqYiNkpwxMaE53pXytqs4CT1yQz5Z7fZpjUXAz2QQAfnMEE6U8asg1nm94b3hZ56EahDpxbLa6BN4xj2hJ1EEHvjByyJ2khBJJhTSmz2HzfKDkTEQAmJRKzTdCggVbCjrtA8Wd",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### responder <--- (2018-10-16 17:14:08.839)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmPcdjG1Yd44b7peqPkv1MvUd9bLjcsMRts8F1c95ExCeymMcQxFssD8ksNVb72hyK6wTxiXrQnwsxM2v2nzEoJ6ZD1yinfAj4UJS9rgNNYUhfBHJrnj2zrde9iyhC6VG1ApMeGQ1dUVCZk9a4LeuN4PiTmzxR4iy9SL3oQV87aF93i9tsW1iTNe6xoVPBzqSsgoo6hdUeuMky4R9gcDqQuqYiNkpwxMaE53pXytqs4CT1yQz5Z7fZpjUXAz2QQAfnMEE6U8asg1nm94b3hZ56EahDpxbLa6BN4xj2hJ1EEHvjByyJ2khBJJhTSmz2HzfKDkTEQAmJRKzTdCggVbCjrtA8Wd",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

##### initiator: (2018-10-16 17:14:10.0)
> Funding has been confirmed locally on-chain

##### responder: (2018-10-16 17:14:10.0)
> Funding has been confirmed locally on-chain

##### initiator: (2018-10-16 17:14:10.0)
> Funding has been confirmed on-chain by other party

##### responder: (2018-10-16 17:14:10.0)
> Funding has been confirmed on-chain by other party

##### initiator: (2018-10-16 17:14:10.0)
> Channel is `open` and ready to use

##### responder: (2018-10-16 17:14:10.0)
> Channel is `open` and ready to use

#### initiator ---> (2018-10-16 17:14:10.40)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {}
}
```

#### responder <--- (2018-10-16 17:14:10.47)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "state": "tx_6jPYBUFTkcmPcdjG1Yd44b7peqPkv1MvUd9bLjcsMRts8F1c95ExCeymMcQxFssD8ksNVb72hyK6wTxiXrQnwsxM2v2nzEoJ6ZD1yinfAj4UJS9rgNNYUhfBHJrnj2zrde9iyhC6VG1ApMeGQ1dUVCZk9a4LeuN4PiTmzxR4iy9SL3oQV87aF93i9tsW1iTNe6xoVPBzqSsgoo6hdUeuMky4R9gcDqQuqYiNkpwxMaE53pXytqs4CT1yQz5Z7fZpjUXAz2QQAfnMEE6U8asg1nm94b3hZ56EahDpxbLa6BN4xj2hJ1EEHvjByyJ2khBJJhTSmz2HzfKDkTEQAmJRKzTdCggVbCjrtA8Wd",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### responder <--- (2018-10-16 17:14:10.48)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.48)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "state": "tx_6jPYBUFTkcmPcdjG1Yd44b7peqPkv1MvUd9bLjcsMRts8F1c95ExCeymMcQxFssD8ksNVb72hyK6wTxiXrQnwsxM2v2nzEoJ6ZD1yinfAj4UJS9rgNNYUhfBHJrnj2zrde9iyhC6VG1ApMeGQ1dUVCZk9a4LeuN4PiTmzxR4iy9SL3oQV87aF93i9tsW1iTNe6xoVPBzqSsgoo6hdUeuMky4R9gcDqQuqYiNkpwxMaE53pXytqs4CT1yQz5Z7fZpjUXAz2QQAfnMEE6U8asg1nm94b3hZ56EahDpxbLa6BN4xj2hJ1EEHvjByyJ2khBJJhTSmz2HzfKDkTEQAmJRKzTdCggVbCjrtA8Wd",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.49)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### responder init (2018-10-16 17:14:10.101)
```
ws://localhost:3014/channel?channel_reserve=2&existing_channel_id=ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E&initiator_amount=700&initiator_id=ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7&lock_period=10&offchain_tx=tx_6jPYBUFTkcmPcdjG1Yd44b7peqPkv1MvUd9bLjcsMRts8F1c95ExCeymMcQxFssD8ksNVb72hyK6wTxiXrQnwsxM2v2nzEoJ6ZD1yinfAj4UJS9rgNNYUhfBHJrnj2zrde9iyhC6VG1ApMeGQ1dUVCZk9a4LeuN4PiTmzxR4iy9SL3oQV87aF93i9tsW1iTNe6xoVPBzqSsgoo6hdUeuMky4R9gcDqQuqYiNkpwxMaE53pXytqs4CT1yQz5Z7fZpjUXAz2QQAfnMEE6U8asg1nm94b3hZ56EahDpxbLa6BN4xj2hJ1EEHvjByyJ2khBJJhTSmz2HzfKDkTEQAmJRKzTdCggVbCjrtA8Wd&port=12341&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb&role=responder
```

#### initiator init (2018-10-16 17:14:10.107)
```
ws://localhost:3014/channel?channel_reserve=2&existing_channel_id=ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E&host=localhost&initiator_amount=700&initiator_id=ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7&lock_period=10&offchain_tx=tx_6jPYBUFTkcmPcdjG1Yd44b7peqPkv1MvUd9bLjcsMRts8F1c95ExCeymMcQxFssD8ksNVb72hyK6wTxiXrQnwsxM2v2nzEoJ6ZD1yinfAj4UJS9rgNNYUhfBHJrnj2zrde9iyhC6VG1ApMeGQ1dUVCZk9a4LeuN4PiTmzxR4iy9SL3oQV87aF93i9tsW1iTNe6xoVPBzqSsgoo6hdUeuMky4R9gcDqQuqYiNkpwxMaE53pXytqs4CT1yQz5Z7fZpjUXAz2QQAfnMEE6U8asg1nm94b3hZ56EahDpxbLa6BN4xj2hJ1EEHvjByyJ2khBJJhTSmz2HzfKDkTEQAmJRKzTdCggVbCjrtA8Wd&port=12341&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb&role=initiator
```

#### responder <--- (2018-10-16 17:14:10.110)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_reestablished",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### responder <--- (2018-10-16 17:14:10.110)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.112)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_reestablished",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.112)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### responder <--- (2018-10-16 17:14:10.113)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmPcdjG1Yd44b7peqPkv1MvUd9bLjcsMRts8F1c95ExCeymMcQxFssD8ksNVb72hyK6wTxiXrQnwsxM2v2nzEoJ6ZD1yinfAj4UJS9rgNNYUhfBHJrnj2zrde9iyhC6VG1ApMeGQ1dUVCZk9a4LeuN4PiTmzxR4iy9SL3oQV87aF93i9tsW1iTNe6xoVPBzqSsgoo6hdUeuMky4R9gcDqQuqYiNkpwxMaE53pXytqs4CT1yQz5Z7fZpjUXAz2QQAfnMEE6U8asg1nm94b3hZ56EahDpxbLa6BN4xj2hJ1EEHvjByyJ2khBJJhTSmz2HzfKDkTEQAmJRKzTdCggVbCjrtA8Wd",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.114)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmPcdjG1Yd44b7peqPkv1MvUd9bLjcsMRts8F1c95ExCeymMcQxFssD8ksNVb72hyK6wTxiXrQnwsxM2v2nzEoJ6ZD1yinfAj4UJS9rgNNYUhfBHJrnj2zrde9iyhC6VG1ApMeGQ1dUVCZk9a4LeuN4PiTmzxR4iy9SL3oQV87aF93i9tsW1iTNe6xoVPBzqSsgoo6hdUeuMky4R9gcDqQuqYiNkpwxMaE53pXytqs4CT1yQz5Z7fZpjUXAz2QQAfnMEE6U8asg1nm94b3hZ56EahDpxbLa6BN4xj2hJ1EEHvjByyJ2khBJJhTSmz2HzfKDkTEQAmJRKzTdCggVbCjrtA8Wd",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.157)
```javascript
{
  "id": -576460752303423451,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 699
    },
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 401
    }
  ]
}
```

#### initiator ---> (2018-10-16 17:14:10.157)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
    "to": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.163)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQR9Kv12wCnYA6wpQGhPJgLa2YeVHAq4YVu48yReSV4wRiefwA1HypiapY2iV467w11Vucq7NRMrN3MZ4hE82SpXfwRkeEjMPPzLwbdzncGmJDgvT7c2d89KaXZYqMXNocvKZp5MVDuo8kemwKSsPY3jF3sWvYJRf6uGiAy4jbMm6XCfwpTYkgtSoRQu4WzMch2K1hCp72va8y"
  }
}
```

#### initiator ---> (2018-10-16 17:14:10.165)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4kYXWzUTLEBsyy2Vm6uFxSANeDD2mCkkn9BCxioxNATk56HTkhqnWECYH7KfDtG1HfP3C5vuwH4SSjsD72wiQQL3b7xRNueKvdhCVr2onvZgmELwZYDXZcS7L9u1zGPQYdNDkZRdJMz1uwLKcdufd4WGRm7eaRw3EnpyGyezCwpWQiE8fopk1x73o4o5uDNrGbQ8EPuSZRVCzX6VzhnirTbnGbVeYxXLn9X1ptcT6RNLqRV7Zu3qxC2zcySgBN7h5RvxUmjy8VZwRbWGMvKKHUjbhajJQk29jKw1QxxtsbSSPGV"
  }
}
```

#### responder <--- (2018-10-16 17:14:10.170)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### responder <--- (2018-10-16 17:14:10.170)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQR9Kv12wCnYA6wpQGhPJgLa2YeVHAq4YVu48yReSV4wRiefwA1HypiapY2iV467w11Vucq7NRMrN3MZ4hE82SpXfwRkeEjMPPzLwbdzncGmJDgvT7c2d89KaXZYqMXNocvKZp5MVDuo8kemwKSsPY3jF3sWvYJRf6uGiAy4jbMm6XCfwpTYkgtSoRQu4WzMch2K1hCp72va8y"
  }
}
```

#### responder ---> (2018-10-16 17:14:10.171)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak55y6VpKNDBFZYQe8vAFFTf4m7KvhF6CqFiHNsta4C5xBUcd7AAPyfjKTQxeTGTajbieryfxaRRjwmcQ9bbbQLTuueA8WRTD2cfkWkSpWfT1myomPx7zmvGjvpqr8t24RnnbXq4cPDiuiu561341U6XRTocmojHRQjAX1vjpnX3nNRUjJ8eTekZ7fwAGmQ6dT946vJM61zgY3wgnizK4VzFjuHr1XHYfBoZhB9iRTWaTHbB6PqVuJMxdUJcqP3L1PPVnskX9ExrT8YGyju7gNydofGukXkMEXcZLmXoJXCJeRjME"
  }
}
```

#### responder <--- (2018-10-16 17:14:10.176)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkKRSRso7dVNTqRNgN4BWw2fs6cseiPbiH47Q5wpPGS1nYmPL3zwwjmmb7gmYMqN8VW3s9vw5NZHM4LxJfBHYM69P1gL9nASwZe3kYuw7qsEL5pBF8GgEMBLUktHxeRmhuo6Aa2xB3tWdBfZapsTa5cEsHkV5WDuNPTb6DKXHdp51G6Fyik8qmtPckmGKxCCwHDqMD5zV7487VbNc3rvVnT5CSZ7aFfw2qjVEnHLK2SX8HT7hnLiXjHbSVWYTVcb8nXNdeuim6Bw1XbM1GpM5u6MH7oTXEbLs9z7JYwqLPXWg2VFwnPAjDSjCc653M6eSvgwG6RPW2UbV81C6nJ83x2jYxeTWFFAbDpfE455kR5d59A3xbX7arp47cgN3ygfE51h8XuXmH",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.176)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkKRSRso7dVNTqRNgN4BWw2fs6cseiPbiH47Q5wpPGS1nYmPL3zwwjmmb7gmYMqN8VW3s9vw5NZHM4LxJfBHYM69P1gL9nASwZe3kYuw7qsEL5pBF8GgEMBLUktHxeRmhuo6Aa2xB3tWdBfZapsTa5cEsHkV5WDuNPTb6DKXHdp51G6Fyik8qmtPckmGKxCCwHDqMD5zV7487VbNc3rvVnT5CSZ7aFfw2qjVEnHLK2SX8HT7hnLiXjHbSVWYTVcb8nXNdeuim6Bw1XbM1GpM5u6MH7oTXEbLs9z7JYwqLPXWg2VFwnPAjDSjCc653M6eSvgwG6RPW2UbV81C6nJ83x2jYxeTWFFAbDpfE455kR5d59A3xbX7arp47cgN3ygfE51h8XuXmH",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.181)
```javascript
{
  "id": -576460752303423450,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 698
    },
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 402
    }
  ]
}
```

#### initiator <--- (2018-10-16 17:14:10.182)
```javascript
{
  "id": -576460752303423449,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 402
    },
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 698
    }
  ]
}
```

#### responder ---> (2018-10-16 17:14:10.182)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
    "to": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7"
  }
}
```

#### responder <--- (2018-10-16 17:14:10.186)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQR9Kv12wCnYA6wpQGhPJgLa2YeVHAq4YVu48yReSV4wRiemMfrqXHuvYTni2AzFcLTYvPvZiFdA1erS5iKiJMg4QZYSaorUNhmV98xrMJcuvAomoTKH4n4Pk3jPM2MncVSRpkC6PLPLKMPMW5rEWHUq5RVTs3fQhQqrQCVWcCG5fZkDjhgDDb1PRSvFMuGtnqUDjiQr9xGTSk"
  }
}
```

#### responder ---> (2018-10-16 17:14:10.187)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak5BkX4U5FTFy3zx4bmHZiAigPpnz3rdt97ifktwTumNNvDxpezHnRB2TaPVBRWmfgUYxw3DP3U9YAcrv6KV5ngYKS2H4688vkDAye6WZPzA6aZadmEf2vuNS582thbMb1eEFmi9D1XLpkLyTcsPuP2xuvsViLSKLzNTYGfvSoXpaPsarSRXbZvSoVEqADCqxRGadowk8oa3HeAss8Tv117t6jWxvN4Utw52FPUp856AjEXfCnDgL74i535ZTsfF7Cjt7YDv8arAiZ7FCecs2RLDWgyXsbvYSs8aKQQYfKcd5bFJX"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.192)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.192)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQR9Kv12wCnYA6wpQGhPJgLa2YeVHAq4YVu48yReSV4wRiemMfrqXHuvYTni2AzFcLTYvPvZiFdA1erS5iKiJMg4QZYSaorUNhmV98xrMJcuvAomoTKH4n4Pk3jPM2MncVSRpkC6PLPLKMPMW5rEWHUq5RVTs3fQhQqrQCVWcCG5fZkDjhgDDb1PRSvFMuGtnqUDjiQr9xGTSk"
  }
}
```

#### initiator ---> (2018-10-16 17:14:10.193)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak54SY2b4Z8BLjShcaZ3TtKJrbPSUS1L1WBUgMn9R6N4BkHp1EtFTMtXGegAtPvkWmNtwoCdTemENZeY8UGMC158qZ8v62dr6ce3i8N4drDMzhbUutCSrT6M2wQZVCPbCYXyUvEe9aHQU4cZ22WPiVjwD9RkeWDeVpsPAxxEFRFUo2NrNK3qW4JaN5eyyE5Ki1UTX6ApcfNyN1V4K41tYmcJGjk4ARjWVnqWo8CGyaL6wuUgrqpZJXy7b2shHjZwegGoNWyx3mXEAxv2e1uHCSMu5sDafMMpYtq5uN5wtNSiYGDXj"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.198)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkrBx6CFuw6iywrnuCuAprb9YdDKN4QvBZ6yZpbQwoPbKE81jofuhvDtrz5CrwRu3PgGNywvs7N3wK8kVM5M7ugxdYDEuZprsmbyx7rFu4My1k7QMFcNQifTPvBJokG2Nq91ocRqDvYwzc2EAwHbjzZkjvWGhkakbKdWtjRiLPidNxpKrgNt3H2At9hWn5135bw89L55MDiPaGqZgH6549d3yN48uqsitkB7aNdvXF1DM6vUgksBcsbChijkVKJucgZJEYpxQiE2mCwfH7bRufzNCrNQ8UcPZuaFXx6t6UyFDGTHF9XDkSkaaLbkh1M4yHwwKDq77JxWZJeGN4vann4Hv3q1XkBBdYbcM3W1AqwDBWhKgJ6EaE2TPHR3k1pyt6FG5wsDZi",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### responder <--- (2018-10-16 17:14:10.198)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkrBx6CFuw6iywrnuCuAprb9YdDKN4QvBZ6yZpbQwoPbKE81jofuhvDtrz5CrwRu3PgGNywvs7N3wK8kVM5M7ugxdYDEuZprsmbyx7rFu4My1k7QMFcNQifTPvBJokG2Nq91ocRqDvYwzc2EAwHbjzZkjvWGhkakbKdWtjRiLPidNxpKrgNt3H2At9hWn5135bw89L55MDiPaGqZgH6549d3yN48uqsitkB7aNdvXF1DM6vUgksBcsbChijkVKJucgZJEYpxQiE2mCwfH7bRufzNCrNQ8UcPZuaFXx6t6UyFDGTHF9XDkSkaaLbkh1M4yHwwKDq77JxWZJeGN4vann4Hv3q1XkBBdYbcM3W1AqwDBWhKgJ6EaE2TPHR3k1pyt6FG5wsDZi",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.202)
```javascript
{
  "id": -576460752303423448,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 401
    },
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 699
    }
  ]
}
```

#### initiator <--- (2018-10-16 17:14:10.204)
```javascript
{
  "id": -576460752303423447,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 401
    },
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 699
    }
  ]
}
```

#### responder ---> (2018-10-16 17:14:10.204)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
    "to": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7"
  }
}
```

#### responder <--- (2018-10-16 17:14:10.208)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQR9Kv12wCnYA6wpQGhPJgLa2YeVHAq4YVu48yReSV4wRiernBiP4m7GGPYhZHtNTLErT8V1HKbqunGUyLFC43Qp1b2hzvXKjxRRtJ4J46Mh1GVQm5pLPCweMz1ovj53V9NRx4R3FFxu2m4izLEbThyRLfo8QtN9yjdFAY8j4qp2raCBkGvmLuMFfMA13X57v5uTEd9nEcg7SR"
  }
}
```

#### responder ---> (2018-10-16 17:14:10.209)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4xvEX8JyfkUB9k83FcdwFyqBR1DTtee1WZFGFPpPbMXDPBZKgCSm7Pyiz1LY58URCeFbhkJ17Ei81MzTHhcZzVwhvffZ8NUrdpY5k4kAzbdK33bVTYYFx7c2rdW9EPujy21Ze1kmiXkaZDhpVP3d9rjJgvFSbK3bCXBUzNdCEgGX7ruprjhhuiz7Kd2tvqJmTcAumKTasseh3Db4ujykQUWwBXtDgBkpET8dvo6RMwfSHkFu54vkzdcUB5YZpiJMYNjtfxtsvtHHQtucyQJcMBwucM5v63h2M78doX8nTHaSdep"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.213)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.214)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQR9Kv12wCnYA6wpQGhPJgLa2YeVHAq4YVu48yReSV4wRiernBiP4m7GGPYhZHtNTLErT8V1HKbqunGUyLFC43Qp1b2hzvXKjxRRtJ4J46Mh1GVQm5pLPCweMz1ovj53V9NRx4R3FFxu2m4izLEbThyRLfo8QtN9yjdFAY8j4qp2raCBkGvmLuMFfMA13X57v5uTEd9nEcg7SR"
  }
}
```

#### initiator ---> (2018-10-16 17:14:10.215)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak552Yq7KJBVBjjGbDHNTQnQwzwBWzNVihnsXHFw1VJEYizvm2o7QJ1oJ4njz8Bxo2soGmfGzDfXoy1PDvqfHfNx7GfFKwrJbvi9g6eQxKVop4Ez3EuvD3LF6Po6E5FRMbX8Lef5wxwFVJk5naqPityn6mJEJLKQnsY8sMJBM2QMQfhSjmjyvcks4ULNmpvsDXQjfvcpscJ4s1AfisiFX8P9QS47EUXBBR2po5Hr82DjSzkygR2Her7baugbKXVbaZxN3SqFCVveMdm5xu4ZRC817FDMgHffdwyAiocANLi3XwQLM"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.219)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkghJEboL9jy7tLM7oobggcDwzjbwsFKnTrg77pcT9DCKWJM2VbrdgPVYLngR1Uqb3LbJpSfyFgpFWQDhjaSmjp1UMUaghJTNwMPxwEwTPBzM99KPg4oCHg2xC5JDw93r8ik6cLhNdTJWF27BhKqTeobRKjFJMtihWiZToQGurvTeVG4BAyVftYL1BcZYURhcH88KwwJNqxZeB9TkqVbN1BvgcfCRm8BrBAfjgeWkLnugBE3YkvgYJEYy2daxipoHKFpmnro3e7WNR5C5tnXBgzXqGSA9EkqK2amuTJcpSBJfDZn1X8UFa3PZfnSXTzzAwM4Km1MZsRp8nTZsdTCnxTLuH3ZxB8vUv5bnc4TJ6UgZriqjVPN3bkUrmC9a4FSWzUHbpwu4e",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### responder <--- (2018-10-16 17:14:10.220)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkghJEboL9jy7tLM7oobggcDwzjbwsFKnTrg77pcT9DCKWJM2VbrdgPVYLngR1Uqb3LbJpSfyFgpFWQDhjaSmjp1UMUaghJTNwMPxwEwTPBzM99KPg4oCHg2xC5JDw93r8ik6cLhNdTJWF27BhKqTeobRKjFJMtihWiZToQGurvTeVG4BAyVftYL1BcZYURhcH88KwwJNqxZeB9TkqVbN1BvgcfCRm8BrBAfjgeWkLnugBE3YkvgYJEYy2daxipoHKFpmnro3e7WNR5C5tnXBgzXqGSA9EkqK2amuTJcpSBJfDZn1X8UFa3PZfnSXTzzAwM4Km1MZsRp8nTZsdTCnxTLuH3ZxB8vUv5bnc4TJ6UgZriqjVPN3bkUrmC9a4FSWzUHbpwu4e",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.224)
```javascript
{
  "id": -576460752303423446,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 400
    },
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 700
    }
  ]
}
```

#### initiator <--- (2018-10-16 17:14:10.226)
```javascript
{
  "id": -576460752303423445,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 700
    },
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 400
    }
  ]
}
```

#### initiator ---> (2018-10-16 17:14:10.226)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
    "to": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.229)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQR9Kv12wCnYA6wpQGhPJgLa2YeVHAq4YVu48yReSV4wRiexChZvcEJbzKJh6QnUTzMQVpWS5dHv4RbhjYzZHW2nV1tYtajuV9xBB4vKtyV6ZWjqL17CaQo5SLQpaTf9RaiKwkkC4zeVGygtQ4bxFoXW2nnWY85bXNKzuGt1CH47JjrAhPpgJ2EcEZyKZuahND7ac3EgvK9Ecd"
  }
}
```

#### initiator ---> (2018-10-16 17:14:10.230)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4nqFD57R1T6RX4ZpBhbKRXXoo5TYnZyWGWgyMtyVCNzDXE39SBpvDG4ekoz7qq79mJeX9rBKVXHpHtwnasojRy3SL82eFRUhPpLZWP11o8FkkGqQJwFSCXjCCb7RKJHJPTKNPeVjx8ykDEQKz6hKeDhLZp5AoKEox7sq9cyiR4RqFyNATr9rWX7F7UgBJW8M1XEGMW5wPnsDTx2r7LdGm8f7X9eGPkVBt3FsymU2C95vk8vrwxBc3rrjMutTvV3mdbrs8gYvrww3zhnoNTqoDX2cpVjJNaxxH7CSjGQWtQsqbgD"
  }
}
```

#### responder <--- (2018-10-16 17:14:10.267)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### responder <--- (2018-10-16 17:14:10.269)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQR9Kv12wCnYA6wpQGhPJgLa2YeVHAq4YVu48yReSV4wRiexChZvcEJbzKJh6QnUTzMQVpWS5dHv4RbhjYzZHW2nV1tYtajuV9xBB4vKtyV6ZWjqL17CaQo5SLQpaTf9RaiKwkkC4zeVGygtQ4bxFoXW2nnWY85bXNKzuGt1CH47JjrAhPpgJ2EcEZyKZuahND7ac3EgvK9Ecd"
  }
}
```

#### responder ---> (2018-10-16 17:14:10.272)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4jdbaTtieHscLANoHZtVZhBWka3hj1sSnMXHiTM1tL63DywEEsX8QcBoD75ksnCiUFJmA97meHu3FiJhEV5bdmVKoMYDSyLfnPnDBaH1kEkHKi3BaA64wQvZ2PpkY4zJiSfaG6axCY8VZoSsBwC7Ba1mwwUuCoSjAxrNjtDzifWrSZmZwjaNLSzb2TLStNG6QRioqBzF3agCxLp6AmWNSRMHLfaQo9FfebJqi3QPL1HSKASCUP7Lv2bBNqdWXRyYwcxCCPgVWYqUBtDSYDvswGHric5nSDo3AA9g8yEgaHxjhnj"
  }
}
```

#### responder <--- (2018-10-16 17:14:10.285)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkHrSgp7L8XnR93X6dYbGQHnZrpS8hQJRoXaoZ8xz75MRdBV9Kj1k2zDy6i2CdtjsAfjNkup6kfe6meHTqMX9GRU89B66x2Ew7LoLaxnjec46fy3LDnSVjGuKxr5tKSh4RUvJ6SphQ9qraznFGZC8UC8rgutzLZ52DWoToNUYGB1NnWMTK5acEv9WpQyggCYM5CphxotdhTwxV14T7dfKwHaRTbjzkQBkHDqHdWVfPbq9uV29cHqK7r7unv7aAU1HtwvxhQaybUpag7hY6SQbEn9VHb7Lxvpg2FEZerabWyUPa37gFHbzCzeYwnQiCgm6YU5tqS6SEvunYcwgf2tD7jLpHMV6XPKd9SFTgknCmMfrQdUVzh1mZuPMNzhm4hZGRotCXxTZD",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.287)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkHrSgp7L8XnR93X6dYbGQHnZrpS8hQJRoXaoZ8xz75MRdBV9Kj1k2zDy6i2CdtjsAfjNkup6kfe6meHTqMX9GRU89B66x2Ew7LoLaxnjec46fy3LDnSVjGuKxr5tKSh4RUvJ6SphQ9qraznFGZC8UC8rgutzLZ52DWoToNUYGB1NnWMTK5acEv9WpQyggCYM5CphxotdhTwxV14T7dfKwHaRTbjzkQBkHDqHdWVfPbq9uV29cHqK7r7unv7aAU1HtwvxhQaybUpag7hY6SQbEn9VHb7Lxvpg2FEZerabWyUPa37gFHbzCzeYwnQiCgm6YU5tqS6SEvunYcwgf2tD7jLpHMV6XPKd9SFTgknCmMfrQdUVzh1mZuPMNzhm4hZGRotCXxTZD",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.299)
```javascript
{
  "id": -576460752303423444,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 699
    },
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 401
    }
  ]
}
```

#### initiator <--- (2018-10-16 17:14:10.301)
```javascript
{
  "id": -576460752303423443,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 401
    },
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 699
    }
  ]
}
```

#### responder ---> (2018-10-16 17:14:10.302)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
    "to": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7"
  }
}
```

#### responder <--- (2018-10-16 17:14:10.307)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQR9Kv12wCnYA6wpQGhPJgLa2YeVHAq4YVu48yReSV4wRif3dDRU9hVwiF4gdXgc9KoTWbbtRTZDi36aka69ZQtKDe1Eq9s2UTjKNcFBTfqFBTrggLpT24i9braf68VZETESCgrvy782TaRTxq1KNYxbsAQTV72ajVvKGhUByrvkNK2W4naDmSC86kxQyW1YafiWEZXT866VUA"
  }
}
```

#### responder ---> (2018-10-16 17:14:10.308)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak56FG36MwaZVbPic9gWV2819ua4i7ipbjW683XuaBC7dPumcV8srSdz9BdF8gxpQgshzhqGKcxK3j1aaiELTq85D7LvDJM3HYqqw4PLwLp4YAniLgwHemYuj9bxr7o8jqwrTZEeFNmysUhUyAPY33V1LTBCwru9GAVuv4AVHPmWmm7pQbCFP6qtxzfnKny5r2Ge45XTduezQZz7pxJ5pD8rzxYmpCbH4imzHUWkykBipmJtToTT5cTBWdHaEeXkjPXGCuT9ysizDfjsWUGNRVjVzqX8mBKU1phwLQ8hVNrrKrGqc"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.332)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.333)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQR9Kv12wCnYA6wpQGhPJgLa2YeVHAq4YVu48yReSV4wRif3dDRU9hVwiF4gdXgc9KoTWbbtRTZDi36aka69ZQtKDe1Eq9s2UTjKNcFBTfqFBTrggLpT24i9braf68VZETESCgrvy782TaRTxq1KNYxbsAQTV72ajVvKGhUByrvkNK2W4naDmSC86kxQyW1YafiWEZXT866VUA"
  }
}
```

#### initiator ---> (2018-10-16 17:14:10.335)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4sBk82dv24m412a2awXm4Bx7G8HmLboo2t6M5V7ptDnicjcrZhDZFqdiDvtbHB2jAK29EuacJZ872AzZa9vjUzH8U6JZps1g3JHVYr7UVaVSrH5QvBYxKukADokFB3KwLcGqyfhC93Xgv65bdWuAicgWNTWoZxTUu9QFbokNAtPJwiaros2SX7i5azKDxDcN4zbD1AxCSwkj3kxvFdSJLwMGEhdgFW2E4xTav3y9wAMKcBhBPuyw71p8AHLzn1BYSkoQgfyfFBxwQky9cv5M2BoUVYfd2pnNJ9RSCWmZ9EcJzjT"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.344)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkWqh7kLxx4TGR1hBmBGDRXwX8ZVuL9DRDtEFV8XarKPD59okATwN2nVcv9HR97X7AdDjwgwDnXKTXr7zHyqSDZS6miyRMhcdSfvo8rpoePwXsLisr4kxJSf4dbuMEZ8jRDxQHz3UgapigEuqn2gKnvediJWnDmbvnHKNd1S9HCuWp3r5N1NrQ3YKyFJQFMgK77YCRt8mde6AydaBydK3FJyFggDB2BZn31VD3jbMn73hgNwpYAU4vma4H4vwdNd3UDwbkqGUKBe4etqGCUKrZP8FcmA9C3keXMWwF8YFAkkcjemPfsrqzgzKzDGuE9FeY6HYQHGBnxoQPMepVLjdN3J9KbnnCmWHaSdxM8cwqkYPSbEz4nYZkSpzUieAiMKSDahZWVveM",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### responder <--- (2018-10-16 17:14:10.344)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkWqh7kLxx4TGR1hBmBGDRXwX8ZVuL9DRDtEFV8XarKPD59okATwN2nVcv9HR97X7AdDjwgwDnXKTXr7zHyqSDZS6miyRMhcdSfvo8rpoePwXsLisr4kxJSf4dbuMEZ8jRDxQHz3UgapigEuqn2gKnvediJWnDmbvnHKNd1S9HCuWp3r5N1NrQ3YKyFJQFMgK77YCRt8mde6AydaBydK3FJyFggDB2BZn31VD3jbMn73hgNwpYAU4vma4H4vwdNd3UDwbkqGUKBe4etqGCUKrZP8FcmA9C3keXMWwF8YFAkkcjemPfsrqzgzKzDGuE9FeY6HYQHGBnxoQPMepVLjdN3J9KbnnCmWHaSdxM8cwqkYPSbEz4nYZkSpzUieAiMKSDahZWVveM",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.350)
```javascript
{
  "id": -576460752303423442,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb",
      "balance": 400
    },
    {
      "account": "ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7",
      "balance": 700
    }
  ]
}
```

#### initiator ---> (2018-10-16 17:14:10.429)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### initiator <--- (2018-10-16 17:14:10.432)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "tx": "tx_2M9ipLgcZJKU4mxCu93f47uUyKCWH8MVvK9ai1xwQ5g4HrN5DYF5HnMDicoYfm4e2cCctTi6hiXtmmVqZMTuAgmM2Nj9ug3Kgk3z8teaRbdZ9oeGRLW29"
  }
}
```

#### initiator ---> (2018-10-16 17:14:10.433)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "tx": "tx_2iJcVi27J8Zyq8wK1qc52rsC2CAc3nDNDvJ9hf9VosSYAPKqK6MfFm4eRZ53EPtAS8PzaFxwDeE8Xr2DezDgjEyerzzJsi3HCFtbixmNVUz5u6e5yYqibnXok5YCVQYQBJkRXijsvyCqXN7TmbYx8ACTDoaGaYyxzaBgndLb1u9qWFMYwDkuBFvRKmFvfzwpxSspso6HDQ1gsnvuDdaZQgeLxJ"
  }
}
```

#### responder <--- (2018-10-16 17:14:10.435)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "tx": "tx_2M9ipLgcZJKU4mxCu93f47uUyKCWH8MVvK9ai1xwQ5g4HrN5DYF5HnMDicoYfm4e2cCctTi6hiXtmmVqZMTuAgmM2Nj9ug3Kgk3z8teaRbdZ9oeGRLW29"
  }
}
```

#### responder ---> (2018-10-16 17:14:10.435)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "tx": "tx_2iJcVi27J8ZzrNQkk5Bab4TttBUtSEwE4GCBFNngZFLTrMZ3mrgeyxASVJL2hYQJzEp7rBPNdctAv6qPnkbvECjY2LnST696xkEtsFFStRagxZCqcAvvPaGFbnTUdwUJDjnUBPyhP1b54YKa1ZBFPHxFocAXbBgnyBdogjHVuY8YVrJsbeaKsKugFVKU51cHR93FUYn4EbfqqrmuCg51T5v2fH"
  }
}
```

#### responder <--- (2018-10-16 17:14:10.437)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3wu1WL1txa1XycPHMssmHrzXzKvAEN19RZMrVDcieRH2fDggziXWEbmUtp5jXfRK6ek7pzYSzT4tsdUVRhAMtYj3yoztVoCHZgkk5ihrf1xCFhaBE7dz3KFRSuX4srzCxCgxp6wc56n843WjUS2ZsxD3NrC6YCrvVnGhx8iUMQwAaGMZJdRWXWCe4ay9YwMr6jvL4Es6HHmgCAJeiBen3sCRb4Urt8HiyoQMjS3vMZU6wfaFgw72FVP7aMMskEow6LrYWT7YQUyeUX3chtpZE2gnXm33TzTJBjgZCHDW8AFvk9it1sHB",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### responder <--- (2018-10-16 17:14:10.437)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "close_mutual",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### responder <--- (2018-10-16 17:14:10.438)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.444)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3wu1WL1txa1XycPHMssmHrzXzKvAEN19RZMrVDcieRH2fDggziXWEbmUtp5jXfRK6ek7pzYSzT4tsdUVRhAMtYj3yoztVoCHZgkk5ihrf1xCFhaBE7dz3KFRSuX4srzCxCgxp6wc56n843WjUS2ZsxD3NrC6YCrvVnGhx8iUMQwAaGMZJdRWXWCe4ay9YwMr6jvL4Es6HHmgCAJeiBen3sCRb4Urt8HiyoQMjS3vMZU6wfaFgw72FVP7aMMskEow6LrYWT7YQUyeUX3chtpZE2gnXm33TzTJBjgZCHDW8AFvk9it1sHB",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.445)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "close_mutual",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```

#### initiator <--- (2018-10-16 17:14:10.445)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "died",
    "channel_id": "ch_24rt4WNHKcZSwa7bhaYesKoHbwSfwkUsxVFMk8CLcPmWJMyU8E"
  }
}
```
