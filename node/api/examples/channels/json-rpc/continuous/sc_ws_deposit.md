
#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "Hello",
    "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "message": {
        "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
        "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
        "info": "Hello",
        "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
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
    "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "message": {
        "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
        "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
        "info": "Hello back",
        "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
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
  "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
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
    "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "message": {
        "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
        "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
        "info": "Hello",
        "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
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
    "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "message": {
        "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
        "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
        "info": "Hello back",
        "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBgaV+DmvL9j9vfVuI46KW8utRGzWgdP/ANr7y0NXKTUQoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5lwIAhg/AoHKQAKCJWCE8L58P8qHG/ELSA9ncy1iwWejkLf9YVluaPgjFMgIT4dOyIg==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
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
  "id": -576460752303423331,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEA7y0CiiyLCkoTwqCQgRV0SbFzjbkUD7tq/psWtD0Rj8f8CZOh9CR0bcDe3NzK8ti1c4/hMpOrIVnZ5epXdmKINuHT4cjMBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZcCAIYPwKBykACgiVghPC+fD/KhxvxC0gPZ3MtYsFno5C3/WFZbmj4IxTICE7VIK+g="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
  "id": -576460752303423331,
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEA7y0CiiyLCkoTwqCQgRV0SbFzjbkUD7tq/psWtD0Rj8f8CZOh9CR0bcDe3NzK8ti1c4/hMpOrIVnZ5epXdmKINuHT4cjMBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZcCAIYPwKBykACgiVghPC+fD/KhxvxC0gPZ3MtYsFno5C3/WFZbmj4IxTICE7VIK+g=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
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
  "id": -576460752303423330,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEA7y0CiiyLCkoTwqCQgRV0SbFzjbkUD7tq/psWtD0Rj8f8CZOh9CR0bcDe3NzK8ti1c4/hMpOrIVnZ5epXdmKINuEBgFHBxhm3QjYSGpvDgtwKU03yeplyQ53G0rA2kfjWaU1Q767EYj9Eo7RFIZsSit2axtiQmszvDl149Ct15b1cGuHT4cjMBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZcCAIYPwKBykACgiVghPC+fD/KhxvxC0gPZ3MtYsFno5C3/WFZbmj4IxTICE/3PAuY="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
  "id": -576460752303423330,
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEA7y0CiiyLCkoTwqCQgRV0SbFzjbkUD7tq/psWtD0Rj8f8CZOh9CR0bcDe3NzK8ti1c4/hMpOrIVnZ5epXdmKINuEBgFHBxhm3QjYSGpvDgtwKU03yeplyQ53G0rA2kfjWaU1Q767EYj9Eo7RFIZsSit2axtiQmszvDl149Ct15b1cGuHT4cjMBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZcCAIYPwKBykACgiVghPC+fD/KhxvxC0gPZ3MtYsFno5C3/WFZbmj4IxTICE/3PAuY=",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEA7y0CiiyLCkoTwqCQgRV0SbFzjbkUD7tq/psWtD0Rj8f8CZOh9CR0bcDe3NzK8ti1c4/hMpOrIVnZ5epXdmKINuEBgFHBxhm3QjYSGpvDgtwKU03yeplyQ53G0rA2kfjWaU1Q767EYj9Eo7RFIZsSit2axtiQmszvDl149Ct15b1cGuHT4cjMBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZcCAIYPwKBykACgiVghPC+fD/KhxvxC0gPZ3MtYsFno5C3/WFZbmj4IxTICE/3PAuY=",
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
    "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "message": {
        "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
        "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
        "info": "Hello",
        "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
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
    "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "message": {
        "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
        "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
        "info": "Hello back",
        "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
      }
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEA7y0CiiyLCkoTwqCQgRV0SbFzjbkUD7tq/psWtD0Rj8f8CZOh9CR0bcDe3NzK8ti1c4/hMpOrIVnZ5epXdmKINuEBgFHBxhm3QjYSGpvDgtwKU03yeplyQ53G0rA2kfjWaU1Q767EYj9Eo7RFIZsSit2axtiQmszvDl149Ct15b1cGuHT4cjMBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZcCAIYPwKBykACgiVghPC+fD/KhxvxC0gPZ3MtYsFno5C3/WFZbmj4IxTICE/3PAuY=",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEA7y0CiiyLCkoTwqCQgRV0SbFzjbkUD7tq/psWtD0Rj8f8CZOh9CR0bcDe3NzK8ti1c4/hMpOrIVnZ5epXdmKINuEBgFHBxhm3QjYSGpvDgtwKU03yeplyQ53G0rA2kfjWaU1Q767EYj9Eo7RFIZsSit2axtiQmszvDl149Ct15b1cGuHT4cjMBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZcCAIYPwKBykACgiVghPC+fD/KhxvxC0gPZ3MtYsFno5C3/WFZbmj4IxTICE/3PAuY=",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "state": "tx_+P4LAfiEuEA7y0CiiyLCkoTwqCQgRV0SbFzjbkUD7tq/psWtD0Rj8f8CZOh9CR0bcDe3NzK8ti1c4/hMpOrIVnZ5epXdmKINuEBgFHBxhm3QjYSGpvDgtwKU03yeplyQ53G0rA2kfjWaU1Q767EYj9Eo7RFIZsSit2axtiQmszvDl149Ct15b1cGuHT4cjMBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZcCAIYPwKBykACgiVghPC+fD/KhxvxC0gPZ3MtYsFno5C3/WFZbmj4IxTICE/3PAuY="
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "state": "tx_+P4LAfiEuEA7y0CiiyLCkoTwqCQgRV0SbFzjbkUD7tq/psWtD0Rj8f8CZOh9CR0bcDe3NzK8ti1c4/hMpOrIVnZ5epXdmKINuEBgFHBxhm3QjYSGpvDgtwKU03yeplyQ53G0rA2kfjWaU1Q767EYj9Eo7RFIZsSit2axtiQmszvDl149Ct15b1cGuHT4cjMBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZcCAIYPwKBykACgiVghPC+fD/KhxvxC0gPZ3MtYsFno5C3/WFZbmj4IxTICE/3PAuY="
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
    "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "message": {
        "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
        "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
        "info": "Hello",
        "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
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
    "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "message": {
        "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
        "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
        "info": "Hello back",
        "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
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
  "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
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
    "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "message": {
        "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
        "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
        "info": "Hello",
        "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
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
    "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "message": {
        "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
        "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
        "info": "Hello back",
        "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyMwGhBgaV+DmvL9j9vfVuI46KW8utRGzWgdP/ANr7y0NXKTUQoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTQIAhg/AoHKQAKC8Oyn9WxrGQnpO+MoTLzNS/KqMjUYCJqGcphukQDrxFwMHxG82gQ==",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
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
  "id": -576460752303423329,
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEAHXiyE1gR8ddoXH6CTFCGCa6RU9VJOTawKOnrCdguqQlLlavgvJbdZ3zVa1wYRYmhejy6tMs8qyhDyq3QrSwEDuHT4cjMBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE0CAIYPwKBykACgvDsp/VsaxkJ6TvjKEy8zUvyqjI1GAiahnKYbpEA68RcDB1vvFOw="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
  "id": -576460752303423329,
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEAHXiyE1gR8ddoXH6CTFCGCa6RU9VJOTawKOnrCdguqQlLlavgvJbdZ3zVa1wYRYmhejy6tMs8qyhDyq3QrSwEDuHT4cjMBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE0CAIYPwKBykACgvDsp/VsaxkJ6TvjKEy8zUvyqjI1GAiahnKYbpEA68RcDB1vvFOw=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
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
  "id": -576460752303423328,
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEAHXiyE1gR8ddoXH6CTFCGCa6RU9VJOTawKOnrCdguqQlLlavgvJbdZ3zVa1wYRYmhejy6tMs8qyhDyq3QrSwEDuECj98OR4QCxDKLjlmpJHpfmd6bnwz5YGSzeDguEICNmBrRS4nlVt8Y77u4AmIn8L6DgQvPf/M2BFjgW+v2mmaIPuHT4cjMBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE0CAIYPwKBykACgvDsp/VsaxkJ6TvjKEy8zUvyqjI1GAiahnKYbpEA68RcDB0beTCg="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
  "id": -576460752303423328,
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "info": "deposit_created",
      "tx": "tx_+P4LAfiEuEAHXiyE1gR8ddoXH6CTFCGCa6RU9VJOTawKOnrCdguqQlLlavgvJbdZ3zVa1wYRYmhejy6tMs8qyhDyq3QrSwEDuECj98OR4QCxDKLjlmpJHpfmd6bnwz5YGSzeDguEICNmBrRS4nlVt8Y77u4AmIn8L6DgQvPf/M2BFjgW+v2mmaIPuHT4cjMBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE0CAIYPwKBykACgvDsp/VsaxkJ6TvjKEy8zUvyqjI1GAiahnKYbpEA68RcDB0beTCg=",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "info": "deposit_signed",
      "tx": "tx_+P4LAfiEuEAHXiyE1gR8ddoXH6CTFCGCa6RU9VJOTawKOnrCdguqQlLlavgvJbdZ3zVa1wYRYmhejy6tMs8qyhDyq3QrSwEDuECj98OR4QCxDKLjlmpJHpfmd6bnwz5YGSzeDguEICNmBrRS4nlVt8Y77u4AmIn8L6DgQvPf/M2BFjgW+v2mmaIPuHT4cjMBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE0CAIYPwKBykACgvDsp/VsaxkJ6TvjKEy8zUvyqjI1GAiahnKYbpEA68RcDB0beTCg=",
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
    "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "message": {
        "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
        "from": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT",
        "info": "Hello",
        "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
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
    "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "message": {
        "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
        "from": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR",
        "info": "Hello back",
        "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAHXiyE1gR8ddoXH6CTFCGCa6RU9VJOTawKOnrCdguqQlLlavgvJbdZ3zVa1wYRYmhejy6tMs8qyhDyq3QrSwEDuECj98OR4QCxDKLjlmpJHpfmd6bnwz5YGSzeDguEICNmBrRS4nlVt8Y77u4AmIn8L6DgQvPf/M2BFjgW+v2mmaIPuHT4cjMBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE0CAIYPwKBykACgvDsp/VsaxkJ6TvjKEy8zUvyqjI1GAiahnKYbpEA68RcDB0beTCg=",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAHXiyE1gR8ddoXH6CTFCGCa6RU9VJOTawKOnrCdguqQlLlavgvJbdZ3zVa1wYRYmhejy6tMs8qyhDyq3QrSwEDuECj98OR4QCxDKLjlmpJHpfmd6bnwz5YGSzeDguEICNmBrRS4nlVt8Y77u4AmIn8L6DgQvPf/M2BFjgW+v2mmaIPuHT4cjMBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE0CAIYPwKBykACgvDsp/VsaxkJ6TvjKEy8zUvyqjI1GAiahnKYbpEA68RcDB0beTCg=",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "event": "own_deposit_locked"
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
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
  "method": "channels.info",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "state": "tx_+P4LAfiEuEAHXiyE1gR8ddoXH6CTFCGCa6RU9VJOTawKOnrCdguqQlLlavgvJbdZ3zVa1wYRYmhejy6tMs8qyhDyq3QrSwEDuECj98OR4QCxDKLjlmpJHpfmd6bnwz5YGSzeDguEICNmBrRS4nlVt8Y77u4AmIn8L6DgQvPf/M2BFjgW+v2mmaIPuHT4cjMBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE0CAIYPwKBykACgvDsp/VsaxkJ6TvjKEy8zUvyqjI1GAiahnKYbpEA68RcDB0beTCg="
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "state": "tx_+P4LAfiEuEAHXiyE1gR8ddoXH6CTFCGCa6RU9VJOTawKOnrCdguqQlLlavgvJbdZ3zVa1wYRYmhejy6tMs8qyhDyq3QrSwEDuECj98OR4QCxDKLjlmpJHpfmd6bnwz5YGSzeDguEICNmBrRS4nlVt8Y77u4AmIn8L6DgQvPf/M2BFjgW+v2mmaIPuHT4cjMBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE0CAIYPwKBykACgvDsp/VsaxkJ6TvjKEy8zUvyqjI1GAiahnKYbpEA68RcDB0beTCg="
    }
  },
  "version": 1
}
```
