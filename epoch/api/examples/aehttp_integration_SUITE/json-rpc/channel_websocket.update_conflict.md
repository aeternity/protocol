
#### initiator init (2018-10-24 12:53:28.715)
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=700&initiator_id=ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ&role=initiator
```

#### responder init (2018-10-24 12:53:28.719)
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=700&initiator_id=ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY&lock_period=10&port=12340&protocol=json-rpc&push_amount=1&responder_amount=400&responder_id=ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ&role=responder
```

#### responder <--- (2018-10-24 12:53:29.721)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "undefined",
    "data": {
      "event": "channel_open"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:53:29.723)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "undefined",
    "data": {
      "event": "channel_accept"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:53:29.727)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": "undefined",
    "data": {
      "tx": "tx_3d11KjpALBGjNkDnd6KHWu5iTiKtNxx7QB3F4FAQKEUoRqgew2XUdpGzQSHzCU45vuAQtu9BwjdbpJixR7So3AVsan7KuCjyjhr7NDiNTQ75Reiaog9FiphxWu6wrqdFhLcvtZC2BQ516zK233PhbT2oNjp4QhvNJiPyPE"
    }
  }
}
```

#### initiator ---> (2018-10-24 12:53:29.749)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HnPYGvwivdY3Tev69gkSNswzMfBLcxTKXVeJJq8vsmEaetD5RXKvqjWDjwFX8tWFxusyWJj995SSo8zwHKvfHLkzngetoQGgWG3aFecrx3T9yDexLSCEs7XKmxQVKLvkj9giHg2vACbTvjwh7RXfkM9DQnprRug7SiKvveZDKkEDRCvQFiRutt6irNEtcGrrg1kP6N5VAYJpwqSBEbb7CACBfGXfo9Qm2woDxSoVpEF5iKxjP85ak2T9bCKd7s7dG"
  }
}
```

#### responder <--- (2018-10-24 12:53:29.750)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "undefined",
    "data": {
      "event": "funding_created"
    }
  }
}
```

#### responder <--- (2018-10-24 12:53:29.751)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": "undefined",
    "data": {
      "tx": "tx_3d11KjpALBGjNkDnd6KHWu5iTiKtNxx7QB3F4FAQKEUoRqgew2XUdpGzQSHzCU45vuAQtu9BwjdbpJixR7So3AVsan7KuCjyjhr7NDiNTQ75Reiaog9FiphxWu6wrqdFhLcvtZC2BQ516zK233PhbT2oNjp4QhvNJiPyPE"
    }
  }
}
```

#### responder ---> (2018-10-24 12:53:29.752)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "tx": "tx_4L9GSozvM4HkbdbyQguqxjEAe63dV4z3d7KgFrXq7fKmU3uacZ78v62wWmqV3gPFad8RXwpKNWSw7aSYpoWmG4c3VudwzvAuMX32uPRtL3KAnd5jgGZ8naNESZyi4phCGTv1u4M8k684bB3knjLKPtV6yGuKv9PPDaWN6o8VacgLuhinu4PcXm4zuQk2sSbAvyRMLWxJashWmyTk9Wh834mgEMLnz8MHXckbFkruLdjjvRMewqdTpScZMeT8YLHfqq8SeWqfVbY"
  }
}
```

#### initiator <--- (2018-10-24 12:53:29.753)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "undefined",
    "data": {
      "event": "funding_signed"
    }
  }
}
```

#### responder <--- (2018-10-24 12:53:29.754)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "undefined",
    "data": {
      "tx": "tx_6jPYBUFTkcmPEY3rQCmHLhEPahzhXqGpqs3tYhDAbrNqb8GfGWFsTKs6SQPnkY8QbFzz3zgUdPS7SmgQN1niZsfwYYQBhSubf9oD8uKM5gmN3usEA84LiAN4orQWMSD132xKCgEBd5AucUW2xLwDhNWrUipYL3ZnptteT1KyQQkcgq7zXhcK7yxqVdSXru6shUzLgbR1qfhStqZutyiCDmbW7md92SFRoj6K2zNN47aF3WM6CACwXdP6qxjgAfSXoMfcNGUAR5hWZaHT5bZqFvc7h55TX4QWU2NK4fz8tZXVsSNAs4eFuk8igTsdHD8t19JS82x14wtfpFvFQqKTN8odUyH6pwTCcok2D"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:53:29.755)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "undefined",
    "data": {
      "tx": "tx_6jPYBUFTkcmPEY3rQCmHLhEPahzhXqGpqs3tYhDAbrNqb8GfGWFsTKs6SQPnkY8QbFzz3zgUdPS7SmgQN1niZsfwYYQBhSubf9oD8uKM5gmN3usEA84LiAN4orQWMSD132xKCgEBd5AucUW2xLwDhNWrUipYL3ZnptteT1KyQQkcgq7zXhcK7yxqVdSXru6shUzLgbR1qfhStqZutyiCDmbW7md92SFRoj6K2zNN47aF3WM6CACwXdP6qxjgAfSXoMfcNGUAR5hWZaHT5bZqFvc7h55TX4QWU2NK4fz8tZXVsSNAs4eFuk8igTsdHD8t19JS82x14wtfpFvFQqKTN8odUyH6pwTCcok2D"
    }
  }
}
```

#### initiator ---> (2018-10-24 12:53:33.686)
```javascript
{
  "id": -576460752303423475,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
      "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ"
    ]
  }
}
```

#### initiator <--- (2018-10-24 12:53:33.687)
```javascript
{
  "id": -576460752303423475,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
      "balance": 699
    },
    {
      "account": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
      "balance": 401
    }
  ]
}
```

#### responder <--- (2018-10-24 12:53:35.958)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2W83zYVY911Ab8ybfaJfuYND1FQC6pBaaqpirgs2BbL9WAUvLH",
    "data": {
      "event": "own_funding_locked"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:53:35.959)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2W83zYVY911Ab8ybfaJfuYND1FQC6pBaaqpirgs2BbL9WAUvLH",
    "data": {
      "event": "own_funding_locked"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:53:35.959)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2W83zYVY911Ab8ybfaJfuYND1FQC6pBaaqpirgs2BbL9WAUvLH",
    "data": {
      "event": "funding_locked"
    }
  }
}
```

#### responder <--- (2018-10-24 12:53:35.960)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2W83zYVY911Ab8ybfaJfuYND1FQC6pBaaqpirgs2BbL9WAUvLH",
    "data": {
      "event": "funding_locked"
    }
  }
}
```

#### responder <--- (2018-10-24 12:53:35.962)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2W83zYVY911Ab8ybfaJfuYND1FQC6pBaaqpirgs2BbL9WAUvLH",
    "data": {
      "event": "open"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:53:35.962)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2W83zYVY911Ab8ybfaJfuYND1FQC6pBaaqpirgs2BbL9WAUvLH",
    "data": {
      "event": "open"
    }
  }
}
```

#### responder <--- (2018-10-24 12:53:35.963)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2W83zYVY911Ab8ybfaJfuYND1FQC6pBaaqpirgs2BbL9WAUvLH",
    "data": {
      "state": "tx_6jPYBUFTkcmPEY3rQCmHLhEPahzhXqGpqs3tYhDAbrNqb8GfGWFsTKs6SQPnkY8QbFzz3zgUdPS7SmgQN1niZsfwYYQBhSubf9oD8uKM5gmN3usEA84LiAN4orQWMSD132xKCgEBd5AucUW2xLwDhNWrUipYL3ZnptteT1KyQQkcgq7zXhcK7yxqVdSXru6shUzLgbR1qfhStqZutyiCDmbW7md92SFRoj6K2zNN47aF3WM6CACwXdP6qxjgAfSXoMfcNGUAR5hWZaHT5bZqFvc7h55TX4QWU2NK4fz8tZXVsSNAs4eFuk8igTsdHD8t19JS82x14wtfpFvFQqKTN8odUyH6pwTCcok2D"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:53:35.963)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2W83zYVY911Ab8ybfaJfuYND1FQC6pBaaqpirgs2BbL9WAUvLH",
    "data": {
      "state": "tx_6jPYBUFTkcmPEY3rQCmHLhEPahzhXqGpqs3tYhDAbrNqb8GfGWFsTKs6SQPnkY8QbFzz3zgUdPS7SmgQN1niZsfwYYQBhSubf9oD8uKM5gmN3usEA84LiAN4orQWMSD132xKCgEBd5AucUW2xLwDhNWrUipYL3ZnptteT1KyQQkcgq7zXhcK7yxqVdSXru6shUzLgbR1qfhStqZutyiCDmbW7md92SFRoj6K2zNN47aF3WM6CACwXdP6qxjgAfSXoMfcNGUAR5hWZaHT5bZqFvc7h55TX4QWU2NK4fz8tZXVsSNAs4eFuk8igTsdHD8t19JS82x14wtfpFvFQqKTN8odUyH6pwTCcok2D"
    }
  }
}
```

#### initiator: (2018-10-24 12:53:36.996)
> Funding has been confirmed locally on-chain

#### responder: (2018-10-24 12:53:36.996)
> Funding has been confirmed locally on-chain

#### initiator: (2018-10-24 12:53:36.996)
> Funding has been confirmed on-chain by other party

#### responder: (2018-10-24 12:53:36.996)
> Funding has been confirmed on-chain by other party

#### initiator: (2018-10-24 12:53:36.996)
> Channel is `open` and ready to use

#### responder: (2018-10-24 12:53:36.996)
> Channel is `open` and ready to use

#### initiator ---> (2018-10-24 12:53:37.23)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
    "to": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ"
  }
}
```

#### responder ---> (2018-10-24 12:53:37.23)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 2,
    "from": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY",
    "to": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ"
  }
}
```

#### responder <--- (2018-10-24 12:53:37.27)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2W83zYVY911Ab8ybfaJfuYND1FQC6pBaaqpirgs2BbL9WAUvLH",
    "data": {
      "tx": "tx_GB8bJXCQSjj2wdBdcJfjvQtBdJn9d2TWm2GYC8jGSNZyMRvyor8AqnP22GDzwqMzxKwkhcCxudvRNzc93uaMP2BRiCUzgudsShtgrzCzee7EbL7hrdKRRnyZE3tSGP7MK7FDX3kf7KQ6uwSzQeTBnSG1NNa8FYVzi2KDFhpt3wV6WyXiEDe5wGP6gkNhqQpjw72NELsBATYMQ9qWW6xt"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:53:37.27)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2W83zYVY911Ab8ybfaJfuYND1FQC6pBaaqpirgs2BbL9WAUvLH",
    "data": {
      "tx": "tx_GB8bJXCQSjj2wdBdcJfjvQtBdJn9d2TWm2GYC8jGSNZyMRvyor8AqnP22GDzwqMzxKwkhcCxudvRNzc93uaMP2BRiCUzgudsShtgrzCzee7EbL7hrdKRRnyZE3tSGP7MK7FDX3kf7KQ6uwSzQeTBnSG1NNa8FYVzhsjK8j8V2u8hXAzAzBqKjzjpGpX6yYBLe8MT2TZBAib1sWPjJPCz"
    }
  }
}
```

#### initiator ---> (2018-10-24 12:53:37.28)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4mxKiV8WA5jZA7b5pfwCmR3YyH7NVfr57qAXmMsBjPEdtiXLVD32kueWEyCCJfkRjQPVJuBEyDwZEAieuzWL29p88UjvFHSWYnTwGCh6JauFjAsEgmsQoszNVHo1g9t7w3LhcFmeH9wUvzzgzYjiMqmzesRrSgNmbAKC1FqvFPDNP6rE3nSCxD74njP9PFuu3eUEx13539PjSf7dAfv9S6dGyw1YjTLnh4rsd9ieofASmL5Lvud1MF72rDbbykfatVQ3mWmVBRx7R9k2wXBu4vPUdj5oQW1E2Nv7hzG1SNfxNTh"
  }
}
```

#### responder ---> (2018-10-24 12:53:37.28)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4k46cyMNz7vuN2DQBmebfLZzjDVtzATdQ122Z3tfeUdUW3Am5nrXwKfzL1ekecWUqkSB3QWNYCbvuejbxGLW8q5Vafv8tAqL1StDmKj2NkJD1FQMxSbo1VZkCxmKF73zm4dAJMHMF7gCEM3jkoo7x5W5EEntDjCTVqiwF2XcwrWAzx3UE2CEmd3xhWyjL2PRDYtJYdbb1kbNCvfnsYNQLE7n5Lgd2XKpmBpHgPpRqAmgQvw5aWFZgtxAxGyUEjZTbJ24JeoevAuypvhHPKPCcecswtkLvTGmBw3V8yohATwvvn8"
  }
}
```

#### initiator <--- (2018-10-24 12:53:37.30)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2W83zYVY911Ab8ybfaJfuYND1FQC6pBaaqpirgs2BbL9WAUvLH",
    "data": {
      "round": 1
    }
  }
}
```

#### responder <--- (2018-10-24 12:53:37.30)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2W83zYVY911Ab8ybfaJfuYND1FQC6pBaaqpirgs2BbL9WAUvLH",
    "data": {
      "round": 1
    }
  }
}
```

#### responder ---> (2018-10-24 12:53:37.30)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
    "to": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY"
  }
}
```

#### initiator ---> (2018-10-24 12:53:37.30)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 2,
    "from": "ak_2MpDC9D3cnHn5KDNuDDHSarZYZR988oqzLWHudZe9pHGE78duZ",
    "to": "ak_KcR46Qk9aEmHnWwGZLAW7u5MT3FLsxszmkx9rphLfCZoBAzFY"
  }
}
```

#### responder <--- (2018-10-24 12:53:37.34)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2W83zYVY911Ab8ybfaJfuYND1FQC6pBaaqpirgs2BbL9WAUvLH",
    "data": {
      "tx": "tx_GB8bJXCQSjj2wdBdcJfjvQtBdJn9d2TWm2GYC8jGSNZyMRvyor8AqnP22GDzwqMzxKwkhcojFAMNhvdpDHm6u3EDxxc8tCF5D1z8dVJqCZzXM8fYcazpAxHUFGChRz62sLiUktYvphmzRFxrPyMzG7Lq262jYJWJyEvfbAmmgU9Qte4b8mp2AWY6v6sRVXEwa9UXVJVrHq2eKuHiKLgP"
    }
  }
}
```

#### initiator <--- (2018-10-24 12:53:37.35)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2W83zYVY911Ab8ybfaJfuYND1FQC6pBaaqpirgs2BbL9WAUvLH",
    "data": {
      "tx": "tx_GB8bJXCQSjj2wdBdcJfjvQtBdJn9d2TWm2GYC8jGSNZyMRvyor8AqnP22GDzwqMzxKwkhcojFAMNhvdpDHm6u3EDxxc8tCF5D1z8dVJqCZzXM8fYcazpAxHUFGChRz62sLiUktYvphmzRFxrPyMzG7Lq262jYJWJyPVNPCcKh3gbs374Dcx8joLGoBDXLoygtLMfYdzNWkmtZD1MwbHN"
    }
  }
}
```

#### responder ---> (2018-10-24 12:53:37.35)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak55Xrk1Wdvq3UqKiGoLg31hchy2QswDEVwgSvjJpdgtm4dC7Wb1YayVZ2c6SzQfGyM5FQemMC3PLjNC2Rmjf517oQ32o7XkpFaopEHrXmzD3MDn9aPSrnPhSBWkkYBKLNWA6kieoxwsrMEb3W2v5BzhsQLWTde8ioQVTVd65GHmg8sJzxmDnz6r2vbuHw4SAbA1JZw2YXEYFRDHYdVZwQVfT6s8LJadVETRNr4qQk1rZp6pi7ADTeXgLWQGV4EAjEYm23fF9tmAJTSpVmWdcuh7tmZsELUHjkf3hd1KfAwDdhi5u"
  }
}
```

#### initiator ---> (2018-10-24 12:53:37.36)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_LHMmG11Rak4xVg1vtjPFmCX7QWTUADkpHPy9DPMiVxQrKoeKoj4Yryq3FXmXCY5AquzTyuzXYuKAUZ5SjZ22PDwHhwF4fkSWQKBCJVvJJpd4K5JTJ86uKKp8UJwhrkozjGR6PKTAy7pfdZ9cqwRaV4c4EaR4vYAnJ1mevtPDqAnLvBapms3YtXtudaYAiUzFiqbpM9qugwvejyD1KrvLXwYAXqRddbA1DJMQzKpdkfos7i4yRwpGhkKTqh3UBH46sRhmJUE6mme3FurKHFMzCPFgfhypDEpTV6hf1Apkpbdua86qk5rVYdSWY"
  }
}
```

#### initiator <--- (2018-10-24 12:53:37.37)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2W83zYVY911Ab8ybfaJfuYND1FQC6pBaaqpirgs2BbL9WAUvLH",
    "data": {
      "round": 1
    }
  }
}
```

#### responder <--- (2018-10-24 12:53:37.38)
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2W83zYVY911Ab8ybfaJfuYND1FQC6pBaaqpirgs2BbL9WAUvLH",
    "data": {
      "round": 1
    }
  }
}
```
