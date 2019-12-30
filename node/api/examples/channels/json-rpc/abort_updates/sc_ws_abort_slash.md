
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
      "fsm_id": "ba_lg97ImuDaltKaHgzp7KEog31jO3jUlsNMJxpf13eczWWgyP1"
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
      "fsm_id": "ba_g6MVS2vtPof66y0WJc4EKVnyeZbIKlNKC82keaBRdFNQ2TdG"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4+h5nRJQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422856,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECLDd1+JlPcvV2pHd8FJsm1CSyXcxUKWYMMlQqeXLFgCy52c0KpA6qa8e3PiZPJZ+BmRHSmQWvZBR7mUwalomINuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uPilseTI="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422856,
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
      "signed_tx": "tx_+MsLAfhCuECLDd1+JlPcvV2pHd8FJsm1CSyXcxUKWYMMlQqeXLFgCy52c0KpA6qa8e3PiZPJZ+BmRHSmQWvZBR7mUwalomINuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uPilseTI=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422855,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAiw3dfiZT3L1dqR3fBSbJtQksl3MVClmDDJUKnlyxYAsudnNCqQOqmvHtz4mTyWfgZkR0pkFr2QUe5lMGpaJiDbhAjMwDF3cz1RDkdrstZOCMGZ5aWcuA/AyHg9jvZwxfV9HsgSIc0M2aAF1Md3hQW2/RiKE7cLBhB8/B6ESTiV3GA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7j4En1UE"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422855,
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAiw3dfiZT3L1dqR3fBSbJtQksl3MVClmDDJUKnlyxYAsudnNCqQOqmvHtz4mTyWfgZkR0pkFr2QUe5lMGpaJiDbhAjMwDF3cz1RDkdrstZOCMGZ5aWcuA/AyHg9jvZwxfV9HsgSIc0M2aAF1Md3hQW2/RiKE7cLBhB8/B6ESTiV3GA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7j4En1UE",
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAiw3dfiZT3L1dqR3fBSbJtQksl3MVClmDDJUKnlyxYAsudnNCqQOqmvHtz4mTyWfgZkR0pkFr2QUe5lMGpaJiDbhAjMwDF3cz1RDkdrstZOCMGZ5aWcuA/AyHg9jvZwxfV9HsgSIc0M2aAF1Md3hQW2/RiKE7cLBhB8/B6ESTiV3GA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7j4En1UE",
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAiw3dfiZT3L1dqR3fBSbJtQksl3MVClmDDJUKnlyxYAsudnNCqQOqmvHtz4mTyWfgZkR0pkFr2QUe5lMGpaJiDbhAjMwDF3cz1RDkdrstZOCMGZ5aWcuA/AyHg9jvZwxfV9HsgSIc0M2aAF1Md3hQW2/RiKE7cLBhB8/B6ESTiV3GA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7j4En1UE",
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAiw3dfiZT3L1dqR3fBSbJtQksl3MVClmDDJUKnlyxYAsudnNCqQOqmvHtz4mTyWfgZkR0pkFr2QUe5lMGpaJiDbhAjMwDF3cz1RDkdrstZOCMGZ5aWcuA/AyHg9jvZwxfV9HsgSIc0M2aAF1Md3hQW2/RiKE7cLBhB8/B6ESTiV3GA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7j4En1UE",
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "message": {
        "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "message": {
        "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
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
  "id": -576460752303422854,
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
  "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
  "id": -576460752303422854,
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
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

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "state": "tx_+QENCwH4hLhAiw3dfiZT3L1dqR3fBSbJtQksl3MVClmDDJUKnlyxYAsudnNCqQOqmvHtz4mTyWfgZkR0pkFr2QUe5lMGpaJiDbhAjMwDF3cz1RDkdrstZOCMGZ5aWcuA/AyHg9jvZwxfV9HsgSIc0M2aAF1Md3hQW2/RiKE7cLBhB8/B6ESTiV3GA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7j4En1UE"
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "state": "tx_+QENCwH4hLhAiw3dfiZT3L1dqR3fBSbJtQksl3MVClmDDJUKnlyxYAsudnNCqQOqmvHtz4mTyWfgZkR0pkFr2QUe5lMGpaJiDbhAjMwDF3cz1RDkdrstZOCMGZ5aWcuA/AyHg9jvZwxfV9HsgSIc0M2aAF1Md3hQW2/RiKE7cLBhB8/B6ESTiV3GA7iD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7j4En1UE"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422853,
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
  "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
  "id": -576460752303422853,
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtxXP1jpiDE5kSzNI2g1WEmm/7G8j6raFWCeZt7rg/rjAqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8BynvNRY=",
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
  "id": -576460752303422852,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAtG257gpJLKBYy1iNsWlwkDPZ+O4I3JEibgOBTynRdh6G7lTMuP7o+noDXbvNUVu+hxlub+4G/4Tg44U86Dr8FuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcRnhqq"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
  "id": -576460752303422852,
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAtG257gpJLKBYy1iNsWlwkDPZ+O4I3JEibgOBTynRdh6G7lTMuP7o+noDXbvNUVu+hxlub+4G/4Tg44U86Dr8FuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcRnhqq",
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
  "id": -576460752303422851,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAtG257gpJLKBYy1iNsWlwkDPZ+O4I3JEibgOBTynRdh6G7lTMuP7o+noDXbvNUVu+hxlub+4G/4Tg44U86Dr8FuEDmR1xBP5Y3H8ter52T9aUgHVeL6kC9uFiKJg1LXKCwf1tMqDGJzw3q7uFOco3tQSvnQQHv56eg/zw1iF+0N5QCuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAe9BtJ+"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
  "id": -576460752303422851,
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "state": "tx_+NILAfiEuEAtG257gpJLKBYy1iNsWlwkDPZ+O4I3JEibgOBTynRdh6G7lTMuP7o+noDXbvNUVu+hxlub+4G/4Tg44U86Dr8FuEDmR1xBP5Y3H8ter52T9aUgHVeL6kC9uFiKJg1LXKCwf1tMqDGJzw3q7uFOco3tQSvnQQHv56eg/zw1iF+0N5QCuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAe9BtJ+"
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "state": "tx_+NILAfiEuEAtG257gpJLKBYy1iNsWlwkDPZ+O4I3JEibgOBTynRdh6G7lTMuP7o+noDXbvNUVu+hxlub+4G/4Tg44U86Dr8FuEDmR1xBP5Y3H8ter52T9aUgHVeL6kC9uFiKJg1LXKCwf1tMqDGJzw3q7uFOco3tQSvnQQHv56eg/zw1iF+0N5QCuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAe9BtJ+"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422850,
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
  "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
  "id": -576460752303422850,
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
  "id": -576460752303422849,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
  "id": -576460752303422849,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAtG257gpJLKBYy1iNsWlwkDPZ+O4I3JEibgOBTynRdh6G7lTMuP7o+noDXbvNUVu+hxlub+4G/4Tg44U86Dr8FuEDmR1xBP5Y3H8ter52T9aUgHVeL6kC9uFiKJg1LXKCwf1tMqDGJzw3q7uFOco3tQSvnQQHv56eg/zw1iF+0N5QCuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAe9BtJ+",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422848,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
  "id": -576460752303422848,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000002
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
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
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtxXP1jpiDE5kSzNI2g1WEmm/7G8j6raFWCeZt7rg/rjA6AWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7rWWsus=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "id": -576460752303422847,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECU+OTTvnuSui49ofkXVoANVhp3XTdwOwXq+1i8A+WdoG2XpH3ddlfjpW4PDHdhRTJTGv2GdlyU/FPOBng4kTUIuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7OoX1T"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
  "id": -576460752303422847,
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "signed_tx": "tx_+JALAfhCuECU+OTTvnuSui49ofkXVoANVhp3XTdwOwXq+1i8A+WdoG2XpH3ddlfjpW4PDHdhRTJTGv2GdlyU/FPOBng4kTUIuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7OoX1T",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "id": -576460752303422846,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECU+OTTvnuSui49ofkXVoANVhp3XTdwOwXq+1i8A+WdoG2XpH3ddlfjpW4PDHdhRTJTGv2GdlyU/FPOBng4kTUIuEDdnpsFtOUfoj5PQEt3B57GMJNPOHxTXT7yNawwZlQxI9PSS6Kn8xMNsx71+aSfrvnKUZq0DjvHa7lCnAS6+REGuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7/LoIK"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
  "id": -576460752303422846,
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "state": "tx_+NILAfiEuECU+OTTvnuSui49ofkXVoANVhp3XTdwOwXq+1i8A+WdoG2XpH3ddlfjpW4PDHdhRTJTGv2GdlyU/FPOBng4kTUIuEDdnpsFtOUfoj5PQEt3B57GMJNPOHxTXT7yNawwZlQxI9PSS6Kn8xMNsx71+aSfrvnKUZq0DjvHa7lCnAS6+REGuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7/LoIK"
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "state": "tx_+NILAfiEuECU+OTTvnuSui49ofkXVoANVhp3XTdwOwXq+1i8A+WdoG2XpH3ddlfjpW4PDHdhRTJTGv2GdlyU/FPOBng4kTUIuEDdnpsFtOUfoj5PQEt3B57GMJNPOHxTXT7yNawwZlQxI9PSS6Kn8xMNsx71+aSfrvnKUZq0DjvHa7lCnAS6+REGuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7/LoIK"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422845,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
  "id": -576460752303422845,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000001
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422844,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
  "id": -576460752303422844,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECU+OTTvnuSui49ofkXVoANVhp3XTdwOwXq+1i8A+WdoG2XpH3ddlfjpW4PDHdhRTJTGv2GdlyU/FPOBng4kTUIuEDdnpsFtOUfoj5PQEt3B57GMJNPOHxTXT7yNawwZlQxI9PSS6Kn8xMNsx71+aSfrvnKUZq0DjvHa7lCnAS6+REGuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7/LoIK",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422843,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
  "id": -576460752303422843,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECU+OTTvnuSui49ofkXVoANVhp3XTdwOwXq+1i8A+WdoG2XpH3ddlfjpW4PDHdhRTJTGv2GdlyU/FPOBng4kTUIuEDdnpsFtOUfoj5PQEt3B57GMJNPOHxTXT7yNawwZlQxI9PSS6Kn8xMNsx71+aSfrvnKUZq0DjvHa7lCnAS6+REGuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7/LoIK",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422842,
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
  "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
  "id": -576460752303422842,
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtxXP1jpiDE5kSzNI2g1WEmm/7G8j6raFWCeZt7rg/rjBKAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8BzP941o=",
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
  "id": -576460752303422841,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBWSMJix59O4iOQck3yMIRmSZA2GZC6f4PVRsJp4p1/gY3ZllSm76l2f6rr8mMntq+5rvMDp7PJdvu4gjUKdP4LuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeShR8Z"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
  "id": -576460752303422841,
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBWSMJix59O4iOQck3yMIRmSZA2GZC6f4PVRsJp4p1/gY3ZllSm76l2f6rr8mMntq+5rvMDp7PJdvu4gjUKdP4LuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeShR8Z",
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
  "id": -576460752303422840,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBWSMJix59O4iOQck3yMIRmSZA2GZC6f4PVRsJp4p1/gY3ZllSm76l2f6rr8mMntq+5rvMDp7PJdvu4gjUKdP4LuECNVFHs9wrWtL40Vde4E3fO6rIQfhGIUHZkUBhrKDIf01tS7gmgx+NqF7/OPSilGI70/6ayF324EM9I9Gj6+74GuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcZtQAi"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
  "id": -576460752303422840,
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "state": "tx_+NILAfiEuEBWSMJix59O4iOQck3yMIRmSZA2GZC6f4PVRsJp4p1/gY3ZllSm76l2f6rr8mMntq+5rvMDp7PJdvu4gjUKdP4LuECNVFHs9wrWtL40Vde4E3fO6rIQfhGIUHZkUBhrKDIf01tS7gmgx+NqF7/OPSilGI70/6ayF324EM9I9Gj6+74GuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcZtQAi"
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "state": "tx_+NILAfiEuEBWSMJix59O4iOQck3yMIRmSZA2GZC6f4PVRsJp4p1/gY3ZllSm76l2f6rr8mMntq+5rvMDp7PJdvu4gjUKdP4LuECNVFHs9wrWtL40Vde4E3fO6rIQfhGIUHZkUBhrKDIf01tS7gmgx+NqF7/OPSilGI70/6ayF324EM9I9Gj6+74GuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcZtQAi"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422839,
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
  "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
  "id": -576460752303422839,
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
  "id": -576460752303422838,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
  "id": -576460752303422838,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBWSMJix59O4iOQck3yMIRmSZA2GZC6f4PVRsJp4p1/gY3ZllSm76l2f6rr8mMntq+5rvMDp7PJdvu4gjUKdP4LuECNVFHs9wrWtL40Vde4E3fO6rIQfhGIUHZkUBhrKDIf01tS7gmgx+NqF7/OPSilGI70/6ayF324EM9I9Gj6+74GuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcZtQAi",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422837,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
  "id": -576460752303422837,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000002
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
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
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBtxXP1jpiDE5kSzNI2g1WEmm/7G8j6raFWCeZt7rg/rjBaAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7okHHe8=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "id": -576460752303422836,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBP/AyqhiDZJR/1FHC7/XzdrgE9jyVgyQd08AfHmc7z2TINzm4h8jlQBtmUVijc/Y2yeBPfs42kCRR/TuMX+8wNuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5Rbyj/"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
  "id": -576460752303422836,
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBP/AyqhiDZJR/1FHC7/XzdrgE9jyVgyQd08AfHmc7z2TINzm4h8jlQBtmUVijc/Y2yeBPfs42kCRR/TuMX+8wNuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5Rbyj/",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "id": -576460752303422835,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEALS1j9wreZbJsyztl2ciGEmZx5I8OpNo0ROWV8ItOfbA4cYzaZtfu0P2GeBh7K+AzJXBNcSQVorNfhtokBCi8IuEBP/AyqhiDZJR/1FHC7/XzdrgE9jyVgyQd08AfHmc7z2TINzm4h8jlQBtmUVijc/Y2yeBPfs42kCRR/TuMX+8wNuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4/jZJZ"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
  "id": -576460752303422835,
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "state": "tx_+NILAfiEuEALS1j9wreZbJsyztl2ciGEmZx5I8OpNo0ROWV8ItOfbA4cYzaZtfu0P2GeBh7K+AzJXBNcSQVorNfhtokBCi8IuEBP/AyqhiDZJR/1FHC7/XzdrgE9jyVgyQd08AfHmc7z2TINzm4h8jlQBtmUVijc/Y2yeBPfs42kCRR/TuMX+8wNuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4/jZJZ"
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "state": "tx_+NILAfiEuEALS1j9wreZbJsyztl2ciGEmZx5I8OpNo0ROWV8ItOfbA4cYzaZtfu0P2GeBh7K+AzJXBNcSQVorNfhtokBCi8IuEBP/AyqhiDZJR/1FHC7/XzdrgE9jyVgyQd08AfHmc7z2TINzm4h8jlQBtmUVijc/Y2yeBPfs42kCRR/TuMX+8wNuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4/jZJZ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422834,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
  "id": -576460752303422834,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000001
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422833,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
  "id": -576460752303422833,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEALS1j9wreZbJsyztl2ciGEmZx5I8OpNo0ROWV8ItOfbA4cYzaZtfu0P2GeBh7K+AzJXBNcSQVorNfhtokBCi8IuEBP/AyqhiDZJR/1FHC7/XzdrgE9jyVgyQd08AfHmc7z2TINzm4h8jlQBtmUVijc/Y2yeBPfs42kCRR/TuMX+8wNuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4/jZJZ",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEALS1j9wreZbJsyztl2ciGEmZx5I8OpNo0ROWV8ItOfbA4cYzaZtfu0P2GeBh7K+AzJXBNcSQVorNfhtokBCi8IuEBP/AyqhiDZJR/1FHC7/XzdrgE9jyVgyQd08AfHmc7z2TINzm4h8jlQBtmUVijc/Y2yeBPfs42kCRR/TuMX+8wNuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4/jZJZ",
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
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
  "method": "channels.slash",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEALS1j9wreZbJsyztl2ciGEmZx5I8OpNo0ROWV8ItOfbA4cYzaZtfu0P2GeBh7K+AzJXBNcSQVorNfhtokBCi8IuEBP/AyqhiDZJR/1FHC7/XzdrgE9jyVgyQd08AfHmc7z2TINzm4h8jlQBtmUVijc/Y2yeBPfs42kCRR/TuMX+8wNuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4/jZJZ",
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
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
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBtxXP1jpiDE5kSzNI2g1WEmm/7G8j6raFWCeZt7rg/rjoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79LjU+NILAfiEuEALS1j9wreZbJsyztl2ciGEmZx5I8OpNo0ROWV8ItOfbA4cYzaZtfu0P2GeBh7K+AzJXBNcSQVorNfhtokBCi8IuEBP/AyqhiDZJR/1FHC7/XzdrgE9jyVgyQd08AfHmc7z2TINzm4h8jlQBtmUVijc/Y2yeBPfs42kCRR/TuMX+8wNuEj4RjkCoQbcVz9Y6YgxOZEszSNoNVhJpv+xvI+q2hVgnmbe64P64wWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+65AUz5AUk8AfkBP/kBPKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvkBGPh0oCbziXyYo8Ox+VZtROqlQQtKKd21jKCiqh29ftJZTs5e+FGAgICAgICAgICAgICg7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqug5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqeAgID4T6DlslFZIexXT120YXqqt3xFqwcxbt0Suq1WIBNf47yap+2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAH4T6Dt/5Hiy5W70qsqTzdexfFGw0mN5gAjP38MM0HGdpS2q+2gNbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX//AwMDAwACGGR7ISegAQCY+IbE=",
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "event": "aborted_update"
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422832,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### initiator info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
  "id": -576460752303422832,
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
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422831,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### responder closes WebSocket connection

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2g3JzkkvTbM1YfLGcLXBaC4CLqftbUqfgpTib5vqoM6b552G18",
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
      "fsm_id": "ba_vHGrp/r3Iv6az+uiqyHgPsPpSmyLBe8YTL7O81mzBbnhEpaw"
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
      "fsm_id": "ba_oHkHJheIY84QA1JvHya16oKgimNXij7UImLff7Yg6kPYOrZA"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5A+cn0hg==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422830,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuECWNwgwbUJ0v2i6fSjP7GmaN+aJdz4tq/sAV0uR2gKh4ogjMjExPIqkm22r4o3PdMuK9S6QfHMzomDlV+C0rRgPuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uQJJrHZc="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422830,
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
      "signed_tx": "tx_+MsLAfhCuECWNwgwbUJ0v2i6fSjP7GmaN+aJdz4tq/sAV0uR2gKh4ogjMjExPIqkm22r4o3PdMuK9S6QfHMzomDlV+C0rRgPuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uQJJrHZc=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422829,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAljcIMG1CdL9oun0oz+xpmjfmiXc+Lav7AFdLkdoCoeKIIzIxMTyKpJttq+KNz3TLivUukHxzM6Jg5VfgtK0YD7hAqDoEHTWLF6fiMZ7RF+s066h67IPKavUchSQkD+X29LCUc8qnutYywZJL8bwaaTCSSW6pVEikulL4hvCzqYm/DriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kCSZpXq"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422829,
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAljcIMG1CdL9oun0oz+xpmjfmiXc+Lav7AFdLkdoCoeKIIzIxMTyKpJttq+KNz3TLivUukHxzM6Jg5VfgtK0YD7hAqDoEHTWLF6fiMZ7RF+s066h67IPKavUchSQkD+X29LCUc8qnutYywZJL8bwaaTCSSW6pVEikulL4hvCzqYm/DriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kCSZpXq",
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAljcIMG1CdL9oun0oz+xpmjfmiXc+Lav7AFdLkdoCoeKIIzIxMTyKpJttq+KNz3TLivUukHxzM6Jg5VfgtK0YD7hAqDoEHTWLF6fiMZ7RF+s066h67IPKavUchSQkD+X29LCUc8qnutYywZJL8bwaaTCSSW6pVEikulL4hvCzqYm/DriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kCSZpXq",
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAljcIMG1CdL9oun0oz+xpmjfmiXc+Lav7AFdLkdoCoeKIIzIxMTyKpJttq+KNz3TLivUukHxzM6Jg5VfgtK0YD7hAqDoEHTWLF6fiMZ7RF+s066h67IPKavUchSQkD+X29LCUc8qnutYywZJL8bwaaTCSSW6pVEikulL4hvCzqYm/DriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kCSZpXq",
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAljcIMG1CdL9oun0oz+xpmjfmiXc+Lav7AFdLkdoCoeKIIzIxMTyKpJttq+KNz3TLivUukHxzM6Jg5VfgtK0YD7hAqDoEHTWLF6fiMZ7RF+s066h67IPKavUchSQkD+X29LCUc8qnutYywZJL8bwaaTCSSW6pVEikulL4hvCzqYm/DriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kCSZpXq",
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "message": {
        "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "message": {
        "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
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
  "id": -576460752303422828,
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
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422828,
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "state": "tx_+QENCwH4hLhAljcIMG1CdL9oun0oz+xpmjfmiXc+Lav7AFdLkdoCoeKIIzIxMTyKpJttq+KNz3TLivUukHxzM6Jg5VfgtK0YD7hAqDoEHTWLF6fiMZ7RF+s066h67IPKavUchSQkD+X29LCUc8qnutYywZJL8bwaaTCSSW6pVEikulL4hvCzqYm/DriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kCSZpXq"
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "state": "tx_+QENCwH4hLhAljcIMG1CdL9oun0oz+xpmjfmiXc+Lav7AFdLkdoCoeKIIzIxMTyKpJttq+KNz3TLivUukHxzM6Jg5VfgtK0YD7hAqDoEHTWLF6fiMZ7RF+s066h67IPKavUchSQkD+X29LCUc8qnutYywZJL8bwaaTCSSW6pVEikulL4hvCzqYm/DriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kCSZpXq"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422827,
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
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422827,
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjvWGI9TrM2qmijrjltRcHtyOv2eC27qg2rhJiv6XToXAqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B5o6kE8=",
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
  "id": -576460752303422826,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDSvnNmfBdQrdOdg8ciccr9Wo0rNE/Fsm9KSmganjy9LbAXOf2jukty7QlYzKfIvtO1g64UPInMPedppjCvcvIHuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcyWNKR"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422826,
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDSvnNmfBdQrdOdg8ciccr9Wo0rNE/Fsm9KSmganjy9LbAXOf2jukty7QlYzKfIvtO1g64UPInMPedppjCvcvIHuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcyWNKR",
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
  "id": -576460752303422825,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECM6CngDYb1I8bNk3SH0m+qCbuHsW8WbD4CU24JfmRnVEQS29ZaOOaSxMx1weue2ZqRxj4Sru9L9DkVeY+RmfwLuEDSvnNmfBdQrdOdg8ciccr9Wo0rNE/Fsm9KSmganjy9LbAXOf2jukty7QlYzKfIvtO1g64UPInMPedppjCvcvIHuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAen1SrZ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422825,
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "state": "tx_+NILAfiEuECM6CngDYb1I8bNk3SH0m+qCbuHsW8WbD4CU24JfmRnVEQS29ZaOOaSxMx1weue2ZqRxj4Sru9L9DkVeY+RmfwLuEDSvnNmfBdQrdOdg8ciccr9Wo0rNE/Fsm9KSmganjy9LbAXOf2jukty7QlYzKfIvtO1g64UPInMPedppjCvcvIHuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAen1SrZ"
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "state": "tx_+NILAfiEuECM6CngDYb1I8bNk3SH0m+qCbuHsW8WbD4CU24JfmRnVEQS29ZaOOaSxMx1weue2ZqRxj4Sru9L9DkVeY+RmfwLuEDSvnNmfBdQrdOdg8ciccr9Wo0rNE/Fsm9KSmganjy9LbAXOf2jukty7QlYzKfIvtO1g64UPInMPedppjCvcvIHuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAen1SrZ"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422824,
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
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422824,
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
  "id": -576460752303422823,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422823,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECM6CngDYb1I8bNk3SH0m+qCbuHsW8WbD4CU24JfmRnVEQS29ZaOOaSxMx1weue2ZqRxj4Sru9L9DkVeY+RmfwLuEDSvnNmfBdQrdOdg8ciccr9Wo0rNE/Fsm9KSmganjy9LbAXOf2jukty7QlYzKfIvtO1g64UPInMPedppjCvcvIHuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAen1SrZ",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422822,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422822,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000002
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
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
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjvWGI9TrM2qmijrjltRcHtyOv2eC27qg2rhJiv6XToXA6AWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7nWMEMg=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "id": -576460752303422821,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECq+Yx4ml4lDGXXQUOiq22rA4X7gOR1GS0eWYK1MplWkUAwFAS0vPqITx61gh1oENof2Iwhw6Z/zHJNxyVBMkgLuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+62TtIr"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422821,
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "signed_tx": "tx_+JALAfhCuECq+Yx4ml4lDGXXQUOiq22rA4X7gOR1GS0eWYK1MplWkUAwFAS0vPqITx61gh1oENof2Iwhw6Z/zHJNxyVBMkgLuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+62TtIr",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "id": -576460752303422820,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBOklKuDgpgqHE62fs3+g+waT/rKt5MaUwD755cEQ5HXH5/WUoqZTdLhrWFFo+DZRPFknkHUsTSl2Mq8NWUEIcCuECq+Yx4ml4lDGXXQUOiq22rA4X7gOR1GS0eWYK1MplWkUAwFAS0vPqITx61gh1oENof2Iwhw6Z/zHJNxyVBMkgLuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+57h7uo"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422820,
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "state": "tx_+NILAfiEuEBOklKuDgpgqHE62fs3+g+waT/rKt5MaUwD755cEQ5HXH5/WUoqZTdLhrWFFo+DZRPFknkHUsTSl2Mq8NWUEIcCuECq+Yx4ml4lDGXXQUOiq22rA4X7gOR1GS0eWYK1MplWkUAwFAS0vPqITx61gh1oENof2Iwhw6Z/zHJNxyVBMkgLuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+57h7uo"
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "state": "tx_+NILAfiEuEBOklKuDgpgqHE62fs3+g+waT/rKt5MaUwD755cEQ5HXH5/WUoqZTdLhrWFFo+DZRPFknkHUsTSl2Mq8NWUEIcCuECq+Yx4ml4lDGXXQUOiq22rA4X7gOR1GS0eWYK1MplWkUAwFAS0vPqITx61gh1oENof2Iwhw6Z/zHJNxyVBMkgLuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+57h7uo"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422819,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422819,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000001
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422818,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422818,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBOklKuDgpgqHE62fs3+g+waT/rKt5MaUwD755cEQ5HXH5/WUoqZTdLhrWFFo+DZRPFknkHUsTSl2Mq8NWUEIcCuECq+Yx4ml4lDGXXQUOiq22rA4X7gOR1GS0eWYK1MplWkUAwFAS0vPqITx61gh1oENof2Iwhw6Z/zHJNxyVBMkgLuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+57h7uo",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422817,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422817,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBOklKuDgpgqHE62fs3+g+waT/rKt5MaUwD755cEQ5HXH5/WUoqZTdLhrWFFo+DZRPFknkHUsTSl2Mq8NWUEIcCuECq+Yx4ml4lDGXXQUOiq22rA4X7gOR1GS0eWYK1MplWkUAwFAS0vPqITx61gh1oENof2Iwhw6Z/zHJNxyVBMkgLuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+57h7uo",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422816,
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
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422816,
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjvWGI9TrM2qmijrjltRcHtyOv2eC27qg2rhJiv6XToXBKAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8BwkbN9A=",
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
  "id": -576460752303422815,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECHB1kpj+Jsm8kad9XO3YZbGB09rsI6Cv21gQzKwXLkb3DjofgwjN6LQkFHTlG3P3HGTMeuLzd7SSkNK4K+BpMNuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAe/KMFB"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422815,
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "signed_tx": "tx_+JALAfhCuECHB1kpj+Jsm8kad9XO3YZbGB09rsI6Cv21gQzKwXLkb3DjofgwjN6LQkFHTlG3P3HGTMeuLzd7SSkNK4K+BpMNuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAe/KMFB",
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
  "id": -576460752303422814,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAXnCNwjhvaZ7VWVhzfD+fmhmybkfxQ+uPJRrFFKAnGjod9rBG6mjQxuNrDNC7qNYZB5CoPIH3R5R9ARPWj7dwLuECHB1kpj+Jsm8kad9XO3YZbGB09rsI6Cv21gQzKwXLkb3DjofgwjN6LQkFHTlG3P3HGTMeuLzd7SSkNK4K+BpMNuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfTTvR7"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422814,
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "state": "tx_+NILAfiEuEAXnCNwjhvaZ7VWVhzfD+fmhmybkfxQ+uPJRrFFKAnGjod9rBG6mjQxuNrDNC7qNYZB5CoPIH3R5R9ARPWj7dwLuECHB1kpj+Jsm8kad9XO3YZbGB09rsI6Cv21gQzKwXLkb3DjofgwjN6LQkFHTlG3P3HGTMeuLzd7SSkNK4K+BpMNuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfTTvR7"
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "state": "tx_+NILAfiEuEAXnCNwjhvaZ7VWVhzfD+fmhmybkfxQ+uPJRrFFKAnGjod9rBG6mjQxuNrDNC7qNYZB5CoPIH3R5R9ARPWj7dwLuECHB1kpj+Jsm8kad9XO3YZbGB09rsI6Cv21gQzKwXLkb3DjofgwjN6LQkFHTlG3P3HGTMeuLzd7SSkNK4K+BpMNuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfTTvR7"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422813,
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
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422813,
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
  "id": -576460752303422812,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422812,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAXnCNwjhvaZ7VWVhzfD+fmhmybkfxQ+uPJRrFFKAnGjod9rBG6mjQxuNrDNC7qNYZB5CoPIH3R5R9ARPWj7dwLuECHB1kpj+Jsm8kad9XO3YZbGB09rsI6Cv21gQzKwXLkb3DjofgwjN6LQkFHTlG3P3HGTMeuLzd7SSkNK4K+BpMNuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfTTvR7",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422811,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422811,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000002
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
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
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBjvWGI9TrM2qmijrjltRcHtyOv2eC27qg2rhJiv6XToXBaAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7jCakjM=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "id": -576460752303422810,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDKxyyCRaHowQL3Qvko89wo0PkoAwxmv2rF0Oq84NGOVDNkon3z+rVVYcNjJrf+T0GgZQC8aOAAxKI9cOZPwd4JuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7q5jsz"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422810,
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDKxyyCRaHowQL3Qvko89wo0PkoAwxmv2rF0Oq84NGOVDNkon3z+rVVYcNjJrf+T0GgZQC8aOAAxKI9cOZPwd4JuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+7q5jsz",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "id": -576460752303422809,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECEkCNK5AdjZLkF0a2YqsEVCrWW4LQNUItsXLpsLEeCaV38zF+/Ylzw/7SPbghC16DaTsvxmOmic8lI1P7MaRUFuEDKxyyCRaHowQL3Qvko89wo0PkoAwxmv2rF0Oq84NGOVDNkon3z+rVVYcNjJrf+T0GgZQC8aOAAxKI9cOZPwd4JuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4mxtBT"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422809,
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "state": "tx_+NILAfiEuECEkCNK5AdjZLkF0a2YqsEVCrWW4LQNUItsXLpsLEeCaV38zF+/Ylzw/7SPbghC16DaTsvxmOmic8lI1P7MaRUFuEDKxyyCRaHowQL3Qvko89wo0PkoAwxmv2rF0Oq84NGOVDNkon3z+rVVYcNjJrf+T0GgZQC8aOAAxKI9cOZPwd4JuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4mxtBT"
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "state": "tx_+NILAfiEuECEkCNK5AdjZLkF0a2YqsEVCrWW4LQNUItsXLpsLEeCaV38zF+/Ylzw/7SPbghC16DaTsvxmOmic8lI1P7MaRUFuEDKxyyCRaHowQL3Qvko89wo0PkoAwxmv2rF0Oq84NGOVDNkon3z+rVVYcNjJrf+T0GgZQC8aOAAxKI9cOZPwd4JuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4mxtBT"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422808,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422808,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000001
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422807,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422807,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECEkCNK5AdjZLkF0a2YqsEVCrWW4LQNUItsXLpsLEeCaV38zF+/Ylzw/7SPbghC16DaTsvxmOmic8lI1P7MaRUFuEDKxyyCRaHowQL3Qvko89wo0PkoAwxmv2rF0Oq84NGOVDNkon3z+rVVYcNjJrf+T0GgZQC8aOAAxKI9cOZPwd4JuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4mxtBT",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECEkCNK5AdjZLkF0a2YqsEVCrWW4LQNUItsXLpsLEeCaV38zF+/Ylzw/7SPbghC16DaTsvxmOmic8lI1P7MaRUFuEDKxyyCRaHowQL3Qvko89wo0PkoAwxmv2rF0Oq84NGOVDNkon3z+rVVYcNjJrf+T0GgZQC8aOAAxKI9cOZPwd4JuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4mxtBT",
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
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
  "method": "channels.slash",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECEkCNK5AdjZLkF0a2YqsEVCrWW4LQNUItsXLpsLEeCaV38zF+/Ylzw/7SPbghC16DaTsvxmOmic8lI1P7MaRUFuEDKxyyCRaHowQL3Qvko89wo0PkoAwxmv2rF0Oq84NGOVDNkon3z+rVVYcNjJrf+T0GgZQC8aOAAxKI9cOZPwd4JuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4mxtBT",
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
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
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBjvWGI9TrM2qmijrjltRcHtyOv2eC27qg2rhJiv6XToXoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROELjU+NILAfiEuECEkCNK5AdjZLkF0a2YqsEVCrWW4LQNUItsXLpsLEeCaV38zF+/Ylzw/7SPbghC16DaTsvxmOmic8lI1P7MaRUFuEDKxyyCRaHowQL3Qvko89wo0PkoAwxmv2rF0Oq84NGOVDNkon3z+rVVYcNjJrf+T0GgZQC8aOAAxKI9cOZPwd4JuEj4RjkCoQY71hiPU6zNqpoo645bUXB7cjr9ngtu6oNq4SYr+l06FwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+65AUz5AUk8AfkBP/kBPKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvkBGPh0oCbziXyYo8Ox+VZtROqlQQtKKd21jKCiqh29ftJZTs5e+FGAgICAgICAgICAgICg7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqug5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqeAgID4T6DlslFZIexXT120YXqqt3xFqwcxbt0Suq1WIBNf47yap+2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAH4T6Dt/5Hiy5W70qsqTzdexfFGw0mN5gAjP38MM0HGdpS2q+2gNbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX//AwMDAwACGGR7ISegAFz5IVxI=",
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
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
  "id": -576460752303422806,
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
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
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422806,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422805,
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
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
  "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
  "id": -576460752303422805,
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
    "channel_id": "ch_TMSRQC1dgR75tVeHxfZcwtKh7AjQmHBVrErCMcTLceAe6L7kx",
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
      "fsm_id": "ba_dXVORuzWubPL+pJJRymLJeEkddT5/JgM2aDlJZ+z5+1urzsM"
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
      "fsm_id": "ba_JIb0W38CLH71KDB+rAFDC3qbfkZSNHx3nAQ64PJNFa2Xw7h7"
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5CLtawaA==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422804,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEAg2+PvsxQ8ITLI0wBnOahimBucfDwKMmIz6F7F6SOtxZ1efCDvnx/j4MlkZMiDIw6hvXkzDILjZ/bB0qPmQ5EGuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uQnlDNnY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422804,
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
      "signed_tx": "tx_+MsLAfhCuEAg2+PvsxQ8ITLI0wBnOahimBucfDwKMmIz6F7F6SOtxZ1efCDvnx/j4MlkZMiDIw6hvXkzDILjZ/bB0qPmQ5EGuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uQnlDNnY=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422803,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAINvj77MUPCEyyNMAZzmoYpgbnHw8CjJiM+hexekjrcWdXnwg758f4+DJZGTIgyMOob15MwyC42f2wdKj5kORBrhAjoRHtLhfTJdDPZibIFl1oB01g2w1+vwch9szc6fiUrgk0ptAaKHZCOLgKFVCpxIPsuqL6Ajsr3an7dYDydKqDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kIdChPq"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422803,
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAINvj77MUPCEyyNMAZzmoYpgbnHw8CjJiM+hexekjrcWdXnwg758f4+DJZGTIgyMOob15MwyC42f2wdKj5kORBrhAjoRHtLhfTJdDPZibIFl1oB01g2w1+vwch9szc6fiUrgk0ptAaKHZCOLgKFVCpxIPsuqL6Ajsr3an7dYDydKqDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kIdChPq",
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAINvj77MUPCEyyNMAZzmoYpgbnHw8CjJiM+hexekjrcWdXnwg758f4+DJZGTIgyMOob15MwyC42f2wdKj5kORBrhAjoRHtLhfTJdDPZibIFl1oB01g2w1+vwch9szc6fiUrgk0ptAaKHZCOLgKFVCpxIPsuqL6Ajsr3an7dYDydKqDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kIdChPq",
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAINvj77MUPCEyyNMAZzmoYpgbnHw8CjJiM+hexekjrcWdXnwg758f4+DJZGTIgyMOob15MwyC42f2wdKj5kORBrhAjoRHtLhfTJdDPZibIFl1oB01g2w1+vwch9szc6fiUrgk0ptAaKHZCOLgKFVCpxIPsuqL6Ajsr3an7dYDydKqDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kIdChPq",
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAINvj77MUPCEyyNMAZzmoYpgbnHw8CjJiM+hexekjrcWdXnwg758f4+DJZGTIgyMOob15MwyC42f2wdKj5kORBrhAjoRHtLhfTJdDPZibIFl1oB01g2w1+vwch9szc6fiUrgk0ptAaKHZCOLgKFVCpxIPsuqL6Ajsr3an7dYDydKqDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kIdChPq",
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "message": {
        "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "message": {
        "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
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
  "id": -576460752303422802,
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
  "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
  "id": -576460752303422802,
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "state": "tx_+QENCwH4hLhAINvj77MUPCEyyNMAZzmoYpgbnHw8CjJiM+hexekjrcWdXnwg758f4+DJZGTIgyMOob15MwyC42f2wdKj5kORBrhAjoRHtLhfTJdDPZibIFl1oB01g2w1+vwch9szc6fiUrgk0ptAaKHZCOLgKFVCpxIPsuqL6Ajsr3an7dYDydKqDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kIdChPq"
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "state": "tx_+QENCwH4hLhAINvj77MUPCEyyNMAZzmoYpgbnHw8CjJiM+hexekjrcWdXnwg758f4+DJZGTIgyMOob15MwyC42f2wdKj5kORBrhAjoRHtLhfTJdDPZibIFl1oB01g2w1+vwch9szc6fiUrgk0ptAaKHZCOLgKFVCpxIPsuqL6Ajsr3an7dYDydKqDbiD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kIdChPq"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422801,
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
  "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
  "id": -576460752303422801,
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgCwwhR8ZXQoXHdPYfYyAn55AzPLiIIxp2D5/4olenVnAqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B/878bY=",
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
  "id": -576460752303422800,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEC7wk1YzMEPWMhXr4AfTyqvGfNwi3BrFJJMQDNSZFRtDJuFtCnqwnOt+83OkGxCK2Ofhsv+Lr96FvdbP+/CUHkFuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAen0MHV"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
  "id": -576460752303422800,
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "signed_tx": "tx_+JALAfhCuEC7wk1YzMEPWMhXr4AfTyqvGfNwi3BrFJJMQDNSZFRtDJuFtCnqwnOt+83OkGxCK2Ofhsv+Lr96FvdbP+/CUHkFuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAen0MHV",
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
  "id": -576460752303422799,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEC7wk1YzMEPWMhXr4AfTyqvGfNwi3BrFJJMQDNSZFRtDJuFtCnqwnOt+83OkGxCK2Ofhsv+Lr96FvdbP+/CUHkFuEDpb26t/dPtrOoYwavhjlyF07Txea8hxxMDubJuLLLbUP9jfaB9cLZeovWvIUbRw6GpzIkrhjG3tjq9m64RRggKuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfV8xah"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
  "id": -576460752303422799,
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "state": "tx_+NILAfiEuEC7wk1YzMEPWMhXr4AfTyqvGfNwi3BrFJJMQDNSZFRtDJuFtCnqwnOt+83OkGxCK2Ofhsv+Lr96FvdbP+/CUHkFuEDpb26t/dPtrOoYwavhjlyF07Txea8hxxMDubJuLLLbUP9jfaB9cLZeovWvIUbRw6GpzIkrhjG3tjq9m64RRggKuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfV8xah"
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "state": "tx_+NILAfiEuEC7wk1YzMEPWMhXr4AfTyqvGfNwi3BrFJJMQDNSZFRtDJuFtCnqwnOt+83OkGxCK2Ofhsv+Lr96FvdbP+/CUHkFuEDpb26t/dPtrOoYwavhjlyF07Txea8hxxMDubJuLLLbUP9jfaB9cLZeovWvIUbRw6GpzIkrhjG3tjq9m64RRggKuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfV8xah"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422798,
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
  "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
  "id": -576460752303422798,
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
  "id": -576460752303422797,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
  "id": -576460752303422797,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEC7wk1YzMEPWMhXr4AfTyqvGfNwi3BrFJJMQDNSZFRtDJuFtCnqwnOt+83OkGxCK2Ofhsv+Lr96FvdbP+/CUHkFuEDpb26t/dPtrOoYwavhjlyF07Txea8hxxMDubJuLLLbUP9jfaB9cLZeovWvIUbRw6GpzIkrhjG3tjq9m64RRggKuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAfV8xah",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422796,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
  "id": -576460752303422796,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000002
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
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
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgCwwhR8ZXQoXHdPYfYyAn55AzPLiIIxp2D5/4olenVnA6AWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7svakJw=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "id": -576460752303422795,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDNeIJhFArxgzZYhpR9tcsPU9/cbckysGUlfRfNYeksDIPKkHACuVaBl0e7aWrEBbp9C4UMPTBr2U6j7DjGdZcDuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4X8hpQ"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
  "id": -576460752303422795,
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDNeIJhFArxgzZYhpR9tcsPU9/cbckysGUlfRfNYeksDIPKkHACuVaBl0e7aWrEBbp9C4UMPTBr2U6j7DjGdZcDuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4X8hpQ",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "id": -576460752303422794,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDNeIJhFArxgzZYhpR9tcsPU9/cbckysGUlfRfNYeksDIPKkHACuVaBl0e7aWrEBbp9C4UMPTBr2U6j7DjGdZcDuEDU7ZiCqDNQYx8elaJpgP2b6YUgigvzNCGFrINq6oGeWCokm+TzhJdRDiNZuvN/6tsswM/5BqpoBw4cnPqp8moJuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+62vmsC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
  "id": -576460752303422794,
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "state": "tx_+NILAfiEuEDNeIJhFArxgzZYhpR9tcsPU9/cbckysGUlfRfNYeksDIPKkHACuVaBl0e7aWrEBbp9C4UMPTBr2U6j7DjGdZcDuEDU7ZiCqDNQYx8elaJpgP2b6YUgigvzNCGFrINq6oGeWCokm+TzhJdRDiNZuvN/6tsswM/5BqpoBw4cnPqp8moJuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+62vmsC"
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "state": "tx_+NILAfiEuEDNeIJhFArxgzZYhpR9tcsPU9/cbckysGUlfRfNYeksDIPKkHACuVaBl0e7aWrEBbp9C4UMPTBr2U6j7DjGdZcDuEDU7ZiCqDNQYx8elaJpgP2b6YUgigvzNCGFrINq6oGeWCokm+TzhJdRDiNZuvN/6tsswM/5BqpoBw4cnPqp8moJuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+62vmsC"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422793,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
  "id": -576460752303422793,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000001
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422792,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
  "id": -576460752303422792,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDNeIJhFArxgzZYhpR9tcsPU9/cbckysGUlfRfNYeksDIPKkHACuVaBl0e7aWrEBbp9C4UMPTBr2U6j7DjGdZcDuEDU7ZiCqDNQYx8elaJpgP2b6YUgigvzNCGFrINq6oGeWCokm+TzhJdRDiNZuvN/6tsswM/5BqpoBw4cnPqp8moJuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+62vmsC",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422791,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
  "id": -576460752303422791,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDNeIJhFArxgzZYhpR9tcsPU9/cbckysGUlfRfNYeksDIPKkHACuVaBl0e7aWrEBbp9C4UMPTBr2U6j7DjGdZcDuEDU7ZiCqDNQYx8elaJpgP2b6YUgigvzNCGFrINq6oGeWCokm+TzhJdRDiNZuvN/6tsswM/5BqpoBw4cnPqp8moJuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+62vmsC",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422790,
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
  "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
  "id": -576460752303422790,
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgCwwhR8ZXQoXHdPYfYyAn55AzPLiIIxp2D5/4olenVnBKAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8B0z2XTw=",
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
  "id": -576460752303422789,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED09HX519ouYR36ez7jskmmJnlcmAgDxC6O+EtQntYHqh7Rqt1f6AtdcjFYLI8doUY6K9TMb96wPTM7HzBUUdUDuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcZjDF6"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
  "id": -576460752303422789,
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "signed_tx": "tx_+JALAfhCuED09HX519ouYR36ez7jskmmJnlcmAgDxC6O+EtQntYHqh7Rqt1f6AtdcjFYLI8doUY6K9TMb96wPTM7HzBUUdUDuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcZjDF6",
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
  "id": -576460752303422788,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEDDc8wuuCCeLe5gDbRbXDNM3pkwA/lYQC11qEOCvJxGKklmge2MB5s4Dtp5g259uFgnDNmZRUs0KWahCZeQr+sLuED09HX519ouYR36ez7jskmmJnlcmAgDxC6O+EtQntYHqh7Rqt1f6AtdcjFYLI8doUY6K9TMb96wPTM7HzBUUdUDuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAdmFU75"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
  "id": -576460752303422788,
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "state": "tx_+NILAfiEuEDDc8wuuCCeLe5gDbRbXDNM3pkwA/lYQC11qEOCvJxGKklmge2MB5s4Dtp5g259uFgnDNmZRUs0KWahCZeQr+sLuED09HX519ouYR36ez7jskmmJnlcmAgDxC6O+EtQntYHqh7Rqt1f6AtdcjFYLI8doUY6K9TMb96wPTM7HzBUUdUDuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAdmFU75"
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "state": "tx_+NILAfiEuEDDc8wuuCCeLe5gDbRbXDNM3pkwA/lYQC11qEOCvJxGKklmge2MB5s4Dtp5g259uFgnDNmZRUs0KWahCZeQr+sLuED09HX519ouYR36ez7jskmmJnlcmAgDxC6O+EtQntYHqh7Rqt1f6AtdcjFYLI8doUY6K9TMb96wPTM7HzBUUdUDuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAdmFU75"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422787,
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
  "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
  "id": -576460752303422787,
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
  "id": -576460752303422786,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
  "id": -576460752303422786,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEDDc8wuuCCeLe5gDbRbXDNM3pkwA/lYQC11qEOCvJxGKklmge2MB5s4Dtp5g259uFgnDNmZRUs0KWahCZeQr+sLuED09HX519ouYR36ez7jskmmJnlcmAgDxC6O+EtQntYHqh7Rqt1f6AtdcjFYLI8doUY6K9TMb96wPTM7HzBUUdUDuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAdmFU75",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422785,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
  "id": -576460752303422785,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000002
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
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
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBgCwwhR8ZXQoXHdPYfYyAn55AzPLiIIxp2D5/4olenVnBaAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7o4Fa54=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "id": -576460752303422784,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECQSac5AGloGTWzB9D0PORkeLtX05VUdp6aueRRFCLTu0j9B2tsiCTjSaI0iB54Bq/CgCluwtP6i0PkFq3qPWwEuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5YvlU2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
  "id": -576460752303422784,
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "signed_tx": "tx_+JALAfhCuECQSac5AGloGTWzB9D0PORkeLtX05VUdp6aueRRFCLTu0j9B2tsiCTjSaI0iB54Bq/CgCluwtP6i0PkFq3qPWwEuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5YvlU2",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "id": -576460752303422783,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuECBmxCjTIXJbEXNWr1ApIPqt2dtRlUFY08nzCpkZdqaBcU/obNzqrgqWaE2tr0KuOapYePngHcbKeoBEkcqNSYDuECQSac5AGloGTWzB9D0PORkeLtX05VUdp6aueRRFCLTu0j9B2tsiCTjSaI0iB54Bq/CgCluwtP6i0PkFq3qPWwEuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+76MZYr"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
  "id": -576460752303422783,
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "state": "tx_+NILAfiEuECBmxCjTIXJbEXNWr1ApIPqt2dtRlUFY08nzCpkZdqaBcU/obNzqrgqWaE2tr0KuOapYePngHcbKeoBEkcqNSYDuECQSac5AGloGTWzB9D0PORkeLtX05VUdp6aueRRFCLTu0j9B2tsiCTjSaI0iB54Bq/CgCluwtP6i0PkFq3qPWwEuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+76MZYr"
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "state": "tx_+NILAfiEuECBmxCjTIXJbEXNWr1ApIPqt2dtRlUFY08nzCpkZdqaBcU/obNzqrgqWaE2tr0KuOapYePngHcbKeoBEkcqNSYDuECQSac5AGloGTWzB9D0PORkeLtX05VUdp6aueRRFCLTu0j9B2tsiCTjSaI0iB54Bq/CgCluwtP6i0PkFq3qPWwEuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+76MZYr"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422782,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
  "id": -576460752303422782,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000001
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422781,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
  "id": -576460752303422781,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuECBmxCjTIXJbEXNWr1ApIPqt2dtRlUFY08nzCpkZdqaBcU/obNzqrgqWaE2tr0KuOapYePngHcbKeoBEkcqNSYDuECQSac5AGloGTWzB9D0PORkeLtX05VUdp6aueRRFCLTu0j9B2tsiCTjSaI0iB54Bq/CgCluwtP6i0PkFq3qPWwEuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+76MZYr",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECBmxCjTIXJbEXNWr1ApIPqt2dtRlUFY08nzCpkZdqaBcU/obNzqrgqWaE2tr0KuOapYePngHcbKeoBEkcqNSYDuECQSac5AGloGTWzB9D0PORkeLtX05VUdp6aueRRFCLTu0j9B2tsiCTjSaI0iB54Bq/CgCluwtP6i0PkFq3qPWwEuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+76MZYr",
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
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
  "method": "channels.slash",
  "params": {}
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuECBmxCjTIXJbEXNWr1ApIPqt2dtRlUFY08nzCpkZdqaBcU/obNzqrgqWaE2tr0KuOapYePngHcbKeoBEkcqNSYDuECQSac5AGloGTWzB9D0PORkeLtX05VUdp6aueRRFCLTu0j9B2tsiCTjSaI0iB54Bq/CgCluwtP6i0PkFq3qPWwEuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+76MZYr",
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
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
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBgCwwhR8ZXQoXHdPYfYyAn55AzPLiIIxp2D5/4olenVnoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79LjU+NILAfiEuECBmxCjTIXJbEXNWr1ApIPqt2dtRlUFY08nzCpkZdqaBcU/obNzqrgqWaE2tr0KuOapYePngHcbKeoBEkcqNSYDuECQSac5AGloGTWzB9D0PORkeLtX05VUdp6aueRRFCLTu0j9B2tsiCTjSaI0iB54Bq/CgCluwtP6i0PkFq3qPWwEuEj4RjkCoQYAsMIUfGV0KFx3T2H2MgJ+eQMzy4iCMadg+f+KJXp1ZwWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+65AUz5AUk8AfkBP/kBPKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvkBGPh0oCbziXyYo8Ox+VZtROqlQQtKKd21jKCiqh29ftJZTs5e+FGAgICAgICAgICAgICg7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqug5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqeAgID4T6DlslFZIexXT120YXqqt3xFqwcxbt0Suq1WIBNf47yap+2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAH4T6Dt/5Hiy5W70qsqTzdexfFGw0mN5gAjP38MM0HGdpS2q+2gNbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX//AwMDAwACGGR7ISegAQ10gySA=",
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
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
  "id": -576460752303422780,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
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
  "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
  "id": -576460752303422780,
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
    "channel_id": "ch_1JdwZsNYU2SLpwdNC98o9DRRwx8ub1nJZCkDqyt9HxazeqVaX",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422779,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
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
      "fsm_id": "ba_4AoLGuOzoqXy0QBnL/U/rjH0pSwRNL39cEvyewlXfDbrOtr8"
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
      "fsm_id": "ba_4X4oJUAOcyXSJ/HVzNDVB5cpagf1BKMKBlrumeLcfPIuUduI"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhAcW47IdoVlsitY21h/Ku93EKqO7HEQeD04gBq8ukLLv0hj+qJSJgAKEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCGJGE5yoAAAgoAhhAGeddIAMCgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5D0mU97Q==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422778,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEBnz+SVrXZMNRKC2ZLsYB88j/JjkFdRFZlUpJJsLQwkl87XkEjpktUdkTB3X1bR9DCM0kkgWTfD1DpiFZRD6M4GuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uQ9C5bSo="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422778,
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
      "signed_tx": "tx_+MsLAfhCuEBnz+SVrXZMNRKC2ZLsYB88j/JjkFdRFZlUpJJsLQwkl87XkEjpktUdkTB3X1bR9DCM0kkgWTfD1DpiFZRD6M4GuIP4gTIBoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79IY/qiUiYAChAdE2bzF1EZ9o/w1FLVmp0aaaxGjwVoLXBbZVYWJ3tE4QhiRhOcqAAAIKAIYQBnnXSADAoBZPR7ifdxSRnXthclt4V2LYb4k1nX7ccoJg1YvasN/uQ9C5bSo=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303422777,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhAYtL030wJcwAtTeQn/GLWcSTLsptBKk/QiuWHnpxih8LgDNakZuZxnmbNw6FBwo+QCuhXFNSxb7++tHLmR/4eArhAZ8/kla12TDUSgtmS7GAfPI/yY5BXURWZVKSSbC0MJJfO15BI6ZLVHZEwd19W0fQwjNJJIFk3w9Q6YhWUQ+jOBriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kMsURmj"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303422777,
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QENCwH4hLhAYtL030wJcwAtTeQn/GLWcSTLsptBKk/QiuWHnpxih8LgDNakZuZxnmbNw6FBwo+QCuhXFNSxb7++tHLmR/4eArhAZ8/kla12TDUSgtmS7GAfPI/yY5BXURWZVKSSbC0MJJfO15BI6ZLVHZEwd19W0fQwjNJJIFk3w9Q6YhWUQ+jOBriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kMsURmj",
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QENCwH4hLhAYtL030wJcwAtTeQn/GLWcSTLsptBKk/QiuWHnpxih8LgDNakZuZxnmbNw6FBwo+QCuhXFNSxb7++tHLmR/4eArhAZ8/kla12TDUSgtmS7GAfPI/yY5BXURWZVKSSbC0MJJfO15BI6ZLVHZEwd19W0fQwjNJJIFk3w9Q6YhWUQ+jOBriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kMsURmj",
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAYtL030wJcwAtTeQn/GLWcSTLsptBKk/QiuWHnpxih8LgDNakZuZxnmbNw6FBwo+QCuhXFNSxb7++tHLmR/4eArhAZ8/kla12TDUSgtmS7GAfPI/yY5BXURWZVKSSbC0MJJfO15BI6ZLVHZEwd19W0fQwjNJJIFk3w9Q6YhWUQ+jOBriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kMsURmj",
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QENCwH4hLhAYtL030wJcwAtTeQn/GLWcSTLsptBKk/QiuWHnpxih8LgDNakZuZxnmbNw6FBwo+QCuhXFNSxb7++tHLmR/4eArhAZ8/kla12TDUSgtmS7GAfPI/yY5BXURWZVKSSbC0MJJfO15BI6ZLVHZEwd19W0fQwjNJJIFk3w9Q6YhWUQ+jOBriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kMsURmj",
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "message": {
        "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "message": {
        "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
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
  "id": -576460752303422776,
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
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422776,
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "state": "tx_+QENCwH4hLhAYtL030wJcwAtTeQn/GLWcSTLsptBKk/QiuWHnpxih8LgDNakZuZxnmbNw6FBwo+QCuhXFNSxb7++tHLmR/4eArhAZ8/kla12TDUSgtmS7GAfPI/yY5BXURWZVKSSbC0MJJfO15BI6ZLVHZEwd19W0fQwjNJJIFk3w9Q6YhWUQ+jOBriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kMsURmj"
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "state": "tx_+QENCwH4hLhAYtL030wJcwAtTeQn/GLWcSTLsptBKk/QiuWHnpxih8LgDNakZuZxnmbNw6FBwo+QCuhXFNSxb7++tHLmR/4eArhAZ8/kla12TDUSgtmS7GAfPI/yY5BXURWZVKSSbC0MJJfO15BI6ZLVHZEwd19W0fQwjNJJIFk3w9Q6YhWUQ+jOBriD+IEyAaEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SGP6olImAAoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIYkYTnKgAACCgCGEAZ510gAwKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7kMsURmj"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422775,
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
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422775,
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBoQe82hinYAsa8GJbiHFW+uGrKrR9sXHDRQ0YXYLvyfLAqAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8Byr4vMI=",
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
  "id": -576460752303422774,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBjeIbyP1A38S3XwdgJtnbstE7SDOka0Q5yAWfXra/oZ1HIU6I6ec9PvTQuNIHqXFN9MOkddFWA/B9ITkO+2IULuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAe6piWn"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422774,
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBjeIbyP1A38S3XwdgJtnbstE7SDOka0Q5yAWfXra/oZ1HIU6I6ec9PvTQuNIHqXFN9MOkddFWA/B9ITkO+2IULuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAe6piWn",
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
  "id": -576460752303422773,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBjeIbyP1A38S3XwdgJtnbstE7SDOka0Q5yAWfXra/oZ1HIU6I6ec9PvTQuNIHqXFN9MOkddFWA/B9ITkO+2IULuEB4n7DfHJBpcqsQffjkaBAcJWOO2qfvGojelF9nBQZzUmDhAeXmuJEnP/cTqmP5I36ICwPiVdvguqsXvVrGjuULuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcH0/3O"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422773,
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "state": "tx_+NILAfiEuEBjeIbyP1A38S3XwdgJtnbstE7SDOka0Q5yAWfXra/oZ1HIU6I6ec9PvTQuNIHqXFN9MOkddFWA/B9ITkO+2IULuEB4n7DfHJBpcqsQffjkaBAcJWOO2qfvGojelF9nBQZzUmDhAeXmuJEnP/cTqmP5I36ICwPiVdvguqsXvVrGjuULuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcH0/3O"
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "state": "tx_+NILAfiEuEBjeIbyP1A38S3XwdgJtnbstE7SDOka0Q5yAWfXra/oZ1HIU6I6ec9PvTQuNIHqXFN9MOkddFWA/B9ITkO+2IULuEB4n7DfHJBpcqsQffjkaBAcJWOO2qfvGojelF9nBQZzUmDhAeXmuJEnP/cTqmP5I36ICwPiVdvguqsXvVrGjuULuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcH0/3O"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422772,
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
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422772,
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
  "id": -576460752303422771,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422771,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBjeIbyP1A38S3XwdgJtnbstE7SDOka0Q5yAWfXra/oZ1HIU6I6ec9PvTQuNIHqXFN9MOkddFWA/B9ITkO+2IULuEB4n7DfHJBpcqsQffjkaBAcJWOO2qfvGojelF9nBQZzUmDhAeXmuJEnP/cTqmP5I36ICwPiVdvguqsXvVrGjuULuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywKgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAcH0/3O",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422770,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422770,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000002
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
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
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBoQe82hinYAsa8GJbiHFW+uGrKrR9sXHDRQ0YXYLvyfLA6AWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7py8oUA=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "id": -576460752303422769,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBhvSPEKf/EY1S93cg/dUzuNl3xviqX2ijAdz4QEXc21R3xQwOPlAgiLXLOaAzj3EMw2CUPz0WGqieu7AmAW4sCuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4gFGRq"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422769,
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBhvSPEKf/EY1S93cg/dUzuNl3xviqX2ijAdz4QEXc21R3xQwOPlAgiLXLOaAzj3EMw2CUPz0WGqieu7AmAW4sCuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4gFGRq",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "id": -576460752303422768,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBR54bR4uVlN4GTwjF+mrrITF1qMYAgnCit9gw/24rJHFUrcv/f5e7WAx2/slZuurG3GhrZn6pT6VKOjGJxMMQJuEBhvSPEKf/EY1S93cg/dUzuNl3xviqX2ijAdz4QEXc21R3xQwOPlAgiLXLOaAzj3EMw2CUPz0WGqieu7AmAW4sCuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6ic6me"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422768,
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "state": "tx_+NILAfiEuEBR54bR4uVlN4GTwjF+mrrITF1qMYAgnCit9gw/24rJHFUrcv/f5e7WAx2/slZuurG3GhrZn6pT6VKOjGJxMMQJuEBhvSPEKf/EY1S93cg/dUzuNl3xviqX2ijAdz4QEXc21R3xQwOPlAgiLXLOaAzj3EMw2CUPz0WGqieu7AmAW4sCuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6ic6me"
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "state": "tx_+NILAfiEuEBR54bR4uVlN4GTwjF+mrrITF1qMYAgnCit9gw/24rJHFUrcv/f5e7WAx2/slZuurG3GhrZn6pT6VKOjGJxMMQJuEBhvSPEKf/EY1S93cg/dUzuNl3xviqX2ijAdz4QEXc21R3xQwOPlAgiLXLOaAzj3EMw2CUPz0WGqieu7AmAW4sCuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6ic6me"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422767,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422767,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000001
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422766,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422766,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBR54bR4uVlN4GTwjF+mrrITF1qMYAgnCit9gw/24rJHFUrcv/f5e7WAx2/slZuurG3GhrZn6pT6VKOjGJxMMQJuEBhvSPEKf/EY1S93cg/dUzuNl3xviqX2ijAdz4QEXc21R3xQwOPlAgiLXLOaAzj3EMw2CUPz0WGqieu7AmAW4sCuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6ic6me",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422765,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422765,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBR54bR4uVlN4GTwjF+mrrITF1qMYAgnCit9gw/24rJHFUrcv/f5e7WAx2/slZuurG3GhrZn6pT6VKOjGJxMMQJuEBhvSPEKf/EY1S93cg/dUzuNl3xviqX2ijAdz4QEXc21R3xQwOPlAgiLXLOaAzj3EMw2CUPz0WGqieu7AmAW4sCuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywOgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+6ic6me",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422764,
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
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422764,
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBoQe82hinYAsa8GJbiHFW+uGrKrR9sXHDRQ0YXYLvyfLBKAqG9l6JqC11WrH1owrEqHDz6ErlwysBZym6Ij05UF8BySohx8=",
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
  "id": -576460752303422763,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAoFm46k/ZgNh8ngHZ5tXkndZs7BkNdfPprjlA0Rl92DjyZ/KCwus8hAIwM8BiTd0HVOz9Y2/cVKlhN/EnXELIAuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeeayjs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422763,
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAoFm46k/ZgNh8ngHZ5tXkndZs7BkNdfPprjlA0Rl92DjyZ/KCwus8hAIwM8BiTd0HVOz9Y2/cVKlhN/EnXELIAuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeeayjs",
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
  "id": -576460752303422762,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAkKqd/rPNsqsvxLJFA4ghNNTN388QOtStEUsqSDeFEuTxmoy9Ky35u5NRWhWJ/4H+gRJ4rmnmZMHDJ+QDK70wOuEAoFm46k/ZgNh8ngHZ5tXkndZs7BkNdfPprjlA0Rl92DjyZ/KCwus8hAIwM8BiTd0HVOz9Y2/cVKlhN/EnXELIAuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeGtxe2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422762,
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "state": "tx_+NILAfiEuEAkKqd/rPNsqsvxLJFA4ghNNTN388QOtStEUsqSDeFEuTxmoy9Ky35u5NRWhWJ/4H+gRJ4rmnmZMHDJ+QDK70wOuEAoFm46k/ZgNh8ngHZ5tXkndZs7BkNdfPprjlA0Rl92DjyZ/KCwus8hAIwM8BiTd0HVOz9Y2/cVKlhN/EnXELIAuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeGtxe2"
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "state": "tx_+NILAfiEuEAkKqd/rPNsqsvxLJFA4ghNNTN388QOtStEUsqSDeFEuTxmoy9Ky35u5NRWhWJ/4H+gRJ4rmnmZMHDJ+QDK70wOuEAoFm46k/ZgNh8ngHZ5tXkndZs7BkNdfPprjlA0Rl92DjyZ/KCwus8hAIwM8BiTd0HVOz9Y2/cVKlhN/EnXELIAuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeGtxe2"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422761,
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
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422761,
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
  "id": -576460752303422760,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422760,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAkKqd/rPNsqsvxLJFA4ghNNTN388QOtStEUsqSDeFEuTxmoy9Ky35u5NRWhWJ/4H+gRJ4rmnmZMHDJ+QDK70wOuEAoFm46k/ZgNh8ngHZ5tXkndZs7BkNdfPprjlA0Rl92DjyZ/KCwus8hAIwM8BiTd0HVOz9Y2/cVKlhN/EnXELIAuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywSgKhvZeiagtdVqx9aMKxKhw8+hK5cMrAWcpuiI9OVBfAeGtxe2",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAArDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/48asSI"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422759,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422759,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000002
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
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
    "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
    "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBoQe82hinYAsa8GJbiHFW+uGrKrR9sXHDRQ0YXYLvyfLBaAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7tCfpqU=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "id": -576460752303422758,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDrvyS8U0MUx1obGOCgJvG79RMUzRr8/IyrAqNJX6402OVlQtX+nbgyy6fPtQPIlqkZZLoUpgOsVoxFr2OpssoNuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5fjUuv"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422758,
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDrvyS8U0MUx1obGOCgJvG79RMUzRr8/IyrAqNJX6402OVlQtX+nbgyy6fPtQPIlqkZZLoUpgOsVoxFr2OpssoNuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+5fjUuv",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
          "op": "OffChainTransfer",
          "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
  "id": -576460752303422757,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAN+f2nWc4wXL3kmzzGizws3WayXAKarOZZek0wpkBd4zYO7oiSufSM+3C6bVYABh51zOzqn6bi2QJIrFmGprILuEDrvyS8U0MUx1obGOCgJvG79RMUzRr8/IyrAqNJX6402OVlQtX+nbgyy6fPtQPIlqkZZLoUpgOsVoxFr2OpssoNuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+59WIcv"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422757,
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "state": "tx_+NILAfiEuEAN+f2nWc4wXL3kmzzGizws3WayXAKarOZZek0wpkBd4zYO7oiSufSM+3C6bVYABh51zOzqn6bi2QJIrFmGprILuEDrvyS8U0MUx1obGOCgJvG79RMUzRr8/IyrAqNJX6402OVlQtX+nbgyy6fPtQPIlqkZZLoUpgOsVoxFr2OpssoNuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+59WIcv"
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "state": "tx_+NILAfiEuEAN+f2nWc4wXL3kmzzGizws3WayXAKarOZZek0wpkBd4zYO7oiSufSM+3C6bVYABh51zOzqn6bi2QJIrFmGprILuEDrvyS8U0MUx1obGOCgJvG79RMUzRr8/IyrAqNJX6402OVlQtX+nbgyy6fPtQPIlqkZZLoUpgOsVoxFr2OpssoNuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+59WIcv"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422756,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422756,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
      "balance": 40000000000001
    },
    {
      "account": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422755,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422755,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAN+f2nWc4wXL3kmzzGizws3WayXAKarOZZek0wpkBd4zYO7oiSufSM+3C6bVYABh51zOzqn6bi2QJIrFmGprILuEDrvyS8U0MUx1obGOCgJvG79RMUzRr8/IyrAqNJX6402OVlQtX+nbgyy6fPtQPIlqkZZLoUpgOsVoxFr2OpssoNuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+59WIcv",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEIvKCgEAhiRhOcqAAbDvQAGgxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX/+k/hhK"
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAN+f2nWc4wXL3kmzzGizws3WayXAKarOZZek0wpkBd4zYO7oiSufSM+3C6bVYABh51zOzqn6bi2QJIrFmGprILuEDrvyS8U0MUx1obGOCgJvG79RMUzRr8/IyrAqNJX6402OVlQtX+nbgyy6fPtQPIlqkZZLoUpgOsVoxFr2OpssoNuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+59WIcv",
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NILAfiEuEAN+f2nWc4wXL3kmzzGizws3WayXAKarOZZek0wpkBd4zYO7oiSufSM+3C6bVYABh51zOzqn6bi2QJIrFmGprILuEDrvyS8U0MUx1obGOCgJvG79RMUzRr8/IyrAqNJX6402OVlQtX+nbgyy6fPtQPIlqkZZLoUpgOsVoxFr2OpssoNuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+59WIcv",
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
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
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "signed_tx": "tx_+QJ9CwHAuQJ3+QJ0NwGhBoQe82hinYAsa8GJbiHFW+uGrKrR9sXHDRQ0YXYLvyfLoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROELjU+NILAfiEuEAN+f2nWc4wXL3kmzzGizws3WayXAKarOZZek0wpkBd4zYO7oiSufSM+3C6bVYABh51zOzqn6bi2QJIrFmGprILuEDrvyS8U0MUx1obGOCgJvG79RMUzRr8/IyrAqNJX6402OVlQtX+nbgyy6fPtQPIlqkZZLoUpgOsVoxFr2OpssoNuEj4RjkCoQaEHvNoYp2ALGvBiW4hxVvrhqyq0fbFxw0UNGF2C78nywWgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+65AUz5AUk8AfkBP/kBPKAm84l8mKPDsflWbUTqpUELSindtYygoqodvX7SWU7OXvkBGPh0oCbziXyYo8Ox+VZtROqlQQtKKd21jKCiqh29ftJZTs5e+FGAgICAgICAgICAgICg7f+R4suVu9KrKk83XsXxRsNJjeYAIz9/DDNBxnaUtqug5bJRWSHsV09dtGF6qrd8RasHMW7dErqtViATX+O8mqeAgID4T6DlslFZIexXT120YXqqt3xFqwcxbt0Suq1WIBNf47yap+2gMTZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThCLygoBAIYkYTnKgAH4T6Dt/5Hiy5W70qsqTzdexfFGw0mN5gAjP38MM0HGdpS2q+2gNbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/SLygoBAIY/qiUiX//AwMDAwACGGR7ISegAGbYVppw=",
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
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
  "id": -576460752303422754,
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
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
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422754,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303422753,
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
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
  "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
  "id": -576460752303422753,
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
    "channel_id": "ch_21BrN86zj3FEjJEeUBxXa2pCcroywZVfnZeDvHk19Jj5TTdHYw",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator closes WebSocket connection
