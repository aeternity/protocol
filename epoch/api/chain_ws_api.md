[back](./README.md)
# Chain WebSocket API

The WebSocket API provides the following actions:
* [Get a block by height](#get-block-by-height)
* [Get a block by hash](#get-block-by-hash)
* [Get a header by height](#get-a-header-by-height)
* [Get a header by hash](#get-a-header-by-hash)
* [Receive a message when mining a block](#block-mined)

## Get block by height
### Request
 * **target:** `chain`
 * **action:** `get`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | type | string | `block` | Yes |
  | height | number | Height of the block to fetch | yes |

### Response
 * **origin:** `chain`
 * **action:** `requested_data`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | block | object - [block](#block) |  | Yes |
  | height | number | Height of the block to fetch | yes |
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
  | hash | string | Hash of the block to fetch | yes |

### Response
 * **origin:** `chain`
 * **action:** `requested_data`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | block | object - [block](#block) |  | Yes |
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
  | block | object - [header](#header) |  | Yes |
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
  | block | object - [header](#header) |  | Yes |
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


## Block mined
### Request
None

### Response
 * **origin:** `miner`
 * **action:** `mined_block`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | hash | string | Hash of the mined block | yes |
  | height | number | Height of the mined block | yes |

### Example
```
{"origin":"miner",
 "action":"mined_block",
  "payload":{"hash":"bh$2Tehbaf4QrmxCJHAnnHPxV5AvMwUe1ThpH7bvPpdfd5nEk1u31",
             "height":1
            }
}

```
