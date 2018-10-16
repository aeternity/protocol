
#### initiator init (2018-10-16 17:14:28.664)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb&role=initiator
```

#### responder init (2018-10-16 17:14:28.669)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_TZyMVvzU3hLJtKnYk47u9Kn546c58dbWc1wvXY3gayy11GtM7&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2uHEMCra9RHdoKSRd1525Vx87x4oT354cpwN5bYoLKcGHQkuUb&role=responder
```

#### responder <--- (2018-10-16 17:14:29.668)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_open"
  }
}
```

#### initiator <--- (2018-10-16 17:14:29.669)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "channel_accept"
  }
}
```

#### initiator <--- (2018-10-16 17:14:29.674)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "tx": "tx_3d11KjpALGJSrzwTy6oub8Qv4su7RMx2hck9JNUEgjtyU6qrUG48oB7x4ucqxPokv4rA4P5zaAWfi6eCujMzNBvMMu3xP8p9Svn5xM77VDy3ntvSFDRTNLxquqDLKr53dA7VoLQyju8FB1sKcPCeRhzzU2bUngSwrTNRkD"
  }
}
```

#### initiator ---> (2018-10-16 17:14:29.695)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4Hn5pbqQWJjn5VmeYcUdiws396yv6G2yue8SnrGP3Qphp1kMtBd7YWsSzSeF5fQHf68xTrhadbdXQpBwg8NGwsfgPjJj8CFYaborCEPWMPgYdQgqC9M4reUsVjZCxHDnt5uSeem4tyfsmKcXY6guT6nxV4HfZR3pb6Us8WTA2Bi4Nk5ib1NvCTFwKUz6e6kcs6bAK4MJBuEVx3TLLp6B3ksrEp8cS7C2KHdebacPicf12dyCmcDBiBS44N16fCkWu2"
  }
}
```

#### responder <--- (2018-10-16 17:14:29.696)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_created"
  }
}
```

#### responder <--- (2018-10-16 17:14:29.697)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "tx": "tx_3d11KjpALGJSrzwTy6oub8Qv4su7RMx2hck9JNUEgjtyU6qrUG48oB7x4ucqxPokv4rA4P5zaAWfi6eCujMzNBvMMu3xP8p9Svn5xM77VDy3ntvSFDRTNLxquqDLKr53dA7VoLQyju8FB1sKcPCeRhzzU2bUngSwrTNRkD"
  }
}
```

#### responder ---> (2018-10-16 17:14:29.697)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HjiAQ3LhX91nJs4NLHyJ7vdaMmuUu8iLMr8CU8TZeB9VuYsJuosMErrrV6HnRCyYfw3PANJdvkiXUUpUg3KC1ivrnm9LzrWsoW42wvbir1cKX1QGkCcpdAqXGEYe8LQWTi67gL8tn6VbeUPGkYnEeokw9k5pcX7MPbkpepcRH2cGRvfe6c2pkYnhNH1acL3Lvn6NsrFi5vKq4FBr1ePk5vuQaD75XJHVqSCMkYSQkZahrHpe6C9BnmBhwohfA4xuF"
  }
}
```

#### initiator <--- (2018-10-16 17:14:29.699)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_signed"
  }
}
```

#### responder <--- (2018-10-16 17:14:29.700)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmMi3yoXT9WuXnNj8PYFsz5icy3EgLNxNz1ppPFQmvwdeYtwMm4sKLYQYqVdYnnxpQhFSYuyeoyno1C69rf1xGbNmiinja7xZhNvF265s9DWK7PN7LCCojoHksrFymCRtKsTU9kbWFEmffd3YWh56QHxxDadeoFyGHGKuBQVUePpW36kigm8LA2rLRSMZMa18aoEsZY6t63JRfZTvHtNrmDtgD1Nzcb2Lftf89LsV2JFC7YxSk9qPAADpgtfXsi7VwUM2WFKq1eshwXFKvk5a8kdBcvJ4KjLSacxYBRh7fxXt6eFcQQQPqtPEiijKRuJpnyxVUVGbWpkKnPoNQK2LK6yD79z"
  }
}
```

#### initiator <--- (2018-10-16 17:14:29.700)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_6jPYBUFTkcmMi3yoXT9WuXnNj8PYFsz5icy3EgLNxNz1ppPFQmvwdeYtwMm4sKLYQYqVdYnnxpQhFSYuyeoyno1C69rf1xGbNmiinja7xZhNvF265s9DWK7PN7LCCojoHksrFymCRtKsTU9kbWFEmffd3YWh56QHxxDadeoFyGHGKuBQVUePpW36kigm8LA2rLRSMZMa18aoEsZY6t63JRfZTvHtNrmDtgD1Nzcb2Lftf89LsV2JFC7YxSk9qPAADpgtfXsi7VwUM2WFKq1eshwXFKvk5a8kdBcvJ4KjLSacxYBRh7fxXt6eFcQQQPqtPEiijKRuJpnyxVUVGbWpkKnPoNQK2LK6yD79z"
  }
}
```

#### initiator <--- (2018-10-16 17:14:30.121)
```javascript
{
  "id": -576460752303423419,
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

#### initiator <--- (2018-10-16 17:14:31.983)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### responder <--- (2018-10-16 17:14:31.984)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_funding_locked",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### initiator <--- (2018-10-16 17:14:31.984)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### responder <--- (2018-10-16 17:14:31.985)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "funding_locked",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### responder <--- (2018-10-16 17:14:31.989)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### initiator <--- (2018-10-16 17:14:31.990)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "open",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### responder <--- (2018-10-16 17:14:31.991)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmMi3yoXT9WuXnNj8PYFsz5icy3EgLNxNz1ppPFQmvwdeYtwMm4sKLYQYqVdYnnxpQhFSYuyeoyno1C69rf1xGbNmiinja7xZhNvF265s9DWK7PN7LCCojoHksrFymCRtKsTU9kbWFEmffd3YWh56QHxxDadeoFyGHGKuBQVUePpW36kigm8LA2rLRSMZMa18aoEsZY6t63JRfZTvHtNrmDtgD1Nzcb2Lftf89LsV2JFC7YxSk9qPAADpgtfXsi7VwUM2WFKq1eshwXFKvk5a8kdBcvJ4KjLSacxYBRh7fxXt6eFcQQQPqtPEiijKRuJpnyxVUVGbWpkKnPoNQK2LK6yD79z",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### initiator <--- (2018-10-16 17:14:31.991)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_6jPYBUFTkcmMi3yoXT9WuXnNj8PYFsz5icy3EgLNxNz1ppPFQmvwdeYtwMm4sKLYQYqVdYnnxpQhFSYuyeoyno1C69rf1xGbNmiinja7xZhNvF265s9DWK7PN7LCCojoHksrFymCRtKsTU9kbWFEmffd3YWh56QHxxDadeoFyGHGKuBQVUePpW36kigm8LA2rLRSMZMa18aoEsZY6t63JRfZTvHtNrmDtgD1Nzcb2Lftf89LsV2JFC7YxSk9qPAADpgtfXsi7VwUM2WFKq1eshwXFKvk5a8kdBcvJ4KjLSacxYBRh7fxXt6eFcQQQPqtPEiijKRuJpnyxVUVGbWpkKnPoNQK2LK6yD79z",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

##### initiator: (2018-10-16 17:14:32.226)
> Funding has been confirmed locally on-chain

##### responder: (2018-10-16 17:14:32.226)
> Funding has been confirmed locally on-chain

##### initiator: (2018-10-16 17:14:32.226)
> Funding has been confirmed on-chain by other party

##### responder: (2018-10-16 17:14:32.226)
> Funding has been confirmed on-chain by other party

##### initiator: (2018-10-16 17:14:32.226)
> Channel is `open` and ready to use

##### responder: (2018-10-16 17:14:32.226)
> Channel is `open` and ready to use

#### initiator <--- (2018-10-16 17:14:32.262)
```javascript
{
  "id": -576460752303423418,
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

#### initiator ---> (2018-10-16 17:14:32.262)
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

#### initiator <--- (2018-10-16 17:14:32.268)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQU3nTuQcN4QckwqRURYQD77R89JVuMwfv8PktRgYA5rQs8kFhn6HZPMDPNwF7FW5Vs8e7NCpGaPn5EgQ2EDKse67WKLrdvugz35twYUVf2hkn7pLS4PxtNQ4NykAuCcpCkYiw7W5UcDydvZ2WhsgaaH8SDkSjxGxawXvJMvoLPyK4331FztC6s5raTFy2LtZXmQcr4xzczKi2"
  }
}
```

#### initiator ---> (2018-10-16 17:14:32.269)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4r7LHWR1LgzSezoWmHZRhHS8gE2e326kCy8u2XKXcXsD1dSfXdfiRJ39u5qtnMvRxUMN1Z91i753XMjMvTzrCv1VcTtmRqcCKtC8B8LkV9UkYjid8qqMSjGbtPbJHftV7beRfiaNof6kjTAu3LwFAbfruTpZN5RWC9jEjKrehRpaXCg5wJscanRhF9VK4ZbBHZiau1xAehSTLoZch6zjbCtwniyjW8YRo8cMVDjraEyorzyB1USANo9xbXvaTXuqVnkEsCxgKMp8jiBBnnWC9e2uXAxoMRQwrYTFPR5f65TAm6f"
  }
}
```

#### responder <--- (2018-10-16 17:14:32.274)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### responder <--- (2018-10-16 17:14:32.275)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQU3nTuQcN4QckwqRURYQD77R89JVuMwfv8PktRgYA5rQs8kFhn6HZPMDPNwF7FW5Vs8e7NCpGaPn5EgQ2EDKse67WKLrdvugz35twYUVf2hkn7pLS4PxtNQ4NykAuCcpCkYiw7W5UcDydvZ2WhsgaaH8SDkSjxGxawXvJMvoLPyK4331FztC6s5raTFy2LtZXmQcr4xzczKi2"
  }
}
```

#### responder ---> (2018-10-16 17:14:32.276)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak59sT1MSLWg7V9yZsy8pXaePjPCeVEQ7KD8QkcsSkf2st9F9gbUguWqJRx49uAMWxAvMXnKYE2dm5QKQD1kHdpd5baFYwmv1XTTUfNhJne9KEgd63intfqMQfomW4TtBfPrCk3FkDFzJBBicebN7LubpFSwLm5ZMWVkaAeET9FZyXXrVkTHfuYZcdvQjmbB1kecKrsemuRN12whtZSmVtgXwe7jHFi1LFP2pWJRRyyuFPZbP2tkqH1uKhT3oTC93D1YE8J5o6MjujXJGUXKPiGffmfpktkN4MPk5fuA7ER8VAjKz"
  }
}
```

#### responder <--- (2018-10-16 17:14:32.282)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkUzQ1Z8Au41c8ruvCQNiF16dNHLktP3VMJV5XkzTR8G3QJ1UqU8RXXXcRN76YU4MU5gayuiGExVH8MqRpBM22U5D7VymQ4kH8M3JhmEn9X5XCyG2aLb41PsLAvVB3YXPJs12UehHDYxSf4ypXx91o6GwoQNxX6PSQhBLSe7wNtdTBuDoHNHCpZMaB7hM2nYywbVjDQXNhXyDfTM2PF7joVrY5Go9iy7N4vPh3xRUHoLsJyzSH5XbHC7YTSoEJmD6sPb2Y4SQUKzFXuHZtoiFYDCeM5jQY23QHkKqQXk1D9r12Ub7pz75GsDDUo1xwQxiWu8wp4QJTZDuefnYJvmdg1QEQFydsNeuYygBozLyijyfqMAb8sGz4UE5isVW6uKHZybc2vAAt",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### initiator <--- (2018-10-16 17:14:32.282)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkUzQ1Z8Au41c8ruvCQNiF16dNHLktP3VMJV5XkzTR8G3QJ1UqU8RXXXcRN76YU4MU5gayuiGExVH8MqRpBM22U5D7VymQ4kH8M3JhmEn9X5XCyG2aLb41PsLAvVB3YXPJs12UehHDYxSf4ypXx91o6GwoQNxX6PSQhBLSe7wNtdTBuDoHNHCpZMaB7hM2nYywbVjDQXNhXyDfTM2PF7joVrY5Go9iy7N4vPh3xRUHoLsJyzSH5XbHC7YTSoEJmD6sPb2Y4SQUKzFXuHZtoiFYDCeM5jQY23QHkKqQXk1D9r12Ub7pz75GsDDUo1xwQxiWu8wp4QJTZDuefnYJvmdg1QEQFydsNeuYygBozLyijyfqMAb8sGz4UE5isVW6uKHZybc2vAAt",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### initiator <--- (2018-10-16 17:14:32.287)
```javascript
{
  "id": -576460752303423417,
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

#### initiator <--- (2018-10-16 17:14:32.289)
```javascript
{
  "id": -576460752303423416,
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

#### responder ---> (2018-10-16 17:14:32.289)
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

#### responder <--- (2018-10-16 17:14:32.293)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQU3nTuQcN4QckwqRURYQD77R89JVuMwfv8PktRgYA5rQs8qgDddq2agwK8vnE9dkqKBetTfA6qhRgjZR3KobnVcr8S2oD42gHpE6UsL4MNrNjEfgmmeQYHUDu9aga32d5GeysEEyb5mAEf8bH7EoL1NxoqhPFKFztt7cKtNfwJHt6aao9DYezz2UbxcGQdRjgDKLsH16EzbBN"
  }
}
```

#### responder ---> (2018-10-16 17:14:32.294)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4oEmU8bKZ7r2GPqnE2z1ayxE4WuRohx5QrqjBv7PViHVWS4EKs8LYdqTjnk8aWnraEC8vy5s6KzLSmY5K6Cau67n9zEj2jjhEqjfAPbVnYqDqnRQnPjfc4PHcgEd3ppuweQjsASetaJ8eWv3cdA9H7wMa43HBb33xngS3hzU5GzwmtqJNuTtgnt1aeJdjaXXnYJFK8ehXzAnLa5wHFjdBAgfDjpAm9fTvJ3wbp1aciGVHBHrY2S3aiytXQFmiJnTrv8VcQMCvba2af5Du7Skd3yNARbXCTqYUmwunvFBpvfJEa5"
  }
}
```

#### initiator <--- (2018-10-16 17:14:32.328)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### initiator <--- (2018-10-16 17:14:32.329)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQU3nTuQcN4QckwqRURYQD77R89JVuMwfv8PktRgYA5rQs8qgDddq2agwK8vnE9dkqKBetTfA6qhRgjZR3KobnVcr8S2oD42gHpE6UsL4MNrNjEfgmmeQYHUDu9aga32d5GeysEEyb5mAEf8bH7EoL1NxoqhPFKFztt7cKtNfwJHt6aao9DYezz2UbxcGQdRjgDKLsH16EzbBN"
  }
}
```

#### initiator ---> (2018-10-16 17:14:32.332)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4uVHfET5fXpRLTvSJpKfPQaELXb2qxDDKEZQumB2ngS7X1gZTs1ndkD83cRrQAEr2QSUhNgpGErbGuqF28w9x1NzhzyyeCJG2iFjUJGaMhTeUqwr5VAmxCEQSv2FERueYyEVBBZCKnF8aox5ywpPY29Lhe1q2A7QDKZMUWUFN5NCKw1FADrfdkiPSc3XKrFzLTVDzZY5gVY8FTCdx1ftRQGUqkBCmMhQpi6s6YPMhbBwgwdS8ZDcwrkBdU4ft2oeBWHsC3qGp9xUULoGnfp6zCpMgQKAtdVV8seCZWShskjnoaT"
  }
}
```

#### initiator <--- (2018-10-16 17:14:32.346)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkQ43SiwL6r8h8fkP7BFF5rv7UyDzSqzLp9HxVYtGv4steSFiy2gH89jKJWDZge2TKkrJzscKhnT8nNdS64vHGwxcLKSSPbqmV6Sych8kA3AdEo7Rmkdni5vTs6TGLRf5QRbSVStoL8Dz6j5ghGDQySfiDNWsQk8xMQQjFPzpNLLkQYgo7jjtkZdLL9RpVC8Dib6rXXejkAGT6iBc49NXzEPqtt6GgMdzKdEXsnPpnYodN3qWR5Mmsu4enW9gBXNq4mhPsBTB4CfQvLN7AXATX6AvUqPFKo31zt9q5z3WHvzodUHEdanNzvEdZS7MDQyFYAqHhAvx4JnAyYNabc4XDgsNyoJftd8p9Eb7gGrBr8rcCVmBvJHvB5sZR596Mqc5mL6utHQh9",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### responder <--- (2018-10-16 17:14:32.346)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkQ43SiwL6r8h8fkP7BFF5rv7UyDzSqzLp9HxVYtGv4steSFiy2gH89jKJWDZge2TKkrJzscKhnT8nNdS64vHGwxcLKSSPbqmV6Sych8kA3AdEo7Rmkdni5vTs6TGLRf5QRbSVStoL8Dz6j5ghGDQySfiDNWsQk8xMQQjFPzpNLLkQYgo7jjtkZdLL9RpVC8Dib6rXXejkAGT6iBc49NXzEPqtt6GgMdzKdEXsnPpnYodN3qWR5Mmsu4enW9gBXNq4mhPsBTB4CfQvLN7AXATX6AvUqPFKo31zt9q5z3WHvzodUHEdanNzvEdZS7MDQyFYAqHhAvx4JnAyYNabc4XDgsNyoJftd8p9Eb7gGrBr8rcCVmBvJHvB5sZR596Mqc5mL6utHQh9",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### initiator <--- (2018-10-16 17:14:32.352)
```javascript
{
  "id": -576460752303423415,
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

#### initiator <--- (2018-10-16 17:14:32.354)
```javascript
{
  "id": -576460752303423414,
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

#### responder ---> (2018-10-16 17:14:32.354)
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

#### responder <--- (2018-10-16 17:14:32.358)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQU3nTuQcN4QckwqRURYQD77R89JVuMwfv8PktRgYA5rQs8w6jVBNVn2fEtvKM3kbq6VBd26jApPKp9cJfFHMUENT9vJDKit3YUAqdxmm97dTpvJeQGhiyAiqqS1GGkHVjCf7BTBqWfKseLW5XVbkkVyE49Mw621HDfWNfXb8arF572YoiU6nKKtiWCMx2RerveYqn1wAHgRLB"
  }
}
```

#### responder ---> (2018-10-16 17:14:32.359)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4s42bgVpXvVZEgYMSHztAwayM7tsWATsa6Za73NhnprcxLujm85CbAv7QcRNxfJmYggnvq3hbPU9CimRqK1oSTWmZHxkmk4kFk9KrUpKjdZSGFTZh7CTv2fsDXPDjngrwD5NK1CYjxV2F3Rpw52uHBxi2FdN2AuLJ5B8p8RSYCUFbUgQxyoMLDuJdf6qcmudM4dauShPABfYAaPGVPLZkzCewG3hKDcEYe53UXoMDXFLSqwt43iWHwD5aJJDU8s6xpfxM6RSaq83t9G6Pipb27TpiFQVyuT2BLQFFam9yZgy2xc"
  }
}
```

#### initiator <--- (2018-10-16 17:14:32.363)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### initiator <--- (2018-10-16 17:14:32.363)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQU3nTuQcN4QckwqRURYQD77R89JVuMwfv8PktRgYA5rQs8w6jVBNVn2fEtvKM3kbq6VBd26jApPKp9cJfFHMUENT9vJDKit3YUAqdxmm97dTpvJeQGhiyAiqqS1GGkHVjCf7BTBqWfKseLW5XVbkkVyE49Mw621HDfWNfXb8arF572YoiU6nKKtiWCMx2RerveYqn1wAHgRLB"
  }
}
```

#### initiator ---> (2018-10-16 17:14:32.364)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak5AophP9iv5hqwmDDbz6E9DevqjpL67zm2NKrcUcbKEPK66mykot7Hxnw62fAEWjNgVZ9gvmdZcTrZ8gYsi8pWjMnEJC7mtMXdQ31FQK6s2yytfzUyLsNRP6Qu7vyL1AEkcMXA4hnZ38dT77rJivPSHhDc3D3wB5TdGU9Q8LpVgB2SWPBZQLk5vtPdd6uh38eun1wrrfX8SH3EA54zc4tFP8MNX4xTos1zqcYkumFnyNnsgJ3GAJHKu86sTN4i3fYYrFuVwHNrHbSLEQzTvpNBbYkKozxVyy8daNNxDtfUsg1G3A"
  }
}
```

#### initiator <--- (2018-10-16 17:14:32.369)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkWcRkRsCXKZ9SsTREh28mxWttudzdgY54gErEzdfCoxKCjBVMEvg4SUovWvn6SP8JqViw6zMQ9pi4KHGrCCf4AGjfKjPoyYzEuzVK4b7VsiAqG2d4hekxkJq2XW6KNx5nkvUzR6zYq8MtRVLsmEgu5iitJU9YYnbGMu2KnsRi9zQnZZhxWsTkMCxrxMWAAM4gLP45PzGHmzRT9WbY1cDXP8PJQE9WmR28YwFz6CpttNtiB8vYXKu9P1JMsaTroxMCJ72JW96QmQLmqkWUtwEVqdSyjYhtt7bmjQizGX41zVpBAxt1r4FYqM2HGbuLrk1Gaue8gUBJA1ki5HDNgoiGjs5b4bocxcFDLukttgmejppyLBpcMdH2Dc73bwWE1PFeYG2PTVGS",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### responder <--- (2018-10-16 17:14:32.369)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkWcRkRsCXKZ9SsTREh28mxWttudzdgY54gErEzdfCoxKCjBVMEvg4SUovWvn6SP8JqViw6zMQ9pi4KHGrCCf4AGjfKjPoyYzEuzVK4b7VsiAqG2d4hekxkJq2XW6KNx5nkvUzR6zYq8MtRVLsmEgu5iitJU9YYnbGMu2KnsRi9zQnZZhxWsTkMCxrxMWAAM4gLP45PzGHmzRT9WbY1cDXP8PJQE9WmR28YwFz6CpttNtiB8vYXKu9P1JMsaTroxMCJ72JW96QmQLmqkWUtwEVqdSyjYhtt7bmjQizGX41zVpBAxt1r4FYqM2HGbuLrk1Gaue8gUBJA1ki5HDNgoiGjs5b4bocxcFDLukttgmejppyLBpcMdH2Dc73bwWE1PFeYG2PTVGS",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### initiator <--- (2018-10-16 17:14:32.374)
```javascript
{
  "id": -576460752303423413,
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

#### initiator <--- (2018-10-16 17:14:32.375)
```javascript
{
  "id": -576460752303423412,
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

#### initiator ---> (2018-10-16 17:14:32.376)
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

#### initiator <--- (2018-10-16 17:14:32.379)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQU3nTuQcN4QckwqRURYQD77R89JVuMwfv8PktRgYA5rQs92XFLiuxyNPAeurTwrcVD3EK3XXUWTUTUq4szeavrLvan96ywTnjzv8Qpoc2F325AjDKZZvB29vBq1v1LPSAYZ6snLfFLv7rxfVFrxYr43vB8k4KjSprNG7QGsG26KXGgXkqN1jSDFHj1gUQwEK3rgDC6qprZnm3"
  }
}
```

#### initiator ---> (2018-10-16 17:14:32.380)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak51PqfkFks1r996ETcv6GcfXGupCH7BfG7fEjqXtj8Hd1r8Uw8oPXBLitKRwrKgwCAuFC5gTEDz4jk8KoCxbUd5ZdeWxV5GLQ5x1i8h53fWRtk3SXPzEUX1iN8xT4UDABJDfEPemnkFpaGgZhNNabCxzANPiEHdN1htEFviPaUbJPDTyWh7y3RPaGGQK1e2msK9WBmsH2xDwTJkQBq4Jg4XyPvb5vH6jQG6oZxeMoxjJCFtmsFduYs18A2sCyACFYmovdMbyM31uVHTJZbrsKfRawFZuSr3UukyUA3zUwiS7Bzei"
  }
}
```

#### responder <--- (2018-10-16 17:14:32.413)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### responder <--- (2018-10-16 17:14:32.413)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQU3nTuQcN4QckwqRURYQD77R89JVuMwfv8PktRgYA5rQs92XFLiuxyNPAeurTwrcVD3EK3XXUWTUTUq4szeavrLvan96ywTnjzv8Qpoc2F325AjDKZZvB29vBq1v1LPSAYZ6snLfFLv7rxfVFrxYr43vB8k4KjSprNG7QGsG26KXGgXkqN1jSDFHj1gUQwEK3rgDC6qprZnm3"
  }
}
```

#### responder ---> (2018-10-16 17:14:32.414)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak5CDzfMWbTMXtx2k5K5Ez4nM5RsngjmcTcSUymN6CzRFoHUF2mHunQNiKgLXmWKdq6N3Ne6RaKocWg5fWSa1cbauG8eHAJdS3fb7HRRRA1swEQY4Pv5fj6iKehycYv2ApWGxnwaUexT5jteHzP6QoMh46Ahso7k1oUAquK4HZNxZDAZW8ZZtw8zuNNk3BxrKzY5LRavCVxZzoLqv5prtgRjfUXWPDpegZMa56QAb3Ywf93L1mcWEdiHaBSuXMcgNz2eDddqw7qi8g9fA5XSWe33FVKLtffPRiRFk1YGrJttTnvYJ"
  }
}
```

#### responder <--- (2018-10-16 17:14:32.418)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkkxBSUoeeRzF271Aq5xkUeb3H3XViLG2LT8WVfyYvqL1qxHU7wHEb9A6j8iCuxFr6zZZ5oaMLeujZh39j8tMBvCSEeKSEXdK47tZdyobWHvT8fX4WHNNzW3r2mXSTDDZGkVfUETAhXEMYzZXmDTuPPETC4Ms34Webk96KqS5jZYMBGuvXEnHDpZ8zDrwGcq7xngcy859gfVtZvsrXzMTSemSX5ybEGsCW8WPwzTxFE5W9xbWtcqQWhRHNkmSvocnPx2MpyoTCzmBLeZoZ6bCsQTEgoJSghJYPJhPLD5UQSbu65aCqS8KfAPpfaG9nV4x2CKToiqh4eUs6JiL4ak5NBWrMSGCGPB3QPU2e4b4DfTALUGiteNp4hcLd55AhKWHvDJDyJjdK",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### initiator <--- (2018-10-16 17:14:32.419)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkkxBSUoeeRzF271Aq5xkUeb3H3XViLG2LT8WVfyYvqL1qxHU7wHEb9A6j8iCuxFr6zZZ5oaMLeujZh39j8tMBvCSEeKSEXdK47tZdyobWHvT8fX4WHNNzW3r2mXSTDDZGkVfUETAhXEMYzZXmDTuPPETC4Ms34Webk96KqS5jZYMBGuvXEnHDpZ8zDrwGcq7xngcy859gfVtZvsrXzMTSemSX5ybEGsCW8WPwzTxFE5W9xbWtcqQWhRHNkmSvocnPx2MpyoTCzmBLeZoZ6bCsQTEgoJSghJYPJhPLD5UQSbu65aCqS8KfAPpfaG9nV4x2CKToiqh4eUs6JiL4ak5NBWrMSGCGPB3QPU2e4b4DfTALUGiteNp4hcLd55AhKWHvDJDyJjdK",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### initiator <--- (2018-10-16 17:14:32.423)
```javascript
{
  "id": -576460752303423411,
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

#### initiator <--- (2018-10-16 17:14:32.424)
```javascript
{
  "id": -576460752303423410,
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

#### responder ---> (2018-10-16 17:14:32.424)
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

#### responder <--- (2018-10-16 17:14:32.428)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "tx": "tx_GB8bJXCQU3nTuQcN4QckwqRURYQD77R89JVuMwfv8PktRgYA5rQs97wmCGTSAi76QuPaqzHpf6F68ysJmm84yi5u6ErqhsfCtq3Z4an3n4Kx9fAibBe2HaZfGpMpwE5hzrRgAoF34fMou5ZMpTJThF42GKfbV9kYkh1JgS2yxaUps43bxxaqrs8E7ZCrAm9uzmt1N5XWTbqiPc8kL43A"
  }
}
```

#### responder ---> (2018-10-16 17:14:32.429)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak586AH1jZ8sevhh6dW5HQYrjWyjBq578Acf2YGukNArVTsDegbz9jvpYKR3dh3etJDBLNjLA8NXkaykaw2rnQcdYtoABqaXx9GMuWWJdiwFacP8XPUdfC5Kd7dJc4cXT4V8YKkNxYpGsMek3ysdMUBZcvXCdWDjRLNBxjQ3H4TuMhodtqUnNM9R7fVVqzeBUw3WRhWeLJe2ddhL21nM6NLDJYZM2cYk62Dvz6zYbsJ4csLFrWbus12J7CU2sHbSVo9oaAFDpCcxZc83789gi5gQzkpydU6SHGJe52QCd6GTsRuq4"
  }
}
```

#### initiator <--- (2018-10-16 17:14:32.468)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "update",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### initiator <--- (2018-10-16 17:14:32.470)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "tx": "tx_GB8bJXCQU3nTuQcN4QckwqRURYQD77R89JVuMwfv8PktRgYA5rQs97wmCGTSAi76QuPaqzHpf6F68ysJmm84yi5u6ErqhsfCtq3Z4an3n4Kx9fAibBe2HaZfGpMpwE5hzrRgAoF34fMou5ZMpTJThF42GKfbV9kYkh1JgS2yxaUps43bxxaqrs8E7ZCrAm9uzmt1N5XWTbqiPc8kL43A"
  }
}
```

#### initiator ---> (2018-10-16 17:14:32.473)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_LHMmG11Rak4yQqGMwBCY9p5DQBtnqjxveMFwjbgm8dLvfieW6FwCGkU7D7zMoNJTKeF7ygb483SrFxMThnKzXgPuJeEwb2d5hds75JXH3WvVbNC3GfVyaTiPdpNtu4iTfErnxev9S6pjmgdDNuDSVUH7qTtZk3C7LRpDH3saw6taJQLJUU6emC39ae5KwFtRQYjRb5rVCELFoebCFpCAL1UJGACTfuTA9JBHb7pbccfhidQict4QCqawgGE2ZDyhsHN9KN6Pa7txTxMkG8BRWZYHZTpoMeTuvQ7VknGpzn2wW9RLFeQ3biwqk"
  }
}
```

#### initiator <--- (2018-10-16 17:14:32.488)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkhYTtzLfc8852vUMonhFKUuWjjVpRAuHE5y3XiyXgre7eP5sFTj5JnC5yZ642Gb877KFhVnNgFHYgrsaNDJVRp1pn22i7xagW721tYYmDSCzC5GBWuf74FZGmDATJ5dXoLrJKU4i27oMBVcAHWVZ7TP8nraWWbqzRRGzEqaUoSQ2GWQzY9C3vBgiz68qXrMk74xnD3JYJecRFKBXMjcqtugLvUCcAyrazsXfPW4dk7fxZXC7KpbDeirNJuAdqD1x9bhHzJdEMf8KV9vQNivvarakzUG4KezpReRu2fvhyswxVSAsFviUw9SAAvRugCZVtU4m4wQTS2sBq13VQqj1Wq4ziBjySGkxqzrG5zXf2SC2hh7ZwNSMPwiVbd6T9fFq9LGLzX5yt",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### responder <--- (2018-10-16 17:14:32.490)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3XPhV5wAjiGDkhYTtzLfc8852vUMonhFKUuWjjVpRAuHE5y3XiyXgre7eP5sFTj5JnC5yZ642Gb877KFhVnNgFHYgrsaNDJVRp1pn22i7xagW721tYYmDSCzC5GBWuf74FZGmDATJ5dXoLrJKU4i27oMBVcAHWVZ7TP8nraWWbqzRRGzEqaUoSQ2GWQzY9C3vBgiz68qXrMk74xnD3JYJecRFKBXMjcqtugLvUCcAyrazsXfPW4dk7fxZXC7KpbDeirNJuAdqD1x9bhHzJdEMf8KV9vQNivvarakzUG4KezpReRu2fvhyswxVSAsFviUw9SAAvRugCZVtU4m4wQTS2sBq13VQqj1Wq4ziBjySGkxqzrG5zXf2SC2hh7ZwNSMPwiVbd6T9fFq9LGLzX5yt",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### initiator <--- (2018-10-16 17:14:32.502)
```javascript
{
  "id": -576460752303423409,
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

#### initiator ---> (2018-10-16 17:14:32.571)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- (2018-10-16 17:14:32.580)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "tx": "tx_2C9estKT2wjBoiu7dnfMZ1S9u4uRRLqToEeBXQmH1T8nm48LvMZ8cGpDnpLTWjTnn7p2vWoLmfe5PetY5w4TJxrc54AeHL24LaxEZsJCubGWra88vquVTiVPpvwewPMATLd9qa1noFSybRYGShbA6zMN7GhGfe"
  }
}
```

#### initiator ---> (2018-10-16 17:14:32.582)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "tx": "tx_2WsEQsiC5XsoMzcgF9QqVu1ksTp58rgLwCpw4cQJeUSXvHuEunXAZ2nxpuxznGAt2bF7pXKnKoV6QiattdFyPrKE8FuYuMR7yjbXAurcR9Y2JNFostMS3Gofvjt5vgLKmygEXhBaGU8D4bVqRWZcRL5B7u8UiHpSj7Cp9cFQmG1aQrGqMBY5dgx1QWjPmpTq6PtorRJBaqV3iqMXXg8HQkA52bK9Pa8BEgYMrqMzsm6Ad6eRHqeRsHTJZwngGTGb9Zm"
  }
}
```

#### responder <--- (2018-10-16 17:14:32.583)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "withdraw_created",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### responder <--- (2018-10-16 17:14:32.584)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "tx": "tx_2C9estKT2wjBoiu7dnfMZ1S9u4uRRLqToEeBXQmH1T8nm48LvMZ8cGpDnpLTWjTnn7p2vWoLmfe5PetY5w4TJxrc54AeHL24LaxEZsJCubGWra88vquVTiVPpvwewPMATLd9qa1noFSybRYGShbA6zMN7GhGfe"
  }
}
```

#### responder ---> (2018-10-16 17:14:32.585)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "tx": "tx_2WsEQsiC5XsmqB8r5cSckjHvLdntimoEjDKxkMwAsfrHHyF9a1BZa5yPbcJNz1ejmnf1v9HLgTfBgKwj2HHjTtUCSLJD8DgykJNiSLxCbHgss4co2quoP2Ghc6fy1M7DBHMZxiDYtqDPRJs5GvQWbpaXiqwNe7fKHb8mjB6yPjinRCREGNXZ4S4T77Ks5dMTRqpXGTPBH4FNyc7m1MqwomGJFZU8CHXJvZkxXnyyyjKRFy3A4b4ZfxgUAHmZqPT9B6e"
  }
}
```

#### responder <--- (2018-10-16 17:14:32.587)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3cDMp6242sBySh2B6tdeNGijSp1Ye26Tj78hvdyc7jpEccWx9yLPc71Umwh4Dpmqs7S76w3JzZjxCH6Nq3ba9sw5REKiKPPjg5fHiELBL267Yi3E2Qpr5XtU2KQbrjvKyWsgCzADQFSHJcimmfv6igMf3sNvtvyqaq9YSzwc6uskMnK4SoMKeBD7JmJ6zEN5cLqvmUrE7F3TWLG3q3FXdKFaerNTFk1aEQ5YAhjTY31TdXf2PTAZ7db4yrPcGeg7LtCeATfeoeWrBJnz26saWjAxVENiT2HeqhirJVGfY8Yj55xF28tnLemXuzVkQNikLRew52gVFk2qxXgrJjuTqdKdbeS5Y",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### initiator <--- (2018-10-16 17:14:32.587)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "tx": "tx_3cDMp6242sBySh2B6tdeNGijSp1Ye26Tj78hvdyc7jpEccWx9yLPc71Umwh4Dpmqs7S76w3JzZjxCH6Nq3ba9sw5REKiKPPjg5fHiELBL267Yi3E2Qpr5XtU2KQbrjvKyWsgCzADQFSHJcimmfv6igMf3sNvtvyqaq9YSzwc6uskMnK4SoMKeBD7JmJ6zEN5cLqvmUrE7F3TWLG3q3FXdKFaerNTFk1aEQ5YAhjTY31TdXf2PTAZ7db4yrPcGeg7LtCeATfeoeWrBJnz26saWjAxVENiT2HeqhirJVGfY8Yj55xF28tnLemXuzVkQNikLRew52gVFk2qxXgrJjuTqdKdbeS5Y",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### responder <--- (2018-10-16 17:14:33.679)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_withdraw_locked",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### initiator <--- (2018-10-16 17:14:33.680)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "own_withdraw_locked",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### initiator <--- (2018-10-16 17:14:33.681)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "withdraw_locked",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### responder <--- (2018-10-16 17:14:33.681)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "event": "withdraw_locked",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### responder <--- (2018-10-16 17:14:33.684)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3cDMp6242sBySh2B6tdeNGijSp1Ye26Tj78hvdyc7jpEccWx9yLPc71Umwh4Dpmqs7S76w3JzZjxCH6Nq3ba9sw5REKiKPPjg5fHiELBL267Yi3E2Qpr5XtU2KQbrjvKyWsgCzADQFSHJcimmfv6igMf3sNvtvyqaq9YSzwc6uskMnK4SoMKeBD7JmJ6zEN5cLqvmUrE7F3TWLG3q3FXdKFaerNTFk1aEQ5YAhjTY31TdXf2PTAZ7db4yrPcGeg7LtCeATfeoeWrBJnz26saWjAxVENiT2HeqhirJVGfY8Yj55xF28tnLemXuzVkQNikLRew52gVFk2qxXgrJjuTqdKdbeS5Y",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```

#### initiator <--- (2018-10-16 17:14:33.686)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "state": "tx_3cDMp6242sBySh2B6tdeNGijSp1Ye26Tj78hvdyc7jpEccWx9yLPc71Umwh4Dpmqs7S76w3JzZjxCH6Nq3ba9sw5REKiKPPjg5fHiELBL267Yi3E2Qpr5XtU2KQbrjvKyWsgCzADQFSHJcimmfv6igMf3sNvtvyqaq9YSzwc6uskMnK4SoMKeBD7JmJ6zEN5cLqvmUrE7F3TWLG3q3FXdKFaerNTFk1aEQ5YAhjTY31TdXf2PTAZ7db4yrPcGeg7LtCeATfeoeWrBJnz26saWjAxVENiT2HeqhirJVGfY8Yj55xF28tnLemXuzVkQNikLRew52gVFk2qxXgrJjuTqdKdbeS5Y",
    "channel_id": "ch_2rv8MErgx3ok7DTQu9ZAKbK71q1FykLvDtvyhcuWtDyP3yoetD"
  }
}
```
