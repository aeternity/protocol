
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha&keep_running=false&lock_period=10&port=12652&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF&role=initiator
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
      "fsm_id": "ba_X2hydGcO+Ic+XMSSoBpIGhH+Z4904k31nGT8r/WgrhFton1z"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha&keep_running=false&lock_period=10&port=12652&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF&role=responder
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
      "fsm_id": "ba_IJccVIuPrAfR9OjfjIK/nuw51YE8xaHSyuWIvXZaEpahXGZS"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAXz0GMyA4E0e8QDOUx4u/S5b8mhKyj43sJb2liSu1purhj+qJSJgAKEB32ubym75yFGPMnmsNphehAjMqYCG213hh31RJbnq8k2GJGE5yoAAAgoAhhAGeddIAMCgSkGNDS9Iv0PcGyVs5DiCzKjhf1kWQDaPy3HZRumFmGwBwSQ6vg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421946,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBGgRK5uQs+I6P92mt6VEE+9+Alu6+T8vhDBTa5fyzV4vyzOVKoYbfdnD+ZjUNSlIPNQFIf288KpZaL5Ad4rncCuIP4gTIBoQF89BjMgOBNHvEAzlMeLv0uW/JoSso+N7CW9pYkrtabq4Y/qiUiYAChAd9rm8pu+chRjzJ5rDaYXoQIzKmAhttd4Yd9USW56vJNhiRhOcqAAAIKAIYQBnnXSADAoEpBjQ0vSL9D3BslbOQ4gsyo4X9ZFkA2j8tx2UbphZhsASTa2Rk="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421946,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_IJccVIuPrAfR9OjfjIK/nuw51YE8xaHSyuWIvXZaEpahXGZS"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "signed_tx": "tx_+MsLAfhCuEBGgRK5uQs+I6P92mt6VEE+9+Alu6+T8vhDBTa5fyzV4vyzOVKoYbfdnD+ZjUNSlIPNQFIf288KpZaL5Ad4rncCuIP4gTIBoQF89BjMgOBNHvEAzlMeLv0uW/JoSso+N7CW9pYkrtabq4Y/qiUiYAChAd9rm8pu+chRjzJ5rDaYXoQIzKmAhttd4Yd9USW56vJNhiRhOcqAAAIKAIYQBnnXSADAoEpBjQ0vSL9D3BslbOQ4gsyo4X9ZFkA2j8tx2UbphZhsASTa2Rk=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421945,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhARoESubkLPiOj/dprelRBPvfgJbuvk/L4QwU2uX8s1eL8szlSqGG33Zw/mY1DUpSDzUBSH9vPCqWWi+QHeK53ArhAtYn/EGw+PkbEEgmTBKQESd7xqhKk2Z+EBXlHlJQQFLh+wKXgIoKh+55ki6J0MfEb6fWsfwHcme8BgAh5KH2bCbiD+IEyAaEBfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6uGP6olImAAoQHfa5vKbvnIUY8yeaw2mF6ECMypgIbbXeGHfVElueryTYYkYTnKgAACCgCGEAZ510gAwKBKQY0NL0i/Q9wbJWzkOILMqOF/WRZANo/LcdlG6YWYbAGRo3Wo"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421945,
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhARoESubkLPiOj/dprelRBPvfgJbuvk/L4QwU2uX8s1eL8szlSqGG33Zw/mY1DUpSDzUBSH9vPCqWWi+QHeK53ArhAtYn/EGw+PkbEEgmTBKQESd7xqhKk2Z+EBXlHlJQQFLh+wKXgIoKh+55ki6J0MfEb6fWsfwHcme8BgAh5KH2bCbiD+IEyAaEBfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6uGP6olImAAoQHfa5vKbvnIUY8yeaw2mF6ECMypgIbbXeGHfVElueryTYYkYTnKgAACCgCGEAZ510gAwKBKQY0NL0i/Q9wbJWzkOILMqOF/WRZANo/LcdlG6YWYbAGRo3Wo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_X2hydGcO+Ic+XMSSoBpIGhH+Z4904k31nGT8r/WgrhFton1z"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhARoESubkLPiOj/dprelRBPvfgJbuvk/L4QwU2uX8s1eL8szlSqGG33Zw/mY1DUpSDzUBSH9vPCqWWi+QHeK53ArhAtYn/EGw+PkbEEgmTBKQESd7xqhKk2Z+EBXlHlJQQFLh+wKXgIoKh+55ki6J0MfEb6fWsfwHcme8BgAh5KH2bCbiD+IEyAaEBfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6uGP6olImAAoQHfa5vKbvnIUY8yeaw2mF6ECMypgIbbXeGHfVElueryTYYkYTnKgAACCgCGEAZ510gAwKBKQY0NL0i/Q9wbJWzkOILMqOF/WRZANo/LcdlG6YWYbAGRo3Wo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhARoESubkLPiOj/dprelRBPvfgJbuvk/L4QwU2uX8s1eL8szlSqGG33Zw/mY1DUpSDzUBSH9vPCqWWi+QHeK53ArhAtYn/EGw+PkbEEgmTBKQESd7xqhKk2Z+EBXlHlJQQFLh+wKXgIoKh+55ki6J0MfEb6fWsfwHcme8BgAh5KH2bCbiD+IEyAaEBfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6uGP6olImAAoQHfa5vKbvnIUY8yeaw2mF6ECMypgIbbXeGHfVElueryTYYkYTnKgAACCgCGEAZ510gAwKBKQY0NL0i/Q9wbJWzkOILMqOF/WRZANo/LcdlG6YWYbAGRo3Wo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhARoESubkLPiOj/dprelRBPvfgJbuvk/L4QwU2uX8s1eL8szlSqGG33Zw/mY1DUpSDzUBSH9vPCqWWi+QHeK53ArhAtYn/EGw+PkbEEgmTBKQESd7xqhKk2Z+EBXlHlJQQFLh+wKXgIoKh+55ki6J0MfEb6fWsfwHcme8BgAh5KH2bCbiD+IEyAaEBfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6uGP6olImAAoQHfa5vKbvnIUY8yeaw2mF6ECMypgIbbXeGHfVElueryTYYkYTnKgAACCgCGEAZ510gAwKBKQY0NL0i/Q9wbJWzkOILMqOF/WRZANo/LcdlG6YWYbAGRo3Wo",
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
    "to": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "message": {
        "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
        "from": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
        "info": "Hello",
        "to": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF"
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
    "to": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "message": {
        "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
        "from": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
        "info": "Hello back",
        "to": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421944,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
  "id": -576460752303421944,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_x2mdjJG7A7ocKf9T5qiDT1AGzE2RdKeKmH1wntYeDDY113eha",
      "balance": 69999999999999
    },
    {
      "account": "ak_2hPyRka8YsBFw7gfhj84Ut11d8mtFdgXGFAksjGgjkcn5pVXpF",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+QENCwH4hLhARoESubkLPiOj/dprelRBPvfgJbuvk/L4QwU2uX8s1eL8szlSqGG33Zw/mY1DUpSDzUBSH9vPCqWWi+QHeK53ArhAtYn/EGw+PkbEEgmTBKQESd7xqhKk2Z+EBXlHlJQQFLh+wKXgIoKh+55ki6J0MfEb6fWsfwHcme8BgAh5KH2bCbiD+IEyAaEBfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6uGP6olImAAoQHfa5vKbvnIUY8yeaw2mF6ECMypgIbbXeGHfVElueryTYYkYTnKgAACCgCGEAZ510gAwKBKQY0NL0i/Q9wbJWzkOILMqOF/WRZANo/LcdlG6YWYbAGRo3Wo"
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
    "channel_id": "ch_Mqj2nG3WUjYbGGc3PUVPBfsEqKdRSYcJ5gjAqZMckvKFZxoPo",
    "data": {
      "state": "tx_+QENCwH4hLhARoESubkLPiOj/dprelRBPvfgJbuvk/L4QwU2uX8s1eL8szlSqGG33Zw/mY1DUpSDzUBSH9vPCqWWi+QHeK53ArhAtYn/EGw+PkbEEgmTBKQESd7xqhKk2Z+EBXlHlJQQFLh+wKXgIoKh+55ki6J0MfEb6fWsfwHcme8BgAh5KH2bCbiD+IEyAaEBfPQYzIDgTR7xAM5THi79LlvyaErKPjewlvaWJK7Wm6uGP6olImAAoQHfa5vKbvnIUY8yeaw2mF6ECMypgIbbXeGHfVElueryTYYkYTnKgAACCgCGEAZ510gAwKBKQY0NL0i/Q9wbJWzkOILMqOF/WRZANo/LcdlG6YWYbAGRo3Wo"
    }
  },
  "version": 1
}
```
