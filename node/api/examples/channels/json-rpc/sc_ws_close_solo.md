
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_close_solo_%2F3117%5Binitiator%5D
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
      "fsm_id": "ba_L+iGfp/dgJ9MXCIAwOMqS8YJUn8mlYAquEXNLqcAZxARE5H8"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_close_solo_%2F3117%5Binitiator%5D
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
      "fsm_id": "ba_g84wB6XlABxQwiGDMMVIYwyBL8oX7o82QgqU9B0Nu3PxamYk"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4MiKI7sg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423301,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBZmPHVfacl8zf4nQ5KBAkoHxLj+qzjClsB2v8FGuSy2dqVjTqePnfDHpmjLt8++Vg5U4YVLMKUIfQeldbA7RQDuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uDJlHGAw="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423301,
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
      "signed_tx": "tx_+MsLAfhCuEBZmPHVfacl8zf4nQ5KBAkoHxLj+qzjClsB2v8FGuSy2dqVjTqePnfDHpmjLt8++Vg5U4YVLMKUIfQeldbA7RQDuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uDJlHGAw=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423300,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAWZjx1X2nJfM3+J0OSgQJKB8S4/qs4wpbAdr/BRrkstnalY06nj53wx6Zoy7fPvlYOVOGFSzClCH0HpXWwO0UA7hAefvhVrW6w2u9pmF9qPd9/bteNJQ+HdNdL/65XxUaSyceOmujJ0Mp1BgcZ845Gr76H3oIk4xy/1YlMBdr4PHFAbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gyesajp"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423300,
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
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAWZjx1X2nJfM3+J0OSgQJKB8S4/qs4wpbAdr/BRrkstnalY06nj53wx6Zoy7fPvlYOVOGFSzClCH0HpXWwO0UA7hAefvhVrW6w2u9pmF9qPd9/bteNJQ+HdNdL/65XxUaSyceOmujJ0Mp1BgcZ845Gr76H3oIk4xy/1YlMBdr4PHFAbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gyesajp",
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
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAWZjx1X2nJfM3+J0OSgQJKB8S4/qs4wpbAdr/BRrkstnalY06nj53wx6Zoy7fPvlYOVOGFSzClCH0HpXWwO0UA7hAefvhVrW6w2u9pmF9qPd9/bteNJQ+HdNdL/65XxUaSyceOmujJ0Mp1BgcZ845Gr76H3oIk4xy/1YlMBdr4PHFAbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gyesajp",
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
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAWZjx1X2nJfM3+J0OSgQJKB8S4/qs4wpbAdr/BRrkstnalY06nj53wx6Zoy7fPvlYOVOGFSzClCH0HpXWwO0UA7hAefvhVrW6w2u9pmF9qPd9/bteNJQ+HdNdL/65XxUaSyceOmujJ0Mp1BgcZ845Gr76H3oIk4xy/1YlMBdr4PHFAbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gyesajp",
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
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAWZjx1X2nJfM3+J0OSgQJKB8S4/qs4wpbAdr/BRrkstnalY06nj53wx6Zoy7fPvlYOVOGFSzClCH0HpXWwO0UA7hAefvhVrW6w2u9pmF9qPd9/bteNJQ+HdNdL/65XxUaSyceOmujJ0Mp1BgcZ845Gr76H3oIk4xy/1YlMBdr4PHFAbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gyesajp",
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
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
    "data": {
      "message": {
        "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
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
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
    "data": {
      "message": {
        "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
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
  "id": -576460752303423299,
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
  "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
  "id": -576460752303423299,
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
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
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
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
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
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
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
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
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
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
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
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
    "data": {
      "state": "tx_+QENCwH4hLhAWZjx1X2nJfM3+J0OSgQJKB8S4/qs4wpbAdr/BRrkstnalY06nj53wx6Zoy7fPvlYOVOGFSzClCH0HpXWwO0UA7hAefvhVrW6w2u9pmF9qPd9/bteNJQ+HdNdL/65XxUaSyceOmujJ0Mp1BgcZ845Gr76H3oIk4xy/1YlMBdr4PHFAbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gyesajp"
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
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
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
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
    "data": {
      "state": "tx_+QENCwH4hLhAWZjx1X2nJfM3+J0OSgQJKB8S4/qs4wpbAdr/BRrkstnalY06nj53wx6Zoy7fPvlYOVOGFSzClCH0HpXWwO0UA7hAefvhVrW6w2u9pmF9qPd9/bteNJQ+HdNdL/65XxUaSyceOmujJ0Mp1BgcZ845Gr76H3oIk4xy/1YlMBdr4PHFAbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gyesajp"
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
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBivpKOLfLnCHs0W87PSmv4Y7gxiPplDG/Oy/T6ROmcixoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IC5AUz5AUk8AfkBP/kBPKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvkBGPh0oCbziXyYo8Ox+VZtROqlQQtKKd21jKCiqh29ftJZTs5e+FGAgICAgICAgICAgICg7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqug5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqeAgID4T6DlslFZIexXT120YXqqt3xFqwcxbt0Suq1WIBNf47yap+2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAH4T6Dt/5Hiy5W70qsqTzdexfFGw0mN5gAjP38MM0HGdpS2q+2gNbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX//AwMDAwACGFT7sgIAADW0acl0=",
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
    "signed_tx": "tx_+QHrCwH4QrhArEL+b8QzKwJU2tcwq+6cjR9PEr91cO+HKedeO/StFKSIMunnSVrGoGuw7shXyDQDU/KpzEihqN9ixjTbdkygC7kBovkBnzYBoQYr6Sji3y5wh7NFvOz0pr+GO4MYj6ZQxvzsv0+kTpnIsaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SAuQFM+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMAAhhU+7ICAAA1MP4jV"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhArEL+b8QzKwJU2tcwq+6cjR9PEr91cO+HKedeO/StFKSIMunnSVrGoGuw7shXyDQDU/KpzEihqN9ixjTbdkygC7kBovkBnzYBoQYr6Sji3y5wh7NFvOz0pr+GO4MYj6ZQxvzsv0+kTpnIsaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SAuQFM+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMAAhhU+7ICAAA1MP4jV",
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
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
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
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhArEL+b8QzKwJU2tcwq+6cjR9PEr91cO+HKedeO/StFKSIMunnSVrGoGuw7shXyDQDU/KpzEihqN9ixjTbdkygC7kBovkBnzYBoQYr6Sji3y5wh7NFvOz0pr+GO4MYj6ZQxvzsv0+kTpnIsaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SAuQFM+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMAAhhU+7ICAAA1MP4jV",
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
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
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
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBivpKOLfLnCHs0W87PSmv4Y7gxiPplDG/Oy/T6ROmcixoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIY/qiUiX/+GJGE5yoABAIYPXtZ/KAAEcnkHDg==",
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
    "signed_tx": "tx_+KcLAfhCuEAlReo/doIu3ipYpvs9/VIrJ8hh2MTsbv5dJtMtYEprDiba6il8j5q1CvGehz4P5uqYU17osrrut4vlM+fAuBsLuF/4XTgBoQYr6Sji3y5wh7NFvOz0pr+GO4MYj6ZQxvzsv0+kTpnIsaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl//hiRhOcqAAQCGD17WfygABAzui/g="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEAlReo/doIu3ipYpvs9/VIrJ8hh2MTsbv5dJtMtYEprDiba6il8j5q1CvGehz4P5uqYU17osrrut4vlM+fAuBsLuF/4XTgBoQYr6Sji3y5wh7NFvOz0pr+GO4MYj6ZQxvzsv0+kTpnIsaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl//hiRhOcqAAQCGD17WfygABAzui/g=",
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
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEAlReo/doIu3ipYpvs9/VIrJ8hh2MTsbv5dJtMtYEprDiba6il8j5q1CvGehz4P5uqYU17osrrut4vlM+fAuBsLuF/4XTgBoQYr6Sji3y5wh7NFvOz0pr+GO4MYj6ZQxvzsv0+kTpnIsaEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl//hiRhOcqAAQCGD17WfygABAzui/g=",
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
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
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
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
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
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
    "data": {
      "event": "closed_confirmed"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_LLeEVw8R6Qu6G5yaKGRB1StaJ26eem1RmMTKdFVhTfFZYE3hV",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=initiator&slogan=aehttp_sc_SUITE%3Asc_ws_close_solo_%2F3117%5Bresponder%5D
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
      "fsm_id": "ba_vsdWfFNmZSrhOkz66TNkJKlhUrMZZSn7KTJqDnRBorLM4/Ea"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub&role=responder&slogan=aehttp_sc_SUITE%3Asc_ws_close_solo_%2F3117%5Bresponder%5D
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
      "fsm_id": "ba_tW6CK0KyxPpWRls1Gcb41bl0I2cNYnNxMueuZ+GvB3/h99Bk"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4OJfbkpA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423298,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAgMyNvQdu2aXrbRlfGQpVj6Dcruduiw1ON8smdUt8mYbWEkF8SJf7SeSqicq1hcqVdmNurKvgCA9RyCM9AreUDuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uDu6FLaU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423298,
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
      "signed_tx": "tx_+MsLAfhCuEAgMyNvQdu2aXrbRlfGQpVj6Dcruduiw1ON8smdUt8mYbWEkF8SJf7SeSqicq1hcqVdmNurKvgCA9RyCM9AreUDuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uDu6FLaU=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423297,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAIDMjb0Hbtml620ZXxkKVY+g3K7nbosNTjfLJnVLfJmG1hJBfEiX+0nkqonKtYXKlXZjbqyr4AgPUcgjPQK3lA7hAqa8i+Yq2n8GzNhA1tKrFd49JDitLwrB7GnCPTfk+yNb50WbqHlWFvaNvVtrExr1L4PcAmeZSb+r7zL0bwq9lA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7g5yHnHd"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423297,
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
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAIDMjb0Hbtml620ZXxkKVY+g3K7nbosNTjfLJnVLfJmG1hJBfEiX+0nkqonKtYXKlXZjbqyr4AgPUcgjPQK3lA7hAqa8i+Yq2n8GzNhA1tKrFd49JDitLwrB7GnCPTfk+yNb50WbqHlWFvaNvVtrExr1L4PcAmeZSb+r7zL0bwq9lA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7g5yHnHd",
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
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAIDMjb0Hbtml620ZXxkKVY+g3K7nbosNTjfLJnVLfJmG1hJBfEiX+0nkqonKtYXKlXZjbqyr4AgPUcgjPQK3lA7hAqa8i+Yq2n8GzNhA1tKrFd49JDitLwrB7GnCPTfk+yNb50WbqHlWFvaNvVtrExr1L4PcAmeZSb+r7zL0bwq9lA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7g5yHnHd",
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
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAIDMjb0Hbtml620ZXxkKVY+g3K7nbosNTjfLJnVLfJmG1hJBfEiX+0nkqonKtYXKlXZjbqyr4AgPUcgjPQK3lA7hAqa8i+Yq2n8GzNhA1tKrFd49JDitLwrB7GnCPTfk+yNb50WbqHlWFvaNvVtrExr1L4PcAmeZSb+r7zL0bwq9lA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7g5yHnHd",
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
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAIDMjb0Hbtml620ZXxkKVY+g3K7nbosNTjfLJnVLfJmG1hJBfEiX+0nkqonKtYXKlXZjbqyr4AgPUcgjPQK3lA7hAqa8i+Yq2n8GzNhA1tKrFd49JDitLwrB7GnCPTfk+yNb50WbqHlWFvaNvVtrExr1L4PcAmeZSb+r7zL0bwq9lA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7g5yHnHd",
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
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
    "data": {
      "message": {
        "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
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
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
    "data": {
      "message": {
        "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
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
  "id": -576460752303423296,
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
  "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
  "id": -576460752303423296,
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
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
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
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
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
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
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
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
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
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
    "data": {
      "state": "tx_+QENCwH4hLhAIDMjb0Hbtml620ZXxkKVY+g3K7nbosNTjfLJnVLfJmG1hJBfEiX+0nkqonKtYXKlXZjbqyr4AgPUcgjPQK3lA7hAqa8i+Yq2n8GzNhA1tKrFd49JDitLwrB7GnCPTfk+yNb50WbqHlWFvaNvVtrExr1L4PcAmeZSb+r7zL0bwq9lA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7g5yHnHd"
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
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
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
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
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
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
    "data": {
      "state": "tx_+QENCwH4hLhAIDMjb0Hbtml620ZXxkKVY+g3K7nbosNTjfLJnVLfJmG1hJBfEiX+0nkqonKtYXKlXZjbqyr4AgPUcgjPQK3lA7hAqa8i+Yq2n8GzNhA1tKrFd49JDitLwrB7GnCPTfk+yNb50WbqHlWFvaNvVtrExr1L4PcAmeZSb+r7zL0bwq9lA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7g5yHnHd"
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
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBld5GCx9UF0r2k9OBTUwOY55skjsl9Q3Nyv7EuAobaz7oQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIC5AUz5AUk8AfkBP/kBPKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvkBGPh0oCbziXyYo8Ox+VZtROqlQQtKKd21jKCiqh29ftJZTs5e+FGAgICAgICAgICAgICg7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqug5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqeAgID4T6DlslFZIexXT120YXqqt3xFqwcxbt0Suq1WIBNf47yap+2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAH4T6Dt/5Hiy5W70qsqTzdexfFGw0mN5gAjP38MM0HGdpS2q+2gNbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX//AwMDAwACGFT7sgIAABWEPxsE=",
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
    "signed_tx": "tx_+QHrCwH4QrhA4Z0hUn/37CtdmGG5X3ITev6siTJMKU5oK8RaEk2oj2L15v1Dmi9XqOe4u4dhspDM4WijL0+/SOPjkJKsLaPdB7kBovkBnzYBoQZXeRgsfVBdK9pPTgU1MDmOebJI7JfUNzcr+xLgKG2s+6EB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCAuQFM+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMAAhhU+7ICAAAWpUwUW"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhA4Z0hUn/37CtdmGG5X3ITev6siTJMKU5oK8RaEk2oj2L15v1Dmi9XqOe4u4dhspDM4WijL0+/SOPjkJKsLaPdB7kBovkBnzYBoQZXeRgsfVBdK9pPTgU1MDmOebJI7JfUNzcr+xLgKG2s+6EB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCAuQFM+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMAAhhU+7ICAAAWpUwUW",
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
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
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
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhA4Z0hUn/37CtdmGG5X3ITev6siTJMKU5oK8RaEk2oj2L15v1Dmi9XqOe4u4dhspDM4WijL0+/SOPjkJKsLaPdB7kBovkBnzYBoQZXeRgsfVBdK9pPTgU1MDmOebJI7JfUNzcr+xLgKG2s+6EB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCAuQFM+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMAAhhU+7ICAAAWpUwUW",
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
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
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
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBld5GCx9UF0r2k9OBTUwOY55skjsl9Q3Nyv7EuAobaz7oQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiX/+GJGE5yoABAIYPXtZ/KAAPgW26fA==",
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
    "signed_tx": "tx_+KcLAfhCuEDFodTF+sQr5HEZA8qvOWbQob4lFnAvoMrPJPwaNOF7y2icXXa8/qjoXOuIlmP9d0K9a0KVVPc3iZ/t4X9TQw8HuF/4XTgBoQZXeRgsfVBdK9pPTgU1MDmOebJI7JfUNzcr+xLgKG2s+6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olIl//hiRhOcqAAQCGD17WfygAD7YG0Mo="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDFodTF+sQr5HEZA8qvOWbQob4lFnAvoMrPJPwaNOF7y2icXXa8/qjoXOuIlmP9d0K9a0KVVPc3iZ/t4X9TQw8HuF/4XTgBoQZXeRgsfVBdK9pPTgU1MDmOebJI7JfUNzcr+xLgKG2s+6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olIl//hiRhOcqAAQCGD17WfygAD7YG0Mo=",
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
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEDFodTF+sQr5HEZA8qvOWbQob4lFnAvoMrPJPwaNOF7y2icXXa8/qjoXOuIlmP9d0K9a0KVVPc3iZ/t4X9TQw8HuF/4XTgBoQZXeRgsfVBdK9pPTgU1MDmOebJI7JfUNzcr+xLgKG2s+6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olIl//hiRhOcqAAQCGD17WfygAD7YG0Mo=",
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
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
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
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
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
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
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
    "channel_id": "ch_fXP6mc9Tqp6CtWcTMVRA3UTdpWamRrM7TStGsQw2kBYbWwmMa",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection

#### initiator closes WebSocket connection
