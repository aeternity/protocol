
#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 2,
    "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
    "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBr2j/XUBXzrH54aoG8gkW2gNjecvMWiOVu/WAdbrUsbLAqCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAqXxca4=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
          "to": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
        }
      ]
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBr2j/XUBXzrH54aoG8gkW2gNjecvMWiOVu/WAdbrUsbLAqAh5YXSCzjC3C5f2KaHrz5Qp6zPFnxOBCDOm/SZojmZpapI7+U=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
          "op": "OffChainTransfer",
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
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDfQ3DcxotWm9ckkomVsa8gcLWcfdexnACxgUMx9TePJqXmsubmuXkcT1F3WYjJmAzlNeWxje+re50VuOABgTcCuEj4RjkCoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGywKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKp+x2T"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 1
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 1
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 2,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBr2j/XUBXzrH54aoG8gkW2gNjecvMWiOVu/WAdbrUsbLAqCPVbQrAfYXrWTP0iwmtWIe9nj7Tuv+WHg7LyUfwRTSMYuvKo4=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
          "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
        }
      ]
    }
  },
  "version": 1
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBr2j/XUBXzrH54aoG8gkW2gNjecvMWiOVu/WAdbrUsbLAqBCVQ2rp/+y9mqPBXV6q9fbUVkXc5Dncw8tT8VJHJ/1g9zs9fg=",
      "updates": [
        {
          "amount": 2,
          "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
          "op": "OffChainTransfer",
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
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuED4Q546ljoeRyUd6VX1PoMzBAQ93KdM7rFrZdm0bPUVDFjtvDJCc6NyGJmK+2Ju7KkiIOenCPEMDnZbbZ0d2vQIuEj4RjkCoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGywKgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jHp+Cub"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 1
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
      "error_code": 2,
      "error_msg": "conflict",
      "round": 1
    }
  },
  "version": 1
}
```
