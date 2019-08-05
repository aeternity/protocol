
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_QnZTp2rcuY4zZDQGXuYaMbqPiekMCE2mSsZjNgo4YG6U6pBRP&lock_period=10&port=14035&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_zLYHnnooYQhNMVodsxoXSc5zEv2ouzXUc91rgwYN9sRYPsjdU&role=initiator
```

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_QnZTp2rcuY4zZDQGXuYaMbqPiekMCE2mSsZjNgo4YG6U6pBRP&lock_period=10&port=14035&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_zLYHnnooYQhNMVodsxoXSc5zEv2ouzXUc91rgwYN9sRYPsjdU&role=responder
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
      "signed_tx": "tx_+IgLAcC4g/iBMgGhATYCBrI2BNuE6IvbTxvKKCBHiukJKReG/sl/95YnHm7zhj+qJSJgAKEBgjC/LrZ1mGltIX68J5ML2qxkm4r6rSDZKH/ih6dhz12GJGE5yoAAAgoAhhAGeddIAMCgec6VB+9/6Y9a5tYzaqU5ibParER/CtIESsVAUssbVx8BVUaKtQ==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423323,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MsLAfhCuEA2zJqS9FNG6BdzmzEqO0rJklCvUtwIPDAxIDOCHrNdfMGB0tzC6zOxIlu0pA5YIjT0XicYSPXZy/gun/Qkj2UMuIP4gTIBoQE2AgayNgTbhOiL208byiggR4rpCSkXhv7Jf/eWJx5u84Y/qiUiYAChAYIwvy62dZhpbSF+vCeTC9qsZJuK+q0g2Sh/4oenYc9dhiRhOcqAAAIKAIYQBnnXSADAoHnOlQfvf+mPWubWM2qlOYmz2qxEfwrSBErFQFLLG1cfASTTJCA="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423323,
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
      "signed_tx": "tx_+MsLAfhCuEA2zJqS9FNG6BdzmzEqO0rJklCvUtwIPDAxIDOCHrNdfMGB0tzC6zOxIlu0pA5YIjT0XicYSPXZy/gun/Qkj2UMuIP4gTIBoQE2AgayNgTbhOiL208byiggR4rpCSkXhv7Jf/eWJx5u84Y/qiUiYAChAYIwvy62dZhpbSF+vCeTC9qsZJuK+q0g2Sh/4oenYc9dhiRhOcqAAAIKAIYQBnnXSADAoHnOlQfvf+mPWubWM2qlOYmz2qxEfwrSBErFQFLLG1cfASTTJCA=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423322,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QENCwH4hLhANsyakvRTRugXc5sxKjtKyZJQr1LcCDwwMSAzgh6zXXzBgdLcwuszsSJbtKQOWCI09F4nGEj12cv4Lp/0JI9lDLhA+9vvoYcrQcVORsbTuRFGIoJfa2Vk9r1hKdJMbPeE8Y8ESdFNHkM6yHE77pMitW25ShtcW8Z8RsFHVw3idoHqAriD+IEyAaEBNgIGsjYE24Toi9tPG8ooIEeK6QkpF4b+yX/3licebvOGP6olImAAoQGCML8utnWYaW0hfrwnkwvarGSbivqtINkof+KHp2HPXYYkYTnKgAACCgCGEAZ510gAwKB5zpUH73/pj1rm1jNqpTmJs9qsRH8K0gRKxUBSyxtXHwEzB/xT"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303423322,
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
      "tx": "tx_+QENCwH4hLhANsyakvRTRugXc5sxKjtKyZJQr1LcCDwwMSAzgh6zXXzBgdLcwuszsSJbtKQOWCI09F4nGEj12cv4Lp/0JI9lDLhA+9vvoYcrQcVORsbTuRFGIoJfa2Vk9r1hKdJMbPeE8Y8ESdFNHkM6yHE77pMitW25ShtcW8Z8RsFHVw3idoHqAriD+IEyAaEBNgIGsjYE24Toi9tPG8ooIEeK6QkpF4b+yX/3licebvOGP6olImAAoQGCML8utnWYaW0hfrwnkwvarGSbivqtINkof+KHp2HPXYYkYTnKgAACCgCGEAZ510gAwKB5zpUH73/pj1rm1jNqpTmJs9qsRH8K0gRKxUBSyxtXHwEzB/xT",
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
      "tx": "tx_+QENCwH4hLhANsyakvRTRugXc5sxKjtKyZJQr1LcCDwwMSAzgh6zXXzBgdLcwuszsSJbtKQOWCI09F4nGEj12cv4Lp/0JI9lDLhA+9vvoYcrQcVORsbTuRFGIoJfa2Vk9r1hKdJMbPeE8Y8ESdFNHkM6yHE77pMitW25ShtcW8Z8RsFHVw3idoHqAriD+IEyAaEBNgIGsjYE24Toi9tPG8ooIEeK6QkpF4b+yX/3licebvOGP6olImAAoQGCML8utnWYaW0hfrwnkwvarGSbivqtINkof+KHp2HPXYYkYTnKgAACCgCGEAZ510gAwKB5zpUH73/pj1rm1jNqpTmJs9qsRH8K0gRKxUBSyxtXHwEzB/xT",
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
      "tx": "tx_+QENCwH4hLhANsyakvRTRugXc5sxKjtKyZJQr1LcCDwwMSAzgh6zXXzBgdLcwuszsSJbtKQOWCI09F4nGEj12cv4Lp/0JI9lDLhA+9vvoYcrQcVORsbTuRFGIoJfa2Vk9r1hKdJMbPeE8Y8ESdFNHkM6yHE77pMitW25ShtcW8Z8RsFHVw3idoHqAriD+IEyAaEBNgIGsjYE24Toi9tPG8ooIEeK6QkpF4b+yX/3licebvOGP6olImAAoQGCML8utnWYaW0hfrwnkwvarGSbivqtINkof+KHp2HPXYYkYTnKgAACCgCGEAZ510gAwKB5zpUH73/pj1rm1jNqpTmJs9qsRH8K0gRKxUBSyxtXHwEzB/xT",
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
      "tx": "tx_+QENCwH4hLhANsyakvRTRugXc5sxKjtKyZJQr1LcCDwwMSAzgh6zXXzBgdLcwuszsSJbtKQOWCI09F4nGEj12cv4Lp/0JI9lDLhA+9vvoYcrQcVORsbTuRFGIoJfa2Vk9r1hKdJMbPeE8Y8ESdFNHkM6yHE77pMitW25ShtcW8Z8RsFHVw3idoHqAriD+IEyAaEBNgIGsjYE24Toi9tPG8ooIEeK6QkpF4b+yX/3licebvOGP6olImAAoQGCML8utnWYaW0hfrwnkwvarGSbivqtINkof+KHp2HPXYYkYTnKgAACCgCGEAZ510gAwKB5zpUH73/pj1rm1jNqpTmJs9qsRH8K0gRKxUBSyxtXHwEzB/xT",
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
    "to": "ak_zLYHnnooYQhNMVodsxoXSc5zEv2ouzXUc91rgwYN9sRYPsjdU"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
    "data": {
      "message": {
        "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
        "from": "ak_QnZTp2rcuY4zZDQGXuYaMbqPiekMCE2mSsZjNgo4YG6U6pBRP",
        "info": "Hello",
        "to": "ak_zLYHnnooYQhNMVodsxoXSc5zEv2ouzXUc91rgwYN9sRYPsjdU"
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
    "to": "ak_QnZTp2rcuY4zZDQGXuYaMbqPiekMCE2mSsZjNgo4YG6U6pBRP"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
    "data": {
      "message": {
        "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
        "from": "ak_zLYHnnooYQhNMVodsxoXSc5zEv2ouzXUc91rgwYN9sRYPsjdU",
        "info": "Hello back",
        "to": "ak_QnZTp2rcuY4zZDQGXuYaMbqPiekMCE2mSsZjNgo4YG6U6pBRP"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423321,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_QnZTp2rcuY4zZDQGXuYaMbqPiekMCE2mSsZjNgo4YG6U6pBRP",
      "ak_zLYHnnooYQhNMVodsxoXSc5zEv2ouzXUc91rgwYN9sRYPsjdU"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
  "id": -576460752303423321,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_QnZTp2rcuY4zZDQGXuYaMbqPiekMCE2mSsZjNgo4YG6U6pBRP",
      "balance": 69999999999999
    },
    {
      "account": "ak_zLYHnnooYQhNMVodsxoXSc5zEv2ouzXUc91rgwYN9sRYPsjdU",
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
    "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
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
    "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
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
    "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
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
    "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
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
    "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
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
    "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
    "data": {
      "state": "tx_+QENCwH4hLhANsyakvRTRugXc5sxKjtKyZJQr1LcCDwwMSAzgh6zXXzBgdLcwuszsSJbtKQOWCI09F4nGEj12cv4Lp/0JI9lDLhA+9vvoYcrQcVORsbTuRFGIoJfa2Vk9r1hKdJMbPeE8Y8ESdFNHkM6yHE77pMitW25ShtcW8Z8RsFHVw3idoHqAriD+IEyAaEBNgIGsjYE24Toi9tPG8ooIEeK6QkpF4b+yX/3licebvOGP6olImAAoQGCML8utnWYaW0hfrwnkwvarGSbivqtINkof+KHp2HPXYYkYTnKgAACCgCGEAZ510gAwKB5zpUH73/pj1rm1jNqpTmJs9qsRH8K0gRKxUBSyxtXHwEzB/xT"
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
    "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
    "data": {
      "state": "tx_+QENCwH4hLhANsyakvRTRugXc5sxKjtKyZJQr1LcCDwwMSAzgh6zXXzBgdLcwuszsSJbtKQOWCI09F4nGEj12cv4Lp/0JI9lDLhA+9vvoYcrQcVORsbTuRFGIoJfa2Vk9r1hKdJMbPeE8Y8ESdFNHkM6yHE77pMitW25ShtcW8Z8RsFHVw3idoHqAriD+IEyAaEBNgIGsjYE24Toi9tPG8ooIEeK6QkpF4b+yX/3licebvOGP6olImAAoQGCML8utnWYaW0hfrwnkwvarGSbivqtINkof+KHp2HPXYYkYTnKgAACCgCGEAZ510gAwKB5zpUH73/pj1rm1jNqpTmJs9qsRH8K0gRKxUBSyxtXHwEzB/xT"
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
    "from": "ak_zLYHnnooYQhNMVodsxoXSc5zEv2ouzXUc91rgwYN9sRYPsjdU",
    "to": "ak_QnZTp2rcuY4zZDQGXuYaMbqPiekMCE2mSsZjNgo4YG6U6pBRP"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBsJLIT8izJVsMVwbSQbcXGfzm7tcOFa9Ba2IGThCK2FDAqAt374f7J5JWseXt50WgOqGuYxMz4fo4ScrkxutcyTFQsO4cuk=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_zLYHnnooYQhNMVodsxoXSc5zEv2ouzXUc91rgwYN9sRYPsjdU",
          "op": "OffChainTransfer",
          "to": "ak_QnZTp2rcuY4zZDQGXuYaMbqPiekMCE2mSsZjNgo4YG6U6pBRP"
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
    "signed_tx": "tx_+JALAfhCuECd33QuhsVUofuv+71ww59qp94PIOf2M664i+jOOL1M/Wm4yv8J7xw4H7+B4rl2vjCVQAbBqZ+T2UubSQdhecYHuEj4RjkCoQbCSyE/IsyVbDFcG0kG3Fxn85u7XDhWvQWtiBk4QithQwKgLd++H+yeSVrHl7edFoDqhrmMTM+H6OEnK5MbrXMkxUIuYOzc"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
    "data": {
      "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
      "round": 1
    }
  },
  "version": 1
}
```

#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?port=14035&protocol=json-rpc&reconnect_tx=tx_%2BJ0LAfhCuECY3HW1%2BtkPlWzQoSC2aC3rZLn2KvXFkH%2BGtU6srivnJJjC0VtCrOmM4aThkZ%2FcCQrcdid0tUJ%2FmyB9hDPaStQJuFX4U4ICPwGhBsJLIT8izJVsMVwbSQbcXGfzm7tcOFa9Ba2IGThCK2FDAYlpbml0aWF0b3KhATYCBrI2BNuE6IvbTxvKKCBHiukJKReG%2Fsl%2F95YnHm7zDGhX1Q%3D%3D&role=initiator
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
    "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
    "data": {
      "signed_tx": "tx_+GQLAcC4X/hdNQGhBsJLIT8izJVsMVwbSQbcXGfzm7tcOFa9Ba2IGThCK2FDoQE2AgayNgTbhOiL208byiggR4rpCSkXhv7Jf/eWJx5u84Y2kdavv/+GG0jrV+ABAIYSMJzlQAACxxIJ/A==",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303423320,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEAhg2mIGYJcsvJdlHTh8MH8B/f2lSwmVswjAKZ3yG3LTvyQYIiaLy3atTdixJEiEKCJhZeMJf0K5e1tI/y7+aQAuF/4XTUBoQbCSyE/IsyVbDFcG0kG3Fxn85u7XDhWvQWtiBk4QithQ6EBNgIGsjYE24Toi9tPG8ooIEeK6QkpF4b+yX/3licebvOGNpHWr7//hhtI61fgAQCGEjCc5UAAAqK9arU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
  "id": -576460752303423320,
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
    "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
    "data": {
      "signed_tx": "tx_+KcLAfhCuEAhg2mIGYJcsvJdlHTh8MH8B/f2lSwmVswjAKZ3yG3LTvyQYIiaLy3atTdixJEiEKCJhZeMJf0K5e1tI/y7+aQAuF/4XTUBoQbCSyE/IsyVbDFcG0kG3Fxn85u7XDhWvQWtiBk4QithQ6EBNgIGsjYE24Toi9tPG8ooIEeK6QkpF4b+yX/3licebvOGNpHWr7//hhtI61fgAQCGEjCc5UAAAqK9arU=",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303423319,
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+OkLAfiEuEAhg2mIGYJcsvJdlHTh8MH8B/f2lSwmVswjAKZ3yG3LTvyQYIiaLy3atTdixJEiEKCJhZeMJf0K5e1tI/y7+aQAuEC5T07TNQa5rvnqQnjkPCmYWywLFY49zM3OUvmN1KIjdozjCuj+H+DAQic+yOPF61SyUVKkHp2mwWqwG3hQ0pUNuF/4XTUBoQbCSyE/IsyVbDFcG0kG3Fxn85u7XDhWvQWtiBk4QithQ6EBNgIGsjYE24Toi9tPG8ooIEeK6QkpF4b+yX/3licebvOGNpHWr7//hhtI61fgAQCGEjCc5UAAAqHEQWU="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
  "id": -576460752303423319,
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
    "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAhg2mIGYJcsvJdlHTh8MH8B/f2lSwmVswjAKZ3yG3LTvyQYIiaLy3atTdixJEiEKCJhZeMJf0K5e1tI/y7+aQAuEC5T07TNQa5rvnqQnjkPCmYWywLFY49zM3OUvmN1KIjdozjCuj+H+DAQic+yOPF61SyUVKkHp2mwWqwG3hQ0pUNuF/4XTUBoQbCSyE/IsyVbDFcG0kG3Fxn85u7XDhWvQWtiBk4QithQ6EBNgIGsjYE24Toi9tPG8ooIEeK6QkpF4b+yX/3licebvOGNpHWr7//hhtI61fgAQCGEjCc5UAAAqHEQWU=",
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
    "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
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
    "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
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
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
    "data": {
      "info": "close_mutual",
      "tx": "tx_+OkLAfiEuEAhg2mIGYJcsvJdlHTh8MH8B/f2lSwmVswjAKZ3yG3LTvyQYIiaLy3atTdixJEiEKCJhZeMJf0K5e1tI/y7+aQAuEC5T07TNQa5rvnqQnjkPCmYWywLFY49zM3OUvmN1KIjdozjCuj+H+DAQic+yOPF61SyUVKkHp2mwWqwG3hQ0pUNuF/4XTUBoQbCSyE/IsyVbDFcG0kG3Fxn85u7XDhWvQWtiBk4QithQ6EBNgIGsjYE24Toi9tPG8ooIEeK6QkpF4b+yX/3licebvOGNpHWr7//hhtI61fgAQCGEjCc5UAAAqHEQWU=",
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
    "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
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
    "channel_id": "ch_2UZy2t6CxsjTvtGCQYAs6RvzCoKFZvRpjzCdWwfccV1y4HbvfS",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```
