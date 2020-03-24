
#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "message": {
        "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "message": {
        "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello back",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": "2"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.withdraw",
      "params": {
        "amount": "2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "message": {
        "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "message": {
        "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello back",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBkQy0hv+n+A9kW2IqZ8nYydqjg2eqpR1ZWgbTm86JPyHoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gIAhg/AoHKQAKDqgdNkuhddveVDE/es1N/fevZuJ9NTBtOGxk/KimI/YwQzH+DEbA==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "id": -576460752303422837,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEAa9fNEEPKK3pfO7UBAM4lNtmdJTQgYW0as74lMrd0oBli241AT2e8cskV/xlrHT8Q8hMsao9GuQoM/IiIRSNoKuHT4cjQBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACg6oHTZLoXXb3lQxP3rNTf33r2bifTUwbThsZPyopiP2MEMwlnnvU="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
  "id": -576460752303422837,
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEAa9fNEEPKK3pfO7UBAM4lNtmdJTQgYW0as74lMrd0oBli241AT2e8cskV/xlrHT8Q8hMsao9GuQoM/IiIRSNoKuHT4cjQBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACg6oHTZLoXXb3lQxP3rNTf33r2bifTUwbThsZPyopiP2MEMwlnnvU=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
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
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEAFFHY8La7wdpYgegWTFMEkE+iaJ+6qO8ursmLTRcbEVoPXWF1Ga5Zw0XhcRgO9gJGzfj/1ZwnLxk1YMcOILpEOuEAa9fNEEPKK3pfO7UBAM4lNtmdJTQgYW0as74lMrd0oBli241AT2e8cskV/xlrHT8Q8hMsao9GuQoM/IiIRSNoKuHT4cjQBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACg6oHTZLoXXb3lQxP3rNTf33r2bifTUwbThsZPyopiP2MEMzYc8ow="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
  "id": -576460752303422836,
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEAFFHY8La7wdpYgegWTFMEkE+iaJ+6qO8ursmLTRcbEVoPXWF1Ga5Zw0XhcRgO9gJGzfj/1ZwnLxk1YMcOILpEOuEAa9fNEEPKK3pfO7UBAM4lNtmdJTQgYW0as74lMrd0oBli241AT2e8cskV/xlrHT8Q8hMsao9GuQoM/IiIRSNoKuHT4cjQBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACg6oHTZLoXXb3lQxP3rNTf33r2bifTUwbThsZPyopiP2MEMzYc8ow=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEAFFHY8La7wdpYgegWTFMEkE+iaJ+6qO8ursmLTRcbEVoPXWF1Ga5Zw0XhcRgO9gJGzfj/1ZwnLxk1YMcOILpEOuEAa9fNEEPKK3pfO7UBAM4lNtmdJTQgYW0as74lMrd0oBli241AT2e8cskV/xlrHT8Q8hMsao9GuQoM/IiIRSNoKuHT4cjQBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACg6oHTZLoXXb3lQxP3rNTf33r2bifTUwbThsZPyopiP2MEMzYc8ow=",
      "type": "channel_withdraw_tx"
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
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "message": {
        "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "message": {
        "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello back",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAFFHY8La7wdpYgegWTFMEkE+iaJ+6qO8ursmLTRcbEVoPXWF1Ga5Zw0XhcRgO9gJGzfj/1ZwnLxk1YMcOILpEOuEAa9fNEEPKK3pfO7UBAM4lNtmdJTQgYW0as74lMrd0oBli241AT2e8cskV/xlrHT8Q8hMsao9GuQoM/IiIRSNoKuHT4cjQBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACg6oHTZLoXXb3lQxP3rNTf33r2bifTUwbThsZPyopiP2MEMzYc8ow=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAFFHY8La7wdpYgegWTFMEkE+iaJ+6qO8ursmLTRcbEVoPXWF1Ga5Zw0XhcRgO9gJGzfj/1ZwnLxk1YMcOILpEOuEAa9fNEEPKK3pfO7UBAM4lNtmdJTQgYW0as74lMrd0oBli241AT2e8cskV/xlrHT8Q8hMsao9GuQoM/IiIRSNoKuHT4cjQBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACg6oHTZLoXXb3lQxP3rNTf33r2bifTUwbThsZPyopiP2MEMzYc8ow=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "state": "tx_+P4LAfiEuEAFFHY8La7wdpYgegWTFMEkE+iaJ+6qO8ursmLTRcbEVoPXWF1Ga5Zw0XhcRgO9gJGzfj/1ZwnLxk1YMcOILpEOuEAa9fNEEPKK3pfO7UBAM4lNtmdJTQgYW0as74lMrd0oBli241AT2e8cskV/xlrHT8Q8hMsao9GuQoM/IiIRSNoKuHT4cjQBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACg6oHTZLoXXb3lQxP3rNTf33r2bifTUwbThsZPyopiP2MEMzYc8ow="
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "state": "tx_+P4LAfiEuEAFFHY8La7wdpYgegWTFMEkE+iaJ+6qO8ursmLTRcbEVoPXWF1Ga5Zw0XhcRgO9gJGzfj/1ZwnLxk1YMcOILpEOuEAa9fNEEPKK3pfO7UBAM4lNtmdJTQgYW0as74lMrd0oBli241AT2e8cskV/xlrHT8Q8hMsao9GuQoM/IiIRSNoKuHT4cjQBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACg6oHTZLoXXb3lQxP3rNTf33r2bifTUwbThsZPyopiP2MEMzYc8ow="
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
    "info": "Hello",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "message": {
        "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
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
    "info": "Hello back",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "message": {
        "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello back",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "method": "channels.withdraw",
  "params": {
    "amount": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1008,
        "message": "Not a number"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.withdraw",
      "params": {
        "amount": "2"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "message": {
        "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
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
    "info": "Hello back",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "message": {
        "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello back",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBkQy0hv+n+A9kW2IqZ8nYydqjg2eqpR1ZWgbTm86JPyHoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AIAhg/AoHKQAKAkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOCwUU+iee8g==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "id": -576460752303422835,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuECWNdR445YPp9DjzmRXkS+5BvDpKNgNHB6k4MgYqUHTOIuycGgAjWbkFRbJWBMMVhCpsQ7+rrT0PeSaVqnMsRIPuHT4cjQBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsFFFPO+Hw="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "event": "withdraw_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "signed_tx": "tx_+LwLAfhCuECWNdR445YPp9DjzmRXkS+5BvDpKNgNHB6k4MgYqUHTOIuycGgAjWbkFRbJWBMMVhCpsQ7+rrT0PeSaVqnMsRIPuHT4cjQBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsFFFPO+Hw=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
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
  "id": -576460752303422834,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuECWNdR445YPp9DjzmRXkS+5BvDpKNgNHB6k4MgYqUHTOIuycGgAjWbkFRbJWBMMVhCpsQ7+rrT0PeSaVqnMsRIPuEDqGrJ3N0VyGLop98/xinv9cuEXq/5Z3uienRx3fd9dvOtvbRjweYtuU9bshofOtT4xM5qyD0TIn21psBl1aHsCuHT4cjQBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsFFDrvPt0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
  "id": -576460752303422834,
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuECWNdR445YPp9DjzmRXkS+5BvDpKNgNHB6k4MgYqUHTOIuycGgAjWbkFRbJWBMMVhCpsQ7+rrT0PeSaVqnMsRIPuEDqGrJ3N0VyGLop98/xinv9cuEXq/5Z3uienRx3fd9dvOtvbRjweYtuU9bshofOtT4xM5qyD0TIn21psBl1aHsCuHT4cjQBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsFFDrvPt0=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuECWNdR445YPp9DjzmRXkS+5BvDpKNgNHB6k4MgYqUHTOIuycGgAjWbkFRbJWBMMVhCpsQ7+rrT0PeSaVqnMsRIPuEDqGrJ3N0VyGLop98/xinv9cuEXq/5Z3uienRx3fd9dvOtvbRjweYtuU9bshofOtT4xM5qyD0TIn21psBl1aHsCuHT4cjQBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsFFDrvPt0=",
      "type": "channel_withdraw_tx"
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
    "info": "Hello",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "message": {
        "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
        "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
        "info": "Hello",
        "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
      }
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
    "info": "Hello back",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "message": {
        "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
        "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
        "info": "Hello back",
        "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
      }
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECWNdR445YPp9DjzmRXkS+5BvDpKNgNHB6k4MgYqUHTOIuycGgAjWbkFRbJWBMMVhCpsQ7+rrT0PeSaVqnMsRIPuEDqGrJ3N0VyGLop98/xinv9cuEXq/5Z3uienRx3fd9dvOtvbRjweYtuU9bshofOtT4xM5qyD0TIn21psBl1aHsCuHT4cjQBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsFFDrvPt0=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECWNdR445YPp9DjzmRXkS+5BvDpKNgNHB6k4MgYqUHTOIuycGgAjWbkFRbJWBMMVhCpsQ7+rrT0PeSaVqnMsRIPuEDqGrJ3N0VyGLop98/xinv9cuEXq/5Z3uienRx3fd9dvOtvbRjweYtuU9bshofOtT4xM5qyD0TIn21psBl1aHsCuHT4cjQBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsFFDrvPt0=",
      "type": "channel_withdraw_tx"
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "event": "withdraw_locked"
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "state": "tx_+P4LAfiEuECWNdR445YPp9DjzmRXkS+5BvDpKNgNHB6k4MgYqUHTOIuycGgAjWbkFRbJWBMMVhCpsQ7+rrT0PeSaVqnMsRIPuEDqGrJ3N0VyGLop98/xinv9cuEXq/5Z3uienRx3fd9dvOtvbRjweYtuU9bshofOtT4xM5qyD0TIn21psBl1aHsCuHT4cjQBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsFFDrvPt0="
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "state": "tx_+P4LAfiEuECWNdR445YPp9DjzmRXkS+5BvDpKNgNHB6k4MgYqUHTOIuycGgAjWbkFRbJWBMMVhCpsQ7+rrT0PeSaVqnMsRIPuEDqGrJ3N0VyGLop98/xinv9cuEXq/5Z3uienRx3fd9dvOtvbRjweYtuU9bshofOtT4xM5qyD0TIn21psBl1aHsCuHT4cjQBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsFFDrvPt0="
    }
  },
  "version": 1
}
```
