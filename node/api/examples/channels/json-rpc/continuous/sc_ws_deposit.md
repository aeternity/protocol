
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
  "method": "channels.deposit",
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
      "method": "channels.deposit",
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
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBkQy0hv+n+A9kW2IqZ8nYydqjg2eqpR1ZWgbTm86JPyHoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1gIAhg/AoHKQAKAJfKOkRYFmCfu9WWBbxU0n1wqMcA3FNf3vEd2/gK5qlQIy5lLp7w==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainDeposit"
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
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuECo9B73zCdn9BETKkb0zUQ5M6oc/+ih3DsGncK0aE6vBJhcjtL5cfKiYG2+jVNfshfKP7Q82muXz3tdNjHndZ8KuHT4cjMBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCMiWRi98="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
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
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "signed_tx": "tx_+LwLAfhCuECo9B73zCdn9BETKkb0zUQ5M6oc/+ih3DsGncK0aE6vBJhcjtL5cfKiYG2+jVNfshfKP7Q82muXz3tdNjHndZ8KuHT4cjMBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCMiWRi98=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainDeposit"
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
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBD9dw6TT36HobqnaAiYvQQcx3s0cUo35E/Hg/UTNiolV4w86dSrT8b/X0QbGnILxS1S6p66Z6gs1g0UDXRN08PuECo9B73zCdn9BETKkb0zUQ5M6oc/+ih3DsGncK0aE6vBJhcjtL5cfKiYG2+jVNfshfKP7Q82muXz3tdNjHndZ8KuHT4cjMBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCMpuINLI="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
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
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEBD9dw6TT36HobqnaAiYvQQcx3s0cUo35E/Hg/UTNiolV4w86dSrT8b/X0QbGnILxS1S6p66Z6gs1g0UDXRN08PuECo9B73zCdn9BETKkb0zUQ5M6oc/+ih3DsGncK0aE6vBJhcjtL5cfKiYG2+jVNfshfKP7Q82muXz3tdNjHndZ8KuHT4cjMBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCMpuINLI=",
      "type": "channel_deposit_tx"
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
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEBD9dw6TT36HobqnaAiYvQQcx3s0cUo35E/Hg/UTNiolV4w86dSrT8b/X0QbGnILxS1S6p66Z6gs1g0UDXRN08PuECo9B73zCdn9BETKkb0zUQ5M6oc/+ih3DsGncK0aE6vBJhcjtL5cfKiYG2+jVNfshfKP7Q82muXz3tdNjHndZ8KuHT4cjMBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCMpuINLI=",
      "type": "channel_deposit_tx"
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
      "tx": "tx_+P4LAfiEuEBD9dw6TT36HobqnaAiYvQQcx3s0cUo35E/Hg/UTNiolV4w86dSrT8b/X0QbGnILxS1S6p66Z6gs1g0UDXRN08PuECo9B73zCdn9BETKkb0zUQ5M6oc/+ih3DsGncK0aE6vBJhcjtL5cfKiYG2+jVNfshfKP7Q82muXz3tdNjHndZ8KuHT4cjMBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCMpuINLI=",
      "type": "channel_deposit_tx"
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
      "tx": "tx_+P4LAfiEuEBD9dw6TT36HobqnaAiYvQQcx3s0cUo35E/Hg/UTNiolV4w86dSrT8b/X0QbGnILxS1S6p66Z6gs1g0UDXRN08PuECo9B73zCdn9BETKkb0zUQ5M6oc/+ih3DsGncK0aE6vBJhcjtL5cfKiYG2+jVNfshfKP7Q82muXz3tdNjHndZ8KuHT4cjMBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCMpuINLI=",
      "type": "channel_deposit_tx"
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
      "event": "own_deposit_locked"
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
      "event": "own_deposit_locked"
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
      "event": "deposit_locked"
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
      "state": "tx_+P4LAfiEuEBD9dw6TT36HobqnaAiYvQQcx3s0cUo35E/Hg/UTNiolV4w86dSrT8b/X0QbGnILxS1S6p66Z6gs1g0UDXRN08PuECo9B73zCdn9BETKkb0zUQ5M6oc/+ih3DsGncK0aE6vBJhcjtL5cfKiYG2+jVNfshfKP7Q82muXz3tdNjHndZ8KuHT4cjMBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCMpuINLI="
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
      "event": "deposit_locked"
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
      "state": "tx_+P4LAfiEuEBD9dw6TT36HobqnaAiYvQQcx3s0cUo35E/Hg/UTNiolV4w86dSrT8b/X0QbGnILxS1S6p66Z6gs1g0UDXRN08PuECo9B73zCdn9BETKkb0zUQ5M6oc/+ih3DsGncK0aE6vBJhcjtL5cfKiYG2+jVNfshfKP7Q82muXz3tdNjHndZ8KuHT4cjMBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBscrVSspuuVCwwjdiOX3wyINws7Dt24bgUMf4XazPb9YCAIYPwKBykACgCXyjpEWBZgn7vVlgW8VNJ9cKjHANxTX97xHdv4CuapUCMpuINLI="
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
  "method": "channels.deposit",
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
      "method": "channels.deposit",
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
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBkQy0hv+n+A9kW2IqZ8nYydqjg2eqpR1ZWgbTm86JPyHoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8AIAhg/AoHKQAKBdYyosJiEVkIv3UfhREtMPbLmXGvLesTSuRCc8B8rvQgMT3AiWbA==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainDeposit"
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
  "id": -576460752303422839,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEBINTHOQ6z1tVqUvN0s/XFQp3ZmHOYz/Mro3crUbLYkER1H/2m9tVqIVJf6sHLvkcXyxUExnw4iuS0xLPU4658AuHT4cjMBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDE8EuGWw="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
  "id": -576460752303422839,
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
      "event": "deposit_created"
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEBINTHOQ6z1tVqUvN0s/XFQp3ZmHOYz/Mro3crUbLYkER1H/2m9tVqIVJf6sHLvkcXyxUExnw4iuS0xLPU4658AuHT4cjMBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDE8EuGWw=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainDeposit"
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
  "id": -576460752303422838,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEASygusuHQh8J2dm6nYDYaA982eTKWXp+dKAkhRec24F3POA8nFKt0hVP9Arp6m8MEkMsFadU1mKMiqqBC/VqYPuEBINTHOQ6z1tVqUvN0s/XFQp3ZmHOYz/Mro3crUbLYkER1H/2m9tVqIVJf6sHLvkcXyxUExnw4iuS0xLPU4658AuHT4cjMBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDE3rR7+M="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_X33JHzYXYMZ2QQruEc18hhrDPprgFtfGY1qt3D7uErSZkdX6J",
  "id": -576460752303422838,
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
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEASygusuHQh8J2dm6nYDYaA982eTKWXp+dKAkhRec24F3POA8nFKt0hVP9Arp6m8MEkMsFadU1mKMiqqBC/VqYPuEBINTHOQ6z1tVqUvN0s/XFQp3ZmHOYz/Mro3crUbLYkER1H/2m9tVqIVJf6sHLvkcXyxUExnw4iuS0xLPU4658AuHT4cjMBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDE3rR7+M=",
      "type": "channel_deposit_tx"
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
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEASygusuHQh8J2dm6nYDYaA982eTKWXp+dKAkhRec24F3POA8nFKt0hVP9Arp6m8MEkMsFadU1mKMiqqBC/VqYPuEBINTHOQ6z1tVqUvN0s/XFQp3ZmHOYz/Mro3crUbLYkER1H/2m9tVqIVJf6sHLvkcXyxUExnw4iuS0xLPU4658AuHT4cjMBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDE3rR7+M=",
      "type": "channel_deposit_tx"
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
      "tx": "tx_+P4LAfiEuEASygusuHQh8J2dm6nYDYaA982eTKWXp+dKAkhRec24F3POA8nFKt0hVP9Arp6m8MEkMsFadU1mKMiqqBC/VqYPuEBINTHOQ6z1tVqUvN0s/XFQp3ZmHOYz/Mro3crUbLYkER1H/2m9tVqIVJf6sHLvkcXyxUExnw4iuS0xLPU4658AuHT4cjMBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDE3rR7+M=",
      "type": "channel_deposit_tx"
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
      "tx": "tx_+P4LAfiEuEASygusuHQh8J2dm6nYDYaA982eTKWXp+dKAkhRec24F3POA8nFKt0hVP9Arp6m8MEkMsFadU1mKMiqqBC/VqYPuEBINTHOQ6z1tVqUvN0s/XFQp3ZmHOYz/Mro3crUbLYkER1H/2m9tVqIVJf6sHLvkcXyxUExnw4iuS0xLPU4658AuHT4cjMBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDE3rR7+M=",
      "type": "channel_deposit_tx"
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
      "event": "own_deposit_locked"
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
      "event": "own_deposit_locked"
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
      "event": "deposit_locked"
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
      "event": "deposit_locked"
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
      "state": "tx_+P4LAfiEuEASygusuHQh8J2dm6nYDYaA982eTKWXp+dKAkhRec24F3POA8nFKt0hVP9Arp6m8MEkMsFadU1mKMiqqBC/VqYPuEBINTHOQ6z1tVqUvN0s/XFQp3ZmHOYz/Mro3crUbLYkER1H/2m9tVqIVJf6sHLvkcXyxUExnw4iuS0xLPU4658AuHT4cjMBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDE3rR7+M="
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
      "state": "tx_+P4LAfiEuEASygusuHQh8J2dm6nYDYaA982eTKWXp+dKAkhRec24F3POA8nFKt0hVP9Arp6m8MEkMsFadU1mKMiqqBC/VqYPuEBINTHOQ6z1tVqUvN0s/XFQp3ZmHOYz/Mro3crUbLYkER1H/2m9tVqIVJf6sHLvkcXyxUExnw4iuS0xLPU4658AuHT4cjMBoQZEMtIb/p/gPZFtiKmfJ2Mnao4NnqqUdWVoG05vOiT8h6EBUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvACAIYPwKBykACgXWMqLCYhFZCL91H4URLTD2y5lxry3rE0rkQnPAfK70IDE3rR7+M="
    }
  },
  "version": 1
}
```
