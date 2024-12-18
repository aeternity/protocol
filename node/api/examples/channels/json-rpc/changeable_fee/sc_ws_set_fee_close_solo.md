
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=initiator
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
      "fsm_id": "ba_ru+vYN9rMTFKzep2htAfKfNbRt0VvDo4Goad/T5u/LwmDa/s"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=responder
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
      "fsm_id": "ba_Vu1r7qFIT7ohpQwWaVvxIkmUVpeVvwOqO3w4pu8pRx8jcD8x"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4sCDS4UQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422925,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAUJZY+wLN5ujEbv8vA/wqhRUAgn4Zf/hHLg/bKF0MnGsGmdSoN8Onmj2AtTVGsPYq8jUAcRM6ICTOLuNTWW4YBuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uLF8ML3Q="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422925,
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
      "signed_tx": "tx_+MsLAfhCuEAUJZY+wLN5ujEbv8vA/wqhRUAgn4Zf/hHLg/bKF0MnGsGmdSoN8Onmj2AtTVGsPYq8jUAcRM6ICTOLuNTWW4YBuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uLF8ML3Q=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422924,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAFCWWPsCzeboxG7/LwP8KoUVAIJ+GX/4Ry4P2yhdDJxrBpnUqDfDp5o9gLU1RrD2KvI1AHETOiAkzi7jU1luGAbhAaiUjo0Rrdyo5Qnji9BtaXHRaohUbwLne+A+bte/LvPmP89xZcXdNvW1Qm2B086yFIIUCYtH+IjvTGB5IPAl+AriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7iwO6Mvg"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422924,
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
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAFCWWPsCzeboxG7/LwP8KoUVAIJ+GX/4Ry4P2yhdDJxrBpnUqDfDp5o9gLU1RrD2KvI1AHETOiAkzi7jU1luGAbhAaiUjo0Rrdyo5Qnji9BtaXHRaohUbwLne+A+bte/LvPmP89xZcXdNvW1Qm2B086yFIIUCYtH+IjvTGB5IPAl+AriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7iwO6Mvg",
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
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAFCWWPsCzeboxG7/LwP8KoUVAIJ+GX/4Ry4P2yhdDJxrBpnUqDfDp5o9gLU1RrD2KvI1AHETOiAkzi7jU1luGAbhAaiUjo0Rrdyo5Qnji9BtaXHRaohUbwLne+A+bte/LvPmP89xZcXdNvW1Qm2B086yFIIUCYtH+IjvTGB5IPAl+AriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7iwO6Mvg",
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
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAFCWWPsCzeboxG7/LwP8KoUVAIJ+GX/4Ry4P2yhdDJxrBpnUqDfDp5o9gLU1RrD2KvI1AHETOiAkzi7jU1luGAbhAaiUjo0Rrdyo5Qnji9BtaXHRaohUbwLne+A+bte/LvPmP89xZcXdNvW1Qm2B086yFIIUCYtH+IjvTGB5IPAl+AriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7iwO6Mvg",
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
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAFCWWPsCzeboxG7/LwP8KoUVAIJ+GX/4Ry4P2yhdDJxrBpnUqDfDp5o9gLU1RrD2KvI1AHETOiAkzi7jU1luGAbhAaiUjo0Rrdyo5Qnji9BtaXHRaohUbwLne+A+bte/LvPmP89xZcXdNvW1Qm2B086yFIIUCYtH+IjvTGB5IPAl+AriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7iwO6Mvg",
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
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
    "data": {
      "message": {
        "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "info": "Hello",
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
    "data": {
      "message": {
        "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "info": "Hello back",
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422923,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
  "id": -576460752303422923,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999999
    },
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
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
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
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
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
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
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
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
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
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
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
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
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
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
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
    "data": {
      "state": "tx_+QENCwH4hLhAFCWWPsCzeboxG7/LwP8KoUVAIJ+GX/4Ry4P2yhdDJxrBpnUqDfDp5o9gLU1RrD2KvI1AHETOiAkzi7jU1luGAbhAaiUjo0Rrdyo5Qnji9BtaXHRaohUbwLne+A+bte/LvPmP89xZcXdNvW1Qm2B086yFIIUCYtH+IjvTGB5IPAl+AriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7iwO6Mvg"
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
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
    "data": {
      "state": "tx_+QENCwH4hLhAFCWWPsCzeboxG7/LwP8KoUVAIJ+GX/4Ry4P2yhdDJxrBpnUqDfDp5o9gLU1RrD2KvI1AHETOiAkzi7jU1luGAbhAaiUjo0Rrdyo5Qnji9BtaXHRaohUbwLne+A+bte/LvPmP89xZcXdNvW1Qm2B086yFIIUCYtH+IjvTGB5IPAl+AriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7iwO6Mvg"
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
  "params": {
    "fee": 123456789876543
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBpO1SlTBGJYcpTFymX4durfiW9oRUHQ6MI0xO5ogcu8voQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IC5AUz5AUk8AfkBP/kBPKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvkBGPh0oCbziXyYo8Ox+VZtROqlQQtKKd21jKCiqh29ftJZTs5e+FGAgICAgICAgICAgICg7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqug5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqeAgID4T6DlslFZIexXT120YXqqt3xFqwcxbt0Suq1WIBNf47yap+2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAH4T6Dt/5Hiy5W70qsqTzdexfFGw0mN5gAjP38MM0HGdpS2q+2gNbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX//AwMDAwACGcEiGGw8/LWwYcng=",
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
    "signed_tx": "tx_+QHrCwH4QrhAVU6eRxNxpnotrYHaUtSFgAQt2/rheSyod2OWRFJg2DjAfPK6V5VtkeLmoB/cr3TSpgjjAStASk/0+h+BtTSxCbkBovkBnzYBoQaTtUpUwRiWHKUxcpl+Hbq34lvaEVB0OjCNMTuaIHLvL6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SAuQFM+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMAAhnBIhhsPPy1du31q"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAVU6eRxNxpnotrYHaUtSFgAQt2/rheSyod2OWRFJg2DjAfPK6V5VtkeLmoB/cr3TSpgjjAStASk/0+h+BtTSxCbkBovkBnzYBoQaTtUpUwRiWHKUxcpl+Hbq34lvaEVB0OjCNMTuaIHLvL6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SAuQFM+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMAAhnBIhhsPPy1du31q",
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
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
    "data": {
      "event": "closing"
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
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAVU6eRxNxpnotrYHaUtSFgAQt2/rheSyod2OWRFJg2DjAfPK6V5VtkeLmoB/cr3TSpgjjAStASk/0+h+BtTSxCbkBovkBnzYBoQaTtUpUwRiWHKUxcpl+Hbq34lvaEVB0OjCNMTuaIHLvL6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SAuQFM+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMAAhnBIhhsPPy1du31q",
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
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
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
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBpO1SlTBGJYcpTFymX4durfiW9oRUHQ6MI0xO5ogcu8voQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIY/qiUiX/+GJGE5yoABAIYPXtZ/KAAQAUUEfg==",
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
    "signed_tx": "tx_+KcLAfhCuEC5i1Vzkz++zzee6QxLM0RIXDQaSi3wjk0AcBvdVyAK8g1rtT+5jlzNusxA2n99dvBlzgsDQI7r17Fpw/JT2WoIuF/4XTgBoQaTtUpUwRiWHKUxcpl+Hbq34lvaEVB0OjCNMTuaIHLvL6EB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl//hiRhOcqAAQCGD17WfygAEPyU7hs="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEC5i1Vzkz++zzee6QxLM0RIXDQaSi3wjk0AcBvdVyAK8g1rtT+5jlzNusxA2n99dvBlzgsDQI7r17Fpw/JT2WoIuF/4XTgBoQaTtUpUwRiWHKUxcpl+Hbq34lvaEVB0OjCNMTuaIHLvL6EB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl//hiRhOcqAAQCGD17WfygAEPyU7hs=",
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
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEC5i1Vzkz++zzee6QxLM0RIXDQaSi3wjk0AcBvdVyAK8g1rtT+5jlzNusxA2n99dvBlzgsDQI7r17Fpw/JT2WoIuF/4XTgBoQaTtUpUwRiWHKUxcpl+Hbq34lvaEVB0OjCNMTuaIHLvL6EB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl//hiRhOcqAAQCGD17WfygAEPyU7hs=",
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
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
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
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
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
    "channel_id": "ch_2841Q1nqr6CYjr73MoWU5VtGCvRmJqgFjGMXKackpUZxio284e",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=initiator
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
      "fsm_id": "ba_Vxxz9hU88oLgLj9EY1oHb8Njmo+JGjzxzGfFQPVUFijghgVH"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=responder
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
      "fsm_id": "ba_b/7nVp1U+0QPQItxYkC8B1c/gcrfJbmIzjlzahyuRKBDfOiD"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4uKCkl3w==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422922,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEC5RDSfJGgFHC4eerABXprVL1T+PPifVYB1/8C/zGrwToTaW9qILoU5r+KwIMJCbduO2fwRET7QGdJcYsLMJvYEuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uLhoSsUY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422922,
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
      "signed_tx": "tx_+MsLAfhCuEC5RDSfJGgFHC4eerABXprVL1T+PPifVYB1/8C/zGrwToTaW9qILoU5r+KwIMJCbduO2fwRET7QGdJcYsLMJvYEuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uLhoSsUY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422921,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAU1K3RbdXjvoNR+xcJOLcaozxpUtB1LkgIww6yHOdVOrzH8kfocB+lE1ZLAsjCshsKSy5AbXLqybSyP39GJ/JALhAuUQ0nyRoBRwuHnqwAV6a1S9U/jz4n1WAdf/Av8xq8E6E2lvaiC6FOa/isCDCQm3bjtn8ERE+0BnSXGLCzCb2BLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7i4QfnBx"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422921,
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
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAU1K3RbdXjvoNR+xcJOLcaozxpUtB1LkgIww6yHOdVOrzH8kfocB+lE1ZLAsjCshsKSy5AbXLqybSyP39GJ/JALhAuUQ0nyRoBRwuHnqwAV6a1S9U/jz4n1WAdf/Av8xq8E6E2lvaiC6FOa/isCDCQm3bjtn8ERE+0BnSXGLCzCb2BLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7i4QfnBx",
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
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAU1K3RbdXjvoNR+xcJOLcaozxpUtB1LkgIww6yHOdVOrzH8kfocB+lE1ZLAsjCshsKSy5AbXLqybSyP39GJ/JALhAuUQ0nyRoBRwuHnqwAV6a1S9U/jz4n1WAdf/Av8xq8E6E2lvaiC6FOa/isCDCQm3bjtn8ERE+0BnSXGLCzCb2BLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7i4QfnBx",
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
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAU1K3RbdXjvoNR+xcJOLcaozxpUtB1LkgIww6yHOdVOrzH8kfocB+lE1ZLAsjCshsKSy5AbXLqybSyP39GJ/JALhAuUQ0nyRoBRwuHnqwAV6a1S9U/jz4n1WAdf/Av8xq8E6E2lvaiC6FOa/isCDCQm3bjtn8ERE+0BnSXGLCzCb2BLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7i4QfnBx",
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
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAU1K3RbdXjvoNR+xcJOLcaozxpUtB1LkgIww6yHOdVOrzH8kfocB+lE1ZLAsjCshsKSy5AbXLqybSyP39GJ/JALhAuUQ0nyRoBRwuHnqwAV6a1S9U/jz4n1WAdf/Av8xq8E6E2lvaiC6FOa/isCDCQm3bjtn8ERE+0BnSXGLCzCb2BLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7i4QfnBx",
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
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
    "data": {
      "message": {
        "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "info": "Hello",
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
    "data": {
      "message": {
        "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "info": "Hello back",
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422920,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
  "id": -576460752303422920,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999999
    },
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
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
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
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
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
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
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
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
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
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
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
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
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
    "data": {
      "state": "tx_+QENCwH4hLhAU1K3RbdXjvoNR+xcJOLcaozxpUtB1LkgIww6yHOdVOrzH8kfocB+lE1ZLAsjCshsKSy5AbXLqybSyP39GJ/JALhAuUQ0nyRoBRwuHnqwAV6a1S9U/jz4n1WAdf/Av8xq8E6E2lvaiC6FOa/isCDCQm3bjtn8ERE+0BnSXGLCzCb2BLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7i4QfnBx"
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
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
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
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
    "data": {
      "state": "tx_+QENCwH4hLhAU1K3RbdXjvoNR+xcJOLcaozxpUtB1LkgIww6yHOdVOrzH8kfocB+lE1ZLAsjCshsKSy5AbXLqybSyP39GJ/JALhAuUQ0nyRoBRwuHnqwAV6a1S9U/jz4n1WAdf/Av8xq8E6E2lvaiC6FOa/isCDCQm3bjtn8ERE+0BnSXGLCzCb2BLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7i4QfnBx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {
    "fee": 123456789876543
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBi5lXFZXfQLtaokZaydJArpfvjqk+dsSm0HHrlaxgsYwoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIC5AUz5AUk8AfkBP/kBPKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvkBGPh0oCbziXyYo8Ox+VZtROqlQQtKKd21jKCiqh29ftJZTs5e+FGAgICAgICAgICAgICg7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqug5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqeAgID4T6DlslFZIexXT120YXqqt3xFqwcxbt0Suq1WIBNf47yap+2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAH4T6Dt/5Hiy5W70qsqTzdexfFGw0mN5gAjP38MM0HGdpS2q+2gNbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX//AwMDAwACGcEiGGw8/EWgr3G0=",
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
  "method": "channels.close_solo_sign",
  "params": {
    "signed_tx": "tx_+QHrCwH4QrhAHHEGFphwLZ4/eA3ffouFpq5YZYPmdywHP6DyUosgyTGqZu0VZ2oiohGB5vKCdM65G1RUGyWb5ntsZakxxKqxDrkBovkBnzYBoQYuZVxWV30C7WqJGWsnSQK6X746pPnbEptBx65WsYLGMKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCAuQFM+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMAAhnBIhhsPPxGyLJfo"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAHHEGFphwLZ4/eA3ffouFpq5YZYPmdywHP6DyUosgyTGqZu0VZ2oiohGB5vKCdM65G1RUGyWb5ntsZakxxKqxDrkBovkBnzYBoQYuZVxWV30C7WqJGWsnSQK6X746pPnbEptBx65WsYLGMKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCAuQFM+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMAAhnBIhhsPPxGyLJfo",
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
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
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
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAHHEGFphwLZ4/eA3ffouFpq5YZYPmdywHP6DyUosgyTGqZu0VZ2oiohGB5vKCdM65G1RUGyWb5ntsZakxxKqxDrkBovkBnzYBoQYuZVxWV30C7WqJGWsnSQK6X746pPnbEptBx65WsYLGMKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCAuQFM+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMAAhnBIhhsPPxGyLJfo",
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
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
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
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBi5lXFZXfQLtaokZaydJArpfvjqk+dsSm0HHrlaxgsYwoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIY/qiUiX/+GJGE5yoABAIYPXtZ/KAASGA6vrw==",
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
    "signed_tx": "tx_+KcLAfhCuEA9QLhqe/vhFwsu8LLlmXeT8pX8Hvw/YHX3ZLa7jSxGUgax9OHEIHHwue2gvCFlR6O7GdHHBV45Dhy45mt8xpoDuF/4XTgBoQYuZVxWV30C7WqJGWsnSQK6X746pPnbEptBx65WsYLGMKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl//hiRhOcqAAQCGD17WfygAEvH0Q9g="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEA9QLhqe/vhFwsu8LLlmXeT8pX8Hvw/YHX3ZLa7jSxGUgax9OHEIHHwue2gvCFlR6O7GdHHBV45Dhy45mt8xpoDuF/4XTgBoQYuZVxWV30C7WqJGWsnSQK6X746pPnbEptBx65WsYLGMKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl//hiRhOcqAAQCGD17WfygAEvH0Q9g=",
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
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEA9QLhqe/vhFwsu8LLlmXeT8pX8Hvw/YHX3ZLa7jSxGUgax9OHEIHHwue2gvCFlR6O7GdHHBV45Dhy45mt8xpoDuF/4XTgBoQYuZVxWV30C7WqJGWsnSQK6X746pPnbEptBx65WsYLGMKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl//hiRhOcqAAQCGD17WfygAEvH0Q9g=",
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
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
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
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
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
    "channel_id": "ch_MS85V5F7TM9SV71jyzEeBdNwzUos6remcbjaWTEFRExit5223",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection
