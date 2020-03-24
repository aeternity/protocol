
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
      "fsm_id": "ba_P1NTZ7Qi/oIWcz4vnBZOawHgHasJHXqRAS8rR8RRCnG/Owo6"
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
      "fsm_id": "ba_Yac84SUEKBjY/+vUO1vlvxkU1cHcFFIlT+M8m78YpRDPCjow"
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
      "signed_tx": "tx_+IkLAcC4hPiCMgGhAbHK1UrKbrlQsMI3Yjl98MiDcLOw7duG4FDH+F2sz2/Whj+qJSJgAKEBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCGJGE5yoAAAgoAhhALIe8QAMCgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguBwp0NEFc=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421976,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEAvyCIF/W3rmIXimCOKFamekAW9s7H4zVSjazW6N5wlQV78knwN+CXnVERZvChMTv/UKmCKefvmy4NphUjeNeANuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgcKKBUCF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421976,
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
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
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
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
    "data": {
      "fsm_id": "ba_Yac84SUEKBjY/+vUO1vlvxkU1cHcFFIlT+M8m78YpRDPCjow",
      "signed_tx": "tx_+MwLAfhCuEAvyCIF/W3rmIXimCOKFamekAW9s7H4zVSjazW6N5wlQV78knwN+CXnVERZvChMTv/UKmCKefvmy4NphUjeNeANuIT4gjIBoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiYAChAVCH8UTApf48L0bqFmxZoSIoPJu8emx9L1iwY+YtP8LwhiRhOcqAAAIKAIYQCyHvEADAoCQ1gQA9dV8IiTDFS15mSWHepK29dnTghtzQ9SR14Q4LgcKKBUCF",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421975,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAL8giBf1t65iF4pgjihWpnpAFvbOx+M1Uo2s1ujecJUFe/JJ8Dfgl51REWbwoTE7/1Cpginn75suDaYVI3jXgDbhA+w1fkNNVUt7GY8YVFPlUGj+nMBQN/yV7zFLDFrzWOdWNDsYaVykJrkZjG4V9KazK00tAiSB/2o11CnucWT6HCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HCRiY88g=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
  "id": -576460752303421975,
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
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAL8giBf1t65iF4pgjihWpnpAFvbOx+M1Uo2s1ujecJUFe/JJ8Dfgl51REWbwoTE7/1Cpginn75suDaYVI3jXgDbhA+w1fkNNVUt7GY8YVFPlUGj+nMBQN/yV7zFLDFrzWOdWNDsYaVykJrkZjG4V9KazK00tAiSB/2o11CnucWT6HCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HCRiY88g==",
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
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_P1NTZ7Qi/oIWcz4vnBZOawHgHasJHXqRAS8rR8RRCnG/Owo6"
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
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAL8giBf1t65iF4pgjihWpnpAFvbOx+M1Uo2s1ujecJUFe/JJ8Dfgl51REWbwoTE7/1Cpginn75suDaYVI3jXgDbhA+w1fkNNVUt7GY8YVFPlUGj+nMBQN/yV7zFLDFrzWOdWNDsYaVykJrkZjG4V9KazK00tAiSB/2o11CnucWT6HCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HCRiY88g==",
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
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAL8giBf1t65iF4pgjihWpnpAFvbOx+M1Uo2s1ujecJUFe/JJ8Dfgl51REWbwoTE7/1Cpginn75suDaYVI3jXgDbhA+w1fkNNVUt7GY8YVFPlUGj+nMBQN/yV7zFLDFrzWOdWNDsYaVykJrkZjG4V9KazK00tAiSB/2o11CnucWT6HCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HCRiY88g==",
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
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAL8giBf1t65iF4pgjihWpnpAFvbOx+M1Uo2s1ujecJUFe/JJ8Dfgl51REWbwoTE7/1Cpginn75suDaYVI3jXgDbhA+w1fkNNVUt7GY8YVFPlUGj+nMBQN/yV7zFLDFrzWOdWNDsYaVykJrkZjG4V9KazK00tAiSB/2o11CnucWT6HCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HCRiY88g==",
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
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
    "data": {
      "message": {
        "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
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
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
    "data": {
      "message": {
        "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
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
  "id": -576460752303421974,
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
  "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
  "id": -576460752303421974,
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
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
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
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
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
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
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
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
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
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
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
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
    "data": {
      "state": "tx_+QEOCwH4hLhAL8giBf1t65iF4pgjihWpnpAFvbOx+M1Uo2s1ujecJUFe/JJ8Dfgl51REWbwoTE7/1Cpginn75suDaYVI3jXgDbhA+w1fkNNVUt7GY8YVFPlUGj+nMBQN/yV7zFLDFrzWOdWNDsYaVykJrkZjG4V9KazK00tAiSB/2o11CnucWT6HCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HCRiY88g=="
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
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
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
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
    "data": {
      "state": "tx_+QEOCwH4hLhAL8giBf1t65iF4pgjihWpnpAFvbOx+M1Uo2s1ujecJUFe/JJ8Dfgl51REWbwoTE7/1Cpginn75suDaYVI3jXgDbhA+w1fkNNVUt7GY8YVFPlUGj+nMBQN/yV7zFLDFrzWOdWNDsYaVykJrkZjG4V9KazK00tAiSB/2o11CnucWT6HCLiE+IIyAaEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aGP6olImAAoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IYkYTnKgAACCgCGEAsh7xAAwKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC4HCRiY88g=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
    "data": {
      "signed_tx": "tx_+QGpCwHAuQGj+QGgNgGhBt3OcF3PwTh7H8/7gCS8JaLJDPcBtHPYcaLXHOxgjXPxoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oC5AUz5AUk8AfkBP/kBPKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPkBGPhPoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIn7aAxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf//hPoMSumE/bdTp41hfJ/nw86jdV6brGAmEh8g7FN4y08GrY7aAwh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IvKCgEAhiRhOcqAAfh0oOw+YOD4D/J/e4yoY7zKUFQueatYZaPAWaF1NmKiTj1Y+FGAgICAgKDErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2ICAgICAoF5MpvOld7QCDSiNm1OJJjrVt1RMsLFzE1YAqxpi4LIngICAgIDAwMDAwACGFUOUmEgAgcMJ8xQ3",
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
  "method": "channels.close_solo_sign",
  "params": {
    "signed_tx": "tx_+QHsCwH4QrhAt3W9XsWopGuQ4ZKuf8GzylCE4juXpQR17JHNtHIdF/V0PzKRvnms+f7yUCf0SVk7trNbM8krfdD1N5gZZphCBrkBo/kBoDYBoQbdznBdz8E4ex/P+4AkvCWiyQz3AbRz2HGi1xzsYI1z8aEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhVDlJhIAIHD17YUKg=="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHsCwH4QrhAt3W9XsWopGuQ4ZKuf8GzylCE4juXpQR17JHNtHIdF/V0PzKRvnms+f7yUCf0SVk7trNbM8krfdD1N5gZZphCBrkBo/kBoDYBoQbdznBdz8E4ex/P+4AkvCWiyQz3AbRz2HGi1xzsYI1z8aEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhVDlJhIAIHD17YUKg==",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
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
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHsCwH4QrhAt3W9XsWopGuQ4ZKuf8GzylCE4juXpQR17JHNtHIdF/V0PzKRvnms+f7yUCf0SVk7trNbM8krfdD1N5gZZphCBrkBo/kBoDYBoQbdznBdz8E4ex/P+4AkvCWiyQz3AbRz2HGi1xzsYI1z8aEBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aAuQFM+QFJPAH5AT/5ATyg7D5g4PgP8n97jKhjvMpQVC55q1hlo8BZoXU2YqJOPVj5ARj4T6BeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ+2gMcrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9aLygoBAIY/qiUiX//4T6DErphP23U6eNYXyf58POo3Vem6xgJhIfIOxTeMtPBq2O2gMIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAH4dKDsPmDg+A/yf3uMqGO8ylBULnmrWGWjwFmhdTZiok49WPhRgICAgICgxK6YT9t1OnjWF8n+fDzqN1XpusYCYSHyDsU3jLTwatiAgICAgKBeTKbzpXe0Ag0ojZtTiSY61bdUTLCxcxNWAKsaYuCyJ4CAgICAwMDAwMAAhhVDlJhIAIHD17YUKg==",
      "type": "channel_close_solo_tx"
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
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
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
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
    "data": {
      "signed_tx": "tx_+GULAcC4YPheOAGhBt3OcF3PwTh7H8/7gCS8JaLJDPcBtHPYcaLXHOxgjXPxoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1oY/qiUiX/+GJGE5yoABAIYPY36W8ACBxNx9yJw=",
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
  "method": "channels.settle_sign",
  "params": {
    "error": 42
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
    "data": {
      "event": "aborted_update"
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
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBt3OcF3PwTh7H8/7gCS8JaLJDPcBtHPYcaLXHOxgjXPxoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8IY/qiUiX/+GJGE5yoABAIYPXtZ/KABDe16aQQ==",
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
    "error": 42
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
    "data": {
      "event": "aborted_update"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421973,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
  "id": -576460752303421973,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421972,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
  "id": -576460752303421972,
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
    "channel_id": "ch_2ggkKPVTacmQQVdq8rjKQXuR4J7c9M5teUk3V74szzGvnVikEc",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection
