[back](./README.md)
# Chain WebSocket API

The WebSocket API provides the following actions:
* [Get a block by hash](#get-block-by-hash)
* [Get a header by hash](#get-header-by-hash)
* [Subscribe to block chain events](#subscribe)
* [Unsubscribe from block chain events](#unsubscribe)
* [Receive an event when mining a key block](#mined-key-block)
* [Receive an event when adding a micro block](#added-micro-block)
* [Receive an event when a block is added to the chain](#new-block)
* [Receive an event when a transaction is added to the chain](#tx_chain)

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
  | hash | string | Hash of the block to fetch | Yes |
  | type | string | `block` | Yes |

### Examples
```
Request:
  {"target":"chain",
   "action":"get",
   "payload":{"type":"block",
              "hash":"kh$2Tehbaf4QrmxCJHAnnHPxV5AvMwUe1ThpH7bvPpdfd5nEk1u31"}
  }

Response:
  {"origin":"chain",
   "action":"requested_data",
   "tag":"untagged",
   "payload":{"hash":"kh$2Tehbaf4QrmxCJHAnnHPxV5AvMwUe1ThpH7bvPpdfd5nEk1u31",
              "type":"block",
              "block":{"height":1,
                       "beneficiary":"ak$2evAxTKozswMyw9kXkvjJt3MbomCR1nLrf91BduXKdJLrvaaZt",
                       "miner":"ak$2YifF1Ba6pt29epYdCpYJmBFCNYWDM7brLQsNgpXUVUuoq1WA3",
                       "nonce":13295145107284252443,
                       "pow":[587,4075,4861,5296,5604,7432,7436,7859,8011,
                              8117,8266,8934,9102,9596,9908,10351,11373,
                              13143,13210,13273,13740,13958,15248,15725,
                              16253,18555,18921,21286,22160,22317,23419,
                              23493,25216,25251,27563,28052,28167,29140,
                              29784,31846,31870,32023],
                       "prev_hash":"mh$2FM7g2yCRf4jT4LCf9C9GMPpcGrXDh2hGkwNi1GDS3z8DkDC1q",
                       "state_hash":"bs$27Eij1X7r1TWpchxQ8QCB53AWcBf2KmrXoUh5G5vy9D2H8XkW8",
                       "target":553713663,
                       "time":1516707646911,
                       "version":15}
              }
  }
```

```
Request:
  {"target":"chain",
   "action":"get",
   "payload":{"type":"block",
              "hash":"mh$2cNz9iRZofBFKVZwipREk34o2YqS7HnBjzySzzBgRKR2xtqKpi"}
  }

Response:
  {"origin":"chain",
   "action":"requested_data",
   "tag":"untagged",
   "payload":{"hash":"mh$2cNz9iRZofBFKVZwipREk34o2YqS7HnBjzySzzBgRKR2xtqKpi",
              "type":"block",
              "block":{"height":1,
                       "prev_hash":"kh$2Tehbaf4QrmxCJHAnnHPxV5AvMwUe1ThpH7bvPpdfd5nEk1u31",
                       "signature":[239,191,189,239,191,189,73,107,239,191,189,20,
                                    83,239,191,189,93,239,191,189,56,101,239,191,
                                    189,239,191,189,239,191,189,239,191,189,123,
                                    86,239,191,189,239,191,189,239,191,189,239,
                                    191,189,65,239,191,189,97,20,239,191,189,239,
                                    191,189,239,191,189,239,191,189,58,120,83,239,
                                    191,189,215,171,50,211,138,239,191,189,97,43,
                                    239,191,189,127,18,239,191,189,239,191,189,67,
                                    112,239,191,189,239,191,189,39,239,191,189,62,
                                    239,191,189,239,191,189,239,191,189,239,191,
                                    189,0],
                       "state_hash":"bs$U5dTs9FbUsEaX5Sz1HuFxiZbEAAW5wz3B9mDghCpTu14CJhCD",
                       "time":1516707646920,
                       "transactions":[{"tx":"tx$cT6DAStjYG6BgLm3cL3WesxPwJgJ1CjK3roWw7UtwsqVyTCEzLvtGZLk6o1Ay1skL97FMZFpp6YHoGhaVoYJrRpXbzBUdwK3hwVRNXSJD4ZU1Bip2ak3nvcZRsuEREBdZgnYd1YuzNyWG2BQR4MFaear3x7vYGwwpo44SAKboGkJ8wWAYvysNziYQrQuVqGYRQ1j4kzscQUJWjRkmhLSoiX1EJQV8yGUuKixaG55o8LE6tbEyZaFtKjvApK6Eo"}],
                       "txs_hash": "bx$JYyCS2dnvFeMZtJcakmjF8W9gJTHL45SCYnsrKsfj9wTva3pB",
                       "version":15}
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
  | hash | string | Hash of the header to fetch | Yes |

### Response
 * **origin:** `chain`
 * **action:** `requested_data`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | block | object - [header](#block-structure) |  | Yes |
  | hash | string | Hash of the header to fetch | Yes |
  | type | string | `header` | Yes |

### Examples
```
Request:
  {"target":"chain",
   "action":"get",
   "payload":{"type":"header",
              "hash":"kh$2Tehbaf4QrmxCJHAnnHPxV5AvMwUe1ThpH7bvPpdfd5nEk1u31"}
  }

Response:
  {"origin":"chain",
   "action":"requested_data",
   "tag":"untagged",
   "payload":{"hash":"kh$2Tehbaf4QrmxCJHAnnHPxV5AvMwUe1ThpH7bvPpdfd5nEk1u31",
              "type":"block",
              "block":{"height":1,
                       "beneficiary":"ak$2evAxTKozswMyw9kXkvjJt3MbomCR1nLrf91BduXKdJLrvaaZt",
                       "miner":"ak$2YifF1Ba6pt29epYdCpYJmBFCNYWDM7brLQsNgpXUVUuoq1WA3",
                       "nonce":13295145107284252443,
                       "pow":[587,4075,4861,5296,5604,7432,7436,7859,8011,
                              8117,8266,8934,9102,9596,9908,10351,11373,
                              13143,13210,13273,13740,13958,15248,15725,
                              16253,18555,18921,21286,22160,22317,23419,
                              23493,25216,25251,27563,28052,28167,29140,
                              29784,31846,31870,32023],
                       "prev_hash":"mh$2FM7g2yCRf4jT4LCf9C9GMPpcGrXDh2hGkwNi1GDS3z8DkDC1q",
                       "state_hash":"bs$27Eij1X7r1TWpchxQ8QCB53AWcBf2KmrXoUh5G5vy9D2H8XkW8",
                       "target":553713663,
                       "time":1516707646911,
                       "version":15}
              }
  }
```

```
Request:
  {"target":"chain",
   "action":"get",
   "payload":{"type":"block",
              "hash":"mh$2cNz9iRZofBFKVZwipREk34o2YqS7HnBjzySzzBgRKR2xtqKpi"}
  }

Response:
  {"origin":"chain",
   "action":"requested_data",
   "tag":"untagged",
   "payload":{"hash":"mh$2cNz9iRZofBFKVZwipREk34o2YqS7HnBjzySzzBgRKR2xtqKpi",
              "type":"block",
              "block":{"height":1,
                       "prev_hash":"kh$2Tehbaf4QrmxCJHAnnHPxV5AvMwUe1ThpH7bvPpdfd5nEk1u31",
                       "signature":[239,191,189,239,191,189,73,107,239,191,189,20,
                                    83,239,191,189,93,239,191,189,56,101,239,191,
                                    189,239,191,189,239,191,189,239,191,189,123,
                                    86,239,191,189,239,191,189,239,191,189,239,
                                    191,189,65,239,191,189,97,20,239,191,189,239,
                                    191,189,239,191,189,239,191,189,58,120,83,239,
                                    191,189,215,171,50,211,138,239,191,189,97,43,
                                    239,191,189,127,18,239,191,189,239,191,189,67,
                                    112,239,191,189,239,191,189,39,239,191,189,62,
                                    239,191,189,239,191,189,239,191,189,239,191,
                                    189,0],
                       "state_hash":"bs$U5dTs9FbUsEaX5Sz1HuFxiZbEAAW5wz3B9mDghCpTu14CJhCD",
                       "time":1516707646920,
                       "txs_hash": "bx$JYyCS2dnvFeMZtJcakmjF8W9gJTHL45SCYnsrKsfj9wTva3pB",
                       "version":15}
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
              "oracle_id":"ok$jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdF"}
  }

Response:
  {"origin":"chain",
   "action":"subscribe",
   "tag":"untagged",
   "payload":{"result":"ok",
              "subscribed_to":{"type":"oracle_query",
                               "oracle_id":"ok$jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdF"}}
  }
```

## Mined key block
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
  | hash | string | Hash of the mined key block | Yes |
  | height | number | Height of the mined key block | Yes |

### Example
```
Event:
{"origin":"chain",
 "action":"mined_block",
  "payload":{"hash":"kh$2Tehbaf4QrmxCJHAnnHPxV5AvMwUe1ThpH7bvPpdfd5nEk1u31",
             "height":1
            }
}

```

## Added micro block
### Request
 * **target:** `chain`
 * **action:** `subscribe`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | type | string | `added_micro_block` | Yes |

### Event
 * **origin:** `chain`
 * **action:** `added_micro_block`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | hash | string | Hash of the added micro block | Yes |
  | height | number | Height of the added micro block | Yes |

### Example
```
Event:
{"origin":"chain",
 "action":"added_micro_block",
  "payload":{"hash":"mh$2cNz9iRZofBFKVZwipREk34o2YqS7HnBjzySzzBgRKR2xtqKpi",
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
  | hash | string | Hash of the mined key block or added micro block | Yes |
  | height | number | Height of the mined key block or added micro block | Yes |

### Example
```
Event:
{"origin":"chain",
 "action":"new_block",
  "payload":{"hash":"kh$2Tehbaf4QrmxCJHAnnHPxV5AvMwUe1ThpH7bvPpdfd5nEk1u31",
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
              "oracle_id":"ok$jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdF"}
  }

Response:
  {"origin":"chain",
   "action":"unsubscribe",
   "tag":"untagged",
   "payload":{"result":"ok",
              "subscribed_to":{"type":"oracle_query",
                               "oracle_id":"ok$jzZyCLFtHVD7yVdEhGJFM3LjeXrKqWxnHbCYzhnrrR4DkdF"}}
  }
```

## Data types
### Block structure
A block can be either a key block or a micro block. [The key block](#key-block-structure) does not include any transactions. The micro block consists of a [header](#micro-block-header-structure) and a list of transactions.

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | transactions | [[transaction](#transaction-structure)] | List of transactions included in the block | No |

**Note:** Genesis block lacks transactions and thus - `txs_hash`. Since it
is the first block - it doesn't have `prev_hash`, too.

### Transaction structure
  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | MessagePack encoded transaction object | Yes |

### Key block structure

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | height | number | Height of the block | Yes |
  | prev_hash | string | Hash of the previous block | Yes |
  | state_hash | string | Hash of the root of the state tree | Yes |
  | beneficiary | string | Public key of the beneficiary | Yes |
  | miner | string | Public key of the miner that mined this block | Yes |
  | target | number  | Threshold below which the hash of the Cuckoo Cycle PoW solution must be | Yes |
  | pow | [number] | Block proof of work | Yes |
  | nonce | number | Block nonce | Yes |
  | time | number | Block mining time | Yes |
  | version | number | Version of the block structure | Yes |

### Micro block header structure

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | height | number | Height of the block | Yes |
  | prev_hash | string | Hash of the previous block | Yes |
  | state_hash | string | Hash of the root of the state tree | Yes |
  | txs_hash | string | Root hash of the Merkle tree of transactions included in this block | Yes |
  | time | number | Block mining time | Yes |
  | version | number | Version of the block structure | Yes |

