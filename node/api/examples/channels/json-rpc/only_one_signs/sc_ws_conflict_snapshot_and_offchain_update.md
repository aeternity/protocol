
#### initiator ---> node
```javascript
{
  "id": -576460752303421963,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
  "id": -576460752303421963,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999999
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
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

#### initiator ---> node
```javascript
{
  "id": -576460752303421962,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDfQ3DcxotWm9ckkomVsa8gcLWcfdexnACxgUMx9TePJqXmsubmuXkcT1F3WYjJmAzlNeWxje+re50VuOABgTcCuEj4RjkCoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGywKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKp+x2T"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
  "id": -576460752303421962,
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
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
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
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "signed_tx": "tx_+JALAfhCuEDfQ3DcxotWm9ckkomVsa8gcLWcfdexnACxgUMx9TePJqXmsubmuXkcT1F3WYjJmAzlNeWxje+re50VuOABgTcCuEj4RjkCoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGywKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgKp+x2T",
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

#### responder ---> node
```javascript
{
  "id": -576460752303421961,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBVnRos+OaB/7YVSDFasV08mn2vLF5tbsTH51DhWGeoQKx/WroePgcHlJaN/IRihmkhsMrfyvlQhwAJHcV3XskKuEDfQ3DcxotWm9ckkomVsa8gcLWcfdexnACxgUMx9TePJqXmsubmuXkcT1F3WYjJmAzlNeWxje+re50VuOABgTcCuEj4RjkCoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGywKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgL7UC4N"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
  "id": -576460752303421961,
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
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "state": "tx_+NILAfiEuEBVnRos+OaB/7YVSDFasV08mn2vLF5tbsTH51DhWGeoQKx/WroePgcHlJaN/IRihmkhsMrfyvlQhwAJHcV3XskKuEDfQ3DcxotWm9ckkomVsa8gcLWcfdexnACxgUMx9TePJqXmsubmuXkcT1F3WYjJmAzlNeWxje+re50VuOABgTcCuEj4RjkCoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGywKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgL7UC4N"
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
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "state": "tx_+NILAfiEuEBVnRos+OaB/7YVSDFasV08mn2vLF5tbsTH51DhWGeoQKx/WroePgcHlJaN/IRihmkhsMrfyvlQhwAJHcV3XskKuEDfQ3DcxotWm9ckkomVsa8gcLWcfdexnACxgUMx9TePJqXmsubmuXkcT1F3WYjJmAzlNeWxje+re50VuOABgTcCuEj4RjkCoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGywKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgL7UC4N"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421960,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
  "id": -576460752303421960,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999998
    },
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421959,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
  "id": -576460752303421959,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBVnRos+OaB/7YVSDFasV08mn2vLF5tbsTH51DhWGeoQKx/WroePgcHlJaN/IRihmkhsMrfyvlQhwAJHcV3XskKuEDfQ3DcxotWm9ckkomVsa8gcLWcfdexnACxgUMx9TePJqXmsubmuXkcT1F3WYjJmAzlNeWxje+re50VuOABgTcCuEj4RjkCoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGywKgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgL7UC4N",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/rDvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAKJdlKU"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421958,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
  "id": -576460752303421958,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000002
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBr2j/XUBXzrH54aoG8gkW2gNjecvMWiOVu/WAdbrUsbLA6AkNYEAPXVfCIkwxUteZklh3qStvXZ04Ibc0PUkdeEOC5NuD+Y=",
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

#### responder ---> node
```javascript
{
  "id": -576460752303421957,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBVffWnO28hTscGrC1BbuQ8YX8r+UpZqZKyZpiKy7Raqyhm1BrCOaUlM4uoyaUlDsCuBjhsNH5u8cnUG/3RWqoBuEj4RjkCoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGywOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguhrrr2"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
  "id": -576460752303421957,
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
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
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
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "signed_tx": "tx_+JALAfhCuEBVffWnO28hTscGrC1BbuQ8YX8r+UpZqZKyZpiKy7Raqyhm1BrCOaUlM4uoyaUlDsCuBjhsNH5u8cnUG/3RWqoBuEj4RjkCoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGywOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDguhrrr2",
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

#### initiator ---> node
```javascript
{
  "id": -576460752303421956,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBVffWnO28hTscGrC1BbuQ8YX8r+UpZqZKyZpiKy7Raqyhm1BrCOaUlM4uoyaUlDsCuBjhsNH5u8cnUG/3RWqoBuEDQM1Bn2lPhZ2gG2HSbiMew2bw3UWRkt7X6nULLA3Ww/TVicjWcrt5aq+6CXQ8UvWpMUZjP7FlN38bi7giYp/gGuEj4RjkCoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGywOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsJ+cOC"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
  "id": -576460752303421956,
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
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "state": "tx_+NILAfiEuEBVffWnO28hTscGrC1BbuQ8YX8r+UpZqZKyZpiKy7Raqyhm1BrCOaUlM4uoyaUlDsCuBjhsNH5u8cnUG/3RWqoBuEDQM1Bn2lPhZ2gG2HSbiMew2bw3UWRkt7X6nULLA3Ww/TVicjWcrt5aq+6CXQ8UvWpMUZjP7FlN38bi7giYp/gGuEj4RjkCoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGywOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsJ+cOC"
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
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "state": "tx_+NILAfiEuEBVffWnO28hTscGrC1BbuQ8YX8r+UpZqZKyZpiKy7Raqyhm1BrCOaUlM4uoyaUlDsCuBjhsNH5u8cnUG/3RWqoBuEDQM1Bn2lPhZ2gG2HSbiMew2bw3UWRkt7X6nULLA3Ww/TVicjWcrt5aq+6CXQ8UvWpMUZjP7FlN38bi7giYp/gGuEj4RjkCoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGywOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsJ+cOC"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421955,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
  "id": -576460752303421955,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
      "balance": 40000000000001
    },
    {
      "account": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421954,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
  "id": -576460752303421954,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBVffWnO28hTscGrC1BbuQ8YX8r+UpZqZKyZpiKy7Raqyhm1BrCOaUlM4uoyaUlDsCuBjhsNH5u8cnUG/3RWqoBuEDQM1Bn2lPhZ2gG2HSbiMew2bw3UWRkt7X6nULLA3Ww/TVicjWcrt5aq+6CXQ8UvWpMUZjP7FlN38bi7giYp/gGuEj4RjkCoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGywOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsJ+cOC",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1ovKCgEAhj+qJSJf/7DvQAGgUIfxRMCl/jwvRuoWbFmhIig8m7x6bH0vWLBj5i0/wvCLygoBAIYkYTnKgAG3nRgF"
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
  "method": "channels.snapshot_solo",
  "params": {}
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBr2j/XUBXzrH54aoG8gkW2gNjecvMWiOVu/WAdbrUsbLBKCOwaJmOhpyPuxhIkSe5cRuFX/EAvisEK9WHIA1BzoeAm0cfXo=",
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
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "signed_tx": "tx_+QEuCwHAuQEo+QElOwGhBr2j/XUBXzrH54aoG8gkW2gNjecvMWiOVu/WAdbrUsbLoQFQh/FEwKX+PC9G6hZsWaEiKDybvHpsfS9YsGPmLT/C8LjU+NILAfiEuEBVffWnO28hTscGrC1BbuQ8YX8r+UpZqZKyZpiKy7Raqyhm1BrCOaUlM4uoyaUlDsCuBjhsNH5u8cnUG/3RWqoBuEDQM1Bn2lPhZ2gG2HSbiMew2bw3UWRkt7X6nULLA3Ww/TVicjWcrt5aq+6CXQ8UvWpMUZjP7FlN38bi7giYp/gGuEj4RjkCoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGywOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsAhhMG0SswAEOaDUAH",
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
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEDuOL+C1RiPuuPg6iNFWI2+mnyWD0cAfMKa7/z8ez57mjCGI3zZf51X9mIOWBj2WVNMNhYaWdEZtNE9R+sLv+oIuEj4RjkCoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGywSgjsGiZjoacj7sYSJEnuXEbhV/xAL4rBCvVhyANQc6HgJFCYFU"
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
      "round": 3
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
      "round": 3
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
    "from": "ak_cU4JbcvVzqCtttniEVwvN1z6P7s4vgtTCjfDYfF1kbh7gCs7W",
    "to": "ak_2MJU325LQVfAu36vjGvdVpVgiCDbjRsMAjHZc7ahzuLZHTjWYS"
  }
}
```

#### initiator ---> node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
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
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBr2j/XUBXzrH54aoG8gkW2gNjecvMWiOVu/WAdbrUsbLBKCPVbQrAfYXrWTP0iwmtWIe9nj7Tuv+WHg7LyUfwRTSMVJjr80=",
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
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
    "data": {
      "signed_tx": "tx_+QEvCwHAuQEp+QEmOwGhBr2j/XUBXzrH54aoG8gkW2gNjecvMWiOVu/WAdbrUsbLoQGxytVKym65ULDCN2I5ffDIg3CzsO3bhuBQx/hdrM9v1rjU+NILAfiEuEBVffWnO28hTscGrC1BbuQ8YX8r+UpZqZKyZpiKy7Raqyhm1BrCOaUlM4uoyaUlDsCuBjhsNH5u8cnUG/3RWqoBuEDQM1Bn2lPhZ2gG2HSbiMew2bw3UWRkt7X6nULLA3Ww/TVicjWcrt5aq+6CXQ8UvWpMUZjP7FlN38bi7giYp/gGuEj4RjkCoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGywOgJDWBAD11XwiJMMVLXmZJYd6krb12dOCG3ND1JHXhDgsAhhMLeUL4AIHGgZHp/A==",
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
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEBrx67S1TgnEdOw93tjHKQluqgfJm2B5mk0rmwD//g2HRmGAwDzZNXb4Qnv+ROyuvGYCDMmgpGCcKyEfXeAZQ8PuEj4RjkCoQa9o/11AV86x+eGqBvIJFtoDY3nLzFojlbv1gHW61LGywSgj1W0KwH2F61kz9IsJrViHvZ4+07r/lh4Oy8lH8EU0jE36DKb"
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
      "round": 3
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
      "round": 3
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421953,
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
  "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
  "id": -576460752303421953,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421952,
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
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
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
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
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
  "channel_id": "ch_2SX7dLWnhqetycdHMA4NRQgB2TyfULSyiFamMqAhPmtMFWQt7D",
  "id": -576460752303421952,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
