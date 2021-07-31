
#### initiator opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&host=localhost&initiator_amount=70000000000000&initiator_id=ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn&role=initiator
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_wD90Jp9t+wkmsICaRrp975MiJsyzoaT+2PO2K6+onhJO6DTW"
    }
  },
  "version": 1
}
```

#### initiator info
> The local fsm has been started

#### responder opens a WebSocket connection
```
ws://localhost:3014/channel?channel_reserve=2&initiator_amount=70000000000000&initiator_id=ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv&keep_running=false&lock_period=10&port=13179&protocol=json-rpc&push_amount=1&responder_amount=40000000000000&responder_id=ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn&role=responder
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "fsm_up",
      "fsm_id": "ba_8ODUOsie07jzMYeXewzYmm3osV9irz3hQuiLgOMCervhz8zY"
    }
  },
  "version": 1
}
```

#### responder info
> The local fsm has been started

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_open"
    }
  },
  "version": 1
}
```

#### responder info
> Received an WebSocket opening request

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": null,
    "data": {
      "event": "channel_accept"
    }
  },
  "version": 1
}
```

#### initiator info
> Received an WebSocket connection accepted

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.initiator_sign",
  "params": {
    "channel_id": null,
    "data": {
      "signed_tx": "tx_+IkLAcC4hPiCMgKhAcEx9JI23KmfpH0uP9dxJYB0DY+XRKb4DSeN+YnHNANGhj+qJSJgAKEBEz2ciJGcxrbKc/5lzfvMBttVgar6S5lhtorJSke1o/+GJGE5yoAAAgoAhhALIe8QAMDAoJe1cGW5sUaMM7gL6OM8nTWJY+4H9W7nIDbL3sTcW8M6Ae4d4YI=",
      "updates": []
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421696,
  "jsonrpc": "2.0",
  "method": "channels.initiator_sign",
  "params": {
    "signed_tx": "tx_+MwLAfhCuEABPXA7pfVeKapKMmBcPa0AuhaS1w6BYFe8A48OjlSXasF9Y84+QL30lAA7tvwrA9Kvtkw4SKWGm080RZhWot0EuIT4gjICoQHBMfSSNtypn6R9Lj/XcSWAdA2Pl0Sm+A0njfmJxzQDRoY/qiUiYAChARM9nIiRnMa2ynP+Zc37zAbbVYGq+kuZYbaKyUpHtaP/hiRhOcqAAAIKAIYQCyHvEADAwKCXtXBlubFGjDO4C+jjPJ01iWPuB/Vu5yA2y97E3FvDOgGX8A9a"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": null,
  "id": -576460752303421696,
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "event": "funding_created",
      "fsm_id": "ba_8ODUOsie07jzMYeXewzYmm3osV9irz3hQuiLgOMCervhz8zY"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.responder_sign",
  "params": {
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "signed_tx": "tx_+MwLAfhCuEABPXA7pfVeKapKMmBcPa0AuhaS1w6BYFe8A48OjlSXasF9Y84+QL30lAA7tvwrA9Kvtkw4SKWGm080RZhWot0EuIT4gjICoQHBMfSSNtypn6R9Lj/XcSWAdA2Pl0Sm+A0njfmJxzQDRoY/qiUiYAChARM9nIiRnMa2ynP+Zc37zAbbVYGq+kuZYbaKyUpHtaP/hiRhOcqAAAIKAIYQCyHvEADAwKCXtXBlubFGjDO4C+jjPJ01iWPuB/Vu5yA2y97E3FvDOgGX8A9a",
      "updates": []
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421695,
  "jsonrpc": "2.0",
  "method": "channels.responder_sign",
  "params": {
    "signed_tx": "tx_+QEOCwH4hLhAAT1wO6X1XimqSjJgXD2tALoWktcOgWBXvAOPDo5Ul2rBfWPOPkC99JQAO7b8KwPSr7ZMOEilhptPNEWYVqLdBLhAxw3skqCjhCvxm4jwDYZRZ8M/f2QDOuj16uaTYJn9Qx1yvqflv8NcN2Ar++LbxXd2U5QCQnzxRIB1TsNDSG5aCbiE+IIyAqEBwTH0kjbcqZ+kfS4/13ElgHQNj5dEpvgNJ435icc0A0aGP6olImAAoQETPZyIkZzGtspz/mXN+8wG21WBqvpLmWG2islKR7Wj/4YkYTnKgAACCgCGEAsh7xAAwMCgl7VwZbmxRowzuAvo4zydNYlj7gf1bucgNsvexNxbwzoBOeX7Rg=="
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421695,
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "info": "funding_created",
      "tx": "tx_+QEOCwH4hLhAAT1wO6X1XimqSjJgXD2tALoWktcOgWBXvAOPDo5Ul2rBfWPOPkC99JQAO7b8KwPSr7ZMOEilhptPNEWYVqLdBLhAxw3skqCjhCvxm4jwDYZRZ8M/f2QDOuj16uaTYJn9Qx1yvqflv8NcN2Ar++LbxXd2U5QCQnzxRIB1TsNDSG5aCbiE+IIyAqEBwTH0kjbcqZ+kfS4/13ElgHQNj5dEpvgNJ435icc0A0aGP6olImAAoQETPZyIkZzGtspz/mXN+8wG21WBqvpLmWG2islKR7Wj/4YkYTnKgAACCgCGEAsh7xAAwMCgl7VwZbmxRowzuAvo4zydNYlj7gf1bucgNsvexNxbwzoBOeX7Rg==",
      "type": "channel_create_tx"
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "event": "funding_signed",
      "fsm_id": "ba_wD90Jp9t+wkmsICaRrp975MiJsyzoaT+2PO2K6+onhJO6DTW"
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "info": "funding_signed",
      "tx": "tx_+QEOCwH4hLhAAT1wO6X1XimqSjJgXD2tALoWktcOgWBXvAOPDo5Ul2rBfWPOPkC99JQAO7b8KwPSr7ZMOEilhptPNEWYVqLdBLhAxw3skqCjhCvxm4jwDYZRZ8M/f2QDOuj16uaTYJn9Qx1yvqflv8NcN2Ar++LbxXd2U5QCQnzxRIB1TsNDSG5aCbiE+IIyAqEBwTH0kjbcqZ+kfS4/13ElgHQNj5dEpvgNJ435icc0A0aGP6olImAAoQETPZyIkZzGtspz/mXN+8wG21WBqvpLmWG2islKR7Wj/4YkYTnKgAACCgCGEAsh7xAAwMCgl7VwZbmxRowzuAvo4zydNYlj7gf1bucgNsvexNxbwzoBOeX7Rg==",
      "type": "channel_create_tx"
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAAT1wO6X1XimqSjJgXD2tALoWktcOgWBXvAOPDo5Ul2rBfWPOPkC99JQAO7b8KwPSr7ZMOEilhptPNEWYVqLdBLhAxw3skqCjhCvxm4jwDYZRZ8M/f2QDOuj16uaTYJn9Qx1yvqflv8NcN2Ar++LbxXd2U5QCQnzxRIB1TsNDSG5aCbiE+IIyAqEBwTH0kjbcqZ+kfS4/13ElgHQNj5dEpvgNJ435icc0A0aGP6olImAAoQETPZyIkZzGtspz/mXN+8wG21WBqvpLmWG2islKR7Wj/4YkYTnKgAACCgCGEAsh7xAAwMCgl7VwZbmxRowzuAvo4zydNYlj7gf1bucgNsvexNxbwzoBOeX7Rg==",
      "type": "channel_create_tx"
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "info": "channel_changed",
      "tx": "tx_+QEOCwH4hLhAAT1wO6X1XimqSjJgXD2tALoWktcOgWBXvAOPDo5Ul2rBfWPOPkC99JQAO7b8KwPSr7ZMOEilhptPNEWYVqLdBLhAxw3skqCjhCvxm4jwDYZRZ8M/f2QDOuj16uaTYJn9Qx1yvqflv8NcN2Ar++LbxXd2U5QCQnzxRIB1TsNDSG5aCbiE+IIyAqEBwTH0kjbcqZ+kfS4/13ElgHQNj5dEpvgNJ435icc0A0aGP6olImAAoQETPZyIkZzGtspz/mXN+8wG21WBqvpLmWG2islKR7Wj/4YkYTnKgAACCgCGEAsh7xAAwMCgl7VwZbmxRowzuAvo4zydNYlj7gf1bucgNsvexNxbwzoBOeX7Rg==",
      "type": "channel_create_tx"
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
    "to": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "message": {
        "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
        "from": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
        "info": "Hello",
        "to": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
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
    "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.message",
  "params": {
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "message": {
        "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
        "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
        "info": "Hello back",
        "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
      }
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421694,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
      "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421694,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
      "balance": 69999999999999
    },
    {
      "account": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421693,
  "jsonrpc": "2.0",
  "method": "channels.assume_minimum_depth",
  "params": {
    "tx_hash": "th_2ERU4LEe8Bn8x1iuw9vSh7iHys9t8zwt3Nq2oz5GQj9pAu9pur"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421693,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421692,
  "jsonrpc": "2.0",
  "method": "channels.assume_minimum_depth",
  "params": {
    "tx_hash": "th_2ERU4LEe8Bn8x1iuw9vSh7iHys9t8zwt3Nq2oz5GQj9pAu9pur"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421692,
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "event": "own_funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed locally on-chain

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### responder info
> Funding has been confirmed on-chain by other party

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "event": "funding_locked"
    }
  },
  "version": 1
}
```

#### initiator info
> Funding has been confirmed on-chain by other party

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### responder info
> Channel is `open` and ready to use

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "event": "open"
    }
  },
  "version": 1
}
```

#### initiator info
> Channel is `open` and ready to use

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "state": "tx_+QEOCwH4hLhAAT1wO6X1XimqSjJgXD2tALoWktcOgWBXvAOPDo5Ul2rBfWPOPkC99JQAO7b8KwPSr7ZMOEilhptPNEWYVqLdBLhAxw3skqCjhCvxm4jwDYZRZ8M/f2QDOuj16uaTYJn9Qx1yvqflv8NcN2Ar++LbxXd2U5QCQnzxRIB1TsNDSG5aCbiE+IIyAqEBwTH0kjbcqZ+kfS4/13ElgHQNj5dEpvgNJ435icc0A0aGP6olImAAoQETPZyIkZzGtspz/mXN+8wG21WBqvpLmWG2islKR7Wj/4YkYTnKgAACCgCGEAsh7xAAwMCgl7VwZbmxRowzuAvo4zydNYlj7gf1bucgNsvexNxbwzoBOeX7Rg=="
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "state": "tx_+QEOCwH4hLhAAT1wO6X1XimqSjJgXD2tALoWktcOgWBXvAOPDo5Ul2rBfWPOPkC99JQAO7b8KwPSr7ZMOEilhptPNEWYVqLdBLhAxw3skqCjhCvxm4jwDYZRZ8M/f2QDOuj16uaTYJn9Qx1yvqflv8NcN2Ar++LbxXd2U5QCQnzxRIB1TsNDSG5aCbiE+IIyAqEBwTH0kjbcqZ+kfS4/13ElgHQNj5dEpvgNJ435icc0A0aGP6olImAAoQETPZyIkZzGtspz/mXN+8wG21WBqvpLmWG2islKR7Wj/4YkYTnKgAACCgCGEAsh7xAAwMCgl7VwZbmxRowzuAvo4zydNYlj7gf1bucgNsvexNxbwzoBOeX7Rg=="
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421691,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
      "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421691,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
      "balance": 69999999999999
    },
    {
      "account": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
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
    "amount": "1",
    "from": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
    "to": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
        "to": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
    "meta": 17,
    "to": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
        "meta": 17,
        "to": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
    "to": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBp7tfsHJU7GHsf/8u3KSCdFtIgGM16FuOygYDNRkpG37AqAItoZUv/XRm7XPkPQsAqyTRxEMHCdyvVgPRhJPJ6bYR/2pFxs=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
          "op": "OffChainTransfer",
          "to": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
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
  "id": -576460752303421690,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECEwQ3D4WfXsq35UySpBUeSxTftsujhot8R5Q86k2BZI9rFU5LTmpbMi6KqgfauGusJUei/t4elRH0WaVElDgUEuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wKgCLaGVL/10Zu1z5D0LAKsk0cRDBwncr1YD0YSTyem2EeXS/gs"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421690,
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "signed_tx": "tx_+JALAfhCuECEwQ3D4WfXsq35UySpBUeSxTftsujhot8R5Q86k2BZI9rFU5LTmpbMi6KqgfauGusJUei/t4elRH0WaVElDgUEuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wKgCLaGVL/10Zu1z5D0LAKsk0cRDBwncr1YD0YSTyem2EeXS/gs",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
          "op": "OffChainTransfer",
          "to": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
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
  "id": -576460752303421689,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBkYnrK2VC1CZh78Nak6LkPilRsoHx5Dea7QBt8oveSKfrFaK7XpYQxrGBaIdCS1lO4T5/a8SRL+y6Nd7Y37KANuECEwQ3D4WfXsq35UySpBUeSxTftsujhot8R5Q86k2BZI9rFU5LTmpbMi6KqgfauGusJUei/t4elRH0WaVElDgUEuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wKgCLaGVL/10Zu1z5D0LAKsk0cRDBwncr1YD0YSTyem2EcfPWeO"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421689,
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "state": "tx_+NILAfiEuEBkYnrK2VC1CZh78Nak6LkPilRsoHx5Dea7QBt8oveSKfrFaK7XpYQxrGBaIdCS1lO4T5/a8SRL+y6Nd7Y37KANuECEwQ3D4WfXsq35UySpBUeSxTftsujhot8R5Q86k2BZI9rFU5LTmpbMi6KqgfauGusJUei/t4elRH0WaVElDgUEuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wKgCLaGVL/10Zu1z5D0LAKsk0cRDBwncr1YD0YSTyem2EcfPWeO"
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "state": "tx_+NILAfiEuEBkYnrK2VC1CZh78Nak6LkPilRsoHx5Dea7QBt8oveSKfrFaK7XpYQxrGBaIdCS1lO4T5/a8SRL+y6Nd7Y37KANuECEwQ3D4WfXsq35UySpBUeSxTftsujhot8R5Q86k2BZI9rFU5LTmpbMi6KqgfauGusJUei/t4elRH0WaVElDgUEuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wKgCLaGVL/10Zu1z5D0LAKsk0cRDBwncr1YD0YSTyem2EcfPWeO"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421688,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
      "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421688,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
      "balance": 69999999999998
    },
    {
      "account": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
      "balance": 40000000000002
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421687,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421687,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBkYnrK2VC1CZh78Nak6LkPilRsoHx5Dea7QBt8oveSKfrFaK7XpYQxrGBaIdCS1lO4T5/a8SRL+y6Nd7Y37KANuECEwQ3D4WfXsq35UySpBUeSxTftsujhot8R5Q86k2BZI9rFU5LTmpbMi6KqgfauGusJUei/t4elRH0WaVElDgUEuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wKgCLaGVL/10Zu1z5D0LAKsk0cRDBwncr1YD0YSTyem2EcfPWeO",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDBMfSSNtypn6R9Lj/XcSWAdA2Pl0Sm+A0njfmJxzQDRovKCgEAhj+qJSJf/rDvQAGgEz2ciJGcxrbKc/5lzfvMBttVgar6S5lhtorJSke1o/+LygoBAIYkYTnKgALC0BtF"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421686,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
      "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421686,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
      "balance": 40000000000002
    },
    {
      "account": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
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
    "amount": "1",
    "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
    "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
        "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
    "meta": 17,
    "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
        "meta": 17,
        "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
    "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBp7tfsHJU7GHsf/8u3KSCdFtIgGM16FuOygYDNRkpG37A6CXtXBlubFGjDO4C+jjPJ01iWPuB/Vu5yA2y97E3FvDOl85g+4=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
          "op": "OffChainTransfer",
          "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
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
  "id": -576460752303421685,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEB6rYjaYcwgOti6k4Ujz8n2k1djjuF+ZBZxytKG/GuIrBtQbIrl9clm8gUUTY5vUV0OuKqgF/DqmBzpHo7j5fsLuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wOgl7VwZbmxRowzuAvo4zydNYlj7gf1bucgNsvexNxbwzqbbv4i"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421685,
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "signed_tx": "tx_+JALAfhCuEB6rYjaYcwgOti6k4Ujz8n2k1djjuF+ZBZxytKG/GuIrBtQbIrl9clm8gUUTY5vUV0OuKqgF/DqmBzpHo7j5fsLuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wOgl7VwZbmxRowzuAvo4zydNYlj7gf1bucgNsvexNxbwzqbbv4i",
      "updates": [
        {
          "amount": 1,
          "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
          "op": "OffChainTransfer",
          "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
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
  "id": -576460752303421684,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEB6rYjaYcwgOti6k4Ujz8n2k1djjuF+ZBZxytKG/GuIrBtQbIrl9clm8gUUTY5vUV0OuKqgF/DqmBzpHo7j5fsLuEDQIfeii4YkKKHLTNfqmcAVqRCuzPOExUom2RNYuTnsIypN8sPj6kCJ2EsHrPSWYdUgM2mdeP55UVkJBOax/IUEuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wOgl7VwZbmxRowzuAvo4zydNYlj7gf1bucgNsvexNxbwzpYX+K6"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421684,
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "state": "tx_+NILAfiEuEB6rYjaYcwgOti6k4Ujz8n2k1djjuF+ZBZxytKG/GuIrBtQbIrl9clm8gUUTY5vUV0OuKqgF/DqmBzpHo7j5fsLuEDQIfeii4YkKKHLTNfqmcAVqRCuzPOExUom2RNYuTnsIypN8sPj6kCJ2EsHrPSWYdUgM2mdeP55UVkJBOax/IUEuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wOgl7VwZbmxRowzuAvo4zydNYlj7gf1bucgNsvexNxbwzpYX+K6"
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "state": "tx_+NILAfiEuEB6rYjaYcwgOti6k4Ujz8n2k1djjuF+ZBZxytKG/GuIrBtQbIrl9clm8gUUTY5vUV0OuKqgF/DqmBzpHo7j5fsLuEDQIfeii4YkKKHLTNfqmcAVqRCuzPOExUom2RNYuTnsIypN8sPj6kCJ2EsHrPSWYdUgM2mdeP55UVkJBOax/IUEuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wOgl7VwZbmxRowzuAvo4zydNYlj7gf1bucgNsvexNxbwzpYX+K6"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421683,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
      "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421683,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
      "balance": 40000000000001
    },
    {
      "account": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
      "balance": 69999999999999
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421682,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421682,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEB6rYjaYcwgOti6k4Ujz8n2k1djjuF+ZBZxytKG/GuIrBtQbIrl9clm8gUUTY5vUV0OuKqgF/DqmBzpHo7j5fsLuEDQIfeii4YkKKHLTNfqmcAVqRCuzPOExUom2RNYuTnsIypN8sPj6kCJ2EsHrPSWYdUgM2mdeP55UVkJBOax/IUEuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wOgl7VwZbmxRowzuAvo4zydNYlj7gf1bucgNsvexNxbwzpYX+K6",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDBMfSSNtypn6R9Lj/XcSWAdA2Pl0Sm+A0njfmJxzQDRovKCgEAhj+qJSJf/7DvQAGgEz2ciJGcxrbKc/5lzfvMBttVgar6S5lhtorJSke1o/+LygoBAIYkYTnKgAFgU3ZQ"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421681,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
      "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421681,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
      "balance": 40000000000001
    },
    {
      "account": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
      "balance": 69999999999999
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
    "amount": "1",
    "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
    "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
        "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
    "meta": 17,
    "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
        "meta": 17,
        "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
    "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBp7tfsHJU7GHsf/8u3KSCdFtIgGM16FuOygYDNRkpG37BKArMRarrSyTs6kooYlRMBZb/tbfiBuYvXLPodgg12U85hQYu/w=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
          "op": "OffChainTransfer",
          "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
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
  "id": -576460752303421680,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECRPv8196oY8ccvId+T6L0DwRzZUe5dwXFoKF4b/bFpSq71y0/Z0eAieoNHBoW0N4mihD0Q3K39Si7Xax6ZShABuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wSgKzEWq60sk7OpKKGJUTAWW/7W34gbmL1yz6HYINdlPOZEpm2G"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421680,
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "signed_tx": "tx_+JALAfhCuECRPv8196oY8ccvId+T6L0DwRzZUe5dwXFoKF4b/bFpSq71y0/Z0eAieoNHBoW0N4mihD0Q3K39Si7Xax6ZShABuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wSgKzEWq60sk7OpKKGJUTAWW/7W34gbmL1yz6HYINdlPOZEpm2G",
      "updates": [
        {
          "amount": 1,
          "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
          "op": "OffChainTransfer",
          "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
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
  "id": -576460752303421679,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBM8xgPHd3JDHhsBERmI38bV6XT2jeujgk9iOrG2SEdac7aeLiw1z+GLmEyqP7U2xid6K/DlD1wtiSLP+jhkMIMuECRPv8196oY8ccvId+T6L0DwRzZUe5dwXFoKF4b/bFpSq71y0/Z0eAieoNHBoW0N4mihD0Q3K39Si7Xax6ZShABuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wSgKzEWq60sk7OpKKGJUTAWW/7W34gbmL1yz6HYINdlPOatb+5p"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421679,
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "state": "tx_+NILAfiEuEBM8xgPHd3JDHhsBERmI38bV6XT2jeujgk9iOrG2SEdac7aeLiw1z+GLmEyqP7U2xid6K/DlD1wtiSLP+jhkMIMuECRPv8196oY8ccvId+T6L0DwRzZUe5dwXFoKF4b/bFpSq71y0/Z0eAieoNHBoW0N4mihD0Q3K39Si7Xax6ZShABuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wSgKzEWq60sk7OpKKGJUTAWW/7W34gbmL1yz6HYINdlPOatb+5p"
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "state": "tx_+NILAfiEuEBM8xgPHd3JDHhsBERmI38bV6XT2jeujgk9iOrG2SEdac7aeLiw1z+GLmEyqP7U2xid6K/DlD1wtiSLP+jhkMIMuECRPv8196oY8ccvId+T6L0DwRzZUe5dwXFoKF4b/bFpSq71y0/Z0eAieoNHBoW0N4mihD0Q3K39Si7Xax6ZShABuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wSgKzEWq60sk7OpKKGJUTAWW/7W34gbmL1yz6HYINdlPOatb+5p"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421678,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
      "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421678,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
      "balance": 40000000000000
    },
    {
      "account": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421677,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421677,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBM8xgPHd3JDHhsBERmI38bV6XT2jeujgk9iOrG2SEdac7aeLiw1z+GLmEyqP7U2xid6K/DlD1wtiSLP+jhkMIMuECRPv8196oY8ccvId+T6L0DwRzZUe5dwXFoKF4b/bFpSq71y0/Z0eAieoNHBoW0N4mihD0Q3K39Si7Xax6ZShABuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wSgKzEWq60sk7OpKKGJUTAWW/7W34gbmL1yz6HYINdlPOatb+5p",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDBMfSSNtypn6R9Lj/XcSWAdA2Pl0Sm+A0njfmJxzQDRovKCgEAhj+qJSJgALDvQAGgEz2ciJGcxrbKc/5lzfvMBttVgar6S5lhtorJSke1o/+LygoBAIYkYTnKgABEv1s8"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421676,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
      "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421676,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
      "balance": 70000000000000
    },
    {
      "account": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
      "balance": 40000000000000
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
    "amount": "1",
    "from": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
    "to": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
        "to": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
    "to": "ABCDEF"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
    "meta": 17,
    "to": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
        "meta": 17,
        "to": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
    "to": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBp7tfsHJU7GHsf/8u3KSCdFtIgGM16FuOygYDNRkpG37BaCXtXBlubFGjDO4C+jjPJ01iWPuB/Vu5yA2y97E3FvDOrces/0=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
          "op": "OffChainTransfer",
          "to": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
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
  "id": -576460752303421675,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuECQfs7NRo8zjCwUkNtZVLsMTLDaImvyMrtE6xK8ELrl6nbxeILwuljxenW29DMLrjFqvtLaG/78Q1RGQSlqKvUKuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wWgl7VwZbmxRowzuAvo4zydNYlj7gf1bucgNsvexNxbwzoBMaO/"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421675,
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "signed_tx": "tx_+JALAfhCuECQfs7NRo8zjCwUkNtZVLsMTLDaImvyMrtE6xK8ELrl6nbxeILwuljxenW29DMLrjFqvtLaG/78Q1RGQSlqKvUKuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wWgl7VwZbmxRowzuAvo4zydNYlj7gf1bucgNsvexNxbwzoBMaO/",
      "updates": [
        {
          "amount": 1,
          "from": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
          "op": "OffChainTransfer",
          "to": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
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
  "id": -576460752303421674,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEBOegZHN5+lzu0RyCHYvmegVxfqS1T0o4SL3NVZZKeCNzFQocnWX08epKZvRkvsAVil8zUUtAduWbKKDWzGN7sIuECQfs7NRo8zjCwUkNtZVLsMTLDaImvyMrtE6xK8ELrl6nbxeILwuljxenW29DMLrjFqvtLaG/78Q1RGQSlqKvUKuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wWgl7VwZbmxRowzuAvo4zydNYlj7gf1bucgNsvexNxbwzql0IEM"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421674,
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "state": "tx_+NILAfiEuEBOegZHN5+lzu0RyCHYvmegVxfqS1T0o4SL3NVZZKeCNzFQocnWX08epKZvRkvsAVil8zUUtAduWbKKDWzGN7sIuECQfs7NRo8zjCwUkNtZVLsMTLDaImvyMrtE6xK8ELrl6nbxeILwuljxenW29DMLrjFqvtLaG/78Q1RGQSlqKvUKuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wWgl7VwZbmxRowzuAvo4zydNYlj7gf1bucgNsvexNxbwzql0IEM"
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "state": "tx_+NILAfiEuEBOegZHN5+lzu0RyCHYvmegVxfqS1T0o4SL3NVZZKeCNzFQocnWX08epKZvRkvsAVil8zUUtAduWbKKDWzGN7sIuECQfs7NRo8zjCwUkNtZVLsMTLDaImvyMrtE6xK8ELrl6nbxeILwuljxenW29DMLrjFqvtLaG/78Q1RGQSlqKvUKuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wWgl7VwZbmxRowzuAvo4zydNYlj7gf1bucgNsvexNxbwzql0IEM"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421673,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
      "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421673,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
      "balance": 69999999999999
    },
    {
      "account": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
      "balance": 40000000000001
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421672,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421672,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEBOegZHN5+lzu0RyCHYvmegVxfqS1T0o4SL3NVZZKeCNzFQocnWX08epKZvRkvsAVil8zUUtAduWbKKDWzGN7sIuECQfs7NRo8zjCwUkNtZVLsMTLDaImvyMrtE6xK8ELrl6nbxeILwuljxenW29DMLrjFqvtLaG/78Q1RGQSlqKvUKuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wWgl7VwZbmxRowzuAvo4zydNYlj7gf1bucgNsvexNxbwzql0IEM",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDBMfSSNtypn6R9Lj/XcSWAdA2Pl0Sm+A0njfmJxzQDRovKCgEAhj+qJSJf/7DvQAGgEz2ciJGcxrbKc/5lzfvMBttVgar6S5lhtorJSke1o/+LygoBAIYkYTnKgAFgU3ZQ"
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421671,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
      "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421671,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
      "balance": 40000000000001
    },
    {
      "account": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
      "balance": 69999999999999
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
    "amount": "1",
    "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
    "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
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
      "method": "channels.update.new",
      "params": {
        "amount": "1",
        "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
        "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ABCDEF",
    "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ABCDEF",
        "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
    "to": "ABCDEF"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1005,
        "message": "Broken encoding: account pubkey"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
        "to": "ABCDEF"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
    "meta": 17,
    "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "error": {
    "code": 3,
    "data": [
      {
        "code": 1014,
        "message": "Invalid meta object"
      }
    ],
    "message": "Rejected",
    "request": {
      "jsonrpc": "2.0",
      "method": "channels.update.new",
      "params": {
        "amount": 1,
        "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
        "meta": 17,
        "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
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
  "method": "channels.update.new",
  "params": {
    "amount": 1,
    "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
    "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
  }
}
```

#### responder <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.sign.update",
  "params": {
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "signed_tx": "tx_+E0LAcC4SPhGOQKhBp7tfsHJU7GHsf/8u3KSCdFtIgGM16FuOygYDNRkpG37BqArMRarrSyTs6kooYlRMBZb/tbfiBuYvXLPodgg12U85hyqEVc=",
      "updates": [
        {
          "amount": 1,
          "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
          "op": "OffChainTransfer",
          "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
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
  "id": -576460752303421670,
  "jsonrpc": "2.0",
  "method": "channels.update",
  "params": {
    "signed_tx": "tx_+JALAfhCuEAq1UYcwhb9o6nuTfYqsdxgwj+Z1T2J2DPkNkLmJYWdNoyH1pK3OrtLp64fJqlF5L+Z3A5eKtQoiFe8vBn12l0AuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wagKzEWq60sk7OpKKGJUTAWW/7W34gbmL1yz6HYINdlPOYh8095"
  }
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421670,
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "signed_tx": "tx_+JALAfhCuEAq1UYcwhb9o6nuTfYqsdxgwj+Z1T2J2DPkNkLmJYWdNoyH1pK3OrtLp64fJqlF5L+Z3A5eKtQoiFe8vBn12l0AuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wagKzEWq60sk7OpKKGJUTAWW/7W34gbmL1yz6HYINdlPOYh8095",
      "updates": [
        {
          "amount": 1,
          "from": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
          "op": "OffChainTransfer",
          "to": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
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
  "id": -576460752303421669,
  "jsonrpc": "2.0",
  "method": "channels.update_ack",
  "params": {
    "signed_tx": "tx_+NILAfiEuEAq1UYcwhb9o6nuTfYqsdxgwj+Z1T2J2DPkNkLmJYWdNoyH1pK3OrtLp64fJqlF5L+Z3A5eKtQoiFe8vBn12l0AuEDErQWGGcM4t4Skc+Zz46oZRf9VH65mHF8w7wmvbbF89qIen95GQzcDFBHSGRKdWXQfFlXnFSCKePgEBAn3BeIBuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wagKzEWq60sk7OpKKGJUTAWW/7W34gbmL1yz6HYINdlPOZfWY44"
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421669,
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "state": "tx_+NILAfiEuEAq1UYcwhb9o6nuTfYqsdxgwj+Z1T2J2DPkNkLmJYWdNoyH1pK3OrtLp64fJqlF5L+Z3A5eKtQoiFe8vBn12l0AuEDErQWGGcM4t4Skc+Zz46oZRf9VH65mHF8w7wmvbbF89qIen95GQzcDFBHSGRKdWXQfFlXnFSCKePgEBAn3BeIBuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wagKzEWq60sk7OpKKGJUTAWW/7W34gbmL1yz6HYINdlPOZfWY44"
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "state": "tx_+NILAfiEuEAq1UYcwhb9o6nuTfYqsdxgwj+Z1T2J2DPkNkLmJYWdNoyH1pK3OrtLp64fJqlF5L+Z3A5eKtQoiFe8vBn12l0AuEDErQWGGcM4t4Skc+Zz46oZRf9VH65mHF8w7wmvbbF89qIen95GQzcDFBHSGRKdWXQfFlXnFSCKePgEBAn3BeIBuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wagKzEWq60sk7OpKKGJUTAWW/7W34gbmL1yz6HYINdlPOZfWY44"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421668,
  "jsonrpc": "2.0",
  "method": "channels.get.balances",
  "params": {
    "accounts": [
      "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
      "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv"
    ]
  }
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421668,
  "jsonrpc": "2.0",
  "result": [
    {
      "account": "ak_9UUfv5MBBZRKsS82REfUw4xLxrGVrEtjxuiEHiZDgraJg27Sn",
      "balance": 40000000000000
    },
    {
      "account": "ak_2U5uowyre6aqU1gz3Pkd1VtMkBVc2rquvr3oPWynbPNYozaLhv",
      "balance": 70000000000000
    }
  ],
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421667,
  "jsonrpc": "2.0",
  "method": "channels.get.offchain_state",
  "params": {}
}
```

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421667,
  "jsonrpc": "2.0",
  "result": {
    "calls": "cs_yYICbgGEwz8BwHtqgWY=",
    "half_signed_tx": "",
    "signed_tx": "tx_+NILAfiEuEAq1UYcwhb9o6nuTfYqsdxgwj+Z1T2J2DPkNkLmJYWdNoyH1pK3OrtLp64fJqlF5L+Z3A5eKtQoiFe8vBn12l0AuEDErQWGGcM4t4Skc+Zz46oZRf9VH65mHF8w7wmvbbF89qIen95GQzcDFBHSGRKdWXQfFlXnFSCKePgEBAn3BeIBuEj4RjkCoQae7X7ByVOxh7H//LtykgnRbSIBjNehbjsoGAzUZKRt+wagKzEWq60sk7OpKKGJUTAWW/7W34gbmL1yz6HYINdlPOZfWY44",
    "trees": "ss_+Ks+AIrJggJtAYTDPwHAismCAm4BhMM/AcCKyYICbwGEwz8BwIrJggJwAYTDPwHAismCAnEBhMM/AcC4cPhuggJyAbho+GY/AfhisO9AAaDBMfSSNtypn6R9Lj/XcSWAdA2Pl0Sm+A0njfmJxzQDRovKCgEAhj+qJSJgALDvQAGgEz2ciJGcxrbKc/5lzfvMBttVgar6S5lhtorJSke1o/+LygoBAIYkYTnKgABEv1s8"
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "event": "minimum_depth_achieved",
      "notice": "already_assumed",
      "tx_hash": "th_2ERU4LEe8Bn8x1iuw9vSh7iHys9t8zwt3Nq2oz5GQj9pAu9pur",
      "tx_type": "channel_create_tx"
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "event": "minimum_depth_achieved",
      "notice": "already_assumed",
      "tx_hash": "th_2ERU4LEe8Bn8x1iuw9vSh7iHys9t8zwt3Nq2oz5GQj9pAu9pur",
      "tx_type": "channel_create_tx"
    }
  },
  "version": 1
}
```

#### responder ---> node
```javascript
{
  "id": -576460752303421666,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### initiator <--- node
```javascript
{
  "jsonrpc": "2.0",
  "method": "channels.info",
  "params": {
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### responder <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421666,
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
    "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
    "data": {
      "event": "died"
    }
  },
  "version": 1
}
```

#### initiator ---> node
```javascript
{
  "id": -576460752303421665,
  "jsonrpc": "2.0",
  "method": "channels.system",
  "params": {
    "action": "stop"
  }
}
```

#### responder closes WebSocket connection

#### initiator <--- node
```javascript
{
  "channel_id": "ch_2CzbXD38sjii5eM1nMLtASBvtpKgfUGJSp3MofesFH5DWro8GJ",
  "id": -576460752303421665,
  "jsonrpc": "2.0",
  "result": "ok",
  "version": 1
}
```

#### initiator closes WebSocket connection
