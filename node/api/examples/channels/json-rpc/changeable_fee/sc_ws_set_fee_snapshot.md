
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=initiator
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
      "fsm_id": "ba_OSzwPhDH50ZbaSwydBbvtYvlTBT6JKFgjHxIRZ0KiTs4EYun"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu&role=responder
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
      "fsm_id": "ba_bER6ehEvqPyunIVPwRc7SE0IRoUxI98GpdUY30j/ClqRkLE+"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAb/z1CBs2DNAUvMXDBL4FOb1R0daf6S9ZWziFW54gfUVhj+qJSJgAKEBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+GJGE5yoAAAgoAhhAGeddIAMCgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYn6e6IVg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422969,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBeWD5hMHYFHaeWfOYbWSFN8ldJDBUgDCeNoVbUunAKJvugEyelbwYBhfAlYvAmBKNC9+uR+l/gfyb1BKWShgsLuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2J+prBOg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422969,
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
      "signed_tx": "tx_+MsLAfhCuEBeWD5hMHYFHaeWfOYbWSFN8ldJDBUgDCeNoVbUunAKJvugEyelbwYBhfAlYvAmBKNC9+uR+l/gfyb1BKWShgsLuIP4gTIBoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY/qiUiYAChAWZZUmmRwitTrW5qfAUG2cDknEWQXAZ862YiaC4TKda/hiRhOcqAAAIKAIYQBnnXSADAoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2J+prBOg=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422968,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAXlg+YTB2BR2nlnzmG1khTfJXSQwVIAwnjaFW1LpwCib7oBMnpW8GAYXwJWLwJgSjQvfrkfpf4H8m9QSlkoYLC7hAdFsl4poLDMuNPM9xrHWZRX+C/dLWx7fNsjdYlXPFEE78Zo7XwWnquPTpaglQwiUnTeSMQF+HDnJX/baGSW7pA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiedazcj"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422968,
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAXlg+YTB2BR2nlnzmG1khTfJXSQwVIAwnjaFW1LpwCib7oBMnpW8GAYXwJWLwJgSjQvfrkfpf4H8m9QSlkoYLC7hAdFsl4poLDMuNPM9xrHWZRX+C/dLWx7fNsjdYlXPFEE78Zo7XwWnquPTpaglQwiUnTeSMQF+HDnJX/baGSW7pA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiedazcj",
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAXlg+YTB2BR2nlnzmG1khTfJXSQwVIAwnjaFW1LpwCib7oBMnpW8GAYXwJWLwJgSjQvfrkfpf4H8m9QSlkoYLC7hAdFsl4poLDMuNPM9xrHWZRX+C/dLWx7fNsjdYlXPFEE78Zo7XwWnquPTpaglQwiUnTeSMQF+HDnJX/baGSW7pA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiedazcj",
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAXlg+YTB2BR2nlnzmG1khTfJXSQwVIAwnjaFW1LpwCib7oBMnpW8GAYXwJWLwJgSjQvfrkfpf4H8m9QSlkoYLC7hAdFsl4poLDMuNPM9xrHWZRX+C/dLWx7fNsjdYlXPFEE78Zo7XwWnquPTpaglQwiUnTeSMQF+HDnJX/baGSW7pA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiedazcj",
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAXlg+YTB2BR2nlnzmG1khTfJXSQwVIAwnjaFW1LpwCib7oBMnpW8GAYXwJWLwJgSjQvfrkfpf4H8m9QSlkoYLC7hAdFsl4poLDMuNPM9xrHWZRX+C/dLWx7fNsjdYlXPFEE78Zo7XwWnquPTpaglQwiUnTeSMQF+HDnJX/baGSW7pA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiedazcj",
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
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "message": {
        "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
        "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
        "info": "Hello",
        "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "message": {
        "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
        "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
        "info": "Hello back",
        "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422967,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422967,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 69999999999999
    },
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "event": "funding_locked"
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "state": "tx_+QENCwH4hLhAXlg+YTB2BR2nlnzmG1khTfJXSQwVIAwnjaFW1LpwCib7oBMnpW8GAYXwJWLwJgSjQvfrkfpf4H8m9QSlkoYLC7hAdFsl4poLDMuNPM9xrHWZRX+C/dLWx7fNsjdYlXPFEE78Zo7XwWnquPTpaglQwiUnTeSMQF+HDnJX/baGSW7pA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiedazcj"
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "state": "tx_+QENCwH4hLhAXlg+YTB2BR2nlnzmG1khTfJXSQwVIAwnjaFW1LpwCib7oBMnpW8GAYXwJWLwJgSjQvfrkfpf4H8m9QSlkoYLC7hAdFsl4poLDMuNPM9xrHWZRX+C/dLWx7fNsjdYlXPFEE78Zo7XwWnquPTpaglQwiUnTeSMQF+HDnJX/baGSW7pA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiedazcj"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422966,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422966,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QENCwH4hLhAXlg+YTB2BR2nlnzmG1khTfJXSQwVIAwnjaFW1LpwCib7oBMnpW8GAYXwJWLwJgSjQvfrkfpf4H8m9QSlkoYLC7hAdFsl4poLDMuNPM9xrHWZRX+C/dLWx7fNsjdYlXPFEE78Zo7XwWnquPTpaglQwiUnTeSMQF+HDnJX/baGSW7pA7iD+IEyAaEBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGP6olImAAoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv4YkYTnKgAACCgCGEAZ510gAwKBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdiedazcj",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422965,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422965,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 69999999999999
    },
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
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
    "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBknrgVVtXdhXyt3q50SODfT92Sulm609szmLizO6lRfzAqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt1Wd2yA=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainTransfer",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
  "id": -576460752303422964,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBniYXqgQgYY+Wi0+eZAehBY2PbA+URlwGZdwql4T5FXnNuuziWyjz4MYLnEt4GlEGGPmdRMyAGvLE507O3sPwDuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fInW4Y"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422964,
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBniYXqgQgYY+Wi0+eZAehBY2PbA+URlwGZdwql4T5FXnNuuziWyjz4MYLnEt4GlEGGPmdRMyAGvLE507O3sPwDuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fInW4Y",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainTransfer",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
  "id": -576460752303422963,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAzWnfvChq+YqI+JghYoiTwVsvq/ken3sa8JEJ5S2b9g+SPTme5cO5Spzne1kYkJ3DHEkY7CAyCvyDJ6tfNKJ8JuEBniYXqgQgYY+Wi0+eZAehBY2PbA+URlwGZdwql4T5FXnNuuziWyjz4MYLnEt4GlEGGPmdRMyAGvLE507O3sPwDuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eRBl5E"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422963,
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "state": "tx_+NILAfiEuEAzWnfvChq+YqI+JghYoiTwVsvq/ken3sa8JEJ5S2b9g+SPTme5cO5Spzne1kYkJ3DHEkY7CAyCvyDJ6tfNKJ8JuEBniYXqgQgYY+Wi0+eZAehBY2PbA+URlwGZdwql4T5FXnNuuziWyjz4MYLnEt4GlEGGPmdRMyAGvLE507O3sPwDuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eRBl5E"
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "state": "tx_+NILAfiEuEAzWnfvChq+YqI+JghYoiTwVsvq/ken3sa8JEJ5S2b9g+SPTme5cO5Spzne1kYkJ3DHEkY7CAyCvyDJ6tfNKJ8JuEBniYXqgQgYY+Wi0+eZAehBY2PbA+URlwGZdwql4T5FXnNuuziWyjz4MYLnEt4GlEGGPmdRMyAGvLE507O3sPwDuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eRBl5E"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422962,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422962,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 69999999999998
    },
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422961,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422961,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAzWnfvChq+YqI+JghYoiTwVsvq/ken3sa8JEJ5S2b9g+SPTme5cO5Spzne1kYkJ3DHEkY7CAyCvyDJ6tfNKJ8JuEBniYXqgQgYY+Wi0+eZAehBY2PbA+URlwGZdwql4T5FXnNuuziWyjz4MYLnEt4GlEGGPmdRMyAGvLE507O3sPwDuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eRBl5E",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422960,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {
    "fee": 123456789876543
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422960,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBknrgVVtXdhXyt3q50SODfT92Sulm609szmLizO6lRfzoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FbjU+NILAfiEuEAzWnfvChq+YqI+JghYoiTwVsvq/ken3sa8JEJ5S2b9g+SPTme5cO5Spzne1kYkJ3DHEkY7CAyCvyDJ6tfNKJ8JuEBniYXqgQgYY+Wi0+eZAehBY2PbA+URlwGZdwql4T5FXnNuuziWyjz4MYLnEt4GlEGGPmdRMyAGvLE507O3sPwDuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wKgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cAhnBIhhsPPygWh5RP",
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
  "method": "channels.snapshot_solo_sign",
  "params": {
    "signed_tx": "tx_+QFxCwH4QrhA5B27DLX7CgsUyf0A3reu5K28TgUbAS34S+lhQNiO6KJfl5WJYdxf9GghY9MNQ0UWCjIyG37VE38o08uasQ3+AbkBKPkBJTsBoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX86EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RW41PjSCwH4hLhAM1p37woavmKiPiYIWKIk8FbL6v5Hp97GvCRCeUtm/YPkj05nuXDuUqc53tZGJCdwxxJGOwgMgr8gyerXzSifCbhAZ4mF6oEIGGPlotPnmQHoQWNj2wPlEZcBmXcKpeE+RV5zbrs4lso8+DGC5xLeBpRBhj5nUTMgBryxOdOzt7D8A7hI+EY5AqEGSeuBVW1d2FfK3ernRI4N9P3ZK6WbrT2zOYuLM7qVF/MCoHNhVDnNHJffCxR3ZyCVYahHvSwSCym6yImIHzt1kiu3AIZwSIYbDz8o6Bp6bA=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422959,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422959,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 69999999999998
    },
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "balance": 40000000000002
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
    "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBknrgVVtXdhXyt3q50SODfT92Sulm609szmLizO6lRfzA6Co57fNqBzJCyJHwVtKvbBulGvI7njy2CIguwb3YS0wot+P2Gk=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainTransfer",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
  "id": -576460752303422958,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB0K2T1J2rcRQThwJb7cgirpuftXsgXeAFwonb3O5OoAFawTeWP8tA30sYDRHW/2KmojJckowExKCryO23t458DuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wOgqOe3zagcyQsiR8FbSr2wbpRryO548tgiILsG92EtMKJoLHwW"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422958,
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB0K2T1J2rcRQThwJb7cgirpuftXsgXeAFwonb3O5OoAFawTeWP8tA30sYDRHW/2KmojJckowExKCryO23t458DuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wOgqOe3zagcyQsiR8FbSr2wbpRryO548tgiILsG92EtMKJoLHwW",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainTransfer",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
  "id": -576460752303422957,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEA0B/wI/TCvHMkQw80DFQnkk+Nrj4O88eA9jYCz6cR8K66/fekSu7aG0DRHTvvaa1J5Vomji/gWXruTHc0dylwMuEB0K2T1J2rcRQThwJb7cgirpuftXsgXeAFwonb3O5OoAFawTeWP8tA30sYDRHW/2KmojJckowExKCryO23t458DuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wOgqOe3zagcyQsiR8FbSr2wbpRryO548tgiILsG92EtMKLJvG5T"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422957,
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "state": "tx_+NILAfiEuEA0B/wI/TCvHMkQw80DFQnkk+Nrj4O88eA9jYCz6cR8K66/fekSu7aG0DRHTvvaa1J5Vomji/gWXruTHc0dylwMuEB0K2T1J2rcRQThwJb7cgirpuftXsgXeAFwonb3O5OoAFawTeWP8tA30sYDRHW/2KmojJckowExKCryO23t458DuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wOgqOe3zagcyQsiR8FbSr2wbpRryO548tgiILsG92EtMKLJvG5T"
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "state": "tx_+NILAfiEuEA0B/wI/TCvHMkQw80DFQnkk+Nrj4O88eA9jYCz6cR8K66/fekSu7aG0DRHTvvaa1J5Vomji/gWXruTHc0dylwMuEB0K2T1J2rcRQThwJb7cgirpuftXsgXeAFwonb3O5OoAFawTeWP8tA30sYDRHW/2KmojJckowExKCryO23t458DuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wOgqOe3zagcyQsiR8FbSr2wbpRryO548tgiILsG92EtMKLJvG5T"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422956,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422956,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 69999999999997
    },
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "balance": 40000000000003
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422955,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422955,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEA0B/wI/TCvHMkQw80DFQnkk+Nrj4O88eA9jYCz6cR8K66/fekSu7aG0DRHTvvaa1J5Vomji/gWXruTHc0dylwMuEB0K2T1J2rcRQThwJb7cgirpuftXsgXeAFwonb3O5OoAFawTeWP8tA30sYDRHW/2KmojJckowExKCryO23t458DuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wOgqOe3zagcyQsiR8FbSr2wbpRryO548tgiILsG92EtMKLJvG5T",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/bDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAOT9RNG"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422954,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422954,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "balance": 40000000000003
    },
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 69999999999997
    }
  ],
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
    "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBknrgVVtXdhXyt3q50SODfT92Sulm609szmLizO6lRfzBKBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt28Kg2Q=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
  "id": -576460752303422953,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBbOul2e8p1PgHLp8I03dmQGkepRF2yM51CgLe9zq0/iSlx8hTOCW6g0swUoTDsMIkwti3xbwkmb8sNNRxK1wgBuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dSZwFa"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422953,
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBbOul2e8p1PgHLp8I03dmQGkepRF2yM51CgLe9zq0/iSlx8hTOCW6g0swUoTDsMIkwti3xbwkmb8sNNRxK1wgBuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7dSZwFa",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
  "id": -576460752303422952,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBbOul2e8p1PgHLp8I03dmQGkepRF2yM51CgLe9zq0/iSlx8hTOCW6g0swUoTDsMIkwti3xbwkmb8sNNRxK1wgBuEDXkG7jYqlsLiUwZWvVyRLwbeKAbUZ9OPnjJ0ARUh/fyxc8nYtJarYMKZ9M4kwgBGNp5odwdm/qRy2dMdu/5WwAuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fDyHBe"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422952,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "state": "tx_+NILAfiEuEBbOul2e8p1PgHLp8I03dmQGkepRF2yM51CgLe9zq0/iSlx8hTOCW6g0swUoTDsMIkwti3xbwkmb8sNNRxK1wgBuEDXkG7jYqlsLiUwZWvVyRLwbeKAbUZ9OPnjJ0ARUh/fyxc8nYtJarYMKZ9M4kwgBGNp5odwdm/qRy2dMdu/5WwAuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fDyHBe"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "state": "tx_+NILAfiEuEBbOul2e8p1PgHLp8I03dmQGkepRF2yM51CgLe9zq0/iSlx8hTOCW6g0swUoTDsMIkwti3xbwkmb8sNNRxK1wgBuEDXkG7jYqlsLiUwZWvVyRLwbeKAbUZ9OPnjJ0ARUh/fyxc8nYtJarYMKZ9M4kwgBGNp5odwdm/qRy2dMdu/5WwAuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fDyHBe"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422951,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422951,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "balance": 40000000000002
    },
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 69999999999998
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422950,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422950,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBbOul2e8p1PgHLp8I03dmQGkepRF2yM51CgLe9zq0/iSlx8hTOCW6g0swUoTDsMIkwti3xbwkmb8sNNRxK1wgBuEDXkG7jYqlsLiUwZWvVyRLwbeKAbUZ9OPnjJ0ARUh/fyxc8nYtJarYMKZ9M4kwgBGNp5odwdm/qRy2dMdu/5WwAuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fDyHBe",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhA5B27DLX7CgsUyf0A3reu5K28TgUbAS34S+lhQNiO6KJfl5WJYdxf9GghY9MNQ0UWCjIyG37VE38o08uasQ3+AbkBKPkBJTsBoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX86EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RW41PjSCwH4hLhAM1p37woavmKiPiYIWKIk8FbL6v5Hp97GvCRCeUtm/YPkj05nuXDuUqc53tZGJCdwxxJGOwgMgr8gyerXzSifCbhAZ4mF6oEIGGPlotPnmQHoQWNj2wPlEZcBmXcKpeE+RV5zbrs4lso8+DGC5xLeBpRBhj5nUTMgBryxOdOzt7D8A7hI+EY5AqEGSeuBVW1d2FfK3ernRI4N9P3ZK6WbrT2zOYuLM7qVF/MCoHNhVDnNHJffCxR3ZyCVYahHvSwSCym6yImIHzt1kiu3AIZwSIYbDz8o6Bp6bA==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhA5B27DLX7CgsUyf0A3reu5K28TgUbAS34S+lhQNiO6KJfl5WJYdxf9GghY9MNQ0UWCjIyG37VE38o08uasQ3+AbkBKPkBJTsBoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX86EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RW41PjSCwH4hLhAM1p37woavmKiPiYIWKIk8FbL6v5Hp97GvCRCeUtm/YPkj05nuXDuUqc53tZGJCdwxxJGOwgMgr8gyerXzSifCbhAZ4mF6oEIGGPlotPnmQHoQWNj2wPlEZcBmXcKpeE+RV5zbrs4lso8+DGC5xLeBpRBhj5nUTMgBryxOdOzt7D8A7hI+EY5AqEGSeuBVW1d2FfK3ernRI4N9P3ZK6WbrT2zOYuLM7qVF/MCoHNhVDnNHJffCxR3ZyCVYahHvSwSCym6yImIHzt1kiu3AIZwSIYbDz8o6Bp6bA==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "\u001c��\u001d\u0006_3�\"�H���9�]\u001a�]��QL4a�!E��",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422949,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422949,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBbOul2e8p1PgHLp8I03dmQGkepRF2yM51CgLe9zq0/iSlx8hTOCW6g0swUoTDsMIkwti3xbwkmb8sNNRxK1wgBuEDXkG7jYqlsLiUwZWvVyRLwbeKAbUZ9OPnjJ0ARUh/fyxc8nYtJarYMKZ9M4kwgBGNp5odwdm/qRy2dMdu/5WwAuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wSgc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7fDyHBe",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422948,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422948,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "balance": 40000000000002
    },
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 69999999999998
    }
  ],
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
    "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBknrgVVtXdhXyt3q50SODfT92Sulm609szmLizO6lRfzBaBoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCdqSnp4o=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
  "id": -576460752303422947,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDROQnjqSGSyFSQAsdtah87q6i6WYmmeqTiKGh+O21BpRpu9zO7ibytp2vNKM7K8SOq2KX6ri+mfQIhqE3NLgcBuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYW0WoI"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422947,
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDROQnjqSGSyFSQAsdtah87q6i6WYmmeqTiKGh+O21BpRpu9zO7ibytp2vNKM7K8SOq2KX6ri+mfQIhqE3NLgcBuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYW0WoI",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
  "id": -576460752303422946,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDROQnjqSGSyFSQAsdtah87q6i6WYmmeqTiKGh+O21BpRpu9zO7ibytp2vNKM7K8SOq2KX6ri+mfQIhqE3NLgcBuED98o4Pm6fgQSNqsYxCcjdNr7uNwqtP86GPLSON/C8yltzG1I6zLnGkB3Y5eJYJB3DhquOETfwQi3Jj07XDAbAHuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbkUIJ9"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422946,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "state": "tx_+NILAfiEuEDROQnjqSGSyFSQAsdtah87q6i6WYmmeqTiKGh+O21BpRpu9zO7ibytp2vNKM7K8SOq2KX6ri+mfQIhqE3NLgcBuED98o4Pm6fgQSNqsYxCcjdNr7uNwqtP86GPLSON/C8yltzG1I6zLnGkB3Y5eJYJB3DhquOETfwQi3Jj07XDAbAHuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbkUIJ9"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "state": "tx_+NILAfiEuEDROQnjqSGSyFSQAsdtah87q6i6WYmmeqTiKGh+O21BpRpu9zO7ibytp2vNKM7K8SOq2KX6ri+mfQIhqE3NLgcBuED98o4Pm6fgQSNqsYxCcjdNr7uNwqtP86GPLSON/C8yltzG1I6zLnGkB3Y5eJYJB3DhquOETfwQi3Jj07XDAbAHuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbkUIJ9"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422945,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422945,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "balance": 40000000000001
    },
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422944,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422944,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDROQnjqSGSyFSQAsdtah87q6i6WYmmeqTiKGh+O21BpRpu9zO7ibytp2vNKM7K8SOq2KX6ri+mfQIhqE3NLgcBuED98o4Pm6fgQSNqsYxCcjdNr7uNwqtP86GPLSON/C8yltzG1I6zLnGkB3Y5eJYJB3DhquOETfwQi3Jj07XDAbAHuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbkUIJ9",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422943,
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {
    "fee": 123456789876543
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422943,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBknrgVVtXdhXyt3q50SODfT92Sulm609szmLizO6lRfzoQFmWVJpkcIrU61uanwFBtnA5JxFkFwGfOtmImguEynWv7jU+NILAfiEuEDROQnjqSGSyFSQAsdtah87q6i6WYmmeqTiKGh+O21BpRpu9zO7ibytp2vNKM7K8SOq2KX6ri+mfQIhqE3NLgcBuED98o4Pm6fgQSNqsYxCcjdNr7uNwqtP86GPLSON/C8yltzG1I6zLnGkB3Y5eJYJB3DhquOETfwQi3Jj07XDAbAHuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wWgaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnYAhnBIhhsPPw/0yA4n",
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
  "method": "channels.snapshot_solo_sign",
  "params": {
    "signed_tx": "tx_+QFxCwH4QrhAudHMwLEAruEyWQZEE6+kyhP9Y5y0kna82r5ZN+sVYaRPyKZQ8g5yjNjnGM7qhH/Kzz+FBqe36HjqGZvqC8xhCrkBKPkBJTsBoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX86EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+41PjSCwH4hLhA0TkJ46khkshUkALHbWofO6uoulmJpnqk4ihofjttQaUabvczu4m8radrzSjOyvEjqtil+q4vpn0CIahNzS4HAbhA/fKOD5un4EEjarGMQnI3Ta+7jcKrT/Ohjy0jjfwvMpbcxtSOsy5xpAd2OXiWCQdw4arjhE38EItyY9O1wwGwB7hI+EY5AqEGSeuBVW1d2FfK3ernRI4N9P3ZK6WbrT2zOYuLM7qVF/MFoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2AIZwSIYbDz8PYRtzjg=="
  }
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422942,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422942,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 69999999999999
    },
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
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
    "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
    "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBknrgVVtXdhXyt3q50SODfT92Sulm609szmLizO6lRfzBqBzYVQ5zRyX3wsUd2cglWGoR70sEgspusiJiB87dZIrt727eu8=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainTransfer",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
  "id": -576460752303422941,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAuClI+92f6eZHIry/QHe+thWGjyoKctk+pMfDnZscXSq6VVsjv/By5/7gFswVRtWQ0KxM72ztL7kdHqdNCSWIGuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wagc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cBqgUK"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422941,
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAuClI+92f6eZHIry/QHe+thWGjyoKctk+pMfDnZscXSq6VVsjv/By5/7gFswVRtWQ0KxM72ztL7kdHqdNCSWIGuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wagc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7cBqgUK",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
          "op": "OffChainTransfer",
          "to": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
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
  "id": -576460752303422940,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAuClI+92f6eZHIry/QHe+thWGjyoKctk+pMfDnZscXSq6VVsjv/By5/7gFswVRtWQ0KxM72ztL7kdHqdNCSWIGuECb9Jid5CxDLUALsH66r88rsm28KdjaiFgEjoBO5aqsXSHpyvQc54yNeFP9WouU8uD1IT8roDTjQPhxvI4RD0kHuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wagc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eEDKew"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422940,
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "state": "tx_+NILAfiEuEAuClI+92f6eZHIry/QHe+thWGjyoKctk+pMfDnZscXSq6VVsjv/By5/7gFswVRtWQ0KxM72ztL7kdHqdNCSWIGuECb9Jid5CxDLUALsH66r88rsm28KdjaiFgEjoBO5aqsXSHpyvQc54yNeFP9WouU8uD1IT8roDTjQPhxvI4RD0kHuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wagc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eEDKew"
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "state": "tx_+NILAfiEuEAuClI+92f6eZHIry/QHe+thWGjyoKctk+pMfDnZscXSq6VVsjv/By5/7gFswVRtWQ0KxM72ztL7kdHqdNCSWIGuECb9Jid5CxDLUALsH66r88rsm28KdjaiFgEjoBO5aqsXSHpyvQc54yNeFP9WouU8uD1IT8roDTjQPhxvI4RD0kHuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wagc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eEDKew"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422939,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422939,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 69999999999998
    },
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422938,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422938,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAuClI+92f6eZHIry/QHe+thWGjyoKctk+pMfDnZscXSq6VVsjv/By5/7gFswVRtWQ0KxM72ztL7kdHqdNCSWIGuECb9Jid5CxDLUALsH66r88rsm28KdjaiFgEjoBO5aqsXSHpyvQc54yNeFP9WouU8uD1IT8roDTjQPhxvI4RD0kHuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wagc2FUOc0cl98LFHdnIJVhqEe9LBILKbrIiYgfO3WSK7eEDKew",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/rDvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAKAf7oF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422937,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422937,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "balance": 40000000000002
    },
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 69999999999998
    }
  ],
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
    "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
    "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBknrgVVtXdhXyt3q50SODfT92Sulm609szmLizO6lRfzB6BoRhf9V672F7jNKVoNqDqENf15JcBl/1Vz6PZNXjTCduZRI/8=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
  "id": -576460752303422936,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDidsV4gqXTxqEzLFGK8ypQCsq06ciopSXWm2H6NTrrgyHZFi7t8OJzFmKc0pKmHUDt3WHFW1hVAfBPNLUhvuoIuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wegaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbTfqII"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422936,
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "event": "update"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDidsV4gqXTxqEzLFGK8ypQCsq06ciopSXWm2H6NTrrgyHZFi7t8OJzFmKc0pKmHUDt3WHFW1hVAfBPNLUhvuoIuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wegaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnbTfqII",
      "updates": [
        {
          "amount": 1,
          "from": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
          "op": "OffChainTransfer",
          "to": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
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
  "id": -576460752303422935,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECNXTag9RdIm+7yTrNEQ+k61qUrQ6rbH7a4oLqZR6E/KRGKdr5nC24UFmMvnB/vWprRTl5Wdsyw0QKrD3LVDwYHuEDidsV4gqXTxqEzLFGK8ypQCsq06ciopSXWm2H6NTrrgyHZFi7t8OJzFmKc0pKmHUDt3WHFW1hVAfBPNLUhvuoIuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wegaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaflYUx"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422935,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "state": "tx_+NILAfiEuECNXTag9RdIm+7yTrNEQ+k61qUrQ6rbH7a4oLqZR6E/KRGKdr5nC24UFmMvnB/vWprRTl5Wdsyw0QKrD3LVDwYHuEDidsV4gqXTxqEzLFGK8ypQCsq06ciopSXWm2H6NTrrgyHZFi7t8OJzFmKc0pKmHUDt3WHFW1hVAfBPNLUhvuoIuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wegaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaflYUx"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "state": "tx_+NILAfiEuECNXTag9RdIm+7yTrNEQ+k61qUrQ6rbH7a4oLqZR6E/KRGKdr5nC24UFmMvnB/vWprRTl5Wdsyw0QKrD3LVDwYHuEDidsV4gqXTxqEzLFGK8ypQCsq06ciopSXWm2H6NTrrgyHZFi7t8OJzFmKc0pKmHUDt3WHFW1hVAfBPNLUhvuoIuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wegaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaflYUx"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422934,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422934,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_n5NCzqWFdAzWzFxTGgXVeNBpTqLL8JGf65XSVy1mpHRtLznbu",
      "balance": 40000000000001
    },
    {
      "account": "ak_2TYAjeSxPXcs6y3PBSo8zo947Xb7yPCnpXQZkJxqspcR8JzLu7",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422933,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422933,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECNXTag9RdIm+7yTrNEQ+k61qUrQ6rbH7a4oLqZR6E/KRGKdr5nC24UFmMvnB/vWprRTl5Wdsyw0QKrD3LVDwYHuEDidsV4gqXTxqEzLFGK8ypQCsq06ciopSXWm2H6NTrrgyHZFi7t8OJzFmKc0pKmHUDt3WHFW1hVAfBPNLUhvuoIuEj4RjkCoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX8wegaEYX/Veu9he4zSlaDag6hDX9eSXAZf9Vc+j2TV40wnaflYUx",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaC/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYvKCgEAhj+qJSJf/7DvQAGgZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+LygoBAIYkYTnKgAFHLwz7"
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAudHMwLEAruEyWQZEE6+kyhP9Y5y0kna82r5ZN+sVYaRPyKZQ8g5yjNjnGM7qhH/Kzz+FBqe36HjqGZvqC8xhCrkBKPkBJTsBoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX86EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+41PjSCwH4hLhA0TkJ46khkshUkALHbWofO6uoulmJpnqk4ihofjttQaUabvczu4m8radrzSjOyvEjqtil+q4vpn0CIahNzS4HAbhA/fKOD5un4EEjarGMQnI3Ta+7jcKrT/Ohjy0jjfwvMpbcxtSOsy5xpAd2OXiWCQdw4arjhE38EItyY9O1wwGwB7hI+EY5AqEGSeuBVW1d2FfK3ernRI4N9P3ZK6WbrT2zOYuLM7qVF/MFoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2AIZwSIYbDz8PYRtzjg==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QFxCwH4QrhAudHMwLEAruEyWQZEE6+kyhP9Y5y0kna82r5ZN+sVYaRPyKZQ8g5yjNjnGM7qhH/Kzz+FBqe36HjqGZvqC8xhCrkBKPkBJTsBoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX86EBZllSaZHCK1Otbmp8BQbZwOScRZBcBnzrZiJoLhMp1r+41PjSCwH4hLhA0TkJ46khkshUkALHbWofO6uoulmJpnqk4ihofjttQaUabvczu4m8radrzSjOyvEjqtil+q4vpn0CIahNzS4HAbhA/fKOD5un4EEjarGMQnI3Ta+7jcKrT/Ohjy0jjfwvMpbcxtSOsy5xpAd2OXiWCQdw4arjhE38EItyY9O1wwGwB7hI+EY5AqEGSeuBVW1d2FfK3ernRI4N9P3ZK6WbrT2zOYuLM7qVF/MFoGhGF/1XrvYXuM0pWg2oOoQ1/XklwGX/VXPo9k1eNMJ2AIZwSIYbDz8PYRtzjg==",
      "type": "channel_snapshot_solo_tx"
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "event": "min_depth_achieved",
      "tx_hash": "��Pl���g�a�_��\u0002��6�9��y�\"+y�2���",
      "type": "channel_snapshot_solo_tx"
    }
  },
  "version": 1
}
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBknrgVVtXdhXyt3q50SODfT92Sulm609szmLizO6lRfzoQG/89QgbNgzQFLzFwwS+BTm9UdHWn+kvWVs4hVueIH1FYY2kdavv/+GG0jrV+ABAIYSMJzlQAAprVRRkg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422932,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuED2DfdDVK/Nw0H3nR8CpYx9Ne1d/+6qU5czgslOkaUO47agvcRKpJd8PdVT0X3CXqbI3i91vuJw2/T89P2nLL8HuF/4XTUBoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX86EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7//hhtI61fgAQCGEjCc5UAAKaEQ0YY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422932,
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "event": "shutdown"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "signed_tx": "tx_+KcLAfhCuED2DfdDVK/Nw0H3nR8CpYx9Ne1d/+6qU5czgslOkaUO47agvcRKpJd8PdVT0X3CXqbI3i91vuJw2/T89P2nLL8HuF/4XTUBoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX86EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7//hhtI61fgAQCGEjCc5UAAKaEQ0YY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422931,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuED1dzbs3FkhUXIGvyobdiAi2pyfiGL2dAkHJBgkc8ZjJ525klkti8lybszMbAXiN8l4A4P9+wA0vuDOtkzzyQYGuED2DfdDVK/Nw0H3nR8CpYx9Ne1d/+6qU5czgslOkaUO47agvcRKpJd8PdVT0X3CXqbI3i91vuJw2/T89P2nLL8HuF/4XTUBoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX86EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7//hhtI61fgAQCGEjCc5UAAKVn1t4k="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
  "id": -576460752303422931,
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuED1dzbs3FkhUXIGvyobdiAi2pyfiGL2dAkHJBgkc8ZjJ525klkti8lybszMbAXiN8l4A4P9+wA0vuDOtkzzyQYGuED2DfdDVK/Nw0H3nR8CpYx9Ne1d/+6qU5czgslOkaUO47agvcRKpJd8PdVT0X3CXqbI3i91vuJw2/T89P2nLL8HuF/4XTUBoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX86EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7//hhtI61fgAQCGEjCc5UAAKVn1t4k=",
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuED1dzbs3FkhUXIGvyobdiAi2pyfiGL2dAkHJBgkc8ZjJ525klkti8lybszMbAXiN8l4A4P9+wA0vuDOtkzzyQYGuED2DfdDVK/Nw0H3nR8CpYx9Ne1d/+6qU5czgslOkaUO47agvcRKpJd8PdVT0X3CXqbI3i91vuJw2/T89P2nLL8HuF/4XTUBoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX86EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7//hhtI61fgAQCGEjCc5UAAKVn1t4k=",
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuED1dzbs3FkhUXIGvyobdiAi2pyfiGL2dAkHJBgkc8ZjJ525klkti8lybszMbAXiN8l4A4P9+wA0vuDOtkzzyQYGuED2DfdDVK/Nw0H3nR8CpYx9Ne1d/+6qU5czgslOkaUO47agvcRKpJd8PdVT0X3CXqbI3i91vuJw2/T89P2nLL8HuF/4XTUBoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX86EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7//hhtI61fgAQCGEjCc5UAAKVn1t4k=",
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
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+OkLAfiEuED1dzbs3FkhUXIGvyobdiAi2pyfiGL2dAkHJBgkc8ZjJ525klkti8lybszMbAXiN8l4A4P9+wA0vuDOtkzzyQYGuED2DfdDVK/Nw0H3nR8CpYx9Ne1d/+6qU5czgslOkaUO47agvcRKpJd8PdVT0X3CXqbI3i91vuJw2/T89P2nLL8HuF/4XTUBoQZJ64FVbV3YV8rd6udEjg30/dkrpZutPbM5i4szupUX86EBv/PUIGzYM0BS8xcMEvgU5vVHR1p/pL1lbOIVbniB9RWGNpHWr7//hhtI61fgAQCGEjCc5UAAKVn1t4k=",
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
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
    "channel_id": "ch_ZZBmjrYFrrkqPAzMuKuxqG89ivyoBuVa3NbcXTuhZM532fBSF",
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
