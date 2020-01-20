
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
  "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBhZew5Ookmw3Bs/7SN7rXCFZzENKi5rQeMppkg2nWdVaoQHFuOyHaFZbIrWNtYfyrvdxCqjuxxEHg9OIAavLpCy79AIAhg/AoHKQAKCrxDtQzyez86BLbjvUuOUeV9h2xXHFJA9GSc2nrWsrIQQbwB18cQ==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303423150,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEDiWZRCw7LiQhFA2jxi0J0yOcqRqn+216+w/I24QVyqzp/yV+hqKP4HuCcA+B5Byb345yvDQ4wPNLSRXbzE9vINuHT4cjQBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgq8Q7UM8ns/OgS2471LjlHlfYdsVxxSQPRknNp61rKyEEG7+Mgm0="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
  "id": -576460752303423150,
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEDiWZRCw7LiQhFA2jxi0J0yOcqRqn+216+w/I24QVyqzp/yV+hqKP4HuCcA+B5Byb345yvDQ4wPNLSRXbzE9vINuHT4cjQBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgq8Q7UM8ns/OgS2471LjlHlfYdsVxxSQPRknNp61rKyEEG7+Mgm0=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303423149,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEDiWZRCw7LiQhFA2jxi0J0yOcqRqn+216+w/I24QVyqzp/yV+hqKP4HuCcA+B5Byb345yvDQ4wPNLSRXbzE9vINuED7HoGoU2uhBffPzGl8XNtzCkagJo8a74oDs11Xh8HRe3A7VFMnpyqDRqRunmD4YvgLGDWjkxx2MvBTqirSVFMEuHT4cjQBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgq8Q7UM8ns/OgS2471LjlHlfYdsVxxSQPRknNp61rKyEEG40UpfY="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
  "id": -576460752303423149,
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEDiWZRCw7LiQhFA2jxi0J0yOcqRqn+216+w/I24QVyqzp/yV+hqKP4HuCcA+B5Byb345yvDQ4wPNLSRXbzE9vINuED7HoGoU2uhBffPzGl8XNtzCkagJo8a74oDs11Xh8HRe3A7VFMnpyqDRqRunmD4YvgLGDWjkxx2MvBTqirSVFMEuHT4cjQBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgq8Q7UM8ns/OgS2471LjlHlfYdsVxxSQPRknNp61rKyEEG40UpfY=",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEDiWZRCw7LiQhFA2jxi0J0yOcqRqn+216+w/I24QVyqzp/yV+hqKP4HuCcA+B5Byb345yvDQ4wPNLSRXbzE9vINuED7HoGoU2uhBffPzGl8XNtzCkagJo8a74oDs11Xh8HRe3A7VFMnpyqDRqRunmD4YvgLGDWjkxx2MvBTqirSVFMEuHT4cjQBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgq8Q7UM8ns/OgS2471LjlHlfYdsVxxSQPRknNp61rKyEEG40UpfY=",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "info": "Hello back",
        "to": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB"
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEDiWZRCw7LiQhFA2jxi0J0yOcqRqn+216+w/I24QVyqzp/yV+hqKP4HuCcA+B5Byb345yvDQ4wPNLSRXbzE9vINuED7HoGoU2uhBffPzGl8XNtzCkagJo8a74oDs11Xh8HRe3A7VFMnpyqDRqRunmD4YvgLGDWjkxx2MvBTqirSVFMEuHT4cjQBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgq8Q7UM8ns/OgS2471LjlHlfYdsVxxSQPRknNp61rKyEEG40UpfY=",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEDiWZRCw7LiQhFA2jxi0J0yOcqRqn+216+w/I24QVyqzp/yV+hqKP4HuCcA+B5Byb345yvDQ4wPNLSRXbzE9vINuED7HoGoU2uhBffPzGl8XNtzCkagJo8a74oDs11Xh8HRe3A7VFMnpyqDRqRunmD4YvgLGDWjkxx2MvBTqirSVFMEuHT4cjQBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgq8Q7UM8ns/OgS2471LjlHlfYdsVxxSQPRknNp61rKyEEG40UpfY=",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "event": "own_withdraw_locked"
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "state": "tx_+P4LAfiEuEDiWZRCw7LiQhFA2jxi0J0yOcqRqn+216+w/I24QVyqzp/yV+hqKP4HuCcA+B5Byb345yvDQ4wPNLSRXbzE9vINuED7HoGoU2uhBffPzGl8XNtzCkagJo8a74oDs11Xh8HRe3A7VFMnpyqDRqRunmD4YvgLGDWjkxx2MvBTqirSVFMEuHT4cjQBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgq8Q7UM8ns/OgS2471LjlHlfYdsVxxSQPRknNp61rKyEEG40UpfY="
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "state": "tx_+P4LAfiEuEDiWZRCw7LiQhFA2jxi0J0yOcqRqn+216+w/I24QVyqzp/yV+hqKP4HuCcA+B5Byb345yvDQ4wPNLSRXbzE9vINuED7HoGoU2uhBffPzGl8XNtzCkagJo8a74oDs11Xh8HRe3A7VFMnpyqDRqRunmD4YvgLGDWjkxx2MvBTqirSVFMEuHT4cjQBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEBxbjsh2hWWyK1jbWH8q73cQqo7scRB4PTiAGry6Qsu/QCAIYPwKBykACgq8Q7UM8ns/OgS2471LjlHlfYdsVxxSQPRknNp61rKyEEG40UpfY="
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "info": "Hello back",
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
  "method": "channels.withdraw",
  "params": {
    "amount": "2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "info": "Hello back",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBhZew5Ookmw3Bs/7SN7rXCFZzENKi5rQeMppkg2nWdVaoQHRNm8xdRGfaP8NRS1ZqdGmmsRo8FaC1wW2VWFid7ROEAIAhg/AoHKQAKAWT0e4n3cUkZ17YXJbeFdi2G+JNZ1+3HKCYNWL2rDf7gUKwdKxBw==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303423148,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEDXtviFsEBgO3k4nY+hYVQL1TG5qvcEu+aOmSBOcuQNo5w1zALh8fr3qeXAc/rAcq9mubI4csjCbbbLOm1ScdsIuHT4cjQBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4FCjXhEEc="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
  "id": -576460752303423148,
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEDXtviFsEBgO3k4nY+hYVQL1TG5qvcEu+aOmSBOcuQNo5w1zALh8fr3qeXAc/rAcq9mubI4csjCbbbLOm1ScdsIuHT4cjQBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4FCjXhEEc=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
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
  "id": -576460752303423147,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuECqvJkdn/EI9M2RE/KfcNalqoIQu6D45sKD944J0JJ9IXfaROYOHhIBaEse52ryNWucIFDqH7sBmGN5eDXKH2MIuEDXtviFsEBgO3k4nY+hYVQL1TG5qvcEu+aOmSBOcuQNo5w1zALh8fr3qeXAc/rAcq9mubI4csjCbbbLOm1ScdsIuHT4cjQBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4FCi6MzqY="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
  "id": -576460752303423147,
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuECqvJkdn/EI9M2RE/KfcNalqoIQu6D45sKD944J0JJ9IXfaROYOHhIBaEse52ryNWucIFDqH7sBmGN5eDXKH2MIuEDXtviFsEBgO3k4nY+hYVQL1TG5qvcEu+aOmSBOcuQNo5w1zALh8fr3qeXAc/rAcq9mubI4csjCbbbLOm1ScdsIuHT4cjQBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4FCi6MzqY=",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuECqvJkdn/EI9M2RE/KfcNalqoIQu6D45sKD944J0JJ9IXfaROYOHhIBaEse52ryNWucIFDqH7sBmGN5eDXKH2MIuEDXtviFsEBgO3k4nY+hYVQL1TG5qvcEu+aOmSBOcuQNo5w1zALh8fr3qeXAc/rAcq9mubI4csjCbbbLOm1ScdsIuHT4cjQBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4FCi6MzqY=",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
        "from": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub",
        "info": "Hello",
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
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello back",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "message": {
        "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
        "from": "ak_2W5Z2uyH8s1smQo2ZxgB8V3hH9VCJkXmGCaATmtRQjJUbQ8MNB",
        "info": "Hello back",
        "to": "ak_2b94FCuxybDzRCpVHVCKusRQerR81duJ7ryHDfZdPLAW8YRiub"
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECqvJkdn/EI9M2RE/KfcNalqoIQu6D45sKD944J0JJ9IXfaROYOHhIBaEse52ryNWucIFDqH7sBmGN5eDXKH2MIuEDXtviFsEBgO3k4nY+hYVQL1TG5qvcEu+aOmSBOcuQNo5w1zALh8fr3qeXAc/rAcq9mubI4csjCbbbLOm1ScdsIuHT4cjQBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4FCi6MzqY=",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuECqvJkdn/EI9M2RE/KfcNalqoIQu6D45sKD944J0JJ9IXfaROYOHhIBaEse52ryNWucIFDqH7sBmGN5eDXKH2MIuEDXtviFsEBgO3k4nY+hYVQL1TG5qvcEu+aOmSBOcuQNo5w1zALh8fr3qeXAc/rAcq9mubI4csjCbbbLOm1ScdsIuHT4cjQBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4FCi6MzqY=",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
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
  "method": "channels.update",
  "params": {
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "state": "tx_+P4LAfiEuECqvJkdn/EI9M2RE/KfcNalqoIQu6D45sKD944J0JJ9IXfaROYOHhIBaEse52ryNWucIFDqH7sBmGN5eDXKH2MIuEDXtviFsEBgO3k4nY+hYVQL1TG5qvcEu+aOmSBOcuQNo5w1zALh8fr3qeXAc/rAcq9mubI4csjCbbbLOm1ScdsIuHT4cjQBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4FCi6MzqY="
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
    "channel_id": "ch_ArR8UHQFmJ1GkJGk5BTWfKcZnMdeSyEMx2V9qyXJq2sk8QMBh",
    "data": {
      "state": "tx_+P4LAfiEuECqvJkdn/EI9M2RE/KfcNalqoIQu6D45sKD944J0JJ9IXfaROYOHhIBaEse52ryNWucIFDqH7sBmGN5eDXKH2MIuEDXtviFsEBgO3k4nY+hYVQL1TG5qvcEu+aOmSBOcuQNo5w1zALh8fr3qeXAc/rAcq9mubI4csjCbbbLOm1ScdsIuHT4cjQBoQYWXsOTqJJsNwbP+0je61whWcxDSoua0HjKaZINp1nVWqEB0TZvMXURn2j/DUUtWanRpprEaPBWgtcFtlVhYne0ThACAIYPwKBykACgFk9HuJ93FJGde2FyW3hXYthviTWdftxygmDVi9qw3+4FCi6MzqY="
    }
  },
  "version": 1
}
```
