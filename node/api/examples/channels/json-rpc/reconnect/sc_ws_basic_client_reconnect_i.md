
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_sjuXT1xcbLNFvbMcYBerZuRF8QckyiHY7nBVjVTC1ZXauwGYY&lock_period=10&port=14035&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26zhrAPuCdcFD5f68BgRrHza8LS1wUrKKLHco21mjcBqcfwdU&role=initiator
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_sjuXT1xcbLNFvbMcYBerZuRF8QckyiHY7nBVjVTC1ZXauwGYY&lock_period=10&port=14035&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_26zhrAPuCdcFD5f68BgRrHza8LS1wUrKKLHco21mjcBqcfwdU&role=responder
```

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

#### initiator info
> Received an WebSocket connection accepted

#### responder info
> Received an WebSocket opening request

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAXM19+CQUeyWmvaE0nSNI3jz1pVLk8exNDjvw99hWk9ghj+qJSJgAKEBAoFcTad24H2gEDggwV7ZTNSaQUySSuDIGjfmxT7xPVaGJGE5yoAAAgoAhhAGeddIAMCgex59qbABDWUXFJtJJd3DKuyemGgUoqDzU7MRcNx/GhQB2jR82g==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423488,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEColp24WtMKprGoX24QM9Vt3qeSX9wvO42pCjiftSdz1Jkry5ZXJFO9s8vwA/hmj9z2CLPmKn0C7urIaag1FGEPuIP4gTIBoQFzNffgkFHslpr2hNJ0jSN489aVS5PHsTQ478PfYVpPYIY/qiUiYAChAQKBXE2nduB9oBA4IMFe2UzUmkFMkkrgyBo35sU+8T1WhiRhOcqAAAIKAIYQBnnXSADAoHsefamwAQ1lFxSbSSXdwyrsnphoFKKg81OzEXDcfxoUASf7n/A="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423488,
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
      "signed_tx": "tx_+MsLAfhCuEColp24WtMKprGoX24QM9Vt3qeSX9wvO42pCjiftSdz1Jkry5ZXJFO9s8vwA/hmj9z2CLPmKn0C7urIaag1FGEPuIP4gTIBoQFzNffgkFHslpr2hNJ0jSN489aVS5PHsTQ478PfYVpPYIY/qiUiYAChAQKBXE2nduB9oBA4IMFe2UzUmkFMkkrgyBo35sU+8T1WhiRhOcqAAAIKAIYQBnnXSADAoHsefamwAQ1lFxSbSSXdwyrsnphoFKKg81OzEXDcfxoUASf7n/A=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423487,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAqJaduFrTCqaxqF9uEDPVbd6nkl/cLzuNqQo4n7Unc9SZK8uWVyRTvbPL8AP4Zo/c9giz5ip9Au7qyGmoNRRhD7hAuur2dr0f4rmoiYQaJn51XGm26ksdM6UdCTGJcJSoPXNT9qaWKdiT/1uDXhUuv6L92JlkWPoqNdxAgoZgGozdDriD+IEyAaEBczX34JBR7Jaa9oTSdI0jePPWlUuTx7E0OO/D32FaT2CGP6olImAAoQECgVxNp3bgfaAQOCDBXtlM1JpBTJJK4MgaN+bFPvE9VoYkYTnKgAACCgCGEAZ510gAwKB7Hn2psAENZRcUm0kl3cMq7J6YaBSioPNTsxFw3H8aFAHEJFnz"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423487,
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
      "tx": "tx_+QENCwH4hLhAqJaduFrTCqaxqF9uEDPVbd6nkl/cLzuNqQo4n7Unc9SZK8uWVyRTvbPL8AP4Zo/c9giz5ip9Au7qyGmoNRRhD7hAuur2dr0f4rmoiYQaJn51XGm26ksdM6UdCTGJcJSoPXNT9qaWKdiT/1uDXhUuv6L92JlkWPoqNdxAgoZgGozdDriD+IEyAaEBczX34JBR7Jaa9oTSdI0jePPWlUuTx7E0OO/D32FaT2CGP6olImAAoQECgVxNp3bgfaAQOCDBXtlM1JpBTJJK4MgaN+bFPvE9VoYkYTnKgAACCgCGEAZ510gAwKB7Hn2psAENZRcUm0kl3cMq7J6YaBSioPNTsxFw3H8aFAHEJFnz",
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
      "tx": "tx_+QENCwH4hLhAqJaduFrTCqaxqF9uEDPVbd6nkl/cLzuNqQo4n7Unc9SZK8uWVyRTvbPL8AP4Zo/c9giz5ip9Au7qyGmoNRRhD7hAuur2dr0f4rmoiYQaJn51XGm26ksdM6UdCTGJcJSoPXNT9qaWKdiT/1uDXhUuv6L92JlkWPoqNdxAgoZgGozdDriD+IEyAaEBczX34JBR7Jaa9oTSdI0jePPWlUuTx7E0OO/D32FaT2CGP6olImAAoQECgVxNp3bgfaAQOCDBXtlM1JpBTJJK4MgaN+bFPvE9VoYkYTnKgAACCgCGEAZ510gAwKB7Hn2psAENZRcUm0kl3cMq7J6YaBSioPNTsxFw3H8aFAHEJFnz",
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
      "tx": "tx_+QENCwH4hLhAqJaduFrTCqaxqF9uEDPVbd6nkl/cLzuNqQo4n7Unc9SZK8uWVyRTvbPL8AP4Zo/c9giz5ip9Au7qyGmoNRRhD7hAuur2dr0f4rmoiYQaJn51XGm26ksdM6UdCTGJcJSoPXNT9qaWKdiT/1uDXhUuv6L92JlkWPoqNdxAgoZgGozdDriD+IEyAaEBczX34JBR7Jaa9oTSdI0jePPWlUuTx7E0OO/D32FaT2CGP6olImAAoQECgVxNp3bgfaAQOCDBXtlM1JpBTJJK4MgaN+bFPvE9VoYkYTnKgAACCgCGEAZ510gAwKB7Hn2psAENZRcUm0kl3cMq7J6YaBSioPNTsxFw3H8aFAHEJFnz",
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
      "tx": "tx_+QENCwH4hLhAqJaduFrTCqaxqF9uEDPVbd6nkl/cLzuNqQo4n7Unc9SZK8uWVyRTvbPL8AP4Zo/c9giz5ip9Au7qyGmoNRRhD7hAuur2dr0f4rmoiYQaJn51XGm26ksdM6UdCTGJcJSoPXNT9qaWKdiT/1uDXhUuv6L92JlkWPoqNdxAgoZgGozdDriD+IEyAaEBczX34JBR7Jaa9oTSdI0jePPWlUuTx7E0OO/D32FaT2CGP6olImAAoQECgVxNp3bgfaAQOCDBXtlM1JpBTJJK4MgaN+bFPvE9VoYkYTnKgAACCgCGEAZ510gAwKB7Hn2psAENZRcUm0kl3cMq7J6YaBSioPNTsxFw3H8aFAHEJFnz",
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
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
    "data": {
      "message": {
        "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
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
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
    "data": {
      "message": {
        "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
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
  "id": -576460752303423486,
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
  "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
  "id": -576460752303423486,
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
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
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
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
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
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
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
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
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
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
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
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
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
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
    "data": {
      "state": "tx_+QENCwH4hLhAqJaduFrTCqaxqF9uEDPVbd6nkl/cLzuNqQo4n7Unc9SZK8uWVyRTvbPL8AP4Zo/c9giz5ip9Au7qyGmoNRRhD7hAuur2dr0f4rmoiYQaJn51XGm26ksdM6UdCTGJcJSoPXNT9qaWKdiT/1uDXhUuv6L92JlkWPoqNdxAgoZgGozdDriD+IEyAaEBczX34JBR7Jaa9oTSdI0jePPWlUuTx7E0OO/D32FaT2CGP6olImAAoQECgVxNp3bgfaAQOCDBXtlM1JpBTJJK4MgaN+bFPvE9VoYkYTnKgAACCgCGEAZ510gAwKB7Hn2psAENZRcUm0kl3cMq7J6YaBSioPNTsxFw3H8aFAHEJFnz"
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
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
    "data": {
      "state": "tx_+QENCwH4hLhAqJaduFrTCqaxqF9uEDPVbd6nkl/cLzuNqQo4n7Unc9SZK8uWVyRTvbPL8AP4Zo/c9giz5ip9Au7qyGmoNRRhD7hAuur2dr0f4rmoiYQaJn51XGm26ksdM6UdCTGJcJSoPXNT9qaWKdiT/1uDXhUuv6L92JlkWPoqNdxAgoZgGozdDriD+IEyAaEBczX34JBR7Jaa9oTSdI0jePPWlUuTx7E0OO/D32FaT2CGP6olImAAoQECgVxNp3bgfaAQOCDBXtlM1JpBTJJK4MgaN+bFPvE9VoYkYTnKgAACCgCGEAZ510gAwKB7Hn2psAENZRcUm0kl3cMq7J6YaBSioPNTsxFw3H8aFAHEJFnz"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection
```

```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_26zhrAPuCdcFD5f68BgRrHza8LS1wUrKKLHco21mjcBqcfwdU",
    "to": "ak_sjuXT1xcbLNFvbMcYBerZuRF8QckyiHY7nBVjVTC1ZXauwGYY"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvFUHNvTaJmM0h7WZRyILi7R5xEube4cPidh39qA4rZ3AqA1OxWEaCmQrMsRAz/aOqULrCfnjvXy3CsSqurneRAweq1oQ2o=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26zhrAPuCdcFD5f68BgRrHza8LS1wUrKKLHco21mjcBqcfwdU",
          "op": "OffChainTransfer",
          "to": "ak_sjuXT1xcbLNFvbMcYBerZuRF8QckyiHY7nBVjVTC1ZXauwGYY"
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
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC9qolUALwHM2t73ZWgLujcu2EPv3IWOBll9bmMb0WIJcCqHnz/ZBf3VHxlPWb/VWCY9wp/Z4MOoqqtiLwpApEGuEj4RjkCoQbxVBzb02iZjNIe1mUciC4u0ecRLm3uHD4nYd/agOK2dwKgNTsVhGgpkKzLEQM/2jqlC6wn54718twrEqrq53kQMHpotH/U"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
    "data": {
      "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
      "round": 1
    }
  },
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
    "from": "ak_26zhrAPuCdcFD5f68BgRrHza8LS1wUrKKLHco21mjcBqcfwdU",
    "to": "ak_sjuXT1xcbLNFvbMcYBerZuRF8QckyiHY7nBVjVTC1ZXauwGYY"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBvFUHNvTaJmM0h7WZRyILi7R5xEube4cPidh39qA4rZ3AqA1OxWEaCmQrMsRAz/aOqULrCfnjvXy3CsSqurneRAweq1oQ2o=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_26zhrAPuCdcFD5f68BgRrHza8LS1wUrKKLHco21mjcBqcfwdU",
          "op": "OffChainTransfer",
          "to": "ak_sjuXT1xcbLNFvbMcYBerZuRF8QckyiHY7nBVjVTC1ZXauwGYY"
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
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+NILAfiEuEB2kYkTBh9xELqllJZzHMFcj9oysyo4t6sBbxWI1tm2LZmkh9liZbwHyzNADWjj9FywzWpVceUfiVWhXfwHXFIFuEC9qolUALwHM2t73ZWgLujcu2EPv3IWOBll9bmMb0WIJcCqHnz/ZBf3VHxlPWb/VWCY9wp/Z4MOoqqtiLwpApEGuEj4RjkCoQbxVBzb02iZjNIe1mUciC4u0ecRLm3uHD4nYd/agOK2dwKgNTsVhGgpkKzLEQM/2jqlC6wn54718twrEqrq53kQMHqW0FMw"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
    "data": {
      "state": "tx_+NILAfiEuEB2kYkTBh9xELqllJZzHMFcj9oysyo4t6sBbxWI1tm2LZmkh9liZbwHyzNADWjj9FywzWpVceUfiVWhXfwHXFIFuEC9qolUALwHM2t73ZWgLujcu2EPv3IWOBll9bmMb0WIJcCqHnz/ZBf3VHxlPWb/VWCY9wp/Z4MOoqqtiLwpApEGuEj4RjkCoQbxVBzb02iZjNIe1mUciC4u0ecRLm3uHD4nYd/agOK2dwKgNTsVhGgpkKzLEQM/2jqlC6wn54718twrEqrq53kQMHqW0FMw"
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?port=14035&protocol=json-rpc&reconnect_tx=tx_%2BJ0LAfhCuEAqxhxMDYpXQXvRe9ogDQxz6LaxfJrEGY45mJcWD5snh%2BNFxt2GgNV%2FU1xToVqozdsYVcZyfRa3EkcZ2jAk8CgOuFX4U4ICPwGhBvFUHNvTaJmM0h7WZRyILi7R5xEube4cPidh39qA4rZ3AYlpbml0aWF0b3KhAXM19%2BCQUeyWmvaE0nSNI3jz1pVLk8exNDjvw99hWk9gS2AC9A%3D%3D&role=initiator
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBvFUHNvTaJmM0h7WZRyILi7R5xEube4cPidh39qA4rZ3oQFzNffgkFHslpr2hNJ0jSN489aVS5PHsTQ478PfYVpPYIY2kdavwACGG0jrV+AAAIYSMJzlQAACaWfGyw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423485,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEAjiW+N4T0XSzKS5KGSsknfgDPolcEIiKdMG4bIsQwQF64VO15X2Amnvdim1ErhgS7WFH+HX7BnCQFMYcU3uuQAuF/4XTUBoQbxVBzb02iZjNIe1mUciC4u0ecRLm3uHD4nYd/agOK2d6EBczX34JBR7Jaa9oTSdI0jePPWlUuTx7E0OO/D32FaT2CGNpHWr8AAhhtI61fgAACGEjCc5UAAAp5Zmow="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
  "id": -576460752303423485,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEAjiW+N4T0XSzKS5KGSsknfgDPolcEIiKdMG4bIsQwQF64VO15X2Amnvdim1ErhgS7WFH+HX7BnCQFMYcU3uuQAuF/4XTUBoQbxVBzb02iZjNIe1mUciC4u0ecRLm3uHD4nYd/agOK2d6EBczX34JBR7Jaa9oTSdI0jePPWlUuTx7E0OO/D32FaT2CGNpHWr8AAhhtI61fgAACGEjCc5UAAAp5Zmow=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423484,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEAjiW+N4T0XSzKS5KGSsknfgDPolcEIiKdMG4bIsQwQF64VO15X2Amnvdim1ErhgS7WFH+HX7BnCQFMYcU3uuQAuEBVakfMSbquJaRXdISFooXUDdW5eCVURga229Spl0Zqegw/5UUUriuZ7yzrtfyEcqDg2D5OmFZ4Diccz0ufBwsGuF/4XTUBoQbxVBzb02iZjNIe1mUciC4u0ecRLm3uHD4nYd/agOK2d6EBczX34JBR7Jaa9oTSdI0jePPWlUuTx7E0OO/D32FaT2CGNpHWr8AAhhtI61fgAACGEjCc5UAAAgssSIU="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
  "id": -576460752303423484,
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
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAjiW+N4T0XSzKS5KGSsknfgDPolcEIiKdMG4bIsQwQF64VO15X2Amnvdim1ErhgS7WFH+HX7BnCQFMYcU3uuQAuEBVakfMSbquJaRXdISFooXUDdW5eCVURga229Spl0Zqegw/5UUUriuZ7yzrtfyEcqDg2D5OmFZ4Diccz0ufBwsGuF/4XTUBoQbxVBzb02iZjNIe1mUciC4u0ecRLm3uHD4nYd/agOK2d6EBczX34JBR7Jaa9oTSdI0jePPWlUuTx7E0OO/D32FaT2CGNpHWr8AAhhtI61fgAACGEjCc5UAAAgssSIU=",
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
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
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
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
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

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAjiW+N4T0XSzKS5KGSsknfgDPolcEIiKdMG4bIsQwQF64VO15X2Amnvdim1ErhgS7WFH+HX7BnCQFMYcU3uuQAuEBVakfMSbquJaRXdISFooXUDdW5eCVURga229Spl0Zqegw/5UUUriuZ7yzrtfyEcqDg2D5OmFZ4Diccz0ufBwsGuF/4XTUBoQbxVBzb02iZjNIe1mUciC4u0ecRLm3uHD4nYd/agOK2d6EBczX34JBR7Jaa9oTSdI0jePPWlUuTx7E0OO/D32FaT2CGNpHWr8AAhhtI61fgAACGEjCc5UAAAgssSIU=",
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
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
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
    "channel_id": "ch_2qHR2iopmhCpRq1NYKcqXkAM4ydhKrqCiwyNushZrH94L6TQ4r",
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
