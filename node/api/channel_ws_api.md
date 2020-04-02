[back](./README.md)
# State channel WebSocket API

Messages on the WebSocket API have to follow JSON-RPC specification version 2.0. See: [www.jsonrpc.org](https://www.jsonrpc.org/specification)

The WebSocket API provides the following actions:
 * [Off-chain update](#update)
 * [On-chain deposit](#deposit)
 * [On-chain withdrawal](#withdrawal)
 * [Contracts](#contracts)
 * [Generic message](#generic-message)
 * [Close mutual](#close-mutual)
 * [Close solo](#close-solo)
 * [Slash](#slash)
 * [Settle](#settle)
 * [Leave](#leave)
 * [Snapshot](#snapshot)
 * [Force progress](#force-progress)
 * [Contract dry run](#contract-dry-run)
 * [On-chain transactions](#on-chain-transactions)
 * [Info messages](#info-messages)
 * [System messages](#system-messages)
 * [Signing error replies](#signing-error-replies)

## Update
Roles:
 * Sender
 * Acknowledger

### Sender trigger an update
 * **method:** `channels.update.new`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | from | string | Participant's account to take tokens from | Yes |
  | to | string | Participant's account to add tokens to | Yes |
  | amount | integer | Amount of tokens to transfer | Yes |
  | block_hash | string | The on-chain block hash to pin the off-chain environment | No |
  | meta | array of strings | Meta information about the update | No |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
    "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
  }
}
```

### Sender receives a non-authenticated off-chain state
 * **method:** `channels.sign.update`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | signed_tx | string | `channel_offchain_tx` transaction wrapped in a `signed_tx` with no authentication | Yes |
  | updates | list | off-chain updates | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "signed_tx": "tx_+JU5AaEGrATZCq...",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
          "op": "OffChainTransfer",
          "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
        }
      ]
    }
  },
  "version": 1
}
```

### Sender authenticates off-chain state responsse
 * **method:** `channels.update`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | signed_tx | string | solo-authenticated `channel_offchain_tx` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+N8LAfhCuEA..."
  }
}
```

### Acknowledger receives a non-authenticated off-chain state
 * **method:** `channels.sign.update_ack`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | signed_tx | string | solo-authenticated `channel_offchain_tx` transaction | Yes |
  | updates | list | off-chain updates | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "signed_tx": "tx_+JU5AaEGrATZCq...",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
          "op": "OffChainTransfer",
          "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
        }
      ]
    }
  },
  "version": 1
}
```

### Acknowledger authenticated off-chain state responsse
 * **method:** `channels.update_ack`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | signed_tx | string | co-authenticated `channel_offchain_tx` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+N8LAfhCuE..."
  }
}
```

### Update conflict
 * **method:** `channels.conflict`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | channel_id | string | channel id| Yes |
  | data | object | description of the last mutually authenticated state | Yes |

 * **data:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | channel_id | string | channel id| Yes |
  | round | object | the round of the last mutually authenticated state | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
      "round": 5
    }
  },
  "version": 1
}
```

### Update error
 * **error:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | message | string | error message | Yes |
  | code | integer | error code | Yes |
  | data | json | error description | Yes |
  | request | json | the failed request | Yes |

 * **data:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | message | string | JSON-RPC error message | Yes |
  | code | integer | JSON-RPC error code | Yes |

#### Example
```javascript
{
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1001,
        "message": "Insufficient balance"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 10000000000000000,
        "from": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC",
        "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
      }
    }
  },
  "id": null,
  "jsonrpc": "2.0",
  "version": 1
}
```

## Deposit
Roles:
 * Depositor
 * Acknowledger

### Depositor trigger a update
 * **method:** `channels.deposit`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | amount | integer | Amount of tokens to deposit in the channel | Yes |
  | block_hash | string | The on-chain block hash to pin the off-chain environment | No |
  | fee | integer | The on-chain transaction fee to be used. If not provided the FSM picks a value for the client | No |
  | gas_price | integer | the gas_price to be used for the fee computation | No |
  | nonce | integer | the nonce to be used in the transaction | No |
  | meta | array of strings | Meta information about the update | No |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit",
  "params": {
    "amount": 2
  }
}
```

### Depositor receives an non-authenticated deposit transaction
 * **method:** `channels.sign.deposit_tx`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | channel_id | string | channel ID | Yes |
  | data | object | deposit data | Yes |

 * **data:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | signed_tx | string | `channel_deposit_tx` transaction wrapped in a `signed_tx` with no authentication | Yes |
  | updates | list | off-chain updates | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "signed_tx": "tx_+HIzAaEGgofGx...",
      "updates": [
        {
          "amount": 2,
          "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
          "op": "OffChainDeposit"
        }
      ]
    }
  },
  "version": 1
}
```

### Depositor authenticates deposit response
 * **method:** `channels.deposit_tx`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | signed_tx | string | solo-authenticated `channel_deposit_tx` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhCuEB..."
  }
}
```

### Acknowledger receives a non-authenticated deposit transaction
 * **method:** `channels.sign.deposit_ack`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | channel_id | string | channel ID | Yes |
  | data | object | deposit data | Yes |

 * **data:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | signed_tx | string | solo-authenticated `channel_deposit_tx` transaction | Yes |
  | updates | list | off-chain updates | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "signed_tx": "tx_+LwLAfhCuEB..."
      "updates": [
        {
          "amount": 2,
          "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
          "op": "OffChainDeposit"
        }
      ]
    }
  },
  "version": 1
}
```

### Acknowledger authenticates deposit responsse
 * **method:** `channels.deposit_ack`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | signed_tx | string | co-authenticated `channel_deposit_tx` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "signed_tx": "tx_+LwLAfhCu..."
  }
}
```

## Withdrawal
Roles:
 * Withdrawer
 * Acknowledger

### Withdrawer trigger a update
 * **method:** `channels.withdraw`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | amount | integer | Amount of tokens to withdraw form the channel | Yes |
  | block_hash | string | The on-chain block hash to pin the off-chain environment | No |
  | fee | integer | The on-chain transaction fee to be used. If not provided the FSM picks a value for the client | No |
  | gas_price | integer | the gas_price to be used for the fee computation | No |
  | nonce | integer | the nonce to be used in the transaction | No |
  | meta | array of strings | Meta information about the update | No |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw",
  "params": {
    "amount": 2
  }
}
```

### Withdrawer receives a non-authenticated withdraw transaction
 * **method:** `channels.sign.withdraw_tx`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | channel_id | string | channel ID | Yes |
  | data | object | withdrawal data | Yes |

 * **data:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | signed_tx | string | `channel_withdraw_tx` transaction wrapped in a `signed_tx` with no authentication | Yes |
  | updates | list | off-chain updates | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "signed_tx": "tx_+HI0AaEG...",
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
        }
      ]
    }
  },
  "version": 1
}
```

### Withdrawer authenticates withdraw response
 * **method:** `channels.withdraw_tx`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | signed_tx | string | co-authenticated `channel_withdraw_tx` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "signed_tx": "tx_+LwLAfhC..."
  }
}
```

### Acknowledger receives a non-authenticated withdraw transaction
 * **method:** `channels.sign.withdraw_ack`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | channel_id | string | channel ID | Yes |
  | data | object | withdrawal data | Yes |

 * **data:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | signed_tx | string | solo-authenticated `channel_withdraw_tx` transaction | Yes |
  | updates | list | off-chain updates | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "signed_tx": "tx_+LwLAfhC..."
      "updates": [
        {
          "amount": 2,
          "op": "OffChainWithdrawal",
          "to": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm"
        }
      ]
    }
  },
  "version": 1
}
```

### Acknowledger authenticates withdraw responsse
 * **method:** `channels.withdraw_ack`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | signed_tx | string | co-authenticated `channel_withdraw_tx` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "signed_tx": "tx_+LwLAf..."
  }
}
```

## Contracts

### Contract create

 * **method:** `channels.update.new_contract`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | code | contract code | contract code | Yes |
  | call\_data | call data | call data for contract creation | Yes |
  | vm\_version | integer | contract virtual machine version (vm for which code was compiled) | Yes |
  | abi\_version | integer | contract virtual machine abi version | Yes |
  | deposit | integer | contract creation deposit | Yes |
  | block_hash | string | The on-chain block hash to pin the off-chain environment | No |
  | meta | array of strings | Meta information about the update | No |

#### Example

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract",
  "params": {
    "abi_version": 1,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAnHQYrA==",
    "code": "cb_+QP1RgKg/ukoFMi2RBUIDNHZ3pMMzHSrPs/uKkwO/vEf7cRnitr5Avv5ASqgaPJnYzj/UIg5q6R3Se/6i+h+8oTyB/s9mZhwHNU4h8WEbWFpbrjAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAuEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA+QHLoLnJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqhGluaXS4YAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP//////////////////////////////////////////7kBQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEA//////////////////////////////////////////8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA///////////////////////////////////////////uMxiAABkYgAAhJGAgIBRf7nJVvKLMUmp9Zh6pQXz2hsiCcxXOSNABiu2wb2fn5nqFGIAAMBXUIBRf2jyZ2M4/1CIOaukd0nv+ovofvKE8gf7PZmYcBzVOIfFFGIAAK9XUGABGVEAW2AAGVlgIAGQgVJgIJADYAOBUpBZYABRWVJgAFJgAPNbYACAUmAA81tZWWAgAZCBUmAgkANgABlZYCABkIFSYCCQA2ADgVKBUpBWW2AgAVFRWVCAkVBQgJBQkFZbUFCCkVBQYgAAjFaFMi4xLjAhVoVW",
    "deposit": 10,
    "vm_version": 3
  }
}
```

### Contract call

 * **method:** `channels.update.call_contract`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | contract_id | contract id | contract to call | Yes |
  | call\_data | call data | call data | Yes |
  | abi\_version | integer | call abi version | Yes |
  | amount | integer | amount of tokens to transfer to contract | Yes |
  | block_hash | string | The on-chain block hash to pin the off-chain environment | No |
  | meta | array of strings | Meta information about the update | No |

#### Example

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract_id": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
  }
}
```

## Generic message
Roles:
 * Sender
 * Receiver

### Sender send message
 * **method:** `channels.message`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | to | string | Receiver's address | Yes |
  | info | string | Message body | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "info": "hejsan",
    "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
  }
}
```

### Receiver receives message
 * **method:** `channels.message`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | channel_id | string | channel id | Yes |
  | data | object | data field that contains the message | Yes |

 * **data:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | message | object | the message itself | Yes |

 * **message:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | channel_id | string | channel id| Yes |
  | from | string | Sender's address | Yes |
  | to | string | Receiver's address | Yes |
  | info | string | Message body | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "message": {
        "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
        "from": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
        "info": "hejsan",
        "to": "ak_nQpnNuBPQwibGpSJmjAah6r3ktAB7pG9JHuaGWHgLKxaKqEvC"
      }
    }
  },
  "version": 1
}
```

## Close mutual
Roles:
 * Closer
 * Acknowledger

### Closer initiate mutual close
 * **method:** `channels.shutdown`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | block_hash | string | The on-chain block hash to pin the off-chain environment | No |
  | fee | integer | The on-chain transaction fee to be used. If not provided the FSM picks a value for the client | No |
  | gas_price | integer | the gas_price to be used for the fee computation | No |
  | nonce | integer | the nonce to be used in the transaction | No |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown",
  "params": {}
}
```

### Closer receives mutual close
 * **method:** `channels.sign.shutdown_sign`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | channel_id | string | channel ID | Yes |
  | data | object | closing data | Yes |

 * **data:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | signed_tx | string | `channel_close_mutual_tx` transaction wrapped in a `signed_tx` with no authentication | Yes |
  | updates | list | off-chain updates | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
    "data": {
      "signed_tx": "tx_+F01Aa...",
      "updates": []
    }
  },
  "version": 1
}
```

### Closer returns an authenticated mutual close
 * **method:** `channels.shutdown_sign`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | signed_tx | string | solo-authenticated `channel_close_mutual_tx` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhC..."
  }
}
```

### Acknowledger receives mutual close
 * **method:** `channels.sign.shutdown_sign_ack`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | channel_id | string | channel ID | Yes |
  | data | object | closing data | Yes |

 * **data:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | signed_tx | string | solo-authenticated `channel_close_mutual_tx` transaction | Yes |
  | updates | list | off-chain updates | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
    "data": {
      "signed_tx": "tx_+KcLAfhC..."
      "updates": []
    }
  },
  "version": 1
}
```

### Acknowledger returns an authenticated mutual close
 * **method:** `channels.shutdown_sign_ack`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | signed_tx | string | co-authenticated `channel_close_mutual_tx` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "signed_tx": "tx_+KcLAf..."
  }
}
```

## Snapshot
Roles:
 * Snapshotter

### Snapshotter is prompted to snapshot (not mandatory step)
 * **method:** `channels.on_chain_tx`
 * **params:**

 | Name  | Type | Description | Required |
 | ----- | ---- | ----------- | -------- |
 | info | string | "can_snapshot" | Yes |
 | tx | string | the last on-chain transaction that could be disputed by a snapshot | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_rb...",
    "data": {
      "info": "can_snapshot",
      "tx": "tx_+NIL...",
      "type": "channel_offchain_tx"
    }
  },
  "version": 1
}
```

### Snapshotter initiates solo snapshot
 * **method:** `channels.snapshot_solo`
 * **params:**

 | Name  | Type | Description | Required |
 | ----- | ---- | ----------- | -------- |
 | fee | integer | The on-chain transaction fee to be used. If not provided the FSM picks a value for the client | No |
 | gas_price | integer | the gas_price to be used for the fee computation | No |
 | nonce | integer | the nonce to be used in the transaction | No |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo",
  "params": {}
}
```

### Snapshotter receives solo snapshot
 * **method:** `channels.sign.snapshot_solo_tx`
 * **params:**

 | Name  | Type | Description | Required |
 | ----- | ---- | ----------- | -------- |
 | channel_id | string | channel ID | Yes |
 | data  | object | closing data | Yes |

 * **data:**

 | Name | Type | Description | Required |
 | ---- | ---- | ----------- | -------- |
 | signed_tx | string | `channel_snapshot_solo_tx` transaction wrapped in a `signed_tx` with no authentication | Yes |
 | updates | list | empty list | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.snapshot_solo_tx",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "signed_tx": "tx_+QGfNgGhBn...",
      "updates": []
    }
  },
  "version": 1
}
```

### Snapshotter returns an authenticated solo snapshot
 * **method:** `channels.snapshot_solo_sign`
 * **params:**

 | Name | Type | Description | Required |
 | ---- | ---- | ----------- | -------- |
 | signed_tx | string | solo-authenticated `channel_snapshot_solo_tx` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.snapshot_solo_sign",
  "params": {
    "signed_tx": "tx_+QHrCwH4Q..."
  }
}
```

## Force progress
Roles:
 * Forcer

### Forcer initiates a force progress
 * **method:** `channels.force_progress`
 * **params:**

 | Name  | Type | Description | Required |
 | ----- | ---- | ----------- | -------- |
 | contract_id | contract id | contract to call | Yes |
 | call\_data | call data | call data | Yes |
 | abi\_version | integer | call abi version | Yes |
 | amount | integer | amount of tokens to transfer to contract | Yes |
 | gas\_price | integer | the gas\_price to be used for the fee computation and the update execution | Yes |
 | gas | integer | gas limit, if not provided `1000000` is the default value | No |
 | nonce | integer | the nonce to be used in the transaction | No |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.force_progress",
  "params": { 
    "abi_version":1,
    "amount":10,
    "call_data":"cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
    "contract_id":"ct_5XjcY6aaohWVHf6WSKcZKuMKYL3CfwopJRCnwqSaEgJUGrpbP",
    "gas_price":1000005554
  }
}
```

### Forcer receives a prepared force progress transaction to authenticate
 * **method:** `channels.sign.force_progress_tx`
 * **params:**

 | Name  | Type | Description | Required |
 | ----- | ---- | ----------- | -------- |
 | channel\_id | string | channel ID | Yes |
 | data  | object | closing data | Yes |

 * **data:**

 | Name | Type | Description | Required |
 | ---- | ---- | ----------- | -------- |
 | signed\_tx | string | `channel_force_progress_tx` transaction wrapped in a `signed_tx` with no authentication | Yes |
 | updates | list | a list of a single update | Yes |

 * **update**

 | Name | Type | Description | Required |
 | ---- | ---- | ----------- | -------- |
 | amount | integer | the tokens amount given to the off-chain contract | Yes |
 | abi\_version | integer | abi version | Yes |
 | call\_data | integer | contract execution call data | Yes |
 | call\_stack | list | contract execution call stack | Yes |
 | caller\_id | string | ID of the caller | Yes |
 | contract\_id | string | contract ID to be executed | Yes |
 | gas | integer | gas limit | Yes |
 | gas\_price | integer | gas price | Yes |
 | op | string | "OffChainCallContract" | Yes |


#### Example
```javascript
{ 
   "jsonrpc":"2.0",
   "method":"channels.sign.force_progress_tx",
   "params":{ 
      "channel_id":"ch_2FdiLKkRUdPw4oTRbB6i3M6pquogzWLABQjU373hizDbnD8gGC",
      "data":{ 
         "signed_tx":"tx_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",
         "updates":[ 
            { 
               "abi_version":1,
               "amount":10,
               "call_data":"cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACCzVg5SHSPanMS8lSeSX8SFfJMeAfEkyR6oKfQhD6XCTgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA5gCcXw==",
               "call_stack":[ 

               ],
               "caller_id":"ak_Vu1cGq2d3Dpo9gP7pVJc8KMubXr8PjuX51b4yyJmFDcXgTZxT",
               "contract_id":"ct_55CN7nU2xnfkEUQbe9Aai4xwLEcRyTjYS2zmVpcHtFFqHLVX6",
               "gas":1000000,
               "gas_price":1000000000,
               "op":"OffChainCallContract"
            }
         ]
      }
   },
   "version":1
}
```

### Forcer returns an authenticated force progress transaction
 * **method:** `channels.force_progress_sign`
 * **params:**

 | Name | Type | Description | Required |
 | ---- | ---- | ----------- | -------- |
 | signed\_tx | string | solo-authenticated `channel_snapshot_solo_tx` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.force_progress_sign",
  "params": {
    "signed_tx": "tx_+QkACwH4Qrh..."
  }
}
```

### Contract dry run

 * **method:** `channels.dry_run.call_contract`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | contract_id | contract id | contract to call | Yes |
  | call\_data | call data | call data | Yes |
  | abi\_version | integer | call abi version | Yes |
  | amount | integer | amount of tokens to transfer to contract | Yes |
  | block_hash | string | The on-chain block hash to pin the off-chain environment | No |
  | meta | array of strings | Meta information about the update | No |

#### Example

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.dry_run.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract_id": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
  }
}
```

## On-chain transactions
 * **method:** `channels.on_chain_tx`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | channel_id | string | channel ID | Yes |
  | data | object | closing data | Yes |

 * **data:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | info | string | specific type of event | Yes |
  | signed_tx | string | a mutually authenticated transaction that is posted on-chain | Yes |
  | type | transaction type | Yes |

 The `info` values could be:
 * `"funding_signed"` - reported by the `initiator`, indicating that a `channel_create_tx` has been
   singly authenticated by the `initiator` client, and sent to the `responder` for co-signing.
 * `"funding_created"` - reported by the `responder`, indicating that a `channel_create_tx` has been
   co-authenticated, and will be pushed to the mempool.
 * `"deposit_signed"` - reported by the `depositor`, indicating that a `channel_deposit_tx` has been
   singly authenticated by the `depositor` client, and sent to the `acknowledger` for co-signing.
 * `"deposit_created"` - reported by the `acknowledger`, indicating that a `channel_deposit_tx` has been
   co-authenticated, and will be pushed to the mempool.
 * `"withdraw_signed"` - reported by the `withdrawer`, indicating that a `channel_withdraw_tx` has been
   singly authenticated by the `withdrawer` client, and sent to the `acknowledger` for co-signing.
 * `"withdraw_created"` - reported by the `acknowledger`, indicating that a `channel_withdraw_tx` has been
   co-authenticated, and will be pushed to the mempool.
 * `"channel_changed"` - reported by both parties, indicating that the fsm has detected a channel-related
   transaction on-chain. Note that this will be reported also for the `channel_create_tx`, once it
   appears on-chain. This means that each client will get _two_ `on_chain_tx` reports for the
   create, deposit, withdraw and close_mutual transactions.
 * `"close_mutual"` - reported by both parties, indicating that a `channel_close_mutual_tx` has been
   co-authenticated, and will be pushed to the mempool.
 * `"channel_closed"` - reported by both parties, when the on-chain channel state is detected to transition
   to a `closed` state.
 * `"solo_closing"` - reported by both parties, when the on-chain channel state is detected to transition
   to a proper `solo_closing` state - that is, with the latest known state.
 * `"can_slash"` or `"can_snapshot"`- reported by both parties, when the
   on-chain channel state is seen to transition into an improper state -
   that is, when there exists a later mutually authenticated state than the
   one reported by either party on-chain. If the channel is not yet closing -
   that could be a malicious `channel_force_progress_tx` and the reported
   `info` value is `"can_snapshot"`. If the malicious on-chain transaction is
   `channel_close_solo_tx` or the channel is already closing and a
   `channel_force_progress_tx` is received - then the `info` is `"can_slash"`.
   Other transactions with an older `round` than the latest off-chain are not
   considered harmful.

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "info": "deposit_signed",
      "signed_tx": "tx_+KcLAf..."
      "type": "channel_deposit_tx"
    }
  },
  "version": 1
}
```

## Close solo
Roles:
 * Closer

### Closer initiated solo close
 * **method:** `channels.close_solo`
 * **params:**

 | Name  | Type | Description | Required |
 | ----- | ---- | ----------- | -------- |
 | fee | integer | The on-chain transaction fee to be used. If not provided the FSM picks a value for the client | No |
 | gas_price | integer | the gas_price to be used for the fee computation | No |
 | nonce | integer | the nonce to be used in the transaction | No |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo",
  "params": {}
}
```

### Closer receives solo close
 * **method:** `channels.sign.close_solo_sign`
 * **params:**

 | Name  | Type | Description | Required |
 | ----- | ---- | ----------- | -------- |
 | channel_id | string | channel ID | Yes |
 | data  | object | closing data | Yes |

 * **data:**

 | Name | Type | Description | Required |
 | ---- | ---- | ----------- | -------- |
 | signed_tx | string | `channel_close_solo_tx` transaction wrapped in a `signed_tx` with no authentication | Yes |
 | updates | list | off-chain updates | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "signed_tx": "tx_+QGfNgGhBn...",
      "updates": []
    }
  },
  "version": 1
}
```

### Closer returns an authenticated solo close
 * **method:** `channels.close_solo_sign`
 * **params:**

 | Name | Type | Description | Required |
 | ---- | ---- | ----------- | -------- |
 | signed_tx | string | solo-authenticated `channel_close_solo_tx` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo_sign",
  "params": {
    "signed_tx": "tx_+QHrCwH4Q..."
  }
}
```
## Slash
Roles:
 * Slasher

### Slasher initiated slash
 * **method:** `channels.slash
 * **params:**

 | Name  | Type | Description | Required |
 | ----- | ---- | ----------- | -------- |
 | fee | integer | The on-chain transaction fee to be used. If not provided the FSM picks a value for the client | No |
 | gas_price | integer | the gas_price to be used for the fee computation | No |
 | nonce | integer | the nonce to be used in the transaction | No |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.slash",
  "params": {}
}
```

### Slasher receives slash
 * **method:** `channels.sign.slash_tx`
 * **params:**

 | Name  | Type | Description | Required |
 | ----- | ---- | ----------- | -------- |
 | channel_id | string | channel ID | Yes |
 | data  | object | closing data | Yes |

 * **data:**

 | Name | Type | Description | Required |
 | ---- | ---- | ----------- | -------- |
 | signed_tx | string | `channel_slash_tx` transaction wrapped in a `signed_tx` with no authentication | Yes |
 | updates | list | off-chain updates | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash_tx",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "signed_tx": "tx_+QLDCwHAuQ...",
      "updates": []
    }
  },
  "version": 1
}
```

### Slasher returns an authenticated slash
 * **method:** `channels.slash_sign
 * **params:**

 | Name | Type | Description | Required |
 | ---- | ---- | ----------- | -------- |
 | signed_tx | string | solo-authenticated `channel_slash_tx` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.slash_sign",
  "params": {
    "signed_tx": "tx_+QMGCwH4Qr..."
  }
}
```

## Slash
Roles:
 * Slasher

### Slasher is prompted to slash
 * **method:** `channels.on_chain_tx`
 * **params:**

 | Name  | Type | Description | Required |
 | ----- | ---- | ----------- | -------- |
 | info | string | "can_slash" | Yes |
 | tx | string | the last on-chain transaction that could be slashed | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_rb...",
    "data": {
      "info": "can_slash",
      "tx": "tx_+NIL...",
      "type": "channel_offchain_tx"
    }
  },
  "version": 1
}
```


### Slasher initiates slash
 * **method:** `channels.slash`

#### Example
```javascript
{
  "id": -576460752303423374,
  "jsonrpc": "2.0",
  "method": "channels.slash"
}
```

### Slasher receives slash
 * **method:** `channels.sign.slash`
 * **params:**

 | Name  | Type | Description | Required |
 | ----- | ---- | ----------- | -------- |
 | channel_id | string | channel ID | Yes |
 | data  | object | slashing data | Yes |

 * **data:**

 | Name | Type | Description | Required |
 | ---- | ---- | ----------- | -------- |
 | signed_tx | string | `channel_slash` transaction wrapped in a `signed_tx` with no authentication | Yes |
 | updates | list | empty list of updates updates | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.slash",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "signed_tx": "tx_+QGfNgGhBn...",
      "updates": []
    }
  },
  "version": 1
}
```

### Slasher returns an authenticated slash
 * **method:** `channels.slash_sign`
 * **params:**

 | Name | Type | Description | Required |
 | ---- | ---- | ----------- | -------- |
 | signed_tx | string | solo-authenticated `channel_slash` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.slash_sign",
  "params": {
    "signed_tx": "tx_+QHrCwH4Q..."
  }
}
```

## Settle
Roles:
 * Settler

### Settler initiates settle
 * **method:** `channels.settle`
 * **params:**

 | Name  | Type | Description | Required |
 | ----- | ---- | ----------- | -------- |
 | fee | integer | The on-chain transaction fee to be used. If not provided the FSM picks a value for the client | No |
 | gas_price | integer | the gas_price to be used for the fee computation | No |
 | nonce | integer | the nonce to be used in the transaction | No |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle",
  "params": {}
}
```
### Settler receives settle
 * **method:** `channels.sign.settle_sign`
 * **params:**

 | Name | Type | Description | Required |
 | ---- | ---- | ----------- | -------- |
 | channel_id | string | channel ID | Yes |
 | data | object | settle data | Yes |

 * **data:**

 | Name | Type | Description | Required |
 | ---- | ---- | ----------- | -------- |
 | signed_tx | string | `channel_settle_tx` transaction wrapped in a `signed_tx` with no authentication | Yes |
 | updates | list | off-chain updates | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "signed_tx": "tx_+F04AaE...",
      "updates": []
    }
  },
  "version": 1
}
```
### Settler returns an authenticated settle
 * **method:** `channels.settle_sign`
 * **params:**

 | Name | Type | Description | Required |
 | ---- | ---- | ----------- | -------- |
 | signed_tx | string | solo-authenticated `channel_settle_tx` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle_sign",
  "params": {
    "signed_tx": "tx_+KcLAfhCuEBdI..."
  }
}
```

## Leave
Roles:
 * Leaver
 * Acknowledger

### Leaver initiates leave
 * **method:** `channels.leave`

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {}
}
```

#### Leaver and Acknowledger inform their clients

 * **method:** `channels.leave`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | channel_id | string | channel ID | Yes |
  | data | object | closing data | Yes |

 * **data:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | state | string | a mutually authenticated last state transaction | Yes |

#### Example

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "state": "tx_+QENCwH4hLh..."
    }
  },
  "version": 1
}
```

## Info messages

### Info
 * **method:** `channels.info`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | channel_id | string | channel ID | Yes |
  | data | object | info data | Yes |

 * **data:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | event | string | event description | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "event": "own_deposit_locked"
    }
  },
  "version": 1
}
```

### Latest state
 * **method:** `channels.get.offchain_state`

#### Response
 * **result:**

 | Field name | Value |
 | ---- | ---- |
 | `trees` | channel state trees |
 | `calls` | channel call state tree |
 | `half_signed_tx` | channel latest half authenticated tx or `''` if equal to latest authenticated tx |
 | `signed_tx` | channel latest mutually authenticated tx or `''` if not available |

#### Example

##### Request
```javascript
{
  "id": -576460752303423469,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```
##### Response
```javascript
{
  "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
  "id": -576460752303423469,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+QEhCwH4hLhA...",
    "trees": "ss_+Ks+AIrJggJtAY..."
  },
  "version": 1
}
```

### Latest contract state
 * **method:** `channels.get.contract`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | pubkey | string | requested contract pubkey | Yes |

#### Response
 * **result:**

 | Field name | Value |
 | ---- | ---- |
 | `contract` | object with contract details |
 | `contract->id` | contract id (equals to the requested pubkey) |
 | `contract->owner_id` | contract owner id |
 | `contract->vm_version` | contract vm version (integer) |
 | `contract->abi_version` | contract ABI version (integer) |
 | `contract->active` | "is contract active?" boolean |
 | `contract->referrer_ids` | referrer ids list |
 | `contract->deposit` | contract deposit |
 | `contract_state` | object with contract state |

#### Example

##### Request
```javascript
{
  "id": -576460752303423430,
  "jsonrpc": "2.0",
  "method": "channels.get.contract",
  "params": {
    "pubkey": "ct_uBX2jBr5bPEzD1uGFmV4i7JrGLtpEeLqPU29HvkZCv5iHcY4M"
  }
}
```

##### Response
```javascript
{
  "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
  "id": -576460752303423430,
  "jsonrpc": "2.0",
  "result": {
    "contract": {
      "abi_version": 1,
      "active": true,
      "deposit": 10,
      "id": "ct_uBX2jBr5bPEzD1uGFmV4i7JrGLtpEeLqPU29HvkZCv5iHcY4M",
      "owner_id": "ak_2MGLPW2CHTDXJhqFJezqSwYSNwbZokSKkG7wSbGtVmeyjGfHtm",
      "referrer_ids": [],
      "vm_version": 3
    },
    "contract_state": {
      "ck_AAAAAAAAAAAAAAAAAAAAAAA...": "cv_sbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YlrDqa",
      "ck_AAAAAAAAAAAAAAAAAAAAAAA...": "cv_sbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YlrDqa",
      "ck_AAAAAAAAAAAAAAAAAAAAAAA...": "cv_sbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YlrDqa",
      "ck_AAAAAAAAAAAAAAAAAAAAAAA...": "cv_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA...",
      "ck_AAAAAAAAAAAAAAAAAAAAAAA...": "cv_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA...",
      "ck_ABQG4Fg=": "cv_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDIq10LA12xQcUbe3+xpb7...",
      "ck_AZwSz9w=": "cv_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAA...",
      "ck_AhzDreo=": "cv_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPJ9AW0"
    }
  },
  "version": 1
}
```

## System messages

### ping
 * **method:** `channels.system`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | action | string | the value "ping" | Yes |

#### Response
 * **method:** `channels.system`
 * **params.data:**

 | Field name | Value |
 | ---- | ---- |
 | `action` | "system" |
 | `tag` | "pong" |

#### Example

##### Request
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "ping"
  }
}
```
##### Response
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.system.pong",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "action": "system",
      "tag": "pong"
    }
  },
  "version": 1
}
```

## Signing Error Replies
 * **method:** `channels.initiator_sign | channels.responder_sign | channels.deposit_tx | channels.deposit_ack
            | channels.withdraw_tx | channels.withdraw_ack | channels.responder_sign
            | channels.snapshot_solo_tx | channels.snapshot_solo_sign
            | channels.shutdown_sign | channels.shutdown_sign_ack | channels.update | channels.update_ack
            | channels.close_solo_tx | channels.close_solo_sign | channels.slash_tx | channels.slash_sign
            | channels.settle_tx | channels.settle_sign`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | error | integer | error code | Yes |

It is possible to return an error object in a signing reply. This will abort the ongoing sequence, and the FSM will
fall back to the latest mutually-signed state. Currently defined error codes are:

* 1: validation error
* 2: conflict (typically, race condition)
* 3: timeout
* 4: abort
* 128...65535: user-defined

#### Example
```javascript
{
  "id": -576460752303423252,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "error": 147
  }
}
```

#### Successful operation response

 * **method:** `channels.info`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | channel_id | string | channel ID | Yes |
  | data | object | message data | Yes |

 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | event | string | `aborted_update` | Yes |

 * **data:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | message | string | `Not allowed at current channel state` | Yes |
  | code | integer | `1018` | Yes |


If the abort of the update is successful, the client that aborted receives a
message for it:

```javascript
{ 
   "jsonrpc":"2.0",
   "method":"channels.info",
   "params":{ 
      "channel_id":"ch_95YaTDZAysRu3GkmW2yKkCK1H4fGtcttoj2qwFDfUSduTpCPf",
      "data":{ 
         "event":"aborted_update"
      }
   },
   "version":1
}
```

If the other participant had initiated the update that our client had aborted,
the other participant's FSM will inform its client of each error, using a
`conflict` report.

##### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.conflict",
  "params": {
    "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
    "data": {
      "channel_id": "ch_Bx4x8rvNpeHe2LtnDNqyqCvguqX5jEeotUDk5cRXH3mEXzy77",
      "error_code": 147,
      "error_msg": "user-defined",
      "round": 5
    }
  },
  "version": 1
}
```

#### Unsuccessful operation response

 * **method:** the request method
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | channel_id | string | channel ID | Yes |
  | error | object | error data object | Yes |

 * **error:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | message | string | `Rejected` | Yes |
  | code | integer | the error code provided | Yes |
  | data | json | error description | Yes |
  | request | json | the failed request | Yes |

 * **data:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | message | string | `Not allowed at current channel state` | Yes |
  | code | integer | `1018` | Yes |

If the specified update abort can not be performed now, the request receives
the following error:

```javascript
{
   "channel_id":"ch_95YaTDZAysRu3GkmW2yKkCK1H4fGtcttoj2qwFDfUSduTpCPf",
   "error":{
      "code":3,
      "data":[
         {
            "code":1018,
            "message":"Not allowed at current channel state"
         }
      ],
      "message":"Rejected",
      "request":{
         "jsonrpc":"2.0",
         "method":"channels.update",
         "params":{
           "error":147
         }
      }
   },
   "id":null,
   "jsonrpc":"2.0",
   "version":1
}
```
