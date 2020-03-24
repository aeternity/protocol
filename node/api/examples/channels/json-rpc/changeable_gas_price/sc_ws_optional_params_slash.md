
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_mVVD7Z30ychIKGr6Wu2ZNvqRN1L24wJdDy2X0BZAb282UkIj"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_vXxsUjq6xDqszjT3eEIWhDFWSeYy4/apz4rK5QdsikZZyyMz"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtdJG1hww==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422519,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAnY6JOkv2iX5rAobbGtyrYzHVcUoOdpkoSMFf02pZiu3PRSyrKCB+X+Rcndn+uCOkPVTasaN6Rxt6Fozw4i4wDuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LXZUjqlM="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422519,
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "fsm_id": "ba_vXxsUjq6xDqszjT3eEIWhDFWSeYy4/apz4rK5QdsikZZyyMz",
      "signed_tx": "tx_+MsLAfhCuEAnY6JOkv2iX5rAobbGtyrYzHVcUoOdpkoSMFf02pZiu3PRSyrKCB+X+Rcndn+uCOkPVTasaN6Rxt6Fozw4i4wDuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LXZUjqlM=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422518,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAJ2OiTpL9ol+awKG2xrcq2Mx1XFKDnaZKEjBX9NqWYrtz0Usqyggfl/kXJ3Z/rgjpD1U2rGjekcbehaM8OIuMA7hAr0oLSHvyPNS+30TijhEk/rPAqqzbTAOE60vY724EBR4+EAKnqmphe6jGJu02DbVxm7ZSxfLJaYfDeMnCsi60CLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC12OPPan"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
  "id": -576460752303422518,
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAJ2OiTpL9ol+awKG2xrcq2Mx1XFKDnaZKEjBX9NqWYrtz0Usqyggfl/kXJ3Z/rgjpD1U2rGjekcbehaM8OIuMA7hAr0oLSHvyPNS+30TijhEk/rPAqqzbTAOE60vY724EBR4+EAKnqmphe6jGJu02DbVxm7ZSxfLJaYfDeMnCsi60CLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC12OPPan",
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_mVVD7Z30ychIKGr6Wu2ZNvqRN1L24wJdDy2X0BZAb282UkIj"
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAJ2OiTpL9ol+awKG2xrcq2Mx1XFKDnaZKEjBX9NqWYrtz0Usqyggfl/kXJ3Z/rgjpD1U2rGjekcbehaM8OIuMA7hAr0oLSHvyPNS+30TijhEk/rPAqqzbTAOE60vY724EBR4+EAKnqmphe6jGJu02DbVxm7ZSxfLJaYfDeMnCsi60CLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC12OPPan",
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAJ2OiTpL9ol+awKG2xrcq2Mx1XFKDnaZKEjBX9NqWYrtz0Usqyggfl/kXJ3Z/rgjpD1U2rGjekcbehaM8OIuMA7hAr0oLSHvyPNS+30TijhEk/rPAqqzbTAOE60vY724EBR4+EAKnqmphe6jGJu02DbVxm7ZSxfLJaYfDeMnCsi60CLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC12OPPan",
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAJ2OiTpL9ol+awKG2xrcq2Mx1XFKDnaZKEjBX9NqWYrtz0Usqyggfl/kXJ3Z/rgjpD1U2rGjekcbehaM8OIuMA7hAr0oLSHvyPNS+30TijhEk/rPAqqzbTAOE60vY724EBR4+EAKnqmphe6jGJu02DbVxm7ZSxfLJaYfDeMnCsi60CLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC12OPPan",
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "message": {
        "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "message": {
        "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello back",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422517,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
  "id": -576460752303422517,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999999
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "state": "tx_+QENCwH4hLhAJ2OiTpL9ol+awKG2xrcq2Mx1XFKDnaZKEjBX9NqWYrtz0Usqyggfl/kXJ3Z/rgjpD1U2rGjekcbehaM8OIuMA7hAr0oLSHvyPNS+30TijhEk/rPAqqzbTAOE60vY724EBR4+EAKnqmphe6jGJu02DbVxm7ZSxfLJaYfDeMnCsi60CLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC12OPPan"
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "state": "tx_+QENCwH4hLhAJ2OiTpL9ol+awKG2xrcq2Mx1XFKDnaZKEjBX9NqWYrtz0Usqyggfl/kXJ3Z/rgjpD1U2rGjekcbehaM8OIuMA7hAr0oLSHvyPNS+30TijhEk/rPAqqzbTAOE60vY724EBR4+EAKnqmphe6jGJu02DbVxm7ZSxfLJaYfDeMnCsi60CLiD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC12OPPan"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "poi": "pi_+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMBXVz9I"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422516,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
  "id": -576460752303422516,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999999
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
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
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBsJdUaSRZtMT17ecxng5AZEIbQSFSn3z/8274RM7j0qXAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAut3Q7M=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "id": -576460752303422515,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC3wjhqonweXzoIKfIu7DficVvhMkiuZ5P+mluvpVmuWJCH7clnIY4JJvr2PgfGVrFRJbC0OAvaXQPgFlSg9UMPuEj4RjkCoQbCXVGkkWbTE9e3nMZ4OQGRCG0EhUp98//Nu+ETO49KlwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgL2S18G"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
  "id": -576460752303422515,
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC3wjhqonweXzoIKfIu7DficVvhMkiuZ5P+mluvpVmuWJCH7clnIY4JJvr2PgfGVrFRJbC0OAvaXQPgFlSg9UMPuEj4RjkCoQbCXVGkkWbTE9e3nMZ4OQGRCG0EhUp98//Nu+ETO49KlwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgL2S18G",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "id": -576460752303422514,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBgGjoLcmUWO/TR3w6PmXDrLAJ+Ql/Nag0/S59PbfTBFY/6ceMi73eJJHtHItPPHi+1/OgLihOs33OL5j3aEZcGuEC3wjhqonweXzoIKfIu7DficVvhMkiuZ5P+mluvpVmuWJCH7clnIY4JJvr2PgfGVrFRJbC0OAvaXQPgFlSg9UMPuEj4RjkCoQbCXVGkkWbTE9e3nMZ4OQGRCG0EhUp98//Nu+ETO49KlwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKArG8R"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
  "id": -576460752303422514,
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "state": "tx_+NILAfiEuEBgGjoLcmUWO/TR3w6PmXDrLAJ+Ql/Nag0/S59PbfTBFY/6ceMi73eJJHtHItPPHi+1/OgLihOs33OL5j3aEZcGuEC3wjhqonweXzoIKfIu7DficVvhMkiuZ5P+mluvpVmuWJCH7clnIY4JJvr2PgfGVrFRJbC0OAvaXQPgFlSg9UMPuEj4RjkCoQbCXVGkkWbTE9e3nMZ4OQGRCG0EhUp98//Nu+ETO49KlwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKArG8R"
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "state": "tx_+NILAfiEuEBgGjoLcmUWO/TR3w6PmXDrLAJ+Ql/Nag0/S59PbfTBFY/6ceMi73eJJHtHItPPHi+1/OgLihOs33OL5j3aEZcGuEC3wjhqonweXzoIKfIu7DficVvhMkiuZ5P+mluvpVmuWJCH7clnIY4JJvr2PgfGVrFRJbC0OAvaXQPgFlSg9UMPuEj4RjkCoQbCXVGkkWbTE9e3nMZ4OQGRCG0EhUp98//Nu+ETO49KlwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKArG8R"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422513,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
  "id": -576460752303422513,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999998
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422512,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
  "id": -576460752303422512,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBgGjoLcmUWO/TR3w6PmXDrLAJ+Ql/Nag0/S59PbfTBFY/6ceMi73eJJHtHItPPHi+1/OgLihOs33OL5j3aEZcGuEC3wjhqonweXzoIKfIu7DficVvhMkiuZ5P+mluvpVmuWJCH7clnIY4JJvr2PgfGVrFRJbC0OAvaXQPgFlSg9UMPuEj4RjkCoQbCXVGkkWbTE9e3nMZ4OQGRCG0EhUp98//Nu+ETO49KlwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKArG8R",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBgGjoLcmUWO/TR3w6PmXDrLAJ+Ql/Nag0/S59PbfTBFY/6ceMi73eJJHtHItPPHi+1/OgLihOs33OL5j3aEZcGuEC3wjhqonweXzoIKfIu7DficVvhMkiuZ5P+mluvpVmuWJCH7clnIY4JJvr2PgfGVrFRJbC0OAvaXQPgFlSg9UMPuEj4RjkCoQbCXVGkkWbTE9e3nMZ4OQGRCG0EhUp98//Nu+ETO49KlwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKArG8R",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "event": "closing"
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBgGjoLcmUWO/TR3w6PmXDrLAJ+Ql/Nag0/S59PbfTBFY/6ceMi73eJJHtHItPPHi+1/OgLihOs33OL5j3aEZcGuEC3wjhqonweXzoIKfIu7DficVvhMkiuZ5P+mluvpVmuWJCH7clnIY4JJvr2PgfGVrFRJbC0OAvaXQPgFlSg9UMPuEj4RjkCoQbCXVGkkWbTE9e3nMZ4OQGRCG0EhUp98//Nu+ETO49KlwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKArG8R",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "event": "closing"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422511,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {
    "gas_price": 1000001234
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
  "id": -576460752303422511,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBsJdUaSRZtMT17ecxng5AZEIbQSFSn3z/8274RM7j0qXoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuEBgGjoLcmUWO/TR3w6PmXDrLAJ+Ql/Nag0/S59PbfTBFY/6ceMi73eJJHtHItPPHi+1/OgLihOs33OL5j3aEZcGuEC3wjhqonweXzoIKfIu7DficVvhMkiuZ5P+mluvpVmuWJCH7clnIY4JJvr2PgfGVrFRJbC0OAvaXQPgFlSg9UMPuEj4RjkCoQbCXVGkkWbTE9e3nMZ4OQGRCG0EhUp98//Nu+ETO49KlwKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgK5AUz5AUk8AfkBP/kBPKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfkBGPhPoA14eXtmmtAgLMK7im7vnzMyk+SGhjFI+PP0nFl1fwFz7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/vhPoKtpUvm9rk5XNeVeyl7wSwAT/ak5C0vFtqH2/EVPjkIA7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAvh0oN3FBkIf34tjXkNZtc8R2KYnFXRfwm1j0hrMi/Rgu+IJ+FGAgICAgKCraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAICAgICAoA14eXtmmtAgLMK7im7vnzMyk+SGhjFI+PP0nFl1fwFzgICAgIDAwMDAwACGGR7KUfkIX9VEbmg=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.slash_sign",
  "params": {
    "signed_tx": "tx_+QLACwH4QrhAd5Tj+4uUNdr9+q24bt1VdyiQyBk/bf9QBqyVHLMiTGiKQgeyWSIGS4jmRvbHz0LO6LWqJhCygfSVcEJsAgbrArkCd/kCdDcBoQbCXVGkkWbTE9e3nMZ4OQGRCG0EhUp98//Nu+ETO49Kl6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAYBo6C3JlFjv00d8Oj5lw6ywCfkJfzWoNP0ufT230wRWP+nHjIu93iSR7RyLTzx4vtfzoC4oTrN9zi+Y92hGXBrhAt8I4aqJ8Hl86CCnyLuw34nFb4TJIrmeT/ppbr6VZrliQh+3JZyGOCSb69j4HxlaxUSWwtDgL2l0D4BZUoPVDD7hI+EY5AqEGwl1RpJFm0xPXt5zGeDkBkQhtBIVKffP/zbvhEzuPSpcCoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhhkeylH5CF9QkjjQ"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAd5Tj+4uUNdr9+q24bt1VdyiQyBk/bf9QBqyVHLMiTGiKQgeyWSIGS4jmRvbHz0LO6LWqJhCygfSVcEJsAgbrArkCd/kCdDcBoQbCXVGkkWbTE9e3nMZ4OQGRCG0EhUp98//Nu+ETO49Kl6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAYBo6C3JlFjv00d8Oj5lw6ywCfkJfzWoNP0ufT230wRWP+nHjIu93iSR7RyLTzx4vtfzoC4oTrN9zi+Y92hGXBrhAt8I4aqJ8Hl86CCnyLuw34nFb4TJIrmeT/ppbr6VZrliQh+3JZyGOCSb69j4HxlaxUSWwtDgL2l0D4BZUoPVDD7hI+EY5AqEGwl1RpJFm0xPXt5zGeDkBkQhtBIVKffP/zbvhEzuPSpcCoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhhkeylH5CF9QkjjQ",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAd5Tj+4uUNdr9+q24bt1VdyiQyBk/bf9QBqyVHLMiTGiKQgeyWSIGS4jmRvbHz0LO6LWqJhCygfSVcEJsAgbrArkCd/kCdDcBoQbCXVGkkWbTE9e3nMZ4OQGRCG0EhUp98//Nu+ETO49Kl6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9a41PjSCwH4hLhAYBo6C3JlFjv00d8Oj5lw6ywCfkJfzWoNP0ufT230wRWP+nHjIu93iSR7RyLTzx4vtfzoC4oTrN9zi+Y92hGXBrhAt8I4aqJ8Hl86CCnyLuw34nFb4TJIrmeT/ppbr6VZrliQh+3JZyGOCSb69j4HxlaxUSWwtDgL2l0D4BZUoPVDD7hI+EY5AqEGwl1RpJFm0xPXt5zGeDkBkQhtBIVKffP/zbvhEzuPSpcCoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhhkeylH5CF9QkjjQ",
      "type": "channel_slash_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBsJdUaSRZtMT17ecxng5AZEIbQSFSn3z/8274RM7j0qXoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/6GJGE5yoACAIYPXtZ/KAAn0CiUHg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuECVOy2M1y6tGyj+WryX+oleR6tTiGGPmc+pLFcy2pYhvxx4xCWMKICFKXwoCvSeyS5JsQrqEXuKuWWrAxP0eFMPuF/4XTgBoQbCXVGkkWbTE9e3nMZ4OQGRCG0EhUp98//Nu+ETO49Kl6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAJy9v5z0="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECVOy2M1y6tGyj+WryX+oleR6tTiGGPmc+pLFcy2pYhvxx4xCWMKICFKXwoCvSeyS5JsQrqEXuKuWWrAxP0eFMPuF/4XTgBoQbCXVGkkWbTE9e3nMZ4OQGRCG0EhUp98//Nu+ETO49Kl6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAJy9v5z0=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuECVOy2M1y6tGyj+WryX+oleR6tTiGGPmc+pLFcy2pYhvxx4xCWMKICFKXwoCvSeyS5JsQrqEXuKuWWrAxP0eFMPuF/4XTgBoQbCXVGkkWbTE9e3nMZ4OQGRCG0EhUp98//Nu+ETO49Kl6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAJy9v5z0=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "event": "closed_confirmed"
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "event": "died"
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "event": "closed_confirmed"
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
    "channel_id": "ch_2UbnJDB1V61noNZEhWapJw93p3LQmgwS8rpa8c3YtJ28zzqRj2",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=initiator
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_2vQKJwWgPyO9NCXLRkS/l+U40bVnPAZsk0hHdT6EkQte7Kcm"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W&role=responder
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_V/kFLwZVdty4l0kxAsrdtd9O3CHYeL0nu0VSIVod60vd1cfp"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhAGeddIAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgtgcQyAaw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422510,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAors5wNao/b4XyeyM4FxDtAbnNmIjiap/rg6YFzMDxas5KvhNpjjLYSAw4INs2so5ax8slnhRi6seurEmAquoLuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LYJeTdXI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422510,
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "fsm_id": "ba_V/kFLwZVdty4l0kxAsrdtd9O3CHYeL0nu0VSIVod60vd1cfp",
      "signed_tx": "tx_+MsLAfhCuEAors5wNao/b4XyeyM4FxDtAbnNmIjiap/rg6YFzMDxas5KvhNpjjLYSAw4INs2so5ax8slnhRi6seurEmAquoLuIP4gTIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQBnnXSADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LYJeTdXI=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422509,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAKK7OcDWqP2+F8nsjOBcQ7QG5zZiI4mqf64OmBczA8WrOSr4TaY4y2EgMOCDbNrKOWsfLJZ4UYurHrqxJgKrqC7hAv7SUhSkF34qe8SPwc3IteB+TDYZQMoPglAN+z51HXUl8ju//PdUs5TUqg4MrBULGR9Lujl8LtmxNLGkeg3CxC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2DQXm1z"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
  "id": -576460752303422509,
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAKK7OcDWqP2+F8nsjOBcQ7QG5zZiI4mqf64OmBczA8WrOSr4TaY4y2EgMOCDbNrKOWsfLJZ4UYurHrqxJgKrqC7hAv7SUhSkF34qe8SPwc3IteB+TDYZQMoPglAN+z51HXUl8ju//PdUs5TUqg4MrBULGR9Lujl8LtmxNLGkeg3CxC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2DQXm1z",
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_2vQKJwWgPyO9NCXLRkS/l+U40bVnPAZsk0hHdT6EkQte7Kcm"
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAKK7OcDWqP2+F8nsjOBcQ7QG5zZiI4mqf64OmBczA8WrOSr4TaY4y2EgMOCDbNrKOWsfLJZ4UYurHrqxJgKrqC7hAv7SUhSkF34qe8SPwc3IteB+TDYZQMoPglAN+z51HXUl8ju//PdUs5TUqg4MrBULGR9Lujl8LtmxNLGkeg3CxC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2DQXm1z",
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAKK7OcDWqP2+F8nsjOBcQ7QG5zZiI4mqf64OmBczA8WrOSr4TaY4y2EgMOCDbNrKOWsfLJZ4UYurHrqxJgKrqC7hAv7SUhSkF34qe8SPwc3IteB+TDYZQMoPglAN+z51HXUl8ju//PdUs5TUqg4MrBULGR9Lujl8LtmxNLGkeg3CxC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2DQXm1z",
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAKK7OcDWqP2+F8nsjOBcQ7QG5zZiI4mqf64OmBczA8WrOSr4TaY4y2EgMOCDbNrKOWsfLJZ4UYurHrqxJgKrqC7hAv7SUhSkF34qe8SPwc3IteB+TDYZQMoPglAN+z51HXUl8ju//PdUs5TUqg4MrBULGR9Lujl8LtmxNLGkeg3CxC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2DQXm1z",
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "message": {
        "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "message": {
        "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello back",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422508,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
  "id": -576460752303422508,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999999
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "state": "tx_+QENCwH4hLhAKK7OcDWqP2+F8nsjOBcQ7QG5zZiI4mqf64OmBczA8WrOSr4TaY4y2EgMOCDbNrKOWsfLJZ4UYurHrqxJgKrqC7hAv7SUhSkF34qe8SPwc3IteB+TDYZQMoPglAN+z51HXUl8ju//PdUs5TUqg4MrBULGR9Lujl8LtmxNLGkeg3CxC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2DQXm1z"
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Channel is `open` and ready to use

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "state": "tx_+QENCwH4hLhAKK7OcDWqP2+F8nsjOBcQ7QG5zZiI4mqf64OmBczA8WrOSr4TaY4y2EgMOCDbNrKOWsfLJZ4UYurHrqxJgKrqC7hAv7SUhSkF34qe8SPwc3IteB+TDYZQMoPglAN+z51HXUl8ju//PdUs5TUqg4MrBULGR9Lujl8LtmxNLGkeg3CxC7iD+IEyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAZ510gAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC2DQXm1z"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.get.poi.reply",
  "params": {
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "poi": "pi_+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMBXVz9I"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422507,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
  "id": -576460752303422507,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999999
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
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
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBsJHGTeLaKBhlyB7rXIO78j9bnnCxeribG7ZpkW07uyKAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAqLypnQ=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "id": -576460752303422506,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDj+I5wk8rgKF7LHOCIMDOKOKbyH7BGstnkFZ748CrLBhe84X6xqXNATMyo/hqlW64kVle+6szJkUjVMLM1vuYNuEj4RjkCoQbCRxk3i2igYZcge61yDu/I/W55wsXq4mxu2aZFtO7sigKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIFnVPu"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
  "id": -576460752303422506,
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDj+I5wk8rgKF7LHOCIMDOKOKbyH7BGstnkFZ748CrLBhe84X6xqXNATMyo/hqlW64kVle+6szJkUjVMLM1vuYNuEj4RjkCoQbCRxk3i2igYZcge61yDu/I/W55wsXq4mxu2aZFtO7sigKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgIFnVPu",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "id": -576460752303422505,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDHHVrYJ7foBVhZB2ps+8Z2jlPzHMDqCAIZV0eX+zcqdS0auvzg4CCCXWS1x9++VVkc+7VWSYHBrt4pE3x6OowIuEDj+I5wk8rgKF7LHOCIMDOKOKbyH7BGstnkFZ748CrLBhe84X6xqXNATMyo/hqlW64kVle+6szJkUjVMLM1vuYNuEj4RjkCoQbCRxk3i2igYZcge61yDu/I/W55wsXq4mxu2aZFtO7sigKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLNCEda"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
  "id": -576460752303422505,
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "state": "tx_+NILAfiEuEDHHVrYJ7foBVhZB2ps+8Z2jlPzHMDqCAIZV0eX+zcqdS0auvzg4CCCXWS1x9++VVkc+7VWSYHBrt4pE3x6OowIuEDj+I5wk8rgKF7LHOCIMDOKOKbyH7BGstnkFZ748CrLBhe84X6xqXNATMyo/hqlW64kVle+6szJkUjVMLM1vuYNuEj4RjkCoQbCRxk3i2igYZcge61yDu/I/W55wsXq4mxu2aZFtO7sigKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLNCEda"
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "state": "tx_+NILAfiEuEDHHVrYJ7foBVhZB2ps+8Z2jlPzHMDqCAIZV0eX+zcqdS0auvzg4CCCXWS1x9++VVkc+7VWSYHBrt4pE3x6OowIuEDj+I5wk8rgKF7LHOCIMDOKOKbyH7BGstnkFZ748CrLBhe84X6xqXNATMyo/hqlW64kVle+6szJkUjVMLM1vuYNuEj4RjkCoQbCRxk3i2igYZcge61yDu/I/W55wsXq4mxu2aZFtO7sigKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLNCEda"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422504,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
  "id": -576460752303422504,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999998
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422503,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
  "id": -576460752303422503,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDHHVrYJ7foBVhZB2ps+8Z2jlPzHMDqCAIZV0eX+zcqdS0auvzg4CCCXWS1x9++VVkc+7VWSYHBrt4pE3x6OowIuEDj+I5wk8rgKF7LHOCIMDOKOKbyH7BGstnkFZ748CrLBhe84X6xqXNATMyo/hqlW64kVle+6szJkUjVMLM1vuYNuEj4RjkCoQbCRxk3i2igYZcge61yDu/I/W55wsXq4mxu2aZFtO7sigKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLNCEda",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEDHHVrYJ7foBVhZB2ps+8Z2jlPzHMDqCAIZV0eX+zcqdS0auvzg4CCCXWS1x9++VVkc+7VWSYHBrt4pE3x6OowIuEDj+I5wk8rgKF7LHOCIMDOKOKbyH7BGstnkFZ748CrLBhe84X6xqXNATMyo/hqlW64kVle+6szJkUjVMLM1vuYNuEj4RjkCoQbCRxk3i2igYZcge61yDu/I/W55wsXq4mxu2aZFtO7sigKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLNCEda",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "event": "closing"
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEDHHVrYJ7foBVhZB2ps+8Z2jlPzHMDqCAIZV0eX+zcqdS0auvzg4CCCXWS1x9++VVkc+7VWSYHBrt4pE3x6OowIuEDj+I5wk8rgKF7LHOCIMDOKOKbyH7BGstnkFZ748CrLBhe84X6xqXNATMyo/hqlW64kVle+6szJkUjVMLM1vuYNuEj4RjkCoQbCRxk3i2igYZcge61yDu/I/W55wsXq4mxu2aZFtO7sigKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgLNCEda",
      "type": "channel_offchain_tx"
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "event": "closing"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422502,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {
    "gas_price": 1000001234
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
  "id": -576460752303422502,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBsJHGTeLaKBhlyB7rXIO78j9bnnCxeribG7ZpkW07uyKoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8LjU+NILAfiEuEDHHVrYJ7foBVhZB2ps+8Z2jlPzHMDqCAIZV0eX+zcqdS0auvzg4CCCXWS1x9++VVkc+7VWSYHBrt4pE3x6OowIuEDj+I5wk8rgKF7LHOCIMDOKOKbyH7BGstnkFZ748CrLBhe84X6xqXNATMyo/hqlW64kVle+6szJkUjVMLM1vuYNuEj4RjkCoQbCRxk3i2igYZcge61yDu/I/W55wsXq4mxu2aZFtO7sigKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgK5AUz5AUk8AfkBP/kBPKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfkBGPhPoA14eXtmmtAgLMK7im7vnzMyk+SGhjFI+PP0nFl1fwFz7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/vhPoKtpUvm9rk5XNeVeyl7wSwAT/ak5C0vFtqH2/EVPjkIA7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAvh0oN3FBkIf34tjXkNZtc8R2KYnFXRfwm1j0hrMi/Rgu+IJ+FGAgICAgKCraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAICAgICAoA14eXtmmtAgLMK7im7vnzMyk+SGhjFI+PP0nFl1fwFzgICAgIDAwMDAwACGGR7KUfkIKK7sbC8=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.slash_sign",
  "params": {
    "signed_tx": "tx_+QLACwH4QrhAxAXn0Cllw40ukxxX59o7OQN0Wm3zzCQhZJXXTMjp8YITW+vz7vapwv5oxw/uMLrcXY8wELSodihmjUCulFXZArkCd/kCdDcBoQbCRxk3i2igYZcge61yDu/I/W55wsXq4mxu2aZFtO7siqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAxx1a2Ce36AVYWQdqbPvGdo5T8xzA6ggCGVdHl/s3KnUtGrr84OAggl1ktcffvlVZHPu1VkmBwa7eKRN8ejqMCLhA4/iOcJPK4CheyxzgiDAzijim8h+wRrLZ5BWe+PAqywYXvOF+salzQEzMqP4apVuuJFZXvurMyZFI1TCzNb7mDbhI+EY5AqEGwkcZN4tooGGXIHutcg7vyP1uecLF6uJsbtmmRbTu7IoCoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhhkeylH5CChxmkhc"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAxAXn0Cllw40ukxxX59o7OQN0Wm3zzCQhZJXXTMjp8YITW+vz7vapwv5oxw/uMLrcXY8wELSodihmjUCulFXZArkCd/kCdDcBoQbCRxk3i2igYZcge61yDu/I/W55wsXq4mxu2aZFtO7siqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAxx1a2Ce36AVYWQdqbPvGdo5T8xzA6ggCGVdHl/s3KnUtGrr84OAggl1ktcffvlVZHPu1VkmBwa7eKRN8ejqMCLhA4/iOcJPK4CheyxzgiDAzijim8h+wRrLZ5BWe+PAqywYXvOF+salzQEzMqP4apVuuJFZXvurMyZFI1TCzNb7mDbhI+EY5AqEGwkcZN4tooGGXIHutcg7vyP1uecLF6uJsbtmmRbTu7IoCoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhhkeylH5CChxmkhc",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAxAXn0Cllw40ukxxX59o7OQN0Wm3zzCQhZJXXTMjp8YITW+vz7vapwv5oxw/uMLrcXY8wELSodihmjUCulFXZArkCd/kCdDcBoQbCRxk3i2igYZcge61yDu/I/W55wsXq4mxu2aZFtO7siqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvC41PjSCwH4hLhAxx1a2Ce36AVYWQdqbPvGdo5T8xzA6ggCGVdHl/s3KnUtGrr84OAggl1ktcffvlVZHPu1VkmBwa7eKRN8ejqMCLhA4/iOcJPK4CheyxzgiDAzijim8h+wRrLZ5BWe+PAqywYXvOF+salzQEzMqP4apVuuJFZXvurMyZFI1TCzNb7mDbhI+EY5AqEGwkcZN4tooGGXIHutcg7vyP1uecLF6uJsbtmmRbTu7IoCoI7BomY6GnI+7GEiRJ7lxG4Vf8QC+KwQr1YcgDUHOh4CuQFM+QFJPAH5AT/5ATyg3cUGQh/fi2NeQ1m1zxHYpicVdF/CbWPSGsyL9GC74gn5ARj4T6ANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX/74T6CraVL5va5OVzXlXspe8EsAE/2pOQtLxbah9vxFT45CAO2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAL4dKDdxQZCH9+LY15DWbXPEdimJxV0X8JtY9IazIv0YLviCfhRgICAgICgq2lS+b2uTlc15V7KXvBLABP9qTkLS8W2ofb8RU+OQgCAgICAgKANeHl7ZprQICzCu4pu758zMpPkhoYxSPjz9JxZdX8Bc4CAgICAwMDAwMAAhhkeylH5CChxmkhc",
      "type": "channel_slash_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBsJHGTeLaKBhlyB7rXIO78j9bnnCxeribG7ZpkW07uyKoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/6GJGE5yoACAIYPXtZ/KAAp+XMEng==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEDdqNetL0JQmHzvEEExryg3gHBMUx0NSSN3sQZWnDELTGhoxZlfyYOaOW1tyXEf6WptF45OpGb5UOM9NPzFdtwOuF/4XTgBoQbCRxk3i2igYZcge61yDu/I/W55wsXq4mxu2aZFtO7siqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAKWKkiUM="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDdqNetL0JQmHzvEEExryg3gHBMUx0NSSN3sQZWnDELTGhoxZlfyYOaOW1tyXEf6WptF45OpGb5UOM9NPzFdtwOuF/4XTgBoQbCRxk3i2igYZcge61yDu/I/W55wsXq4mxu2aZFtO7siqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAKWKkiUM=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDdqNetL0JQmHzvEEExryg3gHBMUx0NSSN3sQZWnDELTGhoxZlfyYOaOW1tyXEf6WptF45OpGb5UOM9NPzFdtwOuF/4XTgBoQbCRxk3i2igYZcge61yDu/I/W55wsXq4mxu2aZFtO7siqEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGP6olIl/+hiRhOcqAAgCGD17WfygAKWKkiUM=",
      "type": "channel_settle_tx"
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "event": "closed_confirmed"
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "event": "died"
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "event": "closed_confirmed"
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
    "channel_id": "ch_2UZZhiRDwfCyaHNwUWaEFePEHyyfGWvFuG3HCJTwFh5mqw3qA2",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
