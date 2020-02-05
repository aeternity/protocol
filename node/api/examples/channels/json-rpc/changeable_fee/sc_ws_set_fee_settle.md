
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
      "fsm_id": "ba_J68r2bQGzsuj92zUQ8mAGVO7RMq91MVgK9jSJu+TuR9MUkZS"
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
      "fsm_id": "ba_lwWcHihnwwZub9Y6l1PEI5B3HE9lclHSYAIlWGIGo1wf7Dmi"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+40TlF8Fw==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422901,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEA+94jIrJqXX/FZFAQUKx7Kw2Aeh9VqlGYJDLsTIPj65BCXdwml3FNIrAFLN5hMWW1FZDlcy0IhmC0Hzgv64VkOuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uNFcmocs="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422901,
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
      "signed_tx": "tx_+MsLAfhCuEA+94jIrJqXX/FZFAQUKx7Kw2Aeh9VqlGYJDLsTIPj65BCXdwml3FNIrAFLN5hMWW1FZDlcy0IhmC0Hzgv64VkOuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uNFcmocs=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422900,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAPveIyKyal1/xWRQEFCseysNgHofVapRmCQy7EyD4+uQQl3cJpdxTSKwBSzeYTFltRWQ5XMtCIZgtB84L+uFZDrhAiGoBlF510t4dIO594a43+foq5z5lqvPEAAnEGDgUP05zV5DD5Fr7fpW1X9rz5kTQCcq8rajKGsiV48vyM8v6AriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jRRryOk"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422900,
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
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAPveIyKyal1/xWRQEFCseysNgHofVapRmCQy7EyD4+uQQl3cJpdxTSKwBSzeYTFltRWQ5XMtCIZgtB84L+uFZDrhAiGoBlF510t4dIO594a43+foq5z5lqvPEAAnEGDgUP05zV5DD5Fr7fpW1X9rz5kTQCcq8rajKGsiV48vyM8v6AriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jRRryOk",
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
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAPveIyKyal1/xWRQEFCseysNgHofVapRmCQy7EyD4+uQQl3cJpdxTSKwBSzeYTFltRWQ5XMtCIZgtB84L+uFZDrhAiGoBlF510t4dIO594a43+foq5z5lqvPEAAnEGDgUP05zV5DD5Fr7fpW1X9rz5kTQCcq8rajKGsiV48vyM8v6AriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jRRryOk",
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
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAPveIyKyal1/xWRQEFCseysNgHofVapRmCQy7EyD4+uQQl3cJpdxTSKwBSzeYTFltRWQ5XMtCIZgtB84L+uFZDrhAiGoBlF510t4dIO594a43+foq5z5lqvPEAAnEGDgUP05zV5DD5Fr7fpW1X9rz5kTQCcq8rajKGsiV48vyM8v6AriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jRRryOk",
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
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAPveIyKyal1/xWRQEFCseysNgHofVapRmCQy7EyD4+uQQl3cJpdxTSKwBSzeYTFltRWQ5XMtCIZgtB84L+uFZDrhAiGoBlF510t4dIO594a43+foq5z5lqvPEAAnEGDgUP05zV5DD5Fr7fpW1X9rz5kTQCcq8rajKGsiV48vyM8v6AriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jRRryOk",
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
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
    "data": {
      "message": {
        "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
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
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
    "data": {
      "message": {
        "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
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
  "id": -576460752303422899,
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
  "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
  "id": -576460752303422899,
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
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
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
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
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
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
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
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
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
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
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
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
    "data": {
      "event": "open"
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
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
    "data": {
      "state": "tx_+QENCwH4hLhAPveIyKyal1/xWRQEFCseysNgHofVapRmCQy7EyD4+uQQl3cJpdxTSKwBSzeYTFltRWQ5XMtCIZgtB84L+uFZDrhAiGoBlF510t4dIO594a43+foq5z5lqvPEAAnEGDgUP05zV5DD5Fr7fpW1X9rz5kTQCcq8rajKGsiV48vyM8v6AriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jRRryOk"
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
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
    "data": {
      "state": "tx_+QENCwH4hLhAPveIyKyal1/xWRQEFCseysNgHofVapRmCQy7EyD4+uQQl3cJpdxTSKwBSzeYTFltRWQ5XMtCIZgtB84L+uFZDrhAiGoBlF510t4dIO594a43+foq5z5lqvPEAAnEGDgUP05zV5DD5Fr7fpW1X9rz5kTQCcq8rajKGsiV48vyM8v6AriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jRRryOk"
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
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBjJOT3aSP+bJ+/bu3U38USmfUNyyeGZNGOfsF9weVF/ooQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IC5AUz5AUk8AfkBP/kBPKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvkBGPh0oCbziXyYo8Ox+VZtROqlQQtKKd21jKCiqh29ftJZTs5e+FGAgICAgICAgICAgICg7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqug5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqeAgID4T6DlslFZIexXT120YXqqt3xFqwcxbt0Suq1WIBNf47yap+2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAH4T6Dt/5Hiy5W70qsqTzdexfFGw0mN5gAjP38MM0HGdpS2q+2gNbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX//AwMDAwACGFT7sgIAANfC01qc=",
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
    "signed_tx": "tx_+QHrCwH4QrhAdAlN3gpOGfrJi6gnznudgwmA3N302H9/f+9i2ukdUPVLzUoJZvcEMBMZIqgyx0/B3IfnA84eo/tjF3Bb0wfjA7kBovkBnzYBoQYyTk92kj/myfv27t1N/FEpn1DcsnhmTRjn7BfcHlRf6KEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SAuQFM+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMAAhhU+7ICAADWY84Hy"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAdAlN3gpOGfrJi6gnznudgwmA3N302H9/f+9i2ukdUPVLzUoJZvcEMBMZIqgyx0/B3IfnA84eo/tjF3Bb0wfjA7kBovkBnzYBoQYyTk92kj/myfv27t1N/FEpn1DcsnhmTRjn7BfcHlRf6KEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SAuQFM+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMAAhhU+7ICAADWY84Hy",
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
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
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
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAdAlN3gpOGfrJi6gnznudgwmA3N302H9/f+9i2ukdUPVLzUoJZvcEMBMZIqgyx0/B3IfnA84eo/tjF3Bb0wfjA7kBovkBnzYBoQYyTk92kj/myfv27t1N/FEpn1DcsnhmTRjn7BfcHlRf6KEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SAuQFM+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMAAhhU+7ICAADWY84Hy",
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
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
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
  "params": {
    "fee": 123456789876543
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBjJOT3aSP+bJ+/bu3U38USmfUNyyeGZNGOfsF9weVF/ooQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIY/qiUiX/+GJGE5yoABAIZwSIYbDz8W0+pngw==",
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
    "signed_tx": "tx_+KcLAfhCuEBShEajLGX/qmWX6FDHwr8Ye4lskdXUNNFop9Ie4lXqvfXWNLAlFI+g7p01X9r9EMq2DsHVKpKdVkmO4uBzcZAGuF/4XTgBoQYyTk92kj/myfv27t1N/FEpn1DcsnhmTRjn7BfcHlRf6KEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl//hiRhOcqAAQCGcEiGGw8/Fg5TeYk="
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBShEajLGX/qmWX6FDHwr8Ye4lskdXUNNFop9Ie4lXqvfXWNLAlFI+g7p01X9r9EMq2DsHVKpKdVkmO4uBzcZAGuF/4XTgBoQYyTk92kj/myfv27t1N/FEpn1DcsnhmTRjn7BfcHlRf6KEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl//hiRhOcqAAQCGcEiGGw8/Fg5TeYk=",
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
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEBShEajLGX/qmWX6FDHwr8Ye4lskdXUNNFop9Ie4lXqvfXWNLAlFI+g7p01X9r9EMq2DsHVKpKdVkmO4uBzcZAGuF/4XTgBoQYyTk92kj/myfv27t1N/FEpn1DcsnhmTRjn7BfcHlRf6KEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGP6olIl//hiRhOcqAAQCGcEiGGw8/Fg5TeYk=",
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
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
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
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
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
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
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
    "channel_id": "ch_P9zotmXWTYAfTCW7WQFVQbpUAxbveyQMs2zVABH77MYLTnfEx",
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
      "fsm_id": "ba_/jp/7euSI0NiiEgeSmzGgKtoJ32UbspheeBanBOy9b7+9kQM"
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
      "fsm_id": "ba_AsGE1lAnO9N+bzVVzLFrxVa3A2c5JcGT1bL++K08/5z55wwg"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+42VLBVWQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422898,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEDYrTKSnfc25Iv+WbrU2Jc0Y0zv7I6O8Ifde2ZlnvgLcaoEpLLL7dy0IqDhuvVD6QhUfLyokUzSpfmy1Wgk4yAMuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uNjUK6LY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422898,
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
      "signed_tx": "tx_+MsLAfhCuEDYrTKSnfc25Iv+WbrU2Jc0Y0zv7I6O8Ifde2ZlnvgLcaoEpLLL7dy0IqDhuvVD6QhUfLyokUzSpfmy1Wgk4yAMuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uNjUK6LY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422897,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAdEiA/o8n4Qnk5pdockLP58JhQahW6tw61nhdNmMZK3llzUtJ9RoDTySDLN5LlXemvv1CZBQf/u8lb58DbeRhBbhA2K0ykp33NuSL/lm61NiXNGNM7+yOjvCH3XtmZZ74C3GqBKSyy+3ctCKg4br1Q+kIVHy8qJFM0qX5stVoJOMgDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jaE2Kxd"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422897,
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
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAdEiA/o8n4Qnk5pdockLP58JhQahW6tw61nhdNmMZK3llzUtJ9RoDTySDLN5LlXemvv1CZBQf/u8lb58DbeRhBbhA2K0ykp33NuSL/lm61NiXNGNM7+yOjvCH3XtmZZ74C3GqBKSyy+3ctCKg4br1Q+kIVHy8qJFM0qX5stVoJOMgDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jaE2Kxd",
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
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAdEiA/o8n4Qnk5pdockLP58JhQahW6tw61nhdNmMZK3llzUtJ9RoDTySDLN5LlXemvv1CZBQf/u8lb58DbeRhBbhA2K0ykp33NuSL/lm61NiXNGNM7+yOjvCH3XtmZZ74C3GqBKSyy+3ctCKg4br1Q+kIVHy8qJFM0qX5stVoJOMgDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jaE2Kxd",
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
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAdEiA/o8n4Qnk5pdockLP58JhQahW6tw61nhdNmMZK3llzUtJ9RoDTySDLN5LlXemvv1CZBQf/u8lb58DbeRhBbhA2K0ykp33NuSL/lm61NiXNGNM7+yOjvCH3XtmZZ74C3GqBKSyy+3ctCKg4br1Q+kIVHy8qJFM0qX5stVoJOMgDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jaE2Kxd",
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
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAdEiA/o8n4Qnk5pdockLP58JhQahW6tw61nhdNmMZK3llzUtJ9RoDTySDLN5LlXemvv1CZBQf/u8lb58DbeRhBbhA2K0ykp33NuSL/lm61NiXNGNM7+yOjvCH3XtmZZ74C3GqBKSyy+3ctCKg4br1Q+kIVHy8qJFM0qX5stVoJOMgDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jaE2Kxd",
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
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
    "data": {
      "message": {
        "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
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
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
    "data": {
      "message": {
        "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
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
  "id": -576460752303422896,
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
  "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
  "id": -576460752303422896,
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
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
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
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
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
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
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
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
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
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
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
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
    "data": {
      "state": "tx_+QENCwH4hLhAdEiA/o8n4Qnk5pdockLP58JhQahW6tw61nhdNmMZK3llzUtJ9RoDTySDLN5LlXemvv1CZBQf/u8lb58DbeRhBbhA2K0ykp33NuSL/lm61NiXNGNM7+yOjvCH3XtmZZ74C3GqBKSyy+3ctCKg4br1Q+kIVHy8qJFM0qX5stVoJOMgDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jaE2Kxd"
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
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
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
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
    "data": {
      "state": "tx_+QENCwH4hLhAdEiA/o8n4Qnk5pdockLP58JhQahW6tw61nhdNmMZK3llzUtJ9RoDTySDLN5LlXemvv1CZBQf/u8lb58DbeRhBbhA2K0ykp33NuSL/lm61NiXNGNM7+yOjvCH3XtmZZ74C3GqBKSyy+3ctCKg4br1Q+kIVHy8qJFM0qX5stVoJOMgDLiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jaE2Kxd"
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
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
    "data": {
      "signed_tx": "tx_+QGoCwHAuQGi+QGfNgGhBjau5vj0W2IFNtOb73FfNCt9wOhr9gXdOH7ta8zN3bgLoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IC5AUz5AUk8AfkBP/kBPKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvkBGPh0oCbziXyYo8Ox+VZtROqlQQtKKd21jKCiqh29ftJZTs5e+FGAgICAgICAgICAgICg7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqug5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqeAgID4T6DlslFZIexXT120YXqqt3xFqwcxbt0Suq1WIBNf47yap+2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAH4T6Dt/5Hiy5W70qsqTzdexfFGw0mN5gAjP38MM0HGdpS2q+2gNbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX//AwMDAwACGFT7sgIAANzNXxJw=",
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
    "signed_tx": "tx_+QHrCwH4QrhAKNbvbTMNLA+Gthrz4hK2NErRhNI9/hXOK95FGGTic3m9eS94XRMlO3RDzAwdHnobdmNvtPOnrm8fVcWBATvkAbkBovkBnzYBoQY2rub49FtiBTbTm+9xXzQrfcDoa/YF3Th+7WvMzd24C6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SAuQFM+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMAAhhU+7ICAADfoYc8y"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAKNbvbTMNLA+Gthrz4hK2NErRhNI9/hXOK95FGGTic3m9eS94XRMlO3RDzAwdHnobdmNvtPOnrm8fVcWBATvkAbkBovkBnzYBoQY2rub49FtiBTbTm+9xXzQrfcDoa/YF3Th+7WvMzd24C6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SAuQFM+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMAAhhU+7ICAADfoYc8y",
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
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
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
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
    "data": {
      "info": "solo_closing",
      "tx": "tx_+QHrCwH4QrhAKNbvbTMNLA+Gthrz4hK2NErRhNI9/hXOK95FGGTic3m9eS94XRMlO3RDzAwdHnobdmNvtPOnrm8fVcWBATvkAbkBovkBnzYBoQY2rub49FtiBTbTm+9xXzQrfcDoa/YF3Th+7WvMzd24C6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SAuQFM+QFJPAH5AT/5ATygJvOJfJijw7H5Vm1E6qVBC0op3bWMoKKqHb1+0llOzl75ARj4dKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvhRgICAgICAgICAgICAoO3/keLLlbvSqypPN17F8UbDSY3mACM/fwwzQcZ2lLaroOWyUVkh7FdPXbRheqq3fEWrBzFu3RK6rVYgE1/jvJqngICA+E+g5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqftoDE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4Qi8oKAQCGJGE5yoAB+E+g7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqvtoDW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0i8oKAQCGP6olIl//wMDAwMAAhhU+7ICAADfoYc8y",
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
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
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
  "params": {
    "fee": 123456789876543
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdOAGhBjau5vj0W2IFNtOb73FfNCt9wOhr9gXdOH7ta8zN3bgLoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiX/+GJGE5yoABAIZwSIYbDz84pVMViQ==",
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
    "signed_tx": "tx_+KcLAfhCuEA3FO5Myuw05KCY0jg8EyuwrrhU46VL8yu4T7R07rxoTy4+rj99PNN6a9E9dPSDXAMB6lqbB12Wn1AFm+5M97kPuF/4XTgBoQY2rub49FtiBTbTm+9xXzQrfcDoa/YF3Th+7WvMzd24C6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olIl//hiRhOcqAAQCGcEiGGw8/OCVSvG0="
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEA3FO5Myuw05KCY0jg8EyuwrrhU46VL8yu4T7R07rxoTy4+rj99PNN6a9E9dPSDXAMB6lqbB12Wn1AFm+5M97kPuF/4XTgBoQY2rub49FtiBTbTm+9xXzQrfcDoa/YF3Th+7WvMzd24C6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olIl//hiRhOcqAAQCGcEiGGw8/OCVSvG0=",
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
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
    "data": {
      "info": "channel_closed",
      "tx": "tx_+KcLAfhCuEA3FO5Myuw05KCY0jg8EyuwrrhU46VL8yu4T7R07rxoTy4+rj99PNN6a9E9dPSDXAMB6lqbB12Wn1AFm+5M97kPuF/4XTgBoQY2rub49FtiBTbTm+9xXzQrfcDoa/YF3Th+7WvMzd24C6EBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olIl//hiRhOcqAAQCGcEiGGw8/OCVSvG0=",
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
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
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
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
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
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
    "data": {
      "event": "closed_confirmed"
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
    "channel_id": "ch_R5owLEVmQnjTZ5xKks3A4EzqeE2U8bEFjf8gmMPTNsAKZVfNX",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder closes WebSocket connection
