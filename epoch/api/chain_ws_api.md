[back](./README.md)
# Chain WebSocket API

The WebSocket API provides the following actions:
* [Get a block by height](#get-block-by-height)
* [Get a block by hash](#get-block-by-hash)
* [Get a header by height](#get-header-by-height)
* [Get a header by hash](#get-header-by-hash)
* [Subscribe to block chain events](#subscribe)
* [Unsubscribe to block chain events](#unsubscribe)
* [Receive an event when mining a block](#mined-block)
* [Receive an event when a block is added to the chain](#new-block)
* [Receive an event when a transaction is added to the chain](#tx_chain)

## Get block by height
### Request
 * **target:** `chain`
 * **action:** `get`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | type | string | `block` | Yes |
  | height | number | Height of the block to fetch | Yes |

### Response
 * **origin:** `chain`
 * **action:** `requested_data`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | block | object - [block](#block-structure) |  | Yes |
  | height | number | Height of the block to fetch | Yes |
  | type | string | `block` | Yes |

### Example
```
Request:
  {"target":"chain",
   "action":"get",
   "payload":{"type":"block",
              "height":1}
  }

Response:
  {"origin":"chain",
   "action":"requested_data",
   "tag":"untagged",
   "payload":{"height":1,
              "type":"block",
              "block":{"height":1,
                       "nonce":13295145107284252443,
                       "pow":[587,4075,4861,5296,5604,7432,7436,7859,8011,
                              8117,8266,8934,9102,9596,9908,10351,11373,
                              13143,13210,13273,13740,13958,15248,15725,
                              16253,18555,18921,21286,22160,22317,23419,
                              23493,25216,25251,27563,28052,28167,29140,
                              29784,31846,31870,32023],
                        "prev_hash":"bh$2FM7g2yCRf4jT4LCf9C9GMPpcGrXDh2hGkwNi1GDS3z8DkDC1q",
                        "state_hash":"bs$27Eij1X7r1TWpchxQ8QCB53AWcBf2KmrXoUh5G5vy9D2H8XkW8",
                        "target":553713663,
                        "time":1516707646911,
                        "transactions":[{"tx":"tx$cT6DAStjYG6BgLm3cL3WesxPwJgJ1CjK3roWw7UtwsqVyTCEzLvtGZLk6o1Ay1skL97FMZFpp6YHoGhaVoYJrRpXbzBUdwK3hwVRNXSJD4ZU1Bip2ak3nvcZRsuEREBdZgnYd1YuzNyWG2BQR4MFaear3x7vYGwwpo44SAKboGkJ8wWAYvysNziYQrQuVqGYRQ1j4kzscQUJWjRkmhLSoiX1EJQV8yGUuKixaG55o8LE6tbEyZaFtKjvApK6Eo"}],
                        "txs_hash": "bx$JYyCS2dnvFeMZtJcakmjF8W9gJTHL45SCYnsrKsfj9wTva3pB",
                        "version":4}
              }
  }
```

## Get block by hash
### Request
 * **target:** `chain`
 * **action:** `get`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | type | string | `block` | Yes |
  | hash | string | Hash of the block to fetch | Yes |

### Response
 * **origin:** `chain`
 * **action:** `requested_data`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | block | object - [block](#block-structure) |  | Yes |
  | hash | string | Hash of the block to fetch | yes |
  | type | string | `block` | Yes |

### Example
```
Request:
  {"target":"chain",
   "action":"get",
   "payload":{"type":"block",
              "hash":"bh$2Tehbaf4QrmxCJHAnnHPxV5AvMwUe1ThpH7bvPpdfd5nEk1u31"}
  }

Response:
  {"origin":"chain",
   "action":"requested_data",
   "tag":"untagged",
   "payload":{"hash":"bh$2Tehbaf4QrmxCJHAnnHPxV5AvMwUe1ThpH7bvPpdfd5nEk1u31",
              "type":"block",
              "block":{"height":1,
                       "nonce":13295145107284252443,
                       "pow":[587,4075,4861,5296,5604,7432,7436,7859,8011,
                              8117,8266,8934,9102,9596,9908,10351,11373,
                              13143,13210,13273,13740,13958,15248,15725,
                              16253,18555,18921,21286,22160,22317,23419,
                              23493,25216,25251,27563,28052,28167,29140,
                              29784,31846,31870,32023],
                        "prev_hash":"bh$2FM7g2yCRf4jT4LCf9C9GMPpcGrXDh2hGkwNi1GDS3z8DkDC1q",
                        "state_hash":"bs$27Eij1X7r1TWpchxQ8QCB53AWcBf2KmrXoUh5G5vy9D2H8XkW8",
                        "target":553713663,
                        "time":1516707646911,
                        "transactions":[{"tx":"tx$cT6DAStjYG6BgLm3cL3WesxPwJgJ1CjK3roWw7UtwsqVyTCEzLvtGZLk6o1Ay1skL97FMZFpp6YHoGhaVoYJrRpXbzBUdwK3hwVRNXSJD4ZU1Bip2ak3nvcZRsuEREBdZgnYd1YuzNyWG2BQR4MFaear3x7vYGwwpo44SAKboGkJ8wWAYvysNziYQrQuVqGYRQ1j4kzscQUJWjRkmhLSoiX1EJQV8yGUuKixaG55o8LE6tbEyZaFtKjvApK6Eo"}],
                        "txs_hash": "bx$JYyCS2dnvFeMZtJcakmjF8W9gJTHL45SCYnsrKsfj9wTva3pB",
                        "version":4}
              }
  }
```

## Get header by height
### Request
 * **target:** `chain`
 * **action:** `get`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | type | string | `header` | Yes |
  | height | number | Height of the header to fetch | yes |

### Response
 * **origin:** `chain`
 * **action:** `requested_data`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | block | object - [header](#header-structure) |  | Yes |
  | height | number | Height of the header to fetch | yes |
  | type | string | `header` | Yes |

### Example
```
Request:
  {"target":"chain",
   "action":"get",
   "payload":{"type":"header",
              "height":1}
  }

Response:
  {"origin":"chain",
   "action":"requested_data",
   "tag":"untagged",
   "payload":{"height":1,
              "type":"header",
              "block":{"height":1,
                       "nonce":13295145107284252443,
                       "pow":[587,4075,4861,5296,5604,7432,7436,7859,8011,
                              8117,8266,8934,9102,9596,9908,10351,11373,
                              13143,13210,13273,13740,13958,15248,15725,
                              16253,18555,18921,21286,22160,22317,23419,
                              23493,25216,25251,27563,28052,28167,29140,
                              29784,31846,31870,32023],
                        "prev_hash":"bh$2FM7g2yCRf4jT4LCf9C9GMPpcGrXDh2hGkwNi1GDS3z8DkDC1q",
                        "state_hash":"bs$27Eij1X7r1TWpchxQ8QCB53AWcBf2KmrXoUh5G5vy9D2H8XkW8",
                        "target":553713663,
                        "time":1516707646911,
                         "txs_hash": "bx$JYyCS2dnvFeMZtJcakmjF8W9gJTHL45SCYnsrKsfj9wTva3pB",
                         "version":4}
              }
  }
```

## Get header by hash
### Request
 * **target:** `chain`
 * **action:** `get`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | type | string | `header` | Yes |
  | hash | string | Hash of the header to fetch | yes |

### Response
 * **origin:** `chain`
 * **action:** `requested_data`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | block | object - [header](#header-structure) |  | Yes |
  | hash | string | Hash of the header to fetch | yes |
  | type | string | `header` | Yes |

### Example
```
Request:
  {"target":"chain",
   "action":"get",
   "payload":{"type":"header",
              "hash":"bh$2Tehbaf4QrmxCJHAnnHPxV5AvMwUe1ThpH7bvPpdfd5nEk1u31"}
  }

Response:
  {"origin":"chain",
   "action":"requested_data",
   "tag":"untagged",
   "payload":{"hash":"bh$2Tehbaf4QrmxCJHAnnHPxV5AvMwUe1ThpH7bvPpdfd5nEk1u31",
              "type":"header",
              "block":{"height":1,
                       "nonce":13295145107284252443,
                       "pow":[587,4075,4861,5296,5604,7432,7436,7859,8011,
                              8117,8266,8934,9102,9596,9908,10351,11373,
                              13143,13210,13273,13740,13958,15248,15725,
                              16253,18555,18921,21286,22160,22317,23419,
                              23493,25216,25251,27563,28052,28167,29140,
                              29784,31846,31870,32023],
                        "prev_hash":"bh$2FM7g2yCRf4jT4LCf9C9GMPpcGrXDh2hGkwNi1GDS3z8DkDC1q",
                        "state_hash":"bs$27Eij1X7r1TWpchxQ8QCB53AWcBf2KmrXoUh5G5vy9D2H8XkW8",
                        "target":553713663,
                        "time":1516707646911,
                         "txs_hash": "bx$JYyCS2dnvFeMZtJcakmjF8W9gJTHL45SCYnsrKsfj9wTva3pB",
                         "version":4}
              }
  }
```

## Subscribe
### Request
 * **target:** `chain`
 * **action:** `subscribe`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | type | string | Subscribe to events of `type` | Yes |
  | <type_arg> | string | Some events can be further specialised - see indiviual events | No |

### Response
 * **origin:** `chain`
 * **action:** `subscribe`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | result | string | `ok` or error reason | Yes |
  | subscribed_to | object - query subscribe payload | | Yes on success |

### Example
```
Request:
  {"target":"chain",
   "action":"subscribe",
   "payload":{"type":"oracle_query",
              "oracle_id":"ok$3jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdFtaJuxQvrR8VbbXExDPkCHFAei5q969JA6EayQpb8z5C3Mf"}
  }

Response:
  {"origin":"chain",
   "action":"subscribe",
   "tag":"untagged",
   "payload":{"result":"ok",
              "subscribed_to":{"type":"oracle_query",
                               "oracle_id":"ok$3jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdFtaJuxQvrR8VbbXExDPkCHFAei5q969JA6EayQpb8z5C3Mf"}}
  }
```

## Mined block
### Request
 * **target:** `chain`
 * **action:** `subscribe`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | type | string | `mined_block` | Yes |

### Event
 * **origin:** `chain`
 * **action:** `mined_block`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | hash | string | Hash of the mined block | Yes |
  | height | number | Height of the mined block | Yes |

### Example
```
Event:
{"origin":"chain",
 "action":"mined_block",
  "payload":{"hash":"bh$2Tehbaf4QrmxCJHAnnHPxV5AvMwUe1ThpH7bvPpdfd5nEk1u31",
             "height":1
            }
}

```

## New block
### Request
 * **target:** `chain`
 * **action:** `subscribe`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | type | string | `new_block` | Yes |

### Event
 * **origin:** `chain`
 * **action:** `new_block`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | hash | string | Hash of the mined block | Yes |
  | height | number | Height of the mined block | Yes |

### Example
```
Event:
{"origin":"chain",
 "action":"new_block",
  "payload":{"hash":"bh$2Tehbaf4QrmxCJHAnnHPxV5AvMwUe1ThpH7bvPpdfd5nEk1u31",
             "height":46
            }
}

```

## TX Chain
Get an event when a particular transaction is added to the blockchain.
### Request
 * **target:** `chain`
 * **action:** `subscribe`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | type | string | `tx_chain` | Yes |
  | tx_hash | string | Transaction Hash | Yes |

### Event
 * **origin:** `chain`
 * **action:** `tx_chain`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx_hash | string | Hash of the just added transaction | Yes |

### Example
```
Event:
{"origin":"chain",
 "action":"tx_chain",
  "payload":{"tx_hash":"th$2Tehbaf4QrmxCJHAnnHPxV5AvMwUe1ThpH7bvPpdfd5nEk1u31"
            }
}

```

## Unsubscribe
### Request
 * **target:** `chain`
 * **action:** `unsubscribe`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | type | string | Unsubscribe to events of `type` | Yes |
  | <type_arg> | string | Some events can be further specialised - see indiviual events | No |

### Response
 * **origin:** `chain`
 * **action:** `unsubscribe`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | result | string | `ok` or error reason | Yes |
  | subscribed_to | object - query unsubscribe payload | | Yes on success |

### Example
```
Request:
  {"target":"chain",
   "action":"unsubscribe",
   "payload":{"type":"oracle_query",
              "oracle_id":"ok$3jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdFtaJuxQvrR8VbbXExDPkCHFAei5q969JA6EayQpb8z5C3Mf"}
  }

Response:
  {"origin":"chain",
   "action":"unsubscribe",
   "tag":"untagged",
   "payload":{"result":"ok",
              "subscribed_to":{"type":"oracle_query",
                               "oracle_id":"ok$3jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdFtaJuxQvrR8VbbXExDPkCHFAei5q969JA6EayQpb8z5C3Mf"}}
  }
```

## Data types
### Header structure

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | height | number | Height of the block | Yes |
  | nonce | number | Block nonce | Yes |
  | pow | [number] | Block proof of work | No |
  | prev_hash | string | Hash of the previous block | No |
  | state_hash | string | Hash of the root of the state tree | Yes |
  | target | number  | Threshold below which the hash of the Cuckoo Cycle PoW solution must be | Yes |
  | time | number | Block mining time | Yes |
  | txs_hash | string | Root hash of the Merkle tree of transactions included in this block | No |
  | version | number | Version of the block structure | Yes |

### Block structure
A block consists of a header part and a list of transactions. [The header](#header-structure) is descibed in the section above.

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | transactions | [[transaction](#transaction-structure)] | List of transactions included in the block | No |

**Note:** Genesis block lacks `transactions` and thus - `txs_hash`. Since it
is the first block - it doesn't have `prev_hash`, too.

### Transaction structure
  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | MessagePack encoded transaction object | Yes |

