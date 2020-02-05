
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_slash_%2F3129%5Binitiator44initiator%5D
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
      "fsm_id": "ba_kTnZDsXKfHv0NeAzLYRNZ3AejDk9g1tpWOnaOWToC08PkVC3"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_slash_%2F3129%5Binitiator44initiator%5D
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
      "fsm_id": "ba_+MYOatujfCLalL+pq0PkwjJgIIK6H5bX1+nCRWvc2PIwpAhD"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4Qa9iWyg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423295,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEB3ffTkkNQ3TMCKTZ2UBnMpMF51VD6vqfnwlLnYjrnW9W5xwGiseP2MjA7khFYUQlrh61/ywr83f78ZkTV32TkAuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uEHkkKU4="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423295,
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
      "signed_tx": "tx_+MsLAfhCuEB3ffTkkNQ3TMCKTZ2UBnMpMF51VD6vqfnwlLnYjrnW9W5xwGiseP2MjA7khFYUQlrh61/ywr83f78ZkTV32TkAuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uEHkkKU4=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423294,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAFUchWXz4+J1aP+PejMTDXG5zvpvgOB8M/bgbjrVDZY3prhk+z4Ka5CyY/Zd76JZevCh5/NbQ8u0MXiq/mTn4DbhAd3305JDUN0zAik2dlAZzKTBedVQ+r6n58JS52I651vVuccBorHj9jIwO5IRWFEJa4etf8sK/N3+/GZE1d9k5ALiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hB0yDmO"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423294,
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAFUchWXz4+J1aP+PejMTDXG5zvpvgOB8M/bgbjrVDZY3prhk+z4Ka5CyY/Zd76JZevCh5/NbQ8u0MXiq/mTn4DbhAd3305JDUN0zAik2dlAZzKTBedVQ+r6n58JS52I651vVuccBorHj9jIwO5IRWFEJa4etf8sK/N3+/GZE1d9k5ALiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hB0yDmO",
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAFUchWXz4+J1aP+PejMTDXG5zvpvgOB8M/bgbjrVDZY3prhk+z4Ka5CyY/Zd76JZevCh5/NbQ8u0MXiq/mTn4DbhAd3305JDUN0zAik2dlAZzKTBedVQ+r6n58JS52I651vVuccBorHj9jIwO5IRWFEJa4etf8sK/N3+/GZE1d9k5ALiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hB0yDmO",
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAFUchWXz4+J1aP+PejMTDXG5zvpvgOB8M/bgbjrVDZY3prhk+z4Ka5CyY/Zd76JZevCh5/NbQ8u0MXiq/mTn4DbhAd3305JDUN0zAik2dlAZzKTBedVQ+r6n58JS52I651vVuccBorHj9jIwO5IRWFEJa4etf8sK/N3+/GZE1d9k5ALiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hB0yDmO",
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAFUchWXz4+J1aP+PejMTDXG5zvpvgOB8M/bgbjrVDZY3prhk+z4Ka5CyY/Zd76JZevCh5/NbQ8u0MXiq/mTn4DbhAd3305JDUN0zAik2dlAZzKTBedVQ+r6n58JS52I651vVuccBorHj9jIwO5IRWFEJa4etf8sK/N3+/GZE1d9k5ALiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hB0yDmO",
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "message": {
        "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "message": {
        "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
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
  "id": -576460752303423293,
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
  "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
  "id": -576460752303423293,
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "state": "tx_+QENCwH4hLhAFUchWXz4+J1aP+PejMTDXG5zvpvgOB8M/bgbjrVDZY3prhk+z4Ka5CyY/Zd76JZevCh5/NbQ8u0MXiq/mTn4DbhAd3305JDUN0zAik2dlAZzKTBedVQ+r6n58JS52I651vVuccBorHj9jIwO5IRWFEJa4etf8sK/N3+/GZE1d9k5ALiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hB0yDmO"
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "state": "tx_+QENCwH4hLhAFUchWXz4+J1aP+PejMTDXG5zvpvgOB8M/bgbjrVDZY3prhk+z4Ka5CyY/Zd76JZevCh5/NbQ8u0MXiq/mTn4DbhAd3305JDUN0zAik2dlAZzKTBedVQ+r6n58JS52I651vVuccBorHj9jIwO5IRWFEJa4etf8sK/N3+/GZE1d9k5ALiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hB0yDmO"
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
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "poi": "pi_+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMDiSa4B"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423292,
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
  "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
  "id": -576460752303423292,
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

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBh+EzGQSDhTgg+o7QcjF6i97RFCMtDrF7COb0FktaFyTAqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B1PwlZM=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainTransfer",
          "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
  "id": -576460752303423291,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBCNNHFxu/R+ypbtOCh7BrA+oFrAYYHzhZTR8BmTOgO2yYKd7lXwU7+xlfvD3Mu9dEeVp1T1aVuH8UPk/7wU9UMuEj4RjkCoQYfhMxkEg4U4IPqO0HIxeove0RQjLQ6xewjm9BZLWhckwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfzGW4o"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
  "id": -576460752303423291,
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBCNNHFxu/R+ypbtOCh7BrA+oFrAYYHzhZTR8BmTOgO2yYKd7lXwU7+xlfvD3Mu9dEeVp1T1aVuH8UPk/7wU9UMuEj4RjkCoQYfhMxkEg4U4IPqO0HIxeove0RQjLQ6xewjm9BZLWhckwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfzGW4o",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainTransfer",
          "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
  "id": -576460752303423290,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBCNNHFxu/R+ypbtOCh7BrA+oFrAYYHzhZTR8BmTOgO2yYKd7lXwU7+xlfvD3Mu9dEeVp1T1aVuH8UPk/7wU9UMuECR/+7ZaF0OqeiRuRVkjsd2aEynOBmBk+tFETlA5H/jNIVB2A1RbKDe8yHGBWpUbWZzLnPXK+pl1Wkml094WxUAuEj4RjkCoQYfhMxkEg4U4IPqO0HIxeove0RQjLQ6xewjm9BZLWhckwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcDKgN0"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
  "id": -576460752303423290,
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "state": "tx_+NILAfiEuEBCNNHFxu/R+ypbtOCh7BrA+oFrAYYHzhZTR8BmTOgO2yYKd7lXwU7+xlfvD3Mu9dEeVp1T1aVuH8UPk/7wU9UMuECR/+7ZaF0OqeiRuRVkjsd2aEynOBmBk+tFETlA5H/jNIVB2A1RbKDe8yHGBWpUbWZzLnPXK+pl1Wkml094WxUAuEj4RjkCoQYfhMxkEg4U4IPqO0HIxeove0RQjLQ6xewjm9BZLWhckwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcDKgN0"
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "state": "tx_+NILAfiEuEBCNNHFxu/R+ypbtOCh7BrA+oFrAYYHzhZTR8BmTOgO2yYKd7lXwU7+xlfvD3Mu9dEeVp1T1aVuH8UPk/7wU9UMuECR/+7ZaF0OqeiRuRVkjsd2aEynOBmBk+tFETlA5H/jNIVB2A1RbKDe8yHGBWpUbWZzLnPXK+pl1Wkml094WxUAuEj4RjkCoQYfhMxkEg4U4IPqO0HIxeove0RQjLQ6xewjm9BZLWhckwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcDKgN0"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423289,
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
  "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
  "id": -576460752303423289,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999998
    },
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423288,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
  "id": -576460752303423288,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBCNNHFxu/R+ypbtOCh7BrA+oFrAYYHzhZTR8BmTOgO2yYKd7lXwU7+xlfvD3Mu9dEeVp1T1aVuH8UPk/7wU9UMuECR/+7ZaF0OqeiRuRVkjsd2aEynOBmBk+tFETlA5H/jNIVB2A1RbKDe8yHGBWpUbWZzLnPXK+pl1Wkml094WxUAuEj4RjkCoQYfhMxkEg4U4IPqO0HIxeove0RQjLQ6xewjm9BZLWhckwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcDKgN0",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBCNNHFxu/R+ypbtOCh7BrA+oFrAYYHzhZTR8BmTOgO2yYKd7lXwU7+xlfvD3Mu9dEeVp1T1aVuH8UPk/7wU9UMuECR/+7ZaF0OqeiRuRVkjsd2aEynOBmBk+tFETlA5H/jNIVB2A1RbKDe8yHGBWpUbWZzLnPXK+pl1Wkml094WxUAuEj4RjkCoQYfhMxkEg4U4IPqO0HIxeove0RQjLQ6xewjm9BZLWhckwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcDKgN0",
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEBCNNHFxu/R+ypbtOCh7BrA+oFrAYYHzhZTR8BmTOgO2yYKd7lXwU7+xlfvD3Mu9dEeVp1T1aVuH8UPk/7wU9UMuECR/+7ZaF0OqeiRuRVkjsd2aEynOBmBk+tFETlA5H/jNIVB2A1RbKDe8yHGBWpUbWZzLnPXK+pl1Wkml094WxUAuEj4RjkCoQYfhMxkEg4U4IPqO0HIxeove0RQjLQ6xewjm9BZLWhckwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcDKgN0",
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
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
  "id": -576460752303423287,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
  "id": -576460752303423287,
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBh+EzGQSDhTgg+o7QcjF6i97RFCMtDrF7COb0FktaFyToQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79LjU+NILAfiEuEBCNNHFxu/R+ypbtOCh7BrA+oFrAYYHzhZTR8BmTOgO2yYKd7lXwU7+xlfvD3Mu9dEeVp1T1aVuH8UPk/7wU9UMuECR/+7ZaF0OqeiRuRVkjsd2aEynOBmBk+tFETlA5H/jNIVB2A1RbKDe8yHGBWpUbWZzLnPXK+pl1Wkml094WxUAuEj4RjkCoQYfhMxkEg4U4IPqO0HIxeove0RQjLQ6xewjm9BZLWhckwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAe5AUz5AUk8AfkBP/kBPKBr5sKqJEGy2c6K7OYj3B0QSM9YKqp12Cwu0FcoBE12iPkBGPhPoEqVXL/Gi63p37+99IW1AH7Eb//F/0G9uCVe9zFlBvdG7aAxNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAvh0oGvmwqokQbLZzors5iPcHRBIz1gqqnXYLC7QVygETXaI+FGAgICAgICAgICAgICgbYJjbN6iM9NklD1uSm6sox3iiItBMXXpvq1p2MXyRnGgSpVcv8aLrenfv730hbUAfsRv/8X/Qb24JV73MWUG90aAgID4T6BtgmNs3qIz02SUPW5KbqyjHeKIi0Exdem+rWnYxfJGce2gNbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/7AwMDAwACGGR7ISegAEhFhZsM=",
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
    "signed_tx": "tx_+QLACwH4QrhAsEn+SKhPLOh7mmKoHpj4+OQZaHnVatjP8PUnwci+Xn5RzA4mR36at5rK/5j5l1FZGieSga4SOTHX1SY4o9huAbkCd/kCdDcBoQYfhMxkEg4U4IPqO0HIxeove0RQjLQ6xewjm9BZLWhck6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/S41PjSCwH4hLhAQjTRxcbv0fsqW7TgoewawPqBawGGB84WU0fAZkzoDtsmCne5V8FO/sZX7w9zLvXRHladU9Wlbh/FD5P+8FPVDLhAkf/u2WhdDqnokbkVZI7HdmhMpzgZgZPrRRE5QOR/4zSFQdgNUWyg3vMhxgVqVG1mcy5z1yvqZdVpJpdPeFsVALhI+EY5AqEGH4TMZBIOFOCD6jtByMXqL3tEUIy0OsXsI5vQWS1oXJMCoCob2XomoLXVasfWjCsSocPPoSuXDKwFnKboiPTlQXwHuQFM+QFJPAH5AT/5ATyga+bCqiRBstnOiuzmI9wdEEjPWCqqddgsLtBXKARNdoj5ARj4T6BKlVy/xout6d+/vfSFtQB+xG//xf9BvbglXvcxZQb3Ru2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAL4dKBr5sKqJEGy2c6K7OYj3B0QSM9YKqp12Cwu0FcoBE12iPhRgICAgICAgICAgICAoG2CY2zeojPTZJQ9bkpurKMd4oiLQTF16b6tadjF8kZxoEqVXL/Gi63p37+99IW1AH7Eb//F/0G9uCVe9zFlBvdGgICA+E+gbYJjbN6iM9NklD1uSm6sox3iiItBMXXpvq1p2MXyRnHtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl/+wMDAwMAAhhkeyEnoABJ3oirv"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAsEn+SKhPLOh7mmKoHpj4+OQZaHnVatjP8PUnwci+Xn5RzA4mR36at5rK/5j5l1FZGieSga4SOTHX1SY4o9huAbkCd/kCdDcBoQYfhMxkEg4U4IPqO0HIxeove0RQjLQ6xewjm9BZLWhck6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/S41PjSCwH4hLhAQjTRxcbv0fsqW7TgoewawPqBawGGB84WU0fAZkzoDtsmCne5V8FO/sZX7w9zLvXRHladU9Wlbh/FD5P+8FPVDLhAkf/u2WhdDqnokbkVZI7HdmhMpzgZgZPrRRE5QOR/4zSFQdgNUWyg3vMhxgVqVG1mcy5z1yvqZdVpJpdPeFsVALhI+EY5AqEGH4TMZBIOFOCD6jtByMXqL3tEUIy0OsXsI5vQWS1oXJMCoCob2XomoLXVasfWjCsSocPPoSuXDKwFnKboiPTlQXwHuQFM+QFJPAH5AT/5ATyga+bCqiRBstnOiuzmI9wdEEjPWCqqddgsLtBXKARNdoj5ARj4T6BKlVy/xout6d+/vfSFtQB+xG//xf9BvbglXvcxZQb3Ru2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAL4dKBr5sKqJEGy2c6K7OYj3B0QSM9YKqp12Cwu0FcoBE12iPhRgICAgICAgICAgICAoG2CY2zeojPTZJQ9bkpurKMd4oiLQTF16b6tadjF8kZxoEqVXL/Gi63p37+99IW1AH7Eb//F/0G9uCVe9zFlBvdGgICA+E+gbYJjbN6iM9NklD1uSm6sox3iiItBMXXpvq1p2MXyRnHtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl/+wMDAwMAAhhkeyEnoABJ3oirv",
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAsEn+SKhPLOh7mmKoHpj4+OQZaHnVatjP8PUnwci+Xn5RzA4mR36at5rK/5j5l1FZGieSga4SOTHX1SY4o9huAbkCd/kCdDcBoQYfhMxkEg4U4IPqO0HIxeove0RQjLQ6xewjm9BZLWhck6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/S41PjSCwH4hLhAQjTRxcbv0fsqW7TgoewawPqBawGGB84WU0fAZkzoDtsmCne5V8FO/sZX7w9zLvXRHladU9Wlbh/FD5P+8FPVDLhAkf/u2WhdDqnokbkVZI7HdmhMpzgZgZPrRRE5QOR/4zSFQdgNUWyg3vMhxgVqVG1mcy5z1yvqZdVpJpdPeFsVALhI+EY5AqEGH4TMZBIOFOCD6jtByMXqL3tEUIy0OsXsI5vQWS1oXJMCoCob2XomoLXVasfWjCsSocPPoSuXDKwFnKboiPTlQXwHuQFM+QFJPAH5AT/5ATyga+bCqiRBstnOiuzmI9wdEEjPWCqqddgsLtBXKARNdoj5ARj4T6BKlVy/xout6d+/vfSFtQB+xG//xf9BvbglXvcxZQb3Ru2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAL4dKBr5sKqJEGy2c6K7OYj3B0QSM9YKqp12Cwu0FcoBE12iPhRgICAgICAgICAgICAoG2CY2zeojPTZJQ9bkpurKMd4oiLQTF16b6tadjF8kZxoEqVXL/Gi63p37+99IW1AH7Eb//F/0G9uCVe9zFlBvdGgICA+E+gbYJjbN6iM9NklD1uSm6sox3iiItBMXXpvq1p2MXyRnHtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl/+wMDAwMAAhhkeyEnoABJ3oirv",
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBh+EzGQSDhTgg+o7QcjF6i97RFCMtDrF7COb0FktaFyToQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIY/qiUiX/6GJGE5yoACAIYPXtZ/KAAGdOuHjA==",
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
    "signed_tx": "tx_+KcLAfhCuEBUruq82B2X/Z0d0ukwKimFies1fnN6OQUh8USNGY2N3r+uZiIWbT/ZisCgsKuv0QMUslS9TX/JISn+ScszC2MAuF/4XTgBoQYfhMxkEg4U4IPqO0HIxeove0RQjLQ6xewjm9BZLWhck6EB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl/+hiRhOcqAAgCGD17WfygABklB+gA="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBUruq82B2X/Z0d0ukwKimFies1fnN6OQUh8USNGY2N3r+uZiIWbT/ZisCgsKuv0QMUslS9TX/JISn+ScszC2MAuF/4XTgBoQYfhMxkEg4U4IPqO0HIxeove0RQjLQ6xewjm9BZLWhck6EB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl/+hiRhOcqAAgCGD17WfygABklB+gA=",
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
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBUruq82B2X/Z0d0ukwKimFies1fnN6OQUh8USNGY2N3r+uZiIWbT/ZisCgsKuv0QMUslS9TX/JISn+ScszC2MAuF/4XTgBoQYfhMxkEg4U4IPqO0HIxeove0RQjLQ6xewjm9BZLWhck6EB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl/+hiRhOcqAAgCGD17WfygABklB+gA=",
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
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
    "channel_id": "ch_Et72swxcKCAJ8KzUDm17X1Ukuo6W7516WfYDPdUoTYpArCdfQ",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_slash_%2F3129%5Binitiator44responder%5D
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
      "fsm_id": "ba_rTQrRTFejO7oDkcSmXOwZkZsNJho6IMmggkO9B9dJI0J/AvZ"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_slash_%2F3129%5Binitiator44responder%5D
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
      "fsm_id": "ba_hf8NTsTcGyWOzeiM97m+6Gy18h4isX+RXosBFoFMFNCirBE3"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4Tjbo5RA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423286,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBjdHrxUJ8csd37umJXyx8P+FFQCk0y6GfItu6aEl7ZOshbrlqYcZAOslRifkZ43/XA3lRMl/6bHsaCmSDuvSkPuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uE3xunnQ="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423286,
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
      "signed_tx": "tx_+MsLAfhCuEBjdHrxUJ8csd37umJXyx8P+FFQCk0y6GfItu6aEl7ZOshbrlqYcZAOslRifkZ43/XA3lRMl/6bHsaCmSDuvSkPuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uE3xunnQ=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423285,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAY3R68VCfHLHd+7piV8sfD/hRUApNMuhnyLbumhJe2TrIW65amHGQDrJUYn5GeN/1wN5UTJf+mx7Ggpkg7r0pD7hAwAfWmlLPIawVBaSayb7KFHrkW1dwhGG9JFHO22eL+JWr53YZbCCCmMXSk9qGjTcLeC0FEFLnv8oL/u/6XAyMBriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hPHTEfw"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423285,
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAY3R68VCfHLHd+7piV8sfD/hRUApNMuhnyLbumhJe2TrIW65amHGQDrJUYn5GeN/1wN5UTJf+mx7Ggpkg7r0pD7hAwAfWmlLPIawVBaSayb7KFHrkW1dwhGG9JFHO22eL+JWr53YZbCCCmMXSk9qGjTcLeC0FEFLnv8oL/u/6XAyMBriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hPHTEfw",
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAY3R68VCfHLHd+7piV8sfD/hRUApNMuhnyLbumhJe2TrIW65amHGQDrJUYn5GeN/1wN5UTJf+mx7Ggpkg7r0pD7hAwAfWmlLPIawVBaSayb7KFHrkW1dwhGG9JFHO22eL+JWr53YZbCCCmMXSk9qGjTcLeC0FEFLnv8oL/u/6XAyMBriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hPHTEfw",
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAY3R68VCfHLHd+7piV8sfD/hRUApNMuhnyLbumhJe2TrIW65amHGQDrJUYn5GeN/1wN5UTJf+mx7Ggpkg7r0pD7hAwAfWmlLPIawVBaSayb7KFHrkW1dwhGG9JFHO22eL+JWr53YZbCCCmMXSk9qGjTcLeC0FEFLnv8oL/u/6XAyMBriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hPHTEfw",
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAY3R68VCfHLHd+7piV8sfD/hRUApNMuhnyLbumhJe2TrIW65amHGQDrJUYn5GeN/1wN5UTJf+mx7Ggpkg7r0pD7hAwAfWmlLPIawVBaSayb7KFHrkW1dwhGG9JFHO22eL+JWr53YZbCCCmMXSk9qGjTcLeC0FEFLnv8oL/u/6XAyMBriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hPHTEfw",
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "message": {
        "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "message": {
        "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
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
  "id": -576460752303423284,
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
  "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
  "id": -576460752303423284,
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "state": "tx_+QENCwH4hLhAY3R68VCfHLHd+7piV8sfD/hRUApNMuhnyLbumhJe2TrIW65amHGQDrJUYn5GeN/1wN5UTJf+mx7Ggpkg7r0pD7hAwAfWmlLPIawVBaSayb7KFHrkW1dwhGG9JFHO22eL+JWr53YZbCCCmMXSk9qGjTcLeC0FEFLnv8oL/u/6XAyMBriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hPHTEfw"
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "state": "tx_+QENCwH4hLhAY3R68VCfHLHd+7piV8sfD/hRUApNMuhnyLbumhJe2TrIW65amHGQDrJUYn5GeN/1wN5UTJf+mx7Ggpkg7r0pD7hAwAfWmlLPIawVBaSayb7KFHrkW1dwhGG9JFHO22eL+JWr53YZbCCCmMXSk9qGjTcLeC0FEFLnv8oL/u/6XAyMBriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7hPHTEfw"
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
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "poi": "pi_+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMDiSa4B"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423283,
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
  "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
  "id": -576460752303423283,
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

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
    "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBmYLkYZQB1Ea+afEhexGMxhDhmjOgndIbOATQaeItTeBAqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B4BGiVo=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainTransfer",
          "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
  "id": -576460752303423282,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAJ/iJH7JY6yatdowqAJGpr8eHWuvsm+OCITgJ90H9ZsB+Vau7UXfqXcf1eNvpYQJ5DEqnqqJCXL+07Nn2xtnMAuEj4RjkCoQZmC5GGUAdRGvmnxIXsRjMYQ4ZozoJ3SGzgE0GniLU3gQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeJ92Q+"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
  "id": -576460752303423282,
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAJ/iJH7JY6yatdowqAJGpr8eHWuvsm+OCITgJ90H9ZsB+Vau7UXfqXcf1eNvpYQJ5DEqnqqJCXL+07Nn2xtnMAuEj4RjkCoQZmC5GGUAdRGvmnxIXsRjMYQ4ZozoJ3SGzgE0GniLU3gQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeJ92Q+",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
          "op": "OffChainTransfer",
          "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
  "id": -576460752303423281,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAJ/iJH7JY6yatdowqAJGpr8eHWuvsm+OCITgJ90H9ZsB+Vau7UXfqXcf1eNvpYQJ5DEqnqqJCXL+07Nn2xtnMAuECTfNKFit0oMbyd5o/IvsoKyUwxrSV0LQbopORK+7uwDn0OUeqKJhkG5MH4hUTt22wOrruGGweebxueaZ8pW7EIuEj4RjkCoQZmC5GGUAdRGvmnxIXsRjMYQ4ZozoJ3SGzgE0GniLU3gQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcNi9D4"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
  "id": -576460752303423281,
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "state": "tx_+NILAfiEuEAJ/iJH7JY6yatdowqAJGpr8eHWuvsm+OCITgJ90H9ZsB+Vau7UXfqXcf1eNvpYQJ5DEqnqqJCXL+07Nn2xtnMAuECTfNKFit0oMbyd5o/IvsoKyUwxrSV0LQbopORK+7uwDn0OUeqKJhkG5MH4hUTt22wOrruGGweebxueaZ8pW7EIuEj4RjkCoQZmC5GGUAdRGvmnxIXsRjMYQ4ZozoJ3SGzgE0GniLU3gQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcNi9D4"
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "state": "tx_+NILAfiEuEAJ/iJH7JY6yatdowqAJGpr8eHWuvsm+OCITgJ90H9ZsB+Vau7UXfqXcf1eNvpYQJ5DEqnqqJCXL+07Nn2xtnMAuECTfNKFit0oMbyd5o/IvsoKyUwxrSV0LQbopORK+7uwDn0OUeqKJhkG5MH4hUTt22wOrruGGweebxueaZ8pW7EIuEj4RjkCoQZmC5GGUAdRGvmnxIXsRjMYQ4ZozoJ3SGzgE0GniLU3gQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcNi9D4"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423280,
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
  "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
  "id": -576460752303423280,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999998
    },
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423279,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
  "id": -576460752303423279,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAJ/iJH7JY6yatdowqAJGpr8eHWuvsm+OCITgJ90H9ZsB+Vau7UXfqXcf1eNvpYQJ5DEqnqqJCXL+07Nn2xtnMAuECTfNKFit0oMbyd5o/IvsoKyUwxrSV0LQbopORK+7uwDn0OUeqKJhkG5MH4hUTt22wOrruGGweebxueaZ8pW7EIuEj4RjkCoQZmC5GGUAdRGvmnxIXsRjMYQ4ZozoJ3SGzgE0GniLU3gQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcNi9D4",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAJ/iJH7JY6yatdowqAJGpr8eHWuvsm+OCITgJ90H9ZsB+Vau7UXfqXcf1eNvpYQJ5DEqnqqJCXL+07Nn2xtnMAuECTfNKFit0oMbyd5o/IvsoKyUwxrSV0LQbopORK+7uwDn0OUeqKJhkG5MH4hUTt22wOrruGGweebxueaZ8pW7EIuEj4RjkCoQZmC5GGUAdRGvmnxIXsRjMYQ4ZozoJ3SGzgE0GniLU3gQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcNi9D4",
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAJ/iJH7JY6yatdowqAJGpr8eHWuvsm+OCITgJ90H9ZsB+Vau7UXfqXcf1eNvpYQJ5DEqnqqJCXL+07Nn2xtnMAuECTfNKFit0oMbyd5o/IvsoKyUwxrSV0LQbopORK+7uwDn0OUeqKJhkG5MH4hUTt22wOrruGGweebxueaZ8pW7EIuEj4RjkCoQZmC5GGUAdRGvmnxIXsRjMYQ4ZozoJ3SGzgE0GniLU3gQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcNi9D4",
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
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
  "id": -576460752303423278,
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
  "id": -576460752303423278,
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBmYLkYZQB1Ea+afEhexGMxhDhmjOgndIbOATQaeItTeBoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROELjU+NILAfiEuEAJ/iJH7JY6yatdowqAJGpr8eHWuvsm+OCITgJ90H9ZsB+Vau7UXfqXcf1eNvpYQJ5DEqnqqJCXL+07Nn2xtnMAuECTfNKFit0oMbyd5o/IvsoKyUwxrSV0LQbopORK+7uwDn0OUeqKJhkG5MH4hUTt22wOrruGGweebxueaZ8pW7EIuEj4RjkCoQZmC5GGUAdRGvmnxIXsRjMYQ4ZozoJ3SGzgE0GniLU3gQKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAe5AUz5AUk8AfkBP/kBPKBr5sKqJEGy2c6K7OYj3B0QSM9YKqp12Cwu0FcoBE12iPkBGPhPoEqVXL/Gi63p37+99IW1AH7Eb//F/0G9uCVe9zFlBvdG7aAxNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAvh0oGvmwqokQbLZzors5iPcHRBIz1gqqnXYLC7QVygETXaI+FGAgICAgICAgICAgICgbYJjbN6iM9NklD1uSm6sox3iiItBMXXpvq1p2MXyRnGgSpVcv8aLrenfv730hbUAfsRv/8X/Qb24JV73MWUG90aAgID4T6BtgmNs3qIz02SUPW5KbqyjHeKIi0Exdem+rWnYxfJGce2gNbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/7AwMDAwACGGR7ISegAB/hFvA4=",
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
    "signed_tx": "tx_+QLACwH4QrhAKHw23OIQWCRFqm5eu4BYIOfi0OSVK4HduLOPM1TMbMCqWCcpgLkE4LCZEpwnIqqFchjRdGUOU6lbwuuCextFB7kCd/kCdDcBoQZmC5GGUAdRGvmnxIXsRjMYQ4ZozoJ3SGzgE0GniLU3gaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThC41PjSCwH4hLhACf4iR+yWOsmrXaMKgCRqa/Hh1rr7JvjgiE4CfdB/WbAflWru1F36l3H9Xjb6WECeQxKp6qiQly/tOzZ9sbZzALhAk3zShYrdKDG8neaPyL7KCslMMa0ldC0G6KTkSvu7sA59DlHqiiYZBuTB+IVE7dtsDq67hhsHnm8bnmmfKVuxCLhI+EY5AqEGZguRhlAHURr5p8SF7EYzGEOGaM6Cd0hs4BNBp4i1N4ECoCob2XomoLXVasfWjCsSocPPoSuXDKwFnKboiPTlQXwHuQFM+QFJPAH5AT/5ATyga+bCqiRBstnOiuzmI9wdEEjPWCqqddgsLtBXKARNdoj5ARj4T6BKlVy/xout6d+/vfSFtQB+xG//xf9BvbglXvcxZQb3Ru2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAL4dKBr5sKqJEGy2c6K7OYj3B0QSM9YKqp12Cwu0FcoBE12iPhRgICAgICAgICAgICAoG2CY2zeojPTZJQ9bkpurKMd4oiLQTF16b6tadjF8kZxoEqVXL/Gi63p37+99IW1AH7Eb//F/0G9uCVe9zFlBvdGgICA+E+gbYJjbN6iM9NklD1uSm6sox3iiItBMXXpvq1p2MXyRnHtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl/+wMDAwMAAhhkeyEnoAAfMFhDv"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAKHw23OIQWCRFqm5eu4BYIOfi0OSVK4HduLOPM1TMbMCqWCcpgLkE4LCZEpwnIqqFchjRdGUOU6lbwuuCextFB7kCd/kCdDcBoQZmC5GGUAdRGvmnxIXsRjMYQ4ZozoJ3SGzgE0GniLU3gaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThC41PjSCwH4hLhACf4iR+yWOsmrXaMKgCRqa/Hh1rr7JvjgiE4CfdB/WbAflWru1F36l3H9Xjb6WECeQxKp6qiQly/tOzZ9sbZzALhAk3zShYrdKDG8neaPyL7KCslMMa0ldC0G6KTkSvu7sA59DlHqiiYZBuTB+IVE7dtsDq67hhsHnm8bnmmfKVuxCLhI+EY5AqEGZguRhlAHURr5p8SF7EYzGEOGaM6Cd0hs4BNBp4i1N4ECoCob2XomoLXVasfWjCsSocPPoSuXDKwFnKboiPTlQXwHuQFM+QFJPAH5AT/5ATyga+bCqiRBstnOiuzmI9wdEEjPWCqqddgsLtBXKARNdoj5ARj4T6BKlVy/xout6d+/vfSFtQB+xG//xf9BvbglXvcxZQb3Ru2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAL4dKBr5sKqJEGy2c6K7OYj3B0QSM9YKqp12Cwu0FcoBE12iPhRgICAgICAgICAgICAoG2CY2zeojPTZJQ9bkpurKMd4oiLQTF16b6tadjF8kZxoEqVXL/Gi63p37+99IW1AH7Eb//F/0G9uCVe9zFlBvdGgICA+E+gbYJjbN6iM9NklD1uSm6sox3iiItBMXXpvq1p2MXyRnHtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl/+wMDAwMAAhhkeyEnoAAfMFhDv",
      "type": "channel_slash_tx"
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QLACwH4QrhAKHw23OIQWCRFqm5eu4BYIOfi0OSVK4HduLOPM1TMbMCqWCcpgLkE4LCZEpwnIqqFchjRdGUOU6lbwuuCextFB7kCd/kCdDcBoQZmC5GGUAdRGvmnxIXsRjMYQ4ZozoJ3SGzgE0GniLU3gaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThC41PjSCwH4hLhACf4iR+yWOsmrXaMKgCRqa/Hh1rr7JvjgiE4CfdB/WbAflWru1F36l3H9Xjb6WECeQxKp6qiQly/tOzZ9sbZzALhAk3zShYrdKDG8neaPyL7KCslMMa0ldC0G6KTkSvu7sA59DlHqiiYZBuTB+IVE7dtsDq67hhsHnm8bnmmfKVuxCLhI+EY5AqEGZguRhlAHURr5p8SF7EYzGEOGaM6Cd0hs4BNBp4i1N4ECoCob2XomoLXVasfWjCsSocPPoSuXDKwFnKboiPTlQXwHuQFM+QFJPAH5AT/5ATyga+bCqiRBstnOiuzmI9wdEEjPWCqqddgsLtBXKARNdoj5ARj4T6BKlVy/xout6d+/vfSFtQB+xG//xf9BvbglXvcxZQb3Ru2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAL4dKBr5sKqJEGy2c6K7OYj3B0QSM9YKqp12Cwu0FcoBE12iPhRgICAgICAgICAgICAoG2CY2zeojPTZJQ9bkpurKMd4oiLQTF16b6tadjF8kZxoEqVXL/Gi63p37+99IW1AH7Eb//F/0G9uCVe9zFlBvdGgICA+E+gbYJjbN6iM9NklD1uSm6sox3iiItBMXXpvq1p2MXyRnHtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl/+wMDAwMAAhhkeyEnoAAfMFhDv",
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBmYLkYZQB1Ea+afEhexGMxhDhmjOgndIbOATQaeItTeBoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIY/qiUiX/6GJGE5yoACAIYPXtZ/KAAIDtBH7w==",
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
    "signed_tx": "tx_+KcLAfhCuEBLz6YTqKMDnDygkjAgf+HMj3Wdrs9XNHUQIfmRPisTsoQO9qv/LnkC3B3LXwYesx0mjoPOEJ0kiRQHrWD2RM4MuF/4XTgBoQZmC5GGUAdRGvmnxIXsRjMYQ4ZozoJ3SGzgE0GniLU3gaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl/+hiRhOcqAAgCGD17WfygACGQWiTs="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBLz6YTqKMDnDygkjAgf+HMj3Wdrs9XNHUQIfmRPisTsoQO9qv/LnkC3B3LXwYesx0mjoPOEJ0kiRQHrWD2RM4MuF/4XTgBoQZmC5GGUAdRGvmnxIXsRjMYQ4ZozoJ3SGzgE0GniLU3gaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl/+hiRhOcqAAgCGD17WfygACGQWiTs=",
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBLz6YTqKMDnDygkjAgf+HMj3Wdrs9XNHUQIfmRPisTsoQO9qv/LnkC3B3LXwYesx0mjoPOEJ0kiRQHrWD2RM4MuF/4XTgBoQZmC5GGUAdRGvmnxIXsRjMYQ4ZozoJ3SGzgE0GniLU3gaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl/+hiRhOcqAAgCGD17WfygACGQWiTs=",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "event": "died"
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
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
    "channel_id": "ch_mwcEJEKveAEfUn7h9kSzJdxPuWgmzczydpe9iMuFpuL3cEter",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### responder closes WebSocket connection
