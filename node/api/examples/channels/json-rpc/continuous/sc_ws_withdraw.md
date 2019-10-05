
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
  "method": "channels.withdraw",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBgaV+DmvL9j9vfVuI46KW8utRGzWgdP/ANr7y0NXKTUQoQHzTvBBlVUaCm6ty8Y9lmOmUfsY9o3BpXCITXq35It5lwIAhg/AoHKQAKCwXTqNfqVpnfqc4pdUAAAIsmqqldIFbwJC2QACA7JL7QQUdibFhw==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
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
  "id": -576460752303423327,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEBXceAGAoPAHFHSv3hjReT2xTkPpIwUYjjoig1EGw6CIzqAYN4kcuR7wDPyYp+gXZE3DbN0aIH43aVhXJWiOQUMuHT4cjQBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZcCAIYPwKBykACgsF06jX6laZ36nOKXVAAACLJqqpXSBW8CQtkAAgOyS+0EFEf3WMk="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
  "id": -576460752303423327,
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEBXceAGAoPAHFHSv3hjReT2xTkPpIwUYjjoig1EGw6CIzqAYN4kcuR7wDPyYp+gXZE3DbN0aIH43aVhXJWiOQUMuHT4cjQBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZcCAIYPwKBykACgsF06jX6laZ36nOKXVAAACLJqqpXSBW8CQtkAAgOyS+0EFEf3WMk=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2r9z9fw5UmPLcx6qVS3bAECZxvZqq5j9pzMve2hEgZsLoQ5nZR"
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
  "id": -576460752303423326,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEBXceAGAoPAHFHSv3hjReT2xTkPpIwUYjjoig1EGw6CIzqAYN4kcuR7wDPyYp+gXZE3DbN0aIH43aVhXJWiOQUMuECRlaljUP//tjImWOybsYSKQX6xLQaxxPpoL0aA+GdC4p2OnTRfsTcxopADaLgVOsAl4y68u/djXe2scUGE7rACuHT4cjQBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZcCAIYPwKBykACgsF06jX6laZ36nOKXVAAACLJqqpXSBW8CQtkAAgOyS+0EFDaxegs="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
  "id": -576460752303423326,
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
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEBXceAGAoPAHFHSv3hjReT2xTkPpIwUYjjoig1EGw6CIzqAYN4kcuR7wDPyYp+gXZE3DbN0aIH43aVhXJWiOQUMuECRlaljUP//tjImWOybsYSKQX6xLQaxxPpoL0aA+GdC4p2OnTRfsTcxopADaLgVOsAl4y68u/djXe2scUGE7rACuHT4cjQBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZcCAIYPwKBykACgsF06jX6laZ36nOKXVAAACLJqqpXSBW8CQtkAAgOyS+0EFDaxegs=",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEBXceAGAoPAHFHSv3hjReT2xTkPpIwUYjjoig1EGw6CIzqAYN4kcuR7wDPyYp+gXZE3DbN0aIH43aVhXJWiOQUMuECRlaljUP//tjImWOybsYSKQX6xLQaxxPpoL0aA+GdC4p2OnTRfsTcxopADaLgVOsAl4y68u/djXe2scUGE7rACuHT4cjQBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZcCAIYPwKBykACgsF06jX6laZ36nOKXVAAACLJqqpXSBW8CQtkAAgOyS+0EFDaxegs=",
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
      "tx": "tx_+P4LAfiEuEBXceAGAoPAHFHSv3hjReT2xTkPpIwUYjjoig1EGw6CIzqAYN4kcuR7wDPyYp+gXZE3DbN0aIH43aVhXJWiOQUMuECRlaljUP//tjImWOybsYSKQX6xLQaxxPpoL0aA+GdC4p2OnTRfsTcxopADaLgVOsAl4y68u/djXe2scUGE7rACuHT4cjQBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZcCAIYPwKBykACgsF06jX6laZ36nOKXVAAACLJqqpXSBW8CQtkAAgOyS+0EFDaxegs=",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEBXceAGAoPAHFHSv3hjReT2xTkPpIwUYjjoig1EGw6CIzqAYN4kcuR7wDPyYp+gXZE3DbN0aIH43aVhXJWiOQUMuECRlaljUP//tjImWOybsYSKQX6xLQaxxPpoL0aA+GdC4p2OnTRfsTcxopADaLgVOsAl4y68u/djXe2scUGE7rACuHT4cjQBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZcCAIYPwKBykACgsF06jX6laZ36nOKXVAAACLJqqpXSBW8CQtkAAgOyS+0EFDaxegs=",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "state": "tx_+P4LAfiEuEBXceAGAoPAHFHSv3hjReT2xTkPpIwUYjjoig1EGw6CIzqAYN4kcuR7wDPyYp+gXZE3DbN0aIH43aVhXJWiOQUMuECRlaljUP//tjImWOybsYSKQX6xLQaxxPpoL0aA+GdC4p2OnTRfsTcxopADaLgVOsAl4y68u/djXe2scUGE7rACuHT4cjQBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZcCAIYPwKBykACgsF06jX6laZ36nOKXVAAACLJqqpXSBW8CQtkAAgOyS+0EFDaxegs="
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
      "state": "tx_+P4LAfiEuEBXceAGAoPAHFHSv3hjReT2xTkPpIwUYjjoig1EGw6CIzqAYN4kcuR7wDPyYp+gXZE3DbN0aIH43aVhXJWiOQUMuECRlaljUP//tjImWOybsYSKQX6xLQaxxPpoL0aA+GdC4p2OnTRfsTcxopADaLgVOsAl4y68u/djXe2scUGE7rACuHT4cjQBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB807wQZVVGgpurcvGPZZjplH7GPaNwaVwiE16t+SLeZcCAIYPwKBykACgsF06jX6laZ36nOKXVAAACLJqqpXSBW8CQtkAAgOyS+0EFDaxegs="
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
  "method": "channels.withdraw",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "signed_tx": "tx_+HkLAcC4dPhyNAGhBgaV+DmvL9j9vfVuI46KW8utRGzWgdP/ANr7y0NXKTUQoQH3YzBc8zMZ2QhgwrJC/osmc70/iBKU+p5Fh1yzfiVgTQIAhg/AoHKQAKA149PdAPwzJwnnVXtTfWfJRb4RhbPMamPPXFVFdHrC7QUIPOq2/Q==",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
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
  "id": -576460752303423325,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEDLu5IO9ykqbEKDkfDz0RN4XtSqWerJOJrG202WSZDjoJE+Qflywxbv+zufJ127/ed9NtcLj8Smkz9KQzAYiHgGuHT4cjQBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE0CAIYPwKBykACgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0FCKPNgrs="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
  "id": -576460752303423325,
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEDLu5IO9ykqbEKDkfDz0RN4XtSqWerJOJrG202WSZDjoJE+Qflywxbv+zufJ127/ed9NtcLj8Smkz9KQzAYiHgGuHT4cjQBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE0CAIYPwKBykACgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0FCKPNgrs=",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2sxBUNz66J43vrydzUocL9j9o52UwD7cf58j9G468XupB8xRdT"
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
  "id": -576460752303423324,
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+P4LAfiEuEAqepCr8T5iv6O5iDsorsSmBjWfhLX7QFI0hWJ9asLFmby3YnAZSF9afwb0yxSTFzxG8QcwAPuzEtaXJB1HCqUMuEDLu5IO9ykqbEKDkfDz0RN4XtSqWerJOJrG202WSZDjoJE+Qflywxbv+zufJ127/ed9NtcLj8Smkz9KQzAYiHgGuHT4cjQBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE0CAIYPwKBykACgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0FCHGqD3I="
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
  "id": -576460752303423324,
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
      "info": "withdraw_created",
      "tx": "tx_+P4LAfiEuEAqepCr8T5iv6O5iDsorsSmBjWfhLX7QFI0hWJ9asLFmby3YnAZSF9afwb0yxSTFzxG8QcwAPuzEtaXJB1HCqUMuEDLu5IO9ykqbEKDkfDz0RN4XtSqWerJOJrG202WSZDjoJE+Qflywxbv+zufJ127/ed9NtcLj8Smkz9KQzAYiHgGuHT4cjQBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE0CAIYPwKBykACgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0FCHGqD3I=",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "info": "withdraw_signed",
      "tx": "tx_+P4LAfiEuEAqepCr8T5iv6O5iDsorsSmBjWfhLX7QFI0hWJ9asLFmby3YnAZSF9afwb0yxSTFzxG8QcwAPuzEtaXJB1HCqUMuEDLu5IO9ykqbEKDkfDz0RN4XtSqWerJOJrG202WSZDjoJE+Qflywxbv+zufJ127/ed9NtcLj8Smkz9KQzAYiHgGuHT4cjQBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE0CAIYPwKBykACgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0FCHGqD3I=",
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

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAqepCr8T5iv6O5iDsorsSmBjWfhLX7QFI0hWJ9asLFmby3YnAZSF9afwb0yxSTFzxG8QcwAPuzEtaXJB1HCqUMuEDLu5IO9ykqbEKDkfDz0RN4XtSqWerJOJrG202WSZDjoJE+Qflywxbv+zufJ127/ed9NtcLj8Smkz9KQzAYiHgGuHT4cjQBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE0CAIYPwKBykACgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0FCHGqD3I=",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+P4LAfiEuEAqepCr8T5iv6O5iDsorsSmBjWfhLX7QFI0hWJ9asLFmby3YnAZSF9afwb0yxSTFzxG8QcwAPuzEtaXJB1HCqUMuEDLu5IO9ykqbEKDkfDz0RN4XtSqWerJOJrG202WSZDjoJE+Qflywxbv+zufJ127/ed9NtcLj8Smkz9KQzAYiHgGuHT4cjQBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE0CAIYPwKBykACgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0FCHGqD3I=",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
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
    "channel_id": "ch_3uE6wZL6WDxoYwxNUYuZBk7QiuFHxVKnzmTwGy7UNmijGVauG",
    "data": {
      "state": "tx_+P4LAfiEuEAqepCr8T5iv6O5iDsorsSmBjWfhLX7QFI0hWJ9asLFmby3YnAZSF9afwb0yxSTFzxG8QcwAPuzEtaXJB1HCqUMuEDLu5IO9ykqbEKDkfDz0RN4XtSqWerJOJrG202WSZDjoJE+Qflywxbv+zufJ127/ed9NtcLj8Smkz9KQzAYiHgGuHT4cjQBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE0CAIYPwKBykACgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0FCHGqD3I="
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
      "state": "tx_+P4LAfiEuEAqepCr8T5iv6O5iDsorsSmBjWfhLX7QFI0hWJ9asLFmby3YnAZSF9afwb0yxSTFzxG8QcwAPuzEtaXJB1HCqUMuEDLu5IO9ykqbEKDkfDz0RN4XtSqWerJOJrG202WSZDjoJE+Qflywxbv+zufJ127/ed9NtcLj8Smkz9KQzAYiHgGuHT4cjQBoQYGlfg5ry/Y/b31biOOilvLrURs1oHT/wDa+8tDVyk1EKEB92MwXPMzGdkIYMKyQv6LJnO9P4gSlPqeRYdcs34lYE0CAIYPwKBykACgNePT3QD8MycJ51V7U31nyUW+EYWzzGpjz1xVRXR6wu0FCHGqD3I="
    }
  },
  "version": 1
}
```
