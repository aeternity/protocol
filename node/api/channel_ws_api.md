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
 * [Settle](#settle)
 * [Leave](#leave)
 * [On-chain transactions](#on-chain-transactions)
 * [Info messages](#info-messages)

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

### Sender receives unsigned off-chain state
 * **method:** `channels.sign.update`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | unsigned `channel_offchain` transaction | Yes |
  | updates | list | off-chain updates | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "tx": "tx_+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4Zxbb8Q=",
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

### Sender signed off-chain state responsse
 * **method:** `channels.update`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | signed `channel_offchain` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "tx": "tx_+N8LAfhCuEAFOva8xKyh9tzeIps9Tum89u4xTvbT0yokbLnu78KnIK6wZRZiYlwrBujUEQg0t3Tud9BXDn5oKwnkdJizmA0GuJf4lTkBoQasBNkKrZJu+gk87ymFQsCsenQzLt8Fb1JKm0n7nKzTYgL4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoNUqd4GTOFacRsLar0VqTNSHraQXvmyQrL/MBqX090Lh+pkf9A=="
  }
}
```

### Acknowledger receives unsigned off-chain state
 * **method:** `channels.sign.update_ack`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | unsigned `channel_offchain` transaction | Yes |
  | updates | list | off-chain updates | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update_ack",
  "params": {
    "channel_id": "ch_2Jkzb1BVaA888pdNgxoBjJWQKCMiJRxjLbG972dH6cSC3ULwGK",
    "data": {
      "tx": "tx_+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4Zxbb8Q=",
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

### Acknowledger signed off-chain state responsse
 * **method:** `channels.update_ack`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | signed `channel_offchain` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "tx": "tx_+N8LAfhCuEAGx0qykrlj5/DVq6RJ2AsMe6uiCL4TX8Emv1sC3TL2IdDp9S3jrzRQnIe6gWtM/9kR++JRGwVL+gs+O7SjCKYIuJf4lTkBoQasBNkKrZJu+gk87ymFQsCsenQzLt8Fb1JKm0n7nKzTYgL4TbhL+EmCAjoBoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZqEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oQBoNUqd4GTOFacRsLar0VqTNSHraQXvmyQrL/MBqX090LhNHGU2A=="
  }
}
```

### Update conflict
 * **method:** `channels.conflict`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | channel_id | string | channel id| Yes |
  | data | object | description of the last co-signed state | Yes |

 * **data:**
  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | channel_id | string | channel id| Yes |
  | round | object | the round of the last co-signed state | Yes |

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

### Depositor receives unsigned deposit transaction
 * **method:** `channels.sign.deposit_tx`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | channel_id | string | channel ID | Yes |
  | data | object | deposit data | Yes |

 * **data:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | unsigned `channel_deposit` transaction | Yes |
  | updates | list | off-chain updates | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_tx",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "tx": "tx_+HIzAaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgWhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAgCGEjCc5UAAoIGnTOuUnVM9QThcVqCCAFeJ51D7a6A4ldyhd3nuKg7lAglKqnZP",
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

### Depositor signed deposit response
 * **method:** `channels.deposit_tx`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | signed `channel_deposit` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_tx",
  "params": {
    "tx": "tx_+LwLAfhCuEBpdn6/h5FeyYL9/JMO3XqEDdmaxrtsqamG4XJJAUNoQI0DtzQVkGHWC4lia9rcsNa9vdBj0a5o8S7fGE3I8Z0FuHT4cjMBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACggadM65SdUz1BOFxWoIIAV4nnUPtroDiV3KF3ee4qDuUCCYBI8r0="
  }
}
```

### Acknowledger receives unsigned deposit transaction
 * **method:** `channels.sign.deposit_ack`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | channel_id | string | channel ID | Yes |
  | data | object | deposit data | Yes |

 * **data:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | unsigned `channel_deposit` transaction | Yes |
  | updates | list | off-chain updates | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.deposit_ack",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "tx": "tx_+HIzAaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgWhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAgCGEjCc5UAAoIGnTOuUnVM9QThcVqCCAFeJ51D7a6A4ldyhd3nuKg7lAglKqnZP",
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

### Acknowledger signed deposit responsse
 * **method:** `channels.deposit_ack`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | signed `channel_deposit` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.deposit_ack",
  "params": {
    "tx": "tx_+LwLAfhCuEBa3V9ZXezm+ya0GQGg7RBpS6DbYhiE10oRgSuHpn0JFsdcUz0f2Ldsi1I62JxkLmDAqhxIgYUeya0PP1M4PXsOuHT4cjMBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACggadM65SdUz1BOFxWoIIAV4nnUPtroDiV3KF3ee4qDuUCCXv07Q4="
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

### Withdrawer receives unsigned withdraw transaction
 * **method:** `channels.sign.withdraw_tx`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | channel_id | string | channel ID | Yes |
  | data | object | withdrawal data | Yes |

 * **data:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | unsigned `channel_withdraw` transaction | Yes |
  | updates | list | off-chain updates | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_tx",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "tx": "tx_+HI0AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgWhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAgCGEjCc5UAAoEUfp6Gv3gLYNHIy08ITGVY9Xv7I69D5Yu0FUzyRePtuBAqOT2uR",
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

### Withdrawer signed withdraw response
 * **method:** `channels.withdraw_tx`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | signed `channel_withdraw` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_tx",
  "params": {
    "tx": "tx_+LwLAfhCuECmn6QR8/VwIvc9avwtzuauqSn0NmmDZxYud6Oik+Q0pp6Lev/oK++PdEvZciumZpUbBdlfl3LIqHxc31+43NINuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACgRR+noa/eAtg0cjLTwhMZVj1e/sjr0Pli7QVTPJF4+24ECi9pymI="
  }
}
```

### Acknowledger receives unsigned withdraw transaction
 * **method:** `channels.sign.withdraw_ack`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | channel_id | string | channel ID | Yes |
  | data | object | withdrawal data | Yes |

 * **data:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | unsigned `channel_withdraw` transaction | Yes |
  | updates | list | off-chain updates | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.withdraw_ack",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "tx": "tx_+HI0AaEGgofGx556dTISqbS/e2tCp1ROCgootioM4FHvduCHbgWhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmAgCGEjCc5UAAoEUfp6Gv3gLYNHIy08ITGVY9Xv7I69D5Yu0FUzyRePtuBAqOT2uR",
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

### Acknowledger signed withdraw responsse
 * **method:** `channels.withdraw_ack`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | signed `channel_withdraw` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.withdraw_ack",
  "params": {
    "tx": "tx_+LwLAfhCuEBWNxnIoMVbGTp+NkKKg8NlXbgVe7PbdpiTBsq0qGD3gwDE4waZEjmlWUJKVi3VxHbmdhdKdZ1lFKkVtBfMM3YEuHT4cjQBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACgRR+noa/eAtg0cjLTwhMZVj1e/sjr0Pli7QVTPJF4+24ECjOLPuM="
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

### Contract create from on-chain contract

 * **method:** `channels.update.new_contract_from_onchain`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | contract | contract id | on-chain contract id | Yes |
  | call\_data | call data | call data for contract creation | Yes |
  | deposit | integer | contract creation deposit | Yes |

#### Example

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.new_contract_from_onchain",
  "params": {
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACC5yVbyizFJqfWYeqUF89obIgnMVzkjQAYrtsG9n5+Z6gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAnHQYrA==",
    "contract": "ct_26WLX27MDif5WcqBXX8ndnQ2TQQvLgZ4TfL299BmteioZsJYER",
    "deposit": 10
  }
}
```

### Contract call

 * **method:** `channels.update.call_contract`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | contract | contract id | contract to call | Yes |
  | call\_data | call data | call data | Yes |
  | abi\_version | integer | call abi version | Yes |
  | amount | integer | amount of tokens to transfer to contract | Yes |

#### Example

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update.call_contract",
  "params": {
    "abi_version": 1,
    "amount": 0,
    "call_data": "cb_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBo8mdjOP9QiDmrpHdJ7/qL6H7yhPIH+z2ZmHAc1TiHxQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACo7dbVl",
    "contract": "ct_2Yy7TpPUs7SCm9jkCz7vz3nkb18zs78vcuVQGbgjRaWQNTWpm5"
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
  | tx | string | unsigned `channel_close_mutual` transaction | Yes |
  | updates | list | off-chain updates | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign",
  "params": {
    "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
    "data": {
      "tx": "tx_+F01AaEGXfP3k2aiLfV2X4HR75EK/1UzKSNqQqHHe0CN8/jQc6GhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmhjaR1q+//4YbSOtX4AEAhhIwnOVAAAWwHvpF",
      "updates": []
    }
  },
  "version": 1
}
```

### Closer returns signed mutual close
 * **method:** `channels.shutdown_sign`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | signed `channel_close_mutual` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign",
  "params": {
    "tx": "tx_+KcLAfhCuEC1uzCpbr9f7MYnkb5u/iL9okyhJTcRMGlTIqgMsari9Kdomn+Z+P3FmcAw1ma4GENBPYF/hl/X9EJi1fktkKAOuF/4XTUBoQZd8/eTZqIt9XZfgdHvkQr/VTMpI2pCocd7QI3z+NBzoaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGNpHWr7//hhtI61fgAQCGEjCc5UAABc176hQ="
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
  | tx | string | unsigned `channel_close_mutual` transaction | Yes |
  | updates | list | off-chain updates | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.shutdown_sign_ack",
  "params": {
    "channel_id": "ch_iNuPMRW1pCL17hXT8nHQgW1vMKfpBdsvztuYdM2VpPRh8PYVP",
    "data": {
      "tx": "tx_+F01AaEGXfP3k2aiLfV2X4HR75EK/1UzKSNqQqHHe0CN8/jQc6GhAbG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmhjaR1q+//4YbSOtX4AEAhhIwnOVAAAWwHvpF",
      "updates": []
    }
  },
  "version": 1
}
```

### Acknowledger returns signed mutual close
 * **method:** `channels.shutdown_sign_ack`
 * **params:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | signed `channel_close_mutual` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.shutdown_sign_ack",
  "params": {
    "tx": "tx_+KcLAfhCuEA2hK6nlhTF+hVjLYYoh09xVn5M4BrSwB3dXyjteMotYj8/+WpdbJwvO1KBUsg2p2zedlZnnVfR5g7O4m1q9OkOuF/4XTUBoQZd8/eTZqIt9XZfgdHvkQr/VTMpI2pCocd7QI3z+NBzoaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGNpHWr7//hhtI61fgAQCGEjCc5UAABY9XDr0="
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
  | tx | string | co-signed transaction that is posted on-chain | Yes |
  | updates | list | off-chain updates | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.on_chain_tx",
  "params": {
    "channel_id": "ch_zVDx935M1AogqZrNmn8keST2jH8uvn5kmWwtDqefYXvgcCRAX",
    "data": {
      "tx": "tx_+P4LAfiEuEBa3V9ZXezm+ya0GQGg7RBpS6DbYhiE10oRgSuHpn0JFsdcUz0f2Ldsi1I62JxkLmDAqhxIgYUeya0PP1M4PXsOuEBpdn6/h5FeyYL9/JMO3XqEDdmaxrtsqamG4XJJAUNoQI0DtzQVkGHWC4lia9rcsNa9vdBj0a5o8S7fGE3I8Z0FuHT4cjMBoQaCh8bHnnp1MhKptL97a0KnVE4KCii2KgzgUe924IduBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YCAIYSMJzlQACggadM65SdUz1BOFxWoIIAV4nnUPtroDiV3KF3ee4qDuUCCZiFbkw="
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
 | tx | string | unsigned `channel_close_solo` transaction | Yes |
 | updates | list | off-chain updates | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.close_solo_sign",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "tx": "tx_+QGfNgGhBnHSbcHwBwtR5QRwS0O1mI1Gw/8pkaOwcHQap09BPoMFoQGxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZoC5AUz5AUk8AfkBP/kBPKAeoRWJfw9r7+McQQHdwLN6tS/aqbQUwm8iJYXMIOcncfkBGPh0oB6hFYl/D2vv4xxBAd3As3q1L9qptBTCbyIlhcwg5ydx+FGAgICAgICg7QIWPGJsh916G7zCAZpUeaRQuGVamwjR8JaxQKEPIwmAgICAoEJmfgNwrMeYsFATTDpQ+Y9abOcHR6KUvw5o9LdShJsUgICAgID4T6BCZn4DcKzHmLBQE0w6UPmPWmznB0eilL8OaPS3UoSbFO2gMbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aLygoBAIY/qiUiX//4T6DtAhY8YmyH3XobvMIBmlR5pFC4ZVqbCNHwlrFAoQ8jCe2gNxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAHAwMDAwACGG0jrV+AACPykTFA=",
      "updates": []
    }
  },
  "version": 1
}
```

### Closer returns signed solo close
 * **method:** `channels.close_solo_sign`
 * **params:**
 
 | Name | Type | Description | Required |
 | ---- | ---- | ----------- | -------- |
 | tx | string | signed `channel_close_solo` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.close_solo_sign",
  "params": {
    "tx": "tx_+QHrCwH4QrhACuHMgbcTg1inUPAUSmhXfODKWI2CFchqpav9VDaBlw+xng9Ld0eLPgysTvks47iVHn4d/11VlkEi6iLRBDkIBLkBovkBnzYBoQZx0m3B8AcLUeUEcEtDtZiNRsP/KZGjsHB0GqdPQT6DBaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aAuQFM+QFJPAH5AT/5ATygHqEViX8Pa+/jHEEB3cCzerUv2qm0FMJvIiWFzCDnJ3H5ARj4dKAeoRWJfw9r7+McQQHdwLN6tS/aqbQUwm8iJYXMIOcncfhRgICAgICAoO0CFjxibIfdehu8wgGaVHmkULhlWpsI0fCWsUChDyMJgICAgKBCZn4DcKzHmLBQE0w6UPmPWmznB0eilL8OaPS3UoSbFICAgICA+E+gQmZ+A3Csx5iwUBNMOlD5j1ps5wdHopS/Dmj0t1KEmxTtoDG1d7zTJ8s55V5sAmvWp0obNd5sBlDErlHvq3WeQVtmi8oKAQCGP6olIl//+E+g7QIWPGJsh916G7zCAZpUeaRQuGVamwjR8JaxQKEPIwntoDccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6Ei8oKAQCGJGE5yoABwMDAwMAAhhtI61fgAAiybuMt"
  }
}
```

## Settle
Roles:
 * Settler

### Settler initiates settle
 * **method:** `channels.settle`

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
 | tx | string | unsigned `channel_settle` transaction | Yes |
 | updates | list | off-chain updates | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.settle_sign",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "tx": "tx_+F04AaEGcdJtwfAHC1HlBHBLQ7WYjUbD/ymRo7BwdBqnT0E+gwWhAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6Ehj+qJSJf/4YkYTnKgAEAhhtI61fgAAIwYkCX",
      "updates": []
    }
  },
  "version": 1
}
```
### Settler returns signed settle
 * **method:** `channels.settle_sign`
 * **params:**
 
 | Name | Type | Description | Required |
 | ---- | ---- | ----------- | -------- |
 | tx | string | signed `channel_settle` transaction | Yes |

#### Example
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.settle_sign",
  "params": {
    "tx": "tx_+KcLAfhCuEBdI4Uesh3hYjGQ2BAo0FzD1YPyZlzhy8HyNgf7OzrQdVM44oWQX0yFtmk31HaSLuIJGNDv3hEgdLwe0iZz3LEEuF/4XTgBoQZx0m3B8AcLUeUEcEtDtZiNRsP/KZGjsHB0GqdPQT6DBaEBZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSGP6olIl//hiRhOcqAAQCGG0jrV+AAAgurGvs="
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
  | state | string | co-signed last state transaction | Yes |

#### Example

```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.leave",
  "params": {
    "channel_id": "ch_s8RwBYpaPCPvUxvDsoLxH9KTgSV6EPGNjSYHfpbb4BL4qudgR",
    "data": {
      "state": "tx_+QENCwH4hLhAP+EiPpXFO80MdqGnw6GkaAYpOHCvcP/KBKJZ5IIicYBItA9s95zZA+RX1DNNheorlbZYKHctN3ZyvKnsFa7HDrhAYqWNrW8oDAaLj0JCUeW0NfNNhs4dKDJoHuuCdWhnX4r802c5ZAFKV7EV/mHihVXzgLyaRaI/SVw2KS+z471bAriD+IEyAaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2aGP6olImAAoQFnHFVGRklFdbK0lPZRaCFxBmPYSJPN0tI2A3pUwz7uhIYkYTnKgAACCgCGEjCc5UAAwKCjPk7CXWjSHTO8V2Y9WTad6D/5sB8yCR8WumWh0WxWvwdz6zEk"
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
 | `half_signed_tx` | channel latest half signed tx or `''` if equal to latest signed tx |
 | `signed_tx` | channel latest fully signed tx or `''` if not available |

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
    "signed_tx": "tx_+QEhCwH4hLhABTr2vMSsofbc3iKbPU7pvPbuMU7209MqJGy57u/CpyCusGUWYmJcKwbo1BEINLd07nfQVw5+aCsJ5HSYs5gNBrhABsdKspK5Y+fw1aukSdgLDHurogi+E1/BJr9bAt0y9iHQ6fUt4680UJyHuoFrTP/ZEfviURsFS/oLPju0owimCLiX+JU5AaEGrATZCq2SbvoJPO8phULArHp0My7fBW9SSptJ+5ys02IC+E24S/hJggI6AaEBsbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2ahAWccVUZGSUV1srSU9lFoIXEGY9hIk83S0jYDelTDPu6EAaDVKneBkzhWnEbC2q9FakzUh62kF75skKy/zAal9PdC4ffJBsU=",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaCxtXe80yfLOeVebAJr1qdKGzXebAZQxK5R76t1nkFbZovKCgEAhj+qJSJf/rDvQAGgZxxVRkZJRXWytJT2UWghcQZj2EiTzdLSNgN6VMM+7oSLygoBAIYkYTnKgAJXk16b"
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
      "ck_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAFSSB3aW4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACG5Hw1": "cv_sbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YlrDqa",
      "ck_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJbm8sIEkgd2luAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAD8NuDd": "cv_sbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YlrDqa",
      "ck_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMSSBjbGFpbSB0aGlzAAAAAAAAAAAAAAAAAAAAAAAAAACEEDl2": "cv_sbV3vNMnyznlXmwCa9anShs13mwGUMSuUe+rdZ5BW2YlrDqa",
      "ck_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAArMtts": "cv_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPE19M0=",
      "ck_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPJ9AW0": "cv_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAYAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAEAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAS0AfA=",
      "ck_ABQG4Fg=": "cv_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACDIq10LA12xQcUbe3+xpb7TFHBPbFVOWLUaz7/TKOGKmgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAJEZpbGwgbWUgaW4gd2l0aCBzb21ldGhpbmcgcmVhc29uYWJsZQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKcyIL",
      "ck_AZwSz9w=": "cv_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABIAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAWD//////////////////////////////////////////wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB4AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAyVHQH",
      "ck_AhzDreo=": "cv_AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAPJ9AW0"
    }
  },
  "version": 1
}
```
