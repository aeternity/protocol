
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_sjuXT1xcbLNFvbMcYBerZuRF8QckyiHY7nBVjVTC1ZXauwGYY&lock_period=10&port=14035&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26zhrAPuCdcFD5f68BgRrHza8LS1wUrKKLHco21mjcBqcfwdU&role=initiator
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_sjuXT1xcbLNFvbMcYBerZuRF8QckyiHY7nBVjVTC1ZXauwGYY&lock_period=10&port=14035&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26zhrAPuCdcFD5f68BgRrHza8LS1wUrKKLHco21mjcBqcfwdU&role=responder
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAXM19+CQUeyWmvaE0nSNI3jz1pVLk8exNDjvw99hWk9ghj+qJSJgAKEBAoFcTad24H2gEDggwV7ZTNSaQUySSuDIGjfmxT7xPVaGJGE5yoAAAgoAhhAGeddIAMCgex59qbABDWUXFJtJJd3DKuyemGgUoqDzU7MRcNx/GhQDQJI9Ow==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423483,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECS8JXx8Te1FP7kUAkukX6ifsMkUkcihqmR2EVXy1w7aLQenyqtNQ+dZ1clvTlNurI3S61tSVjArx+96GMyl54EuIP4gTIBoQFzNffgkFHslpr2hNJ0jSN489aVS5PHsTQ478PfYVpPYIY/qiUiYAChAQKBXE2nduB9oBA4IMFe2UzUmkFMkkrgyBo35sU+8T1WhiRhOcqAAAIKAIYQBnnXSADAoHsefamwAQ1lFxSbSSXdwyrsnphoFKKg81OzEXDcfxoUA6JRL2U="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423483,
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
      "signed_tx": "tx_+MsLAfhCuECS8JXx8Te1FP7kUAkukX6ifsMkUkcihqmR2EVXy1w7aLQenyqtNQ+dZ1clvTlNurI3S61tSVjArx+96GMyl54EuIP4gTIBoQFzNffgkFHslpr2hNJ0jSN489aVS5PHsTQ478PfYVpPYIY/qiUiYAChAQKBXE2nduB9oBA4IMFe2UzUmkFMkkrgyBo35sU+8T1WhiRhOcqAAAIKAIYQBnnXSADAoHsefamwAQ1lFxSbSSXdwyrsnphoFKKg81OzEXDcfxoUA6JRL2U=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423482,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAM1iJF40I6ND8+Gzhn6pEEz2dNeNlkaPj5H/rspiNR8sZiuPjneK1/srnwImanUsxJLk4VHI6y91cLee4g/QPBLhAkvCV8fE3tRT+5FAJLpF+on7DJFJHIoapkdhFV8tcO2i0Hp8qrTUPnWdXJb05TbqyN0utbUlYwK8fvehjMpeeBLiD+IEyAaEBczX34JBR7Jaa9oTSdI0jePPWlUuTx7E0OO/D32FaT2CGP6olImAAoQECgVxNp3bgfaAQOCDBXtlM1JpBTJJK4MgaN+bFPvE9VoYkYTnKgAACCgCGEAZ510gAwKB7Hn2psAENZRcUm0kl3cMq7J6YaBSioPNTsxFw3H8aFAMi6L7F"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423482,
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
      "tx": "tx_+QENCwH4hLhAM1iJF40I6ND8+Gzhn6pEEz2dNeNlkaPj5H/rspiNR8sZiuPjneK1/srnwImanUsxJLk4VHI6y91cLee4g/QPBLhAkvCV8fE3tRT+5FAJLpF+on7DJFJHIoapkdhFV8tcO2i0Hp8qrTUPnWdXJb05TbqyN0utbUlYwK8fvehjMpeeBLiD+IEyAaEBczX34JBR7Jaa9oTSdI0jePPWlUuTx7E0OO/D32FaT2CGP6olImAAoQECgVxNp3bgfaAQOCDBXtlM1JpBTJJK4MgaN+bFPvE9VoYkYTnKgAACCgCGEAZ510gAwKB7Hn2psAENZRcUm0kl3cMq7J6YaBSioPNTsxFw3H8aFAMi6L7F",
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
      "tx": "tx_+QENCwH4hLhAM1iJF40I6ND8+Gzhn6pEEz2dNeNlkaPj5H/rspiNR8sZiuPjneK1/srnwImanUsxJLk4VHI6y91cLee4g/QPBLhAkvCV8fE3tRT+5FAJLpF+on7DJFJHIoapkdhFV8tcO2i0Hp8qrTUPnWdXJb05TbqyN0utbUlYwK8fvehjMpeeBLiD+IEyAaEBczX34JBR7Jaa9oTSdI0jePPWlUuTx7E0OO/D32FaT2CGP6olImAAoQECgVxNp3bgfaAQOCDBXtlM1JpBTJJK4MgaN+bFPvE9VoYkYTnKgAACCgCGEAZ510gAwKB7Hn2psAENZRcUm0kl3cMq7J6YaBSioPNTsxFw3H8aFAMi6L7F",
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
      "tx": "tx_+QENCwH4hLhAM1iJF40I6ND8+Gzhn6pEEz2dNeNlkaPj5H/rspiNR8sZiuPjneK1/srnwImanUsxJLk4VHI6y91cLee4g/QPBLhAkvCV8fE3tRT+5FAJLpF+on7DJFJHIoapkdhFV8tcO2i0Hp8qrTUPnWdXJb05TbqyN0utbUlYwK8fvehjMpeeBLiD+IEyAaEBczX34JBR7Jaa9oTSdI0jePPWlUuTx7E0OO/D32FaT2CGP6olImAAoQECgVxNp3bgfaAQOCDBXtlM1JpBTJJK4MgaN+bFPvE9VoYkYTnKgAACCgCGEAZ510gAwKB7Hn2psAENZRcUm0kl3cMq7J6YaBSioPNTsxFw3H8aFAMi6L7F",
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
      "tx": "tx_+QENCwH4hLhAM1iJF40I6ND8+Gzhn6pEEz2dNeNlkaPj5H/rspiNR8sZiuPjneK1/srnwImanUsxJLk4VHI6y91cLee4g/QPBLhAkvCV8fE3tRT+5FAJLpF+on7DJFJHIoapkdhFV8tcO2i0Hp8qrTUPnWdXJb05TbqyN0utbUlYwK8fvehjMpeeBLiD+IEyAaEBczX34JBR7Jaa9oTSdI0jePPWlUuTx7E0OO/D32FaT2CGP6olImAAoQECgVxNp3bgfaAQOCDBXtlM1JpBTJJK4MgaN+bFPvE9VoYkYTnKgAACCgCGEAZ510gAwKB7Hn2psAENZRcUm0kl3cMq7J6YaBSioPNTsxFw3H8aFAMi6L7F",
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
    "to": "ak_26zhrAPuCdcFD5f68BgRrHza8LS1wUrKKLHco21mjcBqcfwdU"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
    "data": {
      "message": {
        "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
        "from": "ak_sjuXT1xcbLNFvbMcYBerZuRF8QckyiHY7nBVjVTC1ZXauwGYY",
        "info": "Hello",
        "to": "ak_26zhrAPuCdcFD5f68BgRrHza8LS1wUrKKLHco21mjcBqcfwdU"
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
    "to": "ak_sjuXT1xcbLNFvbMcYBerZuRF8QckyiHY7nBVjVTC1ZXauwGYY"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
    "data": {
      "message": {
        "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
        "from": "ak_26zhrAPuCdcFD5f68BgRrHza8LS1wUrKKLHco21mjcBqcfwdU",
        "info": "Hello back",
        "to": "ak_sjuXT1xcbLNFvbMcYBerZuRF8QckyiHY7nBVjVTC1ZXauwGYY"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423481,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_sjuXT1xcbLNFvbMcYBerZuRF8QckyiHY7nBVjVTC1ZXauwGYY",
      "ak_26zhrAPuCdcFD5f68BgRrHza8LS1wUrKKLHco21mjcBqcfwdU"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
  "id": -576460752303423481,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_sjuXT1xcbLNFvbMcYBerZuRF8QckyiHY7nBVjVTC1ZXauwGYY",
      "balance": 69999999999999
    },
    {
      "account": "ak_26zhrAPuCdcFD5f68BgRrHza8LS1wUrKKLHco21mjcBqcfwdU",
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
    "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
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
    "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
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
    "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
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
    "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
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
    "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
    "data": {
      "state": "tx_+QENCwH4hLhAM1iJF40I6ND8+Gzhn6pEEz2dNeNlkaPj5H/rspiNR8sZiuPjneK1/srnwImanUsxJLk4VHI6y91cLee4g/QPBLhAkvCV8fE3tRT+5FAJLpF+on7DJFJHIoapkdhFV8tcO2i0Hp8qrTUPnWdXJb05TbqyN0utbUlYwK8fvehjMpeeBLiD+IEyAaEBczX34JBR7Jaa9oTSdI0jePPWlUuTx7E0OO/D32FaT2CGP6olImAAoQECgVxNp3bgfaAQOCDBXtlM1JpBTJJK4MgaN+bFPvE9VoYkYTnKgAACCgCGEAZ510gAwKB7Hn2psAENZRcUm0kl3cMq7J6YaBSioPNTsxFw3H8aFAMi6L7F"
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
    "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
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
    "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
    "data": {
      "state": "tx_+QENCwH4hLhAM1iJF40I6ND8+Gzhn6pEEz2dNeNlkaPj5H/rspiNR8sZiuPjneK1/srnwImanUsxJLk4VHI6y91cLee4g/QPBLhAkvCV8fE3tRT+5FAJLpF+on7DJFJHIoapkdhFV8tcO2i0Hp8qrTUPnWdXJb05TbqyN0utbUlYwK8fvehjMpeeBLiD+IEyAaEBczX34JBR7Jaa9oTSdI0jePPWlUuTx7E0OO/D32FaT2CGP6olImAAoQECgVxNp3bgfaAQOCDBXtlM1JpBTJJK4MgaN+bFPvE9VoYkYTnKgAACCgCGEAZ510gAwKB7Hn2psAENZRcUm0kl3cMq7J6YaBSioPNTsxFw3H8aFAMi6L7F"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection
```

```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_sjuXT1xcbLNFvbMcYBerZuRF8QckyiHY7nBVjVTC1ZXauwGYY",
    "to": "ak_26zhrAPuCdcFD5f68BgRrHza8LS1wUrKKLHco21mjcBqcfwdU"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvcBETvnI6KGYI/QwYTwnW13LGBWOv+oMIhVSfLS7s66AqB9s4/Obkc1m2MwoetvsLCxUAGjnP+DhG9my+JCHYnle4oU4BM=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_sjuXT1xcbLNFvbMcYBerZuRF8QckyiHY7nBVjVTC1ZXauwGYY",
          "op": "OffChainTransfer",
          "to": "ak_26zhrAPuCdcFD5f68BgRrHza8LS1wUrKKLHco21mjcBqcfwdU"
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
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEABWcROtmqnt7hdu1grIppAbGNIQ3096gqKfB/ryXVCGehBdq2ET0EUBRz+pB71o1kAV90Zi884OGNsAj98nz0LuEj4RjkCoQb3ARE75yOihmCP0MGE8J1tdyxgVjr/qDCIVUny0u7OugKgfbOPzm5HNZtjMKHrb7CwsVABo5z/g4RvZsviQh2J5XtyM3B0"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
    "data": {
      "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
      "round": 1
    }
  },
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
    "from": "ak_sjuXT1xcbLNFvbMcYBerZuRF8QckyiHY7nBVjVTC1ZXauwGYY",
    "to": "ak_26zhrAPuCdcFD5f68BgRrHza8LS1wUrKKLHco21mjcBqcfwdU"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvcBETvnI6KGYI/QwYTwnW13LGBWOv+oMIhVSfLS7s66AqB9s4/Obkc1m2MwoetvsLCxUAGjnP+DhG9my+JCHYnle4oU4BM=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_sjuXT1xcbLNFvbMcYBerZuRF8QckyiHY7nBVjVTC1ZXauwGYY",
          "op": "OffChainTransfer",
          "to": "ak_26zhrAPuCdcFD5f68BgRrHza8LS1wUrKKLHco21mjcBqcfwdU"
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
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+NILAfiEuEABWcROtmqnt7hdu1grIppAbGNIQ3096gqKfB/ryXVCGehBdq2ET0EUBRz+pB71o1kAV90Zi884OGNsAj98nz0LuEA+VobKyz4IYh2+tQDXgQTL9jmWo9n/gxrbvhS4Xv1uXDxmi2BXCJ+7dh+A5NWpQMgPkwV+DzaNuZcCWYubnJ0FuEj4RjkCoQb3ARE75yOihmCP0MGE8J1tdyxgVjr/qDCIVUny0u7OugKgfbOPzm5HNZtjMKHrb7CwsVABo5z/g4RvZsviQh2J5XtDyF1V"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
    "data": {
      "state": "tx_+NILAfiEuEABWcROtmqnt7hdu1grIppAbGNIQ3096gqKfB/ryXVCGehBdq2ET0EUBRz+pB71o1kAV90Zi884OGNsAj98nz0LuEA+VobKyz4IYh2+tQDXgQTL9jmWo9n/gxrbvhS4Xv1uXDxmi2BXCJ+7dh+A5NWpQMgPkwV+DzaNuZcCWYubnJ0FuEj4RjkCoQb3ARE75yOihmCP0MGE8J1tdyxgVjr/qDCIVUny0u7OugKgfbOPzm5HNZtjMKHrb7CwsVABo5z/g4RvZsviQh2J5XtDyF1V"
    }
  },
  "version": 1
}
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?port=14035&protocol=json-rpc&reconnect_tx=tx_%2BJ0LAfhCuEBsRxyC73lu%2Bk5uebWiaJWdQ0kyG20jBuWj1pNppFYEWTNCS03SHGY6somzxvgnhkAjfK4aPv%2B8MWYXcr%2Fb2qEPuFX4U4ICPwGhBvcBETvnI6KGYI%2FQwYTwnW13LGBWOv%2BoMIhVSfLS7s66AYlyZXNwb25kZXKhAQKBXE2nduB9oBA4IMFe2UzUmkFMkkrgyBo35sU%2B8T1WipsglQ%3D%3D&role=responder
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBvcBETvnI6KGYI/QwYTwnW13LGBWOv+oMIhVSfLS7s66oQECgVxNp3bgfaAQOCDBXtlM1JpBTJJK4MgaN+bFPvE9VoY2kdavv/6GG0jrV+ACAIYSMJzlQAAB9g64qQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423480,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEAF0isOm6FYEfsfywEumJqCXECTDjv74ye2teyaGOewilz/5zAy2eC/8ivBkRoqeDE1tv9atU9dX6DIWiw26d8BuF/4XTUBoQb3ARE75yOihmCP0MGE8J1tdyxgVjr/qDCIVUny0u7OuqEBAoFcTad24H2gEDggwV7ZTNSaQUySSuDIGjfmxT7xPVaGNpHWr7/+hhtI61fgAgCGEjCc5UAAASPTjLQ="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
  "id": -576460752303423480,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEAF0isOm6FYEfsfywEumJqCXECTDjv74ye2teyaGOewilz/5zAy2eC/8ivBkRoqeDE1tv9atU9dX6DIWiw26d8BuF/4XTUBoQb3ARE75yOihmCP0MGE8J1tdyxgVjr/qDCIVUny0u7OuqEBAoFcTad24H2gEDggwV7ZTNSaQUySSuDIGjfmxT7xPVaGNpHWr7/+hhtI61fgAgCGEjCc5UAAASPTjLQ=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423479,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEAF0isOm6FYEfsfywEumJqCXECTDjv74ye2teyaGOewilz/5zAy2eC/8ivBkRoqeDE1tv9atU9dX6DIWiw26d8BuEB1j32/Dh3bt7wlkQCqC+3QT09WtzOI0F3ibLYxqccwuAZ71RmR11dn4NAxluKjWmWIzD0ywk7laIkt8cxUyWkLuF/4XTUBoQb3ARE75yOihmCP0MGE8J1tdyxgVjr/qDCIVUny0u7OuqEBAoFcTad24H2gEDggwV7ZTNSaQUySSuDIGjfmxT7xPVaGNpHWr7/+hhtI61fgAgCGEjCc5UAAAWvn5nI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
  "id": -576460752303423479,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAF0isOm6FYEfsfywEumJqCXECTDjv74ye2teyaGOewilz/5zAy2eC/8ivBkRoqeDE1tv9atU9dX6DIWiw26d8BuEB1j32/Dh3bt7wlkQCqC+3QT09WtzOI0F3ibLYxqccwuAZ71RmR11dn4NAxluKjWmWIzD0ywk7laIkt8cxUyWkLuF/4XTUBoQb3ARE75yOihmCP0MGE8J1tdyxgVjr/qDCIVUny0u7OuqEBAoFcTad24H2gEDggwV7ZTNSaQUySSuDIGjfmxT7xPVaGNpHWr7/+hhtI61fgAgCGEjCc5UAAAWvn5nI=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
    "data": {
      "event": "close_mutual"
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
    "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAF0isOm6FYEfsfywEumJqCXECTDjv74ye2teyaGOewilz/5zAy2eC/8ivBkRoqeDE1tv9atU9dX6DIWiw26d8BuEB1j32/Dh3bt7wlkQCqC+3QT09WtzOI0F3ibLYxqccwuAZ71RmR11dn4NAxluKjWmWIzD0ywk7laIkt8cxUyWkLuF/4XTUBoQb3ARE75yOihmCP0MGE8J1tdyxgVjr/qDCIVUny0u7OuqEBAoFcTad24H2gEDggwV7ZTNSaQUySSuDIGjfmxT7xPVaGNpHWr7/+hhtI61fgAgCGEjCc5UAAAWvn5nI=",
      "type": "channel_close_mutual_tx"
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
    "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
    "data": {
      "event": "close_mutual"
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
    "channel_id": "ch_2snPcvMNtgofFEmQtywc5BdAggTmZXuT6jDdzMHJZ7HUPHRHkx",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection
```

```
