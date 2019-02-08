[back](./README.md)
# State channel WebSocket API

The WebSocket API provides the following actions:
 * [Off-chain update](#update)
 * [On-chain deposit](#deposit)
 * [On-chain withdrawal](#withdrawal)
 * [Generic message](#generic-message)
 * [Close mutual](#close-mutual)
 * [Leave](#leave)
 * [On-chain transactions](#on-chain-transactions)
 * [Info messages](#info-messages)

## Update
Roles:
 * Sender
 * Acknowledger

### Sender trigger an update
 * **action:** `update`
 * **tag** `new`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | from | string | Participant's account to take tokens from | Yes |
  | to | string | Participant's account to add tokens to | Yes |
  | amount | integer | Amount of tokens to transfer | Yes |

#### Example
```javascript
{'action': 'update',
 'tag': 'new',
 'payload': {
    'from': 'ak_3YGRJv1QMgNbeDzvqX7qJrZWJDaHGmrHYHifxSbhSEgn6anuNYCNPrzsB911xTbZ35bvJYWLyYjrQaQKfvja9gkpvYMfEZ',
    'to': 'ak_3gVuduh7vR9G7Hq3TpFaA7q9oQkMZZF2VsUxDYZabNeKC1uaqtjpKSth7wPn9dxnUzsHoT2fa6GPUzepbDXMHyC2F3HupT',
    'amount': 2
    }
 }
```

### Sender receives unsigned off-chain state
 * **action:** `sign`
 * **tag** `update`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | unsigned `channel_offchain` transaction | Yes |

#### Example
```javascript
{'action': 'sign',
 'tag': 'update',
 'payload' {
    'tx': 'tx_21uV5so71tzLyBzTGBd5qd318n8Z33ninWoJzuBBKa3y3cLv8jL1gBsUpwoT1Wzs57fpxgxk7asMpuxcKpYxRnH1Qk679DjPUjLx3Lu6eNnPnfDwb4NpMq5tmm1Sq1j4MLfi6mFLadQ4CyuiENcytACQgkiU2CP8jWHKDCxAprKxP7EnXRKGbyaXkQRjvxmd5BK5XpnPHMoLb4zrrQfex5Wi8SkJjxWrhRyTr7u8jqyyebVPYmz3iRnnoEHfiECzBLdAYBz12U4VgUNrYug8C3ns5GcB1ytaUmggpDGY4K97dyYR8aMorFfqY6rPjwpRoL1BjbJgUBw54VVgMEijfeVCNcyw8wrVJnZeUAQKSesJcPhWShY717GVeQfGGHLzJhTY7iYBUUQCLfoVms86jJ3vMo1d9DpnahpCXfrZeR2PExg8Cn9DXc'}
}
```

### Sender signed off-chain state responsse
 * **action:** `update`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | signed `channel_offchain` transaction | Yes |

#### Example
```javascript
{'action': 'update',
 'payload': {
    'tx': 'tx_xCHADUvUikbjGRcBmioKtXFQKpGs7yZHvhkcjByxQDG5xnCpU6YVQs4qyBZL6h18xjTSy1wtUFe8ipKMHLp6VmU2KwLgd4mbUtqELz6w9wV6PGTex6ZS2y7TtqZsDuesGFTZqYET8syCor8kzGjemUkzvwHMJdKsQ5guDWj1C2EcuNR3MnK9heJLbKuf19peGDvijjS8zdCD1pxE4QcsVi9pAGUBCgFyKx8FkDzhv6LxjysuxdmuZqeTGq49s71QdVB74Y1DAQUq5JsH1kyhadFxVepS6FYmcBC4xK8h1sefipPAAVFY7YwNtj2W6U9CTCqSVAQSrpfGAo6322gSneD8aRKoGpQpy1NfxVePKqM5igmd1B6QDGcEYDigBzzNwrXpuYqjrdG5eB6C6ehwAxNskmiudbEuKrjwNL5JzExxrR21L5oQCDc3RMyPdeWJxs8eJfHCrWyzyAwsykV4hVGxddbsbrDWd3re42N5HARXpQG6Gq6aMGnSHJAKbXCWxys4Si6Wjpey7HyEgT1hYoxqtmwEGhW96Ksig'
    }
}
```

### Acknowledger receives unsigned off-chain state
 * **action:** `sign`
 * **tag** `update_ack`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | unsigned `channel_offchain` transaction | Yes |

#### Example
```javascript
{'action': 'sign',
 'tag': 'update_ack',
 'payload' {
    'tx': 'tx_21uV5so71tzLyBzTGBd5qd318n8Z33ninWoJzuBBKa3y3cLv8jL1gBsUpwoT1Wzs57fpxgxk7asMpuxcKpYxRnH1Qk679DjPUjLx3Lu6eNnPnfDwb4NpMq5tmm1Sq1j4MLfi6mFLadQ4CyuiENcytACQgkiU2CP8jWHKDCxAprKxP7EnXRKGbyaXkQRjvxmd5BK5XpnPHMoLb4zrrQfex5Wi8SkJjxWrhRyTr7u8jqyyebVPYmz3iRnnoEHfiECzBLdAYBz12U4VgUNrYug8C3ns5GcB1ytaUmggpDGY4K97dyYR8aMorFfqY6rPjwpRoL1BjbJgUBw54VVgMEijfeVCNcyw8wrVJnZeUAQKSesJcPhWShY717GVeQfGGHLzJhTY7iYBUUQCLfoVms86jJ3vMo1d9DpnahpCXfrZeR2PExg8Cn9DXc'}
}
```

### Acknowledger signed off-chain state responsse
 * **action:** `update_ack`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | signed `channel_offchain` transaction | Yes |

#### Example
```javascript
{'action': 'update_ack',
 'payload': {
    'tx': 'tx_xCHADUvUikbjGRcBmj4YQkTJGCoGV6JQVdJW2FU1ZAYGhdayeCZerGqPWbRz4Eduq1KtjUbBJgdxSF3UKyChKMXne3dEDnChRdiUop4HYkHJ8GF3xQpbSspvST5qPTJqvcCstQCDXmJMLiYiWQ2hoPXL3a1qiiVmSwx2ztVuVqsEf1NsQCbMiNeJj8Uvrcp2FKN8TG2VoMTBTiMcCdLGXhX31EaLYTTDVyFTXGgFRUTdAsHgBjcQzm9hgQS75QjhKY7VtyUBCisUEQp8Dcr76rpdT1Qy9n8JYKboPkFZpY9DVx9We2hstbP3fjgZVLgDRAvLoC5YppVE7GZgUbRp6PMmbPUyc3qFYaxA82g7TzndipqnrKuuGzDjoPaM2w5evx1TvXAF5u1beac2kW7kJyKjLfLhjKQ8bnwBwcZ3WpdRfCVe55LtPwYEoZQJtdzojjVcuLmgJjbb2GDHioi8KXTasHre5oZKwkyYByMqzDafVTMT3kJqvdQG6HKAm8XGP6LGRsZFcpkn5jGtGbq7PRpTbAn1RbHWvRAEH'
    }
}
```

### Update conflict
 * **action:** `conflict`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | channel_id | string | channel id| Yes |
  | round | integer | last correct state round | Yes |

#### Example
```javascript
{'action': 'conflict',
 'payload': {'channel_id': 'ch_WmpDbaiCs5roqRCL5KEKbpsDNJSbcbiUvt2cs1qyj4sM9HA3b',
             'round': 42
             }
}
```

### Update error
 * **action:** `error`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | reason | string | description of the error | Yes |
  | request | json | the failed request | Yes |

#### Example
```javascript
{'action': 'error',
 'payload': {'reason': 'insufficient_balance',
             'request': {'action': 'update',
                         'payload': {'amount': 10000,
                                     'from': 'ak_4Kr76woCtc3ehZ45K1sCrmgKX6gnh7qGhjSU1GZYqfLTTjtCgn',
                                     'to': 'ak_35Wxqf2cbzQF5hEV1j9AdXQFTMxqKCwM7iMKNGcqSv47MXAj68'
                                     },
                          'tag': 'new'
                          }
              }
}
```

## Deposit
Roles:
 * Depositor
 * Acknowledger

### Depositor trigger a update
 * **action:** `deposit`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | amount | integer | Amount of tokens to deposit in the channel | Yes |

#### Example
```javascript
{'action': 'deposit',
 'payload': {
    'amount': 2
    }
 }
```

### Depositor receives unsigned deposit transaction
 * **action:** `sign`
 * **tag** `deposit_tx`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | unsigned `channel_deposit` transaction | Yes |

#### Example
```javascript
{'action': 'sign',
 'tag': 'deposit_tx',
 'payload' {
    'tx': 'tx_2C9es4FjJF3MtD1M3Np7tUzgCk8AE3ARVJe94Sxmh63feCNt2CekXvjLhBPS2i8pQ8JKGQfgzMQnvfntEdYmMYo7D1UP59UUQ31Bss5G1gz8sPhzmrx1cXCawF9eB27gjYVhTnaLXwUEqdJfHqfATuwLqJtc1p'}
}
```

### Depositor signed deposit response
 * **action:** `deposit_tx`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | signed `channel_deposit` transaction | Yes |

#### Example
```javascript
{'action': 'deposit_tx',
 'payload': {
    'tx': 'tx_i2WsEQsiC5XsnyKgLeXGW6b9ys87yoQzNB65csymQbK9AsuWApenk9ViHpzxb2oJwUCGiqzA1Cc1D6pJAjkLcQ6w3m8Bhvt41HSqtpSpEd1MciHMcFg1xsZG9CsPu1NUBey9EupgXFJtZ4caNMXcV4evV7ocBjzdBcJo5CUMQgapQZ8ajgUrPgfqQTb3Gq8FFCuHHaHytA7fTNik4KAAvyHiEDutXf1VJxXG2oYkpoNTQGuriV3g4Hxrms3r7LD8ko91'
    }
}
```

### Acknowledger receives unsigned deposit transaction
 * **action:** `sign`
 * **tag** `deposit_ack`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | unsigned `channel_deposit` transaction | Yes |

#### Example
```javascript
{'action': 'sign',
 'tag': 'deposit_ack',
 'payload' {
    'tx': 'tx_2WsEQsiC5Xso1aHppqY8EwniUa9demV2SAdrNckji4H5ZRDnakiMPAWRv4SSksecqXBCriNTTFg6c3dXK9TzmRV7DoqkKH68Vh7XbVGS7g9CQfaj46S8wgsFBdJtoBMnHV3xbbzSz36cMAAN3eosKaA74TMkgXWgrDCD619RnmskuyvArGbgy6fMFqSniG1s9a3WoTMLoFyw6ucpxgS523Dk3SQEbPAxznbL9KsBEjsCroe4HBVZZG5bX3LU8ZX9PUy'
}
```

### Acknowledger signed deposit responsse
 * **action:** `deposit_ack`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | signed `channel_deposit` transaction | Yes |

#### Example
```javascript
{'action': 'deposit_ack',
 'payload': {
    'tx': 'tx_2WsEQsiC5Xso1aHppqY8EwniUa9demV2SAdrNckji4H5ZRDnakiMPAWRv4SSksecqXBCriNTTFg6c3dXK9TzmRV7DoqkKH68Vh7XbVGS7g9CQfaj46S8wgsFBdJtoBMnHV3xbbzSz36cMAAN3eosKaA74TMkgXWgrDCD619RnmskuyvArGbgy6fMFqSniG1s9a3WoTMLoFyw6ucpxgS523Dk3SQEbPAxznbL9KsBEjsCroe4HBVZZG5bX3LU8ZX9PUy'
    }
}
```

## Withdrawal
Roles:
 * Withdrawer
 * Acknowledger

### Withdrawer trigger a update
 * **action:** `withdraw`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | amount | integer | Amount of tokens to withdraw form the channel | Yes |

#### Example
```javascript
{'action': 'withdraw',
 'payload': {
    'amount': 2
    }
 }
```

### Withdrawer receives unsigned withdraw transaction
 * **action:** `sign`
 * **tag** `withdraw_tx`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | unsigned `channel_withdraw` transaction | Yes |

#### Example
```javascript
{'action': 'sign',
 'tag': 'withdraw_tx',
 'payload' {
    'tx': 'tx_2C9estKT2f86WwC7LCa18cDTTmMCrXM7N2AcrXKmgnTo9DNchXjNmewbgNX2YW4RYk8iHkVRnPpeYLRgh6xH96mHNxCMW4aUL2hgTe6iqdrKyM5eqMbCN9YgTdDvUzDyASJwoicxXb7UeDF5kFWvsEMxXBKGX2'}
}
```

### Withdrawer signed withdraw response
 * **action:** `withdraw_tx`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | signed `channel_withdraw` transaction | Yes |

#### Example
```javascript
{'action': 'withdraw_tx',
 'payload': {
    'tx': 'tx_2WsEQsiC5Xsn85g88TmLYonFu2r8HT53jQPJ7f6Ai9uvnZGwnExRyJ51nHS2mU4g2FUTf2PHUsgs22X5Nwg1E1Zy8ofuoJAttqhXpySyYJhCwdWXYKF6bapSXCLwQoKJ9bWLYYZqudsiPfwv43ekzgJHtaWozzFjrEq835B7Xbd8LSd4znVh2FRWfAPW1Zvsm6nKjN2NfEPndwbps7zgqvbQYeKngwFk952CLtDEpGfXXiS5pUp5ExYTwsxGE4E6LKV'
    }
}
```

### Acknowledger receives unsigned withdraw transaction
 * **action:** `sign`
 * **tag** `withdraw_ack`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | unsigned `channel_withdraw` transaction | Yes |

#### Example
```javascript
{'action': 'sign',
 'tag': 'withdraw_ack',
 'payload' {
    'tx': 'tx_2C9estKT2f86WwC7LCa18cDTTmMCrXM7N2AcrXKmgnTo9DNchXjNmewbgNX2YW4RYk8iHkVRnPpeYLRgh6xH96mHNxCMW4aUL2hgTe6iqdrKyM5eqMbCN9YgTdDvUzDyASJwoicxXb7UeDF5kFWvsEMxXBKGX2'}
}
```

### Acknowledger signed withdraw responsse
 * **action:** `withdraw_ack`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | signed `channel_withdraw` transaction | Yes |

#### Example
```javascript
{'action': 'withdraw_ack',
 'payload': {
    'tx': 'tx_2WsEQsiC5XsmkQF6BS1aUhB55XkktxRJi2ZWbpCbGVHgQNPQzUeaEJk57RrhWBagGqNUyUA9YY6PrZhTiXcYs6dK1BxASu8EummTYvfpTjfnA8hU21pw6Ms9fWbJbhBbLNai4hLGPEJZ12r1UHqxLTnq6nJ69vw6szeisRzVJ3XYNpvGgSR5dVyW7Yd2VvtW5CGEMCXCHVYquD8gt6RMBDDr1Q6LeLUTomBpgFGQknjKv56tLtZ2FHkWWa9mU22jXMS'
    }
}
```

## Generic message
Roles:
 * Sender
 * Receiver

### Sender send message
 * **action:** `message`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | to | string | Receiver's address | Yes |
  | info | string | Message body | Yes |

#### Example
```javascript
{'action': 'message',
 'payload': {'info': 'hejsan',
             'to': 'ak_35Wxqf2cbzQF5hEV1j9AdXQFTMxqKCwM7iMKNGcqSv47MXAj68'
             }
}
```

### Receiver receives message
 * **action:** `message`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | message | message object | Message | Yes |

 message object:

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | channel_id | string | channel id| Yes |
  | from | string | Sender's address | Yes |
  | to | string | Receiver's address | Yes |
  | info | string | Message body | Yes |

#### Example
```javascript
{'action': 'message',
 'payload': {'message': {'channel_id': 'ch_6SgSc7a14dGbwMNCsjjQZCYVreVLKkFwBzJEZ58ZSZnV9FiQ1',
                         'from': 'ak_4Kr76woCtc3ehZ45K1sCrmgKX6gnh7qGhjSU1GZYqfLTTjtCgn',
                         'to': 'ak_35Wxqf2cbzQF5hEV1j9AdXQFTMxqKCwM7iMKNGcqSv47MXAj68',
                         'info': 'hejsan'
                         }
            }
}
```

## Close mutual
Roles:
 * Closer
 * Acknowledger

### Closer initiate mutual close
 * **action:** `shutdown`

#### Example
```javascript
{'action': 'shutdown'}
```

### Closer receives mutual close
 * **action:** `sign`
 * **tag:** `shutdown_sign`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | unsigned `channel_close_mutual` transaction | Yes |

#### Example
```javascript
{'action': 'sign',
 'tag': 'shutdown_sign',
 'payload': {
    'tx': 'tx_SUBGDUaJgWhDYs73EPSiX42Xd3PSmHAhRmwd1th9ibGipCVVbsdS96roQZEH4MF'
    }
}
```

### Closer returns signed mutual close
 * **action:** `shutdown_sign`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | signed `channel_close_mutual` transaction | Yes |

#### Example
```javascript
{'action': 'shutdown_sign',
 'payload': {
    'tx': 'tx_8oWtHcfnWDSQV6Wdehp1MdXYhcbV29a7tWe3LWDqU5RwKvMhzPQLiSJKaYhtw4NLaBN1m3pmEtsVjoygkohXi9i8e3vpYgenphdKJmYLrFqjouxmyC5yKbsQUY8m9i4EzcMNuHmrLwrXrrPhKC1qY25Pxb6u74VEVuk'
    }
}
```

### Acknowledger receives mutual close
 * **action:** `sign`
 * **tag:** `shutdown_sign_ack`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | unsigned `channel_close_mutual` transaction | Yes |

#### Example
```javascript
{'action': 'sign',
 'tag': 'shutdown_sign_ack',
 'payload': {
    'tx': 'tx_SUBGDUaJgWhDYs73EPSiX42Xd3PSmHAhRmwd1th9ibGipCVVbsdS96roQZEH4MF'
    }
}
```

### Acknowledger returns signed mutual close
 * **action:** `shutdown_sign_ack`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | signed `channel_close_mutual` transaction | Yes |

#### Example
```javascript
{'action': 'shutdown_sign_ack',
 'payload': {
    'tx': 'tx_8oWtHcfnWDSYu4SfLLLHqYqM5JXiCZd6De7fLQZesMHrArZeWzP7893EVpBpUR56tKUeJXJ3YUTuqB8a4efiHaw6ai3GKwoeu3ZyzfGPUfb5EMG6viv2dM8mhtKqaG7fkEAWuswbmFN4bDjXANbAK2sMU36yfBc9p1h'
    }
}
```

## On-chain transactions
 * **action:** `on_chain_tx`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | tx | string | co-signed transaction that is posted on-chain | Yes |

#### Example
```javascript
{'action': 'shutdown_sign_ack',
 'payload': {
    'tx': 'tx_CWSA5wyxuP9AbAbcxQi8QbZsfUdhQdDouMSgsBTAQCNdN8PDKsLf6qnEhw6JacKRWKmBuwBaJYZTUSDUKih9vygmzkmbn2XC7MkGcz6zbwThk9jdyH8HQhzWq9uZ7ExYNjZyXGpPX6vQLsSRH8d4RxqvD94uG9YhcNqDWeSntM5CtBrjCwEXm9r3wEkZ6NKnoUShU5soJZTV8TAMFAArJMsS2V3EAjXSSVf3Xt5aJeVLgVbSYczcM22gvZt2LEPTCUJEYW2XsDvi6rAtps58d7B1P5uDuXG8s8hEWi11XsjaTyhGhnt9jfcBYVzQVdApG1JpMaQjeyRiEqwNoAVjTranxeM1Cn'
    }
}
```

## Leave
Roles:
 * Leaver
 * Acknowledger

### Leaver initiates leave
 * **action:** `leave`

#### Example
```javascript
{'action': 'leave'}
```

#### Leaver and Acknowledger inform their clients
```javascript
{'action': 'leave',
 'channel_id': 'ch_FhYNM5KorNAcRwexe1CE3jH5DZd7FBD2g9XhBDHGEouDqVRCR',
 'payload': {
    'state': 'tx_6jPYBUFTkcmQ7A3JYkUsYMChMHNqe3TMEhDZaSat7P1sbP4XXQP9QmaFfaAftUDjws3GhdKaBGyJRMBhHKyk2irBZsymgUVuxfQXR63ojEjg7C583D6cNKLSZtybZr9Cw6mmCkSDRVu41WbF1jKEkAkXbXznANm3AyJ1BLqNVB7qiAyFSVeq5qVcvHL4Z1y2DAhcLLw6YGSqFyuyg8pKVQRhL2LuePa9mdtoYZyY5VhvgShLz2oY8R3taBL8RrnnTvcwECvQu51yPKyM2pryoHaQbED5Zn7hdegZy6KN9wfpLXedtNB9ssmMvz5jHcK12vmtfeUMzRrySqtmBDGfiqwFZrYZ5A7xz1uqi'
    }
}
```

## Info messages

### Info
 * **action:** `info`
 * **payload:**

  | Name | Type | Description | Required |
  | ---- | ---- | ----------- | -------- |
  | event | string | event description | Yes |

#### Example
```javascript
{'action': 'info',
 'payload': {'event': 'own_deposit_locked'}
 }
```

### Latest state
 * **action:** `get`
 * **tag:** `offchain_state`

#### Response
 | Field name | Value |
 | ---- | ---- |
 | `trees` | channel state trees |
 | `calls` | channel call state tree |
 | `half_signed_tx` | channel latest half signed tx or `""` if equal to latest signed tx |
 | `signed_tx` | channel latest fully signed tx or `""` if not available |

#### Example

##### Request
```javascript
{'action': 'get', 'payload': {}, 'tag': 'offchain_state'}
```
##### Response
```javascript
{'action': 'get',
 'channel_id': 'ch_2eYSahMjyrytqyd28iyNGK8ETBTW868yki8pYUxDBd6Akp29k4',
 'payload': {
   'calls': 'cs_yYICbgGEwz8BwHtqgWY=',
    'half_signed_tx': '',
    'signed_tx': 'tx_+QEhCwH4hLhABA9QLTLb8+EWeN+ZCL3GmcwlOczQobsgHqDnYWuX+oUmyBKcBLEgDngf2phxqzQZEI5UDsI4/a6raPh9ddP1BLhA5sF1rvkHi3hD6Ms7TpMpkGs/dEOVGFv7LeWnxQ+h8N23Hr2eU5g3C7UMnSiLM97kpVDExjobRWi6eYGHgF1wCriX+JU5AaEG2PCjn3Eu3YTF4cstNGAp7ZGDxjcJrqUCFEU8sIMWbggC+E24S/hJggI6AaEB7qS1cNCbw3GpiqMXadWS4UkmP7hy9Gwff3kErkNExqqhAViP6Wm0p2j/DY8a9978psqBZF9cAupp5+Qfq/jmCizCAaA8q/nvdMUP6xOxo0AYP43zXUs+3k+b8J85LY3cFMzlYBFnSEA=',
    'trees': 'ss_+KQ+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4afhnggJyAbhh+F8/AfhbrexAAaDupLVw0JvDcamKoxdp1ZLhSSY/uHL0bB9/eQSuQ0TGqojHCgEAgwERbqzrQAGgWI/pabSnaP8Njxr33vymyoFkX1wC6mnn5B+r+OYKLMKHxgoBAIKcQquqkGQ='},
  'tag': 'offchain_state',
  'version': 1}
```
